# Semantic Status Encoding

> Semantic color is not decoration when it communicates outcome, risk, evidence, progress, availability, or consequence.

Load this reference when a design contains status badges, alerts, validation, scorecards, review results, evidence states, progress states, destructive actions, operational dashboards, reports, or any repeated state vocabulary.

Foundation owns the **meaning relationship**. Design systems and brands own exact tokens, component anatomy, and icon-library choices.

---

## Universal Contract

A meaningful state should be understandable through multiple coordinated channels:

```text
state meaning
→ explicit text label
→ recognizable icon or shape
→ semantic color/tone when the medium supports it
→ hierarchy proportional to consequence
→ attachment to the affected object or action
```

Color must not be the only carrier of essential meaning.

A full-color interface or report should normally use familiar semantic color conventions when they improve scanning. A monochrome, printed, forced-color, or constrained medium may rely more heavily on label, icon, shape, pattern, placement, and weight.

Do not require one exact HEX value, saturation, icon library, border radius, or component style across every brand and medium.

---

## Keep Status Taxonomies Separate

Several dimensions may appear together, but they are not interchangeable.

### Verdict or outcome

```text
PASS / SUCCESS
CONDITIONAL / RISK / WARNING
FAIL / ERROR
```

### Evidence state

```text
VERIFIED
NOT_VERIFIED
NOT_APPLICABLE
```

### Progress state

```text
PENDING
IN_PROGRESS
COMPLETE
```

### Severity

```text
BLOCKING
IMPORTANT
OPPORTUNITY
```

### Finding type

```text
DEFECT
EVIDENCE_GAP
FOUNDATION_LEARNING
```

### Action consequence

```text
NORMAL
DESTRUCTIVE / DANGER
```

Failure patterns:

```text
- NOT_VERIFIED is styled as WARNING even though no risk evidence exists
- FOUNDATION_LEARNING appears on the same scale as PASS or FAIL
- BLOCKING is treated as an outcome instead of finding severity
- ERROR and DESTRUCTIVE are collapsed although one describes a result and the other an action consequence
- PENDING is presented as failure
```

A component may combine dimensions, but each label must remain conceptually explicit.

---

## Conventional Semantic Mapping

Use familiar conventions as the default when color is available and no stronger domain convention applies.

| State family | Typical meaning | Familiar color family | Familiar icon family |
|---|---|---|---|
| Success / Pass / Verified | achieved, valid, confirmed | green | check, check-circle |
| Warning / Risk / Conditional | attention needed, non-fatal risk | amber or yellow with readable dark foreground | alert-triangle, exclamation |
| Error / Fail | failed, invalid, unavailable result | red | x, x-circle |
| Danger / Destructive | serious consequence or irreversible action | stronger red | alert-octagon, trash, destructive symbol |
| Information | contextual neutral information | blue | info-circle |
| Pending / In progress | work is underway or waiting | blue, indigo, or cool neutral | clock, spinner, progress symbol |
| Not verified | evidence is absent or incomplete | slate, blue-gray, or cool neutral | dashed-circle, question/evidence symbol |
| Not applicable | state does not apply | neutral gray | minus |
| Disabled / unavailable | cannot be used in the current state | low-emphasis neutral | lock, minus, unavailable symbol |

These are semantic defaults, not universal pigment mandates.

Alternative palettes can pass when:

```text
- labels and icons remain explicit
- state families remain distinguishable at a glance
- familiar danger/error conventions are not contradicted without a strong domain reason
- the mapping is stable across the product or artifact
- contrast and theme behavior remain safe
- evidence shows users are not forced to decode a private color language
```

Do not use a brand accent as a universal replacement for every state.

---

## Channel Requirements

### Text label

Use explicit language such as:

```text
✓ Pass
! Conditional
× Fail
○ Not verified
— Not applicable
```

A score alone is not a verdict. `82` does not explain whether the result is pass, conditional, blocked, or incomplete.

### Icon or shape

Use a symbol whose shape supports the meaning. The exact icon set is flexible, but the same state should not randomly switch between unrelated symbols.

Icons must not replace text when the symbol could be ambiguous. Decorative icons should be hidden from assistive technology when an adjacent text label already carries the state.

### Semantic color

Color should accelerate recognition and comparison. It should not introduce a second, contradictory meaning.

Examples:

```text
PASS              → green family
CONDITIONAL/RISK  → amber family
FAIL/BLOCKING     → red family, with blocking visually stronger than ordinary failure
NOT_VERIFIED      → cool neutral, not amber
NOT_APPLICABLE    → neutral gray
```

### Hierarchy and containment

State emphasis should match consequence.

```text
blocking/destructive > fail > warning/conditional > pass > neutral metadata
```

Not every state needs a filled card. An editorial system may use a restrained label, icon, colored rule, tinted field, or semantic foreground. The relationship must still be scannable.

### Attachment

A state must remain visibly attached to the object, action, row, field, chart, review skill, or finding it describes.

Detached badges, legends, or status labels create grouping and interpretation failures.

---

## Score and Verdict Integrity

When numerical scores are shown:

```text
score + explicit verdict + evidence coverage + blocker state
```

Rules:

```text
- score thresholds must be declared by the applicable profile or system
- a higher score must not visually erase a verified blocker
- provisional or partial-evidence scores must be labeled
- NOT_VERIFIED items are not silently treated as zero or pass
- overall score must not imply stronger evidence than the review actually contains
```

Foundation does not prescribe one universal pass threshold.

---

## Accessibility and Multi-Channel Safety

Always inspect:

```text
□ color is not the only state cue
□ label remains understandable without the icon
□ icon remains recognizable at actual size
□ foreground/background contrast is appropriate
□ red/green differences also use label, icon, shape, or placement
□ light and dark themes preserve meaning and contrast
□ grayscale or print output preserves state distinctions where required
□ forced-color/high-contrast modes do not erase the state relationship where applicable
□ text scaling and narrow layouts keep the state attached to its subject
□ dynamic state changes have applicable accessible naming/announcement behavior
```

Detailed live-region announcements, validation timing, focus movement, and interactive error recovery remain owned by the applicable interactive surface reviewer.

Disabled content must remain understandable enough to explain availability where explanation is required. Do not reduce important status text into unreadable low contrast merely because it is secondary.

---

## System and Token Ownership

Foundation requires stable semantic roles, not exact implementation values.

A design system may define tokens such as:

```text
status-success-foreground
status-success-surface
status-success-border
status-warning-foreground
status-danger-surface
status-not-verified-foreground
```

A one-off static artifact may use literal values and still pass when the state language is internally consistent.

Fail when:

```text
- the same state changes color or icon without reason
- unrelated states share one treatment and become indistinguishable
- parallel semantic token vocabularies conflict
- dark mode or export reverses or erases state meaning
- the component uses semantic colors decoratively elsewhere and weakens their signal
```

---

## Medium Adaptation

### Interactive products

Use semantic tokens and component states consistently across badges, alerts, forms, tables, toasts, dialogs, and review surfaces. Runtime behavior remains subject to interactive gates.

### Static reports and presentations

Use labels, icons, legends, rules, and restrained color so the audience can scan status from the expected distance or output size.

### Marketing and editorial surfaces

A restrained visual direction can remain mostly neutral. Semantic color may occupy a small portion of the composition while still differentiating pass, risk, fail, and evidence states.

### Monochrome or print-constrained output

Use text, icon shape, line style, pattern, weight, and placement. Do not fail solely because hue is unavailable when equivalent non-color channels preserve the meaning.

---

## Review Questions

```text
1. Which taxonomy is being encoded: verdict, evidence, progress, severity, type, or consequence?
2. Can the user identify the state without reading every supporting sentence?
3. Is the color convention familiar or explicitly explained?
4. Does the icon reinforce the state rather than decorate it?
5. Is the state attached to the correct object or action?
6. Does consequence receive proportional hierarchy?
7. Does the mapping stay stable across components, themes, viewports, and outputs?
8. Can the meaning survive without color?
9. Are score, verdict, blocker, and evidence coverage conceptually honest?
```

---

## Ownership and Handoff

```text
design-foundation
  owns universal semantic-state relationships and multi-channel encoding

design-system / brand
  owns exact color tokens, icon set, component anatomy, and visual expression

design-review
  evaluates the result through canonical gates such as G1, G3, G10, G12, H3, and R2

interactive/static/domain reviewers
  own stricter runtime, announcement, validation, destructive-action, export, and domain conventions
```

> Semantic state must be understandable through meaning, label, icon or shape, hierarchy, and color when available—not through color alone.