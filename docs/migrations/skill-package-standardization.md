# Skill Package Standardization Migration

Parent epic: #169.

## Rollout

1. Validate the pilot skills `test-driven-development`, `workflow-router`, and `skill-evolution` as blocking.
2. Produce a repository-wide inventory as CI evidence.
3. Treat warnings as migration debt, not compliance.
4. Apply blocking validation to new and materially changed skills.
5. Migrate existing skills by risk, workflow centrality, executable behavior, and regression impact.

## Compliance statuses

- `COMPLIANT`: no package-policy errors or warnings and applicable behavioral evidence exists.
- `PARTIALLY_COMPLIANT`: no blocking error, but migration warnings remain.
- `NEEDS_MIGRATION`: one or more blocking package-policy errors exist.
- `EXEMPT`: reviewed exemption with rationale, owner, and review condition.
- `BLOCKED`: migration cannot proceed because an authority, dependency, or required evidence is unavailable.
- `NOT_VERIFIED`: evidence was not produced or cannot be checked.

## Evidence

Run:

```bash
python scripts/validate-skill-packages.py \
  --report-json .tmp/skill-package-validation/report.json
```

The generated report is the inventory for the evaluated revision. It must remain outside authored skill directories and be uploaded as CI evidence.

## Priority order

1. meta-skills and workflow routers;
2. skills that own acceptance, review, security, or quality gates;
3. skills with bundled executable resources;
4. skills required by multiple workflows;
5. remaining specialist and reference-heavy skills.

No skill is considered compliant merely because its files exist. Structural validation, behavioral evidence, applicable executable tests, and review remain distinct.
