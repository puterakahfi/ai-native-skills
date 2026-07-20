# Component-System Coverage and Typography

Load this reference after the repository implementation systems have been classified as canonical, local, legacy, migration-target, or unknown.

Knowing that a repository uses a component system is not enough. Before implementation, map the capabilities that system actually provides in the current repository.

## Component coverage evidence

Inspect:

```text
component registry configuration
shared component directories and package exports
actual source files
primitive-library imports
variant definitions and CVA contracts
Storybook stories, examples, fixtures, and tests
representative production imports
canonical registry availability
local customizations and ownership
semantic tokens and class-composition utilities
```

For source-copied systems such as shadcn/ui, the repository may not contain a package named after the system. `components.json`, source components, Radix imports, CVA variants, `cn`, semantic CSS variables, and repeated shared imports can establish the implementation model.

Do not infer that every component in an upstream catalog is already installed locally. Separate:

```text
component system is canonical
component is installed locally
variant is available locally
component is available from the canonical registry
component requires bounded extension or composition
capability remains genuinely unavailable
```

## Canonical component inventory

```yaml
canonical_component_inventory:
  system: <canonical component system>
  registry_configuration: []
  shared_paths_and_exports: []

  components:
    - capability: <button | input | select | dialog | tabs | table | other>
      component: <name/path/import>
      status: <installed | registry-available | local-only | legacy | unknown>
      primitives: []
      variants: []
      states: []
      accessibility_contract: []
      token_contract: []
      representative_usage: []
      local_customizations: []
      owner: <owner or unknown>
      evidence: []
```

Inventory components that are relevant to the proposed change. Do not enumerate an entire upstream registry without need.

## Component capability coverage map

```yaml
component_capability_coverage:
  requested_capability: <capability>
  canonical_system: <system>

  existing_components_reviewed: []
  existing_variants_reviewed: []
  composition_options_reviewed: []
  canonical_registry_options_reviewed: []
  semantic_native_eligibility: <eligible | not-eligible | partial | unknown>

  coverage_status: >-
    covered_by_existing_component |
    covered_by_existing_variant |
    covered_by_bounded_variant |
    covered_by_composition |
    available_from_canonical_registry |
    requires_product_specific_component |
    semantic_native_is_sufficient |
    proven_capability_gap |
    unknown

  selected_decision: >-
    semantic_native |
    reuse |
    reuse_variant |
    extend |
    compose |
    add_canonical_registry_component |
    product_specific_component |
    dependency_candidate |
    unresolved

  evidence: []
  rejected_alternatives: []
  verification_requirements: []
```

## Semantic-native precheck

Semantic native structure is evaluated before forcing a component wrapper.

Commonly eligible:

- `main`, `section`, `article`, `header`, `footer`, and `nav`;
- headings, paragraphs, lists, description lists, and links;
- `details` and `summary` when the platform behavior satisfies the accepted disclosure requirement;
- native controls only when repository precedent and the required interaction contract support them.

Ask:

```text
Is this a structural or content-semantic need?
Does the platform element provide the required semantics and behavior?
Is there no fit canonical abstraction adding required state, variants, accessibility, analytics, or product policy?
Can repository tokens and accessibility conventions be preserved?
```

Valid semantic HTML does not authorize duplicating a canonical interactive contract. A page may correctly use `<section>` and `<article>` while still violating conventions by recreating Dialog, Select, Tabs, Tooltip, or Button behavior locally.

## Interactive component decision ladder

For an interactive or component-system-owned capability, evaluate in order:

```text
1. reuse an existing canonical component
2. reuse an existing canonical variant
3. add a bounded variant to the canonical component
4. compose canonical primitives
5. add the component from the canonical registry
6. create a product-specific component using canonical primitives
7. introduce a new dependency only after a proven capability gap
```

### Existing component

Select it when its interaction, accessibility, token, state, responsive, and ownership contracts fit.

### Existing variant

Inspect real variant definitions and accepted examples. Do not treat an arbitrary class string from another route as a canonical variant.

### Bounded variant

Add only when the capability belongs to the shared component responsibility, preserves compatibility, and has a named repeated need.

### Composition

Compose accepted primitives when no single component fits but primitive responsibilities remain authoritative.

### Canonical registry addition

Use when:

- the repository accepts a source-component registry;
- the component is absent locally;
- the official canonical registry supplies a fitting implementation;
- adding it does not overwrite local customizations without review;
- generated/copied source becomes repository-owned and reviewable.

```yaml
canonical_registry_component_decision:
  requested_capability: <capability>
  registry: <canonical registry>
  component: <component>
  local_absence_evidence: []
  repository_configuration_compatibility: []
  target_source_path: <path>
  generated_dependencies_and_primitives: []
  tokens_variants_and_local_customizations: []
  ownership_and_update_model: <model>
  rejected_alternatives: []
  verification_plan: []
```

A canonical registry addition is not permission to pull from an unrelated registry or install a second component system.

### Product-specific component

Use when the product owns unique meaning, policy, state, or workflow that generic primitives should not own. Compose canonical primitives whenever they fit.

### Dependency candidate

Only after installed components, variants, bounded extension, composition, canonical registry availability, semantic-native eligibility, and product-specific composition have been evaluated and a measurable requirement remains unsatisfied.

## Typography role map

Typography is part of the repository component and token system. Do not inspect only font packages.

Inspect:

```text
font-family variables and loaders
type tokens or utility classes
heading and body components if present
existing page-title and section-title treatments
body measure, line-height, weight, and tracking
label, metadata, code, and supporting-text conventions
responsive type behavior
light/dark token behavior
representative production usage
```

```yaml
typography_role_map:
  font_families:
    display: <token/component/utility>
    sans: <token/component/utility>
    mono: <token/component/utility>

  semantic_roles:
    page_title:
      source: <token/component/utility/precedent>
      allowed_variants: []
      representative_usage: []
    section_title: {}
    subsection_title: {}
    body: {}
    supporting_text: {}
    label: {}
    metadata: {}
    code: {}

  extension_rules: []
  prohibited_parallel_patterns: []
  evidence: []
  verification_requirements: []
```

A route-local combination is not automatically wrong. It becomes `CONVENTION_DRIFT` when it creates an unrelated type scale or semantic role despite a fit repository contract and no named product reason.

Typography role mapping does not choose the visual direction. `design-typography`, brand, and product-design owners still define meaning and expression; implementation-context discovery maps that decision to the repository system.

## Common cases

### Installed shadcn Input exists

```text
search input needed
+ canonical Input source and production usage exist
+ route creates a new styled input contract
→ CONVENTION_DRIFT
→ reuse or bounded variant
```

### Dialog missing locally but available from canonical registry

```text
dialog behavior required
+ canonical component system is shadcn/ui
+ Dialog is absent locally
+ configured canonical registry provides Dialog
→ add canonical registry component before considering another library
```

### Semantic document structure

```text
section, article, headings, list
+ no richer shared interaction or product contract
→ semantic native is valid
```

### Div-based dialog inside semantic page

```text
semantic sections are valid
+ canonical Dialog exists and fits
+ local div overlay recreates focus, escape, portal, and accessibility behavior
→ CONVENTION_DRIFT + possible IMPLEMENTATION_DEFECT
```

### Existing typography roles

```text
page-title, section-title, body, label, metadata, and code roles exist
+ route invents unrelated sizes, weights, tracking, and measure
→ CONVENTION_DRIFT
→ map and reuse roles or record a bounded extension
```

## Completion check

Before code production:

- relevant source components and exports were inspected;
- relevant variants and representative usage were inspected;
- canonical registry availability was checked when a component was absent;
- semantic-native eligibility was separated from interactive component reuse;
- requested capabilities have explicit coverage statuses;
- typography families and semantic roles are mapped;
- implementation mapping records the selected decision and rejected alternatives;
- runtime, accessibility, rendered, and architecture verification remain explicit.