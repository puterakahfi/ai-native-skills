# Foundation Gates Scorecard

> Run for every design review before genre, brand, component, or domain-specific approval.

Foundation gates evaluate universal relationships. Profile and genre references may add stricter thresholds, but may not remove these checks.

## Evidence Policy

```text
RENDERED evidence available      → evaluate visual relationship gates
SOURCE/system evidence available → evaluate consistency and implementation gates
INTERACTION evidence available   → evaluate affordance, order, and responsive behavior
missing required evidence        → NOT_VERIFIED, never PASS
```

Use measurements to explain an observed problem. Do not turn one ratio or token heuristic into a universal law.

---

## F1 — Hierarchy and Role Clarity

```text
CHECK:
□ primary, supporting, and tertiary roles are distinguishable at a glance
□ parent and child levels do not compete at equal visual weight
□ siblings look related but remain subordinate to their parent
□ heading, body, label, metadata, and action roles are recognizable
□ later sections preserve the intended global hierarchy

FAIL examples:
- section heading and child item titles look equally dominant
- labels, metadata, and body copy collapse into the same visual role
- multiple competing focal points make the first reading step unclear
```

Useful evidence:

```text
type scale, weight, measure, contrast, placement, spacing,
attention order, blur/squint test, actual-size viewport capture
```

Numeric ratios are diagnostic only.

---

## F2 — Grouping and Gestalt

```text
CHECK:
□ related elements cluster more strongly than unrelated elements
□ within-group spacing is tighter than between-group spacing where applicable
□ parent → child-group separation is stronger than child → child separation
□ similarity communicates sibling roles without hiding important differences
□ enclosure, cards, or surfaces are used only when functionally useful

FAIL examples:
- parent introduction and child collection read as one flat group
- child details feel detached from their item
- unrelated sections appear grouped because their gap is too small
- every item is boxed because proximity and hierarchy are unresolved
```

Diagnostic starting point:

```text
between-group interval ≈ 1.25×–2× within-group interval
```

Verify visually; do not enforce as a universal token.

---

## F3 — Alignment and Optical Continuity

```text
CHECK:
□ repeated roles use stable structural anchors
□ adjacent sections share a coherent shell or declared relationship
□ almost-aligned edges are corrected or intentionally separated
□ mixed-size label/heading pairs are optically aligned
□ asymmetry has visible balancing logic
□ arbitrary local offsets do not replace a shared grid

FAIL examples:
- each section invents a different content start position
- repeated translate/margin nudges create page-wide drift
- DOM boxes align but rendered glyph tops look crooked
- mobile stacking preserves desktop offsets and creates zig-zag order
```

---

## F4 — Spatial Rhythm

```text
CHECK:
□ spacing expresses hierarchy, grouping, sequence, and emphasis
□ one repeated interval is not used for every relationship
□ large empty intervals have an anchor and purpose
□ dense and sparse regions are proportioned intentionally
□ transitions between regions feel neither collapsed nor abandoned
□ each major section boundary has one declared spacing owner

FAIL examples:
- parent-to-children gap equals sibling-to-sibling gap
- every section uses the same top/bottom padding regardless of content
- adjacent sections each add a full boundary interval and create accidental double spacing
- content appears stranded inside a large void
- spacing is compensated with borders instead of corrected relationally
```

A section transition may be owned by the previous section, the following section, or a shared layout primitive. The failure is not the implementation method; it is an unintended sum of independent intervals with no clear structural job.

---

## F5 — Balance and Weight Distribution

```text
CHECK:
□ visual mass is distributed intentionally
□ empty space balances rather than abandons content
□ contrast, scale, color, imagery, and density support the intended focal point
□ asymmetrical layouts have a stable counterweight
□ no secondary region becomes accidentally dominant

FAIL examples:
- one side of the composition feels overloaded without a counterweight
- decorative color or image competes with the main message
- a sparse region appears unfinished because its anchor is too weak
```

Balance is not symmetry.

---

## F6 — Flow and Sequence

```text
CHECK:
□ the first focal point is clear
□ the next intended region or action is discoverable
□ reading order matches semantic/task order
□ transitions preserve context
□ CTA placement follows sufficient meaning, evidence, or task readiness
□ motion supports rather than interrupts the sequence

FAIL examples:
- competing anchors create multiple first steps
- visual order conflicts with DOM or keyboard order
- responsive stacking changes the intended narrative
- decorative elements interrupt the reading path
```

---

## F7 — Legibility and Readability

```text
CHECK:
□ text size, weight, leading, tracking, and case suit the actual context
□ line length and measure support sustained reading or scanning
□ secondary content remains perceivable
□ contrast supports essential information
□ information density is chunked appropriately

FAIL examples:
- metadata becomes visual dust
- low-contrast body copy depends on zoom
- display text overflows or creates unreadable line breaks
- paragraphs are too wide, dense, or fragmented for the medium
```

Use applicable WCAG, platform, print, feed, or presentation thresholds from the surface reviewer.

---

## F8 — System Consistency

```text
CHECK:
□ repeated roles use coherent colors, spacing, type roles, states, and components
□ existing tokens or design-system mechanisms are reused when available
□ exceptions are intentional and documented
□ no parallel token vocabulary is introduced without a migration reason
□ static artifacts remain internally consistent even without source tokens

FAIL examples:
- same semantic role changes treatment without reason
- duplicate spacing/color/type systems coexist accidentally
- local hardcoded values break theme or component consistency
```

Do not require software tokens for a one-off static artifact. Evaluate the medium and available source.

---

## F9 — Accessibility and Affordance

```text
CHECK where applicable:
□ contrast meets contextual accessibility requirements
□ controls have understandable labels and states
□ focus is visible
□ touch/pointer targets are usable
□ semantic and keyboard order are logical
□ reduced-motion preference is respected
□ color is not the only carrier of essential meaning

Any verified accessibility blocker = FAIL.
```

---

## F10 — Responsive Continuity

```text
CHECK:
□ hierarchy survives viewport, orientation, or format changes
□ grouped content stays grouped after stacking
□ reading and interaction order remain predictable
□ labels, titles, content, and actions do not zig-zag accidentally
□ overflow, localization, and text scaling are safe
□ controls adapt to input type and available space

FAIL examples:
- desktop hierarchy becomes flat on mobile
- child details detach from their parent after stacking
- horizontal navigation overlaps or hides without an adaptive pattern
- local offsets produce mobile drift
```

---

## Quick Foundation Review

For a focused visual iteration, inspect in this order:

```text
1. F1 Hierarchy  — what is parent, child group, sibling, and detail?
2. F2 Grouping   — what belongs together before labels are read?
3. F3 Alignment  — what shared anchors create hidden order?
4. F4 Rhythm     — do gaps encode those relationships?
5. F5 Balance    — where is visual mass and counterweight?
```
