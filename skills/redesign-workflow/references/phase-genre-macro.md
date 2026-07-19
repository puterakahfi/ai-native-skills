# Phase 4–5 — Direction, Macrostructure, and Layered Plan

Use this reference after preflight and role composition. Direction is a product and communication decision, not a one-keyword genre lookup.

## Direction inputs

Record the strongest available signals:

```yaml
direction_inputs:
  product_positioning: <position>
  primary_goal: <convert | complete-task | discover | compare | learn | showcase | trust | other>
  audience_expectations: []
  brand_maturity_and_equity: []
  content_volume_and_type: []
  interaction_complexity: <low | medium | high>
  trust_and_risk_requirement: <low | medium | high>
  viewing_contexts: []
  available_assets: []
  existing_hallmarks_to_preserve: []
  category_or_competitive_signals: []
  technical_and_delivery_constraints: []
  evidence_gaps: []
```

Do not decide direction from a single label such as `SaaS`, `creative`, `premium`, `minimal`, or `zen`.

## Candidate directions

Generate a small set of materially different candidates. Each candidate states:

```yaml
direction_candidate:
  name: <descriptive direction>
  genre_or_influences: []
  visual_language:
    hierarchy: <rules>
    density: <rules>
    typography: <role and tone>
    color: <role and restraint>
    depth: <stance>
    imagery: <stance>
    motion: <stance>
  macrostructure: <candidate structure>
  supports:
    - <input signal and reason>
  risks:
    - <trade-off>
  conflicts_with_locks: []
```

A genre may inform the direction, but it does not replace product reasoning.

## Direction decision

Select one candidate using:

```text
fit with the primary user or viewer task
fit with product positioning and trust requirement
fit with brand equity and preservation locks
fit with content density and information complexity
fit with available assets and production constraints
fit with viewing contexts and interaction mode
differentiation without category confusion
cost and reversibility of implementation
```

Record rejected options and why they are less fit.

```yaml
design_direction:
  selected: <candidate>
  rationale:
    product: []
    audience: []
    brand: []
    content: []
    interaction_and_context: []
  rejected_options:
    - option: <name>
      reason: <specific mismatch or trade-off>
  assumptions: []
  evidence_gaps: []
```

## Macrostructure selection

Choose page/artifact shape from relationships between content and tasks, not from a fixed industry map.

Evaluate:

```text
what must be understood or acted on first
whether identity, work, product, data, or action leads
number and hierarchy of sections/items
sequence versus comparison needs
repeated versus unique content modules
navigation depth and return paths
viewport and delivery constraints
existing information architecture and user familiarity
```

Examples of valid reasoning:

```text
high-identity portfolio with a small curated body of work
  → identity-led opening with editorial sequence may fit

high-density operational dashboard
  → task and status hierarchy may require an application shell,
    not a marketing macrostructure

pricing comparison with complex constraints
  → comparison-first structure may fit better than a narrative landing page

mobile discovery surface with many peer categories
  → category access pattern must be chosen with adaptive-component-design,
    not forced into the desktop navigation shape
```

Load `macrostructures` only when a page-level archetype is useful. A custom structure is allowed when no catalog pattern fits, provided the reasoning and acceptance criteria are explicit.

## Visual-language translation

Translate adjectives into observable rules.

Weak:

```text
premium
minimal
zen
modern
```

Usable:

```yaml
visual_language:
  focal_policy: one dominant action or idea per viewing context
  density: low in narrative sections, compact where comparison requires it
  typography: restrained role count with strong size/weight contrast only at primary hierarchy
  color: neutral base, one controlled action accent, semantic states remain distinct
  depth: subtle hierarchy through surface relationships; no decorative glass by default
  imagery: product evidence and authored assets before generic atmosphere
  motion: orientation and feedback only; reduced-motion equivalent required
  whitespace: intentional grouping and pacing, not arbitrary emptiness
```

Do not equate minimalism with warm brown, large empty areas, or removal of necessary information. Do not equate premium with gradients, glass, glow, shadows, or motion.

## Layered redesign plan

Classify every affected layer:

```text
strategy        purpose, positioning, user value, communication objective
foundation      brand, tokens, typography roles, color semantics, accessibility baseline
structure       information architecture, macrostructure, grid, page rhythm
components      navigation, hero, forms, cards, tables, rails, sections, footer
expression      imagery, iconography, illustration, depth, texture, motion
interaction     states, input behavior, feedback, overflow, focus, recovery
content         copy, labels, proof, data, CTA, microcopy
implementation  repository structure, component integration, runtime constraints
```

Each layer is:

```text
preserve | refine | replace | not_applicable
```

```yaml
layered_redesign_plan:
  strategy:
    action: preserve
    reason: <reason>
  foundation:
    action: refine
    scope: []
    owner: <port/adapter>
  structure:
    action: replace
    scope: []
    owner: design-layout
  components:
    action: refine
    scope: []
    owner: <adapters>
  expression:
    action: refine
    scope: []
    owner: design-visual
  interaction:
    action: replace
    scope: []
    owner: design-interaction
  content:
    action: refine
    scope: []
    owner: design-strategy
  implementation:
    action: refine
    scope: []
    owner: master-engineer
```

## Dependency order

```text
unresolved strategy or content structure
  blocks final layout lock

unresolved structure
  blocks detailed component placement

unresolved component behavior
  blocks final expression and verification

missing preservation decisions
  block production

visual polish
  never compensates for task, content, or interaction failure
```

## Iteration declaration

For every correction iteration:

```yaml
iteration_focus:
  iteration: <N>
  primary_layer: <layer>
  secondary_layers: []
  target_findings: []
  preserved_layers_and_regions: []
  not_touching: []
  success_criteria: []
  required_evidence: []
```

Avoid broad unbounded “make it better” iterations.

## Expression and delight boundary

Expression must have a named role:

```text
orientation
affordance
emphasis
atmosphere
identity
continuity
feedback
reward
```

Reject expression that:

```text
hides weak copy or missing content
creates a competing surface or focal point
uses a generic motif unrelated to the product
adds accessibility or performance cost without value
is impossible to produce with available tools
breaks brand or asset locks
```

Do not imply access to image, video, or 3D generation tools unless the runtime actually exposes them.