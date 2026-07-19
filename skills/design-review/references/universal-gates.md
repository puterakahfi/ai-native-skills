# Universal Gates

Load this reference for every visual review. These gates evaluate principles that apply across interactive products, static marketing visuals, and presentations.

`design-foundation` owns the universal composition knowledge. This file is its review adapter: it maps hierarchy, grouping, figure-ground, semantic layering, content resilience, alignment, spacing, balance, flow, legibility, consistency, accessibility, and responsive continuity into evidence-backed review gates.

```text
FOUNDATION SOURCE OF TRUTH
  skills/design-foundation/SKILL.md
  skills/design-foundation/references/principles.md
  skills/design-foundation/references/gates.md
  skills/design-foundation/references/figure-ground-layering.md
  skills/design-foundation/references/content-resilience.md

FOUNDATION REGRESSION FIXTURES
  skills/design-foundation/references/figure-ground-fixtures.md
  skills/design-foundation/references/content-resilience-fixtures.md

UNIVERSAL REVIEW ADAPTER
  this file

GENRE / DOMAIN EXTENSIONS
  selected genre + surface/domain gates
```

Use profile-specific thresholds from `review-profiles.md`, `interactive-surface-gates.md`, or `static-visual-gates.md`. Do not turn one implementation heuristic or placeholder dataset into a universal law.

Existing gate IDs are retained where practical so earlier audit and refinement reports remain understandable.

## Applicability

```text
Rendered visual available             → score visual gates
Source or tokens available            → score implementation/system consistency gates
Rendered interaction available        → verify dynamic layer, state, overflow, focus,
                                        adaptation, and continuity behavior
Representative content variants       → verify supported bounds and resilience
No rendered visual                    → visual gates are NOT_VERIFIED
No declared system or repeated set    → token gates may be NOT_APPLICABLE
Screenshot only                       → scroll, focus, dismissal, recovery, pagination,
                                        and adaptive behavior remain NOT_VERIFIED
Single ideal content state only       → resilience remains NOT_VERIFIED for variable-content surfaces
Fixed one-off artifact with final copy → dynamic states may be NOT_APPLICABLE
```

## Foundation-axis mapping

F1–F10 are **foundation axes**, not canonical reportable gate IDs. Every scored or reported finding must use the registered canonical IDs shown on the right.

```text
F1  Hierarchy                   → G2, G8, R7, H1, H2, H3
F2  Grouping                    → G4, G5, G7, G12
F3  Alignment                   → C3, G7, R3
F4  Space + Rhythm              → G5, R3, G4, G7, CP2
F5  Balance                     → G4, C1, C2, R6, R8
F6  Flow                        → G8, G12, H2 + applicable surface gates
F7  Legibility                  → G2, G9, G10, G11, G12, R1, CP2
F8  System Consistency          → G1, G3, R2, G7
F9  Accessibility + Affordance  → G10 + applicable interactive/static hard gates
F10 Responsive Continuity       → G4, C3, G5, G7 + responsive surface gates
```

A universal score cannot override a verified foundation-axis failure. The final verdict records the axis assessment, but findings and scores use canonical gate IDs from the registry.

## Design consistency

| Gate | Review question | Pass evidence |
|---|---|---|
| G1 System Consistency | Are repeated colors, type roles, spacing, radius, stroke, shadows, semantic layers, components, fallbacks, and content-adaptation policies governed consistently? | Declared tokens/styles or visibly consistent repeated decisions; exceptions have a reason; arbitrary z-index or local overflow hacks do not replace semantic ownership. |
| G3 Color Semantics | Does each functional color communicate a stable role without collapsing unrelated meanings? | Primary action, status, warning, selection, and decoration remain distinguishable where present. |
| G4 Figure/Ground | Are foreground, background, containment, depth, overlap, and occlusion relationships clear for the intended medium and state? | Content layers are distinguishable; surfaces clarify ownership; depth expresses containment/priority/transience/focus/state; required content/actions remain unobscured; text and symbols survive their real background, crop, theme, and viewport. |

Do not fail G1 merely because a one-off poster has no software token file. Evaluate whether repeated visual decisions are internally consistent.

### Figure-ground and layer review

When imagery, surfaces, overlap, sticky/fixed UI, floating controls, popovers, drawers, dialogs, or depth effects are present, identify:

```text
canvas
content
containment
floating layer
modal/blocking layer
system/critical layer
```

Not every artifact needs every layer. For each meaningful overlap or elevated region, inspect:

```text
- what owns the layer?
- what relationship or state does its depth communicate?
- what content may it obscure, for how long, and why?
- what safe region must remain visible and reachable?
- does it stay attached to its trigger, subject, or task?
- what happens after resize, crop, orientation, theme, localization, or text scaling?
- for interactive layers, how does the user continue, dismiss, or recover?
```

Fail `G4` when evidence shows unclear foreground ownership, meaningless depth, detached floating content, background interference, or unintended occlusion. Do not fail only because the design is flat or because it uses little/no shadow.

## Typography, readability, and content shape

| Gate | Review question | Pass evidence |
|---|---|---|
| G2 Typographic Scale | Does the type scale express the intended hierarchy without display text overwhelming content or body text becoming subordinate noise? | Roles remain distinct with realistic short/normal/long content at the actual viewport, export size, or viewing distance. |
| G9 Reading Measure | Are line length, line breaks, paragraph width, wrapping, and text grouping suitable for the content and medium? | Text can be scanned and read without excessive eye travel, orphaned fragments, detached labels/values, or dense walls across supported variants. |
| G10 Contrast | Is text and essential graphical information distinguishable from its background and adjacent elements? | Measured contrast when implementation evidence exists; visual and channel checks for static artifacts; imagery/effects do not create unstable local contrast. |
| G11 Type Legibility | Are size, weight, leading, tracking, case, rendering, and overflow treatment suitable for the intended device, distance, resolution, localization, and text scaling? | Critical text survives actual-size inspection and realistic content variation, not only zoomed canvas or placeholder copy. |
| G12 Cognitive Ease | Is content chunked, labeled, and adapted so the intended message or task can be understood without unnecessary decoding? | Labels, headings, paragraphs, numbers, metadata, missing values, and supporting copy have clear roles and manageable density at declared bounds. |
| R1 Type Roles | Are display, heading, body, label, data, and annotation roles distinct enough for the context? | Distinction may use family, size, weight, width, case, spacing, placement, or content priority; a second font family is not mandatory. |

Profile guidance:

```text
Web prose: body commonly starts around 16px and sustained prose commonly stays near 45–75ch.
Mobile: evaluate platform text scaling, localization, realistic label length, and constrained width.
Poster/social: test final approved copy at actual feed/story/thumbnail size and expected distance.
Reusable template: declare title/body/price/contact/legal/media bounds and unsupported behavior.
Presentation: test realistic titles/data labels at room or screen-share scale, not only editor zoom.
```

These are starting points, not automatic pass/fail values detached from context.

## Spacing, grouping, layout, content density, and alignment

| Gate | Review question | Pass evidence |
|---|---|---|
| G5 Spatial Rhythm | Do spacing and density changes express grouping, content state, sequence, and emphasis rather than repeating one gap/composition everywhere? | Related elements cluster; parent-to-child-group separation is stronger than sibling separation when applicable; major section boundaries have one deliberate spacing owner; empty/sparse/dense states remain intentional. |
| G7 Layout Logic | Does the layout structure and adaptation strategy match content quantity, length, presence, priority, comparison needs, and viewing context? | Column count, grouping, stacking, alignment, containment, wrapping, overflow, pagination, fallback, or component substitution supports the content instead of forcing it. |
| R3 Space System | Are repeated spacing decisions consistent enough to create rhythm and implementation stability? | Named tokens or a coherent base grid where source exists; visually consistent relational intervals for static artifacts and content states. |
| C3 Alignment | Do elements align to meaningful anchors, grids, optical relationships, or intentional exceptions? | No accidental drift, almost-aligned edges, unexplained floating elements, or per-item drift after wrapping/optional content. |

Grouping review must explicitly compare:

```text
within item
between siblings
parent → child group
between major sections
foreground → containing region
floating element → trigger/subject/task
optional content present → absent
one item → many items
short value → long/large value
```

For each major transition, inspect the effective interval after adjacent margins, paddings, layout gaps, and wrappers combine. A large transition may be valid, but its structural job and spacing owner must be clear. Do not approve an unintended double interval merely because both individual section tokens are valid in isolation.

Do not require every distance to be identical or every element to sit on a mathematically rigid grid. Optical correction is valid when intentional and consistent. Cards, borders, surfaces, and fixed heights must not compensate for unresolved proximity, hierarchy, or content bounds.

## Content resilience review

Apply when content can vary or the artifact is a reusable template/system. Record:

```text
SUPPORTED BOUNDS
content source: fixed | curated | generated | user-authored | system/data-driven
quantity: minimum | normal | declared maximum
text/value range: realistic short | normal | long/large
media: required | optional | missing/broken | varied aspect ratio
language/format: locales | scripts | direction | dates/numbers/currency
output: viewports | orientations | crops | delivery contexts

STATES EXERCISED
EMPTY | MINIMUM | NORMAL | MAXIMUM | VARIANT | UNEXPECTED/UNTRUSTED

ADAPTATION STRATEGIES
wrap | clamp | truncate | scroll | paginate | virtualize | summarize |
prioritize | disclose | collapse | fallback | substitute component | fixed-content only

COMBINATIONS EXERCISED
long content + constrained viewport
localization/text scaling + real controls
missing media + dense metadata
large value + constrained column
empty collection + persistent controls
```

Review questions:

```text
- is the supported range explicit rather than inferred from placeholders?
- do critical meaning, identity, comparison, status, and actions survive?
- do optional elements collapse without leaving broken ownership?
- is the adaptation strategy consistent for repeated roles?
- is overflow or disclosure discoverable and appropriate to the task?
- does content stress combine with viewport/format stress?
- is unsupported content constrained or communicated honestly?
```

Canonical reporting:

```text
G7   layout/adaptation strategy and pattern fit
G9   measure, wrapping, line breaks, label/value association
G11  actual-size legibility and overflow treatment
G12  chunking, missing-value clarity, density, cognitive ease
CP2  content amount/proportion for the region and context
G1   repeated adaptation/fallback consistency
G5   empty/sparse/dense rhythm
```

For interactive surfaces, continue to applicable registered gates:

```text
G6   pattern fit
I2   loading/empty/error/success/partial state coverage
G13  adaptive layout
G15  adaptive type
I4   overflow strategy
I5   resize/orientation continuity
```

Do not duplicate those gates inside the foundation. Foundation establishes the universal relationship contract; surface gates verify detailed behavior.

## Composition and balance

| Gate | Review question | Pass evidence |
|---|---|---|
| C1 Focal Point | Is the intended first point of attention clear in the actual viewing context and representative content states? | The eye reaches the main message, task, product, or data without competing anchors created by long values, missing media, or fallback UI. |
| C2 Weight Distribution | Is visual weight distributed intentionally across the frame, page, viewport, slide, and supported content density? | Heavy elements, empty space, imagery, type, values, accents, depth, and overlap create stable or intentionally dynamic balance without hiding required content. |
| R6 Composition Intent | Is symmetry, asymmetry, centering, density, openness, flatness, or layering chosen for a reason rather than inherited from a template? | The composition supports content and brand across declared states; asymmetry and elevation are not mandatory. |
| R8 Restraint | Does every visible element, fallback, and depth effect have a communication, interaction, structural, or brand role? | Decoration does not fill empty states blindly, add meaningless depth, or compete with primary content. |

Balance is not the same as symmetry. Review optical mass, direction, scale, contrast, content density, depth, overlap, and empty space together.

## Visual hierarchy and flow

| Gate | Review question | Pass evidence |
|---|---|---|
| G8 First Impression | Can the viewer identify the primary message or task within the expected attention window and realistic content? | Opening hierarchy communicates purpose before details without relying on placeholder-short copy. |
| R7 Hierarchy | Are importance levels distinguishable without too many competing weights? | Dominant, supporting, and tertiary roles remain clear across supported content lengths/density; exceptions are purposeful. |
| H1 Dominant/Supporting | Is the relationship between the primary anchor and supporting content unambiguous? | Supporting content reinforces rather than competes with the primary anchor, including long or missing variants. |
| H2 Cross-Section Decay | Across a long page, deck, or multi-region artifact, does later content preserve the intended global hierarchy and flow? | A secondary section, elevated surface, dense collection, or slide element does not accidentally overpower the primary narrative anchor; the next region remains discoverable. |
| H3 Role Taxonomy | Can headings, labels, statements, metadata, values, missing states, and annotations be identified by role? | Similar roles look related; different roles and absent/unavailable values do not collapse into one style. |

Nested hierarchy should use at least two cues when spacing or typography alone remains ambiguous. Do not enforce a universal numeric H2/H1 ratio or character limit. Use measured values only when they explain an observed relationship problem.

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
| CP2 Content Proportion | Is the amount, distribution, and adaptation of copy/data suitable for its region and viewing context? | No arbitrary universal word cap; content length/density supports comprehension and action at declared bounds; overflow/fallback does not hide critical meaning. |
| CP3 No Slop | Is the artifact free from generic filler, fake proof, unearned claims, and template-driven content patterns? | Language and content structure are grounded in the actual product or message. |

Examples of automatic review flags, not automatic failures:

```text
“seamless”, “world-class”, “cutting-edge”, or “modern solution” without evidence
fake logo strips, ratings, testimonials, or usage counts
six or more equal-weight cards with no prioritization
headline + three generic benefits + CTA copied without product-specific logic
decoration that mimics current AI design trends but weakens the message
color-only status communication
meaningless glass, shadow, blur, or elevation added to simulate polish
placeholder-equal titles, values, and media used as the only resilience evidence
fixed-height clipping or indiscriminate truncation used to preserve a template
```

A flag becomes a failed gate only when evidence shows it harms clarity, truth, accessibility, brand, content meaning, or task performance.

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

honestly declared unsupported content exceeds a product/template boundary
  → verify boundary communication and recovery; not automatically a foundation defect

focus trap, loading/error behavior, runtime, validation, security, crop, fidelity,
compositing, moderation, or export-specific failure
  → applicable interactive/static/domain/engineering reviewer
```

Examples:

```text
parent/child/sibling hierarchy collapses in zen, SaaS, and editorial
  → foundation defect

sticky or floating layers obscure required content across multiple product genres
  → foundation figure-ground/layering defect

long/optional/dense content breaks grouping and legibility across catalog, dashboard,
and reusable poster templates
  → foundation content-resilience defect

only zen page exceeds its structural-line or elevation budget
  → genre defect

one SectionHeader component misaligns every eyebrow
  → component-system defect

one Card component clips the same title role across every feature
  → component-system content-resilience defect

one Popover component detaches from its trigger everywhere
  → component-system defect plus applicable interactive evidence
```

## Universal quick review

For a quick review, assess the applicable foundation axes through canonical gate IDs:

```text
F1  hierarchy / role clarity
F2  grouping / figure-ground / containment / optional presence
F3  alignment under wrapping and variation
F4  spatial rhythm / content density
F5  balance / depth / content mass
F6  flow / context after adaptation
F7  legibility / content shape / background interference
F8  adaptation and fallback consistency
F10 viewport + content continuity

Canonical scoring subset:
G4  figure-ground
G7  layout and adaptation logic
G9  measure and wrapping
G11 actual-size legibility
G12 cognitive ease and density
CP2 content proportion
applicable registered accessibility/responsive/state gates
```

Any score below 5 is critical. Continue to profile-specific hard gates before declaring the artifact safe or release-ready.
