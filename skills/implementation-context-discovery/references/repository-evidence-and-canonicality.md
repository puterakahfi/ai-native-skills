# Repository Evidence and Canonicality

Load this reference before classifying a repository's implementation systems.

The goal is not to enumerate every installed package. The goal is to identify which implementation choices the repository currently treats as authoritative, which are bounded/local, which are being migrated, and which must not guide new work.

## Evidence hierarchy

```text
engineering contract / accepted ADR / explicit repository policy
  strongest declared authority

shared package, registry, composition root, token source, or wrapper
  strong intended reuse boundary

repeated current production imports and usage
  strong actual-practice evidence

framework and tool configuration
  strong setup evidence

package manifest
  declared direct dependency presence

lockfile
  resolved direct and transitive dependency presence

one isolated file or old screen
  weak canonicality evidence

package popularity, recency, or agent familiarity
  not repository evidence
```

No single source is automatically sufficient. Current repository authority and actual usage can disagree during migrations; record the conflict rather than averaging it away.

## Evidence inventory

```yaml
repository_evidence_inventory:
  repository_ref: <branch/commit/worktree>
  inspected_at: <timestamp>

  authority:
    engineering_contracts: []
    architecture_decisions: []
    migration_decisions: []
    ownership_files_or_policies: []

  workspace:
    manifests: []
    lockfiles: []
    workspace_config: []
    build_config: []
    lint_format_type_config: []
    test_story_example_config: []

  runtime_and_framework:
    framework_config: []
    entrypoints: []
    routing_and_composition_roots: []
    aliases: []

  component_and_style_system:
    component_registry_config: []
    shared_component_paths: []
    primitive_imports: []
    variant_utilities: []
    class_composition_utilities: []
    styling_config: []
    semantic_token_sources: []
    representative_imports: []

  icons_and_visual_assets:
    icon_packages_or_source: []
    icon_wrappers: []
    repeated_icon_imports: []
    deprecated_icon_paths: []

  application_tooling:
    state: []
    forms: []
    query_and_data_fetching: []
    validation: []
    animation: []
    tables_or_virtualization: []
    date_and_formatting: []

  legacy_and_migration:
    deprecated_paths: []
    legacy_dependencies: []
    migration_targets: []
    removal_or_replacement_issues: []

  unknowns_and_conflicts: []
```

## Source-copied component systems

Some component systems are installed by copying source into the repository instead of depending on a package with the system's name.

Evidence may include:

```text
registry configuration
shared `components/ui` or equivalent source
primitive-library imports
class-variance or variant definitions
class-name merge utility
semantic CSS variables
repeated product imports from the shared path
component-specific tests or stories
```

Do not conclude that no component system exists because the package manifest does not contain a package named after the design system.

## Canonicality statuses

### `canonical`

Use for the default accepted system for new work.

Evidence normally includes several of:

- explicit contract or ADR;
- shared ownership or registry;
- repeated current usage;
- stable import path;
- current configuration;
- no superseding migration decision.

### `accepted_but_local`

Use for a bounded solution accepted only inside one module, surface, or legacy boundary. It is not automatically reusable elsewhere.

### `migration_target`

Use for the approved future system that is not yet the universal implementation default.

A migration target requires a migration plan or approved slice before ordinary work may mix it into canonical areas.

### `legacy`

Use for still-operational but non-preferred implementation retained for compatibility or gradual removal.

### `deprecated`

Use when explicit evidence says new use is forbidden or removal is planned.

### `experimental`

Use for spikes, prototypes, branches, or bounded trials with no production authority.

### `transitive_only`

Use when a dependency appears in the lockfile through another package but is not an accepted direct implementation choice.

### `unknown`

Use when evidence is missing, conflicting, stale, or cannot establish authority.

`unknown` blocks irreversible or system-level decisions. It does not authorize the agent's preferred tool.

## Canonicality decision record

```yaml
canonicality_decision:
  capability_family: <component | styling | icons | state | forms | query | other>
  candidate: <system>
  status: <canonicality status>

  evidence:
    declared_dependency_or_source: []
    actual_usage: []
    repetition_or_shared_ownership: []
    repository_convention: []
    current_decision_authority: []
    migration_or_deprecation: []

  contradictions: []
  confidence: <high | medium | low>
  consequence_for_new_work: <preserve | bounded-use | migrate-by-approved-slice | do-not-use | unresolved>
```

## Conflict rules

### Manifest says A, current production says B

Inspect authority and migration history. Do not choose A merely because it is declared or B merely because it is frequent.

### Shared package uses A, one feature uses B

Normally classify A as canonical and B as accepted-local, experimental, legacy, or drift according to evidence.

### ADR selects B, most code still uses A

Classify B as `migration_target` unless the ADR explicitly makes B the immediate default and defines migration scope. Classify A as canonical-current or legacy according to the decision.

### Two systems are common and no authority exists

Return `unknown` or record bounded ownership by module. Do not silently declare both globally canonical.

### Package is popular and solves the problem better

Popularity is an alternative-selection signal only after a real capability gap is established. It is not canonicality evidence.

## Framework and library fixture: Next.js + React + shadcn/ui + Tailwind + Lucide

A product-specific adapter may discover:

```yaml
implementation_context_profile:
  application_framework:
    name: nextjs
    status: canonical
    evidence:
      - package manifest
      - framework configuration
      - app/router source structure

  ui_runtime:
    name: react
    status: canonical

  component_system:
    name: shadcn-ui
    status: canonical
    evidence:
      - components.json
      - shared component source
      - radix primitive imports
      - CVA variants
      - cn utility
      - repeated imports from the shared UI path

  styling_system:
    name: tailwindcss
    status: canonical
    token_strategy: semantic CSS variables

  iconography_implementation:
    name: lucide-react
    status: canonical
    forbidden_parallel_systems:
      - second icon family without approved migration or capability gap
```

This fixture is an example of discovered product evidence, not a universal preference embedded in the reusable contract.

## Completion check

Before implementation mapping:

- relevant capability families were inspected;
- package presence was separated from canonical status;
- source-copied systems were detected from repository evidence;
- current and migration-target systems were distinguished;
- legacy, deprecated, experimental, and transitive-only tooling was marked;
- authority conflicts and unknowns were recorded;
- every convention lock cites concrete paths, imports, configuration, or decisions.
