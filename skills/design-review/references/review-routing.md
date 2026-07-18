# Review Routing

Use this reference during Phase 0 and Phase 1 of `design-review`.

The purpose of routing is to prevent a universal-looking scorecard from applying the wrong rules to the wrong artifact. Classify the review target before selecting gates.

## 1. Classify the surface

Choose one primary profile:

```text
web-marketing       landing page, marketing site, pricing, portfolio, docs home
web-application     dashboard, admin, editor, workflow, settings, commerce flow
mobile-application  native or mobile-first application surface
desktop-application desktop app, multi-panel tool, IDE-like or productivity app
static-marketing    poster, flyer, banner, social creative, ad creative, thumbnail
presentation        individual slide or complete presentation surface
other               declare the viewing context and derive the nearest profile
```

Do not infer `web-marketing` merely because the artifact is shown in a browser. Determine the actual product task and viewing context.

## 2. Classify the artifact state

```text
rendered-interactive  live URL, local running app, interactive prototype
rendered-static       exported image, PDF page, poster, slide, screenshot
source-only           repository or design source without a rendered result
mixed                 rendered result plus source/runtime evidence
```

The artifact state determines what can be verified. It does not change whether a gate is conceptually relevant.

## 3. Classify review depth

```text
quick       critical gates and the user-declared problem only
focused     selected lenses/components plus regression checks
full        all applicable gates for the selected profile
release     full review plus hard gates, runtime, states, and delivery evidence
```

Use `focused` during active refinement. Use `full` or `release` only for broad audit, commit readiness, deployment readiness, or final pass claims.

## 4. Load references on demand

Always load:

```text
review-profiles.md
evidence-and-scoring.md
universal-gates.md
review-report.md
```

Then load by primary profile:

| Profile | Additional references |
|---|---|
| `web-marketing` | `interactive-surface-gates.md`, `component-review.md` |
| `web-application` | `interactive-surface-gates.md`, `component-review.md` |
| `mobile-application` | `interactive-surface-gates.md`, `component-review.md` |
| `desktop-application` | `interactive-surface-gates.md`, `component-review.md` |
| `static-marketing` | `static-visual-gates.md` |
| `presentation` | `static-visual-gates.md`; load `component-review.md` only for reusable UI mockups inside slides |
| `other` | declare selected references and why |

Do not load every reference defensively. Load only the files needed for the current profile and depth.

## 5. Select lenses

Universal lenses:

```text
typography
visual hierarchy
spacing and rhythm
composition and balance
alignment and grid
color and contrast
readability
content clarity
brand consistency
restraint
```

Interactive-only lenses:

```text
navigation and task flow
interaction states and feedback
responsive or adaptive behavior
keyboard, pointer, touch, and gesture behavior
accessibility semantics
motion and reduced motion
runtime integrity
loading, empty, error, success, and permission states
```

Static-only lenses:

```text
viewing-distance legibility
message recognition
asset fidelity
crop, bleed, and safe-area safety
export quality
channel or print suitability
```

## 6. Select components from evidence

Load component checks only for components that actually exist or are required by the task.

```text
navigation
hero or page header
tabs and segmented controls
cards and lists
forms and filters
tables and data views
dialogs, drawers, and popovers
search and command surfaces
empty, loading, error, and success states
footer and closing regions
```

A missing component is not automatically a defect. Fail it only when the user task or information architecture requires it.

## 7. Applicability rules

```text
Relevant + sufficient evidence   → score
Relevant + insufficient evidence → NOT_VERIFIED
Not relevant to the profile      → NOT_APPLICABLE
Relevant but intentionally deferred with accepted risk → score the current result and record the risk
```

Never convert `NOT_VERIFIED` or `NOT_APPLICABLE` into zero.

Examples:

```text
Poster JPEG + reduced motion          → NOT_APPLICABLE
Dashboard screenshot + keyboard flow  → NOT_VERIFIED
Running web app + runtime error        → FAIL RI1
Source-only CSS + visual balance       → NOT_VERIFIED until rendered
Mobile app + desktop footer pattern    → NOT_APPLICABLE unless present or required
```

## 8. Routing output

Record this before scoring:

```yaml
review_route:
  surface_profile: web-application
  artifact_state: mixed
  review_depth: focused
  viewing_context: tablet landscape and mobile portrait
  selected_references:
    - universal-gates
    - interactive-surface-gates
    - component-review
  selected_lenses:
    - visual hierarchy
    - spacing and rhythm
    - responsive behavior
  selected_components:
    - tabs
    - cards and lists
  excluded_as_not_applicable: []
  evidence_gaps:
    - keyboard behavior not yet observed
```

Do not begin scoring until the route is explicit.