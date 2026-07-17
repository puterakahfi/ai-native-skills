# Other Macrostructures — 01 + 03–21

Full detail for all macrostructures except 02 Marquee Hero (see references/marquee-hero.md).

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
Layout lead:    image-led, left-aligned, split 50/50
Heading:        Left, stacked — name then descriptor
Body:           Project list — cards on right panel, identity on left
Dividers:       Minimal — 1px border between left/right panels, between cards
Button voice:   Arrow links (↗), not buttons
Image:          Central — full-width project screenshots or photos
Reveal:         Stagger left sequence first, then right cards

When to use:    Portfolio, personal page, creative studio, photographer
When NOT:       Text-heavy content, SaaS product, personal blog
```

### Studio split-panel layout rules (MANDATORY)

Failing to follow these causes gray void and broken balance — most common Studio bug.

```
Hero wrapper (outer):
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  padding-top: 80px;            ← nav clearance here ONCE — not inside panels

Hero grid:
  flex: 1;                      ← fills remaining height (100vh - 80px)
  display: grid;
  grid-template-columns: 1fr 1fr;
  align-items: stretch;

Left panel:
  display: flex; flex-direction: column; justify-content: center;
  border-right: 1px solid var(--border);
  padding: var(--sp-9) var(--sp-8);
  /* equal top/bottom padding → justify-content:center works correctly */
  /* DO NOT add extra top padding here — it shifts center down */

Right panel (work list):
  display: flex; flex-direction: column;
  gap: 1px;
  background: var(--border);
  padding: 0;
  /* no padding-top — wrapper already handles nav clearance */

Section label inside right panel:
  padding: var(--sp-6) var(--sp-6) var(--sp-5);
  background: var(--bg-alt);

Project cards:
  flex: 1;                      ← fills remaining height equally
  padding: var(--sp-8) var(--sp-6);
  background: var(--bg-alt);
  /* card content won't fill full card height — that's expected, bg color fills it */
```

**Why nav clearance belongs on wrapper, not panels:**
- Clearance inside left panel only → asymmetric padding → justify-content:center shifts down
- Clearance inside right panel only → label not aligned with left content
- Clearance on wrapper → both panels start at same baseline, left content truly centered

**Why void inside cards is acceptable:**
- `flex: 1` = equal height distribution, not content-fill
- Cards taller than content → bottom of card has breathing room
- Gate check: verify card background fills (no raw html background showing), not that content fills

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

**Exception:** If brief clearly signals a specific macrostructure, brief-match beats diversification.

---

## State Your Pick (full template)

Before writing any code, emit:

```
Macrostructure: [name]
Genre: [genre]
Layout lead: [type-led | image-led | grid-led | document-led]
Heading: [left | center | asymmetric]
Differs from last on: [axes] | First build — no constraint
Brief signal: [what in the brief drove this pick]
```
