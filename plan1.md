# Plan 1 (improved): build `profinder` as a seat-finder skill

Complementary to `pitch-rate` (llmresearch PR #8): that skill **rates** a given idea; this skill **finds** sparse developer-tool / infra seats. One job. No verify mode. No overall `/100`.

Delta from the original `plan1.md`: pin the product, spell the finder procedure, add `search-playbook.md` + `seat-generation.md`, specify the candidate YAML, add a deny **fallback** (ADR 0001 still wins), add a hunt dry-run, and treat the missing PR #8 patch as a blocking vendor step instead of “captured in a prior session.”

---

## 0. Product and evidence

**Product (closed):** `profinder` is an occupancy-first **seat hunter** for developer-tool / infrastructure / systems stack positions. It is not a GitHub-profile, freelancer, or professor finder. If the user asks for people-search, abort: wrong skill; do not reuse these references.

**Job split:**

| Skill | Job | Output |
|---|---|---|
| `profinder` (this) | Propose and document vacant seats | Candidate card (`output-template.md`) |
| `pitch-rate` (PR #8) | Rate a given idea / ADR | `PITCH \| KILL \| NEED_EVIDENCE \| FILE_ON_X` |

Compose, do not absorb: hunt emits a candidate; the user runs `pitch-rate` if they want a rater verdict. Packaging (“user does not have pitch-rate installed”) is not a reason to fork verify-mode into this repo.

**Source of truth for scoring rules:** vendored `pitch-rate` files, then `docs/adr/0001-no-pitchable-candidate.md` when present in the *target* workspace. Do not reconstruct rubric / seat-match / calibration from memory or from `plan2.md`. Plan 2’s extra labels (`obsolete`, `price_packaging`) and inlined 7-reject list are unverified unless they appear in the vendor patch.

**Evidence status in this repo:**

| Artifact | Status |
|---|---|
| This plan | In-tree |
| `kirank55/llmresearch` PR #8 patch | **`NEED_EVIDENCE`** — repo not resolvable from this workspace; original plan claimed a local clone at `C:\Users\kiran\code\p\llmresearch` and a patch “captured in a prior session.” Neither is here. |
| ADR 0001 / 0002 / 0003 / 0004 | **`NEED_EVIDENCE`** — live in llmresearch, not vendored |

Until `vendor/pitch-rate/` exists, a builder may scaffold `SKILL.md`, `search-playbook.md`, `seat-generation.md`, `output-template.md`, and deny *fallback* copy. They must **stop** before writing `rubric.md` / `seat-match.md` / `calibration.md` as originals. Cite unread vendor files as `NEED_EVIDENCE`; do not invent them.

**Claimed PR #8 shape** (from the original plan’s inspection; confirm against vendor, do not treat as the files):

- Path: `.pi/skills/pitch-rate/` → we flatten to repo root (`SKILL.md` + `references/`). No `.pi/` prefix, no extension/orchestrator/hunter loop.
- Procedure-only `SKILL.md`, refs on demand.
- Density bands: Saturated 8–10 / Occupied 5–7 / Sparse 2–4 / Greenfield 0–1.
- Seat-match (four labels): `exact` \| `adjacent_pain` \| `language_scoped` \| `wrong_substrate`. Strictest mismatch wins.
- Rater verdicts (pitch-rate only): `PITCH \| KILL \| NEED_EVIDENCE \| FILE_ON_X`.
- PR #7 failure modes to not commit: wrong object, score-first, category collapse, prior-kill-as-rubric.

**Targets:** Agent Skills layout (`SKILL.md` + `references/`) for OpenCode and Claude Code. Root `SKILL.md` is enough; do not hardcode a `.pi/` tree.

---

## 1. Target layout

```text
profinder/
  plan1.md
  vendor/
    README.md                   # how to obtain PR #8; see §2.0
    pitch-rate/                 # BLOCKING copy of PR #8 skill files (not present yet)
  SKILL.md                      # procedure only; load references on demand
  references/
    rubric.md                   # PORT from vendor; do not author
    seat-match.md               # PORT from vendor; four labels until vendor says otherwise
    deny-patterns.md            # port collapse modes + ADR 0001 pointer + short fallback
    search-playbook.md          # NEW: incumbent extraction for a seat already in hand
    seat-generation.md          # NEW: how vacant seats are proposed
    calibration.md              # PORT from vendor (SymMerge, SagaGuard, TenantScale, false-exacts)
    output-template.md          # finder candidate card; not a rater verdict clone
```

---

## 2. Build sequence

### 2.0 Vendor PR #8 (blocking for rubric / seat-match / calibration)

1. From a machine that can read `kirank55/llmresearch`, copy PR #8 (branch `cursor/pitch-rate-skill-bd8d`) into `vendor/pitch-rate/`:
   - `SKILL.md`
   - `references/rubric.md`
   - `references/seat-match.md`
   - `references/deny-patterns.md`
   - `references/calibration.md`
   - `references/output-template.md`
2. Record source in `vendor/README.md`: repo, PR number, commit SHA, date copied.
3. If this step cannot be done, leave those three ports unwritten and mark the build `NEED_EVIDENCE`. Do not fill them from Plan 2.

### 2.1 `SKILL.md` (write now; procedure only)

Frontmatter:

```yaml
---
name: profinder
description: >
  Find sparse developer-tool and infrastructure seats by generating stack
  positions, naming incumbents with URL plus quote, and scoring occupancy
  density. Use when asked to find, hunt, or propose product seats. Abort
  if the request is people-search (GitHub profiles, freelancers, professors).
  Do not use this skill to rate an already-chosen idea when pitch-rate is
  the requested job.
---
```

Constraints (every run):

- No repo writes by default.
- Do not score from memory. Load the cited reference file or emit `NEED_EVIDENCE`.
- No overall `/100`.
- Never inline rubric tables into `SKILL.md`.
- Load references **on demand by step**, not as a mandatory full stack. Do not load `search-playbook.md` before a seat exists. Do not load `calibration.md` unless a label is on a boundary (bundle vs slice, claim-kill vs seat-kill, false exact).
- Object is a **stack seat**, never PR hygiene. If the user pastes a PR process question, abort that object.

Procedure:

1. **Abort checks.** People-finder → stop. Request is “rate this idea / ADR like pitch-rate” → tell the user to run `pitch-rate`; optionally continue only as restatement of a seat into a candidate card, never as a rater verdict.
2. **Choose entry.**
   - User named a seat or pasted an ADR/idea as a seat → go to step 4 (restate).
   - User asked to find / hunt / propose seats → load `seat-generation.md`, produce ≥5 raw seats, then map steps 3–8 over each.
3. **Deny check.** Load `deny-patterns.md`. If the target workspace has `docs/adr/0001-no-pitchable-candidate.md`, that file wins (`deny_catalog: local_adr_0001`). Else use the embedded fallback (`deny_catalog: embedded_baseline`). If both missing, `deny_catalog: incomplete` and do not emit `as_company: PITCH`-equivalent keep.
4. **Restate.** One-line `candidate_seat`, concrete `v1_as_shipped`, named process or protocol, stack substrate. If this cannot be stated without slogans (“AI developer productivity”), drop the seat.
5. **Steelman ceiling.** Strongest case a skeptical founder would still build this. Occupancy ceiling 0–10 **before** search. Published `exact_mechanics_density` must not exceed this ceiling unless new named incumbent rows appear.
6. **Search incumbents.** Load `search-playbook.md`. Collect ≥5 incumbents, each with name, verified URL, exact quote, seat-match label, leftover. 404 or unverified fetch → that row is `NEED_EVIDENCE`; do not invent.
7. **Seat-match + dual-score.** Load `seat-match.md` then `rubric.md`. One label per incumbent; strictest mismatch wins. `problem_density` counts `adjacent_pain`; `exact_mechanics_density` counts `exact` only and must be ≤ steelman ceiling.
8. **Gates.** Apply auto-rejects and falsification from `rubric.md` (the vendored file, not this plan). Load `calibration.md` only if needed to break a tie (SymMerge bundle, TenantScale claim-kill, false exact).
9. **Emit** the candidate card from `output-template.md`. Split `as_company` / `as_oss` / `as_plugin`. Set `file_on` when the honest leftover is a flag, PR, or plugin. Do not emit a headline `decision: PITCH|KILL|…` (that is `pitch-rate`). Finder disposition is the split verdicts plus `file_on` plus `claim_hygiene`.

### 2.2 `references/seat-generation.md` (new; write now)

This file answers “how do I propose seat S?” — not “how do I search incumbents of S?”

**Start from substrates, never from pain slogans.** Pain is abundant; empty seats are not.

Substrate inventory (generate from these nouns):

- Process supervisor / daemon
- Wire proxy / protocol gate
- Compiler, linker, bundler, lockfile
- Kernel / eBPF / LSM
- CI scheduler / merge queue
- Broker / queue protocol
- Schema / tenancy cutover
- Host runtime enforcement (PATH, interpreter, package manager)

Vacancy probes (queries for missing SKUs, not “best tools for X”):

- Named protocol or RFC with no shipping daemon in that seat
- Host that does not consult a sidecar (policy file, third-party lockfile, PATH shim)
- Advisory-only tool sitting in an enforcement seat
- Language-scoped exact (in-process runtime) with a claimed language-agnostic v1 — label later; do not auto-pitch

Each raw seat must include, before search:

```yaml
candidate_seat: <stack position, one line>
v1_as_shipped: <concrete deliverable and where it sits>
substrate: <one item from the inventory>
process_or_protocol: <named process; not a vibe>
why_not_a_slogan: <the mechanic, in one sentence>
```

Drop the seat if `process_or_protocol` or `why_not_a_slogan` cannot be filled.

Generate ≥5 raw seats per hunt request. Then run the `SKILL.md` pipeline on each. Expect most to become `file_on` or drop. A hunt that emits five slogan keeps has failed.

Do not use closed-aisle leftovers as generation seeds (ntfy flags, ngrok companions, “add X to Veln”). That is prior-kill-as-rubric.

### 2.3 `references/search-playbook.md` (new; write now)

Incumbent extraction for a seat already restated.

Query construction:

- Use stack nouns + protocols: `wire protocol proxy`, `eBPF tc filter`, `AST collision queue`, `DPOR interleaving test`, `merge queue scheduler`, `lockfile host enforcement`.
- Do not use value-prop queries: `"best AI testing tool"`, `"developer productivity automation"`.

Extraction rules:

- ≥5 named incumbents per candidate.
- Each row: name, verified URL, exact quote from docs/README, one seat-match label, leftover if this row were exact.
- Unverified or 404 → `NEED_EVIDENCE` on that row. No hallucinated products.

Stop condition: five verified rows or three independent 404/`NEED_EVIDENCE` rows, whichever comes first. If evidence is thin, the candidate’s `claim_hygiene` is `unsourced` and `as_company` must not be Sparse/Greenfield-keep.

### 2.4 `references/deny-patterns.md` (port + fallback)

Port collapse modes from vendor `deny-patterns.md` when it exists.

Always include:

1. **ADR pointer.** If `docs/adr/0001-no-pitchable-candidate.md` exists in the target workspace, its killed-seats tables are authoritative (`deny_catalog: local_adr_0001`).
2. **Collapse modes** (from original plan inspection; confirm against vendor): file-on-incumbent, add-ecosystem-to-Veln, sidecar-without-host-enforcement.
3. **Short embedded fallback** (not a shadow ADR). Use only when ADR 0001 is absent (`deny_catalog: embedded_baseline`). Seed list, to be replaced when ADR is vendored:
   - Phone notifiers for local/CI tasks (ntfy, Pushover)
   - Localhost tunnels and OAuth companions (ngrok, Cloudflare named tunnels, Dev Tunnels)
   - Worktree loopback isolation (silo)
   - Sidecar locks without host enforcement
4. **`deny_catalog: incomplete`** only if vendor deny file, ADR 0001, *and* this fallback are all missing. That is not the happy path.

Do not condense ADR 0001 tables into this file as the working catalog (PR #7 prior-kill-as-rubric).

### 2.5 `references/rubric.md` and `references/seat-match.md` (port only)

Copy from `vendor/pitch-rate/references/`. Adapt nothing except relative links.

Do not add `obsolete` or `price_packaging` unless those strings exist in the vendor file.

Do not paste Plan 2’s auto-reject list into the skill as if it were ADR 0001.

### 2.6 `references/calibration.md` (port only)

Copy from vendor. Expected cases from original inspection (confirm, do not invent replacements):

- SymMerge (ADR 0002) — Gold KILL: a bundle of occupied slices is Occupied, not Sparse.
- TenantScale — Gold claim-kill: kill the physical claim; re-score real cutover slices.
- SagaGuard (ADR 0003) — exact vs `adjacent_pain` (proxy slice vs orchestration).
- False exact / wrong object cases from PR #8.
- Steelman discipline: ceiling 5–6 cannot publish exact 8–9 without new named rows.

Load on demand at `SKILL.md` step 8, not before search.

### 2.7 `references/output-template.md` (finder card; write now)

Headline is a **candidate**, not a rater `decision`. No overall `/100`. Seat-match enum stays at the four vendor labels until vendor adds more.

```yaml
candidate_seat: <one-line stack position>
v1_as_shipped: <concrete v1 and stack placement>
entry: generated | restated

verdicts:
  as_company: <Greenfield|Sparse|Occupied|Saturated> <0-10>
  as_oss:     <Greenfield|Sparse|Occupied|Saturated> <0-10>
  as_plugin:  <Greenfield|Sparse|Occupied|Saturated> <0-10>

density_scores:
  problem_density: <0-10>          # counts adjacent_pain
  exact_mechanics_density: <0-10>  # exact only; <= steelman.occupancy_ceiling

incumbents:
  - name: <tool>
    url: <verified URL>
    quote: "<docs/README quote>"
    seat_match: exact | adjacent_pain | language_scoped | wrong_substrate
    leftover: <what is missing if this row is exact>

auto_rejects_fired: []            # ids from vendored rubric.md
falsification:
  1_vacant_process: pass | fail
  2_not_a_wrapper: pass | fail
  3_mechanical_gap: pass | fail

steelman:
  occupancy_ceiling: <0-10>
  why_build: "<strongest case for building>"

claim_hygiene: ok | unsourced | implausible
file_on: <incumbent repo/issue URL, or none>
deny_catalog: local_adr_0001 | embedded_baseline | incomplete
pitch_rate: <not_run | compose_next>   # never inlined; reminder only
```

---

## 3. Validation

Fail the build if any of these fail.

1. **Frontmatter and links.** `name: profinder` parses; every relative path in `SKILL.md` resolves.
2. **Progressive disclosure.** `SKILL.md` does not contain density-band tables, auto-reject lists, or calibration anecdotes. Those live in `references/`.
3. **No verify mode.** Grep `SKILL.md` for dual-mode / `PITCH | KILL` headline procedure. Must be absent. Composition sentence pointing at `pitch-rate` is allowed.
4. **Port hygiene.** `rubric.md` / `seat-match.md` / `calibration.md` are copies of vendor files (or the build is still `NEED_EVIDENCE` and those files are absent). A reconstructed Plan 2 rubric is a fail.
5. **Known file-on:** ntfy `--wait-cmd` as a restated seat → `file_on` set, `as_company` Occupied/Saturated, auto-reject from vendored rubric fires. Not a hunt-generation seed.
6. **Steelman ceiling:** one restated Sparse *claim* must not publish `exact_mechanics_density` above the pre-search ceiling without new named rows.
7. **Hunt dry-run (the missing original test):** from `seat-generation.md`, generate ≥5 seats. Each must have substrate + named process. Each must collect ≥5 incumbent attempts (verified or `NEED_EVIDENCE`). Most cards must be `file_on` or Occupied/Saturated `as_company`. Fail if any keep is a slogan with no stack noun. Fail if generation uses closed-aisle leftovers as seeds.

OpenCode/Claude load check: skill discovers from repo-root `SKILL.md`. Out of scope to require a live OpenCode binary in this workspace; if present, run one hunt prompt and keep the transcript next to the dry-run.

---

## 4. Explicit non-goals

- Dual-mode `hunt | verify`. That files this skill onto `pitch-rate` (auto-reject 5).
- Scoring PR process / hygiene.
- People-finder references.
- Mandatory load of every reference on every run.
- Authoring ADR 0001 inside this repo as a condensed kill list.
- Six-label seat-match unless the vendor patch already has it.
- Shipping the skill before `vendor/pitch-rate/` exists, except the scaffold files listed in §0.

---

## 5. Done when

- `vendor/pitch-rate/` contains PR #8 files + SHA in `vendor/README.md`.
- `SKILL.md` + seven references exist as specified.
- Validation §3 items 1–7 pass (item 7 transcript checked in).
- A hunt pass can be composed into `pitch-rate` without this skill emitting a rater headline.
