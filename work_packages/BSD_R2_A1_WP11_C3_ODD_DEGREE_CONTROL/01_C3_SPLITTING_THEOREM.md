# Theorem A — complete splitting of `2N` in the `C3` 2-division field

Let `E/Q` satisfy the protected `BSD-R2-A1` hypotheses and assume the residual image is the `C3` branch of WP10:

`im(rho_bar_{E,2}) ~= C3`.

Let `L = Q(E[2])`. Then `Gal(L/Q) ~= C3`.

## A1. Representation-theoretic fact

The unique nontrivial action of `C3` on the two-dimensional `F_2`-space `E[2]` is irreducible.

Indeed, a nontrivial element has order `3`; its minimal polynomial over `F_2` divides `x^3-1=(x-1)(x^2+x+1)`. It cannot have eigenvalue `1`, because then it would fix a nonzero vector and the generated subgroup would lie in a Borel of `GL_2(F_2)`, whose order is `2`. Hence its minimal polynomial is the irreducible polynomial `x^2+x+1`.

Since `C3` has prime order, every nontrivial subgroup is all of `C3`. Therefore any subgroup of `C3` whose action on `E[2]` is reducible must be trivial.

## A2. The prime `2`

`E` has good ordinary reduction at `2`.

For an ordinary elliptic curve over `Q_2`, the finite-flat connected-etale sequence of `E[2]` over `Z_2` gives a `G_{Q_2}`-stable line in the generic fibre `E[2]`. Thus the local mod-2 representation is reducible.

Its image is also a subgroup of the global image `C3`. By A1, the local image must therefore be trivial.

The decomposition group of any prime of `L` above `2` is the local image in `Gal(L/Q)`. Hence it is trivial, so `2` splits completely in `L/Q`.

Equivalently, all of `E[2]` is rational over `Q_2` in the `C3` branch.

## A3. Bad primes `ell|N`

Because `E` is semistable and `ell|N`, the reduction at `ell` is multiplicative.

For split multiplicative reduction, the Tate-curve exact sequence on 2-torsion exhibits a `G_{Q_ell}`-stable copy of `mu_2`, so the local mod-2 representation is reducible.

For nonsplit multiplicative reduction, the curve becomes split multiplicative after an unramified quadratic twist. Modulo `2`, the quadratic character takes values in `{+1,-1}` and becomes trivial in `F_2^x={1}`. Therefore the mod-2 representation still has the same reducible upper-triangular form.

Again the local image is a subgroup of the global `C3`; by A1 it must be trivial. Hence every `ell|N` splits completely in `L/Q`.

## A4. Infinite place

Complex conjugation has order at most `2`. Its image in the odd-order group `C3` is therefore trivial. Thus every embedding of `L` is real and `L/Q` is totally real.

## Theorem A

Under the `C3` residual branch,

- `Gal(Q(E[2])/Q) ~= C3`;
- every prime dividing `2N` splits completely in `Q(E[2])/Q`;
- `Q(E[2])` is totally real.

No assertion is made for the `S3` branch.
