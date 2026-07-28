---
name: package-development-workflow
description: Evidence-backed lifecycle for extracting, designing, testing, versioning, publishing, and proving independently consumable packages, libraries, SDKs, adapters, reusable UI, and shared configuration.
license: MIT
metadata:
  ai-native-skills.version: 0.1.0
  ai-native-skills.author: puterakahfi
  ai-native-skills.requires: "workflow-router role-switcher decision-provenance implementation-context-discovery domain-driven-design ports-and-adapters clean-architecture solid-design design-patterns api-contract test-driven-development architecture-review code-review-workflow"
  ai-native-skills.type: workflow
  ai-native-skills.implements: ai-native-core/contracts/workflows/package-development.contract.yaml
  ai-native-skills.contract-version: ^0.1.0
  ai-native-skills.skills: '{"required":["implementation-context-discovery","api-contract","test-driven-development","architecture-review","code-review-workflow","decision-provenance"],"optional":["domain-driven-design","ports-and-adapters","clean-architecture","solid-design","design-patterns"]}'
---

# Package Development Workflow

```text
intent and ownership
→ implementation context discovery
→ package boundary classification
→ domain and contract design
→ public API design
→ implementation with TDD
→ compatibility verification
→ package build
→ immutable publication
→ fresh external-consumer validation
→ adoption and migration evidence
→ architecture/code review
→ acceptance
```

## Use this workflow

Route here when the requested outcome is to create, extract, evolve, publish, or prove an independently consumable:

- contract or schema package;
- pure domain library;
- application/use-case package;
- SDK/client;
- infrastructure or framework adapter;
- reusable UI package;
- tooling or runtime configuration package.

Do not route a platform-local module here merely because its folder is named `packages`. A module that cannot be consumed independently without platform checkout, workspace topology, private source imports, or runtime coupling must be classified `platform_local_module_not_publishable` until its boundary changes.

## Hard gates

1. Read the issue, repository instructions, current implementation, manifests, tests, publication conventions, and overlapping capabilities before changing files.
2. State canonical owner, bounded context, intended consumers, non-goals, and acceptance authority.
3. Use interfaces/contracts at consumer boundaries. Domain/application code must not know frameworks, databases, providers, environment variables, or concrete adapters.
4. Adapters depend inward. The consuming application is the composition root and chooses adapters, secrets, environment mapping, routes, UI, and product policy.
5. DDD is required when material domain semantics exist; it is not ceremonial for configuration-only packages.
6. SOLID and design patterns require observed variation, substitution, responsibility, or change pressure. Otherwise record `NOT_APPLICABLE` or `NOT_JUSTIFIED`.
7. TDD requires RED-before-GREEN evidence or an attributable authorized exception. Green tests alone do not prove TDD.
8. Public exports, error semantics, dependencies, peer dependencies, optional dependencies, and deprecation policy must be explicit.
9. SemVer follows actual public API and behavior compatibility, not commit size.
10. Inspect the packed artifact. External consumers must not receive `workspace:*`, source imports, owner-repository paths, unpublished artifacts, submodules, or Turborepo requirements.
11. `PUBLICATION PASS` requires an actual immutable registry publish with version, digest/provenance, source commit, and install method.
12. `EXTERNAL_CONSUMER PASS` requires an actual fresh repository installation from the registry, documented imports only, typecheck, tests, build, representative behavior, and adapter substitution.
13. Keep source inspection, unit test, integration test, compatibility check, package build, publication, external installation, consumer build, review, and acceptance as separate evidence.
14. Never promote `NOT_RUN`, `INCOMPLETE`, source inspection, a monorepo build, or reviewer opinion into publication or consumer-proof `PASS`.

Load `references/package-boundaries-and-consumer-proof.md` for classification, dependency rules, status semantics, and forward-test details.

## Workflow record

```yaml
package_development:
  issue_ref: <issue>
  source_repository: <owner/repo>
  source_commit: <sha>
  canonical_owner: <team/repository>
  bounded_context: <name or not_applicable>
  classification: <supported classification>
  intended_consumers: []
  non_goals: []
  base_branch: <verified>
  pr_target: <verified>
  public_api:
    documented_exports: []
    compatibility_baseline: <version/ref>
    dependency_policy: []
  gates:
    source_inspection: <status + evidence>
    unit_test: <status + evidence>
    integration_test: <status + evidence>
    compatibility_check: <status + evidence>
    package_build: <status + evidence>
    publication: <status + evidence>
    external_installation: <status + evidence>
    consumer_build: <status + evidence>
    architecture_review: <status + evidence>
    code_review: <status + evidence>
    acceptance: <status + authority>
```

## Phase 1 — Intent and ownership

Resolve objective, issue, acceptance criteria, canonical meaning/implementation owner, consumers, bounded context, product policy boundary, repository topology, reviewers, write policy, and merge/publication authority.

**Block when:** ownership, issue, base branch, PR target, or acceptance authority is unknown.

## Phase 2 — Implementation-context discovery

Load `implementation-context-discovery`. Inspect repository instructions, current package/module implementation, workspace manifests, lockfiles, exports, build/test tooling, registry config, CI, generated files, contracts, existing skills, and known consumers.

Perform duplicate/overlap check. Reuse DDD, ports/adapters, Clean Architecture, SOLID, patterns, API-contract, TDD, and review capabilities; this workflow only coordinates package-specific lifecycle and evidence.

## Phase 3 — Boundary classification

Classify the candidate and decide `publishable`, `extractable_with_changes`, or `platform_local_module_not_publishable`.

Assess:

```text
semantic ownership
public API candidate
framework/provider/database/environment coupling
product-policy leakage
portable dependencies
consumer composition root
registry distribution feasibility
fresh-consumer feasibility
```

A partially portable validator with filesystem/repository assumptions is not a pure portable library. Split portable validation policy from repository/filesystem adapters or keep it local.

## Phase 4 — Domain and contract design

When semantics are material, use `domain-driven-design`, `ports-and-adapters`, `clean-architecture`, `solid-design`, and `api-contract` as applicable.

Required direction:

```text
consumer → documented public API
adapter → application/domain ports
application → domain/contracts
framework/provider/database/environment → adapter or application composition root only
```

For auth, forward-test this architecture:

```text
@pkahfi/auth-contracts
@pkahfi/auth-domain
@pkahfi/auth-application
@pkahfi/auth-adapter-clerk
@pkahfi/auth-adapter-authjs
@pkahfi/auth-adapter-jwt
@pkahfi/auth-nextjs
```

The app chooses adapter, secrets, environment mapping, routes, UI, and product authorization policy. Domain/application must not know Clerk, Auth.js, JWT implementation, Next.js, Redis, database, or environment variables.

## Phase 5 — Public API design

Define package entry points and documented exports. Prefer the smallest stable surface; keep internal modules unexported.

Record dependency policy:

- dependency: required at package runtime;
- peer dependency: consumer-provided framework/runtime contract, with supported range;
- optional dependency: capability is optional and failure behavior is explicit;
- dev dependency: build/test only and absent from consumer runtime.

For reusable React UI, React/framework packages belong in peer dependencies when the consumer owns them. Framework-specific behavior belongs in a framework adapter, not the reusable visual/domain core.

## Phase 6 — Implement with TDD

Write contract and behavior tests first, capture RED, implement minimum behavior, reach GREEN, refactor without widening the public API, and test supported adapter substitution.

Reject implicit environment reads inside adapters. Inject resolved configuration from the application composition root.

## Phase 7 — Compatibility verification

Compare documented exports, types, behavior, errors, peer ranges, configuration, and serialized contracts against the baseline.

```text
compatible fix → patch
backward-compatible addition → minor
breaking export/type/behavior/configuration change → major + migration/deprecation evidence
```

An SDK breaking public API change cannot be labeled patch/minor because internal tests pass.

## Phase 8 — Package build

Run the repository's actual pack/build commands. Inspect the produced archive/manifest for:

```text
public exports and type declarations
included files and source maps
runtime dependencies and peer ranges
workspace:* or file/link dependencies
owner-repository/source-path leakage
secrets and product-specific defaults
install scripts and platform assumptions
```

A successful monorepo build proves only `package_build` for that context.

## Phase 9 — Immutable publication

Publish an exact immutable version to the selected registry using authorized credentials. Record registry, package name, version, digest/integrity, source commit, timestamp, visibility, and read-only installation instructions.

When publish is not executed, status is `NOT_RUN`; do not claim published, releasable, or external-consumer accepted.

## Phase 10 — Fresh external-consumer validation

Use a new independent repository with no owner checkout or workspace linkage:

```text
fresh independent repository
→ authenticate using read-only registry token
→ install immutable package version
→ import only documented public exports
→ typecheck
→ run tests
→ build
→ exercise representative behavior
→ substitute an adapter without changing domain/application code
```

Prohibited prerequisites: owner checkout, monorepo workspace, `workspace:*`, Turborepo, source-path import, Git submodule, or unpublished local artifact.

A package that builds in its monorepo but fails registry installation or fresh consumer build is `FAIL` for external-consumer acceptance.

## Phase 11 — Adoption and migration

Record real consumer adoption separately from publication. Include migration steps, deprecation window, rollback path, supported version matrix, and unresolved product policy. Planned adoption is not executed adoption.

## Phase 12 — Review and acceptance

Run `architecture-review` and `code-review-workflow`. Review dependency direction, bounded context, public API stability, portability, evidence boundaries, compatibility, artifact contents, and unrelated changes.

Final `ACCEPTED` requires every required gate, authorized review, and explicit acceptance. It does not authorize merge, publication, or release unless the responsible authority separately grants it.

## Status discipline

```text
NOT_STARTED | IN_PROGRESS | BLOCKED | NOT_APPLICABLE | NOT_JUSTIFIED
NOT_RUN | INCOMPLETE | FAIL | PASS | ACCEPTED
```

Always attach the evidence command/output/ref and tested commit to a `PASS`. Keep publication and external-consumer proof independent.
