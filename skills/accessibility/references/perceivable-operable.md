# Perceivable & Operable — A11y Reference

> Part of the `accessibility` skill. See `SKILL.md` for POUR overview and HARD RULES.

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

> **HARD RULE:** Color alone is never sufficient — always pair with text / icon / pattern.

---

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

**Rules:**
- If the image conveys information → write a meaningful alt
- If the image is purely decorative → use `alt=""`
- Never use `alt="image"`, `alt="photo"`, or the filename as alt text

---

### Non-Text Content

```html
<!-- Icon buttons must have accessible label -->

<!-- ❌ Screen reader reads: "button" -->
<button><svg>...</svg></button>

<!-- ✅ Screen reader reads: "Close dialog" -->
<button aria-label="Close dialog"><svg aria-hidden="true">...</svg></button>
```

**Rules for icons and SVGs:**
- Purely decorative SVG → `aria-hidden="true"`
- SVG that conveys meaning → `<title>` inside SVG or `aria-label` on the parent
- Icon-only buttons → always need `aria-label`

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

> **HARD RULE:** Every interactive element needs `focus:visible` and min 44×44 px touch target.

---

### Focus Management

```javascript
// Modal opens → move focus inside modal
function openModal() {
    modal.removeAttribute('hidden');
    const firstFocusable = modal.querySelector(
        'button, [href], input, select, textarea, [tabindex]:not([tabindex="-1"])'
    );
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

**Checklist:**
- [ ] Focus moves into modal when it opens
- [ ] Focus is trapped inside modal while open
- [ ] Focus returns to trigger element when modal closes
- [ ] Page-level focus not lost after dynamic content updates (SPA route changes)

---

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

/* ✅ Respect reduced motion — only suppress animated focus transitions */
@media (prefers-reduced-motion: reduce) {
    :focus-visible {
        transition: none;
    }
}
```

**Rules:**
- Never use `outline: none` without providing a visible alternative
- Focus ring must meet 3:1 contrast against adjacent colors
- Use `:focus-visible` (not `:focus`) to avoid showing ring on mouse click
- Always test: tab through every interactive element and verify ring is visible

> **HARD RULE:** `prefers-reduced-motion` must be respected on ALL animations — including focus transitions.
