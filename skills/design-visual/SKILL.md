---
name: design-visual
description: Visual design port — routes to genre, motion, composition, readability. Load this instead of individual visual skills. Abstraction over implementation.
license: MIT
metadata:
  ai-native-skills.version: 1.0.0
  ai-native-skills.author: puterakahfi
  ai-native-skills.type: meta-skill
  ai-native-skills.implements: ai-native-core/contracts/skills/design/design-visual.contract.yaml
  ai-native-skills.contract-version: "^1.0.0"
  ai-native-skills.related_skills: '["design-depth","design-color","design-typography","design-iconography","design-genre","motion-design","composition","readability"]'
---

# Design Visual Port

> **HARD RULES:**
> 1. Load this port — not individual skills — unless you need one specific skill.
> 2. Genre first — all other visual decisions depend on genre pick.
> 3. Do not improvise visual rules — every rule must come from an adapter skill below.

---

## What This Port Covers

Aesthetic foundations — what things LOOK like.
Answers: What genre? What motion stance? What typography rules? What composition?

**Does NOT cover:**
- Layout/spatial (→ `design-layout` port)
- Interaction behavior (→ `design-interaction` port)
- Token system / theming (→ `design-system` port)

---

## Adapter Skills — Load Per Concern

| Concern | Adapter | When to load |
|---|---|---|
| Typography structure + pairing | `design-typography` | Layer 2 — after genre, before layout |
| Layer stack + depth | `design-depth` | When brief has illustration/depth intent |
| Color palette + harmony | `design-color` | Layer 1.5 — after genre, sets canvas |
| Typeface + visual style | `design-genre` | Always first — gates everything downstream |
| Motion stance + animation | `motion-design` | Phase 4 produce, any animation decision |
| Composition + visual weight | `composition` | Phase 4 produce, layout balance questions |
| Typography legibility | `readability` | Phase 5 review, body text concerns |
| Icon style + a11y | `design-iconography` | Phase 4, any icon decision |

### How to load an adapter
```
skill_view(name='design-genre')
skill_view(name='design-genre', file_path='references/zen.md')   ← per-genre catalog
skill_view(name='motion-design')
skill_view(name='composition')
skill_view(name='readability')
```

---

## Load Sequence for Redesign

```
Phase 0.5 GENRE:
  1. skill_view(name='design-genre')             ← detect genre from brief
  2. skill_view(name='design-genre', file_path='references/<genre>.md')  ← load genre spec

Phase 0.6 VISUAL LANGUAGE (color + typography):
  3. skill_view(name='design-color', file_path='references/genre-palette-map.md')  ← Layer 1.5
  4. skill_view(name='design-typography')        ← Layer 2: pair + scale + hierarchy
  5. skill_view(name='design-typography', file_path='references/genre-typeface-map.md')

Phase 4 PRODUCE (visual concerns):
  5. skill_view(name='motion-design')            ← motion stance + CSS
  6. skill_view(name='composition')              ← visual weight rules

Phase 5 REVIEW (visual gates):
  7. skill_view(name='readability')              ← legibility metrics (contrast, CPL)
```

---

> **REMINDER:** Genre first. Rules come from adapters, not improvisation.
