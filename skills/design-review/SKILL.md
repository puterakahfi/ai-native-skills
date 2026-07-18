---
name: design-review
description: Facade skill for evidence-backed review of digital interfaces and visual communication artifacts — classify the target, select applicable domain reviewers and gates, normalize evidence, then score and report with explicit coverage. Use standalone or from design-audit, design-refinement, and redesign-workflow.
license: MIT
metadata:
  ai-native-skills.version: 3.1.0
  ai-native-skills.author: puterakahfi
  ai-native-skills.type: skill
  ai-native-skills.pattern: facade
  ai-native-skills.related_skills: '["design-audit","design-refinement","redesign-workflow","master-design","design-foundation","design-system","adaptive-component-design","accessibility","readability","responsiveness","motion-design","composition","visual-hierarchy","copywriting","cro"]'
---

# Design Review

Unified review entry point for digital interfaces and visual communication artifacts.

`design-review` is a **facade skill**: callers use one review interface while the facade classifies the target, selects applicable review strategies, normalizes evidence, and produces a consistent score and verdict. It does not own every design discipline's knowledge.

## Facade Ownership Boundary

The facade owns:

```text
surface and domain classification
review profile and strategy selection
applicability status
common evidence model
score, coverage, and verdict policy
finding and report contract
handoff to audit, refinement, redesign, or a specialist
```

Specialist or domain-review skills own:

```text
domain principles and thresholds
component and platform behavior
specialized hard gates
production methods
correction techniques
```

The facade must not copy specialist knowledge into `SKILL.md` merely to avoid loading the governing skill.

## Supported Core Scope

Covered by the built-in review strategies:

```text
digital product interfaces
responsive web experiences
mobile and desktop applications
static marketing and social visuals
advertising creatives and thumbnails
presentation slides and decks
```

Not covered as a complete discipline without an additional domain reviewer:

```text
logo and brand-identity system design
packaging and specialist print production
motion graphics, film, and video editing
industrial or physical product design
architecture, interior, and spatial design
fashion design
service-design research and organizational-service systems
```

Universal visual gates may still provide a limited review for an unsupported discipline, but the report must state the limitation and must not claim full domain coverage.

## Hard Rules

```text
1. Classify the surface and design domain before selecting gates.
2. Separate universal principles from domain and surface thresholds.
3. Never apply interactive gates to static artifacts.
4. Never claim a gate passed without suitable evidence.
5. NOT_APPLICABLE and NOT_VERIFIED are different; neither is zero.
6. Score only verified applicable gates.
7. Load only references and domain reviewers required by the active phase.
8. Every failure needs observation, evidence, impact, and correction direction.
9. Do not turn taste or one style into a universal gate.
10. High score + low coverage is not release approval.
11. Hard gates are contextual, not global.
12. Review does not silently become redesign or implementation.
13. Unsupported domains require a declared adapter or an explicitly limited review.
14. The facade normalizes domain output; it does not rewrite domain knowledge.
```

## Inputs

```text
target            required — URL, app, screenshot, image, PDF page, slide, repo path
design_domain     digital-interface | visual-communication | presentation | other
surface_profile   web-marketing | web-application | mobile-application |
                   desktop-application | static-marketing | presentation | other
artifact_state    rendered-interactive | rendered-static | source-only | mixed
review_depth      quick | focused | full | release
focus             lenses, components, regions, or previous gate IDs
viewing_context   viewports, dimensions, channel, distance, theme, orientation, inputs
required_assets   logos, products, people, copy, price, contact, claims, legal content
goal               user, communication, business, or delivery outcome
domain_reviewers  optional specialist reviewers or adapters required by the domain
```

Infer missing values only when evidence is strong and record the assumption.

## Core Workflow

```text
Phase 0 → CLASSIFY
  Resolve design domain, profile, artifact state, context, and depth.
  Load: references/review-routing.md

Phase 1 → ROUTE
  Select applicable domain reviewers, lenses, surface gates, components, and evidence.
  Load: references/review-profiles.md only when a built-in profile applies.

Phase 2 → INSPECT
  Inspect the complete available artifact before scoring.
  Capture realistic content, states, sizes, themes, assets, and constraints.

Phase 3 → UNIVERSAL REVIEW
  Typography, hierarchy, spacing, composition, balance, alignment,
  color, readability, content, brand consistency, restraint.
  Load: references/universal-gates.md

Phase 4 → DOMAIN AND SURFACE REVIEW
  Interactive → references/interactive-surface-gates.md
  Static/slide → references/static-visual-gates.md
  Unsupported specialized domain → load declared domain reviewer or limit scope.

Phase 5 → COMPONENT REVIEW
  Review only present or required components.
  Load: references/component-review.md when relevant.

Phase 6 → EVIDENCE + SCORE
  Normalize domain findings; assign status, score, weight, hard-gate result, and coverage.
  Load: references/evidence-and-scoring.md

Phase 7 → REPORT
  Prioritize findings, limitations, adapter coverage, and handoff.
  Load: references/review-report.md
```

```text
classify → route → inspect → universal → domain/surface → components
→ normalize evidence → hard gates → score + coverage → report
```

Do not score until route, domain coverage, and evidence are explicit.

## Phase-Specific Loading Policy

Start with `SKILL.md` only. Load references when entering the phase that owns them:

```text
CLASSIFY / ROUTE
  references/review-routing.md
  references/review-profiles.md only for a built-in profile

UNIVERSAL REVIEW
  references/universal-gates.md

DOMAIN / SURFACE REVIEW
  references/interactive-surface-gates.md OR
  references/static-visual-gates.md OR
  declared external domain reviewer

COMPONENT REVIEW
  references/component-review.md only for selected components

EVIDENCE + SCORE
  references/evidence-and-scoring.md

REPORT
  references/review-report.md
```

Never load every reference defensively. A completed phase output is the handoff context for the next phase.

## Review Depth

```text
quick
  Critical universal gates + applicable hard gates + declared issue.
  No release claim.

focused
  Selected lenses/components + adjacent regression checks.
  Default during active refinement.

full
  All applicable universal, domain, and profile gates + major present components.
  Full means full only for domains covered by loaded reviewers.

release
  Full review + contextual hard gates + required states, sizes, themes,
  input methods, runtime/export evidence, and sufficient domain coverage.
```

## Applicability and Evidence

Every selected gate receives exactly one status:

```text
PASS | FAIL | PARTIAL | NOT_VERIFIED | NOT_APPLICABLE
```

Examples:

```text
poster + reduced motion                    → NOT_APPLICABLE
dashboard screenshot + keyboard operation → NOT_VERIFIED
running app + unhandled route error        → FAIL RI1
commercial visual + wrong supplied price  → FAIL fidelity/content hard gate
logo concept without identity reviewer     → limited universal review; no full-domain verdict
```

Contextual hard gates:

```text
interactive release
  RI1 runtime integrity
  G21 reduced motion when applicable
  verified accessibility or task-completion blocker

static commercial delivery
  required logo/product/person/content fidelity
  mandatory text legibility
  crop/safe-area integrity
  delivery resolution

specialized domain
  hard gates declared by the loaded domain reviewer
```

Use rendered visuals, interaction observation, runtime capture, accessibility tree, source inspection, asset comparison, measurements, or user/task evidence as appropriate.

A build is not visual verification. A screenshot is not interaction or runtime verification. Universal visual evidence is not proof of specialist-domain quality.

## Domain Reviewer Contract

A domain reviewer integrated through this facade must declare:

```yaml
domain_reviewer:
  domain: <stable domain id>
  applies_when: []
  required_context: []
  required_evidence: []
  gates: []
  hard_gate_triggers: []
  unsupported_claims: []
  finding_contract: design-review/finding
```

It must:

```text
return PASS/FAIL/PARTIAL/NOT_VERIFIED/NOT_APPLICABLE per selected gate
provide evidence and impact for every failed or partial gate
identify domain-specific hard-gate triggers
map findings into the facade finding contract
preserve the common score and coverage semantics
state what remains outside its own scope
```

It must not:

```text
silently redefine universal gate meanings
count missing evidence as zero
claim coverage outside its declared domain
perform redesign or production unless the caller owns that lifecycle
```

## Score and Verdict

```text
Pass threshold: 8.0 / 10
Critical: verified score below 5
Overall: weighted average of verified applicable gates only
Coverage: verified applicable weight / all applicable selected weight
```

```text
PASS             score >= 8, hard gates pass, sufficient domain/evidence coverage
CONDITIONAL PASS score >= 8, no verified hard-gate failure, gaps remain
NEEDS WORK       score < 8 or important gates fail
CRITICAL         hard gate fails or material critical gate exists
LIMITED REVIEW   specialist domain coverage was not available
```

## Output

Report:

```text
review context and route
design domain and loaded reviewers
score + verified coverage
contextual hard-gate status
executive findings
cluster/component/domain summary
critical / important / polish priority
NOT_APPLICABLE and NOT_VERIFIED gates
scope limitations
recommended handoff
```

Each failed or partial finding includes gate, region, observation, evidence, impact, correction direction, confidence, and governing reviewer.

## Handoff

```text
design-audit       owns full capture, gap analysis, and prioritization
design-refinement  owns targeted fixes, preservation, and focused re-score
redesign-workflow  owns redesign, verification, defect classification, and fix loop
domain specialist  owns unsupported design-domain knowledge and gates
```

`design-review` reports findings. It changes artifacts only when the calling workflow explicitly owns production.

## Final Guard

```text
□ Design domain, profile, artifact state, and viewing context are explicit.
□ Built-in coverage or domain-review adapter coverage is explicit.
□ Only phase-relevant references were loaded.
□ Universal gates were reviewed.
□ Surface/component/domain gates match the target.
□ Hard gates were contextual.
□ Every score has suitable evidence.
□ NOT_VERIFIED and NOT_APPLICABLE remain separate.
□ Score uses verified applicable gates only.
□ Coverage is shown beside score.
□ Unsupported domains are reported as limited, not fully passed.
□ Findings are specific, prioritized, and style-neutral.
```