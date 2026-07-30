# Integration and Handoffs

`systems-reasoning` is a foundational overlay. It supplies a normalized system model while preserving exactly one primary workflow.

## Workflow router

Consumed:

- user request;
- requested outcome;
- ambiguity and cross-system signals.

Produced:

- system classification;
- boundary and risk findings;
- recommended depth;
- materially relevant downstream consumers.

`workflow-router` still owns primary workflow selection.

## Product framing

Provide actors, desired outcomes, environment, constraints, incentives, and system-level trade-offs. Product capabilities still own value, scope, success criteria, and product acceptance.

## Product experience and design

Provide a proportionate system-to-design handoff when a product-experience or broad redesign decision may affect multiple journey stages, routes, actors, products, metrics, reusable page shells, component families, design-system behavior, or downstream outcomes.

```yaml
systemic_design_applicability:
  status: REQUIRED | REDUCED | NOT_APPLICABLE | NOT_VERIFIED
  rationale: string
  activation_signals: []
  omitted_analysis_risk: []

systemic_design_context:
  system_of_interest_ref: string
  purpose_and_desired_outcomes: []
  target_actors_and_users: []
  surface_role_in_journey: string
  upstream_dependencies: []
  downstream_dependencies: []
  important_relationships: []
  invariants_and_locks: []
  constraints: []
  causal_relationships: []
  feedback_loops: []
  delays_or_accumulations: []
  local_optimization_risks: []
  metric_and_goodhart_risks: []
  second_order_effects: []
  leverage_points: []
  trade_offs: []
  design_direction_implications: []
  rejected_system_interventions: []
  evidence_refs: []
  assumptions: []
  unresolved_uncertainty: []
```

`master-design` still owns user experience, candidate comparison, visual direction, component strategy, interaction contracts, synthesis, and engineering handoff. `information-architecture`, design specialists, engineering, and `design-review` retain their existing ownership.

A requested hero, dashboard, card grid, tabs, split layout, or other pattern is classified as a proposed mechanism. The system model may constrain or inform the design decision, but it must not select a layout automatically.

Load `systems-thinking` when reinforcing or balancing loops, delays, emergence, Conway alignment, Goodhart risk, second-order effects, unintended consequences, or leverage-point analysis are material. Do not duplicate that deep dynamics ownership inside `systems-reasoning` or `master-design`.

Use REDUCED or NOT_APPLICABLE for bounded visual corrections with explicit scope, locks, ownership, and no material journey or reusable-system consequence.

## Domain modeling

Provide system boundary candidates, capabilities, policies, invariants, actors, relationships, and unresolved semantic conflicts. Domain modeling owns domain language, aggregates, events, and model design.

## Architecture

Provide capability boundaries, dependency direction, invariants, dynamics, failure propagation, leverage points, constraints, and trade-offs. Architecture owns architectural decisions and mechanism selection.

## Delivery breakdown

Provide independently valuable outcomes, dependency graph, ownership boundaries, risky integration points, and acceptance dependencies. Delivery breakdown owns epic/feature/task topology, branch base, and PR targets.

## Implementation context discovery

Provide the questions that must be verified against the live repository: current boundaries, adapters, runtime bindings, conventions, constraints, and known failure points. Discovery owns verification of actual implementation state.

For design work, do not infer reusable components, page shells, component families, design-system tokens, imports, or framework conventions from the system model. Hand those repository questions to `implementation-context-discovery` before production.

## Test strategy

Provide system risks, boundaries, invariants, failure propagation, feedback delays, and acceptance consequences. Test strategy owns portfolio and test-level selection.

## Quality review

Provide intended system model and trade-offs as review context. Reviewers determine whether implementation evidence preserves the model and accepted decisions.

For user-facing output, `design-review` still controls rendered or implemented design acceptance. Systems reasoning does not self-certify the design.

## Handoff rules

- Include only fields materially needed by the consumer.
- Preserve evidence, inference, assumption, review, approval, and acceptance as separate states.
- Do not convert an unresolved system decision into an implementation or layout default.
- Do not claim downstream capability execution merely because it is named in a handoff.
- Return to systems reasoning only when new evidence materially changes the system boundary, purpose, invariant, relationship, dynamic, or trade-off.
- Preserve exactly one primary workflow and the downstream owner's decision authority.
- Do not activate deep systems analysis for a bounded low-risk design correction merely because the artifact is user-facing.

## Composition examples

### Shared engineering capability

```text
workflow-router selects new-feature-workflow
→ systems-reasoning models shared notification capability
→ product-manager confirms user value and channel policy
→ domain modeling defines canonical notification semantics
→ architecture selects ports and adapter boundaries
→ delivery-work-breakdown defines slices and integration order
→ implementation-context-discovery verifies repository reality
→ implementation and validation proceed
```

### Product experience from zero

```text
workflow-router selects product-development-workflow
→ Product Experience Design classifies systemic-design applicability
→ systems-reasoning models journey role, actors, boundaries, consequences, and leverage when required
→ systems-thinking analyzes deep loops, Goodhart risk, or second-order effects when material
→ information-architecture and master-design consume the bounded handoff
→ master-design compares product-specific experience and visual directions
→ engineering implements through the governing workflow
→ design-review verifies the real artifact
```

### Broad landing-page redesign

```text
workflow-router selects redesign-workflow
→ master-design classifies systemic-design applicability before direction lock
→ systems-reasoning tests whether the leverage point is structure, positioning, proof, onboarding, content, or another journey intervention
→ systems-thinking runs only when deep dynamics are material
→ hero, workbench, document-led, catalogue, manifesto, or another macrostructure remain candidates
→ selected direction records system consequences and evidence needs
→ design-review controls acceptance
```

The overlay ends when the normalized system decisions are sufficient for the downstream owner. It must not remain active as a ceremonial duplicate of every later step.
