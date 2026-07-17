# Color & Spacing Tokens

> Reference for design-system SKILL.md Steps 1 & 2.
> Load this file when declaring color roles or spacing scale.

---

## Step 1: Declare Color Tokens

### Semantic Color Roles

Every color must have exactly one semantic role. Decide role first, pick value second.

| Role | Token Name | What It Means | Where Used |
|---|---|---|---|
| Canvas | `--bg` | Page background | `body` only |
| Canvas alt | `--bg-alt` | Alternate section | Section zebra pattern |
| Surface | `--surface` | Cards, modals, popovers | Elevated elements |
| Surface raised | `--surface-raised` | Tooltips, dropdowns | Above surface |
| Border | `--border` | Dividers, outlines | `border`, `outline` |
| Border subtle | `--border-subtle` | De-emphasized dividers | Secondary separators |
| Content primary | `--text-primary` | Main readable text | Body, labels |
| Content secondary | `--text-secondary` | Supporting text | Captions, meta |
| Content tertiary | `--text-tertiary` | De-emphasized | Placeholders, disabled |
| Content inverse | `--text-inverse` | Text on colored bg | On accent/danger |
| Accent | `--accent` | Brand / primary action | ONE purpose only |
| Accent hover | `--accent-hover` | Accent interaction state | Hover on accent |
| Success | `--success` | Positive, live, confirmed | LIVE badge, success state |
| Warning | `--warning` | Caution state | Warning badge |
| Danger | `--danger` | Error, destructive | Error state, delete |
| Interactive | `--interactive` | Links, clickable | Default link color |
| Interactive hover | `--interactive-hover` | Link hover | Hover state |

### Color Decision Protocol

```
When picking a color value:

1. What is the semantic role? → pick the right token name
2. Is there already a token for this role? → use it, do not add new
3. Dark theme vs light theme → define both in :root + [data-theme="light"]
4. Contrast check: text on background → must be ≥ 4.5:1 (AA)
5. Accent: is this the ONLY place accent is used? → if no, rename the role

Anti-patterns:
  ❌ Same hex value in 3 different variables → consolidate
  ❌ --accent used for: logo + hover + status + CTA → semantic collapse
  ❌ Picking hex first, naming it second → backwards, name role first
```

### Dark Theme Token Values (Sensible Defaults)

```css
:root {
  /* Canvas */
  --bg:              #0c0c0c;
  --bg-alt:          #111111;
  --surface:         #181818;
  --surface-raised:  #222222;

  /* Borders */
  --border:          #2a2a2a;
  --border-subtle:   #1e1e1e;

  /* Content */
  --text-primary:    #f0f0f0;
  --text-secondary:  #a0a0a0;
  --text-tertiary:   #555555;
  --text-inverse:    #0c0c0c;

  /* Brand */
  --accent:          #6366f1;   /* indigo */
  --accent-hover:    #818cf8;

  /* Status */
  --success:         #4ade80;   /* green — LIVE, positive */
  --warning:         #fb923c;   /* orange — caution */
  --danger:          #f87171;   /* red — error, destructive */

  /* Interactive */
  --interactive:     #a0a0a0;
  --interactive-hover: #f0f0f0;
}
```

---

## Step 2: Declare Spacing Tokens

### 8px Base Grid

All spacing from multiples of 4px. Every gap, padding, margin must be a token.

```css
:root {
  --space-1:  4px;
  --space-2:  8px;
  --space-3:  12px;
  --space-4:  16px;
  --space-5:  24px;
  --space-6:  32px;
  --space-7:  48px;
  --space-8:  64px;
  --space-9:  96px;
  --space-10: 128px;
  --space-11: 192px;
  --space-12: 256px;
}
```

### Spacing Decision: Which Token to Use

```
Inline gap between elements:    --space-2 to --space-4
Component internal padding:     --space-3 to --space-5
Component external margin:      --space-4 to --space-6
Section internal padding:       --space-7 to --space-9
Section-to-section gap:         --space-8 to --space-10
Page top/bottom margin:         --space-10 to --space-12

Rule: if two values are adjacent, their difference must be ≥ 1 step
(e.g. icon-to-label: --space-2, component: --space-4 — clear separation)
```
