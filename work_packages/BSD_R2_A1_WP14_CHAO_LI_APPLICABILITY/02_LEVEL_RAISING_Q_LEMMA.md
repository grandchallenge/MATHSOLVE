# Lemma — simultaneous order-two residual Frobenius and inertness in `K`

## Proposition `BSD-A1-Q001`

Let `E/Q` satisfy the selected `BSD-R2-A1` hypotheses and let `K/Q` be any WP09 auxiliary imaginary quadratic field. Then there are infinitely many primes `q` such that:

1. `q` does not divide `2ND`;
2. `q` is inert in `K`;
3. `rho_bar_{E,2}(Frob_q)` has order `2` in `GL_2(F_2) ~= S3`;
4. `a_q(E)` is even.

In particular, such `q` satisfy the mod-2 level-raising parity condition appearing in the admitted Chao Li route.

## Proof

By WP12, if

`L = Q(E[2])`,

then

`Gal(L/Q) ~= S3`.

The extension `K/Q` is quadratic and both `L/Q` and `K/Q` are Galois. There are two possible intersections.

### Case 1 — `L intersect K = Q`

Then

`Gal(LK/Q) ~= S3 x C2`.

Choose a transposition `tau in S3` and the nontrivial element `epsilon in C2`. The element

`(tau,epsilon)`

has the required restrictions: order-two residual Frobenius on `L` and nontrivial Frobenius on `K`.

By Chebotarev, infinitely many primes unramified in `LK` have Frobenius in the conjugacy class of `(tau,epsilon)`. Excluding the finite set dividing `2ND` leaves infinitely many such primes. Their Frobenius in `K/Q` is nontrivial, so they are inert in `K`.

### Case 2 — `K` is contained in `L`

The unique quadratic subfield of an `S3` extension is the fixed field of `A3`; the quotient map

`S3 -> S3/A3 ~= C2`

is the sign map.

Every transposition `tau` has nontrivial image in that quotient. Chebotarev applied to the transposition conjugacy class in `Gal(L/Q)` therefore gives infinitely many primes `q` whose residual Frobenius has order two and whose restriction to `K` is nontrivial. Again exclude the finite set dividing `2ND`.

This proves assertions 1--3 in both cases.

For such a prime `q`, the curve has good reduction. Compatibility of the mod-2 representation gives

`a_q(E) mod 2 = tr(rho_bar_{E,2}(Frob_q))`.

Every order-two element of `GL_2(F_2)` is a nonidentity unipotent matrix. Its trace is `0` in `F_2`. Hence

`a_q(E) == 0 (mod 2)`.

This proves assertion 4.

## Scope

The lemma constructs the auxiliary prime required by the source route. It does not prove that level raising lowers a Selmer rank, does not prove primitivity of a Kolyvagin system, and does not establish any leading-term valuation.
