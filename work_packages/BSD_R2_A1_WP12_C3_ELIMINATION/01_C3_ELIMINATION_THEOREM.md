# Theorem — residual surjectivity in the selected class

Let `E/Q` satisfy the protected `BSD-R2-A1` hypotheses:

- semistable;
- odd conductor `N`;
- good ordinary reduction at `2`;
- `E[2]` irreducible;
- analytic rank exactly one.

The analytic-rank hypothesis is not used in this theorem.

## Step 1. WP10 dichotomy

WP10 proves that irreducibility of `E[2]` leaves exactly two possible residual images:

`C3` or `GL_2(F_2) ~= S3`.

Assume for contradiction that the image is `C3` and set

`L := Q(E[2])`.

Then `L/Q` is cyclic cubic.

## Step 2. Ramification at primes dividing `2N`

WP11 proves, under this `C3` assumption, that every prime dividing `2N` splits completely in `L/Q`.

Therefore the decomposition group, and hence the inertia group, is trivial at every prime dividing `2N`.

WP11 also proves that `L` is totally real.

## Step 3. Ramification away from `2N`

Let `ell` be a finite prime with `ell` not dividing `2N`.

Since `E` is semistable of conductor `N`, `E` has good reduction at `ell`. Also `ell != 2`.

Take the smooth proper elliptic-curve model over `Z_ell`. Multiplication by `2` is etale because `2` is invertible in `Z_ell`; hence its kernel `E[2]` extends to a finite etale group scheme over `Z_ell`.

A finite etale group scheme over `Z_ell` has unramified geometric generic fibre. Thus inertia at `ell` acts trivially on `E[2]`.

Therefore `L/Q` is unramified at every finite prime not dividing `2N` as well.

Combining Steps 2 and 3, `L/Q` is unramified at every finite prime.

Hence its relative discriminant ideal is the unit ideal and its absolute discriminant is

`D_L = 1`.

## Step 4. A totally real cubic field cannot have discriminant `1`

We give the numerical degree-3 Minkowski contradiction explicitly.

For a totally real cubic field `K`, the Minkowski embedding sends `O_K` to a lattice in `R^3` of covolume `sqrt(D_K)`.

Assume `D_K=1`.

For `t>0`, let

`B_t = { (x1,x2,x3) in R^3 : |x1|+|x2|+|x3| < t }`.

This is a centrally symmetric convex body with volume

`vol(B_t) = (4/3) t^3`.

Choose `t` so that

`6 < t^3 < 27`.

Then

`vol(B_t) > 8 = 2^3 * covol(O_K)`.

By the Minkowski convex-body theorem, `B_t` contains a nonzero lattice point corresponding to some nonzero `alpha in O_K`.

By arithmetic-geometric mean,

`|N_{K/Q}(alpha)|
 = product_i |sigma_i(alpha)|
 <= ((|sigma_1(alpha)|+|sigma_2(alpha)|+|sigma_3(alpha)|)/3)^3
 < t^3/27
 < 1`.

But a nonzero algebraic integer has nonzero integral norm, so its absolute norm is at least `1`. Contradiction.

Therefore no totally real cubic number field has discriminant `1`.

## Step 5. Conclusion

The hypothetical `C3` field `L` is a totally real cubic field of discriminant `1`, impossible by Step 4.

Thus the `C3` branch cannot occur.

Since WP10's irreducible-image dichotomy was `C3` or `S3`, we conclude:

**Theorem.** Under the protected semistable odd-conductor good-ordinary-at-2 hypotheses,

`E[2] irreducible  =>  im(rho_bar_{E,2}) = GL_2(F_2) ~= S3`.

Equivalently, residual surjectivity is automatic throughout the selected `BSD-R2-A1` class.

## Firewall

This theorem does not make any other hypothesis of a surjective-residual source theorem automatic. In particular, local Heegner, conductor, Selmer-rank, or level-raising hypotheses must still be checked separately.