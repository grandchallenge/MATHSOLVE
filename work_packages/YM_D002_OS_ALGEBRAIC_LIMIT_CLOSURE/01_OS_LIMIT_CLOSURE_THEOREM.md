# YM-D002-R001-L001 — closed algebraic OS properties survive a common-domain pointwise limit

## Statement

Let `A` be a complex algebra of Euclidean observables containing the unit `1`, and let `A_+ subset A` be the selected positive-time subalgebra. Let `theta` be the selected reflection operation. Let `G_E` act through maps `alpha_g` representing admitted Euclidean transformations, and let `G_gauge` act through maps `beta_h` whenever gauge invariance is represented on the common algebra.

For each `n >= 1`, let

`omega_n : A -> C`

be linear. Assume pointwise convergence on the same algebra:

`omega_n(F) -> omega(F)`

for every fixed `F in A`.

Assume, for every `n`, the relevant properties below hold on their common domains.

1. **Normalization:** `omega_n(1)=1`.
2. **Exact symmetry:** for every admitted finite permutation map `P`, `omega_n(PF)=omega_n(F)`.
3. **Euclidean covariance/invariance:** `omega_n(alpha_g F)=omega_n(F)` whenever both expressions lie in the common admitted domain.
4. **Gauge invariance:** `omega_n(beta_h F)=omega_n(F)` whenever gauge invariance is represented by the common action.
5. **Reflection positivity:** for every `F in A_+`,
   `omega_n(theta(F) F) >= 0`.
   Equivalently, for every finite family `F_1,...,F_m in A_+` and coefficients `c_1,...,c_m in C`,
   `sum_{i,j} conjugate(c_i)c_j omega_n(theta(F_i) F_j) >= 0`.

Then `omega` is linear and satisfies the corresponding five properties.

No conclusion about the remaining analytic, growth, clustering, vacuum, existence, or reconstruction hypotheses of `YM-T-120` follows from this theorem alone.

## Proof

### Step 1 — linearity

Fix `F,H in A` and `a,b in C`.

For every `n`,

`omega_n(aF+bH)=a omega_n(F)+b omega_n(H)`.

All three terms converge by hypothesis. Passing to the limit gives

`omega(aF+bH)=a omega(F)+b omega(H)`.

Thus `omega` is linear.

### Step 2 — normalization

For every `n`, `omega_n(1)=1`. Hence

`omega(1)=lim_n omega_n(1)=1`.

### Step 3 — exact permutation/symmetry equalities

Fix an admitted permutation map `P` and `F` in its common domain.

For every `n`,

`omega_n(PF)=omega_n(F)`.

Pointwise convergence at `PF` and `F` gives

`omega(PF)=omega(F)`.

The same argument applies to any exact finite symmetry equality represented by fixed algebra maps on the common domain.

### Step 4 — Euclidean covariance/invariance

Fix an admitted transformation `g` and `F` such that `F` and `alpha_g F` lie in the common domain.

Since

`omega_n(alpha_g F)=omega_n(F)`

for all `n`, pointwise convergence gives

`omega(alpha_g F)=omega(F)`.

Thus the exact Euclidean invariance equality survives.

### Step 5 — gauge invariance

The identical argument with `beta_h` gives

`omega(beta_h F)=omega(F)`

whenever the common algebra carries the admitted gauge action and every approximant is invariant under it.

This step creates no gauge-invariant observable algebra; it only preserves an invariance equality on an algebra already identified across the sequence.

### Step 6 — reflection positivity

Fix `F in A_+`. Define

`q_n(F)=omega_n(theta(F)F)`.

By assumption, `q_n(F)` is a nonnegative real number for every `n`. Since the element `theta(F)F` is fixed in the common algebra,

`q_n(F) -> omega(theta(F)F)=q(F)`.

The set `[0,infinity)` is closed in `R`. Therefore `q(F)>=0`.

For the finite Gram form, fix `F_1,...,F_m` and coefficients `c_1,...,c_m`. Each matrix entry

`omega_n(theta(F_i)F_j)`

converges to the corresponding entry for `omega`. The finite quadratic forms therefore converge term by term:

`Q_n -> Q`.

Every `Q_n>=0`, hence `Q>=0`. Reflection positivity survives.

This proves the theorem.

## Corollary — what a selected continuum route may reuse

Suppose a future four-dimensional Yang-Mills construction supplies:

- comparison maps placing the relevant regulated gauge-invariant observable hierarchies on one common algebra;
- pointwise convergence of all finite smeared expressions used by the selected algebraic OS conditions;
- exact normalization, symmetry/covariance, gauge invariance, and reflection positivity at every admitted stage.

Then those properties need not be established a second time for the limiting functional: R001 transfers them.

The route still must prove that the hypotheses above actually hold for its construction, and must independently discharge every nonalgebraic selected OS requirement.

## FP1 — fixed-regulator positivity is not continuum positivity without convergence

Reflection positivity at every regulator does not imply reflection positivity of an unidentified “continuum object.”

R001 requires a common algebra and convergence of the reflected products. Without those comparison/convergence data there is no mathematical limit to which the closed-cone argument applies.

## FP2 — algebraic OS closure is not the complete OS profile

The theorem transfers only properties whose proof is an exact equality or membership in a closed finite-dimensional/nonnegative cone after pointwise evaluation.

It does not supply the topology or uniform estimates needed for all regularity/growth requirements, nor the large-distance uniformity needed for clustering.

Therefore R001 cannot by itself satisfy the domain hypotheses of `YM-T-120`.

## FP3 — pointwise convergence does not preserve clustering

For `t in R`, define

`C_n(t)=exp(-|t|/n)`.

For each fixed `n`,

`lim_{|t|->infinity} C_n(t)=0`.

For each fixed `t`,

`lim_{n->infinity} C_n(t)=1`.

Hence the pointwise limiting function is `C(t)=1`, which does not tend to zero at large separation.

Thus stagewise clustering plus bare pointwise convergence in the regulator index does not imply clustering of the limiting hierarchy. The order of limits requires additional uniform control.

## FP4 — route comparison cannot be skipped

If the n-th hierarchy lives on a regulator-dependent observable space `A_n`, the notation `omega_n(F)` for one fixed `F` is meaningless until comparison/identification maps have been supplied.

R001 therefore cannot splice Balaban, MRS, lattice, or any other route by naming formally similar observables. A common-domain theorem or comparison map is a real hypothesis.

## Campaign consequence

`YM-D002` remains open, but its residual is sharper.

The algebraic OS core is conditionally stable under a legitimate common-domain pointwise limit. The smallest material successor is therefore not another abstract reflection-positivity lemma. It is:

`YM-D002-R002 — SELECTED_4D_LIMIT_HIERARCHY_AND_NONALGEBRAIC_OS_PROFILE`.

That successor must be instantiated on an actually selected four-dimensional continuum route and carry the analytic/growth and clustering/vacuum obligations that R001 does not transfer.

## Claim boundary

This is an abstract closure theorem over an assumed common-domain limit. It is not a construction of Yang-Mills measure or Schwinger functions, not an OS reconstruction theorem, and not a mass-gap theorem.
