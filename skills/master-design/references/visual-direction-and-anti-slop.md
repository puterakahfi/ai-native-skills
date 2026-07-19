# Visual Direction and Anti-Slop Contract

Load this reference when direction, visual language, art direction, or a multi-section visual redesign is active.

## Core boundary

```text
product intent + user task + content + audience + viewing context
+ existing equity + brand/system locks + technical constraints
→ materially distinct direction candidates
→ compare support, risks, and trade-offs
→ select one observable visual direction
→ delegate narrow concerns
→ verify the rendered result
```

A style adjective is not a direction. `premium`, `minimal`, `editorial`, `zen`, `modern`, `clean`, or `bold` must be translated into observable rules.

## Direction evidence

Collect before proposing expression:

```yaml
direction_context:
  product_intent:
  primary_user_tasks: []
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
```

Do not invent imagery, proof, metrics, testimonials, product UI, or content merely to make a direction easier to execute.

## Candidate comparison

When direction is not already locked, compare at least two materially different candidates.

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
  component_expression:
  responsive_implications:
  supports: []
  risks: []
  conflicts_with_locks: []
  generic_pattern_risks: []
```

Candidates must differ in structure, hierarchy, containment, pacing, imagery, or interaction expression—not only palette or font.

## Selection

Select the candidate that best supports:

```text
primary task and message
content reality
brand/product equity
trust and credibility
viewing and input context
required differentiation
implementation and asset feasibility
accessibility and performance
```

Record why alternatives are weaker. Do not select the most decorated candidate by default.

## Visual direction contract

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

## Contextual principles

```text
Typography
  One family with strong roles can be excellent.
  Multiple families are valid when they add meaning and remain coherent.
  Pairing is not proven by family count.

Color
  Accent quantity follows semantic purpose, brand, content, and channel.
  One accent can be enough; several roles can be valid in data or expressive systems.
  Random color variety is not hierarchy.

Spacing
  Use the product/design-system scale when available.
  A base grid is a tool, not a universal visual outcome.
  Rhythm is relational: within-group, between-group, section transition, and emphasis.

Composition
  Centered, asymmetric, split, dense, or open compositions can all be valid.
  Intent, balance, focal order, and flow matter more than a prescribed axis.

Hierarchy
  The number of levels follows information complexity.
  Dominance is contextual by page, section, task, and state.
  Numeric ratios are diagnostics, not immutable laws.

Depth
  Flat, shallow, layered, and deep are all valid.
  Premium is not a synonym for blur, shadow, gradient, glass, or 3D.

Restraint
  Remove treatments with no product, semantic, compositional, or emotional role.
  Restraint does not mean every surface must look sparse.
```

## Anti-slop diagnosis

Inspect the repeated visual grammar, not only isolated elements.

### Generic product-independent hero

Signals:

```text
headline could belong to any AI/SaaS product
abstract glow or gradient replaces real product proof
generic dashboard mockup does not reveal a real workflow
badges, metrics, or social proof are invented
CTA is prominent before value or trust is established
```

Correction:

```text
return to product value and content inventory
show real capability, artifact, workflow, or proof
remove invented claims
select a composition that serves the actual message
```

### Repeated section recipe

Signals:

```text
eyebrow + giant heading + centered paragraph + three equal cards
repeated at every section regardless of content type
every content type becomes a rounded card
all sections have equal density and visual weight
```

Correction:

```text
classify each section by role: proof, explanation, comparison, workflow,
artifact, narrative, trust, conversion, or utility
choose the containment and composition that fits that role
preserve system consistency without repeating identical grammar
```

### Effect-stack slop

Signals:

```text
gradient + blur + glow + glass + shadow applied together
all effects have equal strength
no effect has a named compositional or semantic role
legibility or product clarity decreases
```

Correction:

```text
name the intended depth or emphasis role
retain only the smallest technique set that performs it
remove effects used only as premium decoration
```

### Oversized-type slop

Signals:

```text
large type is the only hierarchy strategy
headline wraps awkwardly or dominates unrelated content
section headings compete with the page anchor
small supporting content becomes illegible by contrast
```

Correction:

```text
map page, section, group, item, metadata, and action roles
use scale, measure, contrast, placement, and spacing together
verify actual content and responsive contexts
```

### Empty-space slop

Signals:

```text
large void has no anchor, pacing, grouping, or narrative role
content is pushed away merely to appear minimal or premium
first viewport communicates less because of the empty area
```

Correction:

```text
identify the intended pause or focal framing
add a meaningful anchor or reduce the interval
preserve true whitespace that improves grouping and flow
```

### Reference-copy slop

Signals:

```text
reference structure copied section-for-section
visual motifs survive but product logic does not
content is forced into the reference's component grammar
brand equity is replaced by the reference's identity
```

Correction:

```text
extract principles and interaction/composition lessons
rebuild the direction from this product's content and constraints
record what was transformed and what was rejected
```

## Distinctiveness without randomness

Distinctiveness should come from a coherent product-specific combination:

```text
content selection
information order
focal sequence
composition logic
type roles
imagery or artifact treatment
containment grammar
voice
interaction expression
restraint
```

Do not create uniqueness by random per-section styles, arbitrary colors, uncontrolled asymmetry, or inconsistent components.

## Handoff

```yaml
visual_direction_handoff:
  selected_direction: <reference>
  active_concerns: []
  specialist_delegation:
    genre:
    composition:
    hierarchy:
    typography:
    color:
    depth:
    iconography:
    motion:
    readability:
  preserved_equity: []
  rejected_generic_patterns: []
  implementation_consequences: []
  required_rendered_evidence: []
```

## Final guard

```text
□ Direction is derived from product, user, content, context, and locks.
□ At least two material candidates were compared when direction was open.
□ Style adjectives became observable rules.
□ References were transformed, not copied.
□ Typography, color, spacing, composition, hierarchy, and depth use contextual reasoning.
□ Every repeated visual treatment has a system or product role.
□ Generic hero, cardification, effect-stack, oversized-type, empty-space, and reference-copy slop were checked.
□ Distinctiveness comes from coherent product-specific grammar, not randomness.
□ Specialist outputs are synthesized into one direction.
□ Rendered evidence is required before acceptance.
```
