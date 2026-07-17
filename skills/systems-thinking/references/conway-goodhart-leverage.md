# Conway's Law, Goodhart's Law, Leverage Points, and Checklists

## Conway's Law

```
"Organizations which design systems are constrained to produce designs
which are copies of the communication structures of those organizations."
— Melvin Conway, 1967

Implications:
  - Microservices owned by separate teams → loose coupling by Conway's Law
  - Shared database owned by no team → spaghetti integrations
  - Frontend and backend in one team → BFF pattern naturally emerges
  - Monorepo with one team → coupling follows team structure

Inverse Conway Maneuver:
  Design the org structure you want first, then let the architecture follow.
  If you want microservices → first create independent teams with clear ownership.
  Architecture reform without org reform fails every time.

Diagnostic question:
  "Does our current team structure produce the architecture we want?"
  If no → the architecture will drift back to match the team structure.
```

---

## Goodhart's Law

```
"When a measure becomes a target, it ceases to be a good measure."
— Charles Goodhart

Engineering examples:

  Metric: Test coverage percentage
  Perverse behavior: Trivial tests written to inflate percentage
  Coverage % goes up, code quality stays the same or gets worse

  Metric: Velocity (story points per sprint)
  Perverse behavior: Point inflation, stories split to game estimates
  Velocity goes up, delivery quality goes down

  Metric: Time-to-first-response on incidents
  Perverse behavior: "Acknowledged" replies with no action
  Response time goes down, resolution time unchanged

Before adopting any metric:
  □ What behavior does this metric incentivize?
  □ How would a rational actor game this metric?
  □ What important thing is this metric NOT capturing?
  □ What is the counter-metric that prevents gaming?
```

---

## Unintended Consequences Analysis

```
Three sources of unintended consequences:
  1. Complexity — the system is too complex to fully predict
  2. Perverse incentives — the intervention creates wrong incentives
  3. Feedback delays — the loop is there but the effect is delayed

Framework — for any proposed change, explicitly ask:
  □ Who might be harmed by this that we haven't considered?
  □ What existing equilibria does this disrupt?
  □ What incentives does this create that we didn't intend?
  □ What happens if this is adopted at scale by everyone?
  □ What is the failure mode if this goes wrong?
  □ What feedback loops does this create or break?

Example — "Let's add gamification to our productivity tool"

  Intended: more engagement, more retention

  Unintended consequences to analyze:
  → Creates anxiety in users who fall behind (harm to wellbeing)
  → Gaming behavior — users optimize for points, not productivity
  → Power users dominate leaderboards, discourage new users
  → At scale, everyone games → metric loses meaning (Goodhart)
  → Users resent surveillance feeling of being tracked
```

---

## Leverage Points

```
Donella Meadows' leverage points — places to intervene in a system,
ordered from least to most effective:

Low leverage (easy to change, small effect):
  12. Numbers — change a constant (price, tax rate)
  11. Buffers — change stock size (warehouse capacity)
  10. Stock-flow structure — physical infrastructure

Medium leverage:
   9. Delay lengths — speed of feedback loops
   8. Balancing feedback strength — how hard system self-corrects
   7. Reinforcing feedback strength — how fast growth loops amplify
   6. Information flows — who has access to what information

High leverage (hard to change, large effect):
   5. Rules — incentives, constraints, enforcement
   4. Self-organization — ability of system to change its own structure
   3. Goals — purpose of the system
   2. Paradigm — shared assumptions, beliefs, values
   1. Transcending paradigms — ability to question the paradigm itself

Engineering implication:
  Most teams intervene at 12-10 (change a number, add a buffer).
  Persistent problems often require 6-4 (change information flows, rules, goals).
  "We've tried everything" → try a higher leverage point.
```

---

## The "Whether" Question

```
All other skills answer: "How do we build this well?"
Systems thinking also asks: "Should we build this at all?"

Checklist before any significant feature or system:

  □ What system-level change does this create, beyond its stated purpose?
  □ What feedback loops does this introduce or amplify?
  □ Who benefits? Who bears the risk? Are they the same people?
  □ What second-order effects are we not considering?
  □ Does our team structure allow us to maintain this?  (Conway's Law)
  □ What metric will we use to measure success, and how might it be gamed?  (Goodhart)
  □ What unintended harm might emerge at scale?
  □ Is the problem we're solving better solved at a higher leverage point?
  □ Would we still build this if we had to explain all its effects to those harmed?
```

---

## Systems Thinking Checklist

For any architectural or product decision:
- [ ] Feedback loops identified (reinforcing and balancing)?
- [ ] Second-order effects analyzed (2-3 levels deep)?
- [ ] Conway's Law applied — does team structure support intended architecture?
- [ ] Goodhart's Law risk assessed for any new metrics introduced?
- [ ] Unintended consequences explicitly considered?
- [ ] Leverage point identified — are we solving at the right level?
- [ ] "Whether" question asked before "how" question?
- [ ] Who bears risk vs who benefits — are they the same?
