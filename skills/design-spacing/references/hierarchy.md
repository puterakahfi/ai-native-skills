# Spatial Hierarchy

> Space communicates structure. More space = more separation = different category.

## Spatial Hierarchy Principle

```
GESTALT LAW OF PROXIMITY:
  Items close together → perceived as related
  Items far apart     → perceived as separate

Apply: use spacing to communicate grouping, not just aesthetics.

HIERARCHY LEVELS:
  L1: Page sections      — 80–160px apart (most separated)
  L2: Component groups   — 40–64px apart
  L3: Related components — 24–40px apart
  L4: Inline elements    — 8–16px apart (most related)
```

## Spacing Decision Tree

```
Is this two DIFFERENT sections of the page?
  → L1 spacing (80–160px)

Is this two DISTINCT components in the same section?
  → L2–L3 spacing (32–64px)

Is this RELATED items within one component?
  → L4 spacing (8–24px)

Is this an INLINE pairing (icon+text, badge+label)?
  → 4–12px gap
```

## Component Padding Rules

```
CARD / PANEL:
  padding: var(--sp-4) var(--sp-5)  → 16px 20px tight
  padding: var(--sp-5) var(--sp-6)  → 20px 24px standard
  padding: var(--sp-6) var(--sp-8)  → 24px 32px generous

BUTTON:
  small:   padding: 6px 12px
  default: padding: 10px 20px
  large:   padding: 14px 28px
  min touch target: 44×44px (a11y)

NAV:
  item padding: 8–12px horizontal, 6–8px vertical
  gap between items: 4–8px

HERO:
  padding-top:    clamp(100px, 14vh, 160px)
  padding-bottom: clamp(60px, 10vh, 120px)
  NO min-height: 100vh ← HARD RULE
```

## Common Mistakes

```
❌ Same padding on hero and card → no hierarchy signal
❌ Padding too generous on sparse content → dead space
❌ Section gap smaller than component gap → hierarchy inverted
❌ Inconsistent padding inside same component type → visual noise
✅ More space = more separation = more important boundary
✅ Internal padding < gap between siblings
```
