from __future__ import annotations

import unittest
from unittest.mock import patch

import ci.ns_ci_github_contribution_intake as intake


class WorkerQueueIntakeBindingTest(unittest.TestCase):
    def event(self, actor: str = "alice"):
        return {
            "issue": {"number": 7, "title": "job", "body": "GCL-CONTRIBUTION-DISPATCH/1\n"},
            "comment": {
                "id": 99,
                "body": "ignored-by-mock",
                "created_at": "2026-10-05T01:00:00Z",
                "user": {"login": actor},
            },
        }

    def dispatch(self):
        return {
            "assignment_id": "A",
            "concurrency_mode": "independent_blind",
            "agent_ref": "AGENT",
        }

    def parsed(self):
        return {
            "preamble": {"dispatch_id": "NSCI-C2-A-BLIND-001", "assignment": "A"},
            "sections": {},
        }

    def run_validate(self, actor: str, reservation):
        comments = []
        with (
            patch.object(intake, "parse_result_comment", return_value=self.parsed()),
            patch.object(intake, "load_dispatch", return_value=(intake.NS_PROFILE, self.dispatch())),
            patch.object(intake, "validate_dispatch_issue", return_value=None),
            patch.object(intake, "queue_job_for_dispatch", return_value={"self_claimable": True, "collaboration_mode": "STAGED_DISCLOSURE", "visibility_phase": "BLIND_COLLECTION", "sibling_use_policy": "FORBIDDEN"}),
            patch.object(intake, "active_reservation", return_value=reservation),
        ):
            return intake.validate_event(self.event(actor), intake.ROOT, comments)

    def test_queue_result_requires_active_reservation(self):
        with self.assertRaisesRegex(intake.IntakeError, "no active worker reservation"):
            self.run_validate("alice", None)

    def test_queue_result_requires_reservation_owner(self):
        with self.assertRaisesRegex(intake.IntakeError, "does not match active worker reservation"):
            self.run_validate("bob", {"worker": "alice"})

    def test_queue_result_accepts_reservation_owner(self):
        _, _, _, observed = self.run_validate("alice", {"worker": "alice"})
        self.assertEqual(observed["worker_reservation"]["worker"], "alice")
        self.assertTrue(observed["queue_job"]["self_claimable"])


if __name__ == "__main__":
    unittest.main()
