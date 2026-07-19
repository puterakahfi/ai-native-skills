# Redesign Quality Levels

Use this contract to prevent two opposite failures:

1. a first implementation that is random, taste-led, or missing basic design foundations;
2. a false `pixel-perfect` claim made before the artifact has been rendered and inspected.

Quality level is an **evidence and claim boundary**. It supplements but never overrides decision provenance, confirmed scope, preservation locks, concurrency integrity, canonical gate status, primary-domain coverage, or the `design-review` facade verdict.

## Default quality promise

```text
FIRST PRODUCTION OUTPUT
  must be foundation-safe, direction-consistent, system-aware, and non-random

FINAL APPROVED OUTPUT
  targets pixel-polished by default

PIXEL-MATCHED OUTPUT
  requires a locked reference or measurable specification
```

The workflow must produce the strongest first pass that available evidence allows. Verification is not permission to postpone typography, layout, spacing, hierarchy, grouping, balance, flow, accessibility, or responsive thinking until later.

## Quality levels

### Q0 — Unresolved

```text
- foundation-axis contract incomplete
- brand/design-system locks unresolved
- content, route, behavior, or interaction dependencies unresolved
- direction chosen from agent taste rather than evidence
- required ownership, scope, or approval boundary unresolved
```

Q0 must not enter production.

### Q1 — Foundation-safe

The implementation has been produced from an explicit foundation contract.

```text
□ F1 hierarchy and semantic roles resolved
□ F2 grouping relationships resolved
□ F3 structural and optical alignment approach declared
□ F4 spacing rhythm distinguishes relationship levels
□ F5 visual weight intentionally distributed
□ F6 reading/task flow declared
□ F7 typography, measure, and contrast planned for real use
□ F8 existing tokens and repeated roles remain coherent
□ F9 accessibility and affordance baseline preserved
□ F10 responsive transformation rules declared
□ genre, brand, content, product, and domain constraints propagated
□ no arbitrary component or decoration chosen only from agent preference
□ production respects confirmed scope, locks, ownership, and decision provenance
```

F1–F10 are foundation axes, not canonical score IDs. Any reported or scored finding uses the registered G/R/C/H/I/T/RI/CRO/SV/PR/BI identifiers owned by `design-review` and its domain reviewers.

Q1 is the minimum acceptable first production output. It may be source-complete, but it is not yet a final visual claim.

Allowed language:

```text
foundation-safe first pass
high-quality implementation candidate
ready for rendered verification
```

Forbidden language at Q1:

```text
pixel-perfect
pixel-polished
final visual pass
fully verified
release-ready
```

### Q2 — Render-verified

Q1 plus fresh inspection of the actual rendered or exported artifact using domain-appropriate evidence.

```text
□ required routes, states, slides, exports, or artifact variants render successfully
□ intended fonts and assets load
□ required viewports, dimensions, orientations, or delivery contexts are inspected
□ required themes and states are inspected
□ content wrapping, line breaks, crop, and safe areas are inspected where applicable
□ overflow, clipping, overlap, stranded space, and substitution behavior are inspected
□ hierarchy, grouping, balance, alignment, flow, and legibility are inspected at actual size
□ interactive states and keyboard/touch/gesture behavior are exercised when applicable
□ runtime, console, export, or specialist production errors are checked where applicable
```

Q2 means the artifact has current visual evidence. It does not automatically mean every optical detail is finished or every delivery gate passes.

### Q3 — Pixel-polished

Q2 plus a deliberate optical correction and regression pass.

```text
□ repeated glyph, icon, baseline, image, and control relationships are optically aligned
□ parent/child/sibling hierarchy is unmistakable in every required context
□ spacing rhythm communicates grouping without accidental flatness
□ visual weight remains balanced at representative crops, states, and scroll positions
□ responsive/adaptive transformations preserve semantic grouping and intended order
□ no known typography, layout, spacing, hierarchy, alignment, asset, or state regression remains
□ changed regions and adjacent regions are re-inspected after the final patch
□ applicable canonical foundation, system, genre, domain, accessibility, runtime, and fidelity gates pass
□ provenance, scope, concurrency, preservation, and acceptance requirements pass
```

Q3 is the default final visual quality target for redesign delivery. It does not authorize deployment or merge by itself.

Allowed language:

```text
pixel-polished
rendered and optically corrected
release-ready visual implementation
```

### Q4 — Pixel-matched

Q3 plus comparison against a locked visual reference or measurable design specification.

Required evidence:

```text
□ reference viewport/dimensions, fonts, assets, content, and target states are locked
□ comparison method is declared: overlay, visual diff, measurements, or equivalent
□ accepted tolerance is declared
□ position, size, spacing, typography, color, radius, imagery, and state differences are checked
□ intentional deviations are documented and approved by the correct authority
```

Q4 may use the phrase `pixel-perfect` only when the user explicitly uses that term and the comparison evidence supports it. Prefer the more accurate phrase `pixel-matched within the declared tolerance`.

Without a locked reference, pixel-matched is `NOT_APPLICABLE`, not failed.

## Verification matrix

Record the applicable matrix before final approval:

```yaml
quality_verification:
  target_level: Q3_PIXEL_POLISHED
  current_level: Q1_FOUNDATION_SAFE
  stable_artifact_or_head: <identifier>
  routes_or_artifacts: []
  viewing_contexts:
    - name: mobile-or-small
      dimensions: <when applicable>
      status: pending
    - name: tablet-or-medium
      dimensions: <when applicable>
      status: pending
    - name: desktop-or-large
      dimensions: <when applicable>
      status: pending
  themes: []
  states: []
  foundation_axes: {}
  canonical_gate_results: {}
  domain_and_genre_results: {}
  runtime_or_export_checks: {}
  optical_corrections: []
  adjacent_regressions_checked: []
  reference_comparison:
    applicable: false
    method: null
    tolerance: null
    approved_deviations: []
  integrity:
    provenance: <status>
    scope: <status>
    concurrency: <status>
    preservation: <status>
  unresolved_gaps: []
```

Use real project breakpoints, artifact dimensions, states, and delivery contexts when known. The three viewport classes are coverage categories for responsive interfaces, not mandatory hardcoded widths or universal requirements for static/presentation work.

## Claim gate

```text
Q1 may be claimed from production evidence.
Q2 requires fresh rendered/exported evidence appropriate to the domain.
Q3 requires Q2 + optical correction + adjacent-regression verification + passing acceptance.
Q4 requires Q3 + locked reference comparison.
```

A successful build cannot advance a visual artifact from Q1 to Q2. A screenshot without required states or contexts cannot advance it to Q3. A high review score cannot override missing evidence, failed hard gates, or blocked integrity.

## Default workflow behavior

```text
foundation contract and verified decisions
→ strongest evidence-backed first production output (Q1)
→ render/export required evidence matrix
→ inspect canonical foundation + domain + genre/brand gates (Q2)
→ optical correction and adjacent-regression loop
→ final stable-artifact re-check and acceptance (Q3)
→ optional locked-reference comparison (Q4)
```

The workflow is successful when the output is non-random from the first pass and the final quality claim matches the evidence actually collected.
