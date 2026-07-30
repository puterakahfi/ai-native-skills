---
name: master-design
description: Active product-design authority for user experience, visual direction, information architecture, component strategy, interaction contracts, design-system alignment, critique, and engineering-ready handoff. Compares real alternatives, consumes proportionate system context when consequences cross the surface, rejects rigid page recipes and generic design grammar, and preserves valid product and brand equity.
license: MIT
metadata:
  ai-native-skills.version: 1.3.0
  ai-native-skills.author: puterakahfi
  ai-native-skills.type: skill
  ai-native-skills.implements: ai-native-core/contracts/skills/design/master-design.contract.yaml
  ai-native-skills.contract-version: "~0.2"
  ai-native-skills.requires: "systems-reasoning"
  ai-native-skills.related_skills: '["systems-reasoning","systems-thinking","design-foundation","design-visual","design-layout","design-strategy","design-interaction","design-system","adaptive-component-design","design-genre","composition","visual-hierarchy","design-depth","information-architecture","design-review"]'
---

# Master Design

## Reviewed core contract interface

Source: `ai-native-core/contracts/skills/design/master-design.contract.yaml` · compatible line: `~0.2`

```yaml
required_inputs:
- product_intent
- target_user
- primary_user_tasks
- target_surface
allowed_outputs:
- design_brief
- user_flow
- information_architecture
- direction_candidates
- selected_design_direction
- visual_direction_contract
- component_strategy
- responsive_and_adaptive_strategy
- interaction_contract
- mockup_contract
- engineering_handoff
- verification_plan
- design_decision_record
quality_gates:
- product_intent_and_primary_task_are_visible_in_the_design
- requested_solution_is_evaluated_not_followed_blindly
- selected_direction_is_compared_against_real_alternatives
- selected_direction_is_observable_and_engineering_ready
- hierarchy_grouping_flow_and_accessibility_are_resolved
- visual_expression_matches_content_audience_context_and_brand_equity
- component_strategy_matches_task_content_and_context
- valid_product_brand_and_design_system_locks_are_preserved
- generic_patterns_without_product_reason_are_removed
- required_states_and_responsive_continuity_are_defined
- specialist_findings_are_synthesized_into_one_coherent_decision
- verification_plan_matches_rendered_or_implemented_claims
- independent_design_review_is_required_for_acceptance
```

Separate the product requirement from the proposed solution. Evaluate the request against tasks, content, context, system consequences, and alternatives before selecting or rejecting it.

Keep this interface synchronized with the pinned core contract. The systemic-design composition below is an executable adapter-level interpretation that does not add a new core output or transfer design ownership.

Operate as the active product-design owner, not a passive screen generator, template selector, or style-recipe executor.

```text
product intent + user task + content + context + existing equity + locks
→ classify whether system context is material
→ consume a proportionate system handoff when required
→ compare viable experience and design directions
→ choose and explain one coherent design decision
→ delegate narrow specialist concerns
→ synthesize implementation-ready contracts
→ require independent rendered review
```

## Hard rules

```text
1. Separate the real user/product requirement from the proposed UI or visual solution.
2. Classify systemic-design applicability before structural direction lock when cross-journey,
   cross-route, metric, reusable-system, or second-order consequences may be material.
3. Systems reasoning informs design; it never selects the layout or takes design ownership.
4. Resolve design-foundation before accepting genre or styling.
5. Preserve valid brand, product, content, asset, behavior, and design-system locks.
6. Compare materially different candidates when direction is not already locked.
7. Translate style adjectives into observable hierarchy, composition, density,
   containment, typography, color, depth, imagery, motion, and voice rules.
8. Product category and artifact name are signals, not automatic genres or layouts.
9. Reference sites are evidence and influence, never copy targets.
10. Delegate specialist concerns, but keep final synthesis and trade-off ownership.
11. Do not treat one font pairing, color percentage, spacing grid, composition axis,
    hierarchy ratio, depth technique, hero, card recipe, or macrostructure as universal law.
12. Every repeated visual treatment needs a product, semantic, system,
    compositional, or emotional role.
13. Distinctiveness must come from coherent product-specific grammar, not randomness.
14. Do not invent metrics, testimonials, proof, product UI, imagery, or claims.
15. Required states, adaptive behavior, accessibility, actual content, and downstream
    consequences are part of design.
16. Implementation or rendering must pass design-review before acceptance.
17. A bounded visual correction must not be inflated into ceremonial deep system modeling.
```

## Ownership

`master-design` owns:

```text
product experience direction
final visual direction selection
information and focal hierarchy
component and interaction strategy synthesis
specialist delegation and reconciliation
preservation of valid product and brand equity
design-to-engineering handoff
```

It does not own:

```text
primary workflow selection
foundational system boundary or capability ownership
deep feedback-loop or Goodhart analysis
specialist gate definitions
independent acceptance verdict
repository implementation
product scope approval
legal or regulatory approval
```

## Evaluate the proposed solution

```text
User need:
  users must switch catalogue categories quickly.

User proposal:
  use Tabs everywhere.

Design-owner response:
  preserve the task
  → evaluate Tabs as one candidate
  → delegate cross-context fitness to adaptive-component-design
  → compare rail, tabs, select, sidebar, or other valid patterns
  → select the strongest component contract
  → require rendered evidence
```

The same rule applies to requested cards, dashboards, heroes, gradients, dark mode, editorials, split layouts, drawers, bento grids, and other proposed patterns.

A landing page does not require a hero, three feature cards, testimonials, pricing, repeated CTAs, or a fixed footer sequence. Those are candidate mechanisms whose fitness depends on the user task, content and proof reality, journey role, leverage, product and brand context, constraints, and evidence.

## Role composition

```text
Primary lifecycle selection
→ workflow-router

Foundational system model when material
→ systems-reasoning

Deep loops, emergence, second-order effects, Conway, Goodhart,
unintended consequences, and leverage analysis when material
→ systems-thinking

Product experience and final synthesis
→ master-design

User psychology, content, IA, messaging, conversion
→ design-strategy + narrow adapters

Visual direction, composition, hierarchy, color, type, depth, motion
→ design-visual + narrow adapters

Page shape, macrostructure, responsive layout, component arrangement
→ design-layout + macrostructures + narrow adapters

Cross-context component selection and substitution
→ adaptive-component-design

States, behavior, feedback, keyboard, semantics
→ design-interaction + narrow adapters

Tokens, themes, reusable component system
→ design-system + narrow adapters

Rendered or implemented acceptance
→ design-review + governing domain reviewer
```

Specialists return evidence, trade-offs, and boundaries. They do not emit disconnected decisions for the implementation agent to reconcile.

## Process

### 1. Frame the outcome

Resolve:

```text
target user
primary task or message
surface and lifecycle
success criteria
content reality
non-goals
viewing and input contexts
technical and delivery constraints
```

### 2. Classify systemic-design applicability

Before structural direction lock, classify:

```yaml
systemic_design_applicability:
  status: REQUIRED | REDUCED | NOT_APPLICABLE | NOT_VERIFIED
  rationale: string
  activation_signals: []
  omitted_analysis_risk: []
```

Load `references/systemic-design-reasoning.md` when one or more material signals exist:

- the design crosses journey stages, routes, products, actors, teams, or repositories;
- user value and business, conversion, delivery, or operational metrics may conflict;
- local optimization may damage activation, trust, retention, support burden, accessibility, or maintainability;
- positioning, information architecture, product proof, conversion strategy, reusable page shells, component families, or design-system behavior changes;
- feedback loops, delays, incentives, Goodhart risk, emergence, or second-order effects matter;
- a requested UI pattern is being treated as the requirement without product evidence.

Use `systems-reasoning` to create the bounded system model. It delegates deep dynamics to `systems-thinking` when justified.

Use REDUCED or NOT_APPLICABLE for bounded low-risk work with explicit scope, ownership, locks, and no material journey or reusable-system consequence.

### 3. Consume the bounded system handoff

When applicable, consume only material fields:

```text
purpose and desired outcomes
actors and users
surface role in the journey
upstream and downstream dependencies
relationships and dependency direction
invariants, constraints, locks, and uncertainty
local optimization and metric risks
second-order effects and leverage points
trade-offs and rejected system interventions
```

Do not translate the handoff directly into a layout. The system context constrains candidate evaluation; `master-design` still owns the design decision.

### 4. Inspect existing equity and locks

Inventory:

```text
brand identity and product character
existing design-system contracts
recognizable interaction patterns
real product artifacts and proof
content and asset locks
accepted regions and passing behavior
known research, analytics, or feedback
```

Do not erase useful equity merely to make a redesign look more dramatic.

### 5. Resolve foundation

Load `design-foundation` and establish:

```text
hierarchy relationships
grouping
structural and optical alignment
space rhythm
balance
reading and task flow
legibility
system consistency
accessibility and affordance
responsive continuity
```

Foundation is relational quality, not a theme.

### 6. Compare direction candidates

When direction is open, compare at least two candidates that differ materially in structure or expression—not only color or font.

```yaml
direction_candidate:
  id:
  direction_statement:
  product_and_user_fit:
  hierarchy_and_focal_strategy:
  composition_logic:
  density_and_space_rhythm:
  containment_grammar:
  typography_role_strategy:
  color_and_contrast_stance:
  depth_and_imagery_stance:
  motion_stance:
  component_implications:
  responsive_implications:
  system_fit:
    journey_role:
    supports_outcomes: []
    leverage_points_used: []
    upstream_effects: []
    downstream_effects: []
    metric_risks: []
    second_order_effects: []
    design_system_consequences: []
  supports: []
  risks: []
  conflicts_with_locks: []
  generic_pattern_risks: []
  evidence_needed: []
```

Use system-fit fields only when material. Do not add empty ceremony to a bounded design task.

Load `references/visual-direction-and-anti-slop.md` for the complete visual-direction contract.

### 7. Select and lock one direction

Produce an observable contract:

```yaml
visual_direction:
  selected_candidate_id:
  direction_statement:
  genre_or_influences:
  hierarchy_roles: []
  focal_sequence: []
  composition_logic:
  density_and_space_rhythm:
  containment_grammar:
  typography_roles: []
  color_roles: []
  depth_mode:
  imagery_or_asset_strategy:
  iconography_stance:
  motion_stance:
  voice_and_content_tone:
  component_expression_rules: []
  responsive_continuity_rules: []
  restraint_rules: []
  prohibited_generic_patterns: []
  accepted_system_consequences: []
  residual_system_risks: []
  evidence_plan: []
```

System consequence fields are adapter-level design-decision context. They do not change the reviewed core output taxonomy.

### 8. Delegate active concerns

Load only skills required by the direction, systemic signals, and changed layers. Reconcile specialist recommendations under one selected direction.

### 9. Define component and interaction contracts

For each meaningful component, specify:

```text
user task and information role
why this pattern fits
rejected alternatives
states and edge conditions
content contract
responsive and adaptive behavior
shared state and semantics
accessibility and input behavior
analytics or URL state when applicable
reusable-system and component-family consequences when applicable
```

Do not infer actual repository components, imports, tokens, variants, or framework conventions before `implementation-context-discovery` verifies them.

### 10. Produce engineering-ready handoff

Include:

```text
screen and section inventory
content and asset mapping
layout and component contracts
interaction and state contracts
visual direction rules
token and system implications
preservation locks
implementation consequences
accepted systemic consequences and residual risks when material
acceptance criteria
rendered verification plan
```

### 11. Review real output

Load `design-review` for rendered, exported, or implemented artifacts. Code inspection, system intent, design intent, and a high-level mockup do not prove the final experience passes.

## Contextual design principles

```text
Typography
  One family or several can work. Typography roles, rhythm, legibility,
  context, and character decide; a second family is not mandatory.

Color
  Accent quantity and role follow product semantics, brand, content, and channel.

Spacing
  Use the existing system where valid. Rhythm communicates relationship,
  sequence, pacing, and emphasis—not one repeated gap.

Composition
  Centered, asymmetric, split, dense, open, document-led, grid-led,
  type-led, image-led, or interactive can all be correct.
  Focal order, balance, flow, content, and system role decide.

Hierarchy
  Page, section, group, item, metadata, and action roles may require more than
  three levels. Numeric ratios are diagnostics, not laws.

Depth
  Flat, shallow, layered, and deep are all valid. Premium is not an effect stack.

Restraint
  Remove treatments with no named role. Restraint does not require sparse output.
```

## Metric and Goodhart boundary

When a design decision introduces or optimizes a metric, require the system handoff to identify the intended behavior, proxy failure, likely gaming, counter-metrics, downstream signals, and trust, quality, accessibility, or operational consequences.

For example, CTA clicks do not prove qualified signup, activation, retention, trust, or lower support burden.

`master-design` uses that finding to compare directions. `systems-thinking` owns the deep Goodhart and feedback analysis; product capabilities still own success metrics and product acceptance.

## Reusable design-system consequences

When a direction creates or changes repeated page shells, organisms, components, tokens, or cross-route behavior:

- record reuse, composition, bounded extension, or new-capability implications;
- identify component-family and parallel-system risks;
- preserve maintenance, migration, and compatibility concerns;
- require repository implementation-context evidence before production;
- delegate family consistency to the governing specialist and acceptance to `design-review`.

## Anti-slop checks

Reject or correct:

```text
generic product-independent hero
artifact-name-to-template mapping
repeated eyebrow + giant heading + paragraph + three-card recipe
cardification of unrelated content types
gradient, glow, blur, glass, or shadow without a named role
oversized type as the only hierarchy method
empty space without grouping, pacing, framing, or narrative purpose
fake dashboard, metrics, testimonial, badge, or proof
reference structure copied without product transformation
random per-section style changes used as distinctiveness
visual effects added to compensate for weak content or composition
local conversion optimization that ignores downstream quality
system maps that do not change a design decision
deep systems analysis for a bounded visual fix
```

Diagnose the repeated grammar and patch the smallest causal set. Do not solve generic design by adding more decorative variety.

## Output modes

### Design brief

Use when product or experience intent is unresolved. Include systemic applicability when material.

### Direction decision

Use when multiple structures or visual languages are viable. Include candidates, selection rationale, trade-offs, locks, system consequences when applicable, and evidence plan.

### Wireframe contract

Use when hierarchy, information architecture, and flow must be resolved before expression.

### Mockup contract

Use when implementation follows. Include direction, component, state, adaptive, content, consequence, and verification contracts.

### Design review handoff

Use after rendering or implementation. Include exact evidence, known gaps, domain reviewer, and acceptance boundary.

## Final guard

```text
□ Outcome and proposed solution were separated.
□ Systemic-design applicability was classified when material.
□ Required system context was consumed before structural direction lock.
□ Systems reasoning informed but did not own the design decision.
□ Deep dynamics were delegated to systems-thinking when material.
□ Foundation, existing equity, and valid locks were resolved.
□ Materially different candidates were compared when direction was open.
□ Hero, cards, dashboards, and named patterns remained candidates, not laws.
□ Style adjectives became observable rules.
□ Product category, artifact name, and references were not treated as templates.
□ Typography, color, spacing, composition, hierarchy, and depth use contextual reasoning.
□ Active specialist concerns were delegated and reconciled.
□ Generic visual grammar and invented proof were rejected.
□ Local metric optimization did not hide material downstream consequences.
□ Required states, adaptive behavior, content reality, and accessibility are covered.
□ Engineering handoff contains contracts and evidence criteria, not only visuals.
□ Independent rendered review controls acceptance.
```
