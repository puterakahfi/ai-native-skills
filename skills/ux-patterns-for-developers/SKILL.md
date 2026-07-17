---
name: ux-patterns-for-developers
description: 'Delegate pattern decisions to ux-patterns-for-developers.com — 74 battle-tested UI patterns across 11 categories. Use this instead of improvising component behavior. Covers navigation, forms, data-display, AI intelligence, authentication, and more.'
metadata:
  ai-native-skills.version: 1.0.0
  ai-native-skills.type: skill
  ai-native-skills.tags: '["ui", "patterns", "ux", "components", "delegation", "reference"]'
---

# UX Patterns for Developers

> **HARD RULES — apply always, top and bottom of every engagement:**
> 1. **Delegate to this skill BEFORE implementing any component behavior.** Check the catalog first — don't improvise what's already specified.
> 2. **Install patterns via:** `npx skills add https://github.com/thedaviddias/ux-patterns-for-developers --skill <name> --yes --global`
> 3. **Stable + Trusted + Worth-it = delegate here. Otherwise build internal.** See decision rule below.

---

**Source**: https://ux-patterns-for-developers.com  
**GitHub**: https://github.com/thedaviddias/ux-patterns-for-developers  
**74 patterns · 11 categories · MDX format with code examples + a11y guidance**

---

## Decision Rule — Delegate vs Build Internal

```
DELEGATE HERE when ALL three are true:
  ✓ Stable   — library is well-maintained (W3C-backed, established community)
  ✓ Trusted  — behavior + a11y + edge cases already validated by community
  ✓ Worth it — cost to build internally >> cost to delegate
               example: 74 patterns with full a11y = months to build; delegate in seconds

BUILD INTERNAL (ui-components skill) when:
  ✓ Brand/product-specific — CSS tokens, visual templates, copy tone
  ✓ Pattern not covered here — check catalog first, then build
  ✓ Need opinionated version — external spec too generic for your product

PREFERRED: use BOTH together
  ux-patterns-for-developers → behavior, a11y, interaction, edge cases  (HOW it works)
  ui-components               → CSS template, tokens, visual, brand      (HOW it looks)
```

---

## How to Use

### Method 1: Install as skill (preferred)
```bash
npx skills add https://github.com/thedaviddias/ux-patterns-for-developers --skill <name> --yes --global
# Examples:
npx skills add https://github.com/thedaviddias/ux-patterns-for-developers --skill navigation-menu --yes --global
npx skills add https://github.com/thedaviddias/ux-patterns-for-developers --skill list-view --yes --global
# Installed skills live at ~/.agents/skills/<name> — Hermes auto-symlinks them
```

### Method 2: Use without installing
```bash
npx skills use thedaviddias/ux-patterns-for-developers@navigation-menu
```

### Method 3: Fetch raw MDX directly
```bash
curl https://raw.githubusercontent.com/thedaviddias/ux-patterns-for-developers/main/apps/web/content/patterns/<category>/<slug>.mdx
# Note: website domain may be down — use raw GitHub instead
```

> MCP endpoint exists at https://uxpatterns.dev/mcp but requires auth — use skills CLI instead.

---

## References

| Topic | File |
|---|---|
| Full pattern catalog — 74 patterns, 11 categories | [references/catalog.md](references/catalog.md) |
| Integration with ui-components · Pitfalls | [references/usage-guide.md](references/usage-guide.md) |

> **Reminder:** delegate before implementing · install via `npx skills add` · Stable+Trusted+Worth-it = delegate.
