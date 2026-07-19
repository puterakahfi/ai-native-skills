# Deployment Authorization, Verification, and Outcome

Load this reference for deployment authorization, execution identity, environment verification, confirmation, and rollback decisions.

Load `decision-provenance` for material claims about candidate approval, target environment, deployment window, operator authority, accepted operational risk, confirmation, or rollback authority.

## Boundary

```text
technical readiness
  proves the candidate is technically eligible to be considered for deployment

deployment authorization
  proves an authorized decision permits the exact side effect

deployment execution
  records what artifact actually reached which environment

deployment verification
  proves the deployed environment's observed health

deployment outcome
  confirms the deployment, executes rollback, or records a blocker
```

Never collapse these into one `DEPLOYED` or `SUCCESS` flag.

## Release candidate identity

Record an immutable candidate before readiness or authorization:

```yaml
release_candidate:
  candidate_id: <stable id>
  source_ref: <commit, release, build, or artifact source>
  immutable_artifact_identity: <digest, immutable deployment artifact id, or equivalent>
  intended_environment: <environment>
  approved_scope: []
  acceptance_or_release_readiness_ref: <reference or N/A>
  code_review_verdict_ref: <reference>
  security_review_ref: <reference or N/A>
  rollback_target: <previous known candidate or mechanism>
```

A branch name, `latest` tag, mutable image tag, or unpinned artifact reference is not sufficient by itself.

```text
candidate changes after readiness
  → technical readiness becomes stale

candidate changes after authorization
  → authorization no longer covers the candidate

environment changes
  → context and authorization must be resolved for the new environment
```

## Technical readiness

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

`READY` requires all applicable blocking concerns to be resolved for the same immutable candidate.

```text
READY
  ≠ authorized to deploy

CI green
  ≠ readiness when required review, rollback, configuration, or acceptance evidence is missing
```

## Deployment context

```yaml
deployment_context:
  candidate_id: <id>
  immutable_artifact_identity: <identity>
  target_environment: <environment>
  protected_environment: <true | false>
  provider_and_mechanism: <provider/action>
  configuration_policy: <reference>
  secret_management: <reference>
  change_window: <window or N/A>
  observability_sources: []
  health_checks: []
  smoke_tests: []
  key_flows: []
  verification_window: <duration/condition>
  rollback_target: <target>
  rollback_mechanism: <mechanism>
  emergency_rollback_policy: <reference or N/A>
  deploy_operator_or_automation: <identity>
  confirmation_owner: <owner/policy>
  rollback_owner: <owner/policy>
```

Do not assume all staging environments are unprotected or that every production environment uses the same approval model.

## Deployment authorization

Use `decision-provenance` with the claim:

```text
<authorized actor or automation> may deploy
<candidate identity> to <environment>
for <approved scope/action>
within <time/change boundary>
under <declared risk and rollback conditions>
```

Required record:

```yaml
deployment_authorization_record:
  decision_record_ids: []
  candidate_id: <id>
  immutable_artifact_identity: <identity>
  target_environment: <environment>
  approved_scope: []
  deployment_action: <action>
  change_window: <window or N/A>
  authorized_operator_or_automation: <identity>
  accepted_operational_risks: []
  required_authority: <owner/policy>
  provenance_verdict: <PASS | PROVENANCE_BLOCKED | ROUTE_FOR_APPROVAL>
  status: <AUTHORIZED | NOT_AUTHORIZED | ROUTE_FOR_APPROVAL>
```

Rules:

```text
technical readiness READY
  → may enter authorization gate
  → does not execute deployment

agent-authored issue, PR body, report, commit, or chat summary
  → not authorization without attributable owner acceptance

authorization covers candidate A in staging
  → cannot authorize candidate B or production

authorization has expired or is outside its change window
  → reauthorize

protected side effect requires another authority
  → ROUTE_FOR_APPROVAL
```

Re-resolve authorization immediately before invoking the side effect.

## Execution record

Execute only the exact authorized candidate/environment pair.

```yaml
deployment_execution_record:
  deployment_id: <provider id>
  candidate_id: <id>
  deployed_artifact_identity: <actual identity>
  target_environment: <actual environment>
  provider_and_mechanism: <value>
  operator_or_automation: <identity>
  authorization_record_id: <record>
  started_at: <time or sequence>
  completed_at: <time or sequence>
  execution_status: <EXECUTED | FAILED | NOT_RUN>
  provider_result: <result>
```

Hard mismatch:

```text
actual artifact != authorized artifact
or actual environment != authorized environment
  → stop confirmation
  → record mismatch
  → classify deployment as blocked/incident according to product policy
```

## Direct environment verification

```yaml
deployment_verification_report:
  deployment_id: <id>
  candidate_id: <id>
  deployed_artifact_identity: <identity>
  target_environment: <environment>
  verification_window: <window>
  evidence:
    health_checks: []
    smoke_tests: []
    key_flows: []
    error_and_log_observation: []
    dependency_health: []
    migration_or_data_health: []
    performance_or_slo: []
  evidence_gaps: []
  findings: []
  status: <HEALTHY | DEGRADED | NOT_VERIFIED>
```

```text
provider says deployment completed
  ≠ application healthy

local or CI smoke test
  ≠ deployed-environment smoke test

one health endpoint
  may be insufficient when the acceptance boundary includes key flows,
  dependencies, migration/data health, or SLOs
```

## Confirm or rollback

### Healthy

```text
HEALTHY
+ confirmation permitted by policy
+ required confirmation provenance available
→ CONFIRMED
```

Absence of a confirmation record is not confirmation when policy requires one.

### Degraded

```text
DEGRADED
+ pre-authorized emergency rollback policy applies
→ execute rollback without waiting for a new routine approval
→ verify rollback environment health

DEGRADED
+ rollback authority still required
→ ROUTE_FOR_APPROVAL or ROLLBACK_REQUIRED according to policy
→ do not falsely confirm
```

### Not verified

```text
NOT_VERIFIED
→ OUTCOME_BLOCKED
→ continue bounded observation, collect required evidence,
  or route to the operational owner
```

Do not silently confirm because no alert fired.

## Outcome record

```yaml
deployment_outcome_record:
  deployment_id: <id>
  candidate_id: <id>
  environment: <environment>
  verification_status: <HEALTHY | DEGRADED | NOT_VERIFIED>
  decision_record_ids: []
  outcome: <CONFIRMED | ROLLED_BACK | ROLLBACK_REQUIRED | OUTCOME_BLOCKED>
  action:
    type: <confirm | rollback | observe | route>
    rollback_target: <target or null>
    resulting_deployment_id: <id or null>
  post_action_health: <HEALTHY | DEGRADED | NOT_VERIFIED | N/A>
  incidents_or_followups: []
  owner: <owner>
```

`ROLLED_BACK` requires proof that rollback executed. It does not imply post-rollback health unless directly verified.

## Workflow states

```text
candidate_identified
→ readiness_checking
→ NOT_READY | READY
→ authorization_checking
→ NOT_AUTHORIZED | ROUTE_FOR_APPROVAL | AUTHORIZED
→ deploying
→ EXECUTION_FAILED | deployed
→ verifying
→ HEALTHY | DEGRADED | NOT_VERIFIED
→ confirming | rolling_back | outcome_blocked
→ CONFIRMED | ROLLED_BACK | ROLLBACK_REQUIRED | OUTCOME_BLOCKED
```

## Anti-patterns

```text
❌ CI green, so deploy production now.
❌ Product is RELEASE_READY, so deployment authorization is implied.
❌ PR body says the owner approved deployment.
❌ Approval for staging is reused for production.
❌ Approval for candidate A is reused after rebuilding candidate B.
❌ Deploying a mutable `latest` artifact with no immutable identity.
❌ Provider status “success” is treated as application health.
❌ No alert fired, therefore confirmed.
❌ Health degraded, but wait indefinitely despite a pre-authorized rollback policy.
❌ Claiming rollback succeeded without a rollback deployment record.
❌ Confirming or rolling back a different deployment than the one verified.
```

## Final guard

```text
□ Exact immutable release candidate is identified.
□ Readiness evidence refers to that same candidate.
□ Context names environment, mechanism, health plan, rollback, and owners.
□ Authorization covers exact candidate, environment, action, scope, and time boundary.
□ Authorization was rechecked immediately before the side effect.
□ Actual execution matches the authorization record.
□ Verification observes the deployed environment and deployment ID.
□ Provider success is not confused with application health.
□ Confirmation or rollback follows evidence and product policy.
□ Emergency rollback uses an explicit pre-authorized policy when applicable.
□ Final outcome is explicit and directly traceable.
```
