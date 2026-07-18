# Review Report

Use this reference during the final reporting phase.

A useful design review explains what was reviewed, what evidence exists, what failed, why it matters, and what should change. Do not dump an unprioritized wall of gate scores.

## Mandatory report structure

```markdown
# Design Review — [target]

## Review Context
- Surface profile: [profile]
- Artifact state: [state]
- Review depth: [quick | focused | full | release]
- Goal: [declared user or business goal]
- Viewing contexts: [viewports, dimensions, channels, distance]
- Evidence: [rendered visual, interaction, runtime, source, assets, measurements]

## Verdict
**[X.XX / 10]** — [PASS | CONDITIONAL PASS | NEEDS WORK | CRITICAL]

- Verified coverage: [X%]
- Applicable hard gates: [passed / failed / not verified]
- Critical findings: [count]
- Important findings: [count]

## Executive Findings
1. **[Finding title]** — [severity]
   - Observation: [specific condition]
   - Evidence: [where and how observed]
   - Impact: [user/message/business/delivery impact]
   - Recommendation: [specific correction direction]

## Gate Summary
| Cluster | Score | Coverage | Status | Notes |
|---|---:|---:|---|---|
| Universal visual quality | X.X | X% | ... | ... |
| Surface-specific quality | X.X | X% | ... | ... |
| Components | X.X | X% | ... | ... |
| Fidelity or runtime | X.X | X% | ... | ... |

## Component Findings
[Only selected/present components]

## Priority
### Critical
- [finding]

### Important
- [finding]

### Polish
- [finding]

## Limitations
- Not applicable: [gates and reason]
- Not verified: [gates and missing evidence]
- Accepted risks: [declared risks]

## Recommended Next Action
[design-refinement | redesign-workflow | implementation fix | content correction | ready to deliver]
```

## Quick review format

Use during active iteration:

```markdown
## [target] · Focused Design Review

**X.X / 10** — [status] · Coverage [X%]

**What improved**
- [verified improvement]

**Open findings**
- `[gate]` [score/status] — [observation] → [specific fix direction]

**Regression check**
- [passing adjacent gates preserved]

**Not verified**
- [missing evidence]
```

Do not run or display a full scorecard when only one layer or component changed.

## Finding order

Order findings by:

```text
1. applicable hard-gate failure
2. task, message, fidelity, accessibility, or runtime blocker
3. important hierarchy, component, state, or responsive issue
4. consistency and polish
```

Do not order findings by document gate ID.

## Severity mapping

```text
CRITICAL
  hard-gate failure or score below 5 with material delivery/task impact

IMPORTANT
  score 5–7.9 or a clear issue that weakens comprehension, use, fidelity, or confidence

POLISH
  passing or near-passing quality issue with low task risk
```

A score of 7.9 is not automatically more important than a score of 6.0. Consider impact, frequency, reach, reversibility, and the declared goal.

## Recommendations

Recommendations must state the correction direction without pretending there is only one valid visual solution.

Good:

```text
Replace the narrow-width tabs with a horizontally scrollable tab treatment that exposes both previous and next overflow states, or substitute a control that keeps all primary categories discoverable.
```

Weak:

```text
Use better tabs.
Make spacing cleaner.
Make it premium.
```

When the problem is implementation-specific, name the behavior rather than prescribing an arbitrary library component.

## Score presentation rules

- Score only verified applicable gates.
- Display coverage beside the score.
- Show hard-gate status separately from the average.
- Show `NOT_VERIFIED` and `NOT_APPLICABLE` explicitly.
- Do not use a fenced code block for the main markdown scorecard.
- Do not claim “all passed” when important gates were not verified.
- Do not create false precision from screenshot-only review.

## Handoff rules

Recommend `design-refinement` when:

```text
direction is sound
failing gates are specific
passing areas should be preserved
```

Recommend `redesign-workflow` when:

```text
direction or macrostructure is wrong
multiple critical clusters fail
the selected component model cannot support the task
```

Recommend a local implementation fix when:

```text
the governing skill already contains the correct rule
the defect is isolated to code, data, assets, or runtime configuration
```

Recommend content or asset correction when:

```text
the design structure is sound but claims, product, face, logo, price, contact, or supplied content is inaccurate
```

A review report should never silently expand into redesign work unless the user requested production or the calling workflow owns the fix phase.