# Published Capability Catalog

`ai-native-skills` is the upstream bounded context and canonical owner of executable capability identity, executable type, canonical path, and capability-discovery metadata.

The consumer-facing Published Catalog is generated at:

```text
catalog/published/capability-catalog.json
```

It combines the canonical capability inventory, facets, classifications, topics, and job profiles into one deterministic document. Downstream consumers must use this document as the Published Language instead of coupling to repository-internal source layout.

## Ownership

Upstream owns canonical capability semantics, schema compatibility, and exact source provenance. Downstream products own presentation, ranking behavior, UI state, caching, deployment, and product acceptance.

## Compatibility

Compatible changes are additive capability or metadata changes that preserve the supported schema and existing capability identities and executable types.

The following are breaking or destructive and require explicit consumer review:

- schema-version changes;
- incompatible catalog-version changes;
- capability removal;
- executable-type mutation;
- removal of required fields.

Unknown schema versions, unknown capability types, duplicate identities, invalid counts, and broken canonical source documents fail closed.

## Commands

Generate from the current exact checkout revision:

```bash
python3 scripts/build-published-capability-catalog.py \
  --write \
  --source-revision "$(git rev-parse HEAD)"
```

Verify the committed artifact against canonical sources:

```bash
python3 scripts/build-published-capability-catalog.py --check
```

Run the network-independent regression harness:

```bash
python3 scripts/test-published-capability-catalog.py
```

The harness uses temporary fixture directories and does not modify canonical inventory, discovery documents, or the committed Published Catalog. It covers deterministic generation, exact provenance, duplicate identities, count drift, canonical-path mutations, discovery-schema mutations, mutable revisions, and malformed committed artifacts.

## Temporary validation policy

While GitHub Actions capacity is constrained, local command output is the accepted execution evidence. Record the exact commands, revision, exit status, and output on the pull request. Commands that have not been executed remain `NOT_VERIFIED`; the absence of CI is neither a pass nor a failure.

The generated document records the exact immutable revision used as its source. Generation is deterministic: the same canonical inputs and source revision produce byte-identical output.
