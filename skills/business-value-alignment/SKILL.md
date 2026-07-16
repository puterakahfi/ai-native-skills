---
name: business-value-alignment
description: Align requests, features, redesigns, and product ideas to user value, business value, measurable outcomes, assumptions, risks, and an explicit continue/narrow/experiment/stop verdict before execution.
license: MIT
metadata:
  ai-native-skills.version: 1.0.0
  ai-native-skills.author: puterakahfi
  ai-native-skills.type: skill
  ai-native-skills.implements: ai-native-core/contracts/skills/business/business-value-alignment.contract.yaml
  ai-native-skills.related_skills: '[''experiment-design'', ''product-manager'', ''product-requirements'', ''decision-making'', ''user-research'', ''cro'', ''observability-design'']'
---

# Business Value Alignment

## Overview

Use this skill to make work value-driven before it becomes execution. It connects a request to user value, business value, measurable outcomes, assumptions, risks, and a clear decision on whether to continue, narrow scope, run an experiment, or stop.

This skill implements:

```text
ai-native-core/contracts/skills/business/business-value-alignment.contract.yaml
```

Core principle:

```text
No major work starts until the value hypothesis and success evidence are explicit.
```

## When to Use

Use when the user asks to:

- build a product, MVP, feature, or workflow from an idea
- refine a landing page, dashboard, onboarding flow, or product surface
- prioritize product/engineering work
- decide whether a feature is worth building
- connect a redesign or implementation request to business value
- define success metrics before PRD/spec/implementation
- evaluate whether to continue, narrow scope, experiment first, or stop

Do not use for:

- pure syntax/bug fixes with obvious value and no product tradeoff
- detailed PRD writing; use `product-requirements` after this skill
- architecture records; use `adr` and architecture skills
- analytics implementation details; use product/runtime-specific instrumentation guidance

## Required Output

Always produce this compact brief before recommending execution:

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

Use the strongest applicable value type, not a vague “improve UX.”

| Value type | Meaning | Example metric |
|---|---|---|
| Revenue | Creates or protects revenue | paid conversion, ARPA, qualified leads |
| Activation | Gets users to first value faster | signup→first action rate, time-to-value |
| Retention | Keeps valuable users engaged | repeat usage, churn reduction |
| Credibility | Improves trust or positioning | qualified inbound, project clickthrough |
| Efficiency | Reduces time/cost/operational load | minutes saved, manual steps removed |
| Risk reduction | Lowers security, reliability, compliance, or delivery risk | incident rate, audit findings |
| Learning | Reduces uncertainty before larger investment | interviews, waitlist, prototype feedback |
| Strategic option | Preserves valuable future paths | reversible architecture, validated demand |

## Metrics Rule

Every alignment must include three metric classes:

```text
leading metric   = early signal the work is moving in the right direction
lagging metric   = final outcome the business cares about
guardrail metric = important thing that must not regress
```

Examples:

```text
Landing page refinement:
  Leading: project-link clickthrough, contact CTA clicks
  Lagging: qualified inbound opportunities
  Guardrail: page load time and accessibility do not regress

Affiliate product idea:
  Leading: waitlist signups, interview bookings, sample campaign kit usage
  Lagging: paid beta conversion or retained weekly usage
  Guardrail: generated content accuracy and trust do not regress

Engineering refactor:
  Leading: affected tests pass, reduced duplicated code paths
  Lagging: lower change failure rate or faster feature delivery
  Guardrail: public behavior and performance do not regress
```

## Evidence Labels

Label every important value claim:

```text
KNOWN   = backed by user statement, repo artifact, analytics, customer feedback, or tool output
ASSUMED = plausible but not yet verified
UNKNOWN = material uncertainty that should affect scope or sequencing
```

If the core value claim is mostly `UNKNOWN`, do not recommend a full build. Recommend discovery or load `experiment-design` first.

## Verdict Rules

| Verdict | Use when | Next gate |
|---|---|---|
| `CONTINUE` | Value is clear enough, metrics are defined, risk is acceptable | PRD/spec/implementation gate |
| `NARROW_SCOPE` | Value is real but requested scope is too broad | reduced MVP/slice approval |
| `EXPERIMENT_FIRST` | Value is plausible but key assumptions are unverified | `experiment-design` or discovery |
| `STOP` | Value is weak, not strategic, not measurable, or risk/cost dominates | explain why and suggest alternatives |

## Workflow Integration

### Product from zero

In `product-development-workflow`, run this during discovery before PRD:

```text
opportunity discovery → business-value-alignment → experiment-design when needed → PRD/MVP recommendation
```

Do not produce a PRD until the value hypothesis and success metrics are explicit. If the verdict is `EXPERIMENT_FIRST`, produce an experiment design before PRD/build.

### Existing UI/UX refinement

In `redesign-workflow`, run this before visual production:

```text
audit → business-value-alignment → redesign spec → prototype/patch
```

For landing pages and portfolios, avoid decorative redesign unless clarity, credibility, conversion, or accessibility value is explicit.

### Feature work

In `new-feature-workflow`, use this when value or priority is unclear:

```text
feature request → business-value-alignment → spec/work plan
```

If the feature is low-value or mostly unknown, recommend `EXPERIMENT_FIRST` or `NARROW_SCOPE`.

## Example — Landing Page Refinement

```markdown
# Business Value Alignment

## Request
Refine https://pkahfi.com.

## User Value
- User/customer: hiring managers, collaborators, technical clients
- Pain/opportunity: visitors need to understand credibility and live work quickly
- Value created: clearer positioning and easier path to inspect work/contact

## Business Value
- Value type: credibility
- Why it matters: improves qualified inbound opportunities and reduces explanation needed in DMs/calls
- Value confidence: Medium

## Metrics
- Leading metric: project-link clickthrough and contact CTA clicks
- Lagging metric: qualified inbound opportunities
- Guardrail metric: page load and accessibility do not regress

## Evidence Labels
- Known: site exists and user asked for refinement
- Assumed: visitors currently need clearer positioning
- Unknown: baseline traffic, clickthrough, inbound conversion

## Risks
- Over-polishing without clearer positioning → mitigation: constrain redesign to clarity, hierarchy, and credibility

## Recommendation
Verdict: CONTINUE
Rationale: small-scope refinement has plausible credibility upside and low reversibility risk
Next gate: redesign audit/spec approval before code
```

## Example — Affiliate Product Idea

```markdown
# Business Value Alignment

## Request
Build a digital product for affiliators from zero.

## User Value
- User/customer: affiliators managing product recommendations and campaigns
- Pain/opportunity: campaign creation, publishing, and tracking are fragmented
- Value created: less operational overhead and faster campaign production

## Business Value
- Value type: learning + revenue option
- Why it matters: validates a possible paid product before full dashboard investment
- Value confidence: Low/Medium

## Metrics
- Leading metric: qualified waitlist signups and interview bookings
- Lagging metric: paid beta conversion or weekly retained campaign creation
- Guardrail metric: generated campaign accuracy/trust does not regress

## Evidence Labels
- Known: target segment named by user
- Assumed: affiliators feel friction in campaign creation/tracking
- Unknown: willingness to pay, must-have workflow, distribution channel

## Risks
- Building dashboard before validating core value → mitigation: experiment with landing page + sample campaign kits first

## Recommendation
Verdict: EXPERIMENT_FIRST
Rationale: value is plausible but core demand and willingness-to-pay are unverified
Next gate: experiment design before PRD/MVP build
```

## Common Pitfalls

1. **Decorative value.** “Looks better” is not enough. Tie UI work to clarity, credibility, conversion, accessibility, or reduced friction.
2. **Metric theater.** Do not invent vanity metrics. Use metrics that could change a decision.
3. **Business-only framing.** Value must include user value; business value without user value is extraction, not product value.
4. **Skipping uncertainty.** If important claims are unknown, say so and recommend discovery/experiment before build.
5. **Overbuilding on weak evidence.** Low-confidence value should narrow scope or move to experiment, not full implementation.
6. **No guardrail.** Every positive metric needs a “must not regress” counterpart.

## Verification Checklist

- [ ] User value is explicit and tied to a real user/customer.
- [ ] Business value type is named.
- [ ] Leading, lagging, and guardrail metrics are present.
- [ ] Claims are labeled as known, assumed, or unknown.
- [ ] Risks and mitigations are listed.
- [ ] Verdict is one of `CONTINUE`, `NARROW_SCOPE`, `EXPERIMENT_FIRST`, or `STOP`.
- [ ] Next gate is explicit.
