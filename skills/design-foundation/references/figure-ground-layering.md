# Figure–Ground and Semantic Layering

> Universal relationship guidance for foreground, background, containment, depth, overlap, and occlusion across interactive products, static visuals, and presentations.

Figure–ground is not “add more shadows.” Layering passes when the viewer can understand what is content, what contains it, what floats above it, what temporarily blocks it, and why.

---

## Ownership

This reference strengthens existing foundation axes; it does not create F11.

```text
F2  grouping       → containment, common region, foreground/background
F5  balance        → depth weight, overlap dominance, visual mass
F6  flow           → context when a layer appears, moves, or disappears
F7  legibility     → text/symbol survival against imagery and effects
F9  accessibility  → operability and state clarity for interactive layers
F10 continuity     → layer meaning and occlusion safety across formats
```

Report findings through canonical gates such as `G4`, `C2`, `R8`, and applicable surface gates. F2/F5 remain assessment axes, not report IDs.

---

## Semantic Layer Model

Use roles before implementation-specific z-index values:

```text
L0 CANVAS
   page, artboard, slide, scene, or application background

L1 CONTENT
   primary information, imagery, controls, and task regions

L2 CONTAINMENT
   sections, panels, cards, groups, data regions, and media frames

L3 FLOATING
   menus, tooltips, sticky controls, popovers, transient inspectors

L4 MODAL
   dialogs, drawers, lightboxes, blocking confirmations, focused overlays

L5 SYSTEM / CRITICAL
   platform alerts, permission blockers, emergency or global system feedback
```

A product does not need every layer. Static artifacts may use only canvas, content, and containment. The model clarifies relationships; it does not encourage depth effects.

---

## Universal Rules

### Figure and ground must be distinguishable

```text
□ intended foreground is perceptually separable from its background
□ contrast, placement, edge, texture, motion, or containment provides enough distinction
□ weak separation is not disguised with decorative borders or excessive shadow
□ background atmosphere does not become a competing focal layer
□ text-on-image remains stable across the required text area and crop
```

A flat visual can pass. A highly layered visual can pass. Review the relationship, not the amount of shadow.

### Depth must communicate meaning

```text
□ elevation expresses containment, priority, transience, focus, or state
□ equal semantic roles do not receive arbitrary unequal depth
□ visual depth does not accidentally imply product importance
□ shadows, blur, glass, gradients, and outlines have a structural or expressive job
□ decorative depth does not replace hierarchy, grouping, or spacing
```

### Overlap and occlusion need an owner

For every meaningful overlap, identify:

```text
occluding layer
occluded content
reason for overlap
allowed duration or state
required safe region
responsive behavior
recovery or dismissal path when interactive
```

Fail when:

```text
- sticky or fixed UI covers required content or the primary action
- a floating layer detaches from its trigger, subject, or task
- overlap hides status, price, label, navigation, or required evidence
- decorative objects cross text unpredictably
- individually valid layer tokens combine into unintended occlusion
```

### Containment should clarify, not fragment

```text
□ surfaces group genuinely related information or behavior
□ nested surfaces have clear ownership and avoid card-within-card noise
□ containment does not compensate for weak proximity or hierarchy
□ one continuous task is not split into unrelated-looking islands
□ dense products may use strong containment when comparison and scanning require it
```

### Interactive layers preserve context

```text
user action
→ visible layer/state change
→ current object or task remains understandable
→ focus and input ownership are clear
→ next valid action is discoverable
→ dismissal or recovery returns to a meaningful place
```

Detailed focus traps, input parity, and modal mechanics remain owned by interactive surface gates.

### Layering survives responsive and theme changes

```text
□ stacking does not reverse semantic depth or detach floating controls
□ sticky regions leave enough visible and reachable content at small viewports
□ overlays fit constrained height, orientation, text scaling, and localization
□ alternate themes preserve layer boundaries and contrast
□ crop, safe area, and platform overlays do not consume critical content
```

---

## Evidence Policy

```text
rendered still image
  → verify figure/ground, containment, overlap, visual weight, text survival

rendered interactive flow
  → additionally verify sticky/fixed behavior, focus, dismissal, scrolling, state continuity

source or token evidence
  → inspect semantic layer tokens, portal/overlay structure, z-index ownership, theme mapping

screenshot only
  → interaction, scroll, focus, and recovery remain NOT_VERIFIED

missing alternate viewport/theme/state
  → continuity for that condition remains NOT_VERIFIED
```

Implementation values are evidence, not the verdict. A tidy z-index scale can still produce broken overlap; a one-off static artifact may have no z-index system.

---

## Review Matrix

| Relationship | Foundation axes | Canonical owners | Typical evidence |
|---|---|---|---|
| foreground vs background | F2, F7 | G4, G10 | actual-size render, contrast/context inspection |
| containment/common region | F2 | G4, G7, G5 | grouping comparison, rendered regions |
| depth and dominance | F5 | G4, C1, C2, R6, R8 | full-frame composition, squint/blur test |
| sticky/fixed occlusion | F5, F6, F9, F10 | G4 + interactive gates | scroll recording, viewport matrix, source evidence |
| modal/floating context | F2, F6, F9 | G4 + I1/I7 where applicable | interaction flow, focus/dismissal evidence |
| text/graphics over imagery | F2, F7 | G4, G10 + profile gates | crop, actual-size, and theme variants |
| responsive layer continuity | F10 | G4 + responsive/profile gates | required viewport or format set |

Use `figure-ground-fixtures.md` to test PASS/FAIL discrimination across minimal, dense, expressive, interactive, static, and presentation surfaces.

---

## Defect Classification

```text
relationship fails across multiple genres/surfaces
  → design-foundation knowledge defect

one component family layers incorrectly everywhere
  → component-system defect

correct layer rule exists but one implementation ignores it
  → local implementation defect

only one genre needs stricter depth restraint or expression
  → design-genre defect

focus trap, input parity, runtime, crop, fidelity, compositing, or export failure
  → applicable interactive/static/domain reviewer
```

Do not fix unclear figure–ground by automatically adding borders, shadows, glass, gradients, or cards. Correct the relationship at the smallest valid layer.
