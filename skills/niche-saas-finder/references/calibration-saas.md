# Calibration (SaaS)

Read this before the first 0-10 score in a session. Each case is: claim
-> correct labels -> disposition -> mistake to avoid.

Do not copy these dispositions onto a **new** seat. Copy the **labeling
discipline**. If the restated v1 *is* one of the false keeps below,
apply that case's disposition; do not re-keep it as Sparse because
leftover prose is strong.

Do not add aisle seeds. Labeling notes in
[gate-bind-saas.md](gate-bind-saas.md) and switch hosts in
[seat-generation-saas.md](seat-generation-saas.md) are not extra
false-keeps. Aisle switch trips on those switch hosts, not on these
cases unless the restated v1 *is* one of them.

Do not cite Landlock, Kroxylicious, or `CREATE PUBLICATION` as occupancy
for a vertical SaaS seat. That is a card fail.

## Occupied bundle sold as one SKU

### CSV bridge + reminder + portal as one SKU

**Claim:** Sparse 3.0. Vertical v1 that syncs a spreadsheet, sends
reminders, and hosts a customer portal as one company SKU on a named
SoR.

**Correct:** Occupied **bundle**. Spreadsheet/CSV bridges, reminder
messaging, and portals each have `exact` or adjacent hosts (SoR export,
native reminders / campaigns, SoR or marketplace portal). No single
logo selling the bundle is not vacancy. Leftover "glue the three" is
auto-reject 5 / `file_on` the SoR. `1_vacant_process` may not pass while
an `exact` slice sits on the card. `as_plugin` is not Greenfield.

**Disposition:** `file_on` / `drop` as a company. `as_oss` may still be
Sparse for a bounded slice.

**Mistake to avoid:** Keeping the bundle Sparse because no single logo
sells CSV + reminder + portal. Passing vacant-process by renaming the
seat to "the orchestrator."

## Auto-reject 5 / file_on

### Add missing trade to a ServiceTitan marketplace app

**Claim:** Sparse 2.5. The marketplace app supports plumbing and HVAC;
electrical (or another trade) is missing. Ship a company that is "the
electrical version."

**Correct:** Occupied leftover. The honest move is a flag, vertical
pack, or issue on that marketplace app. Auto-reject 5. `file_on` the
app. `as_plugin` may be Occupied; it cannot be Greenfield with `file_on:
none`.

**Disposition:** `file_on` the named marketplace app. `as_company`
Occupied.

**Mistake to avoid:** Treating cross-trade absence as a vacant process.
Scoring packaging ("not in our vertical yet") as Sparse.

## Wrong substrate / wrapper

### Generic intake form + Zapier as vertical v1

**Claim:** Sparse 2.5. Typeform/Jotform + Zapier into Clio (or
Eaglesoft, Toast, …) *is* the vertical seat.

**Correct:** `wrong_substrate` and/or `adjacent_pain`, not `exact` for a
named-SoR workflow seat. If v1 *is* the recipe, auto-reject 2 (Zapier /
generic form wrap). Horizontal form tools treat the pain; they are not
the SKU on that SoR.

**Disposition:** `as_company` Occupied or drop. Do not keep Sparse by
calling Zapier "just plumbing."

**Mistake to avoid:** Labeling Typeform `exact` for Clio demand-letter
intake. Auto-pitching probe (d).

## SoR gap quote sold as vacancy

### "No dedicated module" then skip class 2-3

**Claim:** Sparse 2.5–3. The SoR help page says it has no native
certification / EPA / 3PO-payout module, so a write-time dispatch
guard, cylinder ledger, or Toast↔DoorDash matcher is a vacant company
seat. Two quotes from that help URL; `exact_mechanics_density: 0`;
`file_on: none`; `keep_gate: pass`.

**Correct:** Occupied leftover. The same page names the workaround
primitive (required Skills at book/assign, Invoice Items + refrigerant
forms, Toast-side Reconciliation report). That workaround is `exact`
for the headline UX slice. Class 3 already sits in the step (payout
matchers, refrigerant ledgers, hours trackers, crash-report portals,
OON reimbursement SKUs). Leftover "auto-remove the Skill when the date
lapses" / "join on Toast write-path" / "sit on the SoR" is auto-reject
5. Two SoR-help rows are a G2 fail. `as_plugin` Occupied plus
`file_on: none` is a card fail. Unadopted waitlists of the matcher are
not Greenfield.

If the restated v1 *is* ServiceTitan license-expiry dispatch guard,
Toast third-party delivery payout reconciliation, or ServiceTitan EPA
refrigerant cylinder ledger, apply this disposition. Do not re-keep
them as Sparse.

**Disposition:** `file_on` the SoR workaround or the class-3 SKU.
`as_company` Occupied. `as_oss` may still be Sparse for a bounded
script.

**Mistake to avoid:** Stopping search because class 1 admitted a gap.
Labeling the workaround `adjacent_pain` so density can be 0. Stamping
`keep_gate: pass` with two incumbents. Recording a tracker "keep"
without emitting a card.

## Sidecar without write-time consult

### Nightly job / standalone ledger outside the SoR

**Claim:** Sparse 3. A nightly diff job, standalone plan/ledger
builder, or matcher that lives outside the SoR (payroll true-up
ledger, spiff-version store, draw ledger, payout matcher, photo
scope-to-estimate draft) is a vacant company seat because the SoR
has no native version of it.

**Correct:** Auto-reject 7 plus auto-reject 5. No fetched SoR
write-path page consults the sidecar at save/post/checkout, so the
wedge is "add this to incumbent X" (SoR report, marketplace sync,
payroll-provider import), not a company. Skipping the write-path
fetch attempt fires the reject; it never exempts the seat.

**Disposition:** `file_on` the SoR primitive or the marketplace
sync SKU. `as_company` Occupied.

**Mistake to avoid:** Scoring "the SoR cannot do this natively" as
vacancy while the v1 never touches the SoR write path. Counting
standalone-sidecar mechanics as `exact_mechanics_density` for a
seat named on the SoR.

## Labeling notes (do not generalize into new seeds)

These are seat-match reminders, not generation seeds and not extra
false-keeps.

- Clio incumbent on a MyCase seat (and Eaglesoft vs Dentrix, Toast vs
  Square) is `wrong_substrate`, not `language_scoped`.
- `language_scoped` is a Python/SDK runtime port claimed as the named
  SoR host (e.g. a Python SDK as the Eaglesoft Windows seat).
- Fetched G2/Capterra listing is `adjacent_pain`. Unfetched is
  `NEED_EVIDENCE`. Neither is `exact`.
- Marketplace app the SoR does not consult at write-time is auto-reject
  7, not a company keep. `exact` requires the write-time consult test
  in [gate-bind-saas.md](gate-bind-saas.md).
- SoR workaround on the class-1 page is `exact` for that slice when it
  is the headline UX. "Manual step" leftover is auto-reject 5, not
  `adjacent_pain` with density 0.

## Steelman discipline

If thinking says occupancy is 5-6 and OSS is plausible, the published
exact-mechanics score may not jump to 8-9 with the same evidence.
Publish the steelman. If you discard it, say which **new named row**
changed the ceiling.
