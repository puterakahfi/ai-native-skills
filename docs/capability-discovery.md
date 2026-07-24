# Capability Discovery

`ai-native-skills` distinguishes **what an executable artifact is** from **where, when, and how people discover it**.

- `metadata["ai-native-skills.type"]` remains the canonical executable type: `skill`, `workflow`, or `meta-skill`.
- [`capability-inventory.json`](capability-inventory.json) remains the generated list of executable entry points.
- [`../catalog/capability-discovery/manifest.json`](../catalog/capability-discovery/manifest.json) is the repository-curated discovery projection for product/runtime consumers.

The discovery catalog answers questions such as:

- Which workflow and skills should I use for product planning?
- Which capabilities should be loaded to build high-quality code?
- Which workflows and skills cover security design, review, release, and incident response?
- Which capabilities apply during `discover`, `build`, `verify`, or `operate`?
- Which capabilities belong to Growth & Marketing or AI & Agent Systems?
- Which capabilities are relevant to Web, GitHub, ChatGPT Apps, or an AI agent runtime?
- Which curated topic is the best browse entry point for this intent?

## Why type is not category

The executable type answers a structural question:

| Type | Question |
|---|---|
| `workflow` | Which lifecycle owns the ordered phases and gates? |
| `meta-skill` | Which router or composer selects other capabilities? |
| `skill` | Which focused capability performs the current concern? |

Discovery dimensions answer different questions:

| Dimension | Question | Semantics |
|---|---|---|
| `domains` | Who primarily owns or practices this capability? | Canonical, many-to-many, ownership-oriented |
| `lifecycle_stages` | During which phases can it be useful? | Canonical, many-to-many |
| `concerns` | Which narrower problem or quality dimension does it address? | Canonical, cross-cutting |
| `ecosystems` | Which technology, platform, or runtime context does it support? | Canonical, context-oriented |
| `topics` | In which curated browse collection should people find it? | Editorial, overlapping, navigation-oriented |
| `job_profiles` | Which workflow routes and capability groups solve a common job? | Opinionated execution composition |

A capability can appear in several dimensions. Do not collapse them into one category string.

```text
domain
  primary ownership or discipline

concern
  cross-cutting problem or quality

ecosystem
  technology/platform/runtime context

topic
  curated browse collection

job profile
  workflow-aware execution recommendation
```

`topics` intentionally follow the useful part of topic directories such as `skills.sh`: a capability can appear in several browse collections. Topics do not replace canonical facets and do not determine execution order.

## Machine-readable contract

Schema version 2 contains four files:

```text
facets.json
  domain, lifecycle-stage, concern, and ecosystem definitions

classifications.json
  complete executable capability coverage through groups, defaults, and overrides

topics.json
  curated overlapping browse collections with recommended starting points

job-profiles.json
  workflow routes, required/optional capability groups, evidence, and completion gates
```

Each executable capability must be assigned exactly once to a classification group. Defaults define common facets; an override changes only the values that differ.

Non-workflow capabilities should use no more than three primary domains. A broader assignment requires an explicit `cross_cutting_reason`. Workflows are exempt because their lifecycle ownership can legitimately span several disciplines.

The catalog is validated against `docs/capability-inventory.json`. Stale names, missing entries, duplicate assignments, invalid facet values, topic reference drift, invalid workflow references, excessive unexplained domain breadth, and missing required topics or job profiles fail closed.

Validate locally:

```bash
python3 scripts/verify-capability-inventory.py
python3 scripts/verify-capability-discovery.py
```

## Canonical domains

The current primary domains are:

- Product Development
- Engineering
- Experience Design
- Quality & Verification
- Security
- Operations & Reliability
- AI & Agent Systems
- Growth & Marketing
- Governance
- Developer Experience

Domain assignment is intentionally narrower than topic membership. For example, `code-review-workflow` is primarily Engineering, Quality, and Governance; security remains a concern and the workflow is still discoverable through the Security Engineering topic and profile.

## Ecosystems

Ecosystems remain separate from domains:

- `technology-agnostic`
- `web`
- `github`
- `chatgpt-apps`
- `ai-agent-runtime`

Do not represent React, Next.js, mobile, databases, or another platform until repository capabilities provide verified coverage for that context. Add ecosystem values with the capabilities and validation evidence that justify them.

## Topics

Initial curated topics:

- Product Management
- Software Architecture
- Engineering Quality
- Security Engineering
- Design & UI
- Agent Workflows
- AI & Agent Systems
- Operations & Reliability
- Developer Experience
- Growth & Marketing

Each topic declares:

- a stable identifier and label;
- a concise browse description;
- one or more recommended starting points;
- a many-to-many capability list.

Topic membership is editorial. It can evolve without changing executable type, canonical workflow procedure, or primary ownership.

## Job profiles

Job profiles are workflow-aware starting points. They do not replace `workflow-router`, repository evidence, active issue acceptance criteria, or phase-specific routing.

### Product Planning

Primary routes:

- `product-development-workflow` for discovery through release and learning.
- `spec-workflow` after the opportunity is accepted and needs precise implementation planning.

Core capability groups:

1. Route and ownership: `workflow-router`, `role-switcher`, `product-development-workflow`, `product-manager`.
2. Value and assumption validation: `business-value-alignment`, `user-research`, `experiment-design`.
3. Requirements and topology: `product-requirements`, `delivery-work-breakdown`, `decision-provenance`, `spec-workflow`.

### Engineering Quality

Workflow selection depends on the job:

- `new-feature-workflow` for approved new behavior.
- `bugfix-workflow` for broken or regressed existing behavior.
- `code-review-workflow` for an evidence-backed merge-readiness verdict.

Independent verification remains separate from implementation ownership.

### Security Engineering

Security does not have one universal lifecycle. Select the workflow from the current job:

- `new-feature-workflow` for a new or materially changed security-sensitive capability.
- `code-review-workflow` for security review and merge readiness.
- `bugfix-workflow` for a confirmed vulnerability or regression.
- `deployment-workflow` for controlled release, runtime verification, and rollback.

Security workflows can be found through the Security Engineering topic/profile even when Security is a concern rather than their primary ownership domain.

## Consumer guidance

A product such as `pkahfi.com/ai-skills` should consume the inventory and discovery manifest together:

1. Read `docs/capability-inventory.json` for executable identity, type, and path.
2. Read the discovery manifest and all four catalog files.
3. Resolve each classification by applying its group defaults and then its named override.
4. Join entries by exact capability `name`.
5. Present executable `type`, canonical facets, topics, and job profiles as distinct concepts.
6. Use topics for broad browse entry points.
7. Use domain, lifecycle, concern, and ecosystem for composable narrowing.
8. Route broad execution intent through job profiles or `workflow-router`.
9. Keep workflow order and quality gates in executable `SKILL.md`; the discovery catalog is an index, not duplicate implementation.

Recommended UI hierarchy:

```text
Start by job
  Product Planning
  Engineering Quality
  Security Engineering

Browse by topic
  Product Management
  Software Architecture
  Engineering Quality
  Security Engineering
  Design & UI
  Agent Workflows
  AI & Agent Systems
  Operations & Reliability
  Developer Experience
  Growth & Marketing

Narrow by
  Type
  Domain
  Lifecycle stage
  Concern
  Ecosystem
```

## Change policy

When adding, renaming, deleting, or materially repurposing a capability:

1. update the executable `SKILL.md`;
2. regenerate and validate `capability-inventory.json` when identity or type changes;
3. update domain, lifecycle-stage, concern, and ecosystem classification;
4. update topics when browse membership or starting points change;
5. update job profiles only when recommended composition or workflow boundaries change;
6. run both validators and fail-closed regressions;
7. update downstream consumers through their own issue, implementation mapping, and acceptance gates.

Do not add a new executable type to represent a domain, topic, ecosystem, job, platform, role, adapter, or reviewer pattern.
