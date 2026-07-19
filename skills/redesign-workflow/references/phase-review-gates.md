# Phase 9 — Design Review Facade Adapter

This reference integrates `redesign-workflow` with the canonical `design-review` facade. The facade owns universal and domain scoring. The redesign workflow additionally owns conformance to the explicit design direction and loaded genre contract.

## Entry condition

Review only after Phase 8 has produced fresh evidence.

```text
□ target rendered or inspected in the declared artifact state
□ design domain and surface profile resolved
□ selected genre reference loaded
□ genre constraints attached to the run state
□ page shell and alignment rails declared
□ required viewports, themes, formats, or channels captured
□ relevant interactions and states exercised
□ runtime or export evidence captured when required
□ preservation locks checked
□ verification report attached to the current iteration
```

A successful build is not visual verification. A screenshot alone is not runtime or interaction verification.

## Facade loading policy

Start with `design-review/SKILL.md`, then load only applicable references.

```text
CLASSIFY / ROUTE
  design-review/references/review-routing.md

UNIVERSAL REVIEW
  design-review/references/universal-gates.md

DOMAIN / SURFACE REVIEW
  design-review/references/interactive-surface-gates.md OR
  design-review/references/static-visual-gates.md OR
  declared external reviewer

COMPONENT REVIEW
  design-review/references/component-review.md only for selected components

EVIDENCE + SCORE
  design-review/references/evidence-and-scoring.md

REPORT
  design-review/references/review-report.md
```

During an active visual loop, also load `iteration-review-mode.md`.

## Contextual hard gate: genre conformance

This gate runs before the facade verdict is accepted.

```yaml
genre_conformance_gate:
  genre: <name>
  reference: <loaded path>
  constraints_tested: []
  source_evidence: []
  rendered_evidence: []
  violations: []
  status: pass | fail | not_verified
```

Rules:

```text
- explicit genre constraints are hard gates when applicable
- a high universal score cannot override a genre violation
- source evidence may identify obvious failures before rendering
- rendered evidence is required for final pass
- not_verified cannot be reported as pass
```

### Zen / space-led conformance gate

When genre is `zen-minimalist`, `editorial-minimal`, or explicitly space-led, verify:

```text
COMPOSITION
□ whitespace and proximity perform most grouping
□ one clear focal object per viewport
□ empty intervals are intentional and anchored

ALIGNMENT CONTINUITY
□ nav, hero, sections, contact, and footer share one declared page shell
□ 2–4 persistent vertical rails are visible across adjacent sections
□ section labels reuse a stable start position
□ mixed-size eyebrow/heading pairs are optically aligned by rendered glyphs, not only layout boxes
□ major headings reuse a stable main-content rail
□ titles, descriptions, and actions align to declared supporting rails
□ asymmetry comes from span, measure, or one declared focal exception
□ repeated arbitrary margin-left, padding-left, or translate-x offsets = 0
□ mobile collapses to a predictable one- or two-rail reading order

STRUCTURAL LINES
□ section dividers = 0
□ repeated per-row separators = 0 by default
□ at most one rare list-boundary hairline is justified
□ typical viewport shows target 0 and maximum 1 structural line

CONTAINMENT
□ cards are rare exceptions
□ no card-to-hairline substitution
□ no repeated bordered metadata rows across multiple sections
□ no giant boxed CTA used only for visual impact

MOTION AND EXPRESSION
□ no hover lift, bounce, glow, or decorative urgency
□ accent and texture remain rare
```

Functional exclusions from the line budget:

```text
form controls, keyboard focus rings, required tables, diagrams, charts,
and data grids whose meaning depends on lines
```

Allowed alignment exception:

```text
one documented focal object or illustration may break a rail when the break
is visually intentional, remains balanced, and does not license unrelated row drift
```

Box alignment is not optical alignment. A small uppercase label and a large display heading can occupy the same grid row yet still look vertically crooked because cap height, ascenders, and line-box metrics differ. Correct repeated label/heading relationships with one shared component or token-level optical offset. Do not add unrelated per-section nudges.

### Required evidence for zen line density and alignment

```text
1. source scan of changed visual components for:
   border-t, border-b, border-y, divide-y, divide-x, repeated <hr>,
   box-shadow separators, and pseudo-element rules

2. source scan for local alignment nudges:
   translate-x, margin-left, padding-left, arbitrary ml-[...], pl-[...],
   percentage indentation, alternating row offsets, and conflicting container widths

3. full-page or representative viewport captures

4. visible structural-line count per inspected viewport

5. alignment-rail inspection across at least three adjacent sections:
   label start, heading start, supporting-content start, action end

6. optical top-edge inspection for repeated eyebrow/heading pairs:
   compare rendered glyph edges, not only DOM boxes; verify one shared correction rule

7. mobile reading-order inspection after desktop rails collapse

8. justification for every allowed line or focal-offset exception
```

Example failed evidence:

```yaml
violations:
  - region: selected-work
    observation: every project row uses border-top
    class: card_to_hairline_substitution
  - region: principles
    observation: section border-y plus per-item border-top
    class: structural_fragmentation
  - region: page-wide
    observation: work list uses ml-[30%], principles alternate translate-x, contact uses another offset
    class: alignment_drift
  - region: selected-work-header
    observation: eyebrow and display heading share a grid row but rendered glyph tops are visibly misaligned
    class: optical_alignment_failure
  - region: responsive
    observation: desktop offsets survive stacking and create mobile zig-zag
    class: rail_collapse_failure
```

Any unapproved structural section border, repeated row-separator system, or repeated arbitrary content offset on a zen page produces `fail` and routes to defect classification.

## Review mode selection

```text
focused iteration
  changed gates plus adjacent regressions

full review
  multi-layer direction or final design approval

release review
  commit, PR, deployment, or delivery readiness
```

A genre correction that changes containment grammar or alignment rails requires at least a focused review across every affected section, not only the initially reported component.

## Route from redesign state

```yaml
review_route:
  design_domain: <digital-interface | visual-communication | presentation | other>
  surface_profile: <from spec>
  artifact_state: <rendered-interactive | rendered-static | mixed>
  review_depth: <focused | full | release>
  coverage_mode: <BUILT_IN | ADAPTER_COVERED | LIMITED | ROUTE_ELSEWHERE>
  domain_reviewers: []
  genre_reviewer: <loaded design-genre reference>
  selected_lenses: []
  selected_components: []
  applicable_hard_gates: []
  evidence_available: []
  evidence_gaps: []
```

Do not default every redesign to `web-marketing`. Use the actual surface and design domain.

## Lightweight iteration evidence

```text
□ inspect every changed region
□ inspect adjacent regions for rhythm, hierarchy, and alignment regressions
□ verify affected viewports and themes
□ exercise changed controls and overflow
□ run changed-file diff, genre-token scan, and local-offset scan
□ capture runtime errors for interactive surfaces
□ record any deferred build/test gates honestly
```

Do not use repeated full builds as a substitute for fresh visual evidence.

## Review decision

Use the facade verdict only after contextual hard gates are applied.

```text
PASS
  facade passes + genre conformance passes + redesign acceptance passes

CONDITIONAL PASS
  only when remaining evidence gaps fit the approval boundary and no genre hard gate fails

NEEDS WORK
  failed genre or scored gate → Phase 10 defect classification

CRITICAL
  blocking runtime, accessibility, fidelity, or destructive failure

LIMITED REVIEW
  missing domain coverage or rendered evidence; never claim full approval
```

A score of 8 or above does not override a failed genre hard gate, missing release evidence, or insufficient domain coverage.

## Defect handoff

```yaml
defect_candidate:
  gate: <id>
  governing_reviewer: <genre reference | design-review | domain reviewer>
  region: <affected region>
  observation: <verified condition>
  evidence: []
  impact: <user | business | accessibility | fidelity | runtime | delivery>
  recommendation: <direction>
  suspected_layer: <foundation | structure | component | expression | interaction | content | implementation>
```

For recurring genre violations, consider:

```text
workflow_orchestration_defect
  selected reference was not loaded or its constraints were not propagated

reference_knowledge_defect
  genre rule was ambiguous or allowed a recurring wrong interpretation

local_implementation_defect
  rule was clear and loaded, but implementation violated it
```

Alignment drift caused by many local offsets is a structure defect, not a set of unrelated component-polish defects. Reopen the shared grid and remove the nudges instead of correcting each item independently.

Repeated optical misalignment in the same label/heading pattern is a component-system defect. Fix the shared primitive once; do not scatter `pt-*`, `top-*`, or transforms across individual sections.

Do not classify solely from the visible symptom.

## Minimum report

```markdown
## [target] · Design Review · Iteration [N]

**X.XX / 10** — [verdict] · Coverage [X%]

- Design domain: [domain]
- Genre: [genre]
- Genre conformance: [pass | fail | not verified]
- Structural line count by viewport: [evidence]
- Page shell: [value]
- Persistent alignment rails: [evidence]
- Optical label/heading alignment: [pass | fail | not verified]
- Arbitrary offset count: [number and regions]
- Responsive rail collapse: [pass | fail | not verified]
- Review coverage: [mode]
- Hard gates: [status]
- Critical findings: [count]
- Important findings: [count]

| Cluster | Score/status | Coverage | Governing reviewer | Notes |
|---|---:|---:|---|---|
| Genre conformance | pass/fail | X% | design-genre | ... |
| Alignment continuity | pass/fail | X% | redesign-workflow | ... |
| Universal visual quality | X.X | X% | design-review | ... |
| Domain/surface quality | X.X | X% | reviewer | ... |
| Components | X.X | X% | reviewer | ... |
| Runtime/export/fidelity | X.X | X% | reviewer | ... |

**Open findings**
- [gate] — [observation] → [correction]

**Not verified**
- [missing evidence]
```

The full report contract remains in `design-review/references/review-report.md`.
