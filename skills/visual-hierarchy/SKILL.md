---
name: visual-hierarchy
description: Relational visual hierarchy for page, section, group, item, metadata, action, and state roles. Uses scale, contrast, measure, placement, spacing, containment, repetition, imagery, and motion together; numeric ratios are diagnostics rather than universal laws. Does not redefine canonical design-review gate IDs.
license: MIT
metadata:
  ai-native-skills.version: 1.1.0
  ai-native-skills.author: puterakahfi
  ai-native-skills.type: skill
  ai-native-skills.related_skills: '["master-design","design-foundation","design-visual","composition","design-typography","readability","design-review"]'
---

# Visual Hierarchy

Hierarchy communicates importance, relationship, sequence, and action through the complete system—not only font size.

## Hard rules

```text
1. Map semantic and task roles before styling them.
2. Hierarchy is relational across page, section, group, item, metadata, action, and state.
3. The number of hierarchy levels follows content and task complexity.
4. A page may have one principal anchor, several task anchors, or state-dependent dominance.
5. Numeric size ratios and contrast deltas are diagnostics, not universal pass rules.
6. Use multiple cues when one cue is ambiguous.
7. Section headings need not always decay monotonically; narrative and task context decide.
8. Large type is not automatically dominant when placement, contrast, imagery, or motion says otherwise.
9. Actual content, responsive contexts, and states must be verified.
10. Canonical H1–H3 identity and verdicts remain owned by design-review.
```

## Role map

```yaml
hierarchy_role_map:
  page_anchor: []
  task_or_state_anchors: []
  section_roles: []
  group_parents: []
  sibling_items: []
  metadata: []
  primary_actions: []
  secondary_actions: []
  status_and_feedback: []
  decorative_or_atmospheric_elements: []
```

Common semantic roles:

```text
ANCHOR
  Establishes page, task, message, or state identity.

SECTION
  Introduces a content or task region.

STATEMENT
  Delivers an authored claim or narrative beat.

GROUP_PARENT
  Explains or labels a related item set.

ITEM
  A repeated comparable unit.

METADATA
  Supporting detail, status, source, time, category, or qualifier.

ACTION
  Enables task progression or conversion.

FEEDBACK
  Communicates loading, success, error, warning, or system state.

ATMOSPHERE
  Supports tone or composition but must not outrank meaningful content.
```

## Hierarchy cues

Evaluate together:

```text
scale
weight
typeface or style
contrast
measure and line breaks
position
spacing and isolation
containment
repetition
imagery mass
motion or state change
interaction affordance
```

A hierarchy role should normally use at least two cues when importance could otherwise be ambiguous.

## Dominance

Dominance is scoped:

```text
page-level identity or message
section-level narrative anchor
task-level current work area
state-level warning or blocking error
modal or overlay context
```

A blocking error may temporarily outrank the page heading. A dense application may have several strong task anchors. A presentation may reset dominance on each slide. Do not force one permanent dominant element across every surface and state.

## Cross-section rhythm

Check whether section weight supports the intended sequence:

```text
progressive explanation
  weight may reduce after the main promise

editorial narrative
  selected later statements may intentionally rise again

application task flow
  task headings and state changes may dominate locally

comparison or pricing
  decision-critical regions may increase weight after explanation
```

Failure occurs when weight changes are accidental, unrelated to content priority, or create competing anchors without a clear reading path.

## Type hierarchy

One or multiple font families may work. Verify roles through:

```text
character and semantic fit
size and measure
weight and style
contrast
spacing and placement
responsive behavior
actual content length
legibility
```

Do not require display and body roles to use different families. Do not accept two families merely because they are different.

## Contrast and emphasis

Contrast may come from lightness, hue, saturation, size, weight, enclosure, motion, or position. Ensure:

```text
important information is perceivable
supporting information remains readable
color is not the only cue for critical state
accent does not compete with primary action or message
repeated roles use coherent emphasis
```

Exact numeric contrast deltas may help diagnose a case but do not replace visual and accessibility verification.

## Responsive and state hierarchy

For each relevant context:

```text
page/task identity remains clear
groups remain subordinate to parents
primary and secondary actions retain priority
metadata does not become illegible
stacking does not invert reading order
long labels and localization do not collapse roles
loading/error/success states have appropriate temporary emphasis
```

## Output

```yaml
visual_hierarchy_contract:
  role_map:
  principal_and_local_anchors: []
  cue_strategy_by_role: []
  section_weight_sequence: []
  action_priority: []
  state_priority: []
  responsive_role_rules: []
  ambiguity_risks: []
  required_rendered_evidence: []
```

## Review handoff

`design-review` owns canonical hierarchy gate identity and verdict. This skill supplies reasoning and evidence for applicable canonical concerns such as dominant/supporting relationships, cross-section weight, role taxonomy, hierarchy, type roles, and flow.

Do not redefine `H1`, `H2`, `H3`, or other registered IDs here.

## Anti-slop checks

```text
one giant heading used as the entire hierarchy system
all section headings use equal scale, spacing, and contrast
small muted text carries critical content
all cards have equal weight despite different importance
accent labels and badges compete with actions
large type copied from a reference without content fit
arbitrary heading shrinkage used only to satisfy a ratio
```

## Final guard

```text
□ Semantic and task roles were mapped before styling.
□ Page, local task, and state dominance are explicit.
□ Hierarchy uses multiple contextual cues.
□ Section weight follows content and task sequence.
□ Typography roles work with actual content and viewing context.
□ Actions, metadata, and feedback have appropriate priority.
□ Responsive and state changes preserve relationships.
□ Numeric ratios remained diagnostic rather than universal.
□ Canonical review gates were not redefined.
```
