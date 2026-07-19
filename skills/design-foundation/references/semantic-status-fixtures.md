# Semantic Status Encoding Fixtures

> Cross-surface PASS/FAIL fixtures for verdict, evidence, progress, severity, availability, and destructive meaning.

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

Exact hues, icon libraries, component anatomy, radius, and token names belong to the design system or artifact implementation.

---

## 1. Review scorecard

### PASS

```text
✓ Pass                 success treatment
! Conditional pass     warning treatment
× Fail                 failure treatment
○ Not verified         cool evidence-gap treatment
— Not applicable       neutral treatment
```

Score, label, icon, and evidence state agree. Grayscale or color-vision simulation still preserves the distinctions.

### FAIL

Pass, conditional, fail, and not verified all use equal gray text. The user must read every word because the system supplies no scanning cue.

Likely findings: `G3`, `G10`, `G12`, `H3`, `R2`.

---

## 2. Form validation

### PASS

- valid field uses an affirmative label and check after validation completes;
- invalid field uses an explicit error linked to the field;
- warning explains a recoverable risk without pretending the input is invalid;
- required/optional meaning is not color-only;
- error summary and inline error use one semantic vocabulary.

### FAIL

- red border is the only error signal;
- green appears before validation completes;
- warning and error use the same icon, label, and strength;
- placeholder carries the only instruction;
- dark mode removes the distinction between normal, warning, and error.

Likely findings: `G3`, `G10`, `G11`, `G12` plus applicable interactive gates.

---

## 3. Alert, banner, toast, and inline message

### PASS

```text
inline information  restrained
page warning        visible but non-blocking
blocking error      dominant enough to interrupt safely
success toast       confirmatory, not celebratory noise
```

Warning does not reuse destructive treatment. Informational blue is not used for confirmed success.

### FAIL

- every message uses brand accent regardless of meaning;
- success, warning, and error differ only by wording;
- destructive red is used for ordinary information;
- low-priority toast dominates the primary task;
- state disappears before it can be perceived.

Likely findings: `G3`, `G4`, `G8`, `G10`, `G12`, `R2`, `R7`.

---

## 4. Destructive confirmation

### PASS

- destructive meaning is explicit in the verb and consequence;
- danger treatment is reserved for the destructive action;
- cancel/escape remains clearly available;
- icon and color reinforce rather than replace wording;
- irreversible and reversible consequences are not styled identically.

### FAIL

- cancel and delete both use red;
- trash icon appears without consequence wording;
- ordinary validation error uses the same dominance as irreversible deletion;
- destructive action is hidden among neutral actions.

Likely findings: `G3`, `G8`, `G10`, `G12`, `H1`, `R7` plus interaction safety gates.

---

## 5. Dashboard and operational health

### PASS

```text
Healthy        success
Degraded       warning
Down           failure
Investigating  pending/in progress
Unknown        not verified/unavailable
```

Status remains distinct in dense rows, charts, legends, filters, mobile views, dark mode, and exported reports. Labels and symbols remain visible when color is removed.

### FAIL

- green means both healthy and selected;
- amber means both warning and pending without labels;
- unknown becomes success because no error was detected;
- chart legend and table use conflicting mappings;
- mobile removes labels and retains only colored dots.

Likely findings: `G1`, `G3`, `G7`, `G10`, `G12`, `H3`, `R2`.

---

## 6. Progress and maturity

### PASS

Pending or in-progress communicates incomplete work without implying danger.

```text
Queued        pending
Running       in progress
Needs review  pending attention
Completed     success
Failed        failure
```

Progress remains distinct from warning. Missing evidence remains distinct from negative evidence.

### FAIL

- all unfinished work is amber warning;
- pending is green because no error exists;
- not verified is treated as fail;
- conditional pass and in progress share one label and icon;
- progress relies on animation without a static label.

Likely findings: `G3`, `G10`, `G12`, `H3`, `R2`.

---

## 7. Evidence and verification

### PASS

```text
Verified        evidence exists and supports the claim
Not verified    required evidence is missing
Not applicable  condition does not apply
Failed          evidence exists and shows failure
```

The review does not convert missing evidence into pass, warning, or failure.

### FAIL

- not verified uses red failure treatment;
- not applicable is hidden;
- source inspection is displayed as rendered verification;
- empty evidence produces a green overall status;
- coverage is shown without naming open conditions.

Likely findings: `G3`, `G10`, `G12`, `H3` and review-profile evidence gates.

---

## 8. Static report and presentation

### PASS

A PDF, slide, poster, or executive report uses semantic state sparingly but clearly. Meaning survives grayscale printing, projector contrast loss, screenshot compression, and small-scale viewing.

### FAIL

- status is communicated only by pale background color;
- red/green dots have no labels;
- saturated colors overpower narrative hierarchy;
- decorative brand color is mistaken for status;
- small legends require zoom.

Likely findings: `G3`, `G8`, `G10`, `G11`, `G12`, `R2`, `R7`.

---

## 9. Light and dark themes

### PASS

- meaning remains stable across themes;
- contrast is verified independently;
- dark mode does not turn all states into equally bright neon;
- tinted surfaces preserve text/icon legibility;
- selected, focused, hovered, and status states remain distinguishable.

### FAIL

- success becomes indistinguishable from brand accent;
- warning loses contrast on warm dark surface;
- danger depends on a border that disappears;
- colors pass in light but bloom or vibrate in dark;
- theme changes alter hue meaning.

Likely findings: `G1`, `G3`, `G4`, `G10`, `R2`.

---

## 10. Color-vision and non-color checks

### PASS

Run applicable checks:

```text
remove color
simulate common color-vision differences
inspect at actual size
inspect low-contrast/dim display
inspect print or screenshot compression
```

State remains understandable through label, symbol, placement, and hierarchy.

### FAIL

- success and error become identical after hue removal;
- icons are decorative while no text exists;
- icon changes but label remains ambiguous;
- instructions refer only to “green state” or “red item.”

Likely findings: `G3`, `G10`, `G11`, `G12`, `H3` plus accessibility gates.

---

## Regression Matrix

| Surface | Required distinctions |
|---|---|
| Review result | pass, conditional, fail, not verified, not applicable, severity |
| Form | valid, warning, invalid, required, disabled |
| Toast/banner | information, success, warning, error, blocking |
| Dashboard | healthy, degraded, down, pending, unknown |
| Workflow | queued, running, review, completed, failed |
| Destructive dialog | neutral, cancel, destructive action, consequence |
| Static report | result, risk, failure, evidence gap |
| Light/dark | stable meaning and sufficient contrast |

A fixture passes only when semantic meaning remains stable without forcing one visual style or fixed palette.
