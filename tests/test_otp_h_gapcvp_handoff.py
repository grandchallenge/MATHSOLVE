from __future__ import annotations

import copy
import importlib.util
import unittest
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
SPEC=importlib.util.spec_from_file_location("validate_otp_h_gapcvp_handoff",ROOT/"ci/validate_otp_h_gapcvp_handoff.py")
mod=importlib.util.module_from_spec(SPEC)
assert SPEC and SPEC.loader
SPEC.loader.exec_module(mod)

class GapCVPHandoffTests(unittest.TestCase):
    def setUp(self): self.record=mod.load(mod.RECORD)
    def reject(self,fn):
        r=copy.deepcopy(self.record); fn(r); self.assertTrue(mod.validation_errors(r),r)
    def test_canonical(self): self.assertEqual(mod.validation_errors(self.record),[])
    def test_target_substitution(self): self.reject(lambda r:r["target_scope"]["lean_theorems"].__setitem__(0,"Other.Target"))
    def test_promise_omission(self): self.reject(lambda r:r["target_scope"]["promise_interfaces"].pop())
    def test_factor_drift(self): self.reject(lambda r:r["target_scope"]["gap_factors"].__setitem__(0,"400"))
    def test_classification_inflation(self): self.reject(lambda r:r["target_scope"]["classifications"].__setitem__(0,"source_exact_interface"))
    def test_semantic_blob_substitution(self): self.reject(lambda r:r["authority"]["semantic_record"].__setitem__("digest","0"*40))
    def test_replay_substitution(self): self.reject(lambda r:r["authority"]["replay"].__setitem__("job_id",1))
    def test_axiom_widening(self): self.reject(lambda r:r["authority"]["replay"]["permitted_axioms"].append("sorryAx"))
    def test_vacuity(self): self.reject(lambda r:r["nonvacuity"].__setitem__("no_witness_count",0))
    def test_route_registration(self): self.reject(lambda r:r["requested_adjudication"].__setitem__("current_route_state","registered"))
    def test_cert_output(self): self.reject(lambda r:r["requested_adjudication"].__setitem__("cert_output",{"id":"x"}))
    def test_historical_registry_mutability(self): self.reject(lambda r:r["route_controls"].__setitem__("historical_six_packet_registry_mutable",True))
    def test_aggregate(self): self.reject(lambda r:r["route_controls"].__setitem__("may_create_aggregate_handoff",True))
    def test_proof_promotion(self): self.reject(lambda r:r["route_controls"].__setitem__("may_claim_mathematical_proof",True))

if __name__=="__main__": unittest.main()
