import json
import tempfile
import unittest
from pathlib import Path

from ci.openmath_cex_github_contribution_intake import IntakeError, emit_intake, parse_result_comment


H1_VALID = """GCL-CONTRIBUTION-RESULT/1
dispatch_id: OM26-H1-H1-12-IA-001
agent_ref: INDEPENDENT-AGENT-001
assignment: OM26-H1-H1-12
disposition: PROVED_REDUCTION
context_class: ZERO_CONTEXT
external_sources: PROTECTED_PACKET_ONLY
timebox_observed: YES

## Strongest exact statement

A precise bounded statement.

## Derivation

A complete bounded derivation.

## Assumptions beyond bootstrap

NONE

## Verification / falsification hooks

Replay the finite argument independently.

## Claim boundary

This does not prove global optimality.

## Next residual

The remaining q>=6 cases remain open.
"""

H2_VALID = H1_VALID.replace(
    "OM26-H1-H1-12-IA-001", "OM26-H2-WP01-IA-001"
).replace(
    "INDEPENDENT-AGENT-001", "INDEPENDENT-AGENT-002"
).replace(
    "OM26-H1-H1-12", "OM26-H2-WP01"
).replace(
    "PROVED_REDUCTION", "INDEPENDENT_SCORER_CONCORDANCE"
)


class OpenMathCEXGitHubContributionIntakeTest(unittest.TestCase):
    def test_h1_result_still_parses(self):
        parsed = parse_result_comment(H1_VALID)
        self.assertEqual(parsed["preamble"]["dispatch_id"], "OM26-H1-H1-12-IA-001")
        self.assertEqual(parsed["preamble"]["disposition"], "PROVED_REDUCTION")

    def test_generic_h2_result_parses_structurally(self):
        parsed = parse_result_comment(H2_VALID)
        self.assertEqual(parsed["preamble"]["dispatch_id"], "OM26-H2-WP01-IA-001")
        self.assertEqual(parsed["preamble"]["assignment"], "OM26-H2-WP01")
        self.assertEqual(parsed["preamble"]["disposition"], "INDEPENDENT_SCORER_CONCORDANCE")

    def test_wrong_agent_rejected_by_dispatch_layer_not_parser(self):
        body = H1_VALID.replace("INDEPENDENT-AGENT-001", "OTHER-AGENT")
        parsed = parse_result_comment(body)
        self.assertEqual(parsed["preamble"]["agent_ref"], "OTHER-AGENT")

    def test_url_in_result_rejected(self):
        body = H1_VALID.replace("A complete bounded derivation.", "See https://example.com")
        with self.assertRaises(IntakeError):
            parse_result_comment(body)

    def test_missing_section_rejected(self):
        body = H1_VALID.replace("## Claim boundary\n\nThis does not prove global optimality.\n\n", "")
        with self.assertRaises(IntakeError):
            parse_result_comment(body)

    def test_bad_disposition_token_rejected_structurally(self):
        body = H1_VALID.replace("PROVED_REDUCTION", "NOT ALLOWED")
        with self.assertRaises(IntakeError):
            parse_result_comment(body)

    def test_dispatch_issue_allows_one_terminal_lf_transport_difference(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            base = root / "contributions/OPENMATH-2026/OM26-H2/WP01"
            dispatch_dir = base / "dispatches"
            dispatch_dir.mkdir(parents=True)
            operation_dir = root / ".gcl/operations/OM26-H2-WP01-IA-001"
            operation_dir.mkdir(parents=True)
            bootstrap = root / "handoffs/OPENMATH-2026/jobs/OM26-H2-WP01-IA-001.md"
            bootstrap.parent.mkdir(parents=True)

            issue_body = """GCL-CONTRIBUTION-DISPATCH/1
dispatch_id: OM26-H2-WP01-IA-001
agent_ref: INDEPENDENT-AGENT-002
assignment: OM26-H2-WP01"""
            bootstrap.write_text(issue_body + "\n", encoding="utf-8")

            dispatch = {
                "schema_version": "1.0.0",
                "record_type": "GCL_EXTERNAL_DISPATCH",
                "dispatch_id": "OM26-H2-WP01-IA-001",
                "campaign": "OPENMATH-2026",
                "hill": "OM26-H2",
                "assignment_id": "OM26-H2-WP01",
                "agent_ref": "INDEPENDENT-AGENT-002",
                "concurrency_mode": "independent_blind",
                "bootstrap_path": "handoffs/OPENMATH-2026/jobs/OM26-H2-WP01-IA-001.md",
                "bootstrap_blob_sha1": "a" * 40,
                "source_handoff_commit_sha": "b" * 40,
                "return_protocol": "GCL-CONTRIBUTION-RESULT/1",
                "github_issue_number": 600,
                "github_issue_url": "https://github.com/grandchallenge/MATHSOLVE/issues/600",
                "github_issue_title": "[GCL-CONTRIB] OPENMATH-2026 OM26-H2-WP01-IA-001 — independent WP01",
                "canonical_mutation_authorized": False,
                "dispatch_status": "READY_FOR_GITHUB_COMMENT",
                "operation_contract": ".gcl/operations/OM26-H2-WP01-IA-001/OPERATION.json",
            }
            (dispatch_dir / "OM26-H2-WP01-IA-001.json").write_text(json.dumps(dispatch), encoding="utf-8")
            operation = {
                "dispatch_id": "OM26-H2-WP01-IA-001",
                "assignment_id": "OM26-H2-WP01",
                "agent_ref": "INDEPENDENT-AGENT-002",
                "acceptable_dispositions": ["INDEPENDENT_SCORER_CONCORDANCE"],
            }
            (operation_dir / "OPERATION.json").write_text(json.dumps(operation), encoding="utf-8")

            event = {
                "issue": {
                    "number": 600,
                    "title": dispatch["github_issue_title"],
                    "body": issue_body + "\n",
                },
                "comment": {
                    "id": 700,
                    "body": H2_VALID,
                    "created_at": "2026-09-29T00:00:00Z",
                    "user": {"login": "external-agent"},
                },
            }
            meta = emit_intake(event, root, root / "out")
            self.assertEqual(meta["dispatch_id"], "OM26-H2-WP01-IA-001")

            invalid = json.loads(json.dumps(event))
            invalid["issue"]["body"] = issue_body + "\n\n"
            with self.assertRaises(IntakeError):
                emit_intake(invalid, root, root / "out2")

    def test_generic_dispatch_drives_assignment_disposition_and_output_path(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            base = root / "contributions/OPENMATH-2026/OM26-H2/WP01"
            dispatch_dir = base / "dispatches"
            dispatch_dir.mkdir(parents=True)
            operation_dir = root / ".gcl/operations/OM26-H2-WP01-IA-001"
            operation_dir.mkdir(parents=True)
            bootstrap = root / "handoffs/OPENMATH-2026/jobs/OM26-H2-WP01-IA-001.md"
            bootstrap.parent.mkdir(parents=True)

            issue_body = """GCL-CONTRIBUTION-DISPATCH/1
dispatch_id: OM26-H2-WP01-IA-001
agent_ref: INDEPENDENT-AGENT-002
assignment: OM26-H2-WP01"""
            bootstrap.write_text(issue_body + "\n", encoding="utf-8")

            dispatch = {
                "schema_version": "1.0.0",
                "record_type": "GCL_EXTERNAL_DISPATCH",
                "dispatch_id": "OM26-H2-WP01-IA-001",
                "campaign": "OPENMATH-2026",
                "hill": "OM26-H2",
                "assignment_id": "OM26-H2-WP01",
                "agent_ref": "INDEPENDENT-AGENT-002",
                "concurrency_mode": "independent_blind",
                "bootstrap_path": "handoffs/OPENMATH-2026/jobs/OM26-H2-WP01-IA-001.md",
                "bootstrap_blob_sha1": "a" * 40,
                "source_handoff_commit_sha": "b" * 40,
                "return_protocol": "GCL-CONTRIBUTION-RESULT/1",
                "github_issue_number": 600,
                "github_issue_url": "https://github.com/grandchallenge/MATHSOLVE/issues/600",
                "github_issue_title": "[GCL-CONTRIB] OPENMATH-2026 OM26-H2-WP01-IA-001 — independent WP01",
                "canonical_mutation_authorized": False,
                "dispatch_status": "READY_FOR_GITHUB_COMMENT",
                "operation_contract": ".gcl/operations/OM26-H2-WP01-IA-001/OPERATION.json",
            }
            (dispatch_dir / "OM26-H2-WP01-IA-001.json").write_text(json.dumps(dispatch), encoding="utf-8")
            operation = {
                "dispatch_id": "OM26-H2-WP01-IA-001",
                "assignment_id": "OM26-H2-WP01",
                "agent_ref": "INDEPENDENT-AGENT-002",
                "acceptable_dispositions": [
                    "INDEPENDENT_SCORER_CONCORDANCE",
                    "SOURCE_SAMPLE_DISCREPANCY",
                ],
            }
            (operation_dir / "OPERATION.json").write_text(json.dumps(operation), encoding="utf-8")

            event = {
                "issue": {
                    "number": 600,
                    "title": dispatch["github_issue_title"],
                    "body": issue_body,
                },
                "comment": {
                    "id": 700,
                    "body": H2_VALID,
                    "created_at": "2026-09-28T00:00:00Z",
                    "user": {"login": "external-agent"},
                },
            }
            out = root / "out"
            meta = emit_intake(event, root, out)
            self.assertEqual(
                meta["raw_repo_path"],
                "contributions/OPENMATH-2026/OM26-H2/WP01/raw/OM26-H2-WP01-IA-001/github-comment-700.md",
            )
            receipt = json.loads((out / "RECEIPT.json").read_text(encoding="utf-8"))
            self.assertEqual(receipt["assignment_id"], "OM26-H2-WP01")
            self.assertEqual(receipt["disposition_declared"], "INDEPENDENT_SCORER_CONCORDANCE")

            bad = json.loads(json.dumps(event))
            bad["comment"]["body"] = H2_VALID.replace(
                "INDEPENDENT_SCORER_CONCORDANCE", "SOURCE_SAMPLE_DISCREPANCY"
            )
            emit_intake(bad, root, root / "out2")

            invalid = json.loads(json.dumps(event))
            invalid["comment"]["body"] = H2_VALID.replace(
                "INDEPENDENT_SCORER_CONCORDANCE", "RANK23_SEARCH_SEED"
            )
            with self.assertRaises(IntakeError):
                emit_intake(invalid, root, root / "out3")


if __name__ == "__main__":
    unittest.main()
