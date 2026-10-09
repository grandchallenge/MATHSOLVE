"""Fail-closed offline tests for worker queue lifecycle and pickup routing."""
import unittest

from ci.gcl_worker_queue_project_status import (
    expected_pickup_mode,
    expected_status,
    validated_item,
)

ATLAS = "grandchallenge/ADAPTIVE-INTELLIGENCE-ATLAS"
CDA = "grandchallenge/COMPUTATIONAL-DIFFICULTY-ATLAS"
MATH = "grandchallenge/MATH-PROGRAMME"
SOLVE = "grandchallenge/MATHSOLVE"
DIRECT = "gcl-pickup:direct-editorial"


def fields(state="RETURNED", campaign="TEST", role="VERIFY", collaboration="COOPERATIVE", phase="SHARED"):
    return [
        {"issue_field_name": "GCL State", "single_select_option": {"name": state}},
        {"issue_field_name": "GCL Campaign", "value": campaign},
        {"issue_field_name": "GCL Role", "single_select_option": {"name": role}},
        {"issue_field_name": "GCL Collaboration", "single_select_option": {"name": collaboration}},
        {"issue_field_name": "GCL Phase", "single_select_option": {"name": phase}},
    ]


def example(repo=ATLAS, state="RETURNED", labels=None, issue=335, status="Todo"):
    if labels is None:
        labels = [
            f"gcl-state:{state.lower()}",
            "gcl-job",
            "gcl-role:verify",
            "gcl-collab:cooperative",
        ]
        if repo in {ATLAS, CDA, MATH}:
            labels.append(DIRECT)
    return (
        {
            "id": f"PVTI_item_{issue}",
            "content": {
                "repository": repo,
                "number": issue,
                "url": f"https://github.com/{repo}/issues/{issue}",
            },
            "status": status,
            "labels": labels,
        },
        fields(state=state),
    )


class WorkerProjectStatusTests(unittest.TestCase):
    def test_state_mapping_is_assignment_only(self):
        self.assertEqual(expected_status("AVAILABLE"), "Todo")
        self.assertEqual(expected_status("RETURNED"), "Done")
        self.assertEqual(expected_status("CLOSED"), "Done")
        self.assertEqual(expected_status("RESERVED"), "In Progress")
        self.assertEqual(expected_status("BLOCKED"), "In Progress")

    def test_direct_repo_requires_direct_pickup_label(self):
        self.assertEqual(
            expected_pickup_mode(ATLAS, {"gcl-job", DIRECT}, "AVAILABLE"),
            "direct_editorial",
        )
        with self.assertRaises(ValueError):
            expected_pickup_mode(ATLAS, {"gcl-job"}, "AVAILABLE")
        with self.assertRaises(ValueError):
            expected_pickup_mode(CDA, {"gcl-job", "gcl-pickup:unknown"}, "AVAILABLE")

    def test_math_programme_direct_editorial_picks_only_with_correct_labels_and_fields(self):
        self.assertEqual(expected_pickup_mode(MATH, {"gcl-job", DIRECT}, "AVAILABLE"), "direct_editorial")
        item, fields_for_issue = example(repo=MATH, state="AVAILABLE", issue=1256)
        actual = validated_item(item, fields_for_issue)
        self.assertEqual(actual["repo"], MATH)
        self.assertEqual(actual["pickup_mode"], "direct_editorial")
        self.assertEqual(actual["to_status"], "Todo")
        with self.assertRaises(ValueError):
            expected_pickup_mode(MATH, {"gcl-job"}, "AVAILABLE")
        with self.assertRaises(ValueError):
            expected_pickup_mode(MATH, {"gcl-job", DIRECT}, "RESERVED")

    def test_direct_repo_cannot_enter_reserved_state(self):
        with self.assertRaises(ValueError):
            expected_pickup_mode(ATLAS, {"gcl-job", DIRECT}, "RESERVED")

    def test_reservation_repo_forbids_direct_pickup_label(self):
        self.assertEqual(
            expected_pickup_mode(SOLVE, {"gcl-job"}, "AVAILABLE"),
            "reservation_controlled",
        )
        with self.assertRaises(ValueError):
            expected_pickup_mode(SOLVE, {"gcl-job", DIRECT}, "AVAILABLE")

    def test_returned_does_not_claim_editorial_acceptance(self):
        item, issue_fields = example()
        result = validated_item(item, issue_fields)
        self.assertEqual(result["to_status"], "Done")
        self.assertEqual(result["state"], "RETURNED")
        self.assertEqual(result["pickup_mode"], "direct_editorial")
        self.assertNotIn("editorially_accepted", result)
        self.assertNotIn("certification", result)

    def test_missing_or_duplicate_state_rejected(self):
        item, issue_fields = example()
        with self.assertRaises(ValueError):
            validated_item(item, [x for x in issue_fields if x["issue_field_name"] != "GCL State"])
        with self.assertRaises(ValueError):
            validated_item(item, issue_fields + [issue_fields[0]])

    def test_core_issue_fields_are_required(self):
        item, issue_fields = example()
        for name in ("GCL Campaign", "GCL Role", "GCL Collaboration", "GCL Phase"):
            with self.subTest(name=name):
                reduced = [x for x in issue_fields if x["issue_field_name"] != name]
                with self.assertRaises(ValueError):
                    validated_item(item, reduced)

    def test_label_field_disagreement_rejected(self):
        item, issue_fields = example(
            state="AVAILABLE",
            labels=["gcl-job", "gcl-state:returned", DIRECT, "gcl-role:verify", "gcl-collab:cooperative"],
        )
        with self.assertRaises(ValueError):
            validated_item(item, issue_fields)
        item, issue_fields = example(
            state="RETURNED",
            labels=["gcl-job", "gcl-state:available", DIRECT, "gcl-role:verify", "gcl-collab:cooperative"],
        )
        with self.assertRaises(ValueError):
            validated_item(item, issue_fields)

    def test_gcl_job_label_required(self):
        item, issue_fields = example(
            labels=["gcl-state:available", DIRECT, "gcl-role:verify", "gcl-collab:cooperative"],
            state="AVAILABLE",
        )
        with self.assertRaises(ValueError):
            validated_item(item, issue_fields)

    def test_unbound_url_and_unknown_repo_rejected(self):
        item, issue_fields = example()
        item["content"]["url"] = "https://github.com/another/issue/issues/1"
        with self.assertRaises(ValueError):
            validated_item(item, issue_fields)

        item, issue_fields = example()
        item["content"]["repository"] = "untrusted/external"
        item["content"]["url"] = "https://github.com/untrusted/external/issues/335"
        with self.assertRaises(ValueError):
            validated_item(item, issue_fields)

    def test_blocked_direct_state_without_state_label_is_not_available(self):
        item, issue_fields = example(
            state="BLOCKED",
            labels=["gcl-job", DIRECT, "gcl-role:verify", "gcl-collab:cooperative"],
        )
        result = validated_item(item, issue_fields)
        self.assertEqual(result["to_status"], "In Progress")
        self.assertEqual(result["pickup_mode"], "direct_editorial")

    def test_role_and_collaboration_label_field_conflict_rejected(self):
        item, issue_fields = example(
            state="AVAILABLE",
            labels=[
                "gcl-job",
                "gcl-state:available",
                DIRECT,
                "gcl-role:adversarial",
                "gcl-collab:cooperative",
            ],
        )
        with self.assertRaises(ValueError):
            validated_item(item, issue_fields)

        item, issue_fields = example(
            state="AVAILABLE",
            labels=[
                "gcl-job",
                "gcl-state:available",
                DIRECT,
                "gcl-role:verify",
                "gcl-collab:staged",
            ],
        )
        with self.assertRaises(ValueError):
            validated_item(item, issue_fields)

    def test_available_is_pickup_not_execution_permission(self):
        item, issue_fields = example(state="AVAILABLE")
        result = validated_item(item, issue_fields)
        self.assertEqual(result["to_status"], "Todo")
        self.assertEqual(result["state"], "AVAILABLE")
        self.assertEqual(result["pickup_mode"], "direct_editorial")

    def test_solve_available_uses_reservation_mode(self):
        self.assertEqual(
            expected_pickup_mode(SOLVE, {"gcl-job", "gcl-state:available"}, "AVAILABLE"),
            "reservation_controlled",
        )


if __name__ == "__main__":
    unittest.main()
