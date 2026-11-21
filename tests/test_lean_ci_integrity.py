"""Negative controls for the required fail-closed Lean workflow boundary."""
from __future__ import annotations

import contextlib
import io
import pathlib
import sys
import tempfile
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "ci"))

import checked_lean
import validate_lean_ci_integrity as workflow_guard


class CheckedLeanProcessTests(unittest.TestCase):
    def run_fake(
        self, body: str, *, exit_status: int = 0, require: tuple[str, ...] = (),
        strict: bool = False, save: bool = False,
    ) -> tuple[int, str, str, str | None]:
        with tempfile.TemporaryDirectory() as temp:
            root = pathlib.Path(temp)
            fake = root / "lean"
            fake.write_text(
                "#!/usr/bin/env python3\n"
                "import sys\n"
                + body + "\n"
                + f"sys.exit({exit_status})\n",
                encoding="utf-8",
            )
            fake.chmod(0o755)
            saved = root / "captured.log" if save else None
            stdout, stderr = io.StringIO(), io.StringIO()
            with contextlib.redirect_stdout(stdout), contextlib.redirect_stderr(stderr):
                status = checked_lean.check_lean(
                    [str(fake), "Proof.lean"], output=saved,
                    require_axioms=require, strict_warnings=strict,
                )
            content = saved.read_text(encoding="utf-8") if saved else None
            return status, stdout.getvalue(), stderr.getvalue(), content

    def test_clean_compilation_and_required_axiom_output(self):
        code, output, diagnostic, captured = self.run_fake(
            'print("\'T.good\' depends on axioms: [propext, Quot.sound]")',
            require=("T.good",), strict=True, save=True,
        )
        self.assertEqual(code, 0)
        self.assertIn("T.good", output)
        self.assertIn("PASS:", diagnostic)
        self.assertEqual(captured, output)

    def test_compiler_nonzero_cannot_be_masked_by_healthy_report(self):
        code, _, diagnostic, _ = self.run_fake(
            'print("\'T.good\' depends on axioms: [propext]")',
            exit_status=17, require=("T.good",),
        )
        self.assertEqual(code, 1)
        self.assertIn("exit status 17", diagnostic)

    def test_zero_exit_with_file_prefixed_error_is_a_failure(self):
        code, _, diagnostic, _ = self.run_fake(
            'print("Proof.lean:99:12: error: unsolved goals")')
        self.assertEqual(code, 1)
        self.assertIn("error diagnostic", diagnostic)

    def test_indented_multiline_sorry_axiom_is_a_failure(self):
        code, _, diagnostic, _ = self.run_fake(
            'print("\'T.bad\' depends on axioms: [propext,\\n  sorryAx,\\n  Quot.sound]")')
        self.assertEqual(code, 1)
        self.assertIn("sorryAx", diagnostic)

    def test_ansi_diagnostic_is_not_hidden(self):
        code, _, diagnostic, _ = self.run_fake(
            'print("\\x1b[31mProof.lean:2:4: error: unsolved goals\\x1b[0m")')
        self.assertEqual(code, 1)
        self.assertIn("error diagnostic", diagnostic)

    def test_warnings_are_rejected_in_strict_mode(self):
        body = 'print("Proof.lean:2:7: warning: unused simp argument")'
        self.assertEqual(self.run_fake(body, strict=False)[0], 0)
        self.assertEqual(self.run_fake(body, strict=True)[0], 1)

    def test_zero_exit_sorry_warning_rejected_even_outside_strict_mode(self):
        code, _, diagnostic, _ = self.run_fake(
            'print("Proof.lean:4: warning: declaration uses sorry")',
            strict=False,
        )
        self.assertEqual(code, 1)
        self.assertIn("proof-placeholder warning", diagnostic)

    def test_stderr_error_even_on_zero_exit_rejected(self):
        code, _, diagnostic, _ = self.run_fake(
            'print("Proof.lean:5: error: invalid proof", file=sys.stderr)')
        self.assertEqual(code, 1)
        self.assertIn("error diagnostic", diagnostic)

    def test_required_axiom_report_must_exist(self):
        code, _, diagnostic, _ = self.run_fake('print("Lean finished")', require=("T.required",))
        self.assertEqual(code, 1)
        self.assertIn("missing axiom reports", diagnostic)

    def test_non_lean_command_and_missing_binary_fail(self):
        self.assertEqual(checked_lean.check_lean(["bash", "-c", "true"]), 2)
        self.assertEqual(checked_lean.check_lean(["/missing/lean", "File.lean"]), 127)

    def test_command_schema_recognizes_lake_build_and_lean(self):
        self.assertTrue(checked_lean.is_lean_command(["lake", "env", "lean", "File.lean"]))
        self.assertTrue(checked_lean.is_lean_command(["lake", "build"]))
        self.assertTrue(checked_lean.is_lean_command(["lean", "File.lean"]))
        self.assertFalse(checked_lean.is_lean_command(["lake", "env", "sh", "true"]))
        self.assertFalse(checked_lean.is_lean_command([]))


class WorkflowSourceGuardTests(unittest.TestCase):
    def check(self, run: str, *, path: str = ".github/workflows/ci.yml",
              job: str = "formal-targets", failfast: bool = True) -> list[str]:
        if failfast and not run.startswith("set -euo pipefail"):
            run = "set -euo pipefail\n" + run
        return workflow_guard.errors_for_run(
            run, relative_path=path, job=job, step_name="Test",
        )

    def test_raw_lean_compilation_rejected_even_without_tee(self):
        self.assertTrue(self.check("lake env lean Foo.lean"))
        self.assertTrue(self.check("set -euo pipefail\nlake env lean Foo.lean"))
        self.assertTrue(self.check("lean File.lean"))
        self.assertTrue(self.check("lake build"))

    def test_pipe_or_swallowed_wrapper_exit_rejected(self):
        self.assertTrue(self.check(
            "python ci/checked_lean.py -- lake env lean File.lean | tee out.log"))
        self.assertTrue(self.check(
            "python ci/checked_lean.py -- lake env lean File.lean || true"))
        self.assertTrue(self.check(
            "python ci/checked_lean.py -- lake env lean File.lean; true"))

    def test_direct_runner_accepted(self):
        self.assertEqual(self.check(
            "python ci/checked_lean.py -- lake env lean Foo.lean"), [])
        self.assertEqual(self.check(
            'python "$GITHUB_WORKSPACE/ci/checked_lean.py" -- lake env lean File.lean'), [])
        self.assertEqual(self.check(
            "python ci/checked_lean.py -- lake build"), [])
        self.assertEqual(self.check("lean --version"), [])

    def test_multiline_pipes_rejected_but_quoted_grep_pipes_allowed(self):
        self.assertTrue(self.check(
            "python ci/checked_lean.py -- lake env lean Proof.lean \\\n"
            " | tee /tmp/lean.log"
        ))
        self.assertEqual(self.check(
            "python ci/checked_lean.py -- lake env lean Proof.lean\n"
            "grep -E 'sorryAx|error:|warning:' /tmp/check.log"
        ), [])

    def test_actual_set_plus_e_false_green_bypass_is_rejected(self):
        source = ("set -euo pipefail\nset +e\n"
                  "python ci/checked_lean.py -- lake env lean Bad.lean\ntrue")
        self.assertTrue(self.check(source))
        self.assertTrue(self.check(
            "set -euo pipefail\nset +o errexit\n"
            "python ci/checked_lean.py -- lake env lean Bad.lean\ntrue"
        ))
        self.assertTrue(self.check(
            "set -euo pipefail\ntrap 'exit 0' ERR\n"
            "python ci/checked_lean.py -- lake env lean Bad.lean"
        ))

    def test_spoofed_python_command_is_not_a_runner(self):
        source = (
            'python -c "print(\'checked_lean.py\')" -- lake env lean Bad.lean'
        )
        self.assertTrue(self.check(source))
        self.assertTrue(self.check(
            'python other.py checked_lean.py -- lake env lean Bad.lean'
        ))
        self.assertFalse(workflow_guard.is_checked_runner_prefix(
            'python -c "print(\'checked_lean.py\')" --'
        ))
        self.assertTrue(workflow_guard.is_checked_runner_prefix(
            'python ci/checked_lean.py --strict-warnings '
            '--require-axiom MathSolve.Erdos602.x --output /tmp/axioms.txt --'
        ))
        self.assertTrue(workflow_guard.is_checked_runner_prefix(
            'python "$GITHUB_WORKSPACE/ci/checked_lean.py" --'
        ))

    def test_failfast_header_missing_is_rejected(self):
        self.assertTrue(self.check(
            "python ci/checked_lean.py -- lake env lean Bad.lean",
            failfast=False,
        ))

    def test_external_container_only_under_exact_pinned_fail_fast_route(self):
        legitimate = (
            "docker run --rm ghcr.io/ottogin/lean-mathlib@sha256:aabbcc "
            "bash -lc 'set -euo pipefail; lean --version; "
            "lean /tmp/H7_D3.lean; lean /tmp/H7_D4.lean'"
        )
        path, job = workflow_guard.ALLOWED_EXTERNAL
        self.assertEqual(self.check(legitimate, path=path, job=job), [])
        self.assertTrue(self.check(legitimate.replace("set -euo pipefail;", "set -e;"),
                                   path=path, job=job))
        self.assertTrue(self.check(legitimate + " | tee /tmp/out", path=path, job=job))
        self.assertTrue(self.check(legitimate, path=path, job="other"))

    def test_required_ledgers_binding_and_all_workflows(self):
        with tempfile.TemporaryDirectory() as temp:
            root = pathlib.Path(temp)
            (root / "ci").mkdir()
            (root / "ci/checked_lean.py").write_text("# test stub\n")
            d = root / ".github/workflows"
            d.mkdir(parents=True)
            (d / "ci.yml").write_text(
                "jobs:\n"
                "  ledgers:\n"
                "    steps:\n"
                "      - name: Assert Lean workflow execution safety\n"
                "        run: |\n"
                "          python ci/validate_lean_ci_integrity.py\n"
                "          python -m unittest tests/test_lean_ci_integrity.py -v\n"
                "  formal-targets:\n"
                "    steps:\n"
                "      - run: |\n"
                "          set -euo pipefail\n"
                "          python ci/checked_lean.py -- lake env lean Foo.lean\n",
                encoding="utf-8",
            )
            self.assertEqual(workflow_guard.scan(root), [])
            (d / "extra.yml").write_text(
                "jobs:\n  formal:\n    steps:\n"
                "      - run: lake env lean Other.lean | tee /tmp/log\n",
                encoding="utf-8",
            )
            self.assertTrue(any("must use checked_lean.py" in s
                                for s in workflow_guard.scan(root)))
            (d / "extra.yml").unlink()
            (d / "ci.yml").write_text(
                (d / "ci.yml").read_text().replace(
                    "python ci/validate_lean_ci_integrity.py",
                    "echo missing-security-validator"
                )
            )
            self.assertTrue(any("required ledgers" in s for s in workflow_guard.scan(root)))


if __name__ == "__main__":
    unittest.main()
