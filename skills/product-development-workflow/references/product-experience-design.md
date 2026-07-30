# Product Experience Design Composition

## Purpose

Define the smallest credible user or consumer experience package before Solution Design without creating a competing design lifecycle.

## Ownership

`product-development-workflow` owns phase sequencing. Existing capabilities own the work:

```text
systems-reasoning → proportionate system and journey model when consequences cross the surface
systems-thinking → deep loops, delays, Goodhart, emergence, and second-order analysis when material
information-architecture → structure and navigation
master-design → coherent experience and visual direction
design-foundation → tokens, states, responsive and accessibility foundations
accessibility → inclusive interaction requirements
decision-provenance → approved locks, exceptions, and not-applicable claims
design-review → independent downstream acceptance, not upfront authorship
```

`systems-reasoning` and `systems-thinking` are overlays. They do not replace Product Experience Design, select a layout, or take ownership from `master-design` or `information-architecture`.

Capability evolution verdict: `DUPLICATE` for a new `product-experience-design` skill. The reusable need is composition guidance inside the existing lifecycle.

## Applicability

First classify whether Product Experience Design itself applies:

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

When experience work applies, classify whether system-level design reasoning is material before structural direction lock:

```yaml
systemic_design_applicability:
  status: REQUIRED | REDUCED | NOT_APPLICABLE | NOT_VERIFIED
  rationale: string
  activation_signals: []
  omitted_analysis_risk: []
```

Use `REQUIRED` or `REDUCED` when one or more are material:

- the experience crosses journey stages, routes, products, actors, teams, or repositories;
- user value and conversion, business, delivery, or operational metrics may conflict;
- local surface optimization may damage qualification, activation, trust, retention, support burden, accessibility, or maintainability;
- positioning, information architecture, product proof, reusable page shells, component families, or design-system behavior changes;
- a requested hero, dashboard, cards, tabs, or another familiar pattern is being treated as the requirement;
- feedback loops, delays, incentives, Goodhart risk, emergence, or second-order effects matter.

Use `NOT_APPLICABLE` for a bounded low-risk decision with explicit scope, locks, ownership, and consequences. Use `NOT_VERIFIED` when evidence is insufficient to classify safely.

## System-to-design handoff

When systemic-design reasoning is `REQUIRED` or `REDUCED`:

```text
systems-reasoning
  establishes purpose, actors, journey role, boundaries, dependencies,
  invariants, constraints, uncertainty, local-optimization risks,
  leverage points, trade-offs, and rejected system interventions

systems-thinking
  is delegated deep loops, delays, Goodhart, emergence,
  second-order effects, unintended consequences, and leverage analysis
  only when those dynamics are material

master-design + information-architecture
  consume the bounded handoff and retain ownership of experience,
  structure, navigation, component strategy, and direction selection
```

The handoff may constrain candidate evaluation. It must not select a hero, macrostructure, component family, visual genre, or interaction pattern on behalf of the design owner.

## Scaled output package

```yaml
product_experience_design:
  mvp_and_prd_references: []
  target_users_or_consumers: []
  user_journey: []
  core_user_flows: []
  systemic_design_applicability: <reference or NOT_APPLICABLE>
  systemic_design_context: <bounded reference or NOT_APPLICABLE>
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
2. Classify experience applicability and scale the package to risk, novelty, reversibility, and interaction complexity.
3. When experience applies, classify systemic-design applicability before structural direction lock.
4. If `REQUIRED` or `REDUCED`, load `systems-reasoning`; delegate deep dynamics to `systems-thinking` only when material.
5. Map the end-to-end journey and critical happy/unhappy paths using the bounded system handoff when available.
6. Let `information-architecture` and `master-design` compare and select structures and directions; familiar patterns remain candidates, not laws.
7. Define structure, navigation, interaction boundaries, ownership, and applicable loading, empty, error, success, permission, degraded, responsive, and accessibility states.
8. Trace every affected acceptance criterion to an experience decision or justified `NOT_APPLICABLE` record.
9. Record design locks and unresolved evidence gaps without pretending they are approved.
10. Define the independent design-review evidence route for Product Acceptance.

## Gate into Solution Design

PASS requires the core MVP experience to be understandable, evaluable, traceable, and sufficiently decided for architecture work. When systemic-design applicability is material, the bounded handoff and its unresolved uncertainty must also be reviewable before structural direction is treated as locked.

`NOT_VERIFIED`, materially missing flows/states, unsupported `NOT_APPLICABLE` claims, or a requested UI pattern treated as the requirement without product/system evaluation block Solution Design.
