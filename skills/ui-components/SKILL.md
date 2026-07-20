---
name: ui-components
description: UI component-pattern selection and implementation handoff. Select the capability from task and content evidence, classify its hierarchy level, route shared organisms and templates through component-family-design, then require repository coverage, variants, registry availability, typography roles, tokens, icons, and behavior mapping before code.
license: MIT
metadata:
  ai-native-skills.version: 1.4.0
  ai-native-skills.author: puterakahfi
  ai-native-skills.type: skill
  ai-native-skills.implements: ai-native-core/contracts/skills/design/ux-ui-patterns.contract.yaml
  ai-native-skills.contract-version: ^1.0.0
  ai-native-skills.related_skills: '["component-family-design","implementation-context-discovery","ux-patterns-for-developers","adaptive-component-design","design-system","design-typography","design-iconography","architecture-review"]'
  ai-native-skills.tags: '["ui","components","patterns","templates","component-families","component-coverage","typography","registry","implementation-context"]'
---

# UI Components

Select the UI capability first. Classify composition responsibility second. Map repository coverage only after the family decision is known.

```text
brief signals + content inventory
→ pattern decision
→ hierarchy classification
→ shared family / template decision
→ adaptive component strategy
→ implementation-context-discovery
→ component coverage + typography mapping
→ semantic-native / reuse / variant / extend / compose / registry / product-specific / dependency decision
→ implementation
→ architecture and design verification
```

## Core contract interface

```yaml
required_inputs:
  - brief_signals
  - content_inventory
allowed_outputs:
  - pattern_selection
  - decision_tree_path
  - pattern_gate_scores
quality_gates:
  - pattern_selected_from_decision_tree_not_arbitrary
  - hero_pattern_matches_content_volume
```

Component work starts with task, content, and context. Select the pattern through the relevant decision tree, record the path, and verify that the pattern matches real content volume and user behavior.

A selected pattern is a capability decision, not proof that a component exists locally, not proof that a new component family is required, and not permission to introduce a parallel system.

## Hard rules

1. Select component capability from task, content, states, and contexts before implementation.
2. Treat requested component names and reference templates as proposals, not immutable implementation choices.
3. Classify the requested surface as atom, molecule, organism, template, or page before route-local creation.
4. Route repeated organisms, shells, and equivalent cross-route product roles through `component-family-design`.
5. In existing repositories, load `implementation-context-discovery` before code production.
6. Require actual component, family, export, variant, story/example, representative usage, and ownership evidence.
7. Require component capability and component-family coverage before local component creation.
8. Reuse a fit canonical component, family, and existing variant before local styling or behavior duplication.
9. Prefer bounded variants and canonical primitive composition before product-specific or parallel systems.
10. When a canonical source-component registry exists, evaluate its official component before another library or custom primitive.
11. Treat generated registry source as repository-owned implementation requiring review.
12. Map typography semantic roles before creating route-local type scales.
13. Native semantic elements remain valid when no richer shared interaction or product contract is needed.
14. Semantic structure does not authorize rebuilding focus, keyboard, portal, validation, disabled, loading, token, or state behavior already owned by a canonical component.
15. Different route content, labels, actions, or menu items do not automatically justify a new organism family.
16. Component substitution across contexts routes through `adaptive-component-design` and must preserve the accepted family identity.
17. Do not install another component, icon, styling, typography, state, form, query, or animation system without a proven capability gap and authority.
18. Generic templates never override repository framework, component, family, token, typography, icon, or behavior conventions.
19. Source alignment does not prove component fitness, family consistency, runtime, rendered, interaction, or accessibility acceptance.

## Hierarchy and family preflight

Before implementation, return:

```yaml
component_hierarchy_classification:
  capability: <capability>
  level: atom | molecule | organism | template | page
  product_role: <role>
  family_relevance: none | existing_family_candidate | new_family_candidate | unknown

family_requirement:
  existing_family: <family or none>
  existing_variants: []
  required_variant: <variant or none>
  invariant_anatomy: []
  configurable_slots: []
  route_instances: []
  new_family_justification: <evidence or none>
```

For organisms and templates, load `component-family-design` before repository implementation mapping.

## Component capability handoff

```yaml
component_capability_handoff:
  pattern_selection: <pattern>
  decision_tree_path: []
  user_task: <task>
  content_contract: <content>
  required_states: []
  required_interactions: []
  accessibility_contract: []
  target_contexts: []

  hierarchy_and_family:
    hierarchy_level: <level>
    component_family: <family or unresolved>
    template_family: <family or not-applicable>
    family_decision: <reuse | reuse_variant | extend | compose | migrate_local | create_new | unresolved>
    invariant_anatomy: []
    configurable_slots: []
    route_instance_mapping: []

  implementation_context:
    canonical_component_system: <system or unknown>
    component_capability_coverage: <coverage status>
    canonical_component_candidates: []
    canonical_variants: []
    canonical_primitives: []
    canonical_registry_candidates: []
    canonical_component_family_candidates: []
    canonical_template_candidates: []
    semantic_native_eligibility: <eligible | not-eligible | partial | unknown>
    typography_roles: []
    styling_and_token_system: <system>
    iconography_implementation: <system>
    behavior_and_state_systems: []
    evidence_gaps: []

  implementation_decision: <semantic_native | reuse | reuse_variant | extend | compose | add_canonical_registry_component | product_specific_component | dependency_candidate | unresolved>
  selected_path_import_or_registry_component: <value or unresolved>
  rejected_alternatives: []
  verification_requirements: []
```

`hierarchy_and_family` comes from `component-family-design`. `implementation_context` comes from `implementation-context-discovery`, not from the template index.

## Component index

Load references only after pattern and family selection:

| Component | Reference file |
|---|---|
| Navbar | `references/navbar.md` |
| Hero | `references/hero.md` |
| Section / Work row | `references/sections-a.md` |
| About / Contact / Footer | `references/sections-b.md` |
| Interaction and verification | `references/interactions.md` |

References describe generic capability anatomy. Translate them through the accepted component family and repository implementation system.

## Repository mapping examples

```text
selected capability: input
repository has fit canonical Input and production usage
→ reuse it

selected capability: outline action
canonical Button has a fit outline variant
→ reuse_variant

selected capability: product navbar
repository has AppHeader organism family
+ menu and actions differ by route
→ component-family-design
→ reuse AppHeader with product variant and slots

selected capability: product shell
repository has AppShell template family
→ reuse template with route-specific content and header variant

selected capability: dialog
canonical source-component system is accepted
+ Dialog is absent locally
+ official registry Dialog fits
→ add_canonical_registry_component

selected capability: searchable resource picker
Input + Popover + Command exist
+ product owns domain policy
→ compose into a product-specific component

selected capability: document structure
section, headings, list, and details/summary satisfy the requirement
→ semantic_native

selected capability: virtualized grid
components, families, variants, composition, registry, and product adapters fail a measured requirement
→ CAPABILITY_GAP before dependency proposal
```

## Typography implementation handoff

When the pattern includes text hierarchy, hand off semantic roles rather than arbitrary class strings:

```yaml
typography_handoff:
  page_title: <repository role/token/component>
  section_title: <repository role/token/component>
  subsection_title: <repository role/token/component>
  body: <repository role/token/component>
  supporting_text: <repository role/token/component>
  label: <repository role/token/component>
  metadata: <repository role/token/component>
  code: <repository role/token/component>
  bounded_extensions: []
  verification_requirements: []
```

The design owner defines expression. Component-family design preserves it across family instances. Implementation-context discovery maps it to repository roles and permitted extensions.

## Failure signals

- Pattern chosen by appearance without a decision-tree path.
- Hierarchy level is not classified before a route-local organism or template is created.
- Template copied before repository and family context are known.
- A library name is known but actual component, family, or variant coverage is not.
- A fit component, family, or variant is bypassed by route-local implementation.
- Equivalent routes create unrelated headers, sidebars, shells, cards, or forms without a proven role gap.
- A canonical registry option is skipped for another library or custom primitive.
- A route creates an unrelated typography system despite fit repository roles.
- Semantic HTML is rejected merely because a library exists.
- Semantic structure is used to excuse a duplicated interactive contract.
- A second icon or component system is introduced for convenience.
- Source-only inspection is labeled component-fit, family-consistent, rendered, interaction, or accessibility PASS.

## Completion

Ready for implementation only when:

- the capability and decision path are explicit;
- hierarchy level and product role are explicit;
- organisms/templates have a family decision and route-instance map;
- invariant anatomy and configurable slots are separated;
- content, states, interactions, accessibility, and contexts are explicit;
- repository canonical systems are discovered;
- actual components, families, variants, registry options, and typography roles are mapped;
- paths, imports, registry additions, and prohibited parallel systems are explicit;
- adaptive variants preserve family identity;
- architecture, runtime, cross-route design, accessibility, and interaction verification is planned.
