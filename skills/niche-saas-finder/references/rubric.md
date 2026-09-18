# Rubric (SaaS occupancy)

Occupancy gate for the vertical-workflow seat under review. Do not invent
a parallel philosophy. Auto-reject **examples** are SaaS; **ids** match
[gate-bind-saas.md](gate-bind-saas.md).

## What is scored

Score **existing-solution density**, not pain. Pain is abundant. Empty
seats are not.

Score **v1 as shipped**, not the Series A architecture.

## Bands

| Band | Score | Meaning |
|------|------:|---------|
| Saturated | 8-10 | Named products already *are* this UX. Do not found. |
| Occupied | 5-7 | Adjacent tools treat the pain. Remaining work is glue, a flag, or a plugin. |
| Sparse | 2-4 | Pieces exist. No widely adopted product sits in the proposed seat. |
| Greenfield | 0-1 | Mechanics are new. |

Pitchable **as a company** only if Sparse or Greenfield **and** no
automatic reject **and** `keep_gate: pass` from
[gate-bind-saas.md](gate-bind-saas.md).

Occupied leftover -> `file_on` (flag / marketplace issue / plugin on
the named SoR). Do not found.

`as_plugin` answers "is the leftover a flag/plugin/issue on a named
host?" It cannot be Greenfield when an incumbent leftover already names
that host. Greenfield plugin plus an `exact` row is a card fail.

`1_vacant_process` fails when any incumbent is `exact` for a slice of
`v1_as_shipped`, unless `file_on` is set on that slice and the company
score is only the remaining process. Redefining the seat as
"orchestration around the SoR primitive" is not a vacant process.

Unadopted is not Greenfield. A thin marketplace listing often means the
seat is gist-shaped or already named.

## Split verdicts

Emit three bands, not one:

| Field | Question |
|-------|----------|
| `as_company` | Would you found this? Sparse/Greenfield + no auto-reject, or no. |
| `as_oss` | Is a bounded library/script worth publishing? May be yes when `as_company` is no. |
| `as_plugin` | Is the honest leftover a flag, plugin, or issue on a named SoR? |

An Occupied company can still be a valid OSS experiment. Do not collapse
those into one 0-100. No overall `/100`.

## Automatic rejects

Any one is fatal for an `as_company` Sparse/Greenfield keep. Ids are
applied as remapped in [gate-bind-saas.md](gate-bind-saas.md):

1. A named incumbent already ships the **headline UX**.
2. v1 is a Zapier/Make recipe, generic form wrap, or equivalent of a
   50-line Action.
3. The core transform is mathematically non-invertible and the pitch
   would have to lie.
4. The remaining wedge is reverse-mapping a security or privacy control.
5. The remaining wedge is "add this to incumbent X" (SoR checkbox,
   marketplace app, filed issue). Diagnostics and orchestration around
   a named primitive are this reject.
6. Silent mutation of user payloads without an advisory-first v1.
7. Marketplace app / sidecar the SoR does **not** consult at write-time.

## Falsification (all three must hold)

A "do not build" catalog is wrong for **this seat** only if:

1. A named workflow step sits where **no incumbent occupies** (not "add
   a checkbox to Clio/Toast").
2. Runtime enforcement **cannot** be a Zapier recipe or generic form wrap.
3. Three incumbents can still be named, and the gap is **mechanical**,
   not a missing marketplace setting.

Do not treat "the pain is real" as falsification.

## Claim hygiene vs occupancy

Unsourced HIPAA/PHI, WTP, TAM, latency, or "sub-second sync" claims fail
**claim hygiene**. Kill the number. Re-score from named incumbents.
Hygiene fail is not Occupied-by-itself.

Price and lock-in are not automatically Occupied-as-glue. Label those
`price_packaging` (see [seat-match.md](seat-match.md)).

Roadmap on an incumbent ("we plan to ship this") is `file_on` / wait,
not Sparse, when the honest move is to file or wait.

## Gates (no overall /100)

`keep` | `hold` | `drop` | `file_on`

- `keep` -- `as_company` is Sparse or Greenfield, no auto-reject, all
  three falsification tests hold, >=5 named incumbents (or explicit
  "could not find 5" plus why), **and** `keep_gate: pass`.
- `file_on` -- Occupied leftover belongs on a named SoR or marketplace app.
- `hold` -- Occupied/Saturated **as a company** but the leftover is a
  clean plugin, OSS experiment, or follow-up seat.
- `drop` -- Occupied/Saturated **as a company** and leftover is not even
  a clean plugin, or an auto-reject fired with no file-on target, or
  evidence is too thin (`NEED_EVIDENCE` rows dominate).
