---
name: design-color
description: Color as design structure — palette construction, color psychology, harmony rules, and genre-to-palette mapping. Covers expressive color decisions. NOT token system (see dark-light-theming) and NOT semantic roles (see design-system).
license: MIT
metadata:
  ai-native-skills.version: 1.0.1
  ai-native-skills.author: puterakahfi
  ai-native-skills.type: skill
  ai-native-skills.implements: ai-native-core/contracts/skills/design/color-theory.contract.yaml
  ai-native-skills.contract-version: "^1.0.0"
  ai-native-skills.boundary.covers: '["hue_saturation_value_decisions","palette_construction","color_harmony_rules","color_psychology_validation","genre_to_palette_mapping"]'
  ai-native-skills.boundary.delegates: '["contrast_ratio_wcag","semantic_token_naming","dark_light_switching","component_level_color"]'
  ai-native-skills.related_skills: '["design-visual","design-genre","design-system","dark-light-theming","design-typography"]'
---

# Design Color Skill

## Reviewed core contract interface

Source: `ai-native-core/contracts/skills/design/color-theory.contract.yaml` · compatible line: `^1.0.0`

```yaml
required_inputs:
- genre_selection
- theme_default
allowed_outputs:
- palette_primitives
- semantic_role_mapping
- accent_definition
- temperature_rationale
quality_gates:
- palette_derives_from_genre_not_reverse
- max_one_accent_one_role
- temperature_consistent_across_palette
- no_hardcoded_hex_in_components
- contrast_ratio_delegated_to_readability_skill
```

Return palette primitives, semantic role mapping, one bounded accent definition, and temperature rationale. Components consume semantic roles; hardcoded hex values inside components are rejected.

Keep this interface synchronized with the pinned core contract. Exact declarations make ownership reviewable; they do not replace rendered, runtime, accessibility, or product evidence.

> **HARD RULES:**
> 1. Genre first — color palette derives from genre, not the reverse.
> 2. Max 3 roles: bg + ink + accent. Every additional color needs a semantic job.
> 3. Accent used for ONE purpose only — never reuse accent for multiple roles.
> 4. Temperature consistency — warm bg needs warm ink. Mixed temperature = visual tension.
> 5. Never hardcode hex in components — always semantic token (see design-system).

---

## Color as Layer 1.5

```
Layer 1:   Canvas        — background color field (this skill)
Layer 1.5: Color system  — palette + roles (this skill)
Layer 2:   Typography    — type on top of color field
Layer 3:   Layout        — arrangement within the field

Color is not decoration — it IS the canvas everything else sits on.
Wrong color = wrong temperature = wrong mood = wrong genre.
```

---

## Core Decisions (in order)

```
1. TEMPERATURE  → warm / cool / neutral? (follows genre)
2. VALUE        → light / dark / mid? (follows theme default)
3. PALETTE      → bg + surface + ink steps (3–5 values)
4. ACCENT       → one color, one job
5. HARMONY      → how colors relate (complementary, analogous, monochromatic)
6. ROLES        → map palette to semantic tokens
```

---

## Reference Files

| Topic | File | When to load |
|---|---|---|
| Color theory foundations | `references/theory.md` | Understanding hue/value/saturation |
| Palette construction | `references/palette.md` | Building a palette from scratch |
| Genre-to-palette map | `references/genre-palette-map.md` | Genre-driven color selection |
| Color psychology | `references/psychology.md` | Emotional + cultural color meaning |

```
skill_view(name='design-color', file_path='references/theory.md')
skill_view(name='design-color', file_path='references/palette.md')
skill_view(name='design-color', file_path='references/genre-palette-map.md')
skill_view(name='design-color', file_path='references/psychology.md')
```

---

## Boundary Map

```
design-color covers:          others cover:
  Hue / saturation / value      Contrast ratio WCAG (readability)
  Palette construction          Token architecture (design-system)
  Color harmony rules           Dark/light switching (dark-light-theming)
  Color psychology + mood       Semantic role naming (design-system)
  Genre → palette mapping       Slop gate: no amber (design-genre/zen)
  Temperature consistency
  Accent role definition
```

---

> **REMINDER:** Genre → temperature → palette → accent → roles. In that order.
> Accent = one color, one job. Temperature must be consistent across palette.
