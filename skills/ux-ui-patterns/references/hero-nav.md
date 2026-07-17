# Hero Patterns + Navigation Patterns

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

## Anti-Patterns (Nav/Hero)

| Anti-Pattern | Problem | Fix |
|---|---|---|
| Hamburger on desktop | Forces extra click, hides navigation | Horizontal nav for ≥ 5 items |
| Primary nav > 6 items flat | Cognitive overload | Group into dropdowns |
| Hover-only state | Inaccessible on touch, keyboard | Add focus + active state |
| Icon-only buttons | No label = confusion | Icon + visible label or tooltip |
| Carousel auto-advance | User loses control | Manual only, or pause on hover |
| Modal on page load | Intrudes before user has context | Trigger only on explicit action |
