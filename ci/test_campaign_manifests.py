from __future__ import annotations

import importlib.util
import json
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "validate_campaign_manifests", ROOT / "ci" / "validate_campaign_manifests.py"
)
module = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(module)


class CampaignManifestTests(unittest.TestCase):
    def setUp(self) -> None:
        self.source = ROOT / "campaign_manifests"

    def copied_registry(self) -> tuple[tempfile.TemporaryDirectory, Path]:
        handle = tempfile.TemporaryDirectory()
        self.addCleanup(handle.cleanup)
        target = Path(handle.name)
        for path in self.source.glob("*.json"):
            (target / path.name).write_text(path.read_text(encoding="utf-8"), encoding="utf-8")
        return handle, target

    def copied_current_cert_registry(self) -> tuple[tempfile.TemporaryDirectory, Path]:
        handle = tempfile.TemporaryDirectory()
        self.addCleanup(handle.cleanup)
        target = Path(handle.name) / "mathcert_current_routes.json"
        target.write_text(
            module.CURRENT_CERT_REGISTRY_PATH.read_text(encoding="utf-8"),
            encoding="utf-8",
        )
        return handle, target

    def test_current_registry_template_and_packets_pass(self) -> None:
        self.assertEqual(module.campaign_manifest_errors(), [])
        self.assertEqual(module.mathcert_handoff_errors(), [])
        self.assertEqual(module.handoff_packet_errors(), [])
        self.assertEqual(module.current_cert_route_errors(), [])

    def test_missing_active_campaign_fails(self) -> None:
        _, target = self.copied_registry()
        (target / "RH-001.json").unlink()
        errors = module.campaign_manifest_errors(target)
        self.assertTrue(any("RH-001" in error and "uncovered" in error for error in errors))

    def test_retrospective_manifest_requires_migration_debt(self) -> None:
        _, target = self.copied_registry()
        path = target / "PNP-001.json"
        data = json.loads(path.read_text(encoding="utf-8"))
        data["solve"]["migration_debt"] = []
        path.write_text(json.dumps(data), encoding="utf-8")
        errors = module.campaign_manifest_errors(target)
        self.assertTrue(any("retrospective coverage requires migration debt" in error for error in errors))

    def test_artifact_identity_drift_fails(self) -> None:
        _, target = self.copied_registry()
        path = target / "HC-001.json"
        data = json.loads(path.read_text(encoding="utf-8"))
        data["work_packages"][0]["artifacts"][0]["digest"] = "0" * 40
        path.write_text(json.dumps(data), encoding="utf-8")
        errors = module.campaign_manifest_errors(target)
        self.assertTrue(any("identity drift" in error for error in errors))

    def test_uc_readme_identity_cannot_regress(self) -> None:
        _, target = self.copied_registry()
        path = target / "UC-001.json"
        data = json.loads(path.read_text(encoding="utf-8"))
        data["work_packages"][0]["artifacts"][0]["digest"] = (
            "e4f4882666653fa1f0996aa7923e6290137fe2ee"
        )
        path.write_text(json.dumps(data), encoding="utf-8")
        errors = module.campaign_manifest_errors(target)
        self.assertTrue(any("identity drift" in error for error in errors))

    def test_repository_commit_cannot_substitute_for_artifact_digest(self) -> None:
        _, target = self.copied_registry()
        path = target / "BSD-001.json"
        data = json.loads(path.read_text(encoding="utf-8"))
        artifact = data["work_packages"][0]["artifacts"][0]
        artifact["digest"] = artifact["commit_sha"]
        path.write_text(json.dumps(data), encoding="utf-8")
        errors = module.campaign_manifest_errors(target)
        self.assertTrue(any("commit cannot substitute" in error for error in errors))

    def test_distinct_ledger_roles_cannot_share_one_path(self) -> None:
        _, target = self.copied_registry()
        path = target / "UC-001.json"
        data = json.loads(path.read_text(encoding="utf-8"))
        data["work_packages"][0]["ledgers"]["resource"] = dict(
            data["work_packages"][0]["ledgers"]["failed_route"]
        )
        data["work_packages"][0]["ledgers"]["resource"]["role"] = "resource_ledger"
        path.write_text(json.dumps(data), encoding="utf-8")
        errors = module.campaign_manifest_errors(target)
        self.assertTrue(any("distinct ledger roles share artifact path" in error for error in errors))

    def test_computational_package_requires_resource_and_failure_ledgers(self) -> None:
        _, target = self.copied_registry()
        path = target / "UC-001.json"
        data = json.loads(path.read_text(encoding="utf-8"))
        data["work_packages"][0]["ledgers"]["resource"] = None
        path.write_text(json.dumps(data), encoding="utf-8")
        errors = module.campaign_manifest_errors(target)
        self.assertTrue(any("requires resource ledger" in error for error in errors))

    def test_ready_route_cannot_pass_judgment(self) -> None:
        errors = module.provider_gate_errors("HC-001", "JUDGMENT")
        self.assertTrue(any("not an adjudicated" in error for error in errors))

    def test_qualified_uc_route_passes_integration_despite_ready_handoff(self) -> None:
        self.assertEqual(module.provider_gate_errors("UC-001", "INTEGRATION"), [])

    def test_qualified_ns_route_passes_judgment_despite_ready_handoff(self) -> None:
        self.assertEqual(module.provider_gate_errors("NS-CI-001", "JUDGMENT"), [])

    def test_qualified_rh_route_passes_integration_despite_pending_handoff(self) -> None:
        self.assertEqual(module.provider_gate_errors("RH-001", "INTEGRATION"), [])

    def test_qualification_does_not_imply_claim_promotion(self) -> None:
        errors = module.provider_gate_errors("RH-001", "CLAIM_PROMOTION")
        self.assertTrue(any("not promotion eligible" in error for error in errors))

    def test_uc_qualification_does_not_imply_claim_promotion(self) -> None:
        errors = module.provider_gate_errors("UC-001", "CLAIM_PROMOTION")
        self.assertTrue(any("not promotion eligible" in error for error in errors))

    def test_promotion_requires_positive_historical_certification(self) -> None:
        _, target = self.copied_registry()
        path = target / "HC-001.json"
        data = json.loads(path.read_text(encoding="utf-8"))
        data["promotion"] = {"eligible": True, "blockers": []}
        data["certification"]["handoff_state"] = "rejected"
        data["certification"]["handoff_packets"][0]["status"] = "rejected"
        path.write_text(json.dumps(data), encoding="utf-8")
        errors = module.campaign_manifest_errors(target)
        self.assertTrue(any("requires certified or qualified" in error for error in errors))

    def test_packet_status_mismatch_fails(self) -> None:
        _, target = self.copied_registry()
        path = target / "UC-001.json"
        data = json.loads(path.read_text(encoding="utf-8"))
        data["certification"]["handoff_state"] = "submitted"
        path.write_text(json.dumps(data), encoding="utf-8")
        errors = module.campaign_manifest_errors(target)
        self.assertTrue(any("aggregate handoff state" in error for error in errors))

    def test_historical_cert_contract_drift_fails(self) -> None:
        _, target = self.copied_registry()
        path = target / "NS-CI-001.json"
        data = json.loads(path.read_text(encoding="utf-8"))
        data["certification"]["contract"]["digest"] = "0" * 40
        path.write_text(json.dumps(data), encoding="utf-8")
        errors = module.campaign_manifest_errors(target)
        self.assertTrue(any("contract identity" in error or "const" in error for error in errors))

    def test_current_cert_contract_drift_fails(self) -> None:
        _, path = self.copied_current_cert_registry()
        data = json.loads(path.read_text(encoding="utf-8"))
        data["authority"]["digest"] = "0" * 40
        path.write_text(json.dumps(data), encoding="utf-8")
        errors = module.current_cert_route_errors(registry_path=path)
        self.assertTrue(any("const" in error or "authority" in error for error in errors))

    def test_qualified_route_requires_exact_output(self) -> None:
        _, path = self.copied_current_cert_registry()
        data = json.loads(path.read_text(encoding="utf-8"))
        data["campaigns"]["RH-001"]["cert_output"] = None
        path.write_text(json.dumps(data), encoding="utf-8")
        errors = module.current_cert_route_errors(registry_path=path)
        self.assertTrue(any("Cert output" in error or "not valid" in error for error in errors))

    def test_uc_qualified_route_requires_exact_output(self) -> None:
        _, path = self.copied_current_cert_registry()
        data = json.loads(path.read_text(encoding="utf-8"))
        data["campaigns"]["UC-001"]["cert_output"]["digest"] = "0" * 40
        path.write_text(json.dumps(data), encoding="utf-8")
        errors = module.current_cert_route_errors(registry_path=path)
        self.assertTrue(any("exact Cert output identity drift" in error for error in errors))

    def test_uc_qualification_scope_cannot_drift(self) -> None:
        _, path = self.copied_current_cert_registry()
        data = json.loads(path.read_text(encoding="utf-8"))
        data["campaigns"]["UC-001"]["qualification_scope"] = "qualified_interface_only"
        path.write_text(json.dumps(data), encoding="utf-8")
        errors = module.current_cert_route_errors(registry_path=path)
        self.assertTrue(any("qualification scope drift" in error for error in errors))

    def test_route_state_cannot_be_replaced_by_handoff_state(self) -> None:
        _, path = self.copied_current_cert_registry()
        data = json.loads(path.read_text(encoding="utf-8"))
        data["campaigns"]["NS-CI-001"]["route_state"] = "ready"
        data["campaigns"]["NS-CI-001"]["cert_output"] = None
        data["campaigns"]["NS-CI-001"]["qualification_scope"] = None
        path.write_text(json.dumps(data), encoding="utf-8")
        errors = module.current_cert_route_errors(registry_path=path)
        self.assertTrue(any("route_state drift" in error for error in errors))

    def test_uc_route_state_cannot_regress_to_ready_handoff(self) -> None:
        _, path = self.copied_current_cert_registry()
        data = json.loads(path.read_text(encoding="utf-8"))
        data["campaigns"]["UC-001"]["route_state"] = "ready"
        data["campaigns"]["UC-001"]["cert_output"] = None
        data["campaigns"]["UC-001"]["qualification_scope"] = None
        path.write_text(json.dumps(data), encoding="utf-8")
        errors = module.current_cert_route_errors(registry_path=path)
        self.assertTrue(any("route_state drift" in error for error in errors))

    def test_uc_qualification_cannot_inflate_to_target_proof(self) -> None:
        _, path = self.copied_current_cert_registry()
        data = json.loads(path.read_text(encoding="utf-8"))
        data["campaigns"]["UC-001"]["mathematical_target_proved"] = True
        path.write_text(json.dumps(data), encoding="utf-8")
        errors = module.current_cert_route_errors(registry_path=path)
        self.assertTrue(any("target proof" in error or "False was expected" in error for error in errors))

    def test_stale_rh_no_replay_assertion_fails(self) -> None:
        _, path = self.copied_current_cert_registry()
        data = json.loads(path.read_text(encoding="utf-8"))
        data["campaigns"]["RH-001"]["current_promotion_blockers"].append(
            "MATHCERT has not independently replayed the target."
        )
        path.write_text(json.dumps(data), encoding="utf-8")
        errors = module.current_cert_route_errors(registry_path=path)
        self.assertTrue(any("superseded no-replay" in error for error in errors))

    def test_pending_packet_requires_blocker(self) -> None:
        handle = tempfile.TemporaryDirectory()
        self.addCleanup(handle.cleanup)
        target = Path(handle.name)
        for path in (ROOT / "cert_handoffs").glob("*.json"):
            data = json.loads(path.read_text(encoding="utf-8"))
            if data["campaign_id"] == "BSD-001":
                data["blockers"] = []
            (target / path.name).write_text(json.dumps(data), encoding="utf-8")
        errors = module.handoff_packet_errors(target)
        self.assertTrue(any("pending packet must identify blockers" in error or "non-empty" in error for error in errors))


if __name__ == "__main__":
    unittest.main()
