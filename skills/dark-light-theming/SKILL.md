---
name: dark-light-theming
description: Dual-theme system design — semantic token mapping, system preference detection, flash-of-wrong-theme prevention, color inversion pitfalls, and mid-session toggle. One token table, two primitive maps.
license: MIT
metadata:
  ai-native-skills.version: 1.0.0
  ai-native-skills.author: puterakahfi
  ai-native-skills.type: skill
  ai-native-skills.implements: ai-native-core/contracts/skills/experience-design/dark-light-theming.contract.yaml
  ai-native-skills.related_skills: '[''design-system'', ''accessibility'', ''readability'']'
---

# Dark/Light Theming Skill

## Core Principle

```
One semantic token table. Two primitive maps.

semantic token (--text-primary)
  → dark mode:  #f0f0f0
  → light mode: #111111

Never:
  color: #f0f0f0  ← hardcoded, breaks in light mode
  color: var(--dark-text)  ← mode-specific var, semantic collapse

Always:
  color: var(--text-primary)  ← semantic, works in both modes
```

---

## Token Architecture

### Layer 1: Primitive Tokens (raw values)

```css
:root {
  /* Dark primitives */
  --gray-950: #0a0a0a;
  --gray-900: #0c0c0c;
  --gray-850: #111111;
  --gray-800: #161616;
  --gray-750: #1e1e1e;
  --gray-700: #222222;
  --gray-600: #3a3a3a;
  --gray-500: #555555;
  --gray-400: #6b6b6b;
  --gray-300: #a0a0a0;
  --gray-200: #d4d4d4;
  --gray-100: #f0f0f0;
  --gray-50:  #f9f9f9;

  /* Brand primitives (same in both modes) */
  --green-400: #4ade80;
  --indigo-400: #818cf8;
  --indigo-500: #6366f1;
  --red-400:    #f87171;
  --amber-400:  #fb923c;
}
```

### Layer 2: Semantic Tokens (mapped to primitives)

```css
/* ── DARK MODE (default) ── */
:root,
[data-theme="dark"] {
  --bg:              var(--gray-900);
  --bg-alt:          var(--gray-850);
  --surface:         var(--gray-800);
  --surface-raised:  var(--gray-750);
  --border:          var(--gray-700);
  --border-subtle:   var(--gray-750);

  --text-primary:    var(--gray-100);
  --text-secondary:  var(--gray-300);
  --text-tertiary:   var(--gray-400);
  --text-inverse:    var(--gray-950);

  --accent:          var(--indigo-500);
  --accent-hover:    var(--indigo-400);
  --success:         var(--green-400);
  --warning:         var(--amber-400);
  --danger:          var(--red-400);

  --interactive:     var(--gray-300);
  --interactive-hover: var(--gray-100);

  /* Shadow direction: downward in dark (light from above) */
  --shadow-sm: 0 1px 2px rgba(0,0,0,0.4);
  --shadow-md: 0 4px 12px rgba(0,0,0,0.5);
}

/* ── LIGHT MODE ── */
[data-theme="light"] {
  --bg:              var(--gray-50);
  --bg-alt:          #ffffff;
  --surface:         #ffffff;
  --surface-raised:  var(--gray-50);
  --border:          var(--gray-200);
  --border-subtle:   #ebebeb;

  --text-primary:    var(--gray-950);   /* inverted */
  --text-secondary:  var(--gray-500);
  --text-tertiary:   var(--gray-400);
  --text-inverse:    var(--gray-100);

  --accent:          var(--indigo-500); /* same brand color */
  --accent-hover:    #4338ca;           /* darker on light bg */
  --success:         #16a34a;           /* darker green — contrast on white */
  --warning:         #d97706;
  --danger:          #dc2626;

  --interactive:     var(--gray-500);
  --interactive-hover: var(--gray-950);

  /* Shadow direction: same, but lighter */
  --shadow-sm: 0 1px 2px rgba(0,0,0,0.08);
  --shadow-md: 0 4px 12px rgba(0,0,0,0.12);
}
```

---

## System Preference Detection

### CSS (zero JS, no flash)

```css
/* Detect OS preference without JS */
@media (prefers-color-scheme: light) {
  :root:not([data-theme="dark"]) {
    /* apply light mode tokens */
    --bg: var(--gray-50);
    /* ... all light tokens ... */
  }
}
```

### JS (with localStorage persistence)

```js
// Run BEFORE first paint — in <head>, not deferred
(function() {
  const stored = localStorage.getItem('theme');
  const system = window.matchMedia('(prefers-color-scheme: dark)').matches
    ? 'dark' : 'light';
  const theme = stored || system;
  document.documentElement.setAttribute('data-theme', theme);
})();
```

**Critical: this script must be:**
- Inline in `<head>` — NOT in a JS file (causes FOUC)
- NOT deferred or async
- Runs synchronously before first paint

### Toggle Implementation

```js
function toggleTheme() {
  const current = document.documentElement.getAttribute('data-theme');
  const next = current === 'dark' ? 'light' : 'dark';
  document.documentElement.setAttribute('data-theme', next);
  localStorage.setItem('theme', next);
}

// Smooth transition (add to CSS — but disable on first load)
function enableThemeTransition() {
  document.documentElement.style.setProperty(
    '--theme-transition', 'background-color 200ms ease, color 200ms ease'
  );
}
// Call after initial load, not before
window.addEventListener('load', enableThemeTransition);
```

---

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

## FOUC Prevention Checklist

```
Flash of Unstyled Content (FOUC) = user sees wrong theme for a frame on load.

Prevention:
  □ Theme detection script is INLINE in <head>
  □ Script is NOT async or deferred
  □ CSS transitions are disabled until after first paint
  □ data-theme attribute set before body renders
  □ CSS fallback: :root defaults to most common expected mode

Test:
  1. Set localStorage.theme = 'light'
  2. Hard refresh
  3. Page should load in light mode instantly — no dark flash
  4. Repeat with dark
```

---

## Theme Toggle UI

```html
<button
  class="theme-toggle"
  aria-label="Switch to light mode"
  onclick="toggleTheme()"
>
  <!-- sun icon -->
  <svg class="icon-light" aria-hidden="true">...</svg>
  <!-- moon icon -->
  <svg class="icon-dark"  aria-hidden="true">...</svg>
</button>
```

```css
.theme-toggle { min-width: 44px; min-height: 44px; } /* touch target */

[data-theme="dark"]  .icon-light { display: block; }
[data-theme="dark"]  .icon-dark  { display: none; }
[data-theme="light"] .icon-light { display: none; }
[data-theme="light"] .icon-dark  { display: block; }
```

Update aria-label on toggle:
```js
const btn = document.querySelector('.theme-toggle');
btn.setAttribute('aria-label',
  next === 'dark' ? 'Switch to light mode' : 'Switch to dark mode'
);
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
