---
name: motion-design
description: Motion design system — micro-interactions, state transitions, scroll-driven animation, staggered entrance, and cinematic narrative motion. Decision tree for choosing the right motion type. Scores motion quality 0–10. Minimum 8 to pass. Always respects prefers-reduced-motion.
license: MIT
metadata:
  ai-native-skills.version: 1.0.0
  ai-native-skills.author: puterakahfi
  ai-native-skills.type: skill
  ai-native-skills.implements: ai-native-core/contracts/skills/design/motion-design.contract.yaml
  ai-native-skills.contract-version: "^1.0.0"
  ai-native-skills.related_skills: '["design-system", "ux-psychology", "ux-ui-patterns", "accessibility", "master-design"]'
---

# Motion Design Skill

> ⛔ **HARD RULES — non-negotiable, checked first**
> 1. `prefers-reduced-motion` is a **HARD GATE** — Gate M7 score 0 = automatic full fail
> 2. Every animation must have a **reduced-motion override**
> 3. **`transform` + `opacity` only** — never animate layout-triggering properties

---

## How to Use This Skill

This skill is split into focused reference files. Load the section(s) relevant to your task:

### Section Overview

| Reference File | Contents | When to Load |
|---|---|---|
| `references/tokens-decisions.md` | Core Principle, Motion Token System (CSS vars), Easing Guide, Decision Tree | Always — foundational tokens and mode selection |
| `references/subtle-interactions.md` | Mode 1 SUBTLE: hover lift, link underline, button press, focus ring, skeleton loading, scroll entrance, stagger (1A–1G) | Building micro-interactions, product UI, personal pages |
| `references/cinematic-compose.md` | Mode 2 CINEMATIC: hero entrance, text split, clip reveal, parallax, scroll fade, counter; + Composing section | Building landing pages, portfolios, editorial sites |
| `references/gates-rules.md` | Motion Gates scoring rubric (M1–M8), Reduced Motion CSS+JS, Anti-Patterns table | Reviewing / auditing motion quality |

### Load Instructions

```
Task: implement hover + scroll entrance
→ Load: tokens-decisions.md + subtle-interactions.md

Task: build portfolio hero with cinematic reveal
→ Load: tokens-decisions.md + cinematic-compose.md

Task: review/score existing motion implementation
→ Load: gates-rules.md (+ others as needed)

Task: full motion design from scratch
→ Load: all four reference files
```

---

## Quick Mode Selection

```
Product app / dashboard    → SUBTLE only (subtle-interactions.md)
Portfolio / landing page   → SUBTLE + CINEMATIC (both mode files)
Editorial / campaign       → CINEMATIC-led (cinematic-compose.md)
Motion audit               → gates-rules.md
```

Minimum passing score: **8.0 / 10** across all gates.

---

> ⛔ **HARD RULES REMINDER**
> 1. `prefers-reduced-motion` is a **HARD GATE** — Gate M7 score 0 = automatic full fail
> 2. Every animation must have a **reduced-motion override**
> 3. **`transform` + `opacity` only** — never animate layout-triggering properties
