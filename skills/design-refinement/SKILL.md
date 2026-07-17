---
name: design-refinement
description: Targeted design improvement workflow — fix specific failing gates without full redesign. Use when design direction is correct but specific gates are failing. Faster than redesign-workflow.
license: MIT
metadata:
  ai-native-skills.version: 1.1.0
  ai-native-skills.author: puterakahfi
  ai-native-skills.type: workflow
  ai-native-skills.implements: ai-native-core/contracts/skills/quality/design-refinement.contract.yaml
  ai-native-skills.contract-version: "^1.0.0"
  ai-native-skills.related_skills: '["design-audit","design-review","redesign-workflow","master-design","ui-components","accessibility","readability","responsiveness"]'
---

# Design Refinement

Targeted gate fix loop. No full redesign. Preserves existing direction.

This is the Hermes/Agent Skills adapter for `ai-native-core/contracts/skills/quality/design-refinement.contract.yaml`. The core contract owns the runtime-agnostic phases and gates; this adapter owns concrete browser probes, patch discipline, score reporting, and handoff to `redesign-workflow` when refinement is the wrong lifecycle.

<!-- CRITICAL RULES -->
```
HARD RULES:
  1. Skill-first: patch skill before patching output
  2. Preserve: do not change what is passing (≥ 8.0)
  3. Scope: fix declared gates only — no drive-by changes
  4. After 2 failed patches on same region → write_file, never 3rd patch
```

## When to Use

Use `design-refinement` when:
- Design direction is correct (overall avg ≥ 7.0)
- Specific gates are failing (< 8.0)
- User approves direction but wants specific issues fixed

Use `redesign-workflow` instead when:
- Overall avg < 7.0 — direction itself is wrong
- Multiple CRITICAL gates (< 5.0) — foundational problems

Use `design-audit` first when:
- You don't know which gates are failing yet

---

## Parameters

| Param | Required | Description |
|---|---|---|
| `target` | YES | File path or URL of existing surface |
| `failing_gates` | YES | List of gate IDs to fix (from design-audit or prior review) |
| `preserve` | NO | Gates/elements to keep unchanged — default: all passing gates |
| `max_iterations` | NO | Default: 3 |

---

## Refinement Loop

### Step 1 — Load audit state

If `design-audit` was already run → use its gap report.  
If not → run quick audit first (8 critical gates minimum).

```
Current state:
  Overall: X.X / 10
  Failing: [gate list]
  Target gates to fix: [subset]
```

### Step 2 — Declare scope

```
REFINEMENT SCOPE
────────────────
Fixing: [gate IDs + names]
Preserving: [all other gates — do not touch]
Approach: [specific changes planned per gate]
```

### Step 3 — Skill-first fix

For each failing gate:
```
A. Identify root cause skill
B. Check if rule exists in skill
C. Patch skill (add rule / strengthen / add pitfall example)
D. Apply fix to surface derived from patched skill
E. Verify that fix: re-score the specific gate
F. Verify no regression: re-score previously passing gates
```

**HARD RULE: do not re-score gates you didn't touch unless verifying regression.**

### Step 4 — Verify

```
DOM probe (run after every fix):
  sheets > 0, overflow = false, touchFail = 0

Visual check:
  browser_vision on affected sections only

Gate re-score:
  Score fixed gates: did they improve?
  Score adjacent gates: did they regress?
```

### Step 5 — Exit

```
Exit when:
  All declared failing gates now ≥ 8.0
  OR max_iterations reached

Report:
  REFINEMENT COMPLETE — [target]
  ──────────────────────────────
  Gates fixed: [list with before→after scores]
  Gates preserved: all passing gates stable
  Skills patched: [list]
  Iterations: N

  Residual (if max reached):
    Gate [id]: [why it couldn't be fully fixed]
```

---

## Common Refinement Targets

### G21 Reduced Motion (most common CRITICAL)
```css
@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after {
    animation-duration: 0.01ms !important;
    transition-duration: 0.01ms !important;
  }
}
```

### G14 Touch Targets
```css
.element {
  min-height: 44px;
  min-width: 44px;
  display: inline-flex;
  align-items: center;
}
```

### G16 Semantic Structure
```html
<a href="#main" class="skip-link">Skip to content</a>
<nav aria-label="Main navigation">
<main id="main">
<section aria-labelledby="section-heading">
<h2 class="sr-only" id="section-heading">Section name</h2>
```

### C1 Focal Point (hero void)
```css
/* Remove min-height:100vh — causes void with sparse content */
.hero {
  padding-top: clamp(120px, 16vh, 180px);
  padding-bottom: clamp(80px, 14vh, 140px);
}
```

### R1 Type Pairing
```css
--font-display: 'Fraunces', Georgia, serif;  /* display: identity, headers */
--font-sans:    'Inter', system-ui, sans-serif; /* body: reading, UI */
```

### G2 Typographic Scale
```css
/* H1/body ratio must be ≤ 3.5x desktop, ≤ 3.0x mobile */
.hero-name { font-size: clamp(3rem, 2rem + 5vw, 5.5rem); }
/* body = 1rem (16px) → max ratio = 5.5 → FAIL */
/* fix: clamp(2.5rem, 1.5rem + 4vw, 4.5rem) → ratio 4.5x still high */
/* fix: clamp(2rem, 1.5rem + 3vw, 3.5rem) → ratio 3.5x → PASS */
```
