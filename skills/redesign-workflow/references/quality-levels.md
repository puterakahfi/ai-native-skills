# Redesign Quality Levels

Use this contract to prevent two opposite failures:

1. a first implementation that is random, taste-led, or missing basic design foundations;
2. a false `pixel-perfect` claim made before the artifact has been rendered and inspected.

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
- foundation contract incomplete
- brand/design-system locks unresolved
- content, route, or interaction dependencies unresolved
- direction chosen from agent taste rather than evidence
```

Q0 must not enter production.

### Q1 — Foundation-safe

The implementation has been produced from an explicit foundation contract.

```text
□ F1 hierarchy and semantic roles resolved
□ F2 grouping relationships resolved
□ F3 structural alignment system declared
□ F4 spacing rhythm distinguishes group levels
□ F5 visual weight intentionally distributed
□ F6 reading/task flow declared
□ F7 typography, measure, and contrast planned for real use
□ F8 existing tokens and repeated roles remain coherent
□ F9 accessibility and affordance baseline preserved
□ F10 responsive collapse rules declared
□ genre, brand, content, and product constraints propagated
□ no arbitrary component or decoration chosen only from agent preference
```

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
```

### Q2 — Render-verified

Q1 plus fresh inspection of the actual rendered artifact.

```text
□ required routes or artifact variants render successfully
□ intended fonts and assets load
□ required desktop, tablet, and mobile widths inspected
□ required light/dark themes inspected
□ content wrapping and line breaks inspected
□ overflow, clipping, overlap, and stranded space inspected
□ hierarchy, grouping, balance, alignment, and flow inspected at actual size
□ interactive states and keyboard/touch behavior exercised when applicable
□ runtime console or export errors checked
```

Q2 means the artifact has visual evidence. It does not automatically mean every optical detail is finished.

### Q3 — Pixel-polished

Q2 plus a deliberate optical correction and regression pass.

```text
□ repeated glyph, icon, baseline, and control relationships are optically aligned
□ parent/child/sibling hierarchy is unmistakable in every required viewport
□ spacing rhythm communicates grouping without accidental flatness
□ visual weight remains balanced at representative crops and scroll positions
□ responsive stacking preserves semantic grouping and intended order
□ no known typography, layout, spacing, hierarchy, alignment, or state regression remains
□ changed regions and adjacent regions were re-inspected after the final patch
□ foundation, system, genre, domain, accessibility, and runtime gates pass
```

Q3 is the default final quality target for redesign delivery.

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
□ reference viewport, dimensions, fonts, assets, and content are locked
□ comparison method is declared: overlay, visual diff, measurements, or equivalent
□ accepted tolerance is declared
□ position, size, spacing, typography, color, radius, and state differences are checked
□ intentional deviations are documented and approved
```

Q4 may use the phrase `pixel-perfect` only when the user explicitly uses that term and the comparison evidence supports it. Prefer the more accurate phrase `pixel-matched within the declared tolerance`.

Without a locked reference, pixel-matched is `NOT_APPLICABLE`, not failed.

## Verification matrix

Record the applicable matrix before final approval:

```yaml
quality_verification:
  target_level: Q3_PIXEL_POLISHED
  current_level: Q1_FOUNDATION_SAFE
  routes_or_artifacts: []
  viewports:
    - name: mobile
      size: <width x height>
      status: pending
    - name: tablet
      size: <width x height>
      status: pending
    - name: desktop
      size: <width x height>
      status: pending
  themes: []
  states: []
  foundation_gates: {}
  genre_or_brand_gates: {}
  runtime_checks: {}
  optical_corrections: []
  adjacent_regressions_checked: []
  reference_comparison:
    applicable: false
    method: null
    tolerance: null
    approved_deviations: []
  unresolved_gaps: []
```

Use real project breakpoints and states when known. The three named viewport classes are coverage categories, not mandatory hardcoded pixel widths.

## Claim gate

```text
Q1 may be claimed from production evidence.
Q2 requires fresh rendered evidence.
Q3 requires rendered evidence + optical correction + regression verification.
Q4 requires Q3 + locked reference comparison.
```

A successful build cannot advance a visual artifact from Q1 to Q2. A screenshot without required states or viewports cannot advance it to Q3. A high review score cannot override missing evidence.

## Default workflow behavior

```text
foundation contract
→ strongest evidence-backed first production output (Q1)
→ render required matrix
→ inspect foundation + domain + genre/brand gates (Q2)
→ optical correction and adjacent-regression loop
→ final rendered re-check (Q3)
→ optional locked-reference comparison (Q4)
```

The workflow is successful when the output is non-random from the first pass and the final quality claim matches the evidence actually collected.
