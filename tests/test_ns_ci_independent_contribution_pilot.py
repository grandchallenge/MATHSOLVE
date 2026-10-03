from __future__ import annotations

import json
import shutil
import tempfile
import unittest
from pathlib import Path

from ci.validate_ns_ci_independent_contribution_pilot import ROOT, validate


RELATIVE_BASE = Path("contributions/NS-CI-001/C2_MIX_DIRECTION_COMPRESSION_LEDGER_CHARGE")
HANDOFF = Path("handoffs/NS-CI-001/C2_MIX_DIRECTION_COMPRESSION_LEDGER_CHARGE_ZERO_CONTEXT.md")
WORKFLOW = Path(".github/workflows/ns-ci-independent-contribution-intake.yml")
INTAKE = Path("ci/ns_ci_github_contribution_intake.py")


class IndependentContributionPilotTest(unittest.TestCase):
    def make_root(self) -> Path:
        temp = Path(tempfile.mkdtemp())
        self.addCleanup(shutil.rmtree, temp, ignore_errors=True)
        for rel in (RELATIVE_BASE, HANDOFF, WORKFLOW, INTAKE):
            src = ROOT / rel
            dst = temp / rel
            dst.parent.mkdir(parents=True, exist_ok=True)
            if src.is_dir():
                shutil.copytree(src, dst)
            else:
                shutil.copy2(src, dst)
        return temp

    def test_current_surface_validates(self) -> None:
        self.assertEqual(validate(ROOT), [])

    def test_superseded_icr_template_is_rejected(self) -> None:
        root = self.make_root()
        path = root / RELATIVE_BASE / "templates" / "INDEPENDENT_CONTRIBUTION_RECORD.md"
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text("old free-form intake", encoding="utf-8")
        self.assertTrue(any("superseded free-form" in item for item in validate(root)))

    def test_dispatch_attachment_permission_is_rejected(self) -> None:
        root = self.make_root()
        path = root / RELATIVE_BASE / "dispatches" / "NSCI-C2-A-BLIND-001.json"
        payload = json.loads(path.read_text(encoding="utf-8"))
        payload["attachments_allowed"] = True
        path.write_text(json.dumps(payload), encoding="utf-8")
        self.assertTrue(any("attachments_allowed must be false" in item for item in validate(root)))

    def test_bootstrap_digest_mismatch_is_rejected(self) -> None:
        root = self.make_root()
        path = root / RELATIVE_BASE / "dispatch_bootstraps" / "NSCI-C2-A-BLIND-001.md"
        path.write_text(path.read_text(encoding="utf-8") + "\nmutation\n", encoding="utf-8")
        self.assertTrue(any("bootstrap digest mismatch" in item for item in validate(root)))

    def test_ready_dispatch_requires_issue_binding(self) -> None:
        root = self.make_root()
        path = root / RELATIVE_BASE / "dispatches" / "NSCI-C2-A-BLIND-001.json"
        payload = json.loads(path.read_text(encoding="utf-8"))
        payload["dispatch_status"] = "READY_FOR_GITHUB_COMMENT"
        payload["github_issue_number"] = None
        payload["github_issue_url"] = None
        path.write_text(json.dumps(payload), encoding="utf-8")
        errors = validate(root)
        self.assertTrue(any("ready dispatch lacks issue number" in item for item in errors))

    def test_comment_level_concurrency_is_rejected(self) -> None:
        root = self.make_root()
        path = root / WORKFLOW
        text = path.read_text(encoding="utf-8").replace(
            "group: ns-ci-contribution-intake-${{ github.event.issue.number }}",
            "group: ns-ci-contribution-intake-${{ github.event.comment.id }}",
        )
        path.write_text(text, encoding="utf-8")
        errors = validate(root)
        self.assertTrue(any("forbidden authority surface" in item or "missing control" in item for item in errors))

    def test_local_pr_creation_authority_is_rejected(self) -> None:
        root = self.make_root()
        path = root / WORKFLOW
        path.write_text(
            path.read_text(encoding="utf-8")
            + "\n# gh pr create\n# pull-requests: write\n",
            encoding="utf-8",
        )
        errors = validate(root)
        self.assertTrue(any("forbidden authority surface" in item for item in errors))

    def test_missing_release_trust_handoff_marker_is_rejected(self) -> None:
        root = self.make_root()
        path = root / WORKFLOW
        path.write_text(
            path.read_text(encoding="utf-8").replace(
                "The bounded Release Trust PR controller owns PR creation",
                "PR ownership unspecified",
            ),
            encoding="utf-8",
        )
        self.assertTrue(any("missing control" in item for item in validate(root)))

    def test_workflow_auto_merge_surface_is_rejected(self) -> None:
        root = self.make_root()
        path = root / WORKFLOW
        path.write_text(path.read_text(encoding="utf-8") + "\n# gh pr merge\n", encoding="utf-8")
        self.assertTrue(any("forbidden authority surface" in item for item in validate(root)))


if __name__ == "__main__":
    unittest.main()
