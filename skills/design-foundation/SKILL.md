---
name: design-foundation
description: Universal design foundation — the base contract all design systems must satisfy. Typography hierarchy, intentional space, no visual noise, semantic tokens, a11y. Every genre and brand extends this; none may override it.
license: MIT
metadata:
  ai-native-skills.version: 1.0.0
  ai-native-skills.author: puterakahfi
  ai-native-skills.type: skill
  ai-native-skills.implements: ai-native-core/contracts/skills/design/design-foundation.contract.yaml
  ai-native-skills.related_skills: '["design-visual","design-layout","design-system","design-genre","design-brand"]'
---

# Design Foundation Skill

> **THIS IS THE BASE. Every genre extends it. Every brand extends it. Nothing overrides it.**

```
LAYER MODEL:
  design-foundation    ← base (this skill) — universal, non-negotiable
      ↑ extends
  design-genre         ← style layer (zen, editorial, modern-minimal...)
      ↑ extends
  design-brand         ← locked system layer (Arbiter, client brand)
      ↑ uses
  redesign-workflow    ← consumer
```

---

## Foundation Principles (universal — all design)

```
1. HIERARCHY    — visual structure must be unambiguous
   H1/body ratio ≥ 2.5× — size OR weight communicates level, not decoration

2. MA           — space must be intentional, not default
   Dead space = content failed to fill it. Breathing room = content earned it.

3. KANSO        — eliminate the unnecessary
   Every element must answer: "what is my job?" No job = remove it.

4. TOKENS       — no hardcoded values in components
   Color, spacing, type size = always semantic tokens. Never raw hex/px.

5. A11Y         — contrast, touch targets, aria — non-negotiable
   These are not "nice to have" — they are foundation gates.
```

---

## Foundation Gates (hard — fail = redesign fails)

| Gate | Rule | Threshold |
|---|---|---|
| F1 Hierarchy | H1/body font-size ratio | ≥ 2.5× |
| F2 Contrast | Primary text on bg | ≥ 4.5:1 |
| F3 Touch | Min touch target | 44×44px |
| F4 Tokens | No hardcoded hex/px in components | 0 violations |
| F5 Space | No dead space (content stranded in void) | 0 instances |
| F6 Noise | No decoration without function | 0 instances |
| F7 Aria | All interactive elements labeled | 0 violations |

**Any F-gate fail = block delivery. No exceptions.**

---

## What Foundation Does NOT Dictate

```
NOT dictated by foundation:     Dictated by genre or brand:
  Which typeface                  Fraunces (zen) / Inter (SaaS)
  Which color palette             warm dark / arbiter blue
  Border presence                 no borders (zen) / component borders (arbiter)
  Spacing scale magnitude         18vh (zen) / 8vh (SaaS)
  Icon family                     Lucide (zen) / custom (arbiter)
  Motion stance                   reduced (zen) / standard (SaaS)
```

---

## Reference Files

| Topic | File | When to load |
|---|---|---|
| Full principles + rationale | `references/principles.md` | Understanding foundation |
| Foundation gates scorecard | `references/gates.md` | Phase 5 review |

```
skill_view(name='design-foundation', file_path='references/principles.md')
skill_view(name='design-foundation', file_path='references/gates.md')
```

---

> **REMINDER:** Foundation gates are non-negotiable. Genre extends. Brand extends. Nothing overrides.
