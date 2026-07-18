---
name: adaptive-component-design
description: Selects and substitutes the right UI component pattern across mobile, tablet, laptop, and desktop based on task intent, option count, label length, discoverability, content width, input method, and interaction cost. Use when a component fits one viewport but overlaps, clips, hides choices, or becomes awkward on another.
license: MIT
metadata:
  ai-native-skills.version: 1.1.0
  ai-native-skills.author: puterakahfi
  ai-native-skills.type: skill
  ai-native-skills.implements: ai-native-core/contracts/skills/design/adaptive-component-design.contract.yaml
  ai-native-skills.contract-version: "~1.0"
  ai-native-skills.related_skills: '["master-design","design-review","responsiveness","ux-ui-patterns","ux-patterns-for-developers","accessibility","ui-components"]'
---

# Adaptive Component Design

## Core rule

Responsive design may change the component, not only its size or layout.

Do not preserve Tabs, Table, Modal, Sidebar, or another pattern merely for visual consistency. Preserve the user task, state, semantics, and information priority; choose the component that performs those jobs best at the available content width.

## Role in composition

This is a specialist skill, not the owner of the complete product experience.

```text
Narrow advisory question about one cross-device component
→ adaptive-component-design may run alone

Broad UI/UX design or redesign
→ owner: master-design
→ specialist: adaptive-component-design
→ reviewer: design-review when rendered or implemented
```

Rules:

- `master-design` owns the overall product-design decision and synthesis.
- This skill owns component fitness and substitution across viewports.
- It may challenge a requested component within its boundary.
- It must return evidence and trade-offs to the design owner.
- It must not independently change product strategy, page macrostructure, visual language, or brand direction.
- An implemented result must not be accepted without `design-review`.

## Scope

This skill owns:

- component-pattern selection per viewport;
- substitution rules between equivalent interaction patterns;
- shared state and behavior across component variants;
- overflow affordances and reachable controls;
- component fitness gates before implementation.

It does not own visual styling, tokens, page macrostructure, product strategy, or breakpoint CSS mechanics.

## Decision procedure

1. Name the user task: navigate, filter, select, compare, edit, inspect, or act.
2. Measure the real content width after shell, sidebar, and gutters.
3. Inventory option count, label length, priority, frequency, and whether choices must remain visible.
4. Check input mode: touch, pointer, keyboard, or mixed.
5. Select the smallest pattern that preserves discoverability and task completion.
6. Define substitutions for each width class.
7. Keep one controlled state and one semantic contract across variants.
8. Record rejected alternatives and trade-offs.
9. Return the recommendation to `master-design` for final synthesis when operating in a composed design task.
10. Verify at boundary widths and with realistic content.

## Component substitution matrix

| User need | Mobile | Tablet | Laptop/Desktop |
|---|---|---|---|
| 2–4 short peer destinations | Segmented control or tabs | Line tabs | Line tabs |
| 5–8 stable primary discovery categories | Icon shortcut rail or labeled horizontal picker | Line tabs or icon shortcuts | Line tabs |
| Many, dynamic, or secondary options | Select, combobox, or bottom-sheet picker | Select/combobox | Searchable select, popover, or filter panel |
| Secondary filters | Button opening bottom sheet/drawer | Sheet or popover | Popover or inline filter bar |
| Dense comparison | Stacked cards or summary/details | Cards or reduced table | Table/grid |
| Multi-step editing | Full-screen step flow | Sheet or split view | Dialog, drawer, or split view |
| Supporting content cards | Horizontal rail with visible peek and edge controls | Two-column grid | Stable grid or stacked supporting column |
| Primary action | Full-width or sticky action | Inline prominent action | Inline action aligned to hierarchy |

## Discovery versus filtering

Primary discovery categories should remain visible. Do not hide a small, stable, high-value category set inside Select.

Use Select or combobox when options are secondary, numerous, dynamic, searchable, or too long for visible shortcuts.

Tabs require sufficient width, readable labels, persistent selected state, and reachable options. If those fail, substitute the pattern.

## Rail contract

A horizontal rail must provide:

- native swipe/trackpad scrolling;
- visible next-item peek or edge treatment;
- right control at the start, paired controls in the middle, left control at the end;
- controls tied to actual scroll position;
- smooth advance by approximately one visible group;
- keyboard-reachable controls with accessible names;
- no item hidden permanently beneath controls.

## Implementation rules

- Prefer existing design-system or shadcn primitives.
- Install or upgrade the primitive before recreating its behavior with custom CSS.
- Avoid switching between conflicting display utilities when legacy CSS can override them; prefer one stable layout system.
- Never use intrinsic image dimensions to determine responsive card height.
- Do not use `h-full` without an explicit ancestor height or bounded grid track.
- Record every component substitution in the design lock.
- Preserve the same value, event semantics, analytics identity, and accessible label across variants.

## Quality gates

Fail the design if any answer is yes:

- Do controls overlap, clip, or shrink below 44×44px?
- Are primary choices hidden without a product reason?
- Is a phone receiving a compressed desktop component?
- Is a tablet treated only as a stretched phone or squeezed desktop?
- Can the user reach every option by touch and keyboard?
- Do mobile and desktop variants drift into different state or behavior?
- Is overflow possible without a visible affordance?
- Was the component selected because it already existed rather than because it fits the task?
- Is this specialist making page-level, product-strategy, or visual-direction decisions without `master-design`?
- Is an implemented result being accepted without independent `design-review` evidence?

## Verification evidence

Before claiming completion, provide:

- component choice and rejected alternatives;
- substitution map for mobile, tablet, laptop, and desktop;
- screenshots at 390×844, 768×1024, 1280×800, and 1440×900;
- checks immediately before and after every used breakpoint;
- interaction evidence for selection, overflow controls, keyboard use, and resize;
- reviewer verdict when the result is rendered or implemented;
- remaining assumptions or mismatches.

Code inspection alone is not visual verification.
