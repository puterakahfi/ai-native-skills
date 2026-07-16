---
name: responsiveness
description: Responsive design strategy — breakpoint system, fluid grid, fluid typography, touch targets, viewport adaptation, and performance. Scores responsiveness 0–10 per dimension. Minimum score 8 required to pass.
version: 1.0.0
author: puterakahfi
license: MIT
type: skill
implements: ai-native-core/contracts/skills/experience-design/responsiveness.contract.yaml
related_skills: [design-system, ux-ui-patterns, accessibility, readability]
---

# Responsiveness Skill

## Core Principle

```
Responsive design is not "make it work on mobile."
It is designing for every viewport as a first-class experience.

Mobile first:
  Start with the smallest viewport.
  Add complexity as viewport grows.
  Never subtract from desktop to make mobile.

Three layers:
  1. Fluid grid   — layout adapts
  2. Fluid type   — text scales
  3. Fluid space  — spacing scales

All three must work together.
```

---

## Wide & Ultrawide Breakpoints

Most skills only define mobile (≤768px) and desktop (≥1024px). This is insufficient.
Wide (1440px+) and ultrawide (1920px+) have distinct failure modes.

```
Breakpoint map (complete):
  xs:    ≤ 480px   — single column, stacked everything
  sm:    ≤ 768px   — mobile — hamburger nav, 1-col layout
  md:    ≤ 1024px  — tablet — optional 2-col
  lg:    ≤ 1280px  — desktop standard — full layout
  xl:    ≤ 1440px  — wide — content must be constrained
  2xl:   > 1440px  — ultrawide — max-width cap mandatory

Wide/ultrawide failure modes:
  □ Content stretches edge-to-edge → line length unreadable (>90 CPL)
  □ Hero void grows with viewport height → name pushed below 50%
  □ Grid columns too wide → visual relationships break
  □ Text too small relative to canvas → feels "lost"
```

### Max-width Container (MANDATORY for all layouts)

```css
/* Every page must have a max-width container */
.container {
  width: 100%;
  max-width: 1280px;   /* standard — comfortable at 1440px */
  margin: 0 auto;
  padding: 0 var(--sp-8);
}

/* For full-bleed sections (hero, dividers): constrain content inside, not wrapper */
.hero-content {
  max-width: 1280px;
  margin: 0 auto;
  width: 100%;
}

/* Nav: constrain inner content */
nav .nav-inner {
  max-width: 1280px;
  margin: 0 auto;
  padding: 0 var(--sp-8);
  width: 100%;
}
```

### Hero Void on Wide Screens

```
Problem: justify-content:center + min-height:100vh + padding-top:80px
  At 768px viewport height: name at ~40% → good
  At 1080px viewport height: name at ~45% → borderline
  At 1440px viewport height: name at ~52% → below optical center → void visible

Fix: clamp padding-top to scale with viewport, OR use grid approach:

/* Option A: padding-top scales with viewport */
.hero {
  padding-top: clamp(80px, 8vh, 120px);  /* 80px min, 8vh at 1000px, 120px max */
  padding-bottom: clamp(var(--sp-9), 10vh, 160px);
}

/* Option B: grid rows — most robust across all heights */
.hero {
  min-height: 100vh;
  display: grid;
  grid-template-rows: 80px 1fr auto var(--sp-9);
  /*                  nav  ↑   content  ↓      */
  padding: 0 var(--sp-8);
}
.hero-content { align-self: center; }  /* true center of remaining space */
```

### Common Violations at Wide Breakpoints

```
□ Nav items spread too far apart — add max-width to nav inner
□ Work rows full-width at 1440px → index number and arrow too far apart
□ About grid 50/50 at 1440px → left column too wide → heading unreadable
□ Contact section: heading and links at opposite ends of 1440px viewport → weird
```



### Standard Breakpoints

```css
/* Mobile first — min-width queries only */

/* Default (no query) = mobile: 0–639px */

@media (min-width: 640px)  { /* sm: tablet portrait */ }
@media (min-width: 768px)  { /* md: tablet landscape */ }
@media (min-width: 1024px) { /* lg: desktop */ }
@media (min-width: 1280px) { /* xl: large desktop */ }
@media (min-width: 1536px) { /* 2xl: wide desktop */ }
```

### When to Add a Breakpoint

```
Rule: add a breakpoint when the content breaks — not at arbitrary sizes.

Signs content is breaking:
  - Text overflows its container
  - Two columns don't fit without awkward wrapping
  - Touch targets become too small
  - Spacing feels wrong (too much or too little)

Do NOT add breakpoints to match device sizes.
Add breakpoints where the design breaks.
```

---

## Fluid Grid

### Grid Progression (mobile first)

```css
.container {
  width: 100%;
  max-width: var(--container-lg);  /* 960px */
  margin: 0 auto;
  padding: 0 var(--space-5);       /* 24px mobile */
}

@media (min-width: 640px) {
  .container { padding: 0 var(--space-6); }   /* 32px tablet */
}

@media (min-width: 1024px) {
  .container { padding: 0 var(--space-8); }   /* 64px desktop */
}
```

### Grid Column Decisions

```
Content type         Mobile    Tablet    Desktop
──────────────────────────────────────────────────
Hero text            1 col     1 col     1 col (left 60%)
Product cards        1 col     2 col     stacked or 2 col
About (text+meta)    1 col     1 col     2 col (1.4fr + 1fr)
Blog grid            1 col     2 col     3 col
Stats                1 col     2 col     4 col
Team members         1 col     2 col     3 col
Nav links            hidden    hidden    visible (hamburger on mobile/tablet)
```

### Auto-Responsive Grid (no breakpoints)

```css
/* Self-healing grid — wraps based on min-width */
.grid-auto {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
  gap: var(--space-4);
}

/* Use when: unknown number of items, all equal size */
/* Do NOT use when: specific column ratios required */
```

---

## Fluid Typography

### clamp() — Fluid Type Scale

Type scales smoothly between min (mobile) and max (desktop) viewports.

```css
:root {
  /* Formula: clamp(min, preferred, max) */
  /* preferred = viewport-relative size that hits target at target viewport */

  --text-xs:   clamp(0.5rem,   0.45rem + 0.25vw,  0.563rem);
  --text-sm:   clamp(0.688rem, 0.65rem  + 0.2vw,   0.75rem);
  --text-base: clamp(0.938rem, 0.875rem + 0.33vw,  1rem);
  --text-lg:   clamp(1.125rem, 1rem     + 0.65vw,  1.333rem);
  --text-xl:   clamp(1.25rem,  1.1rem   + 0.75vw,  1.777rem);
  --text-2xl:  clamp(1.5rem,   1.2rem   + 1.5vw,   2.369rem);
  --text-3xl:  clamp(1.875rem, 1.5rem   + 2vw,     3.157rem);
  --text-4xl:  clamp(2.25rem,  1.75rem  + 2.5vw,   4.209rem);
}
```

### H1/Body Ratio Gate (mobile)

```
At mobile viewport (375px):
  H1 computed size / body computed size ≤ 3.5x

If clamp() makes H1 too large on mobile → cap H1 at --text-3xl on mobile:

@media (max-width: 640px) {
  h1.hero { font-size: var(--text-3xl); }
}
```

---

## Touch Targets

**WCAG 2.5.5 (Level AAA) — minimum 44×44px**
**Apple HIG — minimum 44pt**
**Material Design — minimum 48dp**

```
All interactive elements on mobile must be ≥ 44×44px.
This includes: buttons, links, nav items, checkboxes, radio buttons, tags.

Common failures:
  ❌ Nav links with font-size: 0.7rem and no padding → 20px touch target
  ❌ Icon buttons with only the icon size as target → 16×16px
  ❌ Tag chips with 2px vertical padding → 24px touch target
```

**Touch target fix patterns:**

```css
/* Small visual, large touch target */
.tag {
  font-size: var(--text-xs);
  padding: var(--space-2) var(--space-3);   /* minimum vertical: 8px */
  min-height: 32px;                          /* acceptable for non-primary actions */
}

/* Primary actions — full 44px */
.nav-link {
  display: flex;
  align-items: center;
  min-height: 44px;
  padding: 0 var(--space-4);
}

/* Icon buttons — expand hit area without changing visual */
.icon-btn {
  display: flex;
  align-items: center;
  justify-content: center;
  min-width: 44px;
  min-height: 44px;
}
```

---

## Viewport Adaptation Checklist

### Navigation

```
Mobile (< 768px):
  □ Hamburger menu OR bottom tab bar
  □ Full-screen overlay or slide-in drawer
  □ Close button visible
  □ Tap outside to close

Tablet (768–1024px):
  □ Decide: show desktop nav OR keep mobile nav
  □ If desktop nav: verify items still fit (no overflow)

Desktop (≥ 1024px):
  □ Full horizontal nav visible
  □ Hamburger gone
  □ Active state visible
```

### Hero

```
Mobile:
  □ H1 font-size ≤ --text-3xl (50px)
  □ H1 max 3–4 words per line
  □ Subtitle max-width: 90% (not full bleed)
  □ If SPLIT HERO: visual below text, not beside

Tablet:
  □ H1 between mobile and desktop size
  □ Split hero: evaluate if side-by-side fits

Desktop:
  □ Full H1 scale
  □ Text max-width: 60% for split hero
  □ Visual complements, doesn't overpower text
```

### Product Cards

```
Mobile:
  □ 1 column, full width
  □ Card padding: --space-5 to --space-6

Tablet:
  □ 2 column if cards ≥ 3, else 1 column
  □ Card heights equal (use align-items: stretch)

Desktop:
  □ Layout from ux-ui-patterns grid decision (count-based)
  □ Hover states work (not just click)
```

### Images

```css
img {
  max-width: 100%;
  height: auto;
  display: block;
}

/* Responsive images with different crops */
picture source[media="(max-width: 640px)"] → mobile crop (portrait/square)
picture source[media="(min-width: 641px)"] → desktop crop (landscape)
```

---

## Responsiveness Scoring Rubric

```
RESPONSIVENESS AUDIT — [page name]
────────────────────────────────────────────────
Dimension 1: Mobile Layout
  □ Single column on mobile?
  □ No horizontal overflow?
  □ Text not overflowing container?
  Score: __ / 10

Dimension 2: Touch Targets
  □ All interactive elements ≥ 44×44px on mobile?
  □ Nav links have adequate tap area?
  □ Cards fully clickable?
  Score: __ / 10

Dimension 3: Typography Scaling
  □ H1/body ratio ≤ 3.5x on mobile?
  □ No text smaller than 12px on mobile?
  □ Type scales fluidly between viewpoints?
  Score: __ / 10

Dimension 4: Navigation
  □ Mobile nav present and functional?
  □ Desktop nav hidden on mobile?
  □ Active state visible on both?
  Score: __ / 10

Dimension 5: Images & Media
  □ No image overflow?
  □ Images have width:100%, height:auto?
  □ No fixed-pixel widths on images?
  Score: __ / 10

Dimension 6: Spacing Rhythm
  □ Mobile padding reduced from desktop?
  □ No excess whitespace on mobile?
  □ Sections still have visual separation?
  Score: __ / 10

────────────────────────────────────────────────
TOTAL SCORE: __ / 10  (average of 6 dimensions)
STATUS: PASS (≥ 8.0) | FAIL (< 8.0)

Failing dimensions:
  [list each < 8 with specific fix]
────────────────────────────────────────────────
```

---

## Common Responsiveness Failures

| Failure | Score Impact | Fix |
|---|---|---|
| Horizontal scroll on mobile | D1: -8 | `overflow-x: hidden` on body, find overflow source |
| Touch targets < 44px | D2: -6 | Add min-height: 44px + padding |
| H1 too large on mobile (ratio > 4x) | D3: -4 | Cap at --text-3xl on mobile |
| Desktop nav visible on mobile | D4: -6 | `display: none` on mobile, add hamburger |
| Fixed-width image | D5: -6 | `max-width: 100%; height: auto` |
| Desktop padding unchanged on mobile | D6: -4 | Reduce from --space-8 to --space-5 |
| Two-column grid on 360px viewport | D1: -5 | `grid-template-columns: 1fr` on mobile |
| Text set in vw only (no min) | D3: -4 | Use `clamp()` with minimum size |
| Hover-only interaction (no touch) | D2: -3 | Add click/tap equivalent for all hover actions |
