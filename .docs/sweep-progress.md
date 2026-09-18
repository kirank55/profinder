# SaaS sweep to 1000 — progress tracker

Skill: `skills/niche-saas-finder/` (branch `niche`, PR #11).
Stop when `keeps >= 3` OR `researched >= 1000`.
`researched` = emitted candidate cards per `output-template-saas.md`, not raw seats.
`pitchable` = `as_company` Sparse (2-4) / Greenfield (0-1) + 0 auto-rejects +
  3/3 falsification + >= 5 verified incumbents + `keep_gate: pass` (G1-G9).

## Counter (sweep 1)

- Researched: **95** cards
- Keeps: **10** (provisional, subagent-scored, spot-verified)
- Drops: **85** (mostly Occupied / file_on native primitive)

| SoR | cards | keeps |
| --- | ---: | ---: |
| Patterson Eaglesoft (Windows) | 10 | 0 |
| Dentrix (Windows) | 5 | 0 |
| Clio cloud | 11 | 1 |
| MyCase cloud | 5 | 0 |
| ServiceTitan cloud | 15 | 3 |
| Housecall Pro cloud | 5 | 0 |
| Toast cloud | 10 | 1 |
| Square cloud | 5 | 0 |
| Mindbody cloud | 12 | 1 |
| Buildertrend cloud | 5 | 0 |
| Jane cloud | 10 | 1 |
| SimplePractice cloud | 12 | 3 |
| **Total** | **95** | **10** |

## Top 3 keeps (see `.idea/`)

1. `saas-01` ServiceTitan — technician license-expiry dispatch guard (Sparse 2.5)
2. `saas-02` Toast — third-party delivery payout reconciliation (Sparse 3)
3. `saas-03` ServiceTitan — EPA refrigerant cylinder ledger (Sparse 2.5)

Other keeps: ServiceTitan warranty packet builder, Clio crash-report DOT
order helper, Mindbody intro-offer duplicate detection, SimplePractice
supervision hours accumulator, SimplePractice medical-necessity guard,
Jane referral-letter draft, SimplePractice superbill tracker.

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
