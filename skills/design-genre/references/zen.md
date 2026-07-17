# Genre: Zen / Minimalist

> Still, deliberate, unhurried — every element earns its place.

## Signal Words
```
zen, minimalist, ma, stillness, restraint, breathe, quiet, monk,
sparse, wabi-sabi, negative space, personal portfolio (senior/expert level)
```

## Voice & Copy
```
Voice:     Still, deliberate, unhurried
Copy tone: Short sentences, no filler. Specificity over warmth.
           "I build systems meant to last." NOT "passionate engineer".
           No superlatives. No buzzwords.
```

## Typography
```
Pair:      Light-weight display serif (wt 300) + Light sans (wt 300–400)
           Recommended: Fraunces 300 + Inter 300

HIERARCHY RULE: restraint = no decoration, NOT no size
  H1: weight 300 + size LARGE (clamp text-3xl → text-4xl) — dominant focal object
  H2: weight 300 + size medium (clamp text-xl → text-2xl) — subordinate
  body: weight 300–400 + size base — quiet
  ❌ weight 300 + size small → hierarchy collapses → FAIL
  ✅ weight 300 + size large → zen dominant without loudness

H1/body ratio: ≥ 3.5x (heavier fonts cap at 3.0x — not applicable here)
Leading: 1.7–1.8 · Hero bio: max 44ch
ALL-CAPS: forbidden — use letter-spacing 0.08–0.12em on labels instead
font-variation-settings: "wght" 300 — explicit for variable fonts
```

## Color
```
Dark mode primary
Bg: warm dark (#0c0b09) — NOT cold black (#000000)
Ink steps: muted / subtle / ink / bright (4 steps only)
Accent: ONE purpose-only — sage/stone for status ONLY
  sage dark:  #7a9e7a
  sage light: #4a7a4a

FORBIDDEN: amber/orange/yellow (#d97706 and variants)
border: rgba(255,255,248,0.06) — barely-there

LIGHT MODE:
  bg = pure white (#ffffff) — NOT warm ivory (Kanso: remove before adding)
  Work rows: transparent on white (no card needed)
```

## Layout — 7 Wabi-Sabi Principles Applied
```
Fukinsei (不均斉): asymmetry — 2-col about (heading left, content right)
Kanso (簡素):     simplicity — remove before adding
Seijaku (静寂):   silence — space is the divider, not lines

LINE RULE (Seijaku + oneness):
  ZERO structural borders between sections
  Borders split the page = NOT zen = FAIL
  Section separation = padding rhythm ONLY
  Exception: work-row border-top — one internal list system, not section divider
  ❌ hero border-bottom → splits identity from work
  ❌ section border-top → fragments oneness
  ✅ padding change → page breathes as one whole

VOID RULE (Ma 間 — intentional space):
  Every space needs a visual anchor
  Hero MUST have anchor below bio: contact row OR scroll cue
  Without anchor → hero reads abandoned → FAIL
  Section padding: clamp(64px,8vh,80px) consistent rhythm

Work rows:
  Dark: subtle surface bg (warm-700 #222018) — Shibui subtle lift
  Light: transparent — white page is enough
```

## Motion
```
Stance: STILLNESS
Only permitted: color-shift transition (150–200ms ease)
Reveal: fade + translateY(6–8px), max 500ms
NO: hover lift · bounce · glow · scale transforms
prefers-reduced-motion: hard gate — must be respected
```

## Macrostructures
```
Marquee Hero (zen variant), Specimen, Studio, Atelier, Lumen
```

## Nav & Footer
```
Nav:    minimal (N1a) — transparent until scrolled, bg+blur on scroll
Footer: minimal (Ft1)
```

## Slop Gates
```
❌ Amber/orange/yellow accent anywhere
❌ ALL-CAPS nav — sentence case only
❌ Hover lift or box-shadow glow on interactive elements
❌ Hero without anchor below bio
❌ Bold/700+ weight in body text
❌ Background color swap between sections (borders too)
❌ More than 1 accent color
✅ Sage/stone for single-purpose status only
✅ Dot-grid texture at opacity ≤ 0.03
✅ One strong focal object per viewport (H1)
```
