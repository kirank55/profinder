# Seat generation (SaaS)

This file answers "how do I propose seat S?" -- not "how do I search
incumbents of S?"

**Start from named SoRs, never from pain slogans.** Pain is abundant;
empty seats are not.

## Niche first

Do not open this file on a slogan hunt. If the scope gate has not passed,
return to [intake-saas.md](intake-saas.md).

Generate **inside the niche**. `system_of_record` constrains the
inventory: drop SoRs that are not that SKU/host unless `niche.source` is
`agent_opt_out`.

When intake named `workflow_step`, do not wander to a different step.
When it was unset, each raw seat supplies a named step in that SoR.
Search never runs with `workflow_step` blank.

`hard_nos` are generation filters, not occupancy scores. Drop a raw seat
that matches a hard no **before** deny.

When `source: agent_opt_out`, pick **exactly one** row via **Interest
routing** below and set `niche.source: agent_opt_out` on every raw seat.
Fill `icp` from that row's default ICP. Do not generate across every SoR
in one hunt.

Horizontal CRM/marketing and developer-tool seats are out of scope.

## Seed SoR inventory

Interest routes into this list; it does not score. Opt-out uses exactly
one row per hunt. Class-1/2 **switch hosts** are aisle machinery, not
generation seeds and not extra calibration seeds.

| SKU | Hosting | Default ICP (opt-out fill) | Class-1 switch host | Class-2 switch host |
| --- | --- | --- | --- | --- |
| ServiceTitan | cloud | home-service operators | ServiceTitan native job/dispatch/invoice workflow | ServiceTitan App Marketplace app the SoR consults at write-time |
| Housecall Pro | cloud | home-service operators | Housecall Pro native job workflow | Housecall Pro app / integration catalog |
| Patterson Eaglesoft | Windows | independent dental practices / labs | Eaglesoft native workflow for the named step | Patterson eServices / marketplace addon the SoR consults |
| Dentrix | named SKU + hosting as stated | dental practices | Dentrix native workflow for the named step | Dentrix Developer / marketplace addon the SoR consults |
| Clio | cloud | law firms | Clio Manage / Clio API workflow for the named step | Clio App Directory app the SoR consults at write-time |
| MyCase | cloud | law firms | MyCase native workflow for the named step | MyCase marketplace addon the SoR consults |
| Toast | cloud | restaurants | Toast POS native workflow for the named step | Toast Shop app the SoR consults at write-time |
| Square | cloud | restaurants / retail as named | Square native API/POS for the named step | Square App Marketplace app the SoR consults |
| Mindbody | cloud | studios / wellness | Mindbody native scheduling/POS workflow | Mindbody Marketplace addon the SoR consults |
| Buildertrend | cloud | residential builders | Buildertrend native workflow for the named step | Buildertrend integration the SoR consults |
| Jane | cloud | allied health clinics | Jane App native chart/schedule/billing | Jane integrations the SoR consults |
| SimplePractice | cloud | private practices | SimplePractice native workflow for the named step | SimplePractice integrations the SoR consults |

Each seat's `system_of_record` is `SKU + hosting constraint` (e.g.
`Clio cloud`, `Patterson Eaglesoft on Windows`).

## Interest routing (first match wins)

Apply only when `source` is `agent_opt_out`. User-named SoR is never
overridden.

| Interest contains (case-insensitive) | Inventory row |
| --- | --- |
| dental, eaglesoft, lab | Patterson Eaglesoft |
| dentrix | Dentrix |
| law, legal, attorney, clio, PI, "personal injury" | Clio |
| mycase | MyCase |
| home service, HVAC, plumber, electrician, servicetitan | ServiceTitan |
| housecall | Housecall Pro |
| restaurant, toast, POS (with restaurant) | Toast |
| square, retail | Square |
| mindbody, salon, studio, wellness, yoga | Mindbody |
| builder, construction, buildertrend | Buildertrend |
| jane, allied health, physio, chiro | Jane |
| simplepractice, therapy, counselor | SimplePractice |
| (no match) | ServiceTitan (first inventory row) |

`dental` does not pick Dentrix. `law` does not pick MyCase. Those SKUs
require the SKU name or an explicit user SoR.

## Vacancy probes

Queries for missing SKUs, not "best tools for X":

- (a) named workflow step with no shipping integration in that seat
- (b) marketplace app the SoR does not consult at write-time -- apply
  the write-time consult test in [gate-bind-saas.md](gate-bind-saas.md);
  auto-reject 7 analogue
- (c) spreadsheet/CSV bridge sitting in an enforcement seat
- (d) generic-form tool claimed as vertical v1 -- label later; do not auto-pitch

## Aisle switch

After the first two restated seats in a hunt:

- Count a trip if the seat is `exact` on that row's class-1 or class-2
  **switch host**, or matches a local deny one-liner. Do not trip from
  the calibration false keeps unless the restated v1 *is* one of those
  cases.
- Opt-out: pick a **different** inventory row (do not reuse a
  just-closed SKU). Fill niche from the new row. Generate a new set of
  >=5 seats.
- User-named SoR: keep the SKU. If intake `workflow_step` was named,
  stop that step (Occupied / `file_on`); do not invent a second SoR. If
  intake step was unset, pick a different named step in the same SoR
  and continue; do not emit three more Occupied cards for the closed
  step.

Switch hosts are deny/aisle machinery. Do not generate "a new
ServiceTitan App Marketplace."

## Raw seat shape

Each raw seat must include, before search:

```yaml
candidate_seat: <stack position, one line>
v1_as_shipped: <concrete deliverable and where it sits>
workflow_step: <named step; required here>
system_of_record: <named SKU/host>
why_not_a_slogan: <the mechanic, in one sentence>
niche:
  icp: <from intake or opt-out default>
  system_of_record: <from intake>
  workflow_step: <this seat's step>
  ship_form: company | oss | plugin | unset
  unique_data_or_distribution: <from intake or unset>
  hard_nos: []
  source: user | agent_opt_out
```

Drop the seat if `workflow_step` or `why_not_a_slogan` cannot be filled.
Drop the seat if it ignores `system_of_record` or a `hard_nos` entry.
Do not emit a `niche_icp` key.

## Hunt discipline

Generate >=5 raw seats per hunt request **inside the niche**. Then run
the `SKILL.md` pipeline on each (deny after restate). Expect most to
become `file_on` or drop. A hunt that emits five slogan keeps has
failed. A hunt that emits seats outside the SoR has failed. A hunt that
emits Sparse company keeps without `keep_gate: pass` has failed. A hunt
that records tracker "keeps" without emitting
[output-template-saas.md](output-template-saas.md) cards has failed.

If `v1_as_shipped` is a conjunction, list slices on the raw seat before
search.

Do not use closed-aisle leftovers as generation seeds (add a trade to a
ServiceTitan app, generic form + Zapier, CSV + reminder + portal as one
SKU, SoR "no dedicated module" write-time guard). That is
prior-kill-as-rubric. Do not port the previous hunt's
one-line seats onto a new SoR (Clio demand-letter leftover → MyCase
demand-letter leftover). Re-search **this** SoR.
