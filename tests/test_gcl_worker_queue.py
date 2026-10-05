from __future__ import annotations

import json
import tempfile
import unittest
from datetime import datetime, timedelta, timezone
from pathlib import Path
from unittest.mock import patch

import ci.gcl_worker_queue as queue
from ci.gcl_worker_queue_contract import active_reservation


def marker(dispatch: str, worker: str, claimed: datetime, expires: datetime, state: str = "RESERVED") -> str:
    return "\n".join([
        "GCL-WORKER-RESERVATION/1",
        f"dispatch_id: {dispatch}",
        f"state: {state}",
        f"worker: {worker}",
        "controller_actor: github-actions[bot]",
        f"claimed_at: {claimed.isoformat().replace('+00:00','Z')}",
        f"expires_at: {expires.isoformat().replace('+00:00','Z')}",
        "reservation_is_execution_authority: NO",
        "mathematical_effect: NO",
        "certification_effect: NO",
    ])


class WorkerQueueTest(unittest.TestCase):
    def test_active_and_expired_reservation(self):
        now = datetime(2026, 10, 5, tzinfo=timezone.utc)
        comments = [{
            "id": 1,
            "created_at": "2026-10-05T00:00:00Z",
            "user": {"login": "github-actions[bot]"},
            "body": marker("D-1", "alice", now - timedelta(minutes=1), now + timedelta(minutes=10)),
        }]
        self.assertEqual(active_reservation(comments, "D-1", now, {"github-actions[bot]"})["worker"], "alice")
        self.assertIsNone(active_reservation(comments, "D-1", now + timedelta(minutes=11), {"github-actions[bot]"}))

    def make_repo(self, root: Path) -> dict:
        (root / ".gcl/worker_queue").mkdir(parents=True)
        (root / "dispatches").mkdir()
        (root / "tasks").mkdir()
        config = {
            "operators": ["operator"],
            "controller_comment_actors": ["github-actions[bot]"],
            "labels": {"available": "a", "reserved": "r", "returned": "x"},
        }
        registry = {"jobs": [{
            "dispatch_id": "D-1",
            "issue_number": 7,
            "role": "RECONNAISSANCE",
            "self_claimable": True,
            "reservation_ttl_minutes": 65,
            "collaboration_mode": "STAGED_DISCLOSURE",
            "visibility_phase": "BLIND_COLLECTION",
            "sibling_use_policy": "FORBIDDEN",
            "cohort_id": "C-1",
            "dispatch_path": "dispatches/D-1.json",
            "task_commit": "1" * 40,
        }]}
        dispatch = {
            "dispatch_id": "D-1",
            "github_issue_number": 7,
            "github_issue_title": "job",
            "dispatch_status": "READY_FOR_GITHUB_COMMENT",
            "protected_lease_required": True,
            "lease_state": "ACTIVE",
            "canonical_mutation_authorized": False,
            "certification_authorized": False,
            "task_path": "tasks/D-1.md",
        }
        (root / ".gcl/worker_queue/CONFIG.json").write_text(json.dumps(config), encoding="utf-8")
        (root / ".gcl/worker_queue/JOBS.json").write_text(json.dumps(registry), encoding="utf-8")
        (root / "dispatches/D-1.json").write_text(json.dumps(dispatch), encoding="utf-8")
        (root / "tasks/D-1.md").write_text("task", encoding="utf-8")
        return {
            "issue": {"number": 7, "title": "job"},
            "comment": {"body": "/claim", "user": {"login": "alice"}},
        }

    def run_process(self, root: Path, event: dict, comments: list[dict], now: datetime):
        with (
            patch.object(queue, "ROOT", root),
            patch.object(queue, "CONFIG", root / ".gcl/worker_queue/CONFIG.json"),
            patch.object(queue, "REGISTRY", root / ".gcl/worker_queue/JOBS.json"),
        ):
            return queue.process(event, comments, now)

    def test_claim_second_claim_expiry_and_release(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            event = self.make_repo(root)
            now = datetime(2026, 10, 5, tzinfo=timezone.utc)
            first = self.run_process(root, event, [], now)
            self.assertEqual(first["outcome"], "RESERVED")
            self.assertIn("sibling_use_policy: FORBIDDEN", first["response"])
            comment = {
                "id": 1,
                "created_at": now.isoformat(),
                "user": {"login": "github-actions[bot]"},
                "body": first["response"],
            }
            second = self.run_process(root, event, [comment], now + timedelta(minutes=1))
            self.assertEqual(second["outcome"], "REJECTED_ALREADY_RESERVED")
            expired = self.run_process(root, event, [comment], now + timedelta(minutes=66))
            self.assertEqual(expired["outcome"], "RESERVED")
            release_event = {
                "issue": {"number": 7, "title": "job"},
                "comment": {"body": "/release", "user": {"login": "alice"}},
            }
            release = self.run_process(root, release_event, [comment], now + timedelta(minutes=1))
            self.assertEqual(release["outcome"], "RELEASED")

    def test_non_owner_release_and_result_comment_block(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            event = self.make_repo(root)
            now = datetime(2026, 10, 5, tzinfo=timezone.utc)
            first = self.run_process(root, event, [], now)
            comment = {
                "id": 1,
                "created_at": now.isoformat(),
                "user": {"login": "github-actions[bot]"},
                "body": first["response"],
            }
            release_event = {
                "issue": {"number": 7, "title": "job"},
                "comment": {"body": "/release", "user": {"login": "bob"}},
            }
            release = self.run_process(root, release_event, [comment], now + timedelta(minutes=1))
            self.assertEqual(release["outcome"], "REJECTED_NOT_OWNER")
            result_comment = {
                "id": 2,
                "created_at": now.isoformat(),
                "user": {"login": "alice"},
                "body": "GCL-CONTRIBUTION-RESULT/1\ninvalid",
            }
            blocked = self.run_process(root, event, [result_comment], now)
            self.assertEqual(blocked["outcome"], "REJECTED_RESULT_COMMENT_PRESENT")

    def test_inactive_dispatch_fails_closed(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            event = self.make_repo(root)
            p = root / "dispatches/D-1.json"
            dispatch = json.loads(p.read_text(encoding="utf-8"))
            dispatch["lease_state"] = "EXPIRED"
            p.write_text(json.dumps(dispatch), encoding="utf-8")
            with self.assertRaises(queue.QueueError):
                self.run_process(root, event, [], datetime(2026, 10, 5, tzinfo=timezone.utc))


if __name__ == "__main__":
    unittest.main()
