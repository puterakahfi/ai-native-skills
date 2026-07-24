# Affiliate Discovery Behavioral Evaluation

Source cases:

- `puterakahfi/visualmate#98`
- `puterakahfi/visualmate#99`
- `puterakahfi/ai-native-skills#70`

## Result

```text
overall: APPLIED
workflow-router: APPLIED
product-development-workflow: APPLIED
business-value-alignment: APPLIED
experiment-design: APPLIED
user-research: APPLIED
decision-provenance: APPLIED
promotion_verdict: EVAL_ONLY
```

All required patterns were present and no forbidden pattern was found for the six natural-trigger cases.

The composition behavior remained correct:

```text
unverified opportunity
→ product-development-workflow
→ discovery
→ business-value-alignment
→ experiment-design
→ after_experiment_design stop point
→ no implementation authority

agent-authored commission proposal
→ NON_AUTHORITATIVE
→ PROVENANCE_BLOCKED
→ ROUTE_FOR_APPROVAL
```

## Canonical runner verification

The captured outputs were executed directly with the pinned canonical runner:

```text
runner: ai-native-core/scripts/run-eval.py
core_ref: 5c4c6f21859636a4a143a511030879c9923b2ef1
workflow_run_id: 29928054775
artifact_id: 8532790125
overall: APPLIED
failed assertions: 0
```

The temporary verification workflows were removed after the run. The final PR diff does not add product-specific GitHub Actions automation to the shared repository.

## Evidence boundary

The runner result is direct and pinned, but the response generation itself occurred in an active ChatGPT project conversation that already had access to VisualMate context and governing skill documents. The natural triggers contained no skill names, but this was not an isolated fresh-session generation run.

Remaining gate:

1. repeat generation in an isolated fresh runtime;
2. preserve model, runtime, and context provenance;
3. rerun the captured outputs after relevant model or context changes.

No skill body, workflow methodology, core contract, or runtime framework patch is justified by this run. The verified reusable change remains regression coverage only.
