---
name: design-strategy
description: UX strategy, content, information architecture, and collection discovery port. Routes user-centered concerns to ux-psychology, information-architecture, collection-discovery-design, CRO, copywriting, and content-strategy before layout, visual expression, or interaction adapters are locked.
license: MIT
metadata:
  ai-native-skills.version: 1.1.0
  ai-native-skills.author: puterakahfi
  ai-native-skills.type: meta-skill
  ai-native-skills.implements: ai-native-core/contracts/skills/design/design-strategy.contract.yaml
  ai-native-skills.contract-version: ^1.1.0
  ai-native-skills.related_skills: '["ux-psychology","information-architecture","collection-discovery-design","cro","copywriting","content-strategy"]'
---

# Design Strategy Port

> **HARD RULES:**
> 1. Strategy before aesthetics — understand user needs before visual decisions.
> 2. Taxonomy meaning must be established before collection presentation strategy.
> 3. Collection strategy must be established before selecting pagination, tabs, filters, infinite scroll, or another interaction adapter.
> 4. CRO only when business goal is conversion — do not add CTAs to identity or portfolio pages by convention.
> 5. Copy is design — run copywriting before locking layout.

## What this port covers

User-centered thinking — why information, content, and discovery work the way they do.

Answers:

- What do users need?
- What content and taxonomy exist?
- How do users find, browse, narrow, compare, and return within a collection?
- What copy and content structure support the task?
- Is conversion an explicit goal?

Does not cover:

- visual style → `design-visual`;
- spatial layout → `design-layout`;
- interaction behavior → `design-interaction`;
- context-specific component fitness → `adaptive-component-design`;
- implementation → engineering or product adapter.

## Adapter skills — load per concern

| Concern | Adapter | When to load |
|---|---|---|
| User cognition and behavior | `ux-psychology` | Persuasion, trust, decision, cognitive-load concerns |
| Navigation and taxonomy meaning | `information-architecture` | Content inventory, classification, navigation, hierarchy, search-vs-browse meaning |
| Collection retrieval and discovery strategy | `collection-discovery-design` | Catalog, registry, directory, feed, gallery, table, library, or search-results surface needs grouping, search, facets, sorting, traversal, disclosure, or state strategy |
| Conversion optimization | `cro` | Only when conversion is an explicit goal |
| UI copy and microcopy | `copywriting` | Any material copy decision |
| Content planning | `content-strategy` | Content-heavy surfaces, inventory, lifecycle, editorial planning |

### Routing distinction

```text
What do the categories mean?
→ information-architecture

How should users retrieve and traverse the collection?
→ collection-discovery-design

How should the selected adapter behave and remain accessible?
→ design-interaction

Does the selected component fit each actual context?
→ adaptive-component-design
```

Do not route a collection-wide strategy failure directly to a pagination, tabs, filter-panel, or component implementation skill.

## How to load

```text
skill_view(name='ux-psychology')
skill_view(name='information-architecture')
skill_view(name='collection-discovery-design')
skill_view(name='cro')
skill_view(name='copywriting')
skill_view(name='content-strategy')
```

## Load sequence for redesign

```text
PRE-FLIGHT / INSPECT
  1. content-strategy
     → content inventory when the surface is content-heavy

  2. information-architecture
     → taxonomy, hierarchy, navigation, and search-vs-browse meaning

  3. collection-discovery-design
     → only when the surface contains a material collection
     → diagnosis and strategy before adapters

DIRECTION / SPECIFY
  4. cro
     → only when conversion is explicit

  5. copywriting
     → copy before layout lock

  6. ux-psychology
     → cognition, trust, decision, and comprehension concerns

PRODUCE
  collection-discovery-design handoff
  → design-interaction selects behavior adapters
  → adaptive-component-design selects fit component variants by context
```

## Collection-heavy trigger

Load `collection-discovery-design` when one or more are true:

- users must find a known item inside a collection;
- groups or default lists are long or growing;
- categories, filters, facets, sorting, or traversal need justification;
- position, URL, selected view, query, filter, or return context must persist;
- desktop and mobile may need different disclosure or component adapters;
- an audit finding spans the collection model rather than one broken component.

Do not load it merely because a page has three cards or one short list.

> **REMINDER:** Strategy before aesthetics. Taxonomy before collection presentation. Collection strategy before adapter selection. Copy before layout.
