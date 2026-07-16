---
name: design-review
description: Design system compliance reviewer and AI slop detector — checks UI design and implementation against the product design system contract. Catches generic templates, one-off styles, visual direction drift, and AI-generated slop before it ships.
version: 1.0.0
author: puterakahfi
license: MIT
implements: ai-native-core/contracts/skills/experience-design/design-review.contract.yaml
---

# Design Review

## The Core Rule

```
No UI output — designed or generated — passes review
without being checked against the Product Design System Contract.
"Make it clean and modern" is not a design contract.
```

## When to Use

- Before shipping any new page or component
- After AI generates UI code or mockup
- When a new component is proposed
- When visual direction feels "off"
- When reviewing a PR that touches UI
- When evaluating a design from a new team member or agent

## Prerequisites

1. Load the product's `product-ui-design-system-contract.yaml` before starting
2. Have the design artifact, mockup, or UI code diff ready

---

## Review Checklist

### 1. Visual Direction Compliance

Check against `visual_direction` in the design contract:

- [ ] Feels like the declared style (e.g. "clean_blue_saas", "minimal_dashboard")?
- [ ] Matches declared personality traits?
- [ ] Does NOT feel like any item in `must_not_feel_like`?

**Slop signal:** Generic, could-be-any-product feel. Interchangeable with a random admin template.

---

### 2. AI Slop Detection

These patterns indicate AI-generated slop — auto-flag for review:

**Visual slop:**
- Gradient hero sections on a dashboard product
- Glassmorphism used without product precedent
- Random card shadows inconsistent with token system
- "Modern" icons that don't match icon system
- Color usage that doesn't map to any design token

**Template slop:**
- Sidebar + topbar + metric cards combo copy-pasted from a generic template
- "Welcome back, User!" hero text on an operational tool
- Random testimonial or pricing section appearing in a product UI
- AI-generated landing page structure applied to a dashboard

**Typography slop:**
- Font sizes not from typography token system
- Random `font-weight: 600` or `font-size: 13px` inline styles
- Mixed font families not defined in contract

---

### 3. Component Reuse vs One-Off Styles

- [ ] Uses required components from design contract?
- [ ] No new one-off page-level components that duplicate existing ones?
- [ ] No `style={{ color: '#3b82f6' }}` hardcoded colors?
- [ ] No ad-hoc `className="text-[13px] font-medium leading-[1.4]"`?

**Violation signal:** Any inline style or Tailwind arbitrary value that maps to an existing token.

---

### 4. Color Token Compliance

- [ ] All colors reference token roles (bgApp, bgSurface, accentBlue, etc)?
- [ ] No hardcoded hex values?
- [ ] No new color introduced without design contract update?
- [ ] Status colors follow status badge rules?

---

### 5. Layout Pattern Compliance

- [ ] Page uses declared layout patterns (app_shell, command_center_page, etc)?
- [ ] No arbitrary new layout invented for one page?
- [ ] Information density matches product direction?

---

### 6. Status & Semantic Rules

- [ ] Status badges follow status_rules in contract?
- [ ] Loading/error/empty states use declared patterns?
- [ ] No custom status color invented without contract update?

---

### 7. Responsive Rules

- [ ] Follows declared responsive breakpoints?
- [ ] Mobile view follows stacked/compact pattern defined in contract?
- [ ] No desktop-only layout shipped without mobile consideration?

---

### 8. Accessibility Baseline

- [ ] Text contrast meets readable_contrast rule?
- [ ] Focus states visible?
- [ ] Semantic heading hierarchy followed?
- [ ] Interactive elements keyboard accessible?

---

## Verdict Format

```
DESIGN REVIEW VERDICT
─────────────────────
Status: PASS | FAIL | PASS WITH FLAGS

Slop Detected:
  - [BLOCKING] <description>
  - [WARNING]  <description>

Visual Direction: ALIGNED | DRIFTED
  → Drift reason: <if drifted>

Token Violations:
  - <element> uses hardcoded <value> → should use <token>

Component Issues:
  - <component> is a one-off duplicate of <existing component>

Recommendation:
  <summary of what must change before shipping>
```

## AI Slop Smell Detector

These outputs from AI agents justify an immediate design review request:

- Any UI that "looks professional" but has no token references
- Gradient + glassmorphism + rounded cards combo on a B2B SaaS product
- "Clean and modern" as the only design direction given to the agent
- New page that matches zero declared layout patterns
- Component that hardcodes colors, spacing, and font sizes inline
- UI generated from a generic template prompt, not from the design contract

## Common Anti-Patterns (Auto-Fail)

| Anti-Pattern | Why It Fails |
|---|---|
| `color: '#3b82f6'` hardcoded | Token system violation |
| New page with custom sidebar layout | Layout pattern violation |
| Status badge with custom red/green | Status badge rule violation |
| Glassmorphism card on clean SaaS product | Visual direction violation |
| Copy-pasted landing page hero in dashboard | Template slop |
| `font-size: 13px` inline | Typography token violation |
| "AI generated it, looks good to me" | Design contract not consulted |

## Intentionality Test

For every design decision, ask:

> **"Was this intentional per the design contract, or was it just what the AI produced?"**

If you cannot answer "intentional" with a contract reference — it fails.
