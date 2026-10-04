from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from ci.gcl_erdos3_github_contribution_intake import IntakeError, emit_intake, git_blob_sha1_text


DISPATCH_ID = "GCL-ERDOS3-E3-V03-IA-001"
ASSIGNMENT = "E3-V03"
AGENT = "INDEPENDENT-AGENT-E3-V03-001"
ISSUE_NUMBER = 798
ISSUE_TITLE = "[GCL-CONTRIB] GCL-ERDOS3 E3-V03-IA-001 — gluing-radius equivalence replay"

BOOTSTRAP = """GCL-CONTRIBUTION-DISPATCH/1

# E3-V03 — test bootstrap
"""

RESULT = """GCL-CONTRIBUTION-RESULT/1
dispatch_id: GCL-ERDOS3-E3-V03-IA-001
assignment: E3-V03
agent_ref: INDEPENDENT-AGENT-E3-V03-001
disposition: VERIFIED
context_class: ZERO_CONTEXT
external_sources: PROTECTED_PACKET_ONLY

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

        self.bootstrap_path = self.root / "work_packages/GCL_ERDOS3/launch/E3-V03-IA-001.md"
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
            "bootstrap_path": "work_packages/GCL_ERDOS3/launch/E3-V03-IA-001.md",
            "bootstrap_blob_sha1": git_blob_sha1_text(BOOTSTRAP),
            "context_class": "ZERO_CONTEXT",
            "external_sources": "PROTECTED_PACKET_ONLY",
            "canonical_mutation_authorized": False,
            "return_protocol": "GCL-CONTRIBUTION-RESULT/1",
            "state": "DISPATCHED__AWAITING_RETURN",
            "dispatch_status": "READY_FOR_GITHUB_COMMENT",
            "first_valid_result_lock": True,
            "automated_intake_canonical_effect": False,
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
                "created_at": "2026-10-04T00:00:00Z",
                "user": {"login": "independent-contributor"},
            },
        }

    def test_valid_exact_bound_result_emits_unadjudicated_receipt(self) -> None:
        output = self.root / "out"
        meta = emit_intake(self.event(), self.root, output)
        receipt = json.loads((output / "RECEIPT.json").read_text(encoding="utf-8"))
        self.assertEqual(meta["dispatch_id"], DISPATCH_ID)
        self.assertEqual(receipt["github_issue_number"], ISSUE_NUMBER)
        self.assertEqual(receipt["disposition_declared"], "VERIFIED")
        self.assertFalse(receipt["mathematical_correctness_adjudicated"])
        self.assertFalse(receipt["canonical_claim_effect"])
        self.assertFalse(receipt["frontier_effect"])
        self.assertFalse(receipt["certification_effect"])
        self.assertEqual((output / "RAW.md").read_text(encoding="utf-8"), RESULT)

    def test_wrong_issue_is_rejected(self) -> None:
        with self.assertRaisesRegex(IntakeError, "wrong issue"):
            emit_intake(self.event(number=999), self.root, self.root / "out")

    def test_wrong_issue_title_is_rejected(self) -> None:
        with self.assertRaisesRegex(IntakeError, "issue title"):
            emit_intake(self.event(title="tampered title"), self.root, self.root / "out")

    def test_task_byte_drift_is_rejected(self) -> None:
        self.task_path.write_text("# changed after dispatch\n", encoding="utf-8")
        with self.assertRaisesRegex(IntakeError, "task bytes drifted"):
            emit_intake(self.event(), self.root, self.root / "out")

    def test_unregistered_disposition_is_rejected(self) -> None:
        bad = RESULT.replace("disposition: VERIFIED", "disposition: PROVED")
        with self.assertRaisesRegex(IntakeError, "disposition"):
            emit_intake(self.event(body=bad), self.root, self.root / "out")

    def test_agent_mismatch_is_rejected(self) -> None:
        bad = RESULT.replace(AGENT, "INDEPENDENT-AGENT-WRONG")
        with self.assertRaisesRegex(IntakeError, "agent_ref"):
            emit_intake(self.event(body=bad), self.root, self.root / "out")

    def test_bootstrap_byte_drift_is_rejected(self) -> None:
        event = self.event()
        event["issue"]["body"] = BOOTSTRAP + "tamper\n"
        with self.assertRaisesRegex(IntakeError, "issue body differs"):
            emit_intake(event, self.root, self.root / "out")


if __name__ == "__main__":
    unittest.main()
