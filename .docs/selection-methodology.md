# Selection Methodology & Vacancy Scoring

This document explains the evaluation framework, scoring rules, and rationale that guided the discovery and selection of **Kafkatrap** and **PgLSN Gateway**.

---

## 1. Core Philosophy: Occupancy Over Pain

Most startup ideation frameworks fail because they ask: *"Is this problem painful?"*
In developer tooling and cloud infrastructure, **pain is abundant, but empty seats are not**.

When developers experience pain, incumbents frequently already exist to treat that pain. The remaining gap is usually:
- A missing CLI flag (e.g., `ntfy --wait-cmd`),
- A 50-line CI script or GitHub Action,
- A plugin on an existing platform (e.g., adding an ecosystem to Pixi/OpenTofu/Cursor), or
- An occupied bundle of tools where no single vendor sells all three, but the individual slices are saturated.

Under the [Profinder](file:///c:/Users/kiran/code/p/profinder/SKILL.md) skill, a seat is evaluated on **occupancy density**—specifically, whether an adopted product already occupies the **exact mechanics** of the proposed `v1_as_shipped`.

---

## 2. The Scope Gate: Stack Noun & Immutable Host

Under Profinder rules ([`intake.md`](file:///c:/Users/kiran/code/p/profinder/references/intake.md)), abstract prompts such as *"find me a SaaS idea"* or *"AI developer productivity tool"* fail the scope gate immediately. "SaaS" is a billing model, not a substrate.

Vacancy cannot be calculated in the abstract. It is strictly relative to:
1. **Substrate / Protocol**: The technical wire, RPC, or binary format the product interfaces with (e.g., Kafka wire protocol, PostgreSQL v3 wire protocol).
2. **Immutable Host**: The platform the customer **cannot replace** (e.g., Kafka running in Docker/CI, AWS RDS / Aurora Postgres).

By fixing the substrate and immutable host, we prevent category collapse and avoid hallucinating vacant seats where existing platforms have already absorbed the feature.

---

## 3. Rubric Bands & Split Verdicts

Profinder strictly forbids arbitrary single-number ratings (`/100`). Instead, it mandates **split verdicts** across three distinct packaging shapes:

| Band | Density Score | Interpretation |
|---|---|---|
| **Greenfield** | 0 – 1 | Mechanics are completely new; zero prior art in this exact stack position. |
| **Sparse** | 2 – 4 | Adjacent pieces exist, but **no widely adopted product occupies the proposed seat**. Pitchable as a company. |
| **Occupied** | 5 – 7 | Existing tools already solve this via adjacent mechanisms, plugins, or flags. Do not found a standalone company. |
| **Saturated** | 8 – 10 | Named products *are* this headline UX. Fatal for a startup. |

### Dual Density Scoring
Every candidate is assigned two distinct scores:
- **`problem_density` (0-10)**: Measures how many existing tools attempt to alleviate the user's high-level pain (including `adjacent_pain` and workarounds).
- **`exact_mechanics_density` (0-10)**: Measures only tools that occupy the **exact same stack placement and SKU** as the proposed v1.
- **Steelman Ceiling Rule**: The published `exact_mechanics_density` must never exceed the pre-search `steelman.occupancy_ceiling` unless new named incumbent rows are discovered.

---

## 4. Why These Two Ideas Were Chosen

### Candidate 1: Kafkatrap (Developer Tool)
- **Why it qualified**:
  - `problem_density` is high (**7/10**): Teams struggle constantly with Kafka consumer group rebalances, partition revoking deadlocks, and split-brain consumer logic.
  - `exact_mechanics_density` is low (**2/10**): The only exact wire proxy in the Kafka aisle is Kroxylicious, which is an enterprise production gateway for payload encryption, not a developer-facing CI fault injection tool.
  - Incumbents like Toxiproxy are byte-level droppers (cannot trigger protocol rebalances without closing the socket); Testcontainers is a container lifecycle runner with zero protocol awareness; Filibuster is HTTP/gRPC only; Antithesis is a multi-million-dollar VM hypervisor.
  - **Company Verdict: `Sparse 2.5`** (Pitchable standalone dev tool).

### Candidate 2: PgLSN Gateway (Developer SaaS)
- **Why it qualified**:
  - `problem_density` is high (**8/10**): Every engineering team on AWS RDS / Aurora Postgres suffers from replication lag and stale reads when trying to use cheap Read Replicas, forcing them to over-provision expensive Primary DBs.
  - `exact_mechanics_density` is low (**2/10**): AWS RDS Proxy explicitly refuses to perform query inspection or read/write splitting; Pgpool-II relies on coarse cluster-wide polling; PgCat splits reads to replicas blindly without per-session causal LSN tracking; Heimdall Data uses table-level write timestamps that lockout entire tables.
  - Zero existing SaaS products offer transparent PgWire causal session consistency for AWS RDS/Aurora Postgres.
  - **Company Verdict: `Sparse 2.5`** (Pitchable B2B infra SaaS).
