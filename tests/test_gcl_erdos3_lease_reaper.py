from __future__ import annotations

import json
import tempfile
import unittest
from datetime import datetime, timezone
from pathlib import Path

from ci.gcl_erdos3_lease_reaper import expire_v03


class GclErdos3LeaseReaperTests(unittest.TestCase):
    def setUp(self) -> None:
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        base = self.root / "work_packages/GCL_ERDOS3"
        (base / "dispatches").mkdir(parents=True)

        self.dispatch_id = "GCL-ERDOS3-E3-V03-IA-003"
        self.agent_ref = "INDEPENDENT-AGENT-E3-V03-003"
        dispatch = {
            "dispatch_id": self.dispatch_id,
            "assignment_id": "E3-V03",
            "agent_ref": self.agent_ref,
            "issue_number": 900,
            "issue_url": "https://github.com/grandchallenge/MATHSOLVE/issues/900",
            "state": "DISPATCHED__AWAITING_RETURN",
            "dispatch_status": "READY_FOR_GITHUB_COMMENT",
            "lease_policy_id": "GCL-IA-LEASE-25M-24M-001",
            "lease_clock_source": "GITHUB_ACTIVATION_COMMENT",
            "lease_epoch": 3,
            "lease_attempt_ordinal": 3,
            "replay_budget_ordinal": 1,
        }
        (base / "dispatches" / f"{self.dispatch_id}.json").write_text(
            json.dumps(dispatch), encoding="utf-8"
        )

        campaign = {
            "status": "ACTIVE__E3_V03_DISPATCHED",
            "dispatch_state": "VERIFY_DISPATCHED__AWAITING_RETURN",
            "active_dispatches": {
                "E3-V03": {
                    "dispatch_id": self.dispatch_id,
                    "issue_number": 900,
                    "lease_epoch": 3,
                }
            },
            "verification_dispatches": {
                "E3-V03": {
                    "dispatch_id": self.dispatch_id,
                    "issue_number": 900,
                    "state": "DISPATCHED__AWAITING_RETURN",
                }
            },
            "completed_dispatches": {},
        }
        (base / "CAMPAIGN.json").write_text(json.dumps(campaign), encoding="utf-8")

        frontier = {
            "nodes": [
                {
                    "id": "E3-V-B03",
                    "status": "LAUNCHED",
                    "replay_budget": 1,
                    "replay_budget_consumed": 0,
                    "dispatch": {
                        "dispatch_id": self.dispatch_id,
                        "issue_number": 900,
                        "lease_epoch": 3,
                    },
                },
                {
                    "id": "E3-Q4-GLUING-RADIUS",
                    "status": "FORMULATED_PENDING_VERIFY",
                    "promotion_gate": "E3-V03",
                },
            ]
        }
        (base / "FRONTIER.json").write_text(json.dumps(frontier), encoding="utf-8")

    def tearDown(self) -> None:
        self.tmp.cleanup()

    @staticmethod
    def dt(value: str) -> datetime:
        return datetime.fromisoformat(value.replace("Z", "+00:00")).astimezone(timezone.utc)

    def activation(self) -> dict:
        return {
            "id": 500,
            "body": (
                "GCL-LEASE-ACTIVATION/1\n"
                f"dispatch_id: {self.dispatch_id}\n"
                "assignment: E3-V03\n"
                "lease_epoch: 3\n"
                "lease_duration_minutes: 25\n"
                "agent_max_execution_minutes: 24"
            ),
            "created_at": "2026-10-04T01:00:00Z",
        }

    def result(self, created_at: str) -> dict:
        return {
            "id": 600,
            "body": (
                "GCL-CONTRIBUTION-RESULT/1\n"
                f"dispatch_id: {self.dispatch_id}\n"
                "assignment: E3-V03\n"
                f"agent_ref: {self.agent_ref}\n"
                "disposition: VERIFIED\n"
                "context_class: ZERO_CONTEXT\n"
                "external_sources: PROTECTED_PACKET_ONLY\n"
                "lease_epoch: 3\n"
                "agent_elapsed_minutes: 24\n"
            ),
            "created_at": created_at,
        }

    def test_unactivated_lease_is_not_reaped(self) -> None:
        result = expire_v03(self.root, self.dt("2026-10-04T02:00:00Z"), [])
        self.assertFalse(result["changed"])
        self.assertEqual(result["reason"], "LEASE_NOT_ACTIVATED")

    def test_active_lease_is_not_reaped(self) -> None:
        result = expire_v03(self.root, self.dt("2026-10-04T01:20:00Z"), [self.activation()])
        self.assertFalse(result["changed"])
        self.assertEqual(result["reason"], "LEASE_STILL_ACTIVE")
        self.assertEqual(result["lease_expires_at"], "2026-10-04T01:25:00Z")

    def test_silent_expiry_releases_without_consuming_replay(self) -> None:
        result = expire_v03(self.root, self.dt("2026-10-04T01:30:00Z"), [self.activation()])
        self.assertTrue(result["changed"])
        self.assertFalse(result["replay_budget_consumed"])

        base = self.root / "work_packages/GCL_ERDOS3"
        dispatch = json.loads((base / "dispatches" / f"{self.dispatch_id}.json").read_text())
        campaign = json.loads((base / "CAMPAIGN.json").read_text())
        frontier = json.loads((base / "FRONTIER.json").read_text())

        self.assertEqual(dispatch["state"], "LEASE_EXPIRED__NO_RETURN")
        self.assertEqual(dispatch["lease_activation_comment_id"], 500)
        self.assertEqual(dispatch["lease_started_at_observed"], "2026-10-04T01:00:00Z")
        self.assertEqual(dispatch["lease_expires_at_observed"], "2026-10-04T01:25:00Z")
        self.assertTrue(dispatch["stale_return_fenced"])
        self.assertFalse(dispatch["replay_budget_consumed"])
        self.assertEqual(campaign["active_dispatches"], {})
        self.assertFalse(campaign["completed_dispatches"]["E3-V03-LEASE-003"]["replay_budget_consumed"])
        vnode = next(x for x in frontier["nodes"] if x["id"] == "E3-V-B03")
        self.assertEqual(vnode["status"], "LEASE_EXPIRED__REISSUE_REQUIRED")
        self.assertEqual(vnode["replay_budget_consumed"], 0)

    def test_timely_result_prevents_silent_expiry(self) -> None:
        comments = [self.activation(), self.result("2026-10-04T01:24:59Z")]
        result = expire_v03(self.root, self.dt("2026-10-04T01:40:00Z"), comments)
        self.assertFalse(result["changed"])
        self.assertEqual(result["reason"], "TIMELY_RESULT_PRESENT_DO_NOT_EXPIRE")

    def test_late_result_does_not_revive_expired_lease(self) -> None:
        comments = [self.activation(), self.result("2026-10-04T01:25:01Z")]
        result = expire_v03(self.root, self.dt("2026-10-04T01:40:00Z"), comments)
        self.assertTrue(result["changed"])

    def test_result_for_other_dispatch_does_not_block_expiry(self) -> None:
        other = self.result("2026-10-04T01:24:00Z")
        other["body"] = other["body"].replace(self.dispatch_id, "GCL-ERDOS3-E3-V03-IA-999")
        result = expire_v03(self.root, self.dt("2026-10-04T01:40:00Z"), [self.activation(), other])
        self.assertTrue(result["changed"])


if __name__ == "__main__":
    unittest.main()
