# Phase 7 — PRODUCTION

Apply design in this order. Load each delegated skill before using its templates.

```text
0. Preservation check    → existing brand, DESIGN.md, tokens, and framework conventions
1. Genre contract        → selected design-genre reference and hard constraints
2. Visual language       → phase-genre-macro.md
3. Macrostructure        → macrostructures skill, filtered by genre constraints
4. Design system tokens  → design-system skill
5. Theme architecture    → dark-light-theming skill
6. Motion                → motion-design only when the genre allows it
7. Content               → content-strategy
8. Components            → ui-components + trusted behavior patterns
9. Component pass        → navbar → hero → sections → lists/cards → contact → footer
10. Genre conformance    → source-level and rendered checks before verification handoff
```

## Precedence

```text
brand and DESIGN.md locks
  > explicit user direction
  > loaded genre reference
  > redesign specification
  > generic production defaults
  > macrostructure and component template defaults
```

A generic recommendation such as cards, hairlines, section backgrounds, or hover motion must be rejected when the loaded genre contract forbids it.

## Preservation-first production

```text
Existing brand tokens      → preserve or map semantically
Existing type scale        → audit and refine; do not replace mechanically
Existing theme infra       → extend; never create a parallel system
Existing sound primitives  → reuse behavior, adapt visual expression to genre
No usable system           → use fallback values and record why
```

Fallbacks are not mandates.

## Implementation stamp

Record production context once per artifact or durable run state.

```yaml
production_context:
  macrostructure: <name>
  genre: <name>
  genre_reference: <path>
  theme: <light-only | dark-only | dual-theme>
  iteration: <N>
  pre_emit: <P H E S R V>
```

Do not add repetitive comments to every component file.

## Design-system policy

### Typography

Preserve a coherent existing scale. When none exists, establish a restrained hierarchy and verify narrow widths.

```text
□ H1 remains dominant without overflow
□ H2 is subordinate
□ body measure and leading remain readable
□ responsive sizes are verified between breakpoints
□ selected genre weight and density rules are respected
```

### Color semantics

Map existing semantic roles before creating new ones.

```text
background / foreground / surface / border / primary / muted / status / interactive
```

Do not create a parallel token vocabulary merely to satisfy a template.

### Figure and ground

Long pages need readable grouping, but grouping does not always require visible boundaries.

Use the lightest genre-permitted method:

```text
1. proximity and whitespace
2. alignment and text measure
3. asymmetrical placement
4. subtle tonal or texture shift when allowed
5. line or surface only when the selected genre and function allow it
```

A requirement for figure/ground separation never overrides a genre rule that forbids section borders or background swaps.

### Whitespace rhythm

```text
Hero:    deliberate opening interval with an anchor
Content: consistent large rhythm adapted to content and viewport
Contact: enough room to resolve the page without becoming a boxed campaign CTA
Footer: quiet closing interval
```

Do not fill intentional space because it appears unfinished.

## Collection layout

Choose from evidence weight and user task, not item count alone.

```text
primary evidence   → weighted sequence, case-study excerpt, or asymmetric feature
secondary evidence → open list, editorial rows, compact index, or disclosure
comparison task    → cards/table only when comparison genuinely benefits
interactive group  → surface only when state and containment require it
```

Live, planned, and experimental work must not receive equal visual weight by default.

## Space-first genre policy

For `zen-minimalist`, `editorial-minimal`, or any explicitly space-led direction, load and enforce the genre line/surface budget.

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

This is a reusable defect pattern:

```text
iteration N: every item is a card
iteration N+1: cards removed, every item receives border-top/border-bottom
result: containment density remains; only the drawing primitive changed
verdict: genre failure, not successful refinement
```

Preferred replacements:

```text
project separation    → larger vertical gaps + alternating alignment or measure
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

## Source-level genre conformance check

Before handing off to rendered verification, inspect changed files for implementation symptoms.

For zen or space-led surfaces, search relevant files for:

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
  genre_allowed: <yes | no>
  action: <keep | remove | replace with space>
```

A source scan is not visual verification, but obvious genre violations must be fixed before rendering.

## First impression

```text
H1 = stance, not job-title boilerplate
Supporting line = what is actually built or changed
Primary action = meaningful next step
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
P Philosophy   — every element has a reason
H Hierarchy    — focal order is immediate
E Execution    — spacing and alignment are coherent
S Specificity  — content is concrete
R Restraint    — unnecessary interruption removed
V Variety      — not another generic template
G Genre        — loaded hard constraints are visibly respected
```

For zen, `G` fails when line density, surface density, or motion exceeds the genre budget even if individual elements look tasteful.

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
□ toggle label describes next action
□ toggle remains reversible
□ genre line/surface budget passes in both themes
```
