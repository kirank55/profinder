---
name: pitch-rate
description: Rate whether a developer-tool or SaaS idea, ADR, or pitch is worth founding. Use when the user asks to rate, score, verify, or kill a product idea. Do not use for code review or PR hygiene unless the user explicitly asked to rate pr_process.
---

# Pitch-rate

Verify whether an idea is worth pitching. Score **existing-solution density**, not pain. Pain is granted. Empty seats are not.

Do not write or modify repo files unless the user asked to save a rating. Default output is the chat verdict only.

## 1. Restate the object

One line, then stop and use it for the rest of the session:

- `idea` — founding / OSS / plugin question
- `adr` — does this ADR survive the filter it claims to pass
- `pr_process` — title, commits, consistency, writing (only if the user asked)

If the user said “rate the ideas,” `object_under_review` is `idea`. Drop PR title, commit list, and writing axes.

## 2. Load references (read, do not inline from memory)

Read in this order:

1. [references/rubric.md](references/rubric.md)
2. [references/seat-match.md](references/seat-match.md)
3. [references/deny-patterns.md](references/deny-patterns.md)
4. [references/output-template.md](references/output-template.md)

If this is the first rating in the session, also read [references/calibration.md](references/calibration.md) **before** any 0–10 score.

If `docs/adr/0001-no-pitchable-candidate.md` exists in the repo, read it. Its killed-seats tables are the deny-list source of truth. If it is missing, use `deny-patterns.md` only and state that the catalog is incomplete.

## 3. Steelman first

Write why a skeptical founder would still build this. Include an occupancy estimate.

That estimate is a **ceiling**. Later exact-mechanics density must not exceed it without new named evidence.

## 4. Search the seat, not the slogan

Search the mechanics (daemon / proxy / compiler / CI / library / protocol). Fill incumbents with **URL + quote** before any density number.

Do not pick an overall 0–100 and fill axes afterwards. Do not treat a previous ADR kill as the rubric. Do not treat pain as a score.

## 5. Seat-match, then dual-score

Label every incumbent with exactly one seat-match from `seat-match.md`. Then score:

- problem density (may count `adjacent_pain`)
- exact-mechanics density (count `exact` only)

## 6. Gates, then emit

Apply hard gates in `rubric.md`. Emit the block in `output-template.md`.

Forbidden:

- overall score out of 100
- “this repeats ADR 0002’s bundling sin” as the primary argument without naming **this** idea’s incumbents
- citing a file you did not successfully read (`NEED_EVIDENCE` instead)
