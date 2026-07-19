---
name: design-review
description: Facade skill for evidence-backed review of digital interfaces and visual communication artifacts — classify the target, select applicable domain reviewers and canonical gates, normalize evidence, then score and report with explicit coverage.
license: MIT
metadata:
  ai-native-skills.version: 3.3.0
  ai-native-skills.author: puterakahfi
  ai-native-skills.type: skill
  ai-native-skills.pattern: facade
  ai-native-skills.implements: ai-native-core/contracts/skills/quality/design-review.contract.yaml
  ai-native-skills.contract-version: "~0.2"
  ai-native-skills.related_skills: '["brand-identity-review","design-audit","design-refinement","redesign-workflow","master-design","design-foundation","design-system","adaptive-component-design","accessibility","readability","responsiveness","motion-design","composition","visual-hierarchy","copywriting","cro"]'
---

# Design Review

Unified review entry point for built-in and adapter-covered design domains.

The facade owns classification, reviewer routing, canonical gate resolution, applicability, evidence normalization, scoring, coverage, verdict, and reporting. Specialist reviewers own domain knowledge, full gate definitions, evidence interpretation, and domain hard gates.

## Hard Rules

```text
1. Classify design domain and surface before selecting gates.
2. Separate universal principles from domain and surface thresholds.
3. Never apply interactive gates to static artifacts.
4. Every selected or reported design gate ID must be canonical and registered.
5. Never redefine a gate in a caller, workflow, report, or eval.
6. Never claim a gate passed without suitable evidence.
7. NOT_APPLICABLE and NOT_VERIFIED are different; neither is zero.
8. Score only verified applicable gates.
9. Load only references and reviewers required by the active phase.
10. Every failure needs observation, evidence, impact, and correction direction.
11. Do not turn taste or one style into a universal gate.
12. High score + low coverage is not release approval.
13. Hard gates are contextual and reviewer-owned.
14. Unsupported domains require an adapter or an explicitly limited review.
15. Unknown gate IDs are rejected, never guessed.
16. Review does not silently become redesign or implementation.
```

## Inputs

```text
target            required — URL, app, screenshot, image, PDF page, slide, repo path
design_domain     digital-interface | visual-communication | presentation |
                   brand-identity | other
surface_profile   web-marketing | web-application | mobile-application |
                   desktop-application | static-marketing | presentation |
                   brand-identity | other
artifact_state    rendered-interactive | rendered-static | source-only | mixed
review_depth      quick | focused | full | release
focus             lenses, components, regions, or canonical previous gate IDs
viewing_context   viewports, dimensions, channel, distance, theme, orientation, inputs
required_assets   logos, products, people, copy, price, contact, claims, legal content
goal               user, communication, business, or delivery outcome
domain_reviewers  optional specialist reviewers required by the domain
```

Infer missing values only when evidence is strong and record the assumption.

## Core Workflow

```text
Phase 0 — CLASSIFY
  Resolve domain, profile, artifact state, context, depth, and coverage mode.
  Load review-routing.md.
  Load facade-boundary.md only when scope or extension behavior matters.

Phase 1 — ROUTE
  Select reviewers, lenses, canonical gates, components, and evidence.
  Resolve incoming IDs through gate-registry.yaml.
  Use gate-migrations.yaml only for a real alias or deprecated ID.
  Load review-profiles.md only for a built-in profile.

Phase 2 — INSPECT
  Inspect the complete available artifact before scoring.
  Capture realistic content, states, sizes, themes, assets, and constraints.

Phase 3 — UNIVERSAL REVIEW
  Load universal-gates.md when cross-domain principles are applicable.

Phase 4 — DOMAIN / SURFACE REVIEW
  Interactive → interactive-surface-gates.md
  Static/slide → static-visual-gates.md
  Brand identity → brand-identity-review
  Other specialized domain → declared reviewer or limited scope

Phase 5 — COMPONENT REVIEW
  Load component-review.md only for present or required interactive components.

Phase 6 — EVIDENCE + SCORE
  Normalize findings, validate gate IDs, assign statuses, scores, weights,
  hard-gate results, evidence coverage, and primary-domain coverage.
  Load evidence-and-scoring.md.

Phase 7 — REPORT
  Report canonical IDs, governing reviewers, findings, limitations, and handoff.
  Load review-report.md.
```

```text
classify → route → resolve canonical gates → inspect → universal
→ domain/surface → components → normalize evidence → hard gates
→ score + coverage → report
```

Do not score until route, domain coverage, selected canonical IDs, and evidence are explicit.

## Phase-Specific Loading

```text
CLASSIFY / ROUTE
  review-routing.md
  facade-boundary.md only for scope/extension decisions
  gate-registry.yaml only for selected, previous, or external gate IDs
  gate-migrations.yaml only for alias/deprecated IDs
  gate-registry.md only when authoring or extending registry behavior
  review-profiles.md only for a built-in profile

UNIVERSAL REVIEW
  universal-gates.md when applicable

DOMAIN / SURFACE REVIEW
  interactive-surface-gates.md OR
  static-visual-gates.md OR
  brand-identity-review OR
  another declared domain reviewer

COMPONENT REVIEW
  component-review.md only for selected interactive components

EVIDENCE + SCORE
  evidence-and-scoring.md

REPORT
  review-report.md
```

Never load every reference defensively. A completed phase output is the handoff context for the next phase.

## Gate Identity Contract

```text
gate-registry.yaml   canonical machine-readable identity and ownership
gate-migrations.yaml aliases, deprecations, and retained legacy IDs
gate-registry.md     authoring and extension rules
owner reference      full review question, evidence rules, and correction knowledge
```

```text
active ID      → use directly
alias          → normalize through migration map
deprecated ID  → report active replacement and migration provenance
unknown ID     → reject
new meaning    → register a new ID and owner
```

External domain reviewers register a unique namespace and may own definitions through a repo-relative skill reference. They must not copy their domain knowledge into the facade.

## Coverage

Built-in:

```text
digital-interface    web, mobile, desktop, and responsive product UI
visual-communication poster, flyer, banner, social, ad, and thumbnail
presentation         slides and decks
```

Available external adapter:

```text
brand-identity       brand-identity-review · namespace BI · ADAPTER_COVERED
```

Packaging, motion/video, industrial, spatial, fashion, and service-design disciplines still require their own domain reviewer. Universal gates alone produce `LIMITED REVIEW`.

## Review Depth

```text
quick
  Critical universal gates + applicable domain hard gates + declared issue.
  No release claim.

focused
  Selected canonical gates/components + adjacent regression checks.

full
  All applicable gates from every loaded reviewer + major present components.
  Full only with built-in or adapter primary-domain coverage.

release
  Full review + contextual hard gates + required states, sizes, themes,
  inputs, runtime/export/domain evidence, and sufficient primary coverage.
```

## Applicability and Evidence

Every selected gate receives exactly one status:

```text
PASS | FAIL | PARTIAL | NOT_VERIFIED | NOT_APPLICABLE
```

```text
poster + reduced motion                    → NOT_APPLICABLE
dashboard screenshot + keyboard operation → NOT_VERIFIED
running app + unhandled route error        → FAIL RI1
commercial visual + wrong supplied price  → FAIL SV11
logo concept + brand-identity-review       → evaluate BI gates
logo concept without identity reviewer     → LIMITED REVIEW
```

Contextual hard gates are declared by the governing reviewer:

```text
interactive release
  RI1 runtime integrity
  G21 reduced motion when applicable
  accessibility/task-completion blockers

static commercial delivery
  SV8–SV11 required asset/content fidelity
  SV5–SV6 mandatory text legibility
  SV12–SV13 crop/safe-area integrity
  SV17 delivery resolution

brand identity
  contextual BI hard gates from brand-identity-review

other specialized domain
  registered hard gates from its loaded reviewer
```

A build is not visual verification. A screenshot is not interaction or runtime verification. Universal evidence is not specialist-domain proof.

## Score and Verdict

```text
Pass threshold: 8.0 / 10
Critical: verified score below 5
Overall: weighted average of verified applicable gates only
Evidence coverage: verified applicable weight / all applicable selected weight
Primary-domain coverage: BUILT_IN | ADAPTER_COVERED | LIMITED | ROUTE_ELSEWHERE
```

```text
PASS             score >= 8, hard gates pass, sufficient coverage
CONDITIONAL PASS score >= 8, no verified hard-gate failure, accepted gaps remain
NEEDS WORK       score < 8 or important gates fail
CRITICAL         hard gate fails or material critical gate exists
LIMITED REVIEW   primary-domain reviewer was unavailable
ROUTE ELSEWHERE  requested claim cannot be reviewed by available reviewers
```

## Output and Handoff

Output:

```text
review context and route
design domain and loaded reviewers
canonical gate IDs and governing owners
score, evidence coverage, and primary-domain coverage
hard-gate status and prioritized findings
NOT_APPLICABLE / NOT_VERIFIED gates
scope limitations and recommended handoff
```

Handoff:

```text
design-audit       full capture, gap analysis, prioritization
design-refinement  targeted fixes, preservation, focused re-score
redesign-workflow  redesign, verification, defect classification, fix loop
domain specialist  unsupported domain knowledge and gates
legal specialist   trademark/legal questions outside design review
```

## Final Guard

```text
□ Domain, profile, artifact state, and context are explicit.
□ Built-in or adapter coverage is explicit.
□ Only phase-relevant references were loaded.
□ Every selected/reported gate ID is active and canonical.
□ Aliases/deprecations were normalized through the migration map.
□ Surface/component/domain gates match the target.
□ Hard gates are contextual and reviewer-owned.
□ Every score has suitable evidence.
□ NOT_VERIFIED and NOT_APPLICABLE remain separate.
□ Evidence and primary-domain coverage are both shown.
□ Unsupported domains are limited, not fully passed.
□ Findings are specific, prioritized, and style-neutral.
```