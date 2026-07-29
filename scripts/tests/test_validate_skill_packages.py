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
        subprocess.run(
            ["bash", "scripts/run-hermes-fleet-runtime-acceptance.sh"],
            cwd=repository,
            check=True,
            env=os.environ.copy(),
        )

        receipt_path = repository / ".tmp/epic-260-hermes-runtime/runtime-receipt.json"
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
