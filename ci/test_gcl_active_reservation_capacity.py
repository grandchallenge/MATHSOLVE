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


NOW = datetime(2026,10,11,0,30,tzinfo=timezone.utc)
CLAIM = {"outcome":"RESERVED","dispatch_id":"D-2",
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
