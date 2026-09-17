# Architecture Specification: PgLSN Gateway (Developer SaaS / B2B Infra)

**Candidate Seat**: PgWire session-aware causal consistency gateway with dynamic WAL LSN replica routing for AWS RDS / Aurora Postgres.

---

## 1. Concrete Problem & Stack Placement

In cloud database operations on AWS RDS and Aurora PostgreSQL:
- **The Replication Lag Dilemma**: Read replicas are cheap and easy to spin up, but PostgreSQL physical streaming replication is asynchronous. Replicas frequently lag behind the primary by 5ms to 500ms (or several seconds during peak write bursts).
- **The Stale Read Bug ("Read-Your-Writes")**: When a user creates a record (e.g., submits an order, updates profile, posts a comment) and is immediately redirected to a view page, their `SELECT` query hits a read replica that has not yet applied the write's Write-Ahead Log (WAL) records. The user sees their data missing or reverted, triggering bug reports and customer panic.
- **The Over-Provisioning Tax**: To avoid stale reads, 80%+ of engineering teams abandon read replicas entirely or restrict them to offline reporting jobs. They route 100% of application traffic to a massive, expensive Primary instance (e.g., `db.r6i.16xlarge` costing $5,000–$15,000/month) simply to ensure read consistency.
- **Incumbent Failure**:
  - AWS RDS Proxy provides connection pooling, but offers **zero query inspection and zero read/write splitting**.
  - Pgpool-II uses coarse cluster-wide byte thresholds that fail to protect individual user sessions.
  - PgCat splits reads to replicas without session LSN awareness, risking stale reads on immediate post-write queries.

`PgLSN Gateway` is a managed data plane and SaaS control plane that sits between application servers and PostgreSQL instances, providing automated, transparent read-your-writes causal consistency.

---

## 2. Why This is Not a Wrapper or Slogan

1. **Wire-Level PostgreSQL Protocol Parsing**: Speaks native PostgreSQL v3 wire protocol (`Frontend/Backend` message format: `Query`, `Parse`, `Bind`, `Execute`, `Sync`, `ReadyForQuery`).
2. **Monotonic LSN Capture**: Upon intercepting a successful transaction commit (`COMMIT` or end of auto-commit `INSERT/UPDATE/DELETE`), the gateway extracts the current primary WAL Log Sequence Number via `pg_current_wal_lsn()` or transaction completion markers.
3. **Causal Session State Management**:
   - **Session Header / Cookie Injection**: For HTTP microservices, the gateway provides a small sidecar/header convention (`X-Pg-Session-LSN: 0/1A2B3C`).
   - **Connection Affinity State**: For stateful client pools (Node.js `pg`, Python `asyncpg`, Go `pgx`), the proxy remembers the connection's last write LSN.
4. **Sub-Millisecond Replica Replay Tracking**: Continuously monitors each read replica's `pg_last_wal_replay_lsn()` over a dedicated high-frequency telemetry channel.
5. **Dynamic Causal Routing**:
   - When a `SELECT` arrives:
     - If `Replica.ReplayLSN >= Session.RequiredLSN`: Route to read replica (safe, zero stale read risk).
     - If `Replica.ReplayLSN < Session.RequiredLSN`: Route to primary (fallback ensuring 100% causal consistency).

---

## 3. Data Plane & Control Plane Architecture

```
+-------------------------------------------------------------------------+
|                         Application Tier                                |
|           (Next.js / Rails / Django / Spring / FastAPI)                 |
+------------------------------------+------------------------------------+
                                     |
                         PostgreSQL v3 Connection
                         (Standard connection string)
                                     |
                                     v
+-------------------------------------------------------------------------+
|                  PgLSN Gateway Data Plane (VPC / Cloud)                 |
|                                                                         |
|  +-------------------------------------------------------------------+  |
|  | PgWire Protocol Parser & SQL Classifier                           |  |
|  | - Classifies Read-Only vs. Mutation vs. Explicit Transaction      |  |
|  +-----------------------------------+-------------------------------+  |
|                                      |                                  |
|  +-----------------------------------v-------------------------------+  |
|  | Session Consistency & LSN Arbiter                                 |  |
|  | - Tracks Connection/Token Monotonic Commit LSN                     |  |
|  | - Compares against Live Replica Lag Matrix                        |  |
|  +-----------------+---------------------------------+---------------+  |
|                    |                                 |                  |
|          Safe to Offload?                 Must Read From Primary?       |
|          (Replay LSN >= Session LSN)      (Replay LSN < Session LSN)    |
|                    |                                 |                  |
|                    v                                 v                  |
|  +---------------------------------+  +-------------------------------+ |
|  | Connection Pool (Read Replicas) |  | Connection Pool (Primary)     | |
|  +-----------------+---------------+  +---------------+---------------+ |
+--------------------|----------------------------------|-----------------+
                     |                                  |
            Read Traffic Offload (80%)         Mutations & Critical Reads
                     |                                  |
                     v                                  v
+-----------------------------+        +----------------------------------+
|   AWS RDS / Aurora Read     | <..... |      AWS RDS / Aurora Primary    |
|   Replicas (1..N instances) |   WAL  |      Writer Instance             |
+-----------------------------+        +----------------------------------+
```

---

## 4. v1 as Shipped Deliverable

1. **Data Plane Deployment Options**:
   - **SaaS Managed Endpoint**: Hosted multi-tenant proxy in AWS (us-east-1, us-west-2, eu-west-1) with VPC peering / AWS PrivateLink.
   - **Bring-Your-Own-Cloud (BYOC) Kubernetes DaemonSet**: Lightweight Rust proxy binary deployed into customer's EKS cluster with managed cloud control plane.
2. **Configuration Surface**:
   ```yaml
   upstream:
     primary: "postgres-primary.c123.rds.amazonaws.com:5432"
     replicas:
       - "postgres-reader-01.c123.rds.amazonaws.com:5432"
       - "postgres-reader-02.c123.rds.amazonaws.com:5432"
   consistency:
     mode: "causal_session"     # causal_session | strict_serializable | bounded_staleness
     max_replica_staleness_ms: 250
     fallback_target: "primary"
   ```
3. **Control Plane Dashboard (SaaS)**:
   - Real-time visualization of queries routed to primary vs. replicas.
   - Exact dollar savings calculated from offloaded primary CPU capacity.
   - P95/P99 replication lag metrics and session LSN catchup latency distributions.

---

## 5. Enterprise Commercial Viability

- **Target Customer**: Mid-market and enterprise SaaS companies spending $3,000–$50,000/month on AWS RDS/Aurora Postgres.
- **Value Proposition**: "Cut your AWS RDS compute bill in half while increasing query throughput 3x without changing a single line of SQL or application code."
- **Pricing**: Consumption-based tiered pricing on proxied query volume + managed node hours (e.g. $199/mo base up to $2,499/mo enterprise).
