# Seat match (SaaS)

Every incumbent gets **exactly one** label. This is the check that stops
category collapse (Clio counted as a MyCase seat, Typeform counted as
Clio demand-letter intake).

Apply [gate-bind-saas.md](gate-bind-saas.md) notes after this file: SKU
mismatch is `wrong_substrate`; fetched G2/Capterra listings are
`adjacent_pain`; write-time consult is required for marketplace `exact`.

## Labels

| Label | Meaning | Counts toward problem density? | Counts toward exact-mechanics density? |
|-------|---------|--------------------------------|----------------------------------------|
| `exact` | Same SoR placement and SKU as the proposed v1 | yes | **yes** |
| `adjacent_pain` | Treats the same pain with different mechanics | yes | no |
| `language_scoped` | Same idea, wrong runtime (SDK / in-process port vs the named SoR host) | weakly | no |
| `wrong_substrate` | Same slogan, different SoR SKU (Clio vs MyCase, Eaglesoft vs Dentrix) | weakly | no |
| `obsolete` | Abandoned or legacy; does not occupy the current year by default | no | no |
| `price_packaging` | A product exists in a nearby aisle; access, price, or lock-in may still be a gap | yes as adjacent | no unless it *is* the SKU |

If two labels could apply, pick the **strictest mismatch** (prefer
`wrong_substrate` / `language_scoped` / `obsolete` over `exact`). Do not
upgrade to `exact` to make a kill easier.

## Dual scores

**Problem density** -- how many ways already stop the *pain*, including
`adjacent_pain`.

**Exact-mechanics density** -- how many products already *are* this
workflow seat on this SoR. Count `exact` only.

A bundle of occupied slices sold as one SKU is **Occupied**, not Sparse.
If `v1_as_shipped` is a conjunction, split slices before labeling.

## Examples (do not generalize beyond the label)

| Cited as occupant | Proposed seat | Correct label |
|-------------------|---------------|---------------|
| Clio Manage native demand letters | demand-letter intake on **MyCase** | `wrong_substrate` |
| Typeform + Zapier | Clio demand-letter intake as vertical v1 | `wrong_substrate` / `adjacent_pain` |
| Fetched Capterra category listing | Toast end-of-night close | `adjacent_pain` |
| Python SDK claimed as Eaglesoft Windows seat | remake-case intake on Eaglesoft | `language_scoped` |
| ServiceTitan App Marketplace app the SoR consults at job-complete | missing-trade pack on that app | `exact` for the app slice; leftover is auto-reject 5 |
| ServiceTitan required Skills + skill-gap alert at book/assign | license-expiry dispatch guard on ServiceTitan | `exact` for the assignment-gate slice; leftover auto-expire is auto-reject 5 |
| Horizontal CRM | vertical workflow on a named SoR | `wrong_substrate` or `adjacent_pain` |

## How to write a row

Required fields per incumbent: name, URL, one quote from **that** page,
`seat_match`, leftover (what is still missing if this row is `exact`).

A row without a URL is not an incumbent. Put it in `NEED_EVIDENCE` or
drop it.
