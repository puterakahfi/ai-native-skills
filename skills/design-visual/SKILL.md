---
name: design-visual
description: Visual design port — routes to genre, motion, composition, readability. Load this instead of individual visual skills. Abstraction over implementation.
license: MIT
metadata:
  ai-native-skills.version: 1.0.0
  ai-native-skills.author: puterakahfi
  ai-native-skills.type: meta-skill
  ai-native-skills.implements: ai-native-core/contracts/skills/experience-design/design-visual.contract.yaml
  ai-native-skills.related_skills: '["design-genre","motion-design","composition","readability"]'
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
| Genre + voice + slop gates | `design-genre` | Always first — gates everything downstream |
| Motion stance + animation | `motion-design` | Phase 4 produce, any animation decision |
| Composition + visual weight | `composition` | Phase 4 produce, layout balance questions |
| Typography legibility | `readability` | Phase 5 review, body text concerns |

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

Phase 4 PRODUCE (visual concerns):
  3. skill_view(name='motion-design')            ← motion stance + CSS
  4. skill_view(name='composition')              ← visual weight rules

Phase 5 REVIEW (visual gates):
  5. skill_view(name='readability')              ← typography/legibility gates
```

---

> **REMINDER:** Genre first. Rules come from adapters, not improvisation.
