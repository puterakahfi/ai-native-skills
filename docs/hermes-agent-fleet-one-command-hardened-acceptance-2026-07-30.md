# Hardened One-command Hermes Fleet Acceptance

Issue: `puterakahfi/ai-native-skills#272`  
Parent epic: `puterakahfi/ai-native-skills#260`  
Pull request: `puterakahfi/ai-native-skills#273`  
Date: 2026-07-30

## Purpose

Repeat the direct Hermes acceptance after the executor received final path and symlink hardening. This supersedes the earlier runtime result as the final executable evidence for the implementation merged by PR #273.

## Evidence identity

```yaml
runtime_evidence:
  implementation_head_before_temporary_harness: 0cfb67f8a3f9ac6006ba54ef253b2e77f165d7c4
  workflow: Skill Package Validation
  workflow_run_id: 30508591811
  workflow_job_id: 90763603592
  workflow_result: PASS
  runtime_test_duration_seconds: 51.959
```

The test harness and helper script were branch-scoped and removed after the result was captured.

## Runtime

```yaml
hermes:
  version: "0.19.0"
  release_identity: "2026.7.20"
  upstream_revision: dd51931b
  install_method: git
  python: "3.11.15"
  openai_sdk: "2.24.0"
  runtime: ephemeral_github_actions
  isolated_hermes_home: true
  user_runtime_touched: false
```

## Final command under test

```bash
bash skills/hermes-agent-fleet-bootstrap/scripts/hermes-fleet \
  bootstrap native-ai-engineering --apply
```

The command was executed twice against the same isolated `HERMES_HOME`, followed by a read-only audit.

## Result

```yaml
acceptance_result: PASS
first_apply: READY
second_apply: READY
audit: READY
idempotency: PASS
path_and_symlink_hardening_tests: PASS
gateway_policy: ORCHESTRATOR_ELIGIBLE_SPECIALISTS_NONE
profiles:
  - backend-platform
  - engineering-orchestrator
  - frontend-engineering
  - product-design
  - product-development
  - quality-review
  - solution-architecture
```

The second apply contained no `CREATED`, `INSTALLED`, or `UPDATED` actions. It returned `SKIP_EXISTS`, `SKIP_IN_SYNC`, and `SKIP_INITIALIZED` for already-conforming state.

## Security hardening proven

The final skill-local suite passed eleven cases, including explicit rejection of:

- preset or profile identifiers containing path traversal;
- unsafe skill identifiers;
- unsupported gateway policy values;
- symlinked Hermes profiles roots;
- symlinked profile or profile-skills directories;
- symlinked managed skill sources or files;
- skill source directories that lack `SKILL.md`.

Unsafe preset or source state fails before profile mutation.

## Safety boundary

The accepted executor:

- creates only missing profiles;
- synchronizes only preset-owned profile-local skill directories;
- preserves existing profile descriptions and unmanaged runtime state;
- does not configure or start messaging gateways;
- does not provision bot tokens or provider credentials;
- does not delete or destructively migrate profiles;
- does not copy sessions, memories, cron state, logs, databases, caches, or product secrets;
- does not claim Hermes profile isolation is an operating-system sandbox.

## Limitations

```yaml
messaging_gateway: NOT_VERIFIED_NO_BOT_CREDENTIALS
model_driven_specialist_reasoning: NOT_APPLICABLE_TO_DETERMINISTIC_BOOTSTRAP
user_existing_hermes_host: NOT_TOUCHED
os_level_sandboxing: NOT_PROVEN
```

## Final verdict

```yaml
product_acceptance:
  one_command_bootstrap: PASS
  real_hermes_profile_creation: PASS
  responsibility_specific_skill_installation: PASS
  kanban_initialization: PASS
  idempotent_replay: PASS
  read_only_audit: PASS
  path_and_symlink_security: PASS
  secret_and_live_state_preservation: PASS
  merge_to_epic_branch: AUTHORIZED_BY_OWNER
  merge_to_main: NOT_AUTHORIZED
  verdict: PASS

skill_evolution:
  finding_type: IMPROVEMENT
  verdict: LOCAL_ONLY
  core_rfc: NOT_JUSTIFIED
```
