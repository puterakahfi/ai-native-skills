# Published Capability Catalog

`ai-native-skills` owns executable capability identity, type, canonical path, and discovery metadata. Downstream consumers should not join repository-internal files themselves.

The published consumer contract is generated at:

```text
catalog/published/capability-catalog.json
```

It combines the canonical capability inventory, facets, classifications, topics, and job profiles into one deterministic, versioned document.

## Ownership boundary

Upstream owns:

- capability identity and executable type;
- canonical source path and discovery metadata;
- schema and catalog version;
- exact immutable source revision;
- compatibility classification and generation provenance.

Downstream products own UI models, ranking and presentation, caching, deployment, and product acceptance.

## Compatibility policy

Additive capability and metadata changes are compatible while the supported schema and existing identities remain valid.

The following are breaking and require explicit consumer review:

- schema-version change;
- capability removal;
- executable-type mutation;
- removal of a required field;
- incompatible catalog-version policy change.

Unknown schema versions, unknown capability types, duplicate identities, invalid counts, invalid canonical paths, and broken discovery references fail closed.

## Commands

Generate from the exact source commit represented by the canonical files:

```bash
python3 scripts/build-published-capability-catalog.py \
  --write \
  --source-revision "$(git rev-parse HEAD)"
```

Verify freshness and determinism:

```bash
python3 scripts/build-published-capability-catalog.py --check
python3 -m unittest scripts/tests/test_build_published_capability_catalog.py
```

Compare against a previous published artifact:

```bash
python3 scripts/build-published-capability-catalog.py \
  --check \
  --baseline path/to/previous-capability-catalog.json
```

A breaking comparison returns non-zero. Release or consumer approval remains outside this compiler.

## Consumer migration

Consumers should pin a catalog artifact or immutable repository revision, verify `schema_version`, and reject unsupported versions. Internal source-file locations may change without downstream changes while the published schema remains compatible.
