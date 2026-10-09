from __future__ import annotations

import json
import tempfile
import unittest
from datetime import datetime, timedelta, timezone
from pathlib import Path
from unittest.mock import patch

import ci.gcl_worker_queue_projection as proj


class WorkerQueueProjectionTest(unittest.TestCase):
    def setup_root(self, root: Path):
        (root / ".gcl/worker_queue").mkdir(parents=True)
        (root / "dispatches").mkdir(parents=True)

        (root / ".gcl/worker_queue/PROJECT.json").write_text(json.dumps({
            "issue_fields": {
                "state": {"rest_id": 1},
                "worker": {"rest_id": 2},
                "reservation_expires": {"rest_id": 3},
                "campaign": {"rest_id": 4},
                "role": {"rest_id": 5},
                "collaboration": {"rest_id": 6},
                "phase": {"rest_id": 7},
                "cohort": {"rest_id": 8},
                "timebox": {"rest_id": 9},
            }
        }), encoding="utf-8")

        (root / "dispatches/D-1.json").write_text(json.dumps({
            "dispatch_id": "D-1",
            "campaign": "ERDOS-OPEN",
        }), encoding="utf-8")

        (root / ".gcl/worker_queue/JOBS.json").write_text(json.dumps({
            "jobs": [{
                "dispatch_id": "D-1",
                "issue_number": 7,
                "role": "RECONNAISSANCE",
                "collaboration_mode": "STAGED_DISCLOSURE",
                "visibility_phase": "BLIND_COLLECTION",
                "cohort_id": "C-1",
                "dispatch_path": "dispatches/D-1.json",
                "timebox_minutes": 35,
            }]
        }), encoding="utf-8")

        (root / ".gcl/worker_queue/CONFIG.json").write_text(json.dumps({
            "controller_comment_actors": ["github-actions[bot]"],
            "project_metadata_projection": {
                "campaign_aliases": {"ERDOS-OPEN": "ERDOS-OPEN-RECON"},
                "role": {"RECONNAISSANCE": "RECON"},
                "collaboration": {"STAGED_DISCLOSURE": "STAGED"},
                "phase": {"BLIND_COLLECTION": "INDEPENDENT"},
            },
        }), encoding="utf-8")

    def run_projection(self, root: Path, *args, **kwargs):
        with (
            patch.object(proj, "ROOT", root),
            patch.object(proj, "PROJECT", root / ".gcl/worker_queue/PROJECT.json"),
            patch.object(proj, "JOBS", root / ".gcl/worker_queue/JOBS.json"),
            patch.object(proj, "CONFIG", root / ".gcl/worker_queue/CONFIG.json"),
        ):
            return proj.projection(*args, **kwargs)

    def metadata(self):
        return [
            {"field_id": 4, "value": "ERDOS-OPEN-RECON"},
            {"field_id": 5, "value": "RECON"},
            {"field_id": 6, "value": "STAGED"},
            {"field_id": 7, "value": "INDEPENDENT"},
            {"field_id": 8, "value": "C-1"},
            {"field_id": 9, "value": 35},
        ]

    def test_claim_sets_metadata_reserved_worker_and_expiry(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            self.setup_root(root)
            out = self.run_projection(root, "command", result={
                "dispatch_id": "D-1",
                "outcome": "RESERVED",
                "worker": "alice",
                "expires_at": "2026-10-05T10:00:00Z",
            })
            self.assertEqual(out["issue_field_values"], self.metadata() + [
                {"field_id": 1, "value": "RESERVED"},
                {"field_id": 2, "value": "alice"},
                {"field_id": 3, "value": "2026-10-05T10:00:00Z"},
            ])
            self.assertEqual(out["clear_field_ids"], [])

    def test_release_clears_reservation_and_keeps_metadata(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            self.setup_root(root)
            out = self.run_projection(root, "command", result={
                "dispatch_id": "D-1", "outcome": "RELEASED", "worker": "alice",
            })
            self.assertEqual(
                out["issue_field_values"],
                self.metadata() + [{"field_id": 1, "value": "AVAILABLE"}],
            )
            self.assertEqual(out["clear_field_ids"], [2, 3])

    def test_command_pending_result_marks_blocked(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            self.setup_root(root)
            out = self.run_projection(root, "command", result={
                "dispatch_id": "D-1",
                "outcome": "REJECTED_RESULT_COMMENT_PRESENT",
            })
            self.assertEqual(
                out["issue_field_values"],
                self.metadata() + [{"field_id": 1, "value": "BLOCKED"}],
            )
            self.assertEqual(out["clear_field_ids"], [3])

    def test_intake_marks_returned_and_keeps_worker(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            self.setup_root(root)
            out = self.run_projection(root, "intake", dispatch_id="D-1")
            self.assertEqual(
                out["issue_field_values"],
                self.metadata() + [{"field_id": 1, "value": "RETURNED"}],
            )
            self.assertEqual(out["clear_field_ids"], [3])

    def test_non_queue_dispatch_is_noop(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            self.setup_root(root)
            out = self.run_projection(root, "intake", dispatch_id="OTHER")
            self.assertFalse(out["queue_managed"])
            self.assertEqual(out["issue_field_values"], [])

    def test_missing_metadata_mapping_fails_closed(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            self.setup_root(root)
            cfg = json.loads((root / ".gcl/worker_queue/CONFIG.json").read_text())
            del cfg["project_metadata_projection"]["role"]["RECONNAISSANCE"]
            (root / ".gcl/worker_queue/CONFIG.json").write_text(json.dumps(cfg))
            with self.assertRaises(ValueError):
                self.run_projection(root, "intake", dispatch_id="D-1")

    def test_reconcile_pending_result_marks_blocked(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            self.setup_root(root)
            comments = [{
                "id": 2,
                "created_at": "2026-10-05T09:01:00Z",
                "user": {"login": "alice"},
                "body": "GCL-CONTRIBUTION-RESULT/1\ndispatch_id: D-1\n",
            }]
            out = self.run_projection(
                root, "reconcile", issue_number=7, comments=comments,
                now=datetime(2026, 10, 5, 10, 0, tzinfo=timezone.utc),
            )
            self.assertEqual(out["reservation_state"], "RESULT_PENDING")
            self.assertEqual(
                out["issue_field_values"],
                self.metadata() + [{"field_id": 1, "value": "BLOCKED"}],
            )
            self.assertEqual(out["clear_field_ids"], [3])

    def test_reconcile_trusted_rejection_reopens_available(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            self.setup_root(root)
            comments = [
                {
                    "id": 2,
                    "created_at": "2026-10-05T09:01:00Z",
                    "user": {"login": "alice"},
                    "body": "GCL-CONTRIBUTION-RESULT/1\ndispatch_id: D-1\n",
                },
                {
                    "id": 3,
                    "created_at": "2026-10-05T09:02:00Z",
                    "user": {"login": "github-actions[bot]"},
                    "body": "INTAKE REJECTED — FORMAT\n\nreplacement required",
                },
            ]
            out = self.run_projection(
                root, "reconcile", issue_number=7, comments=comments,
                now=datetime(2026, 10, 5, 10, 0, tzinfo=timezone.utc),
            )
            self.assertEqual(out["reservation_state"], "RESULT_REJECTED")
            self.assertEqual(
                out["issue_field_values"],
                self.metadata() + [{"field_id": 1, "value": "AVAILABLE"}],
            )
            self.assertEqual(out["clear_field_ids"], [2, 3])

    def test_reconcile_captured_result_marks_returned(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            self.setup_root(root)
            comments = [
                {
                    "id": 2,
                    "created_at": "2026-10-05T09:01:00Z",
                    "user": {"login": "alice"},
                    "body": "GCL-CONTRIBUTION-RESULT/1\ndispatch_id: D-1\n",
                },
                {
                    "id": 3,
                    "created_at": "2026-10-05T09:02:00Z",
                    "user": {"login": "github-actions[bot]"},
                    "body": "INTAKE CAPTURED — raw evidence and receipt were committed.",
                },
            ]
            out = self.run_projection(
                root, "reconcile", issue_number=7, comments=comments,
                now=datetime(2026, 10, 5, 10, 0, tzinfo=timezone.utc),
            )
            self.assertEqual(out["reservation_state"], "RETURNED")
            self.assertEqual(
                out["issue_field_values"],
                self.metadata() + [{"field_id": 1, "value": "RETURNED"}],
            )
            self.assertEqual(out["clear_field_ids"], [3])

    def test_reconcile_active_and_expired(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            self.setup_root(root)
            now = datetime(2026, 10, 5, 9, 0, tzinfo=timezone.utc)
            body = "\n".join([
                "GCL-WORKER-RESERVATION/1",
                "dispatch_id: D-1",
                "state: RESERVED",
                "worker: alice",
                "controller_actor: github-actions[bot]",
                "claimed_at: 2026-10-05T08:00:00Z",
                "expires_at: 2026-10-05T09:30:00Z",
            ])
            comments = [{
                "id": 1,
                "created_at": "2026-10-05T08:00:01Z",
                "user": {"login": "github-actions[bot]"},
                "body": body,
            }]
            active = self.run_projection(
                root, "reconcile", issue_number=7, comments=comments, now=now
            )
            self.assertEqual(active["reservation_state"], "ACTIVE")
            self.assertEqual(
                active["issue_field_values"],
                self.metadata() + [
                    {"field_id": 1, "value": "RESERVED"},
                    {"field_id": 2, "value": "alice"},
                    {"field_id": 3, "value": "2026-10-05T09:30:00Z"},
                ],
            )

            expired = self.run_projection(
                root, "reconcile", issue_number=7, comments=comments,
                now=now + timedelta(hours=1),
            )
            self.assertEqual(expired["reservation_state"], "EXPIRED")
            self.assertEqual(
                expired["issue_field_values"],
                self.metadata() + [{"field_id": 1, "value": "AVAILABLE"}],
            )
            self.assertEqual(expired["clear_field_ids"], [2, 3])


if __name__ == "__main__":
    unittest.main()
