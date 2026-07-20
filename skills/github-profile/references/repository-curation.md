# Repository Curation

Repository curation turns the profile narrative into inspectable proof. It does not reward repository count, recency theatre, or decorative popularity metrics.

## Pinning Principle

GitHub supports a bounded pinned section. Do not fill every available slot merely because it exists. A smaller complementary set is better than six repetitive or weak repositories.

Each recommended pin must answer:

```text
why this repository belongs
what proof role it serves
what the visitor should notice
whether the repository is publicly ready
what action follows inspection
```

## Proof Roles

Use complementary roles rather than six versions of the same evidence:

```text
flagship-system       strongest end-to-end system or product proof
public-contract       architecture, standards, framework, or reusable contract
technical-depth       focused implementation demonstrating engineering depth
open-source-community maintainership, contribution pathway, or reusable public utility
product-proof         product direction, workflow, or shipped user-facing value
writing-resource      documentation, teaching, research, or authored knowledge
case-study            bounded problem, role, decisions, and verified outcome
```

One repository may serve more than one role, but its primary role must be explicit.

## Selection Axes

Evaluate each candidate:

```yaml
repository_pin_candidate:
  repository: owner/name
  state: OBSERVED | NOT_VERIFIED
  audience_relevance: 0..3
  proof_strength: 0..3
  ownership_clarity: 0..3
  public_readiness: 0..3
  currentness: 0..3
  complementarity: 0..3
  maintenance_confidence: 0..3
  primary_proof_role:
  risks: []
  recommendation: pin | keep-pinned | unpin | do-not-pin | NOT_VERIFIED
  reason:
```

Scores support judgment; they do not replace it. A repository with strong stars but weak ownership context may be less useful than a smaller repository that clearly proves the target positioning.

## Pin Set Contract

```yaml
repository_curation:
  current_pins:
    state: OBSERVED | NOT_VERIFIED
    items: []
  recommended_pin_set:
    - repository:
      proof_role:
      visitor_question_answered:
      readiness: PASS | PARTIAL | FAIL | NOT_VERIFIED
      reason:
  recommended_order: []
  unpin_recommendations:
    - repository:
      reason:
  unfilled_slots_reason:
  gaps: []
```

Order pins by visitor decision value, not by repository age or star count.

## Repository Hygiene

For every selected proof repository, inspect:

```text
identity
  repository name is understandable
  description explains purpose and value
  homepage points to the right destination
  topics support discoverability without keyword stuffing

entry experience
  README answers what, why, who, status, setup/use, and where to go next
  proof of ownership or contribution is understandable
  screenshots or diagrams have semantic context

trust
  current, maintenance, experimental, legacy, or archived state is explicit
  license is appropriate when public reuse is implied
  CI/release badges reflect real repository state
  setup instructions are credible
  broken links and stale claims are removed

participation
  contribution guidance exists when collaboration is invited
  issue/discussion destination is appropriate
  security or support expectations are clear when relevant
```

A repository README does not need every section. It needs enough information for its proof role and audience.

## Repository Lifecycle

Classify repositories before recommending archival:

```text
current       actively developed or intentionally current
maintenance   stable, supported, low-change
experimental  learning, prototype, or incomplete by design
legacy        historically useful but not current proof
archived      read-only and explicitly no longer maintained
unknown       insufficient evidence
```

Archive is not a visual cleanup shortcut. Before recommending archive, verify:

```text
□ repository is no longer intended for active work
□ replacement or historical context is documented when relevant
□ README and description can explain the status
□ open issues and pull requests have been considered
□ links from profile, docs, packages, or deployments have been checked
□ user or workflow explicitly approves the lifecycle change
```

Never automatically archive repositories because they are old, small, unfashionable, or visually inconvenient.

## Topics and Descriptions

Topics should describe purpose, subject, community, or language. Avoid duplicate synonyms and generic keyword dumping.

Description contract:

```text
what it is + who/what it serves + differentiating purpose
```

Examples:

```text
Weak:  My project
Weak:  AI tools and stuff
Better: Runtime-agnostic contracts for agent-driven engineering systems.
Better: Reusable design and engineering skills for coding agents and workflows.
```

## Curation Failure Signals

```text
README promises projects that are not public or inspectable
pins repeat the same proof role
popular repositories replace relevant repositories
private implementation is presented as public source proof
archival is recommended from age alone
repository topics are treated as skill proof
empty descriptions force visitors to guess
project README explains setup but not purpose or ownership
all six pin slots are filled despite weak candidates
```
