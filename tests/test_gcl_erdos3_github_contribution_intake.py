from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from ci.gcl_erdos3_github_contribution_intake import (
    IntakeError,
    emit_intake,
    git_blob_sha1_text,
)


DISPATCH_ID = "GCL-ERDOS3-E3-V03-IA-002"
ASSIGNMENT = "E3-V03"
AGENT = "INDEPENDENT-AGENT-E3-V03-002"
ISSUE_NUMBER = 814
ISSUE_TITLE = "[GCL-CONTRIB] GCL-ERDOS3 E3-V03-IA-002 — gluing-radius equivalence replay"

BOOTSTRAP = """GCL-CONTRIBUTION-DISPATCH/1

# E3-V03 — test bootstrap
"""

ACTIVATION = """GCL-LEASE-ACTIVATION/1
dispatch_id: GCL-ERDOS3-E3-V03-IA-002
assignment: E3-V03
lease_epoch: 2
lease_duration_minutes: 25
agent_max_execution_minutes: 24"""

RESULT = """GCL-CONTRIBUTION-RESULT/1
dispatch_id: GCL-ERDOS3-E3-V03-IA-002
assignment: E3-V03
agent_ref: INDEPENDENT-AGENT-E3-V03-002
disposition: VERIFIED
context_class: ZERO_CONTEXT
external_sources: PROTECTED_PACKET_ONLY
lease_epoch: 2
agent_elapsed_minutes: 24

## Strongest exact statement

The bounded bridge replays.

## Derivation / evidence

The inequalities were re-derived from the protected definitions.

## Adversarial checks

All requested edge cases were checked.

## First defect

NONE

## Frontier effect

Verification evidence only.

## Next residual

Adjudication remains with GCL.

## Sources

PROTECTED_PACKET_ONLY
"""


class GclErdos3IntakeTests(unittest.TestCase):
    def setUp(self) -> None:
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        (self.root / "work_packages/GCL_ERDOS3/dispatches").mkdir(parents=True)
        (self.root / "work_packages/GCL_ERDOS3/launch").mkdir(parents=True)
        (self.root / "work_packages/GCL_ERDOS3/work_packages").mkdir(parents=True)

        self.bootstrap_path = self.root / "work_packages/GCL_ERDOS3/launch/E3-V03-IA-002.md"
        self.bootstrap_path.write_text(BOOTSTRAP, encoding="utf-8")
        self.task_path = self.root / "work_packages/GCL_ERDOS3/work_packages/E3-V03.md"
        self.task_path.write_text("# immutable test task\n", encoding="utf-8")

        dispatch = {
            "schema_version": "1.0.0",
            "campaign": "GCL-ERDOS3",
            "assignment_id": ASSIGNMENT,
            "dispatch_id": DISPATCH_ID,
            "agent_ref": AGENT,
            "concurrency_mode": "independent_blind",
            "github_issue_number": ISSUE_NUMBER,
            "github_issue_title": ISSUE_TITLE,
            "task_commit": "a" * 40,
            "task_path": "work_packages/GCL_ERDOS3/work_packages/E3-V03.md",
            "task_blob_sha1": git_blob_sha1_text(self.task_path.read_text(encoding="utf-8")),
            "bootstrap_path": "work_packages/GCL_ERDOS3/launch/E3-V03-IA-002.md",
            "bootstrap_blob_sha1": git_blob_sha1_text(BOOTSTRAP),
            "context_class": "ZERO_CONTEXT",
            "external_sources": "PROTECTED_PACKET_ONLY",
            "canonical_mutation_authorized": False,
            "return_protocol": "GCL-CONTRIBUTION-RESULT/1",
            "state": "DISPATCHED__AWAITING_RETURN",
            "dispatch_status": "READY_FOR_GITHUB_COMMENT",
            "first_valid_result_lock": True,
            "automated_intake_canonical_effect": False,
            "lease_policy_id": "GCL-IA-LEASE-25M-24M-001",
            "lease_policy": "work_packages/GCL_ERDOS3/LEASE_POLICY.json",
            "lease_clock_source": "GITHUB_ACTIVATION_COMMENT",
            "lease_activation_marker": "GCL-LEASE-ACTIVATION/1",
            "lease_epoch": 2,
            "lease_attempt_ordinal": 2,
            "lease_duration_minutes": 25,
            "agent_max_execution_minutes": 24,
            "return_grace_minutes": 1,
            "allowed_dispositions": ["VERIFIED", "REFUTED", "EXACT_BLOCKER"],
            "required_sections": [
                "Strongest exact statement",
                "Derivation / evidence",
                "Adversarial checks",
                "First defect",
                "Frontier effect",
                "Next residual",
                "Sources",
            ],
        }
        (self.root / f"work_packages/GCL_ERDOS3/dispatches/{DISPATCH_ID}.json").write_text(
            json.dumps(dispatch), encoding="utf-8"
        )

    def tearDown(self) -> None:
        self.tmp.cleanup()

    def activation_comments(self) -> list[dict]:
        return [{
            "id": 100,
            "body": ACTIVATION,
            "created_at": "2026-10-04T00:00:00Z",
            "user": {"login": "github-actions[bot]"},
        }]

    def event(self, *, body: str = RESULT, number: int = ISSUE_NUMBER, title: str = ISSUE_TITLE) -> dict:
        return {
            "issue": {
                "number": number,
                "title": title,
                "body": BOOTSTRAP,
            },
            "comment": {
                "id": 123456,
                "body": body,
                "created_at": "2026-10-04T00:24:00Z",
                "user": {"login": "independent-contributor"},
            },
        }

    def emit(self, event: dict | None = None, comments: list[dict] | None = None):
        return emit_intake(
            event or self.event(),
            self.root,
            self.root / "out",
            self.activation_comments() if comments is None else comments,
        )

    def test_valid_later_attempt_result_emits_unadjudicated_receipt(self) -> None:
        meta = self.emit()
        receipt = json.loads((self.root / "out/RECEIPT.json").read_text(encoding="utf-8"))
        self.assertEqual(meta["dispatch_id"], DISPATCH_ID)
        self.assertEqual(receipt["github_issue_number"], ISSUE_NUMBER)
        self.assertEqual(receipt["disposition_declared"], "VERIFIED")
        self.assertEqual(receipt["lease_activation_comment_id"], 100)
        self.assertEqual(receipt["lease_started_at"], "2026-10-04T00:00:00Z")
        self.assertEqual(receipt["lease_expires_at"], "2026-10-04T00:25:00Z")
        self.assertFalse(receipt["mathematical_correctness_adjudicated"])
        self.assertFalse(receipt["canonical_claim_effect"])
        self.assertFalse(receipt["frontier_effect"])
        self.assertFalse(receipt["certification_effect"])
        self.assertEqual((self.root / "out/RAW.md").read_text(encoding="utf-8"), RESULT)

    def test_wrong_issue_is_rejected(self) -> None:
        with self.assertRaisesRegex(IntakeError, "wrong issue"):
            self.emit(self.event(number=999))

    def test_wrong_issue_title_is_rejected(self) -> None:
        with self.assertRaisesRegex(IntakeError, "issue title"):
            self.emit(self.event(title="tampered title"))

    def test_task_byte_drift_is_rejected(self) -> None:
        self.task_path.write_text("# changed after dispatch\n", encoding="utf-8")
        with self.assertRaisesRegex(IntakeError, "task bytes drifted"):
            self.emit()

    def test_unregistered_disposition_is_rejected(self) -> None:
        bad = RESULT.replace("disposition: VERIFIED", "disposition: PROVED")
        with self.assertRaisesRegex(IntakeError, "disposition"):
            self.emit(self.event(body=bad))

    def test_agent_mismatch_is_rejected(self) -> None:
        bad = RESULT.replace(AGENT, "INDEPENDENT-AGENT-WRONG")
        with self.assertRaisesRegex(IntakeError, "agent_ref"):
            self.emit(self.event(body=bad))

    def test_bootstrap_byte_drift_is_rejected(self) -> None:
        event = self.event()
        event["issue"]["body"] = BOOTSTRAP + "tamper\n"
        with self.assertRaisesRegex(IntakeError, "issue body differs"):
            self.emit(event)

    def test_missing_activation_marker_is_rejected(self) -> None:
        with self.assertRaisesRegex(IntakeError, "exactly one matching lease activation marker"):
            self.emit(comments=[])

    def test_duplicate_activation_marker_is_rejected(self) -> None:
        comments = self.activation_comments() + [{
            "id": 101,
            "body": ACTIVATION,
            "created_at": "2026-10-04T00:00:01Z",
            "user": {"login": "github-actions[bot]"},
        }]
        with self.assertRaisesRegex(IntakeError, "exactly one matching lease activation marker"):
            self.emit(comments=comments)

    def test_expired_comment_is_rejected(self) -> None:
        event = self.event()
        event["comment"]["created_at"] = "2026-10-04T00:25:01Z"
        with self.assertRaisesRegex(IntakeError, "lease expired"):
            self.emit(event)

    def test_result_before_activation_is_rejected(self) -> None:
        event = self.event()
        event["comment"]["created_at"] = "2026-10-03T23:59:59Z"
        with self.assertRaisesRegex(IntakeError, "predates lease activation"):
            self.emit(event)

    def test_stale_lease_epoch_is_rejected(self) -> None:
        bad = RESULT.replace("lease_epoch: 2", "lease_epoch: 1")
        with self.assertRaisesRegex(IntakeError, "lease epoch"):
            self.emit(self.event(body=bad))

    def test_agent_execution_cap_is_rejected(self) -> None:
        bad = RESULT.replace("agent_elapsed_minutes: 24", "agent_elapsed_minutes: 25")
        with self.assertRaisesRegex(IntakeError, "24-minute cap"):
            self.emit(self.event(body=bad))


if __name__ == "__main__":
    unittest.main()
