---
name: decision-making
description: Engineering decision-making frameworks — reversibility classification, pre-mortem, OODA loop, options thinking, epistemic humility, and decision traceability. For making better decisions faster, and knowing when to delay.
license: MIT
metadata:
  ai-native-skills.version: 1.0.0
  ai-native-skills.author: puterakahfi
  ai-native-skills.type: skill
  ai-native-skills.implements: ai-native-core/contracts/skills/engineering/decision-making.contract.yaml
  ai-native-skills.related_skills: '[''systems-thinking'', ''adr'', ''ethics-responsible-ai'', ''risk-modeling'']'
---

# Decision Making Skill

## Core Principle

```
Two skills: making good decisions AND knowing when NOT to decide.

The meta-question before any decision:
  "Is this reversible or irreversible?"

Reversible (two-way door):
  → Decide fast, with less information
  → You can course-correct
  → Don't over-analyze

Irreversible (one-way door):
  → Slow down, gather more information
  → Involve more stakeholders
  → Write the decision down (ADR)

Most engineering decisions are reversible.
Most teams treat them as irreversible → slow, over-engineered.
```

---

## Reversibility Classification

```
REVERSIBLE (decide fast — Type 2):
  - Tech stack for a new side feature
  - Variable names, function structure
  - UI copy
  - API endpoint naming (internal)
  - Which library to use for a utility function
  - Color scheme, font choices

IRREVERSIBLE (decide carefully — Type 1):
  - Database schema (columns are easy, removing is hard)
  - Public API contracts (breaking changes affect clients)
  - Authentication architecture
  - Multi-tenancy model
  - Domain boundaries in DDD (expensive to change)
  - Licensing and data privacy architecture

PARTIALLY REVERSIBLE (decide with an exit strategy):
  - Third-party SaaS integration (can migrate, but costly)
  - Infrastructure provider (lock-in risk)
  - ORM choice (schema migration if switching)

Rule: for reversible decisions, the cost of deciding now
      is almost always lower than the cost of delay.
      For irreversible: delay is sometimes the right answer.
```

---

## Pre-Mortem

```
Use when: about to make an important, partially-reversible decision.

Process:
  1. State the decision you're about to make
  2. Imagine it's 6 months later. The decision failed. Badly.
  3. Write down every reason why it failed.
     No filtering — list all plausible failure modes.
  4. For each failure mode: probability × impact = risk score
  5. Mitigate the top 3 risk items before committing
  6. If you can't mitigate them: reconsider the decision.

Example:
  Decision: move to microservices architecture
  
  Failure modes:
    - Team too small to own 8 services independently     [high × high]
    - Network latency kills checkout performance         [medium × high]
    - No distributed tracing → debugging nightmare       [high × medium]
    - Inter-service contracts drift, breaking changes    [medium × high]
  
  Mitigations:
    - Define team size threshold before splitting         ← implement
    - Performance budget: checkout < 200ms E2E           ← implement
    - Add Jaeger/Zipkin before splitting first service    ← implement
    - Versioned API contracts with contract testing       ← implement
  
  If none of these can be implemented first → delay the decision.
```

---

## OODA Loop (for fast-moving decisions)

```
Observe → Orient → Decide → Act → (repeat)

OBSERVE: what is actually happening? (data, not interpretation)
  - Production metrics, error rates, user feedback
  - Never: "I think users are frustrated"
  - Always: "Bounce rate on checkout increased 12% this week"

ORIENT: what does it mean? (context + mental models)
  - What changed this week? (deployment, marketing campaign?)
  - What do we know about this area?
  - What assumptions might be wrong?

DECIDE: what will we do? (specific, time-bounded)
  - Not: "we should investigate"
  - Yes: "Alex will check deploy logs by EOD, report by 6pm"

ACT: execute the decision
  - Do it now — OODA only works if the loop is tight
  - Waiting for perfect information = losing to whoever acts first

Loop speed: for incidents, OODA should complete in minutes.
            For architecture, hours to days.
```

---

## Options Thinking

```
Before committing to a path, ask: "What options am I preserving or closing?"

Real options in engineering:
  
  OPTION 1: Wait and see (preserve optionality)
    Buy time before committing to a direction.
    Valuable when: situation is changing rapidly, more information incoming.
    Cost: delay, potential opportunity cost.
    
  OPTION 2: Experiment (cheap validation)
    Build a spike, prototype, or A/B test.
    Valuable when: high uncertainty, reversible enough to try.
    Cost: spike time.
    
  OPTION 3: Modular bet (hedge)
    Design so the decision can be changed later without full rewrite.
    Valuable when: likely to need to change, but not sure when.
    Cost: slightly more complex architecture (ports/adapters pattern).
    
  OPTION 4: Commit (close options)
    Pick a path, optimize for it, stop hedging.
    Valuable when: direction is clear, hedging costs more than it saves.
    Cost: migration cost if wrong.

Rule: preserve options until the cost of preserving them
      exceeds the cost of committing. Then commit fully.
```

---

## Epistemic Humility

```
Know what you don't know.

Types of uncertainty:
  KNOWN UNKNOWNS: "We don't know how users will react to this."
    → Design experiments to find out

  UNKNOWN UNKNOWNS: things we don't know we don't know
    → Use pre-mortems, diverse reviewers, red teams to surface them
    → Ask: "What would have to be true for this to fail badly?"

  FALSE CERTAINTY: we think we know, but we don't
    → Most dangerous type
    → Check: "What is the evidence for this belief?"
    → Check: "When did we last validate this assumption?"

Humility practices:
  □ Explicitly state confidence level with every major claim
     "I'm 80% confident this will scale to 10k users"
  □ Track prediction accuracy — did what you said would happen, happen?
  □ Read opposing views before committing to a technical direction
  □ Ask: "What would change my mind?" — if nothing: red flag.
```

---

## Decision Traceability

```
For irreversible and partially-reversible decisions: write it down.

Minimum decision record:
  What was decided: [specific, unambiguous statement]
  Why: [the reasoning — not just the conclusion]
  What was rejected: [alternatives considered and why not chosen]
  What we assumed: [what needs to be true for this to be correct]
  How we'll know if wrong: [validation criteria]

Full format: use ADR skill (adr/SKILL.md)

Decision review cadence:
  Revisit major decisions every 6 months.
  Ask: "If we were making this decision today, would we make the same one?"
  If no: evaluate the cost of changing vs continuing.
```

---

## Decision Making Gates (Scored 0–10, Min 8)

```
Gate DM1: Reversibility Check
  □ Irreversible decisions documented as ADR?
  □ Reversible decisions made quickly, not over-engineered?
  Score: __ / 10

Gate DM2: Pre-Mortem Quality
  □ Top failure modes identified for high-stakes decisions?
  □ Mitigations implemented before committing?
  Score: __ / 10

Gate DM3: Option Preservation
  □ Options explicitly listed before committing?
  □ Architecture allows reversal where feasible?
  Score: __ / 10

Gate DM4: Epistemic Honesty
  □ Assumptions documented and ranked by risk?
  □ Confidence levels stated for key claims?
  □ Validation criteria defined?
  Score: __ / 10

OVERALL: __ / 10   MINIMUM: 8.0
```
