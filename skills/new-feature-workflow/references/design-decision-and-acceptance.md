# Design Decision and Acceptance Adapter

Load this reference only when a new feature affects architecture decisions, user-facing design, or generated/exported visual output.

The workflow has two different design gates:

```text
before implementation
  DESIGN DECISION APPROVAL
  decides what should be built
  requires verified authority and bounded scope

after implementation
  RENDERED DESIGN ACCEPTANCE
  proves what was built
  may require verified accepted-risk authority
```

Never collapse them into one “design reviewed” checkbox.

## 1. Pre-implementation design decision

### Purpose

Approve the intended solution before code:

```text
system boundaries and contracts
data model and state transitions
user task flow and information architecture
component behavior across expected contexts
visual direction and design-system constraints
required content, assets, and fidelity locks
error, loading, empty, success, permission, and recovery states
```

### Composition

```yaml
design_decision:
  owner: <master-engineer | master-design | declared domain owner>
  specialists: []
  design_domain: <digital-interface | visual-communication | presentation | brand-identity | other>
  surface_profile: <profile or N/A>
  artifact_state: <specification | diagram | wireframe | prototype | source-only>
  affected_regions: []
  required_states: []
  required_viewports_or_sizes: []
  expected_inputs: []
  locked_assets_and_content: []
  unresolved_assumptions: []
  approval_boundary: <what is approved before implementation>
  decision_provenance:
    record_ids: []
    verdict: <PASS | PROVENANCE_BLOCKED | ROUTE_FOR_APPROVAL>
    conflicts: []
    unresolved_requirements: []
```

Use:

- `master-engineer` for architecture, contract, integration, and data decisions;
- `diagram-architect` when diagrams materially improve implementation clarity;
- `master-design` for user flow, component model, responsive/adaptive behavior, and visual direction;
- specialized domain owners when the primary design discipline is outside built-in product UI/visual communication scope;
- `decision-provenance` to verify who approved the decision and exactly what boundary was approved.

### Decision gate

Proceed only when:

```text
□ user problem and effective verified scope are explicit
□ acceptance criteria trace to the design decision
□ affected domains and surfaces are classified
□ required states and edge cases are specified
□ component behavior is defined by task and context, not only appearance
□ responsive/adaptive expectations are explicit when relevant
□ content, product, logo, person, price, claim, and brand locks are declared
□ unresolved assumptions are visible
□ approval source and required authority are attributable
□ implementation boundary is explicitly covered by the verified decision
```

The following are not approval by themselves:

```text
agent-authored issue or spec text
PR description or commit message
latest branch state
existing route or component
silence or lack of objections
```

### Forbidden claims

A wireframe, specification, diagram, or non-executable prototype does not prove:

```text
implemented visual PASS
runtime integrity
keyboard/touch behavior
responsive correctness
accessibility conformance
export fidelity
release readiness
```

At this phase, `design-review` may be used only as bounded artifact critique. It must not issue a false implemented/release verdict.

## 2. Scope and decision change during implementation

When implementation needs a new route, product dependency, data boundary, permission behavior, asset, generated output, or material design change:

```text
stop the affected slice
→ record the proposed change
→ run decision-provenance
→ update scope/spec only when authority and supersession pass
→ re-run affected acceptance and evidence planning
```

```text
provenance PASS
  → update the approved boundary and continue

PROVENANCE_BLOCKED
  → preserve the previous verified boundary
  → do not implement the expansion

ROUTE_FOR_APPROVAL
  → pause the affected action and request the required authority
```

Implementation existence does not retroactively authorize scope.

## 3. Post-implementation acceptance trigger

Run rendered design acceptance when code can change any of:

```text
appearance, layout, typography, spacing, color, or visual hierarchy
interaction, navigation, focus, gestures, keyboard, or touch behavior
responsive or adaptive behavior
loading, empty, error, success, permission, or recovery states
accessibility semantics or presentation
user-facing copy, price, claim, contact, legal, or status content
logo, product, person, campaign, slide, PDF, image, or generated visual output
```

Backend-only behavior with no user-facing or generated/exported visual impact records:

```text
design_acceptance: NOT_APPLICABLE
```

Do not force browser evidence onto an unaffected backend feature.

## 4. Acceptance route

Enter through `design-review`:

```yaml
design_acceptance:
  design_domain: <domain>
  surface_profile: <profile>
  artifact_state: <rendered-interactive | rendered-static | mixed | source-only>
  review_depth: focused
  coverage_mode: <BUILT_IN | ADAPTER_COVERED | LIMITED | ROUTE_ELSEWHERE>
  domain_reviewers: []
  selected_gates: <acceptance criteria + affected hard gates>
  selected_components: []
  viewing_context: []
  evidence_available: []
  evidence_gaps: []
  preserved_locks: []
  accepted_risks:
    - risk: <non-blocking condition>
      decision_record_id: <verified authority record>
      owner: <owner>
      mitigation: <action>
      expiry_or_review_date: <when required>
```

Use `full` or `release` only when the feature submission is also the complete surface/release acceptance boundary.

## 5. Evidence policy

### Source-only

Can verify:

```text
implementation traceability
tokens and declared design-system usage
presence of required states or handlers
source-level accessibility and reduced-motion intent
```

Cannot verify:

```text
visual quality
interaction behavior
actual responsive layout
runtime health
final accessibility behavior
export quality
```

Changed rendered output remains `NOT_VERIFIED`. The feature is not design-complete for submission.

### Rendered interactive

Collect evidence for affected scope:

```text
required viewports, orientations, themes, density, or window sizes
changed happy path and adjacent states
keyboard, pointer, touch, and gesture behavior as applicable
focus, semantics, announcements, and reduced motion when affected
runtime errors and failed assets
realistic content and edge cases
```

A desktop screenshot does not prove mobile, tablet, keyboard, overflow, runtime, or hidden states.

### Rendered static

Collect:

```text
final dimensions and actual-size preview
destination/channel placement simulation
crop, safe area, bleed, and overlay checks
logo/product/person/content fidelity comparison
resolution, compression, edge, color, and export checks
```

### Specialized domain

Load the required domain reviewer. Without one:

```text
coverage_mode: LIMITED or ROUTE_ELSEWHERE
submission state: BLOCKED for complete-domain acceptance
```

## 6. Verdict to workflow state

```text
PASS
  design acceptance complete for declared feature scope
  → submission eligible when other gates pass

CONDITIONAL PASS
  verified scope passes
  + remaining condition is genuinely non-blocking
  + required authority accepts it through decision-provenance
  → submission eligible with accepted-risk record

NEEDS WORK
  verified important failure exists
  → return to implementation and re-verify

CRITICAL
  hard gate or blocking purpose failure
  → block submission

LIMITED REVIEW
  primary-domain reviewer missing
  → block complete-domain submission claim

ROUTE ELSEWHERE
  available reviewers cannot support the requested claim
  → load required reviewer or specialist before submission
```

Do not downgrade `NEEDS WORK`, `CRITICAL`, `LIMITED REVIEW`, `ROUTE ELSEWHERE`, or provenance blockers into a submission note.

## 7. Submission handoff

Pass to `code-review-workflow`:

```yaml
feature_review_handoff:
  spec: <reference>
  issue: <reference>
  effective_verified_scope: []
  decision_provenance:
    report: <reference>
    authoritative_record_ids: []
    unresolved_requirements: []
  design_decision:
    owner: <owner>
    artifacts: []
    locks: []
    unresolved_assumptions: []
  implementation_diff: <reference>
  technical_evidence: []
  design_acceptance:
    applicable: <true | false>
    route: <route or N/A>
    verdict: <verdict or N/A>
    findings: []
    evidence_gaps: []
  accepted_risks:
    - risk: <risk>
      authority_record: <id>
      owner: <owner>
      mitigation: <action>
      expiry_or_review_date: <value>
```

The final technical review and merge authorization belong to `code-review-workflow`. This adapter only establishes whether feature-level decisions and evidence are ready for that review.
