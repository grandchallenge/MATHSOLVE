# MS-FC-WP00 — Canonical RH and NS-CI Lean targets

## Purpose

This package supplies Programme-routed Lean target interfaces for `RH-001` and
`NS-CI-001`. It consumes the `FC-GDM-001` source lane. It does not consume the
expanded `FC-GDM-002` campaign evidence.

## RH-001

`ProgrammeRiemannHypothesis` expands the zero taxonomy explicitly and is
definitionally equal to mathlib's `RiemannHypothesis`. The carrier is mathlib's
meromorphically continued `riemannZeta`; differentiability away from the pole at
one is replayed from mathlib. ERH, GRH, density statements, finite-height checks,
and equivalent criteria are excluded.

## NS-CI-001

`UniversalCriticalIntegrability` quantifies over positive viscosity, Schwartz
initial data on `R^3`, every unforced Leray–Hopf solution, and every finite
positive time horizon. `criticalL4L6` stores the time exponent first and the
space exponent second. The Leray–Hopf predicate, mixed-norm predicate, and
positive Clay alternative are explicit imported axioms. This avoids presenting
an unavailable PDE library as formalized mathematics.

`CriticalIntegrabilityImpliesClay` is a proposition naming the one-way bridge.
It is not a theorem. No reverse implication is stated.

## Replay

```text
lake build
lake env lean MathSolve/FormalConjectures/Replay.lean
python ci/validate_formal_conjectures_targets.py
PYTHONPATH=ci python -m unittest ci/test_formal_conjectures_targets.py -v
```

## Promotion boundary

Successful elaboration establishes statement identity and interface integrity
only. It does not prove RH, universal critical integrability, the continuation
bridge, or global Navier–Stokes regularity. MATHCERT must independently replay
the exact merged package before recording any certification disposition.
