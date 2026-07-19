---
name: design-visual
description: Visual-design port for context-derived direction, composition, hierarchy, typography, color, optional depth, imagery, iconography, motion, readability, and anti-slop diagnosis. Load this port for broad visual work; it selects only the specialist adapters required by the active direction.
license: MIT
metadata:
  ai-native-skills.version: 1.1.0
  ai-native-skills.author: puterakahfi
  ai-native-skills.type: meta-skill
  ai-native-skills.implements: ai-native-core/contracts/skills/design/design-visual.contract.yaml
  ai-native-skills.contract-version: "^1.1.0"
  ai-native-skills.related_skills: '["design-foundation","design-brand","design-genre","design-color","design-typography","composition","visual-hierarchy","design-depth","design-iconography","motion-design","readability","master-design"]'
---

# Design Visual Port

Resolve visual expression from product context and the selected design direction. Do not begin from a fixed genre recipe or load every aesthetic skill by default.

## Hard rules

```text
1. Foundation and valid product/brand locks precede visual expression.
2. A style keyword is not a complete visual direction.
3. Compare or inherit a material direction before choosing decorative treatments.
4. Load only adapters required by active visual concerns.
5. Composition and hierarchy are relational; numeric ratios are diagnostic only.
6. Depth, motion, imagery, and effects are optional and role-driven.
7. One or multiple font families may be valid.
8. Symmetry, asymmetry, centered layout, and open space are contextual.
9. References are influences, not templates.
10. Repeated visual treatments need a system or product role.
11. Do not invent proof, content, assets, or product UI.
12. Canonical review gate IDs remain owned by design-review.
13. Rendered or exported evidence is required before acceptance.
```

## Inputs

```yaml
visual_input:
  foundation_handoff: <required>
  product_intent: <required>
  content_inventory: <required>
  target_surface: <required>
  selected_design_direction: <existing contract or null>
  brand_and_design_system_locks: []
  audience_and_viewing_context: []
  reference_influences: []
  existing_visual_equity: []
  required_assets: []
  available_assets: []
  active_visual_concerns: []
  prohibited_patterns: []
```

## Resolution sequence

```text
1. Resolve design-foundation.
2. Apply brand, product, asset, and design-system locks.
3. Inherit the accepted direction or compare direction candidates.
4. Identify active visual concerns.
5. Load only the relevant adapters.
6. Synthesize one visual direction contract.
7. Define actual-context verification evidence.
```

Genre is optional when an accepted direction contract already provides clear density, containment, voice, typography, color, depth, imagery, and motion constraints.

## Adapter selection

| Active concern | Adapter |
|---|---|
| Expression family, density, containment, voice | `design-genre` |
| Semantic palette, harmony, contrast | `design-color` |
| Typography roles, pairing, scale, rhythm | `design-typography` |
| Focal order, balance, alignment, flow | `composition` |
| Page/section/group/item role relationships | `visual-hierarchy` |
| Optional layering, atmosphere, imagery, elevation | `design-depth` |
| Icon semantics and optical consistency | `design-iconography` |
| Motion purpose, hierarchy, timing | `motion-design` |
| Actual-context legibility and measure | `readability` |

Do not load `design-depth` merely because the user says “premium”. Do not load `motion-design` when the direction is intentionally still. Do not defer readability until the end when viewing context already constrains the design.

## Visual direction output

```yaml
visual_direction_contract:
  direction_statement:
  genre_or_influences:
    primary:
    secondary:
  hierarchy_roles: []
  focal_sequence: []
  composition_logic:
  density_and_space_rhythm:
  containment_grammar:
  typography_roles: []
  color_roles: []
  depth_mode:
  depth_roles: []
  imagery_or_asset_strategy:
  iconography_stance:
  motion_stance:
  voice:
  restraint_rules: []
  prohibited_generic_patterns: []
  responsive_continuity: []
  evidence_plan: []
```

Every field must describe observable behavior or implementation consequences. “Premium blue”, “clean”, or “editorial” alone is unresolved.

## Anti-slop diagnosis

Check the repeated visual grammar:

```text
generic product-independent hero
same eyebrow/heading/paragraph/card recipe in every section
cardification of every content type
gradient/glow/blur/glass/shadow without a named role
oversized type as the only hierarchy method
empty space without pacing, grouping, framing, or narrative purpose
fake metrics, testimonials, badges, dashboard, or proof
reference structure copied without product-specific transformation
random per-section styling used as distinctiveness
```

Correction flow:

```text
identify repeated generic grammar
→ map each section/content type to its real role
→ remove or replace the smallest causal treatment set
→ preserve coherent system roles and product equity
→ verify the actual rendered result
```

Do not solve generic design by adding more random effects.

## Handoff

```yaml
visual_handoff:
  selected_direction: <reference>
  loaded_adapters: []
  specialist_decisions: []
  resolved_tradeoffs: []
  preserved_equity: []
  rejected_generic_patterns: []
  implementation_consequences: []
  required_evidence: []
```

The design owner receives one reconciled handoff, not a list of disconnected specialist opinions.

## Final guard

```text
□ Foundation and locks were applied first.
□ Direction is observable and context-derived.
□ Only active adapters were loaded.
□ Composition and hierarchy use relational reasoning.
□ Depth, motion, and effects have named roles.
□ Real content, assets, and viewing context were used.
□ Generic visual grammar was diagnosed and corrected.
□ References were transformed rather than copied.
□ Canonical review gates were not redefined.
□ Verification evidence matches the final visual claim.
```
