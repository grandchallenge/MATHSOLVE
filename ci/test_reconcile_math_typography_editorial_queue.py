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

    @patch.object(q, "gh")
    @patch.object(q, "issue")
    def test_create_returned_label_before_taking_available_off(self, issue, runner):
        issue.return_value = {"labels": [{"name": "gcl-state:available"}]}
        runner.side_effect = [json.dumps([{"name": "gcl-state:available"}]), "", "", ""]
        q.set_label(1256, "gcl-state:available", "gcl-state:returned")
        commands = [call.args for call in runner.call_args_list]
        self.assertEqual(commands[1][:3], ("label", "create", "gcl-state:returned"))
        self.assertEqual(commands[2][:3], ("issue", "edit", "1256"))
        self.assertIn("--add-label", commands[2])
        self.assertIn("--remove-label", commands[3])

    @patch.object(q, "gh")
    @patch.object(q, "issue")
    def test_existing_returned_label_is_reused(self, issue, runner):
        issue.return_value = {"labels": [{"name": "gcl-state:available"}]}
        runner.side_effect = [json.dumps([{"name": "gcl-state:returned"}]), "", ""]
        q.set_label(1256, "gcl-state:available", "gcl-state:returned")
        self.assertEqual(runner.call_count, 3)
        self.assertFalse(any(call.args[:2] == ("label", "create")
                             for call in runner.call_args_list))

    @patch.object(q, "gh")
    def test_wrong_role_transition_rejected_without_mutation(self, runner):
        with self.assertRaisesRegex(RuntimeError, "unapproved"):
            q.set_label(1256, "gcl-state:blocked", "gcl-state:returned")
        runner.assert_not_called()

    @patch.object(q, "gh")
    def test_status_option_ids_come_from_live_project(self, runner):
        runner.return_value = json.dumps({"fields": [
            {"name": "Status", "id": q.STATUS_FIELD["field_id"], "options": [
                {"name": "Todo", "id": "live-todo-new"}, {"name": "Done", "id": "live-done-new"}]},
            {"name": "Queue Class", "id": "PVTSSF_lADOB9Ao_c4BlwurzhlJkjI", "options": [
                {"name": "Editorial", "id": "editorial-option"}]}
        ]})
        cl, editorial, status, opts = q.project_fields()
        self.assertEqual(cl, "PVTSSF_lADOB9Ao_c4BlwurzhlJkjI")
        self.assertEqual(editorial, "editorial-option")
        self.assertEqual(status, q.STATUS_FIELD["field_id"])
        self.assertEqual(opts["Done"], "live-done-new")

    @patch.object(q, "gh")
    def test_missing_live_done_option_blocks_before_mutation(self, runner):
        runner.return_value = json.dumps({"fields": [
            {"name": "Status", "id": q.STATUS_FIELD["field_id"], "options": [
                {"name": "Todo", "id": "live-todo"}]},
            {"name": "Queue Class", "id": "PVTSSF_lADOB9Ao_c4BlwurzhlJkjI", "options": [
                {"name": "Editorial", "id": "editorial-option"}]}
        ]})
        with self.assertRaisesRegex(RuntimeError, "live Project Status options"):
            q.project_fields()

    @patch.object(q, "api")
    def test_scoped_project_readback_checks_exact_item_identity(self, api):
        url = f"https://github.com/{q.REPO}/issues/1256"
        api.return_value = {"data": {"nodes": [{
            "id": "I-1256", "content": {"number": 1256,
                   "repository": {"nameWithOwner": q.REPO}},
            "projectStatus": {"name": "Done"},
            "projectClass": {"name": "Editorial"}
        }]}}
        out = q.selected_project_items({url: {"id": "I-1256"}}, [1256])
        self.assertEqual(out[url]["status"], "Done")
        self.assertEqual(out[url]["queueClass"], "Editorial")
        self.assertEqual(api.call_args.args, ("graphql",))
        self.assertEqual(api.call_args.kwargs["payload"]["variables"]["ids"], ["I-1256"])

    @patch.object(q, "api")
    def test_scoped_project_readback_rejects_wrong_issue(self, api):
        url = f"https://github.com/{q.REPO}/issues/1256"
        api.return_value = {"data": {"nodes": [{
            "id": "I-1256", "content": {"number": 999,
                   "repository": {"nameWithOwner": q.REPO}},
            "projectStatus": {"name": "Done"},
            "projectClass": {"name": "Editorial"}
        }]}}
        with self.assertRaisesRegex(RuntimeError, "identity drift"):
            q.selected_project_items({url: {"id": "I-1256"}}, [1256])

    @patch.object(q, "preflight", side_effect=RuntimeError("unmerged prerequisite"))
    def test_no_project_writes_when_protected_preflight_fails(self, preflight):
        with patch.object(sys, "argv", ["controller", "--apply"]), \
             patch.object(q, "project_edit") as mutate:
            with self.assertRaisesRegex(RuntimeError, "unmerged prerequisite"):
                q.main()
            mutate.assert_not_called()

    @patch.object(q, "project_items")
    @patch.object(q, "project_fields", return_value=("classfield", "editorialoption", "statusfield", {"Todo": "live-todo", "Done": "live-done"}))
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
