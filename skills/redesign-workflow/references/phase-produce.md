# Phase 7 — PRODUCTION

Apply design in this order. Load each skill before using its templates.

```text
0. Preservation check    → existing brand, DESIGN.md, tokens, and framework conventions
1. Genre tokens         → design-genre skill
2. Visual language      → phase-genre-macro.md Phase 0.6
3. Macrostructure       → macrostructures skill
4. Design system tokens → design-system skill
5. Theme architecture   → dark-light-theming skill
6. Motion               → motion-design skill (only if motion-on)
7. Content              → content-strategy skill
8. Components           → ui-components (template) + ux-patterns-for-developers (behavior)
9. Component pass       → component-redesign-pass.md (navbar → hero → sections → cards/rows → contact → footer)
```

## Preservation-first production policy

Existing systems are authoritative unless the redesign spec explicitly reopens them.

```text
Existing brand tokens found      → preserve or map semantically; do not replace by taste
Existing type scale found        → audit and refine; do not force a new mathematical scale
Existing theme infrastructure    → extend it; never introduce a parallel theme system
Existing component primitives    → reuse them when behavior and accessibility are sound
No usable system found           → use the fallback production defaults below
```

A fallback is not a mandate. Record why it was used in the run state or delivery manifest.

---

## Implementation Stamp

Record the production context once per artifact, not once per source file.

For a standalone stylesheet or generated prototype, a source comment is acceptable:

```css
/*
 * macrostructure: [name]
 * genre:          [genre]
 * theme:          [light-only | dark-only | dual-theme]
 * iteration:      [N]
 * pre-emit:       P_ H_ E_ S_ R_ V_
 */
```

For component repositories using Tailwind, CSS-in-JS, design tokens, or multiple style files:

```text
- store the stamp in the durable run state, redesign report, or delivery manifest
- optionally place one comment in the primary global theme file
- never add repetitive stamp comments to every TSX, JSX, Vue, Svelte, or component file
```

---

## Design System Policy

### Typographic scale

Preserve a coherent existing type scale when present. When no usable scale exists, use this as a fallback starting point — not an invariant:

```css
--text-xs:   0.563rem;
--text-sm:   0.75rem;
--text-base: 1rem;
--text-lg:   1.333rem;
--text-xl:   1.777rem;
--text-2xl:  2.369rem;
--text-3xl:  3.157rem;
--text-4xl:  4.209rem;
```

Responsive constraints still apply:

```text
- prevent heading overflow at narrow widths
- keep mobile H1/body contrast intentional rather than mechanically oversized
- preserve readable line length and line-height
- use fluid sizing only when intermediate widths have been verified
```

### Color semantics

Use one semantic token per role. Map existing tokens before creating new ones.

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

Do not create duplicate semantic systems when the repository already uses names such as `background`, `foreground`, `primary`, `muted`, and `border`. Extend or document the mapping instead.

### Figure / ground

Never leave a long page as one undifferentiated flat field. Use the lightest sufficient method:

```css
background-image: radial-gradient(circle, #1e1e1e 1px, transparent 1px);
background-size: 32px 32px;
/* OR: linear-gradient(180deg, #0f0f0f 0%, #0a0a0a 100%) */
/* OR: alternating section backgrounds, borders, rhythm, or surface depth */
```

Texture is optional. Figure/ground separation is required.

### Whitespace rhythm

```text
Hero:    padding-top clamp(120px,16vh,180px) — avoid min-height:100vh when it creates a void
Content: 80–96px padding as a starting range
Contact: 48–64px padding as a starting range
Footer:  24–32px padding as a starting range
```

These ranges may be adapted to the existing system, density, device class, and content length.

### Collection layout

Choose layout from content weight, not card count alone.

```text
1 primary item  → full-width feature
2 primary items → stacked or asymmetric split when their evidence needs room
3 primary items → editorial grid, 3-column grid, or stacked sequence
4+ items        → grouped grid, list, filter, or progressive disclosure
```

Do not give live, planned, and experimental items equal visual weight merely because they share a component type.

---

## Portfolio and Product-Hub Proof Architecture

For portfolios, personal sites, studios, product ecosystems, and open-source hubs, minimalism must not erase proof.

```text
Above the fold:
  stance + domain + clear next action

Primary evidence:
  2–4 selected real works with status, outcome, role, or concrete scope

Secondary evidence:
  open source, writing, standards, experiments, or process artifacts

Trust structure:
  honest status labels; released/open work outranks planned/lab work

Avoid:
  a visually beautiful page made mostly of abstract philosophy
  equal cards that hide which work is real, active, or important
  unsupported metrics, fake logos, fake testimonials, or invented outcomes
```

When real screenshots or product assets are unavailable, use honest structured evidence: product name, category, status, scope, link, and a specific description. Do not fabricate visual proof.

---

## First Impression (50ms)

```text
H1 = stance, not job title
FAIL: "Full Stack Engineer specializing in scalable architecture"
PASS: "One codebase. Five products." / "I build systems meant to last."
```

The supporting line should resolve what the person or product actually does. A stance without domain clarity is incomplete.

---

## Accessibility Baseline

```html
<a href="#main">Skip to content</a>
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

## Pre-Emit Self-Critique

Score 1–5. Any axis below 3 requires revision before emit.

```text
P (Philosophy):  Every element has a reason to exist?     __ /5
H (Hierarchy):   Visual hierarchy immediately readable?   __ /5
E (Execution):   Spacing, scale, alignment consistent?    __ /5
S (Specificity): Copy specific, not generic? No slop?     __ /5
R (Restraint):   Anything decorative that could be cut?   __ /5
V (Variety):     Structurally different from last output? __ /5

Stamp: pre-emit P_ H_ E_ S_ R_ V_
```

---

## Slop Red List

Auto-revise if present without a brief-specific reason.

```text
❌ "Get started for free" as primary CTA when the product does not require it
❌ H1 + 3 bullet features + CTA button as the default template
❌ "Trusted by X companies" logo row without verified data
❌ Testimonial grid with fabricated or irrelevant star ratings
❌ Gradient mesh background used as a substitute for composition
❌ "Seamless", "leverage", "world-class", "cutting-edge" in generic copy
❌ 6+ feature cards in an equal-size grid without prioritization
❌ All-caps nav with 5+ items
❌ Minimalist portfolio that removes project evidence and leaves only philosophy
```

---

## Theme System for Dual-Theme Surfaces

```text
Preserve existing infra — do not add a second system:
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
