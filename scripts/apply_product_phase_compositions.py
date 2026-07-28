#!/usr/bin/env python3
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PKG = ROOT / "skills" / "product-development-workflow"
REF = PKG / "references"

experience = '''# Product Experience Design Composition

## Purpose

Define the smallest credible user or consumer experience package before Solution Design without creating a competing design lifecycle.

## Ownership

`product-development-workflow` owns phase sequencing. Existing capabilities own the work:

```text
information-architecture → structure and navigation
master-design → coherent experience and visual direction
design-foundation → tokens, states, responsive and accessibility foundations
accessibility → inclusive interaction requirements
decision-provenance → approved locks, exceptions, and not-applicable claims
design-review → independent downstream acceptance, not upfront authorship
```

Capability evolution verdict: `DUPLICATE` for a new `product-experience-design` skill. The reusable need is composition guidance inside the existing lifecycle.

## Applicability

```yaml
experience_applicability:
  status: REQUIRED | REDUCED | NOT_APPLICABLE
  rationale: string
  affected_users_or_consumers: []
  material_interactions: []
  evidence_gaps: []
  decision_record_ids: []
```

- `REQUIRED`: user-facing or materially interactive product.
- `REDUCED`: narrow, low-risk, reversible interaction.
- `NOT_APPLICABLE`: no material UI/interaction surface; consumer contracts still require definition.

## Scaled output package

```yaml
product_experience_design:
  mvp_and_prd_references: []
  target_users_or_consumers: []
  user_journey: []
  core_user_flows: []
  information_architecture: []
  screen_or_interaction_map: []
  wireframes_interaction_specs_or_prototype: []
  required_states:
    default: []
    loading: []
    empty: []
    error: []
    success: []
    permission: []
    offline_or_degraded: []
  responsive_expectations: []
  accessibility_expectations: []
  content_and_feedback_rules: []
  experience_decisions_and_locks: []
  criterion_traceability: []
  evidence_and_review_route: []
  not_applicable_decisions: []
```

For API-only products, replace fake UI artifacts with consumer journeys, request/response/error/permission expectations, discoverability, versioning, and integration-state behavior.

## Procedure

1. Verify effective PRD, approved MVP, target users/consumers, and provenance.
2. Classify applicability and scale the package to risk, novelty, reversibility, and interaction complexity.
3. Map the end-to-end journey and critical happy/unhappy paths.
4. Define structure, navigation, interaction boundaries, and ownership.
5. Define applicable loading, empty, error, success, permission, degraded, responsive, and accessibility states.
6. Trace every affected acceptance criterion to an experience decision or justified `NOT_APPLICABLE` record.
7. Record design locks and unresolved evidence gaps without pretending they are approved.
8. Define the independent design-review evidence route for Product Acceptance.

## Gate into Solution Design

PASS requires the core MVP experience to be understandable, evaluable, traceable, and sufficiently decided for architecture work. `NOT_VERIFIED`, materially missing flows/states, or unsupported `NOT_APPLICABLE` claims block Solution Design.
'''

solution = '''# Solution Design and Technology Decision Composition

## Purpose

Translate verified product and experience decisions into an executable technical solution after inspecting the real implementation context.

## Ownership

```text
implementation-context-discovery → repository/runtime truth
spec-workflow → executable technical specification
native-ai-engineer / master-engineer → architecture and boundary decisions
api-contract → API and integration contracts
data-modeling → data ownership and model
security / operations capabilities → applicable security, deployment, resilience, observability
```

Do not create a competing `solution-design` workflow. `spec-workflow` remains the specification boundary.

`technology-selection` remains a reusable procedure/reference in this composition (`LOCAL_ONLY`). Promote it to an atomic skill only after repeated independent use and dedicated eval evidence prove separate ownership.

## Solution package

```yaml
solution_design:
  source_artifacts:
    prd: string
    mvp: string
    experience: string
  implementation_context:
    repository_and_branch: string
    stack_and_runtime: []
    reusable_assets: []
    commands_and_conventions: []
    constraints_and_unknowns: []
  domain_and_modules: []
  frontend:
    routes_and_surfaces: []
    component_boundaries: []
    state_ownership: []
    data_access_and_forms: []
    interaction_and_accessibility_states: []
    tests: []
  backend:
    use_cases: []
    authorization: []
    persistence_and_transactions: []
    events_integrations_and_idempotency: []
    tests: []
  data_ownership_and_models: []
  api_and_integration_contracts: []
  security_and_privacy: []
  deployment_topology_and_rollback: []
  resilience_and_observability: []
  testing_and_verification_strategy: []
  technology_decisions: []
  criterion_to_design_traceability: []
  approved_exceptions_and_record_ids: []
  open_questions_and_blockers: []
```

## Technology decision record

```yaml
technology_decision:
  concern: string
  selected: string
  alternatives_considered: []
  product_fit: []
  ecosystem_fit: []
  team_or_runtime_fit: []
  operational_cost: []
  risks: []
  reversal_cost: low | medium | high
  decision_record_ids: []
```

A choice based only on trend, familiarity, or preference fails. Material dependencies, boundary changes, or exceptions outside verified scope require decision provenance.

## Procedure

1. Run `implementation-context-discovery`; record `NOT_VERIFIED` rather than guessing.
2. Map PRD/MVP/experience decisions to domain, frontend, backend, data, API, security, operations, and testing concerns.
3. Reuse existing modules, contracts, conventions, and platform capabilities before adding dependencies.
4. Produce only applicable sections, but never omit material risks, ownership boundaries, rollback, or evidence needs.
5. Evaluate each material technology choice against alternatives, fit, operations, risk, and reversal cost.
6. Route unsupported dependency/boundary changes through decision provenance.
7. Feed the resulting package into `spec-workflow` for executable specification and traceability.

## Gate into Delivery Planning

PASS requires verified implementation context, sufficient solution coverage, evidence-backed material technology decisions, explicit risks/unknowns, and criterion traceability. Trend-only choices or unresolved material boundaries block Delivery Planning.
'''

delivery = '''# Delivery Planning and Vertical-Slice Composition

## Purpose

Convert an approved MVP and sufficient Solution Design into independently testable outcomes and an authorized repository/PR topology.

## Ownership

`delivery-work-breakdown` owns decomposition. Product Development supplies the verified MVP, experience, solution, acceptance, and release context. Do not create another delivery-planning skill.

## Vertical-slice contract

```yaml
vertical_slice:
  id: string
  outcome: string
  acceptance_criteria: []
  experience_decisions: []
  solution_decisions: []
  interface_or_ui: []
  application_or_domain: []
  data_or_integration: []
  tests_and_validators: []
  observability: []
  activation_and_rollback: []
  reviewers: []
  dependencies: []
```

## Delivery package

```yaml
product_delivery_plan:
  release_unit: feature | epic | standalone_product_slice
  effective_mvp_and_prd: []
  source_solution_decisions: []
  vertical_slices: []
  enabling_work: []
  dependency_graph: []
  critical_path: []
  branch_base: string
  integration_branch: string
  child_pr_targets: []
  final_pr_target: string
  activation_strategy: []
  rollback_strategy: []
  verification_and_review_plan: []
  criterion_to_slice_and_task_traceability: []
  release_authorization_boundary: string
```

## Rules

1. Start after sufficient Solution Design; MVP Definition does not own detailed task/branch topology.
2. Prefer end-to-end outcomes over `all frontend`, `all backend`, or `database first` phases.
3. Each slice should include applicable interface, application/domain, data/integration, tests, observability, and acceptance evidence.
4. Horizontal/platform/enabling work is allowed only with a named consuming slice, explicit dependency, observable enablement, validation, activation, and rollback.
5. Every slice and task traces to verified acceptance criteria and solution decisions.
6. Epic child PRs target the approved integration branch; child CI never proves epic/product acceptance.
7. Branch base, final target, release unit, activation, rollback, reviewers, dependencies, and critical path must be explicit where applicable.

## Gate into Implementation

PASS requires independently testable outcomes, complete traceability, justified enabling work, explicit dependency/critical path, approved repository topology, and activation/rollback evidence. Horizontal-only decomposition fails when a credible vertical slice is feasible.
'''

validation = '''# Product Validation and Learning Composition

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
'''

for name, text in {
    'product-experience-design.md': experience,
    'solution-design-and-technology-selection.md': solution,
    'delivery-planning-and-vertical-slices.md': delivery,
    'product-validation-and-learning.md': validation,
}.items():
    (REF / name).write_text(text, encoding='utf-8')

skill_path = PKG / 'SKILL.md'
skill = skill_path.read_text(encoding='utf-8')
skill = skill.replace('ai-native-skills.version: 3.0.0', 'ai-native-skills.version: 3.1.0')
skill = skill.replace(
    'description: End-to-end digital product workflow from zero to launch — discovery, provenance-backed PRD and MVP decisions, technical specification, feature implementation, product acceptance, release readiness, delivery approval, launch, and learning.',
    'description: End-to-end digital product workflow from idea to validated product — Product Brief, PRD, MVP, experience and solution design, vertical-slice delivery, implementation, evidence-backed acceptance, release, deploy, launch, and real-user validation.'
)
needle = '''Formats, stop points, and pitfalls\n  references/formats-pitfalls.md\n'''
replacement = '''Product Experience Design composition\n  references/product-experience-design.md\n\nSolution Design and technology selection composition\n  references/solution-design-and-technology-selection.md\n\nDelivery Planning and vertical-slice composition\n  references/delivery-planning-and-vertical-slices.md\n\nProduct Validation and Learning composition\n  references/product-validation-and-learning.md\n\nFormats, stop points, and pitfalls\n  references/formats-pitfalls.md\n'''
skill = skill.replace(needle, replacement)
skill_path.write_text(skill, encoding='utf-8')

p16_path = REF / 'phases-1-6.md'
p16 = p16_path.read_text(encoding='utf-8')
p16 = p16.replace('Compose existing design capabilities; do not create a duplicate design lifecycle. Scale outputs by product type, risk, and complexity.', 'Compose existing design capabilities; do not create a duplicate design lifecycle. Scale outputs by product type, risk, and complexity. Load `product-experience-design.md` for applicability, package shape, procedure, traceability, and the downstream gate.')
p16 = p16.replace('Load `implementation-context-discovery` before material architecture, dependency, stack, or repository-mapping decisions.', 'Load `implementation-context-discovery` before material architecture, dependency, stack, or repository-mapping decisions. Load `solution-design-and-technology-selection.md` for the complete package and technology-decision gate.')
p16 = p16.replace('Load `delivery-work-breakdown` and `decision-provenance`.', 'Load `delivery-work-breakdown` and `decision-provenance`. Load `delivery-planning-and-vertical-slices.md` for the vertical-slice contract, enabling-work exceptions, topology, and traceability requirements.')
p16_path.write_text(p16, encoding='utf-8')

p712_path = REF / 'phases-7-12.md'
p712 = p712_path.read_text(encoding='utf-8')
p712 = p712.replace('## Phase 12 — Product Validation and Learning', '## Phase 12 — Product Validation and Learning\n\nLoad `product-validation-and-learning.md` for semantic boundaries, evidence package, statuses, decision provenance, and completion gates.')
p712_path.write_text(p712, encoding='utf-8')

test_path = ROOT / 'contracts' / 'tests' / 'product-development-workflow.test.yaml'
test = test_path.read_text(encoding='utf-8')
test = test.replace('version: 3.0.0', 'version: 3.1.0', 1)
extra = '''

    - id: dashboard-experience-package-before-solution-design
      description: A user-facing dashboard defines flows, interaction states, responsive behavior, accessibility, and traceability before solution design.
      trigger: Design the product experience for a project and task monitoring dashboard, then prepare it for technical design.
      must_contain:
        - Product Experience Design
        - user journey
        - core user flows
        - screen or interaction map
        - loading
        - empty
        - error
        - success
        - permission
        - responsive
        - accessibility
        - criterion-to-experience traceability
      must_not_contain:
        - skip to implementation
        - design-review authors the design
      quality_gates_tested:
        - user_facing_experience_precedes_solution_design
        - required_states_and_accessibility_are_considered
        - upfront_design_and_independent_review_remain_separate

    - id: api-only-experience-uses-consumer-contracts
      description: API-only products avoid fake UI while defining consumer interactions and error/permission behavior.
      trigger: Define Product Experience Design for an API-only task service with no visual interface.
      must_contain:
        - NOT_APPLICABLE
        - consumer journey
        - request
        - response
        - error
        - permission
        - contract expectations
      must_not_contain:
        - fake wireframes
        - skip consumer behavior
      quality_gates_tested:
        - non_visual_products_define_consumer_experience
        - not_applicable_requires_rationale

    - id: evidence-backed-technology-selection
      description: Material stack choices follow implementation-context discovery and a complete technology decision record.
      trigger: Pakai stack terbaru aja untuk frontend dan backend produk ini.
      must_contain:
        - implementation-context-discovery
        - alternatives_considered
        - product_fit
        - ecosystem_fit
        - team_or_runtime_fit
        - operational_cost
        - risks
        - reversal_cost
        - BLOCKED
      must_not_contain:
        - latest stack selected automatically
        - preference is sufficient evidence
      quality_gates_tested:
        - implementation_context_precedes_stack_choice
        - trend_only_technology_selection_fails
        - material_decisions_record_tradeoffs

    - id: vertical-slice-plan-rejects-horizontal-phases
      description: Delivery Planning rejects frontend/backend/database phases when end-to-end outcomes are feasible.
      trigger: Bagi delivery jadi build semua frontend, lalu semua backend, lalu database.
      must_contain:
        - vertical slice
        - independently testable outcome
        - acceptance criteria
        - interface_or_ui
        - application_or_domain
        - data_or_integration
        - activation_and_rollback
        - rejected
      must_not_contain:
        - horizontal plan approved
        - child CI proves product acceptance
      quality_gates_tested:
        - vertical_outcomes_are_default
        - horizontal_work_requires_justification
        - slice_traceability_and_rollback_required

    - id: limited-product-validation-does-not-complete-lifecycle
      description: A launched product with insufficient usage remains LIMITED and creates a next experiment rather than false completion.
      trigger: Produk sudah live dan telemetry aktif, tapi baru dua orang mencoba dan belum ada bukti outcome pengguna.
      must_contain:
        - Product Validation
        - LIMITED
        - real-user evidence
        - next experiment
        - decision owner
        - next PRD or backlog action
        - lifecycle incomplete
      must_not_contain:
        - product validated
        - workflow complete
        - telemetry alone proves value
      quality_gates_tested:
        - product_validation_is_distinct_from_verification_and_acceptance
        - weak_evidence_remains_limited
        - owned_next_action_required
'''
if 'dashboard-experience-package-before-solution-design' not in test:
    test = test.rstrip() + extra + '\n'
test_path.write_text(test, encoding='utf-8')

# remove one-time migration resources from final branch state
(ROOT / '.github' / 'workflows' / 'apply-product-phase-compositions.yml').unlink(missing_ok=True)
Path(__file__).unlink(missing_ok=True)
