# Palette Construction

> Build palette bottom-up: start with bg, derive everything else.

## 5-Step Palette Construction

```
STEP 1 — ANCHOR (bg)
  Pick bg value + temperature first. Everything derives from this.
  Warm dark:  hsl(38, 8%, 6%)   → #0c0b09
  Cool dark:  hsl(220, 10%, 8%) → #0d0f14
  Warm light: hsl(40, 20%, 97%) → #faf8f3
  Pure white: hsl(0, 0%, 100%)  → #ffffff

STEP 2 — INK STEPS (4 steps from anchor)
  muted:  anchor + L+35 → barely visible (decorative, disabled)
  subtle: anchor + L+50 → secondary text, labels
  ink:    anchor + L+70 → primary text
  bright: anchor + L+85 → emphasis, display text

STEP 3 — SURFACE (between bg and muted)
  surface:     anchor + L+8  → card, input background
  surface-alt: anchor + L+12 → hover state, elevated surface

STEP 4 — ACCENT (one color, one job)
  Derive from genre (see genre-palette-map.md)
  Must contrast with bg: ≥ 3:1 for decorative, ≥ 4.5:1 for text

STEP 5 — SEMANTIC ROLES
  --bg, --surface, --border, --muted, --subtle, --ink, --bright, --accent
  Hand off to design-system for token naming
```

## Palette Template — Warm Dark (Zen)

```css
/* Primitives */
--warm-950: #0c0b09;   /* bg */
--warm-900: #111009;   /* bg-alt */
--warm-800: #181610;   /* surface */
--warm-700: #222018;   /* surface-raised */
--warm-500: #4a4840;   /* muted */
--warm-400: #7a7870;   /* subtle */
--warm-200: #c4c0b4;   /* ink */
--warm-100: #e8e4d8;   /* bright */
--warm-50:  #f4f0e8;   /* light mode bg */
--sage:     #7a9e7a;   /* accent — live status only */

/* Rule: bg → surface differ by ≥ L+5 to be visible */
/* Rule: ink on bg contrast ≥ 7:1 for dark mode */
```

## Palette Template — Pure Light

```css
--bg:      #ffffff;
--surface: #f8f8f8;
--border:  rgba(0,0,0,0.07);
--muted:   #9a9690;
--subtle:  #5a5650;
--ink:     #1a1810;
--bright:  #0a0800;
--accent:  #4a7a4a;  /* sage — darker for light bg contrast */
```

## Common Mistakes

```
❌ bg and surface same value → no depth, flat
❌ Ink too close to bg (L diff < 50) → fails contrast
❌ Accent reused for 3 different roles → semantic collapse
❌ Mixed temperature (warm bg + cool ink) → visual tension
❌ Mid-value bg (L 40–60%) → neither dark nor light — uncanny valley
✅ Derive ink steps from bg anchor → natural temperature consistency
✅ One accent, one job
```
