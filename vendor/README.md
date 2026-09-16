# vendor/pitch-rate

Copy of `kirank55/llmresearch` PR #8 (`pitch-rate`) used as the scoring-rule source of truth for `profinder`.

`profinder` hunts seats. `pitch-rate` rates ideas. Do not merge them. Port `rubric.md`, `seat-match.md`, `deny-patterns.md`, and `calibration.md` from here; do not reconstruct those files from memory or from `plan2.md`.

## Status

**Populated 2026-09-16.** Copied from `kirank55/llmresearch` PR #8 branch.

- PR: `kirank55/llmresearch#8`
- Branch: `cursor/pitch-rate-skill-bd8d`
- Commit SHA: `31fe44df9714f8ee37a370818b59d3ac5cd51486`
- Date copied: 2026-09-16
- Source paths: `.pi/skills/pitch-rate/SKILL.md` + `.pi/skills/pitch-rate/references/*.md`
- Dest: `vendor/pitch-rate/` (flattened copy; no `.pi/` prefix)

## How to populate (from a machine that can read llmresearch)

```bash
# example; adjust paths
git clone git@github.com:kirank55/llmresearch.git
cd llmresearch
git fetch origin cursor/pitch-rate-skill-bd8d
git checkout cursor/pitch-rate-skill-bd8d

DEST=<profinder>/vendor/pitch-rate
mkdir -p "$DEST/references"
cp .pi/skills/pitch-rate/SKILL.md "$DEST/"
cp .pi/skills/pitch-rate/references/*.md "$DEST/references/"
```

Then record:

- PR: `kirank55/llmresearch#8`
- Branch: `cursor/pitch-rate-skill-bd8d`
- Commit SHA: (paste)
- Date copied: (paste)

Expected files (from the original Plan 1 inspection; confirm):

- `SKILL.md`
- `references/rubric.md`
- `references/seat-match.md`
- `references/deny-patterns.md`
- `references/calibration.md`
- `references/output-template.md`
