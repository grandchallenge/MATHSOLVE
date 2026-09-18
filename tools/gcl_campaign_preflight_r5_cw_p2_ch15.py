#!/usr/bin/env python3
from __future__ import annotations
import hashlib,json,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
def fail(x): raise SystemExit("GCL BSD-R5-CW-P2-CH15 preflight: FAIL: "+x)
def load(p):
 q=ROOT/p
 if not q.exists(): fail("missing "+p)
 return json.loads(q.read_text())
def blob(p):
 d=(ROOT/p).read_bytes()
 return hashlib.sha1(f"blob {len(d)}\0".encode()+d).hexdigest()
def main():
 if len(sys.argv)!=3 or sys.argv[1:]!=["BSD-001","BSD-R5-CW-P2-CH15"]: fail("arguments")
 s=load(".gcl/campaigns/BSD-001/CAMPAIGN_STATE.json")
 o=load(".gcl/operations/BSD-R5-CW-P2-CH15/OPERATION.json")
 f=load(".gcl/admission/BSD-R5-CW-P2-CH15/FREEZE.json")
 if s["current_operation"]!=o["operation"]: fail("operation")
 if s["current_frontier"]["id"]!=o["objective"]["frontier"]: fail("frontier")
 if s["candidate_disposition"]["type"]!="BLOCKED" or o["candidate_disposition"]!="BLOCKED": fail("disposition")
 if s["candidate_disposition"]["blocked_on"]!=o["blocked_on"]: fail("blocked")
 if not s["protected_inputs"]["math_base"].endswith(o["protected_base"]): fail("base")
 if not s["protected_inputs"]["provider"].endswith(o["provider_anchor"]): fail("provider")
 if not s["authority"]["constitution"].endswith(o["constitutional_anchor"]): fail("constitution")
 if f["protected_base"]!=o["protected_base"] or f["provider_anchor"]!=o["provider_anchor"]: fail("freeze anchors")
 ledger=(ROOT/o["validation"]["claim_ledger"]).read_text()
 combined="\n".join([(ROOT/o["validation"][k]).read_text() for k in ("claim_ledger","theorem","frontier_record")])
 for t in o["validation"]["required_tokens"]:
  if t not in combined: fail("missing "+t)
 for t in o["validation"]["forbidden_tokens"]:
  if t in ledger: fail("forbidden "+t)
 for k,v in o["claim_firewall"].items():
  if f"{k}: {'true' if v else 'false'}" not in ledger: fail("firewall "+k)
 routing=load(o["validation"]["routing_registry"])
 if o["validation"]["workflow"] not in {x.get("path") for x in routing["workflows"]}: fail("routing")
 if set(f["artifacts"])!=set(o["governed_artifacts"]): fail("freeze set")
 for p in o["governed_artifacts"]:
  if blob(p)!=f["artifacts"][p]: fail("freeze "+p)
 print(json.dumps({"status":"PASS","operation":o["operation"],"candidate_disposition":"BLOCKED","blocked_on":o["blocked_on"],"r5_res":False,"r5_prim":False,"bsd_r2_a1":False,"mathcert_certified":False},sort_keys=True))
if __name__=="__main__": main()
