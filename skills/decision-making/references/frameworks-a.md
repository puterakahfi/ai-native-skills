# Decision Making — Frameworks A

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
