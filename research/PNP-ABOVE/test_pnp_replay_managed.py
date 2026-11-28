import hashlib
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch
from PNP_REPLAY_MANAGED import on_ssd,managed_preflight,verify_staged_sources

class ManagedGuardTests(unittest.TestCase):
    def test_wrong_workspace_rejected_before_launcher(self):
        with tempfile.TemporaryDirectory() as d, patch('subprocess.check_output') as run:
            with self.assertRaisesRegex(SystemExit,'STAGED_WORKSPACE'):
                managed_preflight(Path(d),Path(d)/'new')
            run.assert_not_called()

    def test_existing_output_rejected(self):
        with tempfile.TemporaryDirectory() as d:
            p=Path(d); u=p/'work'; u.mkdir(); out=u/'old'; out.mkdir()
            with patch('PNP_REPLAY_MANAGED.ROOT',p), patch('subprocess.check_output') as run:
                with self.assertRaisesRegex(SystemExit,'STAGED_WORKSPACE'):
                    managed_preflight(u,out)
                run.assert_not_called()

    def test_symlink_escape_rejected(self):
        with tempfile.TemporaryDirectory() as d:
            p=Path(d); s=p/'ssd'; s.mkdir(); t=p/'hdd'; t.mkdir()
            alias=s/'alias'; alias.symlink_to(t,target_is_directory=True)
            with patch('PNP_REPLAY_MANAGED.SSD',(s,)):
                self.assertFalse(on_ssd(alias))

    def test_staged_source_identity(self):
        with tempfile.TemporaryDirectory() as d:
            p=Path(d); source=p/'file.lean'; source.write_bytes(b'theorem test : True := trivial\n')
            b=source.read_bytes(); oid=hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()
            raw=('100644 blob '+oid+'\tfile.lean\0').encode()
            with patch('PNP_REPLAY_MANAGED.SSD',(p,)), patch('subprocess.check_output',return_value=raw):
                self.assertEqual(verify_staged_sources(p,{'repository':d}),1)
                source.write_bytes(b'changed')
                with self.assertRaisesRegex(SystemExit,'STAGED_SOURCE_MISMATCH'):
                    verify_staged_sources(p,{'repository':d})

if __name__=='__main__': unittest.main()
