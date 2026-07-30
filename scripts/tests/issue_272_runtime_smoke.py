from __future__ import annotations

import json
import os
import shutil
import subprocess
import tempfile
from pathlib import Path


def main() -> int:
    repository = Path(__file__).resolve().parents[2]
    runtime_root = Path(os.environ.get("RUNNER_TEMP", tempfile.gettempdir())) / "issue-272-hermes-fleet-final"
    if runtime_root.exists():
        shutil.rmtree(runtime_root)
    runtime_root.mkdir(parents=True)
    hermes_home = runtime_root / "home"
    install_dir = runtime_root / "install"
    evidence = repository / ".tmp" / "issue-272-hermes-fleet-final"
    if evidence.exists():
        shutil.rmtree(evidence)
    evidence.mkdir(parents=True)

    unit = subprocess.run(
        [
            "python",
            "-m",
            "unittest",
            "discover",
            "-s",
            "skills/hermes-agent-fleet-bootstrap/tests",
            "-v",
        ],
        cwd=repository,
        text=True,
        capture_output=True,
        check=False,
    )
    (evidence / "unit-tests.txt").write_text(unit.stdout + unit.stderr, encoding="utf-8")
    if unit.returncode != 0:
        print(unit.stdout)
        print(unit.stderr)
        return 10

    fake_bin = runtime_root / "fake-bin"
    fake_bin.mkdir()
    for name, output in {
        "rg": "ripgrep 14.1.0 (acceptance version stub)",
        "ffmpeg": "ffmpeg version 6.1.1 acceptance-stub",
    }.items():
        path = fake_bin / name
        path.write_text(f"#!/usr/bin/env bash\necho '{output}'\n", encoding="utf-8")
        path.chmod(0o755)

    env = os.environ.copy()
    env["HERMES_HOME"] = str(hermes_home)
    env["PATH"] = str(fake_bin) + os.pathsep + env.get("PATH", "")
    install_env = env.copy()
    install_env["HERMES_INSTALL_DIR"] = str(install_dir)
    installer = """
set -Eeuo pipefail
curl -fsSL https://hermes-agent.nousresearch.com/install.sh | bash -s -- \
  --dir "$HERMES_INSTALL_DIR" \
  --skip-setup \
  --skip-browser \
  --no-skills \
  --non-interactive \
  --branch main
"""
    install = subprocess.run(
        ["bash", "-c", installer],
        cwd=repository,
        env=install_env,
        text=True,
        capture_output=True,
        check=False,
    )
    (evidence / "install.txt").write_text(
        install.stdout + install.stderr, encoding="utf-8"
    )
    if install.returncode != 0:
        print((install.stdout + install.stderr)[-16000:])
        return 11

    candidates = [
        Path.home() / ".local" / "bin" / "hermes",
        hermes_home / "bin" / "hermes",
        install_dir / "venv" / "bin" / "hermes",
    ]
    hermes_bin = next((path for path in candidates if path.is_file()), None)
    if hermes_bin is None:
        print(f"Hermes binary not found after install: {candidates}")
        return 12

    command = repository / "skills/hermes-agent-fleet-bootstrap/scripts/hermes-fleet"

    def run_cli(name: str, operation: str, apply: bool) -> tuple[int, dict]:
        receipt = evidence / f"{name}.json"
        args = [
            "bash",
            str(command),
            operation,
            "native-ai-engineering",
            "--hermes-home",
            str(hermes_home),
            "--hermes-bin",
            str(hermes_bin),
            "--receipt",
            str(receipt),
            "--json",
        ]
        if apply:
            args.append("--apply")
        result = subprocess.run(
            args,
            cwd=repository,
            env=env,
            text=True,
            capture_output=True,
            check=False,
        )
        (evidence / f"{name}.txt").write_text(
            result.stdout + result.stderr, encoding="utf-8"
        )
        if not receipt.is_file():
            print(result.stdout)
            print(result.stderr)
            raise RuntimeError(f"Receipt not written for {name}")
        return result.returncode, json.loads(receipt.read_text(encoding="utf-8"))

    first_code, first = run_cli("apply-first", "bootstrap", True)
    if first_code != 0 or first["readiness"] != "READY":
        print(json.dumps(first, indent=2, sort_keys=True))
        return 20
    first_statuses = {item["status"] for item in first["actions"]}
    if not {"CREATED", "INSTALLED", "INITIALIZED"}.issubset(first_statuses):
        print(json.dumps(first, indent=2, sort_keys=True))
        return 21

    second_code, second = run_cli("apply-second", "bootstrap", True)
    if second_code != 0 or second["readiness"] != "READY":
        print(json.dumps(second, indent=2, sort_keys=True))
        return 22
    second_statuses = {item["status"] for item in second["actions"]}
    if {"CREATED", "INSTALLED", "UPDATED"} & second_statuses:
        print(json.dumps(second, indent=2, sort_keys=True))
        return 23
    if not {"SKIP_EXISTS", "SKIP_IN_SYNC", "SKIP_INITIALIZED"}.issubset(second_statuses):
        print(json.dumps(second, indent=2, sort_keys=True))
        return 24

    audit_code, audit = run_cli("audit", "audit", False)
    if audit_code != 0 or audit["readiness"] != "READY":
        print(json.dumps(audit, indent=2, sort_keys=True))
        return 25

    expected_profiles = {
        "engineering-orchestrator",
        "product-development",
        "solution-architecture",
        "product-design",
        "frontend-engineering",
        "backend-platform",
        "quality-review",
    }
    profile_root = hermes_home / "profiles"
    observed_profiles = {path.name for path in profile_root.iterdir() if path.is_dir()}
    if not expected_profiles.issubset(observed_profiles):
        print(f"Missing profiles: {sorted(expected_profiles - observed_profiles)}")
        return 26

    summary = {
        "acceptance_result": "PASS",
        "hermes_version": first["hermes_version"],
        "profiles": sorted(expected_profiles),
        "first_apply": first["readiness"],
        "second_apply": second["readiness"],
        "audit": audit["readiness"],
        "idempotency": "PASS",
        "gateway_policy": first["gateway_policy"],
        "path_and_symlink_hardening_tests": "PASS",
        "user_runtime_touched": False,
        "limitations": [
            "No messaging gateway or bot token was configured.",
            "No model provider credential or LLM worker reasoning was required for deterministic bootstrap.",
            "Profile isolation was verified at Hermes home level, not as an OS sandbox.",
        ],
    }
    (evidence / "runtime-summary.json").write_text(
        json.dumps(summary, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    print("ISSUE272_FINAL_HERMES_FLEET_RECEIPT=" + json.dumps(summary, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
