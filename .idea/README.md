# Profinder Vetted Ideas: Executive Summary

This directory contains two candidate cards identified and vetted using the **Profinder** protocol. 

Unlike traditional "idea generation" that relies on customer pain interviews, TAM estimates, and marketing slogans, Profinder scores **occupancy density** on concrete infrastructure and development substrates.

---

## The Two Pitchable Candidates

| Metric | Candidate 1: Infrastructure SaaS | Candidate 2: Developer Tool |
| :--- | :--- | :--- |
| **Seat Name** | [Tenant-Slice Cutover Engine](file:///C:/Users/kiran/.gemini/antigravity/worktrees/profinder/profinder_pitchable_saas_ideas/.idea/saas-candidate.md) | [Hermetic Test Syscall Gate](file:///C:/Users/kiran/.gemini/antigravity/worktrees/profinder/profinder_pitchable_saas_ideas/.idea/devtool-candidate.md) |
| **Substrate** | Schema / tenancy cutover & logical replication | Host runtime enforcement (PATH/interpreter) & Kernel LSM |
| **Immutable Host** | AWS RDS / Aurora PostgreSQL | Standard Linux CI Runner & Developer Workstation |
| **Ship Form** | Managed Company / SaaS Control Plane | Company / Developer Tool CLI + Enterprise Policy Console |
| **`as_company` Verdict** | **Sparse (3.0)** | **Sparse (2.5)** |
| **`as_oss` Verdict** | Sparse (3.5) | Sparse (2.0) |
| **`as_plugin` Verdict** | Greenfield (1.0) | Greenfield (1.0) |
| **Problem Density** | 7.0 (high ad-hoc pain, scripts, heavy alternatives) | 7.5 (high flaky test & supply chain pain) |
| **Exact Mechanics Density**| 1.5 (only native `CREATE PUBLICATION ... WHERE` slice) | 1.0 (no unprivileged drop-in loopback-preserving test gate) |
| **Steelman Ceiling** | 3.5 | 3.0 |
| **Key Incumbents** | Vitess, Citus, AWS DMS, pgroll, pgcopydb, Nile | Bazel, nsjail, Landrun, Trunk Flaky Tests, MSW, unshare |
| **Why Pitchable** | Fills the mechanical gap between shared multi-tenant RDS and dedicated single-tenant RDS without replacing the DB engine. | Fills the mechanical gap between heavy Bazel migration and advisory-only test flakiness dashboards without root privileges. |

---

## Documentation Links

Comprehensive selection rationales, incumbent competitive matrices, falsification proofs, and killed candidate audits are available in the `.docs/` directory:

1. [Profinder Methodology & Scoring Guide](file:///C:/Users/kiran/.gemini/antigravity/worktrees/profinder/profinder_pitchable_saas_ideas/.docs/methodology.md)
2. [SaaS Candidate Deep-Dive Evaluation](file:///C:/Users/kiran/.gemini/antigravity/worktrees/profinder/profinder_pitchable_saas_ideas/.docs/saas-evaluation.md)
3. [Developer Tool Deep-Dive Evaluation](file:///C:/Users/kiran/.gemini/antigravity/worktrees/profinder/profinder_pitchable_saas_ideas/.docs/devtool-evaluation.md)
4. [Killed Candidate Audit & Negative Proofs](file:///C:/Users/kiran/.gemini/antigravity/worktrees/profinder/profinder_pitchable_saas_ideas/.docs/killed-candidates.md)

