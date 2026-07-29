# Documentation Domains and Evidence

Load this reference only after `documentation-assurance` has established the governing workflow, subject, and change evidence.

## Domain ownership map

| Domain | Typical owner/producer | Typical reviewer | Evidence examples |
|---|---|---|---|
| Product requirements and scope | `product-requirements`, product owner | product owner / acceptance owner | effective PRD, decision record, acceptance matrix |
| Architecture and boundaries | architecture owner, `adr` | `architecture-review` | ADR, diagrams, source boundary evidence |
| API/schema/events | `api-contract`, API/data owner | compatibility or API reviewer | OpenAPI/schema/event diff, contract tests |
| Package/SDK/CLI usage | package owner, developer-experience owner | maintainer/reviewer | supported commands, usage tests, generated reference |
| User guidance | product/content owner | product/design/content reviewer | rendered behavior, screenshots, support evidence |
| Operator/deployment/runbook | operations owner | operations/reliability reviewer | actual commands, environment evidence, rollback rehearsal |
| Support/troubleshooting | support or product operations owner | support/operations reviewer | known failure modes, verified recovery path |
| Security/privacy/data handling | security/privacy owner | required authority | threat model, data-flow evidence, policy decision |
| Release notes/changelog | release owner | release reviewer | candidate diff, version/tag, release package |
| Migration/deprecation/removal | architecture/product/release owner | affected domain reviewers | migration test, rollback path, compatibility evidence |

Product repositories may define different names and locations. Resolve actual ownership from governing sources rather than assuming this table is authoritative for a product.

## Evidence strength

```text
DIRECT
  inspectable source, diff, command output, runtime behavior, review result,
  or authoritative decision supporting the exact documentation claim

CORROBORATING
  secondary evidence that supports but does not independently prove the claim

EXPECTED
  planned evidence that has not run

MISSING
  required evidence unavailable

CONFLICTED
  authoritative sources disagree
```

Only direct evidence can establish a PASS-like documentation claim. Expected evidence remains `NOT_VERIFIED`.

## Consistency checks by domain

### Product and scope

- document reflects the effective approved scope;
- removed or deferred behavior has attributable authority;
- acceptance criteria and status are not overstated;
- a draft does not claim approval.

### Architecture and contracts

- diagrams and ADRs match actual boundaries;
- public API/schema/event examples match current contracts;
- compatibility and breaking-change guidance is explicit;
- new dependencies or system changes have decision provenance.

### Developer and operator usage

- installation, setup, environment variables, commands, and examples are executable for the supported version;
- deprecated commands are removed or clearly marked;
- secrets and sensitive values are never embedded;
- failure and rollback paths match actual product behavior.

### User and support content

- labels, flows, limitations, pricing/quota claims, and available features match the actual surface;
- screenshots or examples are not presented as proof of unsupported runtime behavior;
- accessibility and support implications are documented when material.

### Release, migration, and deprecation

- candidate identity and version are correct;
- release notes distinguish shipped, deferred, experimental, and known limitations;
- migration prerequisites, sequence, validation, rollback, and recovery are explicit;
- removal timelines and alternatives are attributable.

## Not-applicable evidence examples

A reasoned `DOCUMENTATION_NOT_APPLICABLE` may be valid for a bounded internal refactor when direct evidence shows:

- no public behavior or contract changed;
- no setup, command, configuration, or operational behavior changed;
- no architecture meaning or accepted decision changed;
- no user/support/security/privacy/release/migration meaning changed;
- existing documentation remains accurate.

A small diff, private symbol, green tests, or developer belief alone is insufficient.

## Blocking examples

```text
public API changed but reference still shows old field
  → REQUIRED_DOCUMENT_MISSING or DOCUMENTATION_DRIFT

runbook command no longer works in the actual environment
  → DOCUMENTATION_DRIFT

migration is planned but rollback instructions do not exist
  → REQUIRED_DOCUMENT_MISSING

PR says docs updated but no document diff or inspectable source exists
  → UPDATE_NOT_VERIFIED

internal refactor is declared not applicable without checking operator or package usage
  → FALSE_NOT_APPLICABLE
```

## Review independence

The person or agent producing a document may perform a self-check, but required domain review remains separate. The report must preserve:

```text
produced
verified technically
reviewed independently
approved by authority
```

None of these states implies the next.