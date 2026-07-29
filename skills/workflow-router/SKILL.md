---
name: workflow-router
description: Detect task intent and route to the correct primary lifecycle or standalone capability, including product, feature, bugfix, design, review, deployment, maintenance signals, continuity, and skill creation or maintenance. Route before execution.
license: MIT
metadata:
  ai-native-skills.version: 1.9.0
  ai-native-skills.author: puterakahfi
  ai-native-skills.requires: "redesign-workflow design-audit design-refinement design-review brand-identity-review new-feature-workflow bugfix-workflow code-review-workflow deployment-workflow product-development-workflow delivery-work-breakdown chatgpt-app-development skill-authoring-workflow skill-evolution skill-eval git-workflow skill-doctor spec-workflow task-continuity production-code-quality-baseline maintenance-case documentation-assurance incident-response technical-debt-governance"
  ai-native-skills.type: meta-skill
  ai-native-skills.implements: ai-native-core/contracts/skills/meta/workflow-router.contract.yaml
  ai-native-skills.contract-version: "~0.2"
  ai-native-skills.related_skills: '["role-switcher","product-development-workflow","delivery-work-breakdown","chatgpt-app-development","redesign-workflow","design-audit","design-refinement","design-review","brand-identity-review","skill-authoring-workflow","skill-doctor","skill-evolution","skill-eval","bugfix-workflow","new-feature-workflow","code-review-workflow","deployment-workflow","spec-workflow","task-continuity","production-code-quality-baseline","maintenance-case","documentation-assurance","incident-response","technical-debt-governance"]'
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

The maintenance signal composition below is an adapter-local refinement using the Core fallback and available-workflows boundary. It does not add canonical Core route classes or change the contract without an RFC.

## Core rule

```text
classify requested outcome
→ select exactly one primary lifecycle or standalone capability
→ attach only justified overlays and specialists
→ resolve ambiguity before execution
→ execute only after routing is explicit
```

The artifact noun does not choose the lifecycle. A skill, dashboard, logo, API, application, incident, alert, or maintenance record may be created, audited, repaired, evolved, evaluated, reviewed, deployed, or closed.

## Route classes

| Intent | Primary route | Supporting capabilities |
|---|---|---|
| Build a product from zero | `product-development-workflow` | research, requirements, design, engineering |
| Add capability to existing product | `new-feature-workflow` | delivery topology, quality overlay, specialists |
| Fix broken implementation | `bugfix-workflow` | debugging, quality overlay, reviewers |
| Plan or specify | `spec-workflow` | product and relevant owners |
| Review code or PR | `code-review-workflow` | architecture/security/design reviewers |
| Deploy, release, or rollback | `deployment-workflow` | operations, security, observability |
| Respond to a qualified active incident | `incident-response` | maintenance-case, observability, deployment/rollback as needed |
| Audit existing design only | `design-audit` | design-review + domain reviewer |
| Fix known design findings | `design-refinement` | preservation scope + reviewer |
| Replace design direction or structure | `redesign-workflow` | design owner + specialists |
| Qualify or close an operational/product maintenance signal | governing route selected after `maintenance-case` | documentation, continuity, applicable specialists |
| Correct documentation only under verified context | `documentation-assurance` standalone capability | owning domain and reviewer |
| Resume or hand off work | `task-continuity` | governing lifecycle remains primary |
| Explore reversible idea | `spike` | experiment skills |
| Create or intentionally manage a skill package | `skill-authoring-workflow` | package policy, doctor, eval, git |
| Audit or repair skill health | `skill-doctor` | package validator + skill-eval when needed |
| Promote a verified reusable lesson | `skill-evolution` | skill-eval + git-workflow |
| Evaluate whether skill behavior was applied | `skill-eval` | saved per-case output and contract |

## Maintenance signal composition

When a user presents an operational, product, security, dependency, performance, cost, data, documentation, deprecation, or technical-debt signal:

```text
maintenance-case
  qualifies signal, active-incident status, evidence confidence,
  bounded outcome, constraints, and routing input

workflow-router
  selects exactly one primary route or standalone capability

role-switcher
  assigns one owner and only justified specialists/reviewers
```

Adapter-local route mapping:

```text
qualified active incident
  → incident-response

verified non-active defect or regression
  → bugfix-workflow

approved improvement or new capability
  → new-feature-workflow

unknown design deficiency
  → design-audit

known narrow design failure
  → design-refinement

broad design replacement
  → redesign-workflow

release/deploy/rollback action
  → deployment-workflow

review-only request
  → code-review-workflow or applicable domain review

product-value uncertainty or metric movement
  → product-development-workflow at Product Validation / experiment composition

documentation-only correction with verified context
  → documentation-assurance

technical debt signal
  → technical-debt-governance for classification, then route an approved code change separately

unqualified or conflicted signal
  → BLOCKED / further investigation through the fallback boundary
```

Rules:

1. Maintenance is not a new primary workflow.
2. One signal may create linked follow-up cases, but each case has one primary route.
3. Current impact must be verified before choosing `incident-response`.
4. A provider advisory or alert does not prove affected usage, defect, or vulnerability.
5. Mitigation and permanent correction may be linked separate cases.
6. Documentation and continuity capabilities overlay the selected route; they do not replace it.
7. Route selection does not authorize production action, merge, release, deployment, accepted risk, or product acceptance.

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

## Documentation assurance overlay

For production changes and maintenance cases, attach `documentation-assurance` when documentation impact is material or not verified. A documentation-only correction may use it as the standalone executor only when governing product/domain context is verified.

```text
DOCUMENTATION_REQUIRED
DOCUMENTATION_NOT_APPLICABLE
DOCUMENTATION_NOT_VERIFIED
```

Documentation verdicts do not authorize merge, release, deployment, or product acceptance.

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

`task-continuity` verifies live state before the original governing lifecycle resumes. It never replaces feature, bugfix, redesign, review, deployment, maintenance, or skill lifecycle ownership. For maintenance work it preserves the case ID, selected route, signal/outcome evidence, documentation verdict, blockers, and exact next action.

## Design routing

```text
audit only → design-audit
known narrow findings with preservation scope → design-refinement
broad direction or structural replacement → redesign-workflow
```

When findings are unknown, audit before production. A narrow problem does not become redesign merely because the user says “polish.”

## Required output

```yaml
workflow_selection: <one primary route or standalone capability>
skill_load_order: []
routing_rationale: <intent and boundary evidence>
ambiguity_resolution: <resolved | clarification required | not applicable>
post_fix_learning_route: <skill-evolution | no promotion | not applicable>
maintenance_case_ref: <reference | not applicable | not verified>
documentation_assurance: <required | not applicable | not verified>
```

The last two fields are adapter-level extensions. Core-compatible consumers may preserve them in context or orchestration metadata without treating them as new canonical Core outputs.

## Hard gates

- No execution before routing is explicit.
- Exactly one primary route or standalone capability is selected.
- Do not guess ambiguous lifecycle, authority, branch base, acceptance state, active-incident status, or affected dependency usage.
- Do not create a duplicate lifecycle because a platform, artifact, or maintenance signal is specialized.
- `maintenance-case` prepares routing input but never replaces `workflow-router`.
- Incident mitigation and permanent correction are separate cases when they require different primary outcomes.
- Do not route package validation to behavioral evaluation or vice versa.
- Documentation impact and continuity are preserved as overlays where applicable.
- Post-fix learning never bypasses repository write, review, or approval policy.