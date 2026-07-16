---
name: redesign-workflow
description: Autonomous UI/UX redesign and refinement loop — audit an existing surface, confirm spec, produce prototype or patch, run design-review gates, fix failures, deliver only when all gates pass. Use for landing pages, dashboards, app screens, onboarding flows, pricing pages, and portfolios.
license: MIT
metadata:
  ai-native-skills.version: 1.0.0
  ai-native-skills.author: puterakahfi
  ai-native-skills.type: workflow
  ai-native-skills.implements: ai-native-core/contracts/workflows/redesign.contract.yaml
  ai-native-skills.related_skills: '[''business-value-alignment'', ''master-design'', ''ux-psychology'', ''design-review'', ''design-system'', ''dark-light-theming'', ''ux-ui-patterns'', ''readability'', ''responsiveness'', ''accessibility'', ''motion-design'', ''design-genre'', ''macrostructures'', ''content-strategy'', ''web-performance'']'
  ai-native-skills.skill_load_order: '[{''phase'': ''preflight'', ''skills'': [''design-genre'', ''macrostructures'', ''information-architecture'', ''dark-light-theming'']}, {''phase'': ''audit'', ''skills'': [''ux-psychology'', ''accessibility'', ''readability'', ''responsiveness'', ''web-performance'', ''dark-light-theming'']}, {''phase'': ''value_alignment'', ''skills'': [''business-value-alignment'', ''product-manager'', ''content-strategy'', ''cro'']}, {''phase'': ''spec'', ''skills'': [''product-manager'', ''master-design'', ''content-strategy'', ''dark-light-theming'']}, {''phase'': ''produce'', ''skills'': [''design-genre'', ''macrostructures'', ''ui-components'', ''ux-patterns-for-developers'', ''design-system'', ''dark-light-theming'', ''ux-ui-patterns'', ''master-design'', ''motion-design'', ''composition'', ''visual-hierarchy'', ''copywriting'', ''cro'']}, {''phase'': ''pre-emit-critique'', ''skills'': [''master-design'', ''ux-psychology'', ''composition'', ''visual-hierarchy'', ''copywriting'', ''cro'']}, {''phase'': ''review'', ''skills'': [''design-review'', ''dark-light-theming'', ''readability'', ''responsiveness'', ''accessibility'', ''motion-design'', ''web-performance'', ''content-strategy'', ''composition'', ''visual-hierarchy'',
    ''copywriting'', ''cro'']}, {''phase'': ''fix'', ''skills'': [''design-genre'', ''macrostructures'', ''design-system'', ''dark-light-theming'', ''ux-ui-patterns'', ''master-design'', ''readability'', ''responsiveness'', ''motion-design'', ''content-strategy'', ''composition'', ''visual-hierarchy'', ''copywriting'', ''cro'']}]'
---

# Redesign Workflow

## The Core Rule

```
This workflow runs autonomously until ALL design-review gates pass.
No delivery before gates are green.

Loop:
  audit → spec → produce → review → fix (if fail) → review → ... → deliver

Layer order:
  strategy → UI → UX → voice → interaction → delight/expression → verification

Exit condition: all gates pass OR max_iterations (3) reached
On max_iterations: deliver best attempt + explicit gate failure report
```

---

## When to Use

Use this workflow for **existing UI/UX surfaces** that need refinement, redesign, polish, or conversion/readability/accessibility improvement.

Good fits:

- landing pages, personal sites, portfolios, pricing pages, docs homepages
- dashboards, admin panels, app screens, onboarding flows, checkout flows
- copy/hierarchy/CTA/CRO refinement on an existing surface with explicit business value
- visual polish where the product goal already exists
- design audit followed by prototype or patch

Do not use for:

- product idea from zero; use `product-development-workflow`
- non-visual feature implementation; use `new-feature-workflow`
- bug isolation; use `bugfix-workflow`
- deploy/release only; use `deployment-workflow`

Surface-specific details belong in the prompt, not in new workflow names.

---

## Parameters

| Param | Required | Description |
|---|---|---|
| `target` | YES | URL, screenshot, repo path, route, or app surface to audit and refine |
| `surface_type` | NO | `landing-page`, `dashboard`, `app-screen`, `onboarding-flow`, `pricing-page`, `portfolio`, `docs`, or product-defined |
| `goal` | YES | What the surface should achieve |
| `content_inventory` | NO | Existing content/products/features to preserve or prioritize; for product showcases, list LIVE products only |
| `cta` | NO | Primary CTA — default: none |
| `audience` | NO | Target audience — default: general |
| `output_mode` | NO | `audit-only`, `spec-only`, `prototype`, or `patch`; default: `prototype` unless user asks to stop for approval |
| `output_path` | NO | Where to save prototype/output — default: `/tmp/{target}-redesign.html` when producing HTML |

---

## Phase 0: PRE-FLIGHT

Before anything — scan the target for existing design context:

```
Pre-flight scan (in order):
  1. design.md / DESIGN.md at project root → locked design system, overrides all picks
  2. CSS custom properties (:root vars) → existing palette + type scale
  3. Theme infrastructure → `next-themes`, `.dark`, `[data-theme]`, `ThemeProvider`, existing toggle components
  4. package.json deps → framework, motion libs, font packages
  5. Existing macrostructure stamp: /* macrostructure: <name> */ in any CSS
  6. Existing surface: browser_navigate/browser_vision for URLs, or inspect local files/screenshots when provided

Output (emit once):
  Pre-flight findings:
  · Existing palette: [found | not found]
  · Existing font stack: [found | not found]
  · Theme infrastructure: [none | class-based | data-theme | next-themes | custom]
  · Current theme default: [light | dark | system | unknown]
  · Motion stance: [motion-on | motion-cut] (based on deps)
  · Macrostructure in use: [name | none]
  · Design system locked: [yes (design.md) | no]

  Hallmark will preserve: [list]
  Will introduce: [list]
  If wrong: correct me before I proceed.

If no signals found: "No pre-flight signals — proceeding with full stack."
```

## Phase 0.5: GENRE + MACROSTRUCTURE PICK

This phase has two gates. Both must pass before Phase 1.

---

### Gate A: Genre Detection (from `design-genre` skill)

Read signals from brief + pre-flight. Assign one genre.

```
Signal → Genre mapping:
  personal page + no CTA + showcase only     → editorial
  SaaS product + pricing + CTAs              → modern-minimal
  creative portfolio + visual work           → atmospheric
  game / toy / consumer app                  → playful
```

State explicitly:
```
Genre: [name]
Signals matched: [list signals from brief that confirm this genre]
```

---

### Gate B: Macrostructure Pick (from `macrostructures` skill)

**Step 1 — Extract brief signals:**
```
□ Primary goal:      [convert | showcase | inform | entertain]
□ Identity weight:   [high = person/brand leads | low = work leads]
□ Content volume:    [N products / N sections / N words]
□ Audience:          [hiring manager | client | developer | general]
□ CTA present:       [yes | no]
□ Visual assets:     [yes = images/screenshots | no = text only]
```

**Step 2 — Match signals to pattern:**

| Goal | Identity | Content vol | Audience | Best macrostructure |
|---|---|---|---|---|
| showcase | high | low (≤3) | hiring manager | Marquee Hero or Specimen |
| showcase | high | low (≤3) | creative client | Studio or Atelier |
| showcase | low | high (4+) | any | Bento or Workbench |
| inform | low | high | developer | Long Document or Almanac |
| convert | low | medium | general | Newsprint or Manifesto |
| brand | high | low | general | Manifesto or Lumen |

**Step 3 — Diversification check (secondary, not primary):**
```
Previous macrostructure: [name from last iteration or "none"]
Candidate macrostructure: [name]
Axes that differ: [list — layout lead / heading / divider / button / image / reveal]
Must differ on ≥2 axes IF previous exists.
If brief-match and diversification conflict → brief-match WINS.
```

**Step 4 — State your pick with justification:**
```
Macrostructure: [name]
Genre: [name]

Justified by brief signals:
  - [signal 1] → [why this supports the pick]
  - [signal 2] → [why this supports the pick]
  - [signal N] → ...

NOT chosen [alternative] because:
  - [reason 1]
  - [reason 2]

Diversification: differs from [previous] on [N] axes: [list axes]
```

**Justification is mandatory.** "Differs from previous" alone is NOT sufficient.
If you cannot justify from brief signals, revisit Step 2 before proceeding.

---

### pkahfi.com example (reference)

```
Brief signals:
  Primary goal:   showcase
  Identity:       high — personal landing page, person leads
  Content vol:    low — 2 LIVE products only
  Audience:       hiring manager / fellow engineer
  CTA:            none
  Visual assets:  none (text-led)

Signal → pattern match:
  showcase + identity high + content low + hiring manager → Marquee Hero or Specimen

Pick: Marquee Hero
  - Identity high: full-width name above fold, work below
  - 2 products: stacked list, not grid (low volume = list beats grid)
  - No CTA: hero does not need action urgency layout
  - Hiring manager: credibility via copy, not visual flair

NOT Studio:
  - Studio = 50/50 split → identity and work equal weight
  - pkahfi.com identity should lead, work is secondary
  - Studio better for creative agency where work IS the identity
```

Load `design-genre` skill. Detect genre from brief signals.
Load `macrostructures` skill. Pick ONE macrostructure.

```
State out loud before writing any code:

Genre: [editorial | modern-minimal | atmospheric | playful]
Signal: [what triggered it | default]
Macrostructure: [name]
Layout lead: [type-led | image-led | grid-led | document-led]
Differs from last on: [axes | first build]

If unsure between 2 macrostructures: offer 3 from categorically different groups,
let user pick, or pick the most distant from default (not Specimen, not Marquee Hero).
```

---

## Phase 0.6: VISUAL LANGUAGE DEFINITION

Before producing a theme-specific redesign, define the visual language in concrete values. A named theme is not a color swap. If the user says “minimalist”, “zen”, “brutalist”, “editorial”, “premium”, or similar, translate the word into rules before touching UI.

### Zen / Minimalist definition

Zen minimalist design is the disciplined use of **silence, emptiness, restraint, and natural rhythm** to create focus. It is closer to ink painting, tea ceremony, gallery walls, and quiet architecture than to “clean SaaS cards with muted colors”.

```text
Core values:
  Ma / emptiness       → negative space is content, not unused area
  Restraint            → remove elements before styling them
  Natural imperfection → asymmetry, organic edges, light texture, not perfect SaaS symmetry
  Stillness            → no loud hover lift, bouncing motion, glow, or decorative urgency
  One focal object     → one strong anchor per viewport: word, image, mark, or object
  Low visual density   → few cards, few badges, few borders, fewer CTAs
  Muted contrast       → ink/stone/paper/sage, mostly neutral; accent is rare
  Editorial hierarchy  → typography breathes; body text is quiet; labels are small
  Material subtlety    → paper grain, ink wash, stone, mist, soft shadow only when needed
```

### Zen / Minimalist UI rules

```text
Palette:
  ✓ paper white, warm ivory, mist gray, charcoal, ink black, stone, sage
  ✓ one low-chroma accent used sparingly
  ✗ swapping blue for brown/green without reducing density
  ✗ bright startup blue, neon, gradient mesh, glassmorphism

Layout:
  ✓ large asymmetrical whitespace
  ✓ narrow text columns and intentional empty areas
  ✓ sections can feel like scrollable prints/posters, not dashboard panels
  ✗ equal-weight card catalogs unless content truly requires it
  ✗ filling every row/column because grid space exists

Typography:
  ✓ fewer type sizes, lighter weights, larger line-height
  ✓ one display moment per viewport; everything else supports it
  ✗ font-black everywhere
  ✗ H1/H2/H3 all shouting with the same weight

Imagery / ornament:
  ✓ ink wash, abstract brush, mist, mountain/roofline silhouette, single object, thin rule
  ✓ decorative elements must create pause or orientation
  ✗ random icons on every card
  ✗ dot grids/blueprints as default “tech texture” when zen is requested

Motion:
  ✓ fade, slow reveal, opacity, tiny translate only when it helps orientation
  ✗ hover lift on every card
  ✗ springy/bouncy motion
```

### Zen / Minimalist anti-patterns

Auto-fail the UI layer if any of these appear after a zen/minimalist request:

```text
❌ “coklat rame”: only changing palette to brown/warm tones while density stays high
❌ many cards + many badges + many tags + many icons = catalog, not zen
❌ visible grid backgrounds dominating the viewport
❌ every section has a big bold headline and bordered card cluster
❌ accent used on labels, icons, badges, CTA, logo dot, and bullets all at once
❌ dark mode simply inverts the whole page into heavy charcoal panels
❌ motion/hover effects added before silence and spacing are solved
```

### Zen / Minimalist check

Before calling a zen/minimalist pass successful, answer:

```text
1. What did we remove?
2. Where is the intentional emptiness?
3. What is the single focal object/idea in this viewport?
4. Which elements became quieter, not just recolored?
5. If all color is removed, does the composition still feel calm?
```

---

## Phase 0.75: LAYERED REDESIGN PLAN

Before producing, classify the work into layers. Redesign is not one undifferentiated "make it better" pass. Each iteration must name which layer it is improving and which layers are intentionally left alone.

```
Layered plan:
  0. Strategy Layer
  1. UI Layer
  2. UX Layer
  3. Voice Layer
  4. Interaction Layer
  5. Delight / Expression Layer
  6. Verification Layer
```

### Layer 0 — Strategy / Positioning

Focus: why the surface exists and what should be remembered first.

Questions:
```
□ What is the surface trying to become? portfolio, SaaS page, docs home, app screen, dashboard?
□ Who is the primary audience?
□ What should be understood in 5 seconds?
□ Which content is primary, secondary, hidden, or deferred?
□ Is there a CTA, or is this a showcase/informational surface?
```

Output:
```
Strategy: [one sentence]
Primary audience: [audience]
First impression: [one idea]
Content priority: [ordered list]
Non-goals: [what the page must NOT feel like]
```

### Layer 1 — UI

Focus: visual structure and aesthetic quality.

Scope:
```
layout, grid, typography, spacing, hierarchy, color, light/dark theme,
visual density, responsive layout, component consistency
```

UI gates:
```
□ Named visual language is defined as rules before styling starts
□ Theme change reduced density/noise, not just changed colors
□ Visual hierarchy is readable at a glance
□ Typography scale is deliberate, not arbitrary
□ Layout matches content count and priority
□ Theme is visually coherent in every supported mode
□ Cards, badges, nav, CTA, and section rhythm feel from one system
□ No visual slop: generic gradients, equal-card filler, random icon use
```

### Layer 2 — UX

Focus: what the user experiences when they read, choose, click, toggle, or move through the surface.

Scope:
```
navigation flow, CTA clarity, theme-switcher behavior, hover/focus/tap states,
user feedback, link target correctness, empty states, labels/messages,
accessibility behavior, route/hash correctness
```

UX gates:
```
□ Every click target leads where the user expects
□ CTAs are clear, not competing or fake
□ Theme toggle works both ways and communicates next action
□ Focus, hover, active, loading, empty, and disabled states are understandable
□ Messages and labels explain state without jargon
□ Keyboard and screen-reader behavior are preserved
```

### Layer 3 — Voice / Copy

Focus: what the interface says and how specific it feels.

Scope:
```
headline, subcopy, CTA label, project description, status wording,
microcopy, error/empty messages, tone/register
```

Voice gates:
```
□ H1 is a stance, not a job title or generic claim
□ Copy is specific to the product/person/domain
□ CTA labels describe the action, not vague marketing
□ Status language is honest: live, planned, lab, private, archived
□ No filler words: seamless, leverage, cutting-edge, world-class, modern solution
```

### Layer 4 — Interaction

Focus: how the interface responds over time.

Scope:
```
hover, focus, active, pressed, selected, scroll behavior, theme transition,
navigation transition, keyboard interaction, reduced motion
```

Interaction gates:
```
□ Interactive states provide useful feedback
□ Focus is visible and not overridden
□ Motion uses transform/opacity and respects prefers-reduced-motion
□ Hover-only affordances have touch/keyboard equivalents
□ State changes are reversible or clearly final
```

### Layer 5 — Delight / Expression

Formal name for "pemanis". Add only after strategy/UI/UX/voice are coherent.

Scope:
```
motion, illustration, icon treatment, decorative texture, diagrams,
ambient backgrounds, mascot/visual metaphor, empty-state illustration,
signature visual motif
```

Delight gates:
```
□ The enhancement clarifies character, meaning, or memory
□ It is not hiding weak copy, weak hierarchy, or missing content
□ It has a named role: orientation, affordance, emphasis, atmosphere, reward
□ It can be removed without breaking comprehension, but keeping it improves recall
□ It is lightweight and does not hurt accessibility or performance
```

### Layer 6 — Verification

Focus: prove the redesign works without breaking the user's iteration flow.

During active visual loops:
```
□ browser visual check
□ console/DOM probes
□ route/hash/link click checks
□ theme checks in all supported modes
□ git diff --check on changed files
```

Only when approved / ready to deploy:
```
□ full lint
□ full build
□ typecheck/test where relevant
□ performance/a11y audits if release-critical
```

### Iteration Declaration

Every iteration must start with a short declaration:

```
Iteration N focus:
  Primary layer: [strategy | UI | UX | voice | interaction | delight | verification]
  Secondary layer(s): [optional]
  Not touching: [layers intentionally deferred]
  Success criteria: [specific checks]
```

If a layer fails, do not jump to delight. Fix the failed lower layer first:

```
Strategy failure blocks UI polish.
UI failure blocks delight.
UX failure blocks final verification.
Voice failure blocks motion/illustration polish.
```



```
1. browser_navigate(url)
2. browser_snapshot(full=true) — capture DOM structure
3. browser_vision("Full visual audit: hierarchy, CTA, typography, colors, whitespace, first impression")
4. Scroll and capture multiple sections if needed

Audit checklist:
  □ Current H1 and value proposition — what does it say?
  □ CTA count and placement — how many, where?
  □ Navigation items — count and labels
  □ Products/sections shown — which are LIVE vs DEV?
  □ Typography — feels proportional or arbitrary?
  □ Color usage — accent used for multiple meanings?
  □ Whitespace — uniform or rhythmic?
  □ First impression 50ms — what does user capture?
  □ Accessibility signals — semantic HTML present?
```

Output: `audit_report` object with findings per gate.

---

## Phase 2: VALUE ALIGNMENT

Before producing a redesign spec, run `business-value-alignment`:

```text
audit findings → user value → business value → leading/lagging/guardrail metrics → continue/narrow/experiment/stop verdict
```

Do not proceed to decorative redesign when the value is unclear. Narrow the scope to clarity, credibility, conversion, accessibility, or performance outcomes.

---

## Phase 3: SPEC CONFIRM

Before producing — align on constraints. Extract from params or ask:

```
spec = {
  goal:      "personal landing page" | "portfolio" | "SaaS marketing" | ...,
  surface_type: "landing-page" | "dashboard" | "app-screen" | "onboarding-flow" | "pricing-page" | "portfolio" | ...,
  content_inventory: [existing content/products/features to preserve or prioritize],
  cta:       "hire me" | "contact" | null,
  audience:  "hiring manager" | "client" | "developer" | "general",
  nav_items: derived from goal (3 max for personal),
  hero_copy: must pass 50ms test — stance, not job description,
  theme: {
    mode_support: "light-only" | "dark-only" | "dual-theme",
    default_mode: "light" | "dark" | "system",
    toggle_required: boolean,
    verification_required: ["light", "dark"] when dual-theme
  }
}
```

If `content_inventory` is not provided → extract from audit. For product showcases, keep LIVE products only.
If `cta` not provided → default null (showcase only).

State spec explicitly before proceeding:
```
SPEC CONFIRMED
──────────────
Surface:  personal landing page
Goal:     showcase only
Content:  Blog (LIVE), Blueprint (LIVE)
CTA:      none
Audience: general / developer community
Nav:      Work · About · Contact
```

---

## Phase 4: PRODUCE

Produce the requested output (`prototype` or `patch`). For HTML prototypes, apply design in this order:
1. Genre tokens (from `design-genre` skill — voice, color family, motion stance)
2. Visual language definition (e.g. zen/minimalist key values before styling)
3. Macrostructure structure (from `macrostructures` skill — layout, heading, dividers)
4. Design system tokens (from `design-system` skill — spacing, type scale, color semantic)
5. Theme architecture (from `dark-light-theming` skill — semantic token mapping, toggle, FOUC prevention, contrast per mode)
6. Motion (from `motion-design` skill — only if motion-on)
7. Content (from `content-strategy` skill — microcopy, button labels, empty states)

Stamp at top of CSS (mandatory):
```css
/*
 * macrostructure: [name]
 * genre: [genre]
 * theme: [theme name | custom]
 * iteration: [N]
 */
```

### Pre-Emit Self-Critique (run BEFORE delivering output)

Score 1–5 on six axes. Anything < 3 = revision pass before emit.

```
Pre-emit critique:
  P (Philosophy):  Does every element have a reason to exist?        __ / 5
  H (Hierarchy):   Is the visual hierarchy immediately readable?     __ / 5
  E (Execution):   Are spacing, scale, alignment consistent?         __ / 5
  S (Specificity): Is copy specific, not generic? No AI slop?        __ / 5
  R (Restraint):   Is anything decorative that could be removed?     __ / 5
  V (Variety):     Does this differ structurally from last output?   __ / 5

Revision trigger: any axis < 3
Fix the lowest axis before delivering.

Stamp in CSS: /* pre-emit: P_ H_ E_ S_ R_ V_ */
```

### Slop Red List (auto-revision if any present)

```
❌ "Get started for free" as primary CTA (unless product requires it)
❌ Hero with H1 + 3 bullet features + CTA button (template pattern)
❌ "Trusted by X companies" with logo row in hero
❌ Testimonial grid with star ratings
❌ Gradient mesh background behind text
❌ Generic stock photo of diverse people in office
❌ "Seamless", "leverage", "world-class", "cutting-edge" in copy
❌ 6+ feature cards in equal-size grid
❌ Login button in hero for first-time visitor page
❌ All-caps nav with 5+ items
```


When `output_mode=prototype`, generate a complete, self-contained HTML file. When `output_mode=patch`, modify the existing surface directly and run the same gates against the result.

### Mandatory Design System (apply every time)

**Typographic Scale — 1.333 Perfect Fourth:**
```css
--text-xs:   0.563rem;
--text-sm:   0.75rem;
--text-base: 1rem;
--text-lg:   1.333rem;
--text-xl:   1.777rem;
--text-2xl:  2.369rem;
--text-3xl:  3.157rem;
--text-4xl:  4.209rem;
/* Mobile: cap H1 at --text-3xl to keep H1/body ratio ≤ 3.5x */
```

**Color Semantic (declare before using):**
```css
/* Each var = ONE semantic role ONLY */
--live:             /* LIVE status indicator — nowhere else */
--interactive-hover:/* hover state — nowhere else */
--bg:               /* base background */
--bg-alt:           /* alternate section background (figure/ground) */
--surface:          /* card/elevated surface */
--border:           /* dividers */
--bright:           /* headings, primary content */
--text:             /* body text */
--subtle:           /* supporting info */
--muted:            /* decorative, disabled */
```

**Figure/Ground:**
```css
/* Always add depth to background — never flat single color */
background-image: radial-gradient(circle, #1e1e1e 1px, transparent 1px);
background-size: 32px 32px;
/* OR: linear-gradient(180deg, #0f0f0f 0%, #0a0a0a 100%) */
/* OR: alternating section backgrounds */
```

**Theme System (mandatory for dual-theme surfaces):**
```
If the app already has theme infrastructure, preserve it instead of adding a second system:
  next-themes + attribute="class" → use `.dark` / `dark:` utilities
  next-themes + attribute="data-theme" → use `[data-theme="dark"]`
  custom/localStorage → inspect existing script before changing

Theme toggle requirements:
  □ one toggle in global nav or settings area
  □ aria-label changes with the next action: "Switch to dark theme" / "Switch to light theme"
  □ touch target ≥ 44×44px
  □ no hydration mismatch: render stable fallback until mounted if using next-themes
  □ all theme colors use semantic tokens; no mode-specific hardcoded hex in components

Dual-theme visual requirements:
  □ Verify light mode screenshot/DOM
  □ Toggle to dark mode and verify screenshot/DOM
  □ Toggle back and verify state reversibility
  □ Status colors remain readable in both modes
  □ Inverse sections are intentional and documented, not accidental token inversion
```

**Whitespace Rhythm:**
```
Hero section:    min-height: 100vh — maximum space, this is a statement
Content sections: 80–96px padding — tighter, reading mode
Contact section:  48–64px padding — minimal, closing quietly
Footer:           24–32px padding — functional only
```

**Empty State Rule:**
```
Count products before choosing layout:
  1 product  → full width
  2 products → full-width stacked (NOT 2-col grid)
  3 products → 3-col grid or stacked
  4+ products → grid
```

**First Impression (50ms):**
```
Hero copy must be a stance, not a job description.
Test: read H1 in 50ms — what ONE idea survives?
FAIL: "Full Stack Engineer specializing in scalable architecture"
PASS: "One codebase. Five products." / "I build systems meant to last."
```

**Accessibility:**
```html
<!-- Semantic structure required -->
<nav>, <main>, <section>, <footer>
<!-- Heading hierarchy: H1 → H2 → H3 — no skipping -->
<!-- Live badge: aria-hidden on decorative elements -->
<!-- Links: descriptive text, rel="noopener" for external -->
<!-- Images: meaningful alt or alt="" if decorative -->
```

---

## Phase 5: REVIEW (Scored Gate Check)

### Verification cadence for visual loops

During active creative redesign loops, do **not** run expensive or deploy-grade verification (`npm run build`, full lint, full typecheck) on every iteration. Keep the loop visual and fast until the user approves the direction or says it is ready to deploy/commit.

Use lightweight iteration checks instead:

```text
- browser visual inspection of changed routes
- browser visual inspection in every supported theme mode (light/dark/system when applicable)
- theme toggle click checks: light → dark → light, aria-label updates, persisted class/data attribute updates
- browser console/DOM probes for horizontal overflow, visible CSS, H1 position, and touch targets
- link/navigation click checks for changed CTAs/hash links
- git diff --check on changed files for patch hygiene
```

Only run full build/lint/typecheck when:

```text
- user says the design is approved / "sip" / ready to deploy
- preparing a commit or PR
- a code change is non-visual and correctness depends on the build
- the user explicitly asks for full verification
```

If lint/build is blocked by repo setup while still in visual loop, report the blocker but do not keep retrying the same command; continue with lightweight browser checks until deploy readiness.

### Theme verification inside redesign loops

When the project has a theme provider, `.dark`/`[data-theme]` tokens, or a theme toggle, treat theme as part of the redesign surface — not an optional afterthought. Load `dark-light-theming` when adding or evaluating theme behavior.

For each affected route, verify both modes before calling the iteration reviewable:

```text
1. Light visual check: nav, hero, cards, badges, CTAs, contact/footer, texture/grid visibility
2. Dark visual check: same sections after toggling theme
3. Toggle behavior: aria-label changes to the next action (e.g. "Switch to light theme")
4. DOM probes in both modes: no horizontal overflow, touch targets >= 44px, body bg/fg changed
5. Link/hash checks remain valid after theme toggling
```

Theme-specific gates:

```text
Gate T1: Token architecture — uses semantic tokens (`bg-background`, `text-foreground`, `border-border`) rather than hardcoded mode colors
Gate T2: Toggle accessibility — real button, >=44px target, accessible label describes next action
Gate T3: Mode contrast — primary/secondary text and badges remain readable in light and dark
Gate T4: Inversion intent — inverse sections (e.g. contact) are intentional; if they flip bright in dark mode, call it out as a design decision or polish flag
```

Run ALL gates across 7 skill dimensions plus universal composition/hierarchy/motion rules. Every gate scored 0–10. Minimum **8.0 average** to pass.

```
DESIGN REVIEW — Iteration N
════════════════════════════════════════════════════

── LAYER FOCUS ────────────────────────────────────
Primary layer: [strategy | UI | UX | voice | interaction | delight | verification]
Secondary layers: [list]
Deferred layers: [list]
Layer verdict:
  Strategy:    PASS | FAIL | DEFERRED
  UI:          PASS | FAIL | DEFERRED
  UX:          PASS | FAIL | DEFERRED
  Voice:       PASS | FAIL | DEFERRED
  Interaction: PASS | FAIL | DEFERRED
  Delight:     PASS | FAIL | DEFERRED
  Verification:PASS | FAIL | DEFERRED

── DESIGN SYSTEM ──────────────────────────────────
Gate 1: Token Completeness
  □ All colors from declared semantic token table?
  □ All spacing from 8px grid tokens?
  □ All font-sizes from modular scale?
  □ No hardcoded hex/px outside token table?
  Score: __ / 10

── VISUAL DESIGN ──────────────────────────────────
Gate 2: Typographic Scale   (1.333 modular, H1/body ≤ 3.5x DESKTOP, ≤ 3.0x MOBILE)
  Common violation: clamp hero to 7rem (112px) with 21px body = 5.3x → FAIL
  Fix: clamp max ≤ 4.5rem for hero, or raise body size proportionally
  Score: __ / 10
Gate 3: Color Semantic      (one token = one role, no collapse)        Score: __ / 10
Gate 4: Figure/Ground       (bg depth: texture/gradient/alt)           Score: __ / 10
Gate V1: Visual Language Definition
  □ Named theme translated into concrete values before styling?
  □ For zen/minimalist: silence, emptiness, restraint, low density, and one focal object are present?
  □ Output is more reduced than the previous iteration, not merely recolored?
  Score: __ / 10
Gate T1: Theme Architecture  (one semantic token table, two primitive maps)
  □ Existing theme provider/infrastructure preserved, not duplicated?
  □ Theme mode support matches spec: light-only | dark-only | dual-theme?
  □ Toggle exists when required and is placed in a predictable global location?
  Score: __ / 10
Gate T2: Theme Toggle A11y + State
  □ Toggle has ≥44×44px target?
  □ aria-label describes the NEXT action, not current state?
  □ Toggle changes class/data-theme and can be reversed light → dark → light?
  Score: __ / 10
Gate T3: Dual-Theme Visual QA
  □ Light mode screenshot/DOM checked?
  □ Dark mode screenshot/DOM checked?
  □ No horizontal overflow or invisible text in either mode?
  □ Borders, cards, badges, inverse sections remain intentional and readable?
  Score: __ / 10
Gate T4: Theme Contrast + Inversion
  □ Primary text ≥ 4.5:1 in each mode?
  □ Secondary text/status badges readable in each mode?
  □ Accent and status colors are not semantically collapsed?
  Score: __ / 10
Gate 5: Whitespace Rhythm   (hero ≠ content ≠ contact padding)        Score: __ / 10

── UX/UI PATTERNS ─────────────────────────────────
Gate 6: Hero Pattern        (correct pattern for page goal, spec met)  Score: __ / 10
Gate 7: Layout Grid         (column count matches content count)       Score: __ / 10
Gate 8: First Impression    (50ms: stance not job description)         Score: __ / 10

── READABILITY ─────────────────────────────────────
Gate 9:  Line Length
  □ Hero stance/bio: max-width 44ch (NOT px — px exceeds 65 CPL at large viewport)
  □ Body prose: max-width 65ch
  Common violation: max-width:553px → 72 CPL at 21px font → FAIL
  Score: __ / 10
Gate 10: Contrast Ratio     (primary ≥ 4.5:1, secondary ≥ 3:1)       Score: __ / 10
Gate 11: Type Size          (body ≥ 16px, smallest ≥ 12px)           Score: __ / 10
Gate 12: Cognitive Ease     (H1 ≤ 8 words, ≤ 4 sentences/para)       Score: __ / 10

── RESPONSIVENESS ──────────────────────────────────
Gate 13: Mobile Layout      (1-col, no overflow)                       Score: __ / 10
Gate 14: Touch Targets      (interactive ≥ 44×44px)                   Score: __ / 10
Gate 15: Type Scaling       (clamp() or mobile cap, ratio ≤ 3.5x)    Score: __ / 10

── ACCESSIBILITY ───────────────────────────────────
Gate 16: Semantic Structure
  □ main, nav[aria-label], footer, sections with aria-labelledby
  □ H1→H2→H3 — no heading level skips
  □ Work/product list: must have H2 even if visually-hidden
  Common violation: work section uses div+div, no H2 → heading outline broken
  Fix: .sr-only { position:absolute;width:1px;height:1px;overflow:hidden;clip:rect(0,0,0,0); }
       Add <h2 class="sr-only">Selected work</h2> inside section
  Score: __ / 10
Gate 17: Interactive A11y   (descriptive links, focus states visible)  Score: __ / 10

── EIGHT UNIVERSAL RULES (from master-design skill) ────────────────
Gate R1: Type          H1 font ≠ body font role (not just weight difference)     Score: __ / 10
Gate R2: Colour        Accent < 5% surface area, max 1 accent hue                Score: __ / 10
Gate R3: Space         All spacing = named token on 4px grid, no raw px          Score: __ / 10
Gate R4: Motion        Every animation has prefers-reduced-motion override        Score: __ / 10
Gate R5: Voice         No buzzwords, distinct register, no neutral middle         Score: __ / 10
Gate R6: Layout        At least one axis intentionally asymmetric, not all-center Score: __ / 10
Gate R7: Hierarchy     H2 ≤ 60% H1, max 3 visual weight levels                  Score: __ / 10
Gate R8: Restraint     Every element has named role, nothing fills space blindly  Score: __ / 10


Gate C1: Focal Point Above-Fold
  □ H1/name visible within first 100vh
  □ Sits at ≤ 50% from top (optical center)
  □ No unframed dead space above focal point
  Common violation: justify-content:flex-end on 100vh → H1 at 80% → void above → FAIL
  Score: __ / 10

Gate C2: Visual Weight Distribution
  □ One heavy (H1), one supporting (H2), one accent (label) — identifiable
  □ No two elements compete for dominance
  Score: __ / 10

Gate C3: Alignment & Anchoring
  □ Every element aligned to grid column, sibling edge, or center axis
  □ No magic-number positioning
  □ Spacing multiples of 8px base unit
  □ No floating/unanchored elements ("ngambang")
  Score: __ / 10

Gate H1: Dominant/Supporting Ratio
  □ Supporting H2 ≤ 60% of H1 size
  □ No H2 larger than H1
  Score: __ / 10

Gate H2: Inter-Section Weight Decay
  □ No section heading carries more visual weight than hero H1
  □ About/manifesto H2 sized as STATEMENT (< H1), not ANCHOR
  Score: __ / 10


Gate 18: Motion Purpose     (every animation = user signal)            Score: __ / 10
Gate 19: Duration + Easing  (hover≤200ms, ease-out enter, ease-in exit) Score: __ / 10
Gate 20: GPU Performance    (transform+opacity only, will-change)      Score: __ / 10
Gate 21: Reduced Motion     (HARD GATE — 0 or 10)                     Score: __ / 10
Gate 22: Cinematic Ratio    (hero=max, contact=min, decreasing)        Score: __ / 10

════════════════════════════════════════════════════
CLUSTER SCORES:
  Design System:    G1         = __ / 10
  Visual Design:    G2–5  avg  = __ / 10
  Theme System:     T1–T4 avg  = __ / 10
  UX/UI Patterns:   G6–8  avg  = __ / 10
  Readability:      G9–12 avg  = __ / 10
  Responsiveness:   G13–15 avg = __ / 10
  Accessibility:    G16–17 avg = __ / 10
  Motion Design:    G18–22 avg = __ / 10  (G21 hard gate)

OVERALL: __ / 10   MINIMUM: 8.0
Gate 21 (Reduced Motion) = non-negotiable: score 0 = automatic full fail
════════════════════════════════════════════════════
Failing gates (< 8):
  Gate __ [name]: score __ — fix: [specific action]
```

Run all gates before any other action:

```
DESIGN REVIEW — Iteration N
────────────────────────────

Gate 1: Typographic Scale
  □ All font sizes from declared scale?
  □ H1/body ratio ≤ 3.5x on mobile?
  Result: PASS | FAIL (reason)

Gate 2: Color Semantic
  □ Each color var has exactly ONE semantic role?
  □ No accent used for multiple meanings?
  Result: PASS | FAIL (reason)

Gate 3: Figure/Ground
  □ Background has depth (texture/gradient/alternating)?
  □ Squint test: foreground separates from background?
  Result: PASS | FAIL (reason)

Gate 4: Theme Verification
  □ Theme support matches spec: light-only | dark-only | dual-theme?
  □ If dual-theme: light screenshot/DOM verified?
  □ If dual-theme: dark screenshot/DOM verified?
  □ Toggle is reversible and aria-label describes next action?
  □ No overflow, invisible text, or unreadable status colors in either mode?
  Result: PASS | FAIL (reason)

Gate 5: Whitespace Rhythm
  □ Section label to first content item: minimum 24px gap (not 0)
  □ Label must have internal padding — never padding:0 when adjacent to cards
  □ No gray void: flex panels use flex:1 on children, not justify-content:center
  □ Split-panel: right panel padding=0, spacing via internal card padding only
  □ Section padding: each section has differentiated top/bottom — no two sections same weight
  □ Hero ≠ content section padding?
  Result: PASS | FAIL (reason)

Gate 5: First Impression (50ms)
  □ H1 communicates ONE memorable idea?
  □ Not a job description or generic tagline?
  Result: PASS | FAIL (reason)

Gate 6: Empty State
  □ Grid layout matches product count?
  □ No 2 items in 4-column grid?
  Result: PASS | FAIL (reason)

Gate 7: Accessibility
  □ Semantic HTML: nav/main/section/footer?
  □ Heading hierarchy correct?
  □ External links have rel="noopener"?
  □ No button-in-anchor?
  Result: PASS | FAIL (reason)

Gate 8: CTA Clarity
  □ If CTA defined: single, prominent, clear action?
  □ If no CTA: no confusing pseudo-CTAs present?
  Result: PASS | FAIL (reason)

──────────────────────────────
TOTAL: N/8 gates passing
STATUS: PASS (deliver) | FAIL (fix → re-review)
```

---

## Phase 6: FIX (Skill-First Mandatory)

When any gate scores < 8.0, run this sequence IN ORDER. Skipping step A is NOT allowed.

```
Step A — Root cause classification (mandatory before any fix):

  For each failing gate, answer:
    1. Which skill encodes the rule for this gate?
    2. Is the rule present in that skill? (yes/no)
    3. If no → the skill is the root cause → patch skill first
    4. If yes → was the rule followed in the output? (yes/no)
    5. If no → the output violated an existing rule → still patch skill
       (add a "common violation" or "pitfall" note to the relevant rule)
    6. Document: SKILL: [name] | RULE: [quoted] | GAP: [what was missing]

Step B — Patch the skill:

  For each root cause identified in Step A:
    - Open the relevant skill file
    - Add/strengthen the missing rule, example, or pitfall
    - Be specific: not "use proper spacing" but "section-label padding must be
      var(--sp-6) var(--sp-6) var(--sp-5) — never 0 when adjacent to cards"
    - Commit the patch to skill before producing new output

Step C — Reproduce from patched skill:

  Re-run Phase 3 (PRODUCE) with the patched skill loaded.
  Do NOT patch the HTML output directly — reproduce from skill.
  This is the only way to verify the skill fix actually works.

Step D — Re-score:

  Re-run Phase 4 (REVIEW) on the new output.
  Compare scores iteration-to-iteration.
  If a gate that previously passed now fails → skill patch introduced regression → fix.
```

## Phase 6: AUTONOMOUS LOOP

Run Phases 3→4→5 autonomously until exit condition.

```
LOOP STATE:
  iteration:     1
  max:           5 (default, configurable)
  active_layer:  [strategy | UI | UX | voice | interaction | delight | verification]
  skill_patches: []   ← log every skill patched this session
  score_history: []   ← [iter1_score, iter2_score, ...]
  layer_history: []   ← [{iter: 1, layer: "UI", verdict: "PASS"}, ...]

LOOP BODY (repeat):
  0. Declare active layer
     → Pick exactly one primary layer for this iteration
     → Name any secondary layers and deferred layers
     → If a lower layer is failing, do not skip ahead to delight/expression

  1. Phase 3: PRODUCE
     → Produce changes for the declared active layer
     → Stamp: macrostructure, genre, iteration N, pre-emit scores

  2. Phase 4: REVIEW
     → Score all applicable gates
     → Score the active layer and any touched secondary layers
     → Compute overall average
     → Log: score_history.append(avg)
     → Log: layer_history.append({iter, layer, verdict})

  3. Check exit:
     IF avg >= 8.0 → EXIT → Phase 7: DELIVER
     IF iteration >= max → EXIT → Phase 7: DELIVER (with gap report)

  4. Phase 5: FIX (skill-first mandatory)
     → Root cause → patch skill → log skill_patches
     → iteration++
     → go to step 1

LOOP REPORT (emit at exit):
  ════════════════════════════════
  Autonomous loop complete: N iterations
  Score progression: [8.0 → 8.4 → 9.1 → 9.6]
  Skills patched this session:
    - macrostructures: Studio split-panel rules
    - redesign-workflow: Gate 5 whitespace proximity
    - master-design: section label padding
  Final score: 9.6 / 10
  Status: ✅ PASS (>= 8.0)

  Residual gaps (if max reached before 8.0):
    Gate N: [description] — [score] — [why not fixed in N iterations]
    Recommendation: extend loop or manual review
  ════════════════════════════════

EXTENSION PROMPT (if max reached, score < 8.0):
  "Loop reached max N iterations. Score: X.X / 10.
   Residual gaps: [list]. Extend loop? (Y = 3 more iterations)"
```

### Why skill-first loop beats output-first loop

```
Output-first loop (wrong):           Skill-first loop (correct):
  Iter 1: produce bad output           Iter 1: produce → review → gap found
  Iter 1: fix HTML directly            Iter 1: patch SKILL → reproduce
  Iter 2: produce from same skill      Iter 2: produce from BETTER skill
  Iter 2: same mistake, fix again      Iter 2: mistake doesn't recur
  Iter 3: same mistake, fix again      Iter 3: new gap → patch skill
  → skill never improves               → skill accumulates knowledge
  → mistakes repeat across sessions    → mistakes do not repeat across sessions
``` (if gates fail)

For each failed gate — apply specific fix, do not rewrite from scratch:

| Gate Failure | Fix |
|---|---|
| Typographic scale | Replace all font-size values with scale vars |
| Color semantic | Rename vars, ensure each has one role |
| Figure/ground | Add dot-grid or gradient to body background |
| Whitespace rhythm | Adjust section padding to vary by weight |
| First impression | Rewrite H1 to stance — test 50ms |
| Empty state | Switch layout to match product count |
| Accessibility | Add missing semantic elements, fix hierarchy |
| CTA clarity | Remove duplicate CTAs, strengthen or remove |

After fix: goto Phase 4 (review). Do NOT skip review after fix.

---

## Phase 7: DELIVER

Only when: all 8 gates PASS (or max_iterations=3 reached).

## PITFALLS

### CSS patch corruption — most common failure
Applying 3+ micro-patches to one CSS block causes rules to nest inside wrong selectors.
Symptom: page goes white, `document.styleSheets.length === 0`.
Rule: after 2 failed patches on same file region → full rewrite with `write_file`. Never a 3rd patch.

### Mandatory CSS/theme verification snippet (run after EVERY CSS or theme change)
```js
const interactive = [...document.querySelectorAll('a,button')];
const ok = {
  themeClass: document.documentElement.className,                  // contains expected light/dark class when themed
  themeLabel: document.querySelector('button[aria-label*="theme"]')
    ?.getAttribute('aria-label'),                                  // next action label
  bg: getComputedStyle(document.body).backgroundColor,              // NOT rgba(0,0,0,0)
  fg: getComputedStyle(document.body).color,                        // readable against bg
  sheets: document.styleSheets.length,                              // > 0
  overflow: document.documentElement.scrollWidth > innerWidth,       // false
  touchFail: interactive.filter(el=>{const b=el.getBoundingClientRect();
    return b.width>0 && b.height>0 && (b.width<44 || b.height<44);}).length,
  h1TopPct: Math.round(document.querySelector('h1')
    .getBoundingClientRect().top/window.innerHeight*100),           // < 50
};
```
All must pass before claiming CSS/theme is working. For dual-theme pages, run once in light mode, toggle, run again in dark mode, then toggle back.



```
Output:
1. Save HTML to output_path
2. MEDIA: output_path → deliver as file to user
3. Gate report summary
4. Key changes from original (table: before → after)
5. If max_iterations reached: honest report of remaining failures
```

Delivery format:
```
REDESIGN COMPLETE — <target>
──────────────────────────────
Gates: 8/8 passing
Iterations: N

Key changes:
  Before: [original issue]   After: [fix applied]
  ...

MEDIA: /tmp/pkahfi-redesign-v3.html
```

---

## Anti-Loop Protection

```
iteration_count = 0
max_iterations  = 3

before each produce/fix:
  iteration_count++
  if iteration_count > max_iterations:
    deliver current best
    report remaining failures
    STOP — do not loop again
```

If same gate fails 2 iterations in a row:
→ Try different approach for that gate specifically
→ Do not keep applying same fix that is not working
