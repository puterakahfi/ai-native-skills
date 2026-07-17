---
name: accessibility
description: WCAG 2.1 AA compliance and inclusive design — semantic HTML, ARIA roles, color contrast, keyboard navigation, focus management, screen reader compatibility, cognitive accessibility.
license: MIT
metadata:
  ai-native-skills.version: 1.1.0
  ai-native-skills.author: puterakahfi
  ai-native-skills.type: skill
  ai-native-skills.implements: ai-native-core/contracts/skills/experience-design/accessibility.contract.yaml
  ai-native-skills.related_skills: '["design-review", "ux-psychology", "master-design", "ethics-responsible-ai"]'
---

# Accessibility (A11y)

## ⛔ HARD RULES — Read First

```
1. Semantic HTML first — ARIA only when no semantic element exists.
2. Color alone is never sufficient — always pair with text / icon / pattern.
3. Every interactive element needs focus:visible and min 44×44 px touch target.
4. prefers-reduced-motion must be respected on ALL animations.
```

These rules are non-negotiable. They apply from the first line of code, not in a final "a11y pass."

---

## The Core Rule

```
Accessibility is not a feature. It is a constraint.

It applies from day one — not in a final "a11y pass".
WCAG 2.1 AA is the minimum legal baseline in most jurisdictions.

Design that is not accessible is not finished.
```

---

## WCAG 2.1 — Four Principles (POUR)

| Principle | Meaning | Reference |
|---|---|---|
| **P**erceivable | Information must be presentable in ways users can perceive | → load `references/perceivable-operable.md` §Perceivable |
| **O**perable | UI components must be operable by all users | → load `references/perceivable-operable.md` §Operable |
| **U**nderstandable | Information and UI operation must be understandable | → load `references/understandable-robust.md` §Understandable |
| **R**obust | Content must be interpretable by current and future assistive tech | → load `references/understandable-robust.md` §Robust |

**When to load references:**
- Implementing or reviewing contrast, alt text, non-text content → `references/perceivable-operable.md`
- Implementing or reviewing keyboard nav, focus management, focus visible → `references/perceivable-operable.md`
- Implementing or reviewing form errors, cognitive a11y, plain language → `references/understandable-robust.md`
- Implementing or reviewing semantic HTML, ARIA patterns → `references/understandable-robust.md`
- Running a full accessibility audit → `references/audit-checklist.md`

---

## Audit Checklist (summary)

Run the full checklist at `references/audit-checklist.md`. Key gates:

**Perceivable:** alt text ✓ | contrast 4.5:1 / 3:1 ✓ | no color-only info ✓ | captions ✓  
**Operable:** keyboard reachable ✓ | no trap ✓ | focus visible ✓ | focus managed on modal ✓  
**Understandable:** errors linked via aria-describedby ✓ | role="alert" ✓ | lang attr ✓  
**Robust:** semantic HTML ✓ | ARIA correct ✓ | tested with screen reader ✓  

---

## ⛔ HARD RULES — Reminder

```
1. Semantic HTML first — ARIA only when no semantic element exists.
2. Color alone is never sufficient — always pair with text / icon / pattern.
3. Every interactive element needs focus:visible and min 44×44 px touch target.
4. prefers-reduced-motion must be respected on ALL animations.
```
