# Visual Personality Preservation

Use this reference when an existing surface belongs to a recognizable product, brand, portfolio, campaign, or design-system family and the redesign changes structure, containment, separators, density, depth, spacing, typography, color, imagery, iconography, or motion.

A redesign may improve information architecture while still regressing the product's visual personality. Functional improvement does not authorize personality drift.

## Surface-family baseline

Inspect the target and enough canonical adjacent surfaces to distinguish shared language from one-page accidents.

```yaml
surface_family_baseline:
  target_surface:
  adjacent_canonical_surfaces: []
  evidence:
    rendered: []
    source: []
    owner_statements: []
  shared_visual_traits: []
  target_specific_traits: []
  allowed_local_variations: []
  prohibited_personality_drift: []
  evidence_gaps: []
```

Canonical adjacent surfaces may include a homepage, sibling product page, established application shell, campaign family, presentation master, or identity guideline. Do not average unrelated legacy screens into a false system.

When no rendered baseline is available:

```text
preserve existing expression by default
→ permit only changes supported by source evidence or explicit owner locks
→ mark pixel, optical, and personality-continuity claims NOT_VERIFIED
→ do not invent a new expression grammar to solve a structural problem
```

## Translate personality into observable locks

Labels such as `zen`, `calm`, `dense`, `bold`, `technical`, `playful`, `editorial`, `minimal`, or `brutalist` are evidence leads, not implementation contracts.

Translate only supported traits:

```yaml
visual_personality_locks:
  hierarchy_behavior:
  composition_behavior:
  density_and_space_rhythm:
  containment_grammar:
  separator_grammar:
  typography_behavior:
  color_and_contrast_behavior:
  depth_behavior:
  imagery_and_iconography_behavior:
  motion_behavior:
  interaction_expression:
  restraint_rules: []
  repeated_treatment_rules: []
  prohibited_drift: []
```

Examples of observable translations:

```text
"zen / calm"
  may mean open composition, slow pacing, low containment, quiet depth,
  limited competing accents, and separators used only at real boundaries

"dense / operational"
  may mean compact rhythm, explicit grouping, persistent controls,
  stronger separators, and shallow but frequent containment

"brutalist"
  may mean exposed structure, hard edges, deliberate contrast,
  and visible system mechanics—not random misalignment or inaccessible type
```

These are hypotheses. Preserve only what is evidenced by the actual surface family and owner decisions.

## Expression-change detection

A structure or component patch also changes expression when it adds, removes, or repeats:

```text
borders or dividers
cards, panels, sheets, wells, or tonal surfaces
shadow, blur, glow, gradient, or elevation
large spacing shifts or density changes
typography role changes
new accent distribution
new icon containers or decorative marks
new motion or transition patterns
```

When expression changes:

```text
design owner: master-design
brand/product continuity: design-brand
visual grammar: design-visual and applicable adapters
spacing/containment layout: design-layout + design-spacing when active
composition repetition: composition when active
acceptance: design-review + governing domain reviewer
```

Do not classify a border-heavy structural patch as layout-only.

## Repeated-treatment audit

Before production and again before acceptance, inventory repeated treatments introduced or materially increased by the patch.

```yaml
repeated_treatment_audit:
  - treatment: <border | divider | card | panel | shadow | accent | badge | other>
    locations: []
    count_before:
    count_after:
    named_roles: []
    role_consistency:
    personality_fit:
    simpler_valid_alternative:
    verdict: preserve | reduce | replace | remove | not_verified
```

Ask:

```text
Does every repeated treatment have a named semantic, interaction,
system, compositional, or emotional role?

Is the treatment carrying hierarchy that should instead come from
space, alignment, type, sequence, contrast, or content grouping?

Did one useful local treatment become the default grammar for every region?

Does the cumulative result still belong to the same surface family?
```

A treatment is not invalid because it is frequent. It fails when frequency has no supported role, conflicts with the visual-personality locks, or replaces clearer relational hierarchy.

## Verification record

```yaml
visual_continuity_report:
  baseline_reference:
  surface_family_traits_checked: []
  changed_expression_layers: []
  specialist_routes: []
  repeated_treatment_audit: []
  preserved_traits: []
  intentional_changes: []
  observed_drift: []
  evidence:
    rendered: []
    runtime: []
    source: []
  verdict: PASS | FAIL | PARTIAL | NOT_VERIFIED
```

`PASS` requires rendered evidence for visual and optical claims. Source inspection can verify class changes and treatment counts, but not the final personality, rhythm, balance, or cumulative visual weight.

## Regression case — pkahfi `/ai-skills`

Observed source: `puterakahfi/pkahfi#8`.

```text
Valid change:
  flat capability dump
  → intent-routed workflow discovery + progressive registry

Regression:
  section borders + row dividers + framed disclosures became the dominant grammar
  → page drifted from the existing zen, spacious, low-containment pkahfi family

Expected workflow behavior:
  capture the surface-family personality
  → translate zen into observable containment/separator/space rules
  → detect expression change despite IA being the primary layer
  → route visual specialists
  → audit repeated borders and panels
  → preserve the improved IA while correcting only the expression layer
```

This case does not establish a universal low-border rule. It establishes that redesign must preserve or intentionally supersede evidenced visual personality through an explicit contract and reviewable evidence.
