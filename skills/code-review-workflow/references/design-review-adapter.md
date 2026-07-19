# Design Review Adapter for Code Review

Load this reference only when a submission can change user-facing appearance, interaction, state, accessibility, content fidelity, responsiveness, or generated/exported visual output.

The code-review workflow owns merge orchestration. The `design-review` facade and its loaded domain reviewers own design routing, gates, evidence normalization, scoring, coverage, and design verdict.

## Trigger

Run the design check when code can change:

```text
rendered appearance, typography, spacing, hierarchy, color, or assets
interaction, navigation, focus, overflow, responsive/adaptive behavior
loading, empty, error, permission, success, or destructive states
generated/exported poster, PDF, slide, thumbnail, or other visual output
accessibility semantics or operability
logo, product, person, price, claim, or required-content fidelity
```

Do not classify design as unaffected merely because the diff contains only CSS, tokens, component props, content data, templates, or generation configuration.

## Facade Route

Start with `design-review/SKILL.md` and record:

```yaml
design_review_route:
  design_domain: <digital-interface | visual-communication | presentation | other>
  surface_profile: <profile>
  artifact_state: <rendered-interactive | rendered-static | source-only | mixed>
  review_depth: <focused | release>
  coverage_mode: <BUILT_IN | ADAPTER_COVERED | LIMITED | ROUTE_ELSEWHERE>
  domain_reviewers: []
  selected_components: []
  changed_regions: []
  required_viewing_contexts: []
  evidence_available: []
  evidence_gaps: []
```

Use `focused` for a bounded PR. Use `release` only when code review is the final design-acceptance boundary and all required evidence exists.

## Evidence Policy

### Source only

Source inspection may verify:

```text
token and contract usage
component and state implementation
content and required-asset references
semantic structure visible in source
presence of reduced-motion or responsive rules
```

It cannot verify the rendered result. Mark visual, interaction, runtime, and export claims `NOT_VERIFIED` and do not approve changed user-facing output.

### Rendered interactive or mixed

Inspect only relevant changed and regression contexts:

```text
changed regions at required viewports and themes
changed interactions and expected inputs
loading, empty, error, success, permission, and destructive states when affected
overflow and adaptive substitution
runtime evidence when executable behavior changed
accessibility semantics, focus, labels, and keyboard path when affected
required asset/content fidelity
```

A screenshot can verify visible composition but cannot prove keyboard operation, post-interaction overflow, reduced motion, console/runtime integrity, or hidden states.

### Rendered static or mixed static output

Inspect:

```text
final dimensions and actual destination placement
crop, bleed, safe area, and thumbnail/actual-size legibility
logo, product, person, copy, price, date, contact, and claim fidelity
export resolution, compression, edges, and color handling
```

## Facade Loading

Load references phase-by-phase:

```text
CLASSIFY / ROUTE
  design-review/references/review-routing.md
  design-review/references/facade-boundary.md when domain coverage is unclear

UNIVERSAL REVIEW
  design-review/references/universal-gates.md

DOMAIN / SURFACE REVIEW
  interactive-surface-gates.md OR static-visual-gates.md OR external reviewer

COMPONENT REVIEW
  component-review.md only for affected components

EVIDENCE + SCORE
  evidence-and-scoring.md

REPORT
  review-report.md
```

Do not maintain a duplicate design checklist in code review.

## Verdict Mapping

```text
PASS
  eligible for approval

CONDITIONAL PASS
  eligible only when every remaining risk is explicit, non-blocking,
  and accepted by the configured authority

NEEDS WORK
  request changes

CRITICAL
  block

LIMITED REVIEW
  block complete-domain approval; load the required domain reviewer
  or explicitly narrow the claim and merge scope

ROUTE_ELSEWHERE
  block until the required specialist reviewer is available

required acceptance remains NOT_VERIFIED
  request evidence or changes; do not silently approve
```

A high score cannot override failed hard gates, weak evidence coverage, or missing primary-domain coverage.

## Handoff to Final Verdict

Return:

```yaml
design_review_result:
  verdict: <verdict>
  score: <verified score or N/A>
  evidence_coverage: <percentage or N/A>
  primary_domain_coverage: <complete | limited | unavailable>
  hard_gates: <passed | failed | not verified>
  blocking_findings: []
  non_blocking_findings: []
  evidence_gaps: []
  domain_limitations: []
  recommended_merge_mapping: <eligible | conditional | request-changes | block>
```

Every blocking design finding must include the governing reviewer, evidence, affected file/region, impact, and required correction or evidence.
