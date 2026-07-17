# Sizing, Weight & Optical Alignment

> Icons scale optically, not mathematically.

## Standard Size Scale

```
SIZE    USE CASE                          STROKE WIDTH
12px    Dense UI labels, badges           1px
16px    Inline with small text, chips     1 – 1.5px
20px    Default UI (nav, buttons, inputs) 1.5px      ← most common
24px    Standard components               1.5 – 2px
32px    Feature icons, section markers    1.5px (outline) or solid
48px    Illustration-scale icons          filled/duotone only
```

## Stroke Width Matching Typography

```
Typography weight 300 (zen)     → stroke-width 1 – 1.5
Typography weight 400 (regular) → stroke-width 1.5
Typography weight 500–600       → stroke-width 2
Typography weight 700+          → stroke-width 2 – 2.5 OR solid

Principle: icon stroke weight should match nearby text weight visually.
Mismatch = icon feels foreign.
```

## Optical Alignment (not mathematical)

```
PROBLEM: Center an icon next to text with flexbox align-items:center
         → mathematically centered, but optically low

WHY: Icons have optical weight at visual center, not bounding box center.
     Circular icons (search, settings) read low. Ascending icons (up arrow) read high.

FIX 1: translate(-1px) or translate(0, -1px) — nudge optically heavy icons up
FIX 2: align-items: baseline + padding adjustment on icon wrapper
FIX 3: Use icon family's built-in optical sizing (Material Symbols has this)

CSS pattern:
  .icon-inline {
    display: inline-flex;
    align-items: center;
    translate: 0 -1px;  /* optical correction for most circular icons */
  }
```

## Sizing Tokens

```css
:root {
  --icon-xs: 12px;
  --icon-sm: 16px;
  --icon-md: 20px;   /* default */
  --icon-lg: 24px;
  --icon-xl: 32px;
}
```

## Anti-Patterns

```
❌ 24px icon next to 12px label → icon dominates, hierarchy wrong
❌ Heavy stroke icon with weight-300 type → icon screams, type whispers
❌ CSS scale(0.5) on 48px icon → blurry, wrong stroke weight
❌ Icon only in button without text label → a11y fail + ambiguous
✅ Icon size ≈ cap-height of adjacent text (not font-size)
✅ Stroke weight matches type weight
```
