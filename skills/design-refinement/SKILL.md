---
name: design-refinement
description: Targeted design improvement workflow — consume an evidence-backed design-review result, fix specific governed failures while preserving passing work, verify with domain-appropriate evidence, re-review through the facade, and promote reusable lessons after a verified fix.
license: MIT
metadata:
  ai-native-skills.version: 2.0.0
  ai-native-skills.author: puterakahfi
  ai-native-skills.type: workflow
  ai-native-skills.requires: "design-audit design-review master-design skill-evolution skill-eval"
  ai-native-skills.implements: ai-native-core/contracts/skills/quality/design-refinement.contract.yaml
  ai-native-skills.contract-version: "^1.0.0"
  ai-native-skills.related_skills: '["design-audit","design-review","redesign-workflow","master-design","skill-evolution","skill-eval","ui-components","accessibility","readability","responsiveness"]'
---

# Design Refinement

Targeted gate-fix loop: preserve the accepted direction, patch specific verified failures, collect domain-appropriate evidence, and re-review through the `design-review` facade.

This workflow owns refinement scope, preservation, patch discipline, verification, regression checks, and post-fix learning. The facade and loaded domain reviewers own gate meanings, applicability, scoring, coverage, and verdicts.

## Hard Rules

```text
1. Start from a routed review result, not an ungrounded aesthetic complaint.
2. Design domain, coverage mode, and governing reviewer must be explicit.
3. Preserve passing gates, locked assets, accepted direction, and unaffected regions.
4. Fix declared failures only; no drive-by redesign.
5. Patch the layer that owns the root cause, not the most visible symptom.
6. Use evidence appropriate to the gate and domain.
7. Re-review through the facade; do not self-invent replacement gate semantics.
8. LIMITED REVIEW cannot authorize specialist-domain refinement as complete.
9. After every verified fix, run skill-evolution + skill-eval.
10. Promote reusable knowledge only after the real artifact passes verification.
11. After two failed patches in the same region, reread and replan; never blindly apply a third.
12. Do not route from average score alone.
```

## Entry Decision

Use `design-refinement` when all are true:

```text
accepted direction or macrostructure is still valid
specific failed or partial gates are known
primary-domain reviewer coverage is BUILT_IN or ADAPTER_COVERED
required evidence can be collected
passing work should remain stable
```

Route elsewhere when:

```text
design-audit
  failures or coverage are not yet known

redesign-workflow
  direction, macrostructure, visual language, or component model is wrong
  the requested change spans multiple foundational clusters

domain specialist / reviewer
  coverage_mode is LIMITED or ROUTE_ELSEWHERE for the primary domain

local implementation/content/asset fix
  the governing rule already exists and no design decision is required
```

A score below or above a fixed number does not decide the route by itself. Consider domain coverage, hard gates, root cause, direction, and scope.

## Parameters

```text
target               required — editable artifact, repository surface, URL, or source
prior_review         required — facade review/audit route, findings, scores, coverage
target_findings      required — failed/partial gate IDs and affected regions
preserve             passing gates, locked assets, accepted regions, content, behavior
design_domain        inherited from prior review
surface_profile      inherited from prior review
coverage_mode        BUILT_IN | ADAPTER_COVERED | LIMITED | ROUTE_ELSEWHERE
domain_reviewers     governing built-in/external reviewers
max_iterations       default 3
approval_mode        repository write policy inherited from the project
```

## Refinement State

Record before editing:

```yaml
refinement:
  target: <target>
  design_domain: <domain>
  surface_profile: <profile>
  coverage_mode: <mode>
  domain_reviewers: []
  target_findings:
    - gate: <id>
      governing_reviewer: <reviewer>
      region: <region>
      current_status: <FAIL | PARTIAL>
      current_score: <score>
      evidence: []
  preserved_gates: []
  preserved_regions: []
  locked_assets: []
  required_evidence: []
  evidence_gaps: []
  max_iterations: 3
```

Stop and route when the primary-domain coverage is insufficient for the requested correction. Universal visual feedback may guide a bounded local change, but it cannot certify a specialist-domain fix.

## Refinement Loop

### Phase 1 — Validate and bound scope

Confirm:

```text
□ prior review uses the current design-review status model
□ target findings are verified, not merely NOT_VERIFIED
□ governing reviewer exists for every target gate
□ accepted direction remains valid
□ preservation set is explicit
□ required evidence is obtainable
□ no hard-gate failure demands immediate redesign or specialist escalation
```

Declare:

```text
REFINEMENT SCOPE
Fixing:      <gate IDs, reviewers, regions>
Preserving:  <passing gates, assets, regions, behavior>
Root cause:  <current hypothesis>
Patch layer: <foundation | structure | component | expression | interaction |
              content | implementation | domain-specialist>
Evidence:    <verification plan>
```

### Phase 2 — Classify the defect

For each target finding:

```text
A. Resolve the governing reviewer and gate definition.
B. Read the complete governing rule/reference.
C. Separate root cause from repeated symptoms.
D. Classify ownership:
   - reusable specialist-skill gap
   - facade/routing/orchestration gap
   - reference or eval gap
   - product-specific design lock
   - local implementation/content/asset defect
E. Choose the smallest correction layer that can resolve the root cause.
```

Do not patch `design-review` merely because a product implementation ignored an existing specialist rule. Do not copy specialist-domain knowledge into the facade.

### Phase 3 — Apply the smallest candidate fix

```text
preserve accepted direction
preserve passing gates
change only the required layer and affected regions
keep required assets and content faithful
avoid introducing unrelated component or style changes
record changed files/regions and rationale
```

A candidate learning is not shared knowledge until verification succeeds.

### Phase 4 — Verify with domain-appropriate evidence

Select only applicable evidence:

```text
interactive digital surface
  rendered visual at affected viewports/themes
  changed interaction and adjacent state walkthrough
  keyboard/pointer/touch/gesture checks as applicable
  accessibility semantics/focus when affected
  runtime capture when the flow is executable

static visual communication
  final-size and destination-placement inspection
  crop/safe-area/overlay checks
  logo/product/person/content comparison when required
  export resolution, compression, edge, and color checks

presentation
  affected slide plus adjacent narrative sequence
  room/screen-share/self-guided scale
  chart, data, source, and repeated-layout checks

specialized domain
  evidence required by the governing domain reviewer

repository implementation
  changed-file diff check
  relevant tests, type/lint/build checks at the appropriate boundary
  source inspection does not replace rendering when visual behavior changed
```

Re-check:

```text
fixed target gates
adjacent regression gates
all explicitly preserved gates and locks
applicable hard gates affected by the change
```

A successful build alone is not design verification.

### Phase 5 — Focused facade re-review

Invoke `design-review` with the inherited route:

```yaml
review_route:
  design_domain: <inherited>
  surface_profile: <inherited>
  artifact_state: <current state>
  review_depth: focused
  coverage_mode: <inherited>
  domain_reviewers: <inherited>
  selected_gates: <target + adjacent regression gates>
  selected_components: <affected components>
  evidence_available: <fresh verification packet>
```

Allowed outcomes:

```text
PASS / target gates >= threshold
  proceed to learning review and exit

CONDITIONAL PASS
  proceed only when remaining gaps are outside the declared refinement boundary
  and do not invalidate preserved or hard gates

NEEDS WORK
  iterate while max_iterations remains

CRITICAL
  stop and route to redesign-workflow, local emergency fix, or specialist

LIMITED REVIEW
  stop complete-domain claims; load the required reviewer or narrow the scope
```

Do not overwrite a failed re-review with a subjective “looks better” judgment.

### Phase 6 — Automatic learning review

After each verified fix, load:

```text
skill-evolution + skill-eval
```

The learning review must:

1. capture the failure, verified fix, before/after evidence, and governing reviewer;
2. extract why the correction worked;
3. classify it as local, product-specific, reusable specialist rule, facade/routing rule, reference, workflow, eval-only, or core contract;
4. remove product names, paths, routes, classes, and accidental breakpoints from shared instructions;
5. test the generalized reason against different contexts and counterexamples;
6. check complete governing files for duplicate coverage;
7. patch the smallest correct owner, never the facade by convenience;
8. add or update a regression eval from the verified case;
9. run relevant conformance checks when available;
10. commit automatically only when repository and approval policy permit.

Allowed learning verdicts:

```text
PROMOTED
EVAL_ONLY
LOCAL_ONLY
DUPLICATE
DEFERRED_UNVERIFIED
NOT_WRITTEN_READ_ONLY
```

### Phase 7 — Exit or handoff

Exit when all declared target findings pass the focused facade review and preserved gates remain stable, or when `max_iterations` is reached.

```text
REFINEMENT COMPLETE — <target>
Design domain: <domain>
Coverage mode: <mode>
Reviewers: <list>
Gates fixed: <before → after>
Gates preserved: <regression result>
Iterations: <N>
Changed regions/files: <list>
Evidence packet: <summary>
Learning verdicts: <list>
Promotion commits: <SHA list or not written>
Residual gaps: <list or none>
Handoff: <none | local fix | redesign-workflow | domain specialist>
```

The workflow is incomplete when a verified fix occurred but no learning-review verdict was recorded.

## Common Pitfalls

| Anti-pattern | Correct behavior |
|---|---|
| Route from average score alone | Use coverage, hard gates, direction, root cause, and domain ownership |
| Treat NOT_VERIFIED as a failing design | Collect evidence or report the gap |
| Refine a logo system with universal UI gates only | Load identity reviewer or return LIMITED REVIEW |
| Run browser checks on a poster | Use final-size, fidelity, crop, and export evidence |
| Patch all visible symptoms separately | Correct the governing root cause once |
| Update the facade with specialist knowledge | Patch the specialist reviewer or domain reference |
| Copy a product case into shared instructions | Promote only generalized verified reasoning |
| Fix unrelated visual areas | Preserve passing gates and scope |
| Claim skill update without a commit result | Report `not written` honestly |