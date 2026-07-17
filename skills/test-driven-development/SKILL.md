---
name: test-driven-development
description: 'TDD: enforce RED-GREEN-REFACTOR cycle — tests written before implementation, every time.'
license: MIT
metadata:
  ai-native-skills.version: 1.1.0
  ai-native-skills.author: puterakahfi
  ai-native-skills.type: skill
  ai-native-skills.implements: ai-native-core/contracts/skills/engineering/test-driven-development.contract.yaml
  ai-native-skills.contract-version: "~0.1"
---

# Test-Driven Development (TDD)

## Overview

Write the test first. Watch it fail. Write minimal code to pass.

**Core principle:** If you didn't watch the test fail, you don't know if it tests the right thing.

**Violating the letter of the rules is violating the spirit of the rules.**

## When to Use

**Always:**
- New features
- Bug fixes
- Refactoring
- Behavior changes

**Exceptions (ask the user first):**
- Throwaway prototypes
- Generated code
- Configuration files

Thinking "skip TDD just this once"? Stop. That's rationalization.

---

## ⚠️ THE IRON LAW (HARD RULES — TOP)

```
NO PRODUCTION CODE WITHOUT A FAILING TEST FIRST
```

- **Tests BEFORE code — no exceptions**
- **Watch the test FAIL before writing implementation**
- **Never write implementation to make a passing test pass faster**
- **RED → GREEN → REFACTOR — never skip or reorder**

Write code before the test? Delete it. Start over.

**No exceptions:**
- Don't keep it as "reference"
- Don't "adapt" it while writing tests
- Don't look at it
- Delete means delete

Implement fresh from tests. Period.

---

## Red-Green-Refactor Cycle

For the full RGR cycle detail, load:

```
references/rgr-cycle.md
```

**Summary:**

| Phase | Action | Mandatory |
|-------|--------|-----------|
| RED | Write one minimal failing test | ✅ |
| Verify RED | Run test, confirm failure | ✅ NEVER SKIP |
| GREEN | Write simplest code to pass | ✅ |
| Verify GREEN | Run test + full suite | ✅ NEVER SKIP |
| REFACTOR | Clean up, keep tests green | ✅ |
| Repeat | Next behavior, next cycle | ✅ |

## Patterns & Pitfalls

For anti-patterns, rationalizations, and red flags, load:

```
references/patterns-pitfalls.md
```

Key rules:
- Use **vertical tracer bullets** (one behavior per cycle), not horizontal slices
- Common rationalizations: "too simple", "after is same", "manual tested" — all invalid
- Red flags: code before test, test passes immediately, "just this once"

## Verification Checklist & Integration

For the completion checklist, Hermes Agent integration, and anti-patterns, load:

```
references/integration.md
```

---

## ⚠️ THE IRON LAW (HARD RULES — BOTTOM)

```
NO PRODUCTION CODE WITHOUT A FAILING TEST FIRST
```

- **Tests BEFORE code — no exceptions**
- **Watch the test FAIL before writing implementation**
- **Never write implementation to make a passing test pass faster**
- **RED → GREEN → REFACTOR — never skip or reorder**

**All red flags mean: Delete code. Start over with TDD.**

```
Production code → test exists and failed first
Otherwise → not TDD
```

No exceptions without the user's explicit permission.
