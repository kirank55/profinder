# SaaS Candidate Evaluation: PostgreSQL Tenant-Slice Cutover Engine

## 1. Candidate Overview & Stack Placement

*   **Candidate Seat:** PostgreSQL row-filtered tenant slice extractor and online zero-downtime cutover orchestrator for AWS RDS / Aurora.
*   **Substrate:** Schema / tenancy cutover & logical streaming replication.
*   **Immutable Host:** AWS RDS PostgreSQL / Aurora PostgreSQL (unmodified vanilla engine; cannot install custom C extensions or swap database engines).
*   **Deliverable (v1 as Shipped):** A managed control plane and worker daemon that introspects relational foreign-key graphs, provisions row-filtered logical replication slots (`pgoutput`), continuously drains WAL replication lag, and orchestrates a sub-second connection-pool write drain cutover to isolate whale tenants from shared RDS databases to dedicated single-tenant instances.

---

## 2. Why This Specific Idea Was Chosen

### The Architectural Dilemma in Multi-Tenant SaaS
Over 90% of B2B SaaS companies start on a multi-tenant relational database (PostgreSQL on AWS RDS or Aurora) using a shared-schema model with a `tenant_id` column on all application tables.

As the company scales and lands six-figure enterprise accounts ("whale tenants"), two hard enterprise requirements emerge:
1.  **Data Sovereignty & Compliance:** The enterprise customer requires their data to live in a dedicated, isolated database instance or specific geographical AWS region (e.g., EU-only, HIPAA, FedRAMP).
2.  **Noisy Neighbor & Blast Radius Isolation:** The whale tenant consumes 40% of the shared database's CPU, buffer pool, and IOPS, degrading performance for all other customers.

### The Missing Off-the-Shelf Mechanical Solution
When engineering teams attempt to "slice out" a whale tenant and move them to a dedicated database instance, they hit an operational wall:
*   **Full database dump/restore (`pg_dump`)** copies the entire database, requiring massive downtime and scrubbing of all other tenants' rows.
*   **Ad-hoc SQL scripts (`INSERT INTO ... SELECT WHERE tenant_id = X`)** fail to handle active writes, lock tables, break foreign-key topologies, and result in hours of maintenance windows.
*   **Replacing the database engine** with Vitess, Citus, or CockroachDB requires months of code rewrites, breaking ORM abstractions and losing native RDS compatibility.

This reveals a high-leverage vacant seat: **An automated engine that operates on vanilla RDS/Aurora, extracts a single tenant across complex foreign-key graphs, replicates ongoing changes in real time, and executes an atomic sub-second cutover.**

---

## 3. Incumbent Audit & Seat-Matching Matrix

To establish the **exact mechanics density** vs **problem density**, we performed web-verified audits of existing tools:

| Tool | Verified URL | Documentation / README Quote | Seat-Match Label | Mechanical Leftover |
| :--- | :--- | :--- | :---: | :--- |
| **PostgreSQL 15+ Native Row Filtering** | [PostgreSQL Docs](https://www.postgresql.org/docs/current/sql-createpublication.html) | *"The WHERE clause only allows simple expressions... A row filter expression allows rows to be replicated conditionally based on the result of the expression."* | `exact` | Only provides the underlying raw replication primitive; lacks foreign-key dependency traversal, sequence resync, DDL pre-flight sync, and cutover connection-pool coordination. |
| **Vitess MoveTables** | [Vitess Docs](https://vitess.io/docs/user-guides/migration/movetables/) | *"MoveTables is a VReplication-based workflow that handles the entire migration lifecycle: copying initial data, streaming ongoing changes, and switching traffic"* | `wrong_substrate` | Architected exclusively for MySQL and Vitess keyspace sharding; incompatible with vanilla PostgreSQL RDS/Aurora. |
| **Citus (`isolate_tenant_to_new_shard`)** | [Citus Docs](https://docs.citusdata.com/en/stable/develop/api_udf.html) | *"It creates a new shard that holds only rows for a specific tenant_id (the value of the distribution column) and splits the original shard to remove those rows..."* | `wrong_substrate` | Requires adopting the Citus distributed extension and colocated distributed tables; cannot run on standard vanilla RDS/Aurora. |
| **AWS Database Migration Service (DMS)** | [AWS DMS Docs](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Tasks.CDC.html) | *"When creating a task, you can select 'Replicate ongoing changes' (CDC-only) or 'Migrate existing data and replicate ongoing changes'..."* | `adjacent_pain` | Designed for full-instance migrations; does not replicate secondary indexes, foreign keys, or sequences, and cannot orchestrate multi-table relational tenant slicing. |
| **pgroll (Xata)** | [pgroll GitHub](https://github.com/xataio/pgroll) | *"pgroll is an open-source command-line tool that offers zero-downtime, reversible schema migrations for PostgreSQL by using an expand-contract pattern"* | `adjacent_pain` | Solves database schema migrations via views and triggers; does not isolate, filter, or re-home tenant data partitions. |
| **pgcopydb** | [pgcopydb GitHub](https://github.com/dimitri/pgcopydb) | *"pgcopydb is an open-source tool designed to copy a PostgreSQL database to a target PostgreSQL server as quickly as possible... By using logical replication slots..."* | `adjacent_pain` | Migrates entire databases at the instance level; lacks row-level relational tenant filtering and live application routing coordination. |
| **Nile** | [Nile Docs](https://www.thenile.dev/docs) | *"Nile is a serverless PostgreSQL platform specifically re-engineered for multi-tenant SaaS applications... Nile modifies Postgres to store each tenant's data in separate, tenant-dedicated pages."* | `wrong_substrate` | Requires replacing the customer's AWS RDS/Aurora database with Nile's proprietary serverless cloud database engine. |

### Density Scores
*   **Problem Density:** `7.0 / 10` (Many adjacent approaches: manual scripts, Citus, Vitess, full-database CDC).
*   **Exact Mechanics Density:** `1.5 / 10` (Only the raw PostgreSQL 15+ `CREATE PUBLICATION ... WHERE` primitive sits in this mechanical slice).
*   **Steelman Ceiling:** `3.5 / 10`.

---

## 4. Proof of Falsification Tests

1.  **Test 1: Vacant Process:**
    *   *Result: PASS.*
    *   No incumbent tool automates the multi-table relational foreign-key traversal, row-filtered WAL publication creation, sequence alignment, and connection-pool cutover for vanilla RDS PostgreSQL.
2.  **Test 2: Not a 50-Line Wrapper:**
    *   *Result: PASS.*
    *   Orchestrating tenant cutover requires:
        *   Building an acyclic dependency graph of 50+ relational tables with foreign keys.
        *   Managing WAL retention and replication slot lag to prevent RDS disk exhaustion.
        *   Synchronizing sequence values (`setval`) without race conditions.
        *   Draining connection poolers (e.g., PgBouncer or AWS RDS Proxy) to achieve a <1s atomic cutover window.
        *   This cannot be accomplished with a simple bash script, curl wrapper, or GitHub Action.
3.  **Test 3: Mechanical Gap:**
    *   *Result: PASS.*
    *   The gap vs. Vitess/Citus is substrate portability (vanilla RDS vs. specialized cluster forks).
    *   The gap vs. AWS DMS/pgcopydb is relational tenant slicing vs. instance-level replication.
    *   The gap vs. pgroll is tenant data re-homing vs. schema evolution.

---

## 5. Defense Against Automatic Rejects

*   **Auto-Reject #1 (Incumbent ships headline UX):** None do. Teams universally build bespoke scripts.
*   **Auto-Reject #2 (50-line Action/wrapper):** Building replication slots and dependency-ordered cutovers is a complex distributed systems challenge.
*   **Auto-Reject #3 (Non-invertible transform):** Relational extraction and WAL replay are mathematically deterministic and invertible.
*   **Auto-Reject #4 (Confused deputy / security bypass):** Uses standard Postgres logical replication authentication and native ACLs.
*   **Auto-Reject #5 (Add to incumbent X):** This is not a pull request to pgroll or DMS; it is a dedicated tenant orchestration control plane.
*   **Auto-Reject #6 (Silent payload mutation):** Data is replicated verbatim via Postgres logical decoding (`pgoutput`).
*   **Auto-Reject #7 (Sidecar without runtime enforcement):** Connects directly to the PostgreSQL logical replication engine and application connection poolers.

---

## 6. Commercialization & Standalone Company Defense

Why is this a venture-scale SaaS company rather than just an open-source tool?
*   **High Enterprise Willingness to Pay:** Unblocking a $250k/year enterprise deal that requires dedicated tenancy justifies a $20k–$50k/year infrastructure software license.
*   **Risk Profile:** Database migrations carry existential risk of data corruption or write loss. Engineering executives buy enterprise-grade software with automated pre-flight checks, rollback guarantees, and 24/7 SLA over homegrown scripts.
*   **Expansion Motion:** Starting as a "tenant extraction tool" naturally expands into **Dynamic Multi-Tenant Fleet Orchestration** (managing 100+ dedicated tenant databases, canary migrations, cross-region tenant replication, and unified observability across vanilla RDS instances).

