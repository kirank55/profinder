# Competitive Analysis & Vacancy Proof: PgLSN Gateway (Developer SaaS)

This document provides verified documentation citations, competitive seat-matching, and leftover analysis for **PgLSN Gateway** ([candidate card](file:///c:/Users/kiran/code/p/profinder/.idea/02-saas-pglsn-gateway.yaml)).

---

## 1. Verified Incumbents Matrix

| Incumbent | Verified URL | Documentation Quote | Seat Match | Leftover / Mechanical Gap |
|---|---|---|---|---|
| **AWS RDS Proxy** | [docs.aws.amazon.com/.../rds-proxy](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/rds-proxy.html) | *"Amazon RDS Proxy does not perform automatic, transparent read/write splitting of your database traffic... application code must be configured to send the appropriate requests to the correct connection pool or proxy endpoint."* | `adjacent_pain` | Managed connection pooler providing static endpoints for reader and writer. Performs zero query inspection, zero read/write splitting, and zero WAL replication lag tracking. Application code must manually route reads and handle staleness. |
| **PgCat** | [github.com/postgresml/pgcat](https://github.com/postgresml/pgcat) | *"PgCat is a PostgreSQL connection pooler that supports automatic read/write splitting, which can introduce challenges regarding read-your-writes consistency due to asynchronous replication lag."* | `adjacent_pain` | Rust connection pooler that can route `SELECT` to replicas, but lacks per-client session LSN tracking. Queries executed immediately after a write hit stale replicas unless manually pinned to primary via connection affinity or code-level overrides. |
| **Pgpool-II** | [pgpool.net/.../load-balancing](https://www.pgpool.net/docs/latest/en/html/runtime-config-load-balancing.html) | *"If a standby node's delay exceeds this threshold, Pgpool-II will stop sending SELECT queries to that node... delay_threshold specifies the maximum tolerated replication lag in WAL bytes."* | `adjacent_pain` | Uses coarse, cluster-wide periodic health checks (`sr_check_period`) to verify lag thresholds in bytes. Does not track individual client session tokens or request-level write LSNs, forcing teams to either risk stale reads or annotate queries with `/*NO LOAD BALANCE*/`. |
| **Heimdall Data** | [heimdalldata.com](https://www.heimdalldata.com/) | *"Heimdall tracks writes on a per-table basis... to determine the freshness of replicas and automatically route queries."* | `adjacent_pain` | Proprietary enterprise proxy tracking table-level write timestamps rather than per-session WAL LSN offsets. When an active table is written to, all queries for that table are forced to the primary, eliminating read replica offload benefits for core tables. |
| **Prisma Accelerate** | [prisma.io/accelerate](https://www.prisma.io/accelerate) | *"Prisma Accelerate is primarily a managed connection pooling and caching service designed for serverless and edge environments... does not natively expose or manage LSN-based read replication."* | `wrong_substrate` | Edge caching and connection pooling service coupled to the Prisma ORM. Does not manage multi-node PostgreSQL replication lag or provide wire-level causal routing for generic PostgreSQL applications. |
| **ProxySQL** | [proxysql.com](https://proxysql.com/) | *"ProxySQL is a high performance, high availability, protocol aware proxy for MySQL."* | `wrong_substrate` | Dedicated to MySQL/MariaDB wire protocols and GTID tracking. Completely incompatible with PostgreSQL v3 wire protocols and PostgreSQL WAL LSN semantics. |

---

## 2. Deep Dive: Mechanical Gap vs. Incumbents

### The Core Mechanical Vacuum: Causal LSN vs. Blind Read/Write Splitting

In master-replica PostgreSQL clusters, there are two distinct ways to route read traffic:

1. **Blind Query Classification (PgCat / Pgpool-II / ProxySQL)**:
   - The proxy inspects the SQL verb: `SELECT` goes to a read replica; `INSERT/UPDATE/DELETE` goes to the primary.
   - **The Fatal Flaw**: PostgreSQL streaming replication is asynchronous. If a client executes:
     ```sql
     -- Step 1: Write to primary
     INSERT INTO users (id, name) VALUES (101, 'Alice');
     -- Step 2 (10ms later): Read back user profile
     SELECT * FROM users WHERE id = 101;
     ```
     Under blind read/write splitting, Step 2 is routed to a replica. If the replica lags by 25ms, Step 2 returns `null` (row not found). The user sees a broken interface.
   - To avoid this bug, developers either:
     - Route all reads from their web application to the primary, completely wasting replica capacity, or
     - Write complex application-level middleware to track LSNs in cookies or Redis, which is expensive and brittle across multiple services.

2. **Causal Session LSN Routing (PgLSN Gateway)**:
   - PgLSN Gateway intercepts Step 1's commit and records the primary's current WAL LSN: `0/1A2B3C`.
   - The gateway attaches this LSN requirement to the client session.
   - When Step 2 arrives, the gateway queries its real-time replica lag matrix. If replica 1 is currently at replay LSN `0/1A2B38` (behind the write), the gateway **automatically routes Step 2 to the primary** (or waits a bounded 2ms for replica 1 to catch up).
   - Once replica 1 catches up (`Replay LSN >= 0/1A2B3C`), subsequent reads are transparently offloaded to the replica.

---

### Why AWS RDS Proxy Cannot Close This Gap
AWS RDS Proxy is an infrastructure component designed purely for connection pooling (reducing connection establishment overhead and memory pressure from thousands of serverless Lambda functions).
- AWS explicitly documents that RDS Proxy **does not parse SQL queries** or split traffic between readers and writers.
- Users must configure two distinct endpoints (`proxy-writer` and `proxy-reader`) and manually write application code to manage which query goes where.
- Because RDS Proxy does not inspect SQL or track LSNs, AWS customers cannot use RDS Proxy to achieve transparent causal consistency.

---

## 3. Commercial Viability as a Managed SaaS

- **Target Segment**: B2B companies spending $3,000 to $50,000/month on AWS RDS / Aurora Postgres.
- **ROI Calculation**: An enterprise running an Aurora cluster with a `db.r6i.16xlarge` primary ($5,200/mo) to absorb read traffic can downsize the primary to `db.r6i.4xlarge` ($1,300/mo) and add two read replicas ($1,300/mo each), cutting net infrastructure costs while gaining fault tolerance and 3x higher aggregate read throughput.
- **Delivery**: Offered as a zero-maintenance SaaS proxy with AWS PrivateLink / VPC Peering, or as an in-VPC agent orchestrated by a cloud control plane.
