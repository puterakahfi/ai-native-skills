# Runtime Instruction Limits

This reference stores provider or workspace capacity constraints used by `project-instruction-generator`.

Limits are runtime facts, not universal Native AI contracts. Keep them outside the reusable policy body and update them only with explicit provenance.

## Verification States

| State | Meaning |
|---|---|
| `VERIFIED_DOCUMENTATION` | An authoritative provider source publishes the limit. |
| `VERIFIED_RUNTIME_OBSERVATION` | The provider UI or API directly rejects or accepts content at the stated boundary. |
| `NOT_VERIFIED` | No credible limit has been established. Do not guess. |

A runtime observation may be used for execution, but its provenance must state that it is observed rather than officially documented.

## Profiles

### ChatGPT Projects

```yaml
runtime_id: chatgpt-projects
instruction_character_limit: 8000
instruction_target_budget: 7200
safety_margin: 800
verification_state: VERIFIED_RUNTIME_OBSERVATION
provenance:
  observed_at: 2026-07-23
  evidence: ChatGPT Project Settings rejected Project Instructions above 8,000 characters
  official_documentation: OpenAI Help documents Project Instructions but did not expose a numeric character limit during verification
counting:
  normalize_line_endings: LF
  preflight_unit: Unicode code points
  runtime_ui_is_authoritative: true
```

Rules:

- `count <= 7,200`: `PASS`
- `7,200 < count <= 8,000`: `NEEDS_WORK`; likely accepted, but safety margin is insufficient
- `count > 8,000`: `FAIL`; the artifact is not paste-ready
- report exact count and remaining hard budget
- keep the UI validator authoritative because provider counting behavior can change

### Claude Projects or Project Instructions

```yaml
runtime_id: claude-projects
instruction_character_limit: null
verification_state: NOT_VERIFIED
```

Do not reuse ChatGPT's limit. Resolve from an authoritative Anthropic source or direct runtime validation before claiming platform acceptance.

### X, Meta, Gemini, and Other Workspaces

```yaml
runtime_id: other-platform
instruction_character_limit: null
verification_state: NOT_VERIFIED
```

Do not infer a limit from model context windows, prompt-token limits, social-post limits, custom-instruction limits, or another provider's workspace.

## Profile Update Rules

Update or add a profile only when:

1. the exact runtime surface is identified;
2. the limit applies to the instruction field being generated;
3. provenance is recorded;
4. date and verification state are included;
5. conflicting evidence is disclosed;
6. regression evals are updated when behavior changes.

Revalidate a profile whenever provider documentation, UI behavior, API behavior, or the target instruction surface changes.

Do not promote provider-specific limits into `ai-native-core` unless a future provider-neutral contract needs a generic capacity interface.
