# Delegation and Verification Matrix

Load this reference during role composition, spec confirmation, production planning, and verification selection.

The workflow owns orchestration. Ports and specialists own decisions. Reviewers own acceptance. Select only capabilities justified by changed layers and acceptance criteria.

## Role slots

```yaml
role_composition:
  lifecycle_owner: redesign-workflow
  design_owner: master-design
  implementation_owner: null
  specialists: []
  reviewer_facade: design-review
  domain_reviewers: []
  coverage_mode: null
```

### Design owner

Use `master-design` for digital product, web, static communication, and presentation redesign unless a declared specialist domain owner is more appropriate.

The design owner:

```text
owns direction and synthesis
resolves specialist trade-offs
protects preservation locks
approves the layered plan and spec
never self-certifies final acceptance
```

### Implementation owner

Load `master-engineer` or a runtime-equivalent implementation owner when:

```text
output_mode is patch
prototype requires executable framework code
behavior or state logic changes
repository architecture or contracts change
```

The implementation owner:

```text
owns repository correctness and implementation boundaries
implements the approved design contract
does not replace the design owner
provides technical evidence to verification
```

### Reviewer composition

```text
digital-interface
  facade: design-review
  domain reviewer: built-in interactive strategy
  coverage: BUILT_IN

visual-communication
  facade: design-review
  domain reviewer: built-in static strategy
  coverage: BUILT_IN

presentation
  facade: design-review
  domain reviewer: built-in presentation strategy
  coverage: BUILT_IN

brand-identity
  facade: design-review
  domain reviewer: brand-identity-review when installed
  coverage: ADAPTER_COVERED
  fallback: LIMITED or ROUTE_ELSEWHERE

other
  facade: design-review
  domain reviewer: declared external adapter
  fallback: LIMITED or ROUTE_ELSEWHERE
```

## Changed-layer delegation

### Strategy

Load `design-strategy` when changing why, what, or for whom the surface communicates.

| Concern | Adapter | Trigger |
|---|---|---|
| Content inventory and sequence | `content-strategy` | content-heavy surface, missing/duplicated sections, content must be removed or reordered |
| Information architecture | `information-architecture` | navigation, grouping, labels, taxonomy, page hierarchy change |
| Copy and microcopy | `copywriting` | headline, CTA, proof, labels, status, onboarding, or tone changes |
| User cognition and trust | `ux-psychology` | confusion, cognitive load, trust, motivation, progressive disclosure |
| Conversion | `cro` | conversion is an explicit goal and CTA/funnel behavior is in scope |

Do not load `cro` for identity, showcase, informational, or internal-tool surfaces without a declared conversion goal.

### Visual

Load `design-visual` when changing visual language or expression.

| Concern | Adapter | Trigger |
|---|---|---|
| Genre / visual direction | `design-genre` | direction changes or no accepted visual language exists |
| Color roles | `design-color` | palette, semantic color, contrast, brand color behavior changes |
| Typography | `design-typography` | typeface, type roles, scale, rhythm, hierarchy changes |
| Depth and layering | `design-depth` | overlap, atmosphere, elevation, illustration integration needed |
| Iconography | `design-iconography` | icon family, stroke, size, metaphor, alignment changes |
| Composition | `composition` | focal point, balance, eye flow, figure/ground changes |
| Motion | `motion-design` | motion is required for orientation, feedback, continuity, or expression |
| Readability | `readability` | body measure, text density, contrast, viewing distance concerns |

Genre is a decision input, not a template selector. It must be reconciled with brand, density, trust, and content needs.

### Layout

Load `design-layout` when changing spatial organization.

| Concern | Adapter | Trigger |
|---|---|---|
| Page-level structure | `macrostructures` | major hierarchy, page shape, section relationship changes |
| Responsive behavior | `responsiveness` | layout must adapt across widths, orientations, or containers |
| Component substitution | `adaptive-component-design` | one component pattern does not fit all viewport/input contexts |
| Component structure | `ui-components` | nav, hero, rail, card, form, table, footer, or other reusable component changes |
| Spatial rhythm | `design-spacing` | density, section rhythm, grouping, proximity, or whitespace changes |

Do not choose a mobile component by shrinking the desktop component. Choose or substitute based on task, option count, frequency, available width, and input mode.

### Interaction

Load `design-interaction` when behavior or states change.

| Concern | Adapter | Trigger |
|---|---|---|
| Established behavior and accessibility | `ux-patterns-for-developers` | tabs, disclosure, dialog, combobox, carousel, forms, navigation, tables, or similar patterns |
| Product-level pattern choice | `ux-ui-patterns` | choosing among interaction/page-section patterns |
| Cross-context substitution | `adaptive-component-design` | tabs/rail/select/sheet/table must adapt by context |

External patterns own behavior, accessibility, and edge cases when selected. Internal components own tokens and brand expression. Do not hand-roll behavior solely to preserve a visual mockup.

### Design system

Load `design-system` when changing reusable tokens or cross-cutting rules.

| Concern | Adapter | Trigger |
|---|---|---|
| Accessibility | `accessibility` | semantics, focus, contrast, target, assistive technology, or cognitive access changes |
| Theme behavior | `dark-light-theming` | multiple themes or color-scheme behavior exist |

Existing project or brand tokens override generic adapter defaults. Do not impose one spacing base, type ratio, radius, or shadow scale on every surface.

## Delegation plan

Record only selected capabilities:

```yaml
delegation_plan:
  strategy:
    port: design-strategy
    adapters: [copywriting]
    reason: headline and CTA sequence change
  visual:
    port: design-visual
    adapters: [design-typography, design-color, composition]
    reason: hierarchy and expression change
  layout:
    port: design-layout
    adapters: [macrostructures, responsiveness, adaptive-component-design]
    reason: section model and category navigation change across widths
  interaction:
    port: design-interaction
    adapters: [ux-patterns-for-developers, adaptive-component-design]
    reason: tab overflow and touch behavior change
  system:
    owner: design-system
    adapters: [accessibility]
    reason: focus and target behavior affected
  implementation:
    owner: master-engineer
    reason: repository patch requested
```

Omit unused branches. Every adapter needs a reason traceable to the layered plan or acceptance criteria.

## Verification strategy

Select the primary packet from design domain. Add secondary packets only for actual cross-domain concerns.

### Digital interface

```text
required affected viewports, orientations, containers, and themes
changed controls, inputs, gestures, focus, overflow, and state transitions
loading, empty, error, success, permission, and recovery when affected
semantic/accessibility evidence when affected
runtime/flow completion when executable
brand/content/asset locks
changed-file diff plus relevant tests/build at commit or release boundary
```

A screenshot-only packet cannot prove runtime, keyboard, focus, hidden states, or responsive substitution.

### Visual communication

```text
final dimensions and real destination placement
actual-size legibility and text survival
crop, safe areas, overlays, bleed, and trim when applicable
supplied logo, product, human, copy, price, date, contact, and claim fidelity
resolution, edge/mask quality, compression, and color output
brand and content locks
```

Do not run keyboard, runtime, or reduced-motion gates on a static poster.

### Presentation

```text
affected slide plus complete available narrative sequence
room, screen-share, or self-guided viewing mode
headline and data legibility at delivery scale
chart/data/source integrity
slide-to-slide continuity and repeated-layout consistency
export or playback evidence
```

One attractive slide does not prove deck narrative quality.

### Brand identity

Load `brand-identity-review/references/evidence-and-hard-gates.md`.

```text
brand brief, rationale, values, audience, and naming constraints
canonical primary mark and construction evidence
small-size, minimum-size, monochrome, and inverse variants
clear space and required lockups
variant family and typography/color integration
real application contexts and production masters
similarity-risk screening with no legal-clearance claim
```

A color hero mockup does not prove identity-system readiness.

### Other specialized domain

Use evidence declared by the loaded domain reviewer. Universal visual evidence is supplementary only.

## Iteration versus release evidence

### Creative iteration

Use a focused fresh packet for changed regions, adjacent regressions, preservation locks, and the target gate. Full lint/build may be deferred when unrelated or blocked, but must be reported as deferred—not passed.

### Commit, PR, or release boundary

Run the relevant implementation, accessibility, runtime, export, or specialist production checks required by the acceptance criteria and loaded reviewers.

## Verification output

```yaml
verification_report:
  design_domain: <domain>
  artifact_state: <state>
  changed_layers: []
  viewing_contexts_checked: []
  evidence_available: []
  evidence_gaps: []
  preservation_locks:
    passed: []
    failed: []
    not_verified: []
  implementation_checks:
    passed: []
    failed: []
    deferred: []
  ready_for_facade_review: true | false
```

`ready_for_facade_review: true` means enough evidence exists to run an honest review. It does not mean the design passed.