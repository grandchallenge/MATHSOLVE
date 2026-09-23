import copy
import unittest

from ci.validate_external_catalog_promotion_dossiers import validate_document


VALID = {
    "schema_version": "1.0.0", "promotion_id": "MS-CAT-PROMOTION-CANARY", "promotion_state": "REVIEWED_PROMOTION",
    "catalog_source": {"catalog_id": "GCL-CAT-CANARY", "catalog_release_id": "GCL-CATALOG-CANARY", "assurance_tier": "SEMANTICALLY_REVIEWED", "exact_campaign_target": False, "reviewed_relation_id": None},
    "review": {"reviewer": "qualified-reviewer", "reviewed_at": "2026-09-23", "evidence": ["review/evidence.md"]},
    "result_status": {"result_status": "OPEN"}, "exposition": {"STATUS_BOX": "01_RESULT_STATUS.md"},
    "trust_quartet": {"WHAT_IS_PROVED": "nothing"}, "theorem_spine": [{"node_id": "CANARY-01"}], "proof_debt": [],
    "required_artifacts": {name: f"dossier/{name}.md" for name in ("RESULT_STATUS", "LAY_COMPANION", "OBJECT_AND_OBSTRUCTION", "STATUS_AUDIT", "CLAIM_LEDGER", "THEOREM_SPINE", "DEPENDENCY_DAG", "PROOFS_AND_COMPUTATIONS", "FAILURE_AND_NEGATIVE_RESULTS", "PROOF_DEBT_REGISTER", "CERT_HANDOFF", "NEXT_EXECUTABLE_STEP")}
}


class PromotionDossierTests(unittest.TestCase):
    def test_canary(self): self.assertEqual(validate_document(VALID), [])
    def test_missing_artifact_fails(self):
        changed = copy.deepcopy(VALID); del changed["required_artifacts"]["CERT_HANDOFF"]
        self.assertTrue(validate_document(changed))
    def test_exact_target_requires_concordance_and_relation(self):
        changed = copy.deepcopy(VALID); changed["catalog_source"]["exact_campaign_target"] = True
        self.assertTrue(validate_document(changed))


if __name__ == "__main__": unittest.main()
