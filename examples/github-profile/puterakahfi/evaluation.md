# Putera Kahfi GitHub Profile Evaluation

## Fixture

```yaml
profile_repository: puterakahfi/puterakahfi
profile_url: https://github.com/puterakahfi
initial_commit: c1a3f65b6138093e8a817019425aca23c681f0c7
refined_commit: d5ebd185a1d78f7ce11cfba87e24c3c30092b9ff
skill: github-profile@1.1.0
mode: create_then_refine
output_mode: patch
```

## Behavioral Result

```text
classification: APPLIED_AND_REFINED
```

The fixture exercises the full feedback loop rather than accepting valid Markdown as finished design:

1. generate a proof-first profile
2. publish to the real GitHub Profile README surface
3. inspect a user-provided desktop screenshot
4. identify hierarchy and differentiation failures
5. refine the live README
6. convert the learning into skill rules and a regression case

## Initial Source Successes

The first version demonstrated important skill behavior:

- audience and positioning appeared before technology detail
- selected work appeared before capability groups
- projects included role, contribution, and current state
- public repositories provided direct proof
- private implementation repositories were not exposed as public proof
- no employer, client, revenue, user-count, or impact metrics were invented
- no badge wall, statistics wall, trophies, counters, animation, or third-party widgets were added
- current-focus statements were dated for maintainability

## Rendered Findings · Version 1.0.0

A desktop screenshot of the live GitHub profile changed the verdict from source-only acceptance to a limited rendered review.

```text
PASS     factual integrity
PASS     proof before badges
PASS     GitHub-native readability
PASS     anti-clutter
PARTIAL  first-viewport memorability
PARTIAL  information hierarchy
PARTIAL  visual composition
FAIL     brand differentiation
```

Observed failures:

- the hero used a generic name + role + paragraph + links pattern
- nearly every section used the same heading-plus-paragraph treatment
- selected projects read like documentation entries rather than proof modules
- Native AI Engineering, How I build systems, Current focus, and Working principles repeated related ideas
- the document was clean but visually anonymous
- the visitor had to read too much before reaching a memorable thesis

This proves that semantic correctness, restraint, and source readability are necessary but insufficient for a strong profile.

## Refinement · Version 1.1.0

The refined README introduces a declared differentiation device:

```text
primary device: thesis-led editorial opening
supporting device: repeated GitHub-native proof blocks
```

Changes:

- replaces the generic role subtitle with a specific engineering proposition
- introduces a memorable system thesis in the opening viewport
- moves selected work directly after the hero
- renders projects as compact blockquote proof modules
- gives the engineering thesis a distinct quote and process-flow treatment
- merges overlapping principles into three bounded statements
- reduces total explanatory density
- keeps all critical information semantic and dependency-free

## Contract Mapping

### `backend-engineer-proof-before-badges`

```text
PASS  selected work exists
PASS  project ownership and contribution are explicit
PASS  AI-native, DDD, and ports-and-adapters positioning exists
PASS  positioning precedes technology detail
PASS  no forbidden badge/counter/trophy behavior
```

### `founder-profile-uses-product-narrative`

```text
PASS  VisualMate is framed by product purpose and ownership
PASS  product proof precedes generic tool lists
PASS  profile remains a personal-brand surface, not a long CV
```

### `username-only-does-not-invent-biography`

```text
PASS  only supplied, authenticated, public-repository, or public-product facts are used
PASS  unsupported employers, metrics, clients, and achievements are excluded
```

### `explicit-clutter-request-is-reframed`

```text
PASS  proof and hierarchy control the composition
PASS  dynamic widgets: none
PASS  critical information is semantic text
```

### `clean-but-anonymous-needs-differentiation`

```text
PASS  rendered feedback is not dismissed because source is valid
PASS  a recognizable engineering thesis is declared
PASS  selected work receives a distinct proof-module treatment
PASS  repeated sections are merged
PASS  all major sections no longer share equal visual weight
```

## GitHub Activation Checks

```text
PASS  repository name matches username
PASS  repository is public
PASS  non-empty README.md exists at repository root
PASS  default branch is main
```

## Source Acceptance · Refined Version

```text
PASS  one semantic H1
PASS  ordered H2/H3 hierarchy
PASS  project proof before capability inventory
PASS  differentiation device declared and implemented
PASS  no external image or widget dependency
PASS  no private email or private repository details exposed
PASS  source remains concise and human-editable
PASS  current statements are dated
```

## Render Acceptance

```text
PASS          initial desktop render captured and reviewed
NOT_VERIFIED  refined desktop render not yet captured
NOT_VERIFIED  narrow-width visual screenshot not captured
NOT_VERIFIED  light/dark visual comparison not captured
```

The initial screenshot is valid evidence for identifying the first composition failure. The refined source must still be captured directly before a full READY verdict. Until then, retain `LIMITED REVIEW` for the live refined result.

## Learning Result

```text
universal design principles are portable
surface implementation rules are contextual
clean is a baseline, not differentiation
source validity does not prove rendered hierarchy
selected work needs visual contrast, not only factual anatomy
GitHub Profile README needs document-specific translation
```

Potential next evolution: compare this fixture with engineer, founder, maintainer, and designer profiles before registering a dedicated `developer-profile` or `document-portfolio` review profile.
