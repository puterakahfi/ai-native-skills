# Delivery Planning and Vertical-Slice Composition

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
