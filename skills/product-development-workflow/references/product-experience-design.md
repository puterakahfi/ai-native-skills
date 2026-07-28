# Product Experience Design Composition

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
