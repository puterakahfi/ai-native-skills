# Phase 4–5 — Direction, Macrostructure, and Layered Plan

Use after routing, role composition, initialization, and preflight.

Direction is a product, communication, and experience decision. It is not a one-keyword genre lookup, product-category preset, reference clone, or decorative mood board.

Load:

```text
master-design
master-design/references/visual-direction-and-anti-slop.md

design-foundation
design-visual and only its active adapters
design-layout when page/artifact structure changes
design-strategy when content, IA, messaging, or conversion changes
```

## Direction context

```yaml
direction_context:
  product_intent:
  primary_user_tasks: []
  primary_message:
  target_audience:
  content_types_and_volume: []
  trust_requirement:
  interaction_complexity:
  viewing_contexts: []
  existing_visual_equity: []
  brand_and_system_locks: []
  required_assets: []
  available_assets: []
  category_expectations: []
  reference_influences: []
  technical_constraints: []
  accessibility_requirements: []
  evidence_gaps: []
```

Do not decide direction from one label such as `SaaS`, `AI`, `creative`, `premium`, `minimal`, `zen`, `editorial`, or `modern`.

Do not invent imagery, proof, metrics, testimonials, product UI, or content to support a preferred direction.

## Foundation and preservation first

Before comparing expression:

```text
resolve hierarchy, grouping, alignment, rhythm, balance, flow,
legibility, consistency, accessibility, and responsive continuity

preserve valid brand identity, product character, content, assets,
design-system contracts, recognizable interaction patterns, and passing regions
```

A direction change must not hide a foundation failure or erase useful product equity.

## Direction candidates

When direction is not locked, compare at least two materially different candidates.

```yaml
direction_candidate:
  id:
  direction_statement:
  genre_or_influences:
    primary:
    secondary:
  product_and_user_fit:
  hierarchy_and_focal_strategy:
  composition_logic:
  density_and_space_rhythm:
  containment_grammar:
  typography_role_strategy:
  color_and_contrast_stance:
  depth_and_imagery_stance:
  motion_stance:
  component_and_interaction_implications:
  responsive_implications:
  macrostructure_candidate:
  supports: []
  risks: []
  conflicts_with_locks: []
  generic_pattern_risks: []
```

Candidates must differ in structure, hierarchy, containment, pacing, imagery, or interaction expression—not only palette or font.

## Direction decision

Select using:

```text
primary task and message
product positioning and trust
content reality and information complexity
audience and viewing context
brand/product equity and preservation locks
required differentiation
available assets and production feasibility
accessibility and performance
cost and reversibility
```

Record rejected candidates and specific trade-offs.

```yaml
design_direction_decision:
  selected_candidate_id:
  rationale:
    product_and_user: []
    content_and_structure: []
    brand_and_equity: []
    visual_expression: []
    interaction_and_context: []
    feasibility: []
  rejected_candidates:
    - id:
      reason:
  assumptions: []
  evidence_gaps: []
```

## Visual direction contract

Translate the decision into observable rules:

```yaml
visual_direction:
  selected_candidate_id:
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
  voice_and_content_tone:
  component_expression_rules: []
  responsive_continuity_rules: []
  intentional_tensions: []
  restraint_rules: []
  prohibited_generic_patterns: []
  evidence_plan: []
```

Weak:

```text
premium
minimal
clean
editorial
modern
```

Usable:

```text
specific focal sequence
role-based hierarchy
content-dependent density
named containment grammar
typography roles and actual-content constraints
semantic color roles
justified flat/shallow/layered depth mode
real asset and product-proof strategy
purposeful or intentionally absent motion
responsive continuity and evidence plan
```

No font-family count, accent percentage, spacing base, heading ratio, composition axis, or effect technique is universal.

## Macrostructure

Choose structure from content and task relationships:

```text
what must be understood or acted on first
identity, task, proof, product, data, comparison, or action lead
sequence versus parallel comparison
unique versus repeated content
navigation depth and return paths
required states and interaction complexity
viewing and responsive contexts
existing IA and user familiarity
```

Examples of reasoning:

```text
small curated portfolio with strong identity
  → identity-led opening and authored sequence may fit

dense operational application
  → compact task/status hierarchy and work area may fit

complex comparison
  → comparison-first structure may fit better than narrative hero sections

many peer categories across contexts
  → component fitness delegated to adaptive-component-design
```

Load `macrostructures` only when a catalog archetype fits. A custom structure is valid when reasoning and acceptance criteria are explicit.

## Anti-slop diagnosis

Check the repeated grammar before production:

```text
generic product-independent hero
same eyebrow + giant heading + paragraph + cards in every section
cardification of unrelated content types
gradient/glow/blur/glass/shadow without named role
oversized type as the only hierarchy method
empty space without grouping, pacing, framing, narrative, or utility role
fake proof, dashboard, metric, badge, or testimonial
reference structure copied without product transformation
random per-section styles used as differentiation
```

Correction:

```text
classify each content region by actual role
→ identify the repeated generic treatment
→ replace or remove the smallest causal set
→ preserve coherent system and product equity
```

## Layered redesign plan

```text
strategy        purpose, positioning, value, content objective
foundation      universal relationships, brand/system locks, accessibility baseline
structure       IA, macrostructure, grid, sequence, responsive composition
components      navigation, hero/header, forms, cards, tables, rails, footer
expression      typography, color, imagery, depth, iconography, motion
interaction     states, feedback, input, overflow, focus, recovery
content         copy, labels, proof, data, CTA, microcopy
implementation  component integration, architecture, runtime constraints
```

Each layer is:

```text
preserve | refine | replace | not_applicable
```

```yaml
layered_redesign_plan:
  strategy: {action: preserve, owner: design-strategy, scope: []}
  foundation: {action: refine, owner: design-foundation, scope: []}
  structure: {action: replace, owner: design-layout, scope: []}
  components: {action: refine, owner: <selected adapters>, scope: []}
  expression: {action: refine, owner: design-visual, scope: []}
  interaction: {action: refine, owner: design-interaction, scope: []}
  content: {action: refine, owner: design-strategy, scope: []}
  implementation: {action: refine, owner: master-engineer, scope: []}
```

## Dependency order

```text
unresolved strategy/content
  blocks final structure and copy-dependent layout

unresolved foundation/locks
  blocks expression production

unresolved structure
  blocks detailed component placement

unresolved component behavior
  blocks final expression and verification

missing preservation or direction contract
  blocks production

visual effects
  never compensate for weak task, content, hierarchy, or interaction
```

## Iteration handoff

```yaml
iteration_focus:
  iteration:
  selected_direction_reference:
  primary_layer:
  secondary_layers: []
  target_findings: []
  preserved_layers_and_regions: []
  not_touching: []
  prohibited_generic_patterns: []
  success_criteria: []
  required_evidence: []
```

Avoid broad unbounded “make it better” iterations.

## Final guard

```text
□ Context, foundation, equity, and locks are explicit.
□ Materially different direction candidates were compared when direction was open.
□ Selection rationale and rejected alternatives are recorded.
□ Visual direction is observable and implementation-relevant.
□ Macrostructure follows task and content relationships.
□ Generic visual grammar and invented proof were rejected.
□ Every changed layer has an owner and preservation boundary.
□ Production has an evidence-ready direction handoff.
```
