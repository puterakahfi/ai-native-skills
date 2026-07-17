# Readability Reference: Line Height · Density · Cognitive Ease

> Covers Dimensions 4–6. See `line-contrast-size.md` for D1–D3.

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
