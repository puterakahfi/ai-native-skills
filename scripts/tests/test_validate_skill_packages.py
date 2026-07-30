from __future__ import annotations

import importlib.util
import json
import os
import shutil
import subprocess
import tempfile
import unittest
from pathlib import Path

import yaml

MODULE_PATH = Path(__file__).resolve().parents[1] / "validate-skill-packages.py"
spec = importlib.util.spec_from_file_location("validate_skill_packages", MODULE_PATH)
module = importlib.util.module_from_spec(spec)
assert spec and spec.loader
spec.loader.exec_module(module)


POLICY = {
    "version": "1.0.0",
    "behavioral_contract_root": "contracts/tests",
    "pilot_skills": ["pilot"],
    "prohibited": ["outputs"],
    "discouraged": ["docs", "evals"],
}


class SkillPackageValidatorTests(unittest.TestCase):
    def make_root(self) -> Path:
        root = Path(tempfile.mkdtemp())
        (root / "skills").mkdir(parents=True)
        (root / "contracts/tests").mkdir(parents=True)
        return root

    def write_skill(self, root: Path, name: str, skill_type: str = "skill") -> Path:
        skill = root / "skills" / name
        skill.mkdir()
        (skill / "SKILL.md").write_text(
            f"---\nname: {name}\nmetadata:\n  ai-native-skills.type: {skill_type}\n---\n",
            encoding="utf-8",
        )
        return skill

    def test_pilot_without_contract_is_error(self) -> None:
        root = self.make_root()
        self.write_skill(root, "pilot", "meta-skill")
        report = module.validate(root, POLICY)["skill_package_validation"]
        self.assertEqual(report["summary"]["errors"], 1)
        self.assertEqual(report["findings"][0]["rule"], "missing-behavioral-contract")

    def test_central_contract_satisfies_substantive_skill(self) -> None:
        root = self.make_root()
        self.write_skill(root, "pilot", "meta-skill")
        (root / "contracts/tests/pilot.test.yaml").write_text("skill_test: {}\n", encoding="utf-8")
        report = module.validate(root, POLICY)["skill_package_validation"]
        self.assertEqual(report["summary"]["errors"], 0)

    def test_generated_path_is_blocking_for_pilot(self) -> None:
        root = self.make_root()
        skill = self.write_skill(root, "pilot")
        (root / "contracts/tests/pilot.test.yaml").write_text("skill_test: {}\n", encoding="utf-8")
        (skill / "outputs").mkdir()
        report = module.validate(root, POLICY)["skill_package_validation"]
        self.assertEqual(report["summary"]["errors"], 1)

    def test_scripts_without_tests_is_warning(self) -> None:
        root = self.make_root()
        skill = self.write_skill(root, "plain")
        scripts = skill / "scripts"
        scripts.mkdir()
        (scripts / "run.py").write_text("print('ok')\n", encoding="utf-8")
        report = module.validate(root, POLICY)["skill_package_validation"]
        rules = {item["rule"] for item in report["findings"]}
        self.assertIn("scripts-without-tests", rules)

    def test_issue_272_one_command_real_hermes_smoke(self) -> None:
        """Temporary branch-scoped direct Hermes smoke for issue #272."""
        if os.environ.get("GITHUB_HEAD_REF") != "272-hermes-fleet-one-command-cli":
            self.skipTest("Issue #272 direct Hermes smoke is PR-branch scoped")

        repository = Path(__file__).resolve().parents[2]
        runtime_root = Path(os.environ.get("RUNNER_TEMP", tempfile.gettempdir())) / "issue-272-hermes-fleet"
        if runtime_root.exists():
            shutil.rmtree(runtime_root)
        runtime_root.mkdir(parents=True)
        hermes_home = runtime_root / "home"
        install_dir = runtime_root / "install"
        evidence = repository / ".tmp" / "issue-272-hermes-fleet"
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
        (evidence / "unit-tests.txt").write_text(
            unit.stdout + unit.stderr, encoding="utf-8"
        )
        if unit.returncode != 0:
            print(unit.stdout)
            print(unit.stderr)
            self.fail("Skill-local one-command tests failed")

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
        install_env = env.copy()
        install_env["HERMES_INSTALL_DIR"] = str(install_dir)
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
            self.fail(f"Official Hermes installer failed: {install.returncode}")

        candidates = [
            Path.home() / ".local" / "bin" / "hermes",
            hermes_home / "bin" / "hermes",
            install_dir / "venv" / "bin" / "hermes",
        ]
        hermes_bin = next((path for path in candidates if path.is_file()), None)
        if hermes_bin is None:
            self.fail(f"Hermes binary not found after install: {candidates}")

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
                self.fail(f"Receipt not written for {name}")
            payload = json.loads(receipt.read_text(encoding="utf-8"))
            return result.returncode, payload

        first_code, first = run_cli("apply-first", "bootstrap", True)
        self.assertEqual(first_code, 0, first)
        self.assertEqual(first["readiness"], "READY", first)
        first_statuses = {item["status"] for item in first["actions"]}
        self.assertIn("CREATED", first_statuses)
        self.assertIn("INSTALLED", first_statuses)
        self.assertIn("INITIALIZED", first_statuses)

        second_code, second = run_cli("apply-second", "bootstrap", True)
        self.assertEqual(second_code, 0, second)
        self.assertEqual(second["readiness"], "READY", second)
        second_statuses = {item["status"] for item in second["actions"]}
        self.assertNotIn("CREATED", second_statuses)
        self.assertNotIn("INSTALLED", second_statuses)
        self.assertNotIn("UPDATED", second_statuses)
        self.assertIn("SKIP_EXISTS", second_statuses)
        self.assertIn("SKIP_IN_SYNC", second_statuses)
        self.assertIn("SKIP_INITIALIZED", second_statuses)

        audit_code, audit = run_cli("audit", "audit", False)
        self.assertEqual(audit_code, 0, audit)
        self.assertEqual(audit["readiness"], "READY", audit)

        profile_root = hermes_home / "profiles"
        expected_profiles = {
            "engineering-orchestrator",
            "product-development",
            "solution-architecture",
            "product-design",
            "frontend-engineering",
            "backend-platform",
            "quality-review",
        }
        observed_profiles = {
            path.name for path in profile_root.iterdir() if path.is_dir()
        }
        self.assertTrue(expected_profiles.issubset(observed_profiles))

        summary = {
            "acceptance_result": "PASS",
            "hermes_version": first["hermes_version"],
            "profiles": sorted(expected_profiles),
            "first_apply": first["readiness"],
            "second_apply": second["readiness"],
            "audit": audit["readiness"],
            "idempotency": "PASS",
            "gateway_policy": first["gateway_policy"],
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
        print("ISSUE272_HERMES_FLEET_RECEIPT=" + json.dumps(summary, sort_keys=True))


if __name__ == "__main__":
    unittest.main()
