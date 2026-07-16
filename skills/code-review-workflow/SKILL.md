---
name: code-review-workflow
description: Structured code review workflow — load contracts, architecture check, design check, logic check, verdict. Enforces engineering contract and design system compliance before any merge.
license: MIT
metadata:
  ai-native-skills.version: 1.0.0
  ai-native-skills.author: puterakahfi
  ai-native-skills.type: workflow
  ai-native-skills.implements: ai-native-core/contracts/workflows/code-review.contract.yaml
  ai-native-skills.skill_load_order: '[{''phase'': ''architecture-check'', ''load'': [''architecture-review'']}, {''phase'': ''design-check'', ''load'': [''design-review'']}, {''phase'': ''logic-check'', ''load'': [''systematic-debugging'', ''master-engineer'']}]'
  ai-native-skills.skills: '{''required'': [''architecture-review''], ''optional'': [''design-review'', ''systematic-debugging'', ''master-engineer'']}'
---

# Code Review Workflow

## The Core Rule

```
Every code submission must be checked against the Engineering Contract.
Compiled ≠ Approved. Generated ≠ Approved.
```

## When to Use

- Before merging any PR, MR, or patch
- After AI agent generates code
- When reviewing a colleague's implementation
- When a new dependency or architecture decision is introduced

## Prerequisites

Before starting, have ready:
1. Product `engineering-contract.yaml`
2. Product `product-ui-design-system-contract.yaml` (if UI changes present)
3. The code diff / PR

---

## Phase 1: Load Context
**Gate:** Contracts loaded before review starts.

```bash
# confirm engineering contract location
cat products/<product>/engineering-contract.yaml

# confirm design contract (if UI involved)
cat products/<product>/ui-design-system-contract.yaml
```

If contracts don't exist → **block review** and request contract creation first.

**Done when:** Engineering contract loaded. Design contract loaded if UI changes present.

---

## Phase 2: Architecture-Check
**Gate:** Engineering contract compliance verified.

Load `architecture-review` skill and run full checklist:

- [ ] Stack compliance — no unauthorized framework/library
- [ ] Layer boundary — no cross-layer violations
- [ ] Dependency audit — no unapproved new dependencies
- [ ] Folder structure — no arbitrary new structure
- [ ] Test strategy — tests present per contract requirement
- [ ] ADR required? — flag if contract change detected
- [ ] Security baseline — no hardcoded secrets

**Done when:** Architecture verdict produced (PASS / FAIL / PASS WITH FLAGS).

---

## Phase 3: Design-Check *(if UI changes present)*
**Gate:** Design system contract compliance verified.

Load `design-review` skill and run full checklist:

- [ ] Visual direction — matches declared style
- [ ] AI slop detection — no generic template patterns
- [ ] Token compliance — no hardcoded colors/spacing
- [ ] Component reuse — no one-off duplicates
- [ ] Layout patterns — follows declared patterns
- [ ] Status rules — badge colors follow contract
- [ ] Responsive — follows declared breakpoints
- [ ] Accessibility — contrast, focus, semantic headings

**Done when:** Design verdict produced (PASS / FAIL / PASS WITH FLAGS).

---

## Phase 4: Logic-Check *(if complex business logic)*
**Gate:** Logic and test coverage verified.

Load `master-engineer` for complex architecture decisions.
Load `systematic-debugging` if a bug fix — verify root cause was actually fixed.

- [ ] Business logic correct per spec/ticket
- [ ] Edge cases handled
- [ ] Error handling present
- [ ] Regression test included (for bugfix)
- [ ] No silent failures

**Done when:** Logic verdict produced.

---

## Phase 5: Verdict
**Gate:** Verdict must cite specific violations, not vague feedback.

Produce structured verdict:

```
CODE REVIEW VERDICT
───────────────────
PR/MR: <link>
Reviewer: <name>
Date: <date>

OVERALL: APPROVED | REQUEST CHANGES | BLOCKED

Architecture: PASS | FAIL | PASS WITH FLAGS
Design:       PASS | FAIL | PASS WITH FLAGS | N/A
Logic:        PASS | FAIL | N/A

Violations (BLOCKING):
  - [ARCH] <specific violation with file:line>
  - [DESIGN] <specific violation>

Flags (NON-BLOCKING):
  - [ARCH] <flag with recommendation>

ADR Required: YES | NO
  → Reason: <if yes>

Approved to merge: YES | NO
```

**Done when:** Verdict delivered to submitter with specific, actionable feedback.

---

## Quick Reference

| Phase | Load Skill | Gate |
|---|---|---|
| **1. Load Context** | — | Contracts loaded |
| **2. Architecture** | `architecture-review` | Contract compliance verified |
| **3. Design** | `design-review` | Design system compliance verified |
| **4. Logic** | `master-engineer`, `systematic-debugging` | Logic and tests verified |
| **5. Verdict** | — | Specific violations cited |

## Anti-Patterns — Auto-Fail Review

| Pattern | Why |
|---|---|
| "Looks good to me" without contract check | Engineering contract not consulted |
| Approve because CI is green | CI ≠ architecture compliance |
| Approve AI-generated code without review | Generated ≠ Approved |
| Vague feedback: "this could be better" | Verdict must be specific and actionable |
| Skip design check on UI PR | Design system contract applies |
