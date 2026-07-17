---
name: ethics-responsible-ai
description: Ethical analysis and responsible AI governance — fairness audit, harm assessment, transparency requirements, consent and data governance, accountability mapping, and power asymmetry analysis.
license: MIT
metadata:
  ai-native-skills.version: 1.0.0
  ai-native-skills.author: puterakahfi
  ai-native-skills.type: skill
  ai-native-skills.implements: ai-native-core/contracts/skills/quality/ethics-responsible-ai.contract.yaml
  ai-native-skills.contract-version: "~0.1"
  ai-native-skills.related_skills: "['ai-system-design', 'threat-modeling', 'accessibility', 'product-manager']"
---

# Ethics & Responsible AI

> **HARD RULES:** Bias audit before deployment. Document model limitations explicitly. Human oversight required for high-stakes decisions.

## The Core Rule

```
Every engineering decision is a moral decision.

Choosing not to consider ethics is itself an ethical choice —
and it is one that harms the people who cannot opt out of your system.

The question is not "is this technically possible?" but
"should we build this, for whom, and with what consequences?"
```

---

## Analysis Areas

This skill is split across two reference files:

### Part 1 — Fairness & Transparency

Covers: stakeholder impact mapping, identifying sensitive attributes, fairness metrics,
transparency and disclosure requirements, explainability, and consent & data governance.

→ See `references/fairness-and-transparency.md`

### Part 2 — Harm, Accountability & Checklist

Covers: accountability mapping, pre-launch harm assessment (direct, indirect, distributional),
power asymmetry analysis and mitigations, and the full pre-ship ethics checklist.

→ See `references/harm-and-accountability.md`

---

## Quick Reference

| Concern | Analysis | Reference |
|---|---|---|
| Who is affected? | Stakeholder impact map | fairness-and-transparency.md |
| Discriminatory outcomes | Fairness audit | fairness-and-transparency.md |
| User awareness | Transparency & disclosure | fairness-and-transparency.md |
| Data collection legality | Consent & data governance | fairness-and-transparency.md |
| Who is responsible? | Accountability map | harm-and-accountability.md |
| Could this hurt people? | Harm assessment | harm-and-accountability.md |
| Power imbalance | Power asymmetry analysis | harm-and-accountability.md |
| Pre-ship gate | Ethics checklist | harm-and-accountability.md |

**Gate:** Run fairness audit and harm assessment before any AI feature ships to production.
