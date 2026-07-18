# Review Report

Use this reference during the final reporting phase.

A useful review states the design domain, loaded reviewers, evidence, score coverage, failed gates, scope limitations, and next lifecycle. Do not dump an unprioritized gate inventory.

## Mandatory Report Structure

```markdown
# Design Review — [target]

## Review Context
- Design domain: [domain]
- Surface profile: [profile]
- Artifact state: [state]
- Review depth: [quick | focused | full | release]
- Coverage mode: [BUILT_IN | ADAPTER_COVERED | LIMITED | ROUTE_ELSEWHERE]
- Loaded reviewers: [built-in and external reviewers]
- Goal: [declared user, message, business, or delivery goal]
- Viewing contexts: [viewports, dimensions, channel, distance, themes, inputs]
- Evidence: [visual, interaction, runtime, source, assets, measurements, task evidence]

## Verdict
**[X.XX / 10]** — [PASS | CONDITIONAL PASS | NEEDS WORK | CRITICAL | LIMITED REVIEW]

- Verified evidence coverage: [X%]
- Primary-domain coverage: [complete | limited | unavailable]
- Applicable hard gates: [passed | failed | not verified]
- Critical findings: [count]
- Important findings: [count]
- Coverage gaps: [count]

## Executive Findings
1. **[Finding title]** — [severity]
   - Governing reviewer: [reviewer]
   - Observation: [specific condition]
   - Evidence: [where and how observed]
   - Impact: [user, message, business, accessibility, fidelity, runtime, or delivery]
   - Recommendation: [specific correction direction]

## Gate Summary
| Reviewer / cluster | Score | Coverage | Status | Notes |
|---|---:|---:|---|---|
| Universal visual quality | X.X | X% | ... | ... |
| Domain or surface quality | X.X | X% | ... | ... |
| Components | X.X | X% | ... | ... |
| Runtime, fidelity, or export | X.X | X% | ... | ... |
| External domain reviewer | X.X / N/A | X% | ... | ... |

## Priority
### Critical
- [finding]

### Important
- [finding]

### Polish
- [finding]

### Coverage Gaps
- [missing reviewer, evidence, state, viewport, input, asset, or domain proof]

## Limitations
- Not applicable: [gates and reason]
- Not verified: [gates and missing evidence]
- Domain limitations: [unsupported or partially covered scope]
- Accepted risks: [explicit risks]

## Recommended Next Action
[local fix | design-refinement | redesign-workflow | domain specialist/reviewer | ready to deliver]
```

A `LIMITED REVIEW` may include scores for verified universal or partial-domain gates, but those scores must not be presented as complete primary-domain approval.

## Focused Review Format

Use during active iteration:

```markdown
## [target] · Focused Design Review

**X.X / 10** — [status] · Evidence coverage [X%]

- Design domain: [domain]
- Coverage mode: [mode]
- Reviewers: [reviewers]

**What improved**
- [verified improvement]

**Open findings**
- `[gate]` [score/status] — [observation] → [correction direction]

**Regression check**
- [passing adjacent gates and locks preserved]

**Not verified / limited**
- [missing evidence or reviewer]
```

Do not display a full scorecard when only one layer, component, or declared gate changed.

## Finding Order

```text
1. primary-domain coverage failure or ROUTE_ELSEWHERE
2. applicable hard-gate failure
3. task, message, fidelity, accessibility, safety, runtime, or delivery blocker
4. important hierarchy, component, state, responsive, or narrative issue
5. consistency and polish
```

Do not order findings by gate ID.

## Severity and Coverage

```text
CRITICAL
  applicable hard-gate failure
  or score below 5 with material delivery/task/domain impact

IMPORTANT
  score 5–7.9
  or clear issue weakening comprehension, use, fidelity, trust, or confidence

POLISH
  passing or near-passing issue with low task and delivery risk

COVERAGE GAP
  relevant gate, required evidence, or primary-domain reviewer is missing
```

`LIMITED REVIEW` is a verdict about domain coverage, not a severity level. A limited review may still contain critical verified universal findings.

## Recommendation Quality

Recommendations must state the required behavior or correction direction without pretending one visual implementation is universally correct.

Good:

```text
Replace the narrow-width tabs with a treatment that keeps peer categories discoverable, exposes both overflow directions, preserves selected state, and remains operable by the expected inputs.
```

Weak:

```text
Use better tabs.
Make spacing cleaner.
Make it premium.
```

When the defect is implementation-specific, name the required behavior before suggesting a library component.

## Score Presentation Rules

- Score only verified applicable gates.
- Display evidence coverage beside the score.
- Display primary-domain coverage separately from evidence coverage.
- Show hard-gate status separately from the average.
- Show `NOT_VERIFIED` and `NOT_APPLICABLE` explicitly.
- Show the governing reviewer for domain-specific findings.
- Do not claim full, release, or production readiness under `LIMITED REVIEW`.
- Do not use a fenced code block for the main markdown scorecard.
- Do not create false precision from screenshot-only or universal-only review.

## Handoff Rules

Recommend `design-refinement` when:

```text
direction is sound
failures are specific and verified
passing areas should be preserved
primary-domain coverage is BUILT_IN or ADAPTER_COVERED
```

Recommend `redesign-workflow` when:

```text
direction, macrostructure, visual language, or component model is wrong
multiple foundational layers require coordinated replacement
primary-domain reviewer supports the redesign acceptance criteria
```

Recommend a local implementation/content/asset fix when:

```text
the governing rule already exists
the defect is isolated to code, data, copy, assets, or configuration
no new design decision is required
```

Recommend a domain specialist or reviewer when:

```text
coverage_mode is LIMITED or ROUTE_ELSEWHERE
the requested claim requires specialist-domain gates
universal visual review cannot certify the requested outcome
```

A review report never silently expands into redesign or production unless the user requested it or the calling workflow owns that phase.