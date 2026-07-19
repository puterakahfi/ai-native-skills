# Brand Identity Evidence and Hard Gates

Use this reference after selecting applicable `BI*` gates.

## Evidence Classes

| Evidence | Suitable for | Limitations |
|---|---|---|
| Brand brief and positioning | BI1, BI2, BI12, BI13 | A vague invented rationale is not evidence. |
| Canonical vector/source artwork | BI5, BI6, BI8, BI10, BI11, BI15 | Source alone does not prove actual-size recognition. |
| Actual-size raster and print tests | BI4, BI7, BI8, BI9, BI13 | Large zoomed previews are insufficient. |
| Overlay and construction comparison | BI5, BI6, BI11 | Mathematical alignment still requires optical interpretation. |
| Lockup and variant matrix | BI8, BI10, BI11, BI12, BI13 | Missing required variant remains NOT_VERIFIED. |
| Application examples | BI9, BI10, BI13, BI14, BI15 | Mockups can hide infeasible production or distorted masters. |
| Audience recognition evidence | BI2, BI4 | Method and audience must match the intended use. |
| Relevant comparison set | BI3, BI16 | Limited comparison does not equal global originality or legal clearance. |
| Production/export package | BI8, BI9, BI10, BI13, BI15 | File existence alone does not prove correct construction. |

## Minimum Evidence by Identity State

```text
concept-only
  brand context
  semantic intent
  primary concept/mark
  realistic recognition view
  declared comparison scope or explicit similarity limitation

primary-mark
  concept-only evidence
  canonical source when available
  actual-size tests
  monochrome/inverse test when required

identity-system
  primary-mark evidence
  required lockups and variants
  clear-space and minimum-size rules
  typography and color systems
  master/export package

application-set
  identity-system evidence
  representative real applications
  production constraints and application comparisons

release review
  complete required identity-system evidence
  all contextual hard gates directly verified
  unresolved legal/trademark questions explicitly handed off
```

## Contextual Hard Gates

A `BI*` gate is hard only when the stated context applies.

```text
BI4 Name and Mark Recognition
  hard when the primary mark, wordmark, initials, or semantic cue must be
  recognizable for the declared use and evidence shows material failure

BI5 Construction Consistency
  hard for identity-system release when approved master variants materially
  change the core construction or cannot be reproduced from one system

BI7 Small-Size Survival
  hard when a declared minimum size, favicon, app icon, label, signage,
  embroidery, engraving, or other constrained use is required

BI8 Monochrome and Inverse
  hard when one-color, reverse, dark/light, print, engraving, stamping,
  or restricted-production use is required

BI9 Clear Space and Minimum Size
  hard when production/application rules are part of the required delivery
  and missing or invalid rules cause crowding or recognition failure

BI10 Lockup System
  hard when multiple required placements cannot be served by the supplied
  lockups without distortion, unreadability, or ad-hoc recomposition

BI11 Variant Consistency
  hard when required variants appear as materially different identities

BI15 Reproduction Readiness
  hard for production handoff when canonical masters or required formats
  are broken, inconsistent, or unavailable

BI16 Similarity Risk Screening
  hard when direct evidence shows obvious close resemblance that creates
  material identity, trust, or legal-escalation risk
```

A triggered hard-gate failure produces `CRITICAL` through the design-review facade. Missing evidence produces `NOT_VERIFIED` and blocks a complete release claim without inventing failure.

## Similarity Screening Boundary

```text
Reviewer may:
  compare the supplied mark with a declared comparison set
  flag close silhouette, construction, monogram, negative-space, or concept patterns
  identify the evidence and degree of design risk
  recommend broader search or legal/trademark specialist review

Reviewer may not:
  guarantee originality
  declare a mark legally registrable
  clear trademark classes or jurisdictions
  replace professional legal search and opinion
```

Risk levels:

```text
LOW
  no material close similarity found in the declared comparison set

MEDIUM
  shared category conventions or notable resemblance require differentiation
  or broader comparison before release

HIGH
  obvious close construction, silhouette, concept, or monogram resemblance
  creates material identity risk and blocks release claim

NOT_VERIFIED
  comparison scope or evidence is insufficient
```

## Evidence Coverage

Use design-review’s common evidence coverage calculation. Keep identity-domain coverage separate from universal visual coverage.

```text
brand-identity-review loaded + sufficient BI evidence
→ ADAPTER_COVERED

brand-identity-review loaded + incomplete BI evidence
→ ADAPTER_COVERED with evidence gaps; verdict cannot exceed evidence

brand-identity-review unavailable
→ LIMITED REVIEW for identity-domain claims
```

## Release Guard

```text
□ Brand context and semantic intent are grounded.
□ Canonical primary mark and required variants are available.
□ Required actual-size tests exist.
□ Required monochrome/inverse behavior is verified.
□ Required lockups, clear space, and minimum sizes are verified.
□ Variant construction remains consistent.
□ Typography and color systems are usable in declared contexts.
□ Master/export assets are reproducible.
□ Similarity risk and legal boundary are explicit.
□ Every contextual hard gate passes or blocks release.
```