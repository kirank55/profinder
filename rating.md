# Rating: `plan1.md` vs `plan2.md`

Object rated: two **implementation plans** for a `profinder` Agent Skill, not two company pitches and not Cursor product SKUs.

These `/100` numbers are **plan-quality** (would you execute this spec). They are not occupancy density and must not be copied into the skill as an idea score. Occupancy verdicts stay `PITCH | KILL | NEED_EVIDENCE | FILE_ON_X` with no overall `/100`.

Source files: `plan1.md` (commit `4862514`, "ms"), `plan2.md` (commit `d140b58`, "gf"). This workspace cannot read `kirank55/llmresearch` (GitHub: repository not resolvable), so every claim that depends on PR #8's exact patch is `NEED_EVIDENCE`.

---

## Score /100

| Plan | Score | Occupancy decision |
|---|---|---|
| **Plan 1** | **70 / 100** | `FILE_ON_X` + `NEED_EVIDENCE` |
| **Plan 2** | **49 / 100** | `KILL` |
| Recommended merge (Plan 1 skeleton + Plan 2 grafts, still missing seat generation) | **84 / 100** | `PITCH` as oss skill spec |

Weighted rubric (same 100 points for each plan):

| Gate | Weight | Plan 1 | Plan 2 |
|---|---|---|---|
| One job / object hygiene | 20 | 18 | 6 |
| Source fidelity (port, don't invent) | 15 | 14 | 7 |
| Skill craft / progressive disclosure | 15 | 14 | 5 |
| Implementable in this repo | 15 | 4 | 13 |
| Hunt-specific completeness | 15 | 6 | 10 |
| PR #7 self-consistency | 10 | 9 | 2 |
| Validation / dry-runs | 10 | 5 | 6 |
| **Total** | **100** | **70** | **49** |

Plan 1 loses 26 points for being unbuildable here (no PR #8 patch) and for having no search playbook or seat-generation procedure. Plan 2's 49 is a completeness score dragged down by dual-mode, inlined rubric, and mandatory full-ref load — salvageable pieces are already counted in hunt completeness and implementability.

---

## Verdict

**Execute Plan 1's shape. Do not execute Plan 2 as written.**

| Plan | /100 | Decision | Why |
|---|---|---|---|
| **Plan 1** | 70 | `FILE_ON_X` + `NEED_EVIDENCE` | Correct complementary job (hunt seats; leave rating to `pitch-rate`). Unbuildable here because the PR #8 patch it wants to port is not in this repo. |
| **Plan 2** | 49 | `KILL` | Dual-mode collapses finder and rater into one object, files verify-mode onto `pitch-rate`, inlines the rubric (score-first), and mandates loading every reference — the failure modes Plan 1 says PR #7 already killed. |

**v1 to ship:** Plan 1 skeleton (procedure-only `SKILL.md`, finder-only, refs on demand) plus three grafts from Plan 2: `references/search-playbook.md`, an embedded deny-catalog **fallback** (not a replacement for ADR 0001), and the finder fields of Plan 2's YAML card. Drop dual-mode `verify`, drop `decision:` as a rater verdict on hunt output, drop mandatory full-ref load.

---

## Steelman (strongest case for each)

**Plan 1.** A skeptical founder would write a thin port: `pitch-rate` already verifies a given idea; the missing job is *finding* vacant stack seats. Copy the five references, invert the procedure, change the output from a verdict to a candidate, keep PR #7 constraints (no `/100`, no memory-as-rubric, cite unread files as `NEED_EVIDENCE`). Don't invent taxonomy. Flag that `profinder` might mean people-search instead of seat-search before burning the wrong references.

**Plan 2.** A skeptical founder would refuse a skill that only works if a private `llmresearch` clone is on disk. Embed the deny list, specify every file so an agent can write it from the plan, add a search playbook (the thing a finder actually needs), and let one skill both hunt and verify so the user does not juggle two installs.

Plan 2's steelman is real on **portability** and **search**. It does not justify **absorbing the rater**. That leftover is a flag on `pitch-rate`, which Plan 1 already named.

Occupancy ceiling for Plan 2's dual-mode claim: **5–6 (Occupied)** — "add hunt mode to the existing rater." Published exact-mechanics cannot exceed that without a new named substrate. None is proposed (still `SKILL.md` + markdown refs).

Occupancy ceiling for Plan 1's finder-only claim: **3–4 (Sparse)** — occupancy-first *hunt* of stack mechanics is not a named shipped skill among public incumbents below; verify is occupied.

---

## Shared seat (what both plans would build)

Both plans assume `profinder` = occupancy-gated hunter of developer-tool / infra **seats**, encoding ADR 0001: score existing-solution density, not pain.

Plan 1 leaves an open fork: GitHub-profile / freelancer / professor finder would replace `references/` entirely. Plan 2 silently closes that fork. Until the name is pinned, any build is one wrong-object turn away from a different product.

**Split verdicts for the skill itself (not the plans):**

| Slice | Band | Action |
|---|---|---|
| `as_company` | Saturated / auto-reject 2 | A markdown skill is not a company. |
| `as_oss` (finder-only occupancy hunter) | Sparse 2–4 | Possible `PITCH` as a bounded skill, if hunt generation is specified. |
| `as_plugin` / file-on `pitch-rate` (verify mode) | Occupied 6 | `FILE_ON_X`. Plan 2's verify path is this slice. |

Falsification of the *finder* slice:

1. Vacant process — occupancy-first generation of stack seats, not pain brainstorming: **pass** (no public incumbent does this as the headline UX).
2. Not a 50-line wrapper — **fail** as a company; **pass** as a skill (the unit of work *is* procedure + refs).
3. Mechanical gap with ≥3 named incumbents — **pass**: public hunters score pain/market/moat or emit `/10` blends; they do not apply Saturated / Occupied / Sparse / Greenfield + seat-match labels.

---

## Incumbents (named, fetched, quoted)

Each row is one label. Stricter mismatch wins.

| Name | URL | Quote | Seat-match | Leftover vs proposed `profinder` |
|---|---|---|---|---|
| **pitch-rate** (llmresearch PR #8) | private; this token cannot resolve `kirank55/llmresearch` | Plan 1: "`pitch-rate` verifies a given idea; `profinder` *finds* seats"; verdicts `PITCH \| KILL \| NEED_EVIDENCE \| FILE_ON_X`, no `/100` | `exact` for Plan 2 **verify**; `adjacent_pain` for Plan 1 **hunt** (reactive vs proactive) | Hunt. Plan 2's dual-mode leftover is "add hunt to this skill." Contents: `NEED_EVIDENCE`. |
| **startup-idea-validator** | https://github.com/mohitagw15856/pm-claude-skills/blob/main/skills/startup-idea-validator/SKILL.md | "Pressure-test a startup idea the way a sharp investor or co-founder would — problem, market, wedge, moat, why-now" | `adjacent_pain` | Occupancy bands, seat-match taxonomy, `FILE_ON_X`. Scores pain. Verdict is Promising / Reconsider. |
| **idea-generator** | https://github.com/rshankras/claude-code-apple-skills/blob/main/skills/product/idea-generator/SKILL.md | "Overall Score = weighted average on 1-10 scale (Solo Dev Scope and Technical Fit weighted 1.5x)." Competition is one of five blended dimensions. | `adjacent_pain` (also `language_scoped` to Apple apps) | Mechanics-first stack search; no `/100`; occupancy as the *only* score. This is the public **hunt** incumbent, and it is slogan/pain/feasibility-first. |
| **startup-design / startup-competitors** | https://github.com/ferdinandobons/startup-skill | "If your idea should die, it will tell you." Battle cards, feature matrices, go/no-go. | `adjacent_pain` | Stack-seat occupancy + exact-mechanics density. Kills on market/strategy, not on named exact UX already shipping. |
| **Agent Skills spec** | https://agentskills.io/specification | "Resources (as needed): Files … are loaded only when required." "Keep your main `SKILL.md` under 500 lines." | `wrong_substrate` | Format, not a finder. Both plans correctly target `SKILL.md` + `references/`. Plan 2 then violates the load rule. |

`problem_density` (counts adjacent): **7 (Occupied)** — idea hunt/validate skills are a crowded aisle.

`exact_mechanics_density` (occupancy-first, seat-match, no `/100`, ≥5 incumbents with URL+quote): **2–3 (Sparse)** for hunt; **8–9 (Saturated)** for verify if PR #8 is what Plan 1 says it is (`NEED_EVIDENCE` on the patch).

---

## Plan 1 card

```yaml
candidate_seat: "Standalone Agent Skill that hunts sparse dev-tool/infra seats by porting pitch-rate refs and inverting the job from rate → find"
decision: FILE_ON_X          # file the complementary hunt on pitch-rate; do not absorb it
# also NEED_EVIDENCE         # PR #8 patch + ADR 0001 tables not in this workspace

verdicts:
  as_company: Saturated 9    # markdown skill
  as_oss: Sparse 3           # finder-only port is the right oss unit
  as_plugin: Occupied 6      # honest leftover is a sibling skill next to pitch-rate

density_scores:
  problem_density: 7
  exact_mechanics_density: 3  # <= steelman ceiling 4
  steelman_ceiling: 4

auto_rejects_fired: []       # as a *plan*, none fatal; as a company, rule 2
falsification:
  1_vacant_process: pass     # hunt, not verify
  2_not_a_wrapper: fail      # still a skill
  3_mechanical_gap: pass     # inversion + candidate output, if search is specified later

claim_hygiene: unsourced     # depends on a private PR not present here
file_on: "kirank55/llmresearch#8 pitch-rate (unreachable from this workspace)"
deny_catalog: incomplete
```

### What Plan 1 gets right

- **One object.** Finder, not finder+rater. Matches the PR #7 "wrong object" constraint it cites.
- **Procedure-only `SKILL.md`, refs on demand.** Matches Agent Skills progressive disclosure.
- **Port, then adapt** — does not reconstruct ADR 0001 from memory. Plan 1's taxonomy is four labels (`exact`, `adjacent_pain`, `language_scoped`, `wrong_substrate`). Plan 2 adds `obsolete` and `price_packaging` without a source cite.
- **Names the naming trap.** If `profinder` is a people-finder, these references are the wrong product.
- **Constraints that prevent score-first:** no repo writes by default, no scoring from memory, no `/100`, unread files → `NEED_EVIDENCE`.
- **Validation intent** is the right kind: known-KILL (`ntfy --wait-cmd` → `FILE_ON_X`) plus steelman-ceiling discipline on a Sparse claim.

### What Plan 1 fails as a build spec

- **Not implementable in this repo.** Steps are "port five files from PR #8 verbatim." `gh repo view kirank55/llmresearch` does not resolve. No patch, no `docs/adr/0001`, no calibration ADRs. The plan itself would have to emit `NEED_EVIDENCE` and stop.
- **Hunt is underspecified.** Inverting sections 1–6 of a rater does not produce a search procedure. There is no playbook for *generating* candidate seats (stack nouns, query construction, when to stop). That is the actual new file.
- **Deny catalog is non-portable.** "If consumer repo has ADR 0001, use it; else `deny_catalog: incomplete`" is honest, but a standalone `profinder/` skill that always reports incomplete is a skill that cannot kill closed aisles.
- **Build steps are a file list**, not a sequence that would catch category collapse (no hunt dry-run: generate N seats, expect most `FILE_ON_X` / `KILL`).

---

## Plan 2 card

```yaml
candidate_seat: "Dual-mode hunt+verify skill that reconstructs pitch-rate in-tree, embeds a deny catalog, and adds a search playbook"
decision: KILL

verdicts:
  as_company: Saturated 9
  as_oss: Occupied 6         # verify half is pitch-rate; hunt half is a plugin on it
  as_plugin: Occupied 7      # FILE_ON pitch-rate, plus add-ecosystem

density_scores:
  problem_density: 7
  exact_mechanics_density: 6  # = steelman ceiling 6; dual-mode cannot honestly go lower
  steelman_ceiling: 6

auto_rejects_fired:
  - 1  # named incumbent (pitch-rate) already ships verify UX
  - 5  # remaining wedge is "add hunt to incumbent X"
falsification:
  1_vacant_process: fail     # verify process is occupied; hunt process is not specified as vacant generation
  2_not_a_wrapper: fail
  3_mechanical_gap: fail     # leftover is a flag/mode, not a new substrate

claim_hygiene: implausible   # reconstructs 7 auto-rejects + 6-label taxonomy as if they were the source of truth
file_on: "pitch-rate verify path; steal search-playbook only"
deny_catalog: embedded_baseline  # and this is the PR #7 prior-kill-as-rubric risk
```

### What Plan 2 gets right (salvage)

- **`search-playbook.md` is the missing hunt file.** Stack nouns + protocols, ban value-prop queries, ≥5 incumbents, URL + quote, 404 → `NEED_EVIDENCE`. Plan 1 has no equivalent.
- **Portability.** An embedded closed-aisle *fallback* when ADR 0001 is absent is required for a standalone repo. Use it as `deny_catalog: embedded_baseline`, never as a license to stop reading a local ADR 0001.
- **Finder YAML fields** (`candidate_seat`, `v1_as_shipped`, incumbents with `leftover`, split `as_company` / `as_oss` / `as_plugin`, steelman ceiling, `claim_hygiene`) are a better candidate card than Plan 1's one-line "change the output template."
- **Named dry-runs beyond ntfy:** SymMerge bundle → Occupied is the right calibration for "bundle of occupied slices ≠ Sparse."
- **Self-contained enough to write files without PR #8** — valuable in *this* workspace, which cannot see llmresearch.

### Why Plan 2 is `KILL` as specified

Plan 1's own PR #7 list: wrong object, score-first, category collapse, prior-kill-as-rubric. Plan 2 commits all four.

1. **Wrong object / category collapse.** Mode is `hunt | verify`. Object is `idea | adr | pr_process` with a note "never mix PR hygiene with idea viability" — then the same skill accepts all three. Output mixes rater `decision: PITCH|KILL|…` with finder `candidate_seat`. That is two products in one schema.
2. **File-on-incumbent (auto-reject 5).** Verify mode *is* `pitch-rate`. Dual-mode is "add hunt to Veln." The complementary skill Plan 1 described is the honest leftover: a second skill, not a second mode.
3. **Score-first.** Section 2 pastes density bands, 7 auto-rejects, 6-label taxonomy, and a full YAML card into the plan. An implementer who copies that into `SKILL.md` produces the opposite of "procedure only; load references on demand." The skill's scoring logic must live in `references/`, sourced from ADR 0001 / PR #8, not from this plan's memory.
4. **Prior-kill-as-rubric.** "Closed Aisles (Embedded Catalog)" condenses killed seats into the working deny list. Plan 1 warned this is a known failure mode. Embed a *pointer + short fallback*, not a shadow ADR.
5. **Progressive-disclosure violation.** "Load in mandatory order (`rubric.md` → … → `search-playbook.md` → `output-template.md`)" plus "always read `calibration.md` before any score" loads every reference on every run. The spec says resources load **as needed**. Verify should not load `search-playbook.md`. Hunt should not reload calibration anecdotes before a single incumbent exists.
6. **Taxonomy drift.** Plan 1 (closer to the port) has four seat-match labels. Plan 2 adds `obsolete` and `price_packaging`. Those may be good labels; they are not a port. Shipping them without the source patch is how category collapse starts.
7. **Hunt generation still missing.** The playbook extracts incumbents *of a seat already in hand*. It does not say how vacant seats are proposed (repo archaeology, protocol gaps, CI scheduler nouns, etc.). Plan 2 is still a rater with a search preamble.
8. **Noise that would leak into the skill:** `$0\text{--}10$` LaTeX, unexplained "Antigravity" target, build steps that are "write the files."

---

## Head-to-head (plan quality, not occupancy)

Totals: **Plan 1 = 70 / 100**, **Plan 2 = 49 / 100**. Point breakdown is in [Score /100](#score-100).

| Gate | Plan 1 | Plan 2 | Winner |
|---|---|---|---|
| One job | Hunt only | Hunt + verify | Plan 1 |
| Matches Agent Skills load rules | On demand | Mandatory full load | Plan 1 |
| Faithful to claimed source | Port verbatim | Reconstruct + extra labels | Plan 1 |
| Buildable in *this* empty repo | No (PR #8 missing) | Yes | Plan 2 |
| Search / hunt procedure | "Search mechanics" one-liner | `search-playbook.md` | Plan 2 |
| Deny list when ADR 0001 absent | `incomplete` (honest, weak) | Embedded catalog (portable, risky) | Tie — need fallback *and* ADR-wins |
| Output schema | "Finder candidate block" (thin) | Full YAML, but mixed objects | Plan 2 fields, Plan 1 object |
| Names unresolved product fork | Yes (people-finder vs seat-finder) | No | Plan 1 |
| Self-consistency with PR #7 | Encodes the modes | Commits the modes | Plan 1 |
| Validation | ntfy + Sparse steelman | ntfy + SymMerge | Plan 2 (narrowly) |
| Dry-run of **hunt** | Missing | Missing | Neither |

---

## Recommended v1 (merge, don't pick a loser to run whole)

Keep Plan 1 as the architecture. Graft, don't dual-mode.

```text
profinder/
  SKILL.md                      # procedure only; hunt-only; load refs on demand
  references/
    rubric.md                   # port from pitch-rate / ADR 0001 when available
    seat-match.md               # four labels until the PR #8 patch is in-tree
    deny-patterns.md            # collapse modes + ADR 0001 pointer + short embedded fallback
    search-playbook.md          # from Plan 2 (incumbent extraction)
    calibration.md              # from pitch-rate; include SymMerge / ntfy / false-exacts
    output-template.md          # Plan 2 YAML minus rater-only mixing
    seat-generation.md          # NOT in either plan; required for a finder
```

`SKILL.md` flow (finder only):

1. Restate the seat (or generate candidates — see gap below).
2. Load `deny-patterns.md`. If local `docs/adr/0001-no-pitchable-candidate.md` exists, it wins; else `deny_catalog: embedded_baseline`.
3. Steelman occupancy ceiling **before** search.
4. Load `search-playbook.md`. Collect ≥5 incumbents with URL + quote. 404 → `NEED_EVIDENCE`, do not invent.
5. Load `seat-match.md` + `rubric.md`. Dual-score. Exact-mechanics ≤ steelman ceiling unless new named rows appear.
6. Gates. Emit **candidate card**, not a `pitch-rate` verdict clone. Split `as_company` / `as_oss` / `as_plugin`. No `/100`.
7. Load `calibration.md` only when a label is on a boundary (bundle vs slice, claim-kill vs seat-kill, false exact).

**Do not** ship `verify` mode. If the user has `pitch-rate` installed, compose: hunt emits a candidate, user runs `pitch-rate` on it. If they don't, that is a packaging problem, not a reason to fork the rater into this repo.

### Gap neither plan closes

Neither plan specifies **seat generation**. Plan 2's playbook answers "how do I search incumbents for seat S?" The finder question is "how do I propose S?" Without that file, `profinder` is `pitch-rate` with a blank idea box. Treat `seat-generation.md` as blocking for any `PITCH` of the hunt slice.

### Blocking evidence

Before writing `rubric.md` / `seat-match.md` as a port:

- Need the PR #8 patch or a local `llmresearch` checkout (Plan 1's claimed source).
- Need ADR 0001 tables if they are the deny-list source of truth.
- Pin the product: **seat hunter** vs **people finder**. If people finder, discard both plans' `references/` and stop; this rating does not apply.

Until those exist, the honest skill output on a "build profinder from these plans" request is `NEED_EVIDENCE`, not a reconstructed rubric.

---

## Calibration notes (for this rating)

- **Bundle rule (SymMerge):** Plan 2 bundling hunt + verify is Occupied, not Sparse. Two jobs in one skill do not create a vacant seat.
- **Claim-kill (TenantScale):** Plan 2's claim "self-contained across OpenCode, Claude, Antigravity, and Pi" is a packaging claim. Kill the claim if any target needs a hardcoded `.pi/` tree; do not mark the hunt seat Occupied because of it.
- **Steelman discipline:** If dual-mode feels like a 3 (Sparse), the published score cannot be 3 while `pitch-rate` already ships verify. Ceiling is Occupied.
- **False exact:** Public idea-generator "Competition Density" is not `exact`. Different mechanics (blended `/10`, Apple-scoped, pain-first). Labeled `adjacent_pain` above on purpose.
