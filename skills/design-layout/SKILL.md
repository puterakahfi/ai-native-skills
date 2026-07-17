---
name: design-layout
description: Layout & structure port — routes to macrostructures, responsiveness, ui-components. Spatial organization of the page. Load this instead of individual layout skills.
license: MIT
metadata:
  ai-native-skills.version: 1.0.0
  ai-native-skills.author: puterakahfi
  ai-native-skills.type: meta-skill
  ai-native-skills.implements: ai-native-core/contracts/skills/experience-design/design-layout.contract.yaml
  ai-native-skills.related_skills: '["design-spacing","macrostructures","responsiveness","ui-components"]'
---

# Design Layout Port

> **HARD RULES:**
> 1. Macrostructure pick BEFORE component layout — page shape drives component arrangement.
> 2. NO min-height:100vh on hero — causes void when content is sparse.
> 3. Responsiveness gates apply to every layout decision — not a phase 5 afterthought.

---

## What This Port Covers

Spatial organization — how things are ARRANGED.
Answers: What macrostructure? What grid? What breakpoints? What component structure?

**Does NOT cover:**
- Aesthetic style (→ `design-visual` port)
- Interaction behavior (→ `design-interaction` port)
- Token system / theming (→ `design-system` port)

---

## Adapter Skills — Load Per Concern

| Concern | Adapter | When to load |
|---|---|---|
| Page-level structure | `macrostructures` | Phase 0.5 — pick macrostructure |
| Breakpoints + fluid grid | `responsiveness` | Phase 4 produce, any responsive concern |
| Component structure (nav, hero, sections) | `ui-components` | Phase 4 produce, building components |
| Rhythm, Ma, spatial hierarchy | `design-spacing` | Phase 4, any spacing decision |

### How to load an adapter
```
skill_view(name='macrostructures')
skill_view(name='macrostructures', file_path='references/marquee-hero.md')  ← per-macrostructure
skill_view(name='responsiveness')
skill_view(name='ui-components')
skill_view(name='ui-components', file_path='references/hero.md')            ← per-component
```

---

## Load Sequence for Redesign

```
Phase 0.5 MACRO PICK:
  1. skill_view(name='macrostructures')          ← pick macrostructure
  2. skill_view(name='macrostructures', file_path='references/<macro>.md')

Phase 4 PRODUCE (layout concerns):
  3. skill_view(name='ui-components')            ← component structure
  4. skill_view(name='responsiveness')           ← breakpoints + fluid
```

---

> **REMINDER:** Macrostructure first. NO min-height:100vh. Responsive from the start.
