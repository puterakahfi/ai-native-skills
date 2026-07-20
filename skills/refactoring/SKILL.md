---
name: refactoring
description: Structured code refactoring without behavior change — name the smell, green tests first, small independent steps, one refactoring type per commit. Covers extract method/class, move, rename, decompose conditional, replace pattern.
license: MIT
metadata:
  ai-native-skills.version: 1.0.1
  ai-native-skills.author: puterakahfi
  ai-native-skills.type: skill
  ai-native-skills.implements: ai-native-core/contracts/skills/engineering/refactoring.contract.yaml
  ai-native-skills.contract-version: "~0.1"
---

# Refactoring

## Reviewed core contract interface

Source: `ai-native-core/contracts/skills/engineering/refactoring.contract.yaml` · compatible line: `~0.1`

```yaml
required_inputs:
- code_or_module
- refactoring_goal
allowed_outputs:
- refactored_code
- refactoring_plan
- test_suite_update
- complexity_delta
quality_gates:
- tests_must_be_green_before_refactoring_starts
- behavior_must_be_identical_before_and_after
- refactoring_steps_must_be_small_and_independently_verifiable
- no_feature_added_during_refactoring
- no_bug_fixed_during_refactoring
- test_coverage_must_not_decrease
- one_refactoring_type_per_commit
- code_smell_must_be_named_before_fix
```

Refactoring preserves behavior. Do not add a feature or fix a bug inside the refactoring change, keep tests green, prevent coverage regression, and report the plan, updated tests, and complexity delta.

Keep this interface synchronized with the pinned core contract. Exact declarations make ownership reviewable; they do not replace runtime, repository, architecture, test, or product evidence.


> **HARD RULES**
> - Tests must pass before AND after refactoring — never refactor a red suite
> - One change type per commit — extract method is one commit, rename is another
> - Never refactor and add features simultaneously — two separate hats

## Quick Reference

| Phase | What to Do | Reference |
|---|---|---|
| Smell identification & core process | Name the smell, run tests, apply Extract Method / Extract Class | [smells-and-core-refactorings.md](references/smells-and-core-refactorings.md) |
| Advanced patterns & checklist | Replace Conditional, Parameter Object, Value Object, final checklist | [advanced-patterns-and-checklist.md](references/advanced-patterns-and-checklist.md) |

## When to Use This Skill

- Code review surfaces a named smell (God Class, Long Method, Primitive Obsession)
- Pre-feature cleanup to make a safe landing zone
- Tech debt sprint — structured improvement without behavior change

## Decision Flow

```
Smell identified?
  └─ Tests green?
       ├─ NO  → Fix tests first. Do not refactor broken code.
       └─ YES → Name the refactoring → apply in small steps → commit per step

Adding a feature?
  └─ Refactor FIRST (separate commits), THEN add feature (separate commit)
     Never mix structural + behavioral change in one commit.
```

## Smell → Refactoring Map

| Smell | Signal | Refactoring |
|---|---|---|
| Long Method | > 20 lines, hard to name | Extract Method |
| God Class | > 300 lines, 10+ responsibilities | Extract Class |
| Primitive Obsession | string for email, int for money | Extract Value Object |
| Long Parameter List | 4+ parameters | Introduce Parameter Object |
| Conditional Complexity | nested if/else, switch on type | Replace Conditional with Polymorphism |
| Feature Envy | uses another class's data more | Move Method |
| Duplicate Code | same logic in 2+ places | Extract Method / Pull Up |
| Anemic Model | entity with only getters | Move logic into entity |

## Gates

- [ ] Smell named before touching code?
- [ ] Full test suite green before first edit?
- [ ] One refactoring type per commit?
- [ ] Commit message: `refactor(scope): description`?
- [ ] Tests still green after every step?
- [ ] No new features or bug fixes mixed in?

---

Load [smells-and-core-refactorings.md](references/smells-and-core-refactorings.md) for smell table, step-by-step process, Extract Method, and Extract Class examples.

Load [advanced-patterns-and-checklist.md](references/advanced-patterns-and-checklist.md) for Replace Conditional with Polymorphism, Parameter Object, Value Object, and final checklist.
