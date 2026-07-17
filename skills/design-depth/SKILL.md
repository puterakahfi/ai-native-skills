---
name: design-depth
description: Visual depth and layering — multi-layer design composition, atmosphere layers, typography interleave, object placement, depth techniques. Transforms flat design into layered spatial experience.
license: MIT
metadata:
  ai-native-skills.version: 1.0.0
  ai-native-skills.author: puterakahfi
  ai-native-skills.type: skill
  ai-native-skills.implements: ai-native-core/contracts/skills/experience-design/design-depth.contract.yaml
  ai-native-skills.related_skills: '["design-visual","design-foundation","composition","motion-design","design-genre"]'
---

# Design Depth Skill

> **HARD RULES:**
> 1. Declare layer stack BEFORE producing — how many layers, what on each.
> 2. Depth is intentional — not every design needs depth. Flat is valid when Kanso applies.
> 3. Objects have no hard edges — they bleed into canvas (no box/card border).
> 4. Typography can be BEHIND and IN FRONT of objects — interleave is the technique.
> 5. Scale = distance — objects in "back" are smaller, objects in "front" are larger.

---

## Flat vs Layered

```
FLAT (valid — zen, SaaS, editorial):
  Layer 1: canvas (bg color)
  Layer 2: all UI at same z-level (type + components + illustration)
  Use when: Kanso — content IS the design, no decoration needed

LAYERED (depth — atmospheric, zen with illustration, editorial with art):
  Layer 1: canvas
  Layer 2: atmosphere (ink wash, mist, gradient, texture)
  Layer 3: typography (mid-ground)
  Layer 4: objects (illustration, photo, 3D — foreground)
  Layer 5: accent (seal, badge, highlight — top)
  Use when: visual richness, spatial storytelling, brand with illustration system
```

---

## Core Decisions (in order)

```
1. DEPTH MODE    → flat / shallow (2-3 layers) / deep (4-5 layers)
2. LAYER STACK   → declare each layer: content + z-level + opacity
3. ATMOSPHERE    → what creates the "ground"? (gradient, texture, wash, blur)
4. INTERLEAVE    → where does type go behind objects? where in front?
5. SCALE RULE    → near = big + sharp / far = small + faded
6. EDGE RULE     → objects bleed into canvas (no bounding box)
```

---

## Reference Files

| Topic | File | When to load |
|---|---|---|
| Layer stack patterns + CSS | `references/layer-stack.md` | Declaring layer architecture |
| Atmosphere techniques | `references/atmosphere.md` | bg wash, mist, gradient depth |
| Typography interleave | `references/type-interleave.md` | Type behind/in front of objects |
| Depth by genre | `references/genre-depth.md` | Which depth technique per genre |

```
skill_view(name='design-depth', file_path='references/layer-stack.md')
skill_view(name='design-depth', file_path='references/atmosphere.md')
skill_view(name='design-depth', file_path='references/type-interleave.md')
skill_view(name='design-depth', file_path='references/genre-depth.md')
```

---

## When to Use Depth

```
USE depth when:
  ✓ Brief has: illustration, photography, art assets
  ✓ Genre: atmospheric, zen with visual richness
  ✓ Goal: emotional impact, spatial storytelling, premium feel
  ✓ Surface: hero section, landing page, editorial spread

STAY FLAT when:
  ✓ Kanso applies — content is the design
  ✓ Genre: SaaS/dashboard — density > atmosphere
  ✓ No art assets available — fake depth = worse than flat
  ✓ Surface: forms, tables, data views
```

---

> **REMINDER:** Declare layer stack first. Objects bleed — no hard edges.
> Type interleaves — not just sits on top. Scale = distance.
