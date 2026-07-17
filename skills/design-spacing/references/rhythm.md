# Visual Rhythm & Section Spacing

> Rhythm = consistent vertical cadence. Eye should flow without interruption.

## Section Spacing Scale

```
SECTION-TO-SECTION (largest unit):
  Comfortable: clamp(80px, 10vh, 120px)   — standard sections
  Generous:    clamp(100px, 14vh, 160px)  — hero to first section
  Dramatic:    clamp(120px, 18vh, 200px)  — zen/atmospheric (Ma)

COMPONENT-TO-COMPONENT (medium unit):
  Tight:   24–32px  — related items (form fields, list items)
  Normal:  40–48px  — sibling components
  Loose:   64–80px  — distinct components

ELEMENT-TO-ELEMENT (smallest unit):
  Inline:  4–8px   — icon + label, badge + text
  Stack:   12–16px — label + input, heading + subheading
  Cluster: 20–24px — card padding, button padding
```

## Rhythm Rules

```
RULE 1 — More space ABOVE than below headings
  h2 margin-top: 2em   margin-bottom: 0.5em  ← enters new section
  h3 margin-top: 1.5em margin-bottom: 0.4em

RULE 2 — Consistent section rhythm
  All sections same spacing scale — pick one and stick to it
  Exception: hero gets 1.5× standard (it's the entry point)

RULE 3 — Vertical rhythm from line-height
  Base unit = 1rem line-height (16px)
  All spacing = multiples of this unit: 8px, 16px, 24px, 32px...
  Matches 8px grid from design-system ✓

RULE 4 — Tighter inside, looser outside
  Internal component padding < gap between components
  Components breathe more than their contents
```

## Anti-Patterns

```
❌ Equal spacing everywhere → no hierarchy, no rhythm
❌ Random spacing values → visual noise, amateur feel
❌ Large section spacing + small component spacing only → disconnected
❌ Hero same spacing as body sections → no entry point signal
✅ Graduated spacing: section > component > element
✅ Hero 1.5–2× standard section spacing
```
