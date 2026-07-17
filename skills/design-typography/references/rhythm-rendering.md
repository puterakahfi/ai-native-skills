# Rhythm, Spacing & Rendering

> Rhythm is the heartbeat of typography — consistent vertical cadence.

## Line Height (Leading)

```
Context               line-height    Why
Display / H1          1.0 – 1.15     Headlines are read in one glance
H2 / H3               1.15 – 1.35    Multi-line headings need tighter space
Body prose            1.6 – 1.8      Eye travels back to start of line
UI labels / captions  1.2 – 1.4      Compact, functional
Dense data            1.4 – 1.5      Readable but tight

Rule: larger text = tighter leading. Smaller text = looser leading.
```

## Letter Spacing (Tracking)

```
Context               letter-spacing    Why
Display (large)       -0.01 – -0.03em  Tight — large glyphs need optical correction
Body prose            0em              Never track body text (kills readability)
ALL-CAPS labels       0.06 – 0.12em    Track caps — narrow letterforms need space
Small UI labels       0.02 – 0.05em    Slight open for legibility at small size
Eyebrow / meta text   0.08 – 0.14em    Tracked caps = premium feel
```

## Paragraph Spacing

```
paragraph margin-bottom: 1em – 1.5em   (same as line-height or 1.5× it)
section gap:             clamp(64px, 8vh, 96px) — consistent rhythm between sections
heading margin-bottom:   0.4em – 0.6em (tighter than paragraph)
heading margin-top:      1.5em – 2em   (more space before = new section signal)
```

## Font Rendering

```css
/* Always apply on body — prevents subpixel aliasing on dark bg */
body {
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}

/* Variable font weight control */
.hero-name {
  font-weight: 300;
  font-variation-settings: "wght" 300;  /* explicit — browsers sometimes snap to 400 */
}

/* Optical sizing (where supported) */
h1 { font-optical-sizing: auto; }
```

## Rendering Anti-Patterns

```
❌ No antialiasing on dark bg → text looks bold/blurry
❌ font-weight: 300 without font-variation-settings → snaps to 400
❌ letter-spacing on body text → destroys readability
❌ Tight leading on body (< 1.5) → eye loses line, fatigue
❌ Paragraph spacing = 0 → walls of text → abandon
✅ antialiased + variation-settings = what you designed, rendered faithfully
```
