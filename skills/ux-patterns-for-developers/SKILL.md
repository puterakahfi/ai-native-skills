---
name: ux-patterns-for-developers
description: 'Delegate pattern decisions to ux-patterns-for-developers.com — 74 battle-tested UI patterns across 11 categories. Use this instead of improvising component behavior. Covers navigation, forms, data-display, AI intelligence, authentication, and more.

  '
metadata:
  ai-native-skills.version: 1.0.0
  ai-native-skills.type: skill
  ai-native-skills.tags: '[''ui'', ''patterns'', ''ux'', ''components'', ''delegation'', ''reference'']'
---

# UX Patterns for Developers

**Source**: https://ux-patterns-for-developers.com  
**GitHub**: https://github.com/thedaviddias/ux-patterns-for-developers  
**74 patterns · 11 categories · MDX format with code examples + a11y guidance**

## RULE: Delegate, Don't Improvise

When building any UI component, check this library FIRST.

**Decision rule — when to delegate here vs build internal:**

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

If a pattern exists here → install → load → extract spec → use verbatim.  
**HARD RULE: never improvise behavior that this library already specifies.**

---

## How to Use (Two Methods)

### Method 1: Use installed skills (preferred)
```bash
# Install a specific pattern as a skill
npx skills add https://github.com/thedaviddias/ux-patterns-for-developers --skill <name> --yes --global

# Examples
npx skills add https://github.com/thedaviddias/ux-patterns-for-developers --skill navigation-menu --yes --global
npx skills add https://github.com/thedaviddias/ux-patterns-for-developers --skill list-view --yes --global
npx skills add https://github.com/thedaviddias/ux-patterns-for-developers --skill back-to-top --yes --global

# Installed skills live at ~/.agents/skills/<name>
# Hermes auto-symlinks them — available immediately
```

### Method 2: Use `npx skills use` without installing
```bash
# Generate a prompt for one skill without installing
npx skills use thedaviddias/ux-patterns-for-developers@navigation-menu
```

### Method 3: Fetch raw MDX directly
```bash
curl https://raw.githubusercontent.com/thedaviddias/ux-patterns-for-developers/main/apps/web/content/patterns/<category>/<slug>.mdx
# Note: website domain ux-patterns-for-developers.com may be down — use raw GitHub instead
```

### Note on MCP
MCP endpoint exists at https://uxpatterns.dev/mcp but requires auth — use skills CLI instead.

---

## Pattern Catalog — 74 patterns, 11 categories

### 🧭 Navigation (11)
```
navigation-menu    /patterns/navigation/navigation-menu     ← primary navbar
hambuger-menu      /patterns/navigation/hambuger-menu       ← mobile (typo: missing 'r')
sidebar            /patterns/navigation/sidebar
tabs               /patterns/navigation/tabs
breadcrumb         /patterns/navigation/breadcrumb
megamenu           /patterns/navigation/megamenu
pagination         /patterns/navigation/pagination
back-to-top        /patterns/navigation/back-to-top
infinite-scroll    /patterns/navigation/infinite-scroll
load-more          /patterns/navigation/load-more
link               /patterns/navigation/link
```

### 📝 Forms (26)
```
button             /patterns/forms/button
text-field         /patterns/forms/text-field
textarea           /patterns/forms/textarea
checkbox           /patterns/forms/checkbox
radio              /patterns/forms/radio
toggle             /patterns/forms/toggle
select             /patterns/forms/selection-input
multi-select       /patterns/forms/multi-select-input
autocomplete       /patterns/forms/autocomplete
date-picker        /patterns/forms/date-picker
date-range         /patterns/forms/date-range
date-input         /patterns/forms/date-input
time-input         /patterns/forms/time-input
file-input         /patterns/forms/file-input
search-field       /patterns/forms/search-field
password           /patterns/forms/password
phone-number       /patterns/forms/phone-number
currency-input     /patterns/forms/currency-input
color-picker       /patterns/forms/color-picker
slider             /patterns/forms/slider
rating-input       /patterns/forms/rating-input
tag-input          /patterns/forms/tag-input
rich-text-editor   /patterns/forms/rich-text-editor
signature-pad      /patterns/forms/signature-pad
code-confirmation  /patterns/forms/code-confirmation
form-validation    /patterns/forms/form-validation
```

### 📊 Data Display (12)
```
table              /patterns/data-display/table
list-view          /patterns/data-display/list-view
card-grid          /patterns/data-display/card-grid
dashboard          /patterns/data-display/dashboard
chart              /patterns/data-display/chart
calendar           /patterns/data-display/calendar
filter-panel       /patterns/data-display/filter-panel
kanban-board       /patterns/data-display/kanban-board
statistics         /patterns/data-display/statistics
comparison-table   /patterns/data-display/comparison-table
timeline           /patterns/data-display/timeline
tree-view          /patterns/data-display/tree-view
```

### 📄 Content Management (7)
```
modal              /patterns/content-management/modal
accordion          /patterns/content-management/accordion
tooltip            /patterns/content-management/tooltip
popover            /patterns/content-management/popover
carousel           /patterns/content-management/carousel
drag-and-drop      /patterns/content-management/drag-and-drop
expandable-text    /patterns/content-management/expandable-text
```

### 🔔 User Feedback (6)
```
notification       /patterns/user-feedback/notification
loading-indicator  /patterns/user-feedback/loading-indicator
skeleton           /patterns/user-feedback/skeleton
progress-indicator /patterns/user-feedback/progress-indicator
empty-states       /patterns/user-feedback/empty-states
cookie-consent     /patterns/user-feedback/cookie-consent
```

### 🔐 Authentication (7)
```
login              /patterns/authentication/login
signup             /patterns/authentication/signup
password-reset     /patterns/authentication/password-reset
two-factor         /patterns/authentication/two-factor
social-login       /patterns/authentication/social-login
user-profile       /patterns/authentication/user-profile
account-settings   /patterns/authentication/account-settings
```

### 🤖 AI Intelligence (10)
```
ai-chat            /patterns/ai-intelligence/ai-chat
prompt-input       /patterns/ai-intelligence/prompt-input
streaming-response /patterns/ai-intelligence/streaming-response
ai-suggestions     /patterns/ai-intelligence/ai-suggestions
ai-loading-states  /patterns/ai-intelligence/ai-loading-states
ai-error-states    /patterns/ai-intelligence/ai-error-states
response-feedback  /patterns/ai-intelligence/response-feedback
model-selector     /patterns/ai-intelligence/model-selector
context-window     /patterns/ai-intelligence/context-window
token-counter      /patterns/ai-intelligence/token-counter
```

### 🔵 Advanced (3)
```
command-palette    /patterns/advanced/command-palette
search-results     /patterns/advanced/search-results
wizard             /patterns/advanced/wizard
```

### 🛒 E-Commerce (3)
```
product-card       /patterns/e-commerce/product-card
shopping-cart      /patterns/e-commerce/shopping-cart
checkout           /patterns/e-commerce/checkout
```

### 🖼️ Media (3)
```
image-gallery      /patterns/media/image-gallery
image-upload       /patterns/media/image-upload
video-player       /patterns/media/video-player
```

### 💬 Social (4)
```
activity-feed      /patterns/social/activity-feed
comment-system     /patterns/social/comment-system
like-button        /patterns/social/like-button
share-dialog       /patterns/social/share-dialog
```

---

## Integration with ui-components skill

`ui-components` skill = CSS templates (how it looks)  
`ux-patterns-for-developers` = behavior spec + a11y (how it works)

Use both together:
```
1. ui-components → copy CSS template for the component
2. ux-patterns-for-developers → fetch behavior spec + a11y requirements
3. Merge: apply behavior to the CSS template
```

---

## PITFALLS

```
□ hambuger-menu URL has a typo — "hambuger" not "hamburger" — use as-is
□ Patterns are MDX — fetch the page URL, not the raw GitHub file
□ Some patterns cover behavior only — still need ui-components for CSS
□ Don't fetch ALL 74 — only fetch the specific pattern you need
```
