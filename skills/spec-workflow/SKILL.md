---
name: spec-workflow
description: 'Spec-driven development workflow — constitution → specify → plan → tasks → implement. Eliminates vibe coding at the input layer: no implementation without a precise, agent-executable spec.'
license: MIT
metadata:
  ai-native-skills.version: 1.0.0
  ai-native-skills.author: puterakahfi
  ai-native-skills.type: workflow
  ai-native-skills.implements: ai-native-core/contracts/workflows/spec-driven.contract.yaml
  ai-native-skills.contract-version: "~0.1"
  ai-native-skills.skill_load_order: '[{''phase'': ''constitution'', ''load'': [''native-ai-engineer'', ''master-engineer'']}, {''phase'': ''specify'', ''load'': [''product-manager'']}, {''phase'': ''plan'', ''load'': [''plan'']}, {''phase'': ''tasks'', ''load'': [''context-manager'', ''rule-manager'']}, {''phase'': ''implement'', ''load'': [''master-engineer'', ''test-driven-development'']}]'
  ai-native-skills.skills: '{''required'': [''product-manager'', ''plan'', ''context-manager'', ''rule-manager'', ''master-engineer'', ''native-ai-engineer''], ''optional'': [''test-driven-development'', ''spike'', ''diagram-architect'']}'
---

# Spec-Driven Development Workflow

## The Core Rule

```
Vague prompts → vibe code → unmaintainable systems.
Precise specs → agent-executable tasks → production-grade output.

No implementation starts without a spec.
No spec is valid without testable acceptance criteria.
```

## When to Use

- Starting any new feature (replace "let me just try this in Claude")
- Onboarding an agent to a non-trivial task
- When a previous attempt produced bloated or wrong output
- When multiple agents or team members will work on the same feature
- Any task where scope ambiguity exists

---

## Phase 1: Constitution
**Gate:** Constitution must exist before spec.

Load `native-ai-engineer` + `master-engineer`.

Define the non-negotiables for this product/repo:

```yaml
constitution:
  architecture_style: ""       # hexagonal, layered, microservices, etc
  stack: []                    # from engineering-contract
  principles:
    - ""                       # e.g. "domain logic must not depend on framework"
    - ""                       # e.g. "no direct DB access outside repositories"
  non_negotiables:
    - ""                       # e.g. "all endpoints require auth"
    - ""                       # e.g. "no raw SQL"
  out_of_bounds:
    - ""                       # e.g. "do not introduce new dependencies without ADR"
```

**If constitution already exists** → load it, verify it's current, skip to Phase 2.

**Done when:** Constitution document exists and reflects current engineering contract.

---

## Phase 2: Specify
**Gate:** Spec must have testable acceptance criteria.

Load `product-manager`.

Write the feature specification:

```yaml
spec:
  title: ""
  problem: ""
  user_segment: ""
  success_metric: ""         # measurable, not "improve UX"

  scope_in: []
  scope_out: []              # explicit — name things that could be assumed in

  acceptance_criteria:
    - id: AC-1
      given: ""
      when: ""
      then: ""

  technical_constraints: []  # from constitution
  open_questions: []
```

**Gate checks:**
- [ ] Every AC follows Given/When/Then?
- [ ] `scope_out` explicit — not empty?
- [ ] Success metric is measurable?
- [ ] No implementation detail without engineering review?

**Done when:** Spec reviewed, all ACs testable, scope explicit.

---

## Phase 3: Plan
**Gate:** Every task must trace to an acceptance criterion.

Load `plan`.

Break spec into ordered tasks:

```markdown
## Plan: <feature-title>

### Tasks
- [ ] TASK-1: <title> [AC-1] [P1]
  - file: src/path/to/file.ts
  - approach: <1-sentence>
- [ ] TASK-2: <title> [AC-1, AC-2] [P1]
  - file: src/path/to/other.ts
- [ ] TASK-3: <title> [AC-2] [P2]
```

**Rules:**
- Each task references exact file paths
- Each task traces to at least one AC
- Tasks are independently verifiable
- No "refactor everything" tasks — scope to what the spec needs

**Done when:** Plan saved to `.hermes/plans/<feature>.md`, all tasks have AC refs.

---

## Phase 4: Tasks
**Gate:** Tasks must have context pack before agent handoff.

Load `context-manager` + `rule-manager`.

For each task handed to an agent, build context pack:

```markdown
## Context Pack — TASK-1

**Spec ref:** <feature-title> AC-1
**File scope:** src/path/to/file.ts
**Stack:** <from constitution>
**Rules:** AGENTS.md loaded
**Constraints:** <from constitution>
**Skills to load:** [master-engineer, test-driven-development]

**Acceptance criterion:**
- AC-1: Given..., When..., Then...

**Out of scope:**
- Everything not in AC-1
```

**Done when:** Context pack complete for each task. Agent knows exactly what to do and what not to do.

---

## Phase 5: Implement
**Gate:** Implementation must not exceed spec scope.

Load `master-engineer` + `test-driven-development`.

Execute tasks in order. For each task:

1. Load context pack
2. Write test first (if TDD applies)
3. Implement to make test pass
4. Verify against AC — does it satisfy Given/When/Then?
5. Check scope — any drift beyond spec?

**Scope drift check:**
- [ ] Files modified are only those in task plan?
- [ ] No new dependencies introduced without ADR?
- [ ] No refactoring outside task scope?
- [ ] AC satisfied — not just "works", but provably satisfies the criterion?

**Done when:** All tasks complete, all ACs satisfied, no scope drift.

---

## Quick Reference

| Phase | Load Skill | Gate |
|---|---|---|
| **1. Constitution** | `native-ai-engineer`, `master-engineer` | Constitution exists |
| **2. Specify** | `product-manager` | Testable ACs, explicit scope |
| **3. Plan** | `plan` | All tasks trace to AC |
| **4. Tasks** | `context-manager`, `rule-manager` | Context pack complete |
| **5. Implement** | `master-engineer`, `test-driven-development` | No scope drift |

---

## vs new-feature-workflow

```
new-feature-workflow  → team process (phases: design → implement → submit → review)
spec-workflow         → input quality (phases: constitution → specify → plan → tasks → implement)
```

These compose: run `spec-workflow` first to produce a valid spec, then execute via `new-feature-workflow`.
