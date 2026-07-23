# Task Continuity

Use `task-continuity` when active work must survive a fresh chat, agent handoff, runtime change, machine change, or interrupted execution.

## What it solves

```text
long or exhausted conversation
agent or runtime handoff
stale checkpoint or summary
missing branch, PR, commit, artifact, or validation evidence
memory that conflicts with the active issue
false completion caused by collapsed statuses
```

## Operating modes

```text
checkpoint
  Capture evidence-supported current task state.

handoff
  Produce a portable package that does not depend on the prior transcript.

resume
  Compare the latest checkpoint with current authoritative sources before execution.

close
  End the continuity chain without inferring review, approval, merge, delivery, or acceptance.
```

## Composition

```text
task-continuity
→ context-manager
→ governing workflow
→ implementation or review capability
```

Use `context-engineering` when durable repository context must be authored or repaired. Use `decision-provenance` when source authority, supersession, scope, or decision conflicts require deeper verification.

## Required result

Every valid handoff or resume must state:

- product and task identity;
- repository, issue, branch, and PR references when applicable;
- governing objective and acceptance criteria;
- evidence-supported completed, pending, and blocked work;
- known failures and risks;
- one exact next action;
- the evidence expected from that action;
- checkpoint version, freshness, supersession, and continuity verdict.

Conversation memory may help locate context, but it must not establish authoritative task state.

## Validation boundary

Structural skill validation, repository eval-contract validation, generated capability inventory, Core contract compatibility, adapter conformance, and behavioral application are separate evidence layers.

A structurally valid skill or passing synthetic eval output does not prove that a runtime naturally activated and applied task continuity. Fresh-session behavioral evidence remains required before claiming full runtime effectiveness.
