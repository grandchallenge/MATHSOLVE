import sys
import unittest
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "ci"))
from solve_ci_impact import classify, LANES, workflow_impact, native_pnp_only

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
