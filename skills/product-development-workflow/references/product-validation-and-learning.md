# Product Validation and Learning Composition

## Purpose

Prove whether the released product creates observable value for real users and produce an attributable next decision.

## Semantic boundary

```text
engineering verification = does the software work correctly?
Product Acceptance      = does it satisfy the approved PRD/MVP?
Product Validation      = does it create observable value for real users?
```

A deployed, technically correct, accepted release is not lifecycle-complete without reviewed real-usage evidence.

## Ownership

Compose `user-research`, `experiment-design`, `business-value-alignment`, `observability-design`, `product-manager`, `decision-making`, and `decision-provenance`. `skill-evolution` reviews reusable findings afterward.

Do not create a separate `product-validation` skill yet. Verdict: `LOCAL_ONLY`; the procedure remains phase composition until independent reuse and eval evidence justify promotion.

## Evidence package

```yaml
product_validation:
  product_and_release: string
  hypothesis: string
  target_users: []
  real_workflow: string
  expected_signals: []
  observed_behavior: []
  quantitative_evidence: []
  qualitative_evidence: []
  limitations: []
  discrepancies: []
  evidence_status: PASS | LIMITED | NOT_VERIFIED | FAIL
  decision: continue | improve | pivot | narrow | stop
  decision_owner: string
  decision_record_ids: []
  next_prd_or_backlog_actions: []
  capability_evolution_verdicts: []
```

## Evidence rules

- Use appropriate analytics, experiments, interviews, observation, support evidence, incidents, adoption/retention, task completion, or outcome signals.
- Activity is not value unless the relationship was declared.
- Too little usage is `LIMITED`; absent or unattributable evidence is `NOT_VERIFIED`.
- Do not turn missing evidence into PASS or FAIL.
- Separate release defects, usability failures, value-hypothesis failures, and measurement limitations.
- Continue/improve/pivot/narrow/stop requires an attributable owner and decision provenance.
- Record the next PRD/backlog action.
- Run `skill-evolution`; shared capabilities never change automatically.

## Completion gate

The workflow completes only when reviewed real-user evidence, limitations, an owned next decision, decision records, and the next PRD/backlog action are explicit. A release with no users or evidence remains incomplete.
