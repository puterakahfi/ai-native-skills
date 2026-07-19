# Brand Identity Gates

This file is the governing owner reference for canonical `BI*` gates.

Load it only when `brand-identity-review` is selected by the `design-review` facade. Universal composition, typography, color, or static-visual gates may supplement this review, but they do not replace identity-domain gates.

## Applicability

```text
concept-only
  BI1–BI4 and BI6 are usually applicable
  system, reproduction, and application gates may be NOT_VERIFIED or NOT_APPLICABLE

primary-mark
  add BI5–BI9 and BI15 where evidence exists

identity-system
  all system, lockup, variant, typography, color, and reproduction gates apply

application-set
  identity-system gates + BI14 application fidelity

source-only
  construction/reproduction may be inspectable
  rendered recognition and actual-use behavior remain NOT_VERIFIED
```

## Strategy and meaning

| Gate | Review question | Pass evidence |
|---|---|---|
| BI1 Brand Logic Alignment | Does the identity express the declared positioning, audience, category, personality, and values without relying on invented strategy? | Brand brief and identity rationale map clearly to observable visual decisions; no contradiction with the declared brand role. |
| BI2 Concept-to-Symbol Translation | Does the mark translate the intended name, idea, object, metaphor, or relationship into a form people can understand without excessive explanation? | The intended concept is legible through form, negative space, gesture, combination, or lockup; the mark is not merely decorative. |
| BI3 Distinctiveness | Is the identity sufficiently ownable and distinguishable within its relevant category and comparison set while remaining appropriate? | Side-by-side comparison shows a recognizable silhouette, construction, or conceptual move that is not generic category shorthand or a close imitation. |
| BI4 Name and Mark Recognition | Can the intended audience recognize the brand name, initials, symbol, or required semantic cue at the expected viewing size and context? | Direct recognition and reading tests at realistic sizes; critical letterforms or symbols do not collapse into another character or unrelated shape. |

`BI2` evaluates whether meaning becomes form. It covers cases such as integrating “panda” and “mie” into one understandable symbol rather than placing two unrelated icons beside each other.

## Construction and optical quality

| Gate | Review question | Pass evidence |
|---|---|---|
| BI5 Construction Consistency | Do curves, angles, terminals, stroke logic, counters, joins, radii, and repeated geometry belong to one intentional construction system? | Vector/source inspection and overlays show repeatable logic; variants do not introduce accidental structural drift. |
| BI6 Optical Balance | Are visual mass, counters, alignment, spacing, tension, and perceived center balanced at actual viewing sizes rather than only mathematically aligned? | Optical overlays and actual-size inspection show stable weight, intentional correction, and no accidental leaning, crowding, or floating parts. |
| BI7 Small-Size Survival | Does the mark preserve recognition, counters, critical gaps, and silhouette at every declared minimum size and low-detail context? | Pixel and print tests at declared minimum sizes, including favicon/app-icon or small-label use where relevant. |
| BI8 Monochrome and Inverse | Does the identity remain recognizable and structurally correct in one color, reversed, dark/light, and restricted-production contexts? | Approved black, white, and one-color variants preserve counters, hierarchy, and construction without improvised redraws. |
| BI9 Clear Space and Minimum Size | Are clear-space and minimum-size rules derived from the mark and sufficient to protect recognition across real uses? | Measurable rules and placement tests prevent crowding, clipping, and unreadable reproduction without arbitrary excessive space. |

Mathematical symmetry is not required. Optical correction is expected when it improves perceived balance and recognition.

## System and variants

| Gate | Review question | Pass evidence |
|---|---|---|
| BI10 Lockup System | Do horizontal, vertical, symbol-only, wordmark, descriptor, and endorsed lockups form a coherent system for the required contexts? | Required lockups have explicit hierarchy, spacing, alignment, and use rules; no lockup feels like a separate logo. |
| BI11 Variant Consistency | Do all approved variants preserve the same core construction, proportions, semantic idea, and recognition cues? | Overlay and side-by-side comparison show controlled adaptation rather than concept drift, random geometry, or inconsistent detail. |
| BI12 Typography Integration | Does the wordmark or supporting type system match the mark’s structure, rhythm, personality, and practical use without becoming generic or competing? | Letterform customization, type choice, spacing, case, and hierarchy support the symbol and remain readable across required lockups. |
| BI13 Color System Robustness | Does the identity color system provide recognizable brand expression and workable primary, secondary, neutral, accessibility, and restricted-use behavior? | Declared palette roles, contrast/reproduction tests, and monochrome fallback remain coherent across digital and print uses. |
| BI14 Application Fidelity | Do real applications preserve approved construction, spacing, color, typography, and hierarchy without uncontrolled distortion or decorative drift? | Direct comparison of applications against master assets and rules; mockups reflect feasible production rather than hiding defects. |
| BI15 Reproduction Readiness | Are canonical master assets, vector paths, export variants, naming, formats, and production constraints sufficient for consistent handoff? | Clean vectors, outlined/linked asset policy, export matrix, color specifications, and reproducible masters exist for declared channels. |

Variant count is not quality. Ten or thirty variants pass only when they are deliberate members of one system rather than unrelated logo ideas.

## Similarity and originality risk

| Gate | Review question | Pass evidence |
|---|---|---|
| BI16 Similarity Risk Screening | Does the mark avoid obvious close visual, structural, or conceptual similarity to relevant known identities in the declared comparison set? | Documented comparison shows meaningful differences in silhouette, construction, concept, and category context; unresolved risk is escalated. |

`BI16` is a design-risk screen, not legal trademark clearance. A pass means no material issue was found in the supplied comparison scope. It does not guarantee availability across jurisdictions, classes, or unsearched marks.

## Quick Review

```text
BI1 brand logic alignment
BI2 concept-to-symbol translation
BI3 distinctiveness
BI4 name and mark recognition
BI6 optical balance
BI7 small-size survival when size evidence exists
BI16 similarity risk screening when comparison evidence exists
```

Quick review cannot issue a production-ready identity-system claim.

## Finding Example

```yaml
finding:
  gate: BI11
  governing_reviewer: brand-identity-review
  status: FAIL
  region: primary-symbol-variants
  observation: the black and inverse variants change the upper loop geometry and counter width
  evidence:
    - type: overlay
      context: primary, monochrome, and inverse vector masters
  impact:
    user: the mark appears to be different identities across contexts
    delivery: vendors cannot reproduce one stable master construction
  recommendation: derive all color modes from one canonical geometry and vary only approved color/reversal behavior
  confidence: high
  effort: medium
```

Do not collapse multiple construction symptoms into separate penalties when one master-asset defect governs them.