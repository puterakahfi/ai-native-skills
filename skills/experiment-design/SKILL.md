---
name: experiment-design
description: Design minimum viable experiments for product and business learning. Use when value is plausible but assumptions are unverified, especially after business-value-alignment recommends EXPERIMENT_FIRST before PRD, MVP, or implementation.
license: MIT
metadata:
  ai-native-skills.version: 1.0.0
  ai-native-skills.author: puterakahfi
  ai-native-skills.type: skill
  ai-native-skills.implements: ai-native-core/contracts/skills/product-management/experiment-design.contract.yaml
  ai-native-skills.related_skills: '["business-value-alignment", "user-research", "product-manager", "product-requirements", "decision-making", "spike", "cro"]'
---

# Experiment Design

## Hard Rule

```
Do not build the product when a smaller experiment can answer the riskiest assumption.
```

## When to Use

- `business-value-alignment` returns `EXPERIMENT_FIRST`
- A product idea has plausible value but weak evidence
- MVP scope feels too large for the evidence available

Do not use for: full PRD writing (`product-requirements`); production implementation (`new-feature-workflow`); generic research synthesis (`user-research`).

## Required Output

```markdown
# Experiment Design

## Hypothesis
<If target segment experiences X, then test Y will show Z value because ...>

## Target Segment
- Primary segment: <who>
- Qualification criteria: <who counts as valid signal>
- Exclusions: <who is not part of this experiment>

## Riskiest Assumption
<the assumption most likely to invalidate the opportunity if false>

## Smallest Test
- Experiment type: concierge_test | landing_page_waitlist | prototype_test | fake_door_test | wizard_of_oz | manual_service_pilot | interview_script | smoke_test | pricing_test | content_or_offer_test | technical_spike
- What we will do: <minimal setup>
- What we will not build yet: <explicit non-build boundary>

## Setup Steps
1. <step>
2. <step>

## Success Criteria
- PASS if: <measurable threshold>
- PARTIAL if: <ambiguous-but-useful threshold>
- FAIL if: <minimum threshold not met>

## Guardrail Criteria
- <privacy, trust, safety, quality, cost, performance, or brand guardrail>

## Duration / Sample Threshold
- Timebox: <duration>
- Minimum signal: <n users / n events / n interviews / n signups>

## Data Collection Plan
- Signal source: <where evidence comes from>
- Evidence stored at: <doc/file/dashboard/link>
- Consent/privacy note: <how data is handled>

## Decision Rule
- PASS → <PRD/MVP/build next step>
- PARTIAL → <follow-up discovery/narrowing>
- FAIL → <stop/pivot/alternative>

## Risks and Mitigations
- <risk> → mitigation: <mitigation>
```

## Experiment Type Guide

| Experiment type | Use when | Example |
|---|---|---|
| `landing_page_waitlist` | Demand/value proposition needs validation | Landing page + waitlist for AI affiliate campaign kits |
| `prototype_test` | UX or comprehension is uncertain | Clickable prototype with 5 target users |
| `fake_door_test` | Measure interest before building | CTA for "Generate campaign kit" with follow-up invite |
| `concierge_test` | Workflow value can be manually delivered first | Manually create affiliate campaign kits for 5 users |
| `wizard_of_oz` | User sees product behavior but backend is manual | AI-like recommendations generated manually |
| `manual_service_pilot` | Operational value needs validation before automation | Run the service by hand for one cohort |
| `interview_script` | Need qualitative validation before any funnel | Structured interviews around pain and alternatives |
| `smoke_test` | Need fast market signal | Ad/post/email to a landing page |
| `pricing_test` | Willingness to pay is uncertain | Paid beta CTA or pricing page test |
| `content_or_offer_test` | Messaging/positioning is uncertain | Compare value props in posts/landing copy |
| `technical_spike` | Feasibility is the riskiest assumption | Timeboxed API/model/prototype spike |

## Procedure

1. **Start from value.** Link experiment to a value alignment brief or state the value hypothesis.
2. **Name the riskiest assumption.** One assumption identified as the primary thing the experiment must test.
3. **Make the hypothesis falsifiable.** A reasonable result can prove the hypothesis wrong.
4. **Choose the smallest test.** Materially cheaper/faster than building the full solution.
5. **Define success before execution.** PASS, PARTIAL, and FAIL thresholds written before experiment runs.
6. **Add guardrails.** No misleading claims, unsafe data collection, or harmful user treatment.
7. **Plan data collection.** Evidence source, storage, and privacy handling explicit.
8. **Set decision rule.** Every outcome maps to a next action.

## Example — Affiliate Product

```markdown
## Hypothesis
Affiliators will join a waitlist for AI-generated campaign kits if the offer promises faster setup and shows realistic examples.

## Riskiest Assumption
Affiliators trust AI-generated campaign assets enough to try them in real campaigns.

## Smallest Test
- Type: landing_page_waitlist
- What we will do: landing page with 3 sample kits, waitlist CTA, interview booking CTA
- What we will not build yet: dashboard, account system, integrations, payment, automated generation

## Success Criteria
- PASS if: 20 qualified signups and 5 interview bookings in 7 days
- PARTIAL if: 8–19 signups or strong qualitative interest with unclear trust objections
- FAIL if: fewer than 8 signups and no repeated pain pattern

## Guardrails
- No unrealistic income claims. Sample copy labeled editable draft. Lead capture must disclose follow-up usage.

## Decision Rule
- PASS → write PRD and MVP slice for campaign kit generator
- PARTIAL → run 5 interviews and narrow value proposition
- FAIL → stop dashboard idea, test a different affiliator pain point
```

## Quality Gates

- Hypothesis is falsifiable.
- Riskiest assumption is explicit and singular.
- Smallest test is smaller than building the product.
- PASS/PARTIAL/FAIL thresholds exist before execution.
- Guardrails cover privacy, trust, safety, or brand risk.
- Data collection plan names signal source and storage.
- Decision rule maps every outcome to next action.
- Experiment states what will not be built yet.

## Common Pitfalls

1. **Building the MVP instead of testing.** If the test requires most of the product, it is not the smallest test.
2. **Testing the easiest assumption.** Pick the assumption that kills the opportunity if false.
3. **No failure threshold.** Without FAIL criteria, every result becomes "promising."
4. **Misleading demand signals.** Waitlist signups are weaker than qualified interviews, usage, or payment intent.
5. **Unsafe fake doors.** Do not trick users in ways that harm trust; explain availability or follow-up.
6. **Ignoring guardrails.** Experiments can create brand, privacy, or trust debt even without a product.
7. **Skipping the decision.** Output is not done until PASS/PARTIAL/FAIL maps to next steps.

## Verification Checklist

- [ ] Experiment traces to a value hypothesis or value alignment brief.
- [ ] Target segment and qualification criteria are explicit.
- [ ] Riskiest assumption is singular and material.
- [ ] Hypothesis is falsifiable.
- [ ] Experiment type is named.
- [ ] Smallest test says what will and will not be built.
- [ ] Success criteria include PASS, PARTIAL, and FAIL thresholds.
- [ ] Guardrail criteria exist.
- [ ] Duration or sample threshold exists.
- [ ] Data collection plan names signal source, storage, and privacy/consent handling.
- [ ] Decision rule maps every outcome to PRD/MVP, further discovery, pivot, or stop.
