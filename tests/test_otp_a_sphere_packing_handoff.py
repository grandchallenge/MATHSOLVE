from __future__ import annotations

import copy
import importlib.util
import unittest
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
SPEC=importlib.util.spec_from_file_location("validate_otp_a_sphere_packing_handoff",ROOT/"ci/validate_otp_a_sphere_packing_handoff.py")
mod=importlib.util.module_from_spec(SPEC)
assert SPEC and SPEC.loader
SPEC.loader.exec_module(mod)

class SpherePackingHandoffTests(unittest.TestCase):
    def setUp(self): self.record=mod.load(mod.RECORD)
    def reject(self,fn):
        r=copy.deepcopy(self.record); fn(r); self.assertTrue(mod.validation_errors(r),r)
    def test_canonical(self): self.assertEqual(mod.validation_errors(self.record),[])
    def test_target_substitution(self): self.reject(lambda r:r["target_scope"]["lean_theorems"].__setitem__(0,"Other.Target"))
    def test_classification_inflation(self): self.reject(lambda r:r["target_scope"]["classifications"].__setitem__(3,"verbatim_source_theorem"))
    def test_composite_blob_substitution(self): self.reject(lambda r:r["authority"]["composite_semantic_record"].__setitem__("digest","0"*40))
    def test_bridge_blob_substitution(self): self.reject(lambda r:r["authority"]["bridge_semantic_record"].__setitem__("digest","0"*40))
    def test_formal_root_substitution(self): self.reject(lambda r:r["authority"]["official_subject"].__setitem__("commit","0"*40))
    def test_replay_substitution(self): self.reject(lambda r:r["authority"]["replay"].__setitem__("job_id",1))
    def test_axiom_widening(self): self.reject(lambda r:r["authority"]["replay"]["permitted_axioms"].append("sorryAx"))
    def test_vacuity_loss(self): self.reject(lambda r:r["nonvacuity"].__setitem__("state","unknown"))
    def test_route_registration(self): self.reject(lambda r:r["requested_adjudication"].__setitem__("current_route_state","registered"))
    def test_decimal_source_inflation(self): self.reject(lambda r:r["route_controls"].__setitem__("decimal_precision_source_authored",True))
    def test_historical_registry_mutability(self): self.reject(lambda r:r["route_controls"].__setitem__("historical_six_packet_registry_mutable",True))
    def test_aggregate(self): self.reject(lambda r:r["route_controls"].__setitem__("may_create_aggregate_handoff",True))
    def test_proof_promotion(self): self.reject(lambda r:r["route_controls"].__setitem__("may_claim_mathematical_proof",True))

if __name__=="__main__": unittest.main()
