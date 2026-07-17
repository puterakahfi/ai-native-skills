# Implementation

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

---

## Toggle Implementation

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

> **Note:** `aria-label` must describe the **next action**, not the current state.
> - Currently dark → label: "Switch to light mode"
> - Currently light → label: "Switch to dark mode"
