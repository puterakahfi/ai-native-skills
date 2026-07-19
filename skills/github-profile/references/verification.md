# GitHub Profile Verification

A README source file is implementation input. Acceptance requires rendered evidence and platform checks.

## Verification Boundary

```text
source verification  → syntax, facts, links, dependencies, maintainability
render verification  → hierarchy, spacing, image behavior, density, theme, narrow width
facade review         → applicable universal/static design gates, evidence, coverage, verdict
profile acceptance    → GitHub-specific checks from this skill
```

Do not collapse these layers into “Markdown looks valid.”

## Render Matrix

Minimum for a generated or materially redesigned profile:

```yaml
render_matrix:
  - viewport: desktop
    theme: light
    evidence: screenshot-or-direct-render
  - viewport: narrow
    theme: light
    evidence: screenshot-or-direct-render
```

Add these when theme-dependent assets, dark-only assets, complex tables, or external widgets are used:

```yaml
  - viewport: desktop
    theme: dark
    evidence: screenshot-or-direct-render
  - viewport: narrow
    theme: dark
    evidence: screenshot-or-direct-render
```

Use the actual GitHub profile render when possible. An equivalent GFM renderer is useful preflight evidence but does not replace GitHub when platform-specific behavior matters.

## Source Checks

```text
□ README exists at the intended root path.
□ Profile repository name and visibility satisfy GitHub requirements when activation is claimed.
□ Heading order is semantic and has one clear H1.
□ Every factual claim has a supplied or verifiable source.
□ All links resolve to the intended destination.
□ Relative assets exist at the committed path.
□ External dependencies are declared and non-critical.
□ No secrets, private repository details, or unintended personal data are exposed.
□ Source remains human-editable and reasonably small.
```

## Render Checks

### Opening hierarchy

```text
Can a new visitor identify the person, positioning, intended audience/value,
and a proof cue before decorative modules dominate?
```

### Content flow

```text
Does section order follow visitor questions?
Are project modules more prominent than generic tool collections?
Is the primary action visually and verbally clear?
```

### Composition

```text
Is there one dominant opening treatment?
Do section weights create a readable rhythm?
Are centered, left-aligned, visual, and text modules used consistently?
Does whitespace separate meaning rather than create arbitrary gaps?
```

### Readability

```text
Are paragraphs concise enough for the medium?
Do badges, images, and tables wrap without horizontal scrolling?
Are link labels meaningful?
Is body text semantic rather than baked into images?
```

### Theme and assets

```text
Do transparent and theme-aware assets retain contrast?
Are light/dark variants equivalent?
Does the profile remain coherent when external images fail?
```

### Authenticity and proof

```text
Does every selected project explain contribution rather than only naming technology?
Are archived, experimental, and current projects labelled honestly?
Are statistics supporting evidence rather than the main credibility mechanism?
```

## Design Review Handoff

Until `design-review` registers a dedicated GitHub/developer-profile reviewer, classify conservatively:

```yaml
design_review_input:
  design_domain: visual-communication
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
    - image and link integrity
```

Use applicable universal gates and only the static visual gates that match this document-like medium. Do not apply poster advertising thresholds or interactive runtime gates.

Because the current built-in static profiles do not explicitly name GitHub Profile README, report primary-domain coverage honestly. Universal/static evidence may support useful findings, but complete domain approval may remain `LIMITED REVIEW` until a dedicated reviewer or registered profile exists.

## Skill-Specific Acceptance

The `github-profile` skill may report its own platform acceptance separately from the facade verdict:

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
```

These are domain acceptance checks, not canonical `design-review` gate IDs. Never prefix them with an invented gate namespace.

## Delivery Rules

```text
READY
  profile checks pass or have explicit non-blocking gaps
  rendered evidence exists
  factual provenance is sufficient
  links/assets are verified
  facade coverage and verdict are reported honestly

NEEDS REFINEMENT
  hierarchy, density, project proof, fallback, accessibility,
  theme, link, or maintainability checks fail

NOT VERIFIED
  no render, unavailable repository, missing factual provenance,
  untested external dependencies, or unavailable theme/narrow evidence

BLOCKED
  private data exposure, fabricated claims, broken critical links,
  missing write authority, or unresolved preservation conflict
```

## Correction Ownership

```text
positioning or content order → design-strategy / content-strategy / copywriting
hierarchy or composition     → design-visual / composition / visual-hierarchy
readability or density       → readability / design-foundation
GitHub platform behavior     → github-profile platform constraints
repository mutation          → calling workflow and repository write owner
factual claim                → user or authoritative public source
```

Fix the smallest causal layer. Do not replace the entire profile because one widget or section fails.

## Regression Evidence

When a reusable failure is found, add a natural-language case under:

```text
contracts/tests/github-profile.test.yaml
```

Good cases distinguish this skill from generic README generation: anti-badge-wall behavior, proof-first project structure, no invented biography, preservation during redesign, and rendered verification.