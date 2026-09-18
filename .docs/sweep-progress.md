# SaaS sweep to 1000 — progress tracker

Skill: `skills/niche-saas-finder/` (branch `niche`, PR #11).
Stop when `keeps >= 3` OR `researched >= 1000`.
`researched` = emitted candidate cards per `output-template-saas.md`, not raw seats.
`pitchable` = `as_company` Sparse (2-4) / Greenfield (0-1) + 0 auto-rejects +
  3/3 falsification + >= 5 verified incumbents + `keep_gate: pass` (G1-G9).

## Counter (sweep 1 + catch-up + wave 2)

- Researched: **167** cards
- Keeps: **17** (provisional, subagent-scored, spot-verified)
- Drops: **150** (mostly Occupied / file_on native primitive)

| SoR | cards | keeps |
| --- | ---: | ---: |
| Patterson Eaglesoft (Windows) | 15 | 0 |
| Dentrix (Windows) | 11 | 0 |
| Clio cloud | 16 | 2 |
| MyCase cloud | 11 | 1 |
| ServiceTitan cloud | 26 | 6 |
| Housecall Pro cloud | 11 | 0 |
| Toast cloud | 16 | 1 |
| Square cloud | 11 | 0 |
| Mindbody cloud | 18 | 2 |
| Buildertrend cloud | 10 | 0 |
| Jane cloud | 15 | 2 |
| SimplePractice cloud | 17 | 3 |
| **Total** | **167** | **17** |

Catch-up hunts logged: Clio trust accounting (+5, 1 keep), ServiceTitan
payroll run 1 (+5, 3 keeps), ServiceTitan payroll run 2 (+6, 0 keeps),
Toast inventory (+6, 0 keeps), Buildertrend change orders (+5, 0 keeps).

Wave 2 (fresh steps, closed aisles avoided): Housecall invoicing (+6, 0),
Eaglesoft claims (+5, 0), Dentrix eligibility (+6, 0), MyCase intake (+6,
1 keep), Square scheduling (+6, 0), Mindbody scheduling (+6, 1 keep),
Jane billing (+5, 1 keep), SimplePractice telehealth (+5, 0).

## Top 3 keeps (see `.idea/`)

1. `saas-01` ServiceTitan — technician license-expiry dispatch guard (Sparse 2.5)
2. `saas-02` Toast — third-party delivery payout reconciliation (Sparse 3)
3. `saas-03` ServiceTitan — EPA refrigerant cylinder ledger (Sparse 2.5)

Other keeps: ServiceTitan warranty packet builder, Clio crash-report DOT
order helper, Mindbody intro-offer duplicate detection, SimplePractice
supervision hours accumulator, SimplePractice medical-necessity guard,
Jane referral-letter draft, SimplePractice superbill tracker,
`saas-04` Clio dormant-trust escheatment sweeper (Sparse 3),
`saas-05` ServiceTitan commission true-up ledger (Sparse 3),
`saas-06` ServiceTitan versioned spiff plan engine (Sparse 3),
`saas-07` ServiceTitan recoverable draw ledger (Sparse 3),
`saas-08` MyCase conflict-check gate (Sparse 3),
`saas-09` Mindbody reliability-weighted waitlist promoter (Sparse 3),
`saas-10` Jane OON superbill-to-reimbursement tracker (Sparse 3).

## Typical drop reasons (correct Occupied)

- Eaglesoft Lab Tracking native ships headline (`Red - Indicates the lab
  case is overdue...`) — exact.
- Jane Wait List Notifications / SimplePractice Fill Slot (`offer the time
  slot to up to 3 clients`) — exact, auto-reject 1.
- Clio Personal Injury Add-On (`track requests for medical records ...
  liens and outstanding balances`) — exact.
- Late-cancel AutoPay / recurring scored-measures — bundle of exact slices.

## Next (to 1000)

- Aisle-switch per `seat-generation-saas.md`: new workflow_step x SoR
  trips (2 trips per class-1/2 host, then switch hosts).
- Per batch: append rows here, add `.idea/saas-NN-*.yaml` keeps only,
  update counters. Delete non-keep iteration cards (do not pile Occupied).
- If keeps stay >= 3, sweep is stress-test; harden exactly one reference
  file per failure mode only when a keep is invalidated.
