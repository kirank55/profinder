---
name: niche-saas-finder
description: >
  Find sparse vertical-workflow SaaS seats by niching ICP plus system of
  record first, then generating workflow positions, naming incumbents with
  URL plus quote, and scoring occupancy density. Fail closed: as_company
  defaults to Occupied or file_on; Sparse/Greenfield company keeps must
  pass keep-gate (literal quotes, SaaS search classes, no occupied bundle).
  Use when asked to find, hunt, or propose vertical SaaS ideas in a named
  industry or SoR (dental, law, home service, restaurant, clinic, Clio,
  Eaglesoft, Toast, ServiceTitan). Broad "SaaS idea" prompts with no SoR
  must be grilled into named ICP plus SKU/host before generation or search;
  do not invent a niche. Do not use for developer-tool or infrastructure
  seats. Abort if the request is people-search (GitHub profiles,
  freelancers, professors). Do not use this skill to rate an
  already-chosen idea when an idea-rater is the requested job.
---

# Niche SaaS finder

Propose and document vacant **vertical workflow** SaaS seats. Score
**occupancy**, not pain. Pain is abundant. Empty seats are not.

A candidate niche is `icp + system_of_record + workflow_step`, all named
nouns. Interest (`dental`, `law`) is input, never a niche, never a score.

This skill is self-contained under `skills/niche-saas-finder/`. Load
only files in this tree. Do not load sibling or parent `references/`
(devtools playbooks, kernel keep-gate, deny-pattern aisles).

## Constraints (every run)

- No repo writes by default.
- Do not score from memory. Load the cited reference file or emit `NEED_EVIDENCE`.
- No overall `/100`. No TAM or WTP as occupancy.
- Never inline rubric tables into `SKILL.md`.
- Load references **on demand by step**, not as a mandatory full stack. Do not load [intake-saas.md](references/intake-saas.md) unless step 2 needs the scope gate. Do not load [seat-generation-saas.md](references/seat-generation-saas.md) or [search-playbook-saas.md](references/search-playbook-saas.md) before that gate passes. Do not load [search-playbook-saas.md](references/search-playbook-saas.md) before a seat exists.
- Scoring files are not optional. Load [calibration-saas.md](references/calibration-saas.md) before the first 0-10 score. Load [gate-bind-saas.md](references/gate-bind-saas.md) before any `as_company` Sparse/Greenfield. Do not skip because the keep "looks clear." Gate-bind **is** the keep latch; do not load a parent `keep-gate.md`.
- Quotes are contiguous substrings of a page fetched this run. Paraphrase is `NEED_EVIDENCE`.
- `as_company` **defaults to Occupied or `file_on`**. A Sparse/Greenfield company keep is fail-closed and requires `keep_gate: pass`.
- No Sparse/Greenfield keep counts without a passing run of [keep-proof-check.py](references/keep-proof-check.py) on the card as written. A failing check is `keep_gate: fail`, not an invitation to relabel rows until it passes.
- Object is a **workflow seat on a named SoR**, never PR hygiene. If the user pastes a PR process question, abort that object.
- User-supplied niche, unique data, and "nobody does this" scope generation. They are not occupancy evidence and do not replace incumbent URLs.
- Never load files outside this tree (parent `search-playbook.md`, `intake.md`, `keep-gate.md`, `deny-patterns.md`, kernel calibration). Loading a devtools playbook is a G2 / procedure fail. Kernel worked examples (Landlock, Kroxylicious, `CREATE PUBLICATION`) on a SaaS card are a card fail.
- Card schema is SaaS-only. Hybrid `niche_icp`, or `search_classes` keys `host_primitive` / `dropin_cli` / `orchestrator`, is a card fail. Use [output-template-saas.md](references/output-template-saas.md).
- A marketplace app is class-2 `exact` only after the write-time consult test in [gate-bind-saas.md](references/gate-bind-saas.md). Else auto-reject 7 or `NEED_EVIDENCE`.
- A SoR "no dedicated module" / "manual step" / "custom report" quote is class-1 occupancy of the workaround on that page, not vacancy. Finish class 2-3 before scoring. Two SoR-help rows forbid `keep_gate: pass`. A tracker name without an emitted card is not a keep.

## Procedure

1. **Abort checks.** People-finder (GitHub profiles, freelancers, professors) -> stop; wrong skill, do not reuse these references. Request is "rate this idea / ADR" -> that is a rater job: hand off to an idea-rating skill or workflow (`rate_next`); optionally continue only as restatement of a seat into a candidate card, never as a rater verdict. Developer-tool / infrastructure hunt -> stop; wrong skill.

2. **Choose entry / scope gate.** A slogan is not a seat. Do not generate or search until `icp` and `system_of_record` are named nouns, or the user opted out, or a named seat restates without slogans.
   - User named a seat or pasted an ADR/idea that already restates as `candidate_seat` + `v1_as_shipped` + named ICP + SoR SKU/host + workflow step without slogans -> go to step 4 (restate), then 3, then 5-9 on that one seat. Do not load intake. Deny does not run before a one-line seat exists.
   - User named a seat that cannot be restated without slogans ("dental SaaS", "AI for law") -> treat as an incomplete hunt. Load [intake-saas.md](references/intake-saas.md). Do not drop at restatement to skip grilling.
   - User named a restatable seat but `v1_as_shipped` or SoR SKU/host is missing -> load [intake-saas.md](references/intake-saas.md) (named-seat branch), ask only those blanks, then step 4. Do not search until restatable.
   - User asked to find / hunt / propose seats -> load [intake-saas.md](references/intake-saas.md). If `icp` or `system_of_record` is unset and the user did not opt out, emit the intake card and **stop**. Do not load seat-generation or search-playbook. Do not invent a niche.
   - Hunt with user niche minimum (named ICP + SoR), or explicit "pick a stack" opt-out -> load [seat-generation-saas.md](references/seat-generation-saas.md), produce >=5 raw seats **inside that niche**, each with a named `workflow_step`, **then** map steps 3-9 over each. Do not deny-check before generation. On `agent_opt_out`, pick **exactly one** seed-SoR row via that file's interest routing. Apply its aisle-switch rule (class-1/2 switch hosts in that table, not the calibration false keeps) instead of five more Occupied cards.

3. **Deny check.** Skip until a restated one-line seat exists. Load [gate-bind-saas.md](references/gate-bind-saas.md). If the target workspace keeps a local killed-seats file, that file wins (`deny_catalog: local_*`). Else use the SaaS embedded fallback (`deny_catalog: embedded_saas_baseline`). If both missing, `deny_catalog: incomplete` and do not emit an `as_company` keep — this is not the happy path on a correct install of this skill. Confirm the candidate's one-line seat against those rows before scoring.

4. **Restate.** One-line `candidate_seat`, concrete `v1_as_shipped`, named `workflow_step`, named `system_of_record`. Copy `niche` from intake (named-seat path may derive it from the restatement; `source: user`). If intake `workflow_step` was unset, fill it from this seat. Search never runs with `workflow_step: unset`. If **this candidate** cannot be stated without slogans ("dental SaaS"), drop the seat. If the *user request* is still a slogan, return to step 2; do not end the hunt by dropping. Drop if it ignores SoR or matches `hard_nos`.

5. **Steelman ceiling.** Strongest case a skeptical founder would still build this. Occupancy ceiling 0-10 **before** search. If `v1_as_shipped` joins two or more mechanisms with "and", list those **slices** first; the ceiling is at least the densest occupied slice. Published `exact_mechanics_density` must not exceed this ceiling unless new named incumbent rows appear.

6. **Search incumbents.** Load [search-playbook-saas.md](references/search-playbook-saas.md) only. Hit all four SaaS query classes, then collect >=5 incumbents, each with name, URL fetched this run, contiguous-substring quote, seat-match label, leftover. 404, unverified fetch, or paraphrase -> that row is `NEED_EVIDENCE`; do not invent. Do not stop at five adjacent logos or five Capterra listings. Do not stop because class 1 admitted a gap; run class 2 marketplace and class 3 commercial SKU queries for **this** step. Apply the write-time consult test before labeling a marketplace app `exact`.

7. **Seat-match + dual-score.** Load [calibration-saas.md](references/calibration-saas.md) (before the first 0-10), then [seat-match.md](references/seat-match.md), then [rubric.md](references/rubric.md). Apply [gate-bind-saas.md](references/gate-bind-saas.md) seat-match notes: SKU mismatch is `wrong_substrate`, not `language_scoped`; fetched G2/Capterra listings are `adjacent_pain`, never `exact`. One label per incumbent; strictest mismatch wins. `problem_density` counts `adjacent_pain`; `exact_mechanics_density` counts `exact` only and must be <= steelman ceiling.

8. **Gates.** Apply auto-rejects and falsification from [rubric.md](references/rubric.md) **as remapped in** [gate-bind-saas.md](references/gate-bind-saas.md). Load gate-bind only (it is the keep latch). G2 classes are those in [search-playbook-saas.md](references/search-playbook-saas.md). A Sparse/Greenfield `as_company` keep requires `keep_gate: pass`. On `keep_gate: fail`, emit Occupied / `file_on` / `drop` as the company verdict even if leftover prose is eloquent.

9. **Latch, then emit.** Before emitting `as_company` Sparse/Greenfield, verify the latch against the card **as written**, in this order: (a) `search_classes` holds all four keys and every incumbent row carries `found_via` naming the class that produced it, with every class hitting >=1 row; (b) >=5 incumbent rows and >=4 distinct URLs, or an explicit could-not-find-5 plus why; (c) zero `NEED_EVIDENCE` rows; (d) `file_on` is set whenever any leftover names a host; (e) falsification 1/2/3 each cite the rows that decide them, and `1_vacant_process` passes only with no `exact` row on any slice. First failure -> `keep_gate: fail`, company verdict Occupied / `file_on` / `drop`, no discretion, no prose override. Then emit the candidate card from [output-template-saas.md](references/output-template-saas.md), including the `niche` block, `slices`, `search_classes`, `keep_gate`, and the `keep_proof` block. Split `as_company` / `as_oss` / `as_plugin`. Do not emit a headline rater decision (that belongs to a rater, not the finder). Finder disposition is the split verdicts plus `file_on` plus `claim_hygiene` plus `keep_gate`. Do not emit this card when step 2 stopped on `intake_blocked`. Do not count a tracker bullet as a keep unless this card was emitted.
