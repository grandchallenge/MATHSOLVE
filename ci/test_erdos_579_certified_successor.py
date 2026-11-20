import copy,json,sys,tempfile,unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).parent))
import validate_vgse_activation as v
class CertifiedSuccessorTests(unittest.TestCase):
 def test_exact_live_certified(self):
  self.assertEqual([],v.erdos_certified_successor_errors())
  self.assertEqual("certified",v.merged_current_route_state(v.ERDOS_ID))
 def mutate(self,fn):
  d=v.load_json(v.ERDOS_CERTIFIED_SUCCESSOR_PATH);fn(d)
  with tempfile.TemporaryDirectory() as tmp:
   p=Path(tmp)/"bad.json";p.write_text(json.dumps(d));return v.erdos_certified_successor_errors(p)
 def test_forged_proof_identity_rejected(self):
  self.assertTrue(any("certificate exact output drift" in e for e in self.mutate(lambda d:d["certificate_output"].__setitem__("digest","0"*40))))
 def test_unapproved_promotion_rejected(self):
  self.assertTrue(any("claim_promotion_eligible drift" in e for e in self.mutate(lambda d:d.__setitem__("claim_promotion_eligible",True))))
