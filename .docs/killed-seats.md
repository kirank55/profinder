# Killed seats (local deny file)

Authoritative for this workspace (`deny_catalog: local_adr_0001`). A restated
candidate that matches a one-line seat here stops: copy the labeling, do not
re-keep as Sparse/`file_on: none`. These are labeling rows, not generation
seeds.

| One-line seat | Disposition | Why |
| --- | --- | --- |
| Tenant-slice cutover orchestrator (row-filter + FK walk + WAL catchup + pool drain as one SaaS) | Occupied bundle · `file_on` pgcopydb / DMS / `pg_easy_replicate` | Keep-gate worked false keep. PG15 `CREATE PUBLICATION ... WHERE` is `exact` for the filter slice. |
| Landlock loopback-only test gate (`hermetic-test` via Landlock v3/v4 IP allowlist) | Occupied · `file_on` landrun or bubblewrap | Landlock net is TCP ports, not IPs. `bwrap --unshare-net` is the loopback-up / no-egress primitive. |
| Kafkatrap: Kafka wire-protocol proxy that injects coordinator frames (`JoinGroup` / `SyncGroup` / `Heartbeat` / `OffsetCommit`) at record offsets in CI | Occupied leftover · `file_on` Kroxylicious Filter API (`shortCircuitResponse` / `JoinGroupRequestFilter`) or kfake `ControlKey` | PR #7/#8. Kroxylicious is `exact` for the proxy slice. Offset-triggered rules are auto-reject 5. Do not re-keep because leftover is "not a lightweight CI daemon." |
| PgLSN Gateway: PgWire session-aware causal consistency gateway (commit LSN capture + replica matrix + managed SaaS) on RDS / Aurora Postgres | Occupied bundle · `file_on` Pgpool-II `disable_load_balance_on_write`, Aurora `apg_write_forward.consistency_mode=SESSION`, or Heimdall R/W-split | PR #7/#8. Conjunction v1. Session stickiness and Aurora `SESSION` already occupy read-your-writes. LSN cookie is auto-reject 5. |
