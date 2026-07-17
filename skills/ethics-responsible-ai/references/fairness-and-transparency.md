# Fairness & Transparency Reference

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
