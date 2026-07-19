# Putera Kahfi GitHub Profile Evaluation

## Fixture

```yaml
profile_repository: puterakahfi/puterakahfi
profile_url: https://github.com/puterakahfi
commit: c1a3f65b6138093e8a817019425aca23c681f0c7
skill: github-profile@1.0.0
mode: create
output_mode: patch
```

## Behavioral Result

```text
classification: APPLIED
```

The generated README demonstrates the skill-specific behavior rather than a generic developer-profile template:

- audience and positioning appear before technology detail
- selected work appears before capability groups
- projects include role, contribution, and current state
- public repositories provide direct proof
- private implementation repositories are not exposed as public proof
- no employer, client, revenue, user-count, or impact metrics were invented
- no badge wall, statistics wall, trophies, counters, animation, or third-party widgets were added
- one editorial technical-authority direction controls the whole document
- current-focus statements are dated for maintainability

## Contract Mapping

### `backend-engineer-proof-before-badges`

```text
PASS  selected work exists
PASS  role and contribution labels exist
PASS  AI-native, DDD, and ports-and-adapters positioning exists
PASS  positioning precedes any technology detail
PASS  no forbidden badge/counter/trophy behavior
```

### `founder-profile-uses-product-narrative`

```text
PASS  VisualMate is framed by product purpose, role, contribution, and state
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

## GitHub Activation Checks

```text
PASS  repository name matches username
PASS  repository is public
PASS  non-empty README.md exists at repository root
PASS  default branch is main
```

## Source Acceptance

```text
PASS  one semantic H1
PASS  ordered H2/H3 hierarchy
PASS  project proof before capability inventory
PASS  no external image or widget dependency
PASS  no private email or private repository details exposed
PASS  source is concise and human-editable
PASS  current statements are dated
```

## Render Acceptance

```text
NOT_VERIFIED  desktop visual screenshot not captured by the current connector
NOT_VERIFIED  narrow-width visual screenshot not captured
NOT_VERIFIED  light/dark visual comparison not captured
```

The profile is live on GitHub, but a complete design-review verdict still requires direct rendered visual evidence. Until that evidence is captured, retain `NOT_VERIFIED` for render-specific checks and `LIMITED REVIEW` for primary-domain facade coverage.

## Learning Result

The test supports the design architecture:

```text
universal design principles are portable
surface implementation rules are contextual
GitHub Profile README needs document-specific translation
render evidence remains distinct from valid Markdown source
```

Potential next evolution: register a `developer-profile` or `document-portfolio` review profile after comparing this fixture with additional engineer, founder, maintainer, and designer profiles.
