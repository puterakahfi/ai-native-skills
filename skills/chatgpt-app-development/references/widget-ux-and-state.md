# Widget UX, State, and Native Capability Handoff

Load this reference when a ChatGPT App includes interactive UI or needs to return work from the widget to the conversation.

## Conversational-first principle

The app must remain useful as a conversation. The widget improves selection, comparison, inspection, and confirmation; it does not replace the assistant response or duplicate an entire web product.

```text
conversation owns
  intent, explanation, natural-language refinement, native ChatGPT capabilities

widget owns
  focused controls, structured choices, staged edits, visual summaries

product backend owns
  durable business state and authoritative records
```

## Choose the smallest UI mode

### Text-only

Use when the result is understandable and actionable without interaction.

Examples:

- concise analysis;
- confirmation that a read completed;
- error with recovery instructions.

### Inline

Use for one focused task or summary.

Examples:

- selected workflow summary;
- brief completion status;
- asset-lock confirmation;
- save confirmation.

Guidelines:

- one dominant purpose;
- minimal controls;
- no nested navigation;
- critical meaning repeated in assistant text;
- avoid more than a small number of primary actions.

### Carousel

Use for a small comparable set.

Examples:

- workflow categories;
- design directions;
- reusable assets or templates.

Guidelines:

- keep the set bounded;
- one clear action per card;
- compare consistent fields;
- do not turn the carousel into a hidden catalog with deep navigation.

### Fullscreen

Use for deeper focused work that benefits from more space while preserving the ChatGPT conversation model.

Examples:

- multi-section workflow review;
- controlled revision scope;
- detailed QC report;
- structured configuration with preview.

Fullscreen is not permission to clone the whole product dashboard.

## Category architecture

For broad products, group choices before showing specific workflows.

```text
Level 1: user goal
  create visual | build identity | manage assets | review and refine

Level 2: workflow
  banner | social feed | ads | carousel | logo | virtual talent | visual QC

Level 3: parameters
  platform | ratio | objective | brand | assets | required text | locks
```

Do not present every capability as an equal top-level tab.

## State model

Classify each state field:

```text
Conversation state
  user intent and natural-language decisions available in the current chat

Tool result state
  structured result returned by MCP

Widget-local state
  selected tab, expanded section, staged input, unsaved comparison

Product backend state
  brand profile, workflow, asset, revision, approval, durable settings
```

Rules:

- durable business state does not live only in the widget;
- widget-local state is not automatically authoritative;
- writes use explicit tools rather than hidden browser persistence;
- server results include version/revision identifiers when edits may conflict;
- avoid copying the entire conversation into widget state.

## Native capability handoff

When generation should use the user's native ChatGPT capability:

```text
1. Build and display the structured context.
2. Let the user review required text, assets, locks, and output format.
3. Send a follow-up message to the conversation using the current supported Apps SDK bridge.
4. Phrase the message as a user request, not as an invisible privileged instruction.
5. Do not invoke the equivalent developer API from the MCP server.
6. Handle capability unavailability honestly.
```

Example handoff payload concept:

```text
Generate the visual using the approved production context.

Required:
- format: 4:5 social feed
- preserve uploaded logo geometry
- preserve product appearance
- use approved headline exactly
- do not add claims not present in the brief

Revision scope:
- none; this is the first approved generation
```

The exact bridge API must be verified against current official Apps SDK documentation.

## Revision UX

A revision request should separate:

```text
change scope
  what may change

preservation scope
  what must remain unchanged

reason
  why the change is needed

acceptance checks
  how the revised output will be reviewed
```

Good:

```text
Change only the headline hierarchy and top spacing.
Preserve product image, logo, colors, body copy, CTA, and composition.
```

Bad:

```text
Make it better and more premium.
```

The widget may stage revision scope, but the application core owns the revision contract.

## Accessibility

- preserve keyboard navigation and visible focus;
- use semantic controls and labels;
- do not encode status only by color;
- support zoom and responsive iframe sizes;
- announce loading, success, and error states;
- provide text alternatives for meaningful imagery;
- maintain readable contrast and touch targets;
- avoid motion that blocks task completion.

## Loading and failure states

Every interactive surface defines:

```text
idle
loading
empty
partial
success
expected error
unexpected error
unauthorized
stale/conflict
```

Do not leave the user with an indefinite spinner when the MCP call fails.

## Anti-patterns

- recreating a left-sidebar SaaS dashboard inside an inline card;
- using many tabs where progressive disclosure is clearer;
- nested scroll areas inside the ChatGPT surface;
- hiding critical tool results only in UI metadata;
- adding a fake chat input inside the widget;
- triggering external writes from selection controls without confirmation;
- presenting native generation as guaranteed on every account;
- keeping durable brand or workflow data only in browser state;
- treating a pretty screenshot as interaction acceptance evidence.

## UX verification

- [ ] The conversation remains understandable without the widget.
- [ ] UI mode matches task depth.
- [ ] Categories use clear grouping and progressive disclosure.
- [ ] Widget-local and durable state are separated.
- [ ] Native handoff does not call the developer API.
- [ ] Important actions and external writes use explicit tools and confirmation policy.
- [ ] Keyboard, focus, responsive, loading, empty, error, and conflict states are verified.
- [ ] Revision scope distinguishes change from preservation.
- [ ] Actual ChatGPT rendering evidence exists, not only standalone browser screenshots.
