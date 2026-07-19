# Foundation Principles

> Universal design quality — applies to every genre, brand, surface, and medium.

Foundation principles describe **relationships**, not a preferred visual style.

---

## 1. Hierarchy — Visual Structure

```text
Hierarchy is navigation before it is styling.
The viewer should understand what matters first, what supports it,
and what belongs to a lower level without reading every word.
```

Review the complete role chain:

```text
page → section → group → item → detail/action
parent → child group → sibling items → metadata
```

Minimum requirements:

```text
□ primary, supporting, and tertiary roles are distinguishable at a glance
□ parent and child levels do not compete at equal visual weight
□ siblings look related but remain subordinate to their parent
□ headings, labels, body, metadata, and actions have identifiable roles
□ later sections do not accidentally overpower the global narrative anchor
```

Hierarchy cues include:

```text
scale, weight, family, width, measure, contrast, placement, spacing,
repetition, sequence, imagery, and motion priority
```

Use at least two cues when a nested relationship remains ambiguous. Numeric type ratios are useful diagnostics, not universal pass/fail laws.

Failure pattern:

```text
section title is large
project titles are almost equally large
parent-to-project gap equals project-to-project gap
result: introduction and children read as one flat group
```

---

## 2. Grouping — Gestalt and Proximity

```text
The viewer should know what belongs together before reading labels.
```

Use:

```text
proximity       → strongest default grouping cue
similarity      → repeated role or sibling relationship
alignment       → shared structural relationship
continuity      → path, sequence, or reading direction
enclosure       → only when function or comparison needs it
common region   → background/surface when genuinely meaningful
```

Rules:

```text
□ related elements cluster more strongly than unrelated elements
□ within-group spacing is usually tighter than between-group spacing
□ parent → child-group separation is stronger than child → child separation
□ enclosure does not replace weak proximity or hierarchy
□ same-looking items do not hide different maturity, priority, or state
```

Practical starting point:

```text
between-group interval ≈ 1.25×–2× within-group interval
```

This is a diagnostic range, not a universal token mandate. Verify at the actual viewport or output size.

---

## 3. Alignment — Structural and Optical Anchors

```text
Alignment creates hidden order. Optical alignment makes that order feel correct.
```

Minimum requirements:

```text
□ repeated roles reuse stable start, center, baseline, or end anchors
□ adjacent regions share a coherent shell or declared relationship
□ nearly aligned edges are corrected or intentionally separated
□ asymmetry has visible balancing logic
□ local transforms and arbitrary margins do not replace a shared grid
```

Geometric alignment is not always visually correct. Mixed font metrics, icons, badges, and irregular silhouettes may require one reusable optical correction.

Good correction:

```text
shared SectionEyebrow component with one optical offset
```

Bad correction:

```text
pt-2 on one section, translate-y on another, margin-top on a third
```

---

## 4. Space and Rhythm — Relationships Over Repetition

```text
Space is an information channel.
It may group, separate, pause, emphasize, sequence, or resolve.
```

Questions for every significant interval:

```text
- What relationship does this gap communicate?
- Is it within a group, between siblings, between parent and child group,
  between sections, or before a focal action?
- Would a different interval clarify the hierarchy?
```

Requirements:

```text
□ spacing changes according to relationship and importance
□ one repeated gap is not used for every level
□ large empty intervals have an anchor and a structural reason
□ sparse and dense sections are adjusted from evidence, not assumptions
□ whitespace does not strand content or conceal the next step
```

Dead space is not simply “large space.” It is space with no understandable job. Breathing room is space that improves grouping, focus, pacing, or comprehension.

---

## 5. Balance — Intentional Weight Distribution

Balance is not symmetry.

Evaluate together:

```text
scale + contrast + density + position + direction + color + imagery + empty space
```

Requirements:

```text
□ no region dominates accidentally
□ empty space balances rather than abandons content
□ asymmetrical layouts have a stable counterweight
□ focal emphasis supports the message or task
□ decorative accents do not distort the intended weight distribution
```

Valid results may be symmetrical, asymmetrical, centered, dense, open, static, or dynamic.

---

## 6. Flow — Reading, Narrative, and Task Sequence

```text
A design is not only a set of regions. It is an ordered experience.
```

Requirements:

```text
□ the first focal point is clear
□ the next intended region or action is discoverable
□ content sequence matches the intended narrative or task
□ visual order and semantic/DOM order do not conflict
□ section and state transitions preserve context
□ motion supports rather than hijacks the sequence
```

Common failure patterns:

```text
- two equally dominant focal points in one viewport
- CTA before enough meaning or proof exists
- desktop visual order that becomes confusing after mobile stacking
- metadata or decoration interrupting the main reading path
```

---

## 7. Legibility and Readability

```text
Legibility: can individual text and symbols be perceived?
Readability: can the content be comfortably understood in sequence?
```

Always inspect in the real context:

```text
viewport, distance, resolution, theme, orientation, localization,
text scaling, feed size, slide room size, or printed output
```

Requirements:

```text
□ type size, weight, leading, tracking, and case suit the role
□ line length and paragraph measure suit the medium
□ secondary content remains readable instead of becoming visual dust
□ contrast supports essential information
□ dense information is chunked and scannable
```

---

## 8. System Consistency

```text
Repeated roles should be predictably related.
Consistency is not forced sameness; it is coherent reuse plus justified exceptions.
```

Requirements:

```text
□ repeated colors, spacing roles, type roles, states, and components are coherent
□ the implementation uses the existing token/system mechanism when available
□ no duplicate token vocabulary is created without a migration reason
□ one-off static artifacts remain internally consistent even without software tokens
□ exceptions are documented and purposeful
```

Do not fail a design merely because it uses literal values in a valid local context. Fail inconsistency, uncontrolled repetition, or a broken existing system.

---

## 9. Accessibility and Affordance

Accessibility is foundational, not a final polish phase.

Always evaluate where applicable:

```text
□ text and essential graphics meet contextual contrast requirements
□ interactive targets are usable by touch, pointer, and keyboard
□ focus is visible
□ controls have understandable labels and states
□ semantic order supports assistive technology
□ reduced-motion preferences are respected
□ color is not the only carrier of essential meaning
```

Genre and brand do not exempt accessibility.

---

## 10. Responsive Continuity

```text
Responsive design preserves relationships, not only width.
```

Requirements:

```text
□ hierarchy survives scale reduction or orientation change
□ grouped content stays grouped after stacking
□ desktop rails collapse into a predictable reading order
□ labels, titles, content, and actions do not zig-zag accidentally
□ overflow, long words, localization, and text scaling remain safe
□ interaction patterns adapt to input and available space
```

A responsive layout fails when all elements technically fit but the original hierarchy, grouping, or flow no longer survives.