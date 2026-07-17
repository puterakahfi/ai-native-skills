---
name: redesign-workflow
description: Autonomous UI/UX redesign loop — audit → spec → produce → review → fix until all gates pass. For landing pages, dashboards, app screens, portfolios, pricing pages.
license: MIT
metadata:
  ai-native-skills.version: 2.0.0
  ai-native-skills.author: puterakahfi
  ai-native-skills.requires: "design-foundation design-brand design-genre design-depth design-color design-typography design-spacing design-iconography design-visual design-layout design-strategy design-interaction design-system design-audit design-review design-refinement master-design macrostructures ui-components composition visual-hierarchy copywriting ux-psychology accessibility"
  ai-native-skills.type: workflow
  ai-native-skills.implements: ai-native-core/contracts/workflows/redesign.contract.yaml
  ai-native-skills.related_skills: '["design-visual","design-layout","design-interaction","design-strategy","design-system","design-audit","design-review","design-refinement"]'
---

# Redesign Workflow

<!-- CRITICAL RULES — read first, applies to every phase -->
```
HARD RULES (non-negotiable):
  1. Skill-first: patch the skill before patching the output — never the reverse
  2. Gates before delivery: minimum 8.0 average across all gates before DELIVER
  3. External before improvise: check ux-patterns-for-developers before writing component behavior
  4. After 2 failed patches on same file region → write_file full rewrite, never 3rd patch
  5. Sub-files are on-demand: load references/ only when entering that phase
```

## Core Loop

```
Phase 0   → PRE-FLIGHT       (scan existing design signals)
Phase 0.5 → GENRE + MACRO    (pick genre + macrostructure from brief)
  → load port: design-visual   (genre detection + visual language)
  → load port: design-layout   (macrostructure pick)
  → load: references/phase-genre-macro.md
Phase 0.75→ LAYERED PLAN     (classify work by layer)
  → load: references/phase-genre-macro.md
Phase 2   → VALUE ALIGNMENT
  → load port: design-strategy (cro only if conversion goal)
Phase 3   → SPEC CONFIRM     (align constraints before producing)
Phase 4   → PRODUCE          (derive from ports, not improvise)
  → load port: design-visual   (motion, composition)
  → load port: design-layout   (ui-components, responsiveness)
  → load port: design-interaction (patterns before implementing behavior)
  → load port: design-strategy (copywriting, ux-psychology)
  → load: references/phase-produce.md
Phase 5   → REVIEW           (foundation gates first, then genre/brand)
  → load: design-foundation   (F1–F7 hard gates — any fail blocks delivery)
  → load port: design-system  (accessibility + token gates)
  → load: references/phase-review-gates.md
Phase 6   → FIX              (skill-first fix loop)
  → load: references/phase-fix-loop.md
Phase 7   → DELIVER
  → load: references/phase-deliver.md

Exit: avg >= 8.0 OR max_iterations (default 5) reached
On max: deliver best attempt + honest gap report
```

---

## When to Use

Good fits:
- landing pages, portfolios, personal sites, pricing pages, docs homepages
- dashboards, admin panels, app screens, onboarding flows, checkout flows
- copy/hierarchy/CTA/CRO refinement with explicit business value
- design audit followed by prototype or patch

Use `design-audit` instead when: audit-only, no redesign needed yet  
Use `design-refinement` instead when: existing design is good, targeting specific failing gates  
Do not use for: product from zero (`product-development-workflow`), non-visual features (`new-feature-workflow`), bugs (`bugfix-workflow`)

---

## Parameters

| Param | Required | Description |
|---|---|---|
| `target` | YES | URL, screenshot, repo path, or app surface |
| `goal` | YES | What the surface should achieve |
| `surface_type` | NO | `landing-page` / `dashboard` / `app-screen` / `portfolio` / `pricing-page` |
| `content_inventory` | NO | Existing content to preserve; LIVE products only for showcases |
| `cta` | NO | Primary CTA — default: none |
| `audience` | NO | Target audience — default: general |
| `output_mode` | NO | `audit-only` / `spec-only` / `prototype` / `patch` — default: `prototype` |
| `output_path` | NO | Save path — default: `/tmp/{target}-redesign.html` |

---

## Phase 0: PRE-FLIGHT

Scan target for existing design signals:

```
0. design-brand file? → skill_view(name='design-brand', file_path='references/<client>.md')
   Found  → BRAND LOCK: respect tokens, genre adapts within brand only
   Not found → free genre selection
1. design.md / DESIGN.md at root → locked system, overrides all picks
2. CSS :root vars → existing palette + type scale
3. Theme infra → next-themes / .dark / [data-theme] / ThemeProvider
4. package.json → framework, motion libs, font packages
5. /* macrostructure: <name> */ stamp in CSS
6. browser_navigate/vision for live URLs; inspect files for local

Emit once:
  Pre-flight findings:
  · Palette:            [found | not found]
  · Font stack:         [found | not found]
  · Theme infra:        [none | class | data-theme | next-themes | custom]
  · Theme default:      [light | dark | system | unknown]
  · Motion stance:      [motion-on | motion-cut]
  · Macrostructure:     [name | none]
  · Design system lock: [yes (design.md) | no]

  Hallmark will preserve: [list]
  Will introduce: [list]
  Correct me before I proceed.
```

---

## Phase 2: VALUE ALIGNMENT

Run `business-value-alignment` before producing:
```
audit findings → user value → business value → metrics → continue/narrow/experiment/stop
```
Do not proceed to decorative redesign when value is unclear.

---

## Phase 3: SPEC CONFIRM

Align before producing:
```
SPEC CONFIRMED
──────────────
Surface:  [type]
Goal:     [one sentence]
Content:  [list — LIVE only for showcases]
CTA:      [label | none]
Audience: [who]
Nav:      [items]
Theme:    [light-only | dark-only | dual-theme]
```

---

## Skill Delegation Rule (applies to Phase 4 + Phase 6)

```
DELEGATE TO EXTERNAL SKILL when ALL three are true:
  ✓ Stable   — well-maintained (W3C, major OSS, established community)
  ✓ Trusted  — a11y + behavior + edge cases already validated
  ✓ Worth it — months to build internally; seconds to delegate

BUILD INTERNAL (ui-components) when:
  ✓ Brand/product-specific — CSS tokens, visual templates, copy tone
  ✓ Not covered externally — check catalog first, then build
  ✓ Need opinionated version — external too generic

BOTH together (preferred):
  external → behavior, a11y, interaction, edge cases   (HOW it works)
  internal → CSS template, tokens, visual, brand        (HOW it looks)
```

Trusted external: `ux-patterns-for-developers` (74 patterns)
→ `npx skills add https://github.com/thedaviddias/ux-patterns-for-developers --skill <name> --yes --global`

---

<!-- CRITICAL RULES repeated at bottom — Lost in Middle fix -->
```
REMINDER — exit only when:
  □ All gates avg >= 8.0
  □ Gate 21 (Reduced Motion) = 10 (hard gate, 0 = full fail)
  □ touchFail = 0
  □ CSS sheets > 0
  □ No gate < 6 (floor rule)
```
