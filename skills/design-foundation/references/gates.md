# Foundation Gates Scorecard

> Run for every design review before genre, brand, component, or domain-specific approval.

Foundation gates evaluate universal relationships. Profile and genre references may add stricter thresholds, but may not remove these checks.

Load `figure-ground-layering.md` when the artifact includes surfaces, imagery behind text, overlap, sticky/fixed UI, popovers, drawers, dialogs, layered compositions, or depth effects.

Load `content-resilience.md` when the artifact or template can receive variable quantity, text length, data shape, localization, text scaling, optional metadata/media, generated/user content, or reusable content variants. Load `content-resilience-fixtures.md` for cross-surface regression.

## Evidence Policy

```text
RENDERED evidence available        → evaluate visual relationship gates
SOURCE/system evidence available   → evaluate consistency and implementation gates
INTERACTION evidence available     → evaluate affordance, order, layer continuity,
                                     overflow, state, and responsive behavior
CONTENT-VARIANT evidence available → evaluate supported bounds and resilience gates
missing required evidence          → NOT_VERIFIED, never PASS
```

A single ideal screenshot does not verify content resilience for a variable-content surface. Record which applicable states were exercised:

```text
EMPTY | MINIMUM | NORMAL | MAXIMUM | VARIANT | UNEXPECTED/UNTRUSTED
```

Use measurements to explain an observed problem. Do not turn one ratio, z-index value, character count, item count, elevation token, or spacing heuristic into a universal law.

---

## F1 — Hierarchy and Role Clarity

```text
CHECK:
□ primary, supporting, and tertiary roles are distinguishable at a glance
□ parent and child levels do not compete at equal visual weight
□ siblings look related but remain subordinate to their parent
□ heading, body, label, metadata, and action roles are recognizable
□ later sections preserve the intended global hierarchy
□ realistic long/short content does not flatten roles into one weight

FAIL examples:
- section heading and child item titles look equally dominant
- labels, metadata, and body copy collapse into the same visual role
- multiple competing focal points make the first reading step unclear
- long content forces every role to the same size, weight, or density
```

Useful evidence:

```text
type scale, weight, measure, contrast, placement, spacing,
attention order, blur/squint test, actual-size viewport capture,
short/normal/long content comparison
```

Numeric ratios are diagnostic only.

---

## F2 — Grouping, Gestalt, Figure–Ground, and Presence

```text
CHECK:
□ related elements cluster more strongly than unrelated elements
□ within-group spacing is tighter than between-group spacing where applicable
□ parent → child-group separation is stronger than child → child separation
□ similarity communicates sibling roles without hiding important differences
□ enclosure, cards, or surfaces are used only when functionally useful
□ foreground, background, and containment ownership are understandable
□ floating or overlapping elements remain visibly attached to the object/task they belong to
□ optional text, media, metadata, and actions can appear/disappear without detaching the rest
□ one item and many items preserve appropriate parent/sibling meaning

FAIL examples:
- parent introduction and child collection read as one flat group
- child details feel detached from their item
- unrelated sections appear grouped because their gap is too small
- every item is boxed because proximity and hierarchy are unresolved
- low-contrast surfaces merge and erase region ownership
- a popover, annotation, or floating control appears detached from its trigger or subject
- nested surfaces create card-within-card fragmentation without a comparison or task reason
- missing metadata leaves an orphan label, action, divider, or unexplained hole
- one item remains stranded in a composition that implies missing siblings
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
□ wrapping, optional content, large values, and missing media preserve meaningful anchors

FAIL examples:
- each section invents a different content start position
- repeated translate/margin nudges create page-wide drift
- DOM boxes align but rendered glyph tops look crooked
- mobile stacking preserves desktop offsets and creates zig-zag order
- multiline labels or large values cause per-item alignment drift with no shared policy
```

---

## F4 — Spatial Rhythm and Content Density

```text
CHECK:
□ spacing expresses hierarchy, grouping, sequence, emphasis, and content state
□ one repeated interval is not used for every relationship
□ large empty intervals have an anchor and purpose
□ empty, sparse, normal, and dense regions are proportioned intentionally
□ transitions between regions feel neither collapsed nor abandoned
□ each major section boundary has one declared spacing owner
□ missing optional content collapses deliberately instead of leaving unexplained gaps
□ maximum content preserves enough interval for scanning and role separation

FAIL examples:
- parent-to-children gap equals sibling-to-sibling gap
- every section uses the same top/bottom padding regardless of content
- adjacent sections each add a full boundary interval and create accidental double spacing
- content appears stranded inside a large void
- spacing is compensated with borders instead of corrected relationally
- empty state preserves a large collection grid with no structural purpose
- dense state compresses every interval until hierarchy becomes flat
- one-card, three-card, and thirty-card states use one composition blindly
```

A section transition may be owned by the previous section, the following section, or a shared layout primitive. The failure is not the implementation method; it is an unintended sum of independent intervals with no clear structural job.

---

## F5 — Balance, Depth, Density, and Weight Distribution

```text
CHECK:
□ visual mass is distributed intentionally
□ empty space balances rather than abandons content
□ contrast, scale, color, imagery, density, depth, and overlap support the intended focal point
□ asymmetrical layouts have a stable counterweight
□ no secondary region, visual layer, long value, or missing-media fallback becomes accidentally dominant
□ overlap and elevation do not obscure required content, status, evidence, or action
□ shadows, blur, glass, gradients, outlines, and depth effects have a structural or expressive job
□ sparse and maximum-content states preserve an intentional weight distribution

FAIL examples:
- one side of the composition feels overloaded without a counterweight
- decorative color, image, or atmospheric background competes with the main message
- a sparse region appears unfinished because its anchor is too weak
- a dark/elevated surface overpowers the page’s actual narrative anchor
- sticky or fixed content covers required text, controls, or the primary action
- decorative overlap creates an accidental second focal point
- depth effects fill space but do not explain containment, priority, transience, focus, or state
- one long title, large number, or fallback asset becomes the unintended focal point
```

Balance is not symmetry. Depth quantity and content quantity are not quality.

---

## F6 — Flow and Sequence

```text
CHECK:
□ the first focal point is clear
□ the next intended region or action is discoverable
□ reading order matches semantic/task order
□ transitions between sections, states, layers, and content adaptations preserve context
□ CTA placement follows sufficient meaning, evidence, or task readiness
□ interactive layers communicate what changed and how to continue or recover
□ truncation, disclosure, pagination, scrolling, or component substitution preserves orientation
□ motion supports rather than interrupts the sequence

FAIL examples:
- competing anchors create multiple first steps
- visual order conflicts with DOM or keyboard order
- responsive stacking changes the intended narrative
- decorative elements interrupt the reading path
- opening or dismissing a layer loses the selected object, task context, or next action
- pagination or pattern substitution resets selection or changes task meaning
- truncated content hides the distinguishing information needed for the next step
```

---

## F7 — Legibility, Readability, and Content Shape

```text
CHECK:
□ text size, weight, leading, tracking, and case suit the actual context
□ line length and measure support sustained reading or scanning
□ secondary content remains perceivable
□ contrast supports essential information
□ imagery, texture, glow, blur, and gradients do not interfere with critical text or symbols
□ information density is chunked appropriately
□ realistic long/short titles, labels, values, numbers, dates, prices, units, and IDs are tested
□ wrapping, clamping, or truncation preserves role association and critical meaning
□ supported localization, mixed scripts, and text scaling remain readable
□ large values and dense data remain distinguishable and comparable

FAIL examples:
- metadata becomes visual dust
- low-contrast body copy depends on zoom
- display text overflows or creates unreadable line breaks
- paragraphs are too wide, dense, or fragmented for the medium
- text-on-image survives only in one favorable crop, theme, or viewport
- labels detach from wrapped values or controls
- fixed-height clipping removes essential text
- truncation makes sibling items indistinguishable
- currency, unit, date, status, or distinguishing suffix disappears
- text is shrunk below useful perception to preserve one-line layout
```

Use applicable WCAG, platform, print, feed, or presentation thresholds from the surface reviewer.

---

## F8 — System Consistency and Adaptation Policy

```text
CHECK:
□ repeated roles use coherent colors, spacing, type roles, states, and components
□ existing tokens or design-system mechanisms are reused when available
□ semantic layer/elevation roles are coherent when a system exists
□ repeated roles use coherent wrap/clamp/truncate/scroll/fallback/optional-content policies
□ component variants are selected from content/task need rather than arbitrary preference
□ declared content bounds are exposed to authors, generators, or implementers where relevant
□ exceptions are intentional and documented
□ no parallel token or adaptation vocabulary is introduced without a migration reason
□ static artifacts remain internally consistent even without source tokens

FAIL examples:
- same semantic role changes treatment without reason
- duplicate spacing/color/type/layer systems coexist accidentally
- local hardcoded values break theme or component consistency
- arbitrary z-index escalation replaces semantic layer ownership
- one card wraps, another clips, and another shrinks the same title role without reason
- local height/character hacks become the hidden maximum-content policy
- reusable template silently accepts content beyond its real supported bounds
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
□ content adaptation does not remove critical labels, names, instructions, or alternatives
□ localization and text scaling do not hide required content or actions
□ reduced-motion preference is respected
□ color is not the only carrier of essential meaning

Any verified accessibility blocker = FAIL.
```

Detailed focus trapping, input parity, validation, announcements, loading/error behavior, and modal mechanics remain owned by applicable interactive surface gates.

---

## F10 — Responsive and Content Continuity

```text
CHECK:
□ hierarchy survives viewport, orientation, format, and supported-content changes
□ grouped content stays grouped after stacking and optional-content changes
□ reading and interaction order remain predictable
□ labels, titles, content, and actions do not zig-zag accidentally
□ overflow, localization, realistic long content, and text scaling are safe
□ controls adapt to input type and available space
□ sticky, fixed, floating, modal, and overlapping relationships remain safe and understandable
□ theme/crop changes preserve layer distinction where applicable
□ long content is tested on constrained viewports, not only on wide layouts
□ dense content and missing media are tested in required formats/viewports
□ component substitution preserves task, state, selection, and comparison meaning

FAIL examples:
- desktop hierarchy becomes flat on mobile
- child details detach from their parent after stacking
- horizontal navigation overlaps or hides without an adaptive pattern
- local offsets produce mobile drift
- sticky header, keyboard, sheet, or floating action overlap and consume required content
- a crop or theme change removes the figure-ground cue
- short content passes mobile while realistic long content clips or overlaps
- desktop table is forced into unreadable cards and loses comparison structure
- localization or text scaling hides primary actions or required values
- missing media collapses the surrounding mobile composition
```

---

## Content Stress Review

For variable-content surfaces, record the applicable matrix before assigning PASS:

```text
SUPPORTED BOUNDS
content source: fixed | curated | generated | user-authored | system/data-driven
quantity: minimum [...] | normal [...] | declared maximum [...]
text/value range: [...]
media variation: [...]
languages/scripts/formats: [...]
output/viewports: [...]

STATES EXERCISED
EMPTY:               PASS | FAIL | NOT_APPLICABLE | NOT_VERIFIED
MINIMUM:             PASS | FAIL | NOT_APPLICABLE | NOT_VERIFIED
NORMAL:              PASS | FAIL | NOT_VERIFIED
MAXIMUM:             PASS | FAIL | NOT_APPLICABLE | NOT_VERIFIED
VARIANT:             PASS | FAIL | NOT_APPLICABLE | NOT_VERIFIED
UNEXPECTED/UNTRUSTED PASS | FAIL | NOT_APPLICABLE | NOT_VERIFIED

COMBINATIONS EXERCISED
long content + constrained viewport
localization/text scaling + real controls
missing media + dense metadata
large values + constrained column
empty collection + persistent controls
```

Do not invent stress states for a locked one-off artifact. Do not mark dynamic resilience passed from placeholder-perfect content.

---

## Quick Foundation Review

For a focused visual iteration, inspect in this order:

```text
1. F1 Hierarchy     — what is parent, child group, sibling, and detail?
2. F2 Grouping      — what belongs together and what survives optional presence?
3. F3 Alignment     — what shared anchors survive wrapping and variation?
4. F4 Rhythm        — do gaps/density encode relationships and content state?
5. F5 Balance       — where are visual mass, depth, density, and counterweight?
6. F6 Flow          — what happens after adaptation, disclosure, or pagination?
7. F7 Legibility    — does realistic content survive actual-size viewing?
8. F10 Continuity   — do relationships survive required content + viewport combinations?
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
Content stress states: [...]
Representative combinations: [...]
Evidence gaps: [...]
Blocking failures: [...]
RESULT: all applicable verified gates pass → continue to genre/domain gates
        any verified fail → classify and correct before release approval
```

## Defect Classification Hints

```text
hierarchy/grouping/spacing/figure-ground/content-resilience failure across multiple regions
  → foundation or structure defect

one repeated component/pattern fails content variation everywhere
  → component-system defect

rule exists but implementation ignores it
  → local implementation defect

foundation rule absent or misleading
  → design-foundation knowledge defect

workflow never loaded foundation before production
  → workflow orchestration defect

honestly declared unsupported quantity/content type is exceeded
  → verify boundary communication and recovery; not automatically a foundation defect

focus trap, loading/error, runtime, validation, security, crop, fidelity, or export-specific failure
  → applicable interactive/static/domain/engineering reviewer
```

Do not fix a foundation failure by adding decoration, shrinking everything, or hiding content indiscriminately. Correct the relationship and choose an explicit adaptation strategy.
