"""Offline negative and contract tests for the bounded Project #2 population."""
from __future__ import annotations

import unittest
from unittest.mock import patch

from ci import activate_math_typography_editorial_queue as activation


class ActivationTests(unittest.TestCase):
    def test_fixed_campaign_and_state_partition(self):
        self.assertEqual(sorted(activation.ROLE_BY_ISSUE), list(range(1256, 1265)))
        self.assertEqual(
            [n for n, x in activation.ROLE_BY_ISSUE.items() if x[2] == "AVAILABLE"],
            list(range(1256, 1263)),
        )
        self.assertEqual(
            [n for n, x in activation.ROLE_BY_ISSUE.items() if x[2] == "BLOCKED"],
            [1263, 1264],
        )
        self.assertEqual(
            activation.REPO, "grandchallenge/MATH-PROGRAMME")
        self.assertEqual(activation.PROJECT, 2)

    def test_exact_fields_per_job(self):
        for n, (role, _, state, phase) in activation.ROLE_BY_ISSUE.items():
            with self.subTest(issue=n):
                rows = activation.field_payload(n)["issue_field_values"]
                self.assertEqual(len(rows), 5)
                values = {row["field_id"]: row["value"] for row in rows}
                self.assertEqual(values[activation.FIELDS["GCL State"]], state)
                self.assertEqual(values[activation.FIELDS["GCL Role"]], role)
                self.assertEqual(values[activation.FIELDS["GCL Phase"]], phase)
                self.assertEqual(values[activation.FIELDS["GCL Campaign"]], activation.CAMPAIGN)
                self.assertEqual(values[activation.FIELDS["GCL Collaboration"]], "COOPERATIVE")

    def test_preflight_refuses_unknown_auth_or_unadmitted_mode(self):
        with patch.object(activation, "api", side_effect=[
            {"login": "unrelated"}, 
        ]):
            with self.assertRaises(RuntimeError):
                activation.verify_authority()
        with patch.object(activation, "api", side_effect=[
            {"login": "jimsteeg"},
            {"merged": False},
        ]):
            with self.assertRaises(RuntimeError):
                activation.verify_authority()

    def test_issue_with_missing_pickup_label_is_rejected(self):
        with patch.object(activation, "verify_authority"):
            with patch.object(activation, "project_items", return_value={}):
                def fake_issue(n):
                    return {"state": "open", "body": f"issues/{activation.PARENT}",
                            "labels": [{"name": "gcl-job"}]}
                with patch.object(activation, "issue", side_effect=fake_issue):
                    with self.assertRaises(RuntimeError):
                        activation.preflight()

    def test_readback_rejects_missing_project_item(self):
        with self.assertRaises(RuntimeError):
            activation.verify_one(1256, {})

    def test_blocked_job_cannot_be_labeled_available(self):
        with patch.object(activation, "issue", return_value={
            "labels": [{"name": "gcl-state:available"}],
        }):
            with self.assertRaises(RuntimeError):
                activation.verify_one(
                    1263, {activation.url(1263): {"status": "In Progress"}})

    def test_duplicate_project_identity_refused(self):
        with patch.object(activation, "gh", return_value='{"totalCount":2,"items":['
                          '{"content":{"url":"https://github.com/example/x"}},'
                          '{"content":{"url":"https://github.com/example/x"}}]}'):
            with self.assertRaises(RuntimeError):
                activation.project_items()


if __name__ == "__main__":
    unittest.main()
