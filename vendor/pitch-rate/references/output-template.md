# Output template

Emit this block as the verdict. Markdown table + lists is fine. Fenced JSON is fine. Do not add an overall score out of 100.

```text
object_under_review: idea | adr | pr_process
decision: PITCH | KILL | NEED_EVIDENCE | FILE_ON_X

as_company: <band> <0-10>
as_oss: <band> <0-10>
as_plugin: <band> <0-10>

problem_density: <0-10>  (cite incumbent rows)
exact_mechanics_density: <0-10>  (cite exact rows only)

incumbents:
  - name:
    url:
    quote:
    seat_match: exact | adjacent_pain | language_scoped | wrong_substrate | obsolete | price_packaging
    leftover:

auto_rejects_fired: [] or list
falsification:
  1_vacant_process: pass | fail
  2_not_a_wrapper: pass | fail
  3_mechanical_gap: pass | fail

steelman:
  occupancy: <0-10>
  why_build:

v1_as_shipped: <one paragraph>
physics_claims: ok | unsourced | implausible
file_on: <incumbent + issue/docs URL, or none>
deny_catalog: complete | incomplete
```

## Self-check (fail the verdict if any box is unchecked)

- [ ] `object_under_review` matches the user’s last instruction (`idea` if they said “rate the ideas”).
- [ ] Steelman written **before** density numbers.
- [ ] At least 5 incumbents with URL + quote, **or** explicit “could not find 5” and why that is not a free pass.
- [ ] Every density score cites supporting rows.
- [ ] Exact-mechanics density uses `exact` rows only.
- [ ] Published exact-mechanics density is ≤ steelman occupancy unless new named evidence raised the ceiling.
- [ ] No overall /100.
- [ ] Unread or empty fetches are `NEED_EVIDENCE`, not invented quotes.
- [ ] Previous ADR ratings used only as deny-list priors, not as this idea’s rubric.
- [ ] Claim-hygiene failures did not auto-fill Occupied for the whole seat.
