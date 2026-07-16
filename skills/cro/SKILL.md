---
name: cro
version: 1.0.0
type: skill
description: >
  Conversion Rate Optimization — attention flow, trust signals, friction audit,
  above-fold optimization, and persuasion architecture for landing pages.
tags: [cro, conversion, persuasion, trust, attention, landing-page]
---

# CRO — Conversion Rate Optimization

## When to Load

Load when:
- Any page has a goal (contact, hire, read, click)
- Auditing whether a landing page converts its intended audience
- "Does this page make someone take action?"
- Portfolio pages where the goal is getting hired or contacted

Note: CRO ≠ only e-commerce. For a portfolio, conversion = someone sends an email
or remembers you. The principles are identical.

---

## The Attention Economy Model

Visitor gives you ~3–8 seconds before deciding to stay or leave.
Every element above the fold must earn the next second of attention.

```
Second 0–1: WHO IS THIS?           → Name/brand legible immediately
Second 1–3: WHAT DO THEY DO?       → Role/stance readable without scroll
Second 3–5: DO I TRUST THEM?       → Evidence, specificity, live work
Second 5–8: WHAT SHOULD I DO?      → Clear next action (scroll, click, contact)

If any second is wasted → bounce probability doubles.
Dead space above hero wastes seconds 0–1 entirely.
```

---

## Trust Signal Architecture

Trust is built in layers. Each layer must be present before the next matters.

```
Layer 1: COMPETENCE SIGNALS
  → Named, specific work (not "various projects")
  → Live products (not "coming soon")
  → Technical specificity (stack, architecture, named concepts)

Layer 2: CONSISTENCY SIGNALS
  → Consistent visual system (not mix of styles)
  → Consistent tone (not formal headline + casual bio)
  → Contact info present (not hidden)

Layer 3: CREDIBILITY SIGNALS
  → Specificity of claims ("maintainable five years later" > "high quality")
  → Named methodologies (DDD, hexagonal, bounded contexts)
  → Evidence that matches claim (Blueprint = architecture doc = proves the claim)

Layer 4: SOCIAL PROOF (optional for portfolio)
  → Employers, clients, open source contributions
  → If absent: compensate with stronger Layer 1–3

Rule: Do not add Layer 4 if Layer 1–3 are weak. Testimonials on a vague page = noise.
```

---

## Friction Audit

Friction = anything that makes the intended action harder than it needs to be.

### Cognitive Friction
```
□ Too many choices above fold → decision paralysis
  Fix: one primary action per section
□ Jargon without context → visitor excludes themselves
  Fix: one plain sentence per technical claim
□ Long paragraphs → skipping → missed message
  Fix: ≤ 3 sentences per paragraph, ≤ 45 words per bio
```

### Navigation Friction
```
□ Nav items that don't reflect page sections → confusion
□ Nav without visual anchor on scroll → lost
□ Mobile nav hidden behind non-obvious icon → friction
  Fix: hamburger must be visible, labeled, 44×44px minimum
```

### Contact Friction
```
□ Contact form with >3 fields → abandonment
  Fix: email link is always lower friction than a form
□ Contact hidden in footer → missed
  Fix: contact in nav + contact section + footer
□ "Get in Touch" → too corporate → reduces click rate
  Fix: "hi@pkahfi.com" or "Let's talk." + direct email link
```

---

## Above-Fold Optimization

The most CRO-critical real estate. Every pixel must pull weight.

```
Must be present above fold:
  □ Name / brand — immediately readable (H1, high contrast)
  □ Role or value prop — one sentence
  □ One signal of credibility (live work, specific claim, or named client)
  □ One clear next action (scroll cue, nav, or contact link)

Must NOT be present above fold:
  □ Unframed dead space > 20% of viewport
  □ Decorative elements that delay reading the name
  □ Navigation that competes with hero for visual weight
  □ Auto-playing video or animation that slows load + distracts
```

### The 5-Second Test (self-audit)
```
Cover everything below the fold.
After 5 seconds, answer:
  1. Whose page is this?
  2. What do they do?
  3. Is there evidence they're good at it?
  4. What should I do next?

If you can't answer all 4 → above-fold fails CRO audit.
```

---

## Persuasion Architecture

The sequence in which information is presented determines conversion.

```
Optimal sequence for personal portfolio (no CTA):

  1. IDENTITY ANCHOR     → Name, immediate
  2. ROLE SIGNAL         → What they do, one sentence
  3. WORLDVIEW CLAIM     → How they think (stance) — creates resonance
  4. EVIDENCE            → Work — proves the claim
  5. DEPTH               → About — for visitors who want more
  6. ACCESS              → Contact — low friction

Anti-patterns:
  × About before Work    → asks trust before giving evidence
  × Work before Identity → visitor doesn't know who to attribute work to
  × Contact before Work  → premature ask
  × Multiple competing H1s — dilutes identity signal
```

---

## For Portfolio Pages (no explicit CTA)

Goal: visitor leaves remembering the name + feeling confident in ability.
Micro-conversion: they save the email, forward the link, or come back.

```
Portfolio CRO checklist:
  □ Name is the single most memorable element on the page
  □ Work entries link to live products (not GitHub readme or Figma file)
  □ Each work entry has a description that adds info beyond the title
  □ Contact is one click from anywhere on the page
  □ Page loads in < 3s (performance = trust signal)
  □ No broken links (broken link = broken trust)
  □ Social links open in new tab (don't pull visitor away)
```

---

## Gates

```
Gate CRO1: Above-Fold Optimization (5-second test)
  □ Name readable immediately
  □ Role/value prop visible without scroll
  □ One credibility signal present above fold
  □ One clear next action present
  Score: __ / 10

Gate CRO2: Trust Signal Completeness
  □ Layer 1 (competence): live work, specificity
  □ Layer 2 (consistency): visual system, tone
  □ Layer 3 (credibility): specific claims with matching evidence
  Score: __ / 10

Gate CRO3: Friction Audit
  □ Cognitive: ≤ 1 primary action per section
  □ Navigation: accessible on all viewports
  □ Contact: ≤ 1 click, no form required
  Score: __ / 10

Gate CRO4: Persuasion Sequence
  □ Identity → Role → Worldview → Evidence → Depth → Access
  □ No anti-pattern ordering
  Score: __ / 10
```
