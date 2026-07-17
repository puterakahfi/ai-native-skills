# IA Reference: Phases 4–5, Site Map & Gates

> Complete after Phases 1–3. Define URL schema, search/browse strategy, output site map, then run gates.

---

## Phase 4: URL Structure

```
Principles:
  1. Human-readable — no GUIDs in user-facing URLs
     ❌ /posts/e3f2a1b4-8c7d-4e9f-a1b2-c3d4e5f6a7b8
     ✅ /posts/building-scalable-saas

  2. Hierarchical — URL mirrors IA
     /projects/:id/tasks/:taskId
     /blog/:year/:slug

  3. Lowercase, hyphens (not underscores)
     ✅ /user-settings
     ❌ /User_Settings

  4. Stable — changing URLs breaks links, SEO
     Use slugs that won't change (title-based slugs can change if title changes)
     Consider: /posts/:id/:slug — ID = stable, slug = readable but not canonical

  5. Short — remove noise
     ❌ /en/website/sections/blog/posts/2026/07/article-title
     ✅ /blog/article-title

  6. Noun-only slugs — no verbs in URL segments
     ✅ /user-settings    ❌ /manage-user-settings
     ✅ /reports          ❌ /view-reports
     ✅ /blog/article     ❌ /read-blog-post
```

---

## Phase 5: Search vs Browse Decision

```
Users find things in two modes:
  BROWSE — "I'll know it when I see it" (exploring, discovering)
  SEARCH — "I know exactly what I want" (known-item seeking)

Provide search when:
  □ > 200 items of same type
  □ Users know the name of what they want
  □ Content is frequently updated
  □ Items have meaningful metadata (date, author, tag)

Provide browse when:
  □ < 100 items
  □ Users are discovering, not retrieving
  □ Items have strong visual identity (images, icons)
  □ Serendipitous discovery has value (portfolio, blog)

Provide both when:
  □ Large content set AND diverse user intent
  □ Add filters as the bridge (search + faceted browse)
```

---

## Site Map Format

```
Output a site map before starting any design:

pkahfi.com
├── / (Home — personal landing)
│   ├── Hero (name + stance)
│   ├── Work (LIVE products only)
│   ├── About
│   └── Contact
├── /blog (external: blog.pkahfi.com)
└── /blueprint (external: blueprint.pkahfi.com)

Notation:
  / = page
  (description) = page purpose
  ├── = child page or section
  [external] = redirects or external domain
  [auth] = requires authentication
  [draft] = not yet built
```

---

## IA Gates (Scored 0–10, Min 8)

```
Gate IA1: Inventory Complete
  □ All content/features listed before design started?
  □ Priority assigned (P0/P1/P2)?
  Score: __ / 10

Gate IA2: Navigation Clarity
  □ ≤ 7 top-level nav items?
  □ Labels task-oriented, not system-oriented?
  □ No item fits in 2+ categories?
  Score: __ / 10

Gate IA3: Depth Appropriate
  □ Core features reachable in ≤ 3 clicks?
  □ Flat vs deep choice matches content volume?
  Score: __ / 10

Gate IA4: URL Structure
  □ URLs human-readable?
  □ URL hierarchy mirrors IA hierarchy?
  □ No GUIDs in user-facing URLs?
  □ Noun-only slugs, no verbs, kebab-case?
  Score: __ / 10

OVERALL: __ / 10   MINIMUM: 8.0
```
