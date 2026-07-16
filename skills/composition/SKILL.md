---
name: composition
version: 1.0.0
type: skill
description: >
  Above-the-fold composition — focal point, visual weight, eye-flow, anchoring.
  Prevents floating/unanchored layouts and dead-space voids.
tags: [design, composition, visual-weight, focal-point, alignment]
---

# Composition

## When to Load

Load when:
- Producing any hero or above-the-fold section
- Layout feels "floating" or content is not immediately visible
- There is unexplained void above or around main content
- Elements feel unbalanced or not grounded

---

## Core Principle: Every Layout Has One Focal Point

The eye needs an anchor — one point it lands on first, then travels from.
Without an anchor, the eye wanders and the layout feels unresolved ("ngambang").

```
WRONG: content pushed to bottom of 100vh → void above → eye enters void first
RIGHT: focal point sits at optical center (45% from top, not 50%) → eye lands immediately
```

---

## Optical Center vs Geometric Center

```
Geometric center: 50% from top (math correct, visually wrong)
Optical center:   45% from top (eye perceives this as "center")

Rule: Primary content should sit at or above optical center.
Never push primary content below 60% of viewport height.

For hero with name as focal point:
  justify-content: center           → name at 50% → slightly low, acceptable
  justify-content: flex-end         → name at bottom → VOID above → FAIL
  padding-top that pushes to ~40%   → optimal
```

---

## Visual Weight Distribution

Weight = how much visual mass an element carries.
Heavy elements: large type, high contrast, bright color.
Light elements: small type, muted color, more whitespace.

```
Rule: Heavy elements anchor the layout. They must be visible without scroll.

Above-the-fold weight budget:
  □ One heavy element (H1 / hero name) — 60–70% of visual weight
  □ One supporting element (stance/bio) — 20–30%
  □ One accent (meta/contact) — 5–10%
  □ Total = 100% — if nothing heavy, layout floats

Checklist:
  □ Is the heaviest element visible within first 100vh?
  □ Is it above the optical center (≤ 45% from top)?
  □ Does it have enough contrast to anchor immediately?
```

---

## Eye Flow Mapping

Eye enters top-left (F-pattern for text, Z-pattern for visual pages).
Design must guide the eye, not leave it to wander.

```
Personal portfolio (dark, editorial):
  Z-pattern:
    top-left (logo/name) → top-right (nav) → diagonal → bottom-left (stance) → bottom-right (meta)

Marquee Hero eye flow:
  Enter top-left (eyebrow) → drop to name (heavy anchor) → right to meta → down to scroll cue
  
VIOLATION: void above name breaks the entry → eye enters void, searches for anchor, fatigues
FIX: name must be reachable from top without crossing dead space
```

---

## Dead Space vs Intentional Breathing Room

```
Dead space (BAD):
  - Void above primary content with no visual purpose
  - No element occupies or intentionally frames the void
  - Eye has nothing to "read" while scanning to content
  - Caused by: justify-content:flex-end, min-height:100vh with little content

Breathing room (GOOD):
  - Whitespace between sections — intentional reset
  - Eye finishes one section, white space signals "next context"
  - Has rhythm: small-larger-small or consistent multiples
  - Caused by: padding between sections, not padding above hero

Rule: Hero must have ZERO dead space above focal point.
      Breathing room lives BETWEEN sections, not BEFORE the first section.
```

---

## Anchoring Patterns

### Pattern A: Top-anchored hero (recommended for personal portfolio)
```css
.hero {
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  justify-content: center;   /* optical center */
  padding-top: 80px;         /* nav clearance — shrinks available space */
  padding-bottom: var(--sp-9);
  padding-left: var(--sp-8);
  padding-right: var(--sp-8);
}
/* Result: content sits at optical center of remaining space (below nav) */
```

### Pattern B: Bottom-anchored hero with scroll cue (editorial/magazine)
```css
/* Content at bottom, but EYEBROW/DATE at top creates visual bookends */
/* Void is intentionally framed by top element — not dead space */
.hero {
  display: grid;
  grid-template-rows: auto 1fr auto;  /* top-anchor, spacer, content */
  min-height: 100vh;
  padding: var(--sp-7) var(--sp-8);
}
.hero-top    { /* eyebrow, date, number */ }
.hero-spacer { /* intentional void — now FRAMED, not dead */ }
.hero-bottom { /* name, stance, meta */ }
```

### Pattern C: Split hero (Studio macrostructure)
```css
/* Both columns must fill — no void inside columns */
.hero {
  display: grid;
  grid-template-columns: 1fr 1fr;
  min-height: 100vh;
  padding-top: 80px;  /* nav clearance on wrapper, not columns */
  align-items: stretch;
}
.hero-left  { display:flex; flex-direction:column; justify-content:center; padding:var(--sp-9) var(--sp-8); }
.hero-right { display:flex; flex-direction:column; padding:0; } /* cards fill height */
.hero-right .card { flex:1; } /* cards stretch to fill */
```

---

## Alignment: Balance vs Symmetry

```
Symmetry: identical weight on both sides (boring, static)
Balance:  equal visual weight, not necessarily equal size (dynamic, interesting)

Alignment rule: every element must be anchored to a grid column or a sibling edge.
"Ngambang" (floating) = element has no visual relationship to anything near it.

Checklist:
  □ Every element aligns to: left edge, right edge, center axis, or sibling
  □ No element is positioned by eye-balling (no magic numbers like margin-top:73px)
  □ Vertical rhythm: spacing between elements is multiples of base unit (8px grid)
  □ If two elements are "near" each other, they must snap to the same grid line
```

---

## Pre-emit Composition Check (run before Phase 3: PRODUCE)

Before writing HTML, answer:
```
1. Where is the focal point? (element name)
2. What % from top of viewport does it sit? (target ≤ 45%)
3. What frames the void above it? (eyebrow? border? nothing? → nothing = FAIL)
4. Eye flow: top-left → ? → ? → ? → exit point
5. Is every element anchored to a grid line or sibling edge? (yes/no)
```

If answer to 3 is "nothing" → change layout pattern before writing any HTML.

---

## Gate: Composition (for redesign-workflow integration)

```
Gate C1: Focal Point Above-Fold
  □ Primary element (H1/name) visible within first 100vh without scroll
  □ Primary element sits at ≤ 50% from top of viewport (optical center)
  □ No unframed dead space above primary element
  Score: __ / 10  (fail = score < 7)

Gate C2: Visual Weight Distribution
  □ One heavy, one supporting, one accent — all identifiable
  □ Heavy element has highest contrast + largest size in section
  □ No two elements compete for dominance (inter-section weight decay)
  Score: __ / 10

Gate C3: Alignment & Anchoring
  □ Every element aligned to grid column, sibling edge, or center axis
  □ No magic-number positioning (margin:73px etc)
  □ Spacing is multiples of base unit (8px grid)
  □ No floating elements — each has a visual relationship to its neighbors
  Score: __ / 10
```
