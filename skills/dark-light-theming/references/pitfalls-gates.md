# Pitfalls & Gates

## Color Inversion Pitfalls

### 1. Status colors need separate values

```
Status green on dark bg: #4ade80 (light green — readable on dark)
Status green on light bg: #16a34a (dark green — readable on white)

FAIL: using same #4ade80 in both modes
  → dark: 7.5:1 contrast ✅
  → light: 2.1:1 contrast ❌ (against white bg)
```

### 2. Shadow direction

```
Dark mode: shadows go DOWN (light source from above)
  box-shadow: 0 4px 12px rgba(0,0,0,0.5)

Light mode: same direction, much less opacity
  box-shadow: 0 4px 12px rgba(0,0,0,0.1)

FAIL: using rgba(0,0,0,0.5) in light mode → looks painted on, not elevated
```

### 3. Images and illustrations

```
Photos:    usually fine in both modes
SVG icons: check fill/stroke colors — hardcoded #000 fails on dark bg
  Fix: use currentColor for icon fills
  <path fill="currentColor" d="..."/>

Background images:
  Dark hero overlay: rgba(0,0,0,0.5) blend
  Light hero overlay: rgba(255,255,255,0.7) blend
```

### 4. Border visibility flip

```
Dark: border needs to be LIGHTER than background
  --border: #222222 (lighter than #0c0c0c bg) ✅

Light: border needs to be DARKER than background
  --border: #e5e5e5 (darker than #ffffff bg) ✅

FAIL: same border value in both modes
  #222222 on white bg = harsh black line
  #e5e5e5 on dark bg = invisible
```

### 5. Dot grid / texture

```css
/* Dark: light dots on dark bg */
background-image: radial-gradient(circle, #1e1e1e 1px, transparent 1px);

/* Light: dark dots on light bg */
[data-theme="light"] body {
  background-image: radial-gradient(circle, #e5e5e5 1px, transparent 1px);
}
```

---

## Theming Gates (Scored 0–10, Min 8)

```
Gate T1: Token Architecture
  □ All colors via semantic tokens — no hardcoded hex in components?
  □ Primitive layer separate from semantic layer?
  Score: __ / 10

Gate T2: FOUC Prevention
  □ Theme script inline in <head>?
  □ No flash on hard refresh in either mode?
  Score: __ / 10

Gate T3: Contrast in Both Modes
  □ Primary text ≥ 4.5:1 in dark mode?
  □ Primary text ≥ 4.5:1 in light mode?
  □ Status colors recalculated for each mode?
  Score: __ / 10

Gate T4: Inversion Pitfalls
  □ Shadows recalculated per mode?
  □ Icons use currentColor?
  □ Borders visible in both modes?
  Score: __ / 10

OVERALL: __ / 10   MINIMUM: 8.0
```
