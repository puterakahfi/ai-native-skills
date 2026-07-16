---
name: design-system
description: Design token decisions and system construction — when to use which spacing scale, type scale, color role, elevation level, and motion token. Produces a declaration table before any pixel is designed. The design system is the single source of truth; all design decisions trace back to it.
license: MIT
metadata:
  ai-native-skills.version: 1.0.0
  ai-native-skills.author: puterakahfi
  ai-native-skills.type: skill
  ai-native-skills.implements: ai-native-core/contracts/skills/experience-design/design-system.contract.yaml
  ai-native-skills.related_skills: '[''master-design'', ''ux-ui-patterns'', ''accessibility'', ''design-review'']'
---

# Design System Skill

## Core Principle

```
Design system = decisions made once, applied everywhere.

Without it: every screen is a new negotiation between color, space, and type.
With it:    every screen is an instance of the same vocabulary.

Before designing ANY screen:
  1. Declare the token table
  2. Design within the tokens
  3. If a value is not in the token table → add it or use the nearest token

Never hardcode a value that should be a token.
```

---

## Step 1: Declare Color Tokens

### Semantic Color Roles

Every color must have exactly one semantic role. Decide role first, pick value second.

| Role | Token Name | What It Means | Where Used |
|---|---|---|---|
| Canvas | `--bg` | Page background | `body` only |
| Canvas alt | `--bg-alt` | Alternate section | Section zebra pattern |
| Surface | `--surface` | Cards, modals, popovers | Elevated elements |
| Surface raised | `--surface-raised` | Tooltips, dropdowns | Above surface |
| Border | `--border` | Dividers, outlines | `border`, `outline` |
| Border subtle | `--border-subtle` | De-emphasized dividers | Secondary separators |
| Content primary | `--text-primary` | Main readable text | Body, labels |
| Content secondary | `--text-secondary` | Supporting text | Captions, meta |
| Content tertiary | `--text-tertiary` | De-emphasized | Placeholders, disabled |
| Content inverse | `--text-inverse` | Text on colored bg | On accent/danger |
| Accent | `--accent` | Brand / primary action | ONE purpose only |
| Accent hover | `--accent-hover` | Accent interaction state | Hover on accent |
| Success | `--success` | Positive, live, confirmed | LIVE badge, success state |
| Warning | `--warning` | Caution state | Warning badge |
| Danger | `--danger` | Error, destructive | Error state, delete |
| Interactive | `--interactive` | Links, clickable | Default link color |
| Interactive hover | `--interactive-hover` | Link hover | Hover state |

### Color Decision Protocol

```
When picking a color value:

1. What is the semantic role? → pick the right token name
2. Is there already a token for this role? → use it, do not add new
3. Dark theme vs light theme → define both in :root + [data-theme="light"]
4. Contrast check: text on background → must be ≥ 4.5:1 (AA)
5. Accent: is this the ONLY place accent is used? → if no, rename the role

Anti-patterns:
  ❌ Same hex value in 3 different variables → consolidate
  ❌ --accent used for: logo + hover + status + CTA → semantic collapse
  ❌ Picking hex first, naming it second → backwards, name role first
```

### Dark Theme Token Values (Sensible Defaults)

```css
:root {
  /* Canvas */
  --bg:              #0c0c0c;
  --bg-alt:          #111111;
  --surface:         #181818;
  --surface-raised:  #222222;

  /* Borders */
  --border:          #2a2a2a;
  --border-subtle:   #1e1e1e;

  /* Content */
  --text-primary:    #f0f0f0;
  --text-secondary:  #a0a0a0;
  --text-tertiary:   #555555;
  --text-inverse:    #0c0c0c;

  /* Brand */
  --accent:          #6366f1;   /* indigo */
  --accent-hover:    #818cf8;

  /* Status */
  --success:         #4ade80;   /* green — LIVE, positive */
  --warning:         #fb923c;   /* orange — caution */
  --danger:          #f87171;   /* red — error, destructive */

  /* Interactive */
  --interactive:     #a0a0a0;
  --interactive-hover: #f0f0f0;
}
```

---

## Step 2: Declare Spacing Tokens

### 8px Base Grid

All spacing from multiples of 4px. Every gap, padding, margin must be a token.

```css
:root {
  --space-1:  4px;
  --space-2:  8px;
  --space-3:  12px;
  --space-4:  16px;
  --space-5:  24px;
  --space-6:  32px;
  --space-7:  48px;
  --space-8:  64px;
  --space-9:  96px;
  --space-10: 128px;
  --space-11: 192px;
  --space-12: 256px;
}
```

### Spacing Decision: Which Token to Use

```
Inline gap between elements:    --space-2 to --space-4
Component internal padding:     --space-3 to --space-5
Component external margin:      --space-4 to --space-6
Section internal padding:       --space-7 to --space-9
Section-to-section gap:         --space-8 to --space-10
Page top/bottom margin:         --space-10 to --space-12

Rule: if two values are adjacent, their difference must be ≥ 1 step
(e.g. icon-to-label: --space-2, component: --space-4 — clear separation)
```

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

---

## Step 6: Declare Layout Tokens

```css
:root {
  --container-sm:   640px;
  --container-md:   768px;
  --container-lg:   960px;
  --container-xl:  1200px;
  --container-2xl: 1400px;

  --radius-none:  0;
  --radius-sm:    2px;
  --radius-md:    4px;
  --radius-lg:    8px;
  --radius-xl:    12px;
  --radius-full:  9999px;
}
/*
Border radius philosophy:
  Sharp (--radius-sm): code, terminal, data tables — precision feel
  Rounded (--radius-md/lg): cards, buttons — approachable
  Full (--radius-full): badges, pills, avatars

Pick ONE primary radius for a product. Mix max 2.
*/
```

---

## Token Declaration Checklist

Before designing any screen, verify this table is complete:

```
□ Color tokens declared — each has ONE semantic role
□ Spacing scale declared — 8px base, 12 steps
□ Type scale declared — one ratio chosen, 8 sizes
□ Font weights declared — 3–4 only
□ Line heights declared — 5 levels
□ Letter spacing declared — 5 levels
□ Elevation declared — 5 shadow levels
□ Motion declared — durations + easings
□ Border radius declared — 1–2 values for the product

FAIL: any hardcoded value in design that is not in token table
FAIL: same hex used in multiple semantic roles
FAIL: any font size not from the scale
FAIL: spacing value not from 8px grid
```
