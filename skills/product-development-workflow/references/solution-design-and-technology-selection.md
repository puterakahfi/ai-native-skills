# Solution Design and Technology Decision Composition

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
