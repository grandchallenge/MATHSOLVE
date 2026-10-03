from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
NSCI_WORKFLOW = ROOT / ".github/workflows/ns-ci-independent-contribution-intake.yml"
OPENMATH_WORKFLOW = ROOT / ".github/workflows/openmath-cex-independent-contribution-intake.yml"


class ContributionIntakeRoutingTest(unittest.TestCase):
    def test_nsci_route_is_campaign_specific(self):
        text = NSCI_WORKFLOW.read_text(encoding="utf-8")
        self.assertIn(
            "startsWith(github.event.issue.title, '[GCL-CONTRIB] NSCI-')",
            text,
        )
        self.assertNotIn(
            "startsWith(github.event.issue.title, '[GCL-CONTRIB] ') &&",
            text,
        )

    def test_openmath_route_is_campaign_specific(self):
        text = OPENMATH_WORKFLOW.read_text(encoding="utf-8")
        self.assertIn(
            "startsWith(github.event.issue.title, '[GCL-CONTRIB] OPENMATH-2026 ')",
            text,
        )

    def test_openmath_snapshot_does_not_open_pr_with_workflow_token(self):
        text = OPENMATH_WORKFLOW.read_text(encoding="utf-8")
        self.assertNotIn("gh pr create", text)
        self.assertNotIn("pull-requests: write", text)
        self.assertIn("environment: release-trust", text)
        self.assertIn("steps.programme-wake-token.outputs.token", text)
        self.assertIn("-f event_type=openmath-return-ready", text)

    def test_routes_are_mutually_exclusive_for_protected_title_prefixes(self):
        nsci_prefix = "[GCL-CONTRIB] NSCI-"
        openmath_prefix = "[GCL-CONTRIB] OPENMATH-2026 "
        self.assertFalse(nsci_prefix.startswith(openmath_prefix))
        self.assertFalse(openmath_prefix.startswith(nsci_prefix))


if __name__ == "__main__":
    unittest.main()
