# Layer Stack Patterns

> Declare layer stack before producing. Every layer needs a job.

## Layer Model (5 levels)

```
Z   NAME          CONTENT                   OPACITY   TECHNIQUE
─────────────────────────────────────────────────────────────────
1   CANVAS        background color/image    100%      solid or subtle gradient
2   ATMOSPHERE    wash, mist, texture       15–50%    opacity + blend-mode
3   TYPOGRAPHY    display text, headlines   80–100%   z-index mid, can interleave
4   OBJECTS       illustration, photo, 3D   100%      no bg, transparent PNG/SVG
5   ACCENT        seal, badge, highlight    100%      smallest, highest contrast
```

## CSS Layer Architecture

```css
.scene {
  position: relative;
  overflow: hidden;
}

/* Layer 1 — Canvas */
.layer-canvas {
  position: absolute; inset: 0;
  background: var(--bg);
  z-index: 0;
}

/* Layer 2 — Atmosphere */
.layer-atmosphere {
  position: absolute; inset: 0;
  z-index: 1;
  opacity: 0.25;            /* tune per design */
  mix-blend-mode: multiply; /* or overlay for dark bg */
  pointer-events: none;
}

/* Layer 3 — Typography */
.layer-type {
  position: relative;
  z-index: 3;               /* above atmosphere, can go below objects */
}

/* Layer 4 — Objects */
.layer-object {
  position: absolute;
  z-index: 4;               /* above type by default */
  filter: drop-shadow(0 8px 24px rgba(0,0,0,0.15));
}

/* Layer 5 — Accent */
.layer-accent {
  position: absolute;
  z-index: 5;
}
```

## Shallow Stack (2–3 layers — most web use cases)

```
Canvas + Typography:
  Standard flat design. Clean. Kanso.

Canvas + Atmosphere + Typography:
  Subtle depth. Atmospheric bg + readable type above.
  Works without illustration assets.
  Atmosphere: CSS gradient, noise texture, subtle pattern.
```

## Deep Stack (4–5 layers — illustration-heavy)

```
Canvas + Atmosphere + Typography (interleaved) + Objects + Accent:
  Full depth. Requires art assets (transparent PNG/SVG/3D).
  Type goes BEHIND some objects, IN FRONT of others.
  Objects cast shadows onto lower layers.
```

## Scale = Distance Rule

```
FOREGROUND object:  100% size, 100% opacity, sharp
MID-GROUND object:  70–80% size, 90% opacity, slightly soft
BACKGROUND object:  40–60% size, 50–70% opacity, blurred (filter: blur(1-2px))

CSS:
  .object-far    { transform: scale(0.6); opacity: 0.6; filter: blur(1px); }
  .object-mid    { transform: scale(0.8); opacity: 0.9; }
  .object-near   { transform: scale(1.0); opacity: 1.0; }
```
