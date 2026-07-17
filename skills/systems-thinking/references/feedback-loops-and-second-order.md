# Feedback Loops and Second-Order Effects

## Feedback Loops

Every system has feedback loops. Identify them before intervening.

### Reinforcing Loops (amplify change)

```
Reinforcing loop — grows in one direction until limited

Example: Recommendation algorithm
  More users → more data → better recommendations
  → more engagement → more users → ...

  Positive: virtuous cycle, network effects
  Negative: can amplify harm (radicalization spiral, filter bubble)

Draw it:
  [Users] → (+) → [Data] → (+) → [Recommendation Quality]
          ↑                                    |
          +←←←←←←←←(+)←←←←←←←←←←←←←←←←←←←←←+

Question: What limits this loop? If nothing, it grows until catastrophe.
```

### Balancing Loops (resist change, seek equilibrium)

```
Balancing loop — maintains stability

Example: Auto-scaling
  High CPU → scale up → CPU decreases → scale trigger resets

Draw it:
  [CPU Load] → (+) → [Scale Up Event] → (+) → [Capacity]
       ↑                                            |
       +←←←←←←←←(-)←←←←←←←←←←←←←←←←←←←←←←←←←←←+

Question: What disrupts this balance? What if scaling has a lag?
  → Lag in balancing loop creates oscillation (thrashing)
  → Solution: cooldown periods, predictive scaling
```

---

## Second-Order Effects

First-order: direct, obvious consequence.
Second-order: consequence of the consequence.

```
Decision: Add rate limiting to API

First-order effect:
  → Fewer API abuse incidents ✓

Second-order effects (often missed):
  → Legitimate high-volume users hit limits, churn
  → Developers work around limits with polling — increases load
  → Rate limit errors become a new attack vector (DOS via rate exhaustion)
  → Third-party integrations break silently, damaging partner relationships

Analysis process:
  For each intended effect → ask "and then what?"
  Do this 2-3 levels deep.
  The most important effects are often 2nd or 3rd order.
```
