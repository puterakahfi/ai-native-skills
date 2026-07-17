# Iteration Review Mode

Use during active layer-by-layer redesign/refinement loops. This is lighter than the full Phase 5 scorecard.

## When to use

Use iteration review when:

```text
✓ user is still reacting to visual direction
✓ only one layer was touched
✓ full build/lint is intentionally deferred
✓ goal is fast feedback, not deploy readiness
```

Use full scorecard when:

```text
✓ user approves direction and asks to commit/deploy
✓ multiple layers changed substantially
✓ release readiness is being claimed
✓ accessibility/performance correctness depends on full gates
```

## Active-layer scorecard

Report only touched gates + regression checks.

```text
## Iteration N · [surface]

Primary layer: [strategy | UI | UX | voice | interaction | delight | verification]
Secondary layers: [optional]
Locked layers: [approved/preserved]

| Gate | Before | After | Verdict | Notes |
|---|---:|---:|---|---|
| [C2 Visual weight] | x.x | x.x | pass/fail | ... |
| [R8 Restraint] | x.x | x.x | pass/fail | ... |

Regression checks:
- DOM: sheets > 0, overflow=false, touchFail=0
- Theme: light/dark still readable if affected
- Route: changed route returns 200
- Locked layers: no unintended changes

Decision:
- Continue iteration / ask user review / escalate to full review
```

## Layer-specific minimal gates

### Strategy

```text
- First impression: one remembered idea
- Audience/goal/content priority unchanged or explicitly reopened
- CTA/no-CTA stance matches product goal
```

### UI

```text
- Visual hierarchy readable at glance
- Density reduced or intentionally increased
- Typography/spacing/token changes coherent
- No new visual slop
```

### UX

```text
- Expected click targets still work
- CTA labels and route/hash behavior clear
- Focus/touch states preserved
```

### Voice

```text
- H1 is a stance
- Copy is specific, no slop words
- Status language honest
```

### Interaction

```text
- Motion has purpose
- Reduced motion respected
- Hover/focus/tap feedback useful
```

### Delight / Expression

```text
- Named role: orientation / affordance / emphasis / atmosphere / reward
- Not hiding weak hierarchy or copy
- Image/motion supports story
- No accessory drift/cardification unless intentional
```

### Verification

```text
- route 200
- DOM probe clean
- browser visual check in affected mode(s)
- git diff --check on changed files
```

## Preserve approved layers

Each iteration must name locked layers. If a fix changes a locked layer, report it as a regression unless the user explicitly approved reopening it.

```text
Locked: Strategy, macrostructure, voice
Touched: Delight asset integration
Allowed edits: image scale/crop/mask/caption proximity
Not allowed: H1 rewrite, section reorder, CTA strategy change
```

## Avoid score inflation

Do not mark a gate as fixed because it “looks better.” Tie each verdict to observable evidence:

```text
✓ screenshot shows image no longer boxed
✓ DOM confirms image rendered dimensions increased/decreased
✓ touchFail remains 0
✓ H1 still within first viewport
```
