---
name: design-brand
description: Locked external design systems — captures brand tokens, constraints, and rules that override genre picks. Load at Phase 0 pre-flight. If brand file exists, respect it fully; genre adapts within brand constraints, never replaces them.
license: MIT
metadata:
  ai-native-skills.version: 1.0.1
  ai-native-skills.author: puterakahfi
  ai-native-skills.type: skill
  ai-native-skills.implements: ai-native-core/contracts/skills/design/design-brand.contract.yaml
  ai-native-skills.contract-version: "^1.0.0"
  ai-native-skills.related_skills: '["design-foundation","design-visual","design-genre","redesign-workflow"]'
---

# Design Brand Skill

## Reviewed core contract interface

Source: `ai-native-core/contracts/skills/design/design-brand.contract.yaml` · compatible line: `^1.0.0`

```yaml
required_inputs:
- brand_identifier
allowed_outputs:
- locked_tokens
- locked_typeface
- locked_palette
- flex_areas
- forbidden_overrides
quality_gates:
- foundation_gates_still_apply
- brand_tokens_respected_not_overridden
- genre_fills_gaps_only
```

Resolve the brand_identifier first. Locked brand tokens, typeface, and palette remain authoritative; genre may fill only declared flex areas and must record forbidden overrides.

Keep this interface synchronized with the pinned core contract. Exact declarations make ownership reviewable; they do not replace rendered, runtime, accessibility, or product evidence.

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

## Brand File Lives in YOUR PROJECT

```
OCP RULE: skill repo stores HOW, not data.
  ai-native-skills/design-brand/ ← process + template only
  your-project/.hermes/brands/   ← actual brand files live here
  your-project/design.md         ← or here (existing convention)
```

Create a brand file when:
- Client/product has existing design system
- Redesign must stay within visual language
- Tokens are locked (CSS vars, Figma tokens, design.md)

How to create:
```
1. Copy template: skill_view(name='design-brand', file_path='references/template.md')
2. Save to: your-project/.hermes/brands/<brand>.md
3. Fill in from: CSS inspect + vision audit + Figma tokens
```

---

## Phase 0 Pre-flight Integration

```
STEP 1: Check for brand file in PROJECT (not in skills repo)
  read_file('.hermes/brands/<brand>.md')   ← project brand file
  OR read_file('design.md')                ← existing convention

STEP 2: Brand file not found + brand mentioned in brief → AUTO-EXTRACT:
  browser_navigate(<brand_url>)
  Extract :root CSS vars + font-family + icon family
  vision_analyze → palette, component style, border usage
  Write to: .hermes/brands/<brand>.md (in PROJECT, not skills)
  Confirm with user before proceeding

STEP 3: If found → extract locked constraints
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
