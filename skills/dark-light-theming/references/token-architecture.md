# Token Architecture

## Core Principle

```
One semantic token table. Two primitive maps.

semantic token (--text-primary)
  → dark mode:  #f0f0f0
  → light mode: #111111

Never:
  color: #f0f0f0           ← hardcoded, breaks in light mode
  color: var(--dark-text)  ← mode-specific var, semantic collapse

Always:
  color: var(--text-primary)  ← semantic, works in both modes
```

---

## Layer 1: Primitive Tokens (raw values)

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

---

## Layer 2: Semantic Tokens (mapped to primitives)

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
