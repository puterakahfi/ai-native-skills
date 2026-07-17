# Wide & Ultrawide Breakpoints

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

---

## Max-width Container (MANDATORY for all layouts)

```css
/* Every page must have a max-width container */
/* HARD RULE: max-width: min(1200px, 90vw) — mandatory on all sections */
.container {
  width: 100%;
  max-width: min(1200px, 90vw);  /* scales with viewport, never edge-to-edge */
  margin: 0 auto;
  padding: 0 var(--sp-8);
}

/* For full-bleed sections (hero, dividers): constrain content inside, not wrapper */
.hero-content {
  max-width: min(1200px, 90vw);
  margin: 0 auto;
  width: 100%;
}

/* Nav: constrain inner content */
nav .nav-inner {
  max-width: min(1200px, 90vw);
  margin: 0 auto;
  padding: 0 var(--sp-8);
  width: 100%;
}
```

---

## Hero Void on Wide Screens

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

---

## Common Violations at Wide Breakpoints

```
□ Nav items spread too far apart — add max-width to nav inner
□ Work rows full-width at 1440px → index number and arrow too far apart
□ About grid 50/50 at 1440px → left column too wide → heading unreadable
□ Contact section: heading and links at opposite ends of 1440px viewport → weird
```

---

## Standard Breakpoints

```css
/* Mobile first — min-width queries only */

/* Default (no query) = mobile: 0–639px */

@media (min-width: 640px)  { /* sm: tablet portrait */ }
@media (min-width: 768px)  { /* md: tablet landscape */ }
@media (min-width: 1024px) { /* lg: desktop */ }
@media (min-width: 1280px) { /* xl: large desktop */ }
@media (min-width: 1536px) { /* 2xl: wide desktop */ }
```

---

## When to Add a Breakpoint

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
