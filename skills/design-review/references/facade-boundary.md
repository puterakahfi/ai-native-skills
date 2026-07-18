# Design Review Facade Boundary

Load this reference during classification when domain coverage, ownership, or extension behavior is relevant.

`design-review` is a facade skill: callers use one review entry point while the facade selects applicable review strategies, normalizes evidence, and produces a consistent score and verdict.

## Ownership

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

The facade must not copy specialist knowledge into its core merely to avoid loading the governing skill.

## Built-in Scope

Covered by built-in review strategies:

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

Universal visual gates may provide a limited review for an unsupported discipline, but the report must state the limitation and must not claim full domain coverage.

## Coverage Modes

```text
BUILT_IN        the facade has a native review strategy for the domain
ADAPTER_COVERED a compatible specialist domain reviewer is loaded
LIMITED         only universal or partial concerns can be reviewed
ROUTE_ELSEWHERE the request requires unavailable specialist knowledge
```

A full or release verdict requires `BUILT_IN` or `ADAPTER_COVERED` coverage for the declared primary domain.

## Domain Reviewer Contract

A domain reviewer integrated through the facade must declare:

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
preserve common score and coverage semantics
state what remains outside its own scope
```

It must not:

```text
silently redefine universal gate meanings
count missing evidence as zero
claim coverage outside its declared domain
perform redesign or production unless the caller owns that lifecycle
```

## Composition Rules

When multiple reviewers match:

```text
choose one primary domain owner
load secondary reviewers only for declared cross-domain concerns
keep universal gates shared rather than duplicated per reviewer
resolve duplicate findings under the reviewer that owns the root cause
do not average unrelated domain scorecards without explicit weighting
```

Examples:

```text
mobile app with marketing onboarding
→ primary: digital-interface/mobile
→ secondary: conversion concerns only when explicitly in scope

presentation containing a dashboard mockup
→ primary: presentation
→ secondary: interactive component review limited to the mockup

logo displayed inside a poster
→ primary: visual-communication/static
→ brand-fidelity checks verify application of the supplied logo
→ logo-design quality itself requires brand-identity reviewer
```

## Boundary Failure Modes

```text
specialist knowledge copied into facade core
every request loads every reviewer
unsupported domain receives a full PASS
one scorecard is forced across unrelated disciplines
facade starts producing or redesigning without caller ownership
new domain requires rewriting unrelated built-in strategies
```

See `docs/facade-skill-pattern.md` for the repository-wide pattern definition.