# Design Genre Definitions

> Genre = voice + color + motion stance. Not just a color palette.

---

## Genre 1: Editorial

```
Voice:     Considered, authoritative, unhurried
Copy tone: Long-form friendly, typographic emphasis, stance-driven
           "I build systems meant to last." — not "Fast. Scalable. Reliable."

Typography: High-contrast serif or grotesk display
            Headlines: large, weighted, left-aligned or centered
            Body: generous leading (1.7–1.85), comfortable measure (60–70ch)

Color:      High contrast dark/light — not necessarily black/white
            Accent: single, chromatic, used sparingly
            Paper: light (L > 85%) or dark (L < 20%) — rarely mid

Layout:     Asymmetric, typographic rhythm, generous whitespace
            Section dividers: typographic (numbers, labels) not decorative
            Images: editorial photography, full-bleed or contained

Macrostructures that fit:
  Specimen, Manifesto, Long Document, Newsprint, Almanac,
  Studio, Atelier, Editorial, Garden, Riso

Nav defaults: minimal (N1a/N1b), masthead (N6), edge-aligned (N9)
Footer defaults: statement (Ft5), minimal (Ft1)

Slop gates (strict):
  ❌ No hero with three bullet points below it
  ❌ No "Get started for free" primary CTA
  ❌ No stock photo hero (illustration or typography only)
  ❌ No gradient background on hero text
```

---

## Genre 2: Modern-Minimal

```
Voice:     Clear, confident, functional
Copy tone: Benefit-first, short sentences, no jargon to end-users
           "Ship faster." — not "Leverage our cutting-edge platform."

Typography: Grotesk or geometric sans
            Headlines: medium-large, regular or medium weight
            Body: compact leading (1.5–1.65), tighter measure (55–65ch)

Color:      Muted base, single accent (often indigo/blue/violet)
            Lots of surface — cards, dividers, subtle borders
            Dark mode common but not required

Layout:     Grid-based, structured, predictable
            Components feel like product screenshots
            Generous padding inside cards, tight between sections

Macrostructures that fit:
  Bento, Workbench, Cobalt, Coral, Terminal,
  Midnight, Sport, Marquee Hero, Aurora

Nav defaults: canonical SaaS (N1b), floating pill (N5), mega-menu (N11), inline ⌘K (N13)
Footer defaults: 4-col links (Ft3 — acceptable here), hub (Ft6)

Slop gates (strict):
  ❌ No decorative blobs or mesh gradients
  ❌ No 5+ feature cards in a grid (max 4)
  ❌ No testimonials with star ratings in hero
  ❌ No "Trusted by X companies" with logos in hero
  ✅ Screenshots/product UI in hero = encouraged
```

---

## Genre 3: Atmospheric

```
Voice:     Evocative, immersive, cinematic
Copy tone: Short, punchy, emotional resonance over information
           "Create without limits." — minimal, room to breathe

Typography: Display or editorial sans, sometimes mono accent
            Headlines: can be very large (5–8rem), light weight on dark bg
            Body: restrained, sparse — less is more

Color:      Dark-first (L < 15% base)
            Gradients: intentional, not decorative — define depth
            Accent: glowing, saturated (phosphor green, electric blue, warm amber)
            Light mode: unusual, requires explicit design intent

Layout:     Full-bleed sections, cinematic pacing
            Motion-heavy: parallax, reveal, stagger entrance
            Images/video: central, large, treated
            White space: dramatic — sections breathe

Macrostructures that fit:
  Bloom, Midnight, Terminal, Aurora, Lumen,
  Marquee Hero (dark variant), Manifesto (dark variant)

Nav defaults: floating pill (N5), scroll-morph (N10), hidden ⌘K (N4)
Footer defaults: statement (Ft5), minimal (Ft1)

Motion stance: MOTION-ON (cinematic entrances required)
  Hero entrance: stagger children — name, tagline, bio, links
  Scroll reveal: clip-reveal on section headings
  Parallax: hero eyebrow, background layer

Slop gates (strict):
  ❌ No light background on hero
  ❌ No feature grid with icons
  ❌ No testimonial section
  ❌ Motion is NOT optional in atmospheric — reduced-motion exception applies,
     but if the user has motion enabled, animate
```

---

## Genre 4: Playful

```
Voice:     Warm, encouraging, human
Copy tone: Conversational, first/second person, light humor acceptable
           "You've got this." — direct, friendly, not corporate

Typography: Rounded sans or humanist sans
            Headlines: medium-large, playful weight variation
            Body: casual leading (1.6–1.75), friendly measure

Color:      Warm or saturated palette — not monochromatic
            Multiple accent colors acceptable (but max 3, semantic roles)
            Light mode primary — dark mode needs explicit intent

Layout:     Softer edges (border-radius generous)
            Illustrations > photography
            Confetti, texture, pattern: acceptable in small doses

Macrostructures that fit:
  Hum, Carnival, Garden, Riso, Sport (light),
  Bento (playful variant)

Nav defaults: floating pill (N5), floating chip (N2), scroll-morph (N10)
Footer defaults: warm (Ft7), minimal (Ft1)

Slop gates (strict):
  ❌ No corporate language ("leverage", "enterprise-grade")
  ❌ No all-dark color palette
  ❌ No photo of a person in a suit
  ✅ Illustrations, icons, emoji: encouraged (not required)
```
