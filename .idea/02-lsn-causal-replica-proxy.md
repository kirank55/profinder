# Candidate 02: Transparent LSN-Tracking Causal Consistency Replica Proxy

## Candidate Card

```yaml
candidate_seat: Transparent LSN-tracking causal consistency read-replica wire proxy for AWS RDS / Aurora Postgres
v1_as_shipped: L7 pgproto3 wire proxy sitting in front of AWS RDS / Aurora clusters that captures primary commit LSNs (pg_current_wal_lsn), embeds session causal tokens, and transparently routes read queries to read replicas only when pg_last_wal_replay_lsn >= session_lsn, eliminating application-level read-after-write stale read bugs with zero ORM code changes.
entry: generated

niche:
  substrate_or_stack: PostgreSQL (v3 wire protocol / WAL LSN tracking)
  immutable_host: AWS RDS PostgreSQL / Aurora Read Replicas
  ship_form: company
  unique_data_or_distribution: unset
  hard_nos: []
  source: agent_opt_out

verdicts:
  as_company: Sparse 3.0
  as_oss:     Greenfield 1.5
  as_plugin:  Occupied 6.5

density_scores:
  problem_density: 7.0          # counts adjacent_pain (RDS Proxy, pgcat, dual-ORM client routing)
  exact_mechanics_density: 0.0  # exact only; <= steelman.occupancy_ceiling

incumbents:
  - name: AWS RDS Proxy
    url: https://aws.amazon.com/rds/proxy/
    quote: "RDS Proxy is not a transparent load balancer that automatically inspects your SQL queries to route SELECT statements to replicas and INSERT/UPDATE statements to the primary. You must configure your application or database driver to route traffic appropriately."
    seat_match: adjacent_pain
    leftover: Requires separate read/write endpoints; forces application code to manage replication lag; does not enforce causal consistency.

  - name: pgcat (postgresml/pgcat)
    url: https://github.com/postgresml/pgcat
    quote: "PostgreSQL pooler, proxy, and load balancer... supports sharding, read/write splitting, and failover."
    seat_match: adjacent_pain
    leftover: Performs naive round-robin read/write splitting; lacks WAL LSN tracking and exposes applications to read-after-write stale data anomalies.

  - name: PgBouncer
    url: https://www.pgbouncer.org/
    quote: "Lightweight connection pooler for PostgreSQL."
    seat_match: adjacent_pain
    leftover: Pure connection multiplexer; no multi-node replica awareness, no query routing, no LSN tracking.

  - name: Readyset (readysettech/readyset)
    url: https://github.com/readysettech/readyset
    quote: "Readyset is an SQL caching engine that sits between your application and database to cache query results."
    seat_match: price_packaging
    leftover: Heavyweight in-memory materialized view cache; does not solve read replica routing across native Postgres storage nodes.

  - name: Vitess (vitessio/vitess)
    url: https://github.com/vitessio/vitess
    quote: "Database clustering system for horizontal scaling of MySQL."
    seat_match: wrong_substrate
    leftover: MySQL-only distributed coordinator; cannot proxy vanilla AWS RDS or Aurora PostgreSQL protocols.

auto_rejects_fired: []
falsification:
  1_vacant_process: pass   # No shipping wire proxy provides automatic LSN causal token tracking for Postgres read replicas.
  2_not_a_wrapper: pass    # Requires stateful wire protocol parser (extended query format), replica LSN polling ring buffer, and connection muxing.
  3_mechanical_gap: pass   # Mechanical gap between naive dumb read splitting (pgcat) and causal consistency token enforcement.

steelman:
  occupancy_ceiling: 3.0
  why_build: "Nearly all growing web applications add read replicas to RDS to offload read traffic from the primary, but immediately encounter the read-after-write race condition: a user updates their profile or creates an order, immediately gets redirected to view it, and receives a 404 or stale state because the replica is 20ms behind. AWS explicitly refuses to solve this in RDS Proxy, and existing poolers like PgBouncer and pgcat leave application developers to write brittle dual-client connection logic in their ORMs."

claim_hygiene: ok
file_on: none
deny_catalog: embedded_baseline
rate_next: not_run
```

---

## Technical Architecture & Mechanics

```
┌────────────────────────────────────────────────────────┐
│               Client Web App / API Pods                │
│             (Single Postgres Connection URL)           │
└───────────────────────────┬────────────────────────────┘
                            │
               Postgres v3 Wire Protocol
                            │
                            ▼
 ┌───────────────────────────────────────────────────────┐
 │          Transparent Causal Replica Proxy             │
 │                                                       │
 │  1. Intercepts Write Transaction (INSERT/UPDATE):     │
 │     - Relays to RDS Primary                           │
 │     - Captures Commit LSN from pg_current_wal_lsn()   │
 │     - Tags Session with: target_lsn = 0/16B2D40       │
 │                                                       │
 │  2. Intercepts Read Query (SELECT):                   │
 │     - Checks Replica LSN Polling Ring Buffer:         │
 │         Replica 1 (Replay LSN: 0/16B2D00) -> Lagged   │
 │         Replica 2 (Replay LSN: 0/16B2E10) -> CAUGHT UP│
 │     - Routes SELECT to Replica 2                      │
 │     - If all replicas lagged, falls back to Primary   │
 │       or pauses with bounded microsecond wait         │
 └──────────────┬────────────────────────┬───────────────┘
                │                        │
       Write Traffic /           Read Queries
       Immediate Fallback        (Guaranteed Consistent)
                │                        │
                ▼                        ▼
     ┌─────────────────────┐  ┌─────────────────────┐
     │  RDS Writer Primary │  │  RDS Read Replica   │
     └─────────────────────┘  └─────────────────────┘
```

### The Wedge (Why It Wins)
1. **Drop-in Database URL**: Replaces RDS connection string with proxy endpoint. Zero changes to Django, Rails, Prisma, Drizzle, or Hibernate codebase.
2. **Instant Hardware Cost Reduction**: Unlocks 70-80% offloading of read traffic from the expensive primary writer instance to cheaper read replicas without engineering teams fearing stale read bugs.
3. **Commercial SaaS / Managed Plane**:
   - **Control Plane**: Self-hosted or managed proxy cluster deployed inside customer AWS VPC.
   - **Observability Dashboard**: Real-time replication lag distributions, LSN latency histograms, and query routing heatmaps.
