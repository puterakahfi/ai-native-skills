# Understandable & Robust — A11y Reference

> Part of the `accessibility` skill. See `SKILL.md` for POUR overview and HARD RULES.

---

## Understandable

### Form Error Handling

```html
<!-- ❌ Error not announced to screen reader -->
<input type="email" class="error">
<span style="color:red">Invalid email</span>

<!-- ✅ Error associated with input, announced on change -->
<label for="email">Email address</label>
<input
    type="email"
    id="email"
    aria-describedby="email-error"
    aria-invalid="true"
>
<span id="email-error" role="alert">
    Enter a valid email address (e.g. name@example.com)
</span>
```

**Rules:**
- Always link error message to its input via `aria-describedby`
- Set `aria-invalid="true"` on the input when it has an error
- Use `role="alert"` on the error container so screen readers announce it immediately
- Error message must be visible text — never color alone
- Provide an example of valid input in the error message when format matters

**Full form validation pattern:**
```html
<form novalidate>
    <div class="field">
        <label for="phone">Phone number <span aria-hidden="true">*</span><span class="sr-only">(required)</span></label>
        <input
            type="tel"
            id="phone"
            name="phone"
            required
            aria-required="true"
            aria-describedby="phone-hint phone-error"
        >
        <span id="phone-hint" class="hint">Format: +1 (555) 000-0000</span>
        <span id="phone-error" role="alert" class="error" hidden></span>
    </div>
</form>
```

---

### Cognitive Accessibility

```
Plain language:
  ❌ "The authentication credentials provided were not recognized by the system"
  ✅ "Wrong email or password. Please try again."

Predictable patterns:
  - Navigation stays in same place on every page
  - Links that look the same do the same thing
  - No unexpected context changes (page refresh on focus, auto-submit on select)

Error prevention:
  - Confirm before destructive actions
  - Allow undo
  - Input validation before submit, not after
```

**Checklist:**
- [ ] Error messages use plain language (< 8th grade reading level)
- [ ] Destructive actions require confirmation
- [ ] Navigation is consistent across pages
- [ ] No auto-submit, auto-redirect, or context change on focus
- [ ] Timeout warnings give users ≥ 20 seconds to respond
- [ ] Page title describes the current page (not just the app name)

---

## Robust

### Semantic HTML First

> **HARD RULE:** Semantic HTML first — ARIA only when no semantic element exists.

```html
<!-- ❌ Divs for everything — no semantic meaning for screen readers -->
<div class="header">
  <div class="nav">
    <div class="nav-item">Products</div>
  </div>
</div>

<!-- ✅ Semantic HTML — screen readers understand structure -->
<header>
  <nav aria-label="Main navigation">
    <ul>
      <li><a href="/products">Products</a></li>
    </ul>
  </nav>
</header>
```

**Landmark elements:**
| HTML Element | Implicit ARIA Role | Use for |
|---|---|---|
| `<header>` | `banner` | Site-wide header |
| `<nav>` | `navigation` | Navigation blocks |
| `<main>` | `main` | Primary page content |
| `<footer>` | `contentinfo` | Site-wide footer |
| `<aside>` | `complementary` | Secondary content |
| `<section>` | `region` (needs label) | Thematic grouping |
| `<article>` | `article` | Self-contained content |
| `<button>` | `button` | All interactive triggers |

**Use `<button>` for actions, `<a href>` for navigation. Never swap them.**

---

### ARIA — Use Correctly

```
ARIA rules:
  1. No ARIA is better than bad ARIA
  2. Never override native semantics unless necessary
  3. All interactive ARIA widgets must be keyboard operable
  4. Don't use role on everything — most HTML elements have implicit roles

Common correct usage:
  aria-label      → name for element with no visible text
  aria-labelledby → name from another element's text
  aria-describedby → supplementary description
  aria-expanded   → open/closed state of expandable widget
  aria-live       → announce dynamic content changes
  role="alert"    → urgent message, announced immediately
```

```html
<!-- ✅ Tabs with correct ARIA -->
<div role="tablist" aria-label="Account settings">
    <button role="tab" aria-selected="true" aria-controls="profile-panel" id="profile-tab">Profile</button>
    <button role="tab" aria-selected="false" aria-controls="billing-panel" id="billing-tab">Billing</button>
</div>
<div role="tabpanel" id="profile-panel" aria-labelledby="profile-tab">...</div>
<div role="tabpanel" id="billing-panel" aria-labelledby="billing-tab" hidden>...</div>
```

**Common ARIA mistakes to avoid:**
- `role="button"` on `<button>` — redundant
- `aria-label` on `<div>` with no role — ignored by screen readers
- `aria-hidden="true"` on a focusable element — traps keyboard users
- `role="presentation"` on an interactive element — removes its semantics
- `aria-live="assertive"` for non-urgent updates — interrupts screen reader

**Screen reader testing matrix:**

| Screen Reader | Browser | Platform |
|---|---|---|
| VoiceOver | Safari | macOS / iOS |
| NVDA | Firefox / Chrome | Windows |
| JAWS | Chrome / Edge | Windows |
| TalkBack | Chrome | Android |
