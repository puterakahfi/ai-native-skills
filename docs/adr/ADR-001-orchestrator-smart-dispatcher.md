# ADR-001: Orchestrator as Smart Dispatcher

**Date**: 2026-07-31
**Status**: ACCEPTED
**Author**: puterakahfi

## Context

agent-orchestrator was behaving as an implementor — reading 10-16 files before dispatching,
exhausting iteration budget (30/30), and double-investigating files that specialist agents
would re-read anyway.

## Decision

Orchestrator scope is limited to:
1. Scope identification only (max 5 tool calls): identify component, entry point filenames, risk
2. Always dispatch to specialist for implementation (except trivial 1-line hotfixes)
3. No file content reads before dispatching

## Changes applied

- SOUL.md agent-orchestrator: added Smart Dispatcher section with explicit DO/DO NOT rules
- config.yaml agent-orchestrator: max_turns raised from 30 to 60
- workflow-router: enforce dispatch for single_task non-hotfix (pending)

## How to apply on a new machine

Via Hermes chat (agent-orchestrator profile):
```
/hermes-agent-fleet-bootstrap bootstrap native-ai-engineering --apply
```

Or via terminal (full path to script):
```bash
bash "/home/<user>/.hermes/profiles/agent-orchestrator/skills/hermes-agent-fleet-bootstrap/scripts/hermes_fleet.py" \
  bootstrap native-ai-engineering --apply
```

Note: `hermes-fleet` is NOT a standalone CLI command — it runs through the skill script.

## Consequences

- Specialist agents receive bounded context (component + entry point + acceptance criteria)
- Specialist agents do their own deep investigation
- Orchestrator iteration budget no longer exhausted on investigation
- Pipeline can complete within budget for typical epic (3 workers + review)
