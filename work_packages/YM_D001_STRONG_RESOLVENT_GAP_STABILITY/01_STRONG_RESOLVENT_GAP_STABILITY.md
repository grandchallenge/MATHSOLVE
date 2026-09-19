# YM-D001-L001 — strong-resolvent preservation of a uniform spectral exclusion

## Statement

Let `K` be a complex Hilbert space. For each `n`, let `H_n` be a nonnegative self-adjoint operator on `K`, and let `H` be a nonnegative self-adjoint operator on `K`.

Fix one number

`Delta > 0`.

Assume that, for every sufficiently large `n`,

`sigma(H_n) subset {0} union [Delta,infinity)`.

Assume also that

`(I + H_n)^(-1) -> (I + H)^(-1)`

strongly on `K`.

Then

`sigma(H) subset {0} union [Delta,infinity)`.

Equivalently,

`E_H((0,Delta)) = 0`.

Thus one common positive spectral exclusion in fixed units survives strong-resolvent convergence.

The statement permits arbitrary multiplicity of the zero spectral subspace and does not assert that a zero-energy vacuum survives the limit.

## Proof

Discard finitely many initial indices so that the regulated spectral exclusion holds for every remaining `n`.

Set

`B_n := (I + H_n)^(-1)`,

`B := (I + H)^(-1)`,

and

`a := 1/(1+Delta)`.

Because every `H_n` and `H` is nonnegative and self-adjoint, every `B_n` and `B` is a bounded positive self-adjoint contraction.

The scalar map

`r(lambda) = 1/(1+lambda)`

maps `[0,infinity)` continuously and monotonically onto `(0,1]`. By the spectral calculus, the assumption

`sigma(H_n) subset {0} union [Delta,infinity)`

implies

`sigma(B_n) subset [0,a] union {1}`.

Define the real polynomial

`q(x) := (x-a)(1-x)`.

For every `x in [0,a] union {1}`,

`q(x) <= 0`.

Hence the continuous functional calculus gives the operator inequality

`q(B_n) <= 0`

for every `n`.

By hypothesis,

`B_n -> B`

strongly. Since `||B_n|| <= 1`, multiplication is stable for this sequence:

for every `psi in K`,

`||(B_n^2-B^2)psi||`

`<= ||B_n(B_n-B)psi|| + ||(B_n-B)B psi||`

`<= ||(B_n-B)psi|| + ||(B_n-B)B psi|| -> 0`.

Therefore

`B_n^2 -> B^2`

strongly, and hence

`q(B_n) -> q(B)`

strongly.

For every `psi in K`,

`<psi,q(B)psi>`

`= lim_n <psi,q(B_n)psi>`

`<= 0`.

Thus

`q(B) <= 0`.

Because `B` is a positive contraction, `sigma(B) subset [0,1]`. If `sigma(B)` met the open interval `(a,1)`, then the spectral mapping theorem for the polynomial `q` would put a positive number in `sigma(q(B))`, contradicting `q(B) <= 0`. Consequently

`sigma(B) subset [0,a] union {1}`.

Now suppose, for contradiction, that some

`lambda in sigma(H) intersect (0,Delta)`.

The resolvent transform sends it to

`mu := 1/(1+lambda)`.

Since `0 < lambda < Delta`,

`a < mu < 1`.

The spectral calculus for `B=(I+H)^(-1)` gives

`mu in sigma(B)`,

contradicting the previous spectral inclusion. Therefore

`sigma(H) intersect (0,Delta) = emptyset`.

Since `H >= 0`, this is equivalent to

`sigma(H) subset {0} union [Delta,infinity)`

and to

`E_H((0,Delta)) = 0`.

QED.

## Why strong resolvent is enough

The proof does not require norm-resolvent convergence. The key point is that the regulated spectral condition is encoded by a polynomial sign inequality for the bounded resolvents. Uniform boundedness of the resolvents upgrades strong convergence to strong convergence of the quadratic polynomial appearing in that inequality.

This is specific to having one common forbidden interval. It does not manufacture such an interval from regulator-dependent lower bounds.

## FP1 — weak resolvent convergence can fill the gap

Let

`K = L2([0,1])`

and fix `Delta > 0`. Put

`a = 1/(1+Delta)`.

For each `n >= 1`, let `r_n` be the `n`th Rademacher function: it takes values `+1` and `-1` on alternating dyadic half-cells of scale `2^(-n)`. Let

`A_n := {x : r_n(x)=+1}`

and let `P_n` be multiplication by `1_{A_n}`.

Then `P_n` is an orthogonal projection. For arbitrary `f,g in L2([0,1])`, the product `conj(f) g` lies in `L1`. Dyadic step functions are dense in `L1`, and for every dyadic step function of fixed level `m`, its integral against `r_n` is zero whenever `n>m`. Hence

`integral conj(f) g r_n -> 0`.

Since

`1_{A_n} = (1+r_n)/2`,

we obtain

`<f,P_n g> -> (1/2)<f,g>`.

Thus

`P_n -> (1/2) I`

in the weak operator topology.

Define

`H_n := Delta (I-P_n)`.

Each `H_n` is bounded, nonnegative, and self-adjoint, with

`sigma(H_n) = {0,Delta}`.

Its resolvent is

`(I+H_n)^(-1)`

`= P_n + a(I-P_n)`

`= a I + (1-a)P_n`.

Therefore these resolvents converge weakly to

`b I`,

where

`b := (1+a)/2`.

Because `a < b < 1`, there is a scalar

`h := b^(-1)-1`

with

`0 < h < Delta`.

The weak limit `bI` is exactly

`(I+hI)^(-1)`.

Hence `H_n` converge in the weak-resolvent sense at `-1` to the Hamiltonian `hI`, whose entire spectrum lies strictly inside the formerly forbidden interval.

So weak convergence of the resolvents is insufficient.

## FP2 — a vacuum can disappear under strong resolvent convergence

Let

`K = l2(N)`

with standard basis `e_1,e_2,...`, and let `P_n` be the rank-one projection onto `e_n`. Define

`H_n := Delta(I-P_n)`.

Then

`ker(H_n) = span{e_n}`

and

`sigma(H_n) = {0,Delta}`.

For every `psi in l2(N)`, its coordinate `psi_n` tends to zero, so

`||P_n psi|| = |psi_n| -> 0`.

Thus `P_n -> 0` strongly. As above,

`(I+H_n)^(-1) = aI + (1-a)P_n -> aI`

strongly. But

`aI = (I+Delta I)^(-1)`.

Therefore

`H_n -> Delta I`

in the strong-resolvent sense. The limiting operator has no zero-energy vector at all.

The spectral exclusion theorem remains true, but persistence of a vacuum is a separate hypothesis and theorem obligation.

## FP3 — positive gaps without a common lower bound are insufficient

On any nonzero Hilbert space, set

`H_n := (1/n) I`.

Every `H_n` has a strictly positive spectral gap `1/n`. Indeed,

`sigma(H_n) = {1/n}`.

But

`H_n -> 0`

in operator norm, hence also in norm-resolvent and strong-resolvent senses. The limiting spectral bottom is zero.

Therefore the phrase "every regulator is gapped" has no limiting force unless the gaps possess one common positive lower bound after conversion to the same physical units.

## Physical-rescaling corollary

Suppose a regulated family is originally written as self-adjoint `K_n` and positive conversion factors `s_n`, with physically rescaled operators

`H_n := s_n K_n`.

If, after whatever state-space identification is separately justified,

1. `sigma(H_n) subset {0} union [Delta,infinity)` for one common physical `Delta > 0`; and
2. `(I+H_n)^(-1) -> (I+H)^(-1)` strongly,

then the limiting `H` has no spectrum in `(0,Delta)`.

The corollary does not prove that the factors `s_n`, the state-space identifications, the uniform lower bound, or the strong-resolvent convergence exist for four-dimensional Yang–Mills.

## Relation to YM-D001

`YM-D001` requires both a uniform regulated lower bound in fixed physical units and a convergence theorem that preserves spectral exclusion. `YM-D001-L001` discharges only the abstract second component for the strong-resolvent topology on an identified Hilbert space.

The remaining Yang–Mills-specific obligations include:

- construction of the relevant regulated Hamiltonians along the chosen continuum trajectory;
- the physical rescaling and comparison/identification of state spaces;
- one cutoff- and volume-uniform `Delta > 0` after that rescaling;
- strong-resolvent convergence to the target limiting Hamiltonian, or a rigorously defined generalized convergence notion with an analogous stability theorem;
- separate control of the vacuum sector if a nonzero vacuum vector is to survive.

No continuum Yang–Mills existence or physical mass-gap claim follows from this abstract theorem alone.
