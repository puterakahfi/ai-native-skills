---
name: software-testing-workflow
description: Compose risk discovery, justified test-level selection, verified adapter selection, execution, failure analysis, normalized evidence, and acceptance handoff within an existing primary engineering lifecycle.
license: MIT
metadata:
  ai-native-skills.version: 0.1.0
  ai-native-skills.author: puterakahfi
  ai-native-skills.type: workflow
  ai-native-skills.requires: "test-strategy unit-testing integration-testing contract-testing acceptance-testing end-to-end-testing behavior-driven-development implementation-context-discovery decision-provenance"
  ai-native-skills.related_skills: '["test-driven-development","production-code-quality-baseline","workflow-router","role-switcher","code-review-workflow"]'
---

# Software Testing Workflow

## Ownership

This workflow composes testing capabilities inside the active feature, bugfix, refactoring, review, specification, or release lifecycle. It never becomes a competing product or delivery lifecycle. The primary workflow remains accountable for outcome and acceptance.

## Lifecycle

```text
verify objective, acceptance, repository, and primary workflow
→ discover change surface, risks, boundaries, and existing commands
→ run test-strategy
→ record selected and rejected test levels with rationale
→ select adapters only after stack discovery
→ implement and execute selected capabilities
→ inspect failures, retries, skips, flakiness, and unavailable environments
→ aggregate normalized evidence
→ run confidence and acceptance gate
→ return evidence to the primary workflow
```

## Applicability

Activate only for materially justified risks. Do not run all levels unconditionally. Preserve:

- `NOT_APPLICABLE`: the level cannot address this change or risk;
- `NOT_JUSTIFIED`: possible but disproportionate or duplicative;
- `NOT_VERIFIED`: required evidence could not be obtained.

None may silently become PASS.

## Adapter selection

Load the relevant adapter reference only after repository stack, scripts, services, and validation commands are verified:

- `adapters/javascript-typescript.md`
- `adapters/go.md`
- `adapters/php.md`

Tools and execution providers remain replaceable adapters; they do not redefine canonical test-level or evidence semantics.

## Validation execution providers

GitHub Actions is optional as an execution provider. A clean local runtime, ephemeral self-hosted runner, Vercel build, or another CI provider may execute the canonical repository commands when hosted GitHub runners are unavailable.

Provider substitution changes only the executor. It must not weaken commands, risk coverage, evidence semantics, acceptance authority, or merge gates. The replacement executor must run the same applicable repository-defined commands unless an explicit, provenance-backed equivalent is approved by the governing repository authority.

Replacement evidence must:

- identify the exact repository, branch, and commit;
- execute the applicable verified repository commands;
- record executor and environment versions;
- preserve command results, failures, skips, flakiness, and limitations;
- distinguish provider unavailability from test failure;
- never translate an unavailable provider into PASS.

## Evidence contract

Load `references/normalized-testing-evidence.md`. Every result traces to a risk, boundary, contract, criterion, behavior example, or journey. Failed, flaky, skipped, unavailable, retried, and unsupported states remain visible.

## Composition rule

Load `references/workflow-composition.md`. `workflow-router` selects one primary lifecycle. `role-switcher` assigns one delivery owner and relevant testing specialists. This workflow is a verification composition owned by that primary lifecycle.

## Normalized output

```yaml
software_testing:
  primary_workflow: <id>
  context_status: VERIFIED | PARTIAL | NOT_VERIFIED
  risks: []
  selected_levels: []
  rejected_levels: []
  adapters: []
  execution_provider:
    id: <github-actions | local-clean-runtime | self-hosted | vercel | other>
    status: AVAILABLE | UNAVAILABLE | PARTIAL
  commands: []
  results: []
  failures: []
  flaky_results: []
  skipped_results: []
  unavailable_evidence: []
  traceability: []
  limitations: []
  confidence: SUFFICIENT | INSUFFICIENT | NOT_VERIFIED
  acceptance_handoff: PASS | FAIL | NEEDS_WORK | NOT_VERIFIED
```

## Gates

- risks and boundaries precede framework choice;
- selected and rejected levels have rationale;
- each command is verified from repository evidence;
- adapters match the verified stack;
- execution evidence is attributable to an exact repository and commit;
- provider failure remains separate from test failure;
- duplicate E2E, ceremonial BDD, mock abuse, and browser-by-default are rejected;
- unresolved failures or insufficient evidence block PASS;
- product acceptance and merge authorization remain external.

## Stop conditions

Stop with `NEEDS_WORK`, `NOT_VERIFIED`, or `BLOCKED` when repository context, required environment, commands, traceability, or authority cannot be proven.
