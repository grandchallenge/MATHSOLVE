"""Hostile source-link tests: synthetic fixtures test rejection, not positive admission."""
from __future__ import annotations

import copy
import hashlib
import importlib.util
import json
import subprocess
import tempfile
import unittest
from pathlib import Path

MODULE = Path(__file__).resolve().parents[1] / "ci" / "solve_specialist_source_preflight.py"
spec = importlib.util.spec_from_file_location("source_preflight", MODULE)
m = importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)


class SourcePreflightTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        subprocess.run(["git", "init", "-q", str(self.root)], check=True)
        subprocess.run(["git", "-C", str(self.root), "config", "user.name", "Test"], check=True)
        subprocess.run(["git", "-C", str(self.root), "config", "user.email", "test@example.invalid"], check=True)
        self.dispatch = "DEMO-WP01-IA-001"
        prefix = f"contributions/DEMO/{self.dispatch}"
        self.raw = (prefix + "/RAW.md", b"bounded independently returned result\n")
        digest = hashlib.sha256(self.raw[1]).hexdigest()
        self.effects = {k: False for k in m.EFFECTS}
        capture = dict(record_type=m.KINDS[0], dispatch_id=self.dispatch, result_ref="issue:42#comment:1",
                       result_sha256=digest, captured_result_path=self.raw[0],
                       authenticated_intake_provenance={"actor": "test-fixture-only"})
        self.write(self.raw[0], self.raw[1])
        self.binding = dict(schema_version="1.0.0", dispatch_id=self.dispatch,
                            result_ref="issue:42#comment:1", result_sha256=digest,
                            claim_effects=self.effects)
        self.add_record("capture", capture)
        evidence = dict(record_type="GCL_SOLVE_ACTUAL_REPLAY_OUTPUT",
                        execution=dict(dispatch_id=self.dispatch, raw_sha256=digest,
                                       replay_pass=True, specialist_positive_receipt=False,
                                       mathematical_certification=False))
        evidence_path = f"contributions/DEMO/{self.dispatch}/reproducibility.json"
        proof_data = (json.dumps(evidence, sort_keys=True) + "\n").encode()
        self.write(evidence_path, proof_data)
        proof_sha = m.blob_sha(proof_data)
        replay = dict(record_type=m.KINDS[1], dispatch_id=self.dispatch, result_ref="issue:42#comment:1",
                      input_result_sha256=digest, capture_blob_sha=self.binding["capture"]["blob_sha"],
                      replay_pass=True, reproducibility_artifact=evidence_path, reproducibility_blob_sha=proof_sha)
        self.add_record("replay", replay)
        adjud = dict(record_type=m.KINDS[2], dispatch_id=self.dispatch, result_ref="issue:42#comment:1",
                     replay_blob_sha=self.binding["replay"]["blob_sha"], adjudication_id="DEMO-ADJ-001",
                     adjudication_disposition="REPLAYED_AND_ADJUDICATED", claim_effects=self.effects)
        self.add_record("adjudication", adjud)
        subprocess.run(["git", "-C", str(self.root), "add", "."], check=True)
        subprocess.run(["git", "-C", str(self.root), "commit", "-qm", "Synthetic negative-test fixture"], check=True)
        self.revision = subprocess.check_output(
            ["git", "-C", str(self.root), "rev-parse", "HEAD"], text=True).strip()

    def write(self, path, data):
        target = self.root / path
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(data)

    def add_record(self, kind, obj):
        path = f"contributions/DEMO/{self.dispatch}/{kind}.json"
        payload = (json.dumps(obj, sort_keys=True) + "\n").encode()
        self.write(path, payload)
        self.binding[kind] = {"path": path, "blob_sha": m.blob_sha(payload)}

    def check(self, binding=None):
        return m.preflight(self.root, self.revision, binding or self.binding)

    def test_linkage_pass_only_never_certifies(self):
        receipt = self.check()
        self.assertEqual(receipt["state"], "SOURCE_LINK_PREFLIGHT_PASS_ONLY")
        self.assertFalse(receipt["specialist_positive_receipt"])

    def test_wrong_dispatch(self):
        bad = copy.deepcopy(self.binding)
        bad["dispatch_id"] = "OTHER-IA-001"
        with self.assertRaises(m.EvidenceError):
            self.check(bad)

    def test_tampered_result_digest(self):
        bad = copy.deepcopy(self.binding)
        bad["result_sha256"] = "f" * 64
        with self.assertRaises(m.EvidenceError):
            self.check(bad)

    def test_changed_replay_blob(self):
        bad = copy.deepcopy(self.binding)
        bad["replay"]["blob_sha"] = "0" * 40
        with self.assertRaises(m.EvidenceError):
            self.check(bad)

    def test_false_promotion(self):
        bad = copy.deepcopy(self.binding)
        bad["claim_effects"]["certification_effect"] = True
        with self.assertRaises(m.EvidenceError):
            self.check(bad)

    def test_malformed_protected_pointer(self):
        bad = copy.deepcopy(self.binding)
        bad["capture"]["path"] = "../outside.json"
        with self.assertRaises(m.EvidenceError):
            self.check(bad)


    def test_missing_reproducibility_lock(self):
        bad = copy.deepcopy(self.binding)
        bad["replay"]["blob_sha"] = "f" * 40
        with self.assertRaises(m.EvidenceError):
            self.check(bad)

    def test_unprotected_revision(self):
        with self.assertRaises(m.EvidenceError):
            m.preflight(self.root, "working-tree", self.binding)


if __name__ == "__main__":
    unittest.main()
