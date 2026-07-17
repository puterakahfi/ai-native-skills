# Readability Reference: Scoring Rubric & Common Fixes

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
