from __future__ import annotations

import copy
import importlib.util
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "validate_openai_ten_proofs_downstream_certification_observation",
    ROOT / "ci/validate_openai_ten_proofs_downstream_certification_observation.py",
)
assert SPEC and SPEC.loader
M = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(M)


class DownstreamCertificationObservationTests(unittest.TestCase):
    def setUp(self) -> None:
        self.record = M.load(M.RECORD)
        self.schema = M.load(M.SCHEMA)
        self.blobs = {name: expected for name, (_, expected) in M.FILES.items()}

    def errors(self, *, record=None, schema=None, blobs=None):
        return M.validation_errors(
            record=copy.deepcopy(self.record if record is None else record),
            schema=copy.deepcopy(self.schema if schema is None else schema),
            blobs=copy.deepcopy(self.blobs if blobs is None else blobs),
        )

    def test_baseline(self):
        self.assertEqual([], self.errors())

    def test_handoff_registry_drift(self):
        blobs = copy.deepcopy(self.blobs)
        blobs["handoff_registry"] = "0" * 40
        self.assertTrue(self.errors(blobs=blobs))

    def test_packet_drift(self):
        for key in ("ehrhart_packet", "compactness_packet", "two_degenerate_packet"):
            with self.subTest(key=key):
                blobs = copy.deepcopy(self.blobs)
                blobs[key] = "0" * 40
                self.assertTrue(self.errors(blobs=blobs))

    def test_cert_closure_drift(self):
        record = copy.deepcopy(self.record)
        record["mathcert_authority"]["documentary_closure_merge"] = "0" * 40
        self.assertTrue(self.errors(record=record))

    def test_solve_adjudication_authority_inflation(self):
        record = copy.deepcopy(self.record)
        record["solve_authority"]["owns_adjudication"] = True
        self.assertTrue(self.errors(record=record))

    def test_packet_mutation_admitted(self):
        record = copy.deepcopy(self.record)
        record["observed_family_state"][0]["producer_packet_unchanged"] = False
        self.assertTrue(self.errors(record=record))

    def test_compactness_qualification_inflation(self):
        record = copy.deepcopy(self.record)
        record["observed_family_state"][1]["route_state"] = "qualified"
        self.assertTrue(self.errors(record=record))

    def test_aggregate_handoff_insertion(self):
        record = copy.deepcopy(self.record)
        record["aggregate_handoff"] = {"path": "forged.json"}
        self.assertTrue(self.errors(record=record))

    def test_proof_promotion(self):
        record = copy.deepcopy(self.record)
        record["mathematical_targets_marked_proved"] = 1
        self.assertTrue(self.errors(record=record))

    def test_blocker_removal(self):
        record = copy.deepcopy(self.record)
        record["preserved_limitations"]["blocked_repair_lanes"] = []
        self.assertTrue(self.errors(record=record))

    def test_open_schema(self):
        schema = copy.deepcopy(self.schema)
        schema["additionalProperties"] = True
        self.assertTrue(self.errors(schema=schema))

    def test_unexpected_authority_field(self):
        record = copy.deepcopy(self.record)
        record["solve_certification_authority"] = True
        self.assertTrue(self.errors(record=record))


if __name__ == "__main__":
    unittest.main()
