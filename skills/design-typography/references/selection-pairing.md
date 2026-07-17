# Typeface Selection & Pairing

> Genre governs personality — load design-genre before this file.

## Typeface Personality Spectrum

```
HUMANIST ←────────────────────────────→ GEOMETRIC
warm, organic, editorial              cold, precise, modern
  Fraunces, Lora, Playfair              Inter, DM Sans, Space Grotesk

SERIF ←────────────────────────────────→ SANS-SERIF
authoritative, classical, editorial    clean, neutral, functional
  Fraunces, Instrument Serif            Inter, Plus Jakarta Sans

VARIABLE ←─────────────────────────────→ STATIC
flexible weight range (300–900)        fixed weights only
  Fraunces VF, Inter VF                 many display fonts
```

## Pairing Rules

```
RULE 1 — Contrast over harmony
  Good pair = different categories (serif display + sans body)
  Bad pair  = two serifs, two grotesks — too similar, no contrast

RULE 2 — One display, one workhorse
  Display: personality, large sizes, headlines only
  Workhorse: neutral, body text, UI labels, small sizes

RULE 3 — Max 2 typefaces per page
  Exception: mono accent (code, labels) = 3rd allowed

RULE 4 — Variable fonts preferred
  font-variation-settings: "wght" 300 — fine-grained control
  Reduces HTTP requests, enables weight animation
```

## Proven Pairs by Genre

```
ZEN/MINIMALIST:
  Display: Fraunces (wt 300, light — warm humanist serif)
  Body:    Inter (wt 300-400 — clean, neutral)
  Why:     warmth of Fraunces + clarity of Inter = restrained elegance

EDITORIAL:
  Display: Fraunces / Playfair Display / Instrument Serif
  Body:    Inter / Lato / Source Serif Pro
  Why:     authoritative display + readable body

MODERN MINIMAL:
  Display: Space Grotesk / DM Sans / Geist
  Body:    Inter / DM Sans / System UI
  Why:     geometric precision + clean neutrality

ATMOSPHERIC:
  Display: Anything large + light weight on dark bg
  Body:    Inter or minimal sans — body is sparse
  Why:     display dominates, body is almost invisible

PLAYFUL:
  Display: Plus Jakarta Sans / Nunito / Quicksand
  Body:    Plus Jakarta Sans / Nunito
  Why:     rounded, friendly, same family or close siblings
```

## Google Fonts Recommendations (free, reliable)

```
Humanist serif display: Fraunces (variable, 100–900)
Classical serif:        Instrument Serif, Lora, Playfair Display
Geometric sans:         Space Grotesk, DM Sans
Humanist sans:          Plus Jakarta Sans, Nunito
Neutral workhorse:      Inter (variable), Source Sans 3
Mono accent:            JetBrains Mono, Fira Code, IBM Plex Mono
```
