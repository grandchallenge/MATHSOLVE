#!/usr/bin/env python3
"""Hostile and golden cache tests against an actual pinned full replay."""
import copy
import json
import os
from pathlib import Path
import shutil
import tempfile
import unittest
from unittest.mock import patch

import PNP_REPLAY_CACHE as cache


class CacheTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.gcl = Path(os.environ["PNP_GCL_ROOT"])
        cls.upstream = Path(os.environ["PNP_UPSTREAM_ROOT"])
        cls.full = Path(os.environ["PNP_FULL_REPLAY_ROOT"])
        cls.key, cls.data = cache.inputs(cls.upstream, cls.gcl)

    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory(prefix="pnp-cache-test-")
        self.addCleanup(self.cleanup_tmp)
        self.root = Path(self.tmp.name) / "cache"
        self.root.mkdir(mode=0o700)

    def cleanup_tmp(self):
        for base, dirs, files in os.walk(self.tmp.name, topdown=True, followlinks=False):
            for directory in dirs:
                p = Path(base) / directory
                if not p.is_symlink():
                    p.chmod(0o700)
        self.tmp.cleanup()

    def seed(self):
        entry = cache.cache_entry(self.root, self.key)
        cache.publish_seed(self.root, entry, self.key, self.data,
                           self.full, self.gcl)
        return entry

    def test_01_seed_restore_validate_all_65(self):
        entry = self.seed()
        self.assertEqual(len(cache.verify_entry(entry, self.key, self.data)["payload"]), 65)
        restored = Path(self.tmp.name) / "restored"
        cache.restore(entry, self.key, self.data, restored)
        self.assertEqual(len(list((restored / "PNPAbove").glob("*.olean"))), 65)
        self.assertFalse(json.loads((restored / "cache_dev_receipt.json").read_text())["admission_eligible"])

    def test_02_warm_repeat_seed_idempotent(self):
        entry = self.seed()
        one = cache.verify_entry(entry, self.key, self.data)
        two = cache.publish_seed(self.root, entry, self.key, self.data,
                                 self.full, self.gcl)
        self.assertEqual(one, two)

    def test_03_corrupted_olean_rejected(self):
        entry = self.seed()
        p = entry / "PNPAbove/WP23Probe.olean"
        p.chmod(0o600)
        with p.open("ab") as file:
            file.write(b"HOSTILE-OLEAN")
        with self.assertRaisesRegex(cache.Invalid, "CACHE_PAYLOAD_CORRUPT"):
            cache.verify_entry(entry, self.key, self.data)

    def test_04_corrupted_source_rejected(self):
        entry = self.seed()
        p = entry / "PNPAbove/WP08.lean"
        p.chmod(0o600)
        with p.open("ab") as file:
            file.write(b"-- accidental-source-drift")
        with self.assertRaisesRegex(cache.Invalid, "CACHE_PAYLOAD_CORRUPT"):
            cache.verify_entry(entry, self.key, self.data)

    def test_05_changed_manifest_fingerprint_rejected(self):
        entry = self.seed()
        changed = copy.deepcopy(self.data)
        changed["manifests"]["WP23A"] = "0" * 64
        with self.assertRaisesRegex(cache.Invalid, "CACHE_ENTRY_INPUTS_MISMATCH"):
            cache.verify_entry(entry, self.key, changed)

    def test_06_changed_toolchain_fingerprint_rejected(self):
        entry = self.seed()
        changed = copy.deepcopy(self.data)
        changed["environment"]["lean_executable_sha256"] = "0" * 64
        with self.assertRaisesRegex(cache.Invalid, "CACHE_ENTRY_INPUTS_MISMATCH"):
            cache.verify_entry(entry, self.key, changed)

    def test_07_missing_module_rejected(self):
        entry = self.seed()
        p = entry / "PNPAbove/WP22Gap.olean"
        p.parent.chmod(0o700)
        p.chmod(0o600)
        p.unlink()
        with self.assertRaisesRegex(cache.Invalid, "FILE_MISSING_OR_SYMLINK"):
            cache.verify_entry(entry, self.key, self.data)

    def test_08_symlink_attack_rejected(self):
        entry = self.seed()
        p = entry / "PNPAbove/WP23Probe.olean"
        p.parent.chmod(0o700)
        p.chmod(0o600)
        p.unlink()
        p.symlink_to(self.full / "PNPAbove/WP23Probe.olean")
        with self.assertRaisesRegex(cache.Invalid, "FILE_MISSING_OR_SYMLINK"):
            cache.verify_entry(entry, self.key, self.data)

    def test_09_tampered_metadata_identity_rejected(self):
        entry = self.seed()
        p = entry / "metadata.json"
        doc = json.loads(p.read_text())
        doc["key"] = "f" * 64
        p.chmod(0o600)
        p.write_text(json.dumps(doc))
        with self.assertRaisesRegex(cache.Invalid, "CACHE_ENTRY_IDENTITY_MISMATCH"):
            cache.verify_entry(entry, self.key, self.data)

    def test_10_restore_never_overwrites_workspace(self):
        entry = self.seed()
        work = Path(self.tmp.name) / "existing"
        work.mkdir()
        (work / "important.txt").write_text("never overwrite")
        with self.assertRaisesRegex(cache.Invalid, "RESTORE_DESTINATION_ALREADY_EXISTS"):
            cache.restore(entry, self.key, self.data, work)
        self.assertEqual((work / "important.txt").read_text(), "never overwrite")

    def test_11_incomplete_full_replay_rejected(self):
        empty = Path(self.tmp.name) / "empty"
        empty.mkdir()
        with self.assertRaisesRegex(cache.Invalid, "FILE_MISSING_OR_SYMLINK"):
            cache.check_replay(empty, self.gcl, self.data["source"])

    def test_12_exact_head_ancestry_and_terminal_checked(self):
        result = cache.check_replay(self.full, self.gcl, self.data["source"])
        self.assertEqual(result["full_replay_candidate"],
                         "ebb9a2a6652506baa699b176955c4eb6150638ae")
        self.assertEqual(result["full_log_sha256"],
                         cache.digest_file(self.full.with_suffix(".log")))

    def test_13_new_source_provenance_drift_rejected(self):
        with patch.object(cache, "source_catalog", return_value={}):
            key, inputs = cache.inputs(self.upstream, self.gcl)
        self.assertNotEqual(key, self.key)
        self.assertNotEqual(inputs["source"], self.data["source"])

    def test_14_stage_source_inventory_includes_every_module(self):
        names = self.data["source"]
        self.assertEqual(len(names), 65)
        self.assertIn("WP08.lean", names)
        self.assertIn("WP22Gap.lean", names)
        self.assertIn("WP23Probe.lean", names)

    def test_15_reproducible_content_address(self):
        key2, _ = cache.inputs(self.upstream, self.gcl)
        self.assertEqual(self.key, key2)
        self.assertEqual(len(self.key), 64)

    def test_16_cache_entry_cannot_be_replaced_by_symlink(self):
        entry = self.seed()
        (entry / "PNPAbove").chmod(0o700)
        entry.chmod(0o700)
        shutil.rmtree(entry)
        entry.symlink_to(self.full)
        with self.assertRaisesRegex(cache.Invalid, "UNSAFE_DIRECTORY"):
            cache.verify_entry(entry, self.key, self.data)


if __name__ == "__main__":
    unittest.main(verbosity=2)
