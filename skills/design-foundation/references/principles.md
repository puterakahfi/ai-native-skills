# Foundation Principles

> Universal design quality — applies to every genre, every brand.

## 1. Hierarchy (Visual Structure)

```
Hierarchy is not decoration — it is navigation.
Without hierarchy, the eye has no path. Without a path, content is not read.

MINIMUM REQUIREMENTS:
  H1/body ratio:   ≥ 2.5× (size, weight, or both)
  H2/body ratio:   ≥ 1.6×
  H3/body ratio:   ≥ 1.25×
  Adjacent levels: must be visually distinguishable at a glance

GENRE ADJUSTS MAGNITUDE, NOT PRESENCE:
  zen (wt 300):   needs ≥ 3.5× ratio — weight not doing work, size must
  editorial:      2.5–3.5× — balance authority + readability
  SaaS:           2.5–3×   — clear but dense
  playful:        2.5–3×   — bold weights can compress ratio
```

## 2. Ma — Intentional Space

```
Ma is not "add whitespace" — Ma is "this space has a job."

TEST: cover the space. Does adjacent content feel crowded?
  YES → Ma was working. Restore it.
  NO  → Dead space. Remove or restructure content to fill it.

DEAD SPACE CAUSES:
  min-height: 100vh on sparse content   ← FORBIDDEN (foundation rule)
  large section padding + 2 lines text  ← restructure content
  hero with nothing below fold          ← shrink hero, add content

MA IS EARNED:
  Content earns space by being rich, dense, or visually complex.
  Sparse content needs less space, not more.
```

## 3. Kanso — Eliminate the Unnecessary

```
Every element must answer one question: "What is my job?"

DECORATIVE ELEMENT has no job → remove
DUPLICATE ELEMENT says the same thing twice → remove one
AMBIENT ELEMENT "just to fill space" → remove + tighten layout

KANSO CHECKLIST:
  □ Does this element carry information?
  □ Does this element aid navigation or affordance?
  □ Does this element establish hierarchy or rhythm?
  □ No to all three → it does not belong

Applies to: dividers, icons, background patterns, gradients, animations,
            empty sections, redundant labels, filler copy
```

## 4. Semantic Tokens

```
Rule: no component ever knows a raw value.

❌ color: #7a9e7a
❌ padding: 24px
❌ font-size: 38px

✅ color: var(--accent)
✅ padding: var(--sp-6)
✅ font-size: var(--text-2xl)

WHY: tokens = single source of truth. Change token → everything updates.
     Hardcoded values = maintenance debt + theming breakage.

GENRE provides token VALUES.
FOUNDATION requires token USAGE.
```

## 5. Accessibility as Foundation

```
A11y is not a phase 5 checkbox — it is a foundation constraint.

ALWAYS REQUIRED:
  Contrast ≥ 4.5:1 primary text (WCAG AA)
  Contrast ≥ 3:1 large text + UI components
  Touch targets ≥ 44×44px
  Focus-visible on all interactive elements
  aria-label on icons, buttons without text
  Skip link for keyboard navigation
  prefers-reduced-motion respected

GENRE DOES NOT EXEMPT FROM A11Y:
  zen dark mode: still needs 4.5:1 contrast
  atmospheric: glowing neon still needs contrast check
  playful: colorful palette still needs accessible ratios
```
