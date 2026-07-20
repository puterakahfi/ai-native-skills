---
name: accessibility
description: WCAG 2.1 AA compliance and inclusive design — semantic HTML, ARIA roles, color contrast, keyboard navigation, focus management, screen reader compatibility, cognitive accessibility.
license: MIT
metadata:
  ai-native-skills.version: 1.1.1
  ai-native-skills.author: puterakahfi
  ai-native-skills.type: skill
  ai-native-skills.implements: ai-native-core/contracts/skills/design/accessibility.contract.yaml
  ai-native-skills.contract-version: "~0.1"
  ai-native-skills.related_skills: '["design-review", "ux-psychology", "master-design", "ethics-responsible-ai"]'
---

# Accessibility (A11y)

## Reviewed core contract interface

Source: `ai-native-core/contracts/skills/design/accessibility.contract.yaml` · compatible line: `~0.1`

```yaml
required_inputs:
- ui_component_or_page
allowed_outputs:
- accessibility_audit_report
- wcag_violation_list
- remediation_plan
- aria_recommendations
- keyboard_navigation_map
quality_gates:
- wcag_21_aa_is_minimum_baseline
- all_images_must_have_meaningful_alt_text
- color_contrast_must_meet_ratio_requirements
- all_interactive_elements_must_be_keyboard_accessible
- focus_management_must_be_explicit_on_dynamic_content
- aria_roles_must_be_correct_not_cosmetic
- form_errors_must_be_announced_to_screen_readers
- cognitive_accessibility_must_be_considered
```

Treat the supplied ui_component_or_page as evidence. Every meaningful image needs meaningful alternative text; decorative images must be explicitly hidden. Return the audit, violations, remediation, ARIA guidance, and keyboard map as separate evidence-bearing outputs.

Keep this interface synchronized with the pinned core contract. Exact declarations make ownership reviewable; they do not replace rendered, runtime, accessibility, or product evidence.

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
