# Figure–Ground and Semantic Layering

> Universal relationship guidance for foreground, background, containment, depth, overlap, and occlusion. This applies across interactive products, static visuals, and presentations without prescribing a visual style.

Figure–ground is not “add more shadows.” Layering passes when the viewer can understand what is content, what contains it, what floats above it, what is temporarily blocking it, and why.

---

## Ownership

This reference strengthens existing foundation axes rather than creating a new axis:

```text
F2 GROUPING
  owns containment, common-region, and foreground/background relationships

F5 BALANCE
  owns depth weight, overlap dominance, and visual-mass distribution

F6 FLOW
  owns context preservation when a layer appears, moves, or disappears

F7 LEGIBILITY
  owns text/symbol survival against imagery, effects, and surfaces

F9 ACCESSIBILITY + AFFORDANCE
  owns operability and state clarity for interactive layers

F10 RESPONSIVE CONTINUITY
  owns layer meaning and occlusion safety across viewport/format changes
```

Canonical review findings remain reported through registered gates such as `G4`, `C2`, `R8`, and applicable surface gates. F2/F5 are assessment axes, not new report IDs.

---

## Layer Model

Use semantic roles before implementation-specific z-index values:

```text
L0 CANVAS
   page, artboard, slide, scene, or application background

L1 CONTENT
   primary information, imagery, controls, and reading/task regions

L2 CONTAINMENT
   surfaces, panels, cards, sections, groups, data regions, and media frames

L3 FLOATING
   menus, tooltips, sticky controls, popovers, transient inspectors

L4 MODAL
   dialogs, drawers, lightboxes, blocking confirmations, focused overlays

L5 SYSTEM / CRITICAL
   platform alerts, emergency states, permission blockers, or global system feedback
```

A product does not need every layer. Static artifacts may use only canvas, content, and containment. The model exists to clarify relationships, not to encourage depth effects.

---

## Universal Rules

### 1. Figure and ground must be distinguishable

```text
□ the intended foreground is perceptually separable from its background
□ contrast, placement, edge, texture, motion, or containment provides enough distinction
□ weak separation is not hidden behind decorative borders or excessive shadow
□ background atmosphere does not become a competing focal layer
□ text-on-image remains stable across the full required text area and crop
```

A flat visual can pass. A highly layered visual can pass. The question is whether the relationship is understandable.

### 2. Depth must communicate meaning

```text
□ elevation expresses containment, priority, transience, focus, or system state
□ equal semantic roles do not receive arbitrary unequal depth
□ higher visual depth does not accidentally imply higher product importance
□ shadows, blur, glass, gradients, and outlines have a structural or expressive job
□ decorative depth does not replace hierarchy, grouping, or spacing
```

### 3. Overlap and occlusion need an owner

For every meaningful overlap, identify:

```text
occluding layer
occluded content
reason for overlap
allowed duration/state
recovery or dismissal path when interactive
required safe region
responsive behavior
```

Fail when:

```text
- sticky or fixed UI covers required content or the primary action
- a floating layer detaches from the control or object it belongs to
- overlap hides status, price, label, navigation, or required evidence
- decorative objects cross text unpredictably
- one valid layer token combines with another and produces unintended occlusion
```

### 4. Containment should clarify, not fragment

```text
□ surfaces group genuinely related information or behavior
□ nested surfaces have distinguishable ownership and do not create card-within-card noise
□ containment does not compensate for unresolved proximity or role hierarchy
□ one continuous task is not split into unrelated-looking islands
□ dense products may use strong containment when comparison and scanning require it
```

### 5. Interactive layers preserve context

Where applicable:

```text
user action
→ visible layer/state change
→ current object or task remains understandable
→ focus and input ownership are clear
→ next valid action is discoverable
→ dismissal or recovery returns to a meaningful place
```

Detailed focus traps, input parity, and modal mechanics remain owned by interactive surface gates.

### 6. Layering survives responsive and theme changes

```text
□ stacking does not reverse semantic depth or detach floating controls
□ sticky regions leave enough visible and reachable content at small viewports
□ overlays fit constrained height, orientation, text scaling, and localization
□ light/dark or alternate themes preserve layer boundaries and contrast
□ crop, safe area, and platform overlays do not consume critical content
```

---

## Evidence Policy

```text
rendered still image
  → verify figure/ground, containment, overlap, visual weight, text survival

rendered interactive flow
  → additionally verify sticky/fixed behavior, focus, dismissal, scrolling, state continuity

source or token evidence
  → inspect semantic layer tokens, portal/overlay structure, z-index ownership, theme mapping

screenshot only
  → interaction, scroll, focus, and recovery remain NOT_VERIFIED

missing alternate viewport/theme/state
  → continuity for that condition remains NOT_VERIFIED
```

Implementation values are evidence, not the verdict. A tidy z-index scale can still produce a visually broken overlap; a local static artifact may have no z-index system at all.

---

## Review Matrix

| Relationship | Foundation axes | Canonical review owners | Typical evidence |
|---|---|---|---|
| foreground vs background | F2, F7 | G4, G10 | actual-size render, contrast/context inspection |
| containment and common region | F2 | G4, G7, G5 | grouping comparison, rendered regions |
| depth and visual dominance | F5 | C1, C2, R6, R8 | full-frame composition, squint/blur test |
| sticky/fixed occlusion | F5, F6, F9, F10 | G4 + interactive surface gates | scroll recording, viewport matrix, DOM/source evidence |
| modal/floating context | F2, F6, F9 | G4 + I1/I7 where applicable | interaction flow, focus/dismissal evidence |
| text or graphics over imagery | F2, F7 | G4, G10 + static/interactive profile gates | crop variants, actual-size render, theme variants |
| responsive layer continuity | F10 | G13, I4, I5 or static crop/safe-area gates | desktop/tablet/mobile or required format set |

---

## Cross-Genre Regression Fixtures

Use these as reasoning fixtures. They test relationship quality, not preferred aesthetics.

### Dense dashboard — PASS candidate

```text
- strong data regions and table containment
- sticky header remains compact and never covers row actions
- popovers remain anchored to their trigger
- selected state is distinguishable without excessive elevation
- dense visual language is accepted because scanning and comparison stay clear
```

### Dense dashboard — FAIL candidate

```text
- every nested region has its own shadow and border
- sticky toolbar plus table header consume most small-screen height
- menu opens beneath another panel
- status color blends into the containing surface
```

### Zen/minimal landing page — PASS candidate

```text
- near-flat canvas with little or no shadow
- grouping comes from spacing, alignment, and type hierarchy
- one dark install surface has a clear functional purpose
- no decorative layer is required to fill whitespace
```

### Zen/minimal landing page — FAIL candidate

```text
- low-contrast sections merge into the canvas
- sticky navigation hides anchors after in-page navigation
- pale text over atmospheric imagery survives only in one crop
- a dark surface becomes more dominant than the page’s actual narrative anchor
```

### Playful or expressive poster — PASS candidate

```text
- overlapping forms create energy while preserving the primary message
- product/person remains separated from the background
- mandatory price/contact/legal details stay unobstructed
- irregular depth supports the concept rather than simulating generic 3D decoration
```

### Playful or expressive poster — FAIL candidate

```text
- decorative shapes cross required text unpredictably
- glow and texture erase silhouette or edge clarity
- overlapping objects create an accidental second focal point
- safe-area crop removes the figure/ground cue
```

### Mobile application — PASS candidate

```text
- bottom sheet clearly belongs to the current task
- background state remains understandable but appropriately de-emphasized
- primary action remains reachable above system and keyboard areas
- dismissal restores focus/context
```

### Mobile application — FAIL candidate

```text
- sheet, keyboard, and sticky action overlap
- scrim does not distinguish blocking from non-blocking state
- floating action button covers list content
- orientation change detaches popover or resets task context
```

### Presentation — PASS candidate

```text
- depth or overlap reinforces one dominant idea
- annotations clearly belong to the chart or image they explain
- foreground claim remains readable at delivery distance
```

### Presentation — FAIL candidate

```text
- floating labels appear detached from their data
- background imagery competes with the slide claim
- decorative layers create document-like density with no narrative role
```

---

## Defect Classification

```text
relationship fails across multiple genres/surfaces
  → design-foundation knowledge defect

one component family layers incorrectly everywhere
  → component-system defect

correct layer rule exists but one implementation ignores it
  → local implementation defect

only one declared genre needs stricter depth restraint or expression
  → design-genre defect

focus trap, input parity, runtime, crop, fidelity, or export-specific failure
  → applicable interactive/static/domain reviewer
```

Do not fix unclear figure–ground by automatically adding borders, shadows, glass, gradients, or cards. Correct the relationship at the smallest valid layer.