# Niche Discovery Tracker

Branch: `niche-discovery` (from `origin/niche`, local `niche` untouched).
Skill: `skills/niche-saas-finder/SKILL.md` — hardened in this branch only. Future runs use hardened skill, never the original.
Stop condition: 3 pitchable ideas OR 100 seats researched.

Pitchable = `as_company` Sparse (2-4) / Greenfield (0-1) + zero auto-rejects + `keep_gate: pass` + falsification 1/2/3 hold + >=5 verified incumbents (or explicit could-not-find-5 + why). No /100, no TAM/WTP as occupancy.

Counters (update every seat):
- Researched: 3 / 100
- Pitchable (kept as_company): 0 / 3
- Filed/OSS-only (hold/file_on): 0
- Dropped: 3
- Current iteration: 1
- Skill hardenings: 0

Categories to cover (seed SoR inventory):
- [x] Dental: Patterson Eaglesoft on Windows (3/5 seats scored, 2 queued)
- [ ] Dental: Dentrix (named SKU/host as stated)
- [ ] Law: Clio cloud
- [ ] Law: MyCase cloud
- [ ] Home-service: ServiceTitan cloud
- [ ] Home-service: Housecall Pro cloud
- [ ] Restaurant: Toast cloud
- [ ] Retail: Square cloud
- [ ] Studio/wellness: Mindbody cloud
- [ ] Construction: Buildertrend cloud
- [ ] Clinic: Jane cloud
- [ ] Clinic: SimplePractice cloud

## Iteration log
| Iter | Skill state | Seats | Result | Hardening applied |
|------|-------------|-------|--------|-------------------|
| 1 | origin/niche HEAD 15406bf (PR #15 hardened) | 0 so far | in progress | none yet |

## Ideas
| # | Iteration | Candidate seat (icp+SoR+step) | Steelman ceiling | problem / exact density | as_company | as_oss/plugin | keep_gate | auto_rejects | file_on | Verdict: KEEP / FILE / DROP | Why (mechanical gap or occupant + quote source) |
|---|-----------|-------------------------------|------------------|-------------------------|------------|---------------|-----------|--------------|---------|------------------------------|--------------------------------------------------|
| 1 | 1 | Eaglesoft lab-case remake block at completion (indep. practices/Eaglesoft Win) | 8 | 8 / 8 | Occupied 7 | Occ 6 / Occ 6 | fail | [1] | Eaglesoft Answer 451 | DROP | Native Lab Tracking ships the step + USTech sells remake trigger as headline UX (both fetched literal quotes). G4 fail. Card: discovery/iteration-1/idea-001.yaml |
| 2 | 1 | Eaglesoft claim attachment assembly at creation (indep. practices/Eaglesoft Win) | 8 | 9 / 8 | Occupied 8 | Occ 6 / Occ 6 | fail | [1] | Patterson Vyne 43891 | DROP | Vyne plugin is the default claim form + JETT attachments + auto-send validated-claims check all fetched verbatim. DentalXChange row NEED_EVIDENCE (403). G4 fail. Card: discovery/iteration-1/idea-002.yaml |
| 3 | 1 | Eaglesoft recall enforcement at schedule-save (indep. practices/Eaglesoft Win) | 9 | 9 / 9 | Occupied 8 | Occ 6 / Occ 6 | fail | [1] | eReminders 7440 | DROP | eReminders native + status writeback + RevenueWell + Solutionreach all fetched verbatim with recall-outreach-writeback loop. G4 fail. Card: discovery/iteration-1/idea-003.yaml |
| 3 | 1 | Eaglesoft recall enforcement at schedule-save (indep. practices/Eaglesoft Win) | 9 | 9 / 9 | Occupied 8 | Occ 6 / Occ 6 | fail | [1] | eReminders 7440 | DROP | Native eReminders + status writeback + RevenueWell + Solutionreach all ship recall-read/outreach/writeback on this SoR (6 verified rows). G4 fail. Card: discovery/iteration-1/idea-003.yaml |
| 3 | 1 | Eaglesoft recall enforcement at schedule-save (indep. practices/Eaglesoft Win) | 9 | 9 / 9 | Occupied 8 | Occ 6 / Occ 6 | fail | [1] | eReminders 7440 | DROP | Native eReminders + status writeback + RevenueWell + Solutionreach all ship recall-read/outreach/writeback on this SoR (6 verified rows). G4 fail. Card: discovery/iteration-1/idea-003.yaml |
<!-- append-only; never rewrite history. On harden+delete, keep these rows, bump iteration, new cards go in discovery/iteration-N/ -->

## Skill hardenings (in niche-discovery only)
| # | Date | Trigger idea(s) | Failure mode | File(s) changed | Rule added |
|---|------|-----------------|--------------|-----------------|------------|
<!-- record each harden here -->

## Deleted ideas
- On harden: delete `discovery/iteration-N/*.yaml` cards but KEEP this tracker history. Note deletion here with commit hash.
