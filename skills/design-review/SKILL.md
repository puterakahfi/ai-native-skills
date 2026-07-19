---
name: design-review
description: Facade skill for evidence-backed review of digital interfaces and visual communication artifacts — evaluate universal design-foundation gates first, then select applicable genre, domain, surface, and component reviewers with explicit evidence coverage.
license: MIT
metadata:
  ai-native-skills.version: 3.2.0
  ai-native-skills.author: puterakahfi
  ai-native-skills.type: skill
  ai-native-skills.pattern: facade
  ai-native-skills.related_skills: '["design-audit","design-refinement","redesign-workflow","master-design","design-foundation","design-system","adaptive-component-design","accessibility","readability","responsiveness","motion-design","composition","visual-hierarchy","copywriting","cro"]'
---

# Design Review

Unified review entry point for digital interfaces and visual communication artifacts.

This facade owns classification, applicability, evidence normalization, scoring, coverage, verdict, and reporting. `design-foundation` owns universal composition knowledge. Specialist reviewers own genre, domain, surface, component, and contextual hard gates. Load `references/facade-boundary.md` when scope or extension behavior matters.

## Hard Rules

```text
1. Classify the design domain and surface before selecting contextual gates.
2. Load design-foundation for every design review.
3. Evaluate universal foundation relationships before genre/domain approval.
4. Separate universal principles from domain and surface thresholds.
5. Never apply interactive gates to static artifacts.
6. Never claim a gate passed without suitable evidence.
7. NOT_APPLICABLE and NOT_VERIFIED are different; neither is zero.
8. Score only verified applicable gates.
9. Load only references and reviewers required by the active phase.
10. Every failure needs observation, evidence, impact, and correction direction.
11. Do not turn taste or one style into a universal gate.
12. High score + low coverage is not release approval.
13. Hard gates are contextual, except verified foundation/accessibility blockers.
14. Review does not silently become redesign or implementation.
15. Unsupported domains require an adapter or an explicitly limited review.
16. The facade normalizes domain output; it does not copy specialist knowledge.
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
domain_reviewers  optional specialist reviewers required by the domain
```

Infer missing values only when evidence is strong and record the assumption.

## Core Workflow

```text
Phase 0 → CLASSIFY
  Resolve domain, profile, artifact state, context, depth, and coverage mode.
  Load: references/review-routing.md
  Load: references/facade-boundary.md when domain scope is unclear or extended.

Phase 1 → ROUTE
  Select domain reviewers, lenses, surface gates, components, and evidence.
  Load: references/review-profiles.md only for a built-in profile.

Phase 2 → INSPECT
  Inspect the complete available artifact before scoring.
  Capture realistic content, states, sizes, themes, assets, and constraints.

Phase 3 → FOUNDATION / UNIVERSAL REVIEW
  Hierarchy, grouping, alignment, spacing rhythm, balance, flow,
  legibility, consistency, accessibility, responsive continuity,
  color, content integrity, and restraint.
  Load: design-foundation/SKILL.md
  Load: design-foundation/references/gates.md
  Load: references/universal-gates.md

Phase 4 → GENRE / DOMAIN / SURFACE REVIEW
  Genre → selected design-genre reference when applicable
  Interactive → references/interactive-surface-gates.md
  Static/slide → references/static-visual-gates.md
  Specialized domain → declared domain reviewer or limited scope.

Phase 5 → COMPONENT REVIEW
  Review only present or required components.
  Load: references/component-review.md when relevant.

Phase 6 → EVIDENCE + SCORE
  Normalize findings; assign status, score, weight, hard-gate result, coverage.
  Load: references/evidence-and-scoring.md

Phase 7 → REPORT
  Prioritize findings, limitations, foundation status, domain coverage, and handoff.
  Load: references/review-report.md
```

```text
classify → route → inspect → foundation/universal → genre/domain/surface
→ components → normalize evidence → hard gates → score + coverage → report
```

Do not score until route, foundation coverage, domain coverage, and evidence are explicit.

## Phase-Specific Loading

Start with `SKILL.md` only.

```text
CLASSIFY / ROUTE
  review-routing.md
  facade-boundary.md only for scope/extension decisions
  review-profiles.md only for a built-in profile

FOUNDATION / UNIVERSAL REVIEW
  design-foundation/SKILL.md
  design-foundation/references/gates.md
  universal-gates.md

GENRE / DOMAIN / SURFACE REVIEW
  selected design-genre reference when applicable
  interactive-surface-gates.md OR
  static-visual-gates.md OR
  declared domain reviewer

COMPONENT REVIEW
  component-review.md only for selected components

EVIDENCE + SCORE
  evidence-and-scoring.md

REPORT
  review-report.md
```

Never load every reference defensively. A completed phase output is the handoff context for the next phase.

## Built-In Coverage

```text
digital-interface    web, mobile, desktop, and responsive product UI
visual-communication poster, flyer, banner, social, ad, and thumbnail
presentation         slides and decks
```

Identity systems, packaging, motion/video, industrial, spatial, fashion, and service-design disciplines require a domain reviewer for a complete verdict. Foundation and universal gates alone produce `LIMITED REVIEW` for unsupported specialist domains.

## Review Depth

```text
quick
  Critical foundation/universal gates + applicable hard gates + declared issue.
  No release claim.

focused
  Selected foundation axes/lenses/components + adjacent regression checks.
  Default during active refinement.

full
  All applicable gates from every loaded reviewer + major present components.
  Full only for domains covered by built-in or adapter reviewers.

release
  Full review + foundation gates + contextual hard gates + required states,
  sizes, themes, inputs, runtime/export evidence, and sufficient domain coverage.
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
commercial visual + wrong supplied price  → FAIL fidelity/content hard gate
logo concept without identity reviewer     → LIMITED REVIEW
```

Foundation applicability:

```text
hierarchy, grouping, alignment, spacing, balance, flow, legibility
  → applicable to every visual artifact with suitable rendered evidence

system consistency
  → applicable when repeated roles or source/system evidence exists

accessibility / responsive continuity
  → applicable according to medium, interaction, and viewing context
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

Use evidence appropriate to the gate: rendered visual, interaction, runtime, accessibility tree, source, asset comparison, measurements, or user/task evidence.

A build is not visual verification. A screenshot is not interaction or runtime verification. Universal visual evidence is not specialist-domain proof.

## Foundation Verdict Rule

```text
verified foundation FAIL
  → blocks release PASS even when weighted score is high

foundation NOT_VERIFIED
  → report evidence gap; never convert to PASS

foundation PASS
  → continue to genre, domain, surface, and component verdicts
```

Do not average away hierarchy, grouping, alignment, balance, flow, legibility, or accessibility failures.

## Score and Verdict

```text
Pass threshold: 8.0 / 10
Critical: verified score below 5
Overall: weighted average of verified applicable gates only
Coverage: verified applicable weight / all applicable selected weight
```

```text
PASS             score >= 8, foundation + contextual hard gates pass,
                 sufficient domain/evidence coverage
CONDITIONAL PASS score >= 8, no verified foundation/hard-gate failure, gaps remain
NEEDS WORK       score < 8 or important gates fail
CRITICAL         foundation/hard gate fails or material critical gate exists
LIMITED REVIEW   primary-domain reviewer was not available
```

## Output

```text
review context and route
design domain and loaded reviewers
foundation gate status F1–F10
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
design-foundation  owns reusable universal relationship defects
design-genre       owns reusable style/containment/density defects
domain specialist  owns unsupported domain knowledge and gates
```

`design-review` reports findings. It changes artifacts only when the calling workflow explicitly owns production.

## Final Guard

```text
□ Domain, profile, artifact state, and viewing context are explicit.
□ Built-in or adapter coverage is explicit.
□ Only phase-relevant references were loaded.
□ Design-foundation was loaded.
□ Foundation gates F1–F10 were reviewed with applicable evidence.
□ Universal adapter gates were reviewed.
□ Genre/surface/component/domain gates match the target.
□ Hard gates were contextual and foundation blockers were not averaged away.
□ Every score has suitable evidence.
□ NOT_VERIFIED and NOT_APPLICABLE remain separate.
□ Score uses verified applicable gates only.
□ Coverage is shown beside score.
□ Unsupported domains are limited, not fully passed.
□ Findings are specific, prioritized, and style-neutral.
```