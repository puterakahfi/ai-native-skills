# Fluid Grid & Fluid Typography

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

---

## H1/Body Ratio Gate (mobile)

```
At mobile viewport (375px):
  H1 computed size / body computed size ≤ 3.5x

If clamp() makes H1 too large on mobile → cap H1 at --text-3xl on mobile:

@media (max-width: 640px) {
  h1.hero { font-size: var(--text-3xl); }
}
```

---

## Why clamp() over fixed breakpoints for type

```
Fixed breakpoints for type:
  h1 { font-size: 2rem; }
  @media (min-width: 1024px) { h1 { font-size: 4rem; } }
  → Hard jump at 1024px, feels mechanical

clamp():
  h1 { font-size: clamp(2rem, 1.5rem + 2vw, 4rem); }
  → Smooth scale from 375px to 1440px, feels designed

Use clamp() for all headings and body text.
Only use breakpoint override for ratio gate (H1 > 3.5x body on mobile).
```
