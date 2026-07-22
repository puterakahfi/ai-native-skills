---
name: product-manager
description: Product management skill — write PRDs, define acceptance criteria, break down tasks, set scope, and prioritize. Ensures every feature has testable criteria and explicit scope before implementation starts.
license: MIT
metadata:
  ai-native-skills.version: 1.2.0
  ai-native-skills.author: puterakahfi
  ai-native-skills.type: skill
  ai-native-skills.implements: ai-native-core/contracts/skills/product/product-manager.contract.yaml
  ai-native-skills.contract-version: "~0.1"
  ai-native-skills.related_skills: '["delivery-work-breakdown","decision-provenance","product-development-workflow","new-feature-workflow"]'
---

# Product Manager

## Reviewed core contract interface

Source: `ai-native-core/contracts/skills/product/product-manager.contract.yaml` · compatible line: `~0.1`

```yaml
required_inputs:
- product_intent_or_feature_request
allowed_outputs:
- product_intent_document
- prd
- feature_spec
- acceptance_criteria
- task_breakdown
- priority_list
- out_of_scope_list
quality_gates:
- acceptance_criteria_must_be_testable_not_vague
- scope_in_and_scope_out_must_both_be_explicit
- tasks_must_trace_to_acceptance_criteria
- no_implementation_detail_in_prd_without_engineering_review
- priority_must_be_explicit_not_implicit
- prd_must_define_success_metric
```

Start from an attributable product_intent_or_feature_request. Produce the appropriate product intent, PRD or feature spec, testable acceptance criteria, task breakdown, explicit priority list, and out-of-scope list. Every task traces to acceptance criteria. Multi-slice work and unresolved repository targets hand off to `delivery-work-breakdown`; task breakdown alone does not choose an epic or PR target. Implementation detail requires engineering review rather than being smuggled into product definition.

Keep this interface synchronized with the pinned core contract. Exact declarations make ownership reviewable; they do not replace user evidence, product approval, experiment results, decision provenance, engineering review, or business outcome proof.

## The Core Rule

```text
No implementation starts without:
1. Explicit acceptance criteria (testable, not vague)
2. Explicit scope — what's IN and what's OUT
3. A success metric
```

## When to Use

- Writing a PRD or feature spec
- Breaking down a feature into tasks
- Defining acceptance criteria for a ticket
- Prioritizing one item or comparing competing initiatives
- Reviewing scope creep
- Onboarding a new feature to a sprint

---

## 1. Product Intent

Start with why before what:

```yaml
product_intent:
  title: ""
  problem: ""           # what user problem does this solve?
  user_segment: ""      # who experiences this problem?
  business_value: ""    # why does this matter to the business?
  success_metric: ""    # how do we know it worked?
  non_goals: []         # explicitly what this does NOT solve
```

**Gate:** Success metric must be measurable, not "improve UX."

---

## 2. Feature Spec / PRD

```yaml
feature_spec:
  title: ""
  intent_ref: ""        # links back to product intent
  scope_in: []           # explicit list of what's included
  scope_out: []          # explicit list of what's excluded
  acceptance_criteria:
    - id: AC-1
      given: ""         # context/precondition
      when: ""          # action
      then: ""          # expected outcome
  technical_notes: ""   # high-level only — no implementation detail without engineering review
  open_questions: []
  dependencies: []
```

**Gate:** Every acceptance criterion must follow Given/When/Then or equivalent testable format.

**Anti-pattern:** "The feature should work correctly" is NOT an acceptance criterion.

---

## 3. Task Breakdown

Each task must trace to an acceptance criterion:

```yaml
task:
  id: ""
  title: ""
  work_item_type: task | spike | bug
  parent_ref: ""
  traces_to: [AC-1, AC-2]   # must reference AC
  type: feat | fix | chore | spike
  estimate: ""              # product_defined unit (SP, hours, etc)
  dependencies: []
  definition_of_done: []
```

**Gate:** No task without AC reference. No floating tasks.

---

## Delivery topology handoff

`product-manager` owns intent, scope, acceptance criteria, priority, and task intent. When dependent slices or branch targets are unresolved, pass the verified scope and criteria to `delivery-work-breakdown`. It returns release unit, parent hierarchy, dependency graph, base branches, PR targets, integration plan, and epic acceptance plan. `git-workflow` then executes that approved topology.

## 4. Prioritization

Choose the smallest mode that can support the decision.

### Mode A — Simple priority labeling

Use this only when the work is already understood and no material trade-off remains unresolved.

```yaml
priority_matrix:
  - id: ""
    priority: P1 | P2 | P3
    reason: ""              # why this priority
    sprint: ""              # target sprint
```

**P1** — Must have, blocks success metric or a verified mandatory condition  
**P2** — Should have, materially improves a success metric  
**P3** — Nice to have, no direct or time-sensitive metric impact

List position is never priority evidence.

### Mode B — Comparative prioritization

Use this when choosing between two or more initiatives, sequencing competing work, or resolving value-versus-risk and value-versus-dependency trade-offs.

```text
name the decision and alternatives
→ resolve product success metrics, constraints, and authority
→ separate mandatory gates from scored trade-offs
→ compare evidence, assumptions, unknowns, confidence, and deferral impact
→ produce a recommendation and sensitivity notes
→ route the final decision to product authority
```

Load [`references/comparative-prioritization.md`](references/comparative-prioritization.md) for the full procedure and matrices.

#### Mandatory gates come before scoring

Do not dilute a verified mandatory condition into an average score. Examples include:

- active security or trust exposure;
- legal, regulatory, or contractual obligation;
- operational instability or data-loss risk;
- prerequisite work blocking multiple accepted outcomes;
- an explicit product or release policy gate.

A mandatory gate must be attributable and scoped. A vague fear, unsupported risk claim, or generic "security is important" statement is not enough to manufacture a blocker.

#### Product-defined comparison criteria

The product owns the criteria, weights, thresholds, and final authority. Reusable default lenses may include:

```text
user value
business value
strategic alignment
urgency and cost of delay
risk exposure and risk reduction
dependency and prerequisite effect
evidence strength and confidence
implementation effort and opportunity cost
reversibility and learning value
consequences of deferral
```

These lenses support reasoning; they are not a universal formula. Numeric scores must identify their method and weights and must not be presented as objective truth.

#### Evidence discipline

For every material criterion, record one of:

```text
attributable evidence
explicit assumption
explicit unknown
```

Do not fabricate conversion lift, user demand, security severity, implementation effort, deadline, or business impact. Low-confidence recommendations remain low-confidence and route to the smallest useful evidence-gathering step.

#### Comparative output

```yaml
priority_decision:
  decision_scope: ""
  alternatives:
    - id: ""
      value:
        user: ""
        business: ""
        strategic_alignment: ""
      urgency:
        cost_of_delay: ""
        deadline_or_trigger: ""
      risk:
        current_exposure: ""
        risk_reduction: ""
      dependencies:
        blocks: []
        blocked_by: []
      delivery:
        effort: ""
        opportunity_cost: ""
        reversibility: ""
      evidence: []
      assumptions: []
      unknowns: []
      confidence: low | medium | high
  mandatory_gates: []
  comparison_method: product_defined
  recommendation: ""
  rationale: []
  consequences_of_deferral: []
  sensitivity: []
  evidence_next_step: ""
  decision_authority: product_defined
  verdict: RECOMMEND | NEEDS_EVIDENCE | BLOCKED
```

#### Verdict semantics

- `RECOMMEND` — evidence is sufficient for a bounded recommendation; approval remains separate.
- `NEEDS_EVIDENCE` — a material comparison depends on unresolved evidence, assumptions, or sensitivity.
- `BLOCKED` — the decision scope, alternatives, mandatory gate, authority, or product constraint is too unclear to make a responsible recommendation.

#### Comparative quality gates

```text
priority is explicit, not inferred from order
mandatory gates are separated from weighted trade-offs
material claims identify evidence, assumption, or unknown
scores identify product-defined method and weights
effort alone does not determine priority
business value does not erase verified material risk
dependencies and consequences of deferral remain explicit
low confidence does not become fabricated certainty
recommendation remains distinct from product approval
prioritization does not choose repository topology or execute implementation
```

After priority and scope are accepted, hand multi-slice delivery planning to `delivery-work-breakdown`. Use `decision-provenance` when decision authority, supersession, approval, or governing policy is material.

---

## 5. Scope Review

Before finalizing spec, run scope check:

- [ ] Every item in `scope_in` has at least one AC?
- [ ] `scope_out` explicitly names things that could be assumed in?
- [ ] No implementation detail snuck into PRD without engineering review?
- [ ] No AC that says "should work correctly" or "be easy to use"?
- [ ] Success metric is measurable?
- [ ] Priority is explicit and supported by the selected mode?
- [ ] Comparative recommendations separate evidence, assumptions, unknowns, and authority?

---

## Output Templates

### Minimal Feature Spec

```markdown
## Feature: <title>

**Problem:** <what user problem>
**Success metric:** <measurable outcome>

**In scope:**
- item 1
- item 2

**Out of scope:**
- item A
- item B

**Acceptance criteria:**
- AC-1: Given <context>, when <action>, then <outcome>
- AC-2: Given <context>, when <action>, then <outcome>
```

### Task Breakdown

```markdown
## Tasks

- [ ] TASK-1: <title> [traces: AC-1] [P1]
- [ ] TASK-2: <title> [traces: AC-2] [P1]
- [ ] TASK-3: <title> [traces: AC-1, AC-2] [P2]
```

---

## Common Anti-Patterns

| Anti-Pattern | Why It Fails |
|---|---|
| "Make it user-friendly" as AC | Not testable — fails gate |
| Spec with no scope_out | Scope creep guaranteed |
| Tasks with no AC reference | No traceability — fails gate |
| Task list silently targets the default branch | Route repository topology to `delivery-work-breakdown` |
| Success metric: "users are happy" | Not measurable |
| Implementation detail in PRD without engineering review | Bypasses engineering contract |
| Priority order implicit in list position | Must be explicit P1/P2/P3 or comparative recommendation |
| Universal scoring formula presented as truth | Criteria and weights are product-defined |
| Security or legal blocker averaged into a weighted score | Mandatory gates precede scored trade-offs |
| High-value claim with no evidence | Return `NEEDS_EVIDENCE` or mark the assumption |
| Lowest-effort item automatically wins | Ignores value, dependencies, risk, and cost of delay |
| Skill recommendation presented as approval | Product authority owns the final decision |
