---
name: information-architecture
description: Information architecture for digital products — site map design, navigation hierarchy, content grouping, URL structure, and search vs browse decisions. Foundation skill that runs before design starts.
version: 1.0.0
author: puterakahfi
license: MIT
type: skill
implements: ai-native-core/contracts/skills/experience-design/information-architecture.contract.yaml
related_skills: [ux-psychology, ux-ui-patterns, content-strategy, product-manager]
---

# Information Architecture Skill

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

## Phase 1: Content Inventory

List everything that needs to exist:

```
For each item, record:
  - Name
  - Type (page | feature | data | action)
  - Owner (who creates/maintains this?)
  - Audience (who needs this?)
  - Priority (P0 = must have | P1 = should | P2 = nice)
  - Current location (if migrating)

Output: content inventory spreadsheet
```

---

## Phase 2: Classification (Card Sorting)

Group inventory items into clusters that make sense to users.

### Open Card Sort (discovery)
```
Method: give users unlabeled cards, ask them to group and name groups
Use when: new product, unknown mental model
Output: affinity map → candidate navigation labels
```

### Closed Card Sort (validation)
```
Method: give users pre-defined categories, ask where items belong
Use when: you have a draft structure, want to validate
Output: % agreement per card → confidence per placement
```

### Heuristic grouping (agent shortcut)
```
When user research is not available, apply these rules:

  1. Group by user task — not by system function
     ❌ "Data Management" (system-oriented)
     ✅ "Your projects" (user-oriented)

  2. Group by frequency of use
     High frequency → top nav or persistent sidebar
     Low frequency → settings, profile, help

  3. Separate content from configuration
     Content: what users create/consume
     Config: how the product behaves
     Never mix these in same nav level

  4. Limit top-level nav to 5–7 items (Miller's Law)
     More → user cannot hold structure in working memory

  5. Parallel structure — items at same level should be same type
     ❌ Dashboard | Projects | Create New | Settings | Help
         (action mixed with nouns)
     ✅ Dashboard | Projects | Team | Settings
```

---

## Phase 3: Navigation Hierarchy

### Flat vs Deep

```
Flat (1–2 levels):
  Pro:  everything visible, low cognitive load
  Con:  too many items at top = overwhelming
  Use:  simple sites, ≤ 12 total pages

Deep (3+ levels):
  Pro:  scalable, handles large content sets
  Con:  users get lost, breadcrumbs required
  Use:  complex apps, documentation, e-commerce

Rule: depth ≤ 3 for primary flows. Users should reach any core feature in ≤ 3 clicks.
```

### Navigation Patterns

```
Top Nav Bar:
  Use: flat site, 3–7 primary sections
  Not: apps with complex hierarchy

Sidebar Nav:
  Use: 7+ sections, frequent switching, nested hierarchy
  Not: mobile-first, content-reading experiences

Bottom Nav (mobile):
  Use: 3–5 primary sections on mobile
  Not: more than 5 items (use hamburger instead)

Breadcrumbs:
  Use: depth > 2, content-heavy hierarchies
  Not: flat sites (noise, no benefit)

Tab Nav:
  Use: sibling pages with related content (Settings: Profile | Security | Billing)
  Not: primary navigation (too many tabs = confusion)
```

### Navigation Labels

```
Good labels are:
  - Short (1–2 words)
  - Task-oriented ("View reports" not "Reports Module")
  - Mutually exclusive (items should not fit in 2+ categories)
  - Exhaustive (every item has exactly one right place)

Test labels with first-click testing:
  Show nav, ask "where would you click to do X?"
  ≥ 80% agreement = label is working
  < 60% agreement = rethink the label or grouping
```

---

## Phase 4: URL Structure

```
Principles:
  1. Human-readable — no GUIDs in user-facing URLs
     ❌ /posts/e3f2a1b4-8c7d-4e9f-a1b2-c3d4e5f6a7b8
     ✅ /posts/building-scalable-saas

  2. Hierarchical — URL mirrors IA
     /projects/:id/tasks/:taskId
     /blog/:year/:slug

  3. Lowercase, hyphens (not underscores)
     ✅ /user-settings
     ❌ /User_Settings

  4. Stable — changing URLs breaks links, SEO
     Use slugs that won't change (title-based slugs can change if title changes)
     Consider: /posts/:id/:slug — ID = stable, slug = readable but not canonical

  5. Short — remove noise
     ❌ /en/website/sections/blog/posts/2026/07/article-title
     ✅ /blog/article-title
```

---

## Phase 5: Search vs Browse Decision

```
Users find things in two modes:
  BROWSE — "I'll know it when I see it" (exploring, discovering)
  SEARCH — "I know exactly what I want" (known-item seeking)

Provide search when:
  □ > 200 items of same type
  □ Users know the name of what they want
  □ Content is frequently updated
  □ Items have meaningful metadata (date, author, tag)

Provide browse when:
  □ < 100 items
  □ Users are discovering, not retrieving
  □ Items have strong visual identity (images, icons)
  □ Serendipitous discovery has value (portfolio, blog)

Provide both when:
  □ Large content set AND diverse user intent
  □ Add filters as the bridge (search + faceted browse)
```

---

## Site Map Format

```
Output a site map before starting any design:

pkahfi.com
├── / (Home — personal landing)
│   ├── Hero (name + stance)
│   ├── Work (LIVE products only)
│   ├── About
│   └── Contact
├── /blog (external: blog.pkahfi.com)
└── /blueprint (external: blueprint.pkahfi.com)

Notation:
  / = page
  (description) = page purpose
  ├── = child page or section
  [external] = redirects or external domain
  [auth] = requires authentication
  [draft] = not yet built
```

---

## IA Gates (Scored 0–10, Min 8)

```
Gate IA1: Inventory Complete
  □ All content/features listed before design started?
  □ Priority assigned (P0/P1/P2)?
  Score: __ / 10

Gate IA2: Navigation Clarity
  □ ≤ 7 top-level nav items?
  □ Labels task-oriented, not system-oriented?
  □ No item fits in 2+ categories?
  Score: __ / 10

Gate IA3: Depth Appropriate
  □ Core features reachable in ≤ 3 clicks?
  □ Flat vs deep choice matches content volume?
  Score: __ / 10

Gate IA4: URL Structure
  □ URLs human-readable?
  □ URL hierarchy mirrors IA hierarchy?
  □ No GUIDs in user-facing URLs?
  Score: __ / 10

OVERALL: __ / 10   MINIMUM: 8.0
```
