---
name: task-continuity
description: Preserve task direction across fresh chats, agent handoffs, runtime changes, and interrupted work. Creates source-backed checkpoints and portable handoffs, verifies current issue/repository/branch/PR state before resume, detects stale or conflicting context, and prevents false completion when implementation, validation, review, approval, delivery, merge, or acceptance are still distinct.
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
conversation memory
  → retrieval hint only

current source of truth
  → verified task state

verified task state
  → checkpoint | handoff | resume | close
```

Task continuity preserves **where the work actually is**, not merely what the previous conversation remembered.

## Load when

- the user says to continue work in a new chat or fresh session;
- the current conversation is too long and needs a clean handoff;
- work moves to another agent, runtime, model, machine, or teammate;
- a task was interrupted and must be resumed safely;
- a prior checkpoint, summary, memory, or handoff may be stale;
- the agent must explain what is done, pending, blocked, or next;
- a task is closing and official decisions must leave chat memory.

Do not load only to summarize a conversation with no continuing task.

## Core rule

```text
Memory helps recover context.
Sources of truth establish task state.
```

Never continue from chat history alone when repository, issue, branch, PR, artifact, validation, review, approval, or delivery state is material.

## Ownership

```text
task-continuity
  checkpoint, handoff, resume verification,
  staleness/conflict classification, exact next action, closure

context-manager
  resolve the complete context pack required before execution

context-engineering
  author durable AGENTS.md, contracts, rules, and context templates

decision-provenance
  verify authority, scope, supersession, and conflict of decisions

governing workflow / implementation agent
  perform the actual task

review, approval, delivery, and product authority
  own their distinct outcomes

Native AI OS or product adapter
  persist and query checkpoints
```

## Four operating modes

Classify the request before producing output:

| Mode | Trigger | Output |
|---|---|---|
| `checkpoint` | Save current work state | `task_continuity_checkpoint` |
| `handoff` | Move work to another session or agent | `session_handoff` |
| `resume` | Continue from prior state | `resume_context` + verdict |
| `close` | End or stop the continuity chain | `closure_record` |

A request may require `checkpoint → handoff` or `resume → checkpoint`, but do not turn this skill into the implementation workflow itself.

## Source priority

Use the product-defined source hierarchy. When no product hierarchy is explicit, apply this conservative order and disclose it:

```text
latest explicit governing instruction
→ active issue and acceptance criteria
→ accepted product/core contracts and ADRs
→ current repository, branch, commit, and PR evidence
→ current artifacts, tests, gates, reviews, approvals, and delivery records
→ previous checkpoint or handoff
→ conversation memory
→ assumptions
```

Assumptions never become verified checkpoint facts.

Load [`references/resume-protocol.md`](references/resume-protocol.md) when current state must be revalidated across multiple sources or conflicts exist.

## Status semantics

Keep these states separate:

```text
planned
attempted
implemented
verified
gate passed
reviewed
approved
delivered
merged
accepted
```

Examples:

- changed files exist → may support `implemented`;
- build passed → supports a named validation result, not design approval;
- screenshot exists → artifact available, not automatically visually accepted;
- reviewer found no blockers → review result, not product approval;
- PR merged → merged, not automatically released or accepted;
- deployment succeeded → delivery evidence, not product acceptance.

Never use `done` without stating the strongest evidence-supported state.

## Mode 1 — Checkpoint

### Procedure

1. Resolve product and task identity.
2. Verify repository, issue, branch, and PR references when applicable.
3. Restate the objective and active acceptance criteria from governing sources.
4. Partition work into planned, attempted, implemented, verified, pending, blocked, and abandoned.
5. Record decisions with provenance and authority.
6. Link changed files, commits, artifacts, commands, tests, and exact results.
7. Disclose failures, missing evidence, blockers, and risks.
8. Define **one next exact action** and the evidence expected from it.
9. Record checkpoint version, observed time, source revisions, and supersession.

Load [`references/checkpoint-schema.md`](references/checkpoint-schema.md) when creating a full checkpoint artifact.

### Gate

A checkpoint is invalid when it:

- says only “continue later”;
- has no governing task reference;
- collapses implementation into verification or acceptance;
- copies memory claims without sources;
- omits known failures or pending gates;
- has no exact next action;
- lacks freshness/version information.

## Mode 2 — Handoff

A handoff must work **without the prior transcript**.

Required contents:

```text
checkpoint reference and version
authoritative sources to load
objective and acceptance criteria
verified current state
pending, blocked, and not-verified state
accepted and provisional decisions
artifacts and validation evidence
warnings and stale conditions
one next exact action
expected evidence from that action
```

Use [`references/handoff-quality-gates.md`](references/handoff-quality-gates.md) for cross-agent and cross-runtime handoffs.

### Bad

```text
Lanjutkan refinement seperti obrolan sebelumnya.
```

### Good

```text
Open issue #78 and branch 78-add-task-continuity-skill.
Verify the current Core contract ref, then run the skill package validator.
Expected evidence: validator command, exit status, and any exact failing path.
```

## Mode 3 — Resume

Resume is not “load summary and continue.” It is a verification gate.

### Ordered procedure

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

### Resume rules

- current authoritative sources override an older checkpoint;
- a newer timestamp alone does not prove higher authority;
- do not repeat work already verified complete;
- do not skip pending validation, review, approval, delivery, or acceptance;
- missing branch/PR/commit evidence remains `NOT_VERIFIED`;
- conflicting objective or acceptance criteria blocks execution;
- refresh `context-manager` output before task handoff when the context pack changed.

## Mode 4 — Close

Close continuity when the task is completed, stopped, cancelled, superseded, or blocked indefinitely.

Before closure:

1. State the terminal task condition precisely.
2. Record remaining work, known failures, and risks.
3. Preserve separate review, approval, delivery, merge, and acceptance states.
4. Link the final checkpoint and superseded versions.
5. Promote official chat-only decisions to durable repository knowledge or create an explicit promotion request.
6. Delegate reusable learning to `skill-evolution` or the governed learning workflow.

Allowed closure states:

```text
COMPLETED_WITH_EVIDENCE
STOPPED_WITH_REMAINING_WORK
CANCELLED
SUPERSEDED
BLOCKED
```

Closure never means product acceptance unless explicit authority evidence says so.

## Continuity gap classifications

| Finding | Meaning | Route |
|---|---|---|
| `IDENTITY_MISSING` | Product/task/repo identity unresolved | Resolve sources; block if required |
| `SOURCE_UNAVAILABLE` | Required source cannot be inspected | Mark `NOT_VERIFIED` |
| `STALE_CHECKPOINT` | Source revision changed after checkpoint | Refresh checkpoint |
| `SUPERSEDED_CHECKPOINT` | Newer explicit continuity state exists | Preserve history; use successor |
| `STATUS_CONFLICT` | Checkpoint and current source disagree | Resolve authority; block if material |
| `SCOPE_CONFLICT` | Objective or acceptance criteria changed | Re-plan from governing source |
| `FALSE_COMPLETION_RISK` | Evidence does not support claimed state | Downgrade to supported status |
| `HANDOFF_INCOMPLETE` | Next action or required evidence missing | Repair handoff |
| `DURABLE_KNOWLEDGE_GAP` | Official decision exists only in chat/memory | Create promotion request |

## Required outputs

### Continuity validation verdict

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

### Compact handoff summary

```text
repository
issue
active_branch
pull_request
objective
acceptance_criteria
completed_with_evidence
in_progress
pending
blocked
decisions_and_provenance
artifacts_and_validation
known_failures_and_risks
next_exact_action
expected_evidence
checkpoint_version
observed_at
continuity_verdict
```

## Quality gates

- [ ] Conversation history and model memory are retrieval aids, not authority.
- [ ] Material status claims are source-backed or `NOT_VERIFIED`.
- [ ] Objective and acceptance criteria come from governing sources.
- [ ] Planned, attempted, implemented, verified, reviewed, approved, delivered, merged, and accepted remain distinct.
- [ ] Checkpoint version, freshness, and supersession are explicit.
- [ ] Missing and conflicting context is reported, never invented.
- [ ] Resume verifies current sources before execution.
- [ ] Completed work is not repeated and pending gates are not skipped.
- [ ] Handoff works without the prior transcript.
- [ ] Exactly one concrete next action is named.
- [ ] Official chat-only decisions are routed to durable knowledge.
- [ ] Closure does not imply unsupported authority or acceptance.

## Failure signals

Stop or downgrade the verdict when:

- repository, issue, branch, PR, or checkpoint identity cannot be resolved;
- required source access is missing;
- checkpoint and current acceptance criteria conflict;
- a branch or artifact is claimed but cannot be found;
- status language exceeds its evidence;
- the next action is vague or repeats completed work;
- the task is marked complete while required validation or governance remains pending.

## Handoff to execution

This skill ends by supplying verified continuity state to:

```text
context-manager
→ governing workflow
→ implementation or review capability
```

It does not perform repository mutations, implementation, review, approval, merge, deployment, acceptance, or learning promotion.
