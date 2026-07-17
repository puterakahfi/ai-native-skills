# Component Redesign Pass

Use this reference when redesigning or refining a complete page surface. It bridges `redesign-workflow` with `ui-components` so page-level work does not skip navbar, hero, footer, or interaction states.

## Principle

A page is not finished when the hero looks good. Review components in order, preserve approved layers, and only change the components that support the active layer.

```text
Pass order:
1. Navbar / global header
2. Hero / above-fold story
3. Primary sections
4. Work rows / cards / project lists
5. About / credibility section
6. Contact / CTA section
7. Footer
8. Interaction states
9. Verification packet
```

For each component, state:

```text
Component: [name]
Role: [orientation | stance | proof | navigation | closure | conversion | support]
Preserve: [approved content, routes, copy, visual language]
Can change: [spacing, hierarchy, state, layout, density, copy, behavior]
Must verify: [component-specific checks]
Reference: [ui-components file / hero-patterns / external behavior skill]
```

## 1. Navbar / global header

Load:

```text
skill_view(name='ui-components', file_path='references/navbar.md')
```

Role:

```text
orientation, trust, global navigation, theme access
```

Can change:

```text
- spacing and containment
- sticky/fixed treatment
- link order and active state
- theme toggle placement
- mobile menu behavior
- focus/hover treatment
```

Must verify:

```text
□ nav has aria-label
□ logo/home link is descriptive
□ links are ≤7 visible items unless product requires more
□ touch targets ≥44×44px
□ sticky/fixed behavior does not cover anchors
□ theme toggle aria-label describes next action
□ keyboard focus is visible
□ mobile menu, if present, has Escape close + aria-expanded state
```

Common failures:

```text
❌ nav visually heavier than hero
❌ fixed header covers hash targets
❌ theme toggle has static/ambiguous label
❌ desktop link spacing copied directly to mobile
```

## 2. Hero / above-fold story

Load:

```text
skill_view(name='ui-components', file_path='references/hero.md')
skill_view(name='redesign-workflow', file_path='references/hero-patterns.md')
```

Role:

```text
first remembered idea, stance, primary focal object
```

Can change:

```text
- H1 scale and line breaks
- eyebrow and supporting copy
- CTA weight and count
- hero image role, crop, mask, opacity, placement
- hero spacing and next-section entry
```

Must verify:

```text
□ one primary focal object
□ H1 is visible within first viewport
□ H1 is a stance, not a generic job title
□ supporting copy ≤44ch when possible
□ CTA urgency matches page goal
□ image role is named if image exists: evidence / support / atmosphere / decoration
□ no accessory drift or cardification unless intentional
□ mobile preserves the same story without crowding
```

Common failures:

```text
❌ H1 + bullets + CTA looks like a template
❌ hero image is small, boxed, and removable without meaning loss
❌ next section leaks into above-fold focus too early
❌ min-height:100vh creates dead void with sparse content
```

## 3. Primary sections

Load:

```text
skill_view(name='ui-components', file_path='references/sections-a.md')
```

Role:

```text
structure, scanning, evidence grouping, rhythm after hero
```

Can change:

```text
- section order and grouping only if strategy is open
- heading role and scale
- labels/eyebrows
- dividers and section backgrounds
- density and whitespace rhythm
```

Must verify:

```text
□ section role is clear: proof / explanation / list / narrative / CTA
□ H2 scale is below hero H1 weight
□ section spacing differs by importance
□ no equal-weight section stack unless intentionally editorial
□ anchors have scroll margin if linked from nav
```

Common failures:

```text
❌ every section has same large heading and same card grid
❌ labels decorate but do not orient
❌ whitespace exists but does not create hierarchy
```

## 4. Work rows / cards / project lists

Load:

```text
skill_view(name='ui-components', file_path='references/sections-a.md')
```

Role:

```text
proof, status honesty, scannable portfolio evidence
```

Can change:

```text
- row vs card vs grid pattern
- status labels
- metadata density
- link affordance
- live/planned/lab ordering
```

Must verify:

```text
□ live/released work has more weight than planned/lab work
□ statuses are accurate and visible
□ external links have descriptive labels and rel when needed
□ cards/rows are not equal if project maturity is unequal
□ no badge/tag clutter unless it improves scanning
```

Common failures:

```text
❌ live, planned, lab, and archived items look equally finished
❌ too many tags make the portfolio feel like a catalog
❌ card borders become the design instead of the content
```

## 5. About / credibility section

Load:

```text
skill_view(name='ui-components', file_path='references/sections-b.md')
```

Role:

```text
identity, credibility, context, trust
```

Can change:

```text
- biography length
- proof points
- location/context
- stack/focus grouping
- portrait or visual accent only if it supports trust
```

Must verify:

```text
□ bio is specific and concise
□ credibility comes from real work, not generic claims
□ typography stays quieter than hero
□ layout does not become a resume wall
□ no unsupported seniority or fake trust signals
```

Common failures:

```text
❌ generic full-stack bio with no point of view
❌ stack badges dominate the person/work story
❌ about section visually competes with product proof
```

## 6. Contact / CTA section

Load:

```text
skill_view(name='ui-components', file_path='references/sections-b.md')
```

Role:

```text
conversion, invitation, next action
```

Can change:

```text
- CTA copy and hierarchy
- contact link order
- section weight
- form vs direct contact pattern
```

Must verify:

```text
□ primary action is clear
□ links are descriptive and reachable by keyboard
□ touch targets ≥44×44px
□ urgency matches page type
□ no fake scarcity or SaaS-style pressure on a personal portfolio
```

Common failures:

```text
❌ CTA is louder than the page purpose
❌ contact links are tiny or icon-only
❌ contact section repeats hero copy without adding action clarity
```

## 7. Footer

Load:

```text
skill_view(name='ui-components', file_path='references/sections-b.md')
```

Role:

```text
closure, secondary navigation, identity persistence
```

Can change:

```text
- secondary nav links
- social links
- copyright/current year
- brand mark scale
- density and alignment
```

Must verify:

```text
□ footer is lighter than main content
□ links are descriptive
□ social links have accessible labels
□ footer does not introduce new primary navigation strategy
□ copyright/current year is correct when shown
```

Common failures:

```text
❌ footer becomes a second navbar with too much weight
❌ icon-only links lack labels
❌ footer spacing collapses on mobile
```

## 8. Interaction states

Load:

```text
skill_view(name='ui-components', file_path='references/interactions.md')
skill_view(name='ux-patterns-for-developers') when behavior is not trivial
```

Role:

```text
feedback, orientation, accessibility, perceived quality
```

Must verify:

```text
□ hover/focus/tap states exist where useful
□ focus-visible is obvious and not color-only
□ prefers-reduced-motion is respected
□ interactions use transform/opacity when animated
□ no hover-only affordance hides important meaning
```

Common failures:

```text
❌ hover lift on every card in a restrained design
❌ motion added before spacing/hierarchy is solved
❌ reduced motion rule exists but component animation ignores it
```

## 9. Verification packet

Use after the component pass:

```text
□ changed-file git diff --check
□ route status 200 for affected routes
□ browser DOM probe: sheets > 0, overflow=false, touchFail=0
□ light/dark check if theme, color, image blending, or nav changed
□ hash/anchor click check if nav/CTA changed
□ browser visual check for affected viewport(s)
```

Report compactly:

```text
Component pass result:
- Navbar: [unchanged | fixed | needs review]
- Hero: [unchanged | fixed | needs review]
- Sections: [unchanged | fixed | needs review]
- Work/cards: [unchanged | fixed | needs review]
- About: [unchanged | fixed | needs review]
- Contact: [unchanged | fixed | needs review]
- Footer: [unchanged | fixed | needs review]
- Verification: [evidence]
```

## Preservation rule

Do not use the component pass as permission to redesign everything.

```text
If active layer is Delight:
  allowed: hero image crop/mask/weight, supporting caption, atmospheric details
  not allowed: nav strategy, H1 rewrite, project ordering, footer IA

If active layer is UX:
  allowed: nav anchors, focus states, CTA clarity, touch targets
  not allowed: visual language reset unless UI layer is reopened
```
