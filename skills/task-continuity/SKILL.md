---
name: task-continuity
description: Preserve verified task direction across fresh chats, agent handoffs, runtime changes, and interrupted work. Create source-backed checkpoints and portable handoffs, verify current issue/repository/branch/PR state before resume, detect stale or conflicting context, and prevent false completion.
license: MIT
metadata:
  ai-native-skills.version: 1.0.0
  ai-native-skills.author: puterakahfi
  ai-native-skills.type: skill
  ai-native-skills.implements: ai-native-core/contracts/skills/context/task-continuity.contract.yaml
  ai-native-skills.contract-version: "~0.1"
  ai-native-skills.boundary.covers: '["source_backed_task_checkpoint_creation","portable_cross_session_handoff_creation","checkpoint_freshness_and_supersession_evaluation","current_source_verification_before_resume","continuity_gap_staleness_and_conflict_classification","status_semantic_preservation_across_handoff","exact_next_action_definition","continuity_closure_evaluation","durable_knowledge_promotion_request_for_official_chat_only_decisions"]'
  ai-native-skills.boundary.delegates: '["chat_transcript_storage","provider_specific_memory_api_implementation","product_specific_checkpoint_persistence","repository_issue_branch_or_pull_request_mutation","task_implementation_or_execution","evidence_generation_or_gate_evaluation","review_or_approval_execution","delivery_merge_or_product_acceptance_authority","learning_candidate_evaluation_or_promotion","product_specific_source_priority_policy"]'
  ai-native-skills.related_skills: '["context-manager","context-engineering","decision-provenance","implementation-context-discovery","workflow-router","git-workflow","skill-evolution"]'
---

# Task Continuity

```text
conversation memory → retrieval hint only
current sources      → verified task state
verified task state  → checkpoint | handoff | resume | close
```

Preserve where work actually is, not merely what a previous conversation remembered.

## Load when

- the user asks to continue in a fresh chat or session;
- work moves to another agent, runtime, model, machine, or teammate;
- a task was interrupted and must resume safely;
- a checkpoint, summary, memory, or handoff may be stale;
- the agent must state what is done, pending, blocked, or next;
- continuity is closing and official decisions must leave chat memory.

Do not load only to summarize a conversation with no continuing task.

## Core rule

```text
Memory helps recover context.
Authoritative sources establish task state.
```

Never continue from chat history alone when repository, issue, branch, PR, artifact, validation, review, approval, delivery, or acceptance state is material.

## Ownership

`task-continuity` owns checkpoint, handoff, resume verification, stale/conflict classification, exact next action, and continuity closure.

It composes with:

- `context-manager` for the execution context pack;
- `context-engineering` for durable rules and documentation;
- `decision-provenance` for authority and supersession;
- the governing workflow for actual execution;
- independent review, approval, delivery, and product-acceptance owners;
- a Native AI OS or product adapter for persistence.

## Operating modes

| Mode | Trigger | Output |
|---|---|---|
| `checkpoint` | Save current work state | `task_continuity_checkpoint` |
| `handoff` | Move work to another session or agent | `session_handoff` |
| `resume` | Continue from prior state | `resume_context` + verdict |
| `close` | End or stop the continuity chain | `closure_record` |

A request may compose `checkpoint → handoff` or `resume → checkpoint`. This skill never becomes the implementation workflow.

## Source priority

Use the product-defined hierarchy. When none is explicit, disclose and apply:

```text
latest explicit governing instruction
→ active issue and acceptance criteria
→ accepted contracts and ADRs
→ current repository, branch, commit, and PR evidence
→ current artifacts, tests, gates, reviews, approvals, and delivery records
→ previous checkpoint or handoff
→ conversation memory
→ assumptions
```

Assumptions never become verified checkpoint facts.

## Status semantics

Keep these distinct:

```text
planned → attempted → implemented → verified → gate passed
→ reviewed → approved → delivered → merged → accepted
```

Examples:

- changed files may support `implemented`;
- a passing build supports that named validation only;
- a screenshot is an artifact, not automatic visual acceptance;
- a reviewer verdict is not product approval;
- a merged PR is not automatically released or accepted;
- deployment success is delivery evidence, not product acceptance.

Never use `done` without naming the strongest evidence-supported state.

## Checkpoint procedure

1. Resolve product and task identity.
2. Verify repository, issue, branch, PR, and artifact references when applicable.
3. Restate objective and acceptance criteria from governing sources.
4. Partition state into planned, attempted, implemented, verified, pending, blocked, and abandoned.
5. Record decisions with provenance and authority.
6. Link changed files, commits, artifacts, commands, tests, and exact results.
7. Disclose failures, missing evidence, blockers, and risks.
8. Define exactly one next action and its expected evidence.
9. Record checkpoint version, observed time, source revisions, and supersession.

Load [checkpoint schema](references/checkpoint-schema.md) for a full artifact.

A checkpoint is invalid when it lacks a governing task, sources, status separation, pending gates, freshness metadata, or one exact next action.

## Handoff procedure

A handoff must work without the prior transcript and include:

```text
checkpoint reference and version
authoritative sources to load
objective and acceptance criteria
verified current state
pending, blocked, and NOT_VERIFIED state
decisions and provenance
artifacts and validation evidence
warnings and stale conditions
one next exact action
expected evidence from that action
```

Load [handoff quality gates](references/handoff-quality-gates.md) for cross-agent or cross-runtime movement.

`Continue as discussed` is not a valid handoff.

## Resume procedure

Resume is a verification gate:

```text
1. Load latest candidate checkpoint.
2. Resolve current governing sources.
3. Compare identity, objective, acceptance criteria, versions, and statuses.
4. Classify missing, stale, superseded, and conflicting state.
5. Refresh the context pack.
6. Issue a continuity validation verdict.
7. Continue only when required context is sufficient.
```

Allowed verdicts:

- `VALID`
- `VALID_WITH_WARNINGS`
- `STALE_REFRESH_REQUIRED`
- `CONFLICT_RESOLUTION_REQUIRED`
- `MISSING_CONTEXT`
- `BLOCKED`

Rules:

- current authoritative sources override an older checkpoint;
- a newer timestamp alone does not prove higher authority;
- do not repeat work already verified complete;
- do not skip pending validation, review, approval, delivery, or acceptance;
- missing branch, PR, commit, or artifact evidence remains `NOT_VERIFIED`;
- conflicting objective or acceptance criteria blocks execution.

Load [resume protocol](references/resume-protocol.md) when multiple sources or conflicts are involved.

## Close procedure

Close continuity only when the task is completed with evidence, stopped with remaining work, cancelled, superseded, or blocked.

Before closure:

1. state the terminal condition precisely;
2. disclose remaining work, failures, and risks;
3. preserve review, approval, delivery, merge, and acceptance as separate states;
4. link final and superseded checkpoints;
5. route official chat-only decisions into durable repository knowledge or a promotion request;
6. delegate reusable learning to `skill-evolution`.

Closure never means product acceptance without explicit authority evidence.

## Gap classifications

| Finding | Meaning | Route |
|---|---|---|
| `IDENTITY_MISSING` | Product/task/repository identity unresolved | Resolve or block |
| `SOURCE_UNAVAILABLE` | Required source cannot be inspected | `NOT_VERIFIED` |
| `STALE_CHECKPOINT` | Source revision changed | Refresh |
| `SUPERSEDED_CHECKPOINT` | Newer explicit continuity state exists | Preserve history; use successor |
| `STATUS_CONFLICT` | Checkpoint and current source disagree | Resolve authority |
| `SCOPE_CONFLICT` | Objective or acceptance criteria changed | Re-plan from governing source |
| `FALSE_COMPLETION_RISK` | Claimed state exceeds evidence | Downgrade |
| `HANDOFF_INCOMPLETE` | Next action or evidence missing | Repair handoff |
| `DURABLE_KNOWLEDGE_GAP` | Official decision exists only in chat | Promotion request |

## Required verdict output

```yaml
continuity_validation:
  verdict: VALID | VALID_WITH_WARNINGS | STALE_REFRESH_REQUIRED | CONFLICT_RESOLUTION_REQUIRED | MISSING_CONTEXT | BLOCKED
  checkpoint_ref: ""
  verified_sources: []
  stale_sources: []
  conflicts: []
  missing_context: []
  warnings: []
  next_exact_action: ""
  expected_evidence: []
```

## Quality gates

- [ ] Memory is retrieval help, not authority.
- [ ] Material claims are source-backed or `NOT_VERIFIED`.
- [ ] Objective and acceptance criteria come from governing sources.
- [ ] Status states remain distinct.
- [ ] Freshness and supersession are explicit.
- [ ] Missing or conflicting context is never invented.
- [ ] Resume verifies current sources before execution.
- [ ] Completed work is not repeated and pending gates are not skipped.
- [ ] Handoff works without the prior transcript.
- [ ] Exactly one next action is named.
- [ ] Chat-only official decisions are routed to durable knowledge.
- [ ] Closure does not imply unsupported authority or acceptance.

## Handoff to execution

```text
task-continuity → context-manager → governing workflow → implementation or review
```

This skill does not mutate repositories, implement work, review, approve, merge, deploy, accept, or promote learning.
