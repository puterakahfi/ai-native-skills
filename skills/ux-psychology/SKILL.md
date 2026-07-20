---
name: ux-psychology
description: Behavioral and psychological UX analysis — cognitive load, habit loops, heuristics, Fitts's Law, Hick's Law, gestalt principles, and friction mapping. Finds why users struggle, not just what looks wrong.
license: MIT
metadata:
  ai-native-skills.version: 1.0.1
  ai-native-skills.author: puterakahfi
  ai-native-skills.type: skill
  ai-native-skills.implements: ai-native-core/contracts/skills/design/ux-psychology.contract.yaml
  ai-native-skills.contract-version: "~0.1"
---

# UX Psychology

## Reviewed core contract interface

Source: `ai-native-core/contracts/skills/design/ux-psychology.contract.yaml` · compatible line: `~0.1`

```yaml
required_inputs:
- ui_or_flow_to_analyze
allowed_outputs:
- cognitive_load_report
- habit_loop_analysis
- heuristic_violation_list
- behavioral_friction_map
- improvement_recommendations
quality_gates:
- findings_must_cite_specific_principle_not_just_opinion
- every_violation_must_have_actionable_recommendation
- cognitive_load_must_be_assessed_per_screen
- habit_loop_analysis_required_for_core_user_flows
- recommendations_must_be_prioritized_by_user_impact
- no_vague_feedback_like_confusing_or_overwhelming
```

Analyze the supplied UI or flow and return cognitive load, habit loop, heuristic violations, friction map, and prioritized improvements. Vague labels such as confusing or overwhelming are rejected unless tied to a specific principle and observable evidence.

Keep this interface synchronized with the pinned core contract. Exact declarations make ownership reviewable; they do not replace rendered, runtime, accessibility, or product evidence.

## Hard Rule

```
"Confusing" is not a finding. "Overwhelming" is not a finding.
Every finding must cite a principle and have an actionable fix.
```

## When to Use

- Design audit — why users drop off or struggle
- New feature UX review before implementation
- Onboarding/form/checkout flow critique
- Any flow where user behavior data shows friction

---

## Framework 1: Cognitive Load

| Type | Description | Design Problem |
|---|---|---|
| **Intrinsic** | Complexity of the task itself | Manage with progressive disclosure |
| **Extraneous** | Complexity added by bad design | Eliminate — unnecessary steps, unclear labels |
| **Germane** | Mental effort building useful mental model | Optimize — clear patterns, consistent behavior |

**Audit checklist:**
- [ ] How many decisions does the user face on this screen?
- [ ] Is information grouped by user mental model (not system model)?
- [ ] Are labels self-explanatory without needing docs?
- [ ] Does the screen require memory of previous screens?
- [ ] Is there visual noise that adds no meaning?

**Miller's Law:** Working memory holds ~7±2 chunks. >7 distinct decision elements = cognitive overload.

---

## Framework 2: Habit Loop (Hooked Model)

```
Trigger → Action → Variable Reward → Investment
```

| Stage | Question |
|---|---|
| **Trigger** | What cue brings user here? Is it clear? |
| **Action** | Is the action the simplest possible? (BJ Fogg: Motivation × Ability × Prompt) |
| **Variable Reward** | Does the user get a meaningful, slightly unpredictable reward? |
| **Investment** | Does the user put in data/content/social that increases future value? |

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
| 9 | **Help users recognize, diagnose, recover from errors** | Error message says "Error 500" not what happened + what to do |
| 10 | **Help and documentation** | No contextual help at the point of confusion |

---

## Framework 4: Fitts's Law + Hick's Law

**Fitts's Law** — time to click ∝ distance / size. Violations: small touch targets (<44px), primary CTA far from eye-land, destructive actions same size as constructive.

**Hick's Law** — decision time ∝ number of choices. Violations: 8+ top-level nav items, dropdowns with 20+ options (no search), all features exposed at once.

---

## Framework 5: Gestalt Principles

| Principle | Design Violation |
|---|---|
| **Proximity** | Unrelated elements grouped by accident |
| **Similarity** | Different actions look the same |
| **Continuity** | Visual flow broken by misaligned elements |
| **Figure/Ground** | Low contrast — user can't identify focal point |

**Figure/ground depth test:** Single color background + text = no depth; eye can't distinguish canvas from content. Fix: subtle texture, alternating section backgrounds (#0a0a0a vs #0f0f0f), 1px card borders, or top-to-bottom gradient.

**Color semantics:** One accent = one signal. Green for live status AND logo AND hover = semantic collapse.

---

## Output Format

```
UX PSYCHOLOGY AUDIT — <feature/screen>
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
| 2 items in 4-column grid | Gestalt completion — looks broken |
