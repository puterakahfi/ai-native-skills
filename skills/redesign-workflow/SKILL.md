---
name: redesign-workflow
description: Contract-driven UI/UX redesign workflow — route → inspect → align → specify → produce → verify → review → classify → fix → deliver. For existing landing pages, dashboards, app screens, portfolios, pricing pages, and other visual surfaces.
license: MIT
metadata:
  ai-native-skills.version: 2.1.0
  ai-native-skills.author: puterakahfi
  ai-native-skills.requires: "design-foundation design-brand design-genre design-depth design-color design-typography design-spacing design-iconography design-visual design-layout design-strategy design-interaction design-system design-audit design-review design-refinement master-design macrostructures ui-components composition visual-hierarchy copywriting ux-psychology accessibility business-value-alignment"
  ai-native-skills.type: workflow
  ai-native-skills.implements: ai-native-core/contracts/skills/quality/redesign-workflow.contract.yaml
  ai-native-skills.contract-version: "^1.1.0"
  ai-native-skills.related_skills: '["design-visual","design-layout","design-interaction","design-strategy","design-system","design-audit","design-review","design-refinement","business-value-alignment"]'
---

# Redesign Workflow

Contract-driven redesign orchestrator for improving an existing visual surface without losing brand, product, content, or implementation constraints.

This workflow owns the redesign lifecycle. Specialized design skills own their respective decisions.

<!-- CRITICAL RULES — read first, applies to every phase -->
```text
HARD RULES (non-negotiable):
  1. Contract-first: follow ai-native-core redesign-workflow contract v1.1.x.
  2. Route before produce: decide redesign vs refinement vs audit-only first.
  3. Preserve locks: brand and DESIGN.md rules override genre preferences.
  4. External before improvise: check trusted interaction patterns before inventing behavior.
  5. Verify before review: never score an artifact that has not been rendered or inspected.
  6. Evidence before score: every scored gate requires concrete evidence.
  7. Classify before fix: identify the defect class before choosing what to patch.
  8. Patch the correct layer: skill-first applies only to reusable skill defects.
  9. Bounded correction: maximum iterations default to 5.
 10. After 2 failed patches in the same file region, follow rewrite safety; never blindly apply a third patch.
 11. Sub-files are on-demand: load references/ only when entering the relevant phase.
 12. Never deliver as passed unless every hard gate and scored-gate rule passes.
```

---

## Core Workflow

```text
Phase 0  → ROUTE
  Decide: redesign | refinement | audit-only
  Load: references/redesign-vs-refinement.md

Phase 1  → INITIALIZE RUN
  Validate input, resolve approval mode, create durable run state

Phase 2  → PRE-FLIGHT
  Inspect existing design, brand, content, theme, framework, and constraints

Phase 3  → DIRECTION
  Select and justify genre, visual language, and macrostructure
  Load port: design-visual
  Load port: design-layout
  Load: references/phase-genre-macro.md

Phase 4  → LAYERED PLAN
  Classify work by foundation, structure, components, expression, interaction, and content
  Load: references/phase-genre-macro.md
  Load: references/user-feedback-parser.md when feedback is qualitative

Phase 5  → VALUE ALIGNMENT
  Connect redesign changes to user value, business value, and measurable outcomes
  Load: business-value-alignment
  Load port: design-strategy

Phase 6  → SPEC CONFIRMATION
  Lock scope, preservation rules, content, audience, CTA, theme, and acceptance criteria

Phase 7  → PRODUCTION
  Produce audit, spec, prototype, or repository patch from delegated capabilities
  Load port: design-visual
  Load port: design-layout
  Load port: design-interaction
  Load port: design-strategy
  Load: references/phase-produce.md
  Load component/hero/image references only when relevant

Phase 8  → VERIFICATION
  Render and inspect the result; check runtime, responsiveness, accessibility, and implementation health
  Load: references/visual-loop-verification.md when fresh visual verification is requested

Phase 9  → REVIEW
  Run hard gates first, then scored gates with evidence
  Load: design-foundation
  Load port: design-system
  Load: references/phase-review-gates.md
  Load: references/iteration-review-mode.md during iterative refinement

Phase 10 → DEFECT CLASSIFICATION
  Classify each failed gate before selecting the correction layer

Phase 11 → FIX
  Patch the skill, reference, workflow, or implementation according to defect class
  Run regression verification
  Load: references/phase-fix-loop.md

Phase 12 → DELIVERY
  Deliver a passing result, or the best bounded attempt with an honest gap report
  Load: references/phase-deliver.md
```

### Canonical loop

```text
route
→ initialize_run
→ preflight
→ direction
→ layered_plan
→ value_alignment
→ spec_confirmation
→ approval gate when required
→ production
→ verification
→ review
   ├─ pass → delivery
   ├─ fail + iterations remain → defect_classification → fix → verification
   └─ max iterations reached → delivery with gap report
```

---

## When to Use

Good fits:

- landing pages, portfolios, personal sites, pricing pages, and docs homepages
- dashboards, admin panels, app screens, onboarding flows, and checkout flows
- copy, hierarchy, CTA, or CRO improvements with explicit user or business value
- an existing design audit followed by a prototype or repository patch

Route elsewhere when:

- use `design-audit` for audit-only work with no redesign requested
- use `design-refinement` when the current design is already sound and only specific gates fail
- use `product-development-workflow` for a net-new product
- use `new-feature-workflow` for non-visual features
- use `bugfix-workflow` for general implementation bugs unrelated to redesign quality

Do not use this workflow for deployment, publishing, destructive repository operations, or production environment changes.

---

## Parameters

| Parameter | Required | Description |
|---|---:|---|
| `target` | YES | URL, screenshot, artifact path, repository path, or named app surface |
| `goal` | NO | Outcome the visual surface should achieve; infer only when evidence is strong |
| `surface_type` | NO | `landing-page`, `dashboard`, `app-screen`, `portfolio`, `pricing-page`, or another declared type |
| `products_in_scope` | NO | Live products or product areas allowed in the redesign |
| `content_inventory` | NO | Existing content to preserve; showcases must use live content only |
| `audience` | NO | Target audience; default is `general` |
| `primary_cta` | NO | Primary CTA; default is `none` |
| `output_mode` | NO | `audit-only`, `spec-only`, `prototype`, or `patch`; default is `prototype` |
| `output_path` | NO | Safe writable output path; default should use a slug and run ID |
| `approval_mode` | NO | `autonomous`, `spec-gated`, `patch-gated`, or `fully-gated`; default is `spec-gated` |
| `max_iterations` | NO | Positive integer; default is `5` |

Compatibility aliases:

```text
target_url_or_artifact → target
cta                    → primary_cta
```

### Input validation

Before pre-flight:

```text
□ target is resolvable
□ output_mode is supported
□ max_iterations is a positive integer
□ patch mode has a repository path or editable artifact
□ output_path is safe and writable when provided
□ high-impact or destructive work has explicit approval
```

On validation failure, stop before production and return the validation errors plus required correction.

---

## Run State

Initialize a durable state object once and update it after every completed phase.

```yaml
run:
  id: redesign-<timestamp-or-run-id>
  state: initialized
  route: redesign
  iteration: 0
  max_iterations: 5
  output_mode: prototype
  approval_mode: spec-gated

input:
  target: <resolved target>
  goal: <goal or unresolved>
  surface_type: <type or unknown>

locks:
  brand_locked: false
  design_system_locked: false
  preserved_elements: []

artifacts:
  route_decision: null
  preflight_report: null
  design_direction: null
  layered_redesign_plan: null
  value_alignment_report: null
  redesign_spec: null
  redesigned_artifact: null
  verification_report: null
  gate_score_report: null
  defect_report: null
  fix_report: null
  delivery_manifest: null

review:
  average_score: null
  minimum_score: null
  hard_gates_passed: false
  unresolved_gaps: []
```

Allowed runtime states:

```text
initialized → routed → preflight_complete → direction_selected → plan_ready
→ spec_ready → awaiting_approval → producing → verifying → reviewing
→ classifying_defect → fixing → approved → delivered
```

Failure states:

```text
validation_failed | production_failed | verification_failed | max_iterations_reached
```

---

## Approval Policy

```text
autonomous
  No routine pause. Still requires approval for destructive or irreversible changes.

spec-gated (default)
  Pause before production only when scope or direction materially changes from the user's request.

patch-gated
  Pause before repository patch or full-file rewrite.

fully-gated
  Pause before production, every repository patch, and full-file rewrite.
```

Always require explicit approval for:

- destructive changes
- irreversible changes
- production environment changes
- deletion of user content

For `audit-only` and `spec-only`, stop after producing the requested report unless the user also requested production.

---

## Phase 2: Pre-flight

Scan the target for existing design signals:

```text
0. design-brand file?
   Found     → BRAND LOCK: genre may adapt only within brand constraints
   Not found → free genre selection within the brief

1. design.md / DESIGN.md at repository root
   Found → locked design system; overrides new visual picks

2. CSS :root variables
   Capture palette, typography, spacing, radius, shadow, and semantic tokens

3. Theme infrastructure
   Detect next-themes, .dark, [data-theme], ThemeProvider, or custom implementation

4. package.json or equivalent
   Detect framework, component system, motion library, fonts, lint, build, and test commands

5. Macrostructure stamp
   Detect comments or metadata declaring an existing macrostructure

6. Target inspection
   Live URL → browser/vision inspection
   Local target → repository and artifact inspection
```

Produce `preflight_report`:

```text
Pre-flight findings
───────────────────
Palette:             [found | not found]
Font stack:          [found | not found]
Theme infrastructure:[none | class | data-theme | next-themes | custom]
Theme default:       [light | dark | system | unknown]
Motion stance:       [motion-on | motion-cut]
Macrostructure:      [name | none]
Design-system lock:  [yes | no]
Brand lock:          [yes | no]

Hallmarks to preserve: [list]
Safe changes:          [list]
Risks or unknowns:     [list]
```

Do not always pause after pre-flight. Apply the selected `approval_mode`.

---

## Phase 3–4: Direction and Layered Plan

Direction must be derived from brief signals and existing locks, not personal taste.

Record:

```yaml
design_direction:
  genre: <selected genre>
  visual_language: <visual rules>
  macrostructure: <selected page shape>
  rationale:
    brief_signals: []
    existing_signals: []
    rejected_options: []
```

Classify proposed work into layers:

```text
foundation  → tokens, accessibility baseline, typography hierarchy
structure   → macrostructure, grid, page rhythm, information architecture
components  → navbar, hero, sections, cards, rows, forms, footer
expression  → imagery, illustration, motion, depth, texture, delight
interaction → states, feedback, keyboard behavior, touch behavior
content     → headline, copy sequence, CTA, proof, labels, microcopy
```

A layer may be marked `preserve`, `refine`, `replace`, or `not_applicable`.

---

## Phase 5: Value Alignment

Run `business-value-alignment` before decorative production.

```text
audit finding
→ user impact
→ business impact
→ measurable signal
→ decision: continue | narrow | experiment | stop
```

Do not proceed with a decorative change when its value is unclear. Preserve the existing design or narrow the change instead.

---

## Phase 6: Spec Confirmation

Produce `redesign_spec`:

```text
SPEC CONFIRMED
──────────────
Surface:             [type]
Goal:                [one sentence]
Audience:            [who]
Content inventory:   [live content to preserve]
Products in scope:   [list]
Primary CTA:         [label | none]
Navigation:          [items]
Theme:               [light-only | dark-only | dual-theme]
Preserved hallmarks: [list]
Allowed changes:     [list]
Out of scope:        [list]
Acceptance criteria: [testable criteria]
Output mode:         [mode]
Approval mode:       [mode]
```

A material change after spec confirmation must be recorded in the run state and handled according to `approval_mode`.

---

## Phase 7: Production

Produce from delegated capabilities; do not improvise outside their contracts.

Load references only when applicable:

- `references/phase-produce.md` for production rules
- `references/component-redesign-pass.md` for page-level components
- `references/hero-patterns.md` for above-fold hero work
- `references/delight-expression-image-assets.md` for imagery, illustration, video, or graphic embellishment

Output behavior by mode:

```text
audit-only → produce audit artifact; redesigned_artifact records not_applicable with reason
spec-only  → produce redesign spec; redesigned_artifact records not_applicable with reason
prototype  → produce a renderable prototype at a safe path
patch      → modify the editable artifact or repository after approval policy passes
```

Preserve the last known good artifact before any risky patch or rewrite.

---

## Phase 8: Verification

Never review from source code alone when the surface can be rendered.

Verify applicable dimensions:

```text
□ artifact renders successfully
□ no blocking runtime error
□ stylesheets or equivalent styling output are present
□ responsive layouts were inspected
□ keyboard navigation works where applicable
□ touch targets and interaction states are valid
□ accessibility baseline passes
□ reduced-motion behavior passes
□ design-system and brand locks remain intact
□ implementation lint/build/test checks pass when available
```

If full lint/build is intentionally deferred, record why and run fresh visual-loop verification. A deferred check is not silently treated as passed.

Produce `verification_report` with commands, inspected surfaces, evidence, failures, and deferred checks.

---

## Phase 9: Evidence-based Review

Run foundation and hard gates first. A failed hard gate blocks passing delivery regardless of average score.

Every gate record must contain:

```yaml
- gate_id: <id>
  score_or_pass_fail: <0-10 or pass/fail>
  status: pass | fail | not_applicable
  evidence:
    - <observable evidence>
  affected_region:
    - <component, selector, file, or viewport>
  recommended_fix_when_failed:
    - <specific correction>
```

Do not assign a score without evidence. An unscored applicable gate without evidence is a failure.

Maintain `score_progression` per completed review iteration.

---

## Phase 10: Defect Classification

Classify every failed gate before fixing it.

| Defect class | Meaning | Correction order |
|---|---|---|
| `reusable_skill_defect` | A reusable rule or capability produced the wrong behavior | patch skill/rule → regenerate or patch artifact → verify regression |
| `reference_knowledge_defect` | Reference material is missing, misleading, or incomplete | patch reference → regenerate or patch artifact → verify regression |
| `workflow_orchestration_defect` | Phase order, routing, state, or delegation is wrong | patch workflow → resume from safe phase → verify regression |
| `local_implementation_defect` | The reusable rules are correct; the local implementation is wrong | patch artifact → verify regression |

`skill-first` is mandatory only for `reusable_skill_defect`. Never pollute a global skill with a one-off local bug.

Produce `defect_report` containing failed gate, evidence, defect class, target layer, and selected correction path.

---

## Phase 11: Fix Loop

Apply only the correction path selected by defect classification.

For each patch, log:

```yaml
- defect_class: <class>
  target_file_or_skill: <target>
  reason: <why this layer owns the defect>
  change_summary: <what changed>
  verification_result: <pass/fail and evidence>
```

Iteration rules:

```text
- Increment iteration after a completed review.
- Default maximum iterations: 5.
- Maximum patches in the same file region: 2.
```

After two failed patches in the same region:

```text
1. Re-read the full file.
2. Identify dependencies and ownership.
3. Mark locked or preserved regions.
4. Create a rewrite plan.
5. Rewrite only when justified and approval policy allows it.
6. Run full verification.
```

Never perform an automatic third patch against the same region.

---

## Delivery Gate

Delivery passes only when all conditions are true:

```text
SCORED GATES
□ average across applicable scored gates >= 8.0
□ no applicable scored gate < 6.0
□ every applicable score includes evidence

HARD GATES
□ foundation gates pass
□ accessibility passes
□ reduced-motion passes
□ touch failures = 0
□ artifact is renderable
□ no blocking runtime error
□ design-system lock is respected when present
□ macrostructure is justified from brief signals
□ pre-emit critique dimensions are all >= 3
```

The average alone never overrides a failed hard gate.

When maximum iterations are reached without passing:

```text
status: max_iterations_reached
action: deliver best attempt with honest gap report
```

A bounded best attempt must never be labeled as fully passed.

---

## Required Output Artifacts

Every run must expose:

```text
redesigned_artifact
  The produced artifact, patch, prototype, or explicit not_applicable descriptor.

gate_score_report
  Gate scores or pass/fail results with evidence and affected regions.

loop_summary
  Final status, iterations used, delivery decision, and unresolved gaps.

delivery_manifest
  Paths, changed files, verification status, score summary, approval history, and rollback information.
```

Produce when applicable:

```text
route_decision
run_state
preflight_report
design_direction
layered_redesign_plan
value_alignment_report
redesign_spec
verification_report
defect_report
fix_report
skill_patch_log
score_progression
gap_report
```

---

## Skill Delegation Rule

```text
DELEGATE TO AN EXTERNAL SKILL when all are true:
  ✓ Stable   — maintained by W3C, major OSS, or established community
  ✓ Trusted  — accessibility, behavior, and edge cases are validated
  ✓ Worth it — expensive to reproduce internally and quick to delegate

BUILD INTERNAL through ui-components when:
  ✓ Brand or product-specific — tokens, visual templates, and copy tone
  ✓ Not covered externally — catalog checked first
  ✓ An opinionated product version is required

PREFERRED COMBINATION:
  external → behavior, accessibility, interaction, edge cases (how it works)
  internal → CSS, tokens, visual language, brand expression (how it looks)
```

Trusted external source for component behavior:

```text
ux-patterns-for-developers
npx skills add https://github.com/thedaviddias/ux-patterns-for-developers --skill <name> --yes --global
```

---

## Failure Handling

```text
validation_failed
  Stop before production. Return validation errors and required correction.

production_failed
  Preserve the last known good artifact and report the failure.

verification_failed
  Classify the defect before attempting a fix.

missing_dependency
  Stop the affected phase and report the missing dependency.

approval_denied
  Preserve artifacts and end without applying the blocked patch.
```

Never hide a failed command, missing dependency, deferred verification, or unresolved gap.

---

<!-- CRITICAL RULES repeated at bottom — Lost in Middle fix -->
```text
REMINDER — DELIVER AS PASSED ONLY WHEN:
  □ contract version ^1.1.0 is followed
  □ every hard gate passes
  □ applicable scored-gate average >= 8.0
  □ no applicable scored gate < 6.0
  □ every score has evidence
  □ verification inspected the rendered result
  □ defect classification preceded every fix
  □ unresolved gaps are empty

ON MAX ITERATIONS:
  Deliver the best preserved attempt + explicit gap report.
  Never claim full pass.
```
