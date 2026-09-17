# Pitchable Developer Tools & Infrastructure SaaS Ideas

Curated product seats discovered and verified using the **Profinder** skill methodology.

Each candidate has passed the scope gate against an immutable host, undergone incumbent web extraction (minimum 5 verified URL/quote citations), survived auto-rejects and falsification tests, and achieved a **Sparse** occupancy density score (`as_company: Sparse 2.0-4.0` / `exact_mechanics_density <= steelman ceiling`).

---

## Index of Pitchable Candidates

### 1. [01-online-shadow-partitioner.md](file:///c:/Users/kiran/code/p/profinder/.idea/01-online-shadow-partitioner.md)
- **Candidate Seat**: Online shadow-table partitioning and zero-downtime table restructuring daemon for AWS RDS Postgres
- **Substrate**: Schema / tenancy cutover
- **Host**: AWS RDS PostgreSQL / Aurora PostgreSQL
- **The Gap**: No shipping tool in PostgreSQL uses native logical replication (`pgoutput`) to migrate monolithic 500GB+ tables into partitioned tables without `ACCESS EXCLUSIVE` table locks. Trigger-based tools (`pg-osc`) do not support partitioned tables and introduce write amplification; `pg_partman` only maintains existing partitions; `gh-ost` is MySQL-only.
- **Verdict**: `as_company: Sparse 3.5` | `as_oss: Greenfield 1.0` | `exact_mechanics_density: 0.0`

### 2. [02-lsn-causal-replica-proxy.md](file:///c:/Users/kiran/code/p/profinder/.idea/02-lsn-causal-replica-proxy.md)
- **Candidate Seat**: Transparent LSN-tracking causal consistency read-replica wire proxy for AWS RDS / Aurora Postgres
- **Substrate**: Wire proxy / protocol gate
- **Host**: AWS RDS PostgreSQL / Aurora Read Replicas
- **The Gap**: Scaling read traffic to RDS read replicas introduces the fundamental "read-after-write" race condition (stale reads). AWS RDS Proxy explicitly refuses to inspect queries or route based on replication lag, requiring split endpoints. Open-source poolers (`pgcat`, `PgBouncer`) lack LSN tracking and rely on dumb round-robin routing.
- **Verdict**: `as_company: Sparse 3.0` | `as_oss: Greenfield 1.5` | `exact_mechanics_density: 0.0`

---

## Scoring Rubric Summary

- **Occupancy Density vs Pain**: Ideas are evaluated on existing-solution density, not user pain. Pain is ubiquitous; empty seats are rare.
- **Dual Scoring**:
  - `problem_density`: Measures how many existing tools (including `adjacent_pain`) treat the problem.
  - `exact_mechanics_density`: Measures how many shipping products already *are* this exact SKU (must be `Sparse` / `Greenfield` for a keep).
- **Falsification Gate**:
  1. A named process or protocol sits where no incumbent occupies.
  2. Runtime enforcement cannot be reduced to a 50-line Action, hook, or curl script.
  3. Minimum 3 incumbents verified with direct quotes demonstrating a mechanical gap rather than a missing checkbox.
