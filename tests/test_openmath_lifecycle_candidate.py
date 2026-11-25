import copy
import json
import tempfile
import unittest
from pathlib import Path

from ci.openmath_lifecycle_candidate import refresh_summary, board_text, index_text, plan, successor_identity, successor_transport_header, apply_candidate, LifecycleCandidateError

ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / ".gcl/campaigns/OPENMATH-2026/CEX_ASSIGNMENTS.json"


class OpenMathLifecycleCandidateStateTest(unittest.TestCase):
    def load_registry(self):
        return json.loads(REGISTRY.read_text(encoding="utf-8"))

    def test_h1_uses_wp_successor_identity(self):
        self.assertEqual(successor_identity("OM26-H1-WP01"), ("OM26-H1", "OM26-H1-WP02", "OM26-H1-WP02-IA-001", "INDEPENDENT-AGENT-102"))

    def test_replacement_return_for_closed_dispatch_cannot_mutate_registry(self):
        registry=self.load_registry()
        predecessor=next(x for x in registry["assignments"] if x["assignment_id"]=="OM26-H2-WP03")
        with tempfile.TemporaryDirectory() as td:
            root=Path(td)/"repo"
            intake=Path(td)/"intake"
            intake.mkdir()
            for path in (".gcl/campaigns/OPENMATH-2026/CEX_ASSIGNMENTS.json", "work_packages/OPENMATH_2026/HILL_LANES.json"):
                target=root/path
                target.parent.mkdir(parents=True,exist_ok=True)
                target.write_bytes((ROOT/path).read_bytes())
            before={p.relative_to(root):p.read_bytes() for p in root.rglob("*") if p.is_file()}
            (intake/"META.json").write_text(json.dumps({"comment_id":999999}))
            (intake/"RECEIPT.json").write_text(json.dumps({"assignment_id":predecessor["assignment_id"],"dispatch_id":predecessor["lease"]["dispatch_id"],"agent_ref":predecessor["lease"]["agent_ref"]}))
            (intake/"RAW.md").write_text("GCL-CONTRIBUTION-RESULT/1\nreplacement evidence\n")
            with self.assertRaisesRegex(LifecycleCandidateError,"predecessor is not open: ACCEPTED"):
                apply_candidate(root,intake,999999,"https://github.com/grandchallenge/MATHSOLVE/issues/999999")
            after={p.relative_to(root):p.read_bytes() for p in root.rglob("*") if p.is_file()}
            self.assertEqual(before,after)

    def test_current_summary_is_state_derived(self):
        registry = self.load_registry()
        expected = copy.deepcopy(registry["mathematics_release_policy"]["summary"])
        self.assertEqual(refresh_summary(registry), expected)

    def test_generated_board_and_index_use_literal_markdown(self):
        registry=self.load_registry()
        board=board_text(registry)
        launch_index=index_text(registry)
        self.assertIn("| `OM26-H2-WP10` | `OM26-H2` |",board)
        self.assertIn("`LINK_IN_RELAY_OUT`",board)
        self.assertIn("`LINK_IN_RELAY_OUT`",launch_index)
        self.assertNotIn("\\`",board)
        self.assertNotIn("\\`",launch_index)


    def test_generated_successor_requires_authenticated_durable_return(self):
        header = successor_transport_header()
        self.assertIn("GITHUB_ACCESS_REQUIRED: PARTICIPANT_ENVIRONMENT_AUTHENTICATED_COMMENT_CAPABILITY", header)
        self.assertIn("RETURN_COMPLETION_RECEIPT_REQUIRED: GITHUB_ISSUE_COMMENT_URL", header)
        self.assertNotIn("GITHUB_ACCESS_REQUIRED: NO", header)

    def test_terminal_mode_rejects_automatic_successor(self):
        with tempfile.TemporaryDirectory() as temp:
            intake=Path(temp)/"intake"
            root=Path(temp)/"repo"
            intake.mkdir(); root.mkdir()
            contract=root/".gcl/campaigns/OPENMATH-2026/LIFECYCLE_CONTRACT.json"
            contract.parent.mkdir(parents=True)
            contract.write_text(json.dumps({
                "successor_policy":{"mode":"FRONTIER_GATE_REQUIRED"}
            }),encoding="utf-8")
            (intake/"META.json").write_text(json.dumps({"comment_id":123}),encoding="utf-8")
            (intake/"RECEIPT.json").write_text(json.dumps({
                "assignment_id":"OM26-H3-WP01",
                "dispatch_id":"OM26-H3-WP01-IA-001",
            }),encoding="utf-8")
            (intake/"RAW.md").write_text("GCL-CONTRIBUTION-RESULT/1\n",encoding="utf-8")
            with self.assertRaisesRegex(LifecycleCandidateError, "protected frontier disposition required"):
                plan(intake,root)


    def test_terminal_summary_has_no_open_replay_leases(self):
        registry = self.load_registry()
        summary = refresh_summary(registry)
        self.assertEqual(summary["leased_not_launched_agents"], 0)
        self.assertEqual(summary["launched_agents"], 0)
        scripts = list(registry["launch_contract"]["current_scripts"].values())
        scripts += list(registry["launch_contract"].get("support_scripts", {}).values())
        self.assertTrue(all(row.get("executable") is False for row in scripts))


if __name__ == "__main__":
    unittest.main()
