---
name: decision-making
description: Engineering decision-making frameworks — reversibility classification, pre-mortem, OODA loop, options thinking, epistemic humility, and decision traceability. For making better decisions faster, and knowing when to delay.
license: MIT
metadata:
  ai-native-skills.version: 1.1.0
  ai-native-skills.author: puterakahfi
  ai-native-skills.type: skill
  ai-native-skills.implements: ai-native-core/contracts/skills/product/decision-making.contract.yaml
  ai-native-skills.related_skills: "['systems-thinking', 'adr', 'ethics-responsible-ai', 'risk-modeling']"
---

# Decision Making Skill

## HARD RULES

- **Classify reversibility first** — every decision is Type 1 or Type 2 before analysis begins
- **Use pre-mortem on any irreversible decision** — no exceptions
- **Document decision + rationale + alternatives considered** — for all Type 1 decisions

---

## Core Principle

```
Two skills: making good decisions AND knowing when NOT to decide.

The meta-question before any decision:
  "Is this reversible or irreversible?"

Reversible (Type 2 — two-way door):
  → Decide fast, with less information
  → You can course-correct
  → Don't over-analyze

Irreversible (Type 1 — one-way door):
  → Slow down, gather more information
  → Involve more stakeholders
  → Write the decision down (ADR)

Most engineering decisions are reversible.
Most teams treat them as irreversible → slow, over-engineered.
```

---

## Framework Overview

| Framework | Purpose | Load reference |
|---|---|---|
| Reversibility Classification | Type 1 vs Type 2 — classify first | `references/frameworks-a.md` |
| Pre-Mortem | Anticipate failure before committing | `references/frameworks-a.md` |
| OODA Loop | Fast-moving decisions and incidents | `references/frameworks-a.md` |
| Options Thinking | Preserve optionality, hedge bets | `references/frameworks-b.md` |
| Epistemic Humility | Know what you don't know | `references/frameworks-b.md` |
| Decision Traceability | Record + ADR for irreversible decisions | `references/frameworks-b.md` |
| Decision Gates | Scored quality gates (min 8/10) | `references/frameworks-b.md` |

**Load references before applying frameworks.**

Load frameworks A: `skill_view(name='decision-making', file_path='references/frameworks-a.md')`
Load frameworks B: `skill_view(name='decision-making', file_path='references/frameworks-b.md')`
