---
name: design-layout
description: Layout and structure port — routes spatial decisions through macrostructures, ui-components, component-family-design, adaptive-component-design, and responsiveness in canonical order. Load this instead of selecting layout adapters ad hoc.
license: MIT
metadata:
  ai-native-skills.version: 1.2.0
  ai-native-skills.author: puterakahfi
  ai-native-skills.type: meta-skill
  ai-native-skills.implements: ai-native-core/contracts/skills/design/design-layout.contract.yaml
  ai-native-skills.contract-version: "^2.0.1"
  ai-native-skills.related_skills: '["design-spacing","macrostructures","ui-components","component-family-design","responsiveness","adaptive-component-design"]'
---

# Design Layout Port

Route spatial decisions through the canonical layout sequence:

```text
macrostructure
→ component capability and structure
→ organism / template family composition
→ adaptive component selection or substitution
→ responsive breakpoint and fluid-grid validation
```

## Hard rules

```text
1. Pick macrostructure before component layout.
2. Define component capability and hierarchy before creating route-local components.
3. Route repeated organisms and page shells through component-family-design.
4. Define invariant anatomy, configurable slots, and route variants before adaptive selection.
5. Select or substitute adaptive components while preserving the accepted family identity.
6. Define mobile, tablet, and desktop behavior for major components.
7. Never use min-height: 100vh on a hero solely to fill the viewport.
8. Responsiveness applies from the start; it is not a final polish phase.
```

## What this port covers

Spatial organization: how page structure, component structure, component families, adaptive variants, and responsive mechanics compose.

It answers:

```text
What page-level spatial pattern applies?
What component capability and hierarchy represent the content and task?
Does a canonical organism or template family already own this product role?
Which differences are slots or bounded variants?
Does the same family remain fit across contexts?
How are breakpoints and fluid behavior validated after selection?
```

It does not own:

- aesthetic style or brand expression → `design-visual`;
- interaction states and feedback → `design-interaction`;
- token architecture or theming → `design-system`;
- repository paths and framework mapping → `implementation-context-discovery`;
- independent acceptance → `design-review`.

## Canonical adapter order

| Order | Concern | Adapter | Responsibility |
|---:|---|---|---|
| 1 | Page-level spatial pattern | `macrostructures` | Select the page macrostructure before arranging components. |
| 2 | Component capability and structure | `ui-components` | Define navigation, hero, section, and component capability from task/content evidence. |
| 3 | Organism and template composition | `component-family-design` | Classify hierarchy, preserve shared family anatomy, define slots/variants, and map routes to family instances. |
| 4 | Cross-context component fitness | `adaptive-component-design` | Preserve, adapt, or substitute component patterns while retaining family identity and shared semantics. |
| 5 | Responsive mechanics and validation | `responsiveness` | Define and verify breakpoints, fluid grids, and behavior after component and family selection. |

`design-spacing` remains a related specialist for rhythm, Ma, and spatial hierarchy after the structural route is known. It is not a substitute for the five ordered port adapters.

## Load sequence

```text
1. skill_view(name='macrostructures')
2. skill_view(name='ui-components')
3. skill_view(name='component-family-design') when an organism, template, or repeated family is involved
4. skill_view(name='adaptive-component-design')
5. skill_view(name='responsiveness')
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
component hierarchy and product role classified
existing organism/template families inventoried
invariant anatomy and configurable slots separated
route differences mapped to configuration or bounded variants when fit
adaptive component strategy selected without losing family identity
major mobile, tablet, and desktop behavior explicit
hero does not create artificial void through min-height: 100vh
responsiveness is integrated from the beginning
```

> **Reminder:** structure first, family composition second, adaptive decision third, responsive mechanics fourth. Do not validate breakpoints around a route-local component that bypasses a fit shared family.
