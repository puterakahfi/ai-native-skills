# Semantic Status Encoding Fixtures

> Cross-surface PASS/FAIL fixtures for status, severity, progress, evidence, and destructive meaning.

Load this file when evaluating whether semantic state remains understandable across visual styles, themes, media, and accessibility conditions.

## Universal fixture contract

Every applicable fixture must preserve:

```text
meaning
+ explicit label
+ recognizable symbol or shape
+ semantic visual treatment
+ sufficient contrast
+ stable cross-component usage
```

Color may reinforce meaning. Color alone may not carry essential meaning.

Exact hues, icon libraries, component anatomy, border radius, and token names belong to the design system or artifact implementation.

---

## Fixture 1 — Review scorecard

### PASS

```text
✓ Pass                 green semantic treatment
! Conditional pass     amber semantic treatment
× Fail                 red semantic treatment
○ Not verified         cool pending treatment
— Not applicable       neutral treatment
```

The score, label, and icon agree. A monochrome print or color-vision simulation still preserves the distinction through text and symbol.

### FAIL

```text
Pass               gray text
Conditional pass   gray text
Fail               gray text
Not verified       gray text
```

The user must read every word because all states have equal visual treatment.

Likely findings: `G3`, `G10`, `G12`, `H3`, `R2`.

---

## Fixture 2 — Form validation

### PASS

- valid field uses a success message and check icon only after validation is complete;
- invalid field uses an explicit error label linked to the field;
- warning explains a recoverable risk without pretending the input is invalid;
- required and optional states are not encoded only by color;
- error summary and inline error use the same semantic vocabulary.

### FAIL

- red border is the only error signal;
- success green appears before server validation completes;
- warning and error use the same icon, label, and strength;
- placeholder text carries the only instruction;
- dark theme removes the distinction between normal, warning, and error.

Likely findings: `G3`, `G10`, `G11`, `G12` plus applicable interactive gates.

---

## Fixture 3 — Alert, banner, toast, and inline message

### PASS

The same state keeps stable meaning while intensity adapts to context:

```text
inline info       restrained
page warning      visible but non-blocking
blocking error    dominant enough to interrupt safely
success toast     confirmatory, not celebratory noise
```

A warning banner does not reuse the destructive treatment. Informational blue is not used for confirmed success.

### FAIL

- every message uses the brand accent regardless of meaning;
- success, warning, and error differ only by headline wording;
- destructive red is used for ordinary information;
- a low-priority toast visually dominates the page task;
- the toast disappears before its meaning can be perceived.

Likely findings: `G3`, `G4`, `G8`, `G10`, `G12`, `R2`, `R7`.

---

## Fixture 4 — Destructive confirmation

### PASS

- destructive meaning is explicit in the verb and consequence;
- danger treatment is reserved for the destructive action;
- cancel/escape remains clearly available;
- icon and color reinforce rather than replace the wording;
- irreversible and reversible consequences are not styled identically.

### FAIL

- both cancel and delete use the same red treatment;
- a trash icon appears without a consequence label;
- ordinary validation errors use the same dominance as irreversible deletion;
- the primary destructive action is visually hidden among neutral actions.

Likely findings: `G3`, `G8`, `G10`, `G12`, `H1`, `R7` plus applicable interaction safety gates.

---

## Fixture 5 — Dashboard and operational status

### PASS

```text
Healthy        success
Degraded       warning
Down           failure
Investigating  pending/in progress
Unknown        not verified / unavailable
```

Status remains distinct in dense rows, charts, legends, filters, dark mode, and exported reports. Labels and symbols remain visible when color is removed.

### FAIL

- green means both healthy and selected;
- amber means both warning and pending with no label;
- unknown is shown as success because no error was detected;
- chart legend colors differ from table status colors;
- compact mobile rows remove the text label and retain only dots.

Likely findings: `G1`, `G3`, `G7`, `G10`, `G12`, `H3`, `R2`.

---

## Fixture 6 — Progress and pending state

### PASS

Pending or in-progress treatment communicates that work is not complete without implying danger.

```text
Queued       pending
Running      in progress
Needs review pending attention
Completed    success
Failed       failure
```

The implementation distinguishes progress from warning and distinguishes no evidence from negative evidence.

### FAIL

- all unfinished work is amber warning;
- pending is green because no error exists;
- not verified is treated as fail;
- conditional pass and in progress share one label and icon;
- progress relies on animation with no static state label.

Likely findings: `G3`, `G10`, `G12`, `H3`, `R2`.

---

## Fixture 7 — Evidence and verification

### PASS

```text
Verified        evidence exists and supports the claim
Not verified    required evidence is missing
Not applicable  condition does not apply
Failed          evidence exists and shows failure
```

The review does not convert missing evidence into pass, warning, or failure. Each state has a distinct label and visual treatment.

### FAIL

- not verified uses the same red failure treatment;
- not applicable is hidden;
- source inspection is displayed as rendered verification;
- an empty evidence list produces a green overall status;
- evidence coverage is shown without naming open conditions.

Likely findings: `G3`, `G10`, `G12`, `H3` and review-profile evidence gates.

---

## Fixture 8 — Static report and presentation

### PASS

A PDF, slide, poster, or executive report uses semantic state sparingly but clearly. Meaning survives grayscale printing, projector contrast loss, screenshot compression, and small-scale viewing.

### FAIL

- status is communicated only by pale background color;
- red/green dots have no labels;
- saturated status colors overpower the actual narrative hierarchy;
- decorative brand color is mistaken for a status color;
- small legends require zoom to decode.

Likely findings: `G3`, `G8`, `G10`, `G11`, `G12`, `R2`, `R7`.

---

## Fixture 9 — Light and dark themes

### PASS

- semantic meaning remains stable across themes;
- contrast is verified independently in each theme;
- dark mode does not turn all states into equally bright neon accents;
- tinted surfaces preserve text and icon legibility;
- selected, focused, hovered, and status states remain distinguishable.

### FAIL

- success green becomes indistinguishable from the brand accent;
- warning loses contrast on a warm dark surface;
- danger is visible only through a border that disappears in dark mode;
- status colors pass in light theme but bloom or vibrate in dark theme;
- theme changes alter the meaning of a hue.

Likely findings: `G1`, `G3`, `G4`, `G10`, `R2`.

---

## Fixture 10 — Color-vision and non-color checks

### PASS

Run applicable checks:

```text
remove color
simulate common color-vision differences
inspect at actual size
inspect low contrast / dim display
inspect print or screenshot compression
```

The state remains understandable through label, icon/shape, placement, and hierarchy.

### FAIL

- success and error are identical after hue removal;
- check and x icons are decorative and hidden from relevant assistive semantics while no text exists;
- icon shape changes but labels remain ambiguous;
- color names such as “green state” are used as the only instruction.

Likely findings: `G3`, `G10`, `G11`, `G12`, `H3` plus applicable accessibility gates.

---

## Regression matrix

| Surface | Required distinctions |
|---|---|
| Review result | pass, conditional, fail, not verified, not applicable, severity |
| Form | valid, warning, invalid, required, disabled |
| Toast/banner | info, success, warning, error, blocking |
| Dashboard | healthy, degraded, down, pending, unknown |
| Workflow | queued, running, review, completed, failed |
| Destructive dialog | neutral choice, cancel, destructive action, consequence |
| Static report | result, risk, failure, evidence gap |
| Light/dark theme | stable meaning and sufficient contrast |

A fixture passes only when semantic meaning remains stable without forcing one visual style or one fixed palette.
