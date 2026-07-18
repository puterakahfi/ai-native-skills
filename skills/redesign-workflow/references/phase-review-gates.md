# Phase 9 — Design Review Facade Adapter

This reference integrates `redesign-workflow` with the canonical `design-review` facade skill.

Do not maintain a duplicate scorecard here. Domain classification, reviewer selection, gate definitions, applicability, evidence normalization, scoring, hard-gate policy, coverage, verdicts, and report format are owned by `skills/design-review/` and its loaded domain reviewers.

## Entry condition

Review only after Phase 8 verification has produced fresh evidence for the redesigned artifact.

```text
□ target rendered or inspected in the declared artifact state
□ design domain and surface profile resolved
□ built-in or adapter reviewer coverage resolved
□ required viewports, formats, themes, or channels captured
□ relevant interactions and states exercised when interactive
□ runtime or export evidence captured when required
□ preservation locks checked
□ verification report attached to the current iteration
```

A successful build alone is not visual verification. A good-looking screenshot alone is not interaction, runtime, export, or specialist-domain verification.

## Facade loading policy

Start Phase 9 with `design-review/SKILL.md`. Then load references only when entering the phase that owns them.

```text
CLASSIFY / ROUTE
  design-review/references/review-routing.md
  design-review/references/facade-boundary.md only when scope or extension is unclear
  design-review/references/review-profiles.md only for a built-in profile

UNIVERSAL REVIEW
  design-review/references/universal-gates.md

DOMAIN / SURFACE REVIEW
  design-review/references/interactive-surface-gates.md OR
  design-review/references/static-visual-gates.md OR
  declared external domain reviewer

COMPONENT REVIEW
  design-review/references/component-review.md only for selected components

EVIDENCE + SCORE
  design-review/references/evidence-and-scoring.md

REPORT
  design-review/references/review-report.md
```

Do not preload every review reference defensively. Each completed review phase produces the handoff context for the next phase.

During an active visual loop, also load `iteration-review-mode.md`.

## Review mode selection

```text
focused iteration
  Use when one layer, component, or declared gate changed.
  Review touched gates plus adjacent regression checks.
  Do not run or display the full inventory.

full review
  Use for a major multi-layer change, audit handoff, or final design approval.
  Full means full only for domains covered by built-in or loaded adapter reviewers.

release review
  Use for commit, PR, deployment, or delivery readiness.
  All applicable contextual hard gates and required domain evidence must be verified.
```

## Route from redesign state

Map redesign state into the facade route:

```yaml
review_route:
  design_domain: <digital-interface | visual-communication | presentation | other>
  surface_profile: <from preflight/spec>
  artifact_state: <rendered-interactive | rendered-static | mixed>
  review_depth: <focused | full | release>
  coverage_mode: <BUILT_IN | ADAPTER_COVERED | LIMITED | ROUTE_ELSEWHERE>
  domain_reviewers: <built-in and external reviewers loaded>
  viewing_context: <from spec and verification>
  selected_lenses: <from changed layers and acceptance criteria>
  selected_components: <changed or high-risk components>
  applicable_hard_gates: <from loaded reviewers>
  evidence_available: <from verification report>
  evidence_gaps: []
```

Do not default every redesign to `web-marketing`. Use the declared product surface and design domain.

Built-in facade coverage includes:

```text
digital-interface    web, mobile, desktop, and responsive product UI
visual-communication poster, flyer, banner, social, ad, and thumbnail
presentation         slides and decks
```

Identity systems, packaging, motion/video, industrial, spatial, fashion, and service-design disciplines require a domain reviewer for a complete verdict. Universal gates alone produce `LIMITED REVIEW`.

## Lightweight iteration evidence

During creative iteration, keep the loop proportional to the changed layer:

```text
□ inspect all changed regions in the browser or final artifact
□ inspect adjacent regions for hierarchy and spacing regression
□ verify relevant viewports or final output ratios
□ verify every affected theme when theme behavior changed
□ exercise changed controls and overflow behavior
□ compare required logos, products, people, or content when fidelity applies
□ run changed-file diff checks when repository files changed
□ capture runtime errors when the changed flow is interactive
□ capture export evidence when the output is static or presentation-based
```

Do not reflexively run full build, lint, or every test after each small visual adjustment. Run them at the appropriate commit, PR, deploy, or release boundary, or when the changed implementation requires them.

If a full command is blocked by missing shared configuration, record the concrete blocker once. Do not repeat the same failing command as a substitute for fresh design evidence.

## Review decision

Use the verdict from the `design-review` facade:

```text
PASS
  → proceed to delivery when redesign acceptance criteria also pass

CONDITIONAL PASS
  → proceed only when evidence gaps or accepted risks fit the current approval boundary

NEEDS WORK
  → proceed to Phase 10 defect classification

CRITICAL
  → stop delivery and proceed to Phase 10 defect classification immediately

LIMITED REVIEW
  → do not claim complete domain approval; load the required domain reviewer,
    narrow the delivery claim, or route to the domain specialist
```

A score of 8 or above does not override a failed contextual hard gate, insufficient release evidence, or missing primary-domain coverage.

## Defect handoff

For each failed or partial gate, pass this structure to Phase 10:

```yaml
defect_candidate:
  gate: <id>
  governing_reviewer: <design-review built-in or domain reviewer>
  region: <affected region>
  observation: <verified condition>
  evidence: []
  impact: <user, business, accessibility, fidelity, runtime, or delivery impact>
  recommendation: <correction direction>
  suspected_layer: <foundation | structure | component | expression | interaction | content | implementation>
```

Do not classify the correction layer solely from the visible symptom. Phase 10 owns final defect classification.

Do not copy a specialist-domain correction into the facade. Route the defect to the governing reviewer or specialist skill.

## Output

Render the scorecard as normal markdown, never as a fenced wall of text.

Minimum output:

```markdown
## [target] · Design Review · Iteration [N]

**X.XX / 10** — [verdict] · Coverage [X%]

- Design domain: [domain]
- Review coverage: [BUILT_IN | ADAPTER_COVERED | LIMITED]
- Loaded reviewers: [list]
- Hard gates: [status]
- Critical findings: [count]
- Important findings: [count]

| Cluster | Score | Coverage | Governing reviewer | Notes |
|---|---:|---:|---|---|
| Universal visual quality | X.X | X% | design-review | ... |
| Domain/surface quality | X.X | X% | [reviewer] | ... |
| Components | X.X | X% | [reviewer] | ... |
| Runtime, export, or fidelity | X.X | X% | [reviewer] | ... |

**Open findings**
- `[gate]` [score/status] — [observation] → [correction direction]

**Not verified**
- [gate and missing evidence]

**Scope limitations**
- [unsupported or uncovered domain concerns]
```

The full report contract remains in `design-review/references/review-report.md`.
