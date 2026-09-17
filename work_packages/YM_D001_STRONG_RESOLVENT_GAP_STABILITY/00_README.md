# YM-D001-R001 — strong-resolvent spectral-exclusion stability

## Metadata

- Campaign: `YM-001`.
- Parent debt: `YM-D001`.
- Work package: `YM-D001-STRONG-RESOLVENT-GAP-STABILITY`.
- Protected Solve baseline: `adaae95545abcb02db4ab9b2281981fc0f8ce07b`.
- Protected Programme routing baseline: `1f4ba5fabab01c084aefab201c5a4aa594d257fc`.
- Target state: `SELECTED_RESTRICTED_TARGET`.
- Certification: none; MATHCERT remains the sole certification authority.

## Why this target is next

`YM-D005-R001` is admitted, but its physical instantiation is blocked by `YM-D002`/`YM-D003`. The current Programme routing gate instead permits selection of another smallest material target among `YM-D001` through `YM-D005`.

`YM-D001` contains two logically separate burdens:

1. obtain one volume- and cutoff-uniform positive spectral lower bound in fixed physical units for the regulated theory;
2. prove that the chosen continuum convergence topology preserves that spectral exclusion.

`YM-D001-R001` isolates the second burden. It asks for the weakest simple operator topology in which a common spectral exclusion can be proved to survive. The package proves that strong-resolvent convergence is sufficient.

## Restricted-target contract — 18 fields

1. **Target ID:** `YM-D001-R001`.
2. **Parent debt:** `YM-D001` (`UNPROVED_BRIDGE`, blocked node `YM-T-150`).
3. **Ambient object:** one complex Hilbert space `K` after whatever regulator-dependent identifications are chosen.
4. **Regulated operators:** nonnegative self-adjoint operators `H_n` on `K`.
5. **Physical rescaling:** any cutoff/volume conversion to physical energy units is performed before the theorem; the resulting operators are the `H_n` appearing here.
6. **Limit operator:** a nonnegative self-adjoint operator `H` on `K`.
7. **Common physical gap input:** one fixed `Delta > 0`, independent of `n`.
8. **Regulated spectral exclusion:** `sigma(H_n) subset {0} union [Delta,infinity)` for every sufficiently large `n`.
9. **Convergence topology:** `(I + H_n)^(-1) -> (I + H)^(-1)` strongly.
10. **Domain handling:** domains may vary; the theorem is stated through bounded resolvents, so no common operator core is assumed.
11. **Conclusion:** `sigma(H) subset {0} union [Delta,infinity)`.
12. **Projection form:** equivalently, `E_H((0,Delta)) = 0`.
13. **Vacuum non-conclusion:** persistence or uniqueness of a zero-energy vacuum is not implied by strong-resolvent convergence alone.
14. **Weak-topology firewall:** weak convergence of the resolvents is insufficient, even when every regulator has exact spectrum `{0,Delta}`.
15. **Uniformity firewall:** a sequence of positive gaps `Delta_n > 0` with `inf_n Delta_n = 0` is insufficient for a positive limiting gap.
16. **Scaling firewall:** a common lower bound in raw regulator units is irrelevant unless the physical rescaling is fixed and the resulting physical-unit `Delta` is uniform.
17. **Arbitrary-input quantifier:** the theorem concerns the full operator spectrum after identification, not selected eigenvalues or correlation channels.
18. **Non-implications:** the result does not construct a Yang–Mills continuum Hamiltonian, prove strong-resolvent convergence for any regulator family, supply a uniform physical gap, preserve a vacuum automatically, establish confinement, or solve the Clay problem.

## Candidate result

`YM-D001-L001` proves the target. If nonnegative self-adjoint `H_n` converge to nonnegative self-adjoint `H` in the strong-resolvent sense and every `H_n` has no spectrum in `(0,Delta)` for one common `Delta > 0`, then `H` also has no spectrum in `(0,Delta)`.

The proof uses the bounded transforms

`B_n = (I + H_n)^(-1)`, `B = (I + H)^(-1)`

and the scalar number

`a = 1/(1+Delta)`.

The regulated gap is equivalent to

`sigma(B_n) subset [0,a] union {1}`.

For the polynomial

`q(x) = (x-a)(1-x)`,

one has `q(B_n) <= 0`. Strong convergence of the uniformly bounded `B_n` implies strong convergence of `B_n^2`, hence `q(B_n) -> q(B)` strongly and `q(B) <= 0`. Since `B` is a positive contraction, its spectrum cannot meet `(a,1)`, which is exactly the resolvent image of `(0,Delta)`.

## Exact false-proof fixtures

### FP1 — weak resolvent convergence is insufficient

On `L2([0,1])`, let `P_n` multiply by the indicator of the `n`th dyadic checkerboard half-set and put

`H_n = Delta (I-P_n)`.

Every `H_n` has spectrum `{0,Delta}`. The projections converge weakly to `(1/2)I`, so the resolvents converge weakly to a scalar resolvent corresponding to a limit Hamiltonian `h I` with `0 < h < Delta`. Thus weak resolvent convergence can fill the forbidden gap.

### FP2 — vacuum persistence is separate

On `l2(N)`, let `P_n` project onto `e_n` and put

`H_n = Delta (I-P_n)`.

Each `H_n` has a unique zero-energy vector `e_n` and otherwise energy `Delta`. Since `P_n -> 0` strongly, the resolvents converge strongly to the resolvent of `Delta I`. The spectral exclusion survives, but the zero-energy state disappears. A physical vacuum therefore requires an additional zero-sector convergence hypothesis.

### FP3 — regulator-by-regulator positivity is insufficient

Take `H_n = (1/n) I`. Every regulator has a strictly positive gap, but there is no common `Delta > 0`; the operators converge even in norm to the zero operator. A positive gap at each regulator separately does not produce a positive physical limiting gap.

## What this package does and does not close

This package closes only the abstract convergence-topology implication inside `YM-D001`. The parent debt remains open until the actual regulated four-dimensional Yang–Mills family supplies, in the same physical scaling and along the same continuum trajectory:

1. one common `Delta > 0` independent of cutoff and volume;
2. a mathematically valid identification of the regulated state spaces with the limiting comparison space (or a stronger generalized convergence framework replacing that identification);
3. strong-resolvent convergence of the physically rescaled Hamiltonians to the target continuum Hamiltonian;
4. any separately required vacuum-sector convergence.

No claim in this package supplies those Yang–Mills-specific inputs.
