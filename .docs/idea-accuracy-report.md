# Independent Rating and Accuracy Audit

Date: 2026-09-17
Object: the two “pitchable” candidates in `.idea/` plus the supporting write-ups in `.docs/`
Method: rater pass against `references/rubric.md` and `references/seat-match.md`, plus live URL and kernel/Postgres checks. This is not a second finder hunt.

## Bottom line

The **process is real**. Occupancy-first scoring, split verdicts, killed-seat tables, and “no overall /100” are the right frame for these substrates.

The **keeps are not**. Both candidates were marked Sparse company-keeps. Independently they are **Occupied leftovers**: a Postgres logical-replication cutover bundle, and a Landlock/bwrap sandbox with a test-runner UX coat. The docs overstate vacancy, under-search incumbents, and treat paraphrased marketing language as verified quotes.

| Artifact | Accuracy of facts | Accuracy of occupancy verdict | Independent rater verdict |
| --- | ---: | ---: | --- |
| `.docs/methodology.md` | 7 / 10 | n/a (process doc) | Faithful to the skill, with inverted falsification wording and drifted score bands |
| SaaS: tenant-slice cutover | 5 / 10 | 4 / 10 | **Occupied 6.0 as_company** · Sparse 3.5 as_oss · `file_on` pgcopydb / `pg_easy_replicate` |
| Dev tool: hermetic syscall gate | 3.5 / 10 | 3 / 10 | **Occupied 7.0 as_company** · Occupied 6.0 as_oss · `file_on` landrun / bubblewrap |
| `.docs/killed-candidates.md` | 8 / 10 | 8.5 / 10 | All five kills stand. One dead GitHub URL |
| `.idea/README.md` | 4 / 10 | 3 / 10 | Executive table repeats the Sparse keeps and uses broken `file://` Windows paths |

**Do not found either company on this evidence.** The honest leftovers are plugins, flags, or bounded OSS experiments on named hosts.

---

## Independent ratings

No overall /100. Bands from `references/rubric.md`.

### 1. PostgreSQL tenant-slice cutover (SaaS)

| Field | Original | Independent |
| --- | --- | --- |
| `as_company` | Sparse 3.0 | **Occupied 6.0** |
| `as_oss` | Sparse 3.5 | **Sparse 3.5** (unchanged leftover) |
| `as_plugin` | Greenfield 1.0 | **Occupied 5.5** · `file_on` |
| `problem_density` | 7.0 | **8.0** |
| `exact_mechanics_density` | 1.5 | **3.5** |
| Steelman ceiling | 3.5 | **5.5** (raised by named rows the hunt missed) |
| `claim_hygiene` | ok | **unsourced + implausible** |
| `file_on` | none | [pgcopydb#161](https://github.com/dimitri/pgcopydb/issues/161), [pg_easy_replicate](https://github.com/shayonj/pg_easy_replicate), AWS DMS source filters |
| Auto-rejects | none | **#5** (add row-filtered switchover to an existing orchestrator). **#1** if the headline UX is “logical-replication cutover,” which already ships |
| Disposition | keep | **`file_on` / `drop` as a company** |

**What is still real.** Shared-schema SaaS on vanilla RDS/Aurora does hit a nasty operation: extract one whale tenant across a foreign-key graph, catch up CDC, cut over routing, then optionally delete the tenant from the shared instance. Native `CREATE PUBLICATION ... WHERE` does not walk that graph, sync sequences, or drain a pooler. Tables that lack `tenant_id` and are only reachable through parent keys are the honest hard leftover.

**Why it is not a company.** The v1 is a **bundle of occupied slices**:

1. Row-filtered logical replication — PostgreSQL 15+ `CREATE PUBLICATION ... WHERE`. The hunt correctly labeled this `exact` for that slice, then ignored the calibration note that the CDC slice is `file_on` native replication / DMS.
2. Row-filtered CDC with table mappings — **AWS DMS source filters** already do `eq` on a column such as `tenant_id`. The write-up called DMS a full-instance migrator. That is false.
3. Online copy + lag watch + read-only cutover + sequence refresh — **`pg_easy_replicate` switchover** and **sbshift** (`preflight / replicate / watch / reconcile / cutover`) already orchestrate that lifecycle on vanilla Postgres.

The remaining gap is “infer the tenant closure and emit the WHERE clauses.” That is a feature request. pgcopydb already has it on the record: issue 161 is literally “extract the customer’s data from a multi-tenant database.” Auto-reject #5 fires.

`as_plugin: Greenfield 1.0` is the worst score in the card. The leftover belongs on pgcopydb, `pg_easy_replicate`, or DMS, not in empty plugin space.

### 2. Hermetic test / build syscall gate (dev tool)

| Field | Original | Independent |
| --- | --- | --- |
| `as_company` | Sparse 2.5 | **Occupied 7.0** |
| `as_oss` | Sparse 2.0 | **Occupied 6.0** |
| `as_plugin` | Greenfield 1.0 | **Occupied 6.5** · `file_on` |
| `problem_density` | 7.5 | **8.5** |
| `exact_mechanics_density` | 1.0 | **6.0** |
| Steelman ceiling | 3.0 | **6.5** (discarded: new named rows, plus a physics fail) |
| `claim_hygiene` | ok | **implausible** |
| `file_on` | none | [landrun](https://github.com/Zouuup/landrun), [bubblewrap](https://github.com/containers/bubblewrap) |
| Auto-rejects | none | **#1** (headline UX already ships) and **#5** (add test diagnostics to landrun / wrap `bwrap`) |
| Disposition | keep | **`file_on` / `drop` as a company** |

**Physics fail, same class as the calibration checksum kill.** The v1 claims Landlock LSM v3/v4 plus seccomp-bpf will “enforce loopback-only (`127.0.0.1`, `::1`, `AF_UNIX`)” while still reaching local Redis/Postgres.

Landlock network rules (ABI v4, kernel 6.7+) match **TCP port numbers, not IP addresses**. Allowing `CONNECT_TCP` on 5432 allows any IPv4/IPv6 host on 5432. Denying all TCP connect also kills localhost TCP. Classic seccomp-bpf cannot dereference `sockaddr` to inspect the IP. The proposed mechanism cannot implement the proposed property.

The mechanism that *does* give “loopback up, no egress” is a **new network namespace with `lo` brought up**. That SKU already ships:

- `bwrap --unshare-net` (loopback is configured automatically)
- `firejail --net=none`
- `systemd-run -p PrivateNetwork=yes`

Those sandboxes have their **own** `127.0.0.1`. Host Postgres/Redis on the host loopback is not reachable. The evaluation treats “local test databases work” and “unshare destroys loopback” as if they were the same fact. They are not. `unshare -n` leaves `lo` down; `unshare --user --net` plus bringing `lo` up, or bubblewrap, restores in-namespace loopback and still cannot see the host’s loopback.

**landrun is the Landlock CLI wrapper.** Filesystem jail, TCP bind/connect ports, unprivileged, drop-in `landrun <command>`. The hunt labeled it `adjacent_pain` because it lacks test-runner diagnostics. Under seat-match, same stack placement and SKU is `exact`; leftover is “prettier CI errors.” That is auto-reject #5, which the write-up denies in prose while listing neither bubblewrap nor firejail as incumbents.

`as_oss: Sparse 2.0` while `as_company: Sparse 2.5` is inverted. If anything is publishable here, it is a thin wrapper around landrun/bwrap, which the rubric calls Occupied leftover, not a sparser OSS seat.

---

## How accurate are the docs?

### Methodology (`.docs/methodology.md`) — 7 / 10

What it gets right:

- Occupancy vs pain is the actual skill.
- Dual scores, six seat-match labels, seven auto-rejects, three falsification tests, and “no /100” match the references.
- The pipeline shape matches `SKILL.md`.

What it gets wrong:

1. **Falsification wording is inverted.** The rubric says: a “do not build” catalog is *wrong for this seat* only if all three tests hold. The methodology says a seat is “falsified as pitchable” if those tests pass. Same checklist, opposite English. Readers will think pass = kill.
2. **Score bands drifted.** Rubric: Greenfield 0–1, Sparse 2–4, Occupied 5–7, Saturated 8–10. Methodology: 0.0–1.9 / 2.0–4.9 / 5.0–7.9 / 8.0–10.0. That lets a 4.9 still be called Sparse.
3. **`wrong_substrate` is over-counted.** Seat-match counts it *weakly* toward problem density. Methodology lists it with `adjacent_pain` and `price_packaging` as a full counter.
4. **Stage order vs skill.** Methodology: Intake → Deny → Generate. Skill: scope gate, then generate only after the gate, then deny, then restate. Small, but it hides that slogan hunts must stop at intake.

The methodology is a decent popularization of the skill. It is not a substitute for the reference files, and the two keep cards did not actually apply the bundle / `file_on` / steelman-ceiling rules it describes.

### SaaS evaluation — 5 / 10 factual, 4 / 10 occupancy

Correct and useful:

- Immutable host (vanilla RDS/Aurora, no custom C extensions) is the right constraint.
- Vitess / Citus / Nile as `wrong_substrate` is correctly labeled.
- pgroll as `adjacent_pain` (schema expand/contract, not tenant extract) is correct.
- Sequences are not replicated by logical replication; leftover is real.
- “90% of B2B SaaS start on shared-schema Postgres” and “$20k–$50k/year license” are unsourced TAM. Rubric: kill the number, do not Occupied-score from it. The card marked `claim_hygiene: ok` anyway.

Material errors:

| Claim | Check |
| --- | --- |
| DMS “designed for full-instance migrations; cannot orchestrate multi-table tenant slicing” | DMS **source filters** are per-column, including `eq` on `tenant_id`. FKs and sequences remain weak. Label should stay `adjacent_pain`, leftover must mention filters. |
| Only PG15 WHERE sits in the mechanical slice | Missed `pg_easy_replicate`, sbshift, pg_dbmigrator, DMS filters, pgcopydb#161 |
| “Sub-second connection-pool write drain” via PgBouncer **or RDS Proxy** | RDS Proxy has **no PAUSE**. Blue/Green switchover drops connections. `pg_easy_replicate` itself quotes “up to <1min, depending.” Sub-second on a whale tenant is the checksum-class claim. |
| `1_vacant_process: pass` while an `exact` incumbent is on the table | Vacant-process is only true if the seat is redefined as “FK-aware orchestrator.” That redefinition is the Occupied-bundle trick calibration forbids. |
| `as_plugin: Greenfield 1.0` | Contradicts the exact PG15 row and the DMS/pgcopydb leftovers |

### Dev-tool evaluation — 3.5 / 10 factual, 3 / 10 occupancy

Correct and useful:

- Pain (flakes, undeclared egress, secret reads) is real. Pain is not occupancy.
- Bazel as `wrong_substrate` for an in-place `npm test` wrapper is fair.
- MSW as `language_scoped` is correct.
- Trunk Flaky Tests as advisory `adjacent_pain` is correct.
- Kernel 5.13 filesystem Landlock / 6.7 TCP Landlock versions are right.

Material errors:

| Claim | Check |
| --- | --- |
| Landlock v3/v4 enforces loopback-only IPs | **False.** ABI v4 is TCP **ports**. |
| `unshare -n` “completely destroys loopback” | Overstated. `lo` starts down; user+net ns can bring it up. Host loopback is a different namespace either way. |
| Zero unprivileged tools provide loopback-preserving isolation | **False.** bubblewrap, firejail `--net=none`, systemd `PrivateNetwork` |
| landrun lacks loopback preservation, so the Landlock product is vacant | The candidate uses the **same** Landlock net model landrun already exposes (`--connect-tcp` / `--bind-tcp`) |
| “Compiling Landlock cannot be done in a 50-line script” | landrun is the compiled binary. Remaining work is argv and diagnostics. Auto-reject #2/#5 |
| “95% of teams cannot afford Bazel” | Unsourced |
| GitHub Actions Ubuntu, no root, Landlock v4 | ubuntu-24.04 runners are currently ~6.17 and can support high Landlock ABIs; ubuntu-22.04 is ~6.8 (ABI 4 possible). User namespaces are a separate host lottery. Not a fatal error, but the immutable host is not uniform |

### Killed-candidate audit — 8 / 10

| Killed seat | Independent | Notes |
| --- | --- | --- |
| Merge-stack bundle | **drop** stands | Matches calibration case 1. Mergiraf occupies syntax-aware merge. SemaMerge-as-cited is the calibration prior; do not treat “no single logo sells all three slices” as Sparse |
| Worktree loopback isolation | **`file_on` silo** stands | Product is real at [silo.rs](https://www.silo.rs/). Cited `https://github.com/graphprotocol/silo` is **404**. Current repo is [silo-rs/silo](https://github.com/silo-rs/silo) |
| Universal SQL mutation upcast | **drop** stands | Auto-reject #3 is correctly applied |
| Secret reverse-mapper | **drop** stands | Auto-reject #4 is correctly applied |
| Third-party OpenTofu lockfile | **drop** stands | `.terraform.lock.hcl` already locks **providers**. Module hashes would still be a sidecar the host does not consult. Auto-reject #7 |

Negative proofs are the strongest part of the packet. A hunt that kills five seats and then keeps two Occupied bundles has applied the deny catalog to the wrong rows.

### Executive README — 4 / 10

- Repeats Sparse company verdicts that do not survive a rater pass.
- All documentation links are `file:///C:/Users/kiran/...` Windows worktree paths. They do not work in this repo.
- `as_plugin: Greenfield 1.0` on both cards is advertised as a feature. It is a scoring bug.

---

## Incumbent hygiene (quotes and URLs)

Search playbook: verified URL plus **exact quote from that page**. Most rows are plausible paraphrases, stitched sentences, or quotes from a different URL than the one cited.

| Row | URL | Quote |
| --- | --- | --- |
| PostgreSQL CREATE PUBLICATION | Live | Stitched. “A row filter expression allows rows to be replicated conditionally…” is **not** on the cited page. Real text: “If the optional WHERE clause is specified, it defines a row filter expression.” |
| Vitess MoveTables | **404** (`/docs/user-guides/migration/movetables/`). Live is `/docs/25.0/reference/vreplication/movetables/` or `/docs/23.0/user-guides/migration/move-tables/` | Paraphrase of lifecycle, not a page quote |
| Citus `isolate_tenant_to_new_shard` | `en/stable/...` is stale; current is `en/latest/develop/api_udf.html` | Paraphrase. The “splits the original shard” clause is true on the *cluster management* page, not on the cited UDF page |
| AWS DMS CDC | Cited CDC chapter | Task-type sentence is directionally right; the more important **source filter** page was not searched |
| pgroll | Live | Paraphrase. README says “safe and reversible schema migrations… by serving multiple schema versions,” not “by using an expand-contract pattern” (that phrase is later in “How pgroll works”) |
| pgcopydb | Live | Composite. README says it automates `pg_dump \| pg_restore`. Logical-decoding follow is documented, but not in the quoted sentence |
| Nile | `/docs` is an index/marketing page | Architecture quote about tenant-dedicated pages lives on `/docs/getting-started/architecture`. Label `wrong_substrate` is still correct |
| Bazel sandboxing | Live | Paraphrase. Page says “permission restricting strategy,” not “restricted and temporary execution root” |
| nsjail | GitHub about-text, not README body | Close enough to the repo description |
| landrun | Close to README | Best quote in the table |
| Trunk Flaky Tests | Cited `docs.trunk.io/flaky-tests` | **Quote is not on that page.** The same sentence exists on the marketing page `trunk.io/flaky-tests` |
| MSW | Cited homepage | Exact sentence not on the current homepage |
| unshare(1) | man7.org | Old NAME line. Current is “unshare - run program in new namespaces,” not “with some namespaces unshared from parent” |
| silo (killed table) | graphprotocol/silo | **404** |

`claim_hygiene: ok` on both cards is not supportable once quotes are this loose. Unverified fetch should have been `NEED_EVIDENCE`, not a keep.

---

## Missed incumbents that move the score

### SaaS seat

- **AWS DMS source filters** — row predicates on named columns, including tenant id. Still weak on FKs/sequences. Raises problem density; leftover is orchestration, not “DMS cannot slice.”
- **pg_easy_replicate** — bootstrap, start_sync, lag watch, source read-only, sequence refresh, drop subscription. This *is* the cutover daemon on vanilla Postgres.
- **sbshift** — preflight / replicate / watch / reconcile / cutover on PG15+ logical replication.
- **pgcopydb#161** — explicit tenant-extract feature request; current filters are table/schema only, not row predicates.
- **RDS Blue/Green** — instance-level cutover, not tenant slice; still occupies “sub-second pool drain on RDS” rhetoric.

### Dev-tool seat

- **landrun** — already in the table, **mislabeled**. Should be `exact` or at most `adjacent_pain` with auto-reject #5.
- **bubblewrap `--unshare-net`** — unprivileged, loopback configured, no egress. Mentioned in auto-reject defense, **absent from the incumbent table**.
- **firejail `--net=none`**
- **systemd `PrivateNetwork=yes`**
- **step-security harden-runner** — CI egress policy, different plane (`adjacent_pain` / `wrong_substrate`), but it is how many orgs actually stop undeclared CI network.

---

## Process fidelity (did the hunt follow its own skill?)

| Rule | What happened |
| --- | --- |
| Do not score from memory; verified URLs | URLs exist; several 404 or quote-mismatch. Failed |
| Exact quotes from the cited page | Mostly paraphrases. Failed |
| Steelman ceiling; published exact density may not exceed it unless new named rows appear | SaaS 1.5 ≤ 3.5 and dev 1.0 ≤ 3.0 are internally consistent **because the missed rows never entered the table**. Ceiling was a self-fulfilling search miss |
| Occupied bundle is Occupied, not Sparse | Both keeps are bundles. Failed |
| Auto-reject #5 “add this to incumbent X” | landrun and pgcopydb/pg_easy_replicate. Denied in prose. Failed |
| `as_plugin` is the honest leftover on a named host | Scored Greenfield 1.0 twice. Failed |
| Local deny file wins if present | `.docs/killed-candidates.md` is a killed-seats table; cards say `deny_catalog: embedded_baseline` |
| ≥5 raw seats, expect most to drop | 2 keep + 5 kill is the right *shape*. The two keeps should have been drops |
| Claim hygiene for unsourced ROI / implausible latency | 90%, 95%, $20k–$50k, sub-second cutover, Landlock-by-IP all passed as `ok` |
| `rate_next: compose_next` | Correct: finder must not emit a rater headline. This report is that rater pass |

---

## What a balanced model did well

Credit where it is due. A weaker generator would have emitted “AI developer productivity” and a TAM slide.

- Both keeps are **named stack seats** with `v1_as_shipped`, substrate, and immutable host. Scope gate passed.
- Seat-match on Vitess / Citus / Nile / MSW / Bazel is mostly disciplined. The model did not call Vitess an exact Postgres occupant.
- Killed seats 3–5 (non-invertible SQL, confused-deputy secret proxy, sidecar lockfile) are the skill working.
- Dual scores instead of 85/100 is correct.
- The **idea shapes** (tenant extract on RDS; unprivileged hermetic tests) are problems operators actually have. Occupancy is what failed, not problem discovery.

A balanced model is good at restating a seat and writing confident leftover prose. It is weak at **exhaustive incumbent search**, **verbatim quotes**, and **not talking itself out of auto-reject #5**. Those three failures are exactly how Sparse 2.5/3.0 keeps appear on Occupied aisles.

---

## Recommended dispositions

1. **Do not pitch either as a company** on this packet.
2. If anything is built:
   - SaaS leftover → OSS/plugin: tenant-closure inference + `CREATE PUBLICATION ... WHERE` generation, ideally as a pgcopydb filter or `pg_easy_replicate` group option. Not a control plane.
   - Dev-tool leftover → `landrun` profile or `bwrap --unshare-net` wrapper that prints the denied path/socket. Not a new LSM product.
3. Before another hunt: require quote strings to appear on the fetched page; add bubblewrap/DMS-filters/`pg_easy_replicate` to the default search spine for these two substrates; treat `as_plugin: Greenfield` with an `exact` row already on the table as an automatic card fail.

---

## Sources checked (non-exhaustive)

- PostgreSQL 15/18 CREATE PUBLICATION and row-filter docs
- AWS DMS source filters and PostgreSQL target limitations
- pgcopydb README and issue 161
- pg_easy_replicate README / switchover behavior
- sbshift README
- Nile architecture
- Citus `isolate_tenant_to_new_shard` UDF + cluster management
- Vitess MoveTables (current path; cited path 404)
- Landlock kernel userspace API (ABI v4 = TCP ports)
- landrun README (TCP `--connect-tcp` / `--bind-tcp`)
- bubblewrap `--unshare-net` + loopback setup
- firejail `--net=none`
- systemd `PrivateNetwork`
- silo.rs / silo-rs/silo (graphprotocol/silo 404)
- OpenTofu `.terraform.lock.hcl` (providers only)
- GitHub Actions ubuntu-24.04 kernel ~6.17 vs ubuntu-22.04 ~6.8
