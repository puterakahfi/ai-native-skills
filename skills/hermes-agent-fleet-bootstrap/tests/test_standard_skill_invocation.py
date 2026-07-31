from __future__ import annotations

import unittest
from pathlib import Path


PACKAGE = Path(__file__).resolve().parents[1]
SKILL = PACKAGE / "SKILL.md"
REFERENCE = PACKAGE / "references" / "one-command-cli.md"


class StandardSkillInvocationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.skill_text = SKILL.read_text(encoding="utf-8")
        cls.reference_text = REFERENCE.read_text(encoding="utf-8")

    def test_primary_usage_is_the_standard_slash_command(self) -> None:
        expected = (
            "/hermes-agent-fleet-bootstrap bootstrap "
            "native-ai-engineering --apply"
        )
        self.assertIn(expected, self.skill_text)
        self.assertIn(expected, self.reference_text)

    def test_runner_uses_standard_skill_directory_variable(self) -> None:
        expected = '${HERMES_SKILL_DIR}/scripts/hermes-fleet'
        self.assertIn(expected, self.skill_text)
        self.assertIn(expected, self.reference_text)

    def test_primary_sections_precede_runner_and_low_level_reference(self) -> None:
        slash = "/hermes-agent-fleet-bootstrap bootstrap native-ai-engineering"
        installed_runner = 'bash "${HERMES_SKILL_DIR}/scripts/hermes-fleet"'
        repository_runner = "bash skills/hermes-agent-fleet-bootstrap/scripts/hermes-fleet"

        self.assertLess(self.skill_text.index(slash), self.skill_text.index(installed_runner))
        self.assertLess(
            self.reference_text.index(slash),
            self.reference_text.index(repository_runner),
        )
        self.assertNotIn(repository_runner, self.skill_text)
        self.assertIn("CI, debugging, recovery, and development", self.reference_text)

    def test_all_supported_operations_have_standard_examples(self) -> None:
        examples = [
            "/hermes-agent-fleet-bootstrap bootstrap native-ai-engineering",
            "/hermes-agent-fleet-bootstrap audit native-ai-engineering",
            "/hermes-agent-fleet-bootstrap reconcile native-ai-engineering",
        ]
        for example in examples:
            with self.subTest(example=example):
                self.assertIn(example, self.skill_text)
                self.assertIn(example, self.reference_text)

    def test_skill_forbids_manual_reproduction_of_executor_steps(self) -> None:
        self.assertIn("Do not manually reproduce", self.skill_text)
        self.assertIn("must not manually reproduce", self.reference_text)


if __name__ == "__main__":
    unittest.main()
