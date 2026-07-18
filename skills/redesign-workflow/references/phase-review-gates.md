# Phase 9 — Review Adapter

This reference integrates `redesign-workflow` with the canonical `design-review` skill.

Do not maintain a duplicate scorecard here. Gate definitions, applicability, evidence, scoring, hard-gate policy, and report format are owned by `skills/design-review/`.

## Entry condition

Review only after Phase 8 verification has produced fresh evidence for the redesigned artifact.

```text
□ target rendered or inspected in the declared artifact state
□ required viewports, formats, themes, or channels captured
□ relevant interactions and states exercised when interactive
□ runtime or export evidence captured when required
□ preservation locks checked
□ verification report attached to the current iteration
```

A successful build alone is not visual verification. A good-looking screenshot alone is not interaction or runtime verification.

## Load order

```text
1. design-review/SKILL.md
2. design-review/references/review-routing.md
3. design-review/references/review-profiles.md
4. design-review/references/universal-gates.md
5. surface-specific reference selected by routing
6. design-review/references/component-review.md when relevant
7. design-review/references/evidence-and-scoring.md
8. design-review/references/review-report.md
```

During an active visual loop, also load `iteration-review-mode.md`.

## Review mode selection

```text
focused iteration
  Use when one layer, component, or declared gate changed.
  Review touched gates plus adjacent regression checks.
  Do not run or display the full inventory.

full review
  Use for major multi-layer change, audit handoff, or final design approval.

release review
  Use for commit, PR, deployment, or delivery readiness.
  All applicable contextual hard gates must be verified.
```

## Route from redesign state

Map redesign state into the review route:

```yaml
review_route:
  surface_profile: <from preflight/spec>
  artifact_state: <rendered-interactive | rendered-static | mixed>
  review_depth: <focused | full | release>
  viewing_context: <from spec and verification>
  selected_lenses: <from changed layers and acceptance criteria>
  selected_components: <changed or high-risk components>
  applicable_hard_gates: <from selected design-review profile>
  evidence_available: <from verification report>
  evidence_gaps: []
```

Do not default every redesign to `web-marketing`. Use the declared product surface.

## Lightweight iteration evidence

During creative iteration, keep the loop proportional to the changed layer:

```text
□ inspect all changed regions in the browser or final artifact
□ inspect adjacent regions for hierarchy and spacing regression
□ verify relevant viewports or final output ratios
□ verify every affected theme when theme behavior changed
□ exercise changed controls and overflow behavior
□ run changed-file diff checks when repository files changed
□ capture runtime errors when the changed flow is interactive
```

Do not reflexively run full build, lint, or every test after each small visual adjustment. Run them at the appropriate commit, PR, deploy, or release boundary, or when the changed implementation requires them.

If a full command is blocked by missing shared configuration, record the concrete blocker once. Do not repeat the same failing command as a substitute for fresh visual evidence.

## Review decision

Use the verdict from `design-review`:

```text
PASS
  → proceed to delivery when redesign acceptance criteria also pass

CONDITIONAL PASS
  → proceed only when remaining evidence gaps or accepted risks are compatible with the current approval boundary

NEEDS WORK
  → proceed to Phase 10 defect classification

CRITICAL
  → stop delivery and proceed to Phase 10 defect classification immediately
```

A score of 8 or above does not override a failed contextual hard gate or insufficient release coverage.

## Defect handoff

For each failed or partial gate, pass this structure to Phase 10:

```yaml
defect_candidate:
  gate: <id>
  region: <affected region>
  observation: <verified condition>
  evidence: []
  impact: <user, business, accessibility, fidelity, runtime, or delivery impact>
  recommendation: <correction direction>
  suspected_layer: <foundation | structure | component | expression | interaction | content | implementation>
```

Do not classify the correction layer solely from the visible symptom. Phase 10 owns final defect classification.

## Output

Render the scorecard as normal markdown, never as a fenced wall of text.

Minimum output:

```markdown
## [target] · Design Review · Iteration [N]

**X.XX / 10** — [verdict] · Coverage [X%]

- Hard gates: [status]
- Critical findings: [count]
- Important findings: [count]

| Cluster | Score | Coverage | Notes |
|---|---:|---:|---|
| Universal visual quality | X.X | X% | ... |
| Surface-specific quality | X.X | X% | ... |
| Components | X.X | X% | ... |
| Runtime or fidelity | X.X | X% | ... |

**Open findings**
- `[gate]` [score/status] — [observation] → [correction direction]

**Not verified**
- [gate and missing evidence]
```

The full report contract remains in `design-review/references/review-report.md`.