# Product and Billing Boundary

Load this reference when the product uses generative models, images, subscriptions, usage credits, external providers, or claims that usage is charged to the end user.

## Core distinction

MCP is a transport and tool boundary. It does not itself choose the model, pay a bill, or transfer quota between accounts.

Cost ownership is determined by the execution surface that actually performs the paid work.

```text
ChatGPT-native capability in the user's conversation
  → governed by that user's ChatGPT plan or workspace terms

OpenAI API request using the app developer's credentials
  → governed by the developer's API organization billing and rate limits

External provider request
  → governed by the account and contract used for that request

MCP server compute, database, storage, and bandwidth
  → governed by the app operator's infrastructure
```

ChatGPT subscriptions and API Platform billing are separate systems. Never use a ChatGPT subscription as evidence that developer API calls are included.

## Required capability matrix

For every costly or limited capability, record:

| Capability | Trigger | Execution surface | Credential/account used | Cost or limit owner | Fallback |
|---|---|---|---|---|---|
| Example: native image generation | user asks in chat | ChatGPT conversation | end-user ChatGPT session | end user/workspace | explain plan limitation |
| Example: backend image generation | MCP tool calls Images API | OpenAI API | developer API key | developer | budget/rate-limit policy |
| Example: save workflow | MCP write tool | product backend | product OAuth session | app operator | retry/idempotency |

A row with an unknown credential or unknown cost owner blocks architecture approval.

## User-account native generation pattern

Use this pattern when the product sells workflow, structure, data, or control while generation should remain a native ChatGPT capability.

```text
1. MCP reads or prepares product data.
2. Product application core returns structured generation context.
3. Widget or assistant presents the approved context.
4. A follow-up message returns the request to the ChatGPT conversation.
5. ChatGPT decides whether and how to use its native capability.
6. The app does not call the corresponding OpenAI model/image API.
```

The handoff may include:

- approved brief;
- required text;
- brand or asset references;
- preservation locks;
- forbidden changes;
- output format;
- revision scope;
- QC criteria.

Do not claim that a UI button can force a native capability that is unavailable to the user's plan, workspace, region, policy, or current ChatGPT surface.

## Developer-paid API pattern

Use this pattern only when the product intentionally owns generation cost and operations.

```text
MCP tool
  → authenticated product use case
  → developer-managed OpenAI API or external provider
  → product budget, quota, moderation, retry, observability, and billing policy
```

Required controls:

- explicit economic approval;
- pricing and unit-economics model;
- per-user and global budgets;
- rate limits and concurrency;
- idempotency and duplicate-charge prevention;
- provider error and timeout handling;
- abuse prevention;
- usage metering;
- customer-facing disclosure;
- graceful degradation when budget or quota is exhausted.

## Mixed model

A mixed model is valid but must not be summarized as fully user-paid.

Example:

```text
Native image generation      user ChatGPT plan
Product copy rewrite API     developer OpenAI API
Asset storage                app operator
Third-party background remove customer provider account
```

Expose the mixed ownership in architecture and pricing decisions.

## Pricing implications

A product that does not pay for generation may charge for:

- workflow orchestration;
- connected product data;
- reusable identity or asset management;
- structured prompt/context compilation;
- revision control;
- quality checks;
- collaboration, persistence, and governance.

Do not sell undisclosed generation credits when generation is actually provided by the user's ChatGPT account. State that ChatGPT capability availability and limits follow the user's own plan/workspace.

## Anti-boncos checklist

- [ ] No model/image API is invoked with developer credentials for a user-quota promise.
- [ ] Server-side dependencies are checked for hidden AI calls.
- [ ] Tool names and descriptions do not misrepresent the execution surface.
- [ ] Every paid hop is listed in the capability matrix.
- [ ] Native generation unavailability has a clear fallback message.
- [ ] API-paid features have budgets, metering, and abuse controls.
- [ ] Pricing copy separates the product subscription from ChatGPT subscription requirements.
- [ ] Current official OpenAI plan and billing documentation was verified.

## Failure examples

```text
"MCP means OpenAI charges the user"
  → false generalization; identify the actual execution surface

"Generate in ChatGPT" button calls openai.images.generate with app key
  → developer-paid API hidden behind misleading wording

"Every ChatGPT user can generate images through this app"
  → unverified availability claim

"ChatGPT Plus includes our API usage"
  → conflates separate billing systems
```

## Evidence

Before approval, capture:

- architecture call graph for each generation path;
- credential owner for each provider request;
- environment variables and secret inventory by purpose;
- test proving native handoff does not hit the developer API client;
- test proving developer-paid paths are metered and bounded;
- current official documentation references and retrieval date.
