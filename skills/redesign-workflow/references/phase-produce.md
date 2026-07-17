# Phase 4 — PRODUCE

Apply design in this order. Load each skill before using its templates.

```
1. Genre tokens         → design-genre skill
2. Visual language      → phase-genre-macro.md Phase 0.6
3. Macrostructure       → macrostructures skill
4. Design system tokens → design-system skill
5. Theme architecture   → dark-light-theming skill
6. Motion               → motion-design skill (only if motion-on)
7. Content              → content-strategy skill
8. Components           → ui-components (template) + ux-patterns-for-developers (behavior)
```

---

## Mandatory CSS Stamp (top of every output)

```css
/*
 * macrostructure: [name]
 * genre:          [genre]
 * theme:          [light-only | dark-only | dual-theme]
 * iteration:      [N]
 * pre-emit:       P_ H_ E_ S_ R_ V_
 */
```

---

## Mandatory Design System

**Typographic scale — 1.333 Perfect Fourth:**
```css
--text-xs:   0.563rem;
--text-sm:   0.75rem;
--text-base: 1rem;
--text-lg:   1.333rem;
--text-xl:   1.777rem;
--text-2xl:  2.369rem;
--text-3xl:  3.157rem;
--text-4xl:  4.209rem;
/* Mobile: cap H1 at --text-3xl — keep H1/body ratio ≤ 3.0x */
```

**Color semantic (one var = one role, no collapse):**
```css
--live:              /* LIVE status — nowhere else */
--interactive-hover: /* hover state — nowhere else */
--bg:                /* base background */
--bg-alt:            /* alternate section (figure/ground) */
--surface:           /* card/elevated surface */
--border:            /* dividers */
--bright:            /* headings, primary content */
--text:              /* body text */
--subtle:            /* supporting info */
--muted:             /* decorative, disabled */
```

**Figure/Ground (never flat single color):**
```css
background-image: radial-gradient(circle, #1e1e1e 1px, transparent 1px);
background-size: 32px 32px;
/* OR: linear-gradient(180deg, #0f0f0f 0%, #0a0a0a 100%) */
/* OR: alternating section backgrounds */
```

**Whitespace rhythm:**
```
Hero:    padding-top clamp(120px,16vh,180px) — NO min-height:100vh (causes void)
Content: 80–96px padding
Contact: 48–64px padding
Footer:  24–32px padding
```

**Empty state rule:**
```
1 product  → full width
2 products → full-width stacked (NOT 2-col grid)
3 products → 3-col grid or stacked
4+         → grid
```

**First impression (50ms):**
```
H1 = stance, not job title
FAIL: "Full Stack Engineer specializing in scalable architecture"
PASS: "One codebase. Five products." / "I build systems meant to last."
```

**Accessibility baseline:**
```html
<nav aria-label="Main navigation">
<main id="main">
<section aria-labelledby="[id]">
<footer>
<!-- H1→H2→H3 — no skipping -->
<!-- sr-only H2 if section visually unlabelled -->
<!-- Links: descriptive text, rel="noopener" for external -->
<!-- Skip link: first focusable element, min-height 44px -->
```

---

## Pre-Emit Self-Critique (BEFORE delivering)

Score 1–5. Any axis < 3 = revision before emit.
```
P (Philosophy):  Every element has a reason to exist?     __ /5
H (Hierarchy):   Visual hierarchy immediately readable?   __ /5
E (Execution):   Spacing, scale, alignment consistent?    __ /5
S (Specificity): Copy specific, not generic? No slop?     __ /5
R (Restraint):   Anything decorative that could be cut?   __ /5
V (Variety):     Structurally different from last output? __ /5

Stamp: /* pre-emit: P_ H_ E_ S_ R_ V_ */
```

---

## Slop Red List (auto-revision if present)

```
❌ "Get started for free" as primary CTA (unless product requires it)
❌ H1 + 3 bullet features + CTA button (template pattern)
❌ "Trusted by X companies" logo row in hero
❌ Testimonial grid with star ratings
❌ Gradient mesh background behind text
❌ "Seamless", "leverage", "world-class", "cutting-edge" in copy
❌ 6+ feature cards in equal-size grid
❌ All-caps nav with 5+ items
```

---

## Theme System (dual-theme surfaces)

```
Preserve existing infra — do not add second system:
  next-themes + class  → .dark / dark: utilities
  next-themes + data   → [data-theme="dark"]
  custom/localStorage  → inspect existing script first

Toggle requirements:
  □ one toggle in global nav
  □ aria-label = next action: "Switch to dark theme" / "Switch to light theme"
  □ touch target ≥ 44×44px
  □ no hydration mismatch on SSR

Verify both modes:
  □ Light screenshot/DOM ✓
  □ Toggle → dark screenshot/DOM ✓
  □ Toggle back → state reversible ✓
```
