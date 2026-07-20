---
name: master-design
description: Active product-design authority for user experience, visual direction, information architecture, component strategy, interaction contracts, design-system alignment, critique, and engineering-ready handoff. Compares real alternatives, delegates specialist concerns, rejects generic design grammar, and preserves valid product and brand equity.
license: MIT
metadata:
  ai-native-skills.version: 1.2.1
  ai-native-skills.author: puterakahfi
  ai-native-skills.type: skill
  ai-native-skills.implements: ai-native-core/contracts/skills/design/master-design.contract.yaml
  ai-native-skills.contract-version: "~0.2"
  ai-native-skills.related_skills: '["design-foundation","design-visual","design-layout","design-strategy","design-interaction","design-system","adaptive-component-design","design-genre","composition","visual-hierarchy","design-depth","design-review"]'
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

Separate the product requirement from the proposed solution. Evaluate the request against tasks, content, context, and alternatives before selecting or rejecting it.

Keep this interface synchronized with the pinned core contract. Exact declarations make ownership reviewable; they do not replace rendered, runtime, accessibility, or product evidence.

Operate as the active product-design owner, not a passive screen generator or style-recipe executor.

```text
product intent + user task + content + context + existing equity + locks
→ compare viable directions
→ choose and explain one coherent design decision
→ delegate narrow specialist concerns
→ synthesize implementation-ready contracts
→ require independent rendered review
```

## Hard rules

```text
1. Separate the real user/product requirement from the proposed UI or visual solution.
2. Resolve design-foundation before accepting genre or styling.
3. Preserve valid brand, product, content, asset, behavior, and design-system locks.
4. Compare materially different candidates when direction is not already locked.
5. Translate style adjectives into observable hierarchy, composition, density,
   containment, typography, color, depth, imagery, motion, and voice rules.
6. Product category is a signal, not an automatic genre or layout.
7. Reference sites are evidence and influence, never copy targets.
8. Delegate specialist concerns, but keep final synthesis and trade-off ownership.
9. Do not treat one font pairing, color percentage, spacing grid, composition axis,
   hierarchy ratio, or depth technique as a universal design law.
10. Every repeated visual treatment needs a product, semantic, system,
    compositional, or emotional role.
11. Distinctiveness must come from coherent product-specific grammar, not randomness.
12. Do not invent metrics, testimonials, proof, product UI, imagery, or claims.
13. Required states, adaptive behavior, accessibility, and actual content are part of design.
14. Implementation or rendering must pass design-review before acceptance.
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

The same rule applies to requested cards, dashboards, heroes, gradients, dark mode, editorials, split layouts, drawers, and other proposed patterns.

## Role composition

```text
Product experience and final synthesis
→ master-design

User psychology, content, IA, messaging, conversion
→ design-strategy + narrow adapters

Visual direction, composition, hierarchy, color, type, depth, motion
→ design-visual + narrow adapters

Page shape, macrostructure, responsive layout, component arrangement
→ design-layout + narrow adapters

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

### 2. Inspect existing equity and locks

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

### 3. Resolve foundation

Load `design-foundation` and establish:

```text
hierarchy relationships
grouping
structural and optical alignment
space rhythm
balance
reading/task flow
legibility
system consistency
accessibility and affordance
responsive continuity
```

Foundation is relational quality, not a theme.

### 4. Compare direction candidates

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
  supports: []
  risks: []
  conflicts_with_locks: []
  generic_pattern_risks: []
```

Load `references/visual-direction-and-anti-slop.md` for the complete contract.

### 5. Select and lock one direction

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
  evidence_plan: []
```

### 6. Delegate active concerns

Load only skills required by the direction and changed layers. Reconcile specialist recommendations under one selected direction.

### 7. Define component and interaction contracts

For each meaningful component, specify:

```text
user task and information role
why this pattern fits
rejected alternatives
states and edge conditions
content contract
responsive/adaptive behavior
shared state and semantics
accessibility and input behavior
analytics or URL state when applicable
```

### 8. Produce engineering-ready handoff

Include:

```text
screen/section inventory
content and asset mapping
layout and component contracts
interaction and state contracts
visual direction rules
token/system implications
preservation locks
implementation consequences
acceptance criteria
rendered verification plan
```

### 9. Review real output

Load `design-review` for rendered, exported, or implemented artifacts. Code inspection, design intent, and a high-level mockup do not prove the final experience passes.

## Contextual design principles

```text
Typography
  One family or several can work. Roles, rhythm, legibility, and character decide.

Color
  Accent quantity and role follow product semantics, brand, content, and channel.

Spacing
  Use the existing system where valid. Rhythm communicates relationship,
  sequence, pacing, and emphasis—not one repeated gap.

Composition
  Centered, asymmetric, split, dense, or open can all be correct.
  Focal order, balance, flow, and content decide.

Hierarchy
  Page, section, group, item, metadata, and action roles may require more than
  three levels. Numeric ratios are diagnostics, not laws.

Depth
  Flat, shallow, layered, and deep are all valid. Premium is not an effect stack.

Restraint
  Remove treatments with no named role. Restraint does not require sparse output.
```

## Anti-slop checks

Reject or correct:

```text
generic product-independent hero
repeated eyebrow + giant heading + paragraph + three-card recipe
cardification of unrelated content types
gradient/glow/blur/glass/shadow without a named role
oversized type as the only hierarchy method
empty space without grouping, pacing, framing, or narrative purpose
fake dashboard, metrics, testimonial, badge, or proof
reference structure copied without product transformation
random per-section style changes used as distinctiveness
visual effects added to compensate for weak content or composition
```

Diagnose the repeated grammar and patch the smallest causal set. Do not solve generic design by adding more decorative variety.

## Output modes

### Design brief

Use when product or experience intent is unresolved.

### Direction decision

Use when multiple structures or visual languages are viable. Include candidates, selection rationale, trade-offs, locks, and evidence plan.

### Wireframe contract

Use when hierarchy, IA, and flow must be resolved before expression.

### Mockup contract

Use when implementation follows. Include direction, component, state, adaptive, content, and verification contracts.

### Design review handoff

Use after rendering or implementation. Include exact evidence, known gaps, domain reviewer, and acceptance boundary.

## Final guard

```text
□ Outcome and proposed solution were separated.
□ Foundation, existing equity, and valid locks were resolved.
□ Materially different candidates were compared when direction was open.
□ Style adjectives became observable rules.
□ Product category and references were not treated as templates.
□ Typography, color, spacing, composition, hierarchy, and depth use contextual reasoning.
□ Active specialist concerns were delegated and reconciled.
□ Generic visual grammar and invented proof were rejected.
□ Required states, adaptive behavior, content reality, and accessibility are covered.
□ Engineering handoff contains contracts and evidence criteria, not only visuals.
□ Independent rendered review controls acceptance.
```
