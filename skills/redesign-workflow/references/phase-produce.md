# Phase 7 — PRODUCTION

Apply design in this order. Load each delegated skill before using its templates.

```text
0. Preservation check      → existing brand, DESIGN.md, tokens, framework conventions
1. Foundation contract     → hierarchy, grouping, alignment, space, balance, flow,
                             legibility, consistency, accessibility, responsiveness
2. Genre contract          → selected design-genre reference and stricter expression rules
3. Visual language         → phase-genre-macro.md
4. Macrostructure          → macrostructures skill, filtered by foundation + genre
5. Design-system tokens    → design-system skill
6. Theme architecture      → dark-light-theming skill
7. Motion                  → motion-design only when foundation, task, and genre allow it
8. Content                 → content-strategy
9. Components              → ui-components + trusted behavior patterns
10. Component pass         → navbar → hero → sections → collections → closing → footer
11. Foundation conformance → source-level and rendered relationship checks
12. Genre conformance      → source-level and rendered expression checks
```

## Precedence

```text
design-foundation hard requirements
  > brand and DESIGN.md locks
  > explicit user direction
  > loaded genre reference
  > redesign specification
  > generic production defaults
  > macrostructure and component template defaults
```

Foundation owns universal relationship quality. Brand and genre own expression. A generic recommendation such as cards, hairlines, section backgrounds, hover motion, or equal sizing must be rejected when it breaks the foundation or loaded genre contract.

## Preservation-first production

```text
Existing brand tokens      → preserve or map semantically
Existing type scale        → audit relational hierarchy; do not replace mechanically
Existing theme infra       → extend; never create a parallel system
Existing sound primitives  → reuse behavior, adapt expression to foundation + genre
No usable system           → use fallback values and record why
```

Fallbacks are not mandates.

## Implementation stamp

Record production context once per artifact or durable run state.

```yaml
production_context:
  foundation_reference: <path>
  foundation_axes:
    hierarchy: <rule>
    grouping: <rule>
    alignment: <rule>
    spatial_rhythm: <rule>
    balance: <rule>
    flow: <rule>
    responsive_continuity: <rule>
  macrostructure: <name>
  genre: <name>
  genre_reference: <path>
  theme: <light-only | dark-only | dual-theme>
  iteration: <N>
  pre_emit: <F P H E S R V G>
```

Do not add repetitive comments to every component file.

## Foundation-first composition policy

### Hierarchy

```text
□ primary, supporting, and tertiary roles are recognizable at a glance
□ parent and child levels do not compete at equal visual weight
□ sibling items look related but remain subordinate to their parent
□ nested relationships use at least two cues when one is ambiguous
□ later sections preserve the intended global hierarchy
```

Hierarchy cues:

```text
scale / weight / measure / contrast / placement / spacing / repetition / sequence
```

Do not rely on one large H1 while child titles, metadata, and sibling spacing remain flat.

### Grouping

```text
□ related elements cluster more strongly than unrelated elements
□ within-group spacing is tighter than between-group spacing where applicable
□ parent → child-group separation is stronger than child → child separation
□ enclosure is added only when function or comparison benefits
□ maturity, priority, and state are not flattened by identical treatment
```

Practical diagnostic starting point:

```text
between-group interval ≈ 1.25×–2× within-group interval
```

Verify visually; do not force the ratio as a universal token.

### Alignment

```text
□ repeated roles reuse stable structural anchors
□ optical alignment is checked for mixed type sizes, icons, and irregular shapes
□ local transforms and arbitrary margins do not replace a shared grid
□ asymmetry has visible balancing logic
□ responsive collapse preserves predictable order
```

### Space and rhythm

```text
□ spacing changes according to relationship and importance
□ one repeated interval is not used for every level
□ large empty intervals have an anchor and structural purpose
□ whitespace groups, separates, pauses, emphasizes, or resolves intentionally
```

### Balance

Review together:

```text
scale + contrast + density + position + direction + color + imagery + empty space
```

Do not add decoration to compensate for weak weight distribution.

### Flow

```text
□ first focal point is clear
□ next intended region or action is discoverable
□ reading/task order matches semantic order
□ transitions preserve context
□ motion and metadata do not interrupt the intended path
```

### Responsive continuity

```text
□ hierarchy survives viewport or orientation change
□ grouped content stays grouped after stacking
□ rails collapse into predictable mobile order
□ overflow, localization, text scaling, and touch behavior remain safe
```

## Design-system policy

### Typography

Preserve a coherent existing scale. When none exists, establish a restrained role taxonomy and verify actual viewports.

```text
□ dominant, supporting, child, body, label, metadata, and action roles are distinct
□ child titles remain subordinate to their parent section or page statement
□ body measure and leading remain readable
□ responsive sizes preserve hierarchy between breakpoints
□ selected genre weight and density rules are respected
```

Numeric ratios are evidence, not universal laws.

### Color semantics

Map existing semantic roles before creating new ones.

```text
background / foreground / surface / border / primary / muted / status / interactive
```

Do not create a parallel token vocabulary merely to satisfy a template.

### Figure, ground, and grouping

Long pages need readable grouping, but grouping does not always require visible boundaries.

Use the lightest foundation- and genre-permitted method:

```text
1. proximity and relational spacing
2. hierarchy and text measure
3. shared alignment anchors
4. intentional asymmetrical placement
5. subtle tonal or texture shift when allowed
6. line or surface only when function and genre allow it
```

A grouping requirement never justifies breaking a genre line/surface budget.

### Whitespace rhythm

```text
Hero:       deliberate opening interval with an anchor
Section:    clear parent introduction and subordinate child group
Collection: sibling rhythm tighter than parent-to-collection rhythm
Closing:    enough room to resolve without becoming a boxed campaign CTA
Footer:     quiet closing interval
```

Do not fill intentional space because it appears unfinished. Do not preserve empty space that has no understandable relationship or anchor.

## Collection layout

Choose from evidence weight, hierarchy, and user task, not item count alone.

```text
primary evidence   → weighted sequence, case-study excerpt, or asymmetric feature
secondary evidence → open list, editorial rows, compact index, or disclosure
comparison task    → cards/table only when comparison genuinely benefits
interactive group  → surface only when state and containment require it
```

Live, planned, and experimental work must not receive equal visual weight by default.

For every collection declare:

```yaml
collection_hierarchy:
  parent_intro: <role>
  child_group: <role>
  sibling_items: <role>
  parent_to_group_interval: <token/value>
  sibling_interval: <token/value>
  child_title_role: <type role>
  supporting_role: <type role>
```

## Space-first genre policy

For `zen-minimalist`, `editorial-minimal`, or any explicitly space-led direction, load and enforce the genre line/surface budget after foundation grouping is solved.

### Zen containment order

```text
1. whitespace
2. proximity
3. alignment
4. text measure and indentation
5. numbering or quiet labels
6. rare genre-approved line or surface exception
```

**Do not place hairlines at position three as a generic minimal solution.** A hairline is still a visual interruption.

### Zen structural line budget

```text
section borders:          0
repeated row separators:  0 by default
dense-list exception:     one leading OR trailing hairline for one list system
visible structural lines: target 0; maximum 1 per typical viewport
```

Excluded from this budget only when functionally necessary:

```text
form controls, focus rings, required tables, diagrams, charts, and explicit data grids
```

### Card-to-line substitution failure

```text
iteration N:   every item is a card
iteration N+1: cards removed, every item receives border-top/border-bottom
result:        containment density remains; only the drawing primitive changed
verdict:       genre failure, not successful refinement
```

Preferred replacements:

```text
project separation    → hierarchy + parent/group/sibling spacing
principle separation  → numbered prose with rhythm only
capability separation → definition list or grouped sentence
contact links         → open stack with proximity and hover color
section separation    → padding rhythm only
```

## Portfolio and product-hub proof

Minimalism must not erase truth, but proof does not require chrome.

```text
Above fold:
  stance + domain + clear next action

Primary evidence:
  selected real work with status, role, scope, and link

Secondary evidence:
  writing, open source, standards, and experiments with honest maturity

Avoid:
  abstract philosophy without evidence
  equal cards that flatten maturity
  fake metrics, logos, testimonials, or outcomes
  metadata rendered as repeated badges merely to look structured
```

When screenshots are unavailable, specific text and links are valid proof.

## Internal route dependency integrity

An approved internal link and its destination route form one delivery dependency.

```text
approved internal link
  → destination route exists
  → route remains inside confirmed scope
  → navigation and return paths remain coherent
```

Hard rules:

```text
- explicit user approval of a route overrides baseline-only scope inference
- do not preserve an internal link while deleting or restoring away its destination
- do not delete an approved destination route unless the same patch intentionally removes or redirects every inbound link
- scope sanitation must classify the link and destination as one dependency bundle
- a route introduced on the working branch may still be in scope when the user explicitly protects it
- unresolved internal link/route mismatch is a blocking integrity failure
```

Before final-diff sanitation:

```text
□ enumerate changed internal links
□ resolve every destination file or route
□ record user-protected routes
□ classify each link + destination bundle together
□ verify navbar, footer, CTA, and back-navigation behavior after any route removal
```

Example failure:

```yaml
violation:
  source: homepage active-work link
  destination: /ai-designer
  observation: link remains approved while sanitation deletes the route
  class: internal_route_dependency_break
  verdict: fail
```

## Source-level conformance checks

Before handing off to rendered verification, inspect changed files for implementation symptoms.

### Foundation symptoms

```text
repeated equal spacing at every hierarchy level
child titles using the same role as parent headings
per-item translate/margin nudges
conflicting container widths
visual order that differs from semantic order
metadata below readable size
parallel token systems
```

### Zen or space-led symptoms

```text
border-t border-b border-y divide-y divide-x
rounded-* shadow-* ring-* bg-card bg-secondary
badge pill chip hover:-translate hover:scale
```

Classify each occurrence:

```yaml
- token: <class or style>
  region: <component>
  purpose: <functional reason | decorative grouping>
  foundation_allowed: <yes | no>
  genre_allowed: <yes | no>
  action: <keep | remove | replace relationally>
```

A source scan is not visual verification, but obvious foundation or genre violations must be fixed before rendering.

## First impression

```text
H1 = stance, not job-title boilerplate
Supporting line = what is actually built or changed
Primary action = meaningful next step
First viewport = one clear focal path, not several equal anchors
```

## Accessibility baseline

```html
<a href="#main">Skip to content</a>
<nav aria-label="Main navigation">
<main id="main">
<section aria-labelledby="section-title">
<footer>
```

```text
□ semantic heading order
□ descriptive links
□ external rel="noopener noreferrer"
□ keyboard-visible focus
□ touch targets at least 44×44px where interactive
□ reduced-motion behavior
```

Accessibility controls are not removed to satisfy visual minimalism.

## Pre-emit critique

Score 1–5. Any axis below 3 requires revision.

```text
F Foundation  — hierarchy, grouping, alignment, balance, and flow are coherent
P Philosophy  — every element has a reason
H Hierarchy   — focal and nested role order is immediate
E Execution   — spacing and alignment are coherent
S Specificity — content is concrete
R Restraint   — unnecessary interruption removed
V Variety     — not another generic template
G Genre       — loaded hard constraints are visibly respected
```

For zen, `G` fails when line density, surface density, or motion exceeds the genre budget even if individual elements look tasteful. `F` fails for every genre when parent/child/sibling relationships, grouping, balance, or flow remain ambiguous.

## Slop red list

Auto-revise when present without a functional, brief-specific reason.

```text
❌ generic H1 + three bullets + CTA template
❌ fake trust logos, ratings, metrics, or testimonials
❌ gradient mesh used instead of composition
❌ six or more equal cards without prioritization
❌ cards nested inside cards
❌ three consecutive card-led major sections
❌ every metadata value turned into a pill
❌ giant rounded CTA panel used only for impact
❌ parent, child group, and siblings using equal spacing and visual weight
❌ grouping repaired with boxes before proximity and hierarchy are fixed
❌ arbitrary offsets used to fake balance or asymmetry
❌ minimalist portfolio with no real work evidence
❌ zen page where card removal becomes repeated hairline rows
❌ structural section borders after a zen direction is locked
❌ approved internal link whose destination route was removed by sanitation
```

## Dual-theme surfaces

Preserve the existing theme mechanism. Verify both modes and reversibility.

```text
□ light inspected
□ dark inspected
□ hierarchy and grouping survive contrast changes
□ toggle label describes next action
□ toggle remains reversible
□ foundation gates pass in both themes
□ genre line/surface budget passes in both themes
```