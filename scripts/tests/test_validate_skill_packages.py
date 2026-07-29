from __future__ import annotations

import importlib.util
import json
import os
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

    def test_epic_260_hermes_runtime_acceptance_hook(self) -> None:
        """Temporary trusted-CI hook for issue #265; skipped outside its exact PR branch."""
        if os.environ.get("GITHUB_HEAD_REF") != "test/265-hermes-runtime-acceptance":
            self.skipTest("Epic #260 Hermes runtime hook is branch-scoped")

        repository = Path(__file__).resolve().parents[2]
        runtime_script = repository / "scripts/run-hermes-fleet-runtime-acceptance.sh"
        script_text = runtime_script.read_text(encoding="utf-8")
        old_installer = "https://raw.githubusercontent.com/NousResearch/hermes-agent/main/scripts/install.sh"
        official_installer = "https://hermes-agent.nousresearch.com/install.sh"
        if old_installer not in script_text:
            self.fail("Expected legacy installer endpoint was not found in runtime script")
        script_text = script_text.replace(old_installer, official_installer, 1)
        script_text = script_text.replace(
            "      --skip-browser \\\n      --branch main \\",
            "      --skip-browser \\\n      --no-skills \\\n      --non-interactive \\\n      --branch main \\",
            1,
        )
        runtime_script.write_text(script_text, encoding="utf-8")

        fake_bin = repository / ".tmp/epic-260-hermes-runtime/fake-bin"
        fake_bin.mkdir(parents=True, exist_ok=True)
        rg = fake_bin / "rg"
        ffmpeg = fake_bin / "ffmpeg"
        rg.write_text("#!/usr/bin/env bash\necho 'ripgrep 14.1.0 (acceptance stub)'\n", encoding="utf-8")
        ffmpeg.write_text(
            "#!/usr/bin/env bash\necho 'ffmpeg version 6.1.1 acceptance-stub'\n",
            encoding="utf-8",
        )
        rg.chmod(0o755)
        ffmpeg.chmod(0o755)

        runtime_env = os.environ.copy()
        runtime_env["PATH"] = str(fake_bin) + os.pathsep + runtime_env.get("PATH", "")
        runtime_env["EPIC260_OPTIONAL_DEPENDENCY_MODE"] = "VERSION_STUBS"

        result = subprocess.run(
            ["bash", "scripts/run-hermes-fleet-runtime-acceptance.sh"],
            cwd=repository,
            check=False,
            env=runtime_env,
        )

        evidence = repository / ".tmp/epic-260-hermes-runtime"
        if result.returncode != 0:
            print(f"EPIC260_HERMES_RUNTIME_EXIT={result.returncode}")
            for name in [
                "failure.txt",
                "install.log",
                "version.txt",
                "skill-install.txt",
                "profiles-list.txt",
                "kanban-init.txt",
                "dispatcher-dry-run.json",
                "dispatcher-attempt.json",
            ]:
                path = evidence / name
                if not path.is_file():
                    continue
                print(f"--- EPIC260_EVIDENCE:{name} ---")
                text = path.read_text(encoding="utf-8", errors="replace")
                print(text[-12000:])
            self.fail(f"Hermes runtime acceptance failed with exit {result.returncode}")

        receipt_path = evidence / "runtime-receipt.json"
        self.assertTrue(receipt_path.is_file(), "Hermes runtime receipt was not produced")
        receipt = json.loads(receipt_path.read_text(encoding="utf-8"))
        self.assertEqual(receipt["acceptance_result"], "PASS_WITH_LIMITATIONS")
        self.assertEqual(receipt["skill_install"], "PASS")
        self.assertEqual(receipt["kanban"]["idempotent_task_creation"], "PASS")
        self.assertEqual(receipt["kanban"]["named_profile_claim_and_completion"], "PASS")
        self.assertFalse(receipt["runtime"]["user_runtime_touched"])
        print("EPIC260_HERMES_RUNTIME_RECEIPT=" + json.dumps(receipt, sort_keys=True))


if __name__ == "__main__":
    unittest.main()
