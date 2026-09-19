# Gate bind (SaaS)

Load this file before any `as_company` Sparse/Greenfield and before
applying auto-rejects from [rubric.md](rubric.md).

This file **is** the keep latch (G1-G9). Do not load files outside this
tree. Occupancy philosophy is unchanged; the checks are bound onto
vertical-workflow SaaS nouns.

G2 classes are those in [search-playbook-saas.md](search-playbook-saas.md).
Collapse modes below are the whole deny philosophy for this skill.

Citing Landlock, Kroxylicious, or `CREATE PUBLICATION` as occupancy on
a vertical SaaS card is a card fail.

## G1-G9 bind

**G1. Quotes are literals.** Each incumbent `quote` is a contiguous
substring of a page **fetched this run** at `url`. Ellipsis may join two
substrings only if both appear on that page. 404, JS-empty, paywalled,
or paraphrase -> that row is `NEED_EVIDENCE`. A keep may not include
`NEED_EVIDENCE` rows. A real sentence from a **different** vendor URL
than `url` is still `NEED_EVIDENCE` on that row.

**G2. Query classes, not five logos.** Search hit `sor_primitive`,
`dropin_addon`, `commercial_sku`, and `tracker_leftover` in
[search-playbook-saas.md](search-playbook-saas.md) for this SoR. A table
of five Capterra logos, horizontal CRMs, or generic form builders does
not satisfy G2. Missing `search_classes` keys is G2 fail. Two rows from
one SoR help URL do not satisfy G2, even when those quotes admit a
gap. Class 3 must produce a named commercial SKU row or
`NEED_EVIDENCE`. Skipping class 2-3 because class 1 "does not have a
native module" is G2 fail. A keep whose only incumbents are the named
SoR's help center is G2 fail.

**G3. Leftover names a host -> `file_on` that host.** If any leftover
sentence names a SoR, marketplace app, flag, or issue, `file_on` is
that URL (not `none`). `as_plugin` may not be Greenfield in that case.
`as_plugin` Occupied plus `file_on: none` is a card fail.

**G4. Exact slice occupies vacant-process.** If any row is `exact`,
`1_vacant_process` is `fail` unless `file_on` is set on that slice
**and** `as_company` scores only the remaining named process. You may
not pass vacant process by redefining the seat as "the orchestrator
around the Toast/Clio primitive." You may not pass it by labeling the
SoR workaround `adjacent_pain` because the leftover is "manual" or
"not auto." If the class-1 page describes Skills / forms / Invoice
Items / intro-offer flags / letter templates that *are* the headline
UX, that row is `exact` for that slice.

**G5. Conjunction v1 is a bundle.** If `v1_as_shipped` joins two or more
mechanisms with "and" / "plus" (CSV + reminder + portal, intake +
e-sign + docket, cylinder ledger + threshold + leak-rate math), split
into slices before scoring. If each slice has an `exact` or adjacent
host, the SKU is Occupied. No single logo selling the bundle is not
vacancy. Load [calibration-saas.md](calibration-saas.md)
Occupied-bundle cases.

**G6. Auto-reject #5 default.** Leftover that is diagnostics, a
checkbox, a marketplace setting, "orchestration around SoR X", or
"automate the manual Skill / report / form step the SoR already
documents" is "add this to incumbent X." Fire auto-reject 5. Do not
talk it into a company in prose.

**G7. Mechanism claims.** Unsourced HIPAA/PHI, latency, WTP, TAM, or
"sub-second sync" claims must be stated on a fetched vendor or protocol
page. Else `claim_hygiene: unsourced` or `implausible`, delete the claim
from `v1_as_shipped`, and re-score. Hygiene fail is not Occupied-by-itself
(see [rubric.md](rubric.md)); inventing a SoR property
**is** a keep block until v1 is restated without it.

**G8. Split-verdict sanity.** `as_plugin` Greenfield plus an `exact`
incumbent row is a card fail. `as_plugin` Occupied plus `file_on: none`
is a card fail. `as_oss` occupancy **lower** than `as_company` needs a
one-line reason or it is a card fail.

**G9. Steelman.** Published `exact_mechanics_density` may exceed the
pre-search ceiling only if G2 added **named** rows. Missed-search is not
a low ceiling. Two SoR-help quotes are not a 2.5 ceiling.

`keep_gate: pass` only if G1-G9 hold. `keep_gate: fail` -> `as_company`
is Occupied, Saturated, `file_on`, or `drop`. Never Sparse/Greenfield
keep. `as_oss` / `as_plugin` may still be Sparse. A tracker bullet
without an emitted card from [output-template-saas.md](output-template-saas.md)
is not a keep.

## Worked false keeps (labeling, not generation seeds)

Do not generate from these. If a restated seat **is** one of them, copy
the labeling: company Occupied / `file_on`, not Sparse keep. Full
labeling is in [calibration-saas.md](calibration-saas.md).

| Claimed keep | Correct |
| --- | --- |
| CSV + reminder + portal as one SKU | Occupied bundle. `file_on` the SoR. |
| Add missing trade to a named marketplace app | Auto-reject 5. `file_on` the app. |
| Typeform/Jotform + Zapier as the vertical v1 | Auto-reject 2. Occupied / drop. |
| SoR "no dedicated module" + write-time guard (license-expiry dispatch, 3PO payout join, EPA cylinder ledger) | Class-1 workaround is `exact` for that slice; class 3 occupies the standalone SKU. Skipping class 2-3 is G2 fail. Auto-reject 5. `file_on` the primitive or the matcher/ledger SKU. |

## Write-time consult test (probe b / auto-reject 7)

A drop-in addon is class-2 `exact` only if a page **fetched this run**
from the named SoR (workflow, API, or marketplace "installed on
save/post/checkout/job-complete") quotes a write-path trigger that
invokes that app.

Marketplace listing, dashboard, reporting overlay, or SoR docs that do
not name the app on that write path -> auto-reject 7, not a company.
Cannot fetch either the SoR write-path page or the marketplace page ->
`NEED_EVIDENCE` on that row. A marketplace app labeled `exact` without
that quote is a card fail.

## Fail-closed defaults (apply before scoring, no discretion)

- A class-1 SoR-help row describing the workaround primitive for the
  headline slice **defaults to `exact`**. Demotion to `adjacent_pain`
  requires a quote on the same page showing the v1's write-path gap;
  "manual", "custom", "report", or "not automatic" in the leftover
  never demotes. An unlabeled-or-demoted workaround row beside a
  passing `1_vacant_process` is a card fail.
- Auto-reject 7 fires unless the card records a `write_path_attempt`
  (SoR write-path URL fetched this run plus quoted trigger or explicit
  miss). Skipping the attempt fires the reject; it never exempts the
  seat from it.
- `1_vacant_process` passes only with zero `exact` rows on every
  slice. A pass beside an `exact` row is a card fail, even when
  `file_on` names another slice.

## Auto-reject remap

Rubric ids unchanged. Any one is fatal for an `as_company`
Sparse/Greenfield keep:

1. A named incumbent already ships the **headline UX**.
2. v1 is a Zapier/Make recipe, generic form wrap, or equivalent of a
   50-line Action.
3. The core transform is mathematically non-invertible and the pitch
   would have to lie.
4. The remaining wedge is reverse-mapping a security or privacy control.
5. The remaining wedge is "add this to incumbent X" (Clio / Toast /
   ServiceTitan marketplace app, SoR checkbox, filed issue). Diagnostics
   and orchestration around a named primitive are this reject, not a
   company.
6. Silent mutation of user payloads without an advisory-first v1.
7. Marketplace app / sidecar the SoR does **not** consult at write-time
   (write-time consult test / vacancy probe b). Real engineering, not a
   company.

## Seat-match notes (not calibration seeds)

Load [seat-match.md](seat-match.md) for the six
labels and dual scores. Then apply:

- Clio vs MyCase, Eaglesoft vs Dentrix, Toast vs Square →
  `wrong_substrate` when the seat named the other SKU.
- `language_scoped` → wrong runtime only (SDK / in-process port vs the
  named SoR host). Relabel `language_scoped` on a SKU mismatch; that
  card is a fail until fixed.
- Fetched G2/Capterra listing → `adjacent_pain`. Unfetched →
  `NEED_EVIDENCE`. Never `exact`.
- SoR workaround on the class-1 page (required Skills at assign,
  intro-offer one-purchase, letterhead print, claim scrub, warranty
  holding tasks) is `exact` for that slice when it is the headline UX.
  "Manual" leftover does not demote it to `adjacent_pain`.

Aisle **switch hosts** live in
[seat-generation-saas.md](seat-generation-saas.md). They are not extra
false-keep seeds.

## Collapse modes

1. **File it on the incumbent.** Named product already *is* the headline
   UX.
2. **Add the missing vertical to marketplace app X.** Cross-vertical
   absence is not a company.
3. **Sidecar without SoR write-time enforcement.** A marketplace app or
   CSV the SoR does not consult (write-time consult test). Real
   engineering, not a company.
4. **SoR gap quote as vacancy.** "No dedicated module; use custom
   fields / reports / skills" is occupancy of that workaround, not a
   vacant process.

## SaaS embedded deny fallback

Until the target workspace keeps a local killed-seats file (one-line
seats under `.docs/` or `docs/`), use this list
(`deny_catalog: embedded_saas_baseline`):

- Horizontal CRM/marketing claimed as vertical v1
- Generic form + Zapier as the vertical seat
- Add missing trade/vertical to a named marketplace app
- CSV + reminder + portal bundle as one SKU
- SoR "no dedicated module" leftover claimed as a vacant write-time
  company keep (license-expiry Skill sync, 3PO payout join, EPA
  cylinder ledger on the named FSM)

A previous kill is a deny-list entry, not a scoring template. Do not
generate from this list. Re-search **this** seat.

Local killed-seats file wins (`deny_catalog: local_*`). `incomplete`
only if this fallback and a local file are both missing.
