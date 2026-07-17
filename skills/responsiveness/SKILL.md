---
name: responsiveness
description: Responsive design strategy — breakpoint system, fluid grid, fluid typography, touch targets, viewport adaptation, and performance. Scores responsiveness 0–10 per dimension. Minimum score 8 required to pass.
license: MIT
metadata:
  ai-native-skills.version: 1.0.0
  ai-native-skills.author: puterakahfi
  ai-native-skills.type: skill
  ai-native-skills.implements: ai-native-core/contracts/skills/design/responsiveness.contract.yaml
  ai-native-skills.related_skills: '["design-system", "ux-ui-patterns", "accessibility", "readability"]'
---

# Responsiveness Skill

## HARD RULES (always enforced)

```
❌ NO min-height:100vh on hero — causes void at tall viewports.
   ✅ Use padding-top: clamp(120px, 16vh, 180px) instead.

❌ NO unconstrained full-width sections at wide viewports.
   ✅ max-width: min(1200px, 90vw) — mandatory container on ALL sections.

✅ Mobile-first: start with 1-col layout, add breakpoints only when content breaks.
   Never subtract from desktop to make mobile.
```

---

## Core Principle

```
Responsive design is not "make it work on mobile."
It is designing for every viewport as a first-class experience.

Mobile first:
  Start with the smallest viewport.
  Add complexity as viewport grows.
  Never subtract from desktop to make mobile.

Three layers:
  1. Fluid grid   — layout adapts
  2. Fluid type   — text scales
  3. Fluid space  — spacing scales

All three must work together.
```

---

## Reference Files

| Topic | File | Contents |
|---|---|---|
| Wide & Ultrawide Breakpoints | references/wide-breakpoints.md | Wide/ultrawide failure modes, max-width container, hero void fix, common violations, standard breakpoints |
| Fluid Grid & Typography | references/fluid-grid-type.md | Grid progression, column decisions, auto-grid, clamp() type scale, H1/body ratio gate |
| Touch Targets & Viewport | references/touch-viewport.md | Touch target rules + CSS fixes, navigation/hero/card checklist, scoring rubric, common failures table |

---

## Quick Decision Guide

```
Starting a new design?
  1. Mobile-first: default styles = smallest viewport (0–639px), 1-col, stacked
  2. Add min-width breakpoints at content break points (not device sizes)
  3. Constrain with max-width: min(1200px, 90vw) on every section
  4. Use clamp() for type and spacing — never fixed px for visual scale
  5. Verify touch targets ≥ 44×44px on all interactive elements

Auditing existing design?
  → Load references/touch-viewport.md for the full scoring rubric
  → Minimum score: 8.0 / 10 to pass
```

---

## HARD RULES (bottom — same as top, enforced again)

```
❌ NO min-height:100vh on hero — use clamp() padding instead.
✅ max-width: min(1200px, 90vw) — mandatory container on all sections.
✅ Mobile-first: start with 1-col, add breakpoints only when content breaks.
```
