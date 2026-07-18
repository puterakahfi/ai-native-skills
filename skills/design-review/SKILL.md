---
name: design-review
description: Surface-aware design review orchestrator — classify the artifact, load only relevant universal, interactive, static, and component gates, require evidence, then score and report with explicit coverage. Use standalone or from design-audit, design-refinement, and redesign-workflow.
license: MIT
metadata:
  ai-native-skills.version: 3.0.0
  ai-native-skills.author: puterakahfi
  ai-native-skills.type: skill
  ai-native-skills.related_skills: '["design-audit","design-refinement","redesign-workflow","master-design","design-foundation","design-system","adaptive-component-design","accessibility","readability","responsiveness","motion-design","composition","visual-hierarchy","copywriting","cro"]'
---

# Design Review

Surface-aware, evidence-backed review for interactive products, static marketing visuals, and presentations.

This skill owns routing, applicability, scoring, and reporting. Specialist skills own the underlying design knowledge and correction rules.

<!-- LOAD ON-DEMAND — use standalone or from design-audit, design-refinement, and redesign-workflow. -->

## Hard Rules

```text
1. Classify the surface before selecting gates.
2. Separate universal principles from surface-specific thresholds.
3. Never apply interactive gates to static artifacts.
4. Never claim a gate passed without suitable evidence.
5. Distinguish NOT_APPLICABLE from NOT_VERIFIED; neither is zero.
6. Score only verified applicable gates.
7. Load only the relevant profile, surface, and component references.
8. Every failure needs an observation, evidence, impact, and correction direction.
9. Do not turn personal taste or one style into a universal gate.
10. A high score with low evidence coverage is not release approval.
11. Hard gates are contextual, not global.
12. Review does not silently become redesign or implementation work.
```

## Use and Routing

Use for quick iteration checks, focused component review, full audit scoring, or release/delivery review of:

```text
web marketing
web application
mobile application
desktop application
poster, flyer, banner, social, ad, or thumbnail
presentation or slide
```

Route to:

```text
design-audit       → complete gap-analysis lifecycle
design-refinement  → fix known failing gates while preserving passing work
redesign-workflow  → replace wrong direction, macrostructure, or multiple critical clusters
specialist skill   → knowledge or production without review lifecycle
```

## Parameters

| Parameter | Required | Values or meaning |
|---|---:|---|
| `target` | Yes | URL, app, screenshot, image, PDF page, slide, repository path, or named surface |
| `goal` | No | User, communication, business, or delivery outcome |
| `surface_profile` | No | `web-marketing`, `web-application`, `mobile-application`, `desktop-application`, `static-marketing`, `presentation`, `other` |
| `artifact_state` | No | `rendered-interactive`, `rendered-static`, `source-only`, `mixed` |
| `review_depth` | No | `quick`, `focused`, `full`, `release` |
| `focus` | No | Lenses, components, regions, or prior gate IDs |
| `viewing_context` | No | Viewports, dimensions, channel, distance, theme, orientation, input methods, print requirements |
| `required_assets` | No | Logos, products, people, copy, prices, contacts, claims, legal text, and references to preserve |

Infer missing values only when evidence is strong and record the assumption.

## Core Workflow

```text
Phase 0 → CLASSIFY
  Resolve profile, artifact state, viewing context, and review depth.
  Load: references/review-routing.md

Phase 1 → ROUTE
  Select relevant lenses, surface gates, components, and evidence.
  Load: references/review-profiles.md

Phase 2 → INSPECT
  Inspect the complete available artifact before scoring.
  Capture realistic content, states, sizes, themes, assets, and constraints.

Phase 3 → UNIVERSAL REVIEW
  Typography, hierarchy, spacing, composition, balance, alignment,
  color, readability, content, brand consistency, and restraint.
  Load: references/universal-gates.md

Phase 4 → SURFACE REVIEW
  Interactive → references/interactive-surface-gates.md
  Static/slide → references/static-visual-gates.md

Phase 5 → COMPONENT REVIEW
  Review only present or required components.
  Load: references/component-review.md when relevant.

Phase 6 → EVIDENCE AND SCORE
  Assign status, score, weight, hard-gate result, and coverage.
  Load: references/evidence-and-scoring.md

Phase 7 → REPORT
  Prioritize findings, limitations, and the correct handoff.
  Load: references/review-report.md
```

Canonical loop:

```text
classify → route → inspect → universal → surface → components
→ hard gates → score + coverage → report
```

Do not score until the route and available evidence are explicit.

## Review Depth

```text
quick
  Critical universal gates + applicable hard gates + declared issue.
  No release claim.

focused
  Selected lenses/components + adjacent regression checks.
  Default during active refinement.

full
  All applicable universal and profile gates + major present components.

release
  Full review + applicable hard gates + required states, sizes, themes,
  input methods, runtime/export evidence, and sufficient coverage.
```

Do not run a full scorecard for every small iteration.

## Reference Map

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

Never load all references defensively.

## Applicability and Hard Gates

Every selected gate receives one status:

```text
PASS | FAIL | PARTIAL | NOT_VERIFIED | NOT_APPLICABLE
```

Contextual hard gates include:

```text
interactive release
  RI1 runtime integrity
  G21 reduced motion when applicable
  verified accessibility or task-completion blockers

static commercial delivery
  required logo/product/person/content fidelity
  mandatory text legibility
  crop and safe-area integrity
  delivery resolution
```

A hard gate applies only when its triggering context exists. Missing evidence is `NOT_VERIFIED`, not pass or zero.

## Evidence and Verdict

Evidence may include rendered visuals, interaction observation, runtime capture, accessibility tree, source inspection, asset comparison, measurements, or user/task evidence.

```text
Default pass threshold: 8.0 / 10
Critical: verified score below 5
Overall: weighted average of verified applicable gates only
Coverage: verified applicable weight / all applicable selected weight
```

```text
PASS             score >= 8, hard gates pass, sufficient coverage
CONDITIONAL PASS score >= 8, no verified hard-gate failure, evidence gaps remain
NEEDS WORK       score < 8 or important gates fail
CRITICAL         applicable hard gate fails or material critical gate exists
```

A build is not visual verification. A screenshot is not interaction or runtime verification.

## Output Contract

Report:

```text
review context and route
score + verified coverage
contextual hard-gate status
executive findings
cluster and component summary
critical / important / polish priority
NOT_APPLICABLE and NOT_VERIFIED gates
recommended handoff
```

Each failed or partial finding must contain:

```text
gate and region
specific observation
evidence
user/message/business/delivery impact
correction direction
confidence
```

Do not dump the full gate inventory when a focused report is enough.

## Integration Contract

```text
design-audit
  owns capture, full gap analysis, prioritization, and audit recommendation

design-refinement
  owns targeted fixes, preservation, and focused re-score

redesign-workflow
  owns redesign lifecycle, verification, defect classification, and fix loop
```

`design-review` reports findings. It changes artifacts only when the calling workflow explicitly owns and requests production.

## Final Guard

```text
□ Profile, artifact state, and viewing context are explicit.
□ Only relevant references were loaded.
□ Universal gates were reviewed.
□ Surface and component gates match the target.
□ Hard gates were applied contextually.
□ Every score has suitable evidence.
□ NOT_VERIFIED and NOT_APPLICABLE remain separate.
□ Score uses verified applicable gates only.
□ Coverage is reported beside the score.
□ Findings are specific, prioritized, and style-neutral.
```