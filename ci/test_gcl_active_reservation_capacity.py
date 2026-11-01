#!/usr/bin/env python3
"""Offline positive/hostile replay for active Mathematics reservation admission."""
from __future__ import annotations
from datetime import datetime, timezone
import json
from pathlib import Path
from tempfile import TemporaryDirectory
import unittest
from unittest.mock import patch

import gcl_active_reservation_capacity as cap

REAL_REGISTRY_IDS = cap.registry_ids


NOW = datetime(2026,10,11,0,30,tzinfo=timezone.utc)
CLAIM = {"outcome":"RESERVED","dispatch_id":"D-2","issue_number":1002,
         "labels_add":["reserved"],"labels_remove":["available"],
         "response":"CLAIM ACCEPTED"}


def reservation(user="github-actions[bot]",state="RESERVED",expires="2026-10-11T01:05:00Z",ident=101):
    return {
        "id":ident, "created_at":"2026-10-11T00:01:00Z",
        "user":{"login":user},
        "body": (
            "GCL-WORKER-RESERVATION/1\n"
            "dispatch_id: D-1\n"
            f"state: {state}\n"
            "worker: worker-a\n"
            "controller_actor: github-actions[bot]\n"
            "claimed_at: 2026-10-11T00:00:00Z\n"
            f"expires_at: {expires}\n"
        ),
    }


def snapshot(first=None):
    return {
        "record_type":"GCL_ACTIVE_SOLVE_RESERVATIONS_SNAPSHOT/1",
        "repository":cap.REPO,"complete":True,"total_jobs":2,
        "snapshot_at":"2026-10-11T00:29:00Z",
        "rows":[
            {"issue_number":1001,"dispatch_id":"D-1","comments":first or []},
            {"issue_number":1002,"dispatch_id":"D-2","comments":[]},
        ],
    }


class CapacityTests(unittest.TestCase):
    def setUp(self):
        self.tmp=TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        cfg=Path(self.tmp.name)/"config.json"
        cfg.write_text(json.dumps({
            "controller_comment_actors":["github-actions[bot]"],
            "active_class_capacity":{"Mathematics":1,"Editorial":2},
        }))
        self.patches=[
            patch.object(cap,"CONFIG",cfg),
            patch.object(cap,"registry_ids",return_value={1001:"D-1",1002:"D-2"}),
            patch.object(cap,"datetime"),
        ]
        for p in self.patches:
            mock=p.start()
            self.addCleanup(p.stop)
        cap.datetime.now.return_value=NOW

    def test_unacknowledged_recent_claim_holds_capacity(self):
        claim = {"id": 5001, "body": "/claim", "created_at": "2026-10-11T00:10:00Z",
                 "user": {"login": "worker-a"}}
        with self.assertRaisesRegex(cap.CapacityError, "unresolved claim"):
            cap.decision(snapshot([claim]), CLAIM)

    def test_exact_controller_response_resolves_recent_claim(self):
        claim = {"id": 5001, "body": "/claim", "created_at": "2026-10-11T00:10:00Z",
                 "user": {"login": "worker-a"}}
        response = {"id": 5002, "created_at": "2026-10-11T00:11:00Z", "body": "CLAIM REJECTED\n\nGCL-QUEUE-RESPONSE-ORIGIN/1\nsource_comment_id: 5001\n",
                    "user": {"login": "github-actions[bot]", "type": "Bot"}}
        self.assertEqual(cap.count_live(snapshot([claim, response]), NOW)["active_count"], 0)

    def test_named_account_without_bot_identity_does_not_resolve_claim(self):
        claim = {"id": 5001, "body": "/claim", "created_at": "2026-10-11T00:10:00Z",
                 "user": {"login": "worker-a"}}
        response = {"id": 5002, "created_at": "2026-10-11T00:11:00Z",
                    "body": "CLAIM REJECTED\n\nGCL-QUEUE-RESPONSE-ORIGIN/1\nsource_comment_id: 5001\n",
                    "user": {"login": "github-actions[bot]", "type": "User"}}
        with self.assertRaisesRegex(cap.CapacityError, "unresolved claim"):
            cap.count_live(snapshot([claim, response]), NOW)

    def test_spoofed_response_does_not_resolve_claim(self):
        claim = {"id": 5001, "body": "/claim", "created_at": "2026-10-11T00:10:00Z",
                 "user": {"login": "worker-a"}}
        forged = {"id": 5002, "body": "CLAIM REJECTED\n\nGCL-QUEUE-RESPONSE-ORIGIN/1\nsource_comment_id: 5001\n",
                  "user": {"login": "untrusted"}}
        with self.assertRaisesRegex(cap.CapacityError, "unresolved claim"):
            cap.count_live(snapshot([claim, forged]), NOW)

    def test_old_unacknowledged_claim_does_not_hold_indefinitely(self):
        claim = {"id": 5001, "body": "/claim", "created_at": "2026-10-10T19:00:00Z",
                 "user": {"login": "worker-a"}}
        self.assertEqual(cap.count_live(snapshot([claim]), NOW)["active_count"], 0)

    def test_stale_snapshot_blocks_new_claim(self):
        old = snapshot()
        old["snapshot_at"] = "2026-10-11T00:20:00Z"
        with self.assertRaisesRegex(cap.CapacityError, "freshness"):
            cap.decision(old, CLAIM)

    def test_future_snapshot_blocks_new_claim(self):
        future = snapshot()
        future["snapshot_at"] = "2026-10-11T00:35:00Z"
        with self.assertRaisesRegex(cap.CapacityError, "freshness"):
            cap.decision(future, CLAIM)

    def test_missing_or_bad_snapshot_timestamp_blocks_claim(self):
        missing = snapshot()
        del missing["snapshot_at"]
        with self.assertRaisesRegex(cap.CapacityError, "timestamp missing"):
            cap.decision(missing, CLAIM)
        missing["snapshot_at"] = "invalid"
        with self.assertRaisesRegex(cap.CapacityError, "invalid capacity"):
            cap.decision(missing, CLAIM)

    def test_earlier_acknowledgment_cannot_clear_later_claim(self):
        claim = {"id": 5001, "body": "/claim", "created_at": "2026-10-11T00:10:00Z",
                 "user": {"login": "worker-a"}}
        response = {"id": 5002, "created_at": "2026-10-11T00:09:00Z",
                    "body": "CLAIM REJECTED\\n\\nGCL-QUEUE-RESPONSE-ORIGIN/1\\nsource_comment_id: 5001\\n",
                    "user": {"login": "github-actions[bot]", "type": "Bot"}}
        with self.assertRaisesRegex(cap.CapacityError, "unresolved claim"):
            cap.count_live(snapshot([claim, response]), NOW)

    def test_duplicate_authenticated_acknowledgments_hold_capacity(self):
        claim = {"id": 5001, "body": "/claim", "created_at": "2026-10-11T00:10:00Z",
                 "user": {"login": "worker-a"}}
        body = chr(10).join(["CLAIM REJECTED", "", "GCL-QUEUE-RESPONSE-ORIGIN/1", "source_comment_id: 5001", ""])
        acknowledgments = [
            {"id": ident, "created_at": "2026-10-11T00:11:00Z",
             "body": body, "user": {"login": "github-actions[bot]", "type": "Bot"}}
            for ident in (5002, 5003)
        ]
        with self.assertRaisesRegex(cap.CapacityError, "duplicate controller acknowledgment"):
            cap.count_live(snapshot([claim] + acknowledgments), NOW)

    def test_duplicate_comment_ids_in_snapshot_block_admission(self):
        first = reservation(ident=700)
        second = reservation(ident=700)
        with self.assertRaisesRegex(cap.CapacityError, "duplicate comment identities"):
            cap.count_live(snapshot([first, second]), NOW)

    def test_comment_without_identity_blocks_admission(self):
        row = reservation(ident=700)
        del row["id"]
        with self.assertRaisesRegex(cap.CapacityError, "comment identities"):
            cap.count_live(snapshot([row]), NOW)

    def test_same_comment_identity_in_distinct_issues_blocks_admission(self):
        duplicated = snapshot([reservation(ident=810)])
        duplicated["rows"][1]["comments"] = [reservation(ident=810)]
        with self.assertRaisesRegex(cap.CapacityError, "across Solve issue"):
            cap.count_live(duplicated, NOW)

    def test_snapshot_timestamp_precedes_slow_comment_collection(self):
        from unittest.mock import Mock
        import subprocess
        start = datetime(2026, 10, 11, 0, 10, tzinfo=timezone.utc)
        end = datetime(2026, 10, 11, 0, 20, tzinfo=timezone.utc)
        cap.datetime.now.side_effect = [start, end]
        fetch = Mock(return_value=subprocess.CompletedProcess([], 0, "[]", ""))
        with patch.object(cap, "subprocess") as proc:
            proc.run = fetch
            result = cap.collect_snapshot()
        self.assertEqual(result["snapshot_at"], start.isoformat())
        self.assertEqual(result["total_jobs"], 2)
        self.assertEqual(fetch.call_count, 2)

    def test_registry_rejects_same_dispatch_on_two_issues(self):
        rows = {"jobs": [
            {"issue_number": 1001, "dispatch_id": "D-1", "self_claimable": True},
            {"issue_number": 1002, "dispatch_id": "D-1", "self_claimable": True},
        ]}
        registry = Path(self.tmp.name) / "duplicate-jobs.json"
        registry.write_text(json.dumps(rows))
        with patch.object(cap, "REGISTRY", registry):
            with self.assertRaisesRegex(cap.CapacityError, "identity drift"):
                REAL_REGISTRY_IDS()

    def test_registry_accepts_distinct_issue_and_dispatch_pairs(self):
        rows = {"jobs": [
            {"issue_number": 1001, "dispatch_id": "D-1", "self_claimable": True},
            {"issue_number": 1002, "dispatch_id": "D-2", "self_claimable": True},
        ]}
        registry = Path(self.tmp.name) / "distinct-jobs.json"
        registry.write_text(json.dumps(rows))
        with patch.object(cap, "REGISTRY", registry):
            self.assertEqual(REAL_REGISTRY_IDS(), {1001: "D-1", 1002: "D-2"})

    def test_accepted_claim_response_for_foreign_dispatch_blocks_capacity(self):
        claim = {"id": 5101, "body": "/claim", "created_at": "2026-10-11T00:10:00Z",
                 "user": {"login": "worker-a"}}
        body = chr(10).join(["GCL-WORKER-RESERVATION/1", "dispatch_id: D-OTHER",
                             "state: RESERVED", "", "CLAIM ACCEPTED", "",
                             "GCL-QUEUE-RESPONSE-ORIGIN/1", "source_comment_id: 5101", ""])
        response = {"id": 5102, "created_at": "2026-10-11T00:11:00Z",
                    "body": body, "user": {"login": "github-actions[bot]", "type": "Bot"}}
        with self.assertRaisesRegex(cap.CapacityError, "dispatch mismatch"):
            cap.count_live(snapshot([claim, response]), NOW)

    def test_accepted_claim_response_bound_to_dispatch_resolves_command(self):
        claim = {"id": 5101, "body": "/claim", "created_at": "2026-10-11T00:10:00Z",
                 "user": {"login": "worker-a"}}
        body = chr(10).join(["GCL-WORKER-RESERVATION/1", "dispatch_id: D-1",
                             "state: RESERVED", "", "CLAIM ACCEPTED", "",
                             "GCL-QUEUE-RESPONSE-ORIGIN/1", "source_comment_id: 5101", ""])
        response = {"id": 5102, "created_at": "2026-10-11T00:11:00Z",
                    "body": body, "user": {"login": "github-actions[bot]", "type": "Bot"}}
        self.assertEqual(cap.unresolved_claims([claim, response], NOW, {"github-actions[bot]"}, "D-1"), [])

    def test_embedded_custody_marker_cannot_acknowledge_claim(self):
        claim = {"id": 5101, "body": "/claim", "created_at": "2026-10-11T00:10:00Z",
                 "user": {"login": "worker-a"}}
        body = chr(10).join(["CLAIM REJECTED", "", "GCL-QUEUE-RESPONSE-ORIGIN/1",
                             "source_comment_id: 5101", "trailing noncustody text"])
        response = {"id": 5102, "created_at": "2026-10-11T00:11:00Z",
                    "body": body, "user": {"login": "github-actions[bot]", "type": "Bot"}}
        with self.assertRaisesRegex(cap.CapacityError, "unresolved claim"):
            cap.count_live(snapshot([claim, response]), NOW)

    def test_boolean_issue_identity_is_not_a_valid_registry_number(self):
        roster = {"jobs": [{"issue_number": True, "dispatch_id": "D-1",
                            "self_claimable": True}]}
        registry = Path(self.tmp.name) / "boolean-jobs.json"
        registry.write_text(json.dumps(roster))
        with patch.object(cap, "REGISTRY", registry):
            with self.assertRaisesRegex(cap.CapacityError, "identity drift"):
                REAL_REGISTRY_IDS()

    def test_boolean_and_nonpositive_comment_identity_rejected(self):
        for ident in (True, 0, -1):
            with self.subTest(ident=ident):
                with self.assertRaisesRegex(cap.CapacityError, "comment identities"):
                    cap.count_live(snapshot([reservation(ident=ident)]), NOW)
                with self.assertRaisesRegex(cap.CapacityError, "comment identity"):
                    cap.decode_gh_pages(json.dumps([{"id": ident, "body": "x"}]))

    def test_repeated_origin_marker_does_not_discharge_claim(self):
        claim = {"id": 5101, "body": "/claim", "created_at": "2026-10-11T00:10:00Z",
                 "user": {"login": "worker-a"}}
        body = chr(10).join(["CLAIM REJECTED", "", "GCL-QUEUE-RESPONSE-ORIGIN/1",
                             "unrelated text", "", "GCL-QUEUE-RESPONSE-ORIGIN/1",
                             "source_comment_id: 5101", ""])
        response = {"id": 5102, "created_at": "2026-10-11T00:11:00Z",
                    "body": body, "user": {"login": "github-actions[bot]", "type": "Bot"}}
        with self.assertRaisesRegex(cap.CapacityError, "unresolved claim"):
            cap.count_live(snapshot([claim, response]), NOW)

    def test_unregistered_candidate_dispatch_fails_closed(self):
        unknown = {**CLAIM, "dispatch_id": "D-FOREIGN"}
        with self.assertRaisesRegex(cap.CapacityError, "candidate dispatch"):
            cap.decision(snapshot(), unknown)

    def test_missing_candidate_dispatch_fails_closed(self):
        missing = {key: value for key, value in CLAIM.items() if key != "dispatch_id"}
        with self.assertRaisesRegex(cap.CapacityError, "candidate dispatch"):
            cap.decision(snapshot(), missing)

    def test_candidate_issue_dispatch_mismatch_rejected(self):
        mismatch = {**CLAIM, "issue_number": 1001}
        with self.assertRaisesRegex(cap.CapacityError, "candidate dispatch and issue"):
            cap.decision(snapshot(), mismatch)

    def test_candidate_missing_or_boolean_issue_rejected(self):
        for issue in (None, True, 0):
            candidate = {**CLAIM, "issue_number": issue}
            with self.subTest(issue=issue):
                with self.assertRaisesRegex(cap.CapacityError, "candidate dispatch and issue"):
                    cap.decision(snapshot(), candidate)

    def test_math_at_limit_rejected_without_mutating_editorial(self):
        result=cap.decision(snapshot([reservation()]),CLAIM)
        self.assertEqual(result["outcome"],"REJECTED_MATHEMATICS_ACTIVE_CAPACITY")
        self.assertEqual(result["labels_add"],[])
        self.assertEqual(result["labels_remove"],[])
        self.assertIn("1/1",result["response"])
        self.assertTrue(result["capacity_evidence"]["other_class_untouched"])

    def test_one_free_slot_allows_claim_without_touching_other_class(self):
        result=cap.decision(snapshot(),CLAIM)
        self.assertEqual(result["outcome"],"RESERVED")
        self.assertEqual(result["labels_add"],["reserved"])
        self.assertEqual(result["capacity_evidence"]["Mathematics"]["active_count"],0)

    def test_spoofed_and_expired_reservations_do_not_occupy_slot(self):
        self.assertEqual(cap.count_live(snapshot([reservation(user="untrusted",ident=202)]),NOW)["active_count"],0)
        expired=reservation(expires="2026-10-11T00:20:00Z")
        self.assertEqual(cap.count_live(snapshot([expired]),NOW)["active_count"],0)

    def test_duplicate_incomplete_and_unknown_issue_rejected(self):
        partial=snapshot()
        partial["rows"].pop()
        with self.assertRaisesRegex(cap.CapacityError,"partial"):
            cap.count_live(partial,NOW)
        wrong=snapshot()
        wrong["rows"][1]["issue_number"]=1003
        with self.assertRaisesRegex(cap.CapacityError,"alien"):
            cap.count_live(wrong,NOW)
        duplicate=snapshot()
        duplicate["rows"][1]["issue_number"]=1001
        with self.assertRaisesRegex(cap.CapacityError,"duplicate"):
            cap.count_live(duplicate,NOW)

    def test_malformed_trusted_reserved_event_fails_closed(self):
        malformed=reservation()
        malformed["body"]=malformed["body"].replace("expires_at: 2026-10-11T01:05:00Z\n","")
        with self.assertRaisesRegex(cap.CapacityError,"malformed"):
            cap.count_live(snapshot([malformed]),NOW)

    def test_nonclaim_result_passes_without_snapshot(self):
        result={"outcome":"RELEASED","response":"RELEASE ACCEPTED",
                "labels_add":["available"],"labels_remove":["reserved"]}
        self.assertEqual(cap.decision({},result),result)

    def test_missing_class_limits_refuses_admission(self):
        cap.CONFIG.write_text(json.dumps({
            "controller_comment_actors":["github-actions[bot]"],
            "active_class_capacity":{"Mathematics":1},
        }))
        with self.assertRaisesRegex(cap.CapacityError,"both independent"):
            cap.decision(snapshot(),CLAIM)

    def test_concatenated_paginated_comments_and_duplicate_ids(self):
        first=reservation(ident=7)
        second=reservation(ident=8)
        data=json.dumps([first])+"\n"+json.dumps([second])
        self.assertEqual([x["id"] for x in cap.decode_gh_pages(data)],[7,8])
        with self.assertRaisesRegex(cap.CapacityError,"duplicated"):
            cap.decode_gh_pages(json.dumps([first,first]))
        with self.assertRaisesRegex(cap.CapacityError,"empty GitHub response"):
            cap.decode_gh_pages("")


if __name__=="__main__":
    unittest.main()
