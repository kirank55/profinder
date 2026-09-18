# Intake (SaaS scope gate)

Load this file at step 2 when the object is not yet a restatable seat, or
when the request is a hunt. Do not load
[seat-generation-saas.md](seat-generation-saas.md) or
[search-playbook-saas.md](search-playbook-saas.md) until this gate passes.

This file answers "is the object a vertical workflow seat in a named SoR
yet?" -- not "how do I search incumbents?" and not "what pain is real?"

**Grill placement and constraints. Never grill pain.** Pain questions
produce slogans. Slogans are not seats.

Interest (`dental`, `law`) is input. It never scores and never passes
this gate alone.

## Gate

Pass if any one is true:

1. **Named seat.** The user named a stack position or pasted an ADR/idea
   that restates as `candidate_seat` + `v1_as_shipped` + named ICP + SoR
   SKU/host + workflow step without slogans. If only v1 or SoR SKU/host
   is missing, ask those, then pass. Do not run the hunt questionnaire.
   A slogan ("dental SaaS", "AI for law") is not a named seat -- use the
   hunt questionnaire. Do not drop it at restatement to skip grilling.
2. **User niche minimum.** Hunt request plus a niche card where `icp`
   and `system_of_record` are **named nouns** (not "SaaS", "dental",
   "law", "AI for X"). `workflow_step` and `ship_form` may be `unset`.
3. **Explicit opt-out.** The user said they do not care / pick a stack /
   use the default inventory. Fill the niche from **exactly one**
   seed-SoR row via the interest routing table in
   [seat-generation-saas.md](seat-generation-saas.md)
   (`source: agent_opt_out`). Then pass.

Fail otherwise. Emit the intake card below. **Stop.** Do not generate
seats. Do not search. Do not invent a niche to be helpful.

One-shot with no reply: emit the card and stop. Do not fill blanks from
memory.

Follow-up answers merge into the same `niche` card. Re-run this gate. Do
not keep `intake_blocked` once `icp` and `system_of_record` are named
nouns, or the user opts out.

## Broad prompts that fail the gate

These are not seats. Do not treat them as hunt-ready:

- "give me a SaaS idea"
- "something to build" / "find a startup"
- "dental SaaS" / "AI for law" with no SoR SKU
- "find vacant seats" / "hunt product seats" with no ICP and no SoR

"SaaS" is a billing shape, not a system of record.

**Pass:** "hunt seats around Clio cloud for solo PI firms" -- named ICP
+ named SoR; generate workflow steps inside that SoR.

**Fail:** "give me a dental SaaS idea" -- emit the card, ask questions
1-2 at minimum, stop.

## Questions (max 5)

Ask only blanks. Do not ask pain, TAM, why it matters, or "what problem
are you solving?"

1. **Vertical + ICP.** Named buyer (e.g. `independent dental labs`,
   `solo PI firms`). Not `dental` / `law` alone. This is not the
   system of record.
2. **Immutable system-of-record.** Named SKU + hosting (e.g.
   `Eaglesoft on Windows`, `Clio cloud`). Vacancy is relative to this
   host. `dental` alone does not fill this field.
3. **Workflow step.** Named step in that SoR. Asked if blank; **never
   blocks intake**. Search never runs with this field unset --
   generation names it on every raw seat. If the user named a step, all
   seats stay inside that step.
4. **Ship form.** Company, OSS, or plugin/flag. If they will not say,
   `unset`. Never blocks.
5. **Unique data or distribution + hard nos.** Logs, install base,
   marketplace, sales motion, languages, leftover shapes they will not
   build. Generation filters, not scores. Never block.

Stop asking once `icp` and `system_of_record` are named, or the user
opts out. Questions 3-5 never block the gate. Do not stall a passed
niche to collect them.

## Niche card (emit on fail; copy forward on pass)

```yaml
niche:
  icp: <named or unset>
  system_of_record: <named SKU/host or unset>
  workflow_step: <named step or unset>
  ship_form: company | oss | plugin | unset
  unique_data_or_distribution: <string or unset>
  hard_nos: []
  source: user | agent_opt_out | intake_blocked
unanswered:
  - icp                 # required; omit once named
  - system_of_record    # required; omit once named
```

On fail: this card only. No candidate card. `source: intake_blocked`.
Ask the unanswered questions in the same turn.

On pass: copy `niche` onto every raw seat and every candidate card.
Seats that reach search must have `workflow_step` named. Do not emit a
second `niche_icp` block.

## After pass

- Named seat -> step 4 (restate), then 3 (deny), then 5-9. Deny does
  not run before a one-line seat exists.
- Filled niche or opt-out -> load [seat-generation-saas.md](seat-generation-saas.md).
  Generate >=5 raw seats **inside this niche**. Then `SKILL.md` steps
  3-9. Do not deny-check an empty hunt.
- User answers never replace incumbent URLs. "Nobody does this" is not a
  row. Unique data does not raise `exact_mechanics_density`.
