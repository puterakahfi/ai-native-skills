# GitHub Profile Ecosystem

A GitHub profile is not only a `README.md`. It is a public system of identity, proof, navigation, repository presentation, and contribution context.

Use this reference when `scope` is `profile-surface` or `full-profile-ecosystem`.

## Source Priority

```text
1. explicit user goal and privacy constraints
2. observed GitHub profile and repository state
3. repository-verifiable evidence
4. established brand grammar
5. official GitHub platform behavior
6. third-party profile patterns as optional market references
```

Third-party guides may reveal common expectations, but they do not define quality. Banners, counters, badges, stats, and animations remain conditional enhancements.

## Scope Modes

```yaml
scope_modes:
  readme-only:
    owns:
      - profile README strategy and composition
      - README render and verification
    reports_adjacent_gaps: true

  profile-surface:
    owns:
      - identity metadata audit
      - profile README
      - pinned-item curation recommendation
      - CTA and destination alignment
      - cross-surface consistency review
    repository_depth: selected proof repositories only

  full-profile-ecosystem:
    owns:
      - all profile-surface responsibilities
      - public repository inventory
      - repository hygiene and lifecycle recommendations
      - discoverability metadata review
      - contribution and open-source proof routing
      - enhancement dependency policy
```

Scope controls audit depth. It never expands write authority automatically.

## Public Profile Surfaces

```text
identity metadata
  avatar, display name, bio, location, website, social links, status

profile README
  positioning, proof, selected work, current focus, actions

pinned items
  repositories or gists that visitors should inspect next

repository presentation
  name, description, homepage, topics, README, license, CI/release state,
  public/private/archived status, contribution guidance

contribution context
  recent meaningful work, open-source participation, maintainership,
  issue and pull-request pathways

external destinations
  personal site, product pages, writing, documentation, contact paths
```

Do not treat contribution volume, a green graph, streaks, or top-language cards as direct proof of expertise or impact.

## Observation States

Every ecosystem claim or recommendation must use one state:

```text
OBSERVED        directly visible or tool-verified
RECOMMENDED     proposed from verified evidence and strategy
APPROVED        explicitly accepted by the user or governing workflow
REJECTED        evaluated and intentionally not selected
NOT_VERIFIED    required evidence is unavailable
NOT_APPLICABLE  irrelevant to the selected goal or scope
```

Never silently convert `RECOMMENDED` into `OBSERVED`, or `NOT_VERIFIED` into a negative finding.

## Inventory Contract

```yaml
github_profile_surface_inventory:
  scope: readme-only | profile-surface | full-profile-ecosystem
  profile_identity:
    avatar: { state: OBSERVED | NOT_VERIFIED, note: }
    display_name: { state: OBSERVED | NOT_VERIFIED, value: }
    bio: { state: OBSERVED | NOT_VERIFIED, value: }
    location: { state: OBSERVED | NOT_VERIFIED, value: }
    website: { state: OBSERVED | NOT_VERIFIED, value: }
    social_links: []
    status: { state: OBSERVED | NOT_VERIFIED, value: }
  readme:
    repository:
    state: OBSERVED | NOT_VERIFIED
    active_variant:
    render_evidence: []
  pinned_items:
    current_state: OBSERVED | NOT_VERIFIED
    items: []
  repositories:
    observed: []
    selected_for_deep_review: []
  contribution_context:
    state: OBSERVED | NOT_VERIFIED | NOT_APPLICABLE
    evidence: []
  destinations:
    observed: []
    broken_or_conflicting: []
  privacy_constraints: []
  missing_evidence: []
```

## Cross-Surface Consistency

Verify these relationships:

```text
README positioning ↔ profile bio
selected work      ↔ pinned repositories
project claims     ↔ repository state and README
current focus      ↔ current public evidence or explicit user statement
CTA                ↔ working destination and audience goal
brand grammar      ↔ avatar, README, banners, owned visuals, external site
public proof       ↔ repositories that visitors can actually access
```

A strong README cannot compensate for contradictory pins, inaccessible proof, empty repository descriptions, or project READMEs that do not explain the work.

## Visitor Journey

The profile surface should support one primary journey:

```text
identify person
→ understand positioning
→ inspect strongest proof
→ verify ownership and current state
→ choose a relevant next action
```

Common goal mappings:

```yaml
cta_mapping:
  hiring:
    primary: inspect selected engineering work
    secondary: contact or resume destination
  consulting:
    primary: understand capability and engagement fit
    secondary: discuss a problem
  freelance:
    primary: inspect relevant shipped work
    secondary: request availability
  open-source:
    primary: inspect repositories and contribution paths
    secondary: open issue, discussion, or sponsorship path
  founder:
    primary: inspect products and product thesis
    secondary: partnership or collaboration
  personal-brand:
    primary: explore authored work and systems
    secondary: follow, read, or connect
  community:
    primary: find contribution and support paths
    secondary: join discussion or events
```

CTA labels must be specific. “Connect” is acceptable only when the nearby destination clarifies what kind of interaction is invited.

## Write Boundaries

This skill may recommend changes to identity metadata, pins, repository metadata, archive state, topics, or settings. It must not claim those changes were applied unless a capable write owner performs them and returns tool evidence.

Archive, privacy, pin, and profile-metadata writes require explicit approval because they affect public visibility or repository lifecycle.

## Ecosystem Acceptance

```text
□ scope is declared
□ observed state is separated from recommendations
□ README, pins, repositories, and CTA tell one story
□ public proof destinations are accessible or clearly marked otherwise
□ current pin state is verified or explicitly NOT_VERIFIED
□ recommended pins each have a proof role
□ repository metadata gaps are explicit
□ archive candidates are recommendations, never automatic destructive writes
□ optional enhancements pass the enhancement decision matrix
□ privacy and public-data implications are reported
```
