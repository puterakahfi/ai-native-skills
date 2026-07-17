# Technical Debt: Classification & Inventory

## Debt Classification

### By Origin (classify FIRST)

```
DELIBERATE debt: knowingly incurred — "we'll fix this after launch"
  Must have: written note in register + paydown target sprint
  Risk: compound interest if not tracked

RECKLESS debt: incurred without realising it was a shortcut
  "We didn't have time to do it right"
  Must have: retrospective note + immediate triage

INADVERTENT debt: discovered later — good design at the time, now wrong
  Technology moved, requirements changed, team learned
  Must have: register entry + priority score
```

### By Type

```
1. DESIGN DEBT
   Wrong abstraction, wrong boundaries, premature coupling.
   Symptom: changing one thing breaks unrelated things.
   Cost: slows feature velocity over time (compounding).

2. CODE DEBT
   Duplicated logic, unclear naming, missing tests.
   Symptom: fear of touching a module.
   Cost: each bug takes 2x longer to find + fix.

3. TEST DEBT
   Missing tests, flaky tests, tests that don't test behavior.
   Symptom: releases feel risky, regressions keep appearing.
   Cost: manual QA time + escaped bugs in production.

4. DEPENDENCY DEBT
   Outdated packages, deprecated APIs, pinned versions.
   Symptom: security advisories pile up, upgrades become projects.
   Cost: migration effort grows non-linearly with delay.

5. INFRASTRUCTURE DEBT
   Manual processes, config drift, undocumented infrastructure.
   Symptom: "it works on my machine", deployment anxiety.
   Cost: incidents, slow onboarding.

6. DOCUMENTATION DEBT
   Missing ADRs, outdated READMEs, no onboarding guide.
   Symptom: knowledge silos, new engineers take months to ramp.
   Cost: onboarding time + repeated questions to same people.
```

### By Severity

```
CRITICAL (P0): blocks delivery or causes production risk
  Fix within: current sprint
  Example: no test coverage on payment flow, outdated auth library with CVE

HIGH (P1): significantly slows velocity
  Fix within: next 2 sprints
  Example: 3 duplicate implementations of same business rule

MEDIUM (P2): slows velocity measurably
  Fix within: next quarter
  Example: missing integration tests on core API

LOW (P3): quality issue, not velocity issue
  Fix within: when touching the area
  Example: inconsistent naming conventions in a non-critical module
```

---

## Debt Inventory — Register Format

> **HARD RULE: debt register must be visible to the product team.**

```markdown
## Debt Register

| ID | Type | Origin | Description | Severity | Interest (pts/sprint) | Owner | Target Sprint |
|----|------|--------|-------------|----------|-----------------------|-------|---------------|
| D-001 | Design | Deliberate | Payment and notifications coupled in same service | P1 | 3 | @putera | Sprint 12 |
| D-002 | Test | Reckless | No integration tests for checkout flow | P1 | 5 | @team | Sprint 11 |
| D-003 | Dependency | Inadvertent | Node 16 (EOL), need Node 20 | P2 | 1 | @infra | Sprint 14 |
```

**Interest (pts/sprint):** estimated story points lost each sprint due to this debt.  
Aggregate all interest to get **Debt Tax**: points lost per sprint to existing debt.

---

## Debt Interest Calculation

```
For each debt item, estimate:

  DIRECT COST:
    Extra time to work around this debt each sprint
    Extra bug fixing caused by this debt
    Example: "Working around the coupled service costs ~2h/sprint per engineer"
    2h × 2 engineers = 4h → ~1 story point/sprint

  COMPOUNDING FACTOR:
    Is this debt getting worse over time?
    Design debt: yes (more code builds on wrong abstraction)
    Test debt: yes (more untested code added)
    Dependency debt: yes (more code uses deprecated API)
    → Multiply interest by 1.5x for compounding debt

  BLAST RADIUS:
    How many engineers does this debt slow?
    1 engineer: 1x
    Full team: 4x

Total interest = (direct cost × compounding factor × blast radius)

Debt Tax = SUM(interest for all active debts)

Report Debt Tax each sprint:
  "This sprint, 8 story points lost to technical debt (↑ from 6 last sprint)"
```
