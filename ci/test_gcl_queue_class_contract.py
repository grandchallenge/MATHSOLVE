#!/usr/bin/env python3
"""Positive and hostile replay for queue *class* versus pickup *mode*."""
import copy
import unittest

from gcl_queue_class_contract import (
    QueueIntegrityError, check_admission, classify, validate_snapshot,
)

MODES = {
    "grandchallenge/MATHSOLVE": "reservation_controlled",
    "grandchallenge/ADAPTIVE-INTELLIGENCE-ATLAS": "direct_editorial",
    "grandchallenge/COMPUTATIONAL-DIFFICULTY-ATLAS": "direct_editorial",
    "grandchallenge/MATH-PROGRAMME": "direct_editorial",
}
DIRECT = "gcl-pickup:direct-editorial"

def item(repo, n, title, labels, klass):
    return {
        "repository":repo, "issue_number":n, "title":title,
        "labels":labels, "queue_class":klass,
        "project_item_id":f"item-{n}", "gcl_state":"AVAILABLE",
    }

def fixture():
    return {
        "project_number":2, "complete":True, "total_count":3,
        "rows":[
            item("grandchallenge/MATHSOLVE",999,"Solve theorem",["gcl-job"],"Mathematics"),
            item("grandchallenge/MATH-PROGRAMME",1273,
                 "[GCL-ERDOS] ERDOS-CATALOGUE-0004-S01 — Problem 4",
                 ["gcl-job",DIRECT,"gcl-role:source-audit"],"Mathematics"),
            item("grandchallenge/MATH-PROGRAMME",2556,
                 "EC-ED02 — Erdős #7 — mathematical explanation",
                 ["gcl-job",DIRECT,"gcl-role:constructive"],"Editorial"),
        ],
        "views":{
            "AVAILABLE":{"id":"existing-global-view"},
            "EDITORIAL":{"id":"editorial-view","queue_class":"Editorial"},
            "MATHEMATICS":{"id":"mathematics-view","queue_class":"Mathematics"},
        },
    }


class ClassTest(unittest.TestCase):
    def test_math_research_with_direct_pickup(self):
        c,m = classify("grandchallenge/MATH-PROGRAMME",
                       "[GCL-ERDOS] ERDOS-CATALOGUE-0004-S01 — primes",
                       {DIRECT,"gcl-role:source-audit"},modes=MODES)
        self.assertEqual((c,m),("Mathematics","direct_editorial"))

    def test_specialist_editorial_discovery_not_lost(self):
        from pathlib import Path
        import json
        root=Path(__file__).resolve().parents[1]
        worker=(root/"WORKERS.md").read_text(encoding="utf-8")
        cfg=json.loads((root/".well-known/gcl-worker-queue.json").read_text(encoding="utf-8"))
        specialist=cfg["queue_classes"]["editorial"]["specialist_source_triage"]
        self.assertEqual({entry["issue_number"] for entry in specialist},{1262,1264})
        for entry in specialist:
            self.assertEqual(entry["semantic_class"],"Editorial")
            self.assertEqual(entry["pickup_mode"],"direct_editorial")
            self.assertEqual(entry["discover_only_if_state"],"AVAILABLE")
            self.assertIn(entry["issue_url"],worker)
        self.assertIn("source-defect triage",worker)
        self.assertIn("gcl-role:source-audit",worker)
        self.assertIn(cfg["queue_classes"]["mathematics"]["critical_review_query_url"],worker)
        # The ordinary Editorial search must continue excluding the much
        # larger mathematical source-audit catalogue.
        self.assertIn("-label%3Agcl-role%3Asource-audit",worker)

    def test_typography_source_triage_stays_editorial(self):
        c,m=classify("grandchallenge/MATH-PROGRAMME",
           "MP-MATH-TYPO-ED07 — Complete public documentation defect triage outside named guides and documentaries",
           {DIRECT,"gcl-role:source-audit"},modes=MODES)
        self.assertEqual((c,m),("Editorial","direct_editorial"))
        with self.assertRaisesRegex(QueueIntegrityError,"ambiguous"):
            classify("grandchallenge/MATH-PROGRAMME",
              "An unrelated mathematical source investigation",
              {DIRECT,"gcl-role:source-audit"},modes=MODES)

    def test_erdos_rolling_critic_and_ed09_semantics(self):
        for n in (11,18,25,41):
            name=f"ERDOS {n} — critical source and lemma review of ERDOS-{n:03d}-PROOF-CHECK-001"
            self.assertEqual(classify("grandchallenge/MATH-PROGRAMME",
               name,{DIRECT,"gcl-role:source-audit"},modes=MODES),
               ("Mathematics","direct_editorial"))
        self.assertEqual(classify("grandchallenge/MATH-PROGRAMME",
          "MP-MATH-TYPO-ED09 — Historical mathematical records: evidence-preserving typography triage",
          {DIRECT,"gcl-role:source-audit"},modes=MODES),
          ("Editorial","direct_editorial"))
        with self.assertRaisesRegex(QueueIntegrityError,"identity mismatch"):
            classify("grandchallenge/MATH-PROGRAMME",
              "ERDOS 11 — critical source and lemma review of ERDOS-099-FOO",
              {DIRECT,"gcl-role:source-audit"},modes=MODES)

    def test_erdos41_research_mathematics_with_direct_issue_return(self):
        tracks = [
            ("ERDOS-041-R41-A — fourth-order overlap propagation or counterexample", "gcl-role:constructive", 2790),
            ("ERDOS-041-R41-B — prove or refute a scale-owned capacity invariant", "gcl-role:constructive", 2791),
            ("ERDOS-041-R41-C — independent Pauli-level proof audit and falsification", "gcl-role:verify", 2792),
            ("ERDOS-041-R41-D — spectral moment-flow renormalization experiment", "gcl-role:constructive", 2793),
        ]
        for title,role,n in tracks:
            labels={DIRECT,"gcl-job","gcl-collab:cooperative",role,"gcl-state:available"}
            with self.subTest(issue=n):
                self.assertEqual(classify("grandchallenge/MATH-PROGRAMME",title,labels,modes=MODES),("Mathematics","direct_editorial"))
                f=fixture()
                f["rows"].append(item("grandchallenge/MATH-PROGRAMME",n,title,sorted(labels),"Mathematics"))
                f["total_count"]+=1
                validate_snapshot(f,require_views=True)
                for bad in (labels-{role},labels-{"gcl-collab:cooperative"},labels-{DIRECT}):
                    with self.assertRaises(QueueIntegrityError):
                        classify("grandchallenge/MATH-PROGRAMME",title,bad,modes=MODES)
                f["rows"][-1]["issue_number"]=n+100
                with self.assertRaisesRegex(QueueIntegrityError,"identity drift"):
                    validate_snapshot(f)

    def test_editorial_direct_pickup(self):
        for repo in ("grandchallenge/MATH-PROGRAMME",
                     "grandchallenge/ADAPTIVE-INTELLIGENCE-ATLAS",
                     "grandchallenge/COMPUTATIONAL-DIFFICULTY-ATLAS"):
            self.assertEqual(classify(repo,"Chapter review",{DIRECT},modes=MODES)[0],"Editorial")

    def test_solve_erdos_source_audit_keeps_reservation(self):
        # Real protected Solve dispatches #843 and #1033 carry the SOURCE_AUDIT
        # semantic role. It does not authorize direct-editorial pickup.
        for issue, name in (
            (843, "[GCL-CONTRIB] ERDOS-OPEN ERDOS-593-S1-IA-001 — SOURCE-AUDIT"),
            (1033, "[GCL-CONTRIB] ERDOS-OPEN ERDOS-470-N3-IA-001 — ODD-WEIRD-WORKUNIT-COVER-REPLAY"),
        ):
            with self.subTest(issue=issue):
                self.assertEqual(classify("grandchallenge/MATHSOLVE", name,
                    {"gcl-job", "gcl-role:source-audit"}, modes=MODES),
                    ("Mathematics", "reservation_controlled"))
                with self.assertRaisesRegex(QueueIntegrityError, "reservation issue"):
                    classify("grandchallenge/MATHSOLVE", name,
                        {"gcl-job", "gcl-role:source-audit", DIRECT}, modes=MODES)

    def test_proof_dispatch(self):
        self.assertEqual(classify("grandchallenge/MATHSOLVE","Proof",{"gcl-job"},modes=MODES),
                         ("Mathematics","reservation_controlled"))

    def test_bad_modes_and_ambiguous_source(self):
        cases = [
            ("grandchallenge/OTHER","Misc",[]),
            ("grandchallenge/MATHSOLVE","Proof",[DIRECT]),
            ("grandchallenge/MATH-PROGRAMME","Article",[]),
            ("grandchallenge/MATH-PROGRAMME","Article",[DIRECT,"gcl-role:source-audit"]),
            ("grandchallenge/MATH-PROGRAMME","ERDOS-CATALOGUE-0009-S01",[DIRECT]),
            ("grandchallenge/ADAPTIVE-INTELLIGENCE-ATLAS","Review",[DIRECT,"gcl-pickup:reservation"]),
        ]
        for repo,title,labels in cases:
            with self.subTest(repo=repo,title=title), self.assertRaises(QueueIntegrityError):
                classify(repo,title,labels,modes=MODES)

    def test_full_snapshot(self):
        result=validate_snapshot(fixture(),require_views=True)
        self.assertEqual(result["classes"],{"Mathematics":2,"Editorial":1})
        self.assertTrue(result["views_verified"])

    def test_false_editorial_class_fails(self):
        f=fixture()
        f["rows"][1]["queue_class"]="Editorial"
        with self.assertRaisesRegex(QueueIntegrityError,"expected 'Mathematics'"):
            validate_snapshot(f)

    def test_partial_and_duplicate_rejected(self):
        f=fixture(); f["total_count"]=1294
        with self.assertRaisesRegex(QueueIntegrityError,"partial"):
            validate_snapshot(f)
        f=fixture();f["rows"][2]["project_item_id"]=f["rows"][1]["project_item_id"]
        with self.assertRaisesRegex(QueueIntegrityError,"duplicate"):
            validate_snapshot(f)

    def test_saved_view_evidence_required(self):
        f=fixture();del f["views"]["MATHEMATICS"]
        with self.assertRaisesRegex(QueueIntegrityError,"MATHEMATICS"):
            validate_snapshot(f,require_views=True)

    def test_independent_admission_budgets(self):
        limits={"Editorial":4,"Mathematics":2}
        self.assertFalse(check_admission("Mathematics",{"Editorial":0,"Mathematics":2},limits)["admit"])
        self.assertTrue(check_admission("Editorial",{"Editorial":0,"Mathematics":2},limits)["admit"])
        self.assertFalse(check_admission("Editorial",{"Editorial":4,"Mathematics":0},limits)["admit"])
        self.assertTrue(check_admission("Mathematics",{"Editorial":4,"Mathematics":0},limits)["admit"])

    def test_missing_budget_fails_closed(self):
        with self.assertRaises(QueueIntegrityError):
            check_admission("Editorial",{"Editorial":0,"Mathematics":0},{"Editorial":4})
        with self.assertRaises(QueueIntegrityError):
            check_admission("Research",{"Editorial":0,"Mathematics":0},{"Editorial":4,"Mathematics":2})


if __name__=="__main__":
    unittest.main()
