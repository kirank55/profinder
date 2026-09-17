# Candidate Card: Hermetic Test & Build Syscall Gate (Dev Tool)

```yaml
candidate_seat: Unprivileged Linux host runtime syscall interceptor and loopback-preserving network/filesystem hermeticity gate for arbitrary test runners and build scripts
v1_as_shipped: Standalone single-binary CLI (hermetic-test <command>) that wraps arbitrary package manager test commands (npm test, pytest, cargo test, go test) in Linux user space, compiling kernel Landlock LSM v3/v4 and seccomp-bpf filters to enforce loopback-only (127.0.0.1, ::1, AF_UNIX) network isolation, constrain filesystem writes strictly to workspace roots ($PWD, /tmp), trap unpinned reads to host secrets (~/.ssh, ~/.aws), and output structured failure diagnostics for undeclared external socket/file dependencies.
entry: generated

niche:
  substrate_or_stack: Host runtime enforcement (PATH, interpreter, package manager) & Kernel LSM (Landlock + seccomp-bpf)
  immutable_host: Standard Linux developer workstation and standard Linux CI runner (e.g. GitHub Actions Ubuntu runner) without root/sudo privileges and without Docker-in-Docker daemon access
  ship_form: company
  unique_data_or_distribution: unset
  hard_nos: []
  source: agent_opt_out

verdicts:
  as_company: Sparse 2.5
  as_oss:     Sparse 2.0
  as_plugin:  Greenfield 1.0

density_scores:
  problem_density: 7.5          # High pain: flaky tests due to unmocked external APIs, CI outages, credential exfiltration via malicious postinstall scripts
  exact_mechanics_density: 1.0  # Zero unprivileged drop-in CLI tools provide loopback-preserving test isolation with CI diagnostics; <= steelman.occupancy_ceiling

incumbents:
  - name: Bazel Sandboxing
    url: https://bazel.build/docs/sandboxing
    quote: "Sandboxing is a technique to isolate a running action inside a restricted and temporary execution root, helping to ensure that it doesn't read undeclared inputs or write undeclared outputs. Sandboxing greatly improves hermeticity..."
    seat_match: wrong_substrate
    leftover: Requires a massive, multi-month migration to rewrite all build files into Starlark and abandon native package managers (npm, cargo, pip, go build). Cannot wrap existing test runners in-place.

  - name: nsjail
    url: https://github.com/google/nsjail
    quote: "A light-weight process isolation tool, making use of Linux namespaces and seccomp-bpf syscall filters (with help of the kafel bpf language)"
    seat_match: adjacent_pain
    leftover: Designed as a security sandbox for untrusted multi-tenant code execution / CTFs; does not provide developer-facing test runner diagnostics, fails to differentiate loopback test fixtures from external egress cleanly without root networking setup, and requires root/CAP_SYS_ADMIN for namespace management.

  - name: landrun
    url: https://github.com/zouuup/landrun
    quote: "It allows users to run any Linux command in a secure, unprivileged sandbox without requiring root privileges, containers, or complex security configurations like SELinux or AppArmor... enforces fine-grained restrictions on filesystem access and network access"
    seat_match: adjacent_pain
    leftover: A general-purpose Landlock CLI runner; lacks test runner context, does not configure loopback network preservation for local test databases (Postgres, Redis), and provides no CI failure reporting for undeclared external network socket addresses.

  - name: Trunk Flaky Tests
    url: https://docs.trunk.io/flaky-tests
    quote: "Flaky tests make developers waste time rerunning tests, digging through logs, and chasing problems that might not exist. Over time, they slow down your CI pipeline and make it harder to release code"
    seat_match: adjacent_pain
    leftover: Post-facto CI log analysis and test quarantining; purely advisory and observational, with zero host runtime syscall enforcement to mechanically prevent tests from reaching external networks or reading host files.

  - name: Mock Service Worker (MSW)
    url: https://mswjs.io
    quote: "Mock by intercepting requests on the network level. Seamlessly reuse the same mock definition for testing, development, and debugging."
    seat_match: language_scoped
    leftover: Userland Node.js and browser HTTP monkey-patching library; language-scoped to JavaScript/TypeScript, requires manual mock definitions inside application code, and cannot enforce OS-level syscall boundaries across native binaries, child processes, or other languages (Go, Rust, Python).

  - name: Linux unshare (util-linux)
    url: https://man7.org/linux/man-pages/man1/unshare.1.html
    quote: "unshare - run program with some namespaces unshared from parent... -n, --net: Unshare the network namespace."
    seat_match: adjacent_pain
    leftover: Primitive OS command that completely destroys loopback networking (127.0.0.1) when isolating network namespaces, breaking all local test servers, Postgres, and Redis containers unless complex root-level veth bridges are created.

auto_rejects_fired: []
falsification:
  1_vacant_process: pass
  2_not_a_wrapper: pass
  3_mechanical_gap: pass

steelman:
  occupancy_ceiling: 3.0
  why_build: "Developers constantly battle flaky integration test suites and supply-chain threats where third-party packages make undeclared network calls (hitting production/staging APIs or exfiltrating credentials) or mutate state outside the project directory. The only existing solutions are heavyweight build-system rewrites (Bazel), root-privileged container configurations that break loopback connections, or language-specific mocking libraries that developers routinely forget to configure. Modern Linux kernels (5.13+ for filesystem, 6.7+ for TCP port restriction) provide unprivileged Landlock LSM and seccomp-bpf. An unprivileged CLI that instantly drops into GitHub Actions and developer workstations to guarantee hermetic test execution with zero config rewrite and clear diagnostic error stacks fills a massive, defensible product gap."

claim_hygiene: ok
file_on: none
deny_catalog: embedded_baseline
rate_next: compose_next
```

