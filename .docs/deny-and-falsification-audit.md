# Deny Pattern & Falsification Audit

This document details the rigorous compliance check of **Kafkatrap** and **PgLSN Gateway** against the collapse modes in [`deny-patterns.md`](file:///c:/Users/kiran/code/p/profinder/references/deny-patterns.md) and the gate conditions in [`rubric.md`](file:///c:/Users/kiran/code/p/profinder/references/rubric.md).

---

## 1. Audit Against Deny Patterns (`deny-patterns.md`)

### Collapse Mode 1: "File it on the incumbent"
- *Anti-pattern*: The proposed UX already exists in an incumbent and the pitch is just an extra flag or minor extension (e.g. `ntfy --wait-cmd` for local background jobs, or loopback isolation for worktrees in `silo`).
- **Kafkatrap Audit**: **PASS**. Kroxylicious is an enterprise production proxy built on the Netty JVM stack for data encryption. It is not an ephemeral test runner daemon. Testcontainers is an orchestration container tool, not a protocol injector. Neither vendor considers deterministic offset-level coordinator simulation part of their core roadmap.
- **PgLSN Gateway Audit**: **PASS**. AWS RDS Proxy exists to solve connection pooling for serverless architectures (Lambda), explicitly declining to parse SQL statements or perform query splitting. PgCat is an open-source connection pooler where per-session LSN tracking across arbitrary stateful connections requires a distributed state coordination plane that exceeds the scope of a single local pooler process.

---

### Collapse Mode 2: "Add the missing ecosystem to Veln"
- *Anti-pattern*: Cross-ecosystem porting (e.g. "it's X, but for Elixir/Zig") is an open-source library contribution, not a company.
- **Kafkatrap Audit**: **PASS**. Kafkatrap is wire-protocol agnostic to the client's programming language. Because it operates on the wire at `localhost:9092`, it works identically for Python, Java, Go, Rust, and Node.js Kafka clients without language-specific shims.
- **PgLSN Gateway Audit**: **PASS**. Operates at the PostgreSQL v3 wire protocol level (`Frontend/Backend` protocol messages), working across any ORM (Prisma, SQLAlchemy, ActiveRecord, Hibernate) and any driver (`pgx`, `asyncpg`, `node-postgres`, `psycopg2`).

---

### Collapse Mode 3: "Sidecar without host runtime enforcement"
- *Anti-pattern*: Creating an advisory lockfile, policy file, or wrapper that the underlying platform or database engine can bypass or ignore (`tofulock`, advisory prompt cache inspectors).
- **Kafkatrap Audit**: **PASS**. Kafkatrap sits as the **bootstrap broker** and rewrites `MetadataResponse` advertised listeners. Client SDKs cannot talk to the Kafka broker without traversing Kafkatrap's wire filter.
- **PgLSN Gateway Audit**: **PASS**. The database connection string directs client traffic through the gateway socket. Queries are actively parsed and routed; the gateway controls backend connection pooling to the primary and replicas, ensuring strict physical enforcement.

---

### Collapse Mode 4: Prohibited Fuller Aisles
Neither candidate sits in any of the closed aisles listed in `deny-patterns.md`:
- Not a phone notifier for local/CI tasks
- Not a localhost tunnel / OAuth companion
- Not an advisory prompt-cache inspector
- Not a vendor API contract drift seat
- Not a universal offline SQL mutation upcast (non-invertible)
- Not a PTY secret reverse-map (confused deputy)
- Not an agent sandbox / FS / secrets wrapper already shipped by hosts
- Not a package-manager-shaped lock/integrity seat

---

## 2. Rubric Automatic Reject Audit (`rubric.md`)

Each candidate was tested against the seven fatal automatic rejects:

| Auto-Reject Criterion | Kafkatrap (Dev Tool) | PgLSN Gateway (SaaS) | Status |
|---|---|---|---|
| **1. Incumbent already ships headline UX** | None; Toxiproxy is frame-blind, Kroxylicious is an encryption gateway. | None; RDS Proxy and PgCat do not provide causal LSN replica routing. | **CLEAR** |
| **2. Product is a 50-line Action/curl wrap** | Requires full binary Kafka protocol parser and stateful coordinator simulator. | Requires PostgreSQL v3 protocol parser, transaction state machine, and connection pooler. | **CLEAR** |
| **3. Core transform is mathematically non-invertible** | Operates on standard reversible Kafka RPC frames. | Operates on standard ACID WAL LSN ordering. | **CLEAR** |
| **4. Wedge is reverse-mapping security control** | No secret reverse-mapping or confused deputy involved. | No secret reverse-mapping involved; standard DB auth passthrough. | **CLEAR** |
| **5. Wedge is "add this to incumbent X"** | Standalone CI runner tool; not an upstream PR to Toxiproxy or Kafka. | Standalone data plane; not a patch on RDS Proxy. | **CLEAR** |
| **6. Silent mutation of user payloads** | Does not alter message payloads; injects protocol-level coordinator control frames. | Does not mutate SQL queries; only routes transactions based on LSN metadata. | **CLEAR** |
| **7. Sidecar without host runtime enforcement** | Full wire-level proxy enforcement via bootstrap advertised listener NAT. | Full wire-level TCP connection and transaction enforcement. | **CLEAR** |

---

## 3. Falsification Verification

Under `references/rubric.md`, a catalog of objections is refuted because all three conditions hold for both candidates:

1. **Vacant Process**:
   - *Kafkatrap*: Deterministic consumer group coordinator state injection on precise record offset boundaries has zero shipping implementations.
   - *PgLSN Gateway*: Transparent PgWire causal session consistency via WAL LSN tracking has zero shipping managed SaaS implementations for AWS RDS.
2. **Not a Wrapper**:
   - Neither tool can be implemented as a simple hook, GitHub Action, or curl wrapper. Both require custom binary protocol parsing and connection state machines.
3. **Mechanical Gap**:
   - At least 5 incumbents were named with live documentation quotes and URLs for each candidate. The competitive gap is mechanical (frame awareness, session LSN tracking) rather than a superficial missing feature.

---

## 4. Claim Hygiene Review

- **Kafkatrap**: Avoids implausible combinatorial claims. It does not promise full $O(N!)$ model-checking across multi-broker Raft quorums in $<5$ seconds; it provides targeted deterministic trigger points for specific consumer group transitions.
- **PgLSN Gateway**: Avoids implausible latency bounds. It does not claim sub-microsecond global replication across multi-region clusters; it measures real asynchronous replication lag in standard PostgreSQL streaming replication and routes dynamically to primary if replicas lag beyond safety windows.
- Both candidates receive: `claim_hygiene: ok`.
