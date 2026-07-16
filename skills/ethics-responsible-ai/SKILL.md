---
name: ethics-responsible-ai
description: Ethical analysis and responsible AI governance — fairness audit, harm assessment, transparency requirements, consent and data governance, accountability mapping, and power asymmetry analysis.
version: 1.0.0
author: puterakahfi
license: MIT
type: skill
implements: ai-native-core/contracts/skills/quality-control/ethics-responsible-ai.contract.yaml
related_skills: [ai-system-design, threat-modeling, accessibility, product-manager]
---

# Ethics & Responsible AI

## The Core Rule

```
Every engineering decision is a moral decision.

Choosing not to consider ethics is itself an ethical choice —
and it is one that harms the people who cannot opt out of your system.

The question is not "is this technically possible?" but
"should we build this, for whom, and with what consequences?"
```

---

## Stakeholder Impact Mapping

Before building: identify who is affected and how.

```
For each AI feature or system, map:

  Beneficiaries:  Who gains? (users, company, shareholders)
  Risk-bearers:   Who bears the risk? (often different from beneficiaries)
  Excluded:       Who is invisibilized or excluded?
  Powerless:      Who cannot opt out or appeal?

Example — AI-powered credit scoring:
  Beneficiaries:  Bank (efficiency), low-risk applicants (faster approval)
  Risk-bearers:   Applicants denied by opaque model
  Excluded:       People with thin credit files (young, recent immigrants)
  Powerless:      Denied applicants with no right to explanation or appeal

If risk-bearers ≠ beneficiaries → heightened scrutiny required.
```

---

## Fairness Audit

### Identify Sensitive Attributes

```python
# Attributes that should not drive decisions (or must be carefully justified):
sensitive_attributes = [
    "race", "ethnicity", "gender", "age", "religion",
    "disability", "sexual_orientation", "national_origin",
    "pregnancy_status", "family_status"
]

# Proxy attributes — may encode sensitive attributes indirectly:
proxy_risk = {
    "zip_code":     "may encode race/ethnicity",
    "name":         "may encode ethnicity/gender",
    "school":       "may encode socioeconomic status",
    "credit_file_age": "may encode age/immigration status",
}
```

### Fairness Metrics

```python
# Demographic parity — equal positive rate across groups
def demographic_parity(predictions, group):
    rates = {g: predictions[group == g].mean() for g in group.unique()}
    return rates  # should be equal across groups

# Equal opportunity — equal true positive rate across groups
def equal_opportunity(predictions, labels, group):
    tpr = {g: ((predictions == 1) & (labels == 1))[group == g].mean()
           for g in group.unique()}
    return tpr  # should be equal — same chance of correct positive

# Calibration — predicted probability matches actual rate
def calibration_check(predicted_proba, labels, group):
    # Same predicted probability should mean same actual outcome across groups
    ...
```

**No single fairness metric is universally correct** — document which metric you chose and why, acknowledge the tradeoffs.

---

## Transparency Requirements

### Disclosure to Users

```
Users must know:
  - They are interacting with an AI (not a human)
  - What data is used to make decisions about them
  - What decisions are being made automatically
  - How to request human review of an automated decision

Disclosure levels:
  ALWAYS:  "You are chatting with an AI assistant"
  ALWAYS:  "Your loan application will be scored by our AI model"
  ON REQUEST: "Your score was influenced by: payment history (40%), credit utilization (30%)..."
  ON DENIAL:  "You have the right to request human review of this decision"
```

### Explainability

```python
# High-stakes decisions must be explainable

# ❌ Black box for high-stakes decision
loan_approved = complex_model.predict(applicant_features)

# ✅ Explainable decision with feature importance
loan_decision = explainable_model.predict_with_explanation(applicant_features)
# Returns:
# {
#   "decision": "denied",
#   "confidence": 0.78,
#   "top_factors": [
#     {"factor": "payment_history", "impact": "negative", "weight": 0.40},
#     {"factor": "credit_utilization", "impact": "negative", "weight": 0.30},
#   ],
#   "appeal_available": True
# }
```

---

## Consent & Data Governance

```
Consent must be:
  INFORMED  — user understands what they're consenting to
  SPECIFIC  — not buried in ToS, not bundled with other consent
  REVOCABLE — user can withdraw consent and data is deleted
  PRIOR     — consent before data collection, not after

Questions to answer before collecting data for AI:
  □ What data is collected?
  □ What is it used for (training? inference? both)?
  □ Is it shared with third parties (including model providers)?
  □ How long is it retained?
  □ Can users request deletion?
  □ What happens to models trained on data if user deletes their account?
```

---

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
