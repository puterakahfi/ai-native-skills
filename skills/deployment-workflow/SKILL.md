---
name: deployment-workflow
description: Evidence-backed deployment workflow — identify an immutable candidate, verify technical readiness, resolve environment context and deployment authority, execute the exact authorized artifact, verify deployed health, then explicitly confirm or roll back.
license: MIT
metadata:
  ai-native-skills.version: 2.0.0
  ai-native-skills.author: puterakahfi
  ai-native-skills.requires: "decision-provenance context-manager security-review code-review-workflow observability-design resilience-engineering master-engineer"
  ai-native-skills.type: workflow
  ai-native-skills.implements: ai-native-core/contracts/workflows/deployment.contract.yaml
  ai-native-skills.contract-version: "~0.2"
  ai-native-skills.skill_load_order: '[{"phase":"pre-deploy-check","load":["security-review","architecture-review","code-review-workflow","decision-provenance"]},{"phase":"context-load","load":["context-manager","observability-design","resilience-engineering"]},{"phase":"authorize-deploy","load":["decision-provenance"]},{"phase":"deploy","load":["master-engineer"]},{"phase":"verify-deploy","load":["observability-design","resilience-engineering"]},{"phase":"rollback-or-confirm","load":["decision-provenance","resilience-engineering","incident-response"]}]'
  ai-native-skills.skills: '{"required":["decision-provenance","context-manager","security-review","code-review-workflow","observability-design"],"optional":["architecture-review","resilience-engineering","master-engineer","incident-response"]}'
---

# Deployment Workflow

Identify candidate → verify technical readiness → load environment context → authorize exact side effect → deploy exact artifact → verify actual environment → confirm or roll back.

## Core boundary

```text
technically READY
≠ authorized to deploy

authorized to deploy
≠ successfully executed

provider deployment success
≠ application HEALTHY

HEALTHY
≠ confirmed when confirmation authority is required
```

The workflow owns deployment lifecycle, records, gates, and operational handoffs. Product adapters own provider commands, protected-environment policy, authorization authority, secret management, health checks, verification windows, rollback mechanisms, and emergency procedures.

## Hard rules

```text
1. Identify an immutable release candidate before readiness or authorization.
2. Mutable branch names, latest tags, or unpinned artifacts are not sufficient candidate identity.
3. All readiness evidence must refer to the exact candidate that will be deployed.
4. Technical readiness never implies deployment authorization.
5. Resolve target environment, scope, operator, window, rollback, and observability before the side effect.
6. Material authorization claims require decision-provenance.
7. Agent summaries, PR bodies, commits, and CI status are not deployment authorization.
8. Authorization must cover the exact candidate, environment, action, scope, and applicable time boundary.
9. Recheck authorization immediately before deployment.
10. Candidate or environment changes invalidate stale readiness/authorization.
11. Execute only the authorized candidate/environment pair.
12. Capture provider deployment ID and actual deployed artifact identity.
13. Verify the deployed environment directly; local/CI evidence is not post-deploy health evidence.
14. Provider success alone cannot confirm application health.
15. Missing health evidence is NOT_VERIFIED, not success.
16. Healthy, degraded, and not-verified states must remain distinct.
17. Confirmation and rollback follow evidence, policy, and decision authority.
18. Pre-authorized emergency rollback may execute immediately when its conditions apply.
19. Rollback success requires an execution record and post-action health evidence or an explicit gap.
20. Every run ends with CONFIRMED, ROLLED_BACK, ROLLBACK_REQUIRED, or OUTCOME_BLOCKED.
```

## When to use

Use for staging, production, preview, canary, regional, internal, customer, data-processing, or other deployment environments when a release candidate will cause an external side effect.

```text
release preparation only, no environment side effect
  → product-development-workflow release phase or git-workflow

code/feature acceptance before merge
  → code-review-workflow or new-feature-workflow

incident already active
  → incident-response, optionally invoking this workflow for rollback/redeploy
```

Do not assume staging is always unprotected or production is the only environment requiring authorization.

## Required context

```yaml
deployment_input:
  candidate:
    candidate_id: <stable id>
    source_ref: <commit/release/build>
    immutable_artifact_identity: <digest or immutable artifact id>
    approved_scope: []
    acceptance_or_release_readiness_ref: <reference or N/A>
    code_review_verdict_ref: <reference>
    security_review_ref: <reference or N/A>

  target_environment: <environment>
  deployment_provider: <provider/mechanism>
  approval_policy: <reference>
  protected_environment_policy: <reference>
  change_window: <window or N/A>
  deploy_operator_or_automation: <identity>

  configuration_policy: <reference>
  secret_management: <reference>
  observability_sources: []
  health_checks: []
  smoke_tests: []
  key_flows: []
  verification_window: <window>

  rollback_target: <candidate/deployment>
  rollback_mechanism: <mechanism>
  emergency_rollback_policy: <reference or N/A>
  confirmation_owner: <owner/policy>
  rollback_owner: <owner/policy>

  decision_sources: []
  required_authorities: []
  previous_decision_records: []
```

Unknown required context remains a blocker. Do not fabricate artifact identities, approvals, provider IDs, environment evidence, or rollback outcomes.

## Canonical flow

```text
1  PRE-DEPLOY CHECK
   identify exact candidate
   verify tests, review, security, acceptance/readiness, configuration,
   rollback readiness, and health-verification plan
   → READY | NOT_READY

2  CONTEXT LOAD
   resolve environment, provider, config/secrets policy, observability,
   verification window, rollback, owners, and change window

3  AUTHORIZE DEPLOY
   decision-provenance verifies exact candidate + environment + action + scope
   → AUTHORIZED | NOT_AUTHORIZED | ROUTE_FOR_APPROVAL

4  DEPLOY
   recheck candidate, environment, and authorization immediately before side effect
   execute product-defined mechanism
   capture deployment ID and actual artifact identity
   → EXECUTED | FAILED | NOT_RUN

5  VERIFY DEPLOY
   observe actual deployment/environment
   run health, smoke, key-flow, logs/errors, dependencies,
   migration/data, and SLO checks when applicable
   → HEALTHY | DEGRADED | NOT_VERIFIED

6  ROLLBACK OR CONFIRM
   HEALTHY → confirm when permitted
   DEGRADED → execute or route rollback according to policy
   NOT_VERIFIED → continue bounded observation or block outcome
   → CONFIRMED | ROLLED_BACK | ROLLBACK_REQUIRED | OUTCOME_BLOCKED
```

## Phase 1 — Technical readiness

Load:

```text
security-review
architecture-review when applicable
code-review-workflow
resilience-engineering when rollback/failure-mode review is needed
decision-provenance for claims about approved candidate or accepted operational risk
```

Required output:

```yaml
technical_readiness_report:
  candidate_id: <id>
  artifact_identity: <identity>
  tests_and_ci: <PASS | FAIL | NOT_VERIFIED>
  code_review: <APPROVED | REQUEST_CHANGES | BLOCKED | NOT_VERIFIED>
  security: <PASS | FAIL | NOT_VERIFIED | NOT_APPLICABLE>
  architecture: <PASS | FAIL | NOT_VERIFIED | NOT_APPLICABLE>
  acceptance_or_release_readiness: <PASS | FAIL | NOT_VERIFIED | NOT_APPLICABLE>
  configuration_and_secrets: <PASS | FAIL | NOT_VERIFIED>
  rollback_readiness: <PASS | FAIL | NOT_VERIFIED>
  health_verification_plan: <reference>
  blockers: []
  status: <READY | NOT_READY>
```

`READY` means technical eligibility only.

## Phase 2–6 details

Load:

```text
references/authorization-verification-and-outcome.md
```

That reference owns:

- immutable candidate and environment matching;
- deployment context schema;
- provenance-backed authorization;
- execution record;
- direct environment evidence;
- confirm/rollback decisions;
- emergency rollback boundary;
- final outcome record.

## Gate transitions

```text
NOT_READY
  → return to release/implementation/review/context owner

READY + NOT_AUTHORIZED
  → stop; no side effect

READY + ROUTE_FOR_APPROVAL
  → route to required authority; preserve candidate identity

READY + AUTHORIZED
  → recheck candidate/environment/authorization
  → deploy exact pair

execution FAILED
  → record failure
  → route incident/operational recovery as applicable

HEALTHY
  → confirmation gate

DEGRADED
  → rollback policy gate

NOT_VERIFIED
  → OUTCOME_BLOCKED unless bounded observation/evidence plan remains active
```

## Required outputs

```text
technical_readiness_report
deployment_context
deployment_authorization_record
deployment_execution_record
deployment_verification_report
deployment_outcome_record
```

Final report:

```yaml
deployment_summary:
  candidate_id: <id>
  artifact_identity: <identity>
  environment: <environment>
  technical_readiness: <READY | NOT_READY>
  deployment_authorization: <AUTHORIZED | NOT_AUTHORIZED | ROUTE_FOR_APPROVAL>
  deployment_id: <id or null>
  execution_status: <EXECUTED | FAILED | NOT_RUN>
  verification_status: <HEALTHY | DEGRADED | NOT_VERIFIED | N/A>
  outcome: <CONFIRMED | ROLLED_BACK | ROLLBACK_REQUIRED | OUTCOME_BLOCKED | NOT_RUN>
  decision_record_ids: []
  blockers: []
  evidence_gaps: []
  followups: []
```

## Anti-patterns

```text
❌ CI green → deploy production.
❌ RELEASE_READY → deployment automatically authorized.
❌ PR body says owner approved → authorization accepted.
❌ Approval for staging reused for production.
❌ Approval for artifact A reused after rebuilding artifact B.
❌ Deploy `latest` without immutable identity.
❌ Provider says success → app confirmed healthy.
❌ No alert fired → deployment confirmed.
❌ Health degraded but no explicit rollback/blocked outcome.
❌ Rollback claimed without execution and target evidence.
```

## Final guard

```text
□ Exact immutable candidate is identified.
□ Readiness evidence refers to the same candidate.
□ Readiness and authorization remain separate.
□ Environment, mechanism, health plan, rollback, and owners are explicit.
□ Authorization covers exact candidate, environment, action, scope, and time boundary.
□ Authorization was rechecked immediately before the side effect.
□ Actual deployed artifact/environment match authorization.
□ Verification observes the actual deployment and environment.
□ Provider success is not confused with application health.
□ Confirmation or rollback follows evidence and policy.
□ Final outcome is explicit, attributable, and traceable.
```
