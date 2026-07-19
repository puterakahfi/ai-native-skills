# 13 Core Graphic Design Principles

> Cross-cutting composition lenses for evaluating and producing coherent visual design across UI, websites, mobile and desktop applications, posters, presentations, brand assets, editorial layouts, marketing graphics, and other visual surfaces.

These principles are adapted from the Figma Resource Library's guide to core graphic design principles. They are expressed here as tool-agnostic foundation knowledge for AI-assisted design work.

They do **not** replace the universal foundation gates `F1–F10`. Several principles overlap because real visual quality emerges from relationships between them. Use the principles to reason about a composition; use the gates to decide whether the foundation passes.

---

## Principle-to-Foundation Mapping

| Graphic design principle | Primary foundation axes | Supporting axes |
|---|---|---|
| Alignment | F3 Alignment | F2 Grouping, F6 Flow, F8 System Consistency |
| Contrast | F1 Hierarchy, F7 Legibility | F5 Balance, F9 Accessibility |
| Balance | F5 Balance | F1 Hierarchy, F4 Space + Rhythm, F6 Flow |
| Hierarchy | F1 Hierarchy | F2 Grouping, F4 Space + Rhythm, F6 Flow |
| Color | F7 Legibility, F8 System Consistency | F1 Hierarchy, F5 Balance, F9 Accessibility |
| White Space | F4 Space + Rhythm | F2 Grouping, F5 Balance, F6 Flow |
| Proportion | F1 Hierarchy, F5 Balance | F3 Alignment, F7 Legibility |
| Repetition | F8 System Consistency | F2 Grouping, F4 Space + Rhythm, F6 Flow |
| Rhythm | F4 Space + Rhythm, F6 Flow | F2 Grouping, F8 System Consistency |
| Movement | F6 Flow | F1 Hierarchy, F4 Space + Rhythm, F9 Accessibility |
| Emphasis | F1 Hierarchy | F5 Balance, F6 Flow, F7 Legibility |
| Proximity | F2 Grouping | F3 Alignment, F4 Space + Rhythm |
| Unity | F8 System Consistency | F1–F7 and F10 as a whole-composition result |

---

## 1. Alignment

### Definition

Alignment is the deliberate positioning of elements against shared edges, centers, baselines, axes, or optical anchors.

### Purpose

Alignment creates order, visual connection, predictability, and professional sharpness. It helps separated elements feel related and gives the eye a stable path through the composition.

### Application

```text
- establish a grid, shell, or anchor system before applying local offsets
- align repeated roles to stable start, center, baseline, or end anchors
- use optical correction for icons, mixed type sizes, irregular shapes, and visual mass
- prefer reusable alignment rules over one-off nudges
- break alignment only when the exception has a visible compositional purpose
```

### Review questions

```text
- Which anchors organize the composition?
- Do repeated roles share those anchors?
- Is an apparent misalignment geometric, optical, or accidental?
- Does the alignment still hold after wrapping, resizing, or optional-content changes?
```

### Failure signals

```text
- almost-aligned edges
- drifting baselines
- arbitrary per-element margins or transforms
- centered elements that feel optically off-center
- a grid that exists technically but does not organize visual relationships
```

---

## 2. Contrast

### Definition

Contrast is a meaningful difference between elements in color, luminance, size, weight, shape, texture, density, direction, depth, or spatial treatment.

### Purpose

Contrast creates distinction, attracts attention, supports hierarchy, improves readability, and prevents visual monotony.

### Application

```text
- reserve stronger contrast for information or actions that genuinely need priority
- combine contrast channels when one channel is too subtle or inaccessible
- use sufficient foreground/background contrast for essential text and graphics
- create distinction without making every region compete for attention
- verify contrast in the real theme, background, viewport, medium, and output condition
```

### Review questions

```text
- What deserves the strongest contrast, and why?
- Can primary, supporting, and tertiary roles be distinguished at a glance?
- Is color doing work that should also be communicated by shape, label, position, or state?
- Does contrast remain effective in dark mode, print, projection, low brightness, or over imagery?
```

### Failure signals

```text
- everything is equally loud
- essential text blends into its background
- decorative accents overpower content
- secondary information becomes visual dust
- contrast is high but hierarchy remains unclear
```

---

## 3. Balance

### Definition

Balance is the intentional distribution of visual weight across a composition.

Visual weight may come from:

```text
scale + contrast + density + position + direction + color + imagery + texture + depth + overlap + empty space
```

### Types

```text
SYMMETRICAL
  Comparable weight is distributed around an axis.
  Often communicates stability, formality, clarity, or calm.

ASYMMETRICAL
  Different forms of weight counterbalance one another.
  Often communicates energy, modernity, movement, or editorial tension.
```

Neither type is inherently better.

### Application

```text
- evaluate total visual mass rather than counting objects
- use empty space as an active counterweight
- balance large quiet forms against smaller high-contrast forms
- account for imagery direction, crop, depth, and overlap
- verify sparse, normal, and dense content states independently
```

### Review questions

```text
- Where is the heaviest region?
- What counterbalances it?
- Is the dominant region intentionally dominant?
- Does content variation create a new accidental focal point?
```

### Failure signals

```text
- one side feels abandoned or overloaded
- a large empty region has no anchor or compositional role
- an accent, image, or floating layer dominates accidentally
- asymmetry exists without a visible counterweight
```

---

## 4. Hierarchy

### Definition

Hierarchy is the arrangement and emphasis of elements according to semantic importance and intended reading or task order.

### Purpose

Hierarchy helps viewers understand what matters first, what supports it, what belongs together, and what can be read later.

### Application

```text
- define the role chain before styling: page → section → group → item → detail/action
- distinguish primary, supporting, and tertiary roles using multiple cues
- use scale, weight, contrast, placement, spacing, measure, imagery, depth, and sequence deliberately
- keep siblings related while subordinate to their parent
- preserve role distinctions under real content length and responsive change
```

### Review questions

```text
- What is seen first, second, and third?
- Can the structure be understood without reading every word?
- Do parent and child roles compete at equal visual weight?
- Does the hierarchy match the intended message or task?
```

### Failure signals

```text
- one large heading is treated as proof of hierarchy
- headings, body text, metadata, and actions collapse into one level
- multiple focal points compete in the same viewport
- a local component overpowers the page-level narrative
```

---

## 5. Color

### Definition

Color is the deliberate use of hue, value, saturation, temperature, and relationships between colors to communicate identity, emotion, meaning, state, depth, and emphasis.

### Purpose

Color can strengthen brand recognition, organize information, influence perception, communicate status, and direct attention.

### Application

```text
- define semantic color roles instead of assigning colors arbitrarily
- use a controlled palette with clear primary, supporting, neutral, feedback, and data roles where applicable
- reserve vivid or high-contrast color for meaningful emphasis
- test harmony and differentiation across light, dark, print, projection, and image-backed contexts
- never use color as the only carrier of essential meaning
```

### Review questions

```text
- What does each color role communicate?
- Does the palette support the intended emotional and brand direction?
- Are state colors distinguishable and accessible?
- Is accent color scarce enough to retain meaning?
```

### Failure signals

```text
- colors are attractive individually but incoherent as a system
- too many accents compete for attention
- brand color is forced into every surface or component
- state meaning disappears for users with color-vision differences
- contrast changes unpredictably across themes or backgrounds
```

---

## 6. White Space

### Definition

White space, or negative space, is the intentionally unoccupied area around, between, and within elements. It does not need to be literally white.

### Purpose

White space creates breathing room, clarifies grouping, improves readability, establishes pacing, supports emphasis, and prevents clutter.

### Application

```text
- assign each significant interval a structural purpose
- keep within-group spacing tighter than between-group spacing when relationships require it
- use margins and padding consistently without forcing one gap everywhere
- allow density to match the medium, content, task, and genre
- adjust composition for empty, sparse, normal, and dense states
```

### Review questions

```text
- What relationship does this empty interval communicate?
- Does it group, separate, pause, emphasize, sequence, or resolve?
- Is the space anchored to nearby content?
- Does whitespace improve comprehension or merely enlarge the canvas?
```

### Failure signals

```text
- unexplained dead zones
- equal spacing between every element and hierarchy level
- large padding used to imitate premium quality without structural purpose
- dense content with no meaningful pauses
- missing optional content leaves holes that look accidental
```

---

## 7. Proportion

### Definition

Proportion is the size and visual-weight relationship between elements and between each element and the composition as a whole.

### Purpose

Proportion supports hierarchy, balance, legibility, harmony, and appropriate emphasis.

### Application

```text
- compare scale relationally rather than evaluating elements in isolation
- size icons, controls, images, typography, and supporting details according to role and medium
- use grids, modular scales, or component rules as baselines, not automatic proof of quality
- exaggerate proportion only when the communication purpose justifies it
- test actual output size rather than relying only on zoomed-in design views
```

### Review questions

```text
- Does each element feel appropriately sized for its role?
- Does one object overpower or under-support another?
- Are controls and text proportionate to the viewing distance and input method?
- Does the proportion survive responsive scaling and content variation?
```

### Failure signals

```text
- oversized decoration and undersized essential information
- icons that overpower labels or disappear beside them
- logos, imagery, and typography that compete instead of complementing one another
- proportional relationships that work only at one viewport or zoom level
```

---

## 8. Repetition

### Definition

Repetition is the deliberate reuse of visual elements or rules such as type roles, colors, shapes, spacing patterns, surfaces, components, imagery treatments, or motion behavior.

### Purpose

Repetition builds recognition, cohesion, predictability, rhythm, and brand or system identity.

### Application

```text
- repeat semantic roles consistently
- reuse tokens, components, styles, patterns, and content-adaptation policies where available
- repeat enough to establish a pattern before breaking it for emphasis
- vary repeated structures when content or task differences require it
- keep repetition coherent across pages, states, themes, and responsive variants
```

### Review questions

```text
- What visual or behavioral pattern is being established?
- Are repeated items truly equivalent in role?
- Is an exception meaningful or merely inconsistent?
- Does repetition support recognition or create monotony?
```

### Failure signals

```text
- the same role receives different treatments without reason
- visually identical elements behave differently
- every section invents a new style
- repetition is so rigid that it ignores content and task needs
- an isolated variation attracts attention accidentally
```

---

## 9. Rhythm

### Definition

Rhythm is the cadence created by the placement, spacing, recurrence, and variation of visual elements.

Repetition establishes recurrence; rhythm determines how that recurrence moves through time or space.

### Common rhythm modes

```text
REGULAR
  Repeated elements and intervals follow a stable cadence.

RANDOM
  Variation appears irregular but remains compositionally controlled.

FLOWING
  Curves, organic forms, direction, or gradual transitions create fluid movement.

PROGRESSIVE
  Repeated elements change gradually in scale, color, position, density, or form.
```

### Application

```text
- choose a cadence that matches the message, genre, and task
- use spacing and repetition to create predictable scanning where needed
- introduce variation to mark transitions, priority, or progression
- preserve enough consistency that the viewer can perceive the pattern
- test rhythm across the whole artifact, not only inside one component
```

### Review questions

```text
- Where does the composition accelerate, pause, or resolve?
- Is the recurrence regular, flowing, progressive, or intentionally irregular?
- Does the rhythm guide attention or create fatigue?
- Do section and component rhythms support the same overall experience?
```

### Failure signals

```text
- mechanical repetition with no pacing
- arbitrary spacing changes that feel like errors
- every region has the same density and cadence
- local card rhythm conflicts with page-level flow
- progressive patterns change without a readable direction
```

---

## 10. Movement

### Definition

Movement is the visual path the viewer's eye follows through a composition. In interactive work, it also includes actual animation and state transition where applicable.

### Purpose

Movement guides reading, reveals sequence, connects regions, supports narrative, and helps users discover the next meaningful action.

### Application

```text
- place focal elements along an intentional reading or task path
- use direction, gaze, lines, curves, cropping, gradients, scale, and spatial sequence carefully
- use common scan patterns only when they fit the content and reading context
- make actual motion reinforce state change, causality, hierarchy, or continuity
- preserve semantic and interaction order when the visual layout changes responsively
```

### Review questions

```text
- Where does the eye enter the composition?
- What is the next intended destination?
- Which visual cues create that path?
- Does actual motion explain change or merely decorate it?
```

### Failure signals

```text
- the eye is trapped in a decorative region
- arrows or lines compensate for an unclear layout
- multiple directions compete without hierarchy
- animation hijacks attention from the task
- visual order conflicts with semantic, DOM, or interaction order
```

---

## 11. Emphasis

### Definition

Emphasis is the deliberate creation of a focal point or priority region.

### Purpose

Emphasis ensures that the most important message, object, state, or action is recognized quickly.

### Application

```text
- choose the focal point before adding contrast effects
- create emphasis through contrast, color, scale, weight, proportion, placement, isolation, whitespace, imagery, or motion
- support one dominant focal point with subordinate accents
- ensure the emphasized element deserves its visual priority
- reduce competing emphasis elsewhere
```

### Review questions

```text
- What is the primary focal point?
- Which design decisions make it dominant?
- Is the emphasis proportional to its semantic importance?
- What has been intentionally de-emphasized?
```

### Failure signals

```text
- everything is bold, bright, large, elevated, or animated
- the most decorative element becomes the focal point
- a secondary CTA competes with the primary action
- emphasis depends on a single inaccessible cue
- a focal point is visually strong but contextually premature
```

---

## 12. Proximity

### Definition

Proximity is the spatial relationship between elements used to communicate whether they belong together.

### Purpose

Proximity enables immediate grouping, reduces cognitive effort, clarifies ownership, and separates unrelated information.

### Application

```text
- place related titles, labels, values, controls, media, and actions close enough to read as one group
- separate unrelated groups with a visibly stronger interval
- combine proximity with alignment, similarity, and common region when relationships are complex
- let optional content appear or disappear without detaching the remaining group
- avoid using cards or borders to compensate for weak proximity
```

### Review questions

```text
- What belongs together before labels are read?
- Is within-group spacing tighter than between-group spacing?
- Does every action appear owned by the correct object or section?
- Does the grouping survive missing, wrapped, or additional content?
```

### Failure signals

```text
- labels appear closer to the wrong value or control
- section headings float between sections
- equal spacing flattens parent, child, and sibling relationships
- cards contain unrelated items while related items are split apart
- optional content removal breaks ownership
```

---

## 13. Unity

### Definition

Unity is the whole-composition result in which all elements feel intentionally related and work together to communicate one coherent message, identity, or task.

Unity is not sameness. A design may contain contrast, variation, asymmetry, tension, and multiple content types while still feeling unified.

### Purpose

Unity prevents a design from feeling like unrelated fragments, copied components, or decorative decisions accumulated without a governing idea.

### Application

```text
- establish a clear concept, hierarchy, grid, palette, type system, spacing logic, and imagery treatment
- reuse visual and behavioral rules coherently
- ensure variation supports the same composition rather than introducing a second visual language
- connect local component decisions to the page, product, brand, and task context
- review the artifact at full-composition scale after reviewing individual details
```

### Review questions

```text
- Does the artifact feel like one designed system or many assembled fragments?
- Which repeated relationships hold the composition together?
- Do exceptions strengthen the concept or weaken it?
- Does the whole remain coherent across viewport, state, content, and theme changes?
```

### Failure signals

```text
- every section looks independently polished but unrelated
- multiple type, color, surface, icon, or illustration languages compete
- components appear copied from different products
- decorative motifs do not support the message or task
- responsive variants preserve elements but lose the original composition logic
```

---

## Combined Use

Do not evaluate these principles as isolated checkboxes.

```text
proximity without spacing hierarchy     → groups may still flatten
contrast without emphasis discipline    → everything competes
repetition without rhythm               → mechanical monotony
rhythm without hierarchy                → movement without meaning
color without accessibility             → meaning may disappear
alignment without optical correction    → technically aligned, visually wrong
balance without hierarchy               → stable but directionless
unity without variation                 → coherent but lifeless
variation without unity                 → expressive but fragmented
```

A strong composition typically resolves the following chain:

```text
meaning
  → hierarchy
  → grouping and proximity
  → alignment and proportion
  → contrast and emphasis
  → space, repetition, and rhythm
  → balance and movement
  → color, legibility, and accessibility
  → consistency and unity
  → responsive continuity
```

The chain is diagnostic, not strictly sequential. Iterate whenever a later decision weakens an earlier relationship.

---

## Foundation Review Prompt

Use this compact prompt when producing or reviewing a design:

```text
Evaluate the composition through all 13 graphic design principles:
alignment, contrast, balance, hierarchy, color, white space, proportion,
repetition, rhythm, movement, emphasis, proximity, and unity.

For each relevant principle:
1. identify the intended relationship or purpose,
2. cite visible or runtime evidence,
3. describe any conflict with another principle,
4. map the finding to foundation gates F1–F10,
5. recommend the smallest correct fix layer.

Do not reward visual style alone. Verify that the composition communicates,
remains legible, preserves relationships, and survives supported variation.
```

---

## Source

Adapted and operationalized from Figma Resource Library, **“13 core graphic design principles + how to apply them.”**
