---
name: documentation-assurance
description: Facade skill for classifying documentation impact, mapping affected documents and owners, verifying implementation-to-document consistency and freshness, and producing an evidence-backed completion verdict without replacing the governing engineering lifecycle.
license: MIT
metadata:
  ai-native-skills.version: 1.0.0
  ai-native-skills.author: puterakahfi
  ai-native-skills.type: skill
  ai-native-skills.pattern: facade
  ai-native-skills.related_skills: '["product-requirements","adr","api-contract","content-strategy","onboarding","deployment-workflow","decision-provenance","task-continuity","code-review-workflow","product-development-workflow","new-feature-workflow","bugfix-workflow"]'
---

# Documentation Assurance

Documentation is part of a change when the change alters product intent, public behavior, architecture, contracts, setup, operations, support, release behavior, migration, deprecation, security, privacy, or user-facing guidance.

This facade owns documentation-impact classification, affected-document mapping, shared evidence rules, consistency verification, freshness assessment, normalized verdicts, blockers, and handoff. It does not own every document's content and never replaces the governing product, feature, bugfix, review, deployment, or maintenance lifecycle.

## Facade contract

```yaml
facade:
  capability: documentation_assurance
  owns:
    - documentation_impact_classification
    - affected_document_discovery_and_mapping
    - documentation_owner_and_reviewer_resolution
    - shared_consistency_and_freshness_rules
    - evidence_normalization
    - documentation_verdict
    - blocking_findings_and_handoff
  does_not_own:
    - product_scope_or_prd_authority
    - architecture_or_api_decisions
    - product_specific_document_locations
    - document_content_approval
    - release_merge_or_deployment_authorization
    - primary_lifecycle_routing
  built_in_strategies:
    - production_change_assessment
    - documentation_only_correction
    - release_and_operational_readiness
  extension_contract: product_or_domain_documentation_policy
  fallback_policy: fail_closed
  output_contract: documentation_assurance_report
```

## Trigger

Load when any of these apply:

- production code, configuration, schema, API, workflow, design, or product behavior changes;
- a PR, release, deployment, incident, or maintenance case needs documentation impact evidence;
- an existing document may be stale or contradictory;
- a user requests a documentation-only correction tied to a verified governing context;
- continuity or handoff must preserve affected documentation and unresolved documentation gates.

Do not load for explanation-only questions with no artifact or change assessment. Do not infer `NOT_APPLICABLE` from silence.

## Required inputs

```yaml
documentation_assurance_input:
  governing_workflow: string
  change_or_subject_ref: string
  objective_and_scope_refs: []
  implementation_or_action_evidence: []
  repository_or_product_context: []
  known_documentation_sources: []
  product_documentation_policy_refs: []
  release_or_operational_context: []
```

Missing governing scope, current implementation/action evidence, or repository documentation context yields `DOCUMENTATION_NOT_VERIFIED` for any material claim.

## Documentation domains

Classify each domain as `REQUIRED`, `NOT_APPLICABLE`, or `NOT_VERIFIED`:

```text
product requirements and accepted scope
architecture decisions and system boundaries
public API, schema, events, and compatibility contracts
package, SDK, CLI, and developer usage
user-facing help, onboarding, and product guidance
operator setup, deployment, configuration, and runbooks
support, troubleshooting, and incident knowledge
security, privacy, permissions, and data handling
release notes and changelog
migration, rollback, deprecation, and removal
```

Load `references/documentation-domains-and-evidence.md` when selecting domain owners, evidence, or consistency checks.

## Procedure

### Phase 1 — Establish governing context

1. Identify the primary workflow and exact change or subject.
2. Load approved scope, technical decisions, implementation/action evidence, and product documentation policy.
3. Distinguish planned, implemented, verified, reviewed, released, deployed, and observed behavior.
4. Record unavailable or conflicting sources as evidence gaps.

**Gate:** no impact verdict without attributable governing context.

### Phase 2 — Classify documentation impact

Assess every documentation domain against the actual change.

```text
behavior, contract, setup, operation, support, release, migration, or policy changed
  → DOCUMENTATION_REQUIRED

verified internal change with no changed external, operational, architectural,
contractual, support, release, migration, security, privacy, or user meaning
  → DOCUMENTATION_NOT_APPLICABLE

material impact or current source cannot be established
  → DOCUMENTATION_NOT_VERIFIED
```

`DOCUMENTATION_NOT_APPLICABLE` requires positive evidence describing why every plausible affected domain is unchanged.

### Phase 3 — Map affected documents

For each required document, record:

```yaml
affected_document:
  document_type: string
  current_source_ref: string
  change_reason: string
  owning_role: string
  producer_capability_or_product_owner: string
  reviewer_role: string
  required_before: implementation_complete | acceptance | release | deploy | case_close
  expected_evidence: []
  status: PLANNED | UPDATED | VERIFIED | BLOCKED | NOT_VERIFIED
```

The facade selects and hands off to document owners. It does not copy their specialist methodology into this skill.

### Phase 4 — Verify consistency and freshness

Compare documentation with:

- effective PRD and accepted scope;
- architecture and decision records;
- actual implementation, public contracts, supported commands, and configuration;
- test/runtime/rendered evidence appropriate to the claim;
- release and deployment behavior;
- actual operational behavior when the document is a runbook or incident artifact.

Check for:

```text
missing required document
stale behavior or command
contradictory source of truth
unsupported claim
unrecorded breaking change
missing migration/rollback/deprecation guidance
missing owner or reviewer
planned update represented as completed
```

Source changes alone do not prove user, runtime, deployment, or operational documentation correctness.

### Phase 5 — Produce verdict and gate handoff

Return one impact verdict plus one completion state.

Impact verdict:

```text
DOCUMENTATION_REQUIRED
DOCUMENTATION_NOT_APPLICABLE
DOCUMENTATION_NOT_VERIFIED
```

Completion state:

```text
PASS
NEEDS_WORK
BLOCKED
NOT_VERIFIED
NOT_APPLICABLE
```

Rules:

- `DOCUMENTATION_REQUIRED + PASS` requires every mapped required document to be updated, verified, reviewed where required, and evidenced.
- Any missing, stale, contradictory, unsupported, or unreviewed required document yields `NEEDS_WORK`, `BLOCKED`, or `NOT_VERIFIED`.
- `DOCUMENTATION_NOT_APPLICABLE` can pair only with `NOT_APPLICABLE` and explicit evidence.
- A document draft, issue, TODO, or plan is not update completion.
- Documentation PASS is not merge, release, deployment, or product acceptance authorization.

## Output contract

```yaml
documentation_assurance_report:
  governing_workflow: string
  subject_ref: string
  impact_verdict: DOCUMENTATION_REQUIRED | DOCUMENTATION_NOT_APPLICABLE | DOCUMENTATION_NOT_VERIFIED
  rationale: string
  domain_assessments:
    - domain: string
      status: REQUIRED | NOT_APPLICABLE | NOT_VERIFIED
      evidence_refs: []
      gaps: []
  affected_documents: []
  consistency_findings:
    - id: string
      severity: BLOCKING | WARNING
      observation: string
      evidence_refs: []
      impact: string
      correction_owner: string
  verification_evidence: []
  completion_state: PASS | NEEDS_WORK | BLOCKED | NOT_VERIFIED | NOT_APPLICABLE
  blocking_gaps: []
  required_reviewers: []
  next_eligible_action: string
```

## Lifecycle integration

```text
new-feature-workflow / bugfix-workflow
  assess during planning and verify before submission/review completion

code-review-workflow
  verify documentation impact and actual updated artifacts; do not author silently

product-development-workflow
  include documentation rows in Product Acceptance and release readiness

deployment-workflow
  verify operator, configuration, rollback, and runbook documentation when applicable

maintenance-case
  assess documentation drift and require closure evidence

task-continuity
  preserve documentation verdict, gaps, artifacts, and one next action
```

The governing workflow owns phase progression. This skill returns a gate result and handoff only.

## Hard gates

- [ ] Governing workflow, scope, and subject are explicit.
- [ ] Actual implementation or action evidence is distinguished from plans.
- [ ] Every documentation domain has an explicit applicability status.
- [ ] Silence never becomes `NOT_APPLICABLE`.
- [ ] Every required document has source, owner, producer, reviewer, deadline gate, and expected evidence.
- [ ] Documentation is compared with the actual implementation/action and effective decisions.
- [ ] Planned or drafted documentation is not represented as updated or verified.
- [ ] Stale, contradictory, unsupported, or missing required documentation blocks the dependent completion claim.
- [ ] Product-specific document content and approval remain product-owned.
- [ ] Documentation PASS does not synthesize merge, release, deployment, or product acceptance authority.

## Failure classifications

| Finding | Meaning | Result |
|---|---|---|
| `GOVERNING_CONTEXT_MISSING` | Scope or workflow cannot be established | `DOCUMENTATION_NOT_VERIFIED` |
| `DOCUMENT_SOURCE_MISSING` | Required source or target document cannot be located | `BLOCKED` or `NOT_VERIFIED` |
| `DOCUMENTATION_DRIFT` | Current document contradicts implementation or accepted decisions | `NEEDS_WORK` |
| `REQUIRED_DOCUMENT_MISSING` | Applicable document does not exist | `BLOCKED` |
| `UPDATE_NOT_VERIFIED` | Update is claimed without inspectable evidence | `NOT_VERIFIED` |
| `OWNER_OR_REVIEWER_MISSING` | Required ownership or independent review unavailable | `BLOCKED` or `NOT_VERIFIED` |
| `FALSE_NOT_APPLICABLE` | Material domain was silently or incorrectly excluded | `NEEDS_WORK` |
| `AUTHORITY_CONFLATION` | Documentation verdict treated as approval/authorization | `BLOCKED` |

## Handoff

```text
documentation-assurance
→ document owner produces or updates artifacts
→ documentation/domain reviewer verifies
→ governing workflow reconciles its completion or acceptance gate
→ task-continuity preserves unresolved state when work continues
```

## Capability evolution boundary

This MVP is an adapter-layer capability without a Core contract. Promote universal semantics only after verified real-product and real-maintenance evidence, compatibility analysis, and `skill-evolution` review.