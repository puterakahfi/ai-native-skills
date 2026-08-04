# Facility Scheduler (FS) — Project Reference

Captured: 2026-07-31

## Identity
- **Hermes Project ID**: p_de94f675
- **Hermes Project slug**: facility-scheduler-fs
- **Jira key**: FSDB
- **Jira URL**: https://rschooltoday.atlassian.net/browse/FSDB
- **Repo**: git@bitbucket.org:rschooltoday/facility-scheduler.git

## URLs
| Env | URL |
|-----|-----|
| Local | fs-stag.devel:8081 |
| Staging | https://fs-stag.rschooltoday.com/ |

## Local paths
| Purpose | Path |
|---------|------|
| Root | /data/www/facility-scheduler/ |
| Staging worktree | /data/www/facility-scheduler/staging/fs-stag |
| Staging 2 | /data/www/facility-scheduler/staging/fs-stag2 |
| Per-ticket worktrees | /data/www/facility-scheduler/worktrees/fsdb-{ticket}/ |

## Tech stack
- PHP 8.0 + MySQL 8.0
- Zend Framework v1 + custom framework **CAD**
- Infrastructure depends on **arbiter-docker**
- Composer deps: monolog, mongodb, aws-sdk-php, google/apiclient, sendgrid, dompdf, phpspreadsheet
- Tests: PHPUnit (unit), Playwright (e2e)
- CI: Bitbucket Pipelines (`bitbucket-pipelines.yml`)

## Structure
- `/application/{module}` — modules: accountcode, arbiter, facility, permit, calendar, authentication, etc.
- `/clients/{env}` — env configs: demo, local, prod, stag, test
- `/lib/` — vendor + shared libs
- `/docroot/` — web root

## Task board
- Personal cross-project kanban: `personal-tasks` board (`~/.hermes/kanban/boards/personal-tasks/kanban.db`)
- `bind-board` to Jira not yet supported — tasks tracked manually on kanban board

## Notes
- `git config --global --add safe.directory /data/www/facility-scheduler/staging/fs-stag` required (dubious ownership on shared /data/www/)
- Worktree naming convention: `fsdb-{ticket_number}` or `fsdb-{ticket}-{description}`
