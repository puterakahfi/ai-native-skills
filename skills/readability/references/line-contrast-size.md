# Readability Reference: Line Length · Contrast · Type Size

> Covers Dimensions 1–3. See `rhythm-density-ease.md` for D4–D6.

---

## Dimension 1: Line Length

**Optimal range: 45–75 characters per line (CPL)**

```
< 35 CPL  — too narrow, eye jumps too frequently     → Score: 3–5
35–45 CPL — slightly narrow, acceptable for UI       → Score: 6–7
45–65 CPL — optimal for prose and body text          → Score: 10
65–75 CPL — acceptable, slightly wide                → Score: 8–9
75–90 CPL — too wide, reader loses line tracking     → Score: 4–6
> 90 CPL  — fails readability — must fix             → Score: 0–3
```

**How to enforce:**
```css
/* Body text — optimal reading column */
p, .body-text {
  max-width: 65ch;   /* ch = width of '0' character */
}

/* Lead text — slightly wider allowed */
.lead {
  max-width: 75ch;
}

/* Hero / display — not prose, width constraint less critical */
h1, .display {
  max-width: 20ch;   /* limits line breaks in large type */
}
```

> **HARD RULE:** Hero bio / short display copy → `max-width: 44ch` (ch units ONLY — px exceeds CPL at large viewport).

**Scoring CPL for a given design:**
```
Measure: count characters in the longest comfortable line of body text
Tool: in browser DevTools → pick element → check computed width / font-size
Quick check: if body text spans full 1200px container → FAIL (score 2)
```

---

## Dimension 2: Contrast Ratio

**WCAG 2.1 levels:**

```
AA minimum (required):
  Normal text (< 18pt / < 14pt bold): ≥ 4.5:1
  Large text (≥ 18pt / ≥ 14pt bold): ≥ 3:1
  UI components, icons:               ≥ 3:1

AAA (enhanced):
  Normal text: ≥ 7:1
  Large text:  ≥ 4.5:1
```

**Scoring by ratio:**
```
< 3.0:1   → Score: 0  — invisible, fails everything
3.0–4.4:1 → Score: 5  — passes large text only
4.5–6.9:1 → Score: 8  — passes AA normal text
7.0–10:1  → Score: 10 — passes AAA
> 10:1    → Score: 9  — can feel harsh/aggressive

Dark theme common values:
  #0c0c0c bg + #f0f0f0 text = 17.5:1  → Score: 9 (slightly harsh)
  #0c0c0c bg + #a0a0a0 text = 7.0:1   → Score: 10 (secondary text)
  #0c0c0c bg + #555555 text = 3.1:1   → Score: 5 (tertiary — large text only)
```

**Contrast checking tools:**
```
CSS:         color-contrast() function (Chrome 111+)
JS:          manual calculation from RGB channels
Online:      https://webaim.org/resources/contrastchecker/
Quick rule:  #0c0c0c bg → use #6b6b6b or lighter for body text minimum
```

> **HARD RULE:** Primary text contrast ≥ 4.5:1 · Secondary text contrast ≥ 3:1

---

## Dimension 3: Type Size

**Minimum sizes by context:**

```
Context                   Minimum size    Recommended
───────────────────────────────────────────────────────
Mobile body text          16px (1rem)     16–18px
Desktop body text         15px (0.94rem)  16–18px
Captions, meta            12px (0.75rem)  13–14px
Tags, badges (mono)        9px (0.56rem)  10–11px (ALL CAPS only)
Labels above inputs       13px (0.81rem)  14px
Button text               14px (0.875rem) 15–16px
Nav links                 13px (0.81rem)  13–14px
Footer, legal             11px (0.69rem)  12px
```

**Scoring:**
```
Body text ≥ 16px                            → Score: 10
Body text 14–15px                           → Score: 7
Body text 12–13px                           → Score: 4
Body text < 12px                            → Score: 0 (hard fail)

Secondary text ≥ 12px                       → Score: 10
Secondary text 10–11px (not prose)          → Score: 7
Secondary text < 10px                       → Score: 3

Mobile: any interactive text < 16px         → automatic -2 penalty
```

> **HARD RULE:** Body font-size ≥ 16px · Smallest element ≥ 12px
