# YM-D001-R004-L001 — varying-Hilbert preservation of a uniform spectral exclusion

## Statement

For each `n`, let `K_n` be a complex Hilbert space and let `H_n` be a nonnegative self-adjoint operator on `K_n`.

Let `K` be a complex Hilbert space and let `H` be a nonnegative self-adjoint operator on `K`.

Fix

`Delta > 0`.

Assume that, for every sufficiently large `n`,

`sigma(H_n) subset {0} union [Delta,infinity)`.

Define bounded positive contractions

`B_n := (I+H_n)^(-1)`

on `K_n`, and

`B := (I+H)^(-1)`

on `K`.

Assume there are bounded linear maps

`J_n : K -> K_n`

such that:

### VH1 — asymptotic isometry

`J_n^* J_n -> I_K`

strongly on `K`.

### VH2 — resolvent intertwining

For every `psi in K`,

`||B_n J_n psi - J_n B psi||_{K_n} -> 0`.

Then

`sigma(H) subset {0} union [Delta,infinity)`.

Equivalently,

`E_H((0,Delta)) = 0`.

No assertion is made that a zero-energy vector survives or that the zero eigenspace has any prescribed multiplicity.

## Proof

Discard finitely many initial indices so that the regulated spectral exclusion holds for all remaining `n`.

Set

`a := 1/(1+Delta)`

and

`q(x) := (x-a)(1-x)`.

Because every `H_n` is nonnegative self-adjoint,

`0 <= B_n <= I`.

The spectral transform `lambda -> 1/(1+lambda)` sends

`{0} union [Delta,infinity)`

into

`{1} union (0,a]`.

Allowing the possible spectral limit point `0` for an unbounded `H_n`,

`sigma(B_n) subset [0,a] union {1}`.

On this set,

`q(x) <= 0`.

Hence the bounded functional calculus gives

`q(B_n) <= 0`.

We now transfer this sign inequality to `B`.

### Step 1 — the intertwining extends to the quadratic polynomial

Fix `psi in K`.

By VH2,

`B_n J_n psi - J_n B psi -> 0`

in `K_n`.

Also,

`B_n^2 J_n psi - J_n B^2 psi`

equals

`B_n(B_n J_n psi - J_n B psi) + (B_n J_n B psi - J_n B^2 psi)`.

Since `||B_n|| <= 1`, the norm of the first term tends to zero by VH2 applied to `psi`, and the norm of the second tends to zero by VH2 applied to the fixed vector `B psi`.

Therefore

`B_n^2 J_n psi - J_n B^2 psi -> 0`.

Since `q` is a quadratic polynomial,

`q(B_n) J_n psi - J_n q(B) psi -> 0`.

### Step 2 — asymptotic isometry transfers quadratic forms

VH1 implies, for every fixed `u,v in K`,

`<J_n u, J_n v>_{K_n} -> <u,v>_K`,

because

`<J_n u,J_n v> = <u,J_n^*J_n v>`.

It also implies that `||J_n psi||` is bounded for each fixed `psi`.

Hence

`<J_n psi, q(B_n) J_n psi>`

minus

`<J_n psi, J_n q(B) psi>`

tends to zero.

But `q(B_n) <= 0`, so

`<J_n psi, q(B_n) J_n psi> <= 0`.

Taking limits and using VH1 gives

`<psi,q(B)psi> <= 0`

for every `psi in K`.

Thus

`q(B) <= 0`.

### Step 3 — exclude the forbidden resolvent interval

Because `B` is a positive contraction,

`sigma(B) subset [0,1]`.

The polynomial `q` is strictly positive on

`(a,1)`.

If `sigma(B)` met `(a,1)`, the spectral mapping theorem would put a positive point in `sigma(q(B))`, contradicting `q(B)<=0`.

Therefore

`sigma(B) subset [0,a] union {1}`.

If some

`lambda in sigma(H) intersect (0,Delta)`,

then

`mu=1/(1+lambda)`

lies in `(a,1)` and belongs to `sigma(B)` by the functional calculus, contradiction.

Hence

`sigma(H) intersect (0,Delta) = emptyset`.

Since `H>=0`,

`sigma(H) subset {0} union [Delta,infinity)`.

QED.

## FP1 — compressed resolvents can fill the gap

The condition

`J_n^* B_n J_n -> B`

is not a replacement for VH2.

Take

`K = C`

and, for every `n`,

`K_n = C^2`.

Fix `Delta>0` and set

`a=1/(1+Delta)`.

Let

`H_n = diag(0,Delta)`

and therefore

`B_n = diag(1,a)`.

Choose one number `t in (0,1)` and define the exact isometry

`J : C -> C^2`

by

`J z = z (sqrt(t), sqrt(1-t))`.

Use `J_n=J` for all `n`.

Then

`J_n^*J_n=I`

exactly.

But

`J^* B_n J = b I`

where

`b = t + (1-t)a`.

Since `a<b<1`, define

`h=b^(-1)-1`.

Then

`0<h<Delta`

and

`bI=(I+hI)^(-1)`.

Thus the compressed resolvents agree exactly with the resolvent of the scalar limiting Hamiltonian

`H=hI`,

whose spectrum lies strictly inside the forbidden interval.

So exact isometric compression convergence does not preserve the gap.

What fails is VH2: the one-dimensional subspace `J(C)` mixes the regulated vacuum and excited eigenspaces and is not invariant under `B_n`.

## FP2 — degenerate identifications make intertwining vacuous

If asymptotic isometry is removed, take

`J_n=0`

for every `n`.

Then

`B_n J_n psi - J_n B psi = 0`

for every choice of `H_n` and `H`.

Thus an intertwining statement with collapsing identification maps contains no spectral information.

VH1 prevents this degeneracy.

## Interpretation

VH2 is an identification-map version of strong convergence of the negative-point resolvents: applying a regulated resolvent after embedding a limiting state is asymptotically the same as applying the limiting resolvent first and then embedding.

The theorem does not claim this is the unique or weakest varying-Hilbert convergence formalism. It proves that these two explicit hypotheses are sufficient for the same polynomial-sign argument used in R001.

If a future Yang-Mills construction uses Mosco convergence, form convergence, quasi-unitary equivalence, inductive-limit Hilbert spaces, or another framework, that framework must be shown to imply an equivalent spectral-stability statement before R004 can be invoked.

## Physical-scale boundary

The theorem assumes that the operators `H_n` and `H` are already expressed in one common physical energy normalization, so that the same numerical `Delta` has the same physical meaning for every `n`.

R004 does not construct that normalization.

Therefore `YM-D001-O005 = MISSING_PHYSICAL_ENERGY_SCALE_SETTING` remains open.
