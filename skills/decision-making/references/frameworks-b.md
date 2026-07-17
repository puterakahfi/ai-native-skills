# Decision Making — Frameworks B

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
