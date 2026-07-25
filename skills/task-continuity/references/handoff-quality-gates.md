# Task Continuity Handoff Quality Gates

A continuity handoff must be usable without the previous transcript.

## Required content

```text
checkpoint reference and version
authoritative sources to load
objective and acceptance criteria
verified current state
pending, blocked, and NOT_VERIFIED state
decisions with provenance
artifacts and exact validation results
stale conditions and warnings
one next exact action
expected evidence from that action
```

## Gate checklist

- [ ] Product, task, repository, issue, branch, and PR identity are explicit when applicable.
- [ ] Current state is separated into implemented, verified, reviewed, approved, delivered, merged, and accepted.
- [ ] Every material state claim has an evidence reference or `NOT_VERIFIED`.
- [ ] Missing access and unresolved conflicts are disclosed.
- [ ] Completed work is not queued again.
- [ ] Pending validation or governance is not skipped.
- [ ] Exactly one next action is executable from the listed sources.
- [ ] Expected evidence is concrete: command output, artifact, review verdict, approval, deployment health, or acceptance record.
- [ ] Freshness and supersession metadata are included.
- [ ] The handoff does not depend on phrases such as “as discussed earlier.”

## Verdicts

```text
HANDOFF_VALID
  all required sections and evidence boundaries are present

HANDOFF_VALID_WITH_WARNINGS
  usable, but named non-blocking sources are unavailable or stale

HANDOFF_INCOMPLETE
  identity, source, next action, or expected evidence is missing

HANDOFF_BLOCKED
  a material source conflict or unresolved authority prevents safe continuation
```

## Bad handoff

```text
Continue the refinement from our previous discussion.
```

## Acceptable handoff

```text
Open issue #78 and the active task-continuity branch.
Verify the current Core contract revision and the branch CI state.
Next exact action: run the contract-backed adapter checks on the exact branch head.
Expected evidence: workflow run IDs, conclusions, and exact failing step when non-green.
```

A handoff is not improved by adding more prose. It is improved by source identity, state precision, and an executable next action.
