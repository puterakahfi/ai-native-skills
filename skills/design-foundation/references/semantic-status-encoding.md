# Semantic Status Encoding

> Semantic color is not decoration when it communicates outcome, risk, evidence, progress, availability, maturity, or consequence.

Load this reference when an artifact contains status badges, alerts, validation, scorecards, review results, evidence states, progress states, destructive actions, operational health, or repeated state vocabulary.

Foundation owns the **meaning relationship**. Design systems and brands own exact tokens, component anatomy, and icon-library choices.

---

## Universal Contract

A meaningful state should remain understandable through coordinated channels:

```text
state meaning
→ explicit text label
→ recognizable icon or shape
→ semantic color/tone when the medium supports it
→ hierarchy proportional to consequence
→ visible attachment to the affected object or action
```

Color must not be the only carrier of essential meaning.

A monochrome, printed, forced-color, or otherwise constrained medium may rely more heavily on label, icon, shape, pattern, placement, and weight. Do not require one exact HEX value, icon library, radius, or component style across every brand and medium.

---

## Keep Taxonomies Separate

Several dimensions may appear together, but they are not interchangeable.

```text
VERDICT / OUTCOME
PASS | CONDITIONAL | FAIL

EVIDENCE
VERIFIED | NOT_VERIFIED | NOT_APPLICABLE

PROGRESS / MATURITY
PENDING | IN_PROGRESS | COMPLETE

SEVERITY
BLOCKING | IMPORTANT | OPPORTUNITY

FINDING TYPE
DEFECT | EVIDENCE_GAP | FOUNDATION_LEARNING

ACTION CONSEQUENCE
NORMAL | DESTRUCTIVE
```

Failure patterns:

```text
- NOT_VERIFIED is styled as WARNING although no risk evidence exists
- PENDING is presented as failure
- FOUNDATION_LEARNING competes visually with PASS or FAIL
- BLOCKING is treated as an outcome instead of finding severity
- ERROR and DESTRUCTIVE collapse although one describes a result and one an action
```

A component may combine dimensions, but each label must remain conceptually explicit.

---

## Conventional Semantic Mapping

Use familiar conventions by default when color is available and no stronger domain convention applies.

| State family | Typical meaning | Familiar color family | Familiar icon family |
|---|---|---|---|
| Success / Pass / Verified | achieved, valid, confirmed | green | check, check-circle |
| Warning / Risk / Conditional | attention needed, non-fatal risk | amber/yellow with readable foreground | alert-triangle, exclamation |
| Error / Fail | failed, invalid, unavailable result | red | x, x-circle |
| Danger / Destructive | serious or irreversible consequence | stronger red | alert-octagon, trash, danger symbol |
| Information | contextual neutral information | blue/cyan | info-circle |
| Pending / In progress | waiting or work underway | blue, indigo, or cool neutral | clock, spinner, progress symbol |
| Not verified | evidence absent or incomplete | slate, blue-gray, or cool neutral | dashed-circle, question/evidence symbol |
| Not applicable | condition does not apply | neutral gray | minus |
| Disabled / unavailable | cannot be used in the current state | low-emphasis neutral | lock, unavailable symbol |

These are semantic defaults, not fixed pigment mandates.

Alternative palettes can pass when:

```text
- labels and icons remain explicit
- state families remain distinguishable at a glance
- familiar danger/error conventions are not contradicted without a strong domain reason
- mapping remains stable across the product or artifact
- contrast and theme behavior remain safe
- users are not forced to decode a private color language
```

Do not use a brand accent as a universal replacement for every state.

---

## Channel Requirements

### Explicit label

Use direct language such as:

```text
✓ Pass
! Conditional
× Fail
○ Not verified
— Not applicable
```

A score alone is not a verdict. `82` does not explain whether the result passed, is conditional, is blocked, or lacks evidence.

### Recognizable symbol

The exact icon set is flexible, but the same state should not randomly switch between unrelated symbols. Icons must not replace text when the symbol could be ambiguous. Decorative icons should be hidden from assistive technology when adjacent text already carries the meaning.

### Semantic color

Color should accelerate recognition and comparison without creating a contradictory meaning.

```text
PASS / VERIFIED      → success family
CONDITIONAL / RISK   → warning family
FAIL / ERROR         → failure family
BLOCKING / DANGER    → stronger failure treatment proportional to consequence
PENDING / IN PROGRESS→ cool progress family, not warning
NOT_VERIFIED         → cool evidence-gap family, not failure
NOT_APPLICABLE       → neutral family
```

### Hierarchy

State emphasis should match consequence:

```text
blocking/destructive > fail > warning/conditional > pass > neutral metadata
```

Not every state needs a filled card. A restrained editorial system may use a label, icon, colored rule, tinted field, or semantic foreground. The relationship must still be scannable.

### Attachment

A state must remain visibly attached to the field, row, product, review skill, evidence condition, finding, action, or system it describes. Detached badges or legends create grouping and interpretation failures.

---

## Score and Verdict Integrity

When numerical scores are shown:

```text
score + explicit verdict + evidence coverage + blocker state
```

Rules:

```text
- thresholds are declared by the applicable profile or system
- a high score does not erase a verified blocker
- provisional or partial-evidence scores are labeled
- NOT_VERIFIED items are not silently treated as zero or pass
- overall score does not imply stronger evidence than the review contains
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
□ red/green differences also use label, shape, icon, or placement
□ light and dark themes preserve meaning and contrast
□ grayscale/print preserves distinctions where required
□ forced-color/high-contrast modes do not erase meaning where applicable
□ narrow layouts and text scaling keep state attached to its subject
□ dynamic state changes have applicable accessible naming/announcement behavior
```

Detailed live-region announcements, validation timing, focus movement, and interactive recovery remain owned by the applicable interactive reviewer.

---

## System and Token Ownership

Foundation requires stable semantic roles, not exact implementation values.

A design system may define tokens such as:

```text
status-success-foreground
status-success-surface
status-warning-foreground
status-danger-surface
status-pending-foreground
status-not-verified-foreground
```

A one-off static artifact may use literal values and still pass when the language is internally consistent.

Fail when:

```text
- the same state changes color or icon without reason
- unrelated states share one treatment and become indistinguishable
- parallel semantic token vocabularies conflict
- dark mode or export reverses or erases meaning
- semantic colors are reused decoratively until their signal weakens
```

---

## Medium Adaptation

### Interactive products
Use semantic tokens consistently across badges, alerts, forms, tables, toasts, dialogs, and review surfaces. Runtime behavior remains subject to interactive gates.

### Static reports and presentations
Use labels, icons, legends, rules, and restrained color so status can be scanned at expected distance and output size.

### Marketing and editorial surfaces
A restrained direction may remain mostly neutral. Semantic color can occupy a small portion while still differentiating pass, risk, fail, progress, and evidence.

### Monochrome or print-constrained output
Use label, icon shape, line style, pattern, weight, and placement. Do not fail solely because hue is unavailable when equivalent non-color channels preserve meaning.

---

## Review Questions

```text
1. Which taxonomy is encoded: verdict, evidence, progress, severity, type, or consequence?
2. Can the state be identified without reading every supporting sentence?
3. Is the color convention familiar or explicitly explained?
4. Does the icon reinforce meaning rather than decorate it?
5. Is the state attached to the correct object or action?
6. Does consequence receive proportional hierarchy?
7. Does mapping remain stable across components, themes, viewports, and outputs?
8. Can the meaning survive without color?
9. Are score, verdict, blocker, and evidence coverage conceptually honest?
```

Canonical reporting normally uses `G1`, `G3`, `G10`, `G12`, `H3`, and `R2`, plus applicable interactive/static/domain gates.

---

## Ownership and Handoff

```text
design-foundation
  owns universal semantic-state relationships and multi-channel encoding

design-system / brand
  owns exact tokens, icon set, component anatomy, and expression

design-review
  evaluates evidence through canonical gates

interactive/static/domain reviewers
  own stricter runtime, announcement, validation, destructive-action,
  export, and domain conventions
```

> Semantic state must be understandable through meaning, label, icon or shape, hierarchy, and color when available—not through color alone.
