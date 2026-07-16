---
name: systematic-debugging
description: 4-phase root cause debugging — investigate, analyze, hypothesize, fix. Enforces finding root cause before attempting any fix.
version: 1.0.0
author: puterakahfi
license: MIT
type: skill
implements: ai-native-core/contracts/skills/quality-control/systematic-debugging.contract.yaml
---

# Systematic Debugging

## Overview

Random fixes waste time and create new bugs. Quick patches mask underlying issues.

**Core principle:** ALWAYS find root cause before attempting fixes. Symptom fixes are failure.

## The Iron Law

```
NO FIXES WITHOUT ROOT CAUSE INVESTIGATION FIRST
```

If you haven't completed Phase 1, you cannot propose fixes.

## The Feedback Loop Rule

Before reading code to build a theory, create or identify a **tight** command that can go red on the user's exact symptom and green when the bug is fixed. A tight loop is fast, deterministic, agent-runnable, and specific enough to catch this bug.

When a clean repro is hard, spend disproportionate effort building the loop. Guessing without a red-capable loop is the failure mode this skill exists to prevent.

## When to Use

Use for ANY technical issue:
- Test failures
- Bugs in production
- Unexpected behavior
- Performance problems
- Build failures
- Integration issues

**Especially when:**
- Under time pressure (emergencies make guessing tempting)
- "Just one quick fix" seems obvious
- You've already tried multiple fixes and they're not working

## The Four Phases

You MUST complete each phase before proceeding to the next.

---

## Phase 1: Root Cause Investigation

**BEFORE attempting ANY fix:**

### 1. Read Error Messages Carefully
- Don't skip past errors or warnings — they often contain the exact solution
- Read stack traces completely, note line numbers, file paths, error codes

### 2. Build a Tight Feedback Loop

Can you trigger the user's exact symptom with one command? Try in order:

1. **Failing test** at the seam that reaches the bug
2. **HTTP script / curl** against a running dev server
3. **CLI invocation** with fixture input, diffing stdout/stderr against expected
4. **Headless browser script** asserting on DOM, console, or network
5. **Replay a captured trace**: HAR, request payload, event log
6. **Throwaway harness** that boots the smallest useful slice of the system
7. **Bisection harness** suitable for `git bisect run`

**Tighten the loop:**
- Make it faster: cache setup, narrow scope
- Make the signal sharper: assert the exact symptom
- Make it more deterministic: pin time, seed randomness, isolate filesystem

### 3. Check Recent Changes
```bash
git log --oneline -10
git diff
git log -p --follow src/problematic_file.py | head -100
```

### 4. Gather Evidence in Multi-Component Systems
For each component boundary: log what enters, log what exits, verify config propagation. Run once to gather evidence showing WHERE it breaks, THEN investigate that specific component.

### 5. Trace Data Flow
Where does the bad value originate? Keep tracing upstream until you find the source. Fix at the source, not at the symptom.

### Phase 1 Completion Checklist
- [ ] Error messages fully read and understood
- [ ] Tight loop exists and has been run — it is red-capable
- [ ] Loop is deterministic (or flaky bug has high enough reproduction rate)
- [ ] Recent changes identified and reviewed
- [ ] Root cause hypotheses can be stated

**STOP:** Do not proceed to Phase 2 until you understand WHY it's happening.

---

## Phase 2: Pattern Analysis

### 1. Minimize the Reproduction
Shrink the repro to the smallest scenario that still goes red. Cut inputs, callers, config, data, steps — one at a time. Keep only what is load-bearing for the failure.

### 2. Find Working Examples
Locate similar working code in the same codebase. What works that's similar to what's broken?

### 3. Compare Against References
If implementing a pattern, read the reference implementation completely — don't skim.

### 4. Identify Differences
List every difference between working and broken, however small. Don't assume "that can't matter."

---

## Phase 3: Hypothesis and Testing

### 1. Form Ranked Falsifiable Hypotheses
Generate 3–5 plausible hypotheses before testing any. Rank by likelihood and cheapness to falsify. State the prediction each makes: "If X is the cause, then Y should happen."

### 2. Test Minimally
Test the highest-ranked hypothesis with the smallest possible probe. Change one variable at a time. Prefer debugger/REPL inspection — one breakpoint beats ten logs.

### 3. Verify Before Continuing
- Did it work? → Phase 4
- Didn't work? → Form NEW hypothesis
- DON'T add more fixes on top

---

## Phase 4: Implementation

### 1. Create Failing Test Case
Simplest possible reproduction. Automated test if possible. MUST exist before fixing.

### 2. Implement Single Fix
Address the root cause identified. ONE change at a time. No "while I'm here" improvements.

### 3. Verify Fix
```bash
# Run the specific regression test
pytest tests/test_module.py::test_regression -v

# Run full suite — no regressions
pytest tests/ -q
```

### 4. Rule of Three
If ≥ 3 fixes have failed: **STOP and question the architecture.**

Each fix revealing new coupling in a different place = wrong architecture, not a missing fix.

---

## Red Flags — STOP and Return to Phase 1

- "Quick fix for now, investigate later"
- "Just try changing X and see if it works"
- "It's probably X, let me fix that"
- Proposing solutions before tracing data flow
- "One more fix attempt" after 2+ failures

## Quick Reference

| Phase | Key Activities | Gate |
|---|---|---|
| **1. Root Cause** | Read errors, reproduce, check changes, trace data flow | Understand WHAT and WHY |
| **2. Pattern** | Find working examples, compare, identify differences | Know what's different |
| **3. Hypothesis** | Form ranked theories, test minimally, one variable | Confirmed root cause |
| **4. Implementation** | Regression test first, fix root cause, verify full suite | All tests pass |
