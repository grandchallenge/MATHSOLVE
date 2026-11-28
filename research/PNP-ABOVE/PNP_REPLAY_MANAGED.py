"""Managed CHAD adapter: all Lean invocations go through gcl-lean-work.

The caller retains its exact theorem/source/axiom checks. No compiler
execution on HDD, and no mutation of shared predecessor build objects.
"""
import atexit
import hashlib
import json
import os
import shutil
import subprocess
from pathlib import Path
from PNP_REPLAY_PREFLIGHT import bounded_run

ROOT=Path('/mnt/gcl-lean-work/workspaces')
SSD=(Path('/mnt/gcl-lean-work'),Path('/mnt/gcl-lean-ssd'))
UPSTREAM='5926bdff5db621f44682a101007ef2fe3ae8d970'
PIN='leanprover/lean4:v4.35.0-rc3'
LAUNCHER=Path.home()/'.local/bin/gcl-lean-work'

def on_ssd(path):
    return any(path.resolve().is_relative_to(root) for root in SSD)

def verify_staged_sources(u, stage):
    """Verify the managed Git archive against the pinned tree, not just its marker."""
    repo=Path(stage['repository'])
    raw=subprocess.check_output(['git','ls-tree','-r','-z',UPSTREAM],cwd=repo,timeout=30)
    count=0
    for row in raw.split(b'\0'):
        if not row:
            continue
        meta,name=row.split(b'\t',1)
        mode,kind,oid=meta.decode().split()
        f=u/os.fsdecode(name)
        if kind!='blob' or mode not in ('100644','100755') or f.is_symlink() or not on_ssd(f):
            raise SystemExit('PNP_MANAGED_REPLAY_INVALID_STAGED_ENTRY: '+str(f))
        data=f.read_bytes()
        digest=hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest()
        if digest!=oid:
            raise SystemExit('PNP_MANAGED_REPLAY_STAGED_SOURCE_MISMATCH: '+str(f))
        count+=1
    if count==0:
        raise SystemExit('PNP_MANAGED_REPLAY_EMPTY_SOURCE_TREE')
    return count

def managed_preflight(u,d):
    u,d=Path(u).resolve(),Path(d).resolve()
    if u.parent!=ROOT or not d.is_relative_to(u) or d.exists():
        raise SystemExit('PNP_MANAGED_REPLAY_REQUIRES_NEW_OUTPUT_IN_STAGED_WORKSPACE')
    status=subprocess.check_output([str(LAUNCHER),'status'],text=True,timeout=15)
    stage=dict(line.split('=',1) for line in (u/'.gcl-source').read_text().splitlines())
    if stage['commit']!=UPSTREAM or stage['subdirectory']!='.':
        raise SystemExit('PNP_MANAGED_REPLAY_UPSTREAM_STAGE_MISMATCH')
    checked_sources=verify_staged_sources(u,stage)
    if (u/'lean-toolchain').read_text().strip()!=PIN:
        raise SystemExit('PNP_MANAGED_REPLAY_TOOLCHAIN_MISMATCH')
    manifest=(u/'lake-manifest.json').read_bytes()
    sha=hashlib.sha256(manifest).hexdigest()
    if (u/'.gcl-manifest.sha256').read_text().split()[0]!=sha:
        raise SystemExit('PNP_MANAGED_REPLAY_MANIFEST_MISMATCH')
    revs={}
    for pkg in json.loads(manifest)['packages']:
        name=pkg['name'].strip('«»')
        path=u/'.lake/packages'/name
        if not on_ssd(path):
            raise SystemExit('PNP_MANAGED_REPLAY_NON_SSD_PACKAGE')
        rev=subprocess.check_output(['git','rev-parse','HEAD'],cwd=path,text=True,timeout=15).strip()
        if rev!=pkg['rev']:
            raise SystemExit('PNP_MANAGED_REPLAY_PACKAGE_REV_MISMATCH: '+name)
        subprocess.run(['git','diff','--quiet','HEAD','--'],cwd=path,check=True,timeout=30)
        revs[name]=rev
    free=shutil.disk_usage(u).free
    if free<2*1024**3:
        raise SystemExit('PNP_MANAGED_REPLAY_CAPACITY_BLOCKED')
    base=[str(LAUNCHER),'run',u.name,'lake','env']
    version=subprocess.check_output(base+['lean','--version'],text=True,timeout=45)
    if 'version 4.35.0-rc3,' not in version:
        raise SystemExit('PNP_MANAGED_REPLAY_COMPILER_MISMATCH')
    paths=subprocess.check_output(base+['printenv','LEAN_PATH'],text=True,timeout=45).splitlines()[-1].split(':')
    for path in paths:
        if not path or not on_ssd(u/path):
            raise SystemExit('PNP_MANAGED_REPLAY_NON_SSD_LEAN_PATH: '+path)
    build=u/'.lake/build/lib/lean'
    if not on_ssd(build) or not build.is_dir() or (build/'PNPAbove').exists() or (build/'PNPAbove').is_symlink():
        raise SystemExit('PNP_MANAGED_REPLAY_BUILD_NAMESPACE_NOT_FRESH')
    record={'schema':'PNP_REPLAY_PLACEMENT/1','runner':'CHAD-managed-SSD',
            'workspace':str(u),'upstream_stage':stage,'checked_source_blobs':checked_sources,'manifest_sha256':sha,
            'package_revisions':revs,'version':version,'lean_path':paths,
            'launcher_sha256':hashlib.sha256(LAUNCHER.read_bytes()).hexdigest(),
            'free_bytes':free,'status':status}
    return base,record

def managed_runner(u,d,target,base):
    link=u/'.lake/build/lib/lean/PNPAbove'
    link.symlink_to(target,target_is_directory=True)
    def cleanup():
        if link.is_symlink() and link.resolve()==target.resolve():
            link.unlink()
    atexit.register(cleanup)
    def run(args,log):
        bounded_run(base+['lean','-R',str(d),*map(str,args)],
                    cwd=u,env=os.environ.copy(),log=d/log,
                    receipt=d/'execution.jsonl',seconds=330)
    return run
