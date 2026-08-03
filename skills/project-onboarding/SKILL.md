---
name: project-onboarding
description: Use when setting up project context. Collect facts first.
license: MIT
metadata:
  ai-native-skills.version: 1.0.0
  ai-native-skills.author: puterakahfi
  ai-native-skills.type: skill
---

# Project Onboarding

## Reference files

- `references/facility-scheduler-fs.md` — Facility Scheduler (FS) project: URLs, paths, stack, structure, Jira key, Hermes project ID.
- `references/native-ai-skills.md` — native-ai-skills project: GitHub URL, local path, tech stack, active epics/issues, Hermes project ID p_2a02a913.

## Trigger

Use when the user says "setup project", "tambah project", "daftarin project", "init project context", or provides a URL + local path combination as project info.

## User preference (CRITICAL)

> **Wait for complete input before executing anything.**
> If the user is still typing or providing info (mid-message, partial URL, etc.), do NOT start loading skills or running tool calls. Wait until the user sends a complete, full message with all info. Signal: "aduh wait" or interruptions mid-execution = you started too early.

## Required info to collect before setup

**Infer project type first** — then ask only for fields that apply. Don't block on fields that don't exist for this project type.

**Web app / product repo** (full set):

| Field | Example |
|---|---|
| **Local dev URL** | `fs-stag.devel:8081` |
| **Remote/staging URL** | `https://fs-stag.rschooltoday.com/` |
| **Local path** | `/data/www/facility-scheduler/staging/fs-stag` |
| **Jira/tracker project** | `https://rschooltoday.atlassian.net/browse/FSDB` |
| **Tech stack** | PHP, Laravel, Node, etc. |
| **Purpose of setup** | environment only, Hermes context, full scaffold |

**Skills / tools / infrastructure repo** (reduced set — no dev URL or Jira needed):

| Field | Example |
|---|---|
| **Local path** | `/data/www/ai-native-skills` |
| **GitHub URL** | `https://github.com/puterakahfi/ai-native-skills` |
| **Tech stack** | YAML schemas, Python scripts, Markdown |
| **Active issues / tracker** | GitHub Issues URL |

Signals a repo is a skills/tools type: no `package.json`/`composer.json` at root, no server URL, GitHub Issues as tracker. When clearly a skills repo, skip web-app fields entirely.

Ask for missing fields in ONE message. Do not proceed with `NOT_VERIFIED` fields for required items.

## Execution steps

1. **Verify local path exists** — `ls <local_path>`
2. **Resolve git ownership if needed** — see pitfalls below
3. **Check remote** — `git -C <path> remote -v`
4. **Check current branch + recent commits** — `git -C <path> branch --show-current && git log --oneline -5`
5. **Identify tech stack** from `composer.json`, `package.json`, or framework markers
6. **Create Hermes Project** (REQUIRED — do this before saving to memory):
   ```bash
   hermes project create "<Project Name>" --path <local_path>
   ```
   Or via tool: `project_create(name="...", path="...")` — this registers the project in `~/.hermes/projects`, anchors the session workspace, and updates the sidebar. **Do NOT skip this in favour of memory-only storage.**
7. **Save project context to memory** as a supplement — memory holds quick-lookup facts (URLs, stack, Jira key); the Hermes Project record is the canonical registration.
8. **Optionally bind a board** if the project has a Jira/kanban tracker:
   ```bash
   hermes project bind-board <project-slug> --url <jira-url>
   ```

## Pitfalls

### git dubious ownership error
```
fatal: detected dubious ownership in repository at '<path>'
```
**Fix:**
```bash
git config --global --add safe.directory <path>
```
Common on shared `/data/www/` directories where the repo owner ≠ current user.

### Memory is NOT a substitute for `hermes project create`
The correct canonical registration for a project is `hermes project create` (or `project_create` tool). Memory is supplemental quick-lookup only. If you skip `hermes project create` and only save to memory, the project won't appear in `~/.hermes/projects`, won't anchor the session workspace, and won't show in the sidebar. **Always create the Hermes Project first.**

### Task management: use Hermes kanban, not memory or files
For personal task management across multiple projects, the correct place is a **Hermes kanban board**, not memory entries or project files. Setup:
```bash
hermes kanban init
hermes kanban boards create personal-tasks --name "Personal Tasks"
hermes kanban boards switch personal-tasks
```
One cross-project board (`personal-tasks`) is the recommended default — split per-project only when volume warrants it. To view tasks visually:
```bash
hermes dashboard   # opens at http://localhost:9119
```
Or via tool: `open_preview(url="http://localhost:9119")` to open in the preview pane.

> **Dashboard preview pane = broken.** Opening `http://localhost:9119` via `open_preview` or an external browser throws "Desktop IPC bridge is unavailable" — the dashboard requires the Hermes Electron app's internal IPC context. **Do not suggest the preview pane for the dashboard.**

To read and render task lists directly in chat, use the CLI + present the output as a table:
```bash
HERMES_KANBAN_BOARD=personal-tasks hermes kanban list --json
```
This returns JSON that can be formatted into a markdown table inline. An empty board returns `[]`.

### gh CLI auth — check before PR step
`gh pr create` fails with "please run: gh auth login" even when `git push` via SSH works fine — they use **separate credential paths**. SSH key ≠ gh token. Before attempting PR creation:
```bash
gh auth status 2>&1
```
If not authenticated:
- `gh auth login --web` — opens browser, sets token permanently in `~/.config/gh/`
- `export GH_TOKEN=<token>` — generate at https://github.com/settings/tokens (repo scope)

SSH push working is not evidence that `gh` CLI is authenticated.

#### `gh auth login --web` hangs in Hermes terminal (non-interactive)
Hermes agent terminal has no TTY and no keyring access — `gh auth login --web` prints a one-time code and hangs indefinitely waiting for a browser redirect that never lands. **Do not retry it.** Correct flow:

1. Tell the user to run in **their own terminal** (outside Hermes):
   ```bash
   gh auth login --web   # approve in browser
   gh auth token         # copy the gho_... token
   ```
2. User pastes the token into chat.
3. Pass it inline or export for the session:
   ```bash
   GH_TOKEN=<token> gh pr create ...
   # or
   export GH_TOKEN=<token>
   ```
Even after user approves in browser, `gh auth status` in Hermes terminal will still show "not logged in" — the keyring session is isolated. Always use `GH_TOKEN` env var approach in Hermes.

### bind-board to Jira not yet supported
`hermes project bind-board` currently supports internal kanban boards only — not external Jira projects. Skip this step when the project tracker is Jira.

### Jira import into kanban — use MCP (not raw API calls)
When user asks to import tasks from Jira, use **`mcp-atlassian`** MCP server — not raw REST calls or env vars.

Install:
```bash
pip install mcp-atlassian
```

Register with Hermes:
```bash
hermes mcp add jira \
  --command mcp-atlassian \
  --args "--jira-url=https://rschooltoday.atlassian.net" \
         "--jira-username=EMAIL" \
         "--jira-token=TOKEN"
```

Credentials needed:
- **Email** — Atlassian account email
- **API Token** — generate at https://id.atlassian.com/manage-profile/security/api-tokens

`hermes mcp catalog` does NOT list Jira — it's not in the official catalog. Install manually via pip as above.

Note: `hermes secrets` is for Bitwarden/1Password external vaults — not for simple credential passing.

**OAuth flow for Jira MCP — copy tokens from another profile first.**
The correct Atlassian MCP remote URL is: `https://mcp.atlassian.com/v1/mcp` (NOT `/rest/mcp/1`).

If another Hermes profile (e.g. `arbiter`) already has Atlassian OAuth tokens cached, copy them instead of re-running the browser flow:

```bash
mkdir -p ~/.hermes/profiles/<target-profile>/mcp-tokens/
cp ~/.hermes/profiles/arbiter/mcp-tokens/atlassian-mcp-server.json \
   ~/.hermes/profiles/<target-profile>/mcp-tokens/atlassian-mcp-server.json

hermes mcp add atlassian-mcp-server \
  --url https://mcp.atlassian.com/v1/mcp \
  --auth oauth <<< $'Y\nY'
```

Token file is at: `~/.hermes/profiles/<profile>/mcp-tokens/atlassian-mcp-server.json`
Arbiter's config reference: `mcp_servers.atlassian-mcp-server.url = https://mcp.atlassian.com/v1/mcp`

If no cached tokens exist anywhere, user must run interactively from **Hermes desktop app terminal tab** — agent cannot complete OAuth browser flow from its own terminal session.
> "non-interactive environment and no cached tokens found. Run `hermes mcp login jira` interactively first"

**Fix:** User must run this command directly in the **Hermes desktop app terminal tab** (not via agent's terminal tool). The agent cannot complete OAuth browser flow from its own terminal session. The correct Atlassian MCP remote URL is: `https://mcp.atlassian.com/rest/mcp/1`.

### Stop over-engineering simple tasks (user frustration signal)
User expressed frustration ("gimana sih", "hang mulu bjir") when the agent:
- Kept trying to drive the desktop via computer_use for simple UI navigation
- Suggested preview pane workarounds that obviously wouldn't work
- Kept looping on failed approaches instead of stopping and stating the blocker

**Rule:** If an approach fails twice, stop and state the blocker clearly. Don't escalate to more complex tools (computer_use → browser_vision → more captures) when the answer is just "this doesn't work this way, here's the CLI alternative."

### Don't load workflow-router twice
`workflow-router` is a meta-skill — load it once per session. If routing decision is already made (e.g. `product-development-workflow` confirmed), skip the reload.

### "setup project" is ambiguous — always clarify
Clarify whether the user wants:
- **Hermes context setup** (save project facts so agents know the project)
- **Local environment setup** (install deps, configure .env, etc.)
- **Both**

Do not assume — ask in the same single clarifying message alongside any other missing fields.
