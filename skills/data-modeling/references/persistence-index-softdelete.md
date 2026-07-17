# Persistence, Index Strategy, Soft Delete, and Gates

## Polyglot Persistence Decision

```
Choose storage based on ACCESS PATTERN, not data type.

PostgreSQL (relational):
  ✅ Complex queries, JOINs, ACID transactions
  ✅ Financial data, orders, users
  ✅ When consistency > performance
  ✅ Default choice — reach for this first

Redis (key-value, in-memory):
  ✅ Session storage, rate limiting
  ✅ Caching (query results, computed values)
  ✅ Pub/Sub messaging
  ✅ Leaderboards (sorted sets)
  ❌ Primary data store (not durable by default)

MongoDB (document):
  ✅ Flexible schema (schema evolves frequently)
  ✅ Hierarchical data (nested objects, arrays)
  ✅ High write throughput, horizontal scale
  ❌ Complex queries across documents
  ❌ Transactions spanning many documents

S3 / Object Storage:
  ✅ Files, images, videos, large blobs
  ✅ Logs, backups, archives
  ❌ Structured queries

Elasticsearch / OpenSearch:
  ✅ Full-text search, fuzzy matching
  ✅ Log aggregation, analytics
  ❌ Primary data store (use as derived index)

Decision rule: start with Postgres. Add specialist stores
only when Postgres genuinely cannot serve the access pattern.
```

---

## Index Strategy

```
Add an index when:
  □ Column appears in WHERE, JOIN ON, or ORDER BY frequently
  □ Query planner shows SEQSCAN on large table
  □ Query time > 100ms on production data volume

Index types (Postgres):
  B-tree:   default, most cases, range queries, equality
  Hash:     equality only, faster than B-tree for = queries
  GIN:      JSONB columns, full-text search, arrays
  GiST:     geometric data, proximity queries
  BRIN:     huge tables with natural ordering (timestamps, IDs)

Composite index order:
  Most selective column FIRST
  (user_id, created_at) — if filtering by user_id is more selective
  (created_at, user_id) — if filtering by date range first

Index anti-patterns:
  ❌ Indexing every column "just in case"
  ❌ Unused indexes (writes pay cost, reads get no benefit)
  ❌ Function on indexed column: WHERE LOWER(email) = ?
     Fix: functional index CREATE INDEX ON users(LOWER(email))
  ❌ Index on low-cardinality column (boolean, status with 3 values)
```

---

## Soft Delete Governance

```
Soft delete: set deleted_at timestamp instead of DELETE row.

When to use soft delete:
  ✅ Audit trail required (financial, compliance)
  ✅ Undo/restore feature needed
  ✅ FK references must remain valid after "delete"
  ✅ Regulatory data retention requirements

When NOT to use soft delete:
  ❌ Personal data (GDPR right to erasure = hard delete required)
  ❌ Ephemeral data (sessions, logs — just expire/purge)
  ❌ When query performance matters (every query needs WHERE deleted_at IS NULL)

If using soft delete — mandatory guards:
  1. Default scope: all queries must filter deleted_at IS NULL
     Use ORM default scope or row-level security
  2. Unique constraints: must include deleted_at
     (email, deleted_at) — allows re-registration after soft delete
  3. Archival policy: soft-deleted rows → archive table after N days
  4. Hard delete for PII: separate hard_delete() for personal data
```

---

## Data Modeling Gates (Scored 0–10, Min 8)

```
Gate D1: Query-First Design
  □ Schema designed based on actual query patterns?
  □ Most frequent queries avoid JOIN > 3 tables?
  Score: __ / 10

Gate D2: Migration Safety
  □ Breaking migrations use expand-contract?
  □ Large table migrations use batching?
  □ Migration tested on production-volume data snapshot?
  Score: __ / 10

Gate D3: Index Coverage
  □ Slow queries (> 100ms) have covering index?
  □ No unused indexes on write-heavy tables?
  Score: __ / 10

Gate D4: Soft Delete Governance
  □ Default scope filters deleted_at IS NULL everywhere?
  □ PII has hard delete path?
  □ Archival policy defined?
  Score: __ / 10

OVERALL: __ / 10   MINIMUM: 8.0
```
