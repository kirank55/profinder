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
| merge_group redundant-job cancel daemon on github.com merge queue runners | Occupied · `file_on` Actions concurrency `cancel-in-progress` | Hunt 1. `cancel-in-progress: true` is `exact` for the cancel slice. Auto-reject 1. |
| systemd slice resource guard for merge_queue jobs (CPUQuota + MemoryMax per job scope) | Occupied · `file_on` systemd.resource-control | Hunt 1. CPUQuota/MemoryMax primitives `exact`. Annotation leftover is auto-reject 5. |
| lockfile-to-image drift gate as merge_group required check | Occupied · `file_on` npm-ci | Hunt 1. npm-ci lock mismatch error is `exact` for drift slice. Auto-rejects 2+5. |
| merge-queue impacted-target parallel-lane scheduler for github.com merge queue | Occupied · `file_on` Trunk merge parallel queues | Hunt 1. Trunk impacted-target lanes `exact`. Auto-reject 1. |
| runner egress allowlist ledger joining job ID to destination per merge_group | Occupied · `file_on` harden-runner | Hunt 1. Step-job mapping + domain allowlist `exact`. Auto-rejects 1+5. |
| merge_group flaky-test quarantine gate from historical flake rate | Occupied · `file_on` Trunk flaky-tests | Hunt 1. Trunk quarantine + in-queue anti-flake `exact`. Auto-rejects 1+5. |
| Unprivileged per-package npm lifecycle-script network sandbox (preinstall/install/postinstall under bwrap --unshare-net + write allowlist) | Occupied bundle · `file_on` @lavamoat/allow-scripts / bwrap | Hunt 2. npm `ignore-scripts`, lavamoat allowlist, bwrap `--unshare-net` each `exact` a slice. Per-package wiring is auto-reject 5. |
| Node engines exec interlock refusing the wrong interpreter (engines + volta pin PATH shim) | Occupied · `file_on` Volta / fnm | Hunt 2. Volta pin + shims and fnm `engines.node` support `exact`. Auto-rejects 1+5. |
| Lockfile-pinned node_modules/.bin PATH gate blocking binary shadowing (bin entry + integrity hash) | Occupied · `file_on` lavamoat experimental-bins | Hunt 2. npm bin linking + npx inference + lavamoat bins flag `exact`. Auto-rejects 1+5. |
| npm global prefix redirector isolating npm i -g into per-project stores | Occupied · `file_on` npm prefix config | Hunt 2. npm `prefix` defaults `exact`. Per-project rewrite is a dotfile wrapper. Auto-rejects 2+5. |
| NODE_OPTIONS flag allowlist wrapper stripping inspect/require smuggling | Occupied · `file_on` Node CLI docs / systemd Environment | Hunt 2. `NODE_OPTIONS` precedence + `Environment=` `exact`. Allowlist is wrapper UX. Auto-rejects 2+5. |
