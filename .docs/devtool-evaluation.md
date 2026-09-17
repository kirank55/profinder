# Developer Tool Candidate Evaluation: Hermetic Test & Build Syscall Gate

## 1. Candidate Overview & Stack Placement

*   **Candidate Seat:** Unprivileged Linux host runtime syscall interceptor and loopback-preserving network/filesystem hermeticity gate for arbitrary test runners and build scripts.
*   **Substrate:** Host runtime enforcement (PATH, interpreter, package manager) & Kernel LSM (Landlock + seccomp-bpf).
*   **Immutable Host:** Standard Linux developer workstations and Linux CI runners (e.g., GitHub Actions Ubuntu runner) without root/sudo privileges and without Docker-in-Docker daemon access.
*   **Deliverable (v1 as Shipped):** A standalone single-binary CLI (`hermetic-test <command>`) that wraps arbitrary package manager test commands (`npm test`, `pytest`, `cargo test`, `go test`) in Linux user space, compiling kernel Landlock LSM v3/v4 and seccomp-bpf filters to enforce loopback-only (`127.0.0.1`, `::1`, `AF_UNIX`) network isolation, constrain filesystem writes strictly to workspace roots (`$PWD`, `/tmp`), trap unpinned reads to host secrets (`~/.ssh`, `~/.aws`), and output structured failure diagnostics for undeclared external socket/file dependencies.

---

## 2. Why This Specific Idea Was Chosen

### The Flaky Test & Supply Chain Nightmare
In modern software engineering, automated test suites and build scripts are notorious for non-determinism and security risks:
1.  **Undeclared Network Access (Flaky Tests):** A unit or integration test accidentally makes an external HTTP request to a live staging API, third-party CDN, or remote analytics service instead of using a local mock. When that external service experiences latency or downtime, CI builds fail randomly, eroding developer velocity and trust.
2.  **Environment Pollution & State Leakage:** Tests write temporary files to global host paths or read unpinned configuration files from the developer's home directory (`~/.gitconfig`, `~/.aws/credentials`). The test passes locally on the engineer's laptop but fails in CI.
3.  **Malicious Package Exfiltration:** Modern dependencies (`npm`, `pip`, `crates.io`) execute arbitrary lifecycle scripts during install (`postinstall`, `build.rs`). Compromised packages silently read host credentials and exfiltrate them across the internet during `npm install` or `npm test`.

### The Failure of Existing Solutions
*   **Bazel:** Provides true hermeticity via sandboxing, but requires rewriting an organization's entire codebase and build graph into Starlark, throwing away standard package managers (`npm`, `cargo`, `go`). Over 95% of software teams cannot afford this multi-month migration.
*   **Containers (Docker):** Running test suites inside Docker containers requires a running Docker daemon and root/socket permissions. In CI, Docker-in-Docker is slow, resource-heavy, and complex to cache. Furthermore, containers do not isolate loopback from external egress without complex custom bridge networking and iptables rules.
*   **Linux `unshare -n`:** Dropping network namespaces kills *all* networking, including loopback (`127.0.0.1`), immediately breaking tests that connect to local Redis, PostgreSQL, or mock servers.
*   **Language-Specific Mocking (MSW, Nock):** In-process libraries require developers to manually mock every endpoint. A single missed mock allows silent network calls to escape undetected.

### The Opportunity: Modern Unprivileged Kernel LSM (Landlock)
Starting with Linux Kernel 5.13 (filesystem rules) and 6.7+ (TCP network binding and connection rules), Linux introduced **Landlock**: an unprivileged Linux Security Module (LSM) that allows any standard process to restrict its own access rights and those of all its child processes without root privileges (`CAP_SYS_ADMIN`).

By packaging Landlock v3/v4 and seccomp-bpf into a developer-facing test gate, we unlock **instant, drop-in hermeticity for any existing test runner without configuration rewrites**.

---

## 3. Incumbent Audit & Seat-Matching Matrix

To establish the **exact mechanics density** vs **problem density**, we performed web-verified audits of existing tools:

| Tool | Verified URL | Documentation / README Quote | Seat-Match Label | Mechanical Leftover |
| :--- | :--- | :--- | :---: | :--- |
| **Bazel Sandboxing** | [Bazel Docs](https://bazel.build/docs/sandboxing) | *"Sandboxing is a technique to isolate a running action inside a restricted and temporary execution root, helping to ensure that it doesn't read undeclared inputs or write undeclared outputs..."* | `wrong_substrate` | Requires replacing native package managers and build tools with Bazel/Starlark. Cannot run as an in-place wrapper for existing `npm test` or `cargo test` suites. |
| **nsjail (Google)** | [nsjail GitHub](https://github.com/google/nsjail) | *"A light-weight process isolation tool, making use of Linux namespaces and seccomp-bpf syscall filters (with help of the kafel bpf language)"* | `adjacent_pain` | Designed for untrusted multi-tenant execution/CTFs; requires root or user namespaces, breaks local loopback services unless manually plumbed, and provides zero test-runner diagnostics. |
| **landrun** | [landrun GitHub](https://github.com/zouuup/landrun) | *"It allows users to run any Linux command in a secure, unprivileged sandbox without requiring root privileges, containers, or complex security configurations... enforces fine-grained restrictions on filesystem access and network access"* | `adjacent_pain` | Generic command sandbox; lacks test runner awareness, does not configure loopback network preservation for local test databases, and provides no CI failure reporting for undeclared sockets. |
| **Trunk Flaky Tests** | [Trunk Docs](https://docs.trunk.io/flaky-tests) | *"Flaky tests make developers waste time rerunning tests, digging through logs, and chasing problems that might not exist. Over time, they slow down your CI pipeline and make it harder to release code"* | `adjacent_pain` | Observational post-facto test result analyzer; has no host runtime enforcement to mechanically prevent tests from making undeclared network calls. |
| **Mock Service Worker (MSW)** | [MSW Docs](https://mswjs.io) | *"Mock by intercepting requests on the network level. Seamlessly reuse the same mock definition for testing, development, and debugging."* | `language_scoped` | Scoped to JavaScript/Node.js/browser runtimes; requires in-code mock definitions and cannot enforce OS-level boundaries across native child processes or other languages. |
| **Linux `unshare` (util-linux)** | [unshare Manual](https://man7.org/linux/man-pages/man1/unshare.1.html) | *"unshare - run program with some namespaces unshared from parent... -n, --net: Unshare the network namespace."* | `adjacent_pain` | Completely destroys loopback networking (`127.0.0.1`), causing local test fixtures and database containers to crash. |

### Density Scores
*   **Problem Density:** `7.5 / 10` (Extremely high pain: flaky tests, CI flakiness, credential leak prevention).
*   **Exact Mechanics Density:** `1.0 / 10` (Zero unprivileged tools currently provide loopback-preserving test execution with developer-centric failure diagnostics).
*   **Steelman Ceiling:** `3.0 / 10`.

---

## 4. Proof of Falsification Tests

1.  **Test 1: Vacant Process:**
    *   *Result: PASS.*
    *   No existing tool provides drop-in, unprivileged execution wrapping for standard package managers that permits loopback sockets while blocking and reporting undeclared internet egress.
2.  **Test 2: Not a 50-Line Wrapper:**
    *   *Result: PASS.*
    *   Synthesizing Landlock rulesets across varying Linux kernel ABI versions (ABI v1 to v4), assembling seccomp-bpf filter bytecode for child process tree inheritance (`PR_SET_NO_NEW_PRIVS`), and capturing intercepted socket destination IPs/ports for actionable error messages requires a compiled systems programming binary (Rust/C) interacting directly with Linux kernel syscalls.
3.  **Test 3: Mechanical Gap:**
    *   *Result: PASS.*
    *   The gap vs. Bazel is non-invasive adoption (wrap existing `npm test` in 5 seconds vs. 6-month build migration).
    *   The gap vs. `unshare` is selective loopback preservation (`127.0.0.1` stays alive; external IPs are blocked).
    *   The gap vs. Trunk/DeFlaker is proactive mechanical prevention vs. reactive log tracking.

---

## 5. Defense Against Automatic Rejects

*   **Auto-Reject #1 (Incumbent ships headline UX):** No tool currently markets or ships this drop-in unprivileged test isolation UX.
*   **Auto-Reject #2 (50-line Action/wrapper):** Compiling kernel Landlock and seccomp filters cannot be done in a 50-line shell script.
*   **Auto-Reject #3 (Non-invertible transform):** Syscall filtering either allows an operation or returns `EPERM` with an error report; completely deterministic.
*   **Auto-Reject #4 (Confused deputy / security bypass):** Hardens process security by actively restricting process privileges.
*   **Auto-Reject #5 (Add to incumbent X):** This is not a pull request to `landrun` or `bwrap`; it is a purpose-built developer tool for CI/CD pipelines and local test runners.
*   **Auto-Reject #6 (Silent payload mutation):** Does not mutate payloads; it halts execution on violation and outputs actionable diagnostics.
*   **Auto-Reject #7 (Sidecar without runtime enforcement):** This is native OS kernel-enforced runtime enforcement.

---

## 6. Commercialization & Standalone Company Defense

Why is this a viable developer tooling company?
*   **The "Wedge & Expand" Motion:**
    *   *Open-Source Binary (`hermetic-exec`):* Free CLI distributed via brew/cargo/apt for individual developers to eliminate test flakiness and run tests safely locally.
    *   *Enterprise CI Policy Platform (SaaS):* Cloud dashboard and GitHub App for engineering leadership. Automatically tracks undeclared dependencies across pull requests, audits supply-chain egress calls, enforces workspace boundary policies, and provides CI test speedup metrics by guaranteeing cache safety.
*   **Direct Value Proposition:** Flaky tests cost mid-size engineering organizations hundreds of engineering hours every week. A tool that mechanically guarantees hermeticity without requiring a Bazel migration delivers immediate, measurable ROI.

