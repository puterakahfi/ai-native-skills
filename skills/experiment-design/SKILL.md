---
name: experiment-design
description: Design minimum viable experiments for product and business learning. Use when value is plausible but assumptions are unverified, especially after business-value-alignment recommends EXPERIMENT_FIRST before PRD, MVP, or implementation.
license: MIT
metadata:
  ai-native-skills.version: 1.0.0
  ai-native-skills.author: puterakahfi
  ai-native-skills.type: skill
  ai-native-skills.implements: ai-native-core/contracts/skills/product-management/experiment-design.contract.yaml
  ai-native-skills.related_skills: '[''business-value-alignment'', ''user-research'', ''product-manager'', ''product-requirements'', ''decision-making'', ''spike'', ''cro'']'
---

# Experiment Design

## Overview

Use this skill to turn uncertain product or business value into the smallest ethical test that can produce a decision. It is the bridge between:

```text
business-value-alignment says EXPERIMENT_FIRST
    ↓
experiment-design creates falsifiable learning plan
    ↓
PRD/MVP decision becomes evidence-backed
```

This skill implements:

```text
ai-native-core/contracts/skills/product-management/experiment-design.contract.yaml
```

Core principle:

```text
Do not build the product when a smaller experiment can answer the riskiest assumption.
```

## When to Use

Use when:

- `business-value-alignment` returns `EXPERIMENT_FIRST`
- a product idea has plausible value but weak evidence
- the user wants to validate demand before building
- MVP scope feels too large for the evidence available
- the team needs a landing page, waitlist, prototype, concierge, fake-door, interview, or pricing test
- a PRD has major unknowns that should be tested before implementation

Do not use for:

- full PRD writing; use `product-requirements` after experiment results exist
- production implementation; use `new-feature-workflow`
- generic research synthesis; use `user-research`
- pure technical feasibility spikes unless the riskiest assumption is technical feasibility

## Required Output

Always produce an experiment spec in this shape:

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
3. <step>

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

## Procedure

1. **Start from value.** Completion: link the experiment to a value alignment brief or explicitly state the value hypothesis.
2. **Name the riskiest assumption.** Completion: one assumption is identified as the primary thing the experiment must test.
3. **Make the hypothesis falsifiable.** Completion: a reasonable result can prove the hypothesis wrong.
4. **Choose the smallest test.** Completion: the test is materially cheaper/faster than building the full solution.
5. **Define success before execution.** Completion: PASS, PARTIAL, and FAIL thresholds are written before the experiment runs.
6. **Add guardrails.** Completion: the experiment cannot rely on misleading claims, unsafe data collection, or harmful user treatment.
7. **Plan data collection.** Completion: evidence source, storage, and privacy handling are explicit.
8. **Set decision rule.** Completion: every outcome maps to a next action.

## Experiment Type Guide

| Experiment type | Use when | Example |
|---|---|---|
| `landing_page_waitlist` | Demand/value proposition needs validation | Landing page + waitlist for AI affiliate campaign kits |
| `prototype_test` | UX or comprehension is uncertain | Clickable prototype with 5 target users |
| `fake_door_test` | Need to measure interest in a capability before building | CTA for “Generate campaign kit” with follow-up invite |
| `concierge_test` | Workflow value can be manually delivered first | Manually create affiliate campaign kits for 5 users |
| `wizard_of_oz` | User sees product behavior but backend is manual | AI-like recommendations generated manually behind scenes |
| `manual_service_pilot` | Operational value needs validation before automation | Run the service by hand for one cohort |
| `interview_script` | Need qualitative validation before any funnel | Structured interviews around pain and alternatives |
| `smoke_test` | Need fast market signal | Ad/post/email to a landing page |
| `pricing_test` | Willingness to pay is uncertain | Paid beta CTA or pricing page test |
| `content_or_offer_test` | Messaging/positioning is uncertain | Compare value props in posts/landing copy |
| `technical_spike` | Feasibility is the riskiest assumption | Timeboxed API/model/prototype spike |

## Integration Rules

### With `business-value-alignment`

If verdict is:

```text
EXPERIMENT_FIRST
```

then produce an experiment spec before PRD or build. Preserve these trace links:

```text
business value → hypothesis → riskiest assumption → success criteria → decision rule
```

### With `product-development-workflow`

Use during discovery or MVP slicing when the value is plausible but unproven:

```text
discovery → business-value-alignment → experiment-design → PRD/MVP recommendation
```

If the user asks to stop after PRD/MVP recommendation, include the experiment recommendation as an alternative to build when evidence is weak.

### With `product-requirements`

Do not turn a weak experiment into fake certainty. PRDs should reference experiment evidence when available and list untested assumptions as open questions or risks.

### With `spike`

Use `spike` only when the riskiest assumption is technical feasibility. Most product/business assumptions should use a customer, funnel, prototype, or concierge experiment instead.

## Example — Affiliate Product

```markdown
# Experiment Design

## Hypothesis
Affiliators will join a waitlist for AI-generated campaign kits if the offer promises faster campaign setup and shows realistic examples.

## Target Segment
- Primary segment: solo affiliators promoting digital products through social/content channels
- Qualification criteria: currently publishes affiliate links or campaigns at least weekly
- Exclusions: enterprise affiliate teams and agencies

## Riskiest Assumption
Affiliators trust AI-generated campaign assets enough to try them in real campaigns.

## Smallest Test
- Experiment type: landing_page_waitlist
- What we will do: landing page with 3 sample campaign kits, waitlist CTA, and interview booking CTA
- What we will not build yet: dashboard, account system, integrations, payment, automated generation backend

## Setup Steps
1. Draft landing page with problem, samples, and CTA.
2. Publish to a small qualified audience.
3. Track waitlist signups, interview bookings, and qualitative objections.

## Success Criteria
- PASS if: 20 qualified signups and 5 interview bookings in 7 days
- PARTIAL if: 8-19 qualified signups or strong qualitative interest with unclear trust objections
- FAIL if: fewer than 8 qualified signups and no repeated pain pattern

## Guardrail Criteria
- No unrealistic income claims.
- Sample copy must be labeled editable draft.
- Lead capture must disclose follow-up usage.

## Duration / Sample Threshold
- Timebox: 7 days
- Minimum signal: 100 qualified visitors or targeted outreach to 30 qualified affiliators

## Data Collection Plan
- Signal source: signup form, analytics events, interviews
- Evidence stored at: experiment brief / analytics screenshot / interview notes
- Consent/privacy note: collect only contact and stated campaign context

## Decision Rule
- PASS → write PRD and MVP slice for campaign kit generator
- PARTIAL → run 5 interviews and narrow value proposition
- FAIL → stop dashboard idea and test a different affiliator pain point
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
2. **Testing the easiest assumption.** Pick the assumption that would kill the opportunity if false.
3. **No failure threshold.** Without FAIL criteria, every result becomes “promising.”
4. **Misleading demand signals.** Waitlist signups are weaker than qualified interviews, usage, or payment intent; label confidence honestly.
5. **Unsafe fake doors.** Do not trick users in ways that harm trust; explain availability or follow-up clearly.
6. **Ignoring guardrails.** Experiments can create brand, privacy, or trust debt even when no product is built.
7. **Skipping the decision.** The output is not done until PASS/PARTIAL/FAIL maps to next steps.

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
