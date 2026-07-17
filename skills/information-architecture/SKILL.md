---
name: information-architecture
description: Information architecture for digital products — site map design, navigation hierarchy, content grouping, URL structure, and search vs browse decisions. Foundation skill that runs before design starts.
license: MIT
metadata:
  ai-native-skills.version: 1.1.0
  ai-native-skills.author: puterakahfi
  ai-native-skills.type: skill
  ai-native-skills.implements: ai-native-core/contracts/skills/design/information-architecture.contract.yaml
  ai-native-skills.related_skills: "['ux-psychology', 'ux-ui-patterns', 'content-strategy', 'product-manager']"
---

# Information Architecture Skill

<!-- ROUTER — detailed phases and gates live in references/ -->

## HARD RULES (enforce before any design work)

```
1. Content inventory MUST be complete before any navigation decisions
2. Max 7 top-level nav items (Miller's Law — working memory limit)
3. URL structure: noun-only slugs, no verbs, kebab-case
   ✅ /user-settings    ❌ /manage-user-settings
   ✅ /blog/article     ❌ /view-blog-post
```

---

## Core Principle

```
IA answers: where does this live, and how do users find it?

Three questions to answer before any design starts:
  1. What content/features exist? (inventory)
  2. How should they be grouped? (classification)
  3. How do users navigate between them? (wayfinding)

If you design before answering these, you will redesign later.
```

---

## 5-Phase Overview

| Phase | Name | Reference |
|-------|------|-----------|
| 1 | Content Inventory | [phases-1-3.md](references/phases-1-3.md#phase-1-content-inventory) |
| 2 | Classification (Card Sorting) | [phases-1-3.md](references/phases-1-3.md#phase-2-classification-card-sorting) |
| 3 | Navigation Hierarchy | [phases-1-3.md](references/phases-1-3.md#phase-3-navigation-hierarchy) |
| 4 | URL Structure | [phases-4-5-sitemap.md](references/phases-4-5-sitemap.md#phase-4-url-structure) |
| 5 | Search vs Browse Decision | [phases-4-5-sitemap.md](references/phases-4-5-sitemap.md#phase-5-search-vs-browse-decision) |

### Load instructions

```
Start every IA engagement by running all 5 phases in order:

  Phase 1–3 (foundation):
    → Load references/phases-1-3.md
    → Complete inventory, card sort, nav hierarchy before proceeding

  Phase 4–5 + site map:
    → Load references/phases-4-5-sitemap.md
    → Define URL schema, decide search/browse, output site map

  IA Gates (quality check):
    → Run all 4 gates from references/phases-4-5-sitemap.md
    → Minimum score 8.0 before handing off to design
```

---

## IA Gates Summary (Scored 0–10, Min 8)

| Gate | Check | Min Score |
|------|-------|-----------|
| IA1 | Inventory complete, priorities set | 8 |
| IA2 | ≤ 7 nav items, task-oriented labels | 8 |
| IA3 | Core features ≤ 3 clicks deep | 8 |
| IA4 | Human-readable URLs, mirrors IA | 8 |

Full gate checklists → [references/phases-4-5-sitemap.md#ia-gates](references/phases-4-5-sitemap.md#ia-gates-scored-010-min-8)

---

## HARD RULES (repeat — enforce at delivery)

```
1. Content inventory MUST be complete before any navigation decisions
2. Max 7 top-level nav items (Miller's Law — working memory limit)
3. URL structure: noun-only slugs, no verbs, kebab-case
```
