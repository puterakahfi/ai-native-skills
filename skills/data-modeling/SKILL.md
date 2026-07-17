---
name: data-modeling
description: Data modeling skill — schema design, normalization tradeoffs, migration patterns, polyglot persistence decisions, index strategy, and soft delete governance. For engineers who need to decide WHERE and HOW data lives.
license: MIT
metadata:
  ai-native-skills.version: 1.0.0
  ai-native-skills.author: puterakahfi
  ai-native-skills.type: skill
  ai-native-skills.implements: ai-native-core/contracts/skills/engineering/data-modeling.contract.yaml
  ai-native-skills.contract-version: "^1.0.0"
  ai-native-skills.related_skills: '["domain-driven-design", "refactoring", "technical-debt-governance"]'
---

# Data Modeling Skill

> **HARD RULES**
> - **Model the domain, not the UI** — schema driven by read/write access patterns, not forms or screens
> - **Normalize first, denormalize for performance only** — measure before optimizing; consistency first
> - **Every table needs a natural key** — surrogate PKs alone are insufficient; business identity must be explicit

## Core Principle

```
Schema is the most expensive decision you make.
Changing it later costs 10x more than getting it right now.

The two questions:
  1. What queries will the system run? (query-first modeling)
  2. What are the consistency requirements? (transaction scope)

Never: model based on what the data "is"
Always: model based on how the data will be READ and WRITTEN
```

---

## References

| Topic | File |
|---|---|
| Normalization (1NF–BCNF), When to Denormalize, Migration Patterns (Expand-Contract, Batching) | [references/normalization-and-migration.md](references/normalization-and-migration.md) |
| Polyglot Persistence Decision, Index Strategy, Soft Delete Governance, Data Modeling Gates | [references/persistence-index-softdelete.md](references/persistence-index-softdelete.md) |

---

## Quick Decision Guide

```
Designing a new schema from scratch?        → Query-first, normalize to 3NF — see normalization-and-migration.md
Renaming/removing a column in production?   → Expand-Contract migration — see normalization-and-migration.md
Slow query on large table?                  → Index strategy — see persistence-index-softdelete.md
Which database to use?                      → Polyglot persistence decision — see persistence-index-softdelete.md
Should I soft-delete or hard-delete?        → Soft delete governance — see persistence-index-softdelete.md
Schema review gate score?                   → Data Modeling Gates D1–D4 — see persistence-index-softdelete.md
```
