---
name: design-review
description: Surface-aware design review router — classify an interactive or static artifact, load only relevant universal, surface, and component gates, require evidence, then score and report with explicit coverage. Use standalone or from design-audit, design-refinement, and redesign-workflow.
license: MIT
metadata:
  ai-native-skills.version: 3.0.0
  ai-native-skills.author: puterakahfi
  ai-native-skills.type: skill
  ai-native-skills.related_skills: '["design-audit","design-refinement","redesign-workflow","master-design","design-foundation","design-system","adaptive-component-design","accessibility","readability","responsiveness","motion-design","composition","visual-hierarchy","copywriting","cro"]'
---

# Design Review

Evidence-backed review router for web, mobile, desktop, static marketing, and presentation surfaces.

This skill owns review routing, applicability, scoring, and reporting. Specialist skills own the detailed design knowledge and correction rules.

## Hard Rules

```text
1. Classify the surface before selecting gates.
2. Separate universal principles from surface-specific thresholds.
3. Never apply interactive gates to static artifacts.
4. Never claim a gate passed without suitable evidence.
5. NOT_APPLICABLE and NOT_VERIFIED are different; neither is zero.
6. Score only verified applicable gates.
7. Load only relevant profile, surface, and component references.
8. Every failure needs observation, evidence, impact, and correction direction.
9. Do not turn taste or one style into a universal gate.
10. High score + low coverage is not release approval.
11. Hard gates are contextual, not global.
12. Review does not silently become redesign or implementation.
```

## Inputs

```text
target            required — URL, app, screenshot, image, PDF page, slide, repo path
surface_profile   web-marketing | web-application | mobile-application |
                  desktop-application | static-marketing | presentation | other
artifact_state    rendered-interactive | rendered-static | source-only | mixed
review_depth      quick | focused | full | release
focus             lenses, components, regions, or previous gate IDs
viewing_context   viewports, dimensions, channel, distance, theme, orientation, inputs
required_assets   logos, products, people, copy, price, contact, claims, legal content
goal               user, communication, business, or delivery outcome
```

Infer missing values only when evidence is strong and record the assumption.

## Core Workflow

```text
Phase 0 → CLASSIFY
  Resolve profile, artifact state, context, and depth.
  Load: references/review-routing.md

Phase 1 → ROUTE
  Select relevant lenses, surface gates, components, and evidence.
  Load: references/review-profiles.md

Phase 2 → INSPECT
  Inspect the complete available artifact before scoring.
  Capture realistic content, states, sizes, themes, assets, and constraints.

Phase 3 → UNIVERSAL REVIEW
  Typography, hierarchy, spacing, composition, balance, alignment,
  color, readability, content, brand consistency, restraint.
  Load: references/universal-gates.md

Phase 4 → SURFACE REVIEW
  Interactive → references/interactive-surface-gates.md
  Static/slide → references/static-visual-gates.md

Phase 5 → COMPONENT REVIEW
  Review only present or required components.
  Load: references/component-review.md when relevant.

Phase 6 → EVIDENCE + SCORE
  Assign status, score, weight, hard-gate result, and coverage.
  Load: references/evidence-and-scoring.md

Phase 7 → REPORT
  Prioritize findings, limitations, and handoff.
  Load: references/review-report.md
```

```text
classify → route → inspect → universal → surface → components
→ hard gates → score + coverage → report
```

Do not score until route and evidence are explicit.

## Loading Policy

Always load:

```text
references/review-routing.md
references/review-profiles.md
references/universal-gates.md
references/evidence-and-scoring.md
references/review-report.md
```

Load on demand:

```text
interactive web/mobile/desktop → references/interactive-surface-gates.md
poster/banner/social/slide     → references/static-visual-gates.md
present or required components → references/component-review.md
```

Never load every reference defensively.

## Review Depth

```text
quick
  Critical universal gates + applicable hard gates + declared issue.
  No release claim.

focused
  Selected lenses/components + adjacent regression checks.
  Default during active refinement.

full
  All applicable universal/profile gates + major present components.

release
  Full review + contextual hard gates + required states, sizes, themes,
  input methods, runtime/export evidence, and sufficient coverage.
```

## Applicability and Evidence

Every selected gate receives exactly one status:

```text
PASS | FAIL | PARTIAL | NOT_VERIFIED | NOT_APPLICABLE
```

Examples:

```text
poster + reduced motion                    → NOT_APPLICABLE
dashboard screenshot + keyboard operation → NOT_VERIFIED
running app + unhandled route error        → FAIL RI1
commercial visual + wrong supplied price  → FAIL fidelity/content hard gate
```

Contextual hard gates:

```text
interactive release
  RI1 runtime integrity
  G21 reduced motion when applicable
  verified accessibility or task-completion blocker

static commercial delivery
  required logo/product/person/content fidelity
  mandatory text legibility
  crop/safe-area integrity
  delivery resolution
```

Use rendered visuals, interaction observation, runtime capture, accessibility tree, source inspection, asset comparison, measurements, or user/task evidence as appropriate.

A build is not visual verification. A screenshot is not interaction or runtime verification.

## Score and Verdict

```text
Pass threshold: 8.0 / 10
Critical: verified score below 5
Overall: weighted average of verified applicable gates only
Coverage: verified applicable weight / all applicable selected weight
```

```text
PASS             score >= 8, hard gates pass, sufficient coverage
CONDITIONAL PASS score >= 8, no verified hard-gate failure, gaps remain
NEEDS WORK       score < 8 or important gates fail
CRITICAL         hard gate fails or material critical gate exists
```

## Output

Report:

```text
review context and route
score + verified coverage
contextual hard-gate status
executive findings
cluster/component summary
critical / important / polish priority
NOT_APPLICABLE and NOT_VERIFIED gates
recommended handoff
```

Each failed or partial finding includes gate, region, observation, evidence, impact, correction direction, and confidence.

## Handoff

```text
design-audit       owns full capture, gap analysis, and prioritization
design-refinement  owns targeted fixes, preservation, and focused re-score
redesign-workflow  owns redesign, verification, defect classification, and fix loop
```

`design-review` reports findings. It changes artifacts only when the calling workflow explicitly owns production.

## Final Guard

```text
□ Profile, artifact state, and viewing context are explicit.
□ Only relevant references were loaded.
□ Universal gates were reviewed.
□ Surface/component gates match the target.
□ Hard gates were contextual.
□ Every score has suitable evidence.
□ NOT_VERIFIED and NOT_APPLICABLE remain separate.
□ Score uses verified applicable gates only.
□ Coverage is shown beside score.
□ Findings are specific, prioritized, and style-neutral.
```