# Search playbook

Incumbent extraction for a seat already restated. Do not load this file before a seat exists. Do not load this file if the scope gate failed or the niche is `intake_blocked`. Queries are stack nouns from the niche plus the restated seat, never "SaaS idea" or value-prop language.

## Query construction

- Spine is niche `substrate_or_stack` + `immutable_host` + the restated process or protocol.
- Use stack nouns + protocols: `wire protocol proxy`, `eBPF tc filter`, `AST collision queue`, `DPOR interleaving test`, `merge queue scheduler`, `lockfile host enforcement`.
- Do not use value-prop queries: `"best AI testing tool"`, `"developer productivity automation"`, `"SaaS idea"`.

## Extraction rules

- >=5 named incumbents per candidate.
- Each row: name, verified URL, exact quote from docs/README, one seat-match label, leftover if this row were exact.
- Unverified or 404 -> `NEED_EVIDENCE` on that row. No hallucinated products.

## Stop condition

Five verified rows or three independent 404/`NEED_EVIDENCE` rows, whichever comes first. If evidence is thin, the candidate's `claim_hygiene` is `unsourced` and `as_company` must not be Sparse/Greenfield-keep.
