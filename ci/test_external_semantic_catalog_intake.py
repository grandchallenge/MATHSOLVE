import copy
import json
import unittest

try:
    from ci.validate_external_semantic_catalog_intake import POLICY, validation_errors
except ModuleNotFoundError:  # Direct script execution places ci/ on sys.path.
    from validate_external_semantic_catalog_intake import POLICY, validation_errors


class ExternalSemanticCatalogIntakeTests(unittest.TestCase):
    def setUp(self):
        self.policy = json.loads(POLICY.read_text(encoding="utf-8"))

    def test_committed_policy(self):
        self.assertEqual(validation_errors(self.policy), [])

    def test_source_locked_entry_cannot_seed_solve(self):
        changed = copy.deepcopy(self.policy)
        changed["proposal_gate"]["minimum_assurance_tier"] = "SOURCE_LOCKED"
        self.assertTrue(validation_errors(changed))

    def test_catalog_cannot_become_result_or_claim(self):
        for field in ("catalog_entry_is_mathsolve_result", "catalog_may_mutate_claim_ledger"):
            changed = copy.deepcopy(self.policy)
            changed["forbidden_authority"][field] = True
            self.assertTrue(validation_errors(changed))

    def test_certification_requires_separate_handoff(self):
        changed = copy.deepcopy(self.policy)
        changed["certification_handoff"]["separate_scoped_handoff_required"] = False
        self.assertTrue(validation_errors(changed))

    def test_catalog_entry_does_not_receive_dossier_at_ingestion(self):
        changed = copy.deepcopy(self.policy)
        changed["chaidez_dossier_gate"]["catalog_entries_require_dossier"] = True
        self.assertTrue(validation_errors(changed))

    def test_dossier_trigger_cannot_move_before_reviewed_promotion(self):
        changed = copy.deepcopy(self.policy)
        changed["chaidez_dossier_gate"]["trigger"] = "CATALOG_INGESTION"
        self.assertTrue(validation_errors(changed))


if __name__ == "__main__":
    unittest.main()
