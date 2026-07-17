---
name: readability
description: Text readability scoring and optimization — line length, contrast ratio, type size, line height, density, and cognitive ease. Produces a readability score 0–10 per dimension. Minimum score 8 required before design passes.
license: MIT
metadata:
  ai-native-skills.version: 1.0.0
  ai-native-skills.author: puterakahfi
  ai-native-skills.type: skill
  ai-native-skills.implements: ai-native-core/contracts/skills/design/readability.contract.yaml
  ai-native-skills.related_skills: "['design-system', 'accessibility', 'ux-psychology', 'master-design']"
---

# Readability Skill

<!-- ═══════════════════ HARD RULES — enforce before anything else ═══════════════════ -->

## HARD RULES (always active — never override)

```
1. Hero bio / short display copy:  max-width: 44ch   ← ch units ONLY (px exceeds CPL at large viewport)
2. Body prose:                      max-width: 65ch
3. Body font-size:                  >= 16px           smallest element >= 12px
4. Primary text contrast:           >= 4.5:1          secondary text >= 3:1
```

> These four rules are non-negotiable. A design that violates any of them **auto-fails**
> regardless of the dimension scores below.

---

## Core Principle

```
Readability is not aesthetic — it is functional.
If text requires effort to read, it will not be read.

Readability has 6 measurable dimensions:
  1. Line length    — how many characters per line
  2. Contrast ratio — foreground vs background
  3. Type size      — minimum sizes for different contexts
  4. Line height    — space between lines
  5. Density        — information per viewport area
  6. Cognitive ease — vocabulary and sentence complexity

Each dimension scored 0–10. Minimum 8 to pass.
Overall readability score = average of 6 dimensions.
```

---

## 6-Dimension Overview

Load the reference files below for full scoring tables, CSS snippets, and tools.

### Dimension 1 — Line Length
**Optimal 45–75 CPL.** Full-width prose (> 90 CPL) auto-fails D1.
→ See `references/line-contrast-size.md` § Dimension 1

### Dimension 2 — Contrast Ratio
**Primary ≥ 4.5:1 (AA normal), secondary ≥ 3:1.**
→ See `references/line-contrast-size.md` § Dimension 2

### Dimension 3 — Type Size
**Body ≥ 16px, smallest element ≥ 12px.**
→ See `references/line-contrast-size.md` § Dimension 3

### Dimension 4 — Line Height (Leading)
**Body 1.5–1.75; headings 1.0–1.35.**
→ See `references/rhythm-density-ease.md` § Dimension 4

### Dimension 5 — Density
**25–50% whitespace in content sections; breathing room ≠ dead space.**
→ See `references/rhythm-density-ease.md` § Dimension 5

### Dimension 6 — Cognitive Ease
**Flesch-Kincaid ≤ 8; sentences ≤ 20 words average.**
→ See `references/rhythm-density-ease.md` § Dimension 6

---

## Readability Audit Workflow

1. Load `references/line-contrast-size.md` — audit D1, D2, D3
2. Load `references/rhythm-density-ease.md` — audit D4, D5, D6
3. Fill the scoring rubric template (in `references/scoring-fixes.md`)
4. Any dimension < 8 → apply fix from Common Readability Fixes table
5. Re-audit failing dimensions until all ≥ 8
6. Overall score = average; **PASS requires ≥ 8.0**

---

## Reference Files

| File | Contents |
|---|---|
| `references/line-contrast-size.md` | Dimension 1 Line Length · Dimension 2 Contrast · Dimension 3 Type Size |
| `references/rhythm-density-ease.md` | Dimension 4 Line Height · Dimension 5 Density · Dimension 6 Cognitive Ease |
| `references/scoring-fixes.md` | Readability Scoring Rubric template · Common Readability Fixes table |

---

<!-- ═══════════════════ HARD RULES — repeated at bottom for quick-scroll ═══════════════════ -->

## HARD RULES (bottom reminder)

```
1. Hero bio / short display copy:  max-width: 44ch   ← ch units ONLY (NOT px)
2. Body prose:                      max-width: 65ch
3. Body font-size:                  >= 16px           smallest element >= 12px
4. Primary text contrast:           >= 4.5:1          secondary text >= 3:1
```
