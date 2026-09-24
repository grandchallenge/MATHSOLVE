"""Filesystem and mutation coverage for Chaidez reviewed promotion, never production."""
import copy
import json
import tempfile
import unittest
from pathlib import Path

from ci.chaidez_canary import FIXTURE, commit, materialize, ref, repin_bundle, write_json
from ci.chaidez_contract import ROOT, artifact_bytes, consistency_errors, git, hashes, schema_errors
from ci.validate_external_catalog_promotion_dossiers import validate_document, validate_handoff, validate_registry

DOSSIER = "promotions/external_catalog/MS-CAT-PROMOTION-CANARY.json"
HANDOFF = "cert_handoffs/external_catalog/MS-CAT-HANDOFF-CANARY.json"


class PromotionDossierTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix="chaidez-contract-test.")
        self.addCleanup(self.temp.cleanup)
        self.roots = materialize(self.temp.name)
        self.root = self.roots["grandchallenge/MATHSOLVE"]
        self.d = json.loads((self.root / DOSSIER).read_text())
        self.h = json.loads((self.root / HANDOFF).read_text())

    def validate(self, d=None):
        return validate_document(d or self.d, self.root, self.roots, canary=True)

    def test_complete_on_disk_canary(self):
        self.assertEqual(self.validate(), [])
        self.assertEqual(validate_registry(self.root, self.roots, canary=True), [])
        self.assertEqual(validate_handoff(self.h, self.root, self.roots, canary=True), [])

    def test_production_registry_remains_empty(self):
        data = json.loads((ROOT / "governance/external_catalog_promotion_registry.json").read_text())
        self.assertEqual((data["promotion_count"], data["promotions"]), (0, []))
        self.assertEqual(validate_registry(), [])

    def test_canary_cannot_cross_into_production(self):
        self.assertIn("canary and production contexts may not cross", validate_document(self.d, self.root, self.roots))

    def test_every_required_dossier_member(self):
        schema = json.loads((ROOT / "schemas/external_catalog_promotion_dossier.schema.json").read_text())
        def check(value, spec, path=()):
            for key in spec.get("required", []):
                altered = copy.deepcopy(self.d)
                cursor = altered
                for part in path:
                    cursor = cursor[part]
                del cursor[key]
                with self.subTest(missing=path + (key,)):
                    self.assertTrue(schema_errors(altered, "external_catalog_promotion_dossier.schema.json"))
            if isinstance(value, dict):
                for key, child in value.items():
                    if key in spec.get("properties", {}):
                        check(child, spec["properties"][key], path + (key,))
            elif isinstance(value, list):
                for i, child in enumerate(value):
                    sub = spec.get("prefixItems", [])[i] if i < len(spec.get("prefixItems", [])) else spec.get("items", {})
                    if isinstance(sub, dict):
                        check(child, sub, path + (i,))
            for sub in spec.get("oneOf", []):
                if isinstance(value, dict) and all(k in value for k in sub.get("required", [])):
                    check(value, sub, path)
        check(self.d, schema)

    def test_all_status_fields_stages_quartet_roles_required(self):
        for key in ("result_status", "trust_quartet", "required_artifacts", "escalation_gate"):
            for member in self.d[key]:
                d = copy.deepcopy(self.d)
                del d[key][member]
                with self.subTest(key=key, member=member):
                    self.assertTrue(self.validate(d))
        for i in range(9):
            d = copy.deepcopy(self.d)
            del d["exposition"][i]
            self.assertTrue(self.validate(d))
        d = copy.deepcopy(self.d)
        d["exposition"].reverse()
        self.assertTrue(self.validate(d))

    def test_unknown_enums_and_forbidden_authority(self):
        paths = [("promotion_state",), ("creation_trigger",), ("automatic_promotion",),
                 ("record_class",), ("review", "decision"), ("review", "semantic_fidelity_confirmed"),
                 ("result_status", "support_route_class"), ("result_status", "result_status"),
                 ("result_status", "certification_state"), ("theorem_spine", 0, "role"),
                 ("theorem_spine", 0, "status"), ("proof_debt", 0, "category"),
                 ("proof_debt", 0, "route"), ("proof_debt", 0, "status"),
                 ("non_claim_boundary", "certification_inferred")]
        for path in paths:
            d = copy.deepcopy(self.d)
            cursor = d
            for part in path[:-1]:
                cursor = cursor[part]
            cursor[path[-1]] = not cursor[path[-1]] if isinstance(cursor[path[-1]], bool) else "UNKNOWN"
            with self.subTest(path=path):
                self.assertTrue(self.validate(d))
        for trigger in ("CATALOG_INGESTION", "AUTOMATIC", "NORMALIZATION"):
            d = copy.deepcopy(self.d)
            d["creation_trigger"] = trigger
            self.assertTrue(self.validate(d))

    def test_every_support_route_is_accepted_structurally(self):
        contract = json.loads((ROOT / "contracts/chaidez/chaidez_protocol_contract.json").read_text())
        for route in contract["support_route_classes"]:
            d = copy.deepcopy(self.d)
            d["result_status"]["support_route_class"] = route
            d["theorem_spine"][0]["support_route_class"] = route
            d["proof_debt"][0]["route"] = route
            repin_bundle(self.root, d)
            self.assertEqual(self.validate(d), [], route)

    def test_every_debt_category_and_foundation_disposition(self):
        contract = json.loads((ROOT / "contracts/chaidez/chaidez_protocol_contract.json").read_text())
        for category in contract["proof_debt_categories"]:
            d = copy.deepcopy(self.d)
            d["proof_debt"][0]["category"] = category
            if category == "FOUNDATIONAL_PROFILE_GAP":
                d["result_status"]["foundational_profile"] = {"disposition": category, "debt_id": "CANARY-D1"}
            if category == "EXTERNAL_SOURCE":
                d["trust_quartet"]["WHAT_REQUIRES_EXTERNAL_VERIFICATION"]["debt_ids"] = ["CANARY-D1"]
            repin_bundle(self.root, d)
            self.assertEqual(self.validate(d), [], category)
        d = copy.deepcopy(self.d)
        d["result_status"]["foundational_profile"] = {"disposition": "FOUNDATIONAL_PROFILE_GAP", "debt_id": "missing"}
        self.assertTrue(self.validate(d))

    def test_filesystem_path_and_identity_attacks(self):
        for unsafe in ("../outside", "/etc/passwd", "C:/file", "work_packages/../outside", "a\\b", ".git/config"):
            d = copy.deepcopy(self.d)
            d["required_artifacts"]["RESULT_STATUS"]["path"] = unsafe
            self.assertTrue(self.validate(d), unsafe)
        for key in ("git_blob_sha1", "sha256"):
            d = copy.deepcopy(self.d)
            d["required_artifacts"]["RESULT_STATUS"][key] = "0" * (40 if key == "git_blob_sha1" else 64)
            self.assertTrue(self.validate(d))
        target = self.root / self.d["required_artifacts"]["RESULT_STATUS"]["path"]
        target.write_text("changed bytes\n")
        self.assertTrue(self.validate())
        self.d["required_artifacts"]["RESULT_STATUS"] = ref(self.root, self.d["required_artifacts"]["RESULT_STATUS"]["path"])
        self.assertTrue(self.validate(), "re-pinning untracked edits must not bypass Git blob checks")
        target.unlink()
        self.assertTrue(self.validate())

    def test_untracked_and_symlink_files_rejected(self):
        path = "work_packages/CANARY/untracked.md"
        (self.root / path).write_text("Untracked fixture\n")
        self.d["required_artifacts"]["RESULT_STATUS"] = ref(self.root, path)
        self.assertTrue(self.validate())
        if hasattr(Path, "symlink_to"):
            link = self.root / "work_packages/CANARY/link.md"
            try:
                link.symlink_to(self.root / path)
            except OSError:
                self.skipTest("symlinks unavailable")
            self.d["required_artifacts"]["RESULT_STATUS"]["path"] = "work_packages/CANARY/link.md"
            git(self.root, "add", "--all")
            self.assertTrue(self.validate())

    def test_shared_file_needs_distinct_existing_anchors(self):
        path = "work_packages/CANARY/shared.md"
        (self.root / path).write_text('<a id="lay"></a>\nLay explanation\n<a id="object"></a>\nObject and obstruction\n')
        git(self.root, "add", "--all")
        for role, anchor in (("LAY_COMPANION", "lay"), ("OBJECT_AND_OBSTRUCTION", "object")):
            self.d["required_artifacts"][role] = {**ref(self.root, path), "section_anchor": anchor}
        self.assertEqual(self.validate(), [])
        self.d["required_artifacts"]["OBJECT_AND_OBSTRUCTION"]["section_anchor"] = "lay"
        self.assertTrue(self.validate())
        self.d["required_artifacts"]["OBJECT_AND_OBSTRUCTION"]["section_anchor"] = "missing"
        self.assertTrue(self.validate())

    def test_spine_dependencies_duplicates_debt_and_quartet_consistency(self):
        cases = [
            lambda d: d["theorem_spine"].append(copy.deepcopy(d["theorem_spine"][0])),
            lambda d: d["proof_debt"].append(copy.deepcopy(d["proof_debt"][0])),
            lambda d: d["local_claims"].append(copy.deepcopy(d["local_claims"][0])),
            lambda d: d["theorem_spine"][0].update(dependencies=["UNKNOWN"]),
            lambda d: d["theorem_spine"][0].update(dependencies=["CANARY-N1"]),
            lambda d: d["theorem_spine"][0].update(proof_debt_ids=[]),
            lambda d: d["proof_debt"][0].update(blocked_node="UNKNOWN"),
            lambda d: d["local_claims"][0].update(proof_debt_ids=[]),
            lambda d: d["trust_quartet"]["WHAT_IS_PROVED"].update(claim_ids=["CANARY-CLAIM-001"]),
            lambda d: d["trust_quartet"]["WHAT_REMAINS_OPEN"].update(debt_ids=[]),
            lambda d: d["result_status"].update(result_status="RESTRICTED_RESULT"),
            lambda d: d["result_status"].update(strongest_supported_claim="Every conjecture is proved."),
            lambda d: d.update(local_node_advanced="UNKNOWN"),
            lambda d: d["result_status"]["first_executable_step"].update(node_id="UNKNOWN"),
        ]
        for i, change in enumerate(cases):
            d = copy.deepcopy(self.d)
            change(d)
            repin_bundle(self.root, d)
            self.assertTrue(self.validate(d), i)

    def test_checked_claim_cannot_hide_open_debt(self):
        d = copy.deepcopy(self.d)
        d["theorem_spine"][0]["status"] = d["local_claims"][0]["status"] = "PROVED"
        d["result_status"]["result_status"] = "RESTRICTED_RESULT"
        d["trust_quartet"]["WHAT_IS_PROVED"]["claim_ids"] = ["CANARY-CLAIM-001"]
        d["trust_quartet"]["WHAT_IS_CHECKED"]["claim_ids"] = ["CANARY-CLAIM-001"]
        d["trust_quartet"]["WHAT_REMAINS_OPEN"]["claim_ids"] = []
        repin_bundle(self.root, d)
        self.assertIn("checked/proved node has unresolved prerequisite debt", self.validate(d))

    def test_claim_ledger_and_handoff_disagreement(self):
        for role in ("CLAIM_LEDGER", "THEOREM_SPINE", "PROOF_DEBT_REGISTER", "DEPENDENCY_DAG", "CERT_HANDOFF"):
            d = copy.deepcopy(self.d)
            path = d["required_artifacts"][role]["path"]
            write_json(self.root, path, {})
            git(self.root, "add", "--all")
            d["required_artifacts"][role] = ref(self.root, path)
            self.assertTrue(self.validate(d), role)
            repin_bundle(self.root, self.d)

    def test_inadequate_assurance_and_source_identity(self):
        for key, value in (("assurance_tier", "SOURCE_LOCKED"), ("assurance_tier", "NORMALIZED_REPLAYED"),
                           ("snapshot_id", "OTHER"), ("raw_sha256", "0"*64), ("normalized_sha256", "0"*64),
                           ("catalog_release_id", "OTHER"), ("catalog_id", "GCL-CAT-MISSING")):
            d = copy.deepcopy(self.d)
            d["catalog_source"][key] = value
            self.assertTrue(self.validate(d), key)
        self.assertTrue(validate_document(self.d, self.root, {}, canary=True))
        for field in ("programme_import", "catalog_shard"):
            d = copy.deepcopy(self.d)
            d["catalog_source"][field]["commit"] = "main"
            self.assertTrue(self.validate(d))
        d = copy.deepcopy(self.d)
        d["catalog_source"]["programme_import"]["artifact"]["sha256"] = "0"*64
        self.assertTrue(self.validate(d))

    def test_exact_target_cannot_use_similarity_or_missing_review(self):
        d = copy.deepcopy(self.d)
        d["catalog_source"].update(exact_campaign_target=True, assurance_tier="CAMPAIGN_CONCORDANT", reviewed_relation_id="GCL-REL-MISSING")
        self.assertTrue(self.validate(d))
        forge = self.roots["grandchallenge/MATHFORGE"]
        programme = self.roots["grandchallenge/MATH-PROGRAMME"]
        entry = json.loads((forge / "catalog/entries/canary.jsonl").read_text())
        entry["assurance"]["tier"] = "CAMPAIGN_CONCORDANT"
        entry["relation_ids"] = ["GCL-REL-MATCH"]
        d["catalog_source"]["reviewed_relation_id"] = "GCL-REL-MATCH"
        relation = {"relation_id": "GCL-REL-MATCH", "subject_id": "GCL-CAT-CANARY", "object_id": "GCL-CAMPAIGN:CANARY",
                    "predicate": "same_statement", "review_state": "HUMAN_REVIEWED", "reviewer": "synthetic", "evidence": ["synthetic only"]}
        for predicate, review, accepted in (("same_statement", "HUMAN_REVIEWED", True), ("formalizes", "HUMAN_REVIEWED", True),
                                            ("related", "HUMAN_REVIEWED", False), ("duplicate_candidate", "HUMAN_REVIEWED", False),
                                            ("implies", "HUMAN_REVIEWED", False), ("same_statement", "AUTOMATED", False)):
            (forge / "catalog/entries/canary.jsonl").write_text(json.dumps(entry) + "\n")
            relation.update(predicate=predicate, review_state=review)
            write_json(forge, "catalog/relations/relations.json", {"relations": [relation]})
            forge_commit = commit(forge)
            imp = json.loads((programme / "governance/mathforge_external_source_imports.json").read_text())
            imp["source_foundry"]["commit"] = forge_commit
            imp["providers"][0]["catalog_shards"] = [{"kind": "catalog_shard", **ref(forge, "catalog/entries/canary.jsonl")}]
            imp["catalog_release"]["relation_artifacts"] = [ref(forge, "catalog/relations/relations.json")]
            write_json(programme, "governance/mathforge_external_source_imports.json", imp)
            programme_commit = commit(programme)
            d["catalog_source"]["programme_import"] = {"repository": "grandchallenge/MATH-PROGRAMME", "commit": programme_commit,
                                                       "artifact": ref(programme, "governance/mathforge_external_source_imports.json")}
            d["catalog_source"]["catalog_shard"] = {"repository": "grandchallenge/MATHFORGE", "commit": forge_commit,
                                                   "artifact": ref(forge, "catalog/entries/canary.jsonl")}
            self.assertEqual(not self.validate(d), accepted, (predicate, review))

    def test_stale_import_and_unprotected_commit_fail(self):
        programme = self.roots["grandchallenge/MATH-PROGRAMME"]
        path = "governance/mathforge_external_source_imports.json"
        value = json.loads((programme / path).read_text())
        value["catalog_release"]["catalog_release_id"] = "NEXT"
        write_json(programme, path, value)
        new = commit(programme)
        self.assertTrue(self.validate())
        git(programme, "update-ref", "refs/remotes/origin/main", "HEAD^")
        self.d["catalog_source"]["programme_import"]["commit"] = new
        self.d["catalog_source"]["programme_import"]["artifact"] = ref(programme, path)
        self.assertTrue(self.validate())

    def test_registry_count_duplicate_orphan_missing_dossier(self):
        path = "governance/external_catalog_promotion_registry.json"
        original = json.loads((self.root / path).read_text())
        for data in ({**original, "promotion_count": 0}, {**original, "promotion_count": 2, "promotions": original["promotions"]*2},
                     {**original, "promotion_count": 0, "promotions": []}):
            write_json(self.root, path, data)
            self.assertTrue(validate_registry(self.root, self.roots, canary=True))
        write_json(self.root, path, original)
        (self.root / DOSSIER).unlink()
        self.assertTrue(validate_registry(self.root, self.roots, canary=True))

    def test_handoff_claim_debt_trust_route_and_direct_intake_rejected(self):
        cases = [
            lambda h: h.update(proof_debt_ids=[]),
            lambda h: h["selected_claim"].update(statement="Every problem is solved"),
            lambda h: h.update(theorem_spine_node="OTHER"),
            lambda h: h.update(support_route_class="CONTINUUM_PROOF"),
            lambda h: h.update(certification_route_id="MC-ROUTE-OTHER"),
            lambda h: h["trust_quartet"]["WHAT_IS_PROVED"].update(claim_ids=["CANARY-CLAIM-001"]),
            lambda h: h.update(promotion_id="MS-CAT-PROMOTION-OTHER"),
            lambda h: h.update(record_class="PRODUCTION"),
            lambda h: h["independent_verification"].update(disposition="EVIDENCE_SUBMITTED"),
        ]
        for change in cases:
            h = copy.deepcopy(self.h)
            change(h)
            self.assertTrue(validate_handoff(h, self.root, self.roots, canary=True))
        self.assertTrue(validate_handoff(self.d["catalog_source"], self.root, self.roots, canary=True))

    def test_each_handoff_field_required(self):
        for field in self.h:
            h = copy.deepcopy(self.h)
            del h[field]
            self.assertTrue(validate_handoff(h, self.root, self.roots, canary=True), field)

    def test_wp06_complete_without_claim_expansion(self):
        from ci.validate_chaidez_documentary_migration import WP06, validate_wp06
        d = json.loads((ROOT / WP06).read_text())
        self.assertEqual(validate_wp06(d), [])
        for field in d["result_status"]:
            mutated = copy.deepcopy(d)
            del mutated["result_status"][field]
            self.assertTrue(validate_wp06(mutated))
        for field in d["theorem_spine"][0]:
            mutated = copy.deepcopy(d)
            del mutated["theorem_spine"][0][field]
            self.assertTrue(validate_wp06(mutated))
        for field in d["proof_debt"][0]:
            mutated = copy.deepcopy(d)
            del mutated["proof_debt"][0][field]
            self.assertTrue(validate_wp06(mutated))
        d["result_status"]["strongest_supported_claim"] = "Frankl is proved for every family."
        self.assertTrue(validate_wp06(d))

    def test_eleven_generic_handoffs_and_rm_dio_legacy_preserved(self):
        from ci.validate_chaidez_documentary_migration import validate_legacy
        self.assertEqual(validate_legacy(), [])


if __name__ == "__main__":
    unittest.main()
