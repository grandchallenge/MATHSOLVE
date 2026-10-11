#!/usr/bin/env python3
"""Bounded, no-network tests for typography queue activation preconditions."""
import json
import sys
import unittest
from unittest.mock import patch

import reconcile_math_typography_editorial_queue as q


class ReconcileTest(unittest.TestCase):
    def test_fixed_scope(self):
        self.assertEqual(list(q.PRS), list(range(1256, 1263)))
        self.assertEqual(q.EXPECTED, {
            1256: "RETURNED", 1257: "RETURNED", 1258: "RETURNED",
            1259: "RETURNED", 1260: "RETURNED", 1261: "RETURNED",
            1262: "RETURNED", 1263: "AVAILABLE",
        })
        self.assertNotIn(q.ARCHIVE, q.EXPECTED)

    @patch.object(q, "gh")
    def test_project_snapshot_rejects_partial_inventory(self, runner):
        runner.return_value = json.dumps({
            "totalCount": 1294, "items": [
                {"id": "a", "content": {"url": "https://github.com/example/issues/1"}}
            ],
        })
        with self.assertRaisesRegex(RuntimeError, "incomplete Project"):
            q.project_items()

    @patch.object(q, "gh")
    def test_project_snapshot_rejects_duplicate_identity(self, runner):
        runner.return_value = json.dumps({"totalCount": 9, "items": [
            {"id": str(i), "content": {"url": "https://github.com/x/issues/1"}}
            for i in range(9)
        ]})
        with self.assertRaisesRegex(RuntimeError, "duplicate Project URL"):
            q.project_items()

    @patch.object(q, "field_values")
    @patch.object(q, "issue")
    def test_readback_rejects_stale_available(self, issue, fields):
        fields.return_value = {"GCL State": "RETURNED"}
        issue.return_value = {"labels": [
            {"name": "gcl-state:returned"}, {"name": "gcl-state:available"}]}
        with self.assertRaisesRegex(RuntimeError, "stale AVAILABLE"):
            q.verify(1256, {"status": "Done", "queueClass": "Editorial"}, "RETURNED")

    @patch.object(q, "field_values")
    @patch.object(q, "issue")
    def test_readback_accepts_returned_editor(self, issue, fields):
        fields.return_value = {"GCL State": "RETURNED"}
        issue.return_value = {"labels": [{"name": "gcl-state:returned"}]}
        q.verify(1256, {"status": "Done", "queueClass": "Editorial"}, "RETURNED")

    @patch.object(q, "preflight", side_effect=RuntimeError("unmerged prerequisite"))
    def test_no_project_writes_when_protected_preflight_fails(self, preflight):
        with patch.object(sys, "argv", ["controller", "--apply"]), \
             patch.object(q, "project_edit") as mutate, \
             self.assertRaisesRegex(RuntimeError, "unmerged prerequisite"):
            q.main()
            mutate.assert_not_called()

    @patch.object(q, "project_items")
    @patch.object(q, "project_fields", return_value=("classfield", "editorialoption"))
    @patch.object(q, "preflight", return_value="protectedsha")
    def test_readonly_dry_run_has_no_mutations(self, _, __, items):
        items.return_value = {
            f"https://github.com/{q.REPO}/issues/{n}": {"id": str(n)}
            for n in [*q.PRS, q.SUCCESSOR, q.ARCHIVE]
        }
        with patch.object(sys, "argv", ["controller"]), \
             patch.object(q, "project_edit") as mutate:
            q.main()
            mutate.assert_not_called()


if __name__ == "__main__":
    unittest.main()
