# Branch Topology and PR Targets

Run this decision before `git-workflow`; Git executes the approved topology and does not invent it.

## Default topology for an epic

```text
release branch
└── epic/integration branch
    ├── feature branch
    ├── task branch
    └── spike branch
```

Pull requests flow upward through the governing release unit:

```text
child branch → epic/integration branch
final epic branch → release branch
```

## Required decision matrix

```yaml
repository_topology:
  release_branch: main
  integration_branch: epic/37-chatgpt-app-p0
  branch_naming_policy_ref: <record>
  merge_policy_ref: <record>

pr_target_matrix:
  - work_item_ref: FEATURE-MCP
    branch: feat/mcp-tools
    base_branch: epic/37-chatgpt-app-p0
    pr_target: epic/37-chatgpt-app-p0
    direct_to_release_allowed: false
    rationale: dependent epic child
```

## Direct-to-release decision

Permit only when one route passes:

### Route A — independently releasable

- backward-compatible;
- useful or inert safely by itself;
- no sibling dependency for correctness;
- its acceptance criteria can be directly verified;
- rollback is independent.

### Route B — approved safe flag

- attributable product/repository policy permits incremental release;
- default is disabled or equivalent safe state;
- every incomplete runtime path is protected;
- bypass-path audit is complete;
- disabled behavior is tested;
- rollback/kill behavior exists.

### Route C — equivalent trunk-based policy

A product may avoid long-lived epic branches if its accepted policy provides equivalent controls for:

- incomplete activation prevention;
- parent-child traceability;
- integration acceptance;
- final release authorization;
- rollback.

The skill records the policy reference instead of imposing GitFlow.

## Synchronization

- Child branches take their base from the approved integration branch, not the repository default.
- Integration branches periodically synchronize from the release branch using product policy.
- Do not force-push shared integration branches.
- Reclassification or target changes require updated dependency and provenance records.

## Evidence boundary

A topology document does not prove branches or PRs exist. `git-workflow` must report actual operations and conflicts.
