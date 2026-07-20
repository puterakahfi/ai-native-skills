---
name: macrostructures
description: 21 named page shapes — each bundles heading placement, body composition, divider language, button voice, image treatment, and reveal into a single named choice. Pick ONE before designing. Prevents structural sameness across consecutive outputs. Adapted from Hallmark (Nutlope) for ai-native-skills ecosystem.
license: MIT
metadata:
  ai-native-skills.version: 1.0.1
  ai-native-skills.author: puterakahfi
  ai-native-skills.type: skill
  ai-native-skills.implements: ai-native-core/contracts/skills/design/macrostructures.contract.yaml
  ai-native-skills.contract-version: "^1.0.0"
  ai-native-skills.related_skills: '["design-genre", "ux-ui-patterns", "master-design", "redesign-workflow"]'
---

# Macrostructures Skill

## Core contract interface

```yaml
required_inputs:
  - brief_signals
  - prior_macrostructure_ref
allowed_outputs:
  - macrostructure_selection
  - justification_from_signals
  - diversification_verdict
  - css_pattern_ref
  - macrostructure_gate_scores
quality_gates:
  - selection_must_be_justified_from_brief_signals_not_diversification_only
  - new_pick_must_differ_from_prior_on_2_or_more_axes
  - no_dead_space_in_split_panels
  - cards_must_fill_height_in_split_layout
```

When a prior macrostructure exists, a new pick must differ on at least two declared axes unless stronger brief evidence overrides diversification. Split panels must not create dead space, and cards in a split layout must fill the intended panel height rather than leaving accidental voids.

## HARD RULES (always enforced)

```
❌ NO min-height:100vh on hero — causes void when content is sparse.
   ✅ Use padding-top: clamp(120px, 16vh, 180px) instead.

❌ NEVER justify-content:flex-end — name floats to 75%+ viewport → dead space above → FAIL.
   ✅ Use justify-content:center only, or block + padding-top:clamp().

Pick logic: Justify macrostructure from brief signals — brief-match beats diversification.
  If brief clearly signals a type (e.g. "campaign landing") → pick that macrostructure.
  Only apply diversification rule when brief is ambiguous.
```

---

## Core Principle

```
Pick ONE macrostructure BEFORE designing anything.
A macrostructure is a complete page shape — not a component, not a layout grid.
It bundles: heading placement + body composition + divider language +
            button voice + image treatment + reveal

Picking one named macrostructure = making 6 decisions at once.
It also prevents agent default-attractor sameness (always generating
the same hero → 3-feature → CTA → footer pattern).

Diversification rule (mandatory):
  Before picking: check if this project/session already used a macrostructure.
  If yes: pick a DIFFERENT one that differs on ≥ 2 of these axes:
    - Layout lead (type-led | image-led | grid-led | document-led)
    - Heading placement (left | center | asymmetric | inline)
    - Divider language (typographic | geometric | none | decorative)
```

---

## Macrostructure Catalog — load per item

Pick one. Then load the relevant reference file.

| # | Name | Layout Lead | Heading | Best for | Reference |
|---|---|---|---|---|---|
| 01 | **Specimen** | type-led | asymmetric | Editorial, foundry, portfolio | references/other-structures.md |
| 02 | **Marquee Hero** | image-led | center | Landing, campaign, atmospheric | references/marquee-hero.md |
| 03 | **Bento** | grid-led | left | SaaS features, product overview | references/other-structures.md |
| 04 | **Long Document** | document-led | left | Docs, essays, technical writing | references/other-structures.md |
| 05 | **Workbench** | grid-led | left | Developer tools, dashboards | references/other-structures.md |
| 06 | **Manifesto** | type-led | center | Brands, bold statements | references/other-structures.md |
| 07 | **Studio** | image-led | left | Agency, creative work showcase | references/other-structures.md |
| 08 | **Newsprint** | document-led | asymmetric | Publication, blog, magazine | references/other-structures.md |
| 09 | **Almanac** | document-led | left | Reference, index, directory | references/other-structures.md |
| 10 | **Garden** | image-led | center | Nature, lifestyle, warm brands | references/other-structures.md |
| 11 | **Riso** | grid-led | center | Playful, zine, print-inspired | references/other-structures.md |
| 12 | **Sport** | image-led | left | Bold, kinetic, product launch | references/other-structures.md |
| 13 | **Bloom** | image-led | center | Atmospheric, generative, dark | references/other-structures.md |
| 14 | **Coral** | grid-led | left | Consumer SaaS, mobile-forward | references/other-structures.md |
| 15 | **Cobalt** | grid-led | left | B2B SaaS, platform, API | references/other-structures.md |
| 16 | **Aurora** | image-led | center | AI product, creative tool | references/other-structures.md |
| 17 | **Atelier** | type-led | left | Luxury, fashion, high-end | references/other-structures.md |
| 18 | **Carnival** | grid-led | center | Playful, consumer, event | references/other-structures.md |
| 19 | **Lumen** | type-led | left | Classical, elegant, upright | references/other-structures.md |
| 20 | **Hum** | grid-led | left | Warm, rounded, friendly SaaS | references/other-structures.md |
| 21 | **Terminal** | document-led | left | Dev tool, CLI, technical dark | references/other-structures.md |

---

## State Your Pick

Before writing any code, emit:

```
Macrostructure: [name]
Genre: [genre]
Layout lead: [type-led | image-led | grid-led | document-led]
Heading: [left | center | asymmetric]
Differs from last on: [axes] | First build — no constraint
Brief signal: [what in the brief drove this pick]
```

---

## HARD RULES (bottom — same as top, enforced again)

```
❌ NO min-height:100vh on hero — causes void. Use padding-top:clamp(120px,16vh,180px).
❌ NEVER justify-content:flex-end — causes float/dead space above content.
✅ justify-content:center only.
✅ Justify macrostructure pick from brief signals — brief-match beats diversification.
```
