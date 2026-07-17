# Icon Family Selection & Genre Map

> One icon family per product. Pick once, never mix.

## Icon Family Spectrum

```
OUTLINE (stroke-based)         SOLID (filled)           DUOTONE (two-tone)
clean, modern, lightweight     bold, clear, functional  premium, expressive
  Lucide, Heroicons,             Phosphor (solid),        Phosphor (duotone),
  Feather, Tabler               Material Symbols         Iconoir (some)
```

## Genre → Icon Family

```
ZEN / MINIMALIST:
  Family:  Lucide React / Heroicons (outline)
  Style:   stroke-width 1 – 1.5 (lighter = more refined)
  Why:     Thin strokes match weight-300 typography; heavy icons break restraint
  Avoid:   Solid fills, bold stroke (> 2px)

EDITORIAL:
  Family:  Lucide / Heroicons / Feather
  Style:   stroke-width 1.5 (default) — matches editorial type weight
  Why:     Clean editorial needs clean icons; not too decorative

MODERN MINIMAL (SaaS):
  Family:  Lucide / Heroicons / Radix Icons / Phosphor (regular)
  Style:   stroke-width 1.5 – 2
  Why:     Crisp, functional — icons as UI affordances not decoration

ATMOSPHERIC:
  Family:  Phosphor (duotone) / Heroicons / custom SVG
  Style:   Duotone with accent color in second layer
  Why:     Depth + expressiveness; duotone fits rich dark palette

PLAYFUL:
  Family:  Phosphor (bold) / Iconoir / Remix Icon
  Style:   stroke-width 2 – 2.5 OR solid fills
  Why:     Bolder icons match playful typography weight + energy
```

## Recommended Libraries (free, maintained)

```
Lucide React    — 1000+ icons, outline, stroke-width param, tree-shakeable
Heroicons       — 292 icons, 3 styles, Tailwind team, consistent
Phosphor Icons  — 9000+ icons, 6 weights, most flexible
Tabler Icons    — 5000+ outline icons, stroke-width customizable
Radix Icons     — 300 minimal icons, Radix UI family
Material Symbols — Google, variable font-based, optical sizing built-in
```

## Mixing Rule

```
❌ Lucide nav icons + Material buttons + Heroicons cards → visual noise
❌ Outline hero + solid body → inconsistent language
✅ One family, all instances — no exceptions
✅ Exception: custom brand icons (logo marks, product icons) are separate
```
