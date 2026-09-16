# Calibration

Read this before the first 0–10 score in a session. Each case is: claim → correct labels → decision → mistake to avoid.

Do not copy these verdicts onto a new idea. Copy the **labeling discipline**.

## Gold KILL

### SymMerge (ADR 0002)

**Claim:** Sparse 3.0. AST collision graph + TIA + agent conflict synthesizer as one SKU. Falsifies ADR 0001.

**Correct:** Occupied ~6.5 as a **bundle of exact occupied slices**. SemaMerge / Mergiraf (syntax-aware merge), Trunk parallel queues (interference graph in front of a merge queue), Datadog/Nx/Launchable TIA, Copilot/CodeRabbit/GitButler conflict bots. v1 languages (TS/Python) are where `merge` + `tsc`/`pyright` already catch semantic breaks.

**Decision:** `FILE_ON_X` / `KILL` as a company. Do not supersede ADR 0001.

**Mistake to avoid:** Scoring the *bundle* Sparse because no single logo sells all three. Straw-man table (Git line merge, desktop diff GUI) while omitting the products that *are* the UX.

### ntfy `--wait-cmd` / silo / add Mix to Veln

**Claim:** Phone notifier for silent local builds; worktree loopback isolation; build-hook jail for Mix/Zig/Conan.

**Correct:** Saturated/Occupied exact SKUs (ntfy, silo, Veln wrap). Leftover is add-ecosystem or a gist.

**Decision:** `FILE_ON_X`.

**Mistake to avoid:** Combination novelty (daemon + phone + wait) as a new category.

## Gold CLAIM-kill, seat not auto-Occupied

### TenantScale `sub-10ms` checksum

**Claim:** PgWire proxy + tenant-filtered CDC + atomic cutover, including a sub-10ms cryptographic checksum of a whale tenant. Sparse 2.2.

**Correct:** Kill the **number**. Checksumming the tenant you isolated *because it is huge* does not fit in 10ms; Vitess treats VDiff as async. That is claim hygiene.

PG15 `CREATE PUBLICATION … WHERE (tenant_id = …)` is `exact` for the **filtered-replication slice**. Vitess/Ghostferry are `wrong_substrate` for vanilla RDS Postgres. Citus isolate is not “extract tenant out of vanilla RDS.”

**Decision:** Do not use the checksum fail as proof the whole cutover **seat** is Occupied. Re-score slices. Likely `FILE_ON_X` on native logical replication / DMS for the CDC slice; company verdict follows remaining exact rows, not the physics tell.

**Mistake to avoid:** “Implausible latency ⇒ Occupied 7.0.”

### SagaGuard `<60s` DPOR vs O(N!)

**Claim:** Kafka/Redis wire-protocol proxy, DPOR in CI under 60s, SQL invariants, delta-debug replay. Sparse 2.8.

**Correct:** Kill the **physics** if the ADR also claims O(N!) interleavings *and* sub-minute full exploration of real Kafka + real DBs. Kroxylicious is `exact` for a Kafka proxy slice. Coyote/Shuttle/Loom are `language_scoped`. Temporal is `adjacent_pain`. Antithesis is `price_packaging`.

**Decision:** `as_company` likely Occupied or `FILE_ON_X` if leftover is a Kroxylicious filter plus SQL assertions. `as_oss` may still be a bounded experiment. Do not publish Occupied 8–9 after a steelman of 5–6.

**Mistake to avoid:** Architecture alternatives filling the exact-mechanics column; discarding a steelman.

## Gold false `exact`

These labels were wrong in the PR #7 rating run. Do not repeat them.

| Cited | Proposed seat | Wrong | Right |
|-------|---------------|-------|-------|
| Coyote, Filibuster, Shuttle/Loom | Kafka wire DPOR in CI | `exact` | `language_scoped` or `adjacent_pain` |
| Temporal / Restate / DBOS | CI interleaving tester for existing brokers | `exact` | `adjacent_pain` |
| Vitess / Ghostferry | Vanilla Postgres tenant extract | `exact` | `wrong_substrate` |
| Azure Split-Merge | Live 2026 cutover product | `exact` | `obsolete` |

## Gold wrong-object

**User:** “rate the PR in a table out of 100.” **Follow-up:** “i mean rate the ideas.”

**Correct:** Second pass `object_under_review: idea`. Drop PR title, commit bundling, overwritten pitch memo, and writing quality. Those are `pr_process`.

**Mistake to avoid:** A 41/100 that is mostly hygiene and fidelity-to-previous-rating, then keeping density as a hidden overall after the user corrects the object.

## Steelman discipline

If thinking says occupancy is 5–6 and OSS is plausible, the published exact-mechanics score may not jump to 8–9 with the same evidence. Publish the steelman. If you discard it, say which **new named row** changed the ceiling.
