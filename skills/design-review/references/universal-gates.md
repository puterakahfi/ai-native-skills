# Universal Gates

Load this reference for every visual review. These gates evaluate principles that apply across interactive products, static marketing visuals, and presentations.

`design-foundation` owns the universal composition knowledge. This file is its review adapter: it maps hierarchy, grouping, alignment, spacing, balance, flow, legibility, consistency, accessibility, and responsive continuity into evidence-backed review gates.

```text
FOUNDATION SOURCE OF TRUTH
  skills/design-foundation/SKILL.md
  skills/design-foundation/references/principles.md
  skills/design-foundation/references/gates.md

UNIVERSAL REVIEW ADAPTER
  this file

GENRE / DOMAIN EXTENSIONS
  selected genre + surface/domain gates
```

Use profile-specific thresholds from `review-profiles.md`, `interactive-surface-gates.md`, or `static-visual-gates.md`. Do not turn one implementation heuristic into a universal law.

Existing gate IDs are retained where practical so earlier audit and refinement reports remain understandable.

## Applicability

```text
Rendered visual available           → score visual gates
Source or tokens available          → score implementation/system consistency gates
No rendered visual                  → visual gates are NOT_VERIFIED
No declared system or repeated set  → token gates may be NOT_APPLICABLE
```

## Foundation-axis mapping

F1–F10 are **foundation axes**, not canonical reportable gate IDs. Every scored or reported finding must use the registered canonical IDs shown on the right.

```text
F1  Hierarchy                   → G2, G8, R7, H1, H2, H3
F2  Grouping                    → G4, G5, G7, G12
F3  Alignment                   → C3, G7, R3
F4  Space + Rhythm              → G5, R3, G4
F5  Balance                     → C1, C2, R6, R8
F6  Flow                        → G8, G12, H2 + applicable surface gates
F7  Legibility                  → G2, G9, G10, G11, R1
F8  System Consistency          → G1, G3, R2
F9  Accessibility + Affordance  → G10 + applicable interactive/static hard gates
F10 Responsive Continuity       → C3, G5, G7 + responsive surface gates
```

A universal score cannot override a verified foundation-axis failure. The final verdict records the axis assessment, but findings and scores use canonical gate IDs from the registry.

## Design consistency

| Gate | Review question | Pass evidence |
|---|---|---|
| G1 System Consistency | Are repeated colors, type roles, spacing, radius, stroke, shadows, and component treatments governed consistently? | Declared tokens/styles or visibly consistent repeated decisions; exceptions have a reason. |
| G3 Color Semantics | Does each functional color communicate a stable role without collapsing unrelated meanings? | Primary action, status, warning, selection, and decoration remain distinguishable where present. |
| G4 Figure/Ground | Are foreground, background, grouping, and depth relationships clear for the intended medium? | Content layers are distinguishable without unnecessary decoration or weak low-contrast separation. |

Do not fail G1 merely because a one-off poster has no software token file. Evaluate whether repeated visual decisions are internally consistent.

## Typography and readability

| Gate | Review question | Pass evidence |
|---|---|---|
| G2 Typographic Scale | Does the type scale express the intended hierarchy without display text overwhelming content or body text becoming subordinate noise? | Roles are visually distinct at the actual viewport, export size, or viewing distance. |
| G9 Reading Measure | Are line length, line breaks, paragraph width, and text grouping suitable for the content and medium? | Text can be scanned and read without excessive eye travel, orphaned fragments, or dense walls. |
| G10 Contrast | Is text and essential graphical information distinguishable from its background and adjacent elements? | Measured contrast when implementation evidence exists; visual and channel checks for static artifacts. |
| G11 Type Legibility | Are size, weight, leading, tracking, case, and rendering suitable for the intended device, distance, and resolution? | Critical text survives actual-size inspection, not only zoomed canvas inspection. |
| G12 Cognitive Ease | Is content chunked and phrased so the intended message or task can be understood without unnecessary decoding? | Labels, headings, paragraphs, numbers, and supporting copy have clear roles and manageable density. |
| R1 Type Roles | Are display, heading, body, label, data, and annotation roles distinct enough for the context? | Distinction may use family, size, weight, width, case, spacing, or placement; a second font family is not mandatory. |

Profile guidance:

```text
Web prose: body commonly starts around 16px and sustained prose commonly stays near 45–75ch.
Mobile: evaluate platform text scaling, localization, and constrained width.
Poster/social: test at actual feed/story/thumbnail size and expected viewing distance.
Presentation: test at room or screen-share scale, not only editor zoom.
```

These are starting points, not automatic pass/fail values detached from context.

## Spacing, grouping, layout, and alignment

| Gate | Review question | Pass evidence |
|---|---|---|
| G5 Spatial Rhythm | Do spacing changes express grouping, sequence, and emphasis rather than repeating one gap everywhere? | Related elements cluster; parent-to-child-group separation is stronger than sibling separation when applicable; major section boundaries have one deliberate spacing owner instead of accidental compounded intervals. |
| G7 Layout Logic | Does the layout structure match content quantity, priority, comparison needs, and viewing context? | Column count, grouping, stacking, and alignment support the content instead of forcing it. |
| R3 Space System | Are repeated spacing decisions consistent enough to create rhythm and implementation stability? | Named tokens or a coherent base grid where source exists; visually consistent relational intervals for static artifacts. |
| C3 Alignment | Do elements align to meaningful anchors, grids, optical relationships, or intentional exceptions? | No accidental drift, almost-aligned edges, or unexplained floating elements. |

Grouping review must explicitly compare:

```text
within item
between siblings
parent → child group
between major sections
```

For each major transition, inspect the effective interval after adjacent margins, paddings, layout gaps, and wrappers combine. A large transition may be valid, but its structural job and spacing owner must be clear. Do not approve an unintended double interval merely because both individual section tokens are valid in isolation.

Do not require every distance to be identical or every element to sit on a mathematically rigid grid. Optical correction is valid when intentional and consistent.

## Composition and balance

| Gate | Review question | Pass evidence |
|---|---|---|
| C1 Focal Point | Is the intended first point of attention clear in the actual viewing context? | The eye reaches the main message, task, product, or data without competing anchors. |
| C2 Weight Distribution | Is visual weight distributed intentionally across the frame, page, viewport, or slide? | Heavy elements, empty space, imagery, type, and accents create stable or intentionally dynamic balance. |
| R6 Composition Intent | Is symmetry, asymmetry, centering, density, or openness chosen for a reason rather than inherited from a template? | The composition supports content and brand; asymmetry is not mandatory. |
| R8 Restraint | Does every visible element have a communication, interaction, structural, or brand role? | Decoration does not fill empty space blindly or compete with primary content. |

Balance is not the same as symmetry. Review optical mass, direction, scale, contrast, density, and empty space together.

## Visual hierarchy and flow

| Gate | Review question | Pass evidence |
|---|---|---|
| G8 First Impression | Can the viewer identify the primary message or task within the expected attention window? | Opening hierarchy communicates purpose before details. |
| R7 Hierarchy | Are importance levels distinguishable without too many competing weights? | Dominant, supporting, and tertiary roles are clear; exceptions are purposeful. |
| H1 Dominant/Supporting | Is the relationship between the primary anchor and supporting content unambiguous? | Supporting content reinforces rather than competes with the primary anchor. |
| H2 Cross-Section Decay | Across a long page, deck, or multi-region artifact, does later content preserve the intended global hierarchy and flow? | A secondary section or slide element does not accidentally overpower the primary narrative anchor; the next region remains discoverable. |
| H3 Role Taxonomy | Can headings, labels, statements, metadata, and annotations be identified by role? | Similar roles look related; different roles do not collapse into one style. |

Nested hierarchy should use at least two cues when spacing or typography alone remains ambiguous. Do not enforce a universal numeric H2/H1 ratio. Use measured ratios as evidence only when they explain an observed hierarchy problem.

## Color and expression

| Gate | Review question | Pass evidence |
|---|---|---|
| R2 Color Control | Is color quantity, saturation, and contrast controlled according to brand and communication need? | Accents retain meaning; multiple hues are acceptable when the system or message requires them. |
| R5 Voice | Do visual and verbal tone form a specific, coherent register appropriate to product, audience, and brand? | The result does not fall into generic neutral SaaS, generic luxury, or generic AI language without justification. |

Do not use fixed rules such as “one accent hue” or “accent below five percent” as universal gates. They may be useful heuristics for a declared restrained direction, not for every design.

## Content integrity

| Gate | Review question | Pass evidence |
|---|---|---|
| CP1 Message Specificity | Is the main message, offer, task, or claim specific enough for the intended audience to understand? | Avoids interchangeable claims and unexplained abstraction. |
| CP2 Content Proportion | Is the amount of copy suitable for its region and viewing context? | No arbitrary word cap; content length supports comprehension and action. |
| CP3 No Slop | Is the artifact free from generic filler, fake proof, unearned claims, and template-driven content patterns? | Language and content structure are grounded in the actual product or message. |

Examples of automatic review flags, not automatic failures:

```text
“seamless”, “world-class”, “cutting-edge”, or “modern solution” without evidence
fake logo strips, ratings, testimonials, or usage counts
six or more equal-weight cards with no prioritization
headline + three generic benefits + CTA copied without product-specific logic
decoration that mimics current AI design trends but weakens the message
color-only status communication
```

A flag becomes a failed gate only when evidence shows it harms clarity, truth, accessibility, brand, or task performance.

## Foundation failure handoff

```text
failure appears across genres or surfaces
  → design-foundation knowledge or workflow orchestration defect

foundation rule exists but one implementation ignores it
  → local implementation defect

one repeated component pattern fails everywhere
  → component-system defect

failure is stricter stylistic expression only
  → design-genre defect
```

Examples:

```text
parent/child/sibling hierarchy collapses in zen, SaaS, and editorial
  → foundation defect

only zen page exceeds its structural-line budget
  → genre defect

one SectionHeader component misaligns every eyebrow
  → component-system defect
```

## Universal quick review

For a quick review, assess the applicable foundation axes through canonical gate IDs:

```text
F1  hierarchy / role clarity
F2  grouping
F3  alignment
F4  spatial rhythm
F5  balance
F6  flow
F7  legibility

Canonical scoring subset:
G10 contrast
CP1 message specificity
applicable registered accessibility/responsive gates
```

Any score below 5 is critical. Continue to profile-specific hard gates before declaring the artifact safe or release-ready.
