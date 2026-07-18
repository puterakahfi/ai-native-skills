---
name: design-interaction
description: Interaction & UX patterns port — routes to ux-ui-patterns, ux-patterns-for-developers. Behavioral design. Load this instead of individual interaction skills.
license: MIT
metadata:
  ai-native-skills.version: 1.0.0
  ai-native-skills.author: puterakahfi
  ai-native-skills.type: meta-skill
  ai-native-skills.implements: ai-native-core/contracts/skills/design/design-interaction.contract.yaml
  ai-native-skills.contract-version: "^1.0.0"
  ai-native-skills.related_skills: '["ux-ui-patterns","ux-patterns-for-developers","adaptive-component-design"]'
---

# Design Interaction Port

> **HARD RULES:**
> 1. Check external pattern library BEFORE implementing any interaction behavior.
> 2. External = behavior + a11y + edge cases. Internal = CSS + visual template only.
> 3. Never hand-roll patterns that ux-patterns-for-developers already covers.

---

## What This Port Covers

Behavioral design — how things WORK and RESPOND.
Answers: What pattern for this interaction? What states? What a11y behavior?

**Does NOT cover:**
- Visual style (→ `design-visual` port)
- Spatial layout (→ `design-layout` port)
- UX strategy/research (→ `design-strategy` port)

---

## Adapter Skills — Load Per Concern

| Concern | Adapter | When to load |
|---|---|---|
| UI interaction patterns (74 patterns) | `ux-patterns-for-developers` | Any component behavior question |
| UX/UI pattern templates | `ux-ui-patterns` | Pattern selection for page sections |\n| Cross-device component choice | `adaptive-component-design` | Tabs/rails/selects/sheets/tables must change by context |

### How to load
```
skill_view(name='ux-patterns-for-developers')
skill_view(name='ux-ui-patterns')\nskill_view(name='adaptive-component-design')

External pattern install (when needed):
  npx skills add https://github.com/thedaviddias/ux-patterns-for-developers --skill <name> --yes --global
```

---

## Load Sequence for Redesign

```
Phase 4 PRODUCE (interaction concerns):
  1. skill_view(name='ux-patterns-for-developers')  ← check before implementing behavior
  2. skill_view(name='ux-ui-patterns')              ← page section patterns\n  3. skill_view(name='adaptive-component-design')  ← substitute patterns per viewport

Phase 5 REVIEW (interaction gates):
  Gates: hover states, focus-visible, keyboard nav, ARIA labels
```

---

> **REMINDER:** External pattern library first — never hand-roll what's already solved.
