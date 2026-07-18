---
name: design-audit
description: Standalone facade-backed design audit — classify an existing artifact, capture appropriate evidence, invoke the applicable design-review domain strategy, and produce a prioritized gap report without redesigning.
license: MIT
metadata:
  ai-native-skills.version: 2.1.0
  ai-native-skills.author: puterakahfi
  ai-native-skills.type: skill
  ai-native-skills.related_skills: '["redesign-workflow","design-review","design-refinement","master-design","accessibility","readability","responsiveness"]'
---

# Design Audit

Inspect → classify → capture → review → prioritize → report. No redesign output.

`design-audit` owns evidence capture, gap analysis, prioritization, and lifecycle recommendation. The `design-review` facade owns domain routing, applicability, evidence normalization, scoring, coverage, verdict, and report semantics.

## Hard Rules

```text
1. Classify the design domain and surface before selecting capture methods.
2. Use the design-review facade as the canonical review entry point.
3. Never duplicate facade or domain-review gate inventories here.
4. Capture evidence appropriate to the artifact and selected reviewer.
5. Never score unavailable evidence as zero.
6. Do not apply browser-only checks to static, native, or unsupported domains.
7. Full audit means full only for domains covered by built-in or loaded reviewers.
8. Unsupported primary domains produce LIMITED REVIEW, not a full pass.
9. Every gap needs evidence, impact, governing reviewer, and correction direction.
10. Audit does not silently become redesign or implementation.
```

## When to Use

Use for:

- audit-only requests;
- periodic quality health checks;
- stakeholder gap reports;
- pre-redesign assessment;
- deciding between local fix, refinement, redesign, or specialist review;
- built-in facade domains: digital interface, visual communication, and presentation;
- specialized domains when an appropriate domain reviewer is available.

Output: an evidence-backed gap report and prioritized action, not a replacement artifact.

## Parameters

```text
target            required — URL, app, screenshot, image, PDF, slide, repo path
goal               user, communication, business, or delivery outcome
design_domain      digital-interface | visual-communication | presentation | other
surface_profile    web-marketing | web-application | mobile-application |
                   desktop-application | static-marketing | presentation | other
artifact_state     rendered-interactive | rendered-static | source-only | mixed
review_depth       quick | focused | full | release; default full
viewing_context    viewports, formats, channel, distance, theme, orientation, inputs
required_assets    logos, products, people, copy, prices, claims, legal content
domain_reviewers   specialist reviewers required by the primary domain
```

## Audit Process

### Step 1 — Resolve facade route

Start with `design-review/SKILL.md`, then enter its CLASSIFY / ROUTE phases.

Record:

```yaml
audit_context:
  target: <target>
  goal: <goal>
  design_domain: <domain>
  surface_profile: <profile>
  artifact_state: <state>
  review_depth: <quick | focused | full | release>
  coverage_mode: <BUILT_IN | ADAPTER_COVERED | LIMITED | ROUTE_ELSEWHERE>
  domain_reviewers: []
  viewing_context: []
  required_assets: []
  evidence_available: []
  evidence_gaps: []
  scope_limitations: []
```

Use `design-review/references/facade-boundary.md` when scope or domain coverage is unclear.

Do not continue as a complete audit when `coverage_mode` is `ROUTE_ELSEWHERE`. For `LIMITED`, continue only with an explicitly limited universal review and state that no complete domain verdict is possible.

### Step 2 — Capture current state

Select evidence from the resolved domain and artifact state.

```text
rendered web interface
  complete visual capture at required viewports/themes
  interaction and state walkthrough
  DOM/accessibility evidence
  runtime evidence

mobile or desktop application
  required devices, windows, orientations, density, and resize states
  touch/keyboard/pointer behavior
  accessibility tree when available
  loading, error, permission, offline, interruption, and recovery states

static visual communication
  final-size export and actual placement simulation
  crop, safe-area, bleed, and overlay checks
  supplied asset/content comparison
  resolution, compression, and color inspection

presentation
  complete sequence when available
  room, screen-share, or self-guided viewing mode
  chart, source, data, narrative, and repeated-layout inspection

specialized domain
  evidence required by the loaded domain reviewer
  universal visual evidence is supplementary, not specialist proof

source-only
  implementation, token, content, and asset inspection
  visual/interaction claims remain NOT_VERIFIED until rendered
```

A build is not visual verification. A screenshot is not keyboard, motion, runtime, or hidden-state evidence.

### Step 3 — Run facade review

Load references phase-by-phase according to `design-review`:

```text
CLASSIFY / ROUTE
  review-routing.md
  facade-boundary.md when needed
  review-profiles.md only for a built-in profile

UNIVERSAL REVIEW
  universal-gates.md

DOMAIN / SURFACE REVIEW
  interactive-surface-gates.md OR
  static-visual-gates.md OR
  declared external domain reviewer

COMPONENT REVIEW
  component-review.md only for selected components

EVIDENCE + SCORE
  evidence-and-scoring.md

REPORT
  review-report.md
```

Audit depth:

```text
quick
  critical universal gates + verifiable hard gates + declared issue
  no release claim

focused
  selected lenses/components + adjacent regression checks

full
  all applicable gates from every loaded reviewer
  complete only when primary-domain coverage exists

release
  full audit + all applicable hard gates + required domain evidence
```

### Step 4 — Classify gaps

For every failed or partial gate:

```yaml
gap:
  gate: <id>
  governing_reviewer: <built-in or external reviewer>
  score: <verified score>
  status: <FAIL | PARTIAL>
  finding: <specific observed condition>
  evidence: []
  impact:
    user: <impact>
    business_or_delivery: <impact when relevant>
  correction_direction: <behavior or design requirement>
  suspected_layer: <foundation | structure | component | expression | interaction | content | implementation | domain-specialist>
  effort: <low | medium | high>
  confidence: <high | medium | low>
```

Combine repeated symptoms under one root cause. Do not multiply one spacing, token, state, or domain defect into many independent penalties.

### Step 5 — Prioritize

```text
CRITICAL
  applicable hard-gate failure
  or verified score below 5 with material task, message, fidelity,
  accessibility, runtime, safety, or delivery impact

IMPORTANT
  verified score 5–7.9
  or a clear issue weakening comprehension, usability, trust, or consistency

POLISH
  passing or near-passing issue with low task and delivery risk

COVERAGE GAP
  relevant gate or primary domain remains NOT_VERIFIED or uncovered
```

Coverage gaps do not become cosmetic findings. They limit the verdict.

### Step 6 — Recommend the correct lifecycle

```text
local implementation/content/asset fix
  governing rule exists and the defect is isolated

design-refinement
  direction is sound
  primary-domain coverage is sufficient
  failures are specific and passing work should be preserved

redesign-workflow
  direction, macrostructure, or component model is wrong
  failures reveal a broad design-system or experience problem

domain specialist / reviewer
  primary domain is unsupported or specialist evidence is missing

ready
  score, hard gates, coverage, and declared purpose all pass
```

Do not route from average score alone. Consider coverage, hard gates, root cause, direction, and domain ownership.

## Audit Report

Use `design-review/references/review-report.md` and append the lifecycle recommendation.

```markdown
# Design Audit — [target]

## Context
- Design domain: [domain]
- Surface profile: [profile]
- Artifact state: [state]
- Coverage mode: [mode]
- Loaded reviewers: [reviewers]
- Goal: [goal]

## Verdict
**X.XX / 10** — [PASS | CONDITIONAL PASS | NEEDS WORK | CRITICAL | LIMITED REVIEW] · Coverage [X%]

- Hard gates: [status]
- Critical: [count]
- Important: [count]
- Polish: [count]
- Coverage gaps: [count]

## Priority Findings
1. **[finding]** — [severity]
   - Reviewer: ...
   - Evidence: ...
   - Impact: ...
   - Correction direction: ...

## Limitations
- Not applicable: ...
- Not verified: ...
- Domain limitations: ...

## Recommended Action
[local fix | design-refinement | redesign-workflow | domain specialist | ready]
```

The audit ends with the report. Produce or patch only when the user or calling workflow explicitly requests the next lifecycle.