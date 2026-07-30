from __future__ import annotations

import json
import unittest
from pathlib import Path


TEST_FILE = Path(__file__).resolve()
PACKAGE_ROOT = TEST_FILE.parents[1]
SKILLS_ROOT = TEST_FILE.parents[2]
REPOSITORY_ROOT = TEST_FILE.parents[3]
PRESET_PATH = PACKAGE_ROOT / "assets" / "presets" / "native-ai-engineering.json"
INVENTORY_PATH = REPOSITORY_ROOT / "docs" / "capability-inventory.json"


class NativePresetSkillMappingTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.preset = json.loads(PRESET_PATH.read_text(encoding="utf-8"))
        cls.inventory = json.loads(INVENTORY_PATH.read_text(encoding="utf-8"))
        cls.profiles = {
            profile["id"]: profile for profile in cls.preset["profiles"]
        }
        cls.skill_sets = {
            profile_id: set(profile["skills"])
            for profile_id, profile in cls.profiles.items()
        }
        cls.catalog_names = {
            item["name"] for item in cls.inventory["items"]
        }

    def test_preset_version_and_topology_are_explicit(self) -> None:
        self.assertEqual(self.preset["version"], "1.1.0")
        self.assertEqual(self.preset["topology"], "orchestrator_with_specialists")
        self.assertEqual(self.preset["orchestrator"], "engineering-orchestrator")
        self.assertEqual(
            set(self.profiles),
            {
                "engineering-orchestrator",
                "product-development",
                "solution-architecture",
                "product-design",
                "frontend-engineering",
                "backend-platform",
                "quality-review",
            },
        )

    def test_every_mapped_capability_is_catalog_resolvable(self) -> None:
        mapped = set().union(*self.skill_sets.values())
        missing_from_catalog = sorted(mapped - self.catalog_names)
        missing_from_repository = sorted(
            skill
            for skill in mapped
            if not (SKILLS_ROOT / skill / "SKILL.md").is_file()
        )
        self.assertEqual(missing_from_catalog, [])
        self.assertEqual(missing_from_repository, [])

    def test_orchestrator_has_routing_and_continuity_capabilities(self) -> None:
        self.assertTrue(
            {
                "hermes-agent-fleet-bootstrap",
                "hermes-profile-bootstrap",
                "workflow-router",
                "role-switcher",
                "systems-reasoning",
                "decision-provenance",
                "context-manager",
                "task-continuity",
                "delivery-work-breakdown",
                "skill-eval",
            }.issubset(self.skill_sets["engineering-orchestrator"])
        )

    def test_product_profile_has_planning_and_acceptance_capabilities(self) -> None:
        self.assertTrue(
            {
                "product-development-workflow",
                "product-manager",
                "product-requirements",
                "business-value-alignment",
                "user-research",
                "experiment-design",
                "delivery-work-breakdown",
                "acceptance-testing",
                "decision-provenance",
            }.issubset(self.skill_sets["product-development"])
        )

    def test_architecture_profile_has_boundary_and_contract_capabilities(self) -> None:
        self.assertTrue(
            {
                "implementation-context-discovery",
                "systems-reasoning",
                "systems-thinking",
                "master-engineer",
                "spec-workflow",
                "domain-driven-design",
                "ports-and-adapters",
                "clean-architecture",
                "solid-design",
                "design-patterns",
                "api-contract",
                "data-modeling",
                "adr",
                "event-driven-design",
                "service-design",
                "threat-modeling",
                "resilience-engineering",
                "observability-design",
                "architecture-review",
                "decision-provenance",
            }.issubset(self.skill_sets["solution-architecture"])
        )

    def test_design_profile_has_experience_and_design_system_capabilities(self) -> None:
        self.assertTrue(
            {
                "master-design",
                "design-review",
                "design-system",
                "information-architecture",
                "accessibility",
                "responsiveness",
                "ui-components",
                "ux-ui-patterns",
                "visual-hierarchy",
                "composition",
                "readability",
                "design-interaction",
                "adaptive-component-design",
                "content-strategy",
                "decision-provenance",
            }.issubset(self.skill_sets["product-design"])
        )

    def test_implementation_profiles_have_delivery_and_quality_capabilities(self) -> None:
        shared = {
            "implementation-context-discovery",
            "master-engineer",
            "new-feature-workflow",
            "bugfix-workflow",
            "production-code-quality-baseline",
            "test-driven-development",
            "clean-code",
            "solid-design",
            "refactoring",
            "systematic-debugging",
            "git-workflow",
        }
        self.assertTrue(shared.issubset(self.skill_sets["frontend-engineering"]))
        self.assertTrue(shared.issubset(self.skill_sets["backend-platform"]))

        self.assertTrue(
            {
                "ui-components",
                "design-system",
                "ux-patterns-for-developers",
                "accessibility",
                "responsiveness",
                "web-performance",
            }.issubset(self.skill_sets["frontend-engineering"])
        )
        self.assertTrue(
            {
                "clean-architecture",
                "domain-driven-design",
                "ports-and-adapters",
                "design-patterns",
                "api-contract",
                "data-modeling",
                "service-design",
                "event-driven-design",
                "observability-design",
                "resilience-engineering",
            }.issubset(self.skill_sets["backend-platform"])
        )

    def test_quality_profile_has_independent_verification_capabilities(self) -> None:
        quality = self.skill_sets["quality-review"]
        self.assertTrue(
            {
                "acceptance-testing",
                "software-testing-workflow",
                "code-review-workflow",
                "architecture-review",
                "security-review",
                "design-review",
                "threat-modeling",
                "accessibility",
                "web-performance",
                "decision-provenance",
                "skill-eval",
            }.issubset(quality)
        )
        self.assertTrue(
            quality.isdisjoint(
                {
                    "new-feature-workflow",
                    "bugfix-workflow",
                    "git-workflow",
                    "test-driven-development",
                    "refactoring",
                    "product-manager",
                    "product-requirements",
                }
            )
        )

    def test_profile_authority_boundaries_are_not_flattened(self) -> None:
        routing_capabilities = {
            "hermes-agent-fleet-bootstrap",
            "hermes-profile-bootstrap",
            "workflow-router",
            "role-switcher",
        }
        for profile_id, skills in self.skill_sets.items():
            if profile_id == "engineering-orchestrator":
                continue
            self.assertTrue(
                skills.isdisjoint(routing_capabilities),
                f"{profile_id} must not receive orchestrator-only capabilities",
            )

        product_authority = {
            "product-development-workflow",
            "product-manager",
            "product-requirements",
            "business-value-alignment",
            "user-research",
            "experiment-design",
        }
        for profile_id, skills in self.skill_sets.items():
            if profile_id == "product-development":
                continue
            self.assertTrue(
                skills.isdisjoint(product_authority),
                f"{profile_id} must not absorb product authority",
            )

        all_mapped = set().union(*self.skill_sets.values())
        self.assertNotIn("deployment-workflow", all_mapped)

    def test_skill_manifests_are_curated_not_full_catalog_copies(self) -> None:
        catalog_size = len(self.catalog_names)
        for profile_id, profile in self.profiles.items():
            skills = profile["skills"]
            self.assertEqual(
                len(skills),
                len(set(skills)),
                f"{profile_id} contains duplicate skill IDs",
            )
            self.assertLess(
                len(skills),
                catalog_size / 2,
                f"{profile_id} received an overly broad catalog copy",
            )


if __name__ == "__main__":
    unittest.main()
