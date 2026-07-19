# Design Review Facade Boundary

Load this reference during classification when domain coverage, ownership, or extension behavior is relevant.

`design-review` is a facade: callers use one entry point while it selects reviewers, resolves canonical gate IDs, normalizes evidence, and produces a consistent score and verdict.

## Ownership

The facade owns:

```text
surface and domain classification
review profile and strategy selection
canonical gate resolution and migration
applicability status
common evidence model
score, coverage, and verdict policy
finding and report contract
handoff to audit, refinement, redesign, legal, or specialist routes
```

Domain reviewers own:

```text
domain principles and thresholds
full gate definitions
evidence interpretation
specialized hard gates
production methods and correction knowledge
scope and professional-boundary limits
```

The facade must not copy specialist knowledge merely to avoid loading its owner.

## Coverage

Built-in strategies:

```text
digital product interfaces
responsive web experiences
mobile and desktop applications
static marketing and social visuals
advertising creatives and thumbnails
presentation slides and decks
```

Registered external adapter:

```text
brand-identity
  reviewer: brand-identity-review
  namespace: BI
  owner: skills/brand-identity-review/references/identity-gates.md
  coverage when loaded: ADAPTER_COVERED
```

Still requiring future adapters:

```text
packaging and specialist print production
motion graphics, film, and video editing
industrial or physical product design
architecture, interior, and spatial design
fashion design
service-design systems
```

Universal gates may provide limited observations when a required adapter is unavailable, but they cannot produce complete specialist-domain approval.

## Coverage Modes

```text
BUILT_IN        native facade strategy covers the primary domain
ADAPTER_COVERED compatible specialist reviewer is loaded
LIMITED         only universal or partial concerns can be reviewed
ROUTE_ELSEWHERE requested claim requires unavailable expertise
```

A full or release verdict requires `BUILT_IN` or `ADAPTER_COVERED` primary-domain coverage plus sufficient evidence.

## Domain Reviewer Contract

```yaml
domain_reviewer:
  domain: <stable domain id>
  gate_namespace: <registered uppercase prefix>
  gate_registry_entries: design-review/references/gate-registry.yaml
  required_context: []
  required_evidence: []
  gates: <repo-relative governing owner reference>
  hard_gate_triggers: []
  unsupported_claims: []
  finding_contract: design-review/finding
```

A reviewer must:

```text
register one unique namespace
register every exposed gate ID
keep full definitions in its own governing reference
return PASS/FAIL/PARTIAL/NOT_VERIFIED/NOT_APPLICABLE
provide evidence and impact for failures/partials
identify contextual hard gates
map findings to the facade contract
preserve common score and coverage semantics
state out-of-scope claims
add eval coverage with design_gate_ids
```

It must not:

```text
mint IDs only inside prompts or reports
reuse another domain namespace for unrelated meaning
redefine universal gates silently
count missing evidence as zero
claim coverage outside its domain
perform redesign/production unless caller owns that lifecycle
claim professional clearance outside its boundary
```

The registry validator accepts:

```text
built-in owner filename
  universal-gates.md

external repo-relative owner path
  skills/brand-identity-review/references/identity-gates.md
```

Owner paths cannot escape the repository.

## Composition Rules

When multiple reviewers match:

```text
choose one primary domain owner
load secondary reviewers only for declared cross-domain concerns
keep universal gates shared rather than duplicated
resolve duplicate findings under the root-cause owner
normalize every finding to a canonical registered ID
do not average unrelated scorecards without explicit weighting
```

Examples:

```text
logo identity system
→ primary: brand-identity
→ facade: design-review
→ reviewer: brand-identity-review
→ coverage: ADAPTER_COVERED

logo displayed inside a poster
→ primary: visual-communication/static
→ SV8 verifies application of supplied approved logo
→ BI gates apply only when logo-system quality itself is in scope

presentation containing a dashboard mockup
→ primary: presentation
→ secondary interactive review limited to the mockup
```

## Boundary Failure Modes

```text
specialist knowledge copied into facade core
every request loads every reviewer
unsupported domain receives full PASS
one scorecard forced across unrelated disciplines
facade produces/redesigns without lifecycle ownership
external reviewer invents unregistered IDs
external reviewer stores definitions in the facade
alias guessed from similar wording
similarity screening presented as legal clearance
```

See `gate-registry.md` for extension rules and `docs/facade-skill-pattern.md` for the repository-wide facade pattern.