# MCP Tool and Resource Contracts

Load this reference when defining, reviewing, or changing the MCP surface of a ChatGPT App.

## Contract-first rule

Define the callable surface before implementing handlers or widgets.

Each tool should answer:

```text
What user intent triggers it?
Who owns the concept?
What exact input is required?
What structured result is returned?
Does it read, write, delete, call an open world, or render UI?
What authentication and authorization are required?
Can it be retried safely?
How are expected failures represented?
Which UI resource, if any, renders the result?
```

## One job per tool

Good:

```text
list_brand_profiles
get_identity_lock
analyze_creative_brief
build_production_context
save_workflow
create_revision
render_workflow
```

Bad:

```text
do_everything
manage_visualmate
analyze_generate_save_and_publish
```

A tool that mixes a read with an external write or destructive action makes consent, retries, observability, and testing ambiguous.

## Read, write, render, and generation boundaries

```text
Read tool
  returns data without changing external state

Write tool
  changes product or external state and declares the effect

Render tool/resource
  presents structured data; it does not own business policy

Native capability handoff
  prepares context and returns execution to ChatGPT

Developer-paid generation tool
  calls a provider using declared developer/customer credentials
```

Do not label a developer-paid generation tool as a render tool or native handoff.

## Tool specification template

```yaml
tool:
  name: build_production_context
  purpose: Build an approved, structured generation context from a validated creative brief.
  owner_module: creative-workflow
  auth: optional | required
  side_effect: read-only | write | destructive | open-world
  idempotency: safe | key-required | not-retryable
  input:
    required: []
    optional: []
    constraints: []
  output:
    schema_version: "1"
    structured_fields: []
    human_summary: required
  expected_errors: []
  ui_resource: ui://widget/production-context-v1.html | none
  observability:
    correlation_id: required
    sensitive_fields_redacted: true
```

Use the current Apps SDK/MCP schema and annotation names from official documentation when implementing. Do not preserve outdated field names merely because they appear in an old example.

## Description quality

The model routes tools from metadata. Descriptions should state:

- the user intent;
- what the tool does;
- important prerequisites;
- what it does not do when ambiguity is likely.

Example:

```text
Use this tool after a creative brief has been normalized and the user needs a structured production context. It does not generate an image, save a workflow, or modify brand assets.
```

Avoid marketing copy and vague verbs such as "enhance", "optimize everything", or "handle design".

## Inputs

Inputs should be explicit and minimal.

Prefer:

```json
{
  "brief_id": "brief_123",
  "workflow_type": "social_feed",
  "brand_profile_id": "brand_42",
  "output_ratio": "4:5"
}
```

Avoid passing an unbounded conversation dump when stable IDs and structured fields exist.

Rules:

- validate enums, IDs, lengths, and formats;
- separate user text from trusted system/configuration fields;
- do not accept credentials in ordinary tool input;
- version long-lived structured contracts;
- mark optional values honestly;
- reject unknown destructive scope rather than guessing.

## Outputs

Return structured data for the model and a concise human-readable summary.

A useful result separates:

```text
structuredContent
  stable machine-readable result used by the model/widget

content
  concise explanation for the conversation

metadata
  UI-only or operational fields that should not be treated as user-visible facts
```

Follow the current Apps SDK rules for which fields are visible to the model and widget. Do not place secrets, access tokens, internal prompts, or sensitive raw records in tool results or UI metadata.

## Expected failures

Represent expected business and validation failures predictably:

```yaml
error:
  code: BRAND_PROFILE_NOT_FOUND
  message: The selected brand profile is unavailable.
  retryable: false
  recovery:
    action: list_brand_profiles
```

Unexpected infrastructure failures remain exceptions and are logged with correlation IDs. Do not expose stack traces or provider secrets.

## Idempotency and retries

Read operations should normally be retry-safe.

Write operations should declare one of:

- deterministic idempotency key;
- optimistic version/revision check;
- explicit non-retryable behavior;
- compensating action where justified.

Generation or payment-like provider calls require duplicate prevention because network retries may create repeated cost or output.

## Authentication and authorization

Tool discovery does not equal permission.

For every protected tool specify:

- identity source;
- required scope;
- resource ownership check;
- workspace/tenant boundary;
- confirmation policy for important actions;
- audit event;
- denial result.

A valid OAuth token does not authorize access to every object referenced by user-supplied IDs.

## UI resource binding

A tool that renders UI should point to a versioned UI resource.

```text
ui://widget/workflow-summary-v1.html
```

Version the resource when structural expectations change. Keep the widget compatible with the tool's structured output version.

Do not make rendering a hidden side effect of a write tool when the same write must also work without the widget.

## Tool inventory review

For each proposed tool verify:

- [ ] one clear job;
- [ ] trigger-focused description;
- [ ] owner module is explicit;
- [ ] input schema is minimal and validated;
- [ ] structured result is versioned where necessary;
- [ ] annotations match real effects;
- [ ] auth and object authorization are explicit;
- [ ] retries and idempotency are defined;
- [ ] expected errors have recovery guidance;
- [ ] UI resource binding is versioned;
- [ ] observability does not leak sensitive data;
- [ ] no hidden model/image API call exists;
- [ ] no product business rule lives only in the handler.

## Contract tests

At minimum test:

```text
valid request
missing required input
invalid enum or identifier
unauthenticated request
authenticated but unauthorized object
expected domain failure
infrastructure timeout
retry behavior
write confirmation boundary
structured output compatibility
widget resource resolution
annotation accuracy
no hidden developer API call on native handoff path
```
