"""Positive and hostile replay of the serialized eight-slot Editorial controller."""
import json,unittest
from datetime import datetime,timezone,timedelta
from gcl_editorial_active_capacity import choose,ledger,parse,Denied,MAX_ACTIVE,PREFIX,HUB,REPO
NOW=datetime(2026,10,21,7,0,tzinfo=timezone.utc)
ATLAS="grandchallenge/ADAPTIVE-INTELLIGENCE-ATLAS"
PROGRAMME="grandchallenge/MATH-PROGRAMME"
def body(num,run,op="START",repo=ATLAS):
    text=f"EDITORIAL-{op}/1\nrepository: {repo}\nissue: {num}\nrun_id: {run}"
    if op=="START":text+="\nsource_head: "+"a"*40
    return text+"\n"
def source(num):
    return {"number":num,"state":"open","title":"Atlas chapter acceptance specialist reviewer",
        "labels":[{"name":v} for v in ("gcl-job","gcl-state:available","gcl-pickup:direct-editorial","gcl-role:verify")]}
def event(n,b,actor="agent"):
    return {"issue":{"number":HUB},"comment":{"id":n,"body":b,"user":{"login":actor,"type":"User"}}}
class Capacity(unittest.TestCase):
    def setUp(self):
        self.history=[];self.next=100
    def step(self,issue,op="START",actor="agent",repo=ATLAS,target=None,run=None,now=NOW):
        self.next+=1;rid=run or f"{issue:032x}";b=body(issue,rid,op,repo)
        e=event(self.next,b,actor);self.history.append(e["comment"])
        d=choose(e,self.history,now,source(issue) if target is None else target)
        if d is not None:
            self.next+=1;self.history.append({"id":self.next,"body":PREFIX+json.dumps(d),
                "user":{"login":"github-actions[bot]","type":"Bot"}})
        return d
    def test_fill_eight_and_reject_ninth(self):
        self.assertEqual(MAX_ACTIVE,8)
        for i in range(1,9):self.assertEqual(self.step(i)["outcome"],"GRANTED")
        self.assertEqual(len(ledger(self.history,NOW)[1]),8)
        self.assertEqual(self.step(9)["outcome"],"DENIED")
        self.assertEqual(len(ledger(self.history,NOW)[1]),8)
    def test_release_frees_exactly_one(self):
        for i in range(1,9):self.step(i)
        self.assertEqual(self.step(1,"END",actor="impostor")["outcome"],"DENIED")
        self.assertEqual(self.step(1,"END")["outcome"],"ENDED")
        self.assertEqual(self.step(9)["outcome"],"GRANTED")
        self.assertEqual(len(ledger(self.history,NOW)[1]),8)
    def test_expiry_does_not_hold_capacity(self):
        for i in range(1,9):self.step(i)
        self.assertEqual(len(ledger(self.history,NOW+timedelta(hours=5))[1]),0)
        self.assertEqual(self.step(9,now=NOW+timedelta(hours=5))["outcome"],"GRANTED")
    def test_duplicate_issue_denied(self):
        self.step(11)
        self.assertEqual(self.step(11,run="f"*32,actor="other")["outcome"],"DENIED")
    def test_wrong_class_denied(self):
        title="ERDOS-041-R41-A — fourth-order overlap propagation or counterexample"
        t=source(2790);t["title"]=title;t["number"]=2790
        t["labels"]+=[{"name":"gcl-role:constructive"},{"name":"gcl-collab:cooperative"}]
        self.assertEqual(self.step(2790,repo=PROGRAMME,target=t)["outcome"],"DENIED")
    def test_closed_or_returned_denied(self):
        t=source(30);t["state"]="closed"
        self.assertEqual(self.step(30,target=t)["outcome"],"DENIED")
        t=source(31);t["labels"].append({"name":"gcl-state:returned"})
        t["labels"]=[x for x in t["labels"] if x["name"]!="gcl-state:available"]
        self.assertEqual(self.step(31,target=t)["outcome"],"DENIED")
    def test_authentic_actor_and_comment_binding(self):
        e=event(4,body(3,"3"*32))
        with self.assertRaisesRegex(Denied,"FRESH_HISTORY"):choose(e,[],NOW,source(3))
        self.assertEqual(self.step(3)["outcome"],"GRANTED")
    def test_forensic_bot_spoof_rejected(self):
        self.history.append({"id":1,"user":{"login":"evil"},"body":PREFIX+'{}'})
        self.assertEqual(ledger(self.history,NOW)[1],{})
        self.history.append({"id":2,"user":{"login":"github-actions[bot]"},
                             "body":PREFIX+json.dumps({"request_id":999,"outcome":"GRANTED","op":"START",
                             "repo":ATLAS,"issue":3,"run":"3"*32,"worker":"evil",
                             "expires_at":NOW.isoformat(),"reason":"CAPACITY_ADMITTED"})})
        with self.assertRaisesRegex(Denied,"NOT_BOUND"):ledger(self.history,NOW)
    def test_hostile_grammar(self):
        for b in ("EDITORIAL-START/1\nrepository: evil\nissue: 5\nrun_id: "+"f"*32+"\nsource_head: "+"a"*40,
                  body(5,"f"*32).replace("source_head:","other_head:"),
                  body(5,"f"*32).replace("EDITORIAL-START","/claim")):
            with self.assertRaises(Denied):parse(b)
    def test_idempotent_event(self):
        self.next+=1;e=event(self.next,body(3,"3"*32))
        self.history.append(e["comment"])
        d=choose(e,self.history,NOW,source(3));self.assertEqual(d["outcome"],"GRANTED")
        self.next+=1;self.history.append({"id":self.next,"body":PREFIX+json.dumps(d),"user":{"login":"github-actions[bot]"}})
        self.assertIsNone(choose(e,self.history,NOW,source(3)))
    def test_duplicate_ids_fail_closed(self):
        self.step(4)
        self.history.append(self.history[0])
        with self.assertRaisesRegex(Denied,"IDENTITY_DRIFT"):ledger(self.history,NOW)
if __name__=="__main__":unittest.main()
