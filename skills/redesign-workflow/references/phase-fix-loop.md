# Phase 11 — FIX, VERIFY, AND LEARN

## Core rule

```text
Classify the defect
→ fix the correct local or shared layer
→ verify the real case
→ run skill-evolution automatically
→ promote only reusable reasoning with a regression eval.
```

Do not patch a shared skill merely because an implementation failed. First determine whether the failure came from missing reusable knowledge, ignored existing knowledge, workflow orchestration, reference quality, or local implementation.

## Step A — Defect classification

For every failed gate, record:

```text
Gate:
Observed failure:
Governing skill or workflow:
Existing relevant rule:
Defect class:
  reusable_skill_defect
  reference_knowledge_defect
  workflow_orchestration_defect
  local_implementation_defect
Candidate correction layer:
Evidence needed to prove the fix:
```

Classification rules:

- Missing reusable decision factor, reasoning step, anti-pattern, or quality gate → `reusable_skill_defect`.
- Reusable explanation or decision matrix is incomplete but too detailed for the main skill → `reference_knowledge_defect`.
- Correct skills were not loaded, phases were ordered incorrectly, or review was skipped → `workflow_orchestration_defect`.
- CSS, framework behavior, product state, route, exact breakpoint, or repository-specific component bug → `local_implementation_defect`.
- Existing rule was clear but ignored → patch the artifact or orchestration first; do not duplicate the rule.

## Step B — Apply the smallest candidate fix

Use the correction order from the defect class:

```text
Reusable skill defect
→ formulate a learning candidate
→ apply the candidate reasoning to the real surface
→ verify it
→ promote through skill-evolution after verification.

Reference knowledge defect
→ improve the reusable reference candidate
→ apply and verify
→ promote after verification.

Workflow orchestration defect
→ patch workflow composition or phase ordering
→ resume from a safe phase
→ verify the complete affected path.

Local implementation defect
→ patch only the product artifact
→ verify regression
→ keep the detail in the product repository.
```

A candidate rule is not yet shared knowledge. It becomes promotable only after the real case passes.

## Step C — Verify the real case

Run the evidence appropriate to the failure:

- render and screenshot inspection;
- mobile, tablet, laptop, and desktop checks;
- pointer, touch, keyboard, swipe, scroll, and resize behavior;
- loading, empty, error, success, permission, and edge states;
- DOM probes and accessibility checks;
- build, lint, type, unit, integration, or end-to-end tests;
- fixed-gate and preserved-gate re-scoring.

Record before and after evidence. A successful build alone is not proof that a UI/UX defect is resolved.

If verification fails, continue the bounded correction loop. Do not update shared skills from the failed attempt.

## Step D — Automatic skill-evolution review

After a fix passes verification, load:

```text
skill-evolution + skill-eval
```

Run the learning review without waiting for the user to request it.

The review must decide one of:

```text
PROMOTE_RULE
PROMOTE_REFERENCE
PROMOTE_WORKFLOW
PROMOTE_CONTRACT
EVAL_ONLY
LOCAL_ONLY
DUPLICATE
DEFERRED_UNVERIFIED
```

Promotion rules:

- Extract why the fix worked, not merely which component or code was used.
- Remove product names, route names, file paths, class names, and exact breakpoints from shared instructions.
- Preserve the decision factors, conditions, counterexamples, and trade-offs.
- Check the complete target skill and related skills for duplicate coverage.
- Patch the smallest correct layer.
- Add or update a regression eval derived from the real case.
- Run the relevant evals and contract conformance checks.
- Commit automatically only when repository access and approval policy permit it.
- Store the concrete case provenance outside the reusable `SKILL.md` body.

Examples:

```text
Local fact:
Creative Gallery used a shortcut rail on a narrow viewport.

Reusable reason:
When a small, high-value discovery set must remain visible but does not fit,
preserve discoverability through reachable overflow or component substitution;
do not hide primary choices solely to avoid layout work.
```

The local fact belongs in the product design lock or regression case. The reusable reason may belong in `adaptive-component-design` when it is new and passes transfer checks.

## Step E — Re-run from promoted knowledge

When a shared skill, reference, workflow, or contract was promoted:

1. Reload the updated source.
2. Re-run `skill-eval` for the new regression case.
3. Re-run related evals affected by the boundary.
4. Re-check the original product surface where feasible.
5. Record the promotion commit and verification result.

A skill patch without a passing regression eval is incomplete.

---

## Autonomous correction loop

```text
LOOP STATE:
  iteration:          1
  max:                5
  active_layer:       [strategy | UI | UX | voice | interaction | delight | verification]
  local_patches:      []
  learning_candidates:[]
  promotions:         []
  score_history:      []

LOOP BODY:
  1. Produce or patch the current candidate.
  2. Verify and review with evidence.
  3. If gates fail and iterations remain:
       classify defect
       apply smallest candidate fix
       iteration++
       return to verification.
  4. If a fix passes:
       run skill-evolution automatically
       promote, eval-only, or record no-promotion verdict.
  5. Exit when delivery gates pass or max iterations is reached.
```

## Exit report

```text
CORRECTION AND LEARNING REPORT
────────────────────────────────────
Iterations: <N>
Score progression: <list>
Local implementation patches: <list>
Learning candidates reviewed: <count>
Promoted skill/reference/workflow/contract changes: <list or none>
Eval-only additions: <list or none>
Local-only lessons: <list or none>
Duplicate/deferred candidates: <list or none>
Promotion commits: <sha list or not written>
Residual gaps: <list or none>
Final status: PASS | MAX_REACHED_WITH_GAPS
```

## Hard failures

The phase fails when:

- a shared skill is patched from an unverified idea;
- product-specific implementation history is copied into reusable instructions;
- an existing rule is duplicated instead of tested;
- a promoted patch has no regression eval;
- the agent claims a repository update without a write result or commit;
- delivery occurs without running learning review for verified fixes.
