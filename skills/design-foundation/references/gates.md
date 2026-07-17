# Foundation Gates Scorecard

> Run at Phase 5 REVIEW — before genre/brand gates.
> F-gates are HARD FAIL — any fail blocks delivery.

## Foundation Gates (F1–F7)

### F1 — Visual Hierarchy
```
CHECK: measure H1 font-size ÷ body font-size
  ≥ 3.5× = PASS (zen weight-300 minimum)
  ≥ 2.5× = PASS (standard)
  < 2.5× = FAIL → increase H1 size OR increase weight

CHECK: H2 and H3 visually distinguishable from each other?
  Yes = PASS
  No  = FAIL → adjust size/weight/color steps
```

### F2 — Contrast Ratio
```
TOOL: browser devtools → inspect → accessibility → contrast ratio

Primary text on bg:    ≥ 4.5:1 = PASS  /  < 4.5:1 = FAIL
Secondary text on bg:  ≥ 3.0:1 = PASS  /  < 3.0:1 = FAIL
Large text (24px+):    ≥ 3.0:1 = PASS  /  < 3.0:1 = FAIL
Icon on bg:            ≥ 3.0:1 = PASS  /  < 3.0:1 = FAIL
```

### F3 — Touch Targets
```
CHECK: all interactive elements (buttons, links, toggles)
  min-width + min-height ≥ 44px = PASS
  Any element < 44px = FAIL → add padding wrapper

JS audit:
  document.querySelectorAll('a,button,[role=button]')
    .forEach(el => {
      const r = el.getBoundingClientRect();
      if(r.width < 44 || r.height < 44)
        console.warn('touchFail', el);
    })
```

### F4 — Semantic Tokens
```
CHECK: no raw values in component CSS
  grep for: #[0-9a-fA-F] / [0-9]+px / [0-9]+rem (outside :root)

PASS: all values via var(--token)
FAIL: any hardcoded value in component selector → extract to token
```

### F5 — No Dead Space
```
CHECK: is there a viewport where content feels stranded/lost?
  No = PASS
  Yes = FAIL → fix: remove min-height:100vh, add content, or shrink padding

SPECIFIC CHECKS:
  □ No min-height: 100vh on hero
  □ Sparse sections (< 3 elements) have tighter spacing
  □ No empty sections as spacers
```

### F6 — No Decoration Without Function
```
CHECK: every visual element has a job
  □ Dividers: do they separate meaningfully different sections?
  □ Background patterns: do they add depth or just texture?
  □ Gradient: does it direct attention or just "look nice"?
  □ Icons: informational or decorative (aria-hidden if latter)?

FAIL: any element whose removal improves clarity → remove it
```

### F7 — Aria & Keyboard
```
CHECK:
  □ All buttons have text label or aria-label
  □ All icon-only elements have aria-label or aria-hidden
  □ Skip link present: <a href="#main" class="skip-link">
  □ Focus-visible on all interactive elements (not outline:none)
  □ Tab order logical (follows visual order)
  □ prefers-reduced-motion: animation disabled if requested

Any fail = FAIL gate
```

## Foundation Scorecard Template

```
FOUNDATION GATES
────────────────────────────────
F1 Hierarchy    [ ] PASS  [ ] FAIL  H1/body: ___×
F2 Contrast     [ ] PASS  [ ] FAIL  Primary: ___:1
F3 Touch        [ ] PASS  [ ] FAIL  touchFail: ___
F4 Tokens       [ ] PASS  [ ] FAIL  violations: ___
F5 Dead Space   [ ] PASS  [ ] FAIL  instances: ___
F6 Noise        [ ] PASS  [ ] FAIL  removals: ___
F7 Aria         [ ] PASS  [ ] FAIL  violations: ___
────────────────────────────────
RESULT: ALL PASS → proceed to genre/brand gates
        ANY FAIL → fix before continuing
```
