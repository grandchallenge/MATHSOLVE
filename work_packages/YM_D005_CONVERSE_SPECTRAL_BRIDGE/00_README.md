# YM-D005-R001 — dense-observable converse spectral bridge

## Metadata

- Campaign: `YM-001`.
- Parent debt: `YM-D005`.
- Work package: `YM-D005-CONVERSE-SPECTRAL-BRIDGE`.
- Protected Solve baseline: `499a521870d01aecc9b5ddad8c7db291b999263a`.
- Protected Programme routing baseline: `1f4ba5fabab01c084aefab201c5a4aa594d257fc`.
- Constitutional baseline read before mutation: `f042220f3bed7cb7b5069256e8f6305c850c0628`.
- Target state: `SELECTED_RESTRICTED_TARGET`.
- Certification: none; MATHCERT remains the only certification authority.

## Purpose

Isolate and settle the smallest functional-analytic implication inside `YM-D005`: when Euclidean correlation decay is already represented by one reconstructed Hamiltonian semigroup, determine exactly when a common decay exponent forces a lower bound on the full non-vacuum spectrum.

This tranche deliberately does not attempt the four-dimensional continuum construction, full Osterwalder–Schrader reconstruction, regulator survival, or ultraviolet observable identification.

## Restricted-target contract — 18 fields

1. **Target ID:** `YM-D005-R001`.
2. **Parent debt:** `YM-D005` (`UNPROVED_BRIDGE`, blocked node `YM-T-140`).
3. **Ambient object:** a complex Hilbert space `K`.
4. **Dynamics:** a nonnegative self-adjoint operator `H` on `K`.
5. **Vacuum datum:** a unit vector `Omega` with `H Omega = 0`.
6. **Non-vacuum sector:** the reducing subspace `Omega^perp`.
7. **Observable-vector class:** a linear subspace `D subset Omega^perp`.
8. **Completeness hypothesis:** `D` is norm-dense in `Omega^perp`.
9. **Semigroup/correlation identity:** for vectors supplied by the reconstructed observable class, Euclidean translated diagonal correlations equal `inner(psi, exp(-t H) psi)`.
10. **Common decay scale:** one fixed real number `Delta > 0`, independent of `psi`.
11. **Decay hypothesis:** for every `psi in D`, there exist finite `C_psi` and `T_psi` such that `inner(psi, exp(-t H) psi) <= C_psi exp(-Delta t)` for all `t >= T_psi`.
12. **Allowed prefactor dependence:** `C_psi` and `T_psi` may depend on the vector; `Delta` may not.
13. **Spectral conclusion:** the spectral projection `E_H([0,Delta))` vanishes on `Omega^perp`.
14. **Vacuum conclusion:** `ker(H) = span{Omega}` follows from the hypotheses; it need not be assumed separately.
15. **Gap conclusion:** `inf sigma(H restricted to Omega^perp) >= Delta`.
16. **Arbitrary-input quantifier:** the decay hypothesis ranges over every vector in the dense linear class `D`, not one selected channel.
17. **Falsification tests:** a proper non-dense channel can miss a lower-energy state; dense vectors with only vector-dependent positive rates can coexist with zero global gap.
18. **Non-implications:** the result does not construct a four-dimensional Yang–Mills theory, prove any OS axiom, prove that the required dense class has the decay estimate, prove regulator survival, confinement, novelty, priority, or the Clay mass-gap statement.

## Candidate result

`YM-D005-L001` proves the target. In abstract form:

> Let `H >= 0` be self-adjoint on `K`, let `Omega` be a unit zero-energy vector, let `D` be a linear subspace dense in `Omega^perp`, and fix `Delta > 0`. If every `psi in D` has asymptotic diagonal semigroup decay bounded by `C_psi exp(-Delta t)`, then `E_H([0,Delta))` vanishes on `Omega^perp`. Consequently the vacuum is unique and the reconstructed non-vacuum spectrum is bounded below by `Delta`.

The converse direction is also exact: if the non-vacuum spectrum is bounded below by `Delta`, then every `psi in Omega^perp` satisfies the all-time bound

`inner(psi, exp(-tH) psi) <= norm(psi)^2 exp(-Delta t)`.

Thus, after a valid reconstruction, a common exponential rate on a dense centered observable class is spectrally equivalent to a gap lower bound.

## False-proof firewall

### FP1 — one channel is insufficient

On `C^3`, take

`H = diag(0, epsilon, Delta)` with `0 < epsilon < Delta`, `Omega = e_0`, and observe only `psi = e_2`.

Then

`inner(psi, exp(-tH) psi) = exp(-Delta t)`

while the actual non-vacuum gap is `epsilon`. A selected correlator may decay rapidly while an unobserved state lies lower.

### FP2 — non-uniform rates are insufficient

On `C Omega direct_sum l2(N)`, let

`H Omega = 0`, `H e_n = (1/n) e_n`.

The finite-support subspace is dense in `Omega^perp`. Every finite-support vector has exponential decay with some positive vector-dependent rate, but the infimum of the non-vacuum spectrum is zero. Therefore a single common `Delta > 0` is essential.

## What is proved in this package

- the exact spectral-measure converse theorem `YM-D005-L001`;
- uniqueness of the zero-energy vacuum from dense-class positive decay, rather than as an extra premise;
- the forward gap-to-decay implication;
- exact counterexamples to the one-channel and non-uniform-rate substitutions;
- a precise decomposition of `YM-D005` into an abstract spectral implication and a Yang–Mills-specific instantiation problem.

## What remains open

`YM-D005` itself remains open for four-dimensional Yang–Mills until the same limiting reconstructed theory supplies:

1. the Hamiltonian/semigroup representation from a valid complete reconstruction;
2. the exact gauge-invariant local observable class whose centered image is dense in `Omega^perp`;
3. one common physical-unit decay exponent `Delta > 0` on that entire dense linear class.

The first item depends materially on `YM-D002`; the continuum existence and identification needed to make it a four-dimensional physical theory also depend on `YM-D003`, with observable normalization tied to `YM-D004`. `YM-D001` remains separate regulator-survival debt.

## Successor

The next bounded tranche is `YM-D005-R002`: bind the full positive-time gauge-invariant reconstruction algebra and determine whether the decay-controlled subclass is actually dense. If decay is known only for a proper channel, terminate that route as insufficient rather than promoting a mass-gap claim.
