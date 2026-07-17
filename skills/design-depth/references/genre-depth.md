# Depth by Genre

> Which depth technique matches which genre?

## Zen / Minimalist Depth

```
DEPTH MODE:   shallow → deep depending on asset availability
ATMOSPHERE:   ink wash / sumi-e — multiply blend on paper bg
OBJECTS:      ink paintings, stone, branch, water — transparent PNG
TYPOGRAPHY:   large brush-stroke display, small structured body
INTERLEAVE:   yes — objects emerge through display text
SCALE:        strong perspective — near 100%, far 50% opacity+blur
ACCENT:       red seal stamp — tiny, precise, Layer 5

CSS key:
  bg: #f4f0e8 (warm paper)
  atmosphere: multiply blend, ink wash gradient
  object: drop-shadow(0 12px 40px rgba(0,0,0,0.12))
  type-display: z-index 2 (behind object)
```

## Atmospheric / Dark Depth

```
DEPTH MODE:   deep (4–5 layers)
ATMOSPHERE:   radial vignette + mist fade on dark bg
OBJECTS:      3D renders, photography, glowing elements
TYPOGRAPHY:   large thin display (wt 200–300) on dark
INTERLEAVE:   yes — objects glow through/behind text
SCALE:        cinematic — extreme near/far contrast
ACCENT:       neon/phosphor highlight — tiny, glowing

CSS key:
  bg: #080810 (near black cool)
  atmosphere: radial gradient, vignette
  object: filter drop-shadow(0 0 40px var(--accent-glow))
  type-display: z-index 2, opacity 0.85
```

## Editorial Depth

```
DEPTH MODE:   shallow (2–3 layers)
ATMOSPHERE:   subtle noise texture + warm gradient
OBJECTS:      photography, editorial illustration
TYPOGRAPHY:   dominant — type IS the primary visual element
INTERLEAVE:   selective — one hero moment of overlap
SCALE:        minimal perspective (editorial = flat grid + depth accent)
ACCENT:       pull quote, drop cap, color block

CSS key:
  bg: #faf8f3 (warm white)
  atmosphere: noise 0.03 opacity, very subtle
  object: integrated with text columns, not floating
```

## Modern Minimal / SaaS Depth

```
DEPTH MODE:   flat or very shallow (2 layers max)
ATMOSPHERE:   subtle elevation (box-shadow, not wash)
OBJECTS:      product UI screenshots, device mockups
TYPOGRAPHY:   primary layer — no interleave
INTERLEAVE:   no — clarity > depth for SaaS
SCALE:        device mockups: perspective transform (rotateY/X)
ACCENT:       badge, pill, status indicator

CSS key:
  bg: white / near-white
  depth via: box-shadow, border, elevation tokens
  device mockup: transform: perspective(1000px) rotateY(-15deg)
```

## Flat Mode (no depth)

```
When to use: SaaS forms, dashboards, data tables, admin panels
  Kanso applies — content is the design
  Any atmosphere = distraction
  Any object = decoration without function

Stack: canvas + UI only (2 layers)
```
