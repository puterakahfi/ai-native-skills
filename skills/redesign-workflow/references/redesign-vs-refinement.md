# Redesign vs Refinement Route Decision

Run this before deciding whether to use `redesign-workflow`, `design-refinement`, or `design-audit`.

## Route table

| Current state / user signal | Use | Why |
|---|---|---|
| Direction is wrong, genre is wrong, macrostructure is wrong, or the page feels like the wrong product | `redesign-workflow` | Foundational direction must change. |
| Overall design score is unknown | `design-audit` first, then route | Do not guess which workflow applies. |
| Overall score < 7.0 | `redesign-workflow` | Direction is probably failing, not just polish. |
| Multiple critical gates < 5.0 | `redesign-workflow` | Foundation is unstable. |
| Overall ≥ 7.0 and user approves direction but names specific issues | `design-refinement` | Preserve direction and fix targeted gates only. |
| User says “something feels off” but cannot name it | quick audit + `user-feedback-parser.md` → then route | Qualitative feedback needs classification. |
| User asks to change style/genre/macrostructure | `redesign-workflow` | Style/macro changes reopen direction. |
| User asks to make current direction cleaner/quieter/more integrated | `design-refinement` | Direction stays; gates improve. |
| User asks for deploy/commit readiness | `redesign-workflow` verification phases | Full evidence and delivery gates apply. |

## Decision output

Before producing, state:

```text
Route decision:
  Workflow: [redesign-workflow | design-refinement | design-audit]
  Reason: [score/user signal/failing gate]
  Locked layers: [approved layers to preserve]
  Open layers: [layers allowed to change]
```

## Systemic-design classification for broad redesign

After routing to `redesign-workflow` and before structural direction lock, `master-design` must classify:

```yaml
systemic_design_applicability:
  status: REQUIRED | REDUCED | NOT_APPLICABLE | NOT_VERIFIED
  rationale: string
  activation_signals: []
  omitted_analysis_risk: []
```

Use `REQUIRED` or `REDUCED` when the redesign has material cross-journey, cross-route, metric, positioning, information-architecture, proof, reusable page-shell, component-family, design-system, or second-order consequences.

When applicable:

```text
redesign-workflow remains the one primary lifecycle
→ systems-reasoning creates the bounded system-to-design handoff
→ systems-thinking owns deep loops, delays, Goodhart, emergence,
  second-order effects, unintended consequences, and leverage analysis
  only when material
→ master-design compares and selects the design direction
→ design specialists resolve narrow concerns
→ design-review controls acceptance
```

The system handoff must be available before a broad layout or visual direction is locked. It can constrain candidate evaluation, but it must not select the hero, page recipe, macrostructure, component, or visual genre.

A landing page may correctly use a conventional hero and section sequence. It may also be document-led, workbench-led, interactive, catalogue-led, manifesto-led, or another product-specific structure. Artifact names and familiar patterns are signals, not automatic layouts.

Use `NOT_APPLICABLE` or `REDUCED` for a bounded accepted correction with no material change to content, behavior, route, metric, shared contract, or design-system ownership. Preserve `design-refinement`; do not inflate it into redesign merely to run systems analysis.

## Layer preservation hard rule

Approved lower layers are locked unless the user explicitly reopens them.

```text
Layer lock:
  Strategy approved → do not rewrite positioning while fixing UI.
  UI direction approved → do not change macrostructure while fixing Delight.
  UX flow approved → do not change nav/CTA routes while fixing copy.
  Voice approved → do not rewrite H1/body just to make visuals fit.
```

If a fix appears to require changing a locked layer:

```text
Stop and explain the trade-off:
  “Fixing [gate] requires reopening [locked layer] because [reason].
   Options: preserve current layer and accept smaller improvement, or reopen the layer.”
```

## Skill-first rule scope

Patch the skill before patching output when:

```text
✓ user correction reveals a missing/weak rule
✓ same failure is likely to recur
✓ review gate exists but needs a common-violation example
✓ workflow behavior, not just implementation, was wrong
```

Output-first is allowed when:

```text
✓ rule already exists and implementation simply missed it
✓ change is a one-off visual adjustment
✓ user asks for immediate iteration
✓ patching skill would slow a tight visual feedback loop without improving future behavior
```

If output-first is used and a reusable lesson emerges, patch the skill before final commit.
