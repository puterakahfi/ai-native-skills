# UX Patterns for Developers — Usage Guide & Pitfalls

## Integration with ui-components Skill

`ui-components` skill = CSS templates (how it looks)  
`ux-patterns-for-developers` = behavior spec + a11y (how it works)

**Use both together:**
```
1. ui-components → copy CSS template for the component
2. ux-patterns-for-developers → fetch behavior spec + a11y requirements
3. Merge: apply behavior to the CSS template
```

**Concrete example (navigation):**
```
ux-patterns navigation-menu spec says:
  position: sticky (not fixed)
  aria-label="Open menu" (not "Toggle navigation")
  box-shadow on scroll (not border-bottom)

ui-components navbar template says:
  --bg: #09090a
  font-family: var(--font-mono)
  height: 64px

Result: sticky nav with correct a11y + correct visual style.
Neither skill alone is complete. Both together = correct.
```

---

## PITFALLS

```
□ hambuger-menu URL has a typo — "hambuger" not "hamburger" — use as-is
□ Patterns are MDX — fetch the page URL, not the raw GitHub file (unless offline)
□ Website domain ux-patterns-for-developers.com may be down — use raw GitHub instead:
  https://raw.githubusercontent.com/thedaviddias/ux-patterns-for-developers/main/apps/web/content/patterns/<category>/<slug>.mdx
□ Some patterns cover behavior only — still need ui-components for CSS
□ Don't fetch ALL 74 — only fetch the specific pattern you need
□ MCP endpoint at https://uxpatterns.dev/mcp requires auth — use skills CLI instead
```

---

## Installation Quick Reference

```bash
# Install a specific pattern as a skill (preferred method)
npx skills add https://github.com/thedaviddias/ux-patterns-for-developers --skill <name> --yes --global

# Use without installing
npx skills use thedaviddias/ux-patterns-for-developers@<name>

# Fetch raw MDX directly
curl https://raw.githubusercontent.com/thedaviddias/ux-patterns-for-developers/main/apps/web/content/patterns/<category>/<slug>.mdx
```

## Workflow: Component Implementation

```
1. Check catalog (references/catalog.md) — does the pattern exist?
2. If yes → install: npx skills add ... --skill <name> --yes --global
3. Load the installed skill → extract behavior spec + a11y requirements
4. Load ui-components → get CSS template
5. Merge behavior into CSS template
6. Never improvise behavior the library already specifies
```
