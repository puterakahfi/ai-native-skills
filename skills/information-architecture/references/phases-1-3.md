# IA Reference: Phases 1–3

> Foundation phases — complete these before URL structure or design begins.

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
