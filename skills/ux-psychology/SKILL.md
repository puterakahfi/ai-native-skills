---
name: ux-psychology
description: Behavioral and psychological UX analysis — cognitive load, habit loops, heuristics, Fitts's Law, Hick's Law, gestalt principles, and friction mapping. Finds why users struggle, not just what looks wrong.
version: 1.0.0
author: puterakahfi
license: MIT
type: skill
implements: ai-native-core/contracts/skills/experience-design/ux-psychology.contract.yaml
---

# UX Psychology

## The Core Rule

```
"Confusing" is not a finding. "Overwhelming" is not a finding.
Every finding must cite a principle and have an actionable fix.
```

## When to Use

- Design audit — why users drop off or struggle
- New feature UX review before implementation
- Onboarding flow critique
- Form or checkout flow analysis
- Any flow where user behavior data shows friction
- Composing with `design-review` for a full design critique

---

## Framework 1: Cognitive Load

Cognitive load = mental effort required to use the interface.

**Three types:**
| Type | Description | Design Problem |
|---|---|---|
| **Intrinsic** | Complexity of the task itself | Can't reduce — manage with progressive disclosure |
| **Extraneous** | Complexity added by bad design | Eliminate — unnecessary steps, unclear labels |
| **Germane** | Mental effort building useful mental model | Optimize — clear patterns, consistent behavior |

**Audit checklist:**
- [ ] How many decisions does the user face on this screen?
- [ ] Is information grouped by user mental model (not system model)?
- [ ] Are labels self-explanatory without needing docs?
- [ ] Does the screen require memory of previous screens?
- [ ] Is there visual noise that adds no meaning?

**Heuristic:** Miller's Law — working memory holds ~7±2 chunks. If a screen presents more than 7 distinct elements requiring decision, it has cognitive overload.

---

## Framework 2: Habit Loop (Nir Eyal — Hooked Model)

For product flows meant to build user habits:

```
Trigger → Action → Variable Reward → Investment
```

| Stage | Question to Ask |
|---|---|
| **Trigger** | What internal/external cue brings user here? Is it clear? |
| **Action** | Is the action the simplest possible behavior? (BJ Fogg: Motivation × Ability × Prompt) |
| **Variable Reward** | Does the user get a meaningful, slightly unpredictable reward? |
| **Investment** | Does the user put something in (data, content, social) that increases future value? |

**Audit:** For each core flow — does it complete the loop, or does it break at a stage?

---

## Framework 3: Nielsen's 10 Heuristics

| # | Heuristic | Common Violation |
|---|---|---|
| 1 | **Visibility of system status** | No loading state, no confirmation after action |
| 2 | **Match between system and real world** | Technical jargon instead of user language |
| 3 | **User control and freedom** | No undo, no back, no cancel |
| 4 | **Consistency and standards** | Same action looks different in different places |
| 5 | **Error prevention** | Form submits without validation, irreversible actions without warning |
| 6 | **Recognition over recall** | User must remember info from previous screen |
| 7 | **Flexibility and efficiency** | No shortcuts for expert users |
| 8 | **Aesthetic and minimalist design** | Every extra element competes for attention |
| 9 | **Help users recognize, diagnose, recover from errors** | Error message says "Error 500" not "what happened + what to do" |
| 10 | **Help and documentation** | No contextual help at the point of confusion |

---

## Framework 4: Fitts's Law + Hick's Law

**Fitts's Law** — time to click a target ∝ distance / size.

Violations:
- Small touch targets (<44px on mobile)
- Primary CTA far from where user's eye lands
- Destructive actions (delete) same size/position as constructive actions

**Hick's Law** — decision time ∝ number of choices.

Violations:
- Navigation with 8+ top-level items
- Dropdowns with 20+ options, no search
- Dashboard showing all features at once instead of progressive disclosure

---

## Framework 5: Gestalt Principles

| Principle | What It Means | Design Violation |
|---|---|---|
| **Proximity** | Close items appear related | Unrelated elements grouped by accident |
| **Similarity** | Similar items appear related | Different actions look the same |
| **Continuity** | Eye follows paths | Visual flow broken by misaligned elements |
| **Closure** | Mind completes incomplete shapes | Incomplete UI patterns confuse users |
| **Figure/Ground** | Object vs background | Low contrast — user can't identify focal point |

---

## Output Format

```
UX PSYCHOLOGY AUDIT — <feature/screen>
───────────────────────────────────────
Roles active: ux-psychology

## Cognitive Load
SEVERITY: HIGH | MED | LOW
Finding: <specific observation>
Principle: <e.g. Miller's Law — 11 decision points on one screen>
Fix: <actionable recommendation>

## Habit Loop
Breaking at: <Trigger | Action | Variable Reward | Investment>
Finding: <specific observation>
Fix: <actionable recommendation>

## Heuristic Violations
H1 [Visibility]: <finding> → <fix>
H3 [User control]: <finding> → <fix>

## Fitts / Hick
<finding> → <fix>

## Gestalt
<finding> → <fix>

## Priority Fixes (by user impact)
P1: <most impactful>
P2: <next>
P3: <nice to have>
```

---

## Figure/Ground — Gestalt Extended

Figure/ground is not just about contrast — it is about depth and separation:

```
Flat background problem:
  Single color background (#0a0a0a) with text = no depth
  Eye cannot distinguish "canvas" from "content plane"
  Everything feels on the same layer

Solutions:
  A) Subtle texture (noise, grain, dot grid) — establishes ground plane
  B) Section backgrounds alternate slightly (#0a0a0a vs #0f0f0f)
  C) Cards with 1px border create figure on ground
  D) Gradient from #0a0a0a to #111111 top-to-bottom = subtle depth

Test: squint at the design — can you still tell what is foreground vs background?
If no → figure/ground is failing.
```

---

## Color Psychology in UI

Colors carry meaning before content is read:

```
Dark backgrounds:
  Pure black (#000)     → harsh, contrast fatigue on long reads
  Near black (#0a0a0a)  → sophisticated, intentional
  Dark grey (#111)      → neutral, readable

Accent color semantic rules:
  Green     → live, success, go, nature, positive
  Blue      → trust, information, interactive, calm
  Amber     → warning, energy, attention
  White     → clean, minimal, clarity

Danger: green accent used for BOTH live status AND logo dot AND hover state
        → user maps green to 3 meanings → semantic collapse

One accent = one signal. Always.
```

---

## Common Anti-Patterns

| Anti-Pattern | Principle Violated |
|---|---|
| Modal on page load | Cognitive load — intrudes before user has context |
| 3+ CTAs with equal visual weight | Hick's Law — forces decision |
| Confirm dialog: "Are you sure?" with OK/Cancel | Error prevention — user doesn't know consequence |
| Form error shown only after submit | Error prevention — should show inline |
| Empty state with no guidance | Visibility of system status |
| Onboarding that skips the habit trigger | Habit loop — no trigger = no return |
| 8px touch targets | Fitts's Law — impossible on mobile |
| Flat single-color background, no texture/depth | Figure/ground — no separation between canvas and content |
| Accent color with 3+ semantic roles | Color psychology — meaning collapses |
| Uniform padding on every section | Cognitive load — hierarchy disappears |
| Hero copy = job description | First impression 50ms — captures nothing memorable |
| 2 items in 4-column grid | Gestalt completion — looks broken, not intentionally minimal |
