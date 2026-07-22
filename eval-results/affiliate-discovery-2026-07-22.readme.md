# Affiliate Discovery Behavioral Evaluation

Source cases:

- `puterakahfi/visualmate#98`
- `puterakahfi/visualmate#99`
- `puterakahfi/ai-native-skills#70`

## Result

```text
overall: APPLIED
business-value-alignment: APPLIED
experiment-design: APPLIED
user-research: APPLIED
promotion_verdict: EVAL_ONLY
```

All required patterns were present and no forbidden pattern was found for the three natural-trigger cases.

## Evidence boundary

This is provisional behavioral evidence. The outputs were captured in an active ChatGPT project conversation that already had access to VisualMate context and governing skill documents. The natural triggers themselves contained no skill names, but the runtime was not an isolated fresh session.

The execution container could not resolve `github.com`, so the pinned canonical runner repository could not be cloned. Classification used the exact casefold substring logic from the fetched pinned `ai-native-core/scripts/run-eval.py` source. Final promotion or claims of isolated natural activation still require:

1. a fresh-runtime capture;
2. direct execution of the pinned canonical runner;
3. preservation of model/runtime/context provenance.

No skill body, workflow, or core contract patch is justified by this run.
