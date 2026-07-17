# Typography Interleave

> Type goes BEHIND and IN FRONT of objects — not just on top.
> This is what creates the feeling that type and objects exist in the same space.

## The Technique

```
FLAT (type always on top):
  z: canvas(0) → atmosphere(1) → type(3) → objects(4)
  Result: type floats above everything — no integration

INTERLEAVE (type weaves through):
  Large display text z-index = 2  (below objects)
  Small body text z-index = 4     (above objects)
  Result: objects appear to "emerge through" the text — spatial depth
```

## CSS Implementation

```css
/* Hero scene with interleave */
.hero-scene {
  position: relative;
}

/* Display text — BEHIND main object */
.hero-display {
  position: relative;
  z-index: 2;               /* above atmosphere, below object */
  font-size: var(--text-4xl);
  opacity: 0.9;
}

/* Main object — IN FRONT of display text */
.hero-object {
  position: absolute;
  z-index: 4;               /* above display text */
  right: 0;
  top: -20%;                /* bleeds outside container — no box constraint */
}

/* Body text — above object */
.hero-body {
  position: relative;
  z-index: 5;
}
```

## Interleave Patterns

### Pattern A — Object emerges from text (zen, editorial)
```
[large display text]
        [OBJECT overlaps and covers part of text]
[body text reads over object]
```

### Pattern B — Text wraps around object space (editorial)
```
[text left column]    [OBJECT right, extends beyond bounds]
[text continues]      [object bottom bleeds down]
```

### Pattern C — Foreground / background split (atmospheric)
```
[far object — small, faded, behind text]
[text — mid layer]
[near object — large, sharp, in front of text]
```

## Rules

```
ALWAYS:
  Large/decorative text = lower z (behind objects)
  Small/body text = higher z (in front — must remain readable)
  Objects = no bounding box (overflow: visible, not clip)

NEVER:
  Body text hidden behind object (readability fails F2)
  Object covers CTA or primary action
  Interleave on mobile without responsive fallback
    → mobile: stack vertically, remove interleave, keep atmosphere only
```

## Responsive Rule

```css
/* Mobile: flatten the interleave */
@media (max-width: 640px) {
  .hero-object {
    position: relative;     /* back to flow */
    z-index: auto;
    width: 100%;
    margin-top: var(--sp-8);
  }
  .hero-display { z-index: auto; }
}
```
