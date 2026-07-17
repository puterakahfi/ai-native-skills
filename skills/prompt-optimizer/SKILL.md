---
name: prompt-optimizer
description: Transform vague intent into a precise, token-efficient prompt — explicit scope, constraints, output format, and stop condition. Eliminates agent guessing loops.
license: MIT
metadata:
  ai-native-skills.version: 1.0.0
  ai-native-skills.author: puterakahfi
  ai-native-skills.type: skill
  ai-native-skills.implements: ai-native-core/contracts/skills/context/prompt-optimizer.contract.yaml
  ai-native-skills.contract-version: "~0.1"
---

# Prompt Optimizer

## The Core Problem

```
Vague prompt → agent guesses → wrong output → user corrects → agent re-tries → token waste

Precise prompt → agent executes once → correct output → done
```

Every token spent on agent confusion is wasted. Every correction loop is a failed prompt.

## When to Use

- Before sending any non-trivial task to an agent
- When a previous attempt produced the wrong output
- When task involves multiple possible interpretations
- When output format matters (code, JSON, checklist, report)
- When scope boundaries are ambiguous
- Before delegating to a subagent

---

## Anatomy of a Precise Prompt

Every optimized prompt has 5 components:

```
1. TASK      — what to do (one verb, one object)
2. SCOPE     — what's IN and what's OUT
3. CONSTRAINT — what must NOT happen
4. OUTPUT    — exact format expected
5. STOP      — when to stop, not keep going
```

---

## Pattern Library

### Pattern 1: Single-Task Prompt

```
# Raw (vague):
"improve this function"

# Optimized:
Task: Refactor the `calculateDiscount()` function in src/pricing/discount.ts
Scope in: only this function
Scope out: do not touch callers, do not rename the function
Constraint: no new dependencies, preserve existing return type
Output: the refactored function only, no explanation
Stop: after one refactored version — do not offer alternatives
```

### Pattern 2: Review Prompt

```
# Raw (vague):
"review this code"

# Optimized:
Task: Review src/auth/SessionManager.php for security violations
Scope in: auth logic, session handling, token validation
Scope out: ignore style/formatting issues
Constraint: cite specific line numbers, cite specific rule violated
Output: structured list — [CRITICAL|MAJOR|MINOR] finding: line N — description — fix
Stop: after verdict APPROVED or REQUEST CHANGES — do not suggest unrelated improvements
Skills: architecture-review, security-review
```

### Pattern 3: Generation Prompt

```
# Raw (vague):
"write tests for this"

# Optimized:
Task: Write unit tests for UserService::transferBalance() in tests/unit/UserServiceTest.php
Scope in: happy path + 3 edge cases (negative amount, insufficient funds, same-account transfer)
Scope out: do not test private methods, do not add integration tests
Constraint: use existing PHPUnit setup, no new test helpers
Output: PHPUnit test class only, no explanation
Stop: after the 4 test cases — do not add more without asking
Skills: test-driven-development
```

### Pattern 4: Debug Prompt

```
# Raw (vague):
"fix this bug"

# Optimized:
Task: Diagnose why UserController::updateProfile() returns 500 on line 142
Scope in: the stack trace provided, UserController, UserService
Scope out: do not refactor unrelated code
Constraint: do not propose fix until root cause is confirmed
Output: phase 1 = root cause statement, phase 2 = minimal fix, phase 3 = regression test
Stop: after phase 3 — do not suggest architectural improvements
Skills: systematic-debugging
```

### Pattern 5: Analysis Prompt

```
# Raw (vague):
"what's wrong with this design?"

# Optimized:
Task: Audit the checkout flow UI (screens attached) for UX problems
Scope in: checkout steps 1-3, form interactions, error states
Scope out: ignore brand/visual polish, ignore mobile layout
Constraint: every finding must cite a specific principle (heuristic, law, or pattern)
Output: structured by lens — Product / Design / Psychology — then Synthesis with P1/P2/P3
Stop: after Synthesis — do not suggest implementation solutions
Skills: role-switcher → master-design, ux-psychology, product-manager
```

---

## Optimization Checklist

Before sending a prompt, check:

- [ ] **One task** — does the prompt ask for one thing or several?
  - Multiple tasks → split into separate prompts
- [ ] **Explicit scope** — is `scope_in` AND `scope_out` declared?
  - Missing `scope_out` → agent will drift
- [ ] **No ambiguous verbs** — "improve", "make better", "optimize", "clean up"?
  - Replace with: "refactor X to do Y", "reduce cyclomatic complexity in Z"
- [ ] **Output format** — does the agent know exactly what to produce?
  - Code only? Report? JSON? Checklist?
- [ ] **Stop condition** — does the agent know when to stop?
  - Without stop condition → agent keeps going, adds unrequested content
- [ ] **Constraints** — what must NOT happen?
  - "do not rename", "do not add dependencies", "do not refactor callers"
- [ ] **Skills declared** — which skills should be loaded?
  - Reduces context guessing, ensures right gates applied

---

## Token Cost Anti-Patterns

| Anti-Pattern | Cost | Fix |
|---|---|---|
| "improve this" | Agent asks 3 clarifying questions | State exact improvement target |
| No output format | Agent produces essay when you wanted code | Declare output format explicitly |
| No scope_out | Agent refactors 5 files instead of 1 | Explicitly name what's out of scope |
| No stop condition | Agent adds "bonus" suggestions after task | "Stop after X — do not add more" |
| Ambiguous target | Agent works on wrong file/function | Reference exact path:line |
| No skills declared | Agent uses general knowledge instead of skill gates | Declare `Skills:` in prompt |

---

## Prompt Template

Copy-paste and fill:

```
Task: <one verb + one specific object>
Scope in: <explicit list of what's included>
Scope out: <explicit list of what's excluded>
Constraint: <what must not happen>
Output: <exact format — code only / report / JSON / checklist>
Stop: <when to stop — after X, not before Y>
Skills: <skills to load — optional but recommended>
```

---

## Relationship to Other Skills

```
spec-workflow       → structures WHAT to build (feature spec level)
prompt-optimizer    → structures HOW to ask for it (prompt level)
context-manager     → attaches WHO/WHERE context (context pack level)

Order:
  spec-workflow (once per feature)
    → context-manager (once per task)
      → prompt-optimizer (per prompt sent to agent)
```
