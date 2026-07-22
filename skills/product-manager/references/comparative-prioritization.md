# Comparative Prioritization

Use this reference when `product-manager` must compare competing initiatives rather than merely label already-understood work as P1, P2, or P3.

The method produces a recommendation. It does not create product approval, repository authority, implementation proof, or business outcome evidence.

## 1. Define the decision boundary

Record:

```yaml
decision_context:
  decision_scope: ""
  alternatives: []
  product_intent_ref: ""
  success_metrics: []
  constraints: []
  governing_policy_refs: []
  decision_authority: product_defined
  decision_deadline: ""
```

Rules:

- Compare named alternatives, not vague themes.
- Keep alternatives at a comparable decision level.
- State whether the decision is selection, sequencing, funding, experiment choice, or deferral.
- Unknown authority or policy remains unknown; tool access and repository permission do not fill the gap.

## 2. Establish attributable facts

For each alternative, separate:

```yaml
assessment_basis:
  evidence: []
  assumptions: []
  unknowns: []
  source_refs: []
  confidence: low | medium | high
```

Examples of evidence include accepted product requirements, production incidents, customer research, analytics, security findings, contractual deadlines, dependency maps, estimates with an identified owner, and validated experiments.

Do not invent:

- conversion improvement;
- user demand;
- incident probability;
- security severity;
- implementation effort;
- revenue effect;
- legal obligation;
- deadlines.

An estimate remains an estimate. A stakeholder preference remains a preference. A verified incident remains evidence within its observed scope.

## 3. Detect mandatory gates

Evaluate before weighted or scored comparison:

```yaml
mandatory_gate:
  id: ""
  type: security | legal | contractual | operational | prerequisite | product_policy | other
  statement: ""
  applies_to: []
  evidence_refs: []
  scope: ""
  consequence: ""
  authority_ref: ""
  status: VERIFIED | UNVERIFIED | NOT_APPLICABLE
```

A verified mandatory gate can determine sequencing even when another initiative has greater potential upside.

Examples:

- an active shared credential exposes member access;
- an accepted regulatory deadline is approaching;
- a data-integrity defect risks irreversible loss;
- one platform capability blocks several already-accepted features;
- product policy forbids release before a named control exists.

Do not turn a generic concern into a blocker. If the gate is unverified, record the evidence needed and return `NEEDS_EVIDENCE` when it is decision-critical.

## 4. Select product-defined criteria

The product owns criteria, weights, thresholds, and interpretation. Choose only criteria material to the decision.

| Criterion | Question |
|---|---|
| User value | Which user problem is reduced, and for whom? |
| Business value | Which accepted business outcome or metric is affected? |
| Strategic alignment | Which current product direction does this advance? |
| Urgency / cost of delay | What worsens, expires, or becomes more expensive if deferred? |
| Risk exposure | What verified harm or uncertainty exists now? |
| Risk reduction | How directly does the initiative reduce that exposure? |
| Dependencies | What does this block, unblock, or require first? |
| Evidence strength | How trustworthy and complete is the assessment basis? |
| Effort | What delivery capacity is required, according to an attributable estimate? |
| Opportunity cost | What cannot be done while this is selected? |
| Reversibility | How safely can the decision be changed later? |
| Learning value | What material uncertainty can be reduced? |
| Deferral consequence | What happens if this waits one cycle? |

A product may use RICE, WSJF, cost-of-delay, risk-first sequencing, a custom matrix, or no numeric model. Record the selected method rather than silently mixing frameworks.

## 5. Compare without false precision

Recommended qualitative matrix:

```yaml
comparison:
  method: product_defined
  criteria:
    - id: ""
      weight: "product_defined | not_weighted"
      rationale: ""
  alternatives:
    - id: ""
      assessments:
        - criterion_id: ""
          rating: low | medium | high | unknown
          rationale: ""
          evidence_refs: []
          assumption_refs: []
      confidence: low | medium | high
```

When numeric scoring is used:

- show the formula and weights;
- keep mandatory gates outside the average;
- identify unknown inputs;
- do not manufacture decimal precision;
- test whether reasonable weight changes reverse the result.

A score is a decision aid, not a fact or approval.

## 6. Analyze dependencies and deferral

For each alternative, answer:

```yaml
dependency_and_deferral:
  blocks: []
  blocked_by: []
  sequencing_constraints: []
  consequence_if_deferred: []
  opportunity_cost_if_selected: []
  reversible: true | false | partial | unknown
```

Distinguish:

```text
high value
≠ must be first

low effort
≠ highest priority

prerequisite
≠ most valuable by itself

urgent
≠ important without evidence
```

## 7. Run sensitivity analysis

Sensitivity asks whether the recommendation survives reasonable uncertainty.

Check at least:

- Does removing one weak assumption reverse the ranking?
- Do product-defined weights materially change the result?
- Does a disputed mandatory gate decide the sequence?
- Would a smaller reversible experiment resolve the disagreement?
- Is the recommendation robust enough to act on, or only directional?

Record:

```yaml
sensitivity:
  stable_under_reasonable_changes: true | false | unknown
  reversal_conditions: []
  disputed_inputs: []
  evidence_next_step: ""
```

When reasonable product weights reverse the result, preserve that fact. Do not claim one universal ranking.

## 8. Produce a bounded recommendation

```yaml
priority_decision:
  decision_scope: ""
  alternatives: []
  mandatory_gates: []
  comparison_method: product_defined
  recommendation: ""
  rationale: []
  consequences_of_deferral: []
  sensitivity: []
  assumptions: []
  unknowns: []
  confidence: low | medium | high
  evidence_next_step: ""
  decision_authority: product_defined
  verdict: RECOMMEND | NEEDS_EVIDENCE | BLOCKED
```

Use:

- `RECOMMEND` when evidence supports a scoped recommendation.
- `NEEDS_EVIDENCE` when a material unknown can change the decision.
- `BLOCKED` when scope, alternatives, governing policy, mandatory gate, or authority is too unclear.

The recommendation should explain both:

1. why the selected initiative should proceed first; and
2. what is accepted by deferring the alternatives.

## 9. Choose the smallest evidence step

When evidence is insufficient, do not default to broad research. Select the smallest action that can change the decision, such as:

- inspect the actual authentication implementation;
- verify whether shared credentials remain active;
- retrieve conversion baseline data;
- obtain a bounded engineering estimate;
- validate a dependency through a technical spike;
- run a reversible landing-page experiment;
- confirm policy or authority with the named owner.

The evidence step is not implementation authorization.

## 10. Handoffs

```text
accepted product priority and scope
→ delivery-work-breakdown for release-unit and repository topology
→ implementation-context-discovery for repository evidence
→ implementation workflow
```

Use `decision-provenance` when approval, authority, policy, supersession, or competing decisions are material.

## Anti-patterns

| Anti-pattern | Correct response |
|---|---|
| Highest imagined revenue wins | Require attributable value evidence and check gates |
| Security always wins without scope | Verify exposure, severity, and applicability |
| Every concern becomes a weighted score | Separate mandatory gates from trade-offs |
| Lowest effort wins | Include value, risk, dependencies, and deferral |
| Numerical result presented as objective truth | Show product-defined method, weights, and sensitivity |
| Unknown input silently assigned an average value | Mark unknown and test decision sensitivity |
| Recommendation reported as approved roadmap | Route to product authority |
| Prioritization chooses branch targets | Hand accepted scope to `delivery-work-breakdown` |
