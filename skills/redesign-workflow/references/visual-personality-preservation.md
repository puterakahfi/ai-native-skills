# Visual Personality Preservation

Use this reference when an existing surface belongs to a recognizable product, brand, portfolio, campaign, or design-system family and the redesign changes structure, containment, separators, density, depth, spacing, typography, color, imagery, iconography, or motion.

A redesign may improve information architecture while still regressing the product's visual personality. Functional improvement does not authorize personality drift.

## Ownership boundary

This reference owns continuity detection and preservation handoff. It does not redefine genre semantics.

```text
surface-family evidence and owner locks
  → visual-personality preservation identifies continuity requirements
  → design-genre resolves or inherits the expression family
  → the selected canonical genre reference supplies genre-specific rules
  → design-visual and applicable adapters implement them
```

When the accepted primary genre is `zen-minimalist`, load:

```text
design-genre
skills/design-genre/references/zen.md
```

Do not invent a replacement Zen philosophy inside `redesign-workflow`. The canonical genre reference owns Zen-specific line budgets, containment, spacing expression, alignment rails, motion, exceptions, and hard failures.

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

## Resolve personality through the canonical genre contract

Labels such as `zen`, `calm`, `dense`, `bold`, `technical`, `playful`, `editorial`, `minimal`, or `brutalist` are evidence leads, not implementation contracts.

```yaml
visual_personality_handoff:
  supported_traits: []
  inherited_brand_and_product_locks: []
  selected_or_inherited_genre:
  canonical_genre_reference:
  genre_contract_reference:
  local_surface_family_constraints: []
  intentional_supersessions: []
  unresolved_questions: []
```

The canonical `design-genre` contract owns density, containment, voice, typography stance, color stance, imagery and depth, motion, and composition expression. Visual-personality preservation may add evidenced local constraints, but it must not weaken or silently override the selected genre reference.

Examples:

```text
accepted zen-minimalist family
  → load design-genre/references/zen.md
  → inherit Kanso: remove before adding
  → inherit Seijaku: space is the divider, not lines
  → inherit Ma: intentional intervals with a visual anchor
  → apply the canonical structural-line contract and allowed exceptions

accepted dense operational family
  → load the selected canonical genre reference
  → preserve compact rhythm, explicit grouping, scanning support,
    and stronger boundaries only where that contract supports them
```

These are not universal defaults. They apply only when supported by evidence and the selected genre contract.

## Zen line and separator interpretation

For a selected `zen-minimalist` contract, lines are not universally forbidden. They are exceptional structural tools.

```text
Kanso
  → remove an unnecessary line before adding another treatment

Ma
  → use intentional space, alignment, proximity, measure, and rhythm
    as the default grouping and separation system

Seijaku
  → keep interruption low; space is the divider by default

functional exception
  → retain or add a line only when it performs necessary structural,
    interaction, orientation, data, or diagram work
```

The authoritative line budget remains in `design-genre/references/zen.md`:

```text
section dividers
  → 0

repeated row separators
  → default 0

dense-list exception
  → one leading or trailing hairline may orient one list system

visible structural-line budget
  → target 0 in most viewports
  → maximum 1 visible structural hairline in a typical viewport
  → controls, focus rings, and required data-table or diagram grids are excluded
```

A line exception requires a functional reason in the run state. `The page looked empty`, `it felt cleaner`, or `it needed more structure` without evidence is not sufficient.

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
genre contract: design-genre + selected canonical reference
visual grammar: design-visual and applicable adapters
spacing/containment layout: design-layout + design-spacing when active
composition repetition: composition when active
acceptance: design-review + governing domain reviewer
```

Do not classify a border-heavy structural patch as layout-only. Do not classify all lines as invalid without resolving the genre and its exception contract.

## Repeated-treatment audit

Before production and again before acceptance, inventory repeated treatments introduced or materially increased by the patch.

```yaml
repeated_treatment_audit:
  genre_contract_reference:
  - treatment: <border | divider | card | panel | shadow | accent | badge | other>
    locations: []
    count_before:
    count_after:
    named_roles: []
    functional_exception_reason:
    role_consistency:
    genre_fit:
    personality_fit:
    simpler_valid_alternative:
    verdict: preserve | reduce | replace | remove | not_verified
```

Ask:

```text
Does every repeated treatment have a named semantic, interaction,
system, compositional, emotional, or genre-supported role?

Is the treatment carrying hierarchy that should instead come from
space, alignment, type, sequence, contrast, or content grouping?

Did one useful local treatment become the default grammar for every region?

Does a claimed exception match the canonical genre reference?

Does the cumulative result still belong to the same surface family?
```

A treatment is not invalid because it is frequent or because it is a line. It fails when its frequency has no supported role, conflicts with the selected genre or visual-personality locks, or replaces clearer relational hierarchy.

## Verification record

```yaml
visual_continuity_report:
  baseline_reference:
  genre_contract_reference:
  surface_family_traits_checked: []
  changed_expression_layers: []
  specialist_routes: []
  repeated_treatment_audit: []
  functional_exceptions: []
  preserved_traits: []
  intentional_changes: []
  observed_drift: []
  evidence:
    rendered: []
    runtime: []
    source: []
  verdict: PASS | FAIL | PARTIAL | NOT_VERIFIED
```

`PASS` requires rendered evidence for visual and optical claims. Source inspection can verify class changes, treatment counts, and declared exception reasons, but not the final personality, rhythm, balance, or cumulative visual weight.

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
  → resolve or inherit zen-minimalist through design-genre
  → load design-genre/references/zen.md
  → inherit Seijaku, Ma, Kanso, structural-line budget, and allowed exceptions
  → detect expression change despite IA being the primary layer
  → route visual specialists
  → audit repeated borders and panels
  → preserve the improved IA while correcting only the expression layer
  → retain any genuinely necessary line with an explicit functional reason
```

This case does not establish a universal low-border rule or a universal ban on lines. It establishes that redesign must preserve or intentionally supersede evidenced visual personality through the canonical genre contract, explicit exception reasoning, and reviewable evidence.
