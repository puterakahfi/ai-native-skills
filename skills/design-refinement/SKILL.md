---
name: design-refinement
description: Targeted design improvement workflow — fix specific failing gates without full redesign, verify the result, and automatically promote reusable lessons into skills through skill-evolution.
license: MIT
metadata:
  ai-native-skills.version: 1.2.0
  ai-native-skills.author: puterakahfi
  ai-native-skills.type: workflow
  ai-native-skills.requires: "design-audit design-review master-design skill-evolution skill-eval"
  ai-native-skills.implements: ai-native-core/contracts/skills/quality/design-refinement.contract.yaml
  ai-native-skills.contract-version: "^1.0.0"
  ai-native-skills.related_skills: '["design-audit","design-review","redesign-workflow","master-design","skill-evolution","skill-eval","ui-components","accessibility","readability","responsiveness"]'
---

# Design Refinement

Targeted gate-fix loop. Preserve the correct design direction, fix declared failures, verify the real result, and review every verified fix for reusable learning.

This adapter implements `ai-native-core/contracts/skills/quality/design-refinement.contract.yaml`. The core contract owns runtime-agnostic phases and gates. This adapter owns concrete inspection, patch discipline, visual and interaction verification, automatic learning promotion, score reporting, and handoff to `redesign-workflow` when refinement is the wrong lifecycle.

## Hard rules

```text
1. Classify before patching: identify the governing skill and correct correction layer.
2. Verify before promotion: never update a shared skill from an unverified idea.
3. Preserve: do not change what is already passing (>= 8.0).
4. Scope: fix declared gates only; no drive-by redesign.
5. Learn automatically: after every verified fix, run skill-evolution.
6. Eval required: every promoted shared lesson needs regression evidence.
7. Patch safety: after two failed patches on the same region, reread and plan; never blindly apply a third patch.
```

## When to use

Use `design-refinement` when:

- the design direction is correct, normally overall average `>= 7.0`;
- specific gates are failing below `8.0`;
- the user approves the direction but wants targeted issues fixed.

Use `redesign-workflow` instead when:

- overall average is below `7.0`;
- multiple critical gates are below `5.0`;
- the direction or macrostructure itself is wrong.

Use `design-audit` first when the failing gates are not yet known.

## Parameters

| Parameter | Required | Description |
|---|---:|---|
| `target` | Yes | File path, URL, repository surface, or rendered artifact |
| `failing_gates` | Yes | Gate IDs from a prior audit or review |
| `preserve` | No | Passing gates and elements that must remain stable |
| `max_iterations` | No | Default `3` |
| `approval_mode` | No | Repository write policy inherited from the project |

## Refinement loop

### Step 1 — Load audit state

Use the prior audit/review report. If none exists, run a quick critical-gate audit before editing.

```text
Current overall score:
Failing gates:
Target gates to fix:
Passing gates to preserve:
Evidence currently available:
```

Do not patch before the failing gates and preservation set are explicit.

### Step 2 — Declare scope

```text
REFINEMENT SCOPE
────────────────────────────────────
Fixing: <gate IDs and affected regions>
Preserving: <passing gates and locked elements>
Candidate approach: <smallest likely correction>
Verification plan: <render, viewport, interaction, accessibility, tests>
```

### Step 3 — Classify and apply the candidate fix

For each failing gate:

```text
A. Identify the governing skill, reference, workflow, or product rule.
B. Read the existing rule completely.
C. Classify the defect:
   - reusable skill gap;
   - reference knowledge gap;
   - workflow orchestration gap;
   - local implementation defect.
D. Apply the smallest candidate fix to the correct layer.
E. Record a learning candidate when reusable reasoning may be missing.
```

Do not append a pitfall to a skill merely because an implementation ignored an existing clear rule. Fix the implementation or orchestration and protect the behavior with an eval when needed.

A candidate learning is not promoted knowledge until the real case passes verification.

### Step 4 — Verify

Run evidence appropriate to the affected gate:

```text
Runtime:
  build, lint, type checks, relevant tests

DOM and accessibility:
  overflow, touch targets, headings, semantics, focus, reduced motion

Visual:
  inspect affected regions with realistic content

Responsive and interaction:
  mobile, tablet, laptop, desktop
  keyboard, pointer, touch, swipe, scroll, resize

Gate review:
  re-score fixed gates
  re-check adjacent and preserved gates for regression
```

A successful build alone is not visual verification.

If the candidate fix fails, iterate within the declared scope. Do not update shared skills from the failed attempt.

### Step 5 — Automatic skill-evolution review

After each fix passes verification, load:

```text
skill-evolution + skill-eval
```

Run the review automatically. Do not wait for the user to ask whether the skill should be updated.

The learning review must:

1. capture the observed failure, verified fix, and before/after evidence;
2. extract why the fix worked;
3. classify the knowledge as local, product-specific, reusable rule, reference, workflow, eval-only, or core contract;
4. remove product names, repository paths, routes, class names, and exact breakpoints from shared instructions;
5. test the generalized reason against at least two different contexts and counterexamples;
6. check the complete target skill and related skills for duplicate coverage;
7. apply the smallest justified shared patch;
8. add or update a regression eval derived from the real case;
9. run relevant eval and conformance checks;
10. commit automatically only when repository and approval policy permit it.

Allowed verdicts:

```text
PROMOTED
EVAL_ONLY
LOCAL_ONLY
DUPLICATE
DEFERRED_UNVERIFIED
NOT_WRITTEN_READ_ONLY
```

Examples:

```text
Product-specific fact:
A named gallery used a particular component at a project breakpoint.
→ Store in product design lock or regression provenance.

Reusable reason:
A primary discovery set should not be hidden solely because the current component overflows; evaluate visible overflow or component substitution from task, option count, label length, and available width.
→ Promote to the governing skill only when new, transferable, and verified.
```

### Step 6 — Exit

Exit when all declared failing gates reach `>= 8.0`, or when `max_iterations` is reached.

```text
REFINEMENT COMPLETE — <target>
────────────────────────────────────
Gates fixed: <before -> after scores>
Gates preserved: <regression result>
Iterations: <N>
Local implementation patches: <list>
Learning candidates reviewed: <count>
Promoted skill/reference/workflow changes: <list or none>
Eval-only additions: <list or none>
Local-only or duplicate lessons: <list or none>
Promotion commits: <SHA list or not written>
Residual gaps: <list or none>
```

The workflow is incomplete when a verified fix occurred but no learning-review verdict was recorded.

## Common refinement targets

### Reduced motion

```css
@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after {
    animation-duration: 0.01ms !important;
    transition-duration: 0.01ms !important;
  }
}
```

Treat the snippet as an implementation example, not a universal substitute for checking every motion behavior and semantic transition.

### Touch targets

```css
.element {
  min-height: 44px;
  min-width: 44px;
  display: inline-flex;
  align-items: center;
}
```

The reusable rule is reachable, non-overlapping interaction. The exact CSS remains framework and product dependent.

### Semantic structure

```html
<a href="#main" class="skip-link">Skip to content</a>
<nav aria-label="Main navigation">
<main id="main">
<section aria-labelledby="section-heading">
<h2 class="sr-only" id="section-heading">Section name</h2>
```

### Focal-point void

Avoid using full viewport height by reflex when sparse content creates dead space. Select height and spacing from the intended composition and actual content.

### Type pairing

Use distinct display and body roles when the product's visual language benefits from them. Preserve existing brand typography locks when present.

## Anti-patterns

| Anti-pattern | Correct behavior |
|---|---|
| Patch a shared skill before proving the real fix | Verify first, then promote |
| Copy the product case into `SKILL.md` | Store case provenance separately and promote only reusable reasoning |
| Add a duplicate rule because it was ignored | Fix orchestration or add regression eval |
| Fix unrelated visual areas during refinement | Preserve passing gates |
| Claim skill update without a commit result | Report `not written` honestly |
