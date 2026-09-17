# Independent Rating: PR #7 (Kafkatrap + PgLSN Gateway)

Date: 2026-09-17
Object: the two Sparse 2.5 company-keeps in [kirank55/profinder#7](https://github.com/kirank55/profinder/pull/7) (`feat/kafkatrap-and-pglsn-only` @ `2e3882e`), plus the supporting `.docs/` write-ups in that PR.
Method: rater pass against `references/rubric.md`, `references/seat-match.md`, `references/calibration.md`, and `references/keep-gate.md`, plus live URL checks. This is not a second finder hunt and is not a /100 score of the PR.

PR #7 targets `main`. `main` still loads calibration only “on a boundary.” The Kafka wire-proxy case **is** that boundary. The keep-gate latch from PR #5 lives on this branch (`profinder_pitchable_saas_ideas`); the occupancy verdicts below do not depend on it.

## Bottom line

Using a balanced model with Profinder is the right **job**. These two cards are not a correct **keep**.

Both candidates were marked Sparse 2.5 company-keeps with `file_on: none`. Independently they are **Occupied leftovers**: a Kroxylicious filter plus CI packaging, and a Pgpool/Aurora/Heimdall read-your-writes aisle with an LSN-cookie leftover. The hunt found the exact hosts, labeled them `exact` or cited their docs, then kept Sparse by shrinking the leftover into packaging and by omitting the flags on the pages it already opened.

| Artifact | Accuracy of facts | Accuracy of occupancy verdict | Independent rater verdict |
| --- | ---: | ---: | --- |
| `.docs/selection-methodology.md` | 6.5 / 10 | n/a (process doc) | Occupancy-first frame is real. Band drift and inverted “why Sparse” on these two seats. |
| Dev tool: Kafkatrap | 4 / 10 | 2.5 / 10 | **Occupied 6.0 as_company** · Sparse 3.5 as_oss · Occupied 7.0 as_plugin · `file_on` Kroxylicious |
| SaaS: PgLSN Gateway | 4 / 10 | 2 / 10 | **Occupied 6.5 as_company** · Sparse 3.0 as_oss · Occupied 7.0 as_plugin · `file_on` Pgpool-II / Aurora write-forwarding |
| `.docs/deny-and-falsification-audit.md` | 3 / 10 | 2 / 10 | Auto-reject #5 and vacant-process both fail. Collapse mode 1 was scored PASS on the hosts that occupy the leftover. |
| `.docs/README.md` | 3 / 10 | 2 / 10 | Repeats Sparse keeps. Broken `file://` Windows paths. |

**Do not found either company on this evidence.** Honest leftovers are a Kroxylicious protocol filter (and/or a kfake `ControlKey` harness) and a session-stickiness / LSN-cookie flag on an existing PgWire pooler. `as_plugin: Occupied 6.0` / `7.0` on the cards already said that. `file_on: none` contradicted it.

---

## Independent ratings

No overall /100. Bands from `references/rubric.md` (Greenfield 0–1, Sparse 2–4, Occupied 5–7, Saturated 8–10).

### 1. Kafkatrap (dev tool)

**Claimed seat.** Deterministic Kafka wire-protocol proxy that injects coordinator frames (`JoinGroup`, `SyncGroup`, `Heartbeat`, `OffsetCommit`) at record offsets in CI.

| Field | PR #7 | Independent |
| --- | --- | --- |
| `as_company` | Sparse 2.5 | **Occupied 6.0** |
| `as_oss` | Greenfield 1.5 | **Sparse 3.5** (bounded Kroxylicious filter / kfake harness) |
| `as_plugin` | Occupied 6.0 | **Occupied 7.0** · `file_on` |
| `problem_density` | 7 | **8.5** |
| `exact_mechanics_density` | 2 | **4.5** |
| Steelman ceiling | 3.0 | **6.0** (raised by named rows the hunt had, then under-counted, plus rows it missed) |
| `claim_hygiene` | ok | **unsourced** (stitched / invented quotes) |
| `file_on` | none | [Kroxylicious Filter API](https://kroxylicious.io/documentation/0.20.0/html/developer-guide/) (`JoinGroupRequestFilter`, `HeartbeatRequestFilter`, `shortCircuitResponse` / `errorResponse`); also [kfake `ControlKey`](https://github.com/twmb/franz-go/blob/master/docs/testing.md) |
| Auto-rejects | none | **#5** (add a coordinator-error filter + offset trigger to Kroxylicious). **#1** if the headline UX is “protocol-aware Kafka proxy,” which already ships |
| Keep-gate | omitted | **fail** (G1, G2, G3, G4, G5, G6, G8) |
| Disposition | keep | **`file_on` / `drop` as a company** |

**What is still real.** Consumer-group rebalance bugs are painful. Toxiproxy cannot inject `REBALANCE_IN_PROGRESS` without tearing the TCP socket. Testcontainers does not speak Kafka RPCs. Antithesis is `price_packaging`. Coyote is `language_scoped`. Those labels in the card are fine.

**Why it is not a company.** Calibration on `main` already covers this aisle:

> Kroxylicious is `exact` for a Kafka proxy slice. … `as_company` likely Occupied or `file_on` if leftover is a Kroxylicious filter plus SQL assertions.

The hunt labeled Kroxylicious `exact`, then kept Sparse 2.5 because the leftover is “not a lightweight CI daemon.” That is packaging, not a vacant process.

The spec lists four “not a wrapper” mechanisms. Three already ship on the exact host:

1. **Protocol frame awareness** — Kroxylicious is a Kafka protocol proxy. README: “Kroxylicious is a Kafka protocol proxy.” Filter interfaces exist per API key, including `JoinGroupRequestFilter` and `HeartbeatRequestFilter`.
2. **Advertised-listener rewrite** — Kroxylicious “automatically intercepts all the Kafka RPC responses that contain a broker address” (`Metadata`, `DescribeCluster`, `FindCoordinator`) and rewrites them to the virtual cluster. This is the NAT the spec treats as novel. grepplabs/kafka-proxy does the same rewrite for Metadata / FindCoordinator.
3. **Coordinator error injection** — `RequestFilterResultBuilder.shortCircuitResponse` / `errorResponse(ApiException)` returns a protocol-valid error to the client without forwarding. That is `REBALANCE_IN_PROGRESS` / `ILLEGAL_GENERATION` as a filter, not a new daemon. kfake `ControlKey` injects API-key-specific responses (including errors) in-process for CI.
4. **Offset-triggered rules + local HTTP control API** — this is the only named leftover. It is test-runner UX on top of (1)–(3). Auto-reject #5.

`1_vacant_process: pass` while an `exact` row sits on the card is a G4 fail. G3: leftover sentences name Kroxylicious; `file_on` must be that URL, not `none`. G8: `as_oss` Greenfield 1.5 is an illegal band (Greenfield is 0–1) and is *sparser* than `as_company` 2.5 with no reason. A Kroxylicious filter is more occupied as plugin/OSS, not less.

`as_plugin: Occupied 6.0` was the honest score. Publishing Sparse as_company next to it is the balanced-model skip: leftover prose over the plugin score.

### 2. PgLSN Gateway (SaaS)

**Claimed seat.** Managed PgWire proxy that captures `pg_current_wal_lsn()` on commit and routes later reads to replicas whose `pg_last_wal_replay_lsn()` is caught up, else primary, on AWS RDS / Aurora Postgres.

| Field | PR #7 | Independent |
| --- | --- | --- |
| `as_company` | Sparse 2.5 | **Occupied 6.5** |
| `as_oss` | Sparse 3.0 | **Sparse 3.0** (LSN cookie on an existing pooler; not a company) |
| `as_plugin` | Occupied 7.0 | **Occupied 7.0** · `file_on` (unchanged occupancy, wrong `file_on: none`) |
| `problem_density` | 8 | **9.0** |
| `exact_mechanics_density` | 2 | **4.0** (Aurora `SESSION` is `exact` for the named Aurora host slice; go-pgrouter is `language_scoped` for the LSN-cookie leftover) |
| Steelman ceiling | 3.0 | **6.5** |
| `claim_hygiene` | ok | **unsourced + implausible TAM** (“80%+ of teams,” “3–5x throughput,” `$5k–$15k/mo` primary) |
| `file_on` | none | [Pgpool-II `disable_load_balance_on_write`](https://www.pgpool.net/docs/latest/en/html/runtime-config-load-balancing.html); [Aurora local write forwarding `SESSION`](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-postgresql-write-forwarding-configuring.html); [Heimdall R/W split](https://www.heimdalldata.com/using-the-heimdall-proxy-to-split-reads-and-writes-with-acid-compliance/) |
| Auto-rejects | none | **#5** (add per-session LSN tokens to PgCat / Pgpool / PgDog). **#1** on Aurora if the headline UX is “read-your-writes without splitting connections,” which `apg_write_forward.consistency_mode=SESSION` already is |
| Keep-gate | omitted | **fail** (G1, G2, G3, G4, G5, G6, G7) |
| Disposition | keep | **`file_on` / `drop` as a company** |

**What is still real.** RDS Proxy does not inspect SQL to split reads and writes; applications pick writer vs reader endpoints. Blind `SELECT`→replica routing can return stale rows after a commit. A per-session LSN cookie compared to `pg_last_wal_replay_lsn()` is a real mechanism, and no *widely adopted PgWire SaaS* sells that exact token.

**Why it is not a company.** `v1_as_shipped` is a **conjunction** (G5): PgWire proxy + commit-LSN capture + replica matrix + managed SaaS + “zero application changes.” Each slice has a host.

| Slice | Occupant | Label |
| --- | --- | --- |
| PgWire pooler / proxy | PgCat, Pgpool-II, PgDog, ProxySQL (PostgreSQL protocol is now first-class), RDS Proxy | `exact` for the proxy SKU; leftover is routing policy |
| Stick reads to primary after a write in the session | Pgpool-II `disable_load_balance_on_write` = `always` / `trans_transaction` / `transaction` **on the URL the card already cites** | `exact` for the session-stickiness leftover the write-up claims is missing |
| Host-native read-your-writes on Aurora | `apg_write_forward.consistency_mode=SESSION` (default): reader waits until forwarded writes of *this session* are visible | `exact` for the named Aurora host; `wrong_substrate` only for vanilla RDS Postgres |
| Commercial “no stale reads” R/W split SaaS | Heimdall: last-write table timestamps + measured replica lag, “without modifying your application code” | `adjacent_pain` (timestamp vs LSN) that already sells the headline UX |
| Cluster LSN lag, ban stale replicas | PgDog `pg_current_wal_lsn()` / `pg_last_wal_replay_lsn()`, `ban_replica_lag` | `adjacent_pain` |
| Per-session LSN cookie + fallback to primary | [go-pgrouter](https://github.com/alfari16/go-pgrouter) `pg_min_lsn` cookie, `ReadYourWrites` | `language_scoped` (Go HTTP middleware, not a wire proxy) |

The card’s Pgpool leftover is false on its own citation:

> lacks per-request/session causal tokens, forcing all clients to either risk stale reads or manually annotate SQL with `/*NO LOAD BALANCE*/`

The cited page defines `disable_load_balance_on_write` for exactly “if a client read the same row right after the write query, the client may not see the latest value.” `always` pins the rest of the session to primary. `dml_adaptive` even tracks written tables inside a transaction. That is not “coarse byte polling only.” `delay_threshold` is a second, cluster-wide lag cap; it is not the whole product.

Aurora write forwarding is named in a YAML comment (`problem_density` counts it) and then **dropped from the incumbent table**. That is a G2 miss of the host primitive on the named immutable host.

`as_plugin: Occupied 7.0` with `file_on: none` is the same internal contradiction as Kafkatrap. Occupied plugin leftover cannot be a Sparse company keep.

Falsification `1_vacant_process: pass` fails: the process “do not serve a read from a replica that has not seen this session’s write” is occupied by Pgpool session stickiness and by Aurora `SESSION`. Redefining the seat as “the orchestrator that uses WAL LSN tokens instead of stickiness” is G4.

---

## Keep-gate (fail-closed latch)

Cards omit `keep_gate`, `slices`, and `search_classes`. After PR #5 those fields are required for a Sparse company keep. Even against `main`’s looser finder, G1–G9 fail on the evidence the cards already contain.

| Check | Kafkatrap | PgLSN Gateway |
| --- | --- | --- |
| G1 quotes are literals | **fail** | **fail** |
| G2 four query classes | **fail** (five adjacent logos; missed kfake, kafka-proxy, Filter API short-circuit) | **fail** (missed Aurora `SESSION`, PgDog LSN, go-pgrouter, ProxySQL PG, `disable_load_balance_on_write` despite citing that page) |
| G3 leftover names a host → `file_on` | **fail** (Kroxylicious named; `file_on: none`) | **fail** (Pgpool / PgCat / Heimdall named; `file_on: none`) |
| G4 exact occupies vacant-process | **fail** (Kroxylicious `exact` + `1_vacant_process: pass`) | **fail** (vacant-process pass while Aurora host primitive and Pgpool session flag occupy the process) |
| G5 conjunction v1 is a bundle | **fail** (proxy + listener NAT + coordinator injector + offset trigger + CI harness) | **fail** (proxy + LSN token + replica matrix + managed SaaS) |
| G6 auto-reject #5 | **fail** | **fail** |
| G7 mechanism claims | n/a (no physics number) | **fail** (unsourced 80% / 3–5x / $5k–$15k) |
| G8 split-verdict sanity | **fail** (`as_oss` Greenfield 1.5 < `as_company` 2.5; illegal band) | `as_plugin` Occupied 7.0 vs Sparse company keep is the same class of fail |
| G9 steelman | **fail** (ceiling 3.0 held while `exact` Kroxylicious sat in the table) | **fail** (ceiling 3.0 held while host primitives were in comments or on cited pages) |

---

## Quote hygiene

Search playbook: verified URL plus a **contiguous substring** of that page. `claim_hygiene: ok` is not supportable.

| Row | Cited URL | Quote check |
| --- | --- | --- |
| Kroxylicious | github.com/kroxylicious/kroxylicious | **Stitched.** Page says “the snappy open source proxy for Apache Kafka” and “Kroxylicious is a Kafka protocol proxy.” Not “open-source, protocol-aware wire proxy.” |
| Toxiproxy | github.com/Shopify/toxiproxy | Close to GitHub about-text (“A TCP proxy to simulate network and system conditions for chaos and resiliency testing”). Card adds “and integration testing” and drops the emoji line. Paraphrase. |
| Testcontainers Kafka | testcontainers.com/modules/kafka/ | **Invented.** Page is a module index (“Kafka is an open-source distributed event streaming platform…”). It does not say “programmatically manage Apache Kafka instances in Docker containers during your tests.” |
| Filibuster | filibuster.cloud | **Invented.** Homepage talks about synthesizing reliability tests from existing tests. It does not contain “automated fault injection testing tool that tests microservices for resilience to inter-service failure.” |
| Antithesis | antithesis.com | **Paraphrase.** Current page: custom hypervisor, rewind, fault injection. It does not contain the quoted “runs your software inside a deterministic hypervisor, where it can search for bugs and reproduce them every time.” |
| Coyote | github.com/microsoft/coyote | **Paraphrase.** About-text: “library and tool for testing concurrent C# code and deterministically reproducing bugs.” Not “building reliable asynchronous software in C# and .NET using systematic testing.” Label `language_scoped` is still correct. |
| AWS RDS Proxy | docs.aws.amazon.com/.../rds-proxy.html | **Invented.** That page is pooling / failover / IAM. It does not contain “does not perform automatic, transparent read/write splitting… application code must be configured….” Directionally true on *other* pages (separate `READ_ONLY` endpoints). G1 still fails. |
| PgCat | github.com/postgresml/pgcat | **Invented.** README: “Load balancing of read queries” / query parser routes `SELECT` to replicas. It does not mention “read-your-writes consistency due to asynchronous replication lag.” |
| Pgpool-II | …/runtime-config-load-balancing.html | **Stitched + wrong leftover.** `delay_threshold` exists. The quoted sentence is not a contiguous substring. The same page’s `disable_load_balance_on_write` occupies the leftover the card denies. |
| Heimdall | heimdalldata.com (homepage) | **Wrong URL.** Homepage does not contain “tracks writes on a per-table basis….” That mechanism is on the R/W-split docs. Label `adjacent_pain` is still fair. |
| Prisma Accelerate | prisma.io/accelerate | **Invented, and the URL no longer describes Accelerate.** Fetched page is Prisma’s TypeScript agent platform. No LSN sentence. `wrong_substrate` would have been right for an ORM cache; the quote is still a G1 fail. |
| ProxySQL | proxysql.com | **Stale + false leftover.** Quote “protocol aware proxy for MySQL” is not on the current homepage. Page now: “leading proxy for MySQL, PostgreSQL” with “native support for the MySQL and PostgreSQL wire protocols.” `wrong_substrate` is **wrong**. Label `adjacent_pain`. ProxySQL still does not do per-request LSN RYW (blog: no view of lag versus a global LSN); `max_replication_lag` shuns stale replicas. |

Broken `file:///c:/Users/kiran/code/p/profinder/...` links in `.docs/README.md` and the methodology are the same Windows-worktree bug as the previous hunt.

---

## Missed incumbents that move the score

### Kafkatrap

- **Kroxylicious `shortCircuitResponse` / `errorResponse`** — host primitive for coordinator error injection. Hunt cited the GitHub repo, not the Filter API.
- **Kroxylicious advertised-address rewrite** — host primitive for the spec’s “dynamic advertised listener” slice.
- **kfake `ControlKey`** — drop-in CI cluster that intercepts API keys and returns custom (error) responses. Class 2.
- **grepplabs/kafka-proxy** — Kafka-aware proxy that rewrites Metadata / FindCoordinator advertised hosts. Class 2.

### PgLSN Gateway

- **Pgpool-II `disable_load_balance_on_write`** — on the cited page. Class 1.
- **Aurora `apg_write_forward.consistency_mode=SESSION`** — host primitive on the named Aurora host. Class 1. Mentioned in a comment, omitted as a row.
- **Heimdall table-timestamp + lag window** — commercial SKU for “R/W split without stale reads, no app changes.” Class 3. Under-labeled leftover.
- **PgDog LSN checks / `ban_replica_lag`** — class 2 pooler already comparing `pg_current_wal_lsn()` to replica replay LSN.
- **go-pgrouter** — class 2/4 leftover: `pg_min_lsn` cookie, replica `GetLastReplayLSN`, fallback to primary. `language_scoped`.
- **ProxySQL PostgreSQL** — not MySQL-only. `pgsql_query_rules` R/W split + `max_replication_lag`.

Five-logo tables of Toxiproxy / Testcontainers / Filibuster / Coyote / ProxySQL-as-MySQL are G2: adjacent or wrong-substrate rows without class 1–2.

---

## How accurate are the docs?

### Selection methodology — 6.5 / 10

What it gets right: occupancy vs pain, dual density, split verdicts, no /100, substrate + immutable host.

What it gets wrong:

1. **Score bands drifted** the same way as the previous hunt. Rubric: Sparse 2–4 integers. Methodology: 2.0–4.9. That is how 2.5 looks more precise than the evidence.
2. **“Why these two ideas were chosen” treats leftover packaging as vacancy.** Kroxylicious “is an enterprise production gateway for payload encryption, not a developer-facing CI tool” is a `price_packaging` / SKU-shape argument, not `exact_mechanics_density = 2`.
3. **RDS Proxy “explicitly refuses” query inspection** is overstated. RDS Proxy understands the protocol enough to multiplex and pin; it does not offer SQL R/W split. Separate endpoints exist.
4. **“Zero existing SaaS products offer transparent PgWire causal session consistency”** ignores Heimdall’s sold R/W-split-with-consistency SKU and Aurora’s host-native `SESSION` mode.

### Deny and falsification audit — 3 / 10

Collapse mode 1 (“file it on the incumbent”) is marked PASS for both seats. That is the mode that actually fires.

Auto-reject #5 is marked CLEAR because the leftover is not “an upstream PR to Toxiproxy or Kafka” / “a patch on RDS Proxy.” The rubric’s #5 is “add this to incumbent X,” and the cards already name Kroxylicious and PgCat. CI harness packaging and LSN tokens are that reject.

`1_vacant_process` is marked pass with an `exact` Kroxylicious row and with Pgpool/Aurora occupying the read-your-writes process. Rubric: vacant-process fails when any incumbent is `exact` for a slice of `v1_as_shipped` unless `file_on` is set and the company score is only the remaining process.

Claim-hygiene section congratulates both cards for avoiding implausible physics, then both cards still ship unsourced ROI/TAM. Hygiene fail is not Occupied-by-itself; it still blocks `claim_hygiene: ok`.

### Incumbent vacancy write-ups

Useful: Toxiproxy is frame-blind; Testcontainers is a container lifecycle; RDS Proxy is not a SQL splitter; ProxySQL-as-MySQL would be `wrong_substrate` if it were still true.

Not useful: Kroxylicious reduced to “KMS encryption”; Pgpool reduced to `delay_threshold`; Heimdall leftover “defeats replica scaling during continuous writes” is an argument about *their* coarseness, not proof no SKU occupies the pain; Prisma/Filibuster quotes are not on the cited pages.

---

## Process fidelity (balanced-model hunt)

The skill is finder-only. A balanced model can hunt seats. It cannot be trusted to **keep** Sparse unless the latch files run.

What this hunt did correctly:

- Scope gate: named substrate (Kafka wire protocol / PgWire + WAL LSN) and immutable host (Kafka in CI / RDS+Aurora).
- Split verdicts, dual density, steelman field present, ≥5 named rows.
- Several seat-match labels are right (Toxiproxy / Testcontainers `adjacent_pain`, Antithesis `price_packaging`, Coyote `language_scoped`).
- `as_plugin` Occupied on both cards.

What it skipped, which is why the keeps are wrong:

1. **Calibration on `main` already kills Kafkatrap’s company keep.** “Load calibration only on a boundary” let the model skip the Kafka-proxy case while labeling Kroxylicious `exact`. That is the bug PR #5 closed with a mandatory keep-gate.
2. **No `file_on` despite Occupied `as_plugin`.** Finder disposition is split verdicts **plus** `file_on`. `none` is a keep-shaped lie.
3. **Cited page, omitted occupying flag.** Pgpool load-balancing doc without `disable_load_balance_on_write`. Kroxylicious GitHub without Filter API short-circuit. Aurora named in a comment, not a row.
4. **Paraphrase quotes marked verified.** G1 would have turned those rows into `NEED_EVIDENCE` and blocked the keep.
5. **Conjunction v1 scored as one SKU.** Same Occupied-bundle mistake as tenant-slice cutover and the Landlock test gate.
6. **PR against `main`, not the hardened skill.** Even so, `main` was enough to `file_on` Kroxylicious.

This is the same balanced-model pattern as the previous two Sparse keeps: occupancy vocabulary, adjacent-pain table, eloquent leftover, `file_on: none`.

---

## Dispositions (do not found)

| Seat | Company | OSS leftover | File on |
| --- | --- | --- | --- |
| Kafkatrap | Occupied 6.0 · drop | Sparse 3.5 Kroxylicious filter or kfake `ControlKey` harness that injects coordinator errors at a fetch offset | https://kroxylicious.io/documentation/0.20.0/html/developer-guide/ |
| PgLSN Gateway | Occupied 6.5 · drop | Sparse 3.0 LSN cookie / session token on PgCat, Pgpool, or PgDog | `disable_load_balance_on_write`; Aurora `SESSION` write-forwarding on the Aurora host; Heimdall if the pitch is managed R/W split |

Do not generate new company hunts from these leftovers. They are labeling, not seeds.
