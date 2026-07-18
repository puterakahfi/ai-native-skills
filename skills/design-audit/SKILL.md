---
name: design-audit
description: Standalone design audit — inspect an existing interactive or static visual surface, route through design-review, and produce an evidence-backed prioritized gap report without redesigning.
license: MIT
metadata:
  ai-native-skills.version: 2.0.0
  ai-native-skills.author: puterakahfi
  ai-native-skills.type: skill
  ai-native-skills.related_skills: '["redesign-workflow","design-review","design-refinement","master-design","accessibility","readability","responsiveness"]'
---

# Design Audit

Inspect → route → score → prioritize → report. No redesign output.

`design-audit` owns evidence capture, gap analysis, and recommendation. `design-review` owns gate routing, applicability, scoring, coverage, and review format.

## When to Use

- before a redesign to understand the current state;
- periodic quality health checks;
- stakeholder review of what is wrong and why;
- deciding between targeted refinement and full redesign;
- auditing web, mobile, desktop, poster, social, banner, or presentation surfaces.

Output: an evidence-backed gap report and prioritized fix list, not a replacement artifact.

## Hard Rules

```text
1. Route the surface before choosing capture methods or gates.
2. Capture evidence appropriate to the artifact state.
3. Never score unavailable evidence as zero.
4. Do not apply browser-only checks to static or native artifacts.
5. Use design-review as the canonical gate source; do not duplicate its scorecard.
6. Every gap needs evidence, impact, and a correction direction.
7. Audit does not silently become redesign or implementation work.
```

## Audit Process

### Step 1 — Resolve context

Load `design-review` and run its classification and routing phases.

Record:

```yaml
audit_context:
  target: <target>
  goal: <goal>
  surface_profile: <profile>
  artifact_state: <state>
  review_depth: <quick | focused | full | release>
  viewing_context: []
  required_assets: []
  evidence_available: []
  evidence_gaps: []
```

Default to `full` for a standalone audit unless the user requests a quick or focused review.

### Step 2 — Capture current state

Use the capture path that matches the artifact.

```text
rendered web application
  full visual capture
  required viewports and themes
  interaction and state walkthrough
  DOM/accessibility evidence
  runtime evidence

mobile or desktop application
  required devices, windows, orientations, and density
  touch/keyboard/pointer behavior
  accessibility tree when available
  loading, error, permission, offline, and resize states

static marketing visual
  final-size export
  actual channel/aspect-ratio simulation
  safe-area and crop check
  supplied asset/content comparison
  resolution and compression inspection

presentation
  complete sequence when available
  room or screen-share scale
  chart, data, source, and narrative inspection

source-only
  implementation and asset inspection
  mark unrendered visual/interaction claims NOT_VERIFIED
```

Do not use a successful build as proof of visual quality. Do not use a screenshot as proof of keyboard, motion, or runtime behavior.

### Step 3 — Run design review

Load only the references selected by `design-review/references/review-routing.md`.

```text
quick audit
  universal quick gates
  applicable profile hard gates
  user-declared issue

focused audit
  selected lenses/components
  adjacent regression gates

full audit
  all applicable universal gates
  selected profile gates
  major present components
  evidence coverage

release audit
  full audit
  all applicable hard gates verified
  runtime or export delivery evidence
```

Use the score and coverage model from `design-review/references/evidence-and-scoring.md`.

### Step 4 — Classify each gap

For every failed or partial gate:

```yaml
gap:
  gate: <id>
  score: <verified score>
  status: <FAIL | PARTIAL>
  finding: <specific observed condition>
  evidence: []
  impact:
    user: <impact>
    business_or_delivery: <impact when relevant>
  governing_skill: <skill or product rule>
  correction_direction: <specific action direction>
  suspected_layer: <foundation | structure | component | expression | interaction | content | implementation>
  effort: <low | medium | high>
  confidence: <high | medium | low>
```

Do not prescribe an implementation library merely because the current component is wrong. Describe the behavior and design requirement first.

### Step 5 — Prioritize

```text
CRITICAL
  applicable hard-gate failure
  or verified score below 5 with material task, message, fidelity, accessibility,
  runtime, or delivery impact

IMPORTANT
  verified score 5–7.9
  or a clear issue that weakens comprehension, usability, trust, or consistency

POLISH
  passing or near-passing quality issue with low task risk
```

Combine repeated symptoms under one root-cause finding. Do not penalize six card instances as six independent spacing defects.

### Step 6 — Recommend the lifecycle

```text
design-refinement
  direction is sound
  gaps are specific
  passing regions should be preserved

redesign-workflow
  direction or macrostructure is wrong
  multiple critical clusters fail
  the selected component model cannot support the task

local implementation/content/asset fix
  the governing design rule already exists
  and the defect is isolated to code, data, copy, assets, or configuration
```

Do not use a fixed count of critical gates as the sole redesign trigger. Consider whether the failures share one local root cause or reveal a broken direction.

## Audit Report

Use `design-review/references/review-report.md` and add the audit recommendation.

Minimum output:

```markdown
# Design Audit — [target]

## Context
- Surface profile: [profile]
- Artifact state: [state]
- Goal: [goal]
- Evidence: [evidence]

## Verdict
**X.XX / 10** — [status] · Coverage [X%]

- Hard gates: [status]
- Critical: [count]
- Important: [count]
- Polish: [count]

## Priority Findings
1. **[finding]** — [severity]
   - Evidence: ...
   - Impact: ...
   - Correction direction: ...

## Limitations
- Not applicable: ...
- Not verified: ...

## Recommended Action
[design-refinement | redesign-workflow | local fix | ready]
```

The audit ends with the report. Produce or patch only when the user or calling workflow explicitly requests the next lifecycle.