# Architecture Specification: Kafkatrap (Developer Tool)

**Candidate Seat**: Deterministic Kafka wire-protocol proxy for coordinator frame injection (`JoinGroup`, `SyncGroup`, `Heartbeat`, `OffsetCommit`) at deterministic record offsets in CI test suites.

---

## 1. Concrete Problem & Stack Placement

In distributed streaming architectures (Apache Kafka, Redpanda), consumer group rebalances and partition reassignments are the primary source of subtle concurrency bugs, duplicate processing, message loss, and deadlock loops:
- **Eager vs. Cooperative Sticky Rebalances**: When partitions are revoked and reassigned, in-flight message processing must gracefully pause, commit offsets, and flush state stores before joining the group.
- **Flaky CI Testing**: In existing CI pipelines, teams test these paths by either launching raw brokers (via Testcontainers) and relying on arbitrary `Thread.sleep()` intervals, or using blunt network droppers (Toxiproxy) that sever entire TCP connections.
- **The Mechanical Vacuum**: Neither approach can answer the question: *"What happens if a `RebalanceInProgress` error is returned to consumer B exactly after it processes record offset 4287 but before it flushes its local batch?"*

`Kafkatrap` sits directly on the wire between client SDKs and the Kafka broker in local/CI environments, parsing Kafka protocol frames and orchestrating deterministic coordinator fault injection.

---

## 2. Why This is Not a Wrapper or Slogan

1. **Protocol Frame Awareness**: Unlike generic TCP shims (Toxiproxy), `Kafkatrap` decodes Kafka binary protocol request/response headers (API Key, API Version, Correlation ID) and message batches (`RecordBatch`).
2. **Dynamic Advertised Listener Rewriting**: Kafka brokers return `MetadataResponse` containing the broker's advertised listeners. `Kafkatrap` dynamically rewrites these addresses to loopback proxy ports so multi-broker clusters route all client connections through the proxy without manual client configuration.
3. **Deterministic Offset Triggers**: Tests define declarative interception rules over a local REST/gRPC control API:
   ```json
   {
     "trigger": {
       "topic": "orders-v1",
       "partition": 2,
       "offset": 4287,
       "action": "inject_error",
       "error_code": 27, // REBALANCE_IN_PROGRESS
       "delay_ms": 250
     }
   }
   ```
4. **Stateful Group Coordinator Emulation**: `Kafkatrap` can intercept `FindCoordinatorRequest`, elect itself as a virtual coordinator, or intercept `JoinGroup` / `SyncGroup` responses from the real broker to artificially trigger partition rebalancing at deterministic milestones.

---

## 3. Component Architecture

```
+-------------------------------------------------------------+
|                      CI Test Process                        |
|   (JUnit / PyTest / Go Test / Jest / Rust cargo test)        |
+--------------+------------------------------+---------------+
               |                              |
      1. Control Commands            2. Kafka Client SDK
      (Setup Triggers & Probes)      (Bootstrap: localhost:9092)
               |                              |
               v                              v
+-------------------------------------------------------------+
|                     Kafkatrap Proxy                         |
|                                                             |
|  +---------------------+        +------------------------+  |
|  | Local Control API   |        | Wire Protocol Parser   |  |
|  | (HTTP :9090 / gRPC) |        | (Kafka Binary RFC)     |  |
|  +----------+----------+        +-----------+------------+  |
|             |                               |               |
|             v                               v               |
|  +-------------------------------------------------------+  |
|  | Stateful Trigger & Fault Injection Engine             |  |
|  | - Record Offset Tracker (Fetch / Produce inspection)  |  |
|  | - Coordinator State Machine (JoinGroup/SyncGroup/Hb)  |  |
|  | - Frame Injector / Mutator / Delay Pipe               |  |
|  +--------------------------+----------------------------+  |
|                             |                               |
|                             v                               |
|                 +-----------------------+                   |
|                 | Broker Connection     |                   |
|                 | Multiplexer & NAT     |                   |
|                 +-----------+-----------+                   |
+-----------------------------|-------------------------------+
                              |
                     3. Proxied Kafka RPCs
                              |
                              v
             +---------------------------------+
             |   Target Kafka / Redpanda       |
             |   (Testcontainers / Local)      |
             +---------------------------------+
```

---

## 4. v1 as Shipped Deliverable

- **Distribution**: Standalone static binary (`kafkatrap-linux-amd64`, `kafkatrap-darwin-arm64`) compiled in Go or Rust with zero external runtime dependencies (no JVM, no Docker socket required).
- **GitHub Action / CI Step**:
  ```yaml
  - name: Start Kafkatrap
    run: |
      curl -sSL https://get.kafkatrap.dev | sh
      kafkatrap start --upstream 127.0.0.1:9094 --listen 127.0.0.1:9092 &
  ```
- **Client Test SDKs**: Minimal lightweight helper packages for Python, Java, Go, and TypeScript to register offset triggers and assert rebalance completion:
  ```python
  from kafkatrap import Client, ErrorCode

  trap = Client("http://localhost:9090")
  trap.when_offset("orders", partition=0, offset=150).fail_next_heartbeat(ErrorCode.REBALANCE_IN_PROGRESS)
  ```

---

## 5. Failure Modes & Edge Cases Addressed

1. **SASL / SSL Handshake**: `Kafkatrap` acts as a transparent TLS terminator or pass-through for `SaslHandshake` and `SaslAuthenticate` frames, decrypting payload streams if test certificates are supplied.
2. **Compact Batch Decoding**: Modern Kafka clients use `RecordBatch` with snappy/zstd/lz4 compression. `Kafkatrap` performs lazy stream decompression only when offset triggers match the topic-partition being fetched.
3. **Partition Revocation Leaks**: Allows developers to deterministically catch consumers holding in-memory state or database transaction locks when a partition is revoked mid-batch.
