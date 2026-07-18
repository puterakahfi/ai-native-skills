# Review Routing

Use this reference during Phase 0 and Phase 1 of `design-review`.

The facade must classify both the **design domain** and the **surface profile** before selecting gates. Routing prevents a universal-looking scorecard from applying the wrong rules or claiming expertise the loaded reviewers do not provide.

## 1. Classify the design domain

Choose one primary domain:

```text
digital-interface    interactive product UI and digital experiences
visual-communication static marketing, advertising, social, and campaign visuals
presentation         slide and deck communication
other                specialized discipline requiring a declared reviewer or limited scope
```

Built-in domain coverage:

| Domain | Built-in strategy |
|---|---|
| `digital-interface` | universal + interactive + applicable component gates |
| `visual-communication` | universal + static visual gates |
| `presentation` | universal + static visual + presentation gates |

Domains that require an additional reviewer for a complete verdict include:

```text
brand identity and logo systems
packaging and specialist print production
motion graphics, video, and film
industrial or physical product design
architecture, interior, and spatial design
fashion design
service-design research and service systems
```

For an unsupported domain, select one of these coverage modes:

```text
ADAPTER_COVERED  a suitable domain reviewer is loaded
LIMITED          universal gates only; report cannot claim full-domain quality
ROUTE_ELSEWHERE  the request requires specialist knowledge unavailable here
```

Do not map a specialized discipline to the nearest built-in profile merely because some visual principles overlap.

## 2. Classify the surface

For built-in domains, choose one primary profile:

```text
web-marketing       landing page, marketing site, pricing, portfolio, docs home
web-application     dashboard, admin, editor, workflow, settings, commerce flow
mobile-application  native or mobile-first application surface
desktop-application desktop app, multi-panel tool, IDE-like or productivity app
static-marketing    poster, flyer, banner, social creative, ad creative, thumbnail
presentation        individual slide or complete presentation surface
other               declared specialist surface governed by a domain reviewer
```

Do not infer `web-marketing` merely because the artifact is shown in a browser. Determine the actual task and viewing context.

## 3. Classify the artifact state

```text
rendered-interactive  live URL, local running app, interactive prototype
rendered-static       exported image, PDF page, poster, slide, screenshot
source-only           repository or design source without a rendered result
mixed                 rendered result plus source/runtime evidence
```

The artifact state determines what can be verified. It does not change whether a gate is conceptually relevant.

## 4. Classify review depth

```text
quick       critical gates and the user-declared problem only
focused     selected lenses/components plus regression checks
full        all applicable gates for every loaded reviewer
release     full review plus hard gates, runtime/states/export, and delivery evidence
```

Use `focused` during active refinement. Use `full` or `release` only for broad audit, commit readiness, deployment readiness, or final pass claims.

A `full` review is full only for the domains covered by loaded reviewers.

## 5. Select domain reviewers

Resolve reviewers in this order:

```text
1. built-in domain strategy
2. explicitly requested specialist reviewer
3. installed reviewer whose declared domain and applicability match
4. limited universal review
5. route elsewhere when limited review would not answer the request honestly
```

A compatible domain reviewer must declare:

```text
domain id
applicability conditions
required context and evidence
gates and hard-gate triggers
unsupported claims
finding-contract compatibility
```

When several reviewers match:

```text
choose one primary domain owner
load secondary reviewers only for declared cross-domain concerns
do not average unrelated domain scorecards without explicit weighting
resolve duplicate findings under the reviewer that owns the root cause
```

## 6. Load references by phase

Do not load a permanent baseline bundle. Load references when entering their owning phase:

```text
CLASSIFY / ROUTE
  review-routing.md
  review-profiles.md only for a built-in profile

UNIVERSAL REVIEW
  universal-gates.md

DOMAIN / SURFACE REVIEW
  interactive-surface-gates.md OR
  static-visual-gates.md OR
  declared external domain reviewer

COMPONENT REVIEW
  component-review.md only for selected interactive components

EVIDENCE + SCORE
  evidence-and-scoring.md

REPORT
  review-report.md
```

Profile routing:

| Profile | Domain/surface references |
|---|---|
| `web-marketing` | `interactive-surface-gates.md`; `component-review.md` only for present components |
| `web-application` | `interactive-surface-gates.md`; `component-review.md` only for present components |
| `mobile-application` | `interactive-surface-gates.md`; `component-review.md` only for present components |
| `desktop-application` | `interactive-surface-gates.md`; `component-review.md` only for present components |
| `static-marketing` | `static-visual-gates.md` |
| `presentation` | `static-visual-gates.md`; component review only for a UI mockup reviewed as a secondary surface |
| `other` | declared domain reviewer or limited universal review |

Never load every reference defensively.

## 7. Select lenses

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

Specialized lenses come from the loaded domain reviewer. Do not invent them in the facade.

## 8. Select components from evidence

Load component checks only for interactive components that exist or are required by the task.

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

A missing component is not automatically a defect. Fail it only when the task or information architecture requires it.

## 9. Applicability rules

```text
Relevant + sufficient evidence    → score
Relevant + insufficient evidence  → NOT_VERIFIED
Not relevant to loaded reviewers  → NOT_APPLICABLE
Relevant but outside reviewer scope → declare coverage gap
Deferred with accepted risk       → score current result and record risk
```

Never convert `NOT_VERIFIED`, `NOT_APPLICABLE`, or missing domain coverage into zero.

Examples:

```text
Poster JPEG + reduced motion            → NOT_APPLICABLE
Dashboard screenshot + keyboard flow    → NOT_VERIFIED
Running web app + runtime error          → FAIL RI1
Source-only CSS + visual balance         → NOT_VERIFIED until rendered
Mobile app + desktop footer pattern      → NOT_APPLICABLE unless present or required
Logo concept without identity reviewer   → LIMITED universal review
Packaging dieline without print reviewer → ROUTE_ELSEWHERE or LIMITED with explicit gaps
```

## 10. Routing output

Record this before scoring:

```yaml
review_route:
  design_domain: digital-interface
  coverage_mode: BUILT_IN
  primary_reviewer: design-review/interactive
  secondary_reviewers: []
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
  domain_scope_limitations: []
  excluded_as_not_applicable: []
  evidence_gaps:
    - keyboard behavior not yet observed
```

For an unsupported domain:

```yaml
review_route:
  design_domain: brand-identity
  coverage_mode: LIMITED
  primary_reviewer: universal-gates
  secondary_reviewers: []
  surface_profile: other
  domain_scope_limitations:
    - symbol distinctiveness not reviewed
    - trademark similarity not reviewed
    - identity-system completeness not reviewed
```

Do not begin scoring until design-domain coverage, route, and limitations are explicit.