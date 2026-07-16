---
name: macrostructures
description: 21 named page shapes — each bundles heading placement, body composition, divider language, button voice, image treatment, and reveal into a single named choice. Pick ONE before designing. Prevents structural sameness across consecutive outputs. Adapted from Hallmark (Nutlope) for ai-native-skills ecosystem.
version: 1.0.0
author: puterakahfi
license: MIT
type: skill
implements: ai-native-core/contracts/skills/experience-design/macrostructures.contract.yaml
related_skills: [design-genre, ux-ui-patterns, master-design, redesign-workflow]
---

# Macrostructures Skill

## Core Principle

```
Pick ONE macrostructure BEFORE designing anything.
A macrostructure is a complete page shape — not a component, not a layout grid.
It bundles: heading placement + body composition + divider language +
            button voice + image treatment + reveal

Picking one named macrostructure = making 6 decisions at once.
It also prevents agent default-attractor sameness (always generating
the same hero → 3-feature → CTA → footer pattern).

Diversification rule (mandatory):
  Before picking: check if this project/session already used a macrostructure.
  If yes: pick a DIFFERENT one that differs on ≥ 2 of these axes:
    - Layout lead (type-led | image-led | grid-led | document-led)
    - Heading placement (left | center | asymmetric | inline)
    - Divider language (typographic | geometric | none | decorative)
```

---

## Macrostructure Index

Pick one. Then read only that section below.

| # | Name | Layout Lead | Heading | Best for |
|---|---|---|---|---|
| 01 | **Specimen** | type-led | asymmetric | Editorial, foundry, portfolio |
| 02 | **Marquee Hero** | image-led | center | Landing, campaign, atmospheric |
| 03 | **Bento** | grid-led | left | SaaS features, product overview |
| 04 | **Long Document** | document-led | left | Docs, essays, technical writing |
| 05 | **Workbench** | grid-led | left | Developer tools, dashboards |
| 06 | **Manifesto** | type-led | center | Brands, bold statements |
| 07 | **Studio** | image-led | left | Agency, creative work showcase |
| 08 | **Newsprint** | document-led | asymmetric | Publication, blog, magazine |
| 09 | **Almanac** | document-led | left | Reference, index, directory |
| 10 | **Garden** | image-led | center | Nature, lifestyle, warm brands |
| 11 | **Riso** | grid-led | center | Playful, zine, print-inspired |
| 12 | **Sport** | image-led | left | Bold, kinetic, product launch |
| 13 | **Bloom** | image-led | center | Atmospheric, generative, dark |
| 14 | **Coral** | grid-led | left | Consumer SaaS, mobile-forward |
| 15 | **Cobalt** | grid-led | left | B2B SaaS, platform, API |
| 16 | **Aurora** | image-led | center | AI product, creative tool |
| 17 | **Atelier** | type-led | left | Luxury, fashion, high-end |
| 18 | **Carnival** | grid-led | center | Playful, consumer, event |
| 19 | **Lumen** | type-led | left | Classical, elegant, upright |
| 20 | **Hum** | grid-led | left | Warm, rounded, friendly SaaS |
| 21 | **Terminal** | document-led | left | Dev tool, CLI, technical dark |

---

## 01 · Specimen

```
Layout lead:    type-led, asymmetric
Heading:        Large numbered labels in left margin, huge serif headline spans right
Body:           Long-form justified or left-aligned, wide measure acceptable
Dividers:       Typographic — numbered sections, horizontal rules at section breaks
Button voice:   Underline link style, not filled buttons
Image:          Contained, captioned, editorial — never background
Reveal:         Clip-reveal on headings, stagger body paragraphs

When to use:    Editorial portfolio, type foundry, publication, case study
When NOT:       SaaS product, consumer app, anything that needs a CTA

Example structure:
  01  ←label    Large Heading
                Subtitle or stance
                ─────────────────────────────
                Body text body text body text...
  02  ←label    Second section heading
```

---

## 02 · Marquee Hero

```
Layout lead:    image-led (or full-bleed video/color)
Heading:        Centered, very large, 100vh section
Body:           Brief — 1–2 sentences below headline
Dividers:       Section breaks via background color change
Button voice:   Ghost or outline on dark, solid on light
Image:          Full-bleed background, or large centered image below headline
Reveal:         Hero entrance stagger (cinematic), scroll reveal below

When to use:    Campaign landing, atmospheric brand, product launch, personal landing
When NOT:       Documentation, complex product with many features

Example structure:
  ┌──────────────────────────────────┐
  │  [full-bleed bg image/color]     │  100vh
  │         Very Large Heading       │
  │       Subtitle one sentence      │
  │          [ghost button]          │
  └──────────────────────────────────┘
  [content sections below]
```

---

## 03 · Bento

```
Layout lead:    grid-led
Heading:        Left-aligned, above the grid
Body:           Inside cells — short labels + one sentence per cell
Dividers:       Grid gaps + card borders, no additional dividers
Button voice:   Small, inside cards or below grid
Image:          Inside cells, screenshots or icons
Reveal:         Stagger grid cells on scroll

When to use:    Feature overview, SaaS product page, "what we do" section
When NOT:       Long-form content, personal page, documentary tone

Example structure:
  Features heading
  ┌──────┬──────┬──────┐
  │      │      │      │  2×3 or 3×2 grid
  │      │      │      │
  └──────┴──────┴──────┘
  ┌────────────┬──────┐
  │ wide cell  │      │  varied widths
  └────────────┴──────┘
```

---

## 04 · Long Document

```
Layout lead:    document-led, single column
Heading:        Left-aligned H1, then H2/H3 inline
Body:           Long-form, wide measure (65–80ch), generous leading
Dividers:       Horizontal rules, or just whitespace rhythm
Button voice:   Inline links, minimal CTAs at end
Image:          Inline, full-width breakout acceptable
Reveal:         None or minimal — document flow is the UX

When to use:    Blog post, essay, documentation, case study detail
When NOT:       Landing page, product overview, anything needing conversion
```

---

## 05 · Workbench

```
Layout lead:    grid-led, data-heavy
Heading:        Left-aligned, compact — this is a functional UI
Body:           Tables, code blocks, lists, dense information
Dividers:       Subtle — thin borders, background color shifts
Button voice:   Small, labeled, icon+text
Image:          Screenshots, diagrams, never decorative
Reveal:         None — functional UIs don't animate in

When to use:    Developer tool, API docs, dashboard, CLI documentation
When NOT:       Marketing page, personal portfolio, anything emotional
```

---

## 06 · Manifesto

```
Layout lead:    type-led, centered
Heading:        Very large centered text, bold stance statements
Body:           Short, punchy — one idea per paragraph
Dividers:       Full-width color band between sections
Button voice:   Bold, centered, large
Image:          Rare — let type carry the page
Reveal:         Word-by-word text split on scroll, section wipe

When to use:    Brand statement page, "about us" with strong POV, values page
When NOT:       Product feature page, documentation, e-commerce

Example:
  We don't build fast.
  We build right.
  
  Software is philosophy
  made executable.
```

---

## 07 · Studio

```
Layout lead:    image-led, left-aligned
Heading:        Left, stacked — name then descriptor
Body:           Project grid — large images with hover overlay
Dividers:       Minimal — images carry the visual weight
Button voice:   Arrow links ("View project →"), not buttons
Image:          Central — full-width project screenshots or photos
Reveal:         Stagger project cards on scroll

When to use:    Agency portfolio, creative studio, photographer, designer
When NOT:       Text-heavy content, SaaS product, personal blog
```

---

## 08 · Newsprint

```
Layout lead:    document-led, multi-column
Heading:        Asymmetric — large left, small right column
Body:           Multi-column text layout (2–3 cols on desktop)
Dividers:       Thin rules, section numbers, typographic
Button voice:   Inline text links, no filled buttons
Image:          Full-width breakout or column-spanning
Reveal:         Stagger columns on scroll

When to use:    Magazine, publication, news, editorial blog
When NOT:       SaaS, app, product that needs clear CTAs
```

---

## 09 · Almanac

```
Layout lead:    document-led, index/reference
Heading:        Left-aligned, alphabetical or categorical sections
Body:           Dense list format — definition + description pairs
Dividers:       Letter separators (A—B—C), thin rules
Button voice:   None or very minimal — this is reference material
Image:          None or small thumbnails only
Reveal:         None — reference is scanned not read linearly

When to use:    Glossary, directory, index, reference documentation
When NOT:       Any page that needs to persuade or convert
```

---

## 10–21 · Remaining Macrostructures (Slim)

**10 · Garden** — Warm, organic grid. Nature/lifestyle imagery. Rounded cards, warm palette. Stagger reveal.

**11 · Riso** — Bold overlapping colors (risograph print effect). Angled layouts, loud typography. Playful, zine aesthetic.

**12 · Sport** — Kinetic, bold. Full-bleed number/stat hero. Left-aligned, roman display type. No italic. Strong horizontal motion.

**13 · Bloom** — Dark atmospheric. Large imagery with color overlays. Minimal text, evocative. Cinematic entrance required.

**14 · Coral** — Consumer SaaS. Friendly, rounded. Mobile screenshot hero. Warm neutrals + single accent. Scroll stagger on features.

**15 · Cobalt** — B2B SaaS. Space Grotesk + mono pairing. Code-adjacent. Dark base + cobalt accent. Product screenshot grid.

**16 · Aurora** — AI/creative tool. Dark, gradient backgrounds (aurora borealis colors). Generative imagery. Bold display font.

**17 · Atelier** — Luxury, high-end. Lots of whitespace. Small text, large images. No rounded corners. Precise, deliberate.

**18 · Carnival** — Maximalist playful. Multiple colors, large rounded shapes, illustrated characters. Consumer celebration.

**19 · Lumen** — Classical serif (Instrument Serif). Upright, no italic. Elegant. Verb landmarks via accent + underline.

**20 · Hum** — Plus Jakarta Sans. Rounded, warm, humanist. Friendly SaaS. Soft shadows, pastel accents. Welcoming.

**21 · Terminal** — Monospace everything. Dark bg, phosphor-green or amber accent. CLI aesthetic. Dense, technical.

---

## Diversification Rule — Enforced

Before picking, state out loud:

```
Previous macrostructure: [name | none]
Previous theme: [name | none]
This pick: [name]
Differs on: [list axes that differ]
```

If previous and current share ≥ 2 of these axes — pick again:
- Layout lead (type-led | image-led | grid-led | document-led)
- Heading placement (left | center | asymmetric | inline)
- Divider language (typographic | geometric | none | decorative)
- Dark/light base (dark | light | mid)

---

## State Your Pick

Before writing any code, emit:

```
Macrostructure: [name]
Genre: [genre]
Layout lead: [type-led | image-led | grid-led | document-led]
Heading: [left | center | asymmetric]
Differs from last on: [axes] | First build — no constraint
```
