---
name: design-review
description: Facade skill for evidence-backed review of digital interfaces and visual communication artifacts — classify the target, select applicable domain reviewers and canonical gates, normalize evidence, then score and report with explicit coverage.
license: MIT
metadata:
  ai-native-skills.version: 3.2.0
  ai-native-skills.author: puterakahfi
  ai-native-skills.type: skill
  ai-native-skills.pattern: facade
  ai-native-skills.implements: ai-native-core/contracts/skills/quality/design-review.contract.yaml
  ai-native-skills.contract-version: "~0.2"
  ai-native-skills.related_skills: '["design-audit","design-refinement","redesign-workflow","master-design","design-foundation","design-system","adaptive-component-design","accessibility","readability","responsiveness","motion-design","composition","visual-hierarchy","copywriting","cro"]'
---

# Design Review

Unified review entry point for digital interfaces and visual communication artifacts.

This facade owns classification, reviewer routing, canonical gate resolution, applicability, evidence normalization, score, coverage, verdict, and reporting. Specialist reviewers own domain knowledge, full gate definitions, evidence interpretation, and domain hard gates.

Load `references/facade-boundary.md` when scope or extension behavior matters. Load `references/gate-registry.md` when authoring, migrating, or extending gate identity.

## Hard Rules

```text
1. Classify the design domain and surface before selecting gates.
2. Separate universal principles from domain and surface thresholds.
3. Never apply interactive gates to static artifacts.
4. Every selected or reported design gate ID must resolve through the canonical registry.
5. Never redefine a gate in a caller, workflow, report, or eval.
6. Never claim a gate passed without suitable evidence.
7. NOT_APPLICABLE and NOT_VERIFIED are different; neither is zero.
8. Score only verified applicable gates.
9. Load only references and reviewers required by the active phase.
10. Every failure needs observation, evidence, impact, and correction direction.
11. Do not turn taste or one style into a universal gate.
12. High score + low coverage is not release approval.
13. Hard gates are contextual and owned by the governing reviewer.
14. Review does not silently become redesign or implementation.
15. Unsupported domains require an adapter or an explicitly limited review.
16. The facade normalizes specialist output; it does not copy specialist knowledge.
17. Unknown gate IDs are rejected, never guessed from similar wording.
```

## Inputs

```text
target            required — URL, app, screenshot, image, PDF page, slide, repo path
design_domain     digital-interface | visual-communication | presentation | other
surface_profile   web-marketing | web-application | mobile-application |
                   desktop-application | static-marketing | presentation | other
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
Phase 0 → CLASSIFY
  Resolve domain, profile, artifact state, context, depth, and coverage mode.
  Load: references/review-routing.md
  Load: references/facade-boundary.md when domain scope is unclear or extended.

Phase 1 → ROUTE
  Select domain reviewers, lenses, canonical gates, components, and evidence.
  Resolve incoming gate IDs through references/gate-registry.yaml.
  Apply references/gate-migrations.yaml only for a real alias or deprecated ID.
  Load: references/review-profiles.md only for a built-in profile.

Phase 2 → INSPECT
  Inspect the complete available artifact before scoring.
  Capture realistic content, states, sizes, themes, assets, and constraints.

Phase 3 → UNIVERSAL REVIEW
  Typography, hierarchy, spacing, composition, balance, alignment,
  color, readability, content, brand consistency, restraint.
  Load: references/universal-gates.md

Phase 4 → DOMAIN / SURFACE REVIEW
  Interactive → references/interactive-surface-gates.md
  Static/slide → references/static-visual-gates.md
  Specialized domain → declared domain reviewer or limited scope.

Phase 5 → COMPONENT REVIEW
  Review only present or required components.
  Load: references/component-review.md when relevant.

Phase 6 → EVIDENCE + SCORE
  Normalize findings; verify every gate ID against the registry; assign status,
  score, weight, hard-gate result, evidence coverage, and domain coverage.
  Load: references/evidence-and-scoring.md

Phase 7 → REPORT
  Prioritize findings, limitations, domain coverage, and handoff.
  Report canonical IDs and governing reviewers.
  Load: references/review-report.md
```

```text
classify → route → resolve canonical gates → inspect → universal
→ domain/surface → components → normalize evidence → hard gates
→ score + coverage → report
```

Do not score until route, domain coverage, selected canonical IDs, and evidence are explicit.

## Phase-Specific Loading

Start with `SKILL.md` only.

```text
CLASSIFY / ROUTE
  review-routing.md
  facade-boundary.md only for scope/extension decisions
  gate-registry.yaml only when resolving selected, previous, or external gate IDs
  gate-migrations.yaml only when an alias/deprecated ID is encountered
  gate-registry.md only when authoring or extending registry behavior
  review-profiles.md only for a built-in profile

UNIVERSAL REVIEW
  universal-gates.md

DOMAIN / SURFACE REVIEW
  interactive-surface-gates.md OR
  static-visual-gates.md OR
  declared domain reviewer

COMPONENT REVIEW
  component-review.md only for selected components

EVIDENCE + SCORE
  evidence-and-scoring.md
  canonical gate lookup for every normalized finding

REPORT
  review-report.md
```

Never load every reference defensively. A completed phase output is the handoff context for the next phase.

## Canonical Gate Identity

Machine-readable source:

```text
references/gate-registry.yaml
```

Migration source:

```text
references/gate-migrations.yaml
```

Human authoring rules:

```text
references/gate-registry.md
```

The registry owns:

```text
ID
canonical name/title
namespace
one governing owner
design domain
status
applicability
default weight
contextual hard-gate metadata
migration relationship
```

The governing owner reference owns:

```text
review question
pass/fail interpretation
evidence requirements
examples and counterexamples
correction knowledge
domain-specific hard-gate reasoning
```

Rules:

```text
active ID       → use directly
gate alias      → normalize through the migration map
deprecated ID   → report its active replacement and migration provenance
unknown ID      → reject; do not infer
materially new meaning → register a new ID
wording clarification → keep the ID when meaning and owner remain compatible
```

External domain reviewers must register a unique namespace before exposing gates to the facade. A domain reviewer cannot mint IDs only inside its own report.

## Built-In Coverage

```text
digital-interface    web, mobile, desktop, and responsive product UI
visual-communication poster, flyer, banner, social, ad, and thumbnail
presentation         slides and decks
```

Identity systems, packaging, motion/video, industrial, spatial, fashion, and service-design disciplines require a domain reviewer for a complete verdict. Universal gates alone produce `LIMITED REVIEW`.

## Review Depth

```text
quick
  Critical universal gates + applicable hard gates + declared issue.
  No release claim.

focused
  Selected canonical gates/components + adjacent regression checks.
  Default during active refinement.

full
  All applicable gates from every loaded reviewer + major present components.
  Full only for domains covered by built-in or adapter reviewers.

release
  Full review + contextual hard gates + required states, sizes, themes,
  inputs, runtime/export evidence, and sufficient domain coverage.
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
logo concept without identity reviewer     → LIMITED REVIEW
```

Contextual hard gates:

```text
interactive release
  RI1 runtime integrity
  G21 reduced motion when applicable
  verified accessibility or task-completion blockers

static commercial delivery
  SV8–SV11 required logo/product/person/content fidelity
  SV5–SV6 mandatory text legibility
  SV12–SV13 crop/safe-area integrity
  SV17 delivery resolution

specialized domain
  hard gates declared by the loaded and registered domain reviewer
```

Use evidence appropriate to the gate: rendered visual, interaction, runtime, accessibility tree, source, asset comparison, measurements, or user/task evidence.

A build is not visual verification. A screenshot is not interaction or runtime verification. Universal visual evidence is not specialist-domain proof.

## Score and Verdict

```text
Pass threshold: 8.0 / 10
Critical: verified score below 5
Overall: weighted average of verified applicable gates only
Evidence coverage: verified applicable weight / all applicable selected weight
Primary-domain coverage: BUILT_IN | ADAPTER_COVERED | LIMITED | ROUTE_ELSEWHERE
```

```text
PASS             score >= 8, hard gates pass, sufficient domain/evidence coverage
CONDITIONAL PASS score >= 8, no verified hard-gate failure, gaps remain
NEEDS WORK       score < 8 or important gates fail
CRITICAL         hard gate fails or material critical gate exists
LIMITED REVIEW   primary-domain reviewer was not available
ROUTE ELSEWHERE  requested claim cannot be reviewed by available reviewers
```

## Output

```text
review context and route
design domain and loaded reviewers
canonical gate IDs and governing owners
score + verified evidence coverage
primary-domain coverage
contextual hard-gate status
executive findings
cluster/component/domain summary
critical / important / polish priority
NOT_APPLICABLE and NOT_VERIFIED gates
scope limitations
recommended handoff
```

Each failed or partial finding includes canonical gate ID, region, observation, evidence, impact, correction direction, confidence, and governing reviewer.

## Handoff

```text
design-audit       owns full capture, gap analysis, and prioritization
design-refinement  owns targeted fixes, preservation, and focused re-score
redesign-workflow  owns redesign, verification, defect classification, and fix loop
domain specialist  owns unsupported domain knowledge and gates
```

`design-review` reports findings. It changes artifacts only when the calling workflow explicitly owns production.

## Final Guard

```text
□ Domain, profile, artifact state, and viewing context are explicit.
□ Built-in or adapter coverage is explicit.
□ Only phase-relevant references were loaded.
□ Every selected/reported gate ID is active and canonical.
□ Aliases/deprecations were normalized through the migration map.
□ Universal gates were reviewed.
□ Surface/component/domain gates match the target.
□ Hard gates were contextual and reviewer-owned.
□ Every score has suitable evidence.
□ NOT_VERIFIED and NOT_APPLICABLE remain separate.
□ Score uses verified applicable gates only.
□ Evidence and primary-domain coverage are both shown.
□ Unsupported domains are limited, not fully passed.
□ Findings are specific, prioritized, and style-neutral.
```
