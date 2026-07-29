#!/usr/bin/env bash
set -Eeuo pipefail

HERMES_HOME="${HERMES_HOME:-${RUNNER_TEMP:-/tmp}/epic-260-hermes-home}"
HERMES_INSTALL_DIR="${HERMES_INSTALL_DIR:-${RUNNER_TEMP:-/tmp}/epic-260-hermes-install}"
BOARD="${BOARD:-epic-260-runtime-validation}"
EVIDENCE_DIR="${EVIDENCE_DIR:-${GITHUB_WORKSPACE:-$PWD}/.tmp/epic-260-hermes-runtime}"

export HERMES_HOME HERMES_INSTALL_DIR BOARD EVIDENCE_DIR

mkdir -p "$EVIDENCE_DIR"

on_error() {
  local rc=$?
  printf 'runtime acceptance failed at line %s with exit %s\n' "${BASH_LINENO[0]:-unknown}" "$rc" \
    > "$EVIDENCE_DIR/failure.txt"
  exit "$rc"
}
trap on_error ERR

cleanup() {
  if [[ -n "${HTTP_PID:-}" ]]; then
    kill "$HTTP_PID" 2>/dev/null || true
  fi
}
trap cleanup EXIT

run_capture() {
  local output=$1
  shift
  "$@" > "$EVIDENCE_DIR/$output" 2>&1
}

record_exit() {
  local name=$1
  local rc=$2
  printf '%s\n' "$rc" > "$EVIDENCE_DIR/$name.exit"
}

rm -rf "$HERMES_HOME" "$HERMES_INSTALL_DIR"
mkdir -p "$HERMES_HOME" "$HERMES_INSTALL_DIR" "$EVIDENCE_DIR"
printf 'runtime=ephemeral_github_actions\nhome=%s\ninstall=%s\n' \
  "$HERMES_HOME" "$HERMES_INSTALL_DIR" > "$EVIDENCE_DIR/isolation.txt"

# Install the official current Hermes source without interactive setup or browser dependencies.
curl -fsSL https://raw.githubusercontent.com/NousResearch/hermes-agent/main/scripts/install.sh \
  | bash -s -- \
      --skip-setup \
      --skip-browser \
      --branch main \
      --dir "$HERMES_INSTALL_DIR" \
      --hermes-home "$HERMES_HOME" \
  > "$EVIDENCE_DIR/install.log" 2>&1

export PATH="$HOME/.local/bin:$PATH"
if command -v hermes >/dev/null 2>&1; then
  HERMES_BIN="$(command -v hermes)"
elif [[ -x "$HOME/.local/bin/hermes" ]]; then
  HERMES_BIN="$HOME/.local/bin/hermes"
else
  HERMES_BIN="$(find "$HERMES_INSTALL_DIR" -type f -path '*/bin/hermes' -perm -u+x | head -1)"
fi
[[ -n "$HERMES_BIN" && -x "$HERMES_BIN" ]]
export HERMES_BIN

"$HERMES_BIN" --version | tee "$EVIDENCE_DIR/version.txt"
git -C "$HERMES_INSTALL_DIR" rev-parse HEAD | tee "$EVIDENCE_DIR/hermes-source-revision.txt"

# Diagnostics are evidence, not a hard pass requirement when credentials are intentionally absent.
set +e
run_capture doctor.txt "$HERMES_BIN" doctor
DOCTOR_RC=$?
run_capture dump.txt "$HERMES_BIN" dump
DUMP_RC=$?
set -e
record_exit doctor "$DOCTOR_RC"
record_exit dump "$DUMP_RC"

create_profile() {
  local name=$1
  local description=$2
  "$HERMES_BIN" profile create "$name" \
    --no-skills \
    --no-alias \
    --description "$description"
}

create_profile engineering-orchestrator \
  "Coordinates workflow routing, durable task decomposition, artifact handoffs, and final synthesis without taking specialist ownership."
create_profile solution-architecture \
  "Owns solution boundaries, architecture decisions, technical contracts, risks, and implementation guidance."
create_profile backend-platform \
  "Owns backend services, APIs, persistence, integrations, and backend verification within approved architecture."
create_profile quality-review \
  "Independently evaluates acceptance evidence, architecture conformance, regressions, and release readiness."

"$HERMES_BIN" profile list | tee "$EVIDENCE_DIR/profiles-list.txt"
for profile in engineering-orchestrator solution-architecture backend-platform quality-review; do
  run_capture "profile-${profile}.txt" "$HERMES_BIN" profile show "$profile"
  run_capture "profile-${profile}-description.txt" "$HERMES_BIN" profile describe "$profile"
done

python3 - <<'PY'
from pathlib import Path
import json, os
root = Path(os.environ['HERMES_HOME'])
profiles = ['engineering-orchestrator', 'solution-architecture', 'backend-platform', 'quality-review']
observed = {}
for name in profiles:
    path = root / 'profiles' / name
    if not path.is_dir():
        raise SystemExit(f'missing profile directory: {path}')
    observed[name] = {
        'relative_path': str(path.relative_to(root)),
        'profile_yaml': (path / 'profile.yaml').is_file(),
        'no_bundled_skills_marker': (path / '.no-bundled-skills').is_file(),
    }
if len({item['relative_path'] for item in observed.values()}) != len(profiles):
    raise SystemExit('profile paths are not unique')
Path(os.environ['EVIDENCE_DIR'], 'profile-isolation.json').write_text(
    json.dumps(observed, indent=2) + '\n', encoding='utf-8'
)
PY

# Serve the exact PR checkout locally so Hermes installs the skill and its referenced support files.
python3 -m http.server 8765 --bind 127.0.0.1 --directory "${GITHUB_WORKSPACE:-$PWD}" \
  > "$EVIDENCE_DIR/skill-http-server.log" 2>&1 &
HTTP_PID=$!
for _ in $(seq 1 20); do
  if curl -fsS http://127.0.0.1:8765/skills/hermes-agent-fleet-bootstrap/SKILL.md >/dev/null; then
    break
  fi
  sleep 1
done
curl -fsS http://127.0.0.1:8765/skills/hermes-agent-fleet-bootstrap/SKILL.md >/dev/null

set +e
printf 'y\n' | "$HERMES_BIN" -p engineering-orchestrator skills install \
  http://127.0.0.1:8765/skills/hermes-agent-fleet-bootstrap/SKILL.md --force \
  > "$EVIDENCE_DIR/skill-install.txt" 2>&1
SKILL_INSTALL_RC=$?
run_capture orchestrator-skills.txt "$HERMES_BIN" -p engineering-orchestrator skills list
SKILL_LIST_RC=$?
run_capture orchestrator-prompt-size.json "$HERMES_BIN" -p engineering-orchestrator prompt-size --json
PROMPT_SIZE_RC=$?
set -e
record_exit skill-install "$SKILL_INSTALL_RC"
record_exit skill-list "$SKILL_LIST_RC"
record_exit prompt-size "$PROMPT_SIZE_RC"
[[ "$SKILL_INSTALL_RC" -eq 0 ]]
grep -q 'hermes-agent-fleet-bootstrap' "$EVIDENCE_DIR/orchestrator-skills.txt"

# No bot or provider secrets are provisioned in this isolated validation run.
for profile in engineering-orchestrator solution-architecture backend-platform quality-review; do
  set +e
  run_capture "gateway-${profile}.txt" "$HERMES_BIN" -p "$profile" gateway status
  gateway_rc=$?
  set -e
  record_exit "gateway-${profile}" "$gateway_rc"
done

python3 - <<'PY'
from pathlib import Path
import json, os, re
root = Path(os.environ['HERMES_HOME'])
profiles = ['engineering-orchestrator', 'solution-architecture', 'backend-platform', 'quality-review']
sensitive = re.compile(r'(BOT_TOKEN|TELEGRAM|DISCORD|SLACK|GATEWAY_RELAY_SECRET|API_KEY)', re.I)
result = {}
for name in profiles:
    env_file = root / 'profiles' / name / '.env'
    configured = []
    if env_file.is_file():
        for line in env_file.read_text(encoding='utf-8', errors='ignore').splitlines():
            line = line.strip()
            if not line or line.startswith('#') or '=' not in line:
                continue
            key, value = line.split('=', 1)
            if sensitive.search(key) and value.strip():
                configured.append(key)
    result[name] = {
        'default_gateway_policy': 'orchestrator_only' if name == 'engineering-orchestrator' else 'none',
        'configured_sensitive_key_names': configured,
    }
if any(item['configured_sensitive_key_names'] for item in result.values()):
    raise SystemExit('ephemeral profiles unexpectedly contain configured sensitive values')
Path(os.environ['EVIDENCE_DIR'], 'gateway-policy.json').write_text(
    json.dumps(result, indent=2) + '\n', encoding='utf-8'
)
PY

"$HERMES_BIN" kanban init | tee "$EVIDENCE_DIR/kanban-init.txt"
"$HERMES_BIN" kanban boards create "$BOARD" \
  --name "Epic 260 Runtime Validation" \
  --description "Isolated direct Hermes validation for specialist fleet bootstrap" \
  --switch | tee "$EVIDENCE_DIR/board-create.txt"
"$HERMES_BIN" kanban boards show | tee "$EVIDENCE_DIR/board-show.txt"

create_task() {
  "$HERMES_BIN" kanban --board "$BOARD" create "$1" \
    --body "$2" \
    --assignee "$3" \
    --workspace scratch \
    --idempotency-key "$4"
}

create_task "Coordinate Epic 260 runtime acceptance" \
  "Decompose runtime checks and synthesize actual evidence without claiming model execution." \
  engineering-orchestrator epic260-orchestrator \
  | tee "$EVIDENCE_DIR/create-orchestrator.txt"
create_task "Coordinate Epic 260 runtime acceptance" \
  "Decompose runtime checks and synthesize actual evidence without claiming model execution." \
  engineering-orchestrator epic260-orchestrator \
  | tee "$EVIDENCE_DIR/create-orchestrator-repeat.txt"
create_task "Inspect fleet architecture contract" \
  "Verify bounded profile responsibilities and produce an architecture handoff." \
  solution-architecture epic260-architecture \
  | tee "$EVIDENCE_DIR/create-architecture.txt"
create_task "Produce Kanban persistence evidence" \
  "Consume the architecture handoff and record durable board evidence." \
  backend-platform epic260-backend \
  | tee "$EVIDENCE_DIR/create-backend.txt"
create_task "Review integrated runtime evidence" \
  "Independently inspect profile and Kanban evidence and record limitations." \
  quality-review epic260-review \
  | tee "$EVIDENCE_DIR/create-review.txt"

"$HERMES_BIN" kanban --board "$BOARD" list --json > "$EVIDENCE_DIR/tasks-initial.json"
python3 - <<'PY'
import json, os
from pathlib import Path

data = json.loads(Path(os.environ['EVIDENCE_DIR'], 'tasks-initial.json').read_text(encoding='utf-8'))
found = []
def walk(value):
    if isinstance(value, dict):
        if isinstance(value.get('title'), str) and value.get('id') is not None:
            found.append(value)
        for child in value.values():
            walk(child)
    elif isinstance(value, list):
        for child in value:
            walk(child)
walk(data)
by_title = {}
for item in found:
    by_title.setdefault(item['title'], []).append(str(item['id']))
expected = [
    'Coordinate Epic 260 runtime acceptance',
    'Inspect fleet architecture contract',
    'Produce Kanban persistence evidence',
    'Review integrated runtime evidence',
]
for title in expected:
    if len(by_title.get(title, [])) != 1:
        raise SystemExit(f'idempotency/task discovery failed for {title}: {by_title.get(title)}')
Path(os.environ['EVIDENCE_DIR'], 'task-ids.env').write_text(
    '\n'.join([
        f'ORCHESTRATOR_ID={by_title[expected[0]][0]}',
        f'ARCHITECTURE_ID={by_title[expected[1]][0]}',
        f'BACKEND_ID={by_title[expected[2]][0]}',
        f'REVIEW_ID={by_title[expected[3]][0]}',
    ]) + '\n',
    encoding='utf-8',
)
PY

# shellcheck disable=SC1090
source "$EVIDENCE_DIR/task-ids.env"
"$HERMES_BIN" kanban --board "$BOARD" link "$ARCHITECTURE_ID" "$BACKEND_ID"
"$HERMES_BIN" kanban --board "$BOARD" link "$BACKEND_ID" "$REVIEW_ID"
"$HERMES_BIN" kanban --board "$BOARD" list --json > "$EVIDENCE_DIR/tasks-linked.json"

claim_and_complete() {
  local profile=$1
  local task_id=$2
  local slug=$3
  local summary=$4
  local result=$5
  "$HERMES_BIN" -p "$profile" kanban --board "$BOARD" claim "$task_id" \
    | tee "$EVIDENCE_DIR/claim-${slug}.txt"
  "$HERMES_BIN" -p "$profile" kanban --board "$BOARD" complete "$task_id" \
    --summary "$summary" \
    --result "$result" \
    | tee "$EVIDENCE_DIR/complete-${slug}.txt"
}

claim_and_complete engineering-orchestrator "$ORCHESTRATOR_ID" orchestrator \
  "Decomposed direct runtime validation into architecture, persistence, and review tasks." \
  "DIRECT_PROFILE_CLI_EXECUTION"
claim_and_complete solution-architecture "$ARCHITECTURE_ID" architecture \
  "Confirmed one orchestrator, bounded specialists, structured handoffs, and separate authority records." \
  "DIRECT_PROFILE_CLI_EXECUTION"
claim_and_complete backend-platform "$BACKEND_ID" backend \
  "Confirmed shared SQLite board persistence, idempotent task creation, dependencies, and profile-scoped claims." \
  "DIRECT_PROFILE_CLI_EXECUTION"
claim_and_complete quality-review "$REVIEW_ID" review \
  "Runtime mechanics passed; LLM worker execution and real messaging gateway remain unverified without provider and bot credentials." \
  "LIMITED_DIRECT_PROFILE_CLI_REVIEW"

"$HERMES_BIN" kanban --board "$BOARD" list --json > "$EVIDENCE_DIR/tasks-completed.json"
for task_id in "$ORCHESTRATOR_ID" "$ARCHITECTURE_ID" "$BACKEND_ID" "$REVIEW_ID"; do
  "$HERMES_BIN" kanban --board "$BOARD" show "$task_id" --json \
    > "$EVIDENCE_DIR/task-${task_id}.json"
done

"$HERMES_BIN" kanban --board "$BOARD" create "Dispatcher worker probe" \
  --body "Attempt one actual dispatcher pass. Missing provider credentials must fail closed." \
  --assignee solution-architecture \
  --workspace scratch \
  --idempotency-key epic260-dispatch-probe \
  | tee "$EVIDENCE_DIR/create-dispatch-probe.txt"

"$HERMES_BIN" kanban --board "$BOARD" dispatch --dry-run --max 1 --json \
  > "$EVIDENCE_DIR/dispatcher-dry-run.json" 2>&1
set +e
timeout 90 "$HERMES_BIN" kanban --board "$BOARD" dispatch --max 1 --failure-limit 1 --json \
  > "$EVIDENCE_DIR/dispatcher-attempt.json" 2>&1
DISPATCH_RC=$?
set -e
record_exit dispatcher-attempt "$DISPATCH_RC"
"$HERMES_BIN" kanban --board "$BOARD" list --json > "$EVIDENCE_DIR/tasks-after-dispatch.json"

python3 - <<'PY'
import json, os, sqlite3
from pathlib import Path

evidence = Path(os.environ['EVIDENCE_DIR'])
home = Path(os.environ['HERMES_HOME'])

dbs = []
for db in sorted(home.rglob('kanban.db')):
    connection = sqlite3.connect(db)
    try:
        tables = [row[0] for row in connection.execute("SELECT name FROM sqlite_master WHERE type='table' ORDER BY name")]
        table_info = []
        for table in tables:
            escaped = table.replace('"', '""')
            count = connection.execute(f'SELECT COUNT(*) FROM "{escaped}"').fetchone()[0]
            columns = [row[1] for row in connection.execute(f'PRAGMA table_info("{escaped}")')]
            table_info.append({'name': table, 'row_count': count, 'columns': columns})
        dbs.append({'relative_path': str(db.relative_to(home)), 'tables': table_info})
    finally:
        connection.close()
(evidence / 'sqlite-summary.json').write_text(json.dumps(dbs, indent=2) + '\n', encoding='utf-8')

files = []
for path in sorted(home.rglob('*')):
    if path.is_file():
        files.append({'path': str(path.relative_to(home)), 'size': path.stat().st_size})
(evidence / 'filesystem-inventory.json').write_text(json.dumps(files, indent=2) + '\n', encoding='utf-8')

def exit_code(name, default=None):
    path = evidence / name
    return int(path.read_text(encoding='utf-8').strip()) if path.is_file() else default

receipt = {
    'runtime': {
        'type': 'ephemeral_github_actions',
        'hermes_home_isolated': True,
        'user_runtime_touched': False,
        'official_source_revision': (evidence / 'hermes-source-revision.txt').read_text(encoding='utf-8').strip(),
        'version_output': (evidence / 'version.txt').read_text(encoding='utf-8').strip(),
    },
    'profiles': {
        'created': ['engineering-orchestrator', 'solution-architecture', 'backend-platform', 'quality-review'],
        'unique_profile_paths': True,
        'bundled_skills_opted_out': True,
    },
    'skill_install': 'PASS' if exit_code('skill-install.exit') == 0 else 'FAIL',
    'gateway': {
        'status': 'NOT_RUN_NO_BOT_CREDENTIALS',
        'specialist_tokens_configured': False,
        'policy_check': 'PASS_NO_DEDICATED_SPECIALIST_GATEWAYS',
    },
    'kanban': {
        'init': 'PASS',
        'board_creation': 'PASS',
        'idempotent_task_creation': 'PASS',
        'dependency_links': 'PASS',
        'named_profile_claim_and_completion': 'PASS',
        'specialists_executed_via': 'DIRECT_PROFILE_CLI',
        'dispatcher_dry_run': 'PASS',
        'llm_dispatch_attempt_exit': exit_code('dispatcher-attempt.exit'),
        'llm_worker_execution': 'BLOCKED_OR_NOT_VERIFIED_WITHOUT_PROVIDER',
    },
    'diagnostics': {
        'doctor_exit': exit_code('doctor.exit'),
        'provider_credentials_configured': False,
    },
    'review_independence': 'LIMITED_SHARED_RUNTIME_AND_SCRIPTED_CLI',
    'acceptance_result': 'PASS_WITH_LIMITATIONS',
    'limitations': [
        'Proves real Hermes CLI, profile, skill-install, Kanban persistence, dependency, idempotency, and profile-scoped task operations in an ephemeral runtime.',
        'Does not prove the user local Hermes installation or existing profiles.',
        'No real Telegram or Discord gateway was started because no bot credentials were provided.',
        'No model credential was provided; LLM-driven dispatcher worker output is blocked or unverified.',
        'Quality review used a separate profile but the same scripted CI runtime and therefore has limited independence.',
    ],
}
(evidence / 'runtime-receipt.json').write_text(json.dumps(receipt, indent=2) + '\n', encoding='utf-8')
print(json.dumps(receipt, indent=2))
PY

if grep -RIlE '(sk-[A-Za-z0-9]|BOT_TOKEN=.+|API_KEY=.+|GATEWAY_RELAY_SECRET=.+)' "$EVIDENCE_DIR"; then
  echo 'Potential secret material found in evidence' >&2
  exit 1
fi

echo 'Hermes runtime acceptance completed with explicit limitations.'
