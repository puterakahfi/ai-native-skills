# Elevation Inheritance Model

> **Core insight:** Every visual surface exists at a depth — even transparent ones.
> Transparent ≠ "no layer". Transparent = "borrow parent's plane".

---

## The Problem With Counting Layers

Naively counting layers breaks down because every component is recursive:

```
Page
└── Hero Section          ← is this 1 layer or 2?
    ├── Background         ← background = layer 1?
    └── Content            ← content = layer 2?
        ├── Text           ← text = layer 3?
        ├── Illustration   ← illustration = layer 4?
        └── Bio text       ← bio = layer 5?
```

If you count every DOM node, you get infinite layers.  
If you ignore structure, you lose depth expressiveness.

---

## The Solution: Two-Axis Model

Instead of one global counter, use **two orthogonal axes**:

| Axis | Name | Scope | Range |
|------|------|-------|-------|
| **Plane** | Global Depth Plane | Page-wide | 0–3 |
| **Elevation** | Internal Elevation | Per-component | +0 to +2 |

### Global Planes (perceptual limit: 4)

```
Plane 0 — Canvas      Page background. Sets the tone. Never interactive.
Plane 1 — Atmosphere  Ambient blur/wash/shadow. Felt, not seen.
Plane 2 — Content     Text, illustrations, UI surfaces. The "stage".
Plane 3 — Accent      Badges, tooltips, active overlays.
```

### Internal Elevation (relative, per-component)

Within a component at Plane N, sub-elements use:

```
+0  Component surface / background
+1  Primary content (text, icon, image)
+2  Accent content (badge, highlight, label-over-image)
```

**Ceiling: +2**. If you need +3, that element belongs in a new component at a higher plane.

---

## Transparent Background Resolution

```
transparent → inherit parent's plane

NOT: transparent → plane 0 (canvas)
```

### Example

```
hero-section   plane=2, bg=transparent
               ↓ inherits plane 2 from page's content plane
               ↓ its atmosphere (blur, wash) is still plane 1
               ↓ the section itself has NO atmosphere of its own

hero-name      plane=2+0, z-index=2   ← same plane, base elevation
hero-object    plane=2+1, z-index=3   ← elevated inside section
hero-bio       plane=2+2, z-index=4   ← above object, still "content" plane
```

---

## Layer Stack Declaration Format

Always declare the stack BEFORE implementation:

```
# Global stack
canvas          | plane=0 | elev=+0 | bg=--bg           | page base
atmosphere      | plane=1 | elev=+0 | bg=transparent    | CSS radial wash

# Component: hero
hero-section    | plane=2 | elev=+0 | bg=transparent→2  | no bg, inherits
hero-name       | plane=2 | elev=+0 | —                 | behind object
hero-object     | plane=2 | elev=+1 | transparent       | illustration
hero-bio        | plane=2 | elev=+2 | —                 | above illustration

# Component: card
card            | plane=2 | elev=+0 | bg=--surface      | raised surface
card-content    | plane=2 | elev=+1 | —                 | text, icon
card-badge      | plane=2 | elev=+2 | bg=--accent       | count/status badge
```

---

## z-index Mapping

Convert plane + elevation to actual CSS z-index:

```
z-index = (plane × 10) + elevation
```

| Element | Plane | Elev | z-index |
|---------|-------|------|---------|
| canvas | 0 | +0 | 0 |
| atmosphere | 1 | +0 | 10 |
| hero-name | 2 | +0 | 20 |
| hero-object | 2 | +1 | 21 |
| hero-bio | 2 | +2 | 22 |
| tooltip | 3 | +0 | 30 |

> **Why ×10?** Gap of 10 between planes leaves room for elevation (+0 to +2)
> and avoids z-index collisions across components.

---

## Rules Summary

1. **Every component declares `depth_plane` and `background`** — no implicit layers.
2. **Transparent resolves to parent plane** — never to plane 0.
3. **Internal elevation max = +2** — split component if you need more.
4. **Isolation** — components with internal z-index use `isolation: isolate` to prevent bleed.
5. **Blend modes live at the object level** — not on the section container.

---

## Anti-Patterns

| Anti-pattern | Fix |
|---|---|
| `z-index: 9999` | Assign proper plane (0–3) |
| "no layer" for transparent bg | Declare `bg: transparent → inherit parent` |
| Counting DOM depth as visual depth | Use plane + elevation, not DOM nesting |
| `mix-blend-mode` on section container | Put blend on the specific element (img, div.atmosphere) |
| Sub-component with elevation +5 | Split into two components, higher gets plane+1 |
