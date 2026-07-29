# Runtime Acceptance — Hermes Specialist Agent Fleet Bootstrap

Issue: `puterakahfi/ai-native-skills#265`  
Parent epic: `puterakahfi/ai-native-skills#260`  
PR: `puterakahfi/ai-native-skills#271`  
Date: 2026-07-29

## Acceptance scope

Validate the integrated `hermes-agent-fleet-bootstrap` capability against a real Hermes installation without touching the user's local Hermes profiles, memories, sessions, gateway state, tokens, or credentials.

The acceptance run used an isolated ephemeral GitHub Actions runtime and executed the following sequence:

```text
install official Hermes
→ create bounded named profiles
→ materialize the complete fleet-bootstrap skill package into the orchestrator profile
→ verify profile-local skill discovery
→ initialize a real Kanban board
→ create idempotent tasks and dependency links
→ claim and complete work through four named profiles
→ run dispatcher dry-run and a fail-closed no-provider probe
→ emit a machine-readable runtime receipt
```

## Evidence identity

```yaml
runtime_evidence:
  repository: puterakahfi/ai-native-skills
  branch: test/265-hermes-runtime-acceptance
  head_commit: 7f75cd057eb7a212cfb6490cf04b70233ebbfff9
  pull_request: 271
  workflow: Skill Package Validation
  workflow_run_id: 30471479992
  workflow_job_id: 90642533700
  workflow_conclusion: success
  test_duration_seconds: 78.582
```

The acceptance logic was invoked through a branch-scoped trusted-CI hook and removed from the deliverable after the receipt was recorded.

## Hermes runtime observed

```yaml
hermes:
  version: "0.19.0"
  release_date_identity: "2026.7.20"
  upstream_revision: 1fe06115d1ed00ac859e5aa2a6afcde4a2c8bbbe
  install_method: git
  python: "3.11.15"
  openai_sdk: "2.24.0"
  runtime: ephemeral_github_actions
  isolated_hermes_home: true
  user_runtime_touched: false
```

The installer was run with setup, bundled skills, and browser installation disabled. Optional `ripgrep` and `ffmpeg` checks were satisfied with version-only acceptance stubs because browser, voice, and media behavior were outside this runtime scope.

## Profiles created

```yaml
profiles:
  - engineering-orchestrator
  - solution-architecture
  - backend-platform
  - quality-review
  unique_profile_paths: true
  bundled_skills_opted_out: true
```

Each profile was created through the real Hermes CLI with its own durable profile home and bounded description. All messaging gateways were observed as stopped. No specialist profile contained a configured bot token or provider secret.

## Skill materialization

The complete checked-out package was materialized under the orchestrator profile's local Hermes skill directory:

```text
profiles/engineering-orchestrator/skills/hermes-agent-fleet-bootstrap/
├── SKILL.md
├── references/
└── assets/
```

Validation proved:

- the orchestrator's `hermes skills list` discovered `hermes-agent-fleet-bootstrap`;
- the package entry point existed;
- the specialist archetype reference existed;
- the fleet manifest template existed.

```yaml
skill_install: PASS
```

Direct installation from an unpublished PR-head raw URL was not used as final evidence because Hermes could not fetch that transient source. The accepted evidence is profile-local package materialization and Hermes runtime discovery of the complete package.

## Kanban and profile execution evidence

```yaml
kanban:
  initialization: PASS
  board_creation: PASS
  idempotent_task_creation: PASS
  dependency_links: PASS
  named_profile_claim_and_completion: PASS
  dispatcher_dry_run: PASS
  specialists_executed_via: DIRECT_PROFILE_CLI
```

The real shared board contained bounded tasks for:

1. `engineering-orchestrator` — decomposition and synthesis responsibility;
2. `solution-architecture` — architecture contract inspection;
3. `backend-platform` — durable board and persistence evidence;
4. `quality-review` — review of integrated runtime evidence and limitations.

Each task was claimed and completed through its named profile. Repeating task creation with the same idempotency key produced one logical task rather than a duplicate. Dependency links were created between architecture, backend, and review tasks.

This proves real Hermes profile-scoped Kanban operations. It does not prove model-generated specialist reasoning because the task results were submitted through direct profile CLI operations.

## Dispatcher and provider boundary

```yaml
dispatcher:
  dry_run: PASS
  no_provider_probe_exit: 0
  llm_worker_execution: BLOCKED_OR_NOT_VERIFIED_WITHOUT_PROVIDER
  provider_credentials_configured: false
```

The dispatcher accepted a dry-run and handled the no-provider probe without an uncontrolled crash. No claim is made that an LLM worker completed the task because no model credential was provisioned.

## Gateway boundary

```yaml
gateway:
  orchestrator_bot_started: false
  specialist_bots_started: false
  specialist_tokens_configured: false
  policy_check: PASS_NO_DEDICATED_SPECIALIST_GATEWAYS
  status: NOT_RUN_NO_BOT_CREDENTIALS
```

The run validates the default policy that specialists do not require dedicated bots. It does not prove Telegram, Discord, Slack, or another messaging channel because no bot credential was available or requested.

## Review independence

```yaml
review_independence:
  status: LIMITED_SHARED_RUNTIME_AND_SCRIPTED_CLI
```

`quality-review` was a separate Hermes profile, but the profiles shared one ephemeral CI host and the task operations were driven by one scripted acceptance harness. This is useful separation of profile identity, but not fully independent human or model review.

## Runtime receipt

```yaml
runtime_receipt:
  acceptance_result: PASS_WITH_LIMITATIONS
  doctor: PASS
  profile_creation: PASS
  profile_isolation_at_hermes_home_level: PASS
  skill_discovery: PASS
  kanban_persistence_and_task_flow: PASS
  idempotency: PASS
  dependency_graph: PASS
  named_profile_operations: PASS
  dispatcher_mechanics: PASS_WITH_PROVIDER_LIMITATION
  messaging_gateway: NOT_RUN
  model_driven_specialist_execution: NOT_VERIFIED
  user_local_runtime: NOT_TOUCHED
```

## Limitations

1. The run proves a fresh ephemeral Hermes installation, not the user's existing local installation or current profiles.
2. No Telegram, Discord, or other messaging gateway was started.
3. No model provider credential was configured, so LLM-driven specialist execution remains `NOT_VERIFIED`.
4. Profile separation does not prove operating-system, filesystem, network, or credential sandboxing.
5. Reviewer independence is limited by the shared host and scripted execution context.
6. Product-facing profiles such as `pkahfi`, `visualmate`, `docs`, and `ai` were not migrated; their real audit remains a separate authorized operation.

## Acceptance verdict

```yaml
product_acceptance:
  epic_capability_contract: PASS
  real_hermes_cli: PASS
  real_profile_creation: PASS
  real_profile_local_skill_discovery: PASS
  real_kanban_coordination: PASS
  real_named_profile_task_operations: PASS
  messaging_bot: NOT_VERIFIED
  model_driven_workers: NOT_VERIFIED
  reviewer_independence: LIMITED
  verdict: PASS_WITH_LIMITATIONS
  merge_to_epic_branch: AUTHORIZED_BY_OWNER
  merge_to_main: NOT_AUTHORIZED
```

The integrated Epic is eligible to retain this capability on `260-hermes-agent-fleet-bootstrap`. Final release or merge to `main` remains a separate owner decision.

## Learning review

```yaml
skill_evolution_review:
  classification: LOCAL_ONLY
  rationale:
    - The source case validates Hermes-specific profile, local skill, and Kanban mechanics.
    - No second runtime adapter or cross-runtime transfer evidence exists.
    - The provider-specific Core contract exemption remains appropriate.
  core_rfc: NOT_JUSTIFIED
  next_evidence:
    - real user Hermes installation audit
    - real orchestrator bot gateway
    - provider-backed model worker execution
    - cross-runtime transfer case
```
