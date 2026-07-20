# Reuse, Extension, Registry, and Dependency Decisions

Load this reference after repository evidence, canonicality, component coverage, and typography roles are available.

The question is not “which library would I choose from scratch?” It is “what is the smallest repository-consistent implementation that satisfies the accepted requirement?”

## Decision model

Structural and content-semantic needs receive a semantic-native precheck.

Interactive or component-system-owned capabilities follow:

```text
requirement
→ existing component
→ existing variant
→ bounded variant
→ canonical primitive composition
→ canonical registry component
→ product-specific component using canonical primitives
→ proven capability gap
→ dependency candidate and authority
```

Do not reverse the sequence because another library has a familiar API.

## Semantic-native precheck

Use a native semantic element when:

- the need is structural or content-semantic;
- the platform supplies the required semantics and behavior;
- no fit shared abstraction adds required state, accessibility, analytics, variants, or product policy;
- repository tokens and accessibility conventions can be preserved.

Common examples include landmarks, headings, paragraphs, lists, description lists, links, and suitable `details`/`summary` disclosures.

Native structure does not authorize rebuilding a fit canonical interaction contract. A page can correctly use `<section>` while still drifting by implementing a div-based Dialog or Select.

## Option 1 — Reuse an existing component or utility

Use when the canonical abstraction satisfies task, interaction, accessibility, token, responsive, ownership, and import requirements.

```yaml
reuse_decision:
  requirement: <requirement>
  selected_component_or_utility: <path/import>
  existing_contract: []
  fit_evidence: []
  required_configuration: []
  verification: []
```

Do not rebuild the same abstraction locally to match a mockup faster.

## Option 2 — Reuse an existing variant

Inspect actual variant definitions, stories/examples, and production usage. Use a fit accepted variant before route-local restyling.

An arbitrary class string from another page is not automatically a canonical variant.

## Option 3 — Add a bounded variant

Use when the canonical component remains the right owner, the missing variation is named and reusable, API compatibility is preserved, and tokens/states remain coherent.

```yaml
bounded_variant_decision:
  canonical_component: <component>
  requested_capability: <capability>
  existing_variants_reviewed: []
  new_variant: <name>
  owned_responsibility: <responsibility>
  compatibility: <compatible | migration-required>
  affected_consumers: []
  verification: []
```

Reject a “variant” that embeds unrelated product workflow or turns a primitive into a god component.

## Option 4 — Compose canonical primitives

Use when no single component fits but accepted primitives can satisfy the requirement without duplicating their responsibilities.

Examples:

```text
Input + Popover + Command
→ product resource picker

Button + Dialog + form primitives
→ product workflow dialog

Table primitives + accepted query state
→ comparison surface
```

Preserve primitive APIs, state semantics, focus and keyboard behavior, semantic tokens, error/loading/disabled behavior, analytics identity, and repository form/query/state conventions.

## Option 5 — Add a component from the canonical registry

Use when:

- the repository accepts a source-component registry;
- the component is absent locally;
- the configured canonical registry supplies a fit implementation;
- the generated source and dependencies fit repository configuration;
- local customizations will not be overwritten without review.

```yaml
canonical_registry_component_decision:
  requested_capability: <capability>
  canonical_registry: <registry>
  component: <component>
  local_absence_evidence: []
  repository_configuration_compatibility: []
  generated_or_copied_source_destination: <path>
  generated_dependencies_and_primitives: []
  tokens_variants_and_local_customizations: []
  ownership_and_update_model: <model>
  rejected_alternatives: []
  verification_plan: []
```

Generated or copied source becomes repository-owned. Review it like any other implementation.

A canonical registry addition is not permission to use an unrelated registry or install a second component system.

## Option 6 — Product-specific component

A product-specific component is valid when it owns product meaning, policy, durable state, or workflow that generic primitives should not own.

It should:

- live in the owning product/module boundary;
- compose or wrap canonical primitives when they fit;
- keep domain policy out of generic shared primitives;
- expose a bounded API;
- avoid a parallel component or styling system;
- include product-behavior tests.

A custom component is not automatically drift. A custom reimplementation of a fit canonical abstraction is drift.

## Option 7 — Dependency candidate

A dependency is eligible only after a proven capability gap.

```text
accepted requirement
+ existing components reviewed
+ existing variants reviewed
+ bounded extension reviewed
+ composition reviewed
+ canonical registry reviewed
+ semantic-native eligibility reviewed
+ product-specific composition reviewed
+ requirement remains unsatisfied
= capability gap candidate
```

Preference, novelty, convenience, code brevity, or trend status is not a capability gap.

```yaml
new_dependency_decision:
  requested_capability: <capability>
  proven_capability_gap:
    requirement: <requirement>
    evidence: []
    existing_options_reviewed: []
    why_reuse_failed: []
    why_variant_failed: []
    why_extension_failed: []
    why_composition_failed: []
    why_registry_failed: []
    why_semantic_native_failed: []
    why_product_specific_failed: []
  candidate:
    name: <dependency>
    owned_role: <one bounded role>
    version_or_selection_policy: <policy>
  alternatives_rejected: []
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

## Common classifications

### Existing Button/Input/Select rebuilt locally

```text
fit canonical component or variant exists
+ route creates a parallel visual and interaction contract
→ CONVENTION_DRIFT
```

### Dialog absent locally but available from canonical registry

```text
canonical source-component registry is accepted
+ Dialog is absent locally
+ registry Dialog satisfies the requirement
→ add_canonical_registry_component
```

### Existing typography roles ignored

```text
page-title, section-title, body, label, metadata, and code roles exist
+ route invents an unrelated local scale
→ CONVENTION_DRIFT
```

### Canonical icon family, new icon package

```text
existing icon family covers required symbols
+ another package is added for convenience
→ DEPENDENCY_DRIFT
```

### Valid product composition

```text
canonical primitives remain authoritative
+ product component owns unique policy or workflow
→ valid product-specific composition
```

### Measured virtualization gap

```text
existing components, variants, composition, registry, and product adapters cannot satisfy measured scale and accessibility
+ consequences and authority are reviewed
→ CAPABILITY_GAP with eligible dependency candidate
```

## Decision output

```yaml
reuse_extension_decision:
  requested_capability: <capability>
  existing_options_reviewed: []
  selected_option: <semantic_native | reuse | reuse_variant | extend | compose | add_canonical_registry_component | product_specific_component | dependency_candidate | unresolved>
  evidence: []
  rationale: <reason>
  affected_convention_locks: []
  rejected_alternatives: []
  verification_requirements: []
```

## Stop conditions

Do not proceed when canonicality or component coverage is unknown, a fit abstraction is bypassed, a canonical registry option is skipped without evidence, a migration target is mixed without scope, an extension breaks consumers without migration authority, composition duplicates primitive behavior, a dependency has no bounded role, consequences or approval are missing, or implementation mapping has not been produced.