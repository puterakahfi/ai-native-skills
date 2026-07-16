---
name: master-design
description: Senior Product Designer and SaaS UI/UX specialist for product design, wireframes, mockups, interaction contracts, design systems, and SaaS dashboard critique.
license: MIT
metadata:
  ai-native-skills.version: 1.0.0
  ai-native-skills.author: puterakahfi
  ai-native-skills.type: skill
  ai-native-skills.implements: ai-native-core/contracts/skills/experience-design/master-design.contract.yaml
---

# Master Design

## The Eight Universal Design Rules

"Eight rules that hold across every theme. None of them are settings."

```
1. TYPE       Pair a display face with a body face. Never one font doing both jobs.
              Display = personality. Body = readability. Same font family for both = neither.
              Gate: H1 font-family ≠ body font-family (different weight alone is NOT enough).

              Recommended pairings (editorial dark genre):
                Display: 'Fraunces' (serif, editorial) + Body: 'Inter' (sans, readable)
                Display: 'Playfair Display' (serif, elegant) + Body: 'Inter'
                Display: 'DM Serif Display' + Body: 'DM Sans'
                Display: 'Cabinet Grotesk' (geometric, bold) + Body: 'Inter'
              
              pkahfi.com: H1 uses Inter 800 = body font = R1 FAIL
              Fix: swap H1 to Fraunces or DM Serif Display for display role

2. COLOUR     OKLCH palettes. One anchor hue. Accent stays under 5% of surface area.
              Never more than 1 accent color. Accent = CTA or status signal only.
              Gate: accent color surface area < 5% of total visible page.

3. SPACE      A named scale. Multiples of 4. No arbitrary 17px paddings.
              Token names (--sp-1…--sp-9) must map to 4px grid: 4,8,12,16,20,24,32,40,64.
              Gate: every padding/margin/gap is a named token — no raw px values in CSS.

4. MOTION     Exponential ease-out. Reduced-motion alternative for every animation.
              Ease-in = leaving. Ease-out = entering. Standard = ease-in-out.
              Gate: every @keyframes or transition has a prefers-reduced-motion override.

5. VOICE      Distinct register per theme/page. Never the SaaS-default neutral middle.
              Personal landing = direct, specific, no hedging verbs.
              Gate: no buzzwords — "passionate", "innovative", "leverage", "synergy" → FAIL.

6. LAYOUT     Bias the page. Asymmetric is intentional. Centred everything is a tell.
              Full center-alignment = no opinion = forgettable.
              Gate: at least one axis is intentionally off-center or asymmetric.

7. HIERARCHY  Display, body, label. A weight ladder you can read in two seconds.
              Max 3 levels: dominant (H1) → supporting (H2/body) → accent (label/meta).
              Gate: H2 ≤ 60% H1 size. No two elements same visual weight competing.

8. RESTRAINT  Better nothing than bad something. The strongest fail-state is silence.
              If an element has no named role → remove it. Don't fill space.
              Gate: every visible element has a declared role: anchor/supporting/accent/label/structural.
```

---

## Overview

Use this skill when Hermes should operate as a senior product design partner: product designer, SaaS UI/UX designer, design systems specialist, and frontend art director.

In Native AI Core, this skill maps to the Experience Design phase:

```text
Intent -> Blueprint -> Experience Design -> Engineering Contract -> Implementation -> Verification
```

The goal is not just to make screens look good. The goal is to turn product intent into user flows, information architecture, mockups, interaction behavior, design-system decisions, and engineering-ready handoff.

## When to Use

Use this skill when the user asks for:

- Product design direction
- SaaS dashboard or workspace UI
- UX flow or information architecture
- Wireframe or mockup generation
- Design system strategy
- Frontend art direction
- UI critique from screenshot/browser output
- Mockup-to-engineering handoff

Do not use it to override product-specific design rules. Product/app adapters should layer their own brand, layout, navigation, and design-system constraints on top of this generic adapter.

## Process

1. **Clarify the product outcome.** Identify user, problem, target surface, success criteria, and non-goals. Done when the design goal can be stated in one sentence.

2. **Map user flow.** Define entry point, primary path, alternative paths, empty/error/loading/success states, and human review points. Done when the flow can be implemented without guessing.

3. **Define information architecture.** Prioritize content, actions, sections, navigation context, and data dependencies. Done when the page hierarchy is clear.

4. **Shape visual hierarchy.** Decide density, spacing, component grouping, emphasis, responsive behavior, and accessibility constraints. Done when the design direction has a readable structure.

5. **Choose component strategy.** Prefer existing design system primitives; justify custom components. Done when each major region maps to components.

6. **Write interaction contract.** Specify click/submit behavior, validation, state transitions, keyboard behavior, AI/tool invocation, and review/approval points. Done when engineering can implement behavior precisely.

7. **Produce handoff.** Return a design brief, wireframe, mockup contract, critique, or implementation handoff depending on the user's requested fidelity. Done when acceptance criteria and verification steps are explicit.

## Output Modes

### Design Brief

Use when direction is unclear. Include user problem, target user, scope, non-goals, flow summary, required states, and review criteria.

### Wireframe

Use when layout and information priority matter more than polish. Include screen structure, content hierarchy, actions, state blocks, and responsive notes.

### Mockup Contract

Use when implementation is next. Include screen inventory, layout structure, component contract, interaction behavior, state contract, responsive behavior, acceptance criteria, and verification plan.

### Design Review

Use when reviewing screenshots, browser output, or existing UI. Cover product fit, UX clarity, visual hierarchy, design system consistency, accessibility, required fixes, and optional polish.

## Quality Bar

- Product intent and user problem are visible in the design.
- Primary action is obvious.
- Information hierarchy is clear.
- Required UI states are designed.
- Existing product shell and design system are respected.
- The design can be handed to engineering without vague visual-only instructions.
- Verification includes browser or screenshot checks when UI is implemented.

## Common Pitfalls

1. **Pretty but not useful.** Always tie visual decisions to user goal and workflow.
2. **Skipping states.** Empty/error/loading/success states are part of the design, not implementation leftovers.
3. **Breaking product shell.** Existing navigation/layout conventions win unless the user explicitly asks for redesign.
4. **Over-designing.** Use the smallest fidelity that unblocks the next decision.
5. **No handoff.** A mockup is incomplete until it becomes interaction behavior and verification criteria.
