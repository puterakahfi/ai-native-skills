---
name: design-brand
description: Locked external design systems — captures brand tokens, constraints, and rules that override genre picks. Load at Phase 0 pre-flight. If brand file exists, respect it fully; genre adapts within brand constraints, never replaces them.
license: MIT
metadata:
  ai-native-skills.version: 1.0.0
  ai-native-skills.author: puterakahfi
  ai-native-skills.type: skill
  ai-native-skills.implements: ai-native-core/contracts/skills/experience-design/design-brand.contract.yaml
  ai-native-skills.related_skills: '["design-foundation","design-visual","design-genre","redesign-workflow"]'
---

# Design Brand Skill

> **HARD RULES:**
> 1. Brand file = locked. Do not override brand tokens with genre picks.
> 2. Foundation gates still apply — brand does not exempt from F1–F7.
> 3. Genre adapts WITHIN brand constraints — not the reverse.
> 4. No brand file = pick genre freely. Genre is not a brand.

---

## Layer Model

```
design-foundation   ← base (non-negotiable)
    ↑ extends
design-brand        ← locked system (client/product — overrides genre picks)
    ↑ genre adapts within
design-genre        ← style direction (constrained by brand)

IF brand file exists:
  use brand tokens → genre fills gaps brand doesn't specify
  brand color → locked, no genre override
  brand typeface → locked, no genre override
  brand spacing → locked if specified, else genre decides

IF no brand file:
  pick genre freely → genre IS the system for this project
```

---

## Brand File Structure

Each brand = one file in `references/`:
```
references/
  arbiter.md      ← Arbiter Sports design system
  <client>.md     ← add per client/product
```

Create a brand file when:
- Client has existing design system
- Product has locked tokens (CSS vars, design.md, Figma tokens)
- Redesign must stay within visual language (no full genre switch)

---

## Phase 0 Pre-flight Integration

```
STEP 1: Check for brand file
  skill_view(name='design-brand', file_path='references/<client>.md')

STEP 2: If found → extract locked constraints
  Emit: "Brand lock detected: [client]"
  List: locked tokens, locked typeface, locked palette, flex areas

STEP 3: If not found → proceed to genre pick
  No brand file = free genre selection

STEP 4: Genre fills gaps
  Brand defines: color, typeface, component rules
  Genre still applies: spacing philosophy, motion stance, composition
  Foundation always applies: F1–F7 gates
```

---

## How to Create a Brand File

```
skill_view(name='design-brand', file_path='references/arbiter.md')
← see arbiter.md as template

Structure:
  ## Identity        — brand voice, audience, personality
  ## Color Tokens    — locked palette + semantic roles
  ## Typography      — locked typeface + scale
  ## Spacing         — locked or flexible
  ## Components      — borders, radius, elevation rules
  ## Icons           — locked family
  ## Flex Areas      — what genre CAN adjust
  ## Forbidden       — what must never change
```

---

> **REMINDER:** Brand locked → foundation always applies → genre adapts within.
> No brand file → genre is free → foundation always applies.
