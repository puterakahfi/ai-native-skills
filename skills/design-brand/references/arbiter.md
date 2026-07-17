# Arbiter Sports — Design Brand

> Source: https://arbiter.io
> Status: INFERRED from visual inspection — verify with actual design.md if available

## Identity

```
Product:   Sports officiating + scheduling platform (B2B)
Audience:  Sports officials, assignors, athletic administrators
Voice:     Professional, reliable, authoritative — not playful, not zen
Genre fit: Modern Minimal (SaaS) — closest match within brand constraints
```

## Color Tokens (inferred)

```
Primary:   deep blue family (professional, trust, authority)
           verify: inspect arbiter.io CSS :root vars

Semantic roles (standard SaaS pattern):
  --color-primary:    brand blue (CTAs, links, active states)
  --color-secondary:  lighter blue or neutral
  --color-bg:         white / very light gray
  --color-surface:    #f8f9fa or similar
  --color-ink:        near-black (#1a1a1a or similar)
  --color-border:     rgba(0,0,0,0.1) — component borders PRESENT

NOTE: Arbiter uses component borders — this is their design language.
      Do NOT apply zen no-border rule here. Foundation allows borders
      when they are the brand's structural language.
```

## Typography (inferred)

```
Inspect arbiter.io to verify actual font stack.
Likely: Inter or similar neutral SaaS sans-serif
Scale: 1.250 Major Third (SaaS density)
Weight: 400 body, 500–600 headings
```

## Component Rules (inferred)

```
Borders:    YES — component borders are Arbiter's visual language
Radius:     4–8px (professional, not overly rounded)
Elevation:  subtle box-shadow on cards/panels
Icons:      TBD — inspect arbiter.io for icon family
Density:    medium-high — product UI, not marketing page
```

## Spacing

```
Scale:      8px base grid (standard SaaS)
Ma:         moderate — functional breathing room, not zen-generous
Section:    clamp(48px, 6vh, 80px) — tighter than zen
```

## Flex Areas (genre can adjust)

```
Motion stance:  can be reduced-motion friendly
Copy tone:      professional, clear — within Arbiter voice
Layout macro:   dashboard / workbench / specimen patterns ok
```

## Forbidden

```
✗ Zen-style no-border rule — Arbiter uses borders as structure
✗ Warm dark palette — not their brand temperature
✗ Fraunces 300 display — not their voice
✗ Generous Ma (18vh) — product UI needs tighter spacing
```

## Foundation Gates Still Apply

```
F1–F7 non-negotiable even within Arbiter brand.
Brand does not override: contrast, touch targets, aria, hierarchy.
```

---

> NOTE: This file is inferred from visual inspection of arbiter.io.
> Replace with actual design tokens when Arbiter provides design.md or Figma file.
