from __future__ import annotations

import hashlib
import json
import shutil
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from ci import ns_ci_github_contribution_intake as intake
from ci.validate_queue_intake_bindings import validate as validate_coverage

REPO = Path(__file__).resolve().parents[1]
DISPATCH = "ERDOS-593-R2-IA-001"
ISSUE_BODY = "Immutable protected issue text for offline intake contract test."
RESULT = """GCL-CONTRIBUTION-RESULT/1
dispatch_id: ERDOS-593-R2-IA-001
agent_ref: INDEPENDENT-AGENT-ERDOS-593-R2
assignment: ERDOS-593-R2
disposition: PROVED_REDUCTION
context_class: ZERO_CONTEXT
external_sources: PRIMARY_SOURCES_REQUIRED
timebox_observed: YES

## Strongest exact statement
This is a bounded source-conditional mathematical statement.

## Derivation
The asserted implication follows from a stated theorem.

## Assumptions beyond bootstrap
Primary theorem dependency remains to be checked.

## Verification / falsification hooks
Replay the indicated finite step independently.

## Claim boundary
No mathematical certification or source independence is inferred.

## Next residual
Independently verify the cited source condition.
"""


class NewGenerationIntakeTest(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        for rel in (
            ".gcl/worker_queue/JOBS.json",
            ".gcl/worker_queue/INTAKE_BINDINGS.json",
            "contributions/ERDOS-OPEN-001/SUCCESSOR_002/dispatches/ERDOS-593-R2-IA-001.json",
            "handoffs/GCL-WORKER-QUEUE/launch/2026-10-08/ERDOS-593-R2-IA-001.md",
        ):
            dest = self.root / rel
            dest.parent.mkdir(parents=True, exist_ok=True)
            dest.write_bytes((REPO / rel).read_bytes())

        manifest_path = self.root / ".gcl/worker_queue/INTAKE_BINDINGS.json"
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        for binding in manifest["bindings"]:
            if binding["dispatch_id"] == DISPATCH:
                binding["issue_body_sha256"] = hashlib.sha256(ISSUE_BODY.encode()).hexdigest()
        manifest_path.write_text(json.dumps(manifest), encoding="utf-8")
        self.dispatch = json.loads(
            (self.root / "contributions/ERDOS-OPEN-001/SUCCESSOR_002/dispatches/ERDOS-593-R2-IA-001.json").read_text(encoding="utf-8")
        )

    def event(self, *, body: str=RESULT, actor: str="reviewer", issue_body: str=ISSUE_BODY):
        return {
            "issue": {
                "number":1008,
                "title":self.dispatch["github_issue_title"],
                "body":issue_body,
                "html_url":self.dispatch["github_issue_url"],
            },
            "comment": {
                "id":900,
                "body":body,
                "user":{"login":actor},
                "created_at":"2026-10-09T01:00:00Z",
            },
        }

    def validate(self, event=None, reservation=None):
        if event is None:
            event=self.event()
        if reservation is None:
            reservation={"worker":"reviewer"}
        with patch.object(intake,"active_reservation",return_value=reservation):
            return intake.validate_event(event,self.root,comments=[{"body":"reservation-marker"}])

    def test_protected_queue_profile_resolves_without_legacy_bootstrap(self):
        p=intake.profile_for_dispatch(DISPATCH,self.root)
        self.assertTrue(p.queue_binding)
        self.assertEqual(p.campaign,"ERDOS-OPEN")
        self.assertIn("PROVED_REDUCTION",p.dispositions)
        self.assertEqual(intake.parse_result_comment(RESULT,self.root)["preamble"]["dispatch_id"],DISPATCH)

    def test_new_receipt_has_pinned_task_and_issue_evidence(self):
        event=self.event()
        with patch.object(intake,"active_reservation",return_value={"worker":"reviewer"}):
            meta=intake.emit_intake(event,self.root,self.root/"receipt-output",comments=[{"body":"reservation-marker"}])
        receipt=json.loads((self.root/"receipt-output/RECEIPT.json").read_text(encoding="utf-8"))
        self.assertEqual(receipt["task_commit"],self.dispatch["task_commit"])
        self.assertEqual(receipt["intake_binding_kind"],"PROTECTED_QUEUE_TASK_AND_ISSUE_DIGEST")
        self.assertEqual(receipt["worker_reservation_owner"],"reviewer")
        self.assertEqual(meta["dispatch_id"],DISPATCH)
        self.assertNotIn("bootstrap_path",receipt)
        self.assertFalse(receipt["certification_effect"])

    def test_wrong_issue_bytes_fail_closed(self):
        with self.assertRaisesRegex(intake.IntakeError,"issue-body digest"):
            self.validate(self.event(issue_body=ISSUE_BODY+" tampered"))

    def test_wrong_task_bytes_fail_closed(self):
        p=self.root/self.dispatch["task_path"]
        p.write_text("changed protected task",encoding="utf-8")
        with self.assertRaisesRegex(intake.IntakeError,"immutable queue task"):
            self.validate()

    def test_wrong_worker_fails_closed(self):
        with self.assertRaisesRegex(intake.IntakeError,"does not match active worker reservation"):
            self.validate(self.event(actor="impostor"))

    def test_wrong_agent_ref_fails_closed(self):
        bad=RESULT.replace("INDEPENDENT-AGENT-ERDOS-593-R2","OTHER")
        with self.assertRaisesRegex(intake.IntakeError,"agent_ref"):
            self.validate(self.event(body=bad))

    def test_wrong_issue_number_fails_closed(self):
        e=self.event()
        e["issue"]["number"]=777
        with self.assertRaisesRegex(intake.IntakeError,"issue not bound"):
            self.validate(e)

    def test_unapproved_external_sources_fail_closed(self):
        bad=RESULT.replace("PRIMARY_SOURCES_REQUIRED","ADDITIONAL_PUBLIC_SOURCES")
        with self.assertRaisesRegex(intake.IntakeError,"external_sources is not approved"):
            self.validate(self.event(body=bad))

    def test_narrative_only_guard_remains(self):
        bad=RESULT.replace("Replay the indicated finite step", "See https://example.org and replay the indicated finite step")
        with self.assertRaisesRegex(intake.IntakeError,"forbidden content"):
            self.validate(self.event(body=bad))

    def test_non_registered_new_queue_id_rejected(self):
        with self.assertRaisesRegex(intake.IntakeError,"unregistered form"):
            intake.profile_for_dispatch("ERDOS-593-R99-IA-001",self.root)

    def test_missing_manifest_coverage_rejected(self):
        manifest_path=self.root/".gcl/worker_queue/INTAKE_BINDINGS.json"
        m=json.loads(manifest_path.read_text(encoding="utf-8"))
        m["bindings"]=[b for b in m["bindings"] if b["dispatch_id"] != DISPATCH]
        manifest_path.write_text(json.dumps(m),encoding="utf-8")
        errors=validate_coverage(self.root)
        self.assertTrue(any("lacks intake binding" in e for e in errors))


if __name__=="__main__":
    unittest.main()
