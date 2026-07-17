---
name: ui-components
description: 'UI component patterns — exact CSS templates, behavior specs, interaction states, and composition rules for Navbar, Hero, Section, Work/List rows, About, Contact, Footer. Template-based: copy-paste, do NOT improvise.

  '
metadata:
  ai-native-skills.version: 1.0.0
  ai-native-skills.type: skill
  ai-native-skills.implements: ai-native-core/contracts/skills/design/ux-ui-patterns.contract.yaml
  ai-native-skills.contract-version: "^1.0.0"
  ai-native-skills.tags: '[''ui'', ''components'', ''patterns'', ''templates'', ''css'', ''behavior'']'
---

# UI Components

## ⚠️ HARD RULES

1. **Copy template verbatim — zero improvisation.** Improvisation = bugs. Template = correct behavior on all viewports.
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

1. **Copy template verbatim — zero improvisation.**
2. **External behavior:** check `ux-patterns-for-developers` before writing component behavior.
3. **After 2 failed patches → `write_file` full rewrite.**
