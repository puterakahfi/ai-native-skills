---
name: technical-debt-governance
description: Technical debt governance — debt inventory, classification, interest calculation, paydown strategy, coupling metrics, and Boy Scout Rule enforcement. For teams that want to track and reduce debt systematically, not just complain about it.
license: MIT
metadata:
  ai-native-skills.version: 1.0.1
  ai-native-skills.author: puterakahfi
  ai-native-skills.type: skill
  ai-native-skills.implements: ai-native-core/contracts/skills/engineering/technical-debt-governance.contract.yaml
  ai-native-skills.contract-version: "^1.0.0"
  ai-native-skills.related_skills: '["refactoring", "systems-thinking", "observability-design", "adr"]'
---

# Technical Debt Governance Skill

## Reviewed core contract interface

Source: `ai-native-core/contracts/skills/engineering/technical-debt-governance.contract.yaml` · compatible line: `^1.0.0`

```yaml
required_inputs:
- codebase_ref
allowed_outputs:
- debt_inventory
- classification_report
- paydown_priority_list
- debt_gate_scores
quality_gates:
- debt_classified_by_type_and_impact
- high_impact_debt_has_paydown_plan
- new_debt_logged_before_merging
```

New debt must be classified and logged before merge. High-impact debt needs an owned paydown plan, priority, and gate status rather than an informal TODO.

Keep this interface synchronized with the pinned core contract. Exact declarations make ownership reviewable; they do not replace runtime, repository, architecture, test, or product evidence.


> **HARD RULES — apply always, top and bottom of every engagement:**
> 1. **Classify debt before paying it** — deliberate vs reckless vs inadvertent. Unclassified debt is unmanaged debt.
> 2. **Never pay debt without tests.** No test coverage = can't safely refactor.
> 3. **Debt register must be visible to the product team.** Engineering-only registers drift into irrelevance.

---

## Core Principle

```
Debt is not inherently bad — untracked debt is.

Good debt: deliberate shortcut to ship, with a clear paydown plan.
Bad debt: accidental complexity that compounds silently.

The test:
  Can you explain the debt to a new engineer in 2 sentences?
  Do you know what it costs per sprint to keep it?
  Is there a written plan to pay it down?

If no to any: the debt is unmanaged. Govern it now.
```

---

## References

| Topic | File |
|---|---|
| Debt classification (type + severity) · Debt inventory · Interest calculation | [references/debt-classification-and-inventory.md](references/debt-classification-and-inventory.md) |
| Paydown strategy · Boy Scout Rule · Coupling metrics · Governance ceremony · Gates | [references/paydown-and-governance.md](references/paydown-and-governance.md) |

---

## Quick-Start

1. **Classify** every known debt item (deliberate / reckless / inadvertent) → see `debt-classification-and-inventory.md`
2. **Enter** each item in the Debt Register with severity + interest estimate
3. **Calculate** Debt Tax = SUM(interest for all active debts) — report each sprint
4. **Allocate** 20% of sprint capacity to paydown — prioritise by ROI score
5. **Apply** Boy Scout Rule on every PR — leave it cleaner than you found it
6. **Review** in 15-min sprint ceremony — see `paydown-and-governance.md`

> **Reminder:** classify before paying · no paydown without tests · register visible to product team.
