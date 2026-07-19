# Phase 8 — Delegated Production

Load this reference only after route, roles, direction, layered plan, value alignment, spec, and approval boundary are explicit.

Production implements the approved design contract through selected ports and adapters. It does not invent a second direction or import generic UI defaults as universal rules.

## Entry packet

```yaml
production_input:
  design_domain: <domain>
  surface_profile: <profile>
  output_mode: <prototype | patch>
  design_owner: <owner>
  implementation_owner: <owner or null>
  delegation_plan: <selected ports and adapters>
  direction: <approved direction>
  layered_plan: <preserve/refine/replace decisions>
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

Stop when the packet is incomplete or the approval policy has not passed.

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
9. Record what changed and why.
10. Hand off to domain-appropriate verification.
```

The sequence may overlap during implementation, but later styling must not hide unresolved content, structure, interaction, or accessibility problems.

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

A prototype does not prove production runtime, data integration, or release readiness.

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

## Production self-check

Before verification:

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
```

## Production report

```yaml
production_report:
  output_mode: <prototype | patch>
  artifact: <path or target>
  design_owner: <owner>
  implementation_owner: <owner or null>
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

`ready_for_verification` means a current artifact exists. It does not mean the artifact passed.