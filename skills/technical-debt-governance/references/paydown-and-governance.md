# Technical Debt: Paydown Strategy, Governance & Gates

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

> **HARD RULE: Never pay debt without tests.** Write or verify test coverage before refactoring.

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
