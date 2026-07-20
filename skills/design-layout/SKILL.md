---
name: design-layout
description: Layout and structure port — routes spatial decisions through macrostructures, ui-components, adaptive-component-design, and responsiveness in canonical order. Load this instead of selecting layout adapters ad hoc.
license: MIT
metadata:
  ai-native-skills.version: 1.1.0
  ai-native-skills.author: puterakahfi
  ai-native-skills.type: meta-skill
  ai-native-skills.implements: ai-native-core/contracts/skills/design/design-layout.contract.yaml
  ai-native-skills.contract-version: "^2.0.1"
  ai-native-skills.related_skills: '["design-spacing","macrostructures","responsiveness","adaptive-component-design","ui-components"]'
---

# Design Layout Port

Route spatial decisions through the canonical layout sequence:

```text
macrostructure
→ component structure
→ adaptive component selection or substitution
→ responsive breakpoint and fluid-grid validation
```

## Hard rules

```text
1. Pick macrostructure before component layout.
2. Define component structure before selecting cross-context variants.
3. Select or substitute adaptive components before responsive validation.
4. Define mobile, tablet, and desktop behavior for major components.
5. Never use min-height: 100vh on a hero solely to fill the viewport.
6. Responsiveness applies from the start; it is not a final polish phase.
```

## What this port covers

Spatial organization: how page structure, component structure, adaptive component families, and responsive mechanics compose.

It answers:

```text
What page-level spatial pattern applies?
What component structure represents the content and task?
Does the same component family remain fit across contexts?
How are breakpoints and fluid behavior validated after selection?
```

It does not own:

- aesthetic style or brand expression → `design-visual`;
- interaction states and feedback → `design-interaction`;
- token architecture or theming → `design-system`;
- independent acceptance → `design-review`.

## Canonical adapter order

| Order | Concern | Adapter | Responsibility |
|---:|---|---|---|
| 1 | Page-level spatial pattern | `macrostructures` | Select the page macrostructure before arranging components. |
| 2 | Component structure | `ui-components` | Define navigation, hero, section, and component structure. |
| 3 | Cross-context component fitness | `adaptive-component-design` | Preserve, adapt, or substitute component patterns from task, content, real width, and interaction context. |
| 4 | Responsive mechanics and validation | `responsiveness` | Define and verify breakpoints, fluid grids, and behavior after component selection. |

`design-spacing` remains a related specialist for rhythm, Ma, and spatial hierarchy after the structural route is known. It is not a substitute for the four ordered port adapters.

## Load sequence

```text
1. skill_view(name='macrostructures')
2. skill_view(name='ui-components')
3. skill_view(name='adaptive-component-design')
4. skill_view(name='responsiveness')
```

Load detailed references only for the selected concern, for example:

```text
skill_view(name='macrostructures', file_path='references/<macrostructure>.md')
skill_view(name='ui-components', file_path='references/<component>.md')
```

## Quality gate

Do not complete the layout route until:

```text
macrostructure selected before component layout
component structure defined before adaptive selection
adaptive component strategy selected before responsive validation
major mobile, tablet, and desktop behavior explicit
hero does not create artificial void through min-height: 100vh
responsiveness is integrated from the beginning
```

> **Reminder:** structure first, adaptive component decision second, responsive mechanics third. Do not validate breakpoints around a component family that has not yet been proven fit.
