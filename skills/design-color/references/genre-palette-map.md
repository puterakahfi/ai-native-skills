# Genre → Palette Map

> Given a genre, what palette direction?
> Load genre spec first: skill_view(name='design-genre', file_path='references/<genre>.md')

## Zen / Minimalist

```
Temperature:  WARM — organic, wabi-sabi, aged paper quality
Value:        DARK primary / PURE WHITE light mode
Saturation:   S 5–15% (near-neutral warm gray)
Accent:       Sage / stone / muted earth — ONE purpose (status only)
              sage: #7a9e7a (dark) / #4a7a4a (light)
Forbidden:    Amber (#d97706), orange, yellow, cold blue, neon

Dark palette:
  bg:      #0c0b09  (hsl 38°, 8%, 6%)
  ink:     #c4c0b4  (hsl 38°, 8%, 71%)
  accent:  #7a9e7a  (sage)

Light palette:
  bg:      #ffffff  (pure white — Kanso)
  ink:     #2a2820  (hsl 38°, 12%, 15%)
  accent:  #4a7a4a  (sage dark — maintains contrast on white)
```

## Editorial

```
Temperature:  WARM or NEUTRAL — paper quality
Value:        LIGHT primary (dark valid with explicit intent)
Saturation:   S 0–20% base, accent S 40–60%
Accent:       Single chromatic — deep red, forest green, warm amber ok here

Light palette:
  bg:      #faf8f3 (warm white — paper)
  ink:     #1a1814 (warm near-black)
  accent:  one of: #8b1a1a (crimson) / #2d5a27 (forest) / #c8860a (amber)
```

## Modern Minimal (SaaS)

```
Temperature:  COOL to NEUTRAL — crisp, professional
Value:        LIGHT primary, dark popular
Saturation:   S 5–15% base, accent S 70–90%
Accent:       Indigo / blue / violet — high saturation, clear signal

Light:
  bg:      #ffffff / #f9fafb
  accent:  #6366f1 (indigo) / #3b82f6 (blue) / #8b5cf6 (violet)

Dark:
  bg:      #0f1117 (cool dark)
  accent:  #818cf8 (indigo light) / #60a5fa (blue light)
```

## Atmospheric

```
Temperature:  COOL or DRAMATIC — cinematic depth
Value:        DARK (L < 10%) — almost black
Saturation:   S 60–90% accent — glowing, neon-adjacent
Accent:       Phosphor green / electric blue / warm amber glow

Dark:
  bg:      #080810 (near black, slight cool)
  accent:  #39d353 (phosphor) / #00d4ff (electric) / #ffb347 (amber glow)
  Gradient: intentional depth — bg → slightly lighter center
```

## Playful

```
Temperature:  WARM — inviting, human
Value:        LIGHT primary
Saturation:   S 50–80% — multiple accents ok (max 3 semantic roles)
Accent:       Warm coral / teal / golden yellow

Light:
  bg:      #fffbf5 (warm white)
  accent1: #ff6b6b (coral — primary action)
  accent2: #4ecdc4 (teal — secondary)
  accent3: #ffd93d (golden — highlight)
```
