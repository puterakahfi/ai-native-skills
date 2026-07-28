# Package Boundaries and Consumer Proof

## Classification matrix

| Classification | Owns | Must remain outside |
|---|---|---|
| Contract/schema package | Stable messages, types, schemas, compatibility semantics | Runtime implementation, product policy |
| Pure domain library | Domain model, invariants, value objects, domain services | Framework, database, provider, environment |
| Application/use-case package | Use cases and ports coordinating domain behavior | Concrete adapters and composition root |
| SDK/client | Stable consumer API over a remote/system contract | Product secrets and server policy |
| Infrastructure adapter | Concrete implementation of inward-facing ports | Domain ownership and product authorization policy |
| Framework adapter | Framework-specific wiring, routes, lifecycle integration | Framework-neutral domain/application behavior |
| Reusable UI | Components, documented props/events, accessibility contract | Product-only workflow/policy; consumer-owned framework runtime when peer dependency applies |
| Tooling configuration | Build/lint/test/type policy shared by compatible repositories | Runtime secrets and product-specific deployment policy |
| Runtime configuration | Typed runtime configuration contract and explicit mapping boundary | Implicit environment reads inside domain/application |
| Platform-local module | Platform-owned behavior that cannot currently be consumed independently | Misleading publication or portability claims |

## Publishability decision

A candidate is publishable only when canonical ownership, public API, dependency direction, versioning, distribution, and independent consumer behavior are explicit. Folder location, `package.json`, or a successful workspace build is insufficient.

Use this decision order:

```text
keep product-local when policy is product-specific
→ keep platform-local when orchestration/runtime state is platform-owned
→ split portable policy/contracts from filesystem/framework/provider adapters
→ publish only the independently consumable boundary
```

## Dependency and configuration rules

- Domain and application code depend on owned interfaces, not concrete infrastructure.
- Adapters implement ports and receive configuration through constructors/factories.
- Environment parsing belongs to the consuming application's composition root or a dedicated framework/runtime adapter.
- Product authorization policy remains in the application/product repository.
- `workspace:*`, `file:`, local links, source-path imports, owner checkout, submodules, and Turborepo knowledge are prohibited in the external consumer proof.
- Hardcoded product, owner, repository, registry, or provider values are portability failures unless they are the package's explicit canonical identity.

## Public API and compatibility

Review all externally observable surfaces:

```text
exports and subpath exports
types, generics, interfaces, errors
runtime behavior and defaults
configuration fields and environment mapping contract
serialized schemas and wire formats
peer dependency ranges
adapter registration and substitution behavior
```

Breaking any supported consumer surface requires a major release for stable packages, plus migration and deprecation evidence where applicable. Internal refactoring that preserves the public surface does not require a major release.

## Evidence ledger

| Evidence | What it proves | What it does not prove |
|---|---|---|
| Source inspection | Static boundaries and declarations observed | Executed behavior |
| Unit tests | Isolated tested behavior | Registry distribution or consumer integration |
| Integration tests | Exercised integration in tested environment | Fresh external installation |
| Compatibility check | Compared API/behavior surface | Publication or adoption |
| Package build/pack | Artifact can be constructed and inspected | Registry publication or independent installation |
| Registry publication | Exact immutable version exists with provenance | Consumer build or representative behavior |
| External installation | Fresh repo can resolve/install exact version | Typecheck/test/build unless run |
| Consumer build | Fresh consumer typechecks/tests/builds | Adapter substitution unless exercised |
| Review | Independent assessment | Acceptance or merge authority |
| Acceptance | Authorized lifecycle result | Merge, release, or publication authority unless explicitly included |

## External-consumer proof record

```yaml
external_consumer_proof:
  repository: <fresh independent repo/ref>
  package: <registry/name>
  version: <exact immutable version>
  registry_visibility: <public|private>
  authentication: <read-only token mechanism; never secret value>
  owner_repository_checkout: false
  workspace_protocol: false
  turborepo_required: false
  source_imports: false
  git_submodule: false
  unpublished_local_artifact: false
  documented_exports_used: []
  commands:
    install: <command + output ref>
    typecheck: <command + output ref>
    test: <command + output ref>
    build: <command + output ref>
    behavior: <command/scenario + output ref>
    adapter_substitution: <command/scenario + output ref>
  tested_source_commit: <sha>
  result: <NOT_RUN|INCOMPLETE|FAIL|PASS>
  gaps: []
```

Private registries satisfy the same proof. Authentication evidence records the mechanism and successful read-only resolution without exposing credentials.

## Auth forward-test

Expected packages:

```text
@pkahfi/auth-contracts
@pkahfi/auth-domain
@pkahfi/auth-application
@pkahfi/auth-adapter-clerk
@pkahfi/auth-adapter-authjs
@pkahfi/auth-adapter-jwt
@pkahfi/auth-nextjs
```

Required boundary:

```text
auth-contracts: shared types and port contracts
auth-domain: identities, sessions, authorization-neutral invariants
auth-application: use cases depending on contracts/domain ports
provider adapters: Clerk/Auth.js/JWT implementation details
nextjs adapter: framework routing/session integration
application: composition root, secrets, env mapping, routes, UI, product authorization policy
```

Substitution proof must replace Clerk/Auth.js/JWT wiring without changing `auth-domain` or `auth-application` source.

## Failure examples

- A validator is only partially portable when core rules are framework-neutral but it reads repository paths/filesystem implicitly. Split the portable validation engine from repository/filesystem ports and adapters.
- A React UI package must declare compatible React/framework peer dependency ranges and keep framework-specific routing/data behavior in an adapter.
- An SDK removing or changing a documented method is a breaking public API change even when repository tests are green.
- A package that builds through monorepo aliases but fails exact registry installation in a fresh repository fails external-consumer acceptance.
