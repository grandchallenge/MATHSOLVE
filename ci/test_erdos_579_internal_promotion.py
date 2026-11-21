import json,sys,tempfile,unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).parent))
import validate_vgse_activation as v
class InternalPromotionTests(unittest.TestCase):
 def test_exact_bounded_internal_decision(self):
  self.assertEqual([],v.erdos_internal_promotion_errors())
  self.assertEqual([],v.merged_provider_gate_errors(v.ERDOS_ID,"CLAIM_PROMOTION"))
  r=v.load_json(v.ERDOS_INTERNAL_PROMOTION_PATH)
  self.assertTrue(r["internal_claim_promotion_eligible"])
  self.assertFalse(r["external_publication_authorized"])
 def tampered(self,key,value):
  r=v.load_json(v.ERDOS_INTERNAL_PROMOTION_PATH);r[key]=value
  with tempfile.TemporaryDirectory() as tmp:
   p=Path(tmp)/"bad.json";p.write_text(json.dumps(r));return v.erdos_internal_promotion_errors(p)
 def test_publication_inflation_denied(self):
  self.assertTrue(any("external_publication_authorized" in e for e in self.tampered("external_publication_authorized",True)))
 def test_novelty_inflation_denied(self):
  self.assertTrue(any("novelty_or_priority_claimed" in e for e in self.tampered("novelty_or_priority_claimed",True)))
 def test_independent_evidence_drift_denied(self):
  r=v.load_json(v.ERDOS_INTERNAL_PROMOTION_PATH);r["evidence"]["independent_kernel_replay_decl_count"]=0
  with tempfile.TemporaryDirectory() as tmp:
   p=Path(tmp)/"bad.json";p.write_text(json.dumps(r))
   self.assertTrue(any("source/axiom/replay identity drift" in e for e in v.erdos_internal_promotion_errors(p)))
