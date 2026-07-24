# NS-CI-WP02 — Adversarial semantic review

**Review date:** 2026-07-23  
**Campaign:** `NS-CI-001`  
**Provider PR:** `grandchallenge/MATHSOLVE#21`

## Verdict

**APPROVE FOR REFEREE PROMOTION AS A SOURCE-NORMALIZED CONDITIONAL LEDGER.**

The package correctly reconstructs the classical conditional regularity chain at `(time,space)=(4,6)`, preserves the distinction between imported theorems and local derivations, and does not claim the critical integral is universally finite.

Promotion applies to the ledger and its one-way implication architecture. It does not certify the universal target, a new regularity criterion, or bidirectional equivalence with the Clay statement.

## Adversarial questions

The review tested whether the ledger:

1. uses a strong-level test before strong regularity is available;
2. hides pressure or time-regularity assumptions;
3. miscomputes the Holder, Gagliardo–Nirenberg, or Young exponents;
4. treats a formal weak–strong identity as an unconditional pointwise equality;
5. silently transfers between domains, data classes, or solution classes;
6. converts a one-way implication into equivalence;
7. replaces the universal Leray–Hopf quantifier by a selected solution;
8. uses computation or formal interfaces as analytic proof.

## CR-005 verification — `H^1` estimate

At the smooth or sufficiently strong level,

```math
\frac12\frac d{dt}\|\nabla u\|_2^2
+\nu\|\Delta u\|_2^2
=-\int (u\cdot\nabla)u\cdot\Delta u.
```

Holder uses `(6,3,2)`:

```math
\left|\int (u\cdot\nabla)u\cdot\Delta u\right|
\le \|u\|_6\|\nabla u\|_3\|\Delta u\|_2.
```

The three-dimensional interpolation

```math
\|\nabla u\|_3
\le C\|\nabla u\|_2^{1/2}\|\Delta u\|_2^{1/2}
```

gives

```math
C\|u\|_6\|\nabla u\|_2^{1/2}\|\Delta u\|_2^{3/2}.
```

Young with conjugate exponents `4/3` and `4`, taking the viscosity-weighted first factor proportional to `nu^(3/4)||Delta u||_2^(3/2)`, yields

```math
\frac\nu2\|\Delta u\|_2^2
+C\nu^{-3}\|u\|_6^4\|\nabla u\|_2^2.
```

The exponent `4` and viscosity power `-3` are correct.

The calculation remains explicitly conditional on test admissibility. WP01 fixtures `FP-005` and `FP-006` correctly block unconditional application to an arbitrary Leray–Hopf solution.

## CR-006 verification — weak–strong uniqueness

For a strong solution `u` and a Leray–Hopf solution `v`, set `w=v-u`. The displayed differential identity in the provider narrative is a **formal smooth-pair identity**. The rigorous weak–strong theorem uses the weak energy inequality, the strong energy equality, admissible time regularization, and the cross-tested formulations to obtain the integrated inequality

```math
\frac12\|w(t)\|_2^2
+\nu\int_0^t\|\nabla w(s)\|_2^2ds
\le
\int_0^t\left|\int (w\cdot\nabla)w\cdot u\,dx\right|ds.
```

The nonlinear term satisfies

```math
\left|\int (w\cdot\nabla)w\cdot u\right|
\le \|u\|_6\|w\|_3\|\nabla w\|_2
\le C\|u\|_6\|w\|_2^{1/2}\|\nabla w\|_2^{3/2}.
```

Young gives, in integrated or distributional form,

```math
\frac d{dt}\|w\|_2^2
+\nu\|\nabla w\|_2^2
\le C\nu^{-3}\|u\|_6^4\|w\|_2^2.
```

Thus `u in L^4_tL^6_x` makes the Gronwall coefficient integrable and equal initial data imply `w=0`.

**Semantic ruling:** the formal equality must never be cited as an unconditional weak-solution identity. The authoritative claim is the integrated weak–strong inequality supplied by the audited theorem interface. This clarification is nonblocking because the provider text already labels the equality formal and delegates the rigorous step to the source theorem.

## CR-007 verification — restart argument

Assume the maximal `H^1` strong solution has finite critical integral up to `T_*`. CR-005 gives a uniform gradient bound. Together with the energy bound this gives a uniform `H^1` bound. The audited local `H^1` theory supplies a lifespan depending only on the bounded `H^1` norm and `nu`. Restarting at times approaching `T_*` extends the solution beyond `T_*`, contradicting maximality.

The exact theorem-number and lifespan formula remain provenance debt, but the operational bridge is sound within the source interface already adopted by WP00.

## CR-008 and CR-009 quantifier review

For campaign data, `u_0` is in `H^1`. A Leray–Hopf solution satisfying the critical norm is therefore strong from the initial time under the operational LPS theorem. Weak–strong uniqueness then identifies every Leray–Hopf solution with the strong solution.

The one-way programme implication is correctly stated:

```text
universal full-data critical integrability
  -> global weak existence
  -> conditional strongness and uniqueness on every finite interval
  -> no finite maximal strong time
  -> classical smooth continuation for smooth rapid-decay data
  -> Fefferman statement (A).
```

The smooth-bootstrap and pressure-recovery step is part of the adopted classical strong-solution interface. Exact theorem-number normalization is retained as nonblocking provenance debt; it is not treated as a new theorem.

## Reverse correspondence

CR-010 remains separate and pending. The review found no document that silently upgrades the one-way implication to equivalence. The pending bridge must still establish finite `L^4_tL^6_x` membership in the exact official smooth class and identify every Leray–Hopf solution.

## Source-ID reconciliation

Every required source ID in `ns_ci_wp02_theorem_ledger.yaml` occurs in the MATHFORGE source ledger:

- `NS-CI-SRC-CLAY-FEFFERMAN`;
- `NS-CI-SRC-LERAY-1934`;
- `NS-CI-SRC-OZANSKI-POOLEY`;
- `NS-CI-SRC-PRODI-1959`;
- `NS-CI-SRC-SERRIN-1962`;
- `NS-CI-SRC-LADYZHENSKAYA-1967`;
- `NS-CI-SRC-OPERATIONAL-LPS-2024`.

Audit-state distinctions are preserved: historical theorem-body and translation gaps remain explicit, while the modern operational theorem is used for the actual chain.

## Cross-document consistency

Checked against:

- WP00 problem, data-class, source, theorem-spine, and correspondence records;
- WP01 fixtures `FP-001`, `FP-002`, `FP-004`, `FP-005`, `FP-006`, `FP-009`, `FP-012`, `FP-013`, and `FP-014`;
- the MATHCERT imported-interface boundary;
- the canonical tracker `MATH-PROGRAMME#55`.

No blocking conflict was found.

## Remaining nonblocking debt

- exact Leray theorem concordance;
- original Serrin theorem-body extraction;
- Ladyzhenskaya mathematical translation;
- exact local-lifespan theorem number;
- explicit source location for the final smooth-bootstrap and pressure-recovery interface;
- reverse correspondence CR-010;
- theorem-prover certification of the scaling and implication substrate.

None of these debts changes the conditional theorem chain or the claim boundary of WP02.

## Promotion decision

- Prospector: **reviewed**.
- Verifier: **reviewed**.
- Adversary: **reviewed**.
- Formalist boundary: **reviewed**.
- Amanuensis consistency: **reviewed**.
- Referee: **approved**.
- Blocking obligations: **none**.
- Programme status: `REFEREE_PROMOTED_CONDITIONAL_REGULARITY_LEDGER`.
