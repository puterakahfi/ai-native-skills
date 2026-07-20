---
name: design-depth
description: Optional visual depth and layering for structural separation, atmosphere, imagery integration, focus, overlays, and state. Selects flat, shallow, layered, or deep treatment from product meaning, assets, context, performance, and accessibility rather than using glow, blur, shadow, glass, or typography interleave as a generic premium recipe.
license: MIT
metadata:
  ai-native-skills.version: 1.1.1
  ai-native-skills.author: puterakahfi
  ai-native-skills.type: skill
  ai-native-skills.implements: ai-native-core/contracts/skills/design/design-depth.contract.yaml
  ai-native-skills.contract-version: "^2.1.0"
  ai-native-skills.boundary.covers: '["depth_need_assessment","surface_and_elevation_relationships","atmosphere_and_imagery_integration","overlap_and_layer_architecture","optional_typography_interleave","responsive_depth_fallback","depth_effect_restraint"]'
  ai-native-skills.boundary.delegates: '["illustration_creation","product_specific_elevation_token_values","motion_timing_and_reduced_motion_implementation","page_macrostructure","independent_design_acceptance"]'
  ai-native-skills.related_skills: '["design-visual","master-design","design-foundation","composition","design-genre","motion-design","readability","design-review"]'
---

# Design Depth

## Reviewed core contract interface

Source: `ai-native-core/contracts/skills/design/design-depth.contract.yaml` · compatible line: `^2.1.0`

```yaml
required_inputs:
- selected_design_direction
- depth_need_assessment
- target_surface
allowed_outputs:
- depth_need_assessment
- depth_mode
- depth_role_map
- layer_stack_declaration
- atmosphere_spec
- elevation_or_surface_spec
- imagery_integration_spec
- optional_interleave_spec
- responsive_depth_fallback
- performance_and_accessibility_constraints
- depth_verification_plan
quality_gates:
- depth_mode_is_justified_by_message_task_assets_and_context
- every_depth_technique_has_a_named_role
- layer_stack_is_declared_when_overlap_or_layering_requires_it
- flat_components_are_not_forced_to_declare_fake_depth_metadata
- body_text_and_controls_remain_legible_and_operable
- responsive_and_reduced_motion_fallbacks_preserve_hierarchy
- performance_cost_matches_delivery_context
- effects_do_not_replace_foundation_composition_or_content
- depth_is_not_used_as_a_generic_premium_recipe
```

Name the depth roles, declare the layer stack only when needed, and separate atmosphere, elevation/surface, and imagery integration. Body text and controls must remain legible and operable in every depth mode.

Keep this interface synchronized with the pinned core contract. Exact declarations make ownership reviewable; they do not replace rendered, runtime, accessibility, or product evidence.

Depth is optional. Use it only when it improves separation, focus, imagery integration, spatial storytelling, interaction state, or emotional meaning.

## Hard rules

```text
1. Assess whether depth is needed before selecting techniques.
2. Flat, shallow, layered, and deep are all valid.
3. Premium is not equivalent to gradient, glow, blur, glass, shadow, or 3D.
4. Every depth technique needs a named role.
5. Do not require artificial depth metadata for flat components.
6. Hard edges, borders, soft edges, and bleed are all contextual.
7. Typography interleave is optional and requires readability plus fallback.
8. Effects must not replace foundation, content, composition, or product proof.
9. Performance, reduced motion, responsive behavior, and accessibility constrain depth.
10. Rendered evidence is required before acceptance.
```

## Depth need assessment

```yaml
depth_need_assessment:
  target_surface:
  selected_design_direction:
  message_or_task:
  required_separation:
  available_imagery_or_assets: []
  interaction_overlays_or_states: []
  viewing_contexts: []
  performance_constraints: []
  accessibility_constraints: []
  depth_value:
  risks: []
  recommended_mode: <flat | shallow | layered | deep>
```

```text
FLAT
  hierarchy, grouping, and flow are clear without perceptual layering

SHALLOW
  limited surface separation, focus, or state distinction is needed

LAYERED
  meaningful overlap, imagery, atmosphere, or interaction planes are active

DEEP
  spatial storytelling or complex imagery requires several coordinated planes
```

Do not select layered or deep mode merely because the page feels flat or not premium enough. Diagnose hierarchy, composition, content, and asset quality first.

## Depth roles

Allowed roles:

```text
CANVAS
  establishes the base field

STRUCTURAL_SEPARATION
  separates content regions or component states

CONTENT_PLANE
  establishes the primary readable/task layer

ATMOSPHERE
  supports mood, environment, or spatial continuity

IMAGERY_INTEGRATION
  combines photography, illustration, or product artifacts with content

FOCUS_OR_EMPHASIS
  temporarily prioritizes an element or narrative beat

INTERACTION_OVERLAY
  expresses modal, popover, drawer, tooltip, or other layered interaction

FEEDBACK_OR_STATE
  distinguishes loading, selected, warning, success, or error conditions
```

Every technique must point to one or more roles.

## Technique selection

Potential techniques:

```text
surface contrast or border
elevation and shadow
overlap and crop
scale and perspective
gradient or light field
blur or atmospheric wash
edge bleed
hard-edge containment
typography interleave
parallax or motion depth
```

Rules:

```text
border or hard edge
  valid when containment, system language, comparison, or interaction requires it

edge bleed
  valid when imagery integration or composition benefits

shadow/elevation
  valid when it communicates plane, state, or focus

gradient/glow/blur
  valid when it creates a specific light, atmosphere, or separation role

typography interleave
  valid only when reading order and responsive fallback remain clear

perspective/3D
  valid only when assets and message justify the cost
```

## Layer stack

Declare a layer stack only when overlap or depth behavior requires it:

```yaml
layer:
  name:
  role:
  relative_plane:
  background_or_blend:
  content_relationship:
  responsive_fallback:
  legibility_constraints:
```

Implementation z-index values are product/runtime defined. Transparent surfaces inherit their parent context. Do not create a four-plane stack for every component by convention.

## Restraint and hierarchy

```text
one dominant depth cue
→ primary plane, imagery, or focus

supporting cues
→ lower intensity separation or atmosphere

local interaction depth
→ only when state or behavior requires it
```

Equal shadow, blur, and glow on every card flattens the hierarchy instead of creating depth.

## Responsive and accessibility behavior

Verify:

```text
text and controls remain readable over imagery/effects
focus and interaction overlays remain clear
mobile crops and overlaps preserve meaning
reduced-motion mode preserves hierarchy when motion contributes depth
low-performance contexts retain the essential separation
zoom/text scaling does not create destructive overlap
```

## Output

```yaml
depth_contract:
  depth_mode:
  depth_roles: []
  layer_stack: []
  technique_map: []
  imagery_integration:
  optional_interleave:
  responsive_fallbacks: []
  performance_constraints: []
  accessibility_constraints: []
  prohibited_effect_stacks: []
  required_rendered_evidence: []
```

## Anti-slop checks

```text
gradient + blur + glow + glass + shadow stacked without role
every card uses equal elevation
dark atmosphere reduces product/content clarity
fake 3D added without suitable assets
typography interleave used only for novelty
data-heavy task surface receives decorative depth
all sections become floating isolated surfaces
depth added to compensate for weak hierarchy or content
```

Correction:

```text
identify the intended role
→ keep the smallest technique set that performs it
→ remove roleless effects
→ restore clear readable planes
```

## References

Load only when applicable:

```text
references/elevation-inheritance.md
references/layer-stack.md
references/atmosphere.md
references/type-interleave.md
references/genre-depth.md
```

## Final guard

```text
□ Depth need and mode are justified.
□ Every technique has a named role.
□ Flat components are not forced into artificial planes.
□ Hard/soft edges and containment match the direction and task.
□ Effects do not replace foundation, composition, content, or proof.
□ Text, controls, states, and responsive contexts remain safe.
□ Performance and reduced-motion constraints are addressed.
□ Generic premium effect stacks were rejected.
□ Rendered evidence supports the depth claim.
```
