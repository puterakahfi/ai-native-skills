---
name: ux-ui-patterns
description: UI/UX pattern library for making layout decisions — which hero pattern fits the goal, which card pattern fits the content, which nav pattern fits the context. Decision tree for pattern selection, not just a list of patterns.
license: MIT
metadata:
  ai-native-skills.version: 1.0.1
  ai-native-skills.author: puterakahfi
  ai-native-skills.type: skill
  ai-native-skills.implements: ai-native-core/contracts/skills/design/ux-ui-patterns.contract.yaml
  ai-native-skills.contract-version: "^1.0.0"
  ai-native-skills.related_skills: "['master-design', 'ux-psychology', 'design-system', 'readability']"
---

# UX/UI Patterns Skill

## Reviewed core contract interface

Source: `ai-native-core/contracts/skills/design/ux-ui-patterns.contract.yaml` · compatible line: `^1.0.0`

```yaml
required_inputs:
- brief_signals
- content_inventory
allowed_outputs:
- pattern_selection
- decision_tree_path
- pattern_gate_scores
quality_gates:
- pattern_selected_from_decision_tree_not_arbitrary
- hero_pattern_matches_content_volume
```

Use brief_signals and content_inventory before choosing a pattern. Return the pattern selection, decision-tree path, and gate scores so the decision can be reviewed instead of treated as arbitrary taste.

Keep this interface synchronized with the pinned core contract. Exact declarations make ownership reviewable; they do not replace rendered, runtime, accessibility, or product evidence.

> ⚠️ **HARD RULE — Pattern Selection**
> Use the decision tree in the relevant reference file FIRST.
> Never pick a pattern by aesthetics alone.
> Check `ux-patterns-for-developers` before implementing any component behavior.

---

## Pattern Categories & Reference Files

### 1. Hero Patterns + Navigation Patterns
**File:** `references/hero-nav.md`

Load when:
- Designing or choosing a hero section (personal, SaaS, portfolio, marketing)
- Selecting a nav structure (top nav, sidebar, hamburger, bottom tab)

Contains:
- Core Principle + decision process
- Hero Pattern Selection Decision Tree
- TEXT / SPLIT / CENTERED / GRID Hero specs
- Nav Pattern Selection (by content volume + user type)
- HORIZONTAL TOP NAV + SIDEBAR NAV specs

---

### 2. Card Patterns + Layout Grid Patterns
**File:** `references/cards-grid.md`

Load when:
- Choosing a card type (feature, editorial, stat, profile, comparison, timeline)
- Deciding on a grid layout (1–6+ items, responsive breakpoints)

Contains:
- Card Type Selection decision tree
- FEATURE / EDITORIAL / STAT Card specs
- Grid Selection Rule (content count → grid choice)
- Responsive grid CSS with breakpoints

---

### 3. Section Patterns + Form Patterns + State Patterns
**File:** `references/sections-forms-states.md`

Load when:
- Laying out a personal or marketing page section flow
- Designing form inputs, labels, errors
- Ensuring all interactive states are designed (hover, focus, error, loading, etc.)

Contains:
- Section Flow for Personal Pages (eye-tracking proven order)
- Section Break Patterns (alternating bg, borders, whitespace)
- Input Field Spec (height, padding, label, error, a11y)
- Full State Pattern checklist (Default → Success)
- Full Anti-Pattern Catalog

---

## How to Use This Skill

1. **Identify the design problem** (hero, nav, card, grid, section, form, state)
2. **Load the relevant reference file** from the table above
3. **Follow the decision tree** — never skip to specs without the tree
4. **Check the Anti-Patterns** at the bottom of each reference file before finalizing
5. **Verify component behavior** against `ux-patterns-for-developers` before shipping

---

> ⚠️ **HARD RULE — Before Finalizing**
> Anti-patterns are listed at the bottom of each sub-file.
> Agent MUST check anti-patterns before marking any pattern implementation complete.
> Missing interactive states (focus, error, loading) = incomplete design — do not ship.
