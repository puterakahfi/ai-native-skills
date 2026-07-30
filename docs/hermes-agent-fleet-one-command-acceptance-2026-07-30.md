# Hermes Agent Fleet One-command Runtime Acceptance

Issue: `puterakahfi/ai-native-skills#272`  
Parent epic: `puterakahfi/ai-native-skills#260`  
Pull request: `puterakahfi/ai-native-skills#273`  
Date: 2026-07-30

## Objective

Prove that the approved Native AI Engineering specialist fleet can be created through one deterministic command rather than a manual sequence of profile, skill, and Kanban commands.

Primary command under test:

```bash
bash skills/hermes-agent-fleet-bootstrap/scripts/hermes-fleet \
  bootstrap native-ai-engineering --apply
```

## Evidence identity

```yaml
runtime_evidence:
  repository: puterakahfi/ai-native-skills
  branch: 272-hermes-fleet-one-command-cli
  source_commit: 3139610076ae2a6a71b0d73efb2876a74b588c1f
  pull_request: 273
  workflow: Skill Package Validation
  workflow_run_id: 30507923051
  workflow_job_id: 90761602162
  workflow_result: PASS
  runtime_test_duration_seconds: 59.473
```

The direct runtime smoke was invoked through a temporary branch-scoped trusted-CI hook. The hook was removed after evidence was captured and is not part of the final deliverable.

## Runtime observed

```yaml
hermes:
  version: "0.19.0"
  release_identity: "2026.7.20"
  upstream_revision: f1120ada
  install_method: git
  python: "3.11.15"
  openai_sdk: "2.24.0"
  runtime: ephemeral_github_actions
  isolated_hermes_home: true
  user_runtime_touched: false
```

Hermes was installed from the official installer into an isolated temporary install directory and `HERMES_HOME`. Bundled skills, setup, and browser installation were disabled. Optional `ripgrep` and `ffmpeg` availability checks used version-only stubs because browser, voice, and media behavior were outside this acceptance scope.

## Unit and fixture validation

The skill-local suite executed before the direct runtime flow and passed all nine cases:

1. plan-only does not mutate runtime;
2. apply creates profiles, installs skills, and initializes Kanban;
3. repeated apply is idempotent;
4. missing required skill fails before mutation;
5. missing Hermes fails closed;
6. audit reports missing state without mutation;
7. exactly one orchestrator is gateway-eligible;
8. every preset skill resolves to a real repository package;
9. Hermes profile-command failure is recorded as blocked.

## Preset executed

```yaml
preset:
  id: native-ai-engineering
  version: 1.0.1
  topology: orchestrator_with_specialists
  orchestrator: engineering-orchestrator
  gateway_policy: ORCHESTRATOR_ELIGIBLE_SPECIALISTS_NONE
  profiles:
    - engineering-orchestrator
    - product-development
    - solution-architecture
    - product-design
    - frontend-engineering
    - backend-platform
    - quality-review
```

The CLI did not start any messaging gateway and did not provision a bot token or provider credential.

## First apply

The first one-command apply returned:

```yaml
first_apply:
  exit_code: 0
  readiness: READY
  profiles_created: PASS
  responsibility_specific_skills_installed: PASS
  kanban_initialized: PASS
  receipt_written: PASS
```

The seven expected profile directories were present under the isolated Hermes home after execution.

## Second apply and idempotency

The exact command was executed a second time against the same isolated Hermes home.

```yaml
second_apply:
  exit_code: 0
  readiness: READY
  duplicate_profiles_created: false
  skills_reinstalled_without_change: false
  skills_updated_without_change: false
  profile_actions: SKIP_EXISTS
  skill_actions: SKIP_IN_SYNC
  kanban_action: SKIP_INITIALIZED
  idempotency: PASS
```

This proves deterministic replay for the approved preset and checked-out skill catalog.

## Audit

The read-only audit command was then executed:

```bash
bash skills/hermes-agent-fleet-bootstrap/scripts/hermes-fleet \
  audit native-ai-engineering
```

```yaml
audit:
  exit_code: 0
  readiness: READY
  runtime_mutation: false
  profile_conformance: PASS
  managed_skill_digest_conformance: PASS
```

## Runtime receipt

```yaml
runtime_receipt:
  acceptance_result: PASS
  first_apply: READY
  second_apply: READY
  audit: READY
  idempotency: PASS
  gateway_policy: ORCHESTRATOR_ELIGIBLE_SPECIALISTS_NONE
  profiles:
    - backend-platform
    - engineering-orchestrator
    - frontend-engineering
    - product-design
    - product-development
    - quality-review
    - solution-architecture
  user_runtime_touched: false
```

## Safety and preservation evidence

The executor:

- verified all required local skill sources before mutation;
- created only missing profiles;
- used profile-local managed skill directories;
- preserved existing profile descriptions and unmanaged runtime state;
- did not delete, merge, split, or destructively migrate profiles;
- did not read or write provider credentials;
- did not copy sessions, memories, cron state, logs, databases, or product secrets;
- did not represent Hermes profile separation as an operating-system sandbox.

## Limitations

1. No Telegram, Discord, or other messaging gateway was started.
2. No bot token was configured.
3. No model-provider credential or LLM specialist reasoning was required for deterministic bootstrap.
4. Profile separation was verified at the Hermes-home level, not as filesystem, process, network, or credential sandboxing.
5. The run used a fresh ephemeral runtime rather than the user's existing Hermes host.
6. Existing product-facing profiles such as `pkahfi`, `visualmate`, `docs`, and `ai` were not migrated.

## Acceptance verdict

```yaml
product_acceptance:
  one_command_plan: PASS
  one_command_apply: PASS
  real_hermes_profile_creation: PASS
  responsibility_specific_skill_installation: PASS
  kanban_initialization: PASS
  idempotent_second_apply: PASS
  read_only_audit: PASS
  gateway_policy: PASS
  secret_and_live_state_preservation: PASS
  real_messaging_bot: NOT_VERIFIED
  model_driven_specialist_execution: NOT_APPLICABLE_TO_BOOTSTRAP
  verdict: PASS
  merge_to_epic_branch: AUTHORIZED_BY_OWNER
  merge_to_main: NOT_AUTHORIZED
```

## Learning review

```yaml
skill_evolution:
  verdict: LOCAL_ONLY
  finding_type: IMPROVEMENT
  rationale:
    - The prior capability was correct but operationally too manual.
    - A deterministic approved-preset executor removes unnecessary bootstrap friction.
    - Evidence remains Hermes-specific and does not justify a runtime-agnostic Core contract change.
  core_rfc: NOT_JUSTIFIED
```
