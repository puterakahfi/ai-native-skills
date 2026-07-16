---
name: technical-debt-governance
description: Technical debt governance — debt inventory, classification, interest calculation, paydown strategy, coupling metrics, and Boy Scout Rule enforcement. For teams that want to track and reduce debt systematically, not just complain about it.
version: 1.0.0
author: puterakahfi
license: MIT
type: skill
implements: ai-native-core/contracts/skills/engineering/technical-debt-governance.contract.yaml
related_skills: [refactoring, systems-thinking, observability-design, adr]
---

# Technical Debt Governance Skill

## Core Principle

```
Debt is not inherently bad — untracked debt is.

Good debt: deliberate shortcut to ship, with a clear paydown plan.
Bad debt: accidental complexity that compounds silently.

The test:
  Can you explain the debt to a new engineer in 2 sentences?
  Do you know what it costs per sprint to keep it?
  Is there a written plan to pay it down?

If no to any: the debt is unmanaged. Govern it now.
```

---

## Debt Classification

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

## Debt Inventory

Maintain a debt register. Minimum fields:

```markdown
## Debt Register

| ID | Type | Description | Severity | Interest (pts/sprint) | Owner | Target Sprint |
|----|------|-------------|----------|-----------------------|-------|---------------|
| D-001 | Design | Payment and notifications coupled in same service | P1 | 3 | @putera | Sprint 12 |
| D-002 | Test | No integration tests for checkout flow | P1 | 5 | @team | Sprint 11 |
| D-003 | Dependency | Node 16 (EOL), need Node 20 | P2 | 1 | @infra | Sprint 14 |
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

---

## Paydown Strategy

### The 20% Rule

```
Allocate 20% of each sprint's capacity to debt paydown.
  10-sprint team velocity: 50 points
  Debt budget: 10 points/sprint

If Debt Tax > 20%: escalate to engineering leadership.
If Debt Tax > 40%: stop new features, emergency debt sprint.
```

### Prioritization

```
Priority score = Interest (pts/sprint) × Blast Radius / Effort to fix

Highest score = fix first.

Example:
  D-001: interest=3, blast=4 engineers, effort=5pts
         score = 3 × 4 / 5 = 2.4

  D-002: interest=5, blast=2 engineers, effort=3pts
         score = 5 × 2 / 3 = 3.3  ← fix D-002 first

Fix the highest ROI debt, not the most annoying one.
```

### Boy Scout Rule

```
Every time you touch a file:
  1. Leave it cleaner than you found it
  2. Fix one small debt item in the area you're already working
  3. Document any debt you find but can't fix now (add to register)

Scope: do NOT Boy Scout the whole codebase.
  Only the module you're already working on.
  Unbounded cleanup = never-ending PR, lost focus.

Time box: max 20% of your PR time on Boy Scout cleanup.
```

---

## Coupling Metrics

```
High coupling = one of the most expensive forms of design debt.

Measures:
  Afferent Coupling (Ca): how many modules depend on this module?
    High Ca = this module is hard to change without breaking others
    
  Efferent Coupling (Ce): how many modules does this module depend on?
    High Ce = this module is fragile, breaks when dependencies change

  Instability (I) = Ce / (Ca + Ce)
    I = 0: stable (nothing depends on others, everything depends on it)
    I = 1: unstable (everything depends on others, nothing depends on it)

  Abstractness (A) = abstract classes / total classes
    
  Distance from Main Sequence (D) = |A + I - 1|
    D = 0: balanced (abstract+stable OR concrete+unstable)
    D > 0.5: problematic — either abstract+unstable OR concrete+stable

Tools:
  PHP: phpmetrics, deptrac
  JS/TS: dependency-cruiser, madge
  Python: pydeps
  Java: JDepend, ArchUnit
```

---

## Debt Governance Ceremony

```
Cadence: once per sprint (15 min)

Agenda:
  1. Review Debt Tax (current sprint vs last sprint) — 5 min
  2. New debt identified this sprint — add to register — 5 min
  3. Confirm next sprint's debt paydown items — 5 min

Output:
  - Updated debt register
  - Debt Tax trend chart
  - Items committed for next sprint paydown
```

---

## Technical Debt Gates (Scored 0–10, Min 8)

```
Gate TD1: Debt Visibility
  □ Debt register exists and is current?
  □ Debt Tax calculated this sprint?
  Score: __ / 10

Gate TD2: Prioritization
  □ P0 debt addressed within current sprint?
  □ P1 debt has target sprint assigned?
  Score: __ / 10

Gate TD3: Paydown Budget
  □ ≥ 20% of sprint capacity allocated to debt?
  □ Boy Scout Rule applied to all PRs?
  Score: __ / 10

Gate TD4: Coupling Control
  □ No new modules with I < 0.3 that aren't intentionally stable?
  □ Circular dependencies: zero?
  Score: __ / 10

OVERALL: __ / 10   MINIMUM: 8.0
```
