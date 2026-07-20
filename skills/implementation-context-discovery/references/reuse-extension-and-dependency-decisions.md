# Reuse, Extension, and Dependency Decisions

Load this reference after repository evidence and canonicality decisions are available.

The implementation question is not “which library would I choose from scratch?” It is “what is the smallest repository-consistent implementation that satisfies the accepted requirement?”

## Decision sequence

```text
requirement
→ existing canonical options
→ capability fit
→ reuse or variant
→ bounded extension
→ primitive composition
→ product-specific component
→ semantic native platform element
→ proven capability gap
→ dependency candidate and authority
```

Do not reverse the sequence because a new library has an attractive API or familiar examples.

## Option 1 — Reuse existing component or utility

Use when the canonical abstraction already satisfies:

- task and content requirements;
- interaction and state requirements;
- accessibility contract;
- visual/token contract;
- target contexts;
- ownership and import boundary.

```yaml
reuse_decision:
  requirement: <requirement>
  selected_component_or_utility: <path/import>
  existing_contract: []
  fit_evidence: []
  required_configuration: []
  verification: []
```

Do not rebuild the same abstraction locally merely to match a mockup more quickly.

## Option 2 — Reuse an existing variant

Use when the base component is fit and an accepted variant already expresses the required density, state, intent, size, or layout.

Verify that the variant is actually canonical, not a one-off class string from an unrelated screen.

## Option 3 — Add a bounded variant

Use when:

- the canonical abstraction is still correct;
- one missing variant is broadly or repeatedly useful;
- the variant belongs to the component's owned responsibility;
- existing behavior and API can remain compatible;
- tokens and states remain coherent;
- the change has focused tests and examples.

Reject when the “variant” introduces an unrelated product workflow or turns a primitive into a god component.

```yaml
extension_decision:
  canonical_abstraction: <component/utility>
  missing_capability: <capability>
  extension_type: variant
  existing_contract_preserved: []
  new_contract_fields: []
  consumers_affected: []
  compatibility: <compatible | migration-required>
  verification: []
```

## Option 4 — Compose canonical primitives

Use when no single canonical component fits, but accepted primitives can satisfy the requirement without duplicating their responsibilities.

Examples:

```text
input + popover + command list
→ domain-specific resource picker

button + dialog + form primitives
→ bounded product workflow dialog

table primitives + existing query state
→ product-specific comparison surface
```

Composition must preserve:

- primitive APIs and state semantics;
- focus and keyboard behavior;
- semantic tokens and variants;
- error/loading/disabled behavior;
- analytics identity where applicable;
- shared query/form/state conventions.

## Option 5 — Product-specific component

A product-specific component is valid when it owns product meaning that generic primitives should not own.

It should:

- live in the owning product/module boundary;
- compose or wrap canonical primitives where applicable;
- keep domain policy out of generic shared primitives;
- expose a bounded API;
- avoid creating a parallel component or styling system;
- include tests at the product behavior boundary.

A custom component is not automatically drift. A custom reimplementation of an already-fit canonical abstraction is drift.

## Option 6 — Semantic native platform element

Use native semantic elements when they satisfy the requirement without a repository abstraction.

Examples may include:

- headings, paragraphs, sections, lists, tables, links;
- native form controls when the repository accepts them and the required contract is simple;
- `details`/`summary` for suitable disclosures;
- semantic landmarks and document structure.

Evaluate:

```text
semantic meaning
interaction requirement
browser/platform behavior
accessibility behavior
styling and token needs
shared analytics or state requirements
repository precedent
```

Do not create a shared wrapper that adds no stable behavior or policy. Do not use native controls to bypass a fit canonical product abstraction with required variants, focus behavior, validation, or state semantics.

## Option 7 — New dependency candidate

A dependency is eligible only after a proven capability gap.

### Capability gap definition

```text
accepted requirement
+ existing canonical systems reviewed
+ bounded extension and composition reviewed
+ semantic-native option reviewed when applicable
+ requirement remains unsatisfied
= capability gap candidate
```

Preference, novelty, convenience, code brevity, or trend status is not a capability gap.

## New dependency record

```yaml
new_dependency_decision:
  requested_capability: <capability>

  proven_capability_gap:
    requirement: <requirement>
    evidence: []
    existing_options_reviewed: []
    why_reuse_failed: []
    why_extension_failed: []
    why_composition_failed: []
    why_semantic_native_failed: []

  candidate:
    name: <dependency>
    owned_role: <one bounded role>
    version_or_selection_policy: <policy>

  alternatives_rejected:
    - candidate: <alternative>
      reason: <reason>

  consequences:
    bundle_or_runtime: []
    security_and_supply_chain: []
    accessibility: []
    maintenance_and_upgrade: []
    licensing_or_procurement: []
    interoperability_with_current_systems: []
    test_and_observability: []

  integration:
    owning_module: <owner>
    adapter_or_wrapper_boundary: <boundary>
    tokens_and_styling: <mapping>
    state_and_data: <mapping>
    migration_or_exit_strategy: <strategy>

  authority:
    policy_or_owner: <authority>
    decision_ref: <reference or ROUTE_FOR_APPROVAL>

  verification_plan: []
  verdict: <APPROVED | REJECTED | ROUTE_FOR_APPROVAL | NOT_VERIFIED>
```

## Consequence checklist

Before approval, inspect:

- duplicate capability with current dependencies;
- bundle, runtime, memory, or build cost;
- server/client boundary impact;
- security history and supply-chain risk;
- accessibility behavior and customization limits;
- styling/token interoperability;
- state, form, query, routing, or data ownership conflicts;
- SSR, hydration, rendering, platform, or environment constraints;
- test strategy and mocking cost;
- upgrade cadence and maintenance ownership;
- licensing, procurement, or legal authority where applicable;
- migration and removal strategy.

## Common drift cases

### Component library project, local raw dropdown

```text
canonical Select/Combobox exists and fits
+ local div-based dropdown duplicates focus, keyboard, disabled, and token behavior
→ CONVENTION_DRIFT + possible IMPLEMENTATION_DEFECT
```

### Canonical icon family, new icon package

```text
existing icon family covers required symbols
+ another package is installed for convenience
→ DEPENDENCY_DRIFT
```

### Tailwind/token system, new local stylesheet

```text
one-off CSS is used to recreate existing tokens/variants or a parallel theming grammar
→ CONVENTION_DRIFT
```

This does not mean every CSS file is forbidden. Product assets, print/export styles, complex keyframes, third-party overrides, or bounded specialized rendering may justify CSS when repository conventions permit it.

### Shared primitives, domain component composition

```text
canonical primitives remain authoritative
+ domain-specific component owns unique product behavior
→ valid product-specific composition
```

### Measured virtualization requirement

```text
existing table/list system cannot satisfy measured scale and accessibility requirement
+ alternatives and consequences are reviewed
+ authority approves one bounded rendering adapter
→ CAPABILITY_GAP with eligible dependency
```

## Decision output

```yaml
reuse_extension_decision:
  requested_capability: <capability>
  existing_options_reviewed: []
  selected_option: <reuse | reuse_variant | extend | compose | product_specific_component | semantic_native | dependency_candidate | unresolved>
  evidence: []
  rationale: <reason>
  affected_convention_locks: []
  rejected_alternatives: []
  verification_requirements: []
```

## Stop conditions

Do not proceed when:

- canonicality is unknown for a material system;
- a fit shared abstraction is bypassed without evidence;
- a migration target is being mixed without approved migration scope;
- extension would break existing consumers without an explicit migration decision;
- composition duplicates primitive behavior or loses accessibility contracts;
- a dependency has no bounded role;
- consequences or approval authority are missing;
- implementation mapping has not been produced.
