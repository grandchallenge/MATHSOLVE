"""Fail-closed, offline board projection tests. No GH network or auth required."""
import unittest
from ci.gcl_worker_queue_project_status import expected_status, validated_item

REPO = "grandchallenge/ADAPTIVE-INTELLIGENCE-ATLAS"


def example(state="RETURNED", labels=None, issue=335):
    return (
        {
            "id": f"PVTI_item_{issue}",
            "content": {
                "repository": REPO,
                "number": issue,
                "url": f"https://github.com/{REPO}/issues/{issue}",
            },
            "status": "Todo",
            "labels": labels if labels is not None else [f"gcl-state:{state.lower()}", "gcl-job"],
        },
        [{"issue_field_name": "GCL State", "single_select_option": {"name": state}}],
    )


class WorkerProjectStatusTests(unittest.TestCase):
    def test_state_mapping_is_assignment_only(self):
        self.assertEqual(expected_status("AVAILABLE"), "Todo")
        self.assertEqual(expected_status("RETURNED"), "Done")
        self.assertEqual(expected_status("CLOSED"), "Done")
        self.assertEqual(expected_status("RESERVED"), "In Progress")
        self.assertEqual(expected_status("BLOCKED"), "In Progress")

    def test_returned_does_not_claim_editorial_acceptance(self):
        item, fields = example()
        result = validated_item(item, fields)
        self.assertEqual(result["to_status"], "Done")
        self.assertEqual(result["state"], "RETURNED")
        self.assertNotIn("editorially_accepted", result)
        self.assertNotIn("certification", result)

    def test_missing_or_duplicate_state_rejected(self):
        item, fields = example()
        with self.assertRaises(ValueError):
            validated_item(item, [])
        with self.assertRaises(ValueError):
            validated_item(item, fields + fields)

    def test_label_field_disagreement_rejected(self):
        item, fields = example("AVAILABLE", ["gcl-job", "gcl-state:returned"])
        with self.assertRaises(ValueError):
            validated_item(item, fields)
        item, fields = example("RETURNED", ["gcl-job", "gcl-state:available"])
        with self.assertRaises(ValueError):
            validated_item(item, fields)

    def test_unbound_url_and_unknown_repo_rejected(self):
        item, fields = example()
        item["content"]["url"] = "https://github.com/another/issue/issues/1"
        with self.assertRaises(ValueError):
            validated_item(item, fields)
        item, fields = example()
        item["content"]["repository"] = "untrusted/external"
        with self.assertRaises(ValueError):
            validated_item(item, fields)

    def test_blocked_state_without_label_is_not_available(self):
        item, fields = example("BLOCKED", ["gcl-job"])
        result = validated_item(item, fields)
        self.assertEqual(result["to_status"], "In Progress")

    def test_available_is_pickup_not_execution_permission(self):
        item, fields = example("AVAILABLE")
        result = validated_item(item, fields)
        self.assertEqual(result["to_status"], "Todo")
        self.assertEqual(result["state"], "AVAILABLE")


if __name__ == "__main__":
    unittest.main()
