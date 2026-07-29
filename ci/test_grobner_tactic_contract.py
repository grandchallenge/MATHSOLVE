from __future__ import annotations

import json
import shutil
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from ci import validate_solve


class GroebnerTacticContractTests(unittest.TestCase):
    def setUp(self) -> None:
        self.source_root = Path(__file__).resolve().parents[1]
        self.temp_dir = tempfile.TemporaryDirectory()
        self.root = Path(self.temp_dir.name)
        (self.root / "schemas").mkdir(parents=True)
        (self.root / "governance").mkdir(parents=True)
        (self.root / "examples" / "grobner_tactic_invocations").mkdir(parents=True)
        for name in (
            "grobner_tactic_invocation.schema.json",
            "grobner_tactic_registry.schema.json",
        ):
            shutil.copy2(self.source_root / "schemas" / name, self.root / "schemas" / name)
        shutil.copy2(
            self.source_root / "governance" / "grobner_tactic_registry.json",
            self.root / "governance" / "grobner_tactic_registry.json",
        )
        shutil.copy2(
            self.source_root / "examples" / "grobner_tactic_invocations" / "GB-TACTIC-DEMO-001.json",
            self.root / "examples" / "grobner_tactic_invocations" / "GB-TACTIC-DEMO-001.json",
        )

    def tearDown(self) -> None:
        self.temp_dir.cleanup()

    def errors(self) -> list[str]:
        with (
            patch.object(validate_solve, "ROOT", self.root),
            patch.object(validate_solve, "WORKSPACE", self.root.parent),
            patch.object(
                validate_solve,
                "GROBNER_REGISTRY_PATH",
                self.root / "governance" / "grobner_tactic_registry.json",
            ),
            patch.object(
                validate_solve,
                "GROBNER_INVOCATION_DIR",
                self.root / "examples" / "grobner_tactic_invocations",
            ),
        ):
            return validate_solve.grobner_tactic_errors()

    def load_invocation(self) -> tuple[Path, dict]:
        path = self.root / "examples" / "grobner_tactic_invocations" / "GB-TACTIC-DEMO-001.json"
        return path, json.loads(path.read_text(encoding="utf-8"))

    def rewrite_registry(self, path: Path, *, status: str | None = None) -> None:
        registry_path = self.root / "governance" / "grobner_tactic_registry.json"
        registry = json.loads(registry_path.read_text(encoding="utf-8"))
        registry["invocations"][0]["git_blob_sha1"] = validate_solve.git_blob_sha1(path)
        if status is not None:
            registry["invocations"][0]["status"] = status
        registry_path.write_text(json.dumps(registry, indent=2) + "\n", encoding="utf-8")

    def mutate(self, callback, *, status: str | None = None) -> list[str]:
        path, invocation = self.load_invocation()
        callback(invocation)
        path.write_text(json.dumps(invocation, indent=2) + "\n", encoding="utf-8")
        self.rewrite_registry(path, status=status)
        return self.errors()

    def test_committed_fixture_is_valid(self) -> None:
        self.assertEqual([], self.errors())

    def test_rejects_global_open_problem_encoding(self) -> None:
        errors = self.mutate(lambda item: item.__setitem__("global_open_problem_encoding", True))
        self.assertTrue(any("global_open_problem_encoding" in error for error in errors))

    def test_rejects_ready_without_content_addressed_witness(self) -> None:
        errors = self.mutate(lambda item: item.__setitem__("witness_source", None))
        self.assertTrue(any("requires content-addressed witness_source" in error for error in errors))

    def test_rejects_submitted_without_acknowledgement(self) -> None:
        errors = self.mutate(
            lambda item: item.__setitem__("status", "submitted"),
            status="submitted",
        )
        self.assertTrue(any("requires MATHCERT intake acknowledgement" in error for error in errors))

    def test_rejects_certified_without_output(self) -> None:
        def change(item: dict) -> None:
            item["status"] = "certified"
            item["handoff"]["intake_acknowledgement"] = "MC-INTAKE-DEMO"

        errors = self.mutate(change, status="certified")
        self.assertTrue(any("requires content-addressed MATHCERT output" in error for error in errors))

    def test_rejects_rejected_without_failure_record(self) -> None:
        def change(item: dict) -> None:
            item["status"] = "rejected"
            item["handoff"]["intake_acknowledgement"] = "MC-INTAKE-DEMO"
            item["handoff"]["mathcert_output"] = {
                "repository": "grandchallenge/MATHCERT",
                "commit_sha": "a" * 40,
                "path": "certificates/demo.json",
                "digest_algorithm": "git_blob_sha1",
                "digest": "b" * 40,
                "disposition": "rejected"
            }

        errors = self.mutate(change, status="rejected")
        self.assertTrue(any("requires a failure record" in error for error in errors))

    def test_rejects_unregistered_invocation(self) -> None:
        orphan = self.root / "examples" / "grobner_tactic_invocations" / "ORPHAN.json"
        orphan.write_text("{}\n", encoding="utf-8")
        self.assertTrue(any("unregistered invocation" in error for error in self.errors()))

    def test_rejects_blob_drift(self) -> None:
        path, invocation = self.load_invocation()
        invocation["notes"] += " drift"
        path.write_text(json.dumps(invocation, indent=2) + "\n", encoding="utf-8")
        self.assertTrue(any("git_blob_sha1 mismatch" in error for error in self.errors()))


if __name__ == "__main__":
    unittest.main()
