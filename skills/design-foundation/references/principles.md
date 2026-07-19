# Foundation Principles

> Universal design quality — applies to every genre, brand, surface, and medium.

Foundation principles describe **relationships**, not a preferred visual style.

---

## Universal Foundation Checklist

Before choosing a genre or polishing components, answer:

```text
HIERARCHY
  What is parent, child group, sibling, and supporting detail?

GROUPING
  What belongs together before labels are read?

FIGURE / GROUND + LAYERS
  What is canvas, content, containment, floating, modal, or system-level?
  What may overlap, what may be obscured, and why?

CONTENT RESILIENCE
  What are the supported empty, minimum, normal, maximum, and variant states?
  What may wrap, clamp, truncate, scroll, paginate, collapse, summarize, or substitute?

ALIGNMENT
  Which shared structural and optical anchors create order?

SPACE
  Which gaps mean within-group, sibling, parent-group, section transition, and content state?

BALANCE
  Where are visual mass, depth, overlap, density, and counterweight?

FLOW
  What is seen first, second, and acted on next?

LEGIBILITY
  Does every role survive actual-size viewing, real content, and its real background?

CONSISTENCY
  Which repeated roles, tokens, surfaces, layer semantics, fallbacks, and adaptation policies must remain coherent?

ACCESSIBILITY
  Can the information and interaction be perceived and operated safely?

RESPONSIVE CONTINUITY
  Which relationships must survive stacking, resizing, orientation, theme, crop,
  localization, text scaling, content variation, and input changes?
```

Unresolved foundation questions block final direction approval.

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
□ content length changes do not flatten semantic roles into one weight
```

Hierarchy cues include:

```text
scale, weight, family, width, measure, contrast, placement, spacing,
repetition, sequence, imagery, depth, content priority, and motion priority
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
figure-ground   → ownership between content and its surrounding field
presence        → optional/missing content must not break remaining ownership
```

Rules:

```text
□ related elements cluster more strongly than unrelated elements
□ within-group spacing is usually tighter than between-group spacing
□ parent → child-group separation is stronger than child → child separation
□ enclosure does not replace weak proximity or hierarchy
□ same-looking items do not hide different maturity, priority, or state
□ surfaces and background fields clarify ownership instead of fragmenting one task
□ optional labels, media, metadata, or actions may disappear without detaching the rest
□ one item and many items preserve parent/sibling meaning appropriate to their state
```

Practical starting point:

```text
between-group interval ≈ 1.25×–2× within-group interval
```

This is a diagnostic range, not a universal token mandate. Verify at the actual viewport or output size.

---

## 2b. Figure–Ground and Semantic Layering

```text
Figure-ground answers what is foreground, what supports it, what contains it,
what floats above it, and what temporarily blocks it.
```

Use semantic roles before implementation values:

```text
canvas → content → containment → floating → modal → system/critical
```

Minimum requirements:

```text
□ intended foreground is distinguishable from its background
□ depth communicates containment, priority, transience, focus, or state
□ equal semantic roles do not receive arbitrary unequal elevation
□ overlap has an owner, a reason, a safe region, and a continuity plan
□ sticky or fixed elements do not cover required content or actions
□ text-on-image survives the full required area, crop, theme, and viewport set
□ interactive layers preserve context and provide a clear continuation or recovery path
□ shadows, blur, glass, gradients, outlines, and borders do not replace grouping or hierarchy
```

A flat composition can pass. A highly layered composition can pass. Depth quantity is not the quality criterion.

Load `figure-ground-layering.md` for detailed evidence rules and handoff boundaries. Load `figure-ground-fixtures.md` for cross-genre regression.

---

## 2c. Content Resilience — Relationships Under Variation

```text
Content resilience answers whether the design still communicates correctly when
quantity, length, presence, media, language, or data shape changes within supported bounds.
```

Declare the supported conditions:

```text
EMPTY       no primary items or optional content
MINIMUM     smallest meaningful composition
NORMAL      realistic production content
MAXIMUM     declared high count, long copy, dense metadata, or large values
VARIANT     localization, text scaling, missing media, unusual ratio, mixed scripts/formats
UNEXPECTED  bounded user/generated or malformed content the surface can realistically receive
```

Minimum requirements:

```text
□ supported quantity, text, media, language, and output bounds are explicit
□ optional content can appear or disappear without breaking hierarchy/grouping
□ empty, sparse, normal, and dense states do not reuse one composition blindly
□ critical meaning is not silently clipped, shrunk, or removed
□ wrap, clamp, truncate, scroll, paginate, summarize, prioritize, disclose,
  or component substitution has a clear reason and recovery path where needed
□ repeated roles use coherent overflow, fallback, and missing-content policies
□ media variation preserves surrounding ownership and required information
□ realistic stress combines content variation with constrained viewport/format
□ unsupported content is constrained or communicated honestly rather than failing silently
```

A design is not required to support unlimited content. A strict declared bound can pass. An unstated bound discovered only after content breaks cannot.

Load `content-resilience.md` for the supported-bounds contract, stress matrix, adaptation strategies, evidence policy, and handoff boundaries. Load `content-resilience-fixtures.md` for cross-surface PASS/FAIL regression.

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
□ wrapped or optional content does not create accidental anchor drift
```

Geometric alignment is not always visually correct. Mixed font metrics, icons, badges, irregular silhouettes, large numbers, and multiline values may require one reusable optical correction.

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
  between sections, before a focal action, or a response to content state?
- Would a different interval clarify the hierarchy?
- Is the visible interval the intentional result after adjacent wrappers combine?
- Does this composition still make sense with empty, one, normal, and dense content?
```

Requirements:

```text
□ spacing changes according to relationship and importance
□ one repeated gap is not used for every level
□ large empty intervals have an anchor and a structural reason
□ empty, sparse, normal, and dense sections are adjusted from evidence, not assumptions
□ whitespace does not strand content or conceal the next step
□ each major section boundary has one deliberate spacing owner
□ missing optional content collapses deliberately instead of leaving unexplained holes
□ maximum content does not eliminate every meaningful interval
```

Dead space is not simply “large space.” It is space with no understandable job. Breathing room is space that improves grouping, focus, pacing, or comprehension.

---

## 5. Balance — Intentional Weight Distribution

Balance is not symmetry.

Evaluate together:

```text
scale + contrast + density + position + direction + color + imagery + depth + overlap + empty space
```

Requirements:

```text
□ no region or visual layer dominates accidentally
□ empty space balances rather than abandons content
□ asymmetrical layouts have a stable counterweight
□ focal emphasis supports the message or task
□ decorative accents and depth effects do not distort the intended weight distribution
□ overlap does not hide required information, evidence, status, or action
□ sparse and dense content states preserve an intentional weight distribution
□ one long title, large value, or missing image does not become an accidental focal point
```

Valid results may be symmetrical, asymmetrical, centered, dense, open, flat, layered, static, or dynamic.

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
□ section, state, and layer transitions preserve context
□ an interactive layer communicates what changed and how to continue or recover
□ content adaptation preserves task priority and comparison order
□ pagination, disclosure, or component substitution preserves orientation where applicable
□ motion supports rather than hijacks the sequence
```

Common failure patterns:

```text
- two equally dominant focal points in one viewport
- CTA before enough meaning or proof exists
- desktop visual order that becomes confusing after mobile stacking
- metadata or decoration interrupting the main reading path
- a drawer, dialog, popover, or sheet loses the selected object or next valid action
- truncation, pagination, or substitution hides the distinguishing content or resets context
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
text scaling, content length, numeric/data shape, feed size, slide room size,
crop, overlay, or printed output
```

Requirements:

```text
□ type size, weight, leading, tracking, and case suit the role
□ line length and paragraph measure suit the medium
□ secondary content remains readable instead of becoming visual dust
□ contrast supports essential information
□ imagery, texture, glow, blur, and gradients do not interfere with required text or symbols
□ dense information is chunked and scannable
□ realistic long titles, labels, values, numbers, dates, and units are tested
□ critical meaning is not silently clipped, truncated, or shrunk below useful perception
□ labels and values remain associated after wrapping or recomposition
```

---

## 8. System Consistency

```text
Repeated roles should be predictably related.
Consistency is not forced sameness; it is coherent reuse plus justified exceptions.
```

Requirements:

```text
□ repeated colors, spacing roles, type roles, states, surfaces, and components are coherent
□ semantic layer/elevation roles are coherent where a system exists
□ repeated roles use coherent overflow, fallback, optional-content, and media policies
□ component variants are selected from content/task need rather than arbitrary preference
□ the implementation uses the existing token/system mechanism when available
□ no duplicate token vocabulary is created without a migration reason
□ arbitrary z-index escalation does not replace semantic layer ownership
□ one-off local fixes do not become the hidden maximum-content strategy
□ reusable templates expose meaningful authoring/content constraints
□ one-off static artifacts remain internally consistent even without software tokens
□ exceptions are documented and purposeful
```

Do not fail a design merely because it uses literal values in a valid local context. Fail inconsistency, uncontrolled repetition, hidden bounds, or a broken existing system.

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
□ interactive layers expose understandable state, focus/input ownership, dismissal, and recovery
□ content adaptation does not remove critical labels, names, instructions, or alternatives
□ text scaling and localization do not hide required actions or information
□ reduced-motion preferences are respected
□ color is not the only carrier of essential meaning
```

Genre and brand do not exempt accessibility. Detailed modal safety, state announcements, input parity, validation, and runtime behavior remain owned by interactive surface gates.

---

## 10. Responsive Continuity

```text
Responsive design preserves relationships, not only width.
```

Requirements:

```text
□ hierarchy survives scale reduction or orientation change
□ grouped content stays grouped after stacking and optional-content changes
□ desktop rails collapse into a predictable reading order
□ labels, titles, content, and actions do not zig-zag accidentally
□ overflow, long words, localization, content variation, and text scaling remain safe
□ interaction patterns adapt to input and available space
□ sticky, fixed, floating, modal, and overlapping relationships remain safe and understandable
□ crop and theme changes preserve figure-ground distinction where applicable
□ long content is tested on constrained viewports, not only on wide layouts
□ dense content and missing media are tested in required viewport/format variants
□ component substitution preserves task, state, and selection meaning
```

A responsive layout fails when all elements technically fit but the original hierarchy, grouping, layer meaning, content meaning, or flow no longer survives.
