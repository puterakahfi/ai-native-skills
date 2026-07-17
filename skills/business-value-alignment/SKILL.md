---
name: business-value-alignment
description: Align requests, features, redesigns, and product ideas to user value, business value, measurable outcomes, assumptions, risks, and an explicit continue/narrow/experiment/stop verdict before execution.
license: MIT
metadata:
  ai-native-skills.version: 1.0.0
  ai-native-skills.author: puterakahfi
  ai-native-skills.type: skill
  ai-native-skills.implements: ai-native-core/contracts/skills/product/business-value-alignment.contract.yaml
  ai-native-skills.contract-version: "^1.0.0"
  ai-native-skills.related_skills: '["experiment-design", "product-manager", "product-requirements", "decision-making", "user-research", "cro", "observability-design"]'
---

# Business Value Alignment

## Hard Rule

```
No major work starts until the value hypothesis and success evidence are explicit.
```

## When to Use

Use when the user asks to build, prioritize, refine, or evaluate features/MVPs — or decide whether a feature is worth building. Run this before PRD/spec/implementation.

Do not use for: pure syntax/bug fixes; detailed PRD writing (`product-requirements`); architecture records (`adr`).

## Required Output

```markdown
# Business Value Alignment

## Request
<what was asked>

## User Value
- User/customer: <who>
- Pain/opportunity: <what improves>
- Value created: <specific benefit>

## Business Value
- Value type: revenue | activation | retention | credibility | efficiency | risk reduction | learning | strategic option
- Why it matters: <business rationale>
- Value confidence: High | Medium | Low

## Metrics
- Leading metric: <early signal>
- Lagging metric: <outcome signal>
- Guardrail metric: <must not regress>

## Evidence Labels
- Known: <facts/tool evidence/user-provided facts>
- Assumed: <plausible but unverified>
- Unknown: <needs discovery/experiment>

## Risks
- <risk> → mitigation: <mitigation>

## Recommendation
Verdict: CONTINUE | NARROW_SCOPE | EXPERIMENT_FIRST | STOP
Rationale: <why>
Next gate: <approval/experiment-design/PRD/spec/implementation gate>
```

## Value Types

| Value type | Meaning | Example metric |
|---|---|---|
| Revenue | Creates or protects revenue | paid conversion, ARPA, qualified leads |
| Activation | Gets users to first value faster | signup→first action rate, time-to-value |
| Retention | Keeps valuable users engaged | repeat usage, churn reduction |
| Credibility | Improves trust or positioning | qualified inbound, project clickthrough |
| Efficiency | Reduces time/cost/operational load | minutes saved, manual steps removed |
| Risk reduction | Lowers security, reliability, compliance risk | incident rate, audit findings |
| Learning | Reduces uncertainty before larger investment | interviews, waitlist, prototype feedback |
| Strategic option | Preserves valuable future paths | reversible architecture, validated demand |

## Metrics Rule

Every alignment must include:
```
leading metric   = early signal the work is moving right
lagging metric   = final outcome the business cares about
guardrail metric = important thing that must not regress
```

Examples:
```
Landing page: Leading: clickthrough/CTA clicks | Lagging: qualified inbound | Guardrail: load time/accessibility
Affiliate MVP:  Leading: waitlist signups/interviews | Lagging: paid beta conversion | Guardrail: generated content accuracy
Refactor:       Leading: tests pass, less duplication | Lagging: lower change failure rate | Guardrail: public behavior/perf
```

## Evidence Labels

```
KNOWN   = backed by user statement, repo artifact, analytics, or tool output
ASSUMED = plausible but not yet verified
UNKNOWN = material uncertainty that should affect scope or sequencing
```

If the core value claim is mostly `UNKNOWN`, recommend discovery or load `experiment-design` first.

## Verdict Rules

| Verdict | Use when | Next gate |
|---|---|---|
| `CONTINUE` | Value is clear enough, metrics defined, risk acceptable | PRD/spec/implementation gate |
| `NARROW_SCOPE` | Value is real but scope too broad | reduced MVP/slice approval |
| `EXPERIMENT_FIRST` | Value plausible but key assumptions unverified | `experiment-design` or discovery |
| `STOP` | Value is weak, not strategic, not measurable, or risk/cost dominates | explain why and suggest alternatives |

## Workflow Integration

- **Product from zero:** `discovery → business-value-alignment → experiment-design (if needed) → PRD/MVP`
- **UI/UX refinement:** `audit → business-value-alignment → redesign spec → prototype/patch`
- **Feature work:** `feature request → business-value-alignment → spec/work plan`

Do not produce a PRD until value hypothesis and success metrics are explicit.

## Example — Affiliate Product Idea

```markdown
## User Value
- User/customer: affiliators managing product recommendations and campaigns
- Pain/opportunity: campaign creation, publishing, and tracking are fragmented
- Value created: less operational overhead and faster campaign production

## Business Value
- Value type: learning + revenue option
- Why it matters: validates a possible paid product before full dashboard investment
- Value confidence: Low/Medium

## Metrics
- Leading: waitlist signups and interview bookings
- Lagging: paid beta conversion or weekly retained campaign creation
- Guardrail: generated campaign accuracy/trust does not regress

## Evidence Labels
- Known: target segment named by user
- Assumed: affiliators feel friction in campaign creation/tracking
- Unknown: willingness to pay, must-have workflow, distribution channel

## Recommendation
Verdict: EXPERIMENT_FIRST
Rationale: value is plausible but core demand and willingness-to-pay are unverified
Next gate: experiment design before PRD/MVP build
```

## Common Pitfalls

1. **Decorative value.** "Looks better" is not enough — tie UI work to clarity, credibility, conversion, or friction.
2. **Metric theater.** Don't invent vanity metrics. Use metrics that could change a decision.
3. **Business-only framing.** Value must include user value; business value without user value is extraction.
4. **Skipping uncertainty.** If important claims are unknown, say so and recommend discovery first.
5. **Overbuilding on weak evidence.** Low-confidence value should narrow scope or move to experiment.
6. **No guardrail.** Every positive metric needs a "must not regress" counterpart.

## Verification Checklist

- [ ] User value is explicit and tied to a real user/customer.
- [ ] Business value type is named.
- [ ] Leading, lagging, and guardrail metrics are present.
- [ ] Claims are labeled as known, assumed, or unknown.
- [ ] Risks and mitigations are listed.
- [ ] Verdict is one of `CONTINUE`, `NARROW_SCOPE`, `EXPERIMENT_FIRST`, or `STOP`.
- [ ] Next gate is explicit.
