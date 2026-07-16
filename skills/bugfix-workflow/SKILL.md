---
name: bugfix-workflow
description: Guided bugfix workflow — reproduce, investigate, fix, verify, submit, review. Phases and gates are invariant; branch strategy, issue tracker, and approval policy are product-defined.
version: 1.1.0
author: puterakahfi
license: MIT
type: workflow
implements: ai-native-core/contracts/workflows/bugfix.contract.yaml
skills:
  required:
    - systematic-debugging
    - architecture-review
  optional:
    - master-engineer
skill_load_order:
  - phase: investigate
    load: [systematic-debugging]
  - phase: fix
    load: [systematic-debugging]
  - phase: review
    load: [architecture-review]
---

# Bugfix Workflow

## Overview

A structured bugfix workflow that enforces the right sequence and gates. The phases are invariant across teams — what varies (branch strategy, issue tracker, approval policy) is declared by the product adapter.

## Required Skills

Load these skills before executing the workflow:

| Phase | Load Skill |
|---|---|
| Phase 2: Investigate | `systematic-debugging` |
| Phase 3: Fix | `systematic-debugging` |
| Phase 6: Review | `architecture-review` |

> Agent instruction: when entering each phase, load the listed skill and follow its process before proceeding.

## Required Skill

Load `systematic-debugging` before executing Phase 2.

## Phases

---

### Phase 1: Reproduce
**Gate:** Red loop must exist before any fix.

1. Read the bug report / issue completely
2. Build a tight, deterministic feedback loop — one command that goes red on the exact symptom
3. Confirm the loop is reproducible before moving on

```bash
# Example: failing test
pytest tests/test_module.py::test_name -v

# Example: curl repro
curl -X POST http://localhost:8000/endpoint -d '{"payload": "..."}' | jq
```

**Done when:** You can trigger the bug on demand with one command.

---

### Phase 2: Investigate
**Gate:** Root cause must be stated before fix.

Load and follow `systematic-debugging` skill — complete all 4 phases through root cause identification.

**Done when:** You can state in one sentence: *"The root cause is X because Y."*

---

### Phase 3: Fix
**Gate:** One change at a time. No bundled unrelated changes.

1. Write a regression test that reproduces the bug (RED)
2. Implement the single fix targeting root cause
3. Confirm the regression test passes (GREEN)

**Done when:** Regression test green, root cause addressed, no unrelated changes.

---

### Phase 4: Verify
**Gate:** Verification evidence required before submission.

Run the full test suite — method is product-defined (local, CI, or both).

```bash
# Example: local
pytest tests/ -q

# Example: trigger CI
git push origin <branch>
```

Capture evidence: test output, CI link, or screenshot.

**Done when:** Full suite green, evidence captured.

---

### Phase 5: Submit
**Gate:** Submission must reference issue tracker item.

Submit code for review — mechanism is product-defined (PR, MR, patch).

Checklist:
- [ ] References issue tracker item (ticket ID, issue URL, etc)
- [ ] Description includes: what broke, root cause, fix summary
- [ ] Regression test included
- [ ] Verification evidence attached

**Done when:** Submission open, issue tracker item referenced.

---

### Phase 6: Review
**Gate:** Approval required before merge.

- [ ] Peer review completed
- [ ] Feedback addressed
- [ ] Approved by required reviewers
- [ ] Merged

---

## Quick Reference

| Phase | Gate | Done When |
|---|---|---|
| **1. Reproduce** | Red loop exists | Can trigger bug on demand |
| **2. Investigate** | Root cause stated | One-sentence root cause |
| **3. Fix** | One change, regression test | Test green, root cause addressed |
| **4. Verify** | Full suite evidence | Suite green, evidence captured |
| **5. Submit** | References issue | Submission open + issue linked |
| **6. Review** | Approved | Merged |

## Common Pitfalls

1. **Skipping Phase 1** — fixing without a repro means you can't confirm the fix works
2. **Skipping Phase 2** — symptom fix without root cause → bug comes back
3. **Bundling changes** — makes review hard and breaks bisect
4. **No regression test** — fix regresses silently in future
5. **Submitting before verify** — CI catches what local misses, and vice versa
