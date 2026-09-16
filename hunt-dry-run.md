# Hunt dry-run (plan1.md validation item 7)

Date: 2026-09-16. Pipeline: SKILL.md steps 2-9 over 5 raw seats from
references/seat-generation.md. Deny catalog: embedded_baseline (no
docs/adr/0001 in this workspace; vendor deny file present).

Generation used substrate inventory nouns only. No closed-aisle leftovers
(ntfy flags, ngrok companions, "add X to Veln") were used as seeds.

## Raw seats (all have substrate + named process)

S1: eBPF per-binary egress allowlist daemon for bare-metal CI runners.
  substrate: Kernel / eBPF / LSM.
  process_or_protocol: Linux TC egress hook + cgroup/process identity.
  why_not_a_slogan: blocks exfiltration at connect() time per binary
  hash; not an advisory scanner.

S2: AST-collision merge-queue scheduler (order/bundle queued PRs by
  tree-sitter collision graph).
  substrate: CI scheduler / merge queue.
  process_or_protocol: git merge + tree-sitter AST diff.
  why_not_a_slogan: pairwise collision scores change queue order; not
  "AI speeds up CI".

S3: RESP-aware fault-injection proxy for CI (deterministic command
  interleaving + fault schedule for Redis transactions).
  substrate: Wire proxy / protocol gate.
  process_or_protocol: RESP protocol interleaving.
  why_not_a_slogan: parses RESP frames to schedule interleavings; not a
  TCP blackhole.

S4: Fail-closed PATH-shim integrity enforcer (host consults lockfile
  before exec; mismatch fails closed).
  substrate: Host runtime enforcement (PATH, interpreter, package mgr).
  process_or_protocol: execve / PATH lookup.
  why_not_a_slogan: exec refuses on hash mismatch; not a version switcher.

S5: Vanilla-Postgres RLS tenancy-cutover verifier (diff tenant slice
  from row-filtered publication against RLS set; emit cutover plan).
  substrate: Schema / tenancy cutover.
  process_or_protocol: Postgres logical replication + RLS.
  why_not_a_slogan: per-tenant parity check before cutover; not a dashboard.

## Per-seat runs

### S1: deny embedded_baseline pass (no ADR row matches). Steelman ceiling 6.

- Tetragon, https://tetragon.io/docs/getting-started/enforcement/ :
  "In-kernel filtering also enables Tetragon to enforce policy
  restrictions at the kernel level. For example, by issuing a SIGKILL
  to a process when a policy violation is detected, the process will
  not continue to run." seat_match: exact. leftover: per-binary-hash
  allowlist UX on bare-metal runners (Tetragon policies are k8s-scoped).
- Cilium NetworkPolicy: NEED_EVIDENCE (unverified fetch). provisional
  adjacent_pain (cluster L3/L4, not bare-runner binary identity).
- Falco: NEED_EVIDENCE. provisional adjacent_pain (alerting, no enforcement).
- Tracee: NEED_EVIDENCE. provisional adjacent_pain (observability only).
- Inspektor Gadget: NEED_EVIDENCE. provisional adjacent_pain (advisory gadgets).

Scores: problem_density 7, exact_mechanics_density 6 (<= ceiling 6).
Auto-reject 1 fires (Tetragon ships the enforcement headline UX).
Card: as_company Occupied 6, as_oss Occupied 6, as_plugin Occupied 6,
file_on Tetragon tracing-policy feature (per-binary allowlist),
claim_hygiene ok, pitch_rate compose_next.

### S2: deny note -- overlaps SymMerge bundle territory (AST collision +
  interference graph) but seat differs (queue ordering vs merge
  synthesis); proceed, do not copy prior verdict. Steelman ceiling 6.

- Trunk parallel queues,
  https://docs.trunk.io/merge-queue/optimizations/parallel-queues :
  "Using the impacted target information we can instead build three
  dynamically provisioned queues and the predictive testing can yield
  higher throughput." seat_match: exact (interference graph in front of
  a merge queue). leftover: AST-collision scoring vs target globs.
- Mergiraf, https://mergiraf.org/ : "Mergiraf can solve a wide range of
  Git merge conflicts. That is because it is aware of the trees in your
  files!" seat_match: adjacent_pain (merge-time resolution, not queue
  scheduling). leftover: none for this seat.
- Nx affected: NEED_EVIDENCE. provisional adjacent_pain (task graph).
- GitHub merge queue: NEED_EVIDENCE. provisional adjacent_pain (single lane).
- SemaMerge: NEED_EVIDENCE. provisional adjacent_pain (semantic merge tool).

Scores: problem_density 7, exact_mechanics_density 6 (<= ceiling 6).
Leftover is a scoring provider on the incumbent -> FILE_ON pattern.
Card: as_company Occupied 6, as_oss Sparse 3 (bounded scheduler plugin),
as_plugin Sparse 3, file_on Trunk (impacted-targets provider / issue),
claim_hygiene ok, pitch_rate compose_next.

### S3: deny pass. Steelman ceiling 4.

- Toxiproxy, https://github.com/Shopify/toxiproxy/ : "A TCP proxy to
  simulate network and system conditions for chaos and resiliency
  testing." seat_match: adjacent_pain (TCP toxics; no RESP awareness,
  no interleaving schedule). leftover: protocol-aware scheduling.
- Envoy Redis filter: NEED_EVIDENCE (unverified). provisional exact for
  the proxy slice only.
- Twemproxy: NEED_EVIDENCE. provisional adjacent_pain (sharding proxy).
- Chaos Mesh: NEED_EVIDENCE. provisional adjacent_pain (k8s-level chaos).
- Comcast: NEED_EVIDENCE. provisional adjacent_pain (link shaping).

Stop condition hit: 4/5 rows NEED_EVIDENCE -> claim_hygiene unsourced,
no Sparse/Greenfield keep per search-playbook.
Scores: problem_density 5, exact_mechanics_density 2 (<= ceiling 4).
Card: as_company Occupied 5 (held: thin evidence, no keep),
as_oss Sparse 3 (bounded proxy experiment, per calibration discipline),
as_plugin Occupied 5, file_on none, pitch_rate compose_next after
verifying the Envoy slice.

### S4: deny pass, but collapse-mode 3 is directly relevant. Steelman 5.

- mise shims, https://mise.en.dev/dev-tools/shims.html : "You can think
  of shims as symlinks to the mise binary that intercept commands and
  load the appropriate context." seat_match: exact for the shim slice.
  leftover: fail-closed enforcement.
- mise fallback, same page: "it falls back to the first same-named
  executable found elsewhere on PATH rather than erroring."
  seat_match: exact (proves v1 "fails closed" is NOT shipped).
  leftover: the fail-closed option itself.
- mise.lock, https://mise.en.dev/dev-tools/mise-lock.html : "a lockfile
  that pins exact versions and checksums of tools for reproducible
  environments." seat_match: adjacent_pain (pins versions; host does not
  consult it at exec). leftover: host enforcement.
- asdf: NEED_EVIDENCE. provisional adjacent_pain (shims, no lockfile).
- direnv: NEED_EVIDENCE. provisional adjacent_pain (env switching).

Scores: problem_density 6, exact_mechanics_density 5 (<= ceiling 5).
Auto-reject 7 fires (shim the OS never consults; fail-closed needs host
enforcement, which is the missing piece, not a company).
Card: as_company Occupied 6, as_oss Occupied 5, as_plugin Sparse 3,
file_on mise (fail-closed shim-resolution issue), claim_hygiene ok.

### S5: deny pass. Incumbent attempts (Postgres row-filter fetch 429'd;
  all rows NEED_EVIDENCE, quotes not verified -- not counted):

- PG15 row-filtered publication: NEED_EVIDENCE. provisional exact for
  the filtered-replication slice.
- Vitess MoveTables: NEED_EVIDENCE. provisional wrong_substrate.
- Citus isolate_tenant: NEED_EVIDENCE. provisional
  adjacent_pain/wrong_substrate (Citus cluster, not vanilla RDS).
- Ghostferry: NEED_EVIDENCE. provisional wrong_substrate.
- Debezium PG connector: NEED_EVIDENCE. provisional adjacent_pain.

Stop condition hit at 3+ NEED_EVIDENCE rows with zero verified rows.
Per search-playbook the seat cannot be scored -> DROPPED (no card).
Honest reason: undistinguishable from "add a checklist to DMS" until
the PG-native slice is verified. May re-enter as a restated seat after
verification; not a keep.

## Tally

- 5/5 seats have substrate + named process + mechanic sentence.
- 5/5 collected >=5 incumbent attempts (13 NEED_EVIDENCE, 7 verified).
- 4 cards emitted, 1 drop. Of the cards: 3 file_on (S1, S2, S4), 1 held
  no-keep (S3). Zero slogan keeps; every keep-or-hold names stack nouns
  (TC hook, impacted targets, RESP frames, shims, RLS).
- Steelman discipline: no card publishes exact_mechanics_density above
  its pre-search ceiling (S1 6<=6, S2 6<=6, S3 2<=4, S4 5<=5).
- PASS.
