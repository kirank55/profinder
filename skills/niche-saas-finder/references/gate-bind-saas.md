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
`NEED_EVIDENCE` rows.

**G2. Query classes, not five logos.** Search hit `sor_primitive`,
`dropin_addon`, `commercial_sku`, and `tracker_leftover` in
[search-playbook-saas.md](search-playbook-saas.md) for this SoR. A table
of five Capterra logos, horizontal CRMs, or generic form builders does
not satisfy G2.

**G3. Leftover names a host -> `file_on` that host.** If any leftover
sentence names a SoR, marketplace app, flag, or issue, `file_on` is
that URL (not `none`). `as_plugin` may not be Greenfield in that case.

**G4. Exact slice occupies vacant-process.** If any row is `exact`,
`1_vacant_process` is `fail` unless `file_on` is set on that slice
**and** `as_company` scores only the remaining named process. You may
not pass vacant process by redefining the seat as "the orchestrator
around the Toast/Clio primitive."

**G5. Conjunction v1 is a bundle.** If `v1_as_shipped` joins two or more
mechanisms with "and" (CSV + reminder + portal, intake + e-sign +
docket), split into slices before scoring. If each slice has an `exact`
or adjacent host, the SKU is Occupied. No single logo selling the bundle
is not vacancy. Load [calibration-saas.md](calibration-saas.md)
Occupied-bundle cases.

**G6. Auto-reject #5 default.** Leftover that is diagnostics, a
checkbox, a marketplace setting, or "orchestration around SoR X" is
"add this to incumbent X." Fire auto-reject 5. Do not talk it into a
company in prose.

**G7. Mechanism claims.** Unsourced HIPAA/PHI, latency, WTP, TAM, or
"sub-second sync" claims must be stated on a fetched vendor or protocol
page. Else `claim_hygiene: unsourced` or `implausible`, delete the claim
from `v1_as_shipped`, and re-score. Hygiene fail is not Occupied-by-itself
(see [rubric.md](rubric.md)); inventing a SoR property
**is** a keep block until v1 is restated without it.

**G8. Split-verdict sanity.** `as_plugin` Greenfield plus an `exact`
incumbent row is a card fail. `as_oss` occupancy **lower** than
`as_company` needs a one-line reason or it is a card fail.

**G9. Steelman.** Published `exact_mechanics_density` may exceed the
pre-search ceiling only if G2 added **named** rows. Missed-search is not
a low ceiling.

`keep_gate: pass` only if G1-G9 hold. `keep_gate: fail` -> `as_company`
is Occupied, Saturated, `file_on`, or `drop`. Never Sparse/Greenfield
keep. `as_oss` / `as_plugin` may still be Sparse.

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

## SaaS embedded deny fallback

Until the target workspace keeps a local killed-seats file (one-line
seats under `.docs/` or `docs/`), use this list
(`deny_catalog: embedded_saas_baseline`):

- Horizontal CRM/marketing claimed as vertical v1
- Generic form + Zapier as the vertical seat
- Add missing trade/vertical to a named marketplace app
- CSV + reminder + portal bundle as one SKU

A previous kill is a deny-list entry, not a scoring template. Do not
generate from this list. Re-search **this** seat.

Local killed-seats file wins (`deny_catalog: local_*`). `incomplete`
only if this fallback and a local file are both missing.
