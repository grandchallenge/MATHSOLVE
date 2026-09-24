"""Materialize tracked, deterministic test repositories. Never admits production."""
from __future__ import annotations
import json
import os
import shutil
import subprocess
from pathlib import Path
from ci.chaidez_contract import ROOT, git, hashes

FIXTURE = ROOT / "tests/fixtures/external_catalog_promotion"


def commit(root):
    git(root, "add", "--all")
    env = {**os.environ, "GIT_AUTHOR_NAME": "Synthetic Canary", "GIT_COMMITTER_NAME": "Synthetic Canary",
           "GIT_AUTHOR_EMAIL": "canary@example.invalid", "GIT_COMMITTER_EMAIL": "canary@example.invalid",
           "GIT_AUTHOR_DATE": "2000-01-01T00:00:00+0000", "GIT_COMMITTER_DATE": "2000-01-01T00:00:00+0000"}
    subprocess.run(["git", "-C", str(root), "-c", "commit.gpgsign=false", "commit", "--allow-empty", "-qm", "Non-authoritative fixture"], check=True, env=env)
    git(root, "update-ref", "refs/remotes/origin/main", "HEAD")
    return git(root, "rev-parse", "HEAD").decode().strip()


def initialize(root, source=None):
    if source and source.exists():
        shutil.copytree(source, root)
    else:
        root.mkdir(parents=True)
    git(root, "init", "-q", "--initial-branch=main")
    git(root, "config", "core.autocrlf", "false")


def ref(root, path):
    return {"path": path, **hashes((Path(root) / path).read_bytes())}


def materialize(parent):
    """The checked-in payloads must replay unchanged, including their source pins."""
    roots = {}
    for name in ("forge", "programme", "solve"):
        root = Path(parent) / name
        if name == "solve":
            initialize_solve(root)
            shutil.copytree(FIXTURE / name, root, dirs_exist_ok=True)
        else:
            initialize(root, FIXTURE / name)
        commit(root)
        roots["grandchallenge/" + {"forge": "MATHFORGE", "programme": "MATH-PROGRAMME", "solve": "MATHSOLVE"}[name]] = root
    return roots


def initialize_solve(root):
    initialize(root)
    shutil.copytree(FIXTURE / "solve/work_packages", root / "work_packages")
    return commit(root)


def write_json(root, path, data):
    """Test mutation helper: artifacts are deliberately edited and re-pinned."""
    target = Path(root) / path
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")


def repin_bundle(root, dossier):
    """Keep structural sidecars in sync for adversarial *semantic* mutations."""
    for role, value in (("CLAIM_LEDGER", {"local_claims": dossier["local_claims"]}),
                        ("THEOREM_SPINE", {"theorem_spine": dossier["theorem_spine"]}),
                        ("PROOF_DEBT_REGISTER", {"proof_debt": dossier["proof_debt"]}),
                        ("DEPENDENCY_DAG", {n["node_id"]: n["dependencies"] for n in dossier["theorem_spine"]}),
                        ("CERT_HANDOFF", {"certification_state": "NOT_CERTIFIED", "local_claims": dossier["local_claims"], "trust_quartet": dossier["trust_quartet"]})):
        path = dossier["required_artifacts"][role]["path"]
        write_json(root, path, value)
        dossier["required_artifacts"][role] = ref(root, path)
    git(root, "add", "--all")
    return dossier
