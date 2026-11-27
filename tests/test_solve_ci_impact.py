import sys
import unittest
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "ci"))
from solve_ci_impact import classify, LANES, workflow_impact, native_pnp_only, isolated_research_only, worker_guidance_only, campaign_ledgers_required

class ImpactTests(unittest.TestCase):
    def route(self, paths, old="", new=""):
        return classify(paths, lambda _: old, lambda _: new)
    def test_pnp_above_excludes_unrelated_formal_and_otp(self):
        self.assertEqual(self.route(["research/PNP-ABOVE/WP39_Proof.lean"]), (set(), False))
    def test_pnp_library_and_import_index(self):
        self.assertEqual(self.route(["MathSolve/PNP/Next.lean", "MathSolve.lean"],
            "import MathSolve.RH.SpectralUnbounded\n",
            "import MathSolve.RH.SpectralUnbounded\nimport MathSolve.PNP.Next\n"), ({"pnp"}, False))
    def test_rh_and_erdos_and_uc(self):
        for file,lane in [("MathSolve/RH/SpectralUnbounded.lean","rhns"),
                          ("MathSolve/FormalConjectures/E602Correspondence.lean","erdos"),
                          ("MathSolve/UnionClosed/FunctionalPreorderBridge.lean","uc")]:
            self.assertEqual(self.route([file]), ({lane}, False))
    def test_shared_environment_and_unknown_root(self):
        for file in ("lake-manifest.json", "ci/checked_lean.py", "MathSolve/Unknown.lean"):
            self.assertEqual(self.route([file]), (set(LANES), False))
        self.assertEqual(self.route(["MathSolve.lean"], "import MathSolve.PNP.Next", "def hidden := 1"),
                         (set(LANES), False))
    def test_otp_scope(self):
        self.assertEqual(self.route(["work_packages/OPENAI_TEN_PROOFS_WP00/result_family_handoffs/a.json"]), (set(), True))
    def test_formal_workflow_step_only(self):
        template = "jobs:\n  formal-targets:\n    steps:\n      - name: 'Replay lane: pnp'\n        run: {}\n"
        self.assertEqual(workflow_impact(template.format("old"),template.format("new")), ({"pnp"},False))
    def test_docs_no_formal(self):
        self.assertEqual(self.route(["README.md","docs/explainer.md"]), (set(),False))

    def test_native_pnp_only_requires_every_path(self):
        self.assertTrue(native_pnp_only(["research/PNP-ABOVE/WP39B_Witness.lean",
                                        "research/PNP-ABOVE/WP39B_SOURCE_LOCK.json"]))
        self.assertFalse(native_pnp_only(["research/PNP-ABOVE/WP39B_Witness.lean",
                                         "ci/checked_lean.py"]))
        self.assertFalse(native_pnp_only([]))

    def test_isolated_research_scope(self):
        pnp = "research/PNP-ABOVE/WP39B_Witness.lean"
        scc = "research/SCC-001/interaction_replay.py"
        for paths in ([pnp], [scc], [pnp, scc]):
            self.assertTrue(isolated_research_only(paths))
            self.assertEqual(self.route(paths), (set(), False))
        for paths in ([], [pnp, "ci/checked_lean.py"], [scc, "research/OTHER/proof.lean"],
                      ["research/SCC-001-other/proof.lean"], ["MathSolve/PNP/Next.lean"]):
            self.assertFalse(isolated_research_only(paths))

    def test_worker_guidance_and_campaign_ledger_scope(self):
        for paths in (["AGENTS.md"], ["WORKERS.md"], ["AGENTS.md", "WORKERS.md"]):
            self.assertTrue(worker_guidance_only(paths))
            self.assertFalse(campaign_ledgers_required(paths))
            self.assertEqual(self.route(paths), (set(), False))
        for paths in ([], ["README.md"], ["docs/unknown.md"],
                      ["AGENTS.md", "ci/solve_ci_impact.py"],
                      ["WORKERS.md", "governance/new.json"],
                      ["AGENTS.md", "research/PNP-ABOVE/Proof.lean"],
                      ["research/PNP-ABOVE/Proof.lean", "research/OTHER/a.py"]):
            self.assertFalse(worker_guidance_only(paths))
            self.assertTrue(campaign_ledgers_required(paths))
        for paths in (["research/PNP-ABOVE/Proof.lean"], ["research/SCC-001/a.py"]):
            self.assertFalse(campaign_ledgers_required(paths))

    def test_ledger_gate_bindings(self):
        import yaml
        root = Path(__file__).resolve().parents[1]
        jobs = yaml.safe_load((root / ".github/workflows/ci.yml").read_text())["jobs"]
        steps = {s.get("name"): s for s in jobs["ledgers"]["steps"]}
        for name in ("Validate global worker-queue controls",
                     "Validate recursive campaign manifests and Cert boundaries",
                     "Validate Lean compiler execution safety",
                     "Require successful impact classification"):
            self.assertNotIn("if", steps[name])
        self.assertIn("ci/validate_gcl_worker_bootstrap.py",
                      steps["Validate global worker-queue controls"]["run"])
        self.assertIn("test_gcl_queue_class_contract.py",
                      steps["Validate global worker-queue controls"]["run"])
        self.assertEqual(jobs["impact"]["outputs"]["campaign_ledgers_required"],
                         "${{ steps.classify.outputs.campaign_ledgers_required }}")
        for name in ("Validate Erdős campaign evidence and replays",
                     "Validate campaign-specific intake interfaces",
                     "Validate GCL-ERDOS3 frontier and independent intake",
                     "Validate campaign-specific activation and concordance",
                     "Validate NS-CI WP02 conditional-regularity ledger",
                     "Validate OPENMATH H1-12 three-core arithmetic"):
            self.assertEqual(steps[name]["if"],
                "needs.impact.outputs.campaign_ledgers_required != 'false'")
