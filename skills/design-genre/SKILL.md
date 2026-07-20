---
name: design-genre
description: Selects a contextual visual expression family for density, containment, voice, texture, color, imagery, and motion after foundation and brand/product constraints are resolved. Compares candidates, supports one bounded secondary influence, and blocks genre shortcuts such as generic SaaS minimal, random editorial asymmetry, fake atmospheric glow, or excessive zen whitespace.
license: MIT
metadata:
  ai-native-skills.version: 1.3.1
  ai-native-skills.author: puterakahfi
  ai-native-skills.type: skill
  ai-native-skills.implements: ai-native-core/contracts/skills/design/design-genre.contract.yaml
  ai-native-skills.contract-version: "^1.1.0"
  ai-native-skills.related_skills: '["design-foundation","design-brand","design-visual","master-design","composition","design-depth","design-color","design-typography"]'
---

# Design Genre

## Reviewed core contract interface

Source: `ai-native-core/contracts/skills/design/design-genre.contract.yaml` · compatible line: `^1.1.0`

```yaml
required_inputs:
- foundation_handoff
- product_intent
- audience_and_viewing_context
- content_characteristics
allowed_outputs:
- genre_candidates
- selected_expression_family
- primary_genre
- secondary_influence
- signal_justification
- expression_constraints
- genre_reference_selection
- rejected_candidates
- anti_slop_constraints
- unresolved_direction_questions
quality_gates:
- foundation_and_locks_are_resolved_before_genre_production
- selected_expression_family_matches_product_audience_content_and_context
- selection_is_compared_against_real_alternatives
- genre_is_expressed_as_observable_constraints
- secondary_influence_is_bounded
- rejected_candidates_and_tradeoffs_are_recorded
- foundation_failure_is_not_relabelled_as_genre
- no_generic_genre_slop_patterns_are_accepted
- unresolved_direction_is_reported_honestly
```

Return candidate genres, the selected expression family, signal justification, observable constraints, and selected references. Rejected candidates and trade-offs are part of the decision evidence.

Keep this interface synchronized with the pinned core contract. Exact declarations make ownership reviewable; they do not replace rendered, runtime, accessibility, or product evidence.

Genre is an expression family, not a product-category shortcut, palette preset, or substitute for design foundation.

```text
resolved foundation + product intent + audience + content + context
+ existing equity + brand/system locks + references
→ compare expression candidates
→ select one primary genre and optional bounded secondary influence
→ load observable constraints
```

## Hard rules

```text
1. Resolve design-foundation and valid brand/product locks first.
2. Genre must describe density, containment, voice, typography stance,
   color stance, imagery/depth, motion, and composition expression.
3. Product category is one signal, never an automatic genre.
4. Explicit user direction has high weight but must become observable rules.
5. References are influences, not templates.
6. Compare materially different candidates when direction is open.
7. A secondary influence must be bounded and named.
8. Do not mix multiple genres as uncontrolled per-section variety.
9. Insufficient or conflicting evidence remains unresolved; do not silently default.
10. Genre cannot hide foundation failure.
11. Premium is not a genre.
12. Load only the selected genre references needed by the final contract.
```

## Inputs

```yaml
genre_input:
  foundation_handoff: <required>
  product_intent: <required>
  audience_and_viewing_context: <required>
  content_characteristics: <required>
  explicit_user_direction:
  brand_and_design_system_locks: []
  existing_visual_equity: []
  reference_influences: []
  category_expectations: []
  trust_requirement:
  interaction_complexity:
  available_assets: []
```

## Candidate families

Current catalogs:

```text
zen-minimalist
editorial
modern-minimal
atmospheric
playful
```

These are not mutually exclusive product categories. A product may use one primary family with one bounded influence, for example:

```text
primary: modern-minimal
secondary influence: editorial typography and pacing
```

The secondary influence may affect named concerns only. It must not create two competing systems.

## Candidate comparison

```yaml
genre_candidate:
  id:
  primary_expression_family:
  secondary_influence:
  signal_support: []
  audience_and_product_fit:
  density_and_containment:
  typography_and_voice_implications:
  color_implications:
  depth_and_imagery_implications:
  motion_implications:
  composition_implications:
  supports: []
  risks: []
  conflicts_with_locks: []
  generic_pattern_risks: []
```

Candidates must differ beyond palette.

Useful signals include:

```text
product positioning and maturity
primary task and attention model
content type and volume
audience expectations and trust needs
interaction complexity
viewing context
existing brand/product equity
available imagery or assets
category conventions worth preserving or challenging
explicit user direction
```

## Selection

```text
strong bounded direction and locks already exist
  → inherit them; genre may only label and constrain expression

one candidate clearly best supports product, content, context, and equity
  → select it and record rejected alternatives

multiple candidates remain materially plausible
  → present the trade-off or follow approval mode

signals are weak or conflicting
  → UNRESOLVED
  → do not silently choose editorial or modern-minimal
```

## Genre integrity

```text
ZEN / MINIMALIST
  restraint, attention, pacing, reduction, material honesty
  not excessive empty space or weak hierarchy

EDITORIAL
  authored pacing, typographic voice, narrative sequence, intentional composition
  not random asymmetry, giant serif type, or magazine imitation

MODERN-MINIMAL
  clarity, system confidence, task focus, controlled surfaces, precise detail
  not generic SaaS hero, identical cards, blue gradient, or sterile neutrality

ATMOSPHERIC
  mood, depth, imagery, spatial or sensory storytelling
  not automatic dark mode, glow, blur, gradient, or illegible ambience

PLAYFUL
  approachable energy, expressive feedback, warmth, rhythm, and character
  not random color, rounded everything, stickers, or childish decoration
```

Premium must be translated into specific qualities such as material restraint, confidence, precision, craft, depth, editorial pacing, service detail, or high-fidelity product proof.

## Output

```yaml
genre_contract:
  foundation_reference:
  inherited_foundation_rules: []
  brand_and_product_locks: []
  primary_genre:
  secondary_influence:
    genre:
    applies_to: []
  selection_rationale:
  rejected_candidates: []
  voice:
  density:
  containment_grammar:
  typography_stance:
  color_stance:
  depth_and_imagery_stance:
  motion_stance:
  composition_expression:
  restraint_rules: []
  prohibited_patterns: []
  references_loaded: []
  unresolved_questions: []
```

A genre label without these constraints is unresolved.

## Anti-slop checks

```text
SaaS / developer tool automatically routed to modern-minimal
personal site automatically routed to editorial
creative tool automatically routed to atmospheric dark glow
wellness product automatically routed to playful or zen
palette-only genre changes
genre switch used to hide weak hierarchy or composition
reference site copied section-for-section
multiple genres mixed only to create visual variety
```

Correction:

```text
return to foundation, product intent, content, context, and candidate comparison
```

## References

Load only references selected by the final contract:

| Genre | Reference |
|---|---|
| Zen / Minimalist | `references/zen.md` |
| Editorial | `references/editorial.md` |
| Modern Minimal | `references/modern-minimal.md` |
| Atmospheric | `references/atmospheric.md` |
| Playful | `references/playful.md` |
| Compatibility evidence | `references/genre-compatibility.md` |

## Final guard

```text
□ Foundation and locks were resolved first.
□ Product category was treated as a signal, not a shortcut.
□ Material alternatives were compared when direction was open.
□ Primary and optional secondary influence are explicit and bounded.
□ Genre is expressed as observable rules, not palette or adjective only.
□ References were transformed through product content and constraints.
□ Genre did not hide a foundation failure.
□ Generic genre slop was checked.
□ Unresolved direction is reported honestly.
```
