# Repository Evidence and Canonicality

Load this reference before classifying repository implementation systems.

The goal is not to enumerate every installed package. Identify which choices are authoritative, bounded/local, migration targets, legacy, deprecated, experimental, transitive-only, or unknown.

## Evidence hierarchy

```text
engineering contract / accepted ADR / explicit policy
  strongest declared authority

shared package, component registry, token source, or wrapper
  strong intended reuse boundary

repeated current production imports and usage
  strong actual-practice evidence

component source, exports, variants, stories, and tests
  strong capability-availability evidence

framework and tool configuration
  strong setup evidence

package manifest and lockfile
  dependency-presence evidence only

isolated file, old screen, popularity, recency, or agent familiarity
  weak or invalid canonicality evidence
```

No single source is automatically sufficient. Record authority and actual-practice conflicts instead of averaging them away.

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
    canonical_registry_sources: []
    shared_component_paths_and_exports: []
    component_source_files: []
    primitive_imports: []
    variant_definitions: []
    class_composition_utilities: []
    component_stories_examples_and_tests: []
    representative_component_imports: []
    local_customizations_and_owners: []
    styling_config: []
    semantic_token_sources: []

  typography:
    font_loaders_and_variables: []
    semantic_role_tokens_or_utilities: []
    heading_and_text_components: []
    representative_role_usage: []
    responsive_type_behavior: []
    theme_behavior: []

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

Some systems are copied into repository source instead of installed through a marketing-name package.

Evidence may include:

```text
registry configuration
shared components/ui or equivalent source
primitive imports
variant definitions and CVA
class-name merge utility
semantic CSS variables
repeated imports from shared paths
component stories, examples, tests, and ownership
```

Do not conclude that no component system exists because the manifest lacks its marketing name.

Do not conclude that every upstream component is locally available. Separate:

```text
system is canonical
component is installed locally
variant is available locally
component is available from the canonical registry
component is locally customized
```

## Canonicality statuses

### `canonical`

Default accepted system for new work. Evidence normally combines declared authority, shared ownership or registry, repeated current usage, stable import paths, current configuration, and no superseding migration decision.

### `accepted_but_local`

A bounded solution accepted only within one module, surface, or legacy boundary.

### `migration_target`

Approved future system that is not yet the universal default. It requires an approved migration slice before ordinary work mixes it with current conventions.

### `legacy`

Still operational but non-preferred implementation retained for compatibility or gradual removal.

### `deprecated`

Explicit evidence forbids new use or plans removal.

### `experimental`

Spike, prototype, branch, or bounded trial with no production authority.

### `transitive_only`

Present through another dependency but not an accepted direct implementation choice.

### `unknown`

Evidence is missing, conflicting, stale, or insufficient. Unknown blocks confident system-level decisions.

## Canonicality record

```yaml
canonicality_decision:
  capability_family: <component | typography | styling | icons | state | forms | query | other>
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

- Manifest says A, production says B: inspect authority and migration history.
- Shared package uses A, one feature uses B: A is normally canonical; classify B by evidence.
- ADR selects B, most code uses A: B may be a migration target rather than current default.
- Two systems are common with no authority: return unknown or bounded ownership.
- A popular package appears better: popularity matters only after a real capability gap exists.

## Fixture: Next.js + React + shadcn/ui + Tailwind + Lucide

A product adapter may discover:

```yaml
implementation_context_profile:
  application_framework:
    name: nextjs
    status: canonical
  ui_runtime:
    name: react
    status: canonical
  component_system:
    name: shadcn-ui
    status: canonical
    evidence:
      - components.json
      - shared source components
      - Radix primitive imports
      - CVA variants
      - cn utility
      - semantic CSS variables
      - repeated production imports
  styling_system:
    name: tailwindcss
    status: canonical
    token_strategy: semantic CSS variables
  iconography_implementation:
    name: lucide-react
    status: canonical
```

This is an evidence fixture, not a reusable preference.

The next step must still inventory actual components, variants, registry availability, typography roles, and requested capability coverage.

## Completion check

Before implementation mapping:

- relevant capability families were inspected;
- package presence was separated from canonical status;
- source-copied systems were detected;
- actual component exports, variants, stories/examples, and usage were inventoried;
- canonical registry availability was identified when material;
- typography families and semantic roles were evidenced;
- current and migration-target systems were distinguished;
- legacy, deprecated, experimental, and transitive-only tooling was marked;
- authority conflicts and unknowns were recorded;
- every convention lock cites paths, imports, configuration, usage, or decisions.