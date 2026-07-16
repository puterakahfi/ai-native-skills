---
name: accessibility
description: WCAG 2.1 AA compliance and inclusive design — semantic HTML, ARIA roles, color contrast, keyboard navigation, focus management, screen reader compatibility, cognitive accessibility.
license: MIT
metadata:
  ai-native-skills.version: 1.0.0
  ai-native-skills.author: puterakahfi
  ai-native-skills.type: skill
  ai-native-skills.implements: ai-native-core/contracts/skills/experience-design/accessibility.contract.yaml
  ai-native-skills.related_skills: '[''design-review'', ''ux-psychology'', ''master-design'', ''ethics-responsible-ai'']'
---

# Accessibility (A11y)

## The Core Rule

```
Accessibility is not a feature. It is a constraint.

It applies from day one — not in a final "a11y pass".
WCAG 2.1 AA is the minimum legal baseline in most jurisdictions.

Design that is not accessible is not finished.
```

---

## WCAG 2.1 — Four Principles (POUR)

| Principle | Meaning |
|---|---|
| **P**erceivable | Information must be presentable in ways users can perceive |
| **O**perable | UI components must be operable by all users |
| **U**nderstandable | Information and UI operation must be understandable |
| **R**obust | Content must be interpretable by current and future assistive tech |

---

## Perceivable

### Color Contrast Ratios

```
WCAG AA minimum:
  Normal text (< 18pt):   4.5:1 ratio
  Large text (≥ 18pt):    3.0:1 ratio
  UI components:           3.0:1 ratio against adjacent colors

Tools: WebAIM Contrast Checker, browser DevTools accessibility panel

❌ Fail: #767676 on #ffffff = 4.48:1 (barely below normal text threshold)
✅ Pass: #595959 on #ffffff = 7.0:1
```

### Alt Text

```html
<!-- ❌ Missing alt -->
<img src="order-confirmed.png">

<!-- ❌ Useless alt -->
<img src="order-confirmed.png" alt="image">

<!-- ✅ Meaningful alt -->
<img src="order-confirmed.png" alt="Order confirmed — your order #12345 has been placed">

<!-- ✅ Decorative image — empty alt tells screen reader to skip -->
<img src="decorative-divider.png" alt="">
```

### Non-Text Content

```html
<!-- Icon buttons must have accessible label -->
<!-- ❌ Screen reader reads: "button" -->
<button><svg>...</svg></button>

<!-- ✅ Screen reader reads: "Close dialog" -->
<button aria-label="Close dialog"><svg aria-hidden="true">...</svg></button>
```

---

## Operable

### Keyboard Navigation

Every interactive element must be reachable and operable via keyboard alone.

```
Tab        → move focus forward
Shift+Tab  → move focus backward
Enter      → activate button/link
Space      → toggle checkbox, activate button
Arrow keys → navigate within component (menu, tabs, listbox)
Escape     → close modal/dropdown

Test: unplug mouse, navigate entire flow using keyboard only.
```

```html
<!-- ❌ Div button — not keyboard accessible -->
<div onclick="handleClick()" style="cursor:pointer">Submit</div>

<!-- ✅ Real button — keyboard accessible, screen reader announces role -->
<button type="submit" onclick="handleClick()">Submit</button>

<!-- ✅ If div is necessary, add tabindex + keydown -->
<div
  role="button"
  tabindex="0"
  onclick="handleClick()"
  onkeydown="if(event.key==='Enter'||event.key===' ')handleClick()"
>Submit</div>
```

### Focus Management

```javascript
// Modal opens → move focus inside modal
function openModal() {
    modal.removeAttribute('hidden');
    const firstFocusable = modal.querySelector('button, [href], input, select, textarea, [tabindex]:not([tabindex="-1"])');
    firstFocusable?.focus();
}

// Modal closes → return focus to trigger
function closeModal(triggerElement) {
    modal.setAttribute('hidden', '');
    triggerElement.focus();  // return focus to where user was
}

// Trap focus inside modal
modal.addEventListener('keydown', (e) => {
    if (e.key !== 'Tab') return;
    const focusable = modal.querySelectorAll('button, [href], input, select, textarea');
    const first = focusable[0];
    const last  = focusable[focusable.length - 1];
    if (e.shiftKey && document.activeElement === first) { e.preventDefault(); last.focus(); }
    if (!e.shiftKey && document.activeElement === last) { e.preventDefault(); first.focus(); }
});
```

### Focus Visible

```css
/* ❌ Never remove focus outline without replacement */
:focus { outline: none; }

/* ✅ Custom focus style that meets contrast requirements */
:focus-visible {
    outline: 2px solid #0066cc;
    outline-offset: 2px;
    border-radius: 2px;
}
```

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

---

## Robust

### Semantic HTML First

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

### ARIA — Use Correctly

```
ARIA rules:
  1. No ARIA is better than bad ARIA
  2. Never override native semantics unless necessary
  3. All interactive ARIA widgets must be keyboard operable
  4. Don't use role on everything — most HTML elements have implicit roles

Common correct usage:
  aria-label     → name for element with no visible text
  aria-labelledby → name from another element's text
  aria-describedby → supplementary description
  aria-expanded  → open/closed state of expandable widget
  aria-live      → announce dynamic content changes
  role="alert"   → urgent message, announced immediately
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

---

## Accessibility Audit Checklist

Perceivable:
- [ ] All images have meaningful alt text (or empty alt if decorative)?
- [ ] Color contrast meets WCAG AA (4.5:1 normal text, 3:1 large/UI)?
- [ ] Information not conveyed by color alone?
- [ ] Video content has captions?

Operable:
- [ ] All interactive elements keyboard accessible (Tab + Enter + Space)?
- [ ] No keyboard trap (can always Tab out)?
- [ ] Focus indicator visible at all times?
- [ ] Focus managed correctly when modal opens/closes?
- [ ] No content flashes more than 3 times/second (seizure risk)?

Understandable:
- [ ] Form errors associated with their input (aria-describedby)?
- [ ] Errors announced to screen reader (role="alert" or aria-live)?
- [ ] Page language declared (`<html lang="en">`)?
- [ ] Plain language used for error messages?

Robust:
- [ ] Semantic HTML used (header, nav, main, footer, button, etc.)?
- [ ] ARIA roles used correctly — not overriding native semantics?
- [ ] Interactive ARIA widgets keyboard operable?
- [ ] Tested with screen reader (VoiceOver / NVDA / JAWS)?
