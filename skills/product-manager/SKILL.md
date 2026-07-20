---
name: product-manager
description: Product management skill — write PRDs, define acceptance criteria, break down tasks, set scope, and prioritize. Ensures every feature has testable criteria and explicit scope before implementation starts.
license: MIT
metadata:
  ai-native-skills.version: 1.0.1
  ai-native-skills.author: puterakahfi
  ai-native-skills.type: skill
  ai-native-skills.implements: ai-native-core/contracts/skills/product/product-manager.contract.yaml
  ai-native-skills.contract-version: "~0.1"
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

Start from an attributable product_intent_or_feature_request. Produce the appropriate product intent, PRD or feature spec, testable acceptance criteria, task breakdown, explicit priority list, and out-of-scope list. Every task traces to acceptance criteria; implementation detail requires engineering review rather than being smuggled into product definition.

Keep this interface synchronized with the pinned core contract. Exact declarations make ownership reviewable; they do not replace user evidence, product approval, experiment results, decision provenance, engineering review, or business outcome proof.


## The Core Rule

```
No implementation starts without:
1. Explicit acceptance criteria (testable, not vague)
2. Explicit scope — what's IN and what's OUT
3. A success metric
```

## When to Use

- Writing a PRD or feature spec
- Breaking down a feature into tasks
- Defining acceptance criteria for a ticket
- Prioritizing a backlog
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
  scope_in: []          # explicit list of what's included
  scope_out: []         # explicit list of what's excluded
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
  traces_to: [AC-1, AC-2]   # must reference AC
  type: feat | fix | chore | spike
  estimate: ""              # product_defined unit (SP, hours, etc)
  dependencies: []
  definition_of_done: []
```

**Gate:** No task without AC reference. No floating tasks.

---

## 4. Prioritization

Use explicit priority, not implicit ordering:

```yaml
priority_matrix:
  - id: ""
    priority: P1 | P2 | P3
    reason: ""              # why this priority
    sprint: ""              # target sprint
```

**P1** — Must have, blocks success metric
**P2** — Should have, improves success metric
**P3** — Nice to have, no direct metric impact

---

## 5. Scope Review

Before finalizing spec, run scope check:

- [ ] Every item in `scope_in` has at least one AC?
- [ ] `scope_out` explicitly names things that could be assumed in?
- [ ] No implementation detail snuck into PRD without engineering review?
- [ ] No AC that says "should work correctly" or "be easy to use"?
- [ ] Success metric is measurable?

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
| Success metric: "users are happy" | Not measurable |
| Implementation detail in PRD without engineering review | Bypasses engineering contract |
| Priority order implicit in list position | Must be explicit P1/P2/P3 |
