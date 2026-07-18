---
name: design-review
description: Surface-aware design review orchestrator — classify the artifact, load only relevant visual, interactive, static, and component gates, require evidence, then score and report with explicit coverage. Use standalone or from design-audit, design-refinement, and redesign-workflow.
license: MIT
metadata:
  ai-native-skills.version: 3.0.0
  ai-native-skills.author: puterakahfi
  ai-native-skills.type: skill
  ai-native-skills.related_skills: '["design-audit","design-refinement","redesign-workflow","master-design","design-foundation","design-system","adaptive-component-design","accessibility","readability","responsiveness","motion-design","composition","visual-hierarchy","copywriting","cro"]'
---

# Design Review

Surface-aware, evidence-backed design quality review for interactive products, static marketing visuals, and presentations.

This skill owns review routing, applicability, evidence, scoring, and reporting. Specialized design skills own the underlying design knowledge and correction rules.

<!-- LOAD ON-DEMAND — use standalone or from design-audit, design-refinement, and redesign-workflow. -->

## Hard Rules

```text
1. Classify the surface before selecting gates.
2. Separate universal principles from surface-specific thresholds.
3. Never apply interactive UI gates to static artifacts.
4. Never claim a gate passed without suitable evidence.
5. Distinguish NOT_APPLICABLE from NOT_VERIFIED; neither is zero.
6. Score only verified applicable gates.
7. Load only the relevant profile, surface, and component references.
8. Every failed gate requires an observation, evidence, impact, and correction direction.
9. Do not turn personal taste or one design style into a universal gate.
10. A high score with low evidence coverage is not release approval.
11. Hard gates are contextual, never globally attached to unrelated surface types.
12. Review does not silently become redesign or implementation work.
```

## When to Use

Use `design-review` for:

- scored quality checks of existing designs;
- quick review during an active visual iteration;
- focused review of a declared issue or component;
- full design audit scoring;
- release or delivery readiness checks;
- review of web, mobile, desktop, poster, banner, social, and presentation surfaces.

Route elsewhere when:

- use `design-audit` when the user wants a complete gap report and prioritization lifecycle;
- use `design-refinement` when known failing gates should be fixed while preserving passing work;
- use `redesign-workflow` when direction, macrostructure, or multiple critical clusters need replacement;
- use the governing specialist skill when the request is knowledge or production rather than review.

## Parameters

| Parameter | Required | Description |
|---|---:|---|
| `target` | Yes | URL, rendered app, screenshot, image, PDF page, slide, repository path, or named surface |
| `goal` | No | User, communication, business, or delivery outcome being reviewed |
| `surface_profile` | No | `web-marketing`, `web-application`, `mobile-application`, `desktop-application`, `static-marketing`, `presentation`, or `other` |
| `artifact_state` | No | `rendered-interactive`, `rendered-static`, `source-only`, or `mixed` |
| `review_depth` | No | `quick`, `focused`, `full`, or `release`; default `focused` during iteration, otherwise `full` |
| `focus` | No | Declared lenses, components, regions, or prior failing gate IDs |
| `viewing_context` | No | Viewports, dimensions, channel, distance, theme, orientation, input methods, or print requirements |
| `required_assets` | No | Logos, products, faces, copy, price, contact, legal text, and references that must remain faithful |

Infer missing values only when evidence is strong. Record assumptions in the review context.

## Core Workflow

```text
Phase 0 → CLASSIFY
  Resolve surface profile, artifact state, viewing context, and review depth.
  Load: references/review-routing.md

Phase 1 → ROUTE
  Select universal, surface-specific, and component references.
  Load: references/review-profiles.md

Phase 2 → INSPECT
  Inspect the complete available artifact before scoring.
  Capture realistic content, states, sizes, themes, assets, and constraints.

Phase 3 → UNIVERSAL REVIEW
  Review typography, hierarchy, spacing, composition, balance, alignment,
  color, readability, content clarity, brand consistency, and restraint.
  Load: references/universal-gates.md

Phase 4 → SURFACE REVIEW
  Interactive profile:
    Load: references/interactive-surface-gates.md
  Static or presentation profile:
    Load: references/static-visual-gates.md

Phase 5 → COMPONENT REVIEW
  Review only present or required components.
  Load: references/component-review.md when relevant.

Phase 6 → EVIDENCE AND SCORE
  Assign status, score, weight, confidence, hard-gate result, and coverage.
  Load: references/evidence-and-scoring.md

Phase 7 → REPORT
  Prioritize findings by impact, state limitations, and select the correct handoff.
  Load: references/review-report.md
```

## Canonical Loop

```text
classify
→ route
→ inspect
→ universal review
→ surface review
→ component review when relevant
→ hard-gate check
→ score + coverage
→ report
```

Do not begin scoring until the route and available evidence are explicit.

## Review Depth

```text
quick
  Critical universal gates + applicable profile hard gates + declared issue.
  No release claim.

focused
  Selected lenses/components + adjacent regression checks.
  Use during active design refinement.

full
  All applicable universal gates + profile gates + major present components.

release
  Full review + all applicable hard gates + required states, sizes, themes,
  input methods, runtime or export evidence, and sufficient coverage.
```

Do not run a full scorecard for every small visual iteration.

## Reference Loading Map

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
Interactive web/mobile/desktop → references/interactive-surface-gates.md
Poster/banner/social/slide     → references/static-visual-gates.md
Present/required UI components → references/component-review.md
```

Never load all references merely because they exist.

## Applicability Model

Every selected gate receives exactly one status:

```text
PASS
FAIL
PARTIAL
NOT_VERIFIED
NOT_APPLICABLE
```

Examples:

```text
Poster + reduced motion                    → NOT_APPLICABLE
Dashboard screenshot + keyboard operation → NOT_VERIFIED
Running app + unhandled route error        → FAIL RI1
Source-only CSS + visual balance           → NOT_VERIFIED until rendered
Commercial poster + wrong supplied price   → FAIL static content-fidelity hard gate
```

## Contextual Hard Gates

```text
Interactive release:
  RI1 runtime integrity
  G21 reduced motion when applicable
  required accessibility/task-completion blockers

Static commercial delivery:
  required logo/product/person/content fidelity
  mandatory text legibility
  crop/safe-area integrity
  delivery resolution
```

A hard gate applies only when its triggering context exists. Missing evidence produces `NOT_VERIFIED`, not an invented pass or zero.

## Evidence Before Score

Accepted evidence may include:

```text
rendered visual
interaction observation
runtime capture
DOM or native accessibility tree
source inspection
asset comparison
measurements
user or task evidence
```

A build passing is not visual verification. A screenshot looking correct is not interaction or runtime verification.

## Scoring Policy

```text
Default pass threshold: 8.0 / 10
Critical gate: score below 5
Overall score: weighted average of verified applicable gates only
Coverage: verified applicable weight / all applicable selected weight
```

Verdict requires both score and coverage:

```text
PASS             score >= 8, hard gates pass, sufficient coverage
CONDITIONAL PASS score >= 8, no verified hard-gate failure, evidence gaps remain
NEEDS WORK       score < 8 or important gates fail
CRITICAL         applicable hard gate fails or material critical gate exists
```

## Required Review State

Record before scoring:

```yaml
review_route:
  surface_profile: <profile>
  artifact_state: <state>
  review_depth: <depth>
  viewing_context: []
  selected_references: []
  selected_lenses: []
  selected_components: []
  applicable_hard_gates: []
  evidence_available: []
  evidence_gaps: []
```

Record for each failed or partial gate:

```yaml
finding:
  gate: <id>
  status: <FAIL | PARTIAL>
  score: <0-10 for verified scope>
  region: <location>
  observation: <specific condition>
  evidence: []
  impact:
    user: <impact>
    business_or_delivery: <impact when relevant>
  recommendation: <specific correction direction>
  confidence: <high | medium | low>
```

## Output

The report must include:

```text
review context
score and verified coverage
contextual hard-gate status
executive findings
cluster summary
component findings when relevant
critical / important / polish priority
NOT_APPLICABLE and NOT_VERIFIED gates
recommended handoff
```

Do not dump the entire gate inventory when a focused review is enough.

## Integration Contract

```text
design-audit
  owns capture, full gap analysis, prioritization, and audit recommendation
  calls design-review for routed scoring

design-refinement
  owns targeted fixes and regression preservation
  calls design-review for focused re-score

redesign-workflow
  owns redesign lifecycle and fix loop
  calls design-review after rendered verification
```

`design-review` reports findings. It changes artifacts only when the calling workflow explicitly owns and requests production.

## Final Guard

```text
□ Surface profile is explicit.
□ Artifact state and viewing context are explicit.
□ Only relevant references were loaded.
□ Universal gates were reviewed.
□ Surface and component gates match the target.
□ Hard gates were applied contextually.
□ Every score has suitable evidence.
□ NOT_VERIFIED and NOT_APPLICABLE are separate.
□ Overall score includes verified applicable gates only.
□ Coverage is reported beside the score.
□ Findings are specific and prioritized.
□ No style preference was presented as a universal design law.
```