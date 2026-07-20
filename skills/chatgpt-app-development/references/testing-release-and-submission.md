# Testing, Deployment, and Publication Readiness

Load this reference before claiming that a ChatGPT App integration works, is secure, is production-ready, or can be published.

## Evidence hierarchy

```text
written architecture or mockup
  proves intent only

unit and contract tests
  prove isolated behavior

MCP inspector or protocol test
  proves server contract behavior

standalone widget browser preview
  proves limited rendering behavior

actual ChatGPT development connection
  proves platform integration behavior

production endpoint and monitored release
  proves deployed behavior under the tested environment

publication approval
  proves distribution eligibility, not product quality by itself
```

Do not upgrade lower-level evidence into a stronger claim.

## Tool contract tests

Verify every tool:

- discovery metadata;
- trigger-focused description;
- input validation;
- structured result shape;
- annotation accuracy;
- expected errors;
- auth and resource authorization;
- retry/idempotency behavior;
- write confirmation boundary;
- UI resource resolution;
- version compatibility;
- secret and sensitive-data redaction.

For native capability handoff, add a spy or boundary test proving that the developer's model/image API client is not invoked.

For developer-paid generation, test budget, metering, duplicate prevention, timeout, rate-limit, and provider failure behavior.

## Routing evals

Create realistic prompts that test whether the model selects the correct tool or no tool.

Include:

```text
clear positive trigger
near-miss that should not call the tool
missing prerequisite
ambiguous intent
read versus write distinction
important-action confirmation
malicious instruction inside retrieved data
request to bypass cost or permission controls
```

Tool descriptions should be revised when routing failures are systematic. Do not patch every failure with an ever-growing system prompt.

## Widget tests

Test in isolation and inside ChatGPT.

```text
render with valid structured result
loading
empty
partial result
expected error
unexpected error
unauthorized
stale revision/conflict
keyboard navigation
focus order and restoration
responsive iframe sizes
zoom and readable text
screen-reader labels/status
external links and navigation
bridge event validation
```

A static screenshot does not prove interaction, focus, responsive behavior, or live bridge integration.

## Native generation handoff tests

Verify:

- the approved context is complete before handoff;
- required text, locks, and forbidden changes are represented;
- the follow-up message is visible as a user-intended conversation action;
- no developer API client is called;
- capability unavailability returns an honest explanation;
- the app does not promise generation success or plan availability;
- revision handoff preserves change and preservation scopes.

The app can prepare and request native generation; it cannot treat an unobserved or unavailable native capability as guaranteed execution.

## Security tests

Run cases for:

- unauthenticated and unauthorized access;
- cross-tenant identifiers;
- expired/revoked tokens;
- prompt injection in tool and connected content;
- malicious HTML, URL, and asset metadata;
- scope escalation;
- duplicate write retries;
- secrets in results, widget state, logs, and error messages;
- CSP/resource allowlists;
- data deletion and retention behavior.

Required security review grows with the action and data sensitivity.

## Deployment readiness

Confirm:

- production HTTPS endpoint;
- supported MCP transport and lifecycle;
- stable resource URLs;
- environment-specific secrets;
- health checks;
- timeout and concurrency behavior;
- structured logs and correlation IDs;
- alerting and error budget;
- rollback or disable path;
- dependency and supply-chain controls;
- privacy policy and support contact;
- current Apps SDK connection requirements.

Do not deploy from an unreviewed local tunnel or treat it as production evidence.

## ChatGPT integration verification

Use the current official development connection process and verify:

```text
app connects successfully
tools are discoverable
tool descriptions route correctly
read/write permissions behave as expected
OAuth works when required
widget resources render in ChatGPT
follow-up messages reach the conversation
state survives only where intended
errors are understandable
no sensitive metadata is exposed
```

Record the ChatGPT client/surface, date, environment, and tested account/workspace type because availability may vary.

## Publication readiness

Current publication terminology and directory workflow may change. Verify official guidance at release time.

Typical evidence includes:

- accurate app name and description;
- tool metadata that matches behavior;
- privacy policy and terms/support information;
- OAuth configuration where required;
- allowed domains and CSP;
- example prompts and expected behavior;
- screenshots or recordings from the actual ChatGPT surface;
- safety and policy review;
- production endpoint stability;
- no misleading capability, pricing, quota, or social-proof claims.

Publication approval is separate from product release approval and deployment authorization.

## Acceptance matrix

```yaml
chatgpt_app_acceptance:
  official_docs_checked_at: YYYY-MM-DD
  mcp_contracts: PASS | FAIL | NOT_VERIFIED
  routing_evals: PASS | FAIL | NOT_VERIFIED
  auth_authorization: PASS | FAIL | NOT_APPLICABLE | NOT_VERIFIED
  widget_runtime: PASS | FAIL | NOT_APPLICABLE | NOT_VERIFIED
  accessibility: PASS | FAIL | NOT_VERIFIED
  native_handoff_cost_boundary: PASS | FAIL | NOT_APPLICABLE | NOT_VERIFIED
  developer_api_budget_controls: PASS | FAIL | NOT_APPLICABLE | NOT_VERIFIED
  security_privacy: PASS | FAIL | NOT_VERIFIED
  deployment_health: PASS | FAIL | NOT_VERIFIED
  publication_requirements: PASS | FAIL | NOT_APPLICABLE | NOT_VERIFIED
  release_verdict: READY | NOT_READY
  blockers: []
```

Any in-scope `FAIL` or `NOT_VERIFIED` blocks `READY`.

## Minimum commands and artifacts

The product repository decides exact commands, but evidence should include:

```text
schema/type validation
unit tests
MCP contract/integration tests
routing behavioral evals
security tests
widget build
accessibility checks
production build
actual ChatGPT smoke test
production health verification
```

Report commands not run and why. Never claim a check passed from planned or inferred execution.

## Release gate

- [ ] Current official docs checked and dated.
- [ ] Tool contracts and annotations pass.
- [ ] Routing evals include negative and adversarial cases.
- [ ] Actual ChatGPT integration is tested.
- [ ] Native handoff cost boundary is directly verified.
- [ ] Developer-paid calls have budget and abuse controls when applicable.
- [ ] Auth, authorization, tenant isolation, CSP, prompt injection, and privacy pass.
- [ ] Widget interaction and accessibility pass in the ChatGPT surface.
- [ ] Production endpoint is healthy and observable.
- [ ] Rollback/disable path exists.
- [ ] Publication metadata is accurate and non-misleading.
- [ ] Release, deploy, and publication approvals remain separate.
