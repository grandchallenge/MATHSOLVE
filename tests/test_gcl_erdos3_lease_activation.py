from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from ci.gcl_erdos3_lease_activation import ActivationError, git_blob_sha1_text, plan_activation


class GclErdos3LeaseActivationTests(unittest.TestCase):
    def setUp(self) -> None:
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        base = self.root / "work_packages/GCL_ERDOS3"
        (base / "dispatches").mkdir(parents=True)
        (base / "launch").mkdir(parents=True)

        self.dispatch_id = "GCL-ERDOS3-E3-V03-IA-003"
        self.active_title = "[GCL-CONTRIB] GCL-ERDOS3 E3-V03-IA-003 — gluing-radius equivalence replay"
        self.staging_title = "[GCL-STAGING] GCL-ERDOS3 E3-V03-IA-003 — gluing-radius equivalence replay"
        self.bootstrap = "GCL-CONTRIBUTION-DISPATCH/1\n\n# E3-V03 epoch 3\n"
        boot = base / "launch/E3-V03-IA-003.md"
        boot.write_text(self.bootstrap, encoding="utf-8")

        dispatch = {
            "dispatch_id": self.dispatch_id,
            "assignment_id": "E3-V03",
            "state": "DISPATCHED__AWAITING_RETURN",
            "dispatch_status": "READY_FOR_GITHUB_COMMENT",
            "lease_policy_id": "GCL-IA-LEASE-25M-24M-001",
            "lease_clock_source": "GITHUB_ACTIVATION_COMMENT",
            "lease_epoch": 3,
            "lease_duration_minutes": 25,
            "agent_max_execution_minutes": 24,
            "github_issue_number": 900,
            "github_issue_title": self.active_title,
            "github_issue_staging_title": self.staging_title,
            "bootstrap_path": "work_packages/GCL_ERDOS3/launch/E3-V03-IA-003.md",
            "bootstrap_blob_sha1": git_blob_sha1_text(self.bootstrap),
        }
        (base / "dispatches" / f"{self.dispatch_id}.json").write_text(
            json.dumps(dispatch), encoding="utf-8"
        )
        campaign = {
            "active_dispatches": {
                "E3-V03": {
                    "dispatch_id": self.dispatch_id,
                    "issue_number": 900,
                    "lease_epoch": 3,
                }
            }
        }
        (base / "CAMPAIGN.json").write_text(json.dumps(campaign), encoding="utf-8")

    def tearDown(self) -> None:
        self.tmp.cleanup()

    def issue(self, *, title: str | None = None, body: str | None = None, state: str = "open") -> dict:
        return {
            "number": 900,
            "title": self.staging_title if title is None else title,
            "body": self.bootstrap if body is None else body,
            "state": state,
        }

    def activation(self, *, ident: int = 501) -> dict:
        return {
            "id": ident,
            "created_at": "2026-10-04T02:00:00Z",
            "body": (
                "GCL-LEASE-ACTIVATION/1\n"
                f"dispatch_id: {self.dispatch_id}\n"
                "assignment: E3-V03\n"
                "lease_epoch: 3\n"
                "lease_duration_minutes: 25\n"
                "agent_max_execution_minutes: 24"
            ),
        }

    def test_staging_issue_requires_activation(self) -> None:
        result = plan_activation(self.root, self.issue(), [])
        self.assertTrue(result["activate"])
        self.assertEqual(result["expected_title"], self.active_title)
        self.assertIn("lease_epoch: 3", result["marker_body"])

    def test_partial_title_switch_can_recover_by_posting_marker(self) -> None:
        result = plan_activation(self.root, self.issue(title=self.active_title), [])
        self.assertTrue(result["activate"])

    def test_existing_marker_is_idempotent(self) -> None:
        result = plan_activation(self.root, self.issue(title=self.active_title), [self.activation()])
        self.assertFalse(result["activate"])
        self.assertEqual(result["reason"], "ALREADY_ACTIVATED")
        self.assertEqual(result["activation_comment_id"], 501)

    def test_duplicate_marker_is_rejected(self) -> None:
        with self.assertRaisesRegex(ActivationError, "multiple matching activation markers"):
            plan_activation(
                self.root,
                self.issue(title=self.active_title),
                [self.activation(ident=501), self.activation(ident=502)],
            )

    def test_result_before_activation_is_rejected(self) -> None:
        comments = [{
            "id": 700,
            "created_at": "2026-10-04T01:59:00Z",
            "body": "GCL-CONTRIBUTION-RESULT/1\ndispatch_id: stale\n",
        }]
        with self.assertRaisesRegex(ActivationError, "before lease activation"):
            plan_activation(self.root, self.issue(), comments)

    def test_bootstrap_drift_is_rejected(self) -> None:
        with self.assertRaisesRegex(ActivationError, "issue body differs"):
            plan_activation(self.root, self.issue(body=self.bootstrap + "tamper\n"), [])

    def test_unexpected_title_is_rejected(self) -> None:
        with self.assertRaisesRegex(ActivationError, "neither protected staging nor active"):
            plan_activation(self.root, self.issue(title="unexpected"), [])

    def test_closed_issue_is_idempotent_noop(self) -> None:
        result = plan_activation(self.root, self.issue(state="closed"), [])
        self.assertFalse(result["activate"])
        self.assertEqual(result["reason"], "CANONICAL_ISSUE_CLOSED")
        self.assertEqual(result["dispatch_id"], self.dispatch_id)
        self.assertEqual(result["issue_number"], 900)
        self.assertEqual(result["lease_epoch"], 3)


if __name__ == "__main__":
    unittest.main()
