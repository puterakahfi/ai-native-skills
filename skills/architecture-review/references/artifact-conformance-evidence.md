# Artifact Conformance Evidence

Use this reference when repository implementation claims must be checked against actual files rather than an agent summary alone.

## Required boundary

```text
implementation-context profile and convention locks
+ actual artifact root, changed paths, imports, dependencies, and token/style usage
+ bounded artifact assertions or equivalent inspectable evidence
→ architecture-review compliance verdict
```

Text that says “uses the canonical stack” is decision narrative, not artifact proof. A compiling artifact can still contain a local Dialog, a second icon family, a route-local theme grammar, deprecated imports, or paths that contradict the approved mapping.

## Evidence report

```yaml
artifact_conformance_evidence:
  artifact_ref: <commit, fixture, PR head, or immutable path>
  implementation_context_profile_ref: <ref>
  convention_locks_checked: []
  expected_paths_and_imports: []
  observed_paths_and_imports: []
  dependency_manifest_findings: []
  copied_or_vendored_system_findings: []
  component_and_variant_findings: []
  styling_token_and_typography_findings: []
  iconography_findings: []
  state_form_query_and_data_findings: []
  prohibited_parallel_system_findings: []
  assertion_results: []
  missing_evidence: []
  status: PASS | FAIL | PARTIAL | NOT_VERIFIED
```

## Classification

```text
CONVENTION_DRIFT
  a fit canonical component, variant, token, path, or wrapper is bypassed

DEPENDENCY_DRIFT
  an unauthorized package, copied library, icon family, or parallel system appears

STACK_CONTEXT_MISSING
  the artifact cannot be compared to a verified implementation-context profile

IMPLEMENTATION_DEFECT
  the approved mapping is followed but the code or behavior is incorrect
```

Missing artifact roots, files, imports, or validator evidence remain `NOT_VERIFIED`/`INCOMPLETE`; they are never converted to PASS by a narrative. Artifact assertions prove static artifact properties only. Runtime, rendered, interaction, accessibility, performance, and security acceptance still require their governing evidence.
