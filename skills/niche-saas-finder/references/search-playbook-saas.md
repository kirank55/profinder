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
is a keep-gate G2 fail. Stopping after a SoR help article that admits
"no dedicated module" without class 2-3 is the same G2 fail.

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

## Class-1 gap quote is not a stop

A fetched SoR sentence that says any of: "does not have a native /
dedicated … module", "you must build a custom … report", "is a manual
step", "scheduled report is the only proactive mechanism", "use custom
fields / forms / tags / skills" is **class-1 occupancy of the
workaround named on that same page**. Record that workaround as a row
(Skills required-for-job-type, Invoice Items report, intro-offer
one-purchase flag, chart letterhead templates, claim scrub, warranty
holding workflow). Then run class 2 and class 3. Do not score yet.

That workaround is `exact` for the headline UX when it *is* the
assignment gate / one-purchase rule / letter print / submit block.
Leftover "automate the manual step" or "sync the date field" is
auto-reject 5, not Sparse. Labeling it `adjacent_pain` so
`exact_mechanics_density` can be 0 is a card fail.

Class 3 is a **step-noun query without using the SoR name as the only
token**. Two quotes from one SoR URL do not count as class 3.

| SoR family | Class 3-4 query shapes (always run; not generation seeds) |
| --- | --- |
| Home service | EPA / refrigerant cylinder ledger SKUs; technician license / cert compliance SKUs; manufacturer warranty-claim packet SKUs; `{SoR} marketplace` + the step |
| Restaurant / retail | POS vs DoorDash / Uber Eats / Grubhub payout-matcher SKUs; `{SoR}` Shop / marketplace + payout / recon |
| Legal | crash / police-report order portals; docket / SOL engines; trust escheatment SKUs; `{SoR}` App Directory + the step |
| Clinic / studio | OON superbill / reimbursement trackers; supervision-hours trackers; `{SoR}` letter / template library for the step |
| Dental / construction | claims / lab / change-order add-on SKUs **and** the named marketplace |

Do not copy those SKU names onto a new seat as occupancy. Re-search
**this** step. Name **this** step's class-3 page.

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
- Quote `url` must be the page that contains the quote. A real
  sentence from a different article on the same vendor is still
  `NEED_EVIDENCE` on that row.
- Two incumbent rows from one SoR help URL do not satisfy ">=5 named
  incumbents."

## Stop condition

Do **not** stop at the fifth adjacent logo.

Do **not** stop because class 1 said there is no dedicated module.

Stop when: classes 1-4 have been queried **and** class 3 produced a
named commercial SKU row or `NEED_EVIDENCE` **and** either >=5 verified
rows exist or three independent 404/`NEED_EVIDENCE` rows exist for class
1-2 (SoR primitive and drop-in addon). Thin class 1-2 **or** skipped
class 3 => `claim_hygiene: unsourced` and `as_company` must not be
Sparse/Greenfield-keep. A keep whose only incumbents are the named
SoR's help center is a G2 fail.
