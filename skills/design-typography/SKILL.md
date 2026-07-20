---
name: design-typography
description: Typography as design structure — typeface selection, type scale, pairing, hierarchy, rhythm, and personality. Layer 2 of visual design (after canvas). Covers expressive and structural typography decisions, not legibility metrics (see readability skill for those).
license: MIT
metadata:
  ai-native-skills.version: 1.0.1
  ai-native-skills.author: puterakahfi
  ai-native-skills.type: skill
  ai-native-skills.implements: ai-native-core/contracts/skills/design/typography.contract.yaml
  ai-native-skills.contract-version: "^1.0.0"
  ai-native-skills.boundary.covers: '["typeface_personality_and_selection","display_body_pairing","modular_scale_selection","hierarchy_h1_to_caption","leading_tracking_rhythm","font_rendering_antialiasing","genre_to_typeface_mapping"]'
  ai-native-skills.boundary.delegates: '["contrast_ratio_wcag","characters_per_line","minimum_font_size_px"]'
  ai-native-skills.related_skills: '["design-visual","design-system","readability","design-genre","composition"]'
---

# Design Typography Skill

## Reviewed core contract interface

Source: `ai-native-core/contracts/skills/design/typography.contract.yaml` · compatible line: `^1.0.0`

```yaml
required_inputs:
- genre_selection
allowed_outputs:
- typeface_pair
- modular_scale
- hierarchy_mapping
- rhythm_spec
- rendering_spec
quality_gates:
- genre_loaded_before_typeface_selection
- scale_derived_not_arbitrary
- h1_body_ratio_appropriate_for_weight
- max_two_typefaces_plus_mono
- variable_fonts_preferred
- font_variation_settings_explicit
```

Start from genre_selection and return the pair, hierarchy, rhythm, and rendering specification. Use at most two typefaces plus mono, and prefer variable fonts when they satisfy the required language, weight, and rendering needs.

Keep this interface synchronized with the pinned core contract. Exact declarations make ownership reviewable; they do not replace rendered, runtime, accessibility, or product evidence.

> **HARD RULES:**
> 1. Typography is Layer 2 — after canvas (bg, color), before everything else.
> 2. Type pair first — decide display + body before any sizing.
> 3. Scale before sizing — pick a modular scale, then derive all sizes from it. No arbitrary px.
> 4. Hierarchy is structural, not decorative — H1/H2/H3 differences must be meaningful.
> 5. Genre governs personality — load design-genre before picking typefaces.

---

## Typography as Layer 2

```
Layer 1: Canvas        — background, surface, color field
Layer 2: Typography    — type sets the voice, rhythm, and structure of the page
Layer 3: Layout        — arrangement of typographic + non-typographic elements
Layer 4: Components    — UI elements placed within the layout
Layer 5: Motion        — how layers 1–4 move and transition

Typography is not styling — it IS the page.
Strip everything: if the type is wrong, the page is wrong.
```

---

## Core Decisions (in order)

```
1. PERSONALITY  → what does this brand/page sound like typographically?
2. PAIR         → display typeface + body typeface
3. SCALE        → modular scale ratio (1.250 / 1.333 / 1.414 / 1.618)
4. HIERARCHY    → H1 / H2 / H3 / body / caption — size + weight mapping
5. RHYTHM       → line-height, paragraph spacing, letter-spacing
6. RENDERING    → font-weight, font-variation-settings, antialiasing
```

---

## Reference Files

| Topic | File | When to load |
|---|---|---|
| Typeface selection + pairing theory | `references/selection-pairing.md` | Picking typefaces |
| Modular scale + hierarchy rules | `references/scale-hierarchy.md` | Setting type sizes |
| Rhythm, spacing, rendering | `references/rhythm-rendering.md` | Fine-tuning details |
| Genre-to-typeface mapping | `references/genre-typeface-map.md` | Genre-driven selection |

```
skill_view(name='design-typography', file_path='references/selection-pairing.md')
skill_view(name='design-typography', file_path='references/scale-hierarchy.md')
skill_view(name='design-typography', file_path='references/rhythm-rendering.md')
skill_view(name='design-typography', file_path='references/genre-typeface-map.md')
```

---

## Boundary with Readability Skill

```
design-typography covers:          readability covers:
  Typeface personality               Contrast ratio (WCAG)
  Display vs body pairing            Characters per line (CPL)
  Modular scale selection            Minimum font size (px)
  Hierarchy (H1→H2→H3→body)         Line height for reading comfort
  Type rhythm and spacing            Cognitive ease (Flesch-Kincaid)
  Font weight + variation            Density scoring
  Genre-driven typeface choice

Rule: design-typography = structural/expressive decisions
      readability = functional/measurable outcomes
Both must pass — they are complementary, not overlapping.
```

---

> **REMINDER:** Genre first → pair → scale → hierarchy → rhythm → rendering. In that order.
