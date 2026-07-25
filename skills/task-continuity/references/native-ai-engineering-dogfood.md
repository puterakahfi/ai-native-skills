# Native AI Engineering Dogfood Checkpoint

This checkpoint applies `task-continuity` to the delivery of `task-continuity` itself.

```yaml
checkpoint:
  checkpoint_id: ai-native-task-continuity-delivery
  checkpoint_version: 1
  observed_at: "2026-07-25T04:57:00Z"
  supersedes:
    - ai-native-core/pull/49
    - ai-native-skills/pull/79

  identity:
    product_ref: Native AI Engineering
    task_or_workflow_ref:
      - ai-native-core/issue/48
      - ai-native-skills/issue/78
    repository_refs:
      - puterakahfi/ai-native-core
      - puterakahfi/ai-native-skills
    core_pull_request_ref: puterakahfi/ai-native-core#54
    skills_pull_request_ref: puterakahfi/ai-native-skills#125
    skills_branch_ref: feat/78-task-continuity-v2

  objective: >-
    Define and release the canonical task-continuity contract and executable
    adapter with source-backed checkpoint, portable handoff, verified resume,
    staleness and supersession handling, exact next actions, and safe closure.

  acceptance_criteria:
    - Core contract is merged from current main-compatible source.
    - Executable adapter conforms to the accepted Core contract.
    - Natural fresh-chat and resume requests activate continuity behavior.
    - Governing feature, bug, design, review, or deployment lifecycle is preserved.
    - Inventory, discovery, contract, stack, and behavioral gates pass.
    - Stale superseded PRs are not merged or treated as current.

  work_state:
    implemented:
      - Core contract, tests, and documentation were rebuilt on current Core main.
      - Skills adapter, references, router integration, discovery, and evals exist on PR #125.
      - Generated capability inventory and contract coverage were synchronized by the repository generator.
    verified:
      - Core semantic, schema, identity, port, behavioral, and regression checks passed before merge.
      - Core PR #54 merged at commit 48667ca2d53ebeedc5308cffef9995b6a0531222.
      - Initial Skills runs passed Skill Pack Contracts and Repository Stack Conformance.
      - Generated metadata records task-continuity with an existing Core contract path.
    pending:
      - Run the complete Skills PR gate set on a user-authored head after the generated bot commit.
      - Review the final effective diff and merge PR #125 only when the exact head is green.
      - Produce a closure record after Skills main contains the adapter.
    blocked: []
    abandoned:
      - Core PR #49 was closed as superseded because its generated artifacts conflicted with current main.
      - Skills PR #79 was closed as superseded because it was 79 commits behind current main.

  decisions:
    - decision: Rebuild from current main instead of force-merging stale branches.
      status: accepted
      source_ref:
        - puterakahfi/ai-native-core#54
        - puterakahfi/ai-native-skills#125
      authority: repository delivery policy and explicit owner authorization
    - decision: Continuity is a verification overlay, not a competing lifecycle.
      status: accepted
      source_ref: skills/workflow-router/SKILL.md
      authority: executable adapter boundary
    - decision: Generated inventory and coverage use repository generators.
      status: accepted
      source_ref: .github/workflows/sync-generated-capability-metadata.yml
      authority: repository tooling convention

  validation:
    - command_or_gate: Core Contract Integrity
      exact_result: Semantic checks passed; pre-merge failure was limited to stale generated parity.
      status: PASS_WITH_DISCLOSED_GENERATED_PARITY
      evidence_ref: ai-native-core workflow run 30143983544
    - command_or_gate: Skills initial Skill Pack Contracts
      exact_result: success
      status: PASS
      evidence_ref: ai-native-skills workflow run 30144687583
    - command_or_gate: Skills initial Repository Stack Conformance
      exact_result: success
      status: PASS
      evidence_ref: ai-native-skills workflow run 30144687593
    - command_or_gate: Skills full final PR gates
      exact_result: bot-authored generated commit did not create executable jobs
      status: NOT_EXECUTED
      evidence_ref:
        - ai-native-skills workflow run 30144895093
        - jobs: []

  blockers_and_risks:
    - Final Skills acceptance must use workflows executed on the current user-authored PR head.
    - Structural and synthetic eval validation do not by themselves prove fresh-runtime natural application.

  next_exact_action: >-
    Execute all applicable ai-native-skills PR workflows on the user-authored
    head containing this checkpoint and inspect every non-green step before merge.

  expected_evidence:
    - current PR head SHA
    - workflow run IDs and conclusions
    - exact failing job and step for every non-green result
    - final effective-diff and review-thread result

  provenance:
    authoritative_sources:
      - puterakahfi/ai-native-core#54
      - puterakahfi/ai-native-core@48667ca2d53ebeedc5308cffef9995b6a0531222
      - puterakahfi/ai-native-skills#125
      - puterakahfi/ai-native-skills#78
    unavailable_sources: []
    assumptions: []

  continuity_validation:
    verdict: VALID_WITH_WARNINGS
    warnings:
      - Final Skills workflows have not yet executed on the current human-authored head.
    next_exact_action: Run and inspect all Skills PR gates on this exact head.
```

The checkpoint is evidence for continuity behavior, not proof that PR #125 is merged or accepted.
