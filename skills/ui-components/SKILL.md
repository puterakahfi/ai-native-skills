---
name: ui-components
description: 'UI component patterns — exact CSS templates, behavior specs, interaction states, and composition rules for Navbar, Hero, Section, Work/List rows, About, Contact, Footer. Template-based: copy-paste, do NOT improvise.

  '
metadata:
  ai-native-skills.version: 1.1.0
  ai-native-skills.type: skill
  ai-native-skills.implements: ai-native-core/contracts/skills/design/ux-ui-patterns.contract.yaml
  ai-native-skills.contract-version: "^1.0.0"
  ai-native-skills.tags: '[''ui'', ''components'', ''patterns'', ''templates'', ''css'', ''behavior'']'
---

# UI Components

## Core contract interface

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

Component work starts with `brief_signals` and `content_inventory`. Select the pattern through the relevant decision tree, record the `decision_tree_path`, and verify that the hero pattern matches content volume. Only after selection may the chosen template be copied verbatim.

## ⚠️ HARD RULES

1. **Select first, then copy the chosen template verbatim.** Pattern selection comes from the decision tree, brief signals, and content inventory; improvising after selection still creates bugs.
2. **External behavior:** check `ux-patterns-for-developers` before writing component behavior.
3. **After 2 failed patches → `write_file` full rewrite.** Do not keep patching broken CSS.

---

## Component Index

Load each reference file when working on those components:

| Component | Reference File | Load Command |
|-----------|---------------|-------------|
| 01 · Navbar | navbar.md | `skill_view(name='ui-components', file_path='references/navbar.md')` |
| 02 · Hero | hero.md | `skill_view(name='ui-components', file_path='references/hero.md')` |
| 03 · Section | sections-a.md | `skill_view(name='ui-components', file_path='references/sections-a.md')` |
| 04 · Work Row | sections-a.md | `skill_view(name='ui-components', file_path='references/sections-a.md')` |
| 05 · About | sections-b.md | `skill_view(name='ui-components', file_path='references/sections-b.md')` |
| 06 · Contact | sections-b.md | `skill_view(name='ui-components', file_path='references/sections-b.md')` |
| 07 · Footer | sections-b.md | `skill_view(name='ui-components', file_path='references/sections-b.md')` |
| 08 · Scroll Reveal | interactions.md | `skill_view(name='ui-components', file_path='references/interactions.md')` |
| 09 · Verification | interactions.md | `skill_view(name='ui-components', file_path='references/interactions.md')` |

---

## Pitfalls Summary

- **No improvised CSS** — always copy the template from the reference file
- **No missing max-width** — all sections need `max-width: 1280px` inner container
- **No `min-height:100vh` on Hero** — use `display:block` + `padding` (not grid/flex-center)
- **Touch targets** — `height:44px` + `display:flex` + `align-items:center` on the link itself
- **CSS patch limit** — after 2 failed patches, rewrite full file with `write_file`
- **No self-closing divs** as grid rows

→ Full pitfalls list: `skill_view(name='ui-components', file_path='references/interactions.md')`

---

## ⚠️ HARD RULES (reminder)

1. **Select through the decision tree, then copy the chosen template verbatim.**
2. **External behavior:** check `ux-patterns-for-developers` before writing component behavior.
3. **After 2 failed patches → `write_file` full rewrite.**
