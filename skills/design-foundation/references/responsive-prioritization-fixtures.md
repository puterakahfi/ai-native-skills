# Responsive Prioritization Regression Fixtures

> PASS/FAIL fixtures for deciding what must remain, adapt, defer, or disappear when viewport and available attention shrink. These fixtures test preservation of meaning and task priority, not desktop visual parity.

## Classification Before Adaptation

Classify each candidate element before changing visibility:

```text
ESSENTIAL
  primary message, required information, status, evidence, instruction,
  orientation, distinguishing identity, or next valid action

SUPPORTING
  useful context that may wrap, summarize, disclose, reorder, or substitute

REDUNDANT
  repeats meaning already carried clearly by another channel

DECORATIVE
  atmosphere, texture, ornament, or non-informational illustration
```

Hiding is acceptable only when the surviving composition preserves complete meaning and leaves no structural residue.

---

## 1. Landing-Page Hero

### PASS

```text
- headline, explanation, primary CTA, and identity metadata remain visible
- desktop illustration is hidden below the viewport where its detail becomes unreadable
- the illustration carries no unique information beyond the adjacent copy
- removing it closes the layout naturally without an empty reserved column or gap
- desktop retains the illustration where it contributes useful atmosphere and balance
```

### FAIL

```text
- decorative visual remains on mobile and pushes the primary CTA far below the opening message
- visual detail becomes noise after shrinking but is preserved only for desktop parity
- illustration is hidden even though it contains the only explanation of system relationships
- hidden visual leaves an empty container, excessive gap, detached label, or false loading region
```

---

## 2. Dashboard and Operational Surface

### PASS

```text
- decorative chart texture or redundant sparkline may disappear
- current status, value, comparison basis, alert severity, and action remain
- secondary detail moves into disclosure or a dedicated detail view
- removed columns have an intentional priority rule shared by the table family
```

### FAIL

```text
- status or alert evidence disappears because the mobile layout is difficult
- only color remains after labels or values are hidden
- the sole comparison baseline is removed, changing the interpretation of the metric
- every dashboard instance uses a different local hide rule
```

---

## 3. Navigation and Controls

### PASS

```text
- lower-priority actions move into an overflow menu before controls wrap chaotically
- active state, navigation context, and primary task remain discoverable
- desktop tabs substitute into a fitting mobile pattern while preserving selection
```

### FAIL

```text
- navigation items are hidden with no discoverable route
- pattern substitution resets selection or changes the task meaning
- labels disappear and leave ambiguous icon-only actions without accessible names
```

---

## 4. Marketing Proof and Evidence

### PASS

```text
- decorative logos or repeated proof may be reduced when enough verified proof remains
- unique case-study result, disclaimer, evidence state, and source remain available
- dense proof detail may summarize with a clear path to the full evidence
```

### FAIL

```text
- inconvenient evidence is hidden while promotional claims remain
- disclaimers or qualification context disappear on small screens
- proof count is reduced until the claim becomes misleading
```

---

## 5. Informational Diagram

### PASS

```text
- complex diagram substitutes into a concise text summary plus optional disclosure
- unique relationships remain understandable without requiring the desktop canvas
- labels and reading order remain coherent in the alternate form
```

### FAIL

```text
- diagram is classified as decoration solely because it is visual
- unique architecture, process, or dependency meaning disappears
- the mobile replacement is a thumbnail whose labels are impossible to read
```

---

## Anti-Bias Checks

```text
PASS: minimalist mobile hero with no illustration because copy carries the complete message
PASS: dense mobile dashboard that retains critical status while deferring secondary detail
PASS: expressive mobile creative that keeps imagery because imagery is the primary message

FAIL: hide every image on mobile
FAIL: preserve every desktop element at reduced scale
FAIL: call an element decorative without checking whether it carries unique meaning
FAIL: remove difficult content instead of adapting the component or disclosure path
```

## Expected Review Output

```text
element classification: essential | supporting | redundant | decorative
mobile strategy: preserve | recompose | summarize | disclose | substitute | omit/defer
surviving meaning: complete | incomplete
structural residue after omission: none | present
canonical findings: existing gate IDs only
required specialist handoffs: [...]
```
