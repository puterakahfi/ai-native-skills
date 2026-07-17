# Genre → Typeface Map

> Quick reference: given a genre, which typefaces fit?
> Always load the genre spec first: skill_view(name='design-genre', file_path='references/<genre>.md')

## Genre Typeface Catalog

### Zen / Minimalist
```
Display:  Fraunces 300 (warm humanist serif — restrained elegance)
Body:     Inter 300–400 (neutral, clean)
Mono:     JetBrains Mono (if needed — code only)
Scale:    1.333 – 1.500 (Perfect Fourth or Perfect Fifth)
Weight:   300 across the board — size carries hierarchy, not weight
Avoid:    Geometric sans display (too cold), heavy weights (not zen)
```

### Editorial
```
Display:  Fraunces / Playfair Display / Instrument Serif / Cormorant
Body:     Inter / Lato / Source Serif Pro / Libre Baskerville
Scale:    1.333 Perfect Fourth
Weight:   Display 600–800 / Body 400
Avoid:    Rounded humanist sans (too casual for editorial voice)
```

### Modern Minimal (SaaS)
```
Display:  Space Grotesk / DM Sans / Geist Sans / Syne
Body:     Inter / DM Sans / System UI stack
Scale:    1.250 Major Third (tighter — product density)
Weight:   Display 500–700 / Body 400
Avoid:    Serif display (too editorial, loses SaaS crispness)
```

### Atmospheric
```
Display:  Anything large + wt 200–300 on dark bg (thin = cinematic)
          Options: Fraunces, Outfit, Cabinet Grotesk
Body:     Inter wt 300 — almost invisible, sparse
Scale:    1.414 Augmented Fourth (drama)
Weight:   Display 200–300 / Body 300
Avoid:    Heavy weights in display (kills atmospheric delicacy)
```

### Playful
```
Display:  Plus Jakarta Sans / Nunito / Quicksand / Poppins
Body:     Plus Jakarta Sans / Nunito (same family or close sibling)
Scale:    1.333 Perfect Fourth
Weight:   Display 700–800 / Body 400–500
Avoid:    Serifs (too formal), mono (too technical)
```

## Fallback Stack Pattern

```css
/* Always include system fallbacks */
--font-display: 'Fraunces', Georgia, 'Times New Roman', serif;
--font-sans:    'Inter', system-ui, -apple-system, BlinkMacSystemFont, sans-serif;
--font-mono:    'JetBrains Mono', 'Fira Code', 'Courier New', monospace;
```

## Google Fonts Import Pattern

```html
<!-- Fraunces variable + Inter variable — preconnect first -->
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,100..900;1,9..144,100..900&family=Inter:wght@300;400;500&display=swap" rel="stylesheet">
```
