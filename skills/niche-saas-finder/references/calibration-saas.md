# Calibration (SaaS)

Read this before the first 0-10 score in a session. Each case is: claim
-> correct labels -> disposition -> mistake to avoid.

Do not copy these dispositions onto a **new** seat. Copy the **labeling
discipline**. If the restated v1 *is* one of the three false keeps
below, apply that case's disposition; do not re-keep it as Sparse
because leftover prose is strong.

Do not add seeds. Labeling notes in
[gate-bind-saas.md](gate-bind-saas.md) and switch hosts in
[seat-generation-saas.md](seat-generation-saas.md) are not extra
false-keeps. Aisle switch trips on those switch hosts, not on these
three seeds unless the restated v1 *is* one of them.

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

## Steelman discipline

If thinking says occupancy is 5-6 and OSS is plausible, the published
exact-mechanics score may not jump to 8-9 with the same evidence.
Publish the steelman. If you discard it, say which **new named row**
changed the ceiling.
