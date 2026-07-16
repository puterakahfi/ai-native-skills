---
name: ux-ui-patterns
description: UI/UX pattern library for making layout decisions — which hero pattern fits the goal, which card pattern fits the content, which nav pattern fits the context. Decision tree for pattern selection, not just a list of patterns.
version: 1.0.0
author: puterakahfi
license: MIT
type: skill
implements: ai-native-core/contracts/skills/experience-design/ux-ui-patterns.contract.yaml
related_skills: [master-design, ux-psychology, design-system, readability]
---

# UX/UI Patterns Skill

## Core Principle

```
A pattern is a proven solution to a recurring design problem.
The skill is choosing the RIGHT pattern for the context — not using what looks good.

Decision process:
  1. What is the user's job on this page?
  2. What is the content type and quantity?
  3. What cognitive state is the user in on arrival?
  4. → Then select the pattern that serves those three constraints
```

---

## Hero Patterns

### Pattern Selection Decision Tree

```
What is the primary goal of this page?

├── Showcase personal work/identity
│   ├── 1 clear audience → TEXT HERO
│   └── Multiple products → TEXT HERO + PRODUCT LIST
│
├── Sell a SaaS product
│   ├── Complex product → SPLIT HERO (text left, product screenshot right)
│   └── Simple product → CENTERED HERO + single CTA
│
├── Portfolio (case studies)
│   └── → GRID HERO (masonry or equal-height cards)
│
├── Blog / editorial
│   └── → FEATURED POST HERO (large image, minimal text)
│
└── Marketing / conversion
    └── → CENTERED HERO + CTA + social proof
```

### Hero Pattern Specs

**TEXT HERO** — for personal/identity pages
```
Layout:   left-aligned, 40–60% max-width for text
H1:       display size (--text-4xl desktop, --text-3xl mobile)
Stance:   specific idea, not job title
Subtitle: 1–2 sentences max, --text-lg
CTA:      0–1 (none for pure showcase)
Bg:       subtle texture/gradient — never flat
Height:   100vh — let it breathe
```

**SPLIT HERO** — for SaaS/product pages
```
Layout:   grid 1fr 1fr — text left, visual right
Text:     --text-3xl H1 max (not competing with visual)
Visual:   product screenshot, mockup, or illustration
CTA:      1 primary — prominent, above the fold
Height:   90–100vh
Mobile:   stack — visual goes below text
```

**CENTERED HERO** — for campaigns/marketing
```
Layout:   center-aligned, max-width 640px
H1:       --text-3xl to --text-4xl, centered
CTA:      1–2 buttons (primary + secondary ghost)
Subtext:  --text-lg centered
Height:   80–100vh
Best for: conversion-focused, single product
```

**GRID HERO** — for portfolios
```
Layout:   masonry or equal-height grid
Cards:    thumbnail + title + category + year
No H1 above fold — let the work speak
CTA:      none or "see all work" at bottom
Height:   auto — scroll to explore
```

---

## Navigation Patterns

### Nav Pattern Selection

```
Content volume + user type → nav pattern:

Personal page (3–5 links)   → HORIZONTAL TOP NAV (simple, minimal)
Product app (<8 links)      → HORIZONTAL TOP NAV + dropdown
Product app (8–15 links)    → SIDEBAR NAV
Product app (15+ links)     → SIDEBAR NAV + sections/groups
Mobile always               → HAMBURGER or BOTTOM TAB BAR
Dashboard                   → SIDEBAR NAV (always visible, 240–280px)
```

### Nav Pattern Specs

**HORIZONTAL TOP NAV** — personal/marketing
```
Height:          48–64px
Items:           3–6 max (no cognitive overload)
Logo:            left, links right or centered
Active state:    underline or color change — never background box on personal pages
Sticky:          yes, with backdrop-filter: blur
Mobile:          hamburger at ≤ 768px

Anti-patterns:
  ❌ More than 6 items — use dropdown grouping
  ❌ ALL CAPS for nav that has more than 5 items — too shouty
  ❌ Active state = bold only — insufficient signal for a11y
```

**SIDEBAR NAV** — app/dashboard
```
Width:           240–280px (collapsed: 48–64px icon-only)
Items:           icon + label, grouped by function
Active:          background highlight, left border accent
Collapse:        optional on desktop, required on mobile
Sections:        group with headers if > 8 items
```

---

## Card Patterns

### Card Type Selection

```
Content type → card pattern:

Product/project showcase   → FEATURE CARD
Blog post list             → EDITORIAL CARD
Team/person                → PROFILE CARD
Metric/stat                → STAT CARD
Tool/service comparison    → COMPARISON CARD
Process/timeline           → TIMELINE CARD
```

### Card Pattern Specs

**FEATURE CARD** — products, projects
```
Structure:
  [status badge — LIVE/DEV]
  [title — --text-xl]
  [description — --text-base, max 2–3 lines]
  [tags/tech stack]
  [arrow or link indicator]

Width:   full-width stacked (1–2 items) OR equal-height grid (3+)
Hover:   background lightens, arrow animates
Click:   entire card is clickable (not just title)
```

**EDITORIAL CARD** — blog, articles
```
Structure:
  [cover image — 16:9]
  [category + date]
  [title — --text-xl, max 2 lines]
  [excerpt — --text-base, max 3 lines]
  [author + read time]

Grid:    2-col desktop, 1-col mobile
Image:   required — text-only editorial cards feel unfinished
```

**STAT CARD** — metrics, numbers
```
Structure:
  [label — --text-sm, muted]
  [value — --text-3xl, bold]
  [delta — +/- change, colored]

Grid:    3–4 col desktop, 2-col mobile, 1-col phone
Minimal: no border-radius on stat cards — sharp = precision
```

---

## Layout Grid Patterns

### Grid Selection Rule

```
Content count → grid choice:

1 item          → full-width (100%)
2 items         → stacked (1 col) OR side-by-side (2 col if ≥ 600px width)
3 items         → 3-col grid
4 items         → 2x2 grid OR 4-col
5 items         → 2+3 split OR masonry
6+ items        → equal grid, 2–4 col depending on card width

WARNING — 2 items in 4-col grid = FAIL (looks broken, not minimal)
```

### Responsive Grid Breakpoints

```css
/* Mobile first — add columns as screen grows */

.grid {
  display: grid;
  gap: var(--space-4);
  grid-template-columns: 1fr;                          /* mobile: 1 col */
}

@media (min-width: 640px) {
  .grid { grid-template-columns: repeat(2, 1fr); }    /* tablet: 2 col */
}

@media (min-width: 960px) {
  .grid { grid-template-columns: repeat(3, 1fr); }    /* desktop: 3 col */
}

/* For stacked (intentional 1-col):
   No breakpoints needed — stays 1 col but wider */
.grid-stacked {
  display: flex;
  flex-direction: column;
  gap: 1px; /* hairline separator between cards */
  background: var(--border); /* gap shows as divider */
}
```

---

## Section Patterns

### Section Flow for Personal Pages

```
Optimal flow (proven by eye-tracking studies):

  1. HERO          → who are you + stance (100vh)
  2. WORK          → what have you built (LIVE only)
  3. ABOUT         → who you are in depth
  4. CONTACT        → how to reach you

  Between each: visual break (alternating bg, border, or space)
  Each section: different padding weight (hero > content > contact)
```

### Section Break Patterns

```
Option A: Alternating background
  Hero:    --bg
  Work:    --bg-alt (subtle difference)
  About:   --bg
  Contact: --bg-alt (or --bg with top border)

Option B: Border separators only
  All sections: same --bg
  Separated by: border-top: 1px solid var(--border)

Option C: Whitespace only
  All sections: same --bg
  Separated by: larger padding (--space-11 between sections)

Choose ONE and apply consistently.
```

---

## Form Patterns

### Input Field Spec

```
Height:      40–48px (desktop), 48–56px (mobile — Fitts's Law)
Padding:     12–16px horizontal
Border:      1px solid var(--border) → focus: var(--accent)
Label:       above input (never placeholder-only — a11y fail)
Error:       below input, var(--danger), icon + text
Required:    asterisk next to label, explain in form description

Anti-patterns:
  ❌ Placeholder as label — disappears on focus, a11y fail
  ❌ Input height < 44px — touch target too small
  ❌ Error only on submit — validate on blur
```

---

## State Patterns

Every interactive component needs ALL states designed:

```
States required for every interactive element:
  Default   → what it looks like normally
  Hover     → subtle feedback (background, color change)
  Focus     → visible outline for keyboard nav (2px, offset)
  Active    → pressed/clicked state
  Disabled  → opacity 0.4, cursor not-allowed, no interaction
  Loading   → skeleton or spinner in-place
  Error     → red border + message
  Success   → green confirmation

Missing ANY state = incomplete design.
Common mistake: design default + hover, ship without focus/error/loading.
```

---

## Anti-Pattern Catalog

| Anti-Pattern | Problem | Fix |
|---|---|---|
| Hamburger on desktop | Forces extra click, hides navigation | Horizontal nav for ≥ 5 items |
| Card grid with 2 items in 4 cols | Looks broken/unfinished | Stack or use 2-col |
| Infinite scroll on portfolio | User loses position | Paginate or load-more button |
| Full-width text lines | > 75 chars = hard to track | max-width: 65ch on prose |
| Primary nav > 6 items flat | Cognitive overload | Group into dropdowns |
| Hover-only state | Inaccessible on touch, keyboard | Add focus + active state |
| Icon-only buttons | No label = confusion | Icon + visible label or tooltip |
| Carousel auto-advance | User loses control | Manual only, or pause on hover |
| Modal on page load | Intrudes before user has context | Trigger only on explicit action |
| Nested cards (card in card) | Visual confusion, unclear clickable area | Flatten or use different component |
