---
name: composition
description: Context-aware composition reasoning for focal order, visual weight, balance, alignment, anchoring, empty-space purpose, and eye/task flow across marketing, product, editorial, static, and presentation surfaces. Uses rendered evidence and does not redefine canonical design-review gates.
license: MIT
metadata:
  ai-native-skills.version: 1.1.0
  ai-native-skills.author: puterakahfi
  ai-native-skills.type: skill
  ai-native-skills.related_skills: '["master-design","design-foundation","design-visual","visual-hierarchy","design-layout","design-depth","design-review"]'
---

# Composition

Composition organizes visual mass, empty space, direction, alignment, and sequence so the intended message or task is perceived in the right order.

## Hard rules

```text
1. Resolve content roles, viewing context, and primary task/message first.
2. Composition can be centered, asymmetric, split, dense, open, modular, or layered.
3. Optical and geometric alignment are both valid when intentional.
4. Numeric positions and ratios are diagnostic evidence, not universal laws.
5. Empty space needs a grouping, pacing, framing, emphasis, or narrative role.
6. Heavy visual elements need not always appear above the fold; context and sequence decide.
7. Do not force every page into a hero-centered composition.
8. Use the existing layout/grid/spacing system when valid; do not invent magic nudges.
9. Diagnose composition from the complete surface and actual content.
10. Canonical C1–C3 identity and verdicts remain owned by design-review.
```

## Inputs

```yaml
composition_input:
  target_surface:
  surface_profile:
  viewing_contexts: []
  primary_task_or_message:
  content_inventory: []
  hierarchy_roles: []
  selected_design_direction:
  existing_grid_and_spacing_system:
  required_assets: []
  responsive_contexts: []
```

## Composition model

Evaluate together:

```text
scale
contrast
position
proximity
density
direction
color mass
imagery mass
containment
empty space
motion or state emphasis
```

No single variable proves balance or dominance.

## Focal sequence

Map the intended sequence:

```yaml
focal_sequence:
  entry_context:
  first_focal_point:
  supporting_points: []
  transition_cues: []
  action_or_exit_point:
  alternate_paths: []
```

Different surfaces may require different anchors:

```text
marketing landing
  value/message → proof → explanation → action

application
  page/task identity → current state → primary work area → actions

editorial
  authored entry → narrative progression → supporting detail

static visual
  primary message → required facts/assets → action/contact

presentation
  slide focal point → supporting evidence → narrative transition
```

Do not impose an F-pattern, Z-pattern, or optical-center formula without evidence that it fits the content and reading context.

## Balance

Balance is intentional distribution, not symmetry.

```text
symmetrical
  valid for stability, comparison, ceremony, or system clarity

asymmetrical
  valid when visual mass and direction create a readable counterbalance

open
  valid when empty space frames, pauses, separates, or focuses

dense
  valid when task or information value requires parallel context
```

Failure signals:

```text
one region feels accidentally stranded or overloaded
multiple regions compete without a clear sequence
visual mass contradicts content priority
empty space disconnects related content
imagery or decoration outweighs product/message value
asymmetry has no visible balancing logic
```

## Empty space

Classify large intervals:

```text
GROUPING
  separates unrelated groups or keeps a cluster intact

PACING
  creates a pause or section transition

FRAMING
  isolates a focal element or meaningful asset

NARRATIVE
  creates anticipation, reveal, or editorial sequence

UTILITY
  preserves readability, interaction, safe area, or responsive behavior

ROLELESS
  no observable purpose; candidate defect
```

Minimal, zen, premium, or editorial labels do not automatically justify a large void.

## Alignment and anchoring

```text
structural anchor
  grid column, container edge, baseline, repeated component line

optical anchor
  corrected alignment for type, icons, irregular imagery, or perceived weight

relational anchor
  alignment to a sibling, parent group, focal point, or content sequence
```

Magic numbers are suspicious when they compensate for a missing system. Small optical corrections are valid when reusable and documented.

## Responsive composition

For each relevant context verify:

```text
focal sequence survives
related content remains grouped
reading/task order remains correct
visual mass does not flip accidentally
empty space retains or changes role intentionally
imagery crop and overlap preserve meaning
actions remain discoverable
```

Do not preserve desktop coordinates. Preserve composition intent.

## Output

```yaml
composition_contract:
  primary_task_or_message:
  focal_sequence: []
  weight_distribution:
  balance_strategy:
  structural_anchors: []
  optical_corrections: []
  empty_space_roles: []
  section_transition_logic: []
  responsive_composition_rules: []
  intentional_tensions: []
  failure_risks: []
  required_rendered_evidence: []
```

## Review handoff

`design-review` owns canonical gate identity and verdict. Composition supplies reasoning and evidence for applicable canonical concerns such as focal point, weight distribution, alignment, composition intent, hierarchy, spatial rhythm, and flow.

Do not define new meanings for `C1`, `C2`, `C3`, or other registered IDs in this skill.

## Anti-slop checks

```text
hero composition copied regardless of content
centered everything used as safe default
random asymmetry used as editorial signal
large void called premium without a role
every section given identical visual weight
background effects used to fill composition weakness
floating decorative objects with no relational anchor
```

## Final guard

```text
□ Primary task/message and content roles are explicit.
□ Focal sequence fits the surface and viewing context.
□ Balance considers all visual-weight variables.
□ Empty space has a named role or is reduced.
□ Structural and optical anchors are intentional.
□ Responsive contexts preserve composition intent rather than coordinates.
□ Direction is distinctive without random inconsistency.
□ Rendered evidence supports the claim.
□ Canonical review gates were not redefined.
```
