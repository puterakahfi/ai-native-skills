---
name: dark-light-theming
description: Dual-theme system design — semantic token mapping, system preference detection, flash-of-wrong-theme prevention, color inversion pitfalls, and mid-session toggle. One token table, two primitive maps.
license: MIT
metadata:
  ai-native-skills.version: 1.0.1
  ai-native-skills.author: puterakahfi
  ai-native-skills.type: skill
  ai-native-skills.implements: ai-native-core/contracts/skills/design/dark-light-theming.contract.yaml
  ai-native-skills.contract-version: "^1.0.0"
  ai-native-skills.related_skills: '["design-system", "accessibility", "readability"]'
---

# Dark/Light Theming Skill

## Reviewed core contract interface

Source: `ai-native-core/contracts/skills/design/dark-light-theming.contract.yaml` · compatible line: `^1.0.0`

```yaml
required_inputs:
- color_token_map
- theme_toggle_requirement
allowed_outputs:
- theme_token_map
- fouc_prevention_strategy
- theming_gate_scores
quality_gates:
- no_fouc_on_theme_switch
- tokens_mapped_for_both_themes
- system_preference_respected
```

Map every semantic token for both themes, respect system preference when required, and produce a FOUC-prevention strategy before claiming the theme switch is complete.

Keep this interface synchronized with the pinned core contract. Exact declarations make ownership reviewable; they do not replace rendered, runtime, accessibility, or product evidence.

## ⛔ HARD RULES (read before starting)

1. **Preserve existing theme infra** — never add a second theme system on top of an existing one. If `data-theme` or CSS custom properties are already in place, extend them; do not create parallel systems.
2. **Semantic tokens only** — no hardcoded hex values in components. Always use `var(--semantic-token)`.
3. **Toggle `aria-label` = next action** — label must describe what will happen, not the current state. e.g. "Switch to dark theme" when currently in light mode.
4. **Verify both modes** — take a light screenshot, a dark screenshot, then toggle back and confirm. All three steps required.

---

## Reference Files

Load the relevant reference before implementing:

| File | Contents | When to load |
|------|----------|--------------|
| `references/token-architecture.md` | Core Principle, Layer 1 (primitives), Layer 2 (semantic tokens) | Starting a new theme system or auditing token structure |
| `references/implementation.md` | System preference detection, toggle JS, FOUC prevention checklist, Theme Toggle UI HTML/CSS | Implementing detection, toggle, or fixing flash |
| `references/pitfalls-gates.md` | Color inversion pitfalls (5 types), Theming Gates checklist | Debugging visual bugs or running quality gates |

### How to load

```
skill_view(name='dark-light-theming', file_path='references/token-architecture.md')
skill_view(name='dark-light-theming', file_path='references/implementation.md')
skill_view(name='dark-light-theming', file_path='references/pitfalls-gates.md')
```

---

## Workflow Overview

1. **Audit existing theme infra** — check for existing `data-theme`, CSS vars, or media queries before adding anything.
2. **Load `token-architecture.md`** — set up or verify Layer 1 (primitives) + Layer 2 (semantic) tokens.
3. **Load `implementation.md`** — wire up system-preference detection + toggle. Ensure FOUC prevention script is inline `<head>`.
4. **Load `pitfalls-gates.md`** — review all 5 inversion pitfalls, then run all 4 Theming Gates (min score 8.0).
5. **Verify both modes** — light screenshot → dark screenshot → toggle back.

---

## Quick Reference: Semantic Token Pattern

```
One semantic token table. Two primitive maps.

semantic token (--text-primary)
  → dark mode:  #f0f0f0
  → light mode: #111111

Never:
  color: #f0f0f0           ← hardcoded, breaks in light mode
  color: var(--dark-text)  ← mode-specific var, semantic collapse

Always:
  color: var(--text-primary)  ← semantic, works in both modes
```

---

## ⛔ HARD RULES (reminder at bottom)

1. **Preserve existing theme infra** — never add a second theme system on top of an existing one.
2. **Semantic tokens only** — no hardcoded hex values in components.
3. **Toggle `aria-label` = next action** — e.g. "Switch to dark theme" when currently in light mode.
4. **Verify both modes** — light screenshot + dark screenshot + toggle back. All three required.
