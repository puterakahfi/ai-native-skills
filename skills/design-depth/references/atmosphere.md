# Atmosphere Techniques

> Layer 2 — creates the "ground" the page exists in. Not decoration — spatial context.

## CSS Atmosphere Patterns

### Ink Wash / Sumi-e (zen, atmospheric)
```css
.atmosphere-ink {
  background-image:
    radial-gradient(ellipse 80% 60% at 70% 30%,
      rgba(40,35,25,0.3) 0%,
      transparent 70%),
    radial-gradient(ellipse 60% 40% at 30% 70%,
      rgba(40,35,25,0.15) 0%,
      transparent 60%);
  mix-blend-mode: multiply;
  opacity: 0.4;
}
/* Use on light (paper) backgrounds — multiplies to create ink quality */
```

### Mist / Distance Fade (atmospheric, zen dark)
```css
.atmosphere-mist {
  background: linear-gradient(
    to bottom,
    transparent 0%,
    rgba(var(--bg-rgb), 0.3) 40%,
    rgba(var(--bg-rgb), 0.7) 70%,
    var(--bg) 100%
  );
  /* fades objects into bg — creates infinite distance feeling */
}
```

### Noise Texture (editorial, zen)
```css
.atmosphere-noise {
  background-image: url("data:image/svg+xml,..."); /* SVG noise */
  opacity: 0.04;
  mix-blend-mode: overlay;
  /* adds paper/grain quality — never visible alone, felt collectively */
}
```

### Radial Vignette (atmospheric, dark)
```css
.atmosphere-vignette {
  background: radial-gradient(
    ellipse 100% 80% at 50% 40%,
    transparent 30%,
    rgba(0,0,0,0.4) 100%
  );
  /* darkens edges — eye drawn to center */
}
```

## Atmosphere Rules

```
OPACITY:         15–40% on light bg / 20–50% on dark bg
                 Too high = muddy. Too low = invisible. Sweet spot = felt not seen.

BLEND MODES:
  multiply  → darkens, ink quality (use on light bg)
  screen    → lightens, glow quality (use on dark bg)
  overlay   → contrast boost, texture
  soft-light → subtle mix, safest

EDGES:           always feathered, never hard. Atmosphere has no border.

POINTER EVENTS:  always pointer-events: none — never intercepts clicks
```
