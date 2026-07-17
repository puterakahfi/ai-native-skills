# Typography, Elevation & Motion Tokens

> Reference for design-system SKILL.md Steps 3, 4 & 5.
> Load this file when declaring type scale, shadow levels, or motion tokens.

---

## Step 3: Declare Typography Tokens

### Modular Scale Selection

```
Choose ONE scale ratio for the entire product — do not mix:

  1.125 (Major Second)   → dense UI, dashboards, data-heavy
  1.25  (Major Third)    → balanced UI, standard web apps
  1.333 (Perfect Fourth) → editorial, blogs, landing pages
  1.5   (Perfect Fifth)  → display, high-impact, minimal content

For personal landing pages → 1.333 (Perfect Fourth)
For product apps          → 1.25 (Major Third)
```

### Font Size Tokens (1.333 scale)

```css
:root {
  --text-2xs:  0.422rem;  /*  6.75px — legal, fine print only */
  --text-xs:   0.563rem;  /*  9px    — tags, badges, mono labels */
  --text-sm:   0.75rem;   /* 12px    — captions, secondary meta */
  --text-base: 1rem;      /* 16px    — body text (baseline) */
  --text-lg:   1.333rem;  /* 21px    — lead text, large body */
  --text-xl:   1.777rem;  /* 28px    — card headings, section labels */
  --text-2xl:  2.369rem;  /* 38px    — page headings */
  --text-3xl:  3.157rem;  /* 50px    — display headings (mobile H1 max) */
  --text-4xl:  4.209rem;  /* 67px    — hero display (desktop only) */
}
```

### Font Weight Tokens

```css
:root {
  --weight-regular: 400;
  --weight-medium:  500;
  --weight-semibold: 600;
  --weight-bold:    700;
}
/* Do not use 300 (light) for body — readability drops below 400 */
/* Do not use 800/900 unless display-only, ≥ 2xl size */
```

### Line Height Tokens

```css
:root {
  --leading-tight:   1.1;   /* display headings ≥ 3xl */
  --leading-snug:    1.25;  /* headings 2xl–xl */
  --leading-normal:  1.5;   /* UI labels, buttons */
  --leading-relaxed: 1.65;  /* body text — optimal readability */
  --leading-loose:   1.8;   /* long-form prose */
}
```

### Letter Spacing Tokens

```css
:root {
  --tracking-tight:  -0.04em;  /* large display headings */
  --tracking-snug:   -0.02em;  /* medium headings */
  --tracking-normal:  0;       /* body text */
  --tracking-wide:    0.06em;  /* tags, badges */
  --tracking-wider:   0.1em;   /* nav labels */
  --tracking-widest:  0.14em;  /* section labels, eyebrows */
}
```

---

## Step 4: Declare Elevation Tokens

```css
:root {
  --shadow-none:   none;
  --shadow-sm:     0 1px 2px rgba(0,0,0,0.3);
  --shadow-md:     0 4px 12px rgba(0,0,0,0.4);
  --shadow-lg:     0 8px 24px rgba(0,0,0,0.5);
  --shadow-xl:     0 16px 48px rgba(0,0,0,0.6);
}
/*
Elevation hierarchy:
  Canvas (bg):        shadow-none
  Cards (surface):    shadow-sm
  Modals:             shadow-md
  Dropdowns:          shadow-lg
  Full overlays:      shadow-xl
*/
```

---

## Step 5: Declare Motion Tokens

```css
:root {
  --duration-instant:  50ms;
  --duration-fast:    150ms;   /* hover states, micro interactions */
  --duration-normal:  250ms;   /* standard transitions */
  --duration-slow:    400ms;   /* page transitions, large elements */
  --duration-slower:  600ms;   /* entrance animations */

  --ease-standard:    cubic-bezier(0.4, 0, 0.2, 1);  /* material standard */
  --ease-decelerate:  cubic-bezier(0, 0, 0.2, 1);    /* elements entering */
  --ease-accelerate:  cubic-bezier(0.4, 0, 1, 1);    /* elements leaving */
  --ease-spring:      cubic-bezier(0.175, 0.885, 0.32, 1.275);
}
/*
Rules:
  - Never animate without purpose
  - Motion must be ≤ --duration-normal for responsive UI
  - Prefer transform + opacity (GPU composited) — not width/height/top/left
  - Respect prefers-reduced-motion
*/
```

```css
@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after {
    animation-duration: 0.01ms !important;
    transition-duration: 0.01ms !important;
  }
}
```
