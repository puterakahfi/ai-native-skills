# VisualMate GPT Kanban activity capture — 2026-08-02

## Source board

```yaml
board: visualmate-gpt
parent_epic: t_350617de
parent_title: EPIC - Close VisualMate Naturalism & Fidelity Stress Test v1 gaps
source_artifact: user_supplied_visualmate_naturalism_fidelity_stress_test_report_v1
observed_at: 2026-08-02
```

## Captured activity

The active VisualMate GPT workflow decomposed a Naturalism & Fidelity Stress Test remediation into parallel specialist lanes and downstream review gates:

| Task | Status at capture | Assignee | Observed role |
|---|---:|---|---|
| `t_350617de` | `todo` | `agent-orchestrator` | Parent epic / synthesis owner |
| `t_6084f4ae` | `running` | `agent-architecture` | P0 capability and fidelity honesty architecture |
| `t_71e12e2b` | `running` | `agent-design` | P1 material microtexture and over-regularization gates |
| `t_ca23b379` | `running` | `agent-design` | P2 contact physics and functional imperfection patterns |
| `t_a1f26ac2` | `todo` | `agent-review` | Stress-test rendered-review regression gates |
| `t_b11ce30f` | `todo` | `agent-review` | Integrated Naturalism Stress Test v1 review |

Desired flow:

```text
P0 architecture + P1 design + P2 design
→ rendered-review/eval regression gate
→ independent integrated review
→ orchestrator synthesis / parent status_summary
→ PR/main or Builder/live authority gate only when explicitly authorized
```

## What worked

- Work split into specialist lanes instead of one broad implementation card.
- Review/eval lanes are explicit and dependency-linked behind implementation/design lanes.
- The parent body carries scope, findings, acceptance criteria, and a `done_requires: full_delivery_chain` policy.
- Running state is visible on child lanes, not falsely claimed on the parent.

## What must be fixed in the reusable workflow

### 1. Visible task naming

Observed titles use mixed forms such as:

```text
EPIC - Close VisualMate Naturalism & Fidelity Stress Test v1 gaps
P0 - Enforce capability and fidelity honesty before generation
P1 - Extend material-specific microtexture and over-regularization gates
P2 - Improve contact physics and functional imperfection patterns
EVAL - Add Stress Test v1 rendered-review regression gates
REVIEW - Verify integrated Naturalism Stress Test v1 remediation
```

These are readable to humans but not enough for durable multi-board automation. They do not expose `parent_task_id`, `lane_role`, or hierarchy in the title. Future cards should use the canonical title family:

```text
[EPIC] VisualMate GPT: Close Naturalism & Fidelity Stress Test v1 gaps
[SUBTASK][t_350617de][architecture] P0 enforce capability and fidelity honesty before generation
[SUBTASK][t_350617de][design] P1 extend material-specific microtexture and over-regularization gates
[SUBTASK][t_350617de][design] P2 improve contact physics and functional imperfection patterns
[SUBTASK][t_350617de][test] Add Stress Test v1 rendered-review regression gates
[SUBTASK][t_350617de][review] Verify integrated Naturalism Stress Test v1 remediation
```

Task bodies should keep the full `card_identity` block so board views, dispatchers, and agents do not infer hierarchy from chat history or assignee names.

### 2. Parent status must summarize active children

The parent epic remained `todo` while child lanes were running. That is acceptable only if the parent has a compact `status_summary` comment/body block that says:

```yaml
status_summary:
  board_ref: visualmate-gpt
  tenant: visualmate
  current_lane: parallel_implementation
  current_assignee: null
  current_state: running
  active_child_lanes:
    - task_ref: t_6084f4ae
      lane_ref: architecture
      assignee: agent-architecture
      current_state: running
      run_receipts:
        - t_6084f4ae run 87
    - task_ref: t_71e12e2b
      lane_ref: design-p1
      assignee: agent-design
      current_state: running
      run_receipts:
        - t_71e12e2b run 88
    - task_ref: t_ca23b379
      lane_ref: design-p2
      assignee: agent-design
      current_state: running
      run_receipts:
        - t_ca23b379 run 86
  last_completed_lane: null
  next_lane: rendered-review-regression-gates
  blocked_reason: null
  required_human_gate: null
  verification_evidence_refs:
    - t_6084f4ae run 87
    - t_71e12e2b run 88
    - t_ca23b379 run 86
  updated_at_ref: visualmate-gpt board capture 2026-08-02 / parent status comment pending
```

Without that summary, users see an open/todo parent and may think nothing is happening.

### 3. Hierarchy and execution dependencies must remain distinct

The active board showed the parent epic `t_350617de` with `parents: t_b11ce30f`. That pattern can be used as a parent hold in a legacy board, but it is confusing because a final review appears as the parent of the epic. New pipelines should not encode neutral hierarchy as execution dependencies. Prefer:

```text
P0/P1/P2 → eval → integrated review → synthesis child
```

The synthesis child owns the final parent status update. The epic/subtask relationship remains in `card_identity.parent_task_id`, not as an inverted dependency edge.

### 4. Tenant and board names should be explicit

The board slug is `visualmate-gpt`, while task tenant values appeared as `visualmate`. Future status and synthesis comments should report both:

```yaml
board_ref: visualmate-gpt
tenant: visualmate
project: VisualMate GPT
```

This prevents board-switch confusion when similar task IDs or VisualMate boards exist.

### 5. Review verdict names should be canonical

VisualMate review lanes used names like `PASS_FOR_MAIN_PR` and `BLOCKED_EVIDENCE`. Reusable automation should normalize them to the fleet contract:

```text
PASS_FOR_NEXT_LANE
NEEDS_SPECIALIST_REMEDIATION
BLOCKED_AUTHORITY
FAILED_REVIEW_PROTOCOL
```

Project-specific labels may appear as aliases, but the durable metadata must include the canonical verdict.

## Required reusable workflow changes

- Add this VisualMate board pattern as a regression/eval case in `hermes-task-management-workflow`.
- Require visible `[EPIC]`, `[SUBTASK][parent][lane]`, and `[TASK]` title prefixes for new/reconciled cards.
- Require parent `status_summary` when children are running or waiting.
- Treat inverted final-review → epic edges as a legacy hold pattern that must be reported clearly or replaced by a synthesis child.
- Include board slug plus tenant in status replies.
- Normalize review verdicts to the canonical fleet contract.

## Acceptance implication

The VisualMate GPT run is evidence for the reusable task workflow because it exposed exactly where local/project-specific habits can confuse future agents. The fix belongs in `ai-native-skills` so new Hermes fleets can replicate the workflow instead of learning it from this one local board history.
