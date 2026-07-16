---
name: readability
description: Text readability scoring and optimization — line length, contrast ratio, type size, line height, density, and cognitive ease. Produces a readability score 0–10 per dimension. Minimum score 8 required before design passes.
license: MIT
metadata:
  ai-native-skills.version: 1.0.0
  ai-native-skills.author: puterakahfi
  ai-native-skills.type: skill
  ai-native-skills.implements: ai-native-core/contracts/skills/experience-design/readability.contract.yaml
  ai-native-skills.related_skills: '[''design-system'', ''accessibility'', ''ux-psychology'', ''master-design'']'
---

# Readability Skill

## Core Principle

```
Readability is not aesthetic — it is functional.
If text requires effort to read, it will not be read.

Readability has 6 measurable dimensions:
  1. Line length    — how many characters per line
  2. Contrast ratio — foreground vs background
  3. Type size      — minimum sizes for different contexts
  4. Line height    — space between lines
  5. Density        — information per viewport area
  6. Cognitive ease — vocabulary and sentence complexity

Each dimension scored 0–10. Minimum 8 to pass.
Overall readability score = average of 6 dimensions.
```

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

---

## Dimension 4: Line Height (Leading)

**Optimal range by text size:**

```
Display (≥ 3xl, ≥ 50px):  1.0–1.15   — tighter, less gap
Headings (xl–2xl):        1.2–1.35   — snug but separated
Body text:                1.5–1.75   — optimal for prose
Small UI labels:          1.3–1.4    — not prose, just labels
Captions:                 1.4–1.6    — slightly relaxed
```

**Scoring:**
```
Body line-height:
  < 1.3    → Score: 3  — claustrophobic, hard to track
  1.3–1.45 → Score: 6  — acceptable for UI labels
  1.5–1.65 → Score: 10 — optimal reading
  1.65–1.8 → Score: 9  — slightly loose but good for long-form
  > 1.9    → Score: 5  — too airy, paragraphs feel disconnected

Heading line-height:
  < 1.0    → Score: 4  — descenders collide
  1.0–1.15 → Score: 10 — tight, correct for display
  1.2–1.35 → Score: 9  — snug, correct for sub-headings
  > 1.5    → Score: 5  — headings feel like body text
```

---

## Dimension 5: Density

**Dead space vs Breathing Room — NOT the same:**

```
Dead space (FAIL):
  - Void with no visual purpose above hero focal point
  - Eye enters void first, searches for anchor, fatigues
  - Caused by: justify-content:flex-end on 100vh hero

Breathing room (PASS):
  - Intentional whitespace BETWEEN sections
  - Lives between sections, NEVER before first hero content
  - Has rhythm: multiples of 8px base unit
```



**Information density scoring:**

```
Too sparse:
  > 60% of viewport is empty space above the fold
  Each sentence is its own paragraph
  → Score: 4–5 (not scannable, feels unfinished)

Optimal:
  25–50% whitespace ratio in content sections
  3–5 meaningful elements visible above fold
  Content grouped, not scattered
  → Score: 8–10

Too dense:
  < 15% whitespace in content area
  6+ distinct elements competing for attention
  Walls of text with no breaks
  → Score: 3–5

How to measure density quickly:
  Squint at the page. Can you identify 3 distinct zones?
  If everything blurs together → too dense
  If you see mostly grey space → too sparse
```

**Density scoring by section:**
```
Hero section:      optimal = 30–50% content, 50–70% space  (breathing room)
Work/projects:     optimal = 60–70% content, 30–40% space  (content priority)
About section:     optimal = 55–65% content, 35–45% space  (balanced)
Contact section:   optimal = 20–35% content, 65–80% space  (minimal, closing)
```

---

## Dimension 6: Cognitive Ease

**Vocabulary and sentence complexity:**

```
Flesch-Kincaid Grade Level target: ≤ 8 (US 8th grade)
Hemingway Editor score:            ≤ 10

Rules:
  - Sentences: ≤ 20 words average
  - Paragraphs: ≤ 4 sentences
  - Avoid passive voice (> 10% = issue)
  - No jargon without explanation on first use
  - No nested subordinate clauses in hero copy
```

**Scoring by copy type:**
```
Hero H1:
  One clear idea, ≤ 8 words           → Score: 10
  Two ideas, 8–14 words               → Score: 7
  Three ideas or > 14 words           → Score: 4

Body paragraph:
  ≤ 3 sentences, concrete language    → Score: 10
  4–5 sentences, some abstraction     → Score: 7
  Long, abstract, jargon-heavy        → Score: 3

About section:
  First-person, specific, no buzzwords → Score: 10
  Generic ("passionate", "dynamic")    → Score: 4
```

---

## Readability Scoring Rubric

Run for every design before delivery:

```
READABILITY AUDIT — [page name]
────────────────────────────────────────────────
Dimension 1: Line Length
  Body text CPL: ____ chars
  Score: __ / 10

Dimension 2: Contrast Ratio
  Primary text:   ___:1  → Score: __ / 10
  Secondary text: ___:1  → Score: __ / 10
  Average: __ / 10

Dimension 3: Type Size
  Body text: ____px
  Smallest text: ____px (context: ____)
  Score: __ / 10

Dimension 4: Line Height
  Body leading: ____
  Heading leading: ____
  Score: __ / 10

Dimension 5: Density
  Hero whitespace ratio: ____%
  Content section ratio: ____%
  Score: __ / 10

Dimension 6: Cognitive Ease
  Hero H1 word count: ____
  Body avg sentence length: ____
  Score: __ / 10

────────────────────────────────────────────────
TOTAL SCORE: __ / 10  (average of 6 dimensions)
STATUS: PASS (≥ 8.0) | FAIL (< 8.0)

Failing dimensions:
  [list each < 8 with specific fix]
────────────────────────────────────────────────
```

---

## Common Readability Fixes

| Problem | Score Impact | Fix |
|---|---|---|
| Full-width prose (> 90 CPL) | D1: -6 | Add `max-width: 65ch` to prose |
| Low contrast secondary text | D2: -4 | Lighten to ≥ 4.5:1 ratio |
| Body text 13px | D3: -4 | Increase to 16px minimum |
| line-height: 1.2 on body | D4: -4 | Increase to 1.6 |
| Hero 80% empty | D5: -3 | Add second content element or reduce padding |
| "passionate developer who loves building scalable solutions" | D6: -6 | Rewrite: specific, concrete, first-person |
| Walls of text, no paragraph breaks | D5+D6: -4 | Break into ≤ 4 sentence paragraphs |
| Font-weight: 300 on body | D3: -2 | Use 400 minimum for body |
