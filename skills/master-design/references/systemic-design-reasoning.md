# Systemic Design Reasoning

Load this reference when a product-experience or broad redesign decision may affect multiple journey stages, routes, actors, products, metrics, reusable page shells, component families, design-system behavior, or downstream product outcomes.

Do not load it for a bounded, low-risk visual correction whose scope, locks, ownership, and consequences are already explicit.

## Ownership

```text
workflow-router
  owns exactly one primary lifecycle

systems-reasoning
  owns the proportionate system model and handoff

systems-thinking
  owns deep feedback loops, emergence, second-order effects,
  Conway alignment, Goodhart risk, unintended consequences,
  and leverage-point analysis when material

master-design
  owns experience direction, candidate comparison,
  final synthesis, design contracts, and engineering handoff

design-review
  owns independent rendered or implemented acceptance
```

The system model informs design. It does not prescribe a layout, genre, component, or macrostructure.

## Applicability

Classify before structural direction lock:

```yaml
systemic_design_applicability:
  status: REQUIRED | REDUCED | NOT_APPLICABLE | NOT_VERIFIED
  rationale: string
  activation_signals: []
  omitted_analysis_risk: []
```

### REQUIRED

Use `systems-reasoning` when one or more material signals exist:

- the surface changes more than one journey stage, route, product, actor, team, or repository;
- user value and business, delivery, or operational metrics may conflict;
- a local optimization may damage activation, trust, retention, support burden, accessibility, or maintainability;
- the work changes positioning, information architecture, product proof, conversion strategy, reusable page shells, component families, or design-system behavior;
- feedback loops, delays, incentives, Goodhart risk, emergence, or second-order effects matter;
- a requested UI pattern is being treated as the requirement without verified product reasoning;
- downstream design or engineering owners need one shared system model.

### REDUCED

Use a LIGHT system model when the task is localized but still requires one important boundary, consequence, leverage, or cross-surface decision.

### NOT_APPLICABLE

Do not activate when the task is bounded, low-risk, reversible, and does not materially alter the user journey, reusable design contracts, product meaning, system behavior, or accepted locks.

Examples include a known spacing defect, wrong icon, contrast failure, or text overflow correction with no wider consequence.

### NOT_VERIFIED

Use when evidence is insufficient to classify the consequence or boundary safely. Do not silently choose a familiar page recipe as the fallback.

## Normalized handoff

Consume only fields material to the decision:

```yaml
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

LIGHT or REDUCED execution may omit empty deep-dynamics fields, but must preserve the decision, evidence state, material consequence, and handoff.

## Deep dynamics delegation

Load `systems-thinking` when the design decision materially involves:

- reinforcing or balancing loops;
- delays, accumulation, oscillation, or bottlenecks;
- second-order effects or unintended consequences;
- metric proxy failure or Goodhart risk;
- team and architecture alignment through Conway's Law;
- emergence or leverage-point analysis.

Do not reproduce a ceremonial loop map merely because a page is user-facing. A deep analysis is applied only when its procedure produces an observable finding or decision.

## Direction comparison

For every materially open direction candidate, evaluate:

```yaml
direction_system_fit:
  journey_role:
  supports_outcomes: []
  leverage_points_used: []
  upstream_effects: []
  downstream_effects: []
  metric_risks: []
  second_order_effects: []
  design_system_consequences: []
  evidence_needed: []
```

The candidate may be conventional. It must not be selected merely because it is conventional.

## Landing-page rule

A landing page does not require a hero, three feature cards, testimonials, pricing, repeated CTAs, or any other fixed section sequence.

Treat them as candidate mechanisms. Derive the page shape from:

- primary user evaluation or action task;
- real content and available proof;
- the surface's role in acquisition, onboarding, activation, or another journey stage;
- system leverage and constraints;
- product and brand equity;
- required interaction and responsive behavior;
- evidence and acceptance criteria.

Valid outcomes include hero-led, document-led, workbench, interactive demo, catalogue, manifesto, editorial, grid-led, image-led, or another justified macrostructure.

## Metric and Goodhart check

When optimizing a design metric, record:

```yaml
metric_system_check:
  metric:
  intended_behavior:
  proxy_failure_risks: []
  likely_gaming_behaviors: []
  counter_metrics: []
  downstream_signals: []
  trust_quality_accessibility_effects: []
  evidence_required: []
```

For example, CTA clicks alone do not prove qualified signup, activation, retention, trust, or reduced support burden.

## Reusable design-system consequences

When a design creates or changes repeated shells, organisms, components, tokens, or cross-route behavior, record:

- reuse, composition, bounded extension, or new-capability decision;
- component-family implications;
- parallel-system risk;
- migration and compatibility consequences;
- maintenance ownership;
- implementation-context evidence required before production.

Do not infer actual repository components, imports, framework conventions, or reuse capability before `implementation-context-discovery` verifies them.

## Anti-patterns

Reject:

- artifact-name-to-template mapping;
- hero-first reasoning without product evidence;
- local conversion optimization that ignores downstream quality;
- fake proof added to satisfy a familiar section recipe;
- system maps that do not change a design decision;
- deep analysis for a bounded visual fix;
- system reasoning that takes design ownership;
- design direction that silently redefines system boundaries or accepted product scope.

## Completion gate

Systemic design reasoning is complete only when:

- applicability is explicit;
- the proportionate system model or justified non-activation is reviewable;
- deep dynamics are delegated rather than duplicated when material;
- direction candidates remain design decisions rather than system-model outputs;
- selected direction records material system consequences and evidence needs;
- exactly one primary workflow and one design owner remain explicit;
- independent design review still controls acceptance.
