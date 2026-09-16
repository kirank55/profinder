# Plan1: build `profinder` skill (mirroring PR #8 `pitch-rate`)

## 0. Evidence (read-only, already gathered)

- Workspace `C:\Users\kiran\code\p\profinder` is empty — greenfield target.
- PR #8 (`kirank55/llmresearch`, private, web 404) inspected via local clone `C:\Users\kiran\code\p\llmresearch` + `gh pr view/diff`:
  - Title: `Add pitch-rate Pi skill for occupancy-based idea verification`, branch `cursor/pitch-rate-skill-bd8d` → `main`, DRAFT.
  - 6 files, +355: `.pi/skills/pitch-rate/SKILL.md` (62 lines) + `references/rubric.md` (81), `seat-match.md` (47), `deny-patterns.md` (41), `calibration.md` (74), `output-template.md` (50). Full patch captured in prior session.
  - Design: procedure-only `SKILL.md`, load references on demand, verdicts `PITCH | KILL | NEED_EVIDENCE | FILE_ON_X`, no `/100`. Encodes ADR 0001 density bands + PR #7 failure modes (wrong object, score-first, category collapse, prior-kill-as-rubric).
- Reusable context: `llmresearch/docs/adr/0001-no-pitchable-candidate.md` (deny-list source of truth), `0002-symmerge…`, `docs/pitch_memo.md`, `docs/progress.md`, plus `0003-sagaguard…` / `0004-tenantscale…` on other branches for calibration.
- User choices: same pattern as PR #8, OpenCode/Claude format, built in empty `profinder/` folder.

## 1. Target layout in `C:\Users\kiran\code\p\profinder\`

```text
profinder/
  plan1.md                      # this file
  SKILL.md                      # procedure only; load references on demand (OpenCode/Claude frontmatter)
  references/
    rubric.md                   # port from pitch-rate rubric.md
    seat-match.md               # port from pitch-rate seat-match.md
    deny-patterns.md            # port + condensed ADR 0001 tables
    calibration.md              # SymMerge, SagaGuard, TenantScale, false-exacts
    output-template.md          # finder output block (candidate, not verdict)
```

Direct translation of PR #8's `.pi/skills/pitch-rate/` tree to a standalone skill dir (`SKILL.md` at root works for both OpenCode and Claude; no `.pi/` prefix, no extension/orchestrator/hunter loop).

## 2. Build steps (future build mode work, not done here)

1. **Scaffold `SKILL.md`:**
   - Frontmatter: `name: profinder`, `description:` e.g. "Find sparse developer-tool/SaaS seats worth pitching. Use when asked to find, hunt, or propose product ideas. Searches mechanics, names incumbents with URL+quote, scores density."
   - Mirror PR #8 `SKILL.md` Sections 1-6 but invert job: `pitch-rate` verifies a given idea; `profinder` *finds* seats: restate seat -> load refs -> steelman ceiling -> search mechanics -> seat-match + dual-score -> gates -> emit candidate block.
   - Keep constraints: no repo writes by default, read refs from memory forbidden, no `/100`, cite unread files as `NEED_EVIDENCE`.
2. **Port 5 references** from PR #8 patch verbatim as starting point, then adapt:
   - `rubric.md`, `seat-match.md`: keep as-is (density bands Saturated 8-10 / Occupied 5-7 / Sparse 2-4 / Greenfield 0-1, auto-rejects, falsification, exact vs adjacent_pain vs language_scoped vs wrong_substrate).
   - `deny-patterns.md`: keep collapse modes (file-on-incumbent, add-ecosystem-to-Veln, sidecar-without-host-enforcement) + add pointer: if consumer repo has `docs/adr/0001…`, treat its killed-seats as authoritative; else `deny_catalog: incomplete`.
   - `calibration.md`: keep Gold KILL / claim-kill / false-exact / wrong-object cases.
   - `output-template.md`: change from rating verdict to finder candidate (`seat`, `v1_as_shipped`, `incumbents[5+]`, `as_company/as_oss/as_plugin`, `falsification`, `file_on`, `deny_catalog`).
3. **Validate:** frontmatter parses, all relative links resolve, skill loads in OpenCode, dry-run on one known-KILL seat (e.g. ntfy `--wait-cmd`) -> expect `FILE_ON_X`, and one known-Sparse claim -> check steelman <= exact discipline holds.

## 3. Open decision

Assumed: `profinder` = complementary idea-*finder* (hunt sparse seats) vs `pitch-rate` = idea-*rater*. If instead GitHub-profile / freelancer / professor finder is meant, `references/` content changes completely (API + schema + output template), though `SKILL.md` skeleton stays the same.
