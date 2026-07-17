# Accessibility Audit Checklist

> Part of the `accessibility` skill. Run this checklist before marking any UI as complete.
> Full implementation guidance in `references/perceivable-operable.md` and `references/understandable-robust.md`.

---

## Perceivable

- [ ] All images have meaningful alt text (or `alt=""` if decorative)?
- [ ] Color contrast meets WCAG AA (4.5:1 normal text, 3:1 large text / UI components)?
- [ ] Information not conveyed by color alone (paired with text / icon / pattern)?
- [ ] Video content has captions?
- [ ] Audio content has transcripts?
- [ ] Icon-only buttons have `aria-label` or visible text equivalent?

---

## Operable

- [ ] All interactive elements keyboard accessible (Tab + Enter + Space)?
- [ ] No keyboard trap (can always Tab out of every component)?
- [ ] Focus indicator visible at all times (never `outline: none` without replacement)?
- [ ] Focus indicator meets 3:1 contrast against adjacent colors?
- [ ] Focus managed correctly when modal opens (focus moves in) and closes (focus returns)?
- [ ] Focus not lost after dynamic content updates (SPA route changes, AJAX loads)?
- [ ] No content flashes more than 3 times/second (seizure risk — WCAG 2.3.1)?
- [ ] All interactive elements have minimum 44×44 px touch target?
- [ ] `prefers-reduced-motion` respected on all CSS/JS animations?

---

## Understandable

- [ ] Form errors associated with their input via `aria-describedby`?
- [ ] Errors announced to screen reader (`role="alert"` or `aria-live="polite"`)?
- [ ] `aria-invalid="true"` set on inputs with errors?
- [ ] Page language declared (`<html lang="en">`)?
- [ ] Plain language used for error messages (no jargon, clear next step)?
- [ ] Navigation consistent across pages (no unexpected location changes)?
- [ ] No auto-submit, auto-redirect, or context change on focus / select?
- [ ] Destructive actions require confirmation?
- [ ] Page `<title>` describes the current page?

---

## Robust

- [ ] Semantic HTML used (`<header>`, `<nav>`, `<main>`, `<footer>`, `<button>`, etc.)?
- [ ] `<button>` for actions, `<a href>` for navigation — not swapped?
- [ ] ARIA roles used correctly — not overriding native semantics?
- [ ] No `aria-hidden="true"` on focusable elements?
- [ ] Interactive ARIA widgets keyboard operable (tabs, listbox, combobox, etc.)?
- [ ] `aria-expanded`, `aria-selected`, `aria-checked` states kept in sync with UI?
- [ ] Tested with screen reader (VoiceOver / NVDA / JAWS)?
- [ ] Tested with keyboard only (mouse unplugged)?
- [ ] Tested at 200% browser zoom (no content loss or overlap)?

---

## Sign-off

| Check | Tester | Date |
|---|---|---|
| Manual keyboard test | | |
| Screen reader test (VoiceOver or NVDA) | | |
| Automated scan (axe / Lighthouse) | | |
| Color contrast verified | | |
| 200% zoom test | | |
