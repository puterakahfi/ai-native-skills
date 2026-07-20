# GitHub Profile Verification

A README source file is implementation input. Acceptance requires rendered evidence, factual checks, profile-surface consistency, repository verification, and honest coverage.

## Verification Boundary

```text
source verification    → syntax, facts, links, dependencies, maintainability
render verification    → hierarchy, spacing, density, assets, theme, narrow width
variant verification   → fact invariance, material difference, brand fit
surface verification   → identity metadata, README, pins, CTA, destinations
repository verification→ visibility, state, proof role, metadata, README quality
facade review          → applicable universal/static design gates
profile acceptance     → GitHub-specific checks from this skill
```

Do not collapse these layers into “Markdown looks valid” or “the profile looks nice.”

## Evidence States

```text
OBSERVED | RECOMMENDED | APPROVED | REJECTED | NOT_VERIFIED | NOT_APPLICABLE
```

Use these states for pins, repository health, lifecycle recommendations, enhancements, and mutations.

## Render Matrix

Minimum for a generated or materially redesigned README:

```yaml
render_matrix:
  - viewport: desktop
    theme: light
    evidence: screenshot-or-direct-render
  - viewport: narrow
    theme: light
    evidence: screenshot-or-direct-render
```

Add dark-theme renders when assets, colors, generated cards, tables, or theme-dependent images are used.

Use actual GitHub rendering when possible. Equivalent GFM is preflight evidence, not full platform parity.

## Profile-Surface Evidence Matrix

For `profile-surface` or `full-profile-ecosystem` scope:

```yaml
profile_surface_evidence:
  identity_metadata: OBSERVED | NOT_VERIFIED
  readme_source: OBSERVED | NOT_VERIFIED
  readme_render: OBSERVED | NOT_VERIFIED
  current_pins: OBSERVED | NOT_VERIFIED
  selected_repository_state: OBSERVED | NOT_VERIFIED
  repository_metadata: OBSERVED | PARTIAL | NOT_VERIFIED
  repository_readmes: OBSERVED | PARTIAL | NOT_VERIFIED
  contribution_context: OBSERVED | NOT_VERIFIED | NOT_APPLICABLE
  external_destinations: OBSERVED | PARTIAL | NOT_VERIFIED
```

Absence of evidence is `NOT_VERIFIED`, not a failed profile.

## Variant Comparison Matrix

```yaml
variant_render_matrix:
  locked_fact_set: <one verified identity, project, link, and claim set>
  locked_content_completeness: true
  viewports: [desktop, narrow]
  theme_conditions: equivalent
  renderer: equivalent
  variants: []
```

Verify equal facts, projects, links, proof strength, and repository truth. A variant is not distinct when only headings, colors, or icon families change.

## Source Checks

```text
□ README exists at the intended root path
□ activation requirements are satisfied when activation is claimed
□ heading order is semantic and one identity anchor exists
□ every factual claim has supplied or verifiable provenance
□ links resolve to intended destinations
□ relative assets exist
□ external dependencies are declared and non-critical
□ no secrets, private repository details, or unintended personal data are exposed
□ source remains human-editable and reasonably small
□ profile-surface scope and observation states are declared when applicable
```

## Render Checks

### Opening hierarchy

```text
Can a new visitor identify the person, positioning, intended audience/value,
and a proof cue before decorative modules dominate?
```

### Content flow

```text
Does order follow visitor questions?
Are project modules more prominent than generic tool collections?
Is the primary action visually and verbally clear?
```

### Composition and readability

```text
Is there one dominant opening treatment?
Do section weights and whitespace create meaningful rhythm?
Are paragraphs and link labels appropriate for the medium?
Do badges, images, and tables avoid horizontal scrolling?
Is body meaning semantic rather than baked into images?
```

### Theme and assets

```text
Do transparent and theme-aware assets retain contrast?
Does the profile remain coherent when external images or services fail?
Are animations optional, accessible, and non-blocking?
```

### Authenticity and proof

```text
Does every selected project explain contribution rather than only technology?
Are current, maintenance, experimental, legacy, private, and archived states honest?
Are metrics supporting context rather than the main credibility mechanism?
```

### Variant expression

```text
Does the render express declared variant axes?
Does the variant remain inside the brand grammar?
Is the differentiation device visible without dominating proof?
Would another variant produce a materially different reading experience with the same facts?
```

## Cross-Surface Checks

```text
□ profile bio and README positioning do not contradict each other
□ README selected work and pinned repositories support the same narrative
□ public proof links are actually accessible
□ private products are not labelled as public source proof
□ CTA destinations work and match audience intent
□ brand grammar remains coherent across profile and external destinations
□ current-focus statements have explicit provenance or date
```

A README can pass while the full profile surface remains `PARTIAL` or `NOT_VERIFIED`.

## Pin Verification

GitHub permits a bounded pin set. Verify only what is observable.

```text
□ current pins are tool-observed or explicitly NOT_VERIFIED
□ each recommended pin has a proof role
□ recommended pins are publicly inspectable when used as public proof
□ pin set is complementary rather than repetitive
□ pin order follows visitor decision value
□ empty slots are allowed when candidates are weak
□ unpin recommendations preserve valuable history and user intent
```

Do not infer current pins from repository search order or README links.

## Repository Hygiene Verification

For each selected proof repository:

```text
□ repository visibility and archived state are observed
□ name and description communicate purpose
□ homepage points to the intended destination
□ topics are relevant and not keyword spam
□ root README explains what, why, status, use, and contribution/ownership as needed
□ license and reuse expectations are coherent when relevant
□ CI/release badges describe real state
□ broken links and stale claims are reported
□ collaboration pathways exist when invited
```

Use `PARTIAL` when only repository visibility/state are verified.

## Lifecycle Verification

Archive recommendations require evidence and approval:

```text
□ repository is intentionally no longer active
□ README/description can explain historical or replacement context
□ issues and pull requests were considered
□ downstream links, packages, docs, and deployments were considered
□ user or governing workflow approved the lifecycle action
```

Never archive automatically from age, size, star count, or naming alone.

## Enhancement Verification

For every banner, badge, icon, stat card, counter, generated SVG, certification, or animation:

```text
□ intended job is explicit
□ decision and evidence value are stated
□ brand fit is acceptable
□ visual and narrow-width cost are bounded
□ accessibility and motion risks are handled
□ external service and maintenance owner are declared
□ semantic fallback exists
□ metric interpretation is honest
□ status is APPROVED, RECOMMENDED, REJECTED, or NOT_VERIFIED
```

Reject activity-as-impact, top-languages-as-expertise, visitor-count-as-trust, or stars-as-ownership framing.

## CTA Verification

```text
hiring     → inspect relevant work, then contact/resume
consulting → understand fit, then discuss a problem
freelance  → inspect shipped work, then request availability
open-source→ inspect repositories, then contribute/discuss/sponsor
founder    → inspect products, then partner/collaborate
personal-brand → explore authored work, then read/follow/connect
community  → find support/contribution paths
```

The primary CTA must match the declared audience and goal.

## Design Review Handoff

Until `design-review` registers a dedicated developer-profile reviewer:

```yaml
design_review_input:
  design_domain: other
  surface_profile: other
  artifact_state: rendered-static
  review_depth: focused | full
  viewing_context:
    - GitHub profile page
    - desktop and narrow width
    - light theme
    - dark theme when applicable
  focus:
    - hierarchy
    - composition
    - readability
    - required content fidelity
    - brand consistency
    - variant expression
    - image and link integrity
    - cross-surface consistency when observed
```

Use applicable universal gates and adjacent static-visual knowledge only. Complete domain approval remains `LIMITED REVIEW` until suitable coverage exists.

## Skill-Specific Acceptance

```yaml
github_profile_acceptance:
  activation_requirements: PASS | FAIL | NOT_VERIFIED | NOT_APPLICABLE
  fact_provenance: PASS | FAIL | PARTIAL | NOT_VERIFIED
  opening_clarity: PASS | FAIL | PARTIAL | NOT_VERIFIED
  project_proof: PASS | FAIL | PARTIAL | NOT_VERIFIED | NOT_APPLICABLE
  visual_restraint: PASS | FAIL | PARTIAL | NOT_VERIFIED
  graceful_degradation: PASS | FAIL | PARTIAL | NOT_VERIFIED
  theme_and_narrow_width: PASS | FAIL | PARTIAL | NOT_VERIFIED
  accessibility: PASS | FAIL | PARTIAL | NOT_VERIFIED
  link_and_asset_integrity: PASS | FAIL | PARTIAL | NOT_VERIFIED
  maintainability: PASS | FAIL | PARTIAL | NOT_VERIFIED
  variant_fact_invariance: PASS | FAIL | PARTIAL | NOT_VERIFIED | NOT_APPLICABLE
  variant_distinctness: PASS | FAIL | PARTIAL | NOT_VERIFIED | NOT_APPLICABLE
  variant_brand_fit: PASS | FAIL | PARTIAL | NOT_VERIFIED | NOT_APPLICABLE
  profile_surface_consistency: PASS | FAIL | PARTIAL | NOT_VERIFIED | NOT_APPLICABLE
  pin_curation: PASS | FAIL | PARTIAL | NOT_VERIFIED | NOT_APPLICABLE
  repository_hygiene: PASS | FAIL | PARTIAL | NOT_VERIFIED | NOT_APPLICABLE
  enhancement_governance: PASS | FAIL | PARTIAL | NOT_VERIFIED | NOT_APPLICABLE
  cta_alignment: PASS | FAIL | PARTIAL | NOT_VERIFIED | NOT_APPLICABLE
  mutation_evidence: PASS | FAIL | PARTIAL | NOT_VERIFIED | NOT_APPLICABLE
```

These are domain checks, not canonical `design-review` gate IDs.

## Delivery Rules

```text
READY
  selected scope checks pass or have explicit non-blocking gaps
  rendered evidence exists for materially changed README
  factual provenance and destinations are sufficient
  profile-surface recommendations distinguish observed from proposed
  facade coverage and verdict are honest

NEEDS REFINEMENT
  hierarchy, density, proof, pins, repository presentation, CTA,
  fallback, accessibility, theme, brand fit, or enhancement governance fail

NOT VERIFIED
  unavailable profile state, missing render, missing provenance,
  unobserved pins, untested dependencies, or unavailable repository metadata

BLOCKED
  private-data exposure, fabricated claims, unequal variant facts,
  broken critical proof, destructive action without approval,
  missing write authority, or unresolved preservation conflict
```

## Correction Ownership

```text
positioning/content order → design-strategy / content-strategy / copywriting
scope/surface inventory   → github-profile / profile-ecosystem
pin and repo curation     → github-profile / repository-curation
variant selection         → github-profile variant-selection + master-design
variant expression        → selected variant reference + design-visual
hierarchy/composition     → design-visual / composition / visual-hierarchy
readability/density       → readability / design-foundation / design-spacing
enhancement policy        → enhancement-decision-matrix / accessibility
GitHub platform behavior  → platform constraints
repository mutation       → calling workflow and repository write owner
factual claim             → user or authoritative source
```

Fix the smallest causal layer. Do not replace the whole profile because one repository, widget, or section fails. Do not add decoration to compensate for weak proof.

## Regression Evidence

Add reusable natural-language cases under `contracts/tests/github-profile.test.yaml` for README, variant, ecosystem, curation, CTA, metric interpretation, enhancement governance, and mutation-evidence failures.
