---
name: ui-components
description: UI component-pattern selection and implementation handoff. Select the capability from brief and content evidence, then map it through the repository's canonical component, styling, token, icon, and behavior systems before using templates or writing code.
license: MIT
metadata:
  ai-native-skills.version: 1.2.0
  ai-native-skills.author: puterakahfi
  ai-native-skills.type: skill
  ai-native-skills.implements: ai-native-core/contracts/skills/design/ux-ui-patterns.contract.yaml
  ai-native-skills.contract-version: ^1.0.0
  ai-native-skills.related_skills: '["implementation-context-discovery","ux-patterns-for-developers","adaptive-component-design","design-system","design-iconography","architecture-review"]'
  ai-native-skills.tags: '["ui","components","patterns","templates","behavior","implementation-context"]'
---

# UI Components

Select the component capability first. Map it to the repository second. Implement only after both decisions exist.

```text
brief signals + content inventory
→ pattern decision
→ component capability contract
→ implementation-context-discovery
→ reuse / variant / extend / compose / semantic-native / dependency decision
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

Component work starts with `brief_signals` and `content_inventory`. Select the pattern through the relevant decision tree, record the `decision_tree_path`, and verify that the pattern matches the real content volume and user task.

The selected pattern is a capability decision, not permission to introduce a new component or styling system.

## Hard rules

1. Select the component capability from task, content, and context before implementation.
2. Treat requested components and reference templates as proposals, not immutable requirements.
3. For existing repositories, load `implementation-context-discovery` before code production.
4. Reuse a fit canonical component and existing variant before local implementation.
5. Prefer bounded extension or composition of canonical primitives before a parallel system.
6. Native semantic elements remain valid when no shared abstraction or richer behavior contract is needed.
7. Do not rebuild focus, keyboard, validation, disabled, loading, token, or state behavior already owned by a canonical component.
8. Do not install another component, icon, styling, state, form, query, or animation library without a proven capability gap and authority.
9. Templates in this skill are generic implementation examples. They never override product framework, component-library, styling, token, or iconography conventions.
10. External behavior still routes through `ux-patterns-for-developers` or the active interaction owner.
11. Component substitution across contexts routes through `adaptive-component-design`.
12. Source alignment does not prove rendered or interaction acceptance.

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

  implementation_context:
    canonical_component_candidates: []
    canonical_variants: []
    canonical_primitives: []
    styling_and_token_system: <system>
    iconography_implementation: <system>
    behavior_and_state_systems: []

  implementation_decision: <reuse | reuse_variant | extend | compose | product_specific_component | semantic_native | dependency_candidate | unresolved>
  selected_path_or_import: <path or unresolved>
  rejected_alternatives: []
  verification_requirements: []
```

`implementation_context` and `implementation_decision` are produced by `implementation-context-discovery`, not inferred from the template index.

## Component index

Load references for capability anatomy, generic patterns, and verification prompts:

| Component | Reference file | Load command |
|---|---|---|
| Navbar | `navbar.md` | `skill_view(name='ui-components', file_path='references/navbar.md')` |
| Hero | `hero.md` | `skill_view(name='ui-components', file_path='references/hero.md')` |
| Section / Work row | `sections-a.md` | `skill_view(name='ui-components', file_path='references/sections-a.md')` |
| About / Contact / Footer | `sections-b.md` | `skill_view(name='ui-components', file_path='references/sections-b.md')` |
| Interaction and verification | `interactions.md` | `skill_view(name='ui-components', file_path='references/interactions.md')` |

Use a reference only after pattern selection. Translate its capability and behavior into the repository's accepted implementation system.

## Repository mapping examples

```text
selected capability: dialog
repository has fit canonical Dialog
→ reuse it; do not create a fixed-div overlay

selected capability: searchable selector
repository has Input + Popover + Command primitives
→ compose them inside the owning product component

selected capability: simple document disclosure
repository has no shared abstraction and native semantics are sufficient
→ semantic-native details/summary may be valid

selected capability: virtualized grid
existing systems fail a measured requirement
→ CAPABILITY_GAP record before dependency proposal
```

## Failure signals

- Pattern chosen by appearance without a decision-tree path.
- Template copied before repository implementation context is known.
- Generic CSS template replaces an accepted component or token system.
- A canonical component is bypassed with local raw behavior and no evidence.
- A second icon or component library is introduced for convenience.
- Native semantic structure is rejected merely because a library exists.
- Domain behavior is pushed into generic shared primitives.
- Source-only inspection is labeled rendered or interaction PASS.

## Completion

Component specification is ready for implementation only when:

- the capability and decision-tree path are explicit;
- content, state, interaction, accessibility, and context requirements are explicit;
- repository canonical systems are discovered;
- reuse/extension/composition/native/dependency decision is recorded;
- implementation paths and prohibited parallel systems are mapped;
- applicable architecture, runtime, accessibility, and design verification is planned.
