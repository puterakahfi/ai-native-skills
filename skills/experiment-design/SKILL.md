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

> **Hypothesis before test. Minimum detectable effect before sample size. No peeking at results before the predetermined end.**

## Hard Rule

```
Do not build the product when a smaller experiment can answer the riskiest assumption.
```

## When to Use

- `business-value-alignment` returns `EXPERIMENT_FIRST`
- A product idea has plausible value but weak evidence
- MVP scope feels too large for the evidence available

Do not use for: full PRD writing (`product-requirements`); production implementation (`new-feature-workflow`); generic research synthesis (`user-research`).

---

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

---

## Procedure

1. **Start from value.** Link experiment to a value alignment brief or state the value hypothesis.
2. **Name the riskiest assumption.** One assumption identified as the primary thing the experiment must test.
3. **Make the hypothesis falsifiable.** A reasonable result can prove the hypothesis wrong.
4. **Choose the smallest test.** Materially cheaper/faster than building the full solution.
5. **Define success before execution.** PASS, PARTIAL, and FAIL thresholds written before experiment runs.
6. **Add guardrails.** No misleading claims, unsafe data collection, or harmful user treatment.
7. **Plan data collection.** Evidence source, storage, and privacy handling explicit.
8. **Set decision rule.** Every outcome maps to a next action.

---

## Quality Gates

- Hypothesis is falsifiable.
- Riskiest assumption is explicit and singular.
- Smallest test is smaller than building the product.
- PASS/PARTIAL/FAIL thresholds exist before execution.
- Guardrails cover privacy, trust, safety, or brand risk.
- Data collection plan names signal source and storage.
- Decision rule maps every outcome to next action.
- Experiment states what will not be built yet.

---

## References

- [Experiment Type Guide](references/experiment-types.md) — all 11 experiment types with use-cases and examples
- [Pitfalls, Checklist & Example](references/pitfalls-checklist-example.md) — common pitfalls, verification checklist, worked example
