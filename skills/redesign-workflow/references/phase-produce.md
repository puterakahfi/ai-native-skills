# Phase 8 — Delegated Production

Load this reference only after route, roles, direction, layered plan, value alignment, spec, and approval boundary are explicit.

Load `quality-levels.md` before production. Q0 blocks production. Every produced artifact must reach at least Q1 `FOUNDATION_SAFE` before it may be handed to rendered verification.

Production implements the approved design contract through selected ports and adapters. It does not invent a second direction or import generic UI defaults as universal rules.

## Entry packet

```yaml
production_input:
  design_domain: <domain>
  surface_profile: <profile>
  output_mode: <prototype | patch>
  quality_target: <Q1_FOUNDATION_SAFE | Q2_RENDER_VERIFIED | Q3_PIXEL_POLISHED | Q4_PIXEL_MATCHED>
  design_owner: <owner>
  implementation_owner: <owner or null>
  delegation_plan: <selected ports and adapters>
  direction: <approved direction>
  layered_plan: <preserve/refine/replace decisions>
  foundation_axis_contract:
    F1_hierarchy: <resolved relationship>
    F2_grouping: <resolved relationship>
    F3_alignment: <resolved system>
    F4_space_and_rhythm: <resolved system>
    F5_balance: <resolved intent>
    F6_flow: <resolved order>
    F7_legibility: <resolved context>
    F8_system_consistency: <resolved system>
    F9_accessibility_and_affordance: <resolved baseline>
    F10_responsive_continuity: <resolved transformation>
  acceptance_criteria: []
  viewing_contexts: []
  locks:
    brand: []
    design_system: []
    content: []
    assets: []
    behavior: []
    preserved_regions: []
```

Stop when the packet is incomplete, any required foundation axis remains unresolved, or the approval policy has not passed.

F1–F10 are planning and assessment axes. Production and review findings still use canonical registered gate IDs through `design-review`.

## Production sequence

```text
1. Resolve content and copy that affect structure.
2. Apply approved macrostructure and information hierarchy.
3. Declare or preserve the project design system and tokens.
4. Select components and cross-context substitutions by task.
5. Implement behavior through established patterns when available.
6. Apply visual language, type, color, composition, depth, imagery, and motion.
7. Preserve locked assets, content, behavior, and accepted regions.
8. Produce a renderable/exportable artifact.
9. Check the produced artifact against the Q1 foundation-safe contract.
10. Record what changed and why.
11. Hand off to domain-appropriate verification.
```

The sequence may overlap during implementation, but later styling must not hide unresolved content, structure, interaction, accessibility, or foundation problems.

## Delegation rules

Load only adapters declared in `delegation_plan`.

```text
strategy
  design-strategy + selected adapters

visual
  design-visual + selected adapters

layout
  design-layout + selected adapters

interaction
  design-interaction + selected adapters

system
  design-system + selected adapters

implementation
  master-engineer or runtime equivalent when executable code is produced
```

See `delegation-and-verification.md` for selection rules.

## Contextual defaults, not universal rules

The following must come from the approved brand, project system, selected genre/profile, or explicit design decision:

```text
type scale and ratio
spacing base and density
container width and breakpoints
radius and elevation system
background treatment
hero height and section rhythm
number of columns or cards
component type on each viewport
motion stance and timing
light/dark theme architecture
```

Do not globally require:

```text
one fixed modular type scale
one fixed spacing grid
one gradient, dot pattern, or figure/ground technique
a fixed hero padding or min-height rule
a card/grid arrangement based only on item count
the same component pattern across mobile, tablet, and desktop
motion or depth merely to make the result feel “premium”
```

Adapter defaults are starting hypotheses. Existing product constraints, task density, content, viewing context, and brand locks may require a different valid system.

## Component selection

Choose components by:

```text
user task and decision frequency
number and hierarchy of options
available width and orientation
input mode and target size
content length and localization risk
discoverability and overflow behavior
state complexity and accessibility
existing component-system compatibility
```

Examples:

```text
category navigation on wide tablet
  may use line tabs or horizontal rail when peers remain reachable

same navigation on narrow mobile
  may use a scroll rail, select, sheet, or another substitution

large comparison table on mobile
  may become a focused detail pattern rather than a squeezed desktop table
```

Never force the user-requested component when another pattern better satisfies the underlying task. Record the substitution rationale.

## External versus internal ownership

```text
external trusted pattern
  behavior, keyboard/touch semantics, states, accessibility, edge cases

internal product component
  tokens, copy, layout integration, visual expression, brand treatment
```

Check `ux-patterns-for-developers` before hand-rolling established behavior. Do not copy an external visual style that conflicts with the product system.

## Output modes

### Prototype

```text
create a safe renderable or exportable artifact
avoid destructive changes to the source product
make changed regions and states inspectable
record mock data or simulated behavior honestly
```

A prototype does not prove production runtime, data integration, Q2 rendered verification, or release readiness.

### Patch

```text
implementation owner applies the approved design contract
preserve the last known good state
respect repository architecture and existing component system
run changed-file checks during iteration
run relevant full checks at commit/PR/release boundary
record changed files and rollback path
```

The design owner resolves design trade-offs. The implementation owner resolves technical trade-offs without silently altering the approved direction.

## Asset and content handling

```text
use supplied assets when they are locked
never invent prices, claims, dates, contacts, testimonials, metrics, or product facts
never alter required product or human identity without explicit scope
preserve source attribution and data provenance when applicable
record generated or placeholder assets as such
```

When imagery or motion tooling is unavailable, choose an honest fallback rather than claiming generation occurred.

## Q1 foundation-safe self-check

Before verification:

```text
□ F1–F10 foundation-axis contract is resolved in the produced artifact.
□ Parent, child, sibling, metadata, and action roles do not collapse unintentionally.
□ Grouping and spacing communicate relationships rather than repeat one arbitrary gap.
□ Shared structural or optical alignment logic exists; local nudges do not replace it.
□ Typography, measure, contrast, density, and content fit the intended context.
□ Balance, focal order, and reading/task flow are deliberate.
□ Responsive/adaptive transformation preserves hierarchy, grouping, and usability.
□ Existing design system, brand, accessibility, and behavior locks are preserved.
□ No component or decoration was selected only from agent preference.
```

## Production self-check

```text
□ Output follows the approved direction and layered plan.
□ Every selected adapter has a declared reason.
□ No unused adapter rules were imported.
□ Content and copy are final enough to verify layout honestly.
□ Components fit task and context rather than merely matching desktop mockups.
□ Existing project/brand system overrides generic defaults.
□ Required assets and facts remain faithful.
□ Preserved regions and behaviors were not changed accidentally.
□ Artifact can be rendered or exported for the declared verification strategy.
□ Implementation changes have a rollback path.
□ Current evidence supports Q1_FOUNDATION_SAFE and no higher visual claim is made yet.
```

## Production report

```yaml
production_report:
  output_mode: <prototype | patch>
  artifact: <path or target>
  quality_target: <level>
  quality_achieved: Q1_FOUNDATION_SAFE
  design_owner: <owner>
  implementation_owner: <owner or null>
  foundation_axis_summary:
    passed: []
    blocked: []
  adapters_used:
    - capability: <skill>
      reason: <trace to plan or criterion>
  changed_layers: []
  changed_regions_or_files: []
  preserved_locks_checked: []
  substitutions:
    - requested_or_previous_pattern: <pattern>
      selected_pattern: <pattern>
      reason: <task/context rationale>
  placeholders_or_simulations: []
  rollback: <path or method>
  ready_for_verification: true | false
```

`ready_for_verification` means a current Q1 candidate exists. It does not mean the artifact rendered correctly, passed review, reached Q2/Q3, or is ready for delivery.
