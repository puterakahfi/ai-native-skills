# Evidence and Scoring

Load this reference before assigning any design-review score.

The score is a summary of observed evidence, not a substitute for reasoning. Never assign a precise score to a gate that could not be inspected.

## Gate status

Every selected gate must receive one status:

```text
PASS            verified and meets the review threshold
FAIL            verified and does not meet the threshold
PARTIAL         mixed evidence or only part of the required scope passes
NOT_VERIFIED    relevant, but available evidence cannot prove or disprove it
NOT_APPLICABLE  irrelevant to the selected profile, component, or declared context
```

Rules:

```text
NOT_VERIFIED   is not zero
NOT_APPLICABLE is not zero
PARTIAL        receives a score only for the verified scope and must name the missing scope
PASS           requires suitable evidence
FAIL           requires a specific finding, impact, and evidence
```

## Evidence classes

| Evidence | Suitable for | Typical limitations |
|---|---|---|
| Rendered visual | hierarchy, balance, typography, spacing, color, crop, composition | cannot prove hidden interaction, source consistency, or runtime health |
| Interaction observation | navigation, states, overflow, focus, input behavior, feedback | may miss source-level or untriggered edge cases |
| Runtime capture | errors, asset failures, performance symptoms, flow completion | does not prove visual quality by itself |
| DOM/native accessibility tree | semantics, roles, names, focus relationships | does not prove full usability or visual hierarchy alone |
| Source inspection | tokens, implementation, state coverage, reduced-motion rules | does not prove the rendered result without execution |
| Asset comparison | logo, product, human, content, and brand fidelity | requires approved reference assets |
| Measured output | dimensions, contrast, DPI, safe area, target size | measurements require contextual interpretation |
| User or task evidence | comprehension, success, confusion, business impact | quality depends on sample and method |

Use at least one direct evidence item per failed gate. Release hard gates require evidence appropriate to the gate, not inference from appearance.

## Score rubric

Use a 0–10 score only for verified applicable scope.

```text
10  exceptional: fully resolves the intended need with strong evidence and no meaningful gap
9   strong: clear, robust, and polished with only negligible issues
8   pass: fit for purpose; minor issues do not materially harm the task or message
7   near pass: usable but one clear issue weakens quality or confidence
6   weak: multiple visible issues or one important task/message problem
5   poor: significant friction, confusion, inconsistency, or fidelity risk
3–4 critical: severe problem that materially harms use, comprehension, or delivery
1–2 broken: most of the gate fails or creates serious risk
0   verified complete failure of an applicable gate; never use for missing evidence
```

Default pass threshold: `>= 8.0`.

Scores below 5 are critical. Do not spend review effort on polish while a critical gate remains unresolved.

## Weighting

Weights come from the selected profile and declared goal.

Default:

```text
normal gate          weight 1
profile priority     weight 2
hard gate            pass/fail control; may also carry weight 2
explicit user goal   increase only when directly relevant
```

Do not silently increase weight because the reviewer personally prefers an aspect.

Weighted score:

```text
overall = sum(score × weight for verified applicable gates)
          -------------------------------------------------
          sum(weight for verified applicable gates)
```

Do not include `NOT_VERIFIED` or `NOT_APPLICABLE` in the denominator.

## Coverage

Always report verified coverage beside the score.

```text
coverage = verified applicable weight
           --------------------------
           all applicable selected weight
```

Example:

```text
Overall: 8.4 / 10
Verified coverage: 72%
Not verified: keyboard operation, reduced motion, runtime integrity
```

A high score with low coverage is not release approval.

Suggested verdict policy:

```text
PASS
  overall >= 8.0
  all applicable hard gates pass
  no critical gate
  sufficient coverage for the declared review depth

CONDITIONAL PASS
  overall >= 8.0
  no verified hard-gate failure
  relevant gates remain NOT_VERIFIED or accepted risk remains

NEEDS WORK
  overall < 8.0
  or one or more important gates fail

CRITICAL
  any applicable hard gate fails
  or any verified gate is below 5 and materially blocks the declared purpose
```

## Hard gates are contextual

A gate is hard only when its triggering context applies.

Examples:

```text
RI1 runtime integrity
  hard for release review of a rendered interactive flow
  NOT_VERIFIED for screenshot-only review
  NOT_APPLICABLE for a poster

G21 reduced motion
  hard for release review when motion exists or can be introduced by the platform
  NOT_VERIFIED from screenshot-only evidence
  NOT_APPLICABLE to a static image

SV8–SV11 fidelity and content accuracy
  hard for commercial delivery when a supplied logo, product, person, price, date, contact, or claim must be preserved
  NOT_APPLICABLE only when no specific asset or fact is required
```

Never create a global hard gate that automatically fails unrelated surface types.

## Finding quality

Every failed or partial gate must include:

```yaml
finding:
  gate: I4
  status: FAIL
  score: 6
  region: category-tabs
  observation: only the next chevron is visible after overflow; users cannot discover the previous direction
  evidence:
    - type: interaction
      context: tablet landscape after scrolling right
  impact:
    user: returning to earlier categories is difficult and the control appears one-directional
    business: discovery of earlier gallery categories may decrease
  recommendation: expose synchronized previous and next affordances based on scroll position
  confidence: high
  effort: low
```

Avoid findings such as:

```text
“spacing feels off”
“make it more premium”
“typography could be improved”
“use a better component”
```

Translate qualitative feedback into an observable condition, affected task or message, governing gate, and specific correction direction.

## Review depth and evidence expectations

### Quick

```text
critical universal gates
profile hard gates that can be verified
user-declared issue
no release claim
```

### Focused

```text
selected lenses and components
adjacent regression gates
relevant hard gates when evidence exists
```

### Full

```text
all applicable universal gates
all applicable profile gates
all present major components
coverage and evidence gaps
```

### Release

```text
full review
all applicable hard gates verified
required states and realistic content
required viewports, sizes, themes, and input methods
runtime or export integrity
no pass claim when coverage is insufficient
```

## Review sequence

```text
1. Verify route and context.
2. Run applicable hard gates.
3. Stop and report immediately if a hard gate fails materially.
4. Score universal gates.
5. Score profile gates.
6. Score selected components.
7. Reconcile duplicate findings under the governing root cause.
8. Calculate score and coverage.
9. Produce prioritized findings and limitations.
```

Do not average repeated symptoms as separate failures. One underlying spacing-token defect affecting six cards should be one system finding with affected regions, not six score penalties.