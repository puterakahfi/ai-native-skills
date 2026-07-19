# Foundation Gates Scorecard

> Run for every design review before genre, brand, component, or domain-specific approval.

Foundation gates evaluate universal relationships. Profile and genre references may add stricter thresholds, but may not remove these checks.

Load `figure-ground-layering.md` when the artifact includes surfaces, imagery behind text, overlap, sticky/fixed UI, popovers, drawers, dialogs, layered compositions, or depth effects.

## Evidence Policy

```text
RENDERED evidence available      → evaluate visual relationship gates
SOURCE/system evidence available → evaluate consistency and implementation gates
INTERACTION evidence available   → evaluate affordance, order, layer continuity, and responsive behavior
missing required evidence        → NOT_VERIFIED, never PASS
```

Use measurements to explain an observed problem. Do not turn one ratio, z-index value, elevation token, or spacing heuristic into a universal law.

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

## F2 — Grouping, Gestalt, and Figure–Ground

```text
CHECK:
□ related elements cluster more strongly than unrelated elements
□ within-group spacing is tighter than between-group spacing where applicable
□ parent → child-group separation is stronger than child → child separation
□ similarity communicates sibling roles without hiding important differences
□ enclosure, cards, or surfaces are used only when functionally useful
□ foreground, background, and containment ownership are understandable
□ floating or overlapping elements remain visibly attached to the object/task they belong to

FAIL examples:
- parent introduction and child collection read as one flat group
- child details feel detached from their item
- unrelated sections appear grouped because their gap is too small
- every item is boxed because proximity and hierarchy are unresolved
- low-contrast surfaces merge and erase region ownership
- a popover, annotation, or floating control appears detached from its trigger or subject
- nested surfaces create card-within-card fragmentation without a comparison or task reason
```

Diagnostic starting point:

```text
between-group interval ≈ 1.25×–2× within-group interval
```

Verify visually; do not enforce as a universal token. A flat composition may pass when relationship cues are clear.

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

## F5 — Balance, Depth, and Weight Distribution

```text
CHECK:
□ visual mass is distributed intentionally
□ empty space balances rather than abandons content
□ contrast, scale, color, imagery, density, depth, and overlap support the intended focal point
□ asymmetrical layouts have a stable counterweight
□ no secondary region or visual layer becomes accidentally dominant
□ overlap and elevation do not obscure required content, status, evidence, or action
□ shadows, blur, glass, gradients, outlines, and depth effects have a structural or expressive job

FAIL examples:
- one side of the composition feels overloaded without a counterweight
- decorative color, image, or atmospheric background competes with the main message
- a sparse region appears unfinished because its anchor is too weak
- a dark/elevated surface overpowers the page’s actual narrative anchor
- sticky or fixed content covers required text, controls, or the primary action
- decorative overlap creates an accidental second focal point
- depth effects fill space but do not explain containment, priority, transience, focus, or state
```

Balance is not symmetry. Depth quantity is not quality.

---

## F6 — Flow and Sequence

```text
CHECK:
□ the first focal point is clear
□ the next intended region or action is discoverable
□ reading order matches semantic/task order
□ transitions between sections, states, and layers preserve context
□ CTA placement follows sufficient meaning, evidence, or task readiness
□ interactive layers communicate what changed and how to continue or recover
□ motion supports rather than interrupts the sequence

FAIL examples:
- competing anchors create multiple first steps
- visual order conflicts with DOM or keyboard order
- responsive stacking changes the intended narrative
- decorative elements interrupt the reading path
- opening or dismissing a layer loses the selected object, task context, or next action
```

---

## F7 — Legibility and Readability

```text
CHECK:
□ text size, weight, leading, tracking, and case suit the actual context
□ line length and measure support sustained reading or scanning
□ secondary content remains perceivable
□ contrast supports essential information
□ imagery, texture, glow, blur, and gradients do not interfere with critical text or symbols
□ information density is chunked appropriately

FAIL examples:
- metadata becomes visual dust
- low-contrast body copy depends on zoom
- display text overflows or creates unreadable line breaks
- paragraphs are too wide, dense, or fragmented for the medium
- text-on-image survives only in one favorable crop, theme, or viewport
```

Use applicable WCAG, platform, print, feed, or presentation thresholds from the surface reviewer.

---

## F8 — System Consistency

```text
CHECK:
□ repeated roles use coherent colors, spacing, type roles, states, and components
□ existing tokens or design-system mechanisms are reused when available
□ semantic layer/elevation roles are coherent when a system exists
□ exceptions are intentional and documented
□ no parallel token vocabulary is introduced without a migration reason
□ static artifacts remain internally consistent even without source tokens

FAIL examples:
- same semantic role changes treatment without reason
- duplicate spacing/color/type/layer systems coexist accidentally
- local hardcoded values break theme or component consistency
- arbitrary z-index escalation replaces semantic layer ownership
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
□ interactive layers expose understandable state, focus/input ownership, dismissal, and recovery
□ reduced-motion preference is respected
□ color is not the only carrier of essential meaning

Any verified accessibility blocker = FAIL.
```

Detailed focus trapping, input parity, and modal behavior remain owned by applicable interactive surface gates.

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
□ sticky, fixed, floating, modal, and overlapping relationships remain safe and understandable
□ theme/crop changes preserve layer distinction where applicable

FAIL examples:
- desktop hierarchy becomes flat on mobile
- child details detach from their parent after stacking
- horizontal navigation overlaps or hides without an adaptive pattern
- local offsets produce mobile drift
- sticky header, keyboard, sheet, or floating action overlap and consume required content
- a crop or theme change removes the figure-ground cue
```

---

## Quick Foundation Review

For a focused visual iteration, inspect in this order:

```text
1. F1 Hierarchy     — what is parent, child group, sibling, and detail?
2. F2 Grouping      — what belongs together and what is foreground/ground?
3. F3 Alignment     — what shared anchors create hidden order?
4. F4 Rhythm        — do gaps encode those relationships?
5. F5 Balance       — where are visual mass, depth, overlap, and counterweight?
6. F6 Flow          — what does the eye/user do next, including layer changes?
7. F7 Legibility    — does it survive actual-size viewing and background interference?
8. F10 Continuity   — do relationships and layer safety survive required formats/viewports?
```

F8 and F9 remain mandatory when their evidence and medium are applicable.

---

## Foundation Scorecard Template

```text
FOUNDATION GATES
────────────────────────────────────────────────────
F1  Hierarchy             PASS | FAIL | NOT_VERIFIED
F2  Grouping              PASS | FAIL | NOT_VERIFIED
F3  Alignment             PASS | FAIL | NOT_VERIFIED
F4  Spatial rhythm        PASS | FAIL | NOT_VERIFIED
F5  Balance               PASS | FAIL | NOT_VERIFIED
F6  Flow                  PASS | FAIL | NOT_VERIFIED
F7  Legibility            PASS | FAIL | NOT_VERIFIED
F8  System consistency    PASS | FAIL | NOT_APPLICABLE | NOT_VERIFIED
F9  Accessibility         PASS | FAIL | NOT_APPLICABLE | NOT_VERIFIED
F10 Responsive continuity PASS | FAIL | NOT_APPLICABLE | NOT_VERIFIED
────────────────────────────────────────────────────
Evidence gaps: [...] 
Blocking failures: [...] 
RESULT: all applicable verified gates pass → continue to genre/domain gates
        any verified fail → classify and correct before release approval
```

## Defect Classification Hints

```text
hierarchy/grouping/spacing/figure-ground failure across multiple regions
  → foundation or structure defect

one repeated pattern fails everywhere
  → component-system defect

rule exists but implementation ignores it
  → local implementation defect

foundation rule absent or misleading
  → design-foundation knowledge defect

workflow never loaded foundation before production
  → workflow orchestration defect

focus trap, runtime, crop, fidelity, or export-specific failure
  → applicable interactive/static/domain reviewer
```

Do not fix a foundation failure by adding decoration. Correct the relationship first.