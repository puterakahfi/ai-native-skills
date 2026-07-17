---
name: design-iconography
description: Iconography as design structure — icon style selection, sizing, optical alignment, usage rules, and genre-to-icon mapping. Covers expressive icon decisions, not icon component implementation (see ui-components).
license: MIT
metadata:
  ai-native-skills.version: 1.0.0
  ai-native-skills.author: puterakahfi
  ai-native-skills.type: skill
  ai-native-skills.implements: ai-native-core/contracts/skills/design/iconography.contract.yaml
  ai-native-skills.contract-version: "^1.0.0"
  ai-native-skills.related_skills: '["design-visual","design-typography","design-color","design-system"]'
---

# Design Iconography Skill

> **HARD RULES:**
> 1. Icons support text — they do not replace it (exception: universally understood icons only).
> 2. Style consistency — one icon family per product. Never mix Lucide + Heroicons + Material.
> 3. Optical sizing — icons at 16px need different weight than 24px. Not just scale-down.
> 4. Touch targets — minimum 44×44px tap area even if icon visually smaller.
> 5. All icons need aria-label or aria-hidden — never naked SVG without a11y attr.

---

## Icons as Layer 4.5

```
Layer 4:   Components   — buttons, cards, nav
Layer 4.5: Iconography  — icons within components
Layer 5:   Motion       — icon animations (loading, transition)

Icons are micro-communication — they carry meaning at a glance.
Wrong icon style = wrong genre signal. Missing icon = missed affordance.
Decorative icon without text = accessibility failure.
```

---

## Core Decisions (in order)

```
1. NECESSITY  → does this need an icon, or does text suffice?
2. STYLE      → which icon family matches the genre?
3. SIZE       → 16 / 20 / 24 / 32px — contextual sizing
4. WEIGHT     → stroke width matches typography weight
5. ALIGNMENT  → optical center, not mathematical center
6. A11Y       → aria-label (interactive) or aria-hidden (decorative)
```

---

## Reference Files

| Topic | File | When to load |
|---|---|---|
| Icon family selection + genre map | `references/families.md` | Picking icon style |
| Sizing, weight, optical alignment | `references/sizing-alignment.md` | Using icons in components |
| A11y + usage rules | `references/a11y-usage.md` | Before implementing any icon |

```
skill_view(name='design-iconography', file_path='references/families.md')
skill_view(name='design-iconography', file_path='references/sizing-alignment.md')
skill_view(name='design-iconography', file_path='references/a11y-usage.md')
```

---

## Boundary

```
design-iconography covers:     others cover:
  Icon family selection          SVG component implementation (ui-components)
  Style consistency rules        Icon animation (motion-design)
  Sizing + optical alignment     Token sizing values (design-system)
  Genre-to-icon mapping          WCAG contrast for icon color (readability)
  A11y attribute rules
  Decorative vs functional split
```

---

> **REMINDER:** One family. Text + icon together. aria-label or aria-hidden — always.
