# Candidate Card: PostgreSQL Tenant-Slice Cutover Engine (SaaS)

```yaml
candidate_seat: PostgreSQL row-filtered tenant slice extractor and online zero-downtime cutover orchestrator for AWS RDS / Aurora
v1_as_shipped: Managed control plane and worker agent that inspects relational foreign-key graphs, provisions row-filtered logical replication slots (pgoutput), catches up CDC replication lag, and orchestrates a sub-second connection-pool write drain cutover to isolate whale tenants from shared RDS databases to dedicated single-tenant instances.
entry: generated

niche:
  substrate_or_stack: Schema / tenancy cutover & logical streaming replication
  immutable_host: AWS RDS PostgreSQL / Aurora PostgreSQL (unmodified vanilla engine, cannot install custom C extensions or swap database engines)
  ship_form: company
  unique_data_or_distribution: unset
  hard_nos: []
  source: agent_opt_out

verdicts:
  as_company: Sparse 3.0
  as_oss:     Sparse 3.5
  as_plugin:  Greenfield 1.0

density_scores:
  problem_density: 7.0          # High adjacent pain: teams build ad-hoc Python scripts, suffer downtime, or attempt complex ETL setups
  exact_mechanics_density: 1.5  # Only native CREATE PUBLICATION ... WHERE occupies the replication filter slice; <= steelman.occupancy_ceiling

incumbents:
  - name: PostgreSQL Native Row Filtered Publication (PostgreSQL 15+)
    url: https://www.postgresql.org/docs/current/sql-createpublication.html
    quote: "The WHERE clause only allows simple expressions... A row filter expression allows rows to be replicated conditionally based on the result of the expression."
    seat_match: exact
    leftover: Provides only the kernel-level replication filtering slice; lacks relational foreign-key dependency ordering, sequence resynchronization, schema DDL pre-sync, backpressure guardrails, and connection-pool cutover coordination.

  - name: Vitess MoveTables
    url: https://vitess.io/docs/user-guides/migration/movetables/
    quote: "MoveTables is a VReplication-based workflow that handles the entire migration lifecycle: copying initial data, streaming ongoing changes, and switching traffic"
    seat_match: wrong_substrate
    leftover: Built exclusively for MySQL/Vitess keyspaces and requires adopting the Vitess VTGate/VTTablet distributed clustering layer; cannot operate against vanilla RDS PostgreSQL.

  - name: Citus (isolate_tenant_to_new_shard)
    url: https://docs.citusdata.com/en/stable/develop/api_udf.html
    quote: "It creates a new shard that holds only rows for a specific tenant_id (the value of the distribution column) and splits the original shard to remove those rows, effectively isolating the tenant"
    seat_match: wrong_substrate
    leftover: Requires running the proprietary Citus distributed extension and distributed colocated tables, which is incompatible with standard vanilla RDS/Aurora PostgreSQL instances.

  - name: AWS Database Migration Service (AWS DMS)
    url: https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Tasks.CDC.html
    quote: "When creating a task, you can select 'Replicate ongoing changes' (CDC-only) or 'Migrate existing data and replicate ongoing changes' (Full load + CDC)..."
    seat_match: adjacent_pain
    leftover: General-purpose physical/logical database migration tool; does not replicate secondary indexes, foreign keys, or sequences, and has no native concept of multi-table tenant slicing or atomic connection pool cutover.

  - name: pgroll (Xata)
    url: https://github.com/xataio/pgroll
    quote: "pgroll is an open-source command-line tool that offers zero-downtime, reversible schema migrations for PostgreSQL by using an expand-contract pattern"
    seat_match: adjacent_pain
    leftover: Solves table schema evolutionary migration via views and triggers; does not extract, isolate, or migrate individual tenant data partitions to dedicated instances.

  - name: pgcopydb
    url: https://github.com/dimitri/pgcopydb
    quote: "pgcopydb is an open-source tool designed to copy a PostgreSQL database to a target PostgreSQL server as quickly as possible... By using logical replication slots and logical decoding (defaulting to the pgoutput plugin), pgcopydb can capture and replay ongoing changes while an initial data copy is in progress"
    seat_match: adjacent_pain
    leftover: Migrates entire databases at the instance level; cannot selectively partition or slice rows across multi-table foreign-key hierarchies by tenant ID.

  - name: Nile
    url: https://www.thenile.dev/docs
    quote: "Nile is a serverless PostgreSQL platform specifically re-engineered for multi-tenant SaaS applications... Nile modifies Postgres to store each tenant's data in separate, tenant-dedicated pages. This allows for granular control, such as moving specific tenants between compute instances or regions without affecting others"
    seat_match: wrong_substrate
    leftover: Requires abandoning existing AWS RDS / Aurora infrastructure and adopting Nile's custom serverless cloud database engine.

auto_rejects_fired: []
falsification:
  1_vacant_process: pass
  2_not_a_wrapper: pass
  3_mechanical_gap: pass

steelman:
  occupancy_ceiling: 3.5
  why_build: "B2B SaaS applications universally begin on shared multi-tenant PostgreSQL (RDS/Aurora) using a tenant_id column. When enterprise clients sign six-figure contracts demanding dedicated single-tenant infrastructure or regional data sovereignty, engineering teams face a multi-month, high-risk crisis. No off-the-shelf product orchestrates the end-to-end extraction: calculating foreign-key dependency orders, setting up row-filtered logical replication slots, catching up WAL lag safely without exhausting disk, syncing sequences, and coordinating sub-second connection pool write pauses. Teams are forced to either rewrite on Vitess/Citus or build brittle one-off Python migration scripts that cause prolonged customer downtime."

claim_hygiene: ok
file_on: none
deny_catalog: embedded_baseline
rate_next: compose_next
```

