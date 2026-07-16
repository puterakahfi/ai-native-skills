---
name: data-modeling
description: Data modeling skill — schema design, normalization tradeoffs, migration patterns, polyglot persistence decisions, index strategy, and soft delete governance. For engineers who need to decide WHERE and HOW data lives.
license: MIT
metadata:
  ai-native-skills.version: 1.0.0
  ai-native-skills.author: puterakahfi
  ai-native-skills.type: skill
  ai-native-skills.implements: ai-native-core/contracts/skills/engineering/data-modeling.contract.yaml
  ai-native-skills.related_skills: '[''domain-driven-design'', ''refactoring'', ''technical-debt-governance'']'
---

# Data Modeling Skill

## Core Principle

```
Schema is the most expensive decision you make.
Changing it later costs 10x more than getting it right now.

The two questions:
  1. What queries will the system run? (query-first modeling)
  2. What are the consistency requirements? (transaction scope)

Never: model based on what the data "is"
Always: model based on how the data will be READ and WRITTEN
```

---

## Normalization — When to Normalize, When Not To

### Normal Forms

```
1NF: No repeating groups, atomic values
  ❌ tags: "typescript,nextjs,supabase"  (comma-separated string)
  ✅ tags table with FK to post

2NF: No partial key dependencies (for composite keys)
  Applies when: composite primary key (A+B → C)
  If C depends only on A, not both A+B → violates 2NF

3NF: No transitive dependencies
  ❌ orders(order_id, customer_id, customer_city)
      city depends on customer, not order
  ✅ separate customers table

BCNF: Stricter 3NF — every determinant is a candidate key
  Most schemas should aim for 3NF minimum, BCNF when possible
```

### When to Denormalize

```
Denormalize when:
  - Read performance is critical AND the read query JOINs > 3 tables
  - The field is rarely updated (denormalize a snapshot, not live data)
  - Reporting tables (OLAP) — denormalize aggressively
  - Event sourcing — append-only, reads reconstruct state

Denormalize safely with:
  - Derived columns (store computed value, update on write)
  - Read replicas with materialized views
  - CQRS: write model normalized, read model denormalized

Never denormalize:
  - Frequently updated fields (sync cost exceeds read gain)
  - Financial data (consistency is non-negotiable)
  - Fields that join to user-owned data (privacy complexity)
```

---

## Migration Patterns

### Expand-Contract (zero-downtime migrations)

```
Phase 1 — EXPAND: add new column/table, keep old
  - New code writes to BOTH old and new
  - Old code still reads old column (no breakage)

Phase 2 — MIGRATE: backfill old → new
  - Run migration in batches (never full table lock)
  - batch size: 1000–5000 rows per transaction
  - Add delay between batches (avoid replication lag)

Phase 3 — CONTRACT: remove old column/table
  - Old code updated to read only new column
  - Drop old column after deploy confirmed
  - Deploy → verify → then drop (not simultaneously)

Example:
  Need to rename `user.name` → `user.full_name`:
  1. Add `full_name` column (EXPAND)
  2. Write to both, backfill `full_name` from `name`
  3. Switch reads to `full_name` (deploy)
  4. Drop `name` column (CONTRACT)
```

### Batch Migration Template

```sql
-- Safe large table migration with batching
DO $$
DECLARE
  batch_size INT := 2000;
  last_id    BIGINT := 0;
  max_id     BIGINT;
BEGIN
  SELECT MAX(id) INTO max_id FROM users;
  
  WHILE last_id < max_id LOOP
    UPDATE users
    SET full_name = name
    WHERE id > last_id AND id <= last_id + batch_size
      AND full_name IS NULL;
    
    last_id := last_id + batch_size;
    PERFORM pg_sleep(0.05); -- 50ms pause between batches
  END LOOP;
END $$;
```

---

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
