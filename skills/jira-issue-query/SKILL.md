---
name: jira-issue-query
description: Use when pulling Jira tickets. Always filter by assignee.
license: MIT
tags: [jira, atlassian, query, fsdb]
metadata:
  ai-native-skills.version: 1.0.0
  ai-native-skills.author: puterakahfi
  ai-native-skills.type: skill
---

# Jira Issue Query

## Trigger
Any request like "pull tiket dari jira", "show my jira tickets", "cek tiket fsdb" — or any variant.

## Golden Rule
**Always filter by `assignee = currentUser()`** unless the user explicitly says "semua", "all", or names a different person/team. Pulling the entire project backlog is noise and irritates the user.

## Steps

1. Get cloudId (rschooltoday constant: `d0a11069-5809-40c9-9ddf-e1b85924a39a`)
   - Or fetch fresh: `getAccessibleAtlassianResources()`

2. Query with assignee filter:
   ```jql
   project = FSDB AND assignee = currentUser() ORDER BY updated DESC
   ```

3. Parse and display compact table:
   `Key (linked) | Summary (≤65 chars) | Type | Status | Priority | Updated`

4. Follow with short "Active tickets" callout for non-Completed/non-Removed items.

## Output Format
- Compact table, no preamble
- Link each Key to `https://rschooltoday.atlassian.net/browse/{KEY}`
- Bold assignee name when showing full-project results (only if user explicitly requested)

## Pitfalls
- **DO NOT** pull entire project without assignee filter — user will complain
- Tool result is large (200KB+); parse via `terminal python3 -c`, not `execute_code` (double-parse JSON issue)
- `maxResults=50` is sufficient for personal ticket view

## Project Keys
- `FSDB` — Facility Scheduler (cloudId: `d0a11069-5809-40c9-9ddf-e1b85924a39a`)
