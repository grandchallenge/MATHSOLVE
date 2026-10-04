from __future__ import annotations

import json
import shutil
import tempfile
import unittest
from pathlib import Path

from ci.gcl_erdos3_github_contribution_intake import (
    IntakeError,
    emit_intake,
    git_blob_sha1,
    parse_result_comment,
)


VALID_BODY = """GCL-CONTRIBUTION-RESULT/1
dispatch_id: GCL-ERDOS3-E3-V03-IA-001
assignment: E3-V03
agent_ref: INDEPENDENT-AGENT-E3-V03-001
disposition: VERIFIED
context_class: ZERO_CONTEXT
external_sources: PROTECTED_PACKET_ONLY

## Strongest exact statement

The bounded bridge is verified.

## Derivation / evidence

Re-derive both inequalities directly from the definitions.

## Adversarial checks

Check inequality direction, the factor m, nonempty feasibility, and carry completeness.

## First defect

NONE

## Frontier effect

The bridge may proceed to governed adjudication; no parent claim follows automatically.

## Next residual

Adjudicate the verified bridge under the protected frontier gate.

## Sources

PROTECTED_PACKET_ONLY
"""


class GclErdos3IntakeTests(unittest.TestCase):
    def make_root(self) -> tuple[Path, str, dict]:
        root = Path(tempfile.mkdtemp())
        self.addCleanup(lambda: shutil.rmtree(root, ignore_errors=True))

        base = root / "work_packages/GCL_ERDOS3"
        dispatch_dir = base / "dispatches"
        bootstrap_dir = base / "dispatch_bootstraps"
        dispatch_dir.mkdir(parents=True)
        bootstrap_dir.mkdir(parents=True)

        bootstrap = """GCL-CONTRIBUTION-DISPATCH/1

# E3-V03 fixture
"""
        bootstrap_rel = "work_packages/GCL_ERDOS3/dispatch_bootstraps/GCL-ERDOS3-E3-V03-IA-001.md"
        (root / bootstrap_rel).write_text(bootstrap, encoding="utf-8")

        dispatch = {
            "schema_version": "1.0.0",
            "record_type": "GCL_CONTRIBUTION_DISPATCH",
            "campaign": "GCL-ERDOS3",
            "tranche": "E3-V03",
            "assignment_id": "E3-V03",
            "dispatch_id": "GCL-ERDOS3-E3-V03-IA-001",
            "agent_ref": "INDEPENDENT-AGENT-E3-V03-001",
            "concurrency_mode": "independent_blind",
            "issue_number": 798,
            "github_issue_number": 798,
            "github_issue_title": "[GCL-CONTRIB] GCL-ERDOS3 E3-V03-IA-001 — gluing-radius equivalence replay",
            "bootstrap_path": bootstrap_rel,
            "bootstrap_blob_sha1": git_blob_sha1(bootstrap),
            "task_commit": "e" * 40,
            "task_path": "work_packages/GCL_ERDOS3/work_packages/E3-V03.md",
            "task_blob_sha1": "f" * 40,
            "target_node": "E3-B-GLUING-RADIUS-EQUIV",
            "frontier_action": "INDEPENDENT_VERIFY",
            "replay_budget_ordinal": 1,
            "context_class": "ZERO_CONTEXT",
            "external_sources": "PROTECTED_PACKET_ONLY",
            "canonical_mutation_authorized": False,
            "return_protocol": "GCL-CONTRIBUTION-RESULT/1",
            "state": "DISPATCHED__AWAITING_RETURN",
            "acceptable_dispositions": ["VERIFIED", "REFUTED", "EXACT_BLOCKER"],
            "required_result_sections": [
                "Strongest exact statement",
                "Derivation / evidence",
                "Adversarial checks",
                "First defect",
                "Frontier effect",
                "Next residual",
                "Sources",
            ],
            "intake_policy": {
                "first_valid_result_only": True,
                "raw_urls_allowed": False,
                "markdown_links_allowed": False,
                "html_links_or_images_allowed": False,
                "attachments_allowed": False,
                "next_residual_max_sentences": 3,
                "automatic_mathematical_adjudication": False,
                "automatic_canonical_claim_effect": False,
            },
        }
        (dispatch_dir / "GCL-ERDOS3-E3-V03-IA-001.json").write_text(
            json.dumps(dispatch), encoding="utf-8"
        )
        return root, bootstrap, dispatch

    def event(self, bootstrap: str) -> dict:
        return {
            "issue": {
                "number": 798,
                "title": "[GCL-CONTRIB] GCL-ERDOS3 E3-V03-IA-001 — gluing-radius equivalence replay",
                "body": bootstrap,
            },
            "comment": {
                "id": 99001,
                "body": VALID_BODY,
                "created_at": "2026-10-04T00:30:00Z",
                "user": {"login": "independent-contributor"},
            },
        }

    def test_valid_comment_parses_against_dispatch(self) -> None:
        root, _bootstrap, dispatch = self.make_root()
        parsed = parse_result_comment(VALID_BODY, dispatch)
        self.assertEqual(parsed["preamble"]["dispatch_id"], "GCL-ERDOS3-E3-V03-IA-001")
        self.assertEqual(parsed["preamble"]["disposition"], "VERIFIED")

    def test_event_emits_raw_receipt_without_claim_effect(self) -> None:
        root, bootstrap, _dispatch = self.make_root()
        out = root / "out"
        meta = emit_intake(self.event(bootstrap), root, out)
        self.assertEqual(meta["branch"], "intake/gcl-erdos3-e3-v03-ia-001")
        self.assertEqual((out / "RAW.md").read_text(encoding="utf-8"), VALID_BODY)
        receipt = json.loads((out / "RECEIPT.json").read_text(encoding="utf-8"))
        self.assertEqual(receipt["github_issue_number"], 798)
        self.assertEqual(receipt["github_comment_id"], 99001)
        self.assertEqual(receipt["handling_state"], "received_unadjudicated")
        self.assertFalse(receipt["mathematical_correctness_adjudicated"])
        self.assertFalse(receipt["canonical_claim_effect"])
        self.assertFalse(receipt["certification_effect"])
        self.assertEqual(receipt["replay_budget_ordinal"], 1)

    def test_wrong_issue_number_is_rejected(self) -> None:
        root, bootstrap, _dispatch = self.make_root()
        event = self.event(bootstrap)
        event["issue"]["number"] = 790
        with self.assertRaises(IntakeError):
            emit_intake(event, root, root / "out")

    def test_changed_issue_title_is_rejected(self) -> None:
        root, bootstrap, _dispatch = self.make_root()
        event = self.event(bootstrap)
        event["issue"]["title"] = "[GCL-CONTRIB] GCL-ERDOS3 wrong"
        with self.assertRaises(IntakeError):
            emit_intake(event, root, root / "out")

    def test_changed_bootstrap_is_rejected(self) -> None:
        root, bootstrap, _dispatch = self.make_root()
        event = self.event(bootstrap + "changed")
        with self.assertRaises(IntakeError):
            emit_intake(event, root, root / "out")

    def test_wrong_agent_ref_is_rejected(self) -> None:
        root, bootstrap, _dispatch = self.make_root()
        event = self.event(bootstrap)
        event["comment"]["body"] = VALID_BODY.replace(
            "agent_ref: INDEPENDENT-AGENT-E3-V03-001",
            "agent_ref: INDEPENDENT-AGENT-WRONG",
        )
        with self.assertRaises(IntakeError):
            emit_intake(event, root, root / "out")

    def test_unregistered_disposition_is_rejected(self) -> None:
        root, bootstrap, _dispatch = self.make_root()
        event = self.event(bootstrap)
        event["comment"]["body"] = VALID_BODY.replace(
            "disposition: VERIFIED", "disposition: PROVED"
        )
        with self.assertRaises(IntakeError):
            emit_intake(event, root, root / "out")

    def test_url_is_rejected_under_protected_packet_policy(self) -> None:
        root, bootstrap, _dispatch = self.make_root()
        event = self.event(bootstrap)
        event["comment"]["body"] = VALID_BODY.replace(
            "PROTECTED_PACKET_ONLY\n", "https://example.com\n", 1
        )
        with self.assertRaises(IntakeError):
            emit_intake(event, root, root / "out")

    def test_extra_section_is_rejected(self) -> None:
        root, bootstrap, _dispatch = self.make_root()
        event = self.event(bootstrap)
        event["comment"]["body"] = VALID_BODY + "\n## Extra\n\nNo.\n"
        with self.assertRaises(IntakeError):
            emit_intake(event, root, root / "out")

    def test_four_sentence_next_residual_is_rejected(self) -> None:
        root, bootstrap, _dispatch = self.make_root()
        event = self.event(bootstrap)
        event["comment"]["body"] = VALID_BODY.replace(
            "Adjudicate the verified bridge under the protected frontier gate.",
            "One. Two. Three. Four.",
        )
        with self.assertRaises(IntakeError):
            emit_intake(event, root, root / "out")

    def test_dispatch_not_awaiting_return_is_rejected(self) -> None:
        root, bootstrap, dispatch = self.make_root()
        dispatch["state"] = "ADJUDICATED"
        path = root / "work_packages/GCL_ERDOS3/dispatches/GCL-ERDOS3-E3-V03-IA-001.json"
        path.write_text(json.dumps(dispatch), encoding="utf-8")
        with self.assertRaises(IntakeError):
            emit_intake(self.event(bootstrap), root, root / "out")

    def test_canonical_mutation_authority_is_rejected(self) -> None:
        root, bootstrap, dispatch = self.make_root()
        dispatch["canonical_mutation_authorized"] = True
        path = root / "work_packages/GCL_ERDOS3/dispatches/GCL-ERDOS3-E3-V03-IA-001.json"
        path.write_text(json.dumps(dispatch), encoding="utf-8")
        with self.assertRaises(IntakeError):
            emit_intake(self.event(bootstrap), root, root / "out")


if __name__ == "__main__":
    unittest.main()
