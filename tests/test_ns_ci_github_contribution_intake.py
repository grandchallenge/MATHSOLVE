from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from ci.ns_ci_github_contribution_intake import (
    IntakeError,
    emit_intake,
    parse_result_comment,
)


VALID_BODY = """GCL-CONTRIBUTION-RESULT/1
dispatch_id: NSCI-C2-A-BLIND-001
assignment: A
disposition: REDUCED
context_class: ZERO_CONTEXT
external_sources: NONE
timebox_observed: YES

## Strongest exact statement

A precise reduced statement.

## Derivation

A complete derivation with no external reference.

## Assumptions beyond bootstrap

NONE

## Verification / falsification hooks

Differentiate the displayed identity directly.

## Claim boundary

This does not prove the parent theorem.

## Next residual

Prove the missing persistence bound.
"""


class ResultGrammarTests(unittest.TestCase):
    def test_valid_comment_parses(self) -> None:
        parsed = parse_result_comment(VALID_BODY)
        self.assertEqual(parsed["preamble"]["dispatch_id"], "NSCI-C2-A-BLIND-001")
        self.assertEqual(parsed["preamble"]["disposition"], "REDUCED")

    def test_url_is_rejected(self) -> None:
        with self.assertRaises(IntakeError):
            parse_result_comment(VALID_BODY.replace("complete derivation", "https://example.com derivation"))

    def test_markdown_link_is_rejected(self) -> None:
        with self.assertRaises(IntakeError):
            parse_result_comment(VALID_BODY.replace("complete derivation", "[derivation](elsewhere)"))

    def test_extra_level_two_section_is_rejected(self) -> None:
        with self.assertRaises(IntakeError):
            parse_result_comment(VALID_BODY + "\n## Additional notes\n\nNo.\n")

    def test_wrong_context_class_is_rejected(self) -> None:
        with self.assertRaises(IntakeError):
            parse_result_comment(VALID_BODY.replace("context_class: ZERO_CONTEXT", "context_class: OTHER"))

    def test_wrong_external_sources_is_rejected(self) -> None:
        with self.assertRaises(IntakeError):
            parse_result_comment(VALID_BODY.replace("external_sources: NONE", "external_sources: SOME"))


class EventIntakeTests(unittest.TestCase):
    def make_root(self) -> tuple[Path, str]:
        temp = Path(tempfile.mkdtemp())
        self.addCleanup(lambda: __import__("shutil").rmtree(temp, ignore_errors=True))
        base = temp / "contributions/NS-CI-001/C2_MIX_DIRECTION_COMPRESSION_LEDGER_CHARGE"
        dispatch_dir = base / "dispatches"
        bootstrap_dir = base / "dispatch_bootstraps"
        dispatch_dir.mkdir(parents=True)
        bootstrap_dir.mkdir(parents=True)
        bootstrap = "GCL-CONTRIBUTION-DISPATCH/1\n\n# fixture\n"
        bootstrap_path = bootstrap_dir / "NSCI-C2-A-BLIND-001.md"
        bootstrap_path.write_text(bootstrap, encoding="utf-8")
        import hashlib
        digest = hashlib.sha256(bootstrap.encode("utf-8")).hexdigest()
        dispatch = {
            "schema_version": "0.2-pilot",
            "dispatch_id": "NSCI-C2-A-BLIND-001",
            "assignment_id": "A",
            "concurrency_mode": "independent_blind",
            "blind_cohort_id": "COHORT",
            "return_protocol": "GCL-CONTRIBUTION-RESULT/1",
            "dispatch_status": "READY_FOR_GITHUB_COMMENT",
            "canonical_mutation_authorized": False,
            "github_issue_number": 101,
            "github_issue_title": "[GCL-CONTRIB] NSCI-C2-A-BLIND-001 — Assignment A",
            "bootstrap_path": bootstrap_path.relative_to(temp).as_posix(),
            "bootstrap_sha256": digest,
            "source_handoff_commit_sha": "a" * 40,
            "source_handoff_blob_sha": "b" * 40,
            "source_handoff_sha256": "c" * 64,
        }
        (dispatch_dir / "NSCI-C2-A-BLIND-001.json").write_text(
            json.dumps(dispatch), encoding="utf-8"
        )
        return temp, bootstrap

    def event(self, bootstrap: str) -> dict:
        return {
            "issue": {
                "number": 101,
                "title": "[GCL-CONTRIB] NSCI-C2-A-BLIND-001 — Assignment A",
                "body": bootstrap,
            },
            "comment": {
                "id": 9001,
                "body": VALID_BODY,
                "created_at": "2026-09-20T12:00:00Z",
                "user": {"login": "independent-agent"},
            },
        }

    def test_event_emits_raw_and_receipt(self) -> None:
        root, bootstrap = self.make_root()
        out = root / "out"
        meta = emit_intake(self.event(bootstrap), root, out)
        self.assertTrue((out / "RAW.md").is_file())
        receipt = json.loads((out / "RECEIPT.json").read_text(encoding="utf-8"))
        self.assertEqual(receipt["github_comment_id"], 9001)
        self.assertEqual(receipt["handling_state"], "received_unadjudicated")
        self.assertFalse(receipt["mathematical_correctness_adjudicated"])
        self.assertEqual(meta["branch"], "intake/nsci-c2-a-blind-001")
        self.assertEqual(meta["pr_title"], "NS-CI intake: NSCI-C2-A-BLIND-001")
        self.assertIn("github-comment-9001.md", meta["raw_repo_path"])

    def test_different_comment_ids_share_dispatch_lock_branch(self) -> None:
        root, bootstrap = self.make_root()
        first = self.event(bootstrap)
        second = self.event(bootstrap)
        second["comment"]["id"] = 9002

        first_meta = emit_intake(first, root, root / "first")
        second_meta = emit_intake(second, root, root / "second")

        self.assertEqual(first_meta["branch"], second_meta["branch"])
        self.assertNotEqual(first_meta["raw_repo_path"], second_meta["raw_repo_path"])
        self.assertIn("github-comment-9001.md", first_meta["raw_repo_path"])
        self.assertIn("github-comment-9002.md", second_meta["raw_repo_path"])

    def test_wrong_issue_number_is_rejected(self) -> None:
        root, bootstrap = self.make_root()
        event = self.event(bootstrap)
        event["issue"]["number"] = 102
        with self.assertRaises(IntakeError):
            emit_intake(event, root, root / "out")

    def test_changed_bootstrap_is_rejected(self) -> None:
        root, bootstrap = self.make_root()
        event = self.event(bootstrap + "changed")
        with self.assertRaises(IntakeError):
            emit_intake(event, root, root / "out")

    def test_wrong_assignment_is_rejected(self) -> None:
        root, bootstrap = self.make_root()
        event = self.event(bootstrap)
        event["comment"]["body"] = VALID_BODY.replace("assignment: A", "assignment: B")
        with self.assertRaises(IntakeError):
            emit_intake(event, root, root / "out")


UC_VALID_BODY = """GCL-CONTRIBUTION-RESULT/1
dispatch_id: UC-WP08-D004-WP01-IA-001
agent_ref: INDEPENDENT-AGENT-UC401
assignment: UC-WP08-D004-WP01
disposition: PROVED_REDUCTION
context_class: ZERO_CONTEXT
external_sources: PROTECTED_PACKET_ONLY
timebox_observed: YES

## Strongest exact statement

A bounded exact incidence lemma.

## Derivation

A complete derivation from the packet.

## Assumptions beyond bootstrap

NONE

## Verification / falsification hooks

Check the finite-order identities directly.

## Claim boundary

This does not close UC-P04 or Frankl's conjecture.

## Next residual

Formalize the exact incidence equality.
"""


class UcD004ResultGrammarTests(unittest.TestCase):
    def test_valid_uc_comment_parses(self) -> None:
        parsed = parse_result_comment(UC_VALID_BODY)
        self.assertEqual(parsed["profile"], "UC-001")
        self.assertEqual(parsed["preamble"]["agent_ref"], "INDEPENDENT-AGENT-UC401")

    def test_uc_requires_agent_ref(self) -> None:
        body = UC_VALID_BODY.replace("agent_ref: INDEPENDENT-AGENT-UC401\n", "")
        with self.assertRaises(IntakeError):
            parse_result_comment(body)

    def test_uc_rejects_unregistered_external_sources(self) -> None:
        with self.assertRaises(IntakeError):
            parse_result_comment(
                UC_VALID_BODY.replace(
                    "external_sources: PROTECTED_PACKET_ONLY",
                    "external_sources: NONE",
                )
            )


    def test_crlf_comment_parses_without_normalizing_raw_bytes(self) -> None:
        body = UC_VALID_BODY.replace("\n", "\r\n")
        parsed = parse_result_comment(body)
        self.assertEqual(parsed["profile"], "UC-001")
        self.assertEqual(parsed["preamble"]["dispatch_id"], "UC-WP08-D004-WP01-IA-001")

    def test_mathematical_less_than_text_is_not_html(self) -> None:
        body = UC_VALID_BODY.replace(
            "A complete derivation from the packet.",
            "Take y < a. On M3 use 0 < a, b, c < 1. Hence x<a is also ordinary mathematical text.",
        )
        parsed = parse_result_comment(body)
        self.assertEqual(parsed["profile"], "UC-001")

    def test_actual_anchor_tag_is_rejected(self) -> None:
        body = UC_VALID_BODY.replace(
            "A complete derivation from the packet.",
            "A complete derivation <a href='relative/path'>elsewhere</a>.",
        )
        with self.assertRaises(IntakeError):
            parse_result_comment(body)

    def test_actual_img_tag_is_rejected(self) -> None:
        body = UC_VALID_BODY.replace(
            "A complete derivation from the packet.",
            "A complete derivation <img src='relative-image.png'>.",
        )
        with self.assertRaises(IntakeError):
            parse_result_comment(body)


    def test_three_numbered_next_residual_items_count_as_three_sentences(self) -> None:
        body = UC_VALID_BODY.replace(
            "Formalize the exact incidence equality.",
            "1. Determine the canonical implication base.\n2. Analyze non-unary frequency constraints.\n3. Investigate frequency balance.",
        )
        parsed = parse_result_comment(body)
        self.assertEqual(parsed["profile"], "UC-001")

    def test_four_numbered_next_residual_items_are_rejected(self) -> None:
        body = UC_VALID_BODY.replace(
            "Formalize the exact incidence equality.",
            "1. First residual.\n2. Second residual.\n3. Third residual.\n4. Fourth residual.",
        )
        with self.assertRaises(IntakeError):
            parse_result_comment(body)


CMDG_VALID_BODY = """GCL-CONTRIBUTION-RESULT/1
dispatch_id: CMDG-P3M-SEP-WP-A-IA-001
agent_ref: INDEPENDENT-AGENT-CMDG-A
assignment: CMDG-P3M-SEP-WP-A
disposition: PROVED_REDUCTION
context_class: ZERO_CONTEXT
external_sources: PROTECTED_PACKET_ONLY
timebox_observed: YES

## Strongest exact statement

A bounded one-point separation reduction.

## Derivation

A complete derivation from the protected packet.

## Assumptions beyond bootstrap

NONE

## Verification / falsification hooks

Check the one-point interface directly.

## Claim boundary

This does not prove d equals zero or CM4.

## Next residual

Formalize the smallest missing separation lemma.
"""


class CmdgP3MResultGrammarTests(unittest.TestCase):
    def test_valid_cmdg_comment_parses(self) -> None:
        parsed = parse_result_comment(CMDG_VALID_BODY)
        self.assertEqual(parsed["profile"], "CMDG-CM4")
        self.assertEqual(parsed["preamble"]["agent_ref"], "INDEPENDENT-AGENT-CMDG-A")

    def test_cmdg_rejects_wrong_assignment(self) -> None:
        body = CMDG_VALID_BODY.replace(
            "assignment: CMDG-P3M-SEP-WP-A",
            "assignment: CMDG-P3M-SEP-WP-E",
        )
        with self.assertRaises(IntakeError):
            parse_result_comment(body)


if __name__ == "__main__":
    unittest.main()
