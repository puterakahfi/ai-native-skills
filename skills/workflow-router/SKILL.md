---
name: workflow-router
description: Detect task intent and route to the correct primary lifecycle or standalone capability, including product, feature, bugfix, design, review, deployment, continuity, and skill creation or maintenance. Route before execution.
license: MIT
metadata:
  ai-native-skills.version: 1.8.0
  ai-native-skills.author: puterakahfi
  ai-native-skills.requires: "redesign-workflow design-audit design-refinement design-review brand-identity-review new-feature-workflow bugfix-workflow code-review-workflow deployment-workflow product-development-workflow delivery-work-breakdown chatgpt-app-development skill-authoring-workflow skill-evolution skill-eval git-workflow skill-doctor spec-workflow task-continuity production-code-quality-baseline"
  ai-native-skills.type: meta-skill
  ai-native-skills.implements: ai-native-core/contracts/skills/meta/workflow-router.contract.yaml
  ai-native-skills.contract-version: "~0.2"
  ai-native-skills.related_skills: '["role-switcher","product-development-workflow","delivery-work-breakdown","chatgpt-app-development","redesign-workflow","design-audit","design-refinement","design-review","brand-identity-review","skill-authoring-workflow","skill-doctor","skill-evolution","skill-eval","bugfix-workflow","new-feature-workflow","code-review-workflow","deployment-workflow","spec-workflow","task-continuity","production-code-quality-baseline"]'
---

# Workflow Router

## Reviewed core contract interface

Source: `ai-native-core/contracts/skills/meta/workflow-router.contract.yaml` · compatible line: `~0.2`

```yaml
required_inputs:
- user_request
allowed_outputs:
- workflow_selection
- skill_load_order
- routing_rationale
- ambiguity_resolution
- post_fix_learning_route
quality_gates:
- task_type_must_be_classified_before_workflow_selection
- routing_decision_must_be_stated_explicitly
- ambiguous_requests_must_be_clarified_not_assumed
- selected_workflow_must_be_loaded_before_execution
- no_execution_before_routing_confirmed
- fallback_must_be_defined_when_no_workflow_matches
- product_from_zero_requests_must_not_route_directly_to_implementation
- existing_ui_refinement_requests_must_route_to_redesign_workflow_not_new_surface_workflows
- targeted_design_gate_fixes_must_route_to_design_refinement
- explicit_verified_case_learning_requests_must_route_to_skill_evolution
- parent_workflows_with_verified_fixes_must_route_to_skill_evolution_before_final_delivery
- post_fix_learning_route_must_not_bypass_repository_write_or_approval_policy
```

Exact declarations make ownership reviewable; they do not replace repository, runtime, review, approval, or product evidence.

## Core rule

```text
classify requested outcome
→ select exactly one primary lifecycle or standalone capability
→ attach only justified overlays and specialists
→ resolve ambiguity before execution
→ execute only after routing is explicit
```

The artifact noun does not choose the lifecycle. A skill, dashboard, logo, API, or application may be created, audited, repaired, evolved, evaluated, reviewed, or deprecated.

## Route classes

| Intent | Primary route | Supporting capabilities |
|---|---|---|
| Build a product from zero | `product-development-workflow` | research, requirements, design, engineering |
| Add capability to existing product | `new-feature-workflow` | delivery topology, quality overlay, specialists |
| Fix broken implementation | `bugfix-workflow` | debugging, quality overlay, reviewers |
| Plan or specify | `spec-workflow` | product and relevant owners |
| Review code or PR | `code-review-workflow` | architecture/security/design reviewers |
| Deploy or release | `deployment-workflow` | operations, security, observability |
| Audit existing design only | `design-audit` | design-review + domain reviewer |
| Fix known design findings | `design-refinement` | preservation scope + reviewer |
| Replace design direction or structure | `redesign-workflow` | design owner + specialists |
| Resume or hand off work | `task-continuity` | governing lifecycle remains primary |
| Explore reversible idea | `spike` | experiment skills |
| Create or intentionally manage a skill package | `skill-authoring-workflow` | package policy, doctor, eval, git |
| Audit or repair skill health | `skill-doctor` | package validator + skill-eval when needed |
| Promote a verified reusable lesson | `skill-evolution` | skill-eval + git-workflow |
| Evaluate whether skill behavior was applied | `skill-eval` | saved per-case output and contract |

## Skill lifecycle routing

Classify the requested operation before loading a capability:

```text
new reusable skill/workflow/meta-skill
intentional update, restructure, migration, or deprecation
→ skill-authoring-workflow

health audit, contradiction diagnosis, stale content, package repair
→ skill-doctor

verified real-world fix with candidate reusable learning
→ skill-evolution

score a saved output against a behavioral contract
→ skill-eval

run package compliance only
→ documented package-validator path; do not pretend it is behavioral evaluation
```

Near-miss rules:

- The word “create” does not route to authoring when the user asks to create a regression eval from verified learning; use `skill-evolution`.
- The word “fix” does not route to doctor when the defect and intentional target change are already accepted; use `skill-authoring-workflow`.
- The word “test” does not route to `skill-eval` when the user asks to unit-test bundled scripts; preserve the governing authoring or maintenance lifecycle.
- Package compliance cannot prove that an agent applied a skill.
- Behavioral output evaluation cannot prove the package is structurally compliant.

Ambiguous examples such as “improve this skill” must resolve whether the user wants intentional behavior change, health diagnosis, verified-learning promotion, or output evaluation. No file modification before this distinction is known.

## Production-code quality overlay

For production code changes, preserve the selected lifecycle and attach `production-code-quality-baseline`.

```text
PRODUCTION_CODE_CHANGE
NON_PRODUCTION_CHANGE
DISPOSABLE_EXPERIMENT
NOT_VERIFIED
```

`NOT_VERIFIED` blocks implementation-complete or merge-ready claims. Conditional architecture concerns may be `NOT_APPLICABLE` or `NOT_JUSTIFIED` with evidence; silence is not PASS.

## Delivery topology overlay

Load `delivery-work-breakdown` before Git execution for broad dependent slices, new applications, unresolved branch bases, or epic/feature/task decomposition. Repository defaults and green CI cannot choose the PR target.

## Platform overlays

Platform specialists do not replace the primary lifecycle. For example:

```text
ChatGPT App from zero
→ product-development-workflow + chatgpt-app-development

ChatGPT integration in an existing product
→ new-feature-workflow + chatgpt-app-development
```

## Continuity overlay

`task-continuity` verifies live state before the original governing lifecycle resumes. It never replaces feature, bugfix, redesign, review, deployment, or skill lifecycle ownership.

## Design routing

```text
audit only → design-audit
known narrow findings with preservation scope → design-refinement
broad direction or structural replacement → redesign-workflow
```

When findings are unknown, audit before production. A narrow problem does not become redesign merely because the user says “polish.”

## Required output

```yaml
workflow_selection: <one primary route>
skill_load_order: []
routing_rationale: <intent and boundary evidence>
ambiguity_resolution: <resolved | clarification required | not applicable>
post_fix_learning_route: <skill-evolution | no promotion | not applicable>
```

## Hard gates

- No execution before routing is explicit.
- Do not guess ambiguous lifecycle, authority, branch base, or acceptance state.
- Do not create a duplicate lifecycle because a platform or artifact is specialized.
- Do not route package validation to behavioral evaluation or vice versa.
- Post-fix learning never bypasses repository write, review, or approval policy.
