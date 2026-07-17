---
name: design-spacing
description: Spacing as design structure — visual rhythm, spatial hierarchy, Ma principle, breathing room vs dead space. Covers expressive spacing decisions. NOT token values (see design-system for 8px grid + CSS vars).
license: MIT
metadata:
  ai-native-skills.version: 1.0.0
  ai-native-skills.author: puterakahfi
  ai-native-skills.type: skill
  ai-native-skills.implements: ai-native-core/contracts/skills/experience-design/spacing.contract.yaml
  ai-native-skills.related_skills: '["design-visual","design-layout","design-system","composition"]'
---

# Design Spacing Skill

> **HARD RULES:**
> 1. Spacing is not decoration — it IS the rhythm of the page.
> 2. Ma (間): space must have intent. Dead space ≠ breathing room.
> 3. Vertical rhythm first — section spacing > component spacing > element spacing.
> 4. Never mix token and raw px — all spacing values from design-system tokens.
> 5. Breathing room is earned — sparse content needs LESS space, not more.

---

## Spacing as Layer 3.5

```
Layer 1:   Canvas         — color field
Layer 2:   Typography     — type sets voice and rhythm
Layer 3:   Layout         — macrostructure, grid
Layer 3.5: Spacing        — rhythm, breathing room, hierarchy via space
Layer 4:   Components     — elements placed within the spaced layout
Layer 5:   Motion         — how layers move

Spacing IS the rhythm. Consistent vertical cadence = page feels composed.
Inconsistent spacing = page feels amateur, regardless of other quality.
```

---

## Core Decisions (in order)

```
1. RHYTHM     → section-to-section spacing (largest unit)
2. BREATHING  → component-to-component spacing (medium unit)
3. DENSITY    → element-to-element spacing (smallest unit)
4. MA         → intentional empty space (not absence — presence)
5. HIERARCHY  → more space above = new section signal
```

---

## Reference Files

| Topic | File | When to load |
|---|---|---|
| Visual rhythm + section spacing | `references/rhythm.md` | Section/layout spacing |
| Ma principle + breathing room | `references/ma.md` | Zen/minimalist spacing |
| Spatial hierarchy rules | `references/hierarchy.md` | Component/element spacing |

```
skill_view(name='design-spacing', file_path='references/rhythm.md')
skill_view(name='design-spacing', file_path='references/ma.md')
skill_view(name='design-spacing', file_path='references/hierarchy.md')
```

---

## Boundary with Design-System

```
design-spacing covers:        design-system covers:
  Why this amount of space?     What token value to use?
  Rhythm + cadence decisions    8px grid enforcement
  Ma — intentional emptiness    CSS var declarations
  Breathing room vs dead space  spacing scale (--sp-1 to --sp-12)
  Spatial hierarchy logic       No raw px rule
```

---

> **REMINDER:** Rhythm first. Ma is presence, not absence. Token from design-system, decision from here.
