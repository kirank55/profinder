# Search playbook (SaaS)

Incumbent extraction for a seat already restated. Do not load this file
before a seat exists. Do not load this file if the scope gate failed or
the niche is `intake_blocked`. Queries are SoR nouns from the niche plus
the restated seat, never "SaaS idea" or value-prop language.

Do not load a parent/devtools search playbook. Classes
`host_primitive`, `dropin_cli`, or `orchestrator` on this card are a
fail.

## Query construction

- Spine is niche `system_of_record` + `workflow_step` + the restated
  process.
- Use SKU + step nouns: `Clio demand letter`, `Eaglesoft remake case`,
  `Toast end-of-night close`, `ServiceTitan dispatch board`.
- Do not use value-prop queries: `"best dental SaaS"`, `"AI for law"`,
  `"SaaS idea"`.

## Mandatory query classes

Five logos is not a search. Before scoring, run **all four** classes
against this seat's workflow step. Record the queries on the card under
`search_classes`. Stopping after adjacent pain tools (horizontal CRM,
generic form builders, unfetched G2/Capterra lists) without class 1-2
is a keep-gate G2 fail.

1. **`sor_primitive`.** SoR docs, flags, native workflow, or API for
   that step (the host primitive).
2. **`dropin_addon`.** Marketplace add-on / extension people already
   install for that SoR. Label `exact` only if the write-time consult
   test in [gate-bind-saas.md](gate-bind-saas.md) passes.
3. **`commercial_sku`.** Vertical vendor SKU or control plane that
   already sits in this step.
4. **`tracker_leftover`.** Feature request / issue on class 2 for that
   step. A filed issue **is** occupancy for auto-reject 5.

| SoR family | Class 1-2 query shapes (always hit the named SKU) |
| --- | --- |
| Dental (Eaglesoft / Dentrix) | vendor workflow docs for the named step; Patterson/Dentrix marketplace or eServices catalog; lab case / remake / claims add-ons |
| Legal (Clio / MyCase) | SoR workflow/API docs for the named step; Clio App / MyCase marketplace; document-assembly or intake add-ons **on that SKU** |
| Home service (ServiceTitan / Housecall Pro) | SoR dispatch/job/invoice docs; marketplace apps the SoR consults at write-time |
| Restaurant / retail (Toast / Square) | SoR POS/close/payroll docs; app marketplace for that SKU |
| Clinic / studio (Jane / SimplePractice / Mindbody) | SoR scheduling/chart/billing docs; app marketplace for that SKU |
| Construction (Buildertrend) | SoR selection/change-order/draw docs; marketplace or partner integrations |

These starters are query shapes, not a closed-aisle list and not
generation seeds. Switch hosts for aisle-close live in
[seat-generation-saas.md](seat-generation-saas.md).

## Extraction rules

- >=5 named incumbents per candidate **and** classes 1-4 attempted.
- Each row: name, URL fetched this run, quote that is a **contiguous
  substring** of that page, one seat-match label, leftover if this row
  were exact.
- Unverified, 404, JS-empty, or paywalled -> `NEED_EVIDENCE` on that
  row. No hallucinated products.
- Paraphrase is not a quote. Do not stitch a sentence the page does not
  contain.
- G2, Capterra, GetApp, and similar directories: unfetched or paraphrase
  -> `NEED_EVIDENCE`. A fetched listing is `adjacent_pain`, never
  `exact`. `exact` requires the product page (or SoR / marketplace doc)
  for the SKU in the seat.
- Write-time consult: a marketplace app with no fetched SoR write-path
  quote is not `exact`. See [gate-bind-saas.md](gate-bind-saas.md).

## Stop condition

Do **not** stop at the fifth adjacent logo.

Stop when: classes 1-4 have been queried **and** either >=5 verified
rows exist or three independent 404/`NEED_EVIDENCE` rows exist for class
1-2 (SoR primitive and drop-in addon). Thin class 1-2 evidence =>
`claim_hygiene: unsourced` and `as_company` must not be
Sparse/Greenfield-keep.
