# Candidate 01: Online Shadow-Table Partitioning Daemon

## Candidate Card

```yaml
candidate_seat: Online shadow-table partitioning and zero-downtime table restructuring daemon for AWS RDS Postgres
v1_as_shipped: Out-of-process daemon connecting to AWS RDS Postgres via pgoutput logical replication slot, streaming live CDC DML to a partitioned shadow table, executing chunked historical backfills without table-level write locks, and coordinating an atomic table-swap transaction with sequence synchronization under a sub-second lock_timeout.
entry: generated

niche:
  substrate_or_stack: PostgreSQL (WAL / logical replication)
  immutable_host: AWS RDS PostgreSQL / Aurora PostgreSQL
  ship_form: company
  unique_data_or_distribution: unset
  hard_nos: []
  source: agent_opt_out

verdicts:
  as_company: Sparse 3.5
  as_oss:     Greenfield 1.0
  as_plugin:  Occupied 6.0

density_scores:
  problem_density: 6.5          # counts adjacent_pain (pg-osc, pg_partman, pgroll, manual runbooks)
  exact_mechanics_density: 0.0  # exact only; <= steelman.occupancy_ceiling

incumbents:
  - name: pg-osc (shayonj/pg-osc)
    url: https://github.com/shayonj/pg-osc
    quote: "pg-online-schema-change (pg-osc) is a tool for making schema changes (any ALTER statements) in Postgres tables with minimal locks, thus helping achieve zero downtime schema changes against production workloads. pg-osc uses the concept of shadow table to perform schema changes."
    seat_match: adjacent_pain
    leftover: Uses table triggers with synchronous write amplification; explicitly does not support native partitioned table hierarchies.

  - name: pg_partman (pgpartman/pg_partman)
    url: https://github.com/pgpartman/pg_partman
    quote: "pg_partman is an extension to create and manage both time-based and number-based table partition sets... One key way that pg_partman extends partitioning in Postgres is by providing a means to automate the child table maintenance over time (Ex. adding new children, dropping old ones based on a retention policy)."
    seat_match: adjacent_pain
    leftover: Automates maintenance of existing partition sets; does not perform online data migration or cutover for unpartitioned active production tables.

  - name: pgroll (xataio/pgroll)
    url: https://github.com/xataio/pgroll
    quote: "pgroll is an open source command-line tool that offers safe and reversible schema migrations for PostgreSQL by serving multiple schema versions simultaneously. It takes care of the complex migration operations to ensure that client applications continue working while the database schema is being updated."
    seat_match: adjacent_pain
    leftover: Relies on view-wrapping expand/contract workflows; does not automate converting monolithic tables to native partitioned tables without manual trigger hooks.

  - name: gh-ost (github/gh-ost)
    url: https://github.com/github/gh-ost
    quote: "GitHub's online schema migration for MySQL... gh-ost is a triggerless online schema migration solution for MySQL... Instead, gh-ost uses the binary log stream to capture table changes, and asynchronously applies them onto the ghost table."
    seat_match: wrong_substrate
    leftover: Coupled to MySQL binlog wire format; cannot run against PostgreSQL or AWS RDS Postgres logical decoding.

  - name: pg_repack (reorg/pg_repack)
    url: https://github.com/reorg/pg_repack
    quote: "pg_repack is a PostgreSQL extension which lets you remove bloat from tables and indexes, and optionally restore the physical order of clustered indexes. Unlike CLUSTER and VACUUM FULL it works online, without holding an exclusive lock on the processed tables during processing."
    seat_match: adjacent_pain
    leftover: In-place physical tuple compaction only; cannot convert table storage layouts or alter schemas into partitioned hierarchies.

auto_rejects_fired: []
falsification:
  1_vacant_process: pass   # No shipping tool occupies the WAL-streamed shadow-partitioning seat on Postgres.
  2_not_a_wrapper: pass    # Requires replication state machine, chunked transactional backfiller, and lock-timeout recovery coordinator.
  3_mechanical_gap: pass   # Mechanical gap between trigger-based write amplification (pg-osc) and asynchronous logical WAL replay (gh-ost pattern).

steelman:
  occupancy_ceiling: 3.5
  why_build: "Teams running 500GB+ tables on managed RDS hit a wall when table size degrades index performance: native Postgres offers no online in-place partition conversion without fatal ACCESS EXCLUSIVE locks, trigger-based tools (pg-osc) cause write contention and cannot handle partition hierarchies, and MySQL's proven triggerless replication-stream migration architecture (gh-ost) has never been built as a dedicated engine for PostgreSQL's pgoutput protocol."

claim_hygiene: ok
file_on: none
deny_catalog: embedded_baseline
rate_next: not_run
```

---

## Technical Architecture & Mechanics

```
┌────────────────────────────────────────────────────────┐
│               AWS RDS PostgreSQL Cluster               │
│                                                        │
│   ┌─────────────────────┐    ┌─────────────────────┐   │
│   │ Monolithic Table    │    │ Partitioned Shadow  │   │
│   │ (500GB+ Active DML) │    │ Parent Table        │   │
│   └──────────┬──────────┘    └──────────▲──────────┘   │
│              │                          │              │
│       WAL Stream (pgoutput)             │              │
│       (No Triggers Added)               │              │
└──────────────┼──────────────────────────┼──────────────┘
               │                          │
               ▼                          │
 ┌────────────────────────────────────────┴─────────────┐
 │       Online Shadow Partitioning Daemon (Host)       │
 │                                                      │
 │  1. Creates Publication on Target Table              │
 │  2. Provisions Partitioned Shadow Table Scheme       │
 │  3. Starts Logical Replication Slot (pgoutput)       │
 │  4. Runs Concurrent Chunked Historical Backfill      │
 │  5. Drains & Replays CDC Delta Queue                 │
 │  6. Coordinates Bounded Lock-Timeout Table Swap:     │
 │     BEGIN;                                           │
 │       SET LOCAL lock_timeout = '500ms';              │
 │       ALTER TABLE users RENAME TO users_old;         │
 │       ALTER TABLE users_shadow RENAME TO users;      │
 │       SELECT setval('users_id_seq', ...);            │
 │     COMMIT;                                          │
 └──────────────────────────────────────────────────────┘
```

### The Wedge (Why It Wins)
1. **Triggerless Safety**: MySQL solved this in 2016 with `gh-ost`. In PostgreSQL, teams are still forced to either endure high-risk trigger cascades (`pg-osc`), pay for proprietary platform migrations, or perform manual multi-week engineering runbooks with custom scripts.
2. **Zero Table-Level Locks**: The daemon uses standard unprivileged replication credentials (`rds_replication`) and PostgreSQL native logical decoding, eliminating `ACCESS EXCLUSIVE` table locks during historical backfills.
3. **Managed SaaS Motion**:
   - **OSS Core**: Free CLI tool (`pg-ghost-partitioner`) for single-table local/staging dry-runs.
   - **Commercial SaaS**: Managed orchestration control plane connecting to cloud VPCs, automated health/lag telemetry, automatic rollback on latency regression, and enterprise audit logging for compliance.
