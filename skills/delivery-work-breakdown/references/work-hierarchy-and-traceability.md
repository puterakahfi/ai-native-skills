# Work Hierarchy and Traceability

## Canonical hierarchy

```text
product release
└── epic
    ├── feature
    │   ├── task
    │   ├── spike
    │   └── bug
    └── feature
```

The hierarchy describes delivery ownership and acceptance—not team seniority or code folder structure.

## Required traceability

Every child records:

```yaml
work_item_id: <tracker ref>
work_item_type: <epic | feature | task | spike | bug>
parent_ref: <required for non-root>
acceptance_criteria_refs:
  - <parent criterion id>
dependencies:
  - <work item ref>
independently_releasable: <true | false | unknown>
verification_scope:
  - <observable evidence>
```

## Decomposition rules

- Epics own end-to-end acceptance and release integration.
- Features own independently reviewable behavior slices.
- Tasks implement bounded parts of a feature and do not become floating releases.
- Spikes answer one uncertainty and return evidence/verdict; spike code is not silently shipped.
- Bugs preserve the release boundary in which they are discovered unless an attributable product decision reclassifies them.
- A child may support more than one parent criterion, but it has one governing parent.
- Dependency cycles block execution until resolved or explicitly restructured.

## Acceptance mapping

```yaml
epic_criterion:
  id: EPIC-AC-03
  statement: Native generation remains on the user ChatGPT boundary
  children:
    - FEATURE-HANDOFF
    - TASK-COST-INSTRUMENTATION
    - TASK-RUNTIME-PROOF
  evidence_composition:
    - tool contract evidence
    - runtime network evidence
    - end-to-end ChatGPT evidence
```

Child completion is necessary but may not be sufficient for the parent criterion. The epic acceptance plan states how evidence composes.

## Orphan detection

Block when any non-root item has:

- no parent;
- no acceptance-criterion reference;
- unknown release unit;
- no base branch or PR target while repository execution is requested;
- dependencies that refer to missing items;
- a branch target that bypasses its parent release unit.
