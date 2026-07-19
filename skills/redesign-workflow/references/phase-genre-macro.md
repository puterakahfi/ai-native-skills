# Phase 3–4 — Foundation, Genre, Macrostructure, Visual Language, and Layered Plan

## Phase 3A: Foundation resolution

Load `design-foundation/SKILL.md` first. Load `design-foundation/references/principles.md` when composition decisions are required.

Foundation is incomplete until universal relationships are recorded in run state.

```yaml
foundation_contract:
  hierarchy_roles:
    primary: []
    supporting: []
    tertiary: []
  grouping_model:
    parent_child_groups: []
    sibling_sets: []
    within_group_intervals: []
    between_group_intervals: []
  alignment_model:
    page_shell: <value | unresolved>
    structural_anchors: []
    optical_corrections: []
    allowed_exceptions: []
  spatial_rhythm:
    section_intervals: []
    component_intervals: []
    intentional_voids: []
  balance_strategy: <symmetric | asymmetric | centered | distributed | unresolved>
  flow:
    first_focal_point: <value | unresolved>
    reading_or_task_sequence: []
    next_action_path: []
  legibility_requirements: []
  system_consistency_requirements: []
  accessibility_requirements: []
  responsive_continuity_rules: []
  evidence_gaps: []
```

Hard rule:

```text
design-foundation hard requirements
  > brand and DESIGN.md expression rules
  > explicit user direction
  > selected genre constraints
  > macrostructure and component defaults
```

Brand and genre decide expression. They may not erase hierarchy, grouping, alignment, balance, flow, legibility, accessibility, or responsive continuity.

## Phase 3B: Genre resolution

Load `design-genre/SKILL.md` only after foundation resolution. Genre selection is incomplete until the selected genre reference is loaded and its constraints are stored in run state.

### Signal routing

```text
Explicit user genre direction
  → authoritative unless a locked brand/design system conflicts

ZEN / MINIMALIST
  zen, stillness, restraint, ma, sparse, wabi-sabi, negative space,
  quiet senior portfolio, focus on space, few interruptions

EDITORIAL
  personal portfolio, publication, studio, writing, art direction

MODERN-MINIMAL
  SaaS, enterprise, developer tool, dashboard, productivity

ATMOSPHERIC
  generative media, music, video, cinematic, ambient creative tool

PLAYFUL
  consumer, casual, family, social, friendly, lifestyle
```

Do not let product-category signals silently override an explicit genre. A personal engineering portfolio can remain zen even when its content includes SaaS, APIs, agents, and developer tools.

### Mandatory genre handoff

```yaml
genre_contract:
  genre: <zen-minimalist | editorial | modern-minimal | atmospheric | playful>
  signals_matched: []
  explicit_user_direction: <value | none>
  reference_loaded: <path>
  composition_rules: []
  containment_rules: []
  density_rules: []
  line_or_surface_budget: []
  alignment_rails: []
  arbitrary_offset_budget: <number>
  responsive_collapse_rules: []
  color_rules: []
  motion_rules: []
  hard_failures: []
```

Hard rule:

```text
foundation contract
  > selected genre reference
  > generic redesign production defaults
  > macrostructure template defaults
  > component template defaults
```

If a generic rule conflicts with foundation or the selected genre reference, follow the higher contract and record the override.

## Phase 3C: Macrostructure pick

### Extract brief signals

```text
□ Primary goal:       convert | showcase | inform | entertain | brand
□ Identity weight:    high = person leads | low = work leads
□ Content volume:     N products / N sections
□ Audience:           hiring manager | client | developer | general
□ CTA present:        yes | no
□ Visual assets:      yes | no
□ Foundation contract:resolved | unresolved
□ Genre contract:     resolved | unresolved
```

### Signal → pattern

| Goal | Identity | Volume | Audience | Candidate macrostructure |
|---|---|---|---|---|
| showcase | high | ≤3 | hiring manager | Marquee Hero or Specimen |
| showcase | high | ≤3 | creative client | Studio or Atelier |
| showcase | low | 4+ | any | Bento or Workbench |
| inform | low | high | developer | Long Document or Almanac |
| convert | low | medium | general | Newsprint or Manifesto |
| brand | high | low | general | Manifesto or Lumen |

Candidate does not equal approval. Validate it against both the foundation and loaded genre contracts.

```text
Example:
  Bento may fit volume=4+, but must be rejected when it would flatten
  parent/child hierarchy, break grouping, or violate a space-led genre.
```

### Diversification check

```text
Previous macrostructure: [name | none]
Candidate: [name]
Must differ on at least two axes when variety is needed.
Axes: layout lead / heading / divider / button / image / reveal

Foundation clarity, brief match, and genre conformance always outrank forced variety.
```

### State pick with justification

```yaml
design_direction:
  foundation_reference: <design-foundation path>
  foundation_requirements:
    hierarchy: []
    grouping: []
    alignment: []
    space_rhythm: []
    balance: []
    flow: []
    responsive_continuity: []
  genre: <name>
  genre_reference: <path>
  macrostructure: <name>
  visual_language: <short definition>
  page_shell: <width/token/primitive>
  primary_alignment_rails:
    - <label rail>
    - <main heading rail>
    - <supporting content rail>
    - <action rail if applicable>
  focal_offsets: []
  responsive_rail_collapse: <rule>
  justified_by:
    - signal: <signal>
      reason: <reason>
  rejected_options:
    - option: <name>
      reason: <foundation, genre, or brief conflict>
  inherited_hard_constraints:
    - <constraint copied from foundation or genre contract>
```

A macrostructure is incomplete until its hierarchy roles, grouping relationships, page shell, persistent alignment rails, flow, and responsive collapse are declared. Local component grids must inherit from those decisions instead of inventing new relationships.

## Phase 3D: Visual language definition

Translate the genre into concrete expression rules after foundation relationships are resolved. A theme word or palette swap is insufficient.

### Zen / Minimalist

Load `design-genre/references/zen.md`. Do not summarize away its hard constraints.

```text
Inherited foundation:
  hierarchy       → parent, child group, siblings, and details remain distinct
  grouping        → within-group < between-group where applicable
  alignment       → stable structural and optical anchors
  balance         → empty space participates in weight distribution
  flow            → one clear focal path and discoverable next region

Genre expression:
  Ma / emptiness   → negative space performs grouping and separation
  Restraint        → remove before styling
  Stillness        → no hover lift, glow, or decorative urgency
  One focal object → one dominant anchor per viewport
  Low interruption→ few containers, badges, surfaces, and lines

Containment:
  whitespace > shared alignment rails > proximity > text measure > rare surface
  structural section borders = 0
  repeated row separators = 0 by default
  dense-list exception = one leading or trailing hairline, not per row
  visible structural lines = target 0, maximum 1 per typical viewport

Alignment:
  one persistent page shell across nav, hero, sections, contact, and footer
  define 2–4 reusable vertical start positions
  major labels, headings, titles, content, and actions reuse those rails
  asymmetry comes from span, measure, and whitespace—not repeated manual nudging
  arbitrary per-item offset budget = 0 by default
  one documented focal illustration offset may be allowed

Layout:
  asymmetrical whitespace, narrow measures, intentional intervals
  no equal-weight card catalog
  no card-to-hairline substitution
  no unrelated section-specific alignment systems

Typography:
  fewer sizes, lighter weights, generous leading, one display moment
  child titles must remain subordinate to parent display statements

Motion:
  stillness; restrained fade only when useful
```

Auto-fail after a zen request:

```text
❌ palette becomes warm but density remains high
❌ cards are removed and every row gains border-top/border-bottom
❌ ordinary sections are divided with border-y
❌ more than one visible structural line in a typical viewport without domain need
❌ every section has a headline followed by a ruled list
❌ metadata becomes repeated badges, tags, or labels
❌ repeated translate-x, arbitrary percentage margins, or padding offsets create row drift
❌ headings and body blocks begin on unrelated rails without hierarchy reason
❌ nav, page content, and footer use accidentally different shells
❌ mobile reading order zig-zags because desktop offsets survive collapse
❌ parent, child group, and siblings use equal spacing and visual weight
❌ motion or decoration is used before hierarchy, grouping, spacing, alignment, and silence are solved
```

Zen check before production:

```text
1. What will be removed?
2. Which relationships are communicated by space alone?
3. What is the focal object in each viewport?
4. What is the structural line budget?
5. What are the persistent page rails?
6. Which elements are allowed to break a rail, and why?
7. How do the rails collapse on mobile?
8. How are parent, child-group, and sibling levels distinguished?
9. Which generic component defaults are explicitly overridden?
```

### Other genres

Load the corresponding `design-genre/references/<genre>.md` and copy its concrete constraints into `genre_contract`. Do not improvise from the genre name alone. All genres inherit the same foundation hierarchy, grouping, alignment, balance, flow, legibility, accessibility, and responsive-continuity requirements.

## Phase 4: Layered redesign plan

Classify work into layers. Each iteration names one primary layer.

```text
Layer 0: Foundation  — hierarchy, grouping, alignment, spacing rhythm, balance, flow
Layer 1: Strategy    — why the surface exists, what is remembered first
Layer 2: UI          — structure, typography, color, spacing, hierarchy, alignment rails
Layer 3: UX          — navigation, CTA clarity, states, accessibility
Layer 4: Voice       — copy specificity, labels, status language
Layer 5: Interaction — hover, focus, scroll, theme, reduced motion
Layer 6: Delight     — illustration, texture, visual metaphor
Layer 7: Verification— browser checks, DOM probes, foundation + genre conformance, diff
```

### Dependency rule

```text
Foundation failure→ blocks genre/component polish; fix relationships first
Strategy failure  → blocks UI polish
UI failure        → blocks Delight
Alignment failure → reopens Foundation/UI structure; do not patch with local offsets
Grouping failure  → fix proximity/hierarchy before adding containers
Balance failure   → fix weight distribution before adding decoration
Flow failure      → fix sequence before CTA or motion polish
UX failure        → blocks final Verification
Genre failure     → reopens UI direction; do not treat as local polish
Voice failure     → blocks motion/illustration polish
```

### Iteration declaration

```yaml
iteration:
  number: <N>
  primary_layer: <name>
  secondary_layer: <name | none>
  not_touching: []
  success_criteria: []
  foundation_axes_under_test: []
  genre_constraints_under_test: []
  alignment_rails_under_test: []
  grouping_relationships_under_test: []
  forbidden_local_offsets: []
```

### Delight classification

```text
□ code/vector                     → coding agent may produce
□ raster AI image                 → requires available image generator
□ user-supplied                   → optimize and integrate
□ video/ambient motion            → requires tooling or fallback
```

Do not imply access to unavailable generators.

Delight gates:

```text
□ clarifies character, meaning, memory, or orientation
□ not hiding weak hierarchy, grouping, copy, or missing content
□ has a named role
□ removable without breaking comprehension
□ respects the foundation and selected genre contracts
□ respects the declared page rails unless it is the documented focal exception
□ lightweight and accessible
```

Common failures:

```text
❌ accessory drift
❌ cardification of an illustration
❌ figure/ground mismatch
❌ generic genre motif
❌ using lines, surfaces, or texture to fill intentional emptiness
❌ using illustration offsets as permission for unrelated content drift
❌ using decoration to compensate for hierarchy, grouping, balance, or flow failure
```