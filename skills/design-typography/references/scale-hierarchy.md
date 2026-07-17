# Modular Scale & Hierarchy

> Scale first — all sizes derived from scale, never arbitrary px.

## Modular Scale Options

```
Ratio      Name              Use when
1.125      Major Second      Dense UI, dashboard, data-heavy
1.250      Major Third       SaaS product, modern minimal
1.333      Perfect Fourth    Landing pages, editorial, portfolio ✅ default
1.414      Augmented Fourth  High drama, atmospheric
1.500      Perfect Fifth     Very sparse, zen/minimalist
1.618      Golden Ratio      Max drama — use sparingly

Default: 1.333 Perfect Fourth for most landing pages + editorial
```

## CSS Scale Token Template (1.333)

```css
:root {
  --text-xs:   0.563rem;   /*  9px */
  --text-sm:   0.75rem;    /* 12px */
  --text-base: 1rem;       /* 16px */
  --text-lg:   1.333rem;   /* 21px */
  --text-xl:   1.777rem;   /* 28px */
  --text-2xl:  2.369rem;   /* 38px */
  --text-3xl:  3.157rem;   /* 51px */
  --text-4xl:  4.209rem;   /* 67px */
}
```

## Hierarchy Mapping

```
LEVEL     TOKEN           WEIGHT    USE
H1        text-3xl/4xl    300–700   Page title — ONE per page
H2        text-2xl/3xl    300–600   Section heading
H3        text-xl/2xl     400–600   Sub-section
H4        text-lg/xl      500–600   Card title, label heading
body      text-base       300–400   Prose, descriptions
small     text-sm         400       Captions, footnotes, meta
label     text-xs/sm      500–600   UI labels, tags, eyebrows

RATIO RULES:
  H1/body ratio: 3.0–4.5x (heavier weight = lower ratio ok)
  zen (wt 300): target 3.5–4.2x — weight 300 needs size to carry hierarchy
  editorial (wt 700): 2.5–3.2x — weight does the work
```

## Hierarchy Anti-Patterns

```
❌ H1 weight 300 + size small → hierarchy collapses, page reads flat
❌ H2 same size as H3 → no visual difference → cognitive noise
❌ Arbitrary font-size: 22px → breaks scale → visual inconsistency
❌ Bold everything → no hierarchy → everything is equally loud
❌ 3+ size jumps between adjacent levels → too jarring
✅ Consistent scale steps → eye travels naturally down hierarchy
✅ Weight + size both communicate level — not just one
```
