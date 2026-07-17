# Harm, Accountability & Checklist Reference

## Accountability Map

When AI causes harm — who is responsible?

```
AI accountability chain:

  Model developer      → responsible for training data, model behavior
  Platform operator    → responsible for how model is deployed and constrained
  Product team         → responsible for decisions about when to apply AI
  Individual engineer  → responsible for raising ethical concerns
  User                 → responsible for how they use AI outputs

High-stakes decisions require named accountability:
  "If our AI denies a loan incorrectly, @risk-team is responsible for human review"
  "If our AI generates harmful content, @safety-team is responsible for remediation"
```

---

## Harm Assessment

### Pre-launch Harm Assessment

```
For each AI feature, explicitly assess:

  Direct harms:
    - Can this AI output hurt someone physically? (medical, autonomous systems)
    - Can this AI decision destroy someone's livelihood? (hiring, credit, housing)
    - Can this AI content psychologically harm users? (depression, self-harm triggers)

  Indirect harms:
    - Does this AI create dependency that harms users when removed?
    - Does this AI homogenize information (filter bubble, radicalization)?
    - Does this AI extract value from users without fair exchange?

  Distributional harms:
    - Does this AI harm marginalized groups more than others?
    - Does this AI reinforce existing systemic inequalities?
    - Who bears the cost when this AI is wrong?

For each harm identified:
  → Severity: catastrophic / serious / moderate / minor
  → Probability: very likely / likely / unlikely / very unlikely
  → Mitigation: what reduces severity or probability?
  → Residual risk: what harm remains after mitigation?
  → Decision: proceed / proceed with monitoring / don't build
```

---

## Power Asymmetry

```
Power asymmetry exists when one party has significantly more
ability to set terms, exit, or appeal than the other.

AI amplifies power asymmetry when:
  - System users cannot opt out (government, employer, essential service)
  - System users cannot see how decisions are made
  - System users cannot appeal or have no meaningful appeal process
  - System benefits accumulate to operator, risks accumulate to users

Mitigation:
  - Make AI involvement visible
  - Provide explainability for high-stakes decisions
  - Build meaningful human review process
  - Give users data portability and deletion rights
  - Design for the least powerful user, not the average user
```

---

## Ethics Checklist

Before shipping any AI feature:
- [ ] Stakeholder impact map complete (beneficiaries, risk-bearers, excluded, powerless)?
- [ ] Sensitive attributes identified — does model use them directly or via proxy?
- [ ] Fairness metric chosen and documented with rationale?
- [ ] Fairness evaluated across demographic groups?
- [ ] AI involvement disclosed to users?
- [ ] High-stakes automated decisions have explanation + appeal path?
- [ ] Consent is informed, specific, and revocable?
- [ ] Data governance documented (collection → use → retention → deletion)?
- [ ] Accountability assigned for model errors and harms?
- [ ] Harm assessment completed — severity, probability, mitigation, residual risk?
- [ ] Power asymmetry acknowledged and mitigated?
- [ ] "Whether to build" question answered, not just "how to build"?
