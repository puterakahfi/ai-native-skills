# Evidence and Scoring

Load this reference before assigning any design-review score.

A score summarizes verified applicable evidence. It does not replace reasoning, primary-domain coverage, or contextual hard gates.

## Gate Status

Every selected gate receives exactly one status:

```text
PASS            verified and meets the threshold
FAIL            verified and does not meet the threshold
PARTIAL         mixed evidence or only part of the required scope passes
NOT_VERIFIED    relevant, but evidence cannot prove or disprove it
NOT_APPLICABLE  irrelevant to the selected domain, profile, component, or context
```

Rules:

```text
NOT_VERIFIED   is not zero
NOT_APPLICABLE is not zero
PARTIAL        scores only verified scope and names missing scope
PASS           requires suitable direct evidence
FAIL           requires observation, evidence, impact, and correction direction
```

## Two Different Coverage Dimensions

Do not collapse these into one percentage.

### Primary-domain coverage

```text
BUILT_IN
  the facade has a complete built-in reviewer for the primary domain

ADAPTER_COVERED
  a declared external reviewer covers the primary domain and maps to the facade contract

LIMITED
  universal or adjacent-domain review is possible, but the primary-domain reviewer is missing

ROUTE_ELSEWHERE
  the requested claim cannot be responsibly reviewed by the available facade/reviewers
```

Primary-domain coverage determines the verdict ceiling.

```text
BUILT_IN / ADAPTER_COVERED
  PASS, CONDITIONAL PASS, NEEDS WORK, or CRITICAL are available

LIMITED
  maximum complete-domain verdict is LIMITED REVIEW

ROUTE_ELSEWHERE
  do not calculate or present a misleading complete-domain verdict
```

### Evidence coverage

Evidence coverage measures how much of the selected applicable gate weight was actually verified.

```text
evidence_coverage = verified applicable weight
                    --------------------------
                    all applicable selected weight
```

A high evidence percentage does not repair missing primary-domain coverage. A complete domain reviewer with weak evidence also cannot issue release approval.

## Evidence Classes

| Evidence | Suitable for | Typical limitations |
|---|---|---|
| Rendered visual | hierarchy, balance, typography, spacing, color, crop, composition | cannot prove hidden interaction, source consistency, runtime, or specialist-domain production quality |
| Interaction observation | navigation, states, overflow, focus, input behavior, feedback | may miss source-level and untriggered edge cases |
| Runtime capture | errors, asset failures, performance symptoms, flow completion | does not prove visual or domain quality alone |
| DOM/native accessibility tree | semantics, roles, names, focus relationships | does not prove full usability or visual hierarchy alone |
| Source inspection | tokens, implementation, state coverage, reduced motion | does not prove rendered behavior without execution |
| Asset comparison | logo, product, human, content, brand fidelity | requires approved references and may not cover system-level identity quality |
| Measured output | dimensions, contrast, DPI, safe area, target size | measurements require contextual interpretation |
| User/task evidence | comprehension, success, confusion, business impact | quality depends on method and sample |
| Domain evidence | specialist tests, production constraints, standards, physical/process proof | valid only when required by and interpreted through the domain reviewer |

Use at least one direct evidence item per failed gate. Hard gates require evidence appropriate to the governing reviewer, not inference from appearance.

## Score Rubric

Use 0–10 only for verified applicable scope.

```text
10  exceptional: fully resolves the intended need with strong evidence and no meaningful gap
9   strong: clear, robust, and polished with only negligible issues
8   pass: fit for purpose; minor issues do not materially harm the task or message
7   near pass: usable but one clear issue weakens quality or confidence
6   weak: multiple visible issues or one important task/message/domain problem
5   poor: significant friction, confusion, inconsistency, or fidelity risk
3–4 critical: severe problem materially harming use, comprehension, safety, or delivery
1–2 broken: most of the gate fails or creates serious risk
0   verified complete failure of an applicable gate; never use for missing evidence
```

Default pass threshold: `>= 8.0`.

Scores below 5 are critical. Do not spend review effort on polish while a critical gate or primary-domain coverage gap remains unresolved.

## Weighting

Weights come from the selected profile, domain reviewer, declared goal, and applicable hard-gate policy.

```text
normal gate            weight 1
profile/domain priority weight 2
hard gate              pass/fail control; may also carry weight 2
explicit user goal     increase only when directly relevant
```

Do not silently increase weight because the reviewer prefers an aspect.

```text
overall = sum(score × weight for verified applicable gates)
          -------------------------------------------------
          sum(weight for verified applicable gates)
```

Exclude `NOT_VERIFIED` and `NOT_APPLICABLE` from the score denominator. Still include relevant `NOT_VERIFIED` weight in evidence-coverage calculations.

## Verdict Policy

```text
PASS
  primary-domain coverage is BUILT_IN or ADAPTER_COVERED
  overall >= 8.0
  all applicable hard gates pass
  no material critical gate
  evidence coverage is sufficient for the declared depth

CONDITIONAL PASS
  primary-domain coverage is BUILT_IN or ADAPTER_COVERED
  overall >= 8.0
  no verified hard-gate failure
  evidence gaps or accepted risks remain
  the current approval boundary explicitly permits them

NEEDS WORK
  primary-domain coverage exists
  overall < 8.0
  or one or more important gates fail

CRITICAL
  any applicable hard gate fails
  or a verified gate below 5 materially blocks the declared purpose

LIMITED REVIEW
  primary-domain coverage is LIMITED
  universal or adjacent-domain findings may still be reported
  no complete-domain, release, production-ready, or final-approval claim is allowed

ROUTE_ELSEWHERE
  requested review claim cannot be supported by available reviewers
  stop scoring the unsupported claim and hand off
```

Example:

```text
Overall verified gates: 8.4 / 10
Evidence coverage: 72%
Primary-domain coverage: LIMITED
Verdict: LIMITED REVIEW
Reason: no brand-identity reviewer was loaded
```

The 8.4 score describes verified universal scope only; it does not approve the identity system.

## Contextual Hard Gates

A gate is hard only when its triggering context and governing reviewer apply.

```text
RI1 runtime integrity
  hard for release review of a rendered interactive flow
  NOT_VERIFIED for screenshot-only review
  NOT_APPLICABLE for a poster

G21 reduced motion
  hard for release review when motion exists or can be introduced
  NOT_VERIFIED from screenshot-only evidence
  NOT_APPLICABLE to a static image

SV8–SV11 fidelity/content accuracy
  hard for commercial delivery when supplied logo, product, person,
  price, date, contact, or claim must be preserved

specialized domain hard gates
  declared by the loaded domain reviewer
  cannot be invented by the facade or inferred from universal gates
```

Never create one global hard gate that fails unrelated domains.

## Finding Contract

Every failed or partial gate includes:

```yaml
finding:
  gate: I4
  governing_reviewer: built-in-interactive
  status: FAIL
  score: 6
  region: category-tabs
  observation: only the next overflow direction is visible after scrolling
  evidence:
    - type: interaction
      context: tablet landscape after scrolling right
  impact:
    user: returning to earlier categories is difficult
    business_or_delivery: discovery of earlier categories may decrease
  recommendation: expose synchronized previous and next affordances or substitute a control that preserves discoverability
  confidence: high
  effort: low
```

Avoid:

```text
“spacing feels off”
“make it more premium”
“typography could be improved”
“use a better component”
```

Translate qualitative feedback into an observable condition, governing gate/reviewer, affected outcome, and correction direction.

## Review Depth Expectations

### Quick

```text
critical universal gates
verifiable profile/domain hard gates
user-declared issue
no release or complete-domain claim
```

### Focused

```text
selected gates/components
adjacent regression gates
relevant hard gates when evidence exists
inherited primary-domain coverage
```

### Full

```text
all applicable universal gates
all applicable gates from every loaded reviewer
major present components
complete evidence gaps and scope limitations
full only when primary-domain coverage exists
```

### Release

```text
full review
BUILT_IN or ADAPTER_COVERED primary domain
all applicable hard gates verified
required states, content, assets, sizes, themes, and input methods
runtime, export, or specialist-domain delivery evidence
no pass claim when evidence or domain coverage is insufficient
```

## Review Sequence

```text
1. Verify design domain, surface, artifact state, and review depth.
2. Resolve primary-domain coverage and loaded reviewers.
3. Stop or limit the claim for ROUTE_ELSEWHERE or LIMITED coverage.
4. Run applicable hard gates from loaded reviewers.
5. Stop and report immediately when a hard gate fails materially.
6. Score universal gates.
7. Score domain/profile and selected component gates.
8. Reconcile repeated symptoms under the governing root cause.
9. Calculate verified score and evidence coverage separately.
10. Produce prioritized findings, domain limitations, and handoff.
```

Do not average repeated symptoms as independent failures. One underlying system defect affecting many regions receives one root-cause finding with affected locations.