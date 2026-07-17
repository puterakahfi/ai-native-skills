---
name: design-system
description: Design token decisions and system construction — when to use which spacing scale, type scale, color role, elevation level, and motion token. Produces a declaration table before any pixel is designed. The design system is the single source of truth; all design decisions trace back to it.
license: MIT
metadata:
  ai-native-skills.version: 1.0.0
  ai-native-skills.author: puterakahfi
  ai-native-skills.type: skill
  ai-native-skills.implements: ai-native-core/contracts/skills/design/design-system.contract.yaml
  ai-native-skills.contract-version: "^1.0.0"
  ai-native-skills.related_skills: "['master-design', 'ux-ui-patterns', 'accessibility', 'design-review']"
---

# Design System Port

> This skill doubles as **Port 5: Design System & Accessibility** — the systematic cross-cutting layer.
> Load this for tokens, theming, and accessibility concerns.
> Adapter skills: `dark-light-theming`, `accessibility`

---

# Design System Skill

## ⚠️ HARD RULES (read before anything else)

```
RULE 1 — One semantic token = one role only, NEVER collapse
  ❌ --accent used for: logo + hover + status + CTA → semantic collapse
  ✅ Each token has a single, unambiguous job

RULE 2 — All spacing on 8px grid — NO raw px values
  ❌ padding: 10px; margin: 15px; gap: 7px;
  ✅ padding: var(--space-3); gap: var(--space-2);

RULE 3 — 1.333 Perfect Fourth scale for typography (landing pages / editorial)
  ❌ font-size: 18px; font-size: 22px; (arbitrary)
  ✅ font-size: var(--text-lg); (always from scale)

RULE 4 — Declare token table before using any value
  ❌ Design first, name tokens later
  ✅ Token table declared → then design within it
```

---

## Core Principle

```
Design system = decisions made once, applied everywhere.

Without it: every screen is a new negotiation between color, space, and type.
With it:    every screen is an instance of the same vocabulary.

Before designing ANY screen:
  1. Declare the token table
  2. Design within the tokens
  3. If a value is not in the token table → add it or use the nearest token

Never hardcode a value that should be a token.
```

---

## 6-Step Token Declaration Overview

| Step | Category | Reference File | Load Instruction |
|------|----------|---------------|-----------------|
| 1 | Color Tokens | `references/color-spacing.md` | Load for semantic roles, dark theme defaults, color decision protocol |
| 2 | Spacing Tokens | `references/color-spacing.md` | Load for 8px grid scale, spacing decision guide |
| 3 | Typography Tokens | `references/typography-elevation.md` | Load for type scale (1.333), weights, line heights, letter spacing |
| 4 | Elevation Tokens | `references/typography-elevation.md` | Load for shadow scale and hierarchy |
| 5 | Motion Tokens | `references/typography-elevation.md` | Load for durations, easings, reduced-motion pattern |
| 6 | Layout Tokens | `references/layout-checklist.md` | Load for container widths, border radius, layout philosophy |

> **Load pattern:** when working on any screen, load the relevant reference file(s) for the token categories you need. The checklist at the bottom of `references/layout-checklist.md` is the gate — every box must be checked before design begins.

---

## Step-by-Step Quick Reference

### Step 1 → Color Tokens
→ Load `references/color-spacing.md` — semantic color roles table, dark theme CSS defaults, color decision protocol, anti-patterns.

### Step 2 → Spacing Tokens
→ Load `references/color-spacing.md` — 8px base grid CSS, spacing decision guide (which step to use for inline vs section vs page).

### Step 3 → Typography Tokens
→ Load `references/typography-elevation.md` — scale ratio selection, font size tokens (1.333 scale), font weights, line heights, letter spacing.

### Step 4 → Elevation Tokens
→ Load `references/typography-elevation.md` — shadow levels (`shadow-none` → `shadow-xl`), elevation hierarchy.

### Step 5 → Motion Tokens
→ Load `references/typography-elevation.md` — duration tokens, easing tokens, `prefers-reduced-motion` CSS block.

### Step 6 → Layout Tokens
→ Load `references/layout-checklist.md` — container widths, border radius tokens, radius philosophy, one-primary-radius rule.

---

## Token Declaration Checklist (summary gate)

> Full checklist with FAIL conditions: `references/layout-checklist.md`

```
□ Color tokens declared — each has ONE semantic role
□ Spacing scale declared — 8px base, 12 steps
□ Type scale declared — one ratio chosen, 8 sizes
□ Font weights declared — 3–4 only
□ Line heights declared — 5 levels
□ Letter spacing declared — 5 levels
□ Elevation declared — 5 shadow levels
□ Motion declared — durations + easings
□ Border radius declared — 1–2 values for the product
```

---

## ⚠️ HARD RULES (repeated at bottom — enforced on every output)

```
RULE 1 — One semantic token = one role only, NEVER collapse
RULE 2 — All spacing on 8px grid — NO raw px values
RULE 3 — 1.333 Perfect Fourth scale for typography
RULE 4 — Declare token table before using any value

FAIL: any hardcoded value in design that is not in token table
FAIL: same hex used in multiple semantic roles
FAIL: any font size not from the scale
FAIL: spacing value not from 8px grid
```
