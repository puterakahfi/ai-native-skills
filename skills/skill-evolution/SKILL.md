---
name: skill-evolution
description: Converts verified lessons from real product work into minimal reusable skill, reference, workflow, eval, or core-contract improvements without copying product-specific implementation history into shared skills.
license: MIT
metadata:
  ai-native-skills.version: 1.0.2
  ai-native-skills.author: puterakahfi
  ai-native-skills.type: workflow
  ai-native-skills.requires: "skill-eval git-workflow"
  ai-native-skills.implements: ai-native-core/contracts/skills/quality/skill-evolution.contract.yaml
  ai-native-skills.contract-version: "^1.0.0"
  ai-native-skills.boundary.covers: '["post_fix_learning_review","reusable_reason_extraction","local_vs_shared_knowledge_classification","target_layer_selection","minimal_skill_or_reference_patch","regression_eval_creation","skill_version_and_promotion_decision","provenance_logging_outside_skill_body"]'
  ai-native-skills.boundary.delegates: '["solving_the_original_product_issue","copying_product_implementation_into_shared_skills","storing_product_specific_breakpoints_routes_or_component_names_in_shared_skills","promoting_unverified_anecdotes","bypassing_repository_write_or_approval_policy","replacing_product_design_locks_or_architecture_decisions"]'
  ai-native-skills.related_skills: '["skill-eval","skill-doctor","git-workflow","redesign-workflow","design-refinement","systematic-debugging"]'
---

# Skill Evolution

## Reviewed core contract interface

Source: `ai-native-core/contracts/skills/quality/skill-evolution.contract.yaml` · compatible line: `^1.0.0`

```yaml
required_inputs:
- source_case
- observed_failure
- verified_fix
- before_after_evidence
- candidate_skill_or_workflow
allowed_outputs:
- learning_candidate
- root_reason
- generalization_report
- target_layer_decision
- minimal_patch_plan
- skill_or_reference_patch
- regression_eval
- promotion_verdict
- promotion_commit
- no_promotion_reason
- provenance_record
quality_gates:
- learning_review_runs_after_every_verified_fix_even_when_no_promotion_occurs
- source_case_has_before_after_evidence_and_successful_verification
- local_product_detail_is_not_written_into_shared_skill_body
- promoted_learning_explains_the_reusable_reason_not_only_the_case_solution
- target_layer_is_selected_from_defect_class_and_knowledge_scope
- target_skill_and_related_skills_are_checked_for_duplicate_coverage
- transferable_rule_is_validated_against_multiple_contexts_and_counterexamples
- skill_patch_is_the_smallest_change_that_closes_the_reasoning_gap
- every_promoted_patch_has_a_regression_eval_derived_from_the_real_case
- existing_evals_and_contract_conformance_are_rechecked
- product_specific_case_provenance_is_stored_outside_shared_skill_instructions
- repository_write_and_approval_policy_is_respected
- completion_report_distinguishes_promoted_local_only_duplicate_and_deferred_candidates
```

From source_case, observed_failure, verified_fix, before_after_evidence, and candidate_skill_or_workflow, produce the complete learning and promotion record. A candidate transferable rule must be tested against multiple contexts and counterexamples before promotion; one successful anecdote is not reusable evidence.

Keep this interface synchronized with the pinned core contract. Exact declarations make ownership reviewable; they do not replace repository, runtime, workflow, review, approval, or product evidence.


## Core rule

```text
Verified real case
→ inspect why the fix worked
→ classify the knowledge scope
→ generalize the reusable reason
→ patch the smallest correct shared layer
→ add a regression eval
→ verify
→ commit when repository policy permits.
```

A resolved product issue is always reviewed for learning, but it is **not always promoted**.

Do not copy the implementation story into `SKILL.md`. Shared skills store reusable decision logic. Product repositories store product-specific decisions and implementation details. Tests store concrete regression cases.

## Boundary

This workflow owns post-fix learning review, reusable-reason extraction, local-versus-shared classification, target-layer selection, minimal shared patches, regression evidence, version/promotion decisions, and provenance kept outside the reusable skill body. It does not solve the original product issue, copy product implementation into shared skills, store product-specific routes/breakpoints/component names as universal guidance, promote unverified anecdotes, bypass repository approval policy, or replace product design locks and architecture decisions.

## Automatic invocation

Run this workflow automatically after all of the following are true:

- a real implementation or design issue was observed;
- a fix was applied;
- the fix passed relevant runtime, visual, interaction, accessibility, or test verification;
- the workflow is about to deliver or close the issue.

The parent workflow must not wait for the user to say “update the skill.” The learning review is a required post-fix phase.

If no reusable learning exists, produce an explicit `NO PROMOTION` verdict and continue delivery.

## Inputs

Collect:

```yaml
source_case:
  product: <product or project name>
  observed_failure: <what failed>
  attempted_approaches: <optional>
  verified_fix: <what changed locally>
  before_after_evidence: <tests, screenshots, interaction evidence, gate scores>
  candidate_skill_or_workflow: <likely owner of the missing reasoning>
  implementation_diff: <optional>
```

Product names and implementation details are valid evidence here. They are not automatically valid shared-skill content.

## Phase 1 — Observe

Write the factual case record:

```text
Observed failure:
Why the previous decision failed:
Verified local fix:
Evidence that the fix works:
Remaining uncertainty:
```

Fail closed when the fix is only assumed, visually unverified, or not regression-tested. Unverified ideas are learning candidates, not promotable knowledge.

## Phase 2 — Classify the target layer

Choose exactly one primary destination:

| Classification | Destination | Shared skill patch |
|---|---|---:|
| Local implementation defect | Product repository code | No |
| Product-specific durable decision | Product `DESIGN.md`, design lock, ADR, or context | No |
| Reusable decision rule or quality gate | Target `SKILL.md` | Yes |
| Extended reusable rationale or matrix | Target `references/` | Yes |
| Workflow ordering or role-loading gap | Workflow `SKILL.md` | Yes |
| Correct rule applied unreliably | Regression eval/test | Eval only |
| Missing public cross-adapter obligation | `ai-native-core` contract | Controlled |

Examples of local-only details:

- route names;
- repository paths;
- exact project breakpoints;
- component names unique to one product;
- CSS class conflicts;
- a specific card height;
- brand-specific decisions.

Examples of reusable learning:

- decision factors omitted by the skill;
- a missing “why” behind component selection;
- an anti-pattern that can recur across products;
- a quality gate required to prevent the same class of failure;
- a missing workflow phase or specialist/reviewer composition.

## Phase 3 — Extract the root reason

Ask:

1. What assumption or reasoning step caused the failure?
2. Why did the verified fix work?
3. Which decision factors made it better?
4. Under what conditions would the fix *not* be appropriate?
5. Could the rule guide a different product with different components?

Bad learning:

```text
Creative Gallery mobile must use a shortcut rail.
```

Good learning:

```text
When a small, high-value discovery set must remain visible but does not fit the available width, preserve discoverability through a reachable overflow pattern or component substitution. Do not default to hiding primary choices in a Select solely to avoid layout work.
```

The good version captures the reason, conditions, and trade-off. It does not freeze one implementation.

## Phase 4 — Generalization test

A proposed shared rule must pass all checks:

```text
□ Product names removed from the reusable rule
□ Routes, class names, file paths, and exact breakpoints removed
□ Rule explains why, not only what was implemented
□ Conditions and counterexamples are stated
□ Rule transfers to at least two different hypothetical products
□ Rule belongs to the candidate skill boundary
□ Related skills do not already own the same rule
```

Use two transfer probes, for example:

```text
Context A: media catalogue with six stable discovery categories
Context B: admin tool with twelve dynamic secondary filters
```

A rule that produces the same component for both contexts is probably too implementation-specific. A good rule may produce different decisions from the same reasoning factors.

## Phase 5 — Deduplicate

Before editing:

1. Read the complete target skill.
2. Search its related skills, references, workflow owners, and core contract.
3. Check existing tests/evals.
4. Determine whether the gap is:
   - missing rule;
   - weak or ambiguous rationale;
   - missing quality gate;
   - missing regression eval;
   - already covered.

Verdicts:

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

Never append a second wording of an existing principle merely because a new case confirmed it. Add regression coverage instead.

## Phase 6 — Apply the minimal patch

Patch the smallest correct layer:

- Add one reasoning step instead of a case narrative.
- Add one gate instead of an implementation recipe.
- Clarify an existing rule instead of adding a duplicate section.
- Move long matrices or explanations to `references/`.
- Change a core contract only when the obligation must hold across adapters.

Do not turn a specialist skill into a product changelog.

When modifying a skill:

```text
1. preserve its boundary;
2. update version according to repository policy;
3. update related metadata only when dependencies changed;
4. avoid unrelated cleanup;
5. record the source case outside the skill body.
```

## Phase 7 — Create regression evidence

Every promoted learning needs a test derived from the real case.

The test should preserve the decision pressure without preserving unnecessary product identity:

```yaml
case:
  trigger: <genericized version of the real failure>
  must_contain:
    - <reasoning or behavior unique to the improved skill>
  must_not_contain:
    - <the old failure pattern>
  quality_gates_tested:
    - <gate protected by the learning>
```

Use `skill-eval` to classify behavior as `APPLIED`, `PARTIAL`, or `GHOST`.

A skill patch without a regression eval is incomplete.

## Phase 8 — Verify and promote

Run, when available:

```text
1. target skill regression eval;
2. related skill evals affected by the boundary;
3. core path/version/conformance validation;
4. repository lint or metadata checks;
5. the original real-case verification again when feasible.
```

Promotion behavior:

```text
Autonomous + writable repository + all gates pass
→ patch and commit automatically.

Patch-gated policy
→ prepare exact patch and request approval.

Read-only repository
→ emit a promotion plan and do not claim the skill was updated.
```

Use the repository's configured branch policy. This skill does not invent branches or bypass approval rules.

## Provenance without skill bloat

Keep the concrete source case outside the reusable instructions, for example:

```text
evals/cases/<skill>/<case-id>.yaml
learning-log/<date>-<case-id>.yaml
product DESIGN.md or design lock
commit message and diff
```

A provenance record may contain product names and exact implementation evidence. `SKILL.md` should contain only the promoted reusable reasoning.

## Required completion report

```text
SKILL EVOLUTION REVIEW
────────────────────────────────────
Source case: <case>
Verification: PASS | INCOMPLETE
Root reason: <reason>
Classification: <target layer>
Transfer test: PASS | FAIL
Duplicate check: NEW | EXISTING | OVERLAP
Verdict: PROMOTED | EVAL_ONLY | LOCAL_ONLY | DUPLICATE | DEFERRED
Target: <file or none>
Skill patch: <summary or none>
Regression eval: <file/result or none>
Commit: <sha or not written>
Local provenance: <location>
```

## Hard gates

Fail promotion when any answer is yes:

- Is the fix unverified?
- Does the proposed rule mention product-specific implementation details unnecessarily?
- Does it state only the chosen component without the decision reason?
- Does an equivalent rule already exist?
- Does the patch belong to another skill or product context layer?
- Is there no regression eval?
- Did related evals or conformance checks fail?
- Is repository write or approval policy missing?

## Anti-patterns

| Anti-pattern | Correct behavior |
|---|---|
| Copy every resolved issue into `SKILL.md` | Extract only transferable reasoning |
| Treat every local bug as a knowledge defect | Keep local fixes local |
| Add “mobile uses X” as a universal rule | Store decision factors and conditions |
| Patch skill before proving the fix | Verify the real case first |
| Duplicate an existing rule | Add eval coverage or clarify minimally |
| Update skill without a test | Promotion fails |
| Claim automatic update with read-only access | Report `not written` honestly |
