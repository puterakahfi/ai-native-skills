# Phase 3–4 — Genre, Macrostructure, Visual Language, and Layered Plan

## Phase 3A: Genre resolution

Load `design-genre/SKILL.md` first. Genre selection is incomplete until the selected genre reference is loaded and its constraints are stored in run state.

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
  color_rules: []
  motion_rules: []
  hard_failures: []
```

Hard rule:

```text
selected genre reference
  > generic redesign production defaults
  > macrostructure template defaults
  > component template defaults
```

If a generic rule conflicts with the selected genre reference, follow the genre reference and record the override.

## Phase 3B: Macrostructure pick

### Extract brief signals

```text
□ Primary goal:    convert | showcase | inform | entertain | brand
□ Identity weight: high = person leads | low = work leads
□ Content volume:  N products / N sections
□ Audience:        hiring manager | client | developer | general
□ CTA present:     yes | no
□ Visual assets:   yes | no
□ Genre contract:  resolved | unresolved
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

Candidate does not equal approval. Validate it against the loaded genre reference.

```text
Example:
  Bento may fit volume=4+, but must be rejected for zen prose when it would
  create equal cards, dense containment, or multiple focal objects.
```

### Diversification check

```text
Previous macrostructure: [name | none]
Candidate: [name]
Must differ on at least two axes when variety is needed.
Axes: layout lead / heading / divider / button / image / reveal

Brief match and genre conformance always outrank forced variety.
```

### State pick with justification

```yaml
design_direction:
  genre: <name>
  genre_reference: <path>
  macrostructure: <name>
  visual_language: <short definition>
  justified_by:
    - signal: <signal>
      reason: <reason>
  rejected_options:
    - option: <name>
      reason: <genre or brief conflict>
  inherited_hard_constraints:
    - <constraint copied from genre contract>
```

## Phase 3C: Visual language definition

Translate the genre into concrete rules before touching UI. A theme word or palette swap is insufficient.

### Zen / Minimalist

Load `design-genre/references/zen.md`. Do not summarize away its hard constraints.

```text
Core:
  Ma / emptiness   → negative space performs grouping and separation
  Restraint        → remove before styling
  Stillness        → no hover lift, glow, or decorative urgency
  One focal object → one dominant anchor per viewport
  Low interruption→ few containers, badges, surfaces, and lines

Containment:
  whitespace > alignment > proximity > text measure > rare surface
  structural section borders = 0
  repeated row separators = 0 by default
  dense-list exception = one leading or trailing hairline, not per row
  visible structural lines = target 0, maximum 1 per typical viewport

Layout:
  asymmetrical whitespace, narrow measures, intentional intervals
  no equal-weight card catalog
  no card-to-hairline substitution

Typography:
  fewer sizes, lighter weights, generous leading, one display moment

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
❌ motion or decoration is used before spacing and silence are solved
```

Zen check before production:

```text
1. What will be removed?
2. Which relationships are communicated by space alone?
3. What is the focal object in each viewport?
4. What is the structural line budget?
5. Which generic component defaults are explicitly overridden?
```

### Other genres

Load the corresponding `design-genre/references/<genre>.md` and copy its concrete constraints into `genre_contract`. Do not improvise from the genre name alone.

## Phase 4: Layered redesign plan

Classify work into layers. Each iteration names one primary layer.

```text
Layer 0: Strategy    — why the surface exists, what is remembered first
Layer 1: UI          — structure, typography, color, spacing, hierarchy
Layer 2: UX          — navigation, CTA clarity, states, accessibility
Layer 3: Voice       — copy specificity, labels, status language
Layer 4: Interaction — hover, focus, scroll, theme, reduced motion
Layer 5: Delight     — illustration, texture, visual metaphor
Layer 6: Verification— browser checks, DOM probes, genre conformance, diff
```

### Dependency rule

```text
Strategy failure → blocks UI polish
UI failure       → blocks Delight
UX failure       → blocks final Verification
Genre failure    → reopens UI direction; do not treat as local polish
Voice failure    → blocks motion/illustration polish
```

### Iteration declaration

```yaml
iteration:
  number: <N>
  primary_layer: <name>
  secondary_layer: <name | none>
  not_touching: []
  success_criteria: []
  genre_constraints_under_test: []
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
□ not hiding weak copy or missing content
□ has a named role
□ removable without breaking comprehension
□ respects the selected genre contract
□ lightweight and accessible
```

Common failures:

```text
❌ accessory drift
❌ cardification of an illustration
❌ figure/ground mismatch
❌ generic genre motif
❌ using lines, surfaces, or texture to fill intentional emptiness
```