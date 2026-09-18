# Independent rating: PR #13 sweep 1 keeps

Date: 2026-09-18
Object: the ten “provisional keeps” from sweep 1 on
[PR #13](https://github.com/kirank55/profinder/pull/13)
(`feat/saas-sweep-to-1000`, commit `41a01dc`). Later catch-up / wave
cards (`saas-04`–`saas-12`) are out of scope except as a hygiene note.
Method: rater pass against `skills/niche-saas-finder/` on the PR branch
(`SKILL.md`, `references/rubric.md`, `references/gate-bind-saas.md`,
`references/calibration-saas.md`, `references/seat-match.md`). Live URL
fetches this run. Occupancy, not pain. No overall `/100`. No TAM.

This is not a second finder hunt. Finder cards, where they exist, are
the object under review.

## Bottom line

**No. Sweep 1’s plans are not pitchable as companies.**

The stop condition (`keeps >= 3`) was met by **failing the keep latch**,
not by finding vacant seats. Three YAML cards claim `as_company: Sparse`
and `keep_gate: pass`. Independently they are Occupied leftovers on
named hosts. The other seven keeps have **no candidate cards at all**,
so they cannot be `keep` under the skill (`keep` requires a card that
passes G1–G9).

Pain is real in several aisles (expired EPA cards on a dispatch board,
DoorDash net vs Toast gross, AIM Act 15 lb ledgers). Empty company
seats are not.

| Keep (sweep 1) | Original | Independent `as_company` | Disposition |
| --- | --- | --- | --- |
| `saas-01` ST license-expiry dispatch guard | Sparse 2.5, `keep_gate: pass`, `file_on: none` | **Occupied 6.5** | `file_on` ServiceTitan Skills |
| `saas-02` Toast delivery payout recon | Sparse 3, `keep_gate: pass`, `file_on: none` | **Occupied 6.5** | `file_on` Voosh / Cointab |
| `saas-03` ST EPA refrigerant cylinder ledger | Sparse 2.5, `keep_gate: pass`, `file_on: none` | **Occupied 6.5** | `file_on` RefriTrak / ST forms |
| ST warranty packet builder | keep (name only) | **Occupied ~6.5** | `file_on` ST warranty workflow / JB360 |
| Clio crash-report DOT order helper | keep (name only) | **Occupied ~6.0** | `file_on` CrashDocs / BuyCrash |
| Mindbody intro-offer duplicate detection | keep (name only) | **Occupied ~7.0** | `file_on` Mindbody intro offers + merge |
| SimplePractice supervision-hours accumulator | keep (name only) | **Occupied ~6.0** | `file_on` Time2Track / SP supervision |
| SimplePractice medical-necessity guard | keep (name only) | **Occupied ~6.5** | `file_on` SP diagnosis + claim scrub |
| Jane referral-letter draft | keep (name only) | **Occupied ~7.0** | `file_on` Jane Letters |
| SimplePractice superbill tracker | keep (name only) | **Occupied ~6.5** | `file_on` Mentaya / Reimbursify / SP superbills |

**Do not found any of these.** The honest leftovers are flags, forms,
marketplace issues, or already-shipping commercial SKUs.

---

## How the sweep scored itself (and why that is not occupancy)

Tracker (`41a01dc:.docs/sweep-progress.md`): 95 researched, 10 keeps,
85 drops. Pitchable is defined correctly on the page
(Sparse/Greenfield + 0 auto-rejects + 3/3 falsification + ≥5 verified
incumbents + `keep_gate: pass`).

What actually shipped:

- **Three** cards in `.idea/`. Each has **two** incumbent rows, both
  from **one URL** (or one URL plus a standalone tracker). No
  `search_classes` block. That is a G2 fail before occupancy is even
  argued.
- **Seven** keeps exist only as a comma list in the tracker. The skill
  emits a card from `output-template-saas.md`. A name is not a card.
- `keep_gate: pass` is written on all three YAMLs. G1–G9 do not hold
  (table below).
- `as_plugin` is Occupied on two of the three while `file_on: none`.
  Gate-bind G3: leftover that names a SoR must `file_on` that URL;
  `as_plugin` may not be Greenfield in that case. Sweep 1 did the
  inverse: Occupied plugin, empty `file_on`, Sparse company.

The 85 drops look like the skill working (Eaglesoft Lab Tracking,
Jane waitlist, SimplePractice Fill Slot, Clio PI add-on). The keeps
are the miss: leftover prose was treated as vacancy.

---

## Card hygiene (the three YAMLs)

All three fail `keep_gate` independently of occupancy. A Sparse
company keep is forbidden on `keep_gate: fail`.

| Gate | `saas-01` | `saas-02` | `saas-03` |
| --- | --- | --- | --- |
| G1 quotes are literals from **that** URL | Pass (truncations of real ST sentences) | **Fail** — second quote is not on the cited DoorDash-payout page | Pass for the two cited pages |
| G2 four query classes, not five logos | **Fail** — 2 rows, 1 URL, no `search_classes` | **Fail** — same | **Fail** — 2 rows, no class-2 marketplace / class-3 SKU |
| G3 leftover names host → `file_on` that host | **Fail** — leftover names ST Skills; `file_on: none` | **Fail** — leftover names Toast; `file_on: none` | **Fail** — leftover names ST report; `file_on: none` |
| G4 exact slice occupies vacant-process | **Fail** — Skills **is** the dispatch block | Pass only if you ignore Voosh/Cointab | **Fail** if cylinder+threshold+leak-rate is one SKU |
| G5 conjunction v1 is a bundle | Borderline — “custom-field expiry **plus** scheduled-report sync” | Pass (one matcher) | **Fail** — cylinder ledger **and** 15 lb threshold **and** leak-rate math **and** purchase-ledger export |
| G6 auto-reject 5 default | **Fail** — leftover is auto-remove Skill | **Fail** once class-3 SKUs exist | **Fail** — leftover is “on ST write-time” |
| G8 split-verdict sanity | `as_plugin` Occupied + `file_on: none` | `as_plugin` Sparse 4 with Toast leftover | `as_plugin` Occupied + `file_on: none` |
| G9 steelman | Ceiling = published Sparse score; missed-search is not a low ceiling | Same | Same |

`deny_catalog: embedded_saas_baseline` is the happy path. The cards
did not run the “CSV + reminder + portal” / “add the missing vertical
to marketplace app X” / “sidecar the SoR does not consult” modes
against their own leftovers.

---

## Independent ratings (documented keeps)

### 1. ServiceTitan technician license-expiry dispatch guard (`saas-01`)

| Field | Original | Independent |
| --- | --- | --- |
| `as_company` | Sparse 2.5 | **Occupied 6.5** |
| `as_oss` | Sparse 3 | **Sparse 3.5** (a date→Skill PATCH is gist-shaped) |
| `as_plugin` | Occupied 5 | **Occupied 6.5** · `file_on` |
| `problem_density` | 5 | **7** |
| `exact_mechanics_density` | 0 | **4** (Skills is `exact` for the assignment gate) |
| Steelman ceiling | 2.5 | **6** (raised by the Skills docs the hunt already had) |
| `claim_hygiene` | ok | ok (no TAM) |
| `file_on` | none | [Manage skills for technicians and job types](https://help.servicetitan.com/roofing/docs/manage-skills-for-technicians-and-job-types) |
| Auto-rejects | none | **#1** (headline dispatch UX already ships) and **#5** (sync expiry → Skill) |
| Falsification | 3/3 pass | **`1_vacant_process` fail**; `2` may pass; `3` is a missing checkbox |
| Disposition | keep | **`file_on` / drop as a company** |

**What is still real.** ServiceTitan’s own compliance article says
there is no native certification module with built-in expiration
alerts, and that dropping an expired cert’s Skill is manual. That
sentence is a contiguous substring of
[Stay Compliant with Permits & Regulations](https://help.servicetitan.com/docs/stay-compliant-with-permits-regulations-1):
“If a technician's certification expires, removing their corresponding
Skill is a manual step.”

**Why it is not a company.** The v1 **is** that Skill. The same SoR
already:

1. Maps certifications to Skills and required job types.
2. Alerts on skill gap at book **and** at assign: “If you book a job
   with a technician who doesn't have the right skills for it, you're
   notified about the skills gap when you try to book the job. Also,
   if you try to assign a technician to a job but that technician
   doesn't have the correct skills, you'll be alerted about the skills
   gap.”
   ([Manage skills…](https://help.servicetitan.com/roofing/docs/manage-skills-for-technicians-and-job-types))
3. Stores expiry on technician custom fields and tells you to schedule
   30/60/90-day Technician reports.

The hunt labeled that page `adjacent_pain` and scored
`exact_mechanics_density: 0`. Under seat-match, same SoR placement and
SKU as the proposed write-time assignment block is `exact`. Leftover
is “auto-remove the Skill when the date field lapses.” Calibration’s
ServiceTitan case is this leftover: add the missing sync to the named
host. Auto-reject 5. `1_vacant_process` may not pass while that exact
slice sits on the card.

A third-party sidecar that PATCHes Skills is auto-reject 7 unless a
fetched SoR write-path page quotes that the app is consulted at
dispatch. No such quote was produced. Zapier/Make around custom fields
is auto-reject 2.

### 2. Toast third-party delivery payout reconciliation (`saas-02`)

| Field | Original | Independent |
| --- | --- | --- |
| `as_company` | Sparse 3 | **Occupied 6.5** |
| `as_oss` | Sparse 3 | **Sparse 3.5** (CSV join of Toast export + DoorDash payout) |
| `as_plugin` | Sparse 4 | **Occupied 6.0** · `file_on` |
| `problem_density` | 5 | **8** |
| `exact_mechanics_density` | 0 | **5** (Voosh + Cointab occupy the matcher SKU) |
| Steelman ceiling | 3 | **6.5** (G2 class-3 rows the hunt did not run) |
| `claim_hygiene` | ok | ok |
| `file_on` | none | [Voosh finance reconciliation](https://www.voosh.ai/finance-reconciliation), [Cointab POS vs DoorDash](https://cointab.net/popular-reconciliations/pos-vs-doordash) |
| Auto-rejects | none | **#1** (headline matcher already ships) |
| Falsification | 3/3 pass | **`1_vacant_process` fail** |
| Disposition | keep | **`file_on` / drop as a company** |

**What is still real.** Toast does not pay DoorDash/Uber Eats/Grubhub
marketplace payouts. Fetched:
[When do I get paid by DoorDash, Grubhub, and Uber Eats?](https://support.toasttab.com/en/article/When-do-I-get-paid-by-DoorDash-Grubhub-and-Uber-Eats)
—“third-party ordering platforms like DoorDash*, Grubhub, and Uber
Eats issue payouts directly to you, not through Toast”. Operators do
reconcile this in spreadsheets. Toast’s own Reconciliation report is
Toast-side deposits only.

**G1 miss on the card.** The second incumbent quote, “The
Reconciliation report gives you a single list of every payout Toast
has sent”, is a real contiguous substring of
[Reconciliation Report and Payout Details Overview](https://support.toasttab.com/en/article/Reconciliation-Report-and-Payout-Details-Overview).
It is **not** on the DoorDash-payout URL the card cites. Gate-bind G1:
quote must be a contiguous substring of the page fetched at `url`.

**Why it is not a company.** Class 3 already is this SKU:

- **Voosh** — “Match marketplace orders to POS records and bank
  deposits in one place, surface any short-pays or missing payouts”.
  The Feb 2026 announcement names Toast among POS systems and:
  “Seamlessly match your POS data with orders from third-party
  platforms like DoorDash, Uber Eats, and Grubhub”
  ([Voosh QBO/R365/POS post](https://www.voosh.ai/blogs/voosh-quickbooks-restaurant365-pos-integration)).
  Label: `exact` for the matcher, or `price_packaging` if the honest
  objection is “Wendy’s-franchise pricing.” Price/lock-in is not
  Occupied-as-glue by itself — but it also does not make the SKU
  vacant.
- **Cointab** — “Reconcile POS sales with DoorDash orders, payouts,
  fees, commissions, adjustments, refunds, and bank deposits in one
  structured workflow.” Marketing copy also claims
  single-location restaurants
  ([trial page](https://www.cointab.net/business/reconciliation/restaurant-owners-get-smarter-reconciliation-with-a-30-day-free-trial-no-card-needed/)).
  That kills the “independents only” steelman. Label: `exact` for the
  matcher (POS report in, DoorDash payout out) or `adjacent_pain` if
  you insist on Toast API write-path. Either way it is not Sparse.
- Toast Reconciliation report — `adjacent_pain` (correct leftover:
  Toast-side only).
- xtraCHEF unmatched-deposits article — `adjacent_pain` (clearing
  account for 3PO, not a per-order join).
- **DeliverGuard** (`deliverguard.io`) — waitlist / “coming soon” of
  *this exact v1*. Rubric: unadopted is not Greenfield.

“Neither Toast nor DoorDash ships the join” is true and irrelevant.
The join is a shipping commercial SKU. Auto-reject 1. Cross-POS
absence (“Cointab isn’t Toast-branded”) is auto-reject 5 / add-vertical
to the matcher.

### 3. ServiceTitan EPA refrigerant cylinder ledger (`saas-03`)

| Field | Original | Independent |
| --- | --- | --- |
| `as_company` | Sparse 2.5 | **Occupied 6.5** |
| `as_oss` | Sparse 3 | **Sparse 3.5** (bounded leak-rate calculator) |
| `as_plugin` | Occupied 5 | **Occupied 6.5** · `file_on` |
| `problem_density` | 5 | **8** |
| `exact_mechanics_density` | 0 | **4** as a **bundle of occupied slices** |
| Steelman ceiling | 2.5 | **6.5** |
| `claim_hygiene` | ok | ok on the 15 lb fact (RefrigerantTrack page) |
| `file_on` | none | [RefriTrak features](https://www.refritrak.com/en/features) (ST integration + cylinder tracking); ST refrigerant forms |
| Auto-rejects | none | **#5** (orchestrate around ST invoice items / RefriTrak). **#1** if the headline is “EPA cylinder ledger” |
| Falsification | 3/3 pass | **`1_vacant_process` fail** (G4/G5) |
| Disposition | keep | **`file_on` / drop as a company** |

**What is still real.** ST does not ship a dedicated EPA module. The
cited sentence is on the permits page: “ServiceTitan does not have a
dedicated EPA refrigerant tracking module. You must build a custom
Invoice Items report”. AIM Act 15 lb is a real 2026 rule change;
RefrigerantTrack’s homepage quote is a contiguous substring.

**Why it is not a company.** v1 joins four mechanisms with “and”
(G5): cylinder custody, 15 lb threshold, leak-rate math,
purchase-ledger export. Each slice has a host:

| Slice | Occupant | Label |
| --- | --- | --- |
| Cylinder serial at use | ST: custom field on the material **or** “Refrigerant Usage Log” form (same permits page) | `exact` for capture-on-the-job |
| Invoice-item usage report | ST Invoice Items report filtered by refrigerant SKU | `exact` for the report the hunt called “the gap” |
| Cylinder ledger + QR + leak rate + EPA HAWK | [RefriTrak](https://www.refritrak.com/en/features): “Track disposable, refillable, and recovery cylinders”; “ServiceTitan Integration … Automatically sync work orders and track refrigerant consumption per job” | `exact` for the commercial ledger; ST row is the class-2 consult claim (write-time quote not independently fetched — do not upgrade that integration to `exact` without the SoR write-path page) |
| 15 lb + leak-rate calculator + cert tracking | [RefrigerantTrack](https://refrigeranttrack.com/) | `adjacent_pain` / commercial SKU (standalone, not ST-placed) |

Calibration: no single logo selling the bundle is not vacancy.
Leftover “it doesn’t sit on the ST dispatch/invoice write path” is
auto-reject 5 (orchestration around the SoR primitive) or auto-reject
7 (sidecar ST does not consult). The hunt labeled RefrigerantTrack
`adjacent_pain` for “no ServiceTitan write-time placement” and then
kept Sparse. That leftover *is* the file-on / add-to-host reject.

---

## The seven name-only keeps

No YAML, no incumbents, no `keep_gate`. Independently, the names
collapse onto host primitives or named commercial SKUs. These are
occupancy sketches from fetched/vendor pages this run, not full
finder cards. They are enough to reject `as_company` Sparse.

### ServiceTitan warranty packet builder

ST already books warranty jobs, tracks warranty parts through vendor
credit, and publishes a manufacturer billing workflow (holding /
recognized / adjustment invoice billed to the manufacturer)
([Warranties (Manufacturer): recommended workflow](https://help.servicetitan.com/docs/warranties-manufacturer-recommended-workflow)).
[JB Warranties / JB360](https://marketplace.servicetitan.com/partner/jb-warranties)
is the marketplace claims path (“access JB Warranties plan and claims
data directly within ServiceTitan”). Occupied leftover is a form pack
or an issue on JB360 / ST Warranty Tracking. Auto-reject 1 or 5.

### Clio crash-report DOT order helper

Ordering crash reports is
[CrashDocs](https://www.crashdocs.org/) (CARFAX) and
[LexisNexis BuyCrash](https://policereports.lexisnexis.com/ui/home).
LexisNexis also sells
[Police Records Retrieval](https://risk.lexisnexis.com/products/police-records-retrieval)
to commercial buyers. Clio’s PI add-on was already used *in this
sweep* as an Occupied drop for liens/records. A Clio-flavored order
button is auto-reject 5 (add to Clio) or auto-reject 2 (Zapier around
BuyCrash). Accelirate already sells crash-portal RPA into legal
systems. Not a vacant process on Clio.

### Mindbody intro-offer duplicate detection

Mindbody intro offers are already one-purchase-per-client. Vendor
docs (search snippet of the support article; the Salesforce page was
JS-thin this run): “An introductory offer is a pricing option that a
client can only purchase once.” Duplicate *profiles* are the named
host leftover, and Mindbody already ships
[Locate Duplicate Clients](https://support.mindbodyonline.com/s/article/203259613-Locate-Duplicate-Clients-tool)
and
[Merge Duplicate Clients](https://support.mindbodyonline.com/s/article/203259603-Merge-Duplicate-Clients-tool).
Cross-email identity is the merge tool, not a company. Occupied ~7.
Auto-reject 1.

### SimplePractice supervision-hours accumulator

SimplePractice already designates supervisor/supervisee and gates
note review
([Designating a clinician as a supervisor or supervisee](https://support.simplepractice.com/hc/en-us/articles/41897700430989-Designating-a-clinician-as-a-supervisor-or-supervisee)).
Hours toward licensure are a shipping SKU:
[Time2Track](https://time2track.com/lcsw) — “your training and
supervision hours will be ready to go when it’s time to apply for
your LCSW”; “see your total fieldwork and supervision hours”.
SupervisionAssist / Guidara sit in the same aisle. “On SimplePractice
appointment rows” is auto-reject 5. Occupied as a company.

### SimplePractice medical-necessity guard

SP requires a diagnosis to create a claim, ships diagnosis +
treatment plans, and **scrubs claims before submit**
([Filing primary claims](https://support.simplepractice.com/hc/en-us/articles/360045195192-Filing-primary-claims-in-SimplePractice);
[Resolving scrub errors](https://support.simplepractice.com/hc/en-us/articles/115002721786-Resolving-scrub-errors)
— page was Cloudflare-gated this run; treat the scrub-error *title*
as NEED_EVIDENCE for a contiguous quote, not as a kill of the seat).
Blocking submit without a treatment plan is a checkbox on that scrub.
Auto-reject 5 / `file_on` SP. Occupied.

### Jane referral-letter draft

Jane’s own guide **is** this seat:
[Letters in Jane](https://jane.app/guide/letters-in-jane) —
“Often you need to send Progress Reports, Doctor Letters or other
Form style Letters”; Chart Template Library example; print as
letterhead with clinic letterhead, client info, doctor contact, and
signature. Occupied ~7. Auto-reject 1. Leftover “AI draft” is a
plugin on that template, not a company.

### SimplePractice superbill tracker

SP already creates and locks superbills
([Creating superbills](https://support.simplepractice.com/hc/en-us/articles/360058860991-Creating-superbills)).
Patient-side OON reimbursement tracking is
[Mentaya](https://mentaya.com/) (“Submit out-of-network claims
automatically”; SimplePractice iCal sync in their help center) and
[Reimbursify](https://reimbursify.com/) (claim status dashboard).
“Tracker linked to SP superbill IDs” is add-EHR to Mentaya
(auto-reject 5) or file the status on SP. Occupied.

---

## Missed-search pattern (why the keeps look Sparse)

Sweep 1 searched class 1 until the SoR admitted a gap, then stopped.
That is the opposite of the playbook.

| Class | What sweep 1 did | What a G2 pass requires |
| --- | --- | --- |
| 1 `sor_primitive` | Found the “we don’t have a dedicated module” sentence and treated it as vacancy | That sentence is occupancy of the **workaround primitive** (Skills, custom fields, Invoice Items, intro-offer flag, Jane letter templates) |
| 2 `dropin_addon` | Not run on the three cards | JB360, RefriTrak-on-ST, Mentaya-on-SP iCal |
| 3 `commercial_sku` | RefrigerantTrack only, labeled adjacent because it wasn’t ST-placed | Voosh, Cointab, RefriTrak, Time2Track, CrashDocs/BuyCrash |
| 4 `tracker_leftover` | Not run | A filed “auto-expire Skills” request **is** occupancy for auto-reject 5 |

`exact_mechanics_density: 0` with two rows from the SoR’s own “here
is how you configure it” article is a scoring bug. Steelman ceilings
of 2.5–3 were not raised when the same article described Skills,
forms, and reports. G9: missed-search is not a low ceiling.

---

## Tracker / method accuracy (short)

What the sweep got right:

- Fail-closed philosophy in the tracker’s pitchable definition.
- Dropping Eaglesoft lab tracking, Jane/SP waitlist fill, Clio PI
  add-on, and late-cancel Autopay bundles as Occupied.
- Using `skills/niche-saas-finder/` rather than the parent devtools
  playbook (no Landlock / Kroxylicious / `CREATE PUBLICATION` on these
  cards).
- Spot-checking that several SoR quotes are real contiguous
  substrings (ST permits page, RefrigerantTrack 15 lb line, Toast
  “payouts directly to you”).

What it got wrong:

1. **`keep_gate: pass` with two incumbents.** Keep requires ≥5 named
   incumbents (or an explicit “could not find 5”). 2 ≠ 5.
2. **Names as keeps.** Seven of ten have no card. `researched = 95`
   cannot be audited; non-keep iteration cards were deleted by
   design, which is fine for drops and fatal for unverifiable keeps.
3. **Vacant-process passed beside the host primitive.** G4.
4. **`file_on: none` while leftovers name Toast/ServiceTitan.** G3.
5. **Misattributed Toast Reconciliation quote.** G1.
6. **“Provisional, subagent-scored, spot-verified”** is not a latch.
   Gate-bind is the latch.

Later commits on the same PR (`saas-04`–`saas-12`) grow incumbent
tables to six rows. That fixes the *count* and not the occupancy
error if leftovers still name the SoR with Sparse company +
`keep_gate: pass`. Those cards were not re-rated here.

---

## Disposition

Sweep 1 does not contain a Sparse/Greenfield company keep.

If the hunt continues toward 1000, the useful move is not more
aisle-switch keeps in the same shape. Invalidate these ten, file them
on the hosts above, and harden **one** reference file for the failure
mode that produced them: **SoR “no dedicated module” quote ≠ vacant
process; leftover that names the SoR is `file_on`, not Sparse.**
That is already written in gate-bind G3/G4/G6. The cards did not
apply it.
