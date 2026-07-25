# Task Continuity

`task-continuity` preserves verified task direction across fresh chats, agents, runtimes, and interrupted execution.

```text
checkpoint → portable handoff → current-source verification → resume or block → close
```

## Use it for

- moving active work into a fresh chat;
- handing work to another agent or runtime;
- safely resuming an interrupted task;
- reconciling a checkpoint with current GitHub or product state;
- closing a task without converting implementation or merge into unsupported acceptance.

## Install

```bash
npx skills add puterakahfi/ai-native-skills@task-continuity -g -y
```

Natural requests such as “continue this work in a new chat,” “prepare a handoff,” and “resume the previous task” should route through `workflow-router` into `task-continuity` before the original governing lifecycle resumes.

## Evidence boundary

The capability verifies and packages state. It does not:

- store chat transcripts;
- implement product persistence;
- mutate repositories or issue trackers;
- execute the task;
- perform review, approval, merge, deployment, or product acceptance;
- promote reusable learning automatically.

Those responsibilities remain with runtime/product adapters, governing workflows, reviewers, authorized owners, and `skill-evolution`.

## Core contract

The executable adapter implements:

```text
ai-native-core/contracts/skills/context/task-continuity.contract.yaml@~0.1
```

The contract keeps planned, attempted, implemented, verified, reviewed, approved, delivered, merged, and accepted states distinct.
