# Capability Discovery

`ai-native-skills` distinguishes **what an executable artifact is** from **where and when it is useful**.

- `metadata["ai-native-skills.type"]` remains the canonical executable type: `skill`, `workflow`, or `meta-skill`.
- [`capability-inventory.json`](capability-inventory.json) remains the generated list of executable entry points.
- [`../catalog/capability-discovery/manifest.json`](../catalog/capability-discovery/manifest.json) is the repository-curated discovery projection for product/runtime consumers.

The discovery catalog is intended for questions such as:

- Which workflow and skills should I use for product planning?
- Which capabilities should be loaded to build high-quality code?
- Which workflows and skills cover security design, review, release, and incident response?
- Which capabilities apply during `discover`, `build`, `verify`, or `operate`?
- Which entries belong to Product Development, Engineering, Security, Quality, Design, Operations, or AI Systems?

## Why type is not category

The executable type answers a structural question:

| Type | Question |
|---|---|
| `workflow` | Which lifecycle owns the ordered phases and gates? |
| `meta-skill` | Which router or composer selects other capabilities? |
| `skill` | Which focused capability performs the current concern? |

Discovery facets answer different questions:

| Facet | Question |
|---|---|
| `domains` | Which area of work does this capability support? |
| `lifecycle_stages` | During which phases can it be useful? |
| `concerns` | Which narrower problem or quality dimension does it address? |
| `job_profiles` | Which workflow routes and capability groups solve a common job? |

A capability may belong to several domains, lifecycle stages, and concerns. For example, `security-review` belongs to Engineering, Quality, and Security and is relevant during design, build, verification, and operation. Do not collapse these independent dimensions into one category string.

## Machine-readable contract

The manifest at `catalog/capability-discovery/manifest.json` points to three versioned files:

```text
facets.json
  domain, lifecycle-stage, and concern definitions

classifications.json
  complete executable capability coverage through groups, defaults, and overrides

job-profiles.json
  curated workflow routes, required/optional capability groups, evidence, and completion gates
```

Each executable capability must be assigned exactly once to a classification group. Defaults define the common facets for the group; an override changes only the facets that differ for one capability.

The catalog is validated against `docs/capability-inventory.json`, so stale names, missing entries, duplicate assignments, invalid facet values, invalid workflow references, and missing required job profiles fail closed.

Validate locally:

```bash
python3 scripts/verify-capability-inventory.py
python3 scripts/verify-capability-discovery.py
```

## Job profiles

Job profiles are curated starting points. They do not replace `workflow-router`, repository evidence, active issue acceptance criteria, or phase-specific routing.

### Product Planning

Primary routes:

- `product-development-workflow` for discovery through release and learning.
- `spec-workflow` after the opportunity is accepted and needs precise implementation planning.

Core capability groups:

1. Route and ownership: `workflow-router`, `role-switcher`, `product-development-workflow`, `product-manager`.
2. Value and assumption validation: `business-value-alignment`, `user-research`, `experiment-design`.
3. Requirements and topology: `product-requirements`, `delivery-work-breakdown`, `decision-provenance`, `spec-workflow`.

Use this profile to avoid jumping from an idea directly into implementation.

### Engineering Quality

Workflow selection depends on the job:

- `new-feature-workflow` for approved new behavior.
- `bugfix-workflow` for broken or regressed existing behavior.
- `code-review-workflow` for an evidence-backed merge-readiness verdict.

Core capability groups:

1. Repository and ownership: `workflow-router`, `role-switcher`, `master-engineer`, `implementation-context-discovery`.
2. Build quality: `test-driven-development`, plus applicable architecture and contract skills.
3. Independent verification: `architecture-review`, `code-review-workflow`, `security-review`, `skill-eval`, with debugging, refactoring, performance, or debt skills loaded only when relevant.

Use this profile to preserve repository conventions, test accepted behavior, and keep implementation completion separate from independent review and merge authorization.

### Security Engineering

Security does not have one universal lifecycle. Select the workflow from the current job:

- `new-feature-workflow` for a new or materially changed security-sensitive capability.
- `code-review-workflow` for security review and merge readiness.
- `bugfix-workflow` for a confirmed vulnerability or regression.
- `deployment-workflow` for controlled release, runtime verification, and rollback.

Core capability groups:

1. Authority and threat boundary: `decision-provenance`, `security-engineer`, `threat-modeling`.
2. Secure design and implementation: `implementation-context-discovery`, with `api-contract`, data, architecture, testing, and resilience capabilities loaded when applicable.
3. Independent review and operation: `architecture-review`, `security-review`, `code-review-workflow`, with deployment, observability, resilience, and incident capabilities when the risk reaches runtime.

Use this profile to connect threats to architecture, implementation, independent verification, release ownership, and operational response.

## Consumer guidance

A product such as `pkahfi.com/ai-skills` should consume the inventory and discovery manifest together:

1. Read `docs/capability-inventory.json` for executable identity, type, and path.
2. Read the discovery manifest and its three files for domain, lifecycle, concern, and job-profile discovery.
3. Resolve each classification by applying its group defaults and then its named override.
4. Join entries by exact capability `name`.
5. Present `type` and discovery facets as independent filters.
6. Route broad job intent through `job_profiles` or `workflow-router` before exposing a long atomic-skill list.
7. Treat a job profile as a curated default, not proof that every listed optional capability must be loaded.
8. Keep workflow order and quality gates in the executable `SKILL.md`; the discovery catalog is an index, not a duplicate workflow implementation.

Recommended UI hierarchy:

```text
Start by job
  Product Planning
  Engineering Quality
  Security Engineering

Browse by domain
  Product Development
  Engineering
  Experience Design
  Quality & Verification
  Security
  Operations & Reliability
  AI & Agent Systems
  Governance & Delivery
  Developer Experience

Narrow by
  Type
  Lifecycle stage
  Concern
```

## Change policy

When adding, renaming, deleting, or materially repurposing a capability:

1. update the executable `SKILL.md`;
2. regenerate and validate `capability-inventory.json` when identity or type changes;
3. update the capability's domain, lifecycle-stage, and concern classification;
4. update affected job profiles only when the recommended composition or workflow boundary changes;
5. run both validators;
6. update downstream consumers through their own issue, implementation mapping, and acceptance gates.

Do not add a new executable type to represent a domain, job, platform, role, adapter, or reviewer pattern. Those remain separate facets or patterns unless the official taxonomy, validation, documentation, and consumers are intentionally changed together.
