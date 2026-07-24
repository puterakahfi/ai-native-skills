# Readability and Structure

Use this reference when a clean-code review needs deeper guidance for naming, control flow, functions, classes/modules, local APIs, or tests.

## Review order

```text
behavior and scope
→ vocabulary
→ control flow
→ function focus
→ module ownership
→ local contracts
→ tests
```

Do not start by counting lines. First identify what the code promises, what changes together, and what a maintainer must hold in working memory.

## Naming

A useful name communicates the role of a value in the current domain and abstraction level.

Review questions:

- Does the name match the product or domain vocabulary used by nearby code and specifications?
- Does it describe intent rather than storage type or temporary implementation?
- Are similar concepts named consistently and different concepts distinguishable?
- Does a boolean read as a proposition or state?
- Does a command name expose a side effect?
- Does a collection name indicate what its elements represent?
- Are units, currency, timezone, encoding, or nullable state visible where ambiguity is risky?

Finding examples:

```text
`data`, `item`, `result`
  not automatically wrong;
  report only when the surrounding scope does not make their meaning obvious.

`active`
  ambiguous when it could mean enabled, connected, paid, verified, or not deleted.

`getUser`
  misleading when it mutates, performs network I/O, or creates the user.
```

Avoid thesaurus refactoring. A longer name is not automatically clearer, and repository vocabulary outranks personal preference.

## Control flow

Prefer a flow whose main behavior and exceptional paths are visible without simulating many hidden states.

Inspect:

- nesting that hides the primary path;
- conditionals that combine unrelated business decisions;
- repeated guards that signal an absent invariant;
- boolean flags that create several implicit modes;
- fall-through, mutation, callback, or exception paths that obscure completion;
- early returns that clarify guards versus early returns that fragment one coherent decision;
- duplicated condition knowledge across functions or modules.

Possible corrections:

```text
name a complex condition
introduce an explicit guard
separate independent decisions
replace a mode flag with a named operation
make state transition explicit
return a typed/result contract when failure is expected
```

Do not flatten code mechanically. A nested structure can correctly express hierarchy or transaction scope.

## Functions

A function is cohesive when its statements contribute to one understandable outcome at a consistent abstraction level.

Signals that require inspection:

- the function must be described with “and then also” across unrelated responsibilities;
- callers need hidden ordering knowledge;
- business decisions and infrastructure details are interleaved;
- output depends on distant mutable state;
- parameters encode several modes or partially valid combinations;
- error handling is repeated or detached from the operation that gives it meaning;
- extraction would reveal a stable concept already present in domain language.

Line count is only a navigation signal. A 40-line parser may be coherent; a 6-line function may hide several responsibilities through side effects.

Before extraction, ask:

1. Does the candidate block have a meaningful name?
2. Does it own one concept or merely hide syntax?
3. Will extraction reduce working-memory load?
4. Will data movement and indirection stay understandable?
5. Does repository convention support the placement?
6. Can behavior remain protected by tests?

## Classes and modules

Evaluate cohesion by ownership and reasons to change, not by a universal file-size threshold.

A class or module may need decomposition when:

- unrelated policies change for different stakeholders or events;
- it owns both stable business rules and volatile integration details;
- consumers use disjoint subsets of its API;
- state invariants cover separate concepts;
- tests require unrelated setup families;
- merge conflicts or regressions repeatedly cluster around independent concerns.

Do not split merely to make every file small. Fragmentation can create navigation cost, anemic wrappers, circular dependency, and unclear ownership.

Useful owner map:

```yaml
module_review:
  owned_concept: <concept>
  primary_changes: []
  consumers: []
  state_and_invariants: []
  dependencies: []
  unrelated_change_reasons: []
```

Route architecture or dependency-boundary decisions to `master-engineer` and independent `architecture-review`.

## Parameters and local contracts

Inspect whether callers can construct valid inputs and understand outputs without hidden knowledge.

Potential risks:

- several primitives whose meaning or order is easy to confuse;
- multiple booleans that encode modes;
- nullable parameters with undocumented combinations;
- sentinel values that overload normal data;
- return values whose failure, absence, or partial state is ambiguous;
- a generic map/object crossing a stable local boundary without an explicit contract.

A parameter object or value object is justified when it represents a cohesive concept, protects invariants, or reduces repeated change. Do not introduce one only to reduce a parameter count metric.

## Tests as readable behavior evidence

Review tests for:

- behavior-oriented names;
- setup that exposes the important precondition;
- one clear reason for failure;
- assertions at the correct boundary;
- fixtures/builders that reduce noise without hiding decisive values;
- deterministic control of time, randomness, network, and persistence;
- failure messages that help diagnose the contract;
- duplication that reflects shared behavior versus accidental test syntax.

Avoid tests that mirror implementation line by line. Tests should protect observable behavior and meaningful domain rules so refactoring remains possible.

## Severity guidance

```text
BLOCKING
  likely defect, data loss, security/failure masking, or code cannot be changed safely in current scope

HIGH
  material ambiguity, mixed ownership, or hidden behavior with strong regression risk

MEDIUM
  maintainability cost is concrete but bounded

LOW
  localized clarity improvement with low immediate risk

NOTE
  non-blocking observation or evidence gap
```

A finding is not blocking merely because a rule from a book was violated. Tie severity to the actual system consequence.
