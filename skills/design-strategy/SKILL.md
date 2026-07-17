---
name: design-strategy
description: UX strategy & content port — routes to ux-psychology, information-architecture, cro, copywriting, content-strategy. User-centered thinking. Load this for strategy/content concerns.
license: MIT
metadata:
  ai-native-skills.version: 1.0.0
  ai-native-skills.author: puterakahfi
  ai-native-skills.type: meta-skill
  ai-native-skills.implements: ai-native-core/contracts/skills/experience-design/design-strategy.contract.yaml
  ai-native-skills.related_skills: '["ux-psychology","information-architecture","cro","copywriting","content-strategy"]'
---

# Design Strategy Port

> **HARD RULES:**
> 1. Strategy before aesthetics — understand user needs before visual decisions.
> 2. CRO only when business goal is conversion — do not add CTAs to identity/portfolio pages.
> 3. Copy is design — run copywriting adapter before locking layout.

---

## What This Port Covers

User-centered thinking — WHY things exist as they do.
Answers: What do users need? What is the IA? What copy tone? Is this converting?

**Does NOT cover:**
- Visual style (→ `design-visual` port)
- Spatial layout (→ `design-layout` port)
- Component behavior (→ `design-interaction` port)

---

## Adapter Skills — Load Per Concern

| Concern | Adapter | When to load |
|---|---|---|
| User cognition + behavior | `ux-psychology` | Phase 4 produce, persuasion/trust concerns |
| Navigation + content taxonomy | `information-architecture` | Phase 0.5, IA-heavy redesigns |
| Conversion optimization | `cro` | Phase 4, only when conversion is the goal |
| UI copy + microcopy | `copywriting` | Phase 4, any copy decision |
| Content planning | `content-strategy` | Phase 0, content-heavy pages |

### How to load
```
skill_view(name='ux-psychology')
skill_view(name='information-architecture')
skill_view(name='cro')
skill_view(name='copywriting')
skill_view(name='content-strategy')
```

---

## Load Sequence for Redesign

```
Phase 0 PRE-FLIGHT (strategy concerns):
  1. skill_view(name='content-strategy')         ← content inventory

Phase 2 VALUE ALIGNMENT:
  2. skill_view(name='cro')                      ← only if conversion goal

Phase 4 PRODUCE (content/copy):
  3. skill_view(name='copywriting')              ← UI copy
  4. skill_view(name='ux-psychology')            ← persuasion + cognitive load
```

---

> **REMINDER:** Strategy before aesthetics. Copy is design — decide copy before layout.
