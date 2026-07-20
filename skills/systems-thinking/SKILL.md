---
name: systems-thinking
description: Analyze systems as wholes — feedback loops, emergence, second-order effects, Conway's Law, Goodhart's Law, unintended consequences, and leverage points. The "whether" question before the "how" question.
license: MIT
metadata:
  ai-native-skills.version: 1.0.1
  ai-native-skills.author: puterakahfi
  ai-native-skills.type: skill
  ai-native-skills.implements: ai-native-core/contracts/skills/architecture/systems-thinking.contract.yaml
  ai-native-skills.contract-version: "~0.1"
  ai-native-skills.related_skills: '["adr", "architecture-review", "ethics-responsible-ai", "product-manager", "master-engineer"]'
---

# Systems Thinking

## Reviewed core contract interface

Source: `ai-native-core/contracts/skills/architecture/systems-thinking.contract.yaml` · compatible line: `~0.1`

```yaml
required_inputs:
- system_or_decision_description
allowed_outputs:
- feedback_loop_map
- emergence_analysis
- second_order_effects
- conways_law_analysis
- unintended_consequences_report
- leverage_points
quality_gates:
- feedback_loops_must_be_identified_reinforcing_and_balancing
- second_order_effects_must_be_analyzed_not_just_first
- conways_law_must_be_applied_to_team_and_architecture_alignment
- unintended_consequences_must_be_explicitly_considered
- goodharts_law_risk_must_be_assessed_for_any_new_metric
- leverage_points_must_be_identified_before_intervention
- emergence_must_be_considered_for_complex_systems
- whether_question_must_precede_how_question
```

Analyze reinforcing and balancing loops, second-order effects, Conway alignment, Goodhart risk for new metrics, emergence, leverage points, and unintended consequences before recommending intervention.

Keep this interface synchronized with the pinned core contract. Exact declarations make ownership reviewable; they do not replace runtime, repository, architecture, test, or product evidence.


> **HARD RULES**
> - **Identify feedback loops before proposing solutions** — every intervention creates or modifies a loop
> - **Delays cause oscillation — name them explicitly** — a balancing loop with a lag thrashes; find the lag first
> - **Local optimization often causes global degradation** — optimize the whole system, not the part

## The Core Rule

```
All skills teach HOW to build something.
Systems thinking asks WHETHER and WHAT ELSE.

"What else will change when we change this?"
"Who else is affected that we haven't considered?"
"What feedback loops will our decision create?"
"What are the second-order effects?"

The most dangerous architectural decisions are the ones
where everyone agreed and nobody asked these questions.
```

---

## References

| Topic | File |
|---|---|
| Feedback Loops (Reinforcing + Balancing), Second-Order Effects | [references/feedback-loops-and-second-order.md](references/feedback-loops-and-second-order.md) |
| Conway's Law, Goodhart's Law, Unintended Consequences, Leverage Points, The "Whether" Question, Systems Thinking Checklist | [references/conway-goodhart-leverage.md](references/conway-goodhart-leverage.md) |

---

## Quick Decision Guide

```
Proposing an architectural change?          → Identify feedback loops first — see feedback-loops-and-second-order.md
New metric being introduced?               → Goodhart's Law check — see conway-goodhart-leverage.md
Team structure doesn't match architecture? → Conway's Law / Inverse Conway — see conway-goodhart-leverage.md
Side effects of a feature not clear?       → Second-order effects analysis — see feedback-loops-and-second-order.md
Solution feels like it's not sticking?     → Leverage points — see conway-goodhart-leverage.md
Should we build this at all?               → The "Whether" checklist — see conway-goodhart-leverage.md
```
