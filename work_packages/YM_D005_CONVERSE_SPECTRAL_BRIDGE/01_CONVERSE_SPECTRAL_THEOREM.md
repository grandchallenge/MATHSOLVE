# YM-D005-L001 — dense-observable converse spectral theorem

## Statement

Let `K` be a complex Hilbert space and let `H` be a nonnegative self-adjoint operator on `K`. Let `Omega` be a unit vector with

`H Omega = 0`.

Let `D` be a linear subspace of `Omega^perp` that is norm-dense in `Omega^perp`, and fix one number

`Delta > 0`.

Assume that for every `psi in D` there exist finite constants `C_psi >= 0` and `T_psi >= 0` such that

`<psi, exp(-t H) psi> <= C_psi exp(-Delta t)`

for every `t >= T_psi`.

Then

`E_H([0, Delta)) | Omega^perp = 0`,

where `E_H` is the spectral measure of `H`. In particular,

1. `ker(H) = span{Omega}`;
2. `Omega^perp` is a reducing subspace for `H`;
3. `sigma(H | Omega^perp) subset [Delta, infinity)`;
4. the reconstructed non-vacuum spectral gap is at least `Delta`.

Conversely, if

`sigma(H | Omega^perp) subset [Delta, infinity)`,

then every `psi in Omega^perp` satisfies, for all `t >= 0`,

`<psi, exp(-t H) psi> <= ||psi||^2 exp(-Delta t)`.

Thus the existence of one common exponential rate on a dense centered class is equivalent, after reconstruction, to a spectral lower bound at that rate.

## Proof of the converse-spectral direction

Fix `psi in D`. Let

`mu_psi(B) := <psi, E_H(B) psi>`

be its finite positive spectral measure. The spectral theorem gives

`<psi, exp(-tH) psi> = integral_[0,infinity) exp(-t lambda) d mu_psi(lambda)`.

We first prove that

`mu_psi([0, Delta)) = 0`.

Assume the contrary. Since

`[0, Delta) = union_{a < Delta, a rational} [0,a]`,

continuity from below of finite measures implies that there exists some `a < Delta` with

`m := mu_psi([0,a]) > 0`.

For every `t >= 0`, positivity of the integrand gives

`<psi, exp(-tH) psi>`

`>= integral_[0,a] exp(-t lambda) d mu_psi(lambda)`

`>= m exp(-a t)`.

For all `t >= T_psi`, the assumed decay bound also gives

`m exp(-a t) <= C_psi exp(-Delta t)`.

Equivalently,

`m exp((Delta-a)t) <= C_psi`.

Because `Delta-a > 0`, the left-hand side tends to infinity with `t`, contradicting finiteness of `C_psi`. Hence

`mu_psi([0,Delta)) = 0`.

For a spectral projection `P := E_H([0,Delta))`,

`||P psi||^2 = <psi, P psi> = mu_psi([0,Delta)) = 0`,

so `P psi = 0` for every `psi in D`.

The operator `P` is bounded. Since `D` is dense in `Omega^perp`, continuity implies

`P | Omega^perp = 0`.

Because `H Omega = 0`, the line `span{Omega}` is contained in the zero-energy spectral subspace. Any additional zero-energy vector orthogonal to `Omega` would lie in `Omega^perp` and in the range of `P`, contradicting the previous equality. Therefore

`ker(H) = span{Omega}`.

Self-adjointness and `H Omega = 0` make `Omega^perp` reducing. Since its spectral projection on `[0,Delta)` vanishes, the spectral support of the restriction lies in `[Delta,infinity)`. Thus

`inf sigma(H | Omega^perp) >= Delta`.

This proves the result.

## Proof of the forward direction

Assume

`sigma(H | Omega^perp) subset [Delta,infinity)`.

For `psi in Omega^perp`, its spectral measure is supported in `[Delta,infinity)`. Therefore

`<psi, exp(-tH) psi>`

`= integral_[Delta,infinity) exp(-t lambda) d mu_psi(lambda)`

`<= exp(-Delta t) integral_[Delta,infinity) d mu_psi(lambda)`

`= ||psi||^2 exp(-Delta t)`

for every `t >= 0`.

QED.

## Corollary for an Osterwalder–Schrader reconstruction

Suppose a valid reconstruction of one limiting Euclidean theory supplies:

- a Hilbert space `K`;
- a unit vacuum vector `Omega`;
- a nonnegative self-adjoint Hamiltonian `H`;
- a linear gauge-invariant positive-time observable class `A_decay`;
- reconstructed centered vectors `psi_F in Omega^perp` for `F in A_decay`;
- the translation/semigroup identity

  `C_F(t) = <psi_F, exp(-tH) psi_F>`;

- density of `{psi_F : F in A_decay}` in `Omega^perp`;
- one common `Delta > 0` such that every `C_F(t)` is eventually bounded by `C_F exp(-Delta t)`.

Then the reconstructed Hamiltonian has unique vacuum and non-vacuum spectrum bounded below by `Delta`.

The density premise is automatic only if the decay-controlled class is the full class whose completion defines the reconstructed Hilbert space. If decay is proved merely for a proper subclass, density is a separate theorem obligation.

## Exact false-proof fixture FP1 — one channel

Let `K = C^3`, choose `0 < epsilon < Delta`, and set

`H = diag(0, epsilon, Delta)`,

`Omega = e_0`,

`psi = e_2`.

Then

`<psi, exp(-tH) psi> = exp(-Delta t)`

for all `t >= 0`, but

`inf sigma(H | Omega^perp) = epsilon < Delta`.

The observed channel misses the lower state `e_1`. Therefore decay in one selected correlator does not imply the full physical gap.

## Exact false-proof fixture FP2 — vector-dependent rates

Let

`K = C Omega direct_sum l2(N)`

with orthonormal basis `Omega, e_1, e_2, ...`, and define

`H Omega = 0`,

`H e_n = (1/n) e_n`.

Let `D` be the finite-support vectors in `Omega^perp`. Then `D` is dense. Every nonzero `psi in D` has finite support, so if

`delta_psi := min{1/n : coefficient of e_n in psi is nonzero}`,

then `delta_psi > 0` and

`<psi, exp(-tH) psi> <= ||psi||^2 exp(-delta_psi t)`.

Nevertheless

`inf sigma(H | Omega^perp) = 0`.

Therefore dense-class exponential decay with vector-dependent positive exponents does not imply a positive global gap. The common lower exponent `Delta` is essential.

## Relation to YM-D005

This theorem closes the abstract functional-analytic implication inside `YM-D005`; it does not discharge the Yang–Mills debt itself.

To discharge `YM-D005` for the target four-dimensional theory, one must still prove, for the same limiting reconstructed theory, that:

1. the reconstruction hypotheses are valid;
2. the decay-controlled gauge-invariant local observable vectors form a dense linear subspace of `Omega^perp`;
3. one common positive physical-unit exponent `Delta` controls every vector in that dense class.

The theorem forbids replacing item 2 by one channel or item 3 by a family of positive rates with infimum zero.

## Claim boundary

No statement here constructs four-dimensional Yang–Mills theory, proves the complete Osterwalder–Schrader axioms, takes a regulator limit, identifies ultraviolet curvature observables, proves confinement, establishes novelty or priority, or certifies the Clay mass-gap problem.
