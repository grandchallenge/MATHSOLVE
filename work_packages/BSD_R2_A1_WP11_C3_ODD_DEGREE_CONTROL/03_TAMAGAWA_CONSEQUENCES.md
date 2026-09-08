# Theorem C — discriminant and Tamagawa consequences in the `C3` branch

Assume the WP11 `C3` residual branch.

## C1. Square discriminant class

The action of `G_Q` on the three nonzero points of `E[2]` identifies the residual image with the Galois group of the 2-division cubic. Under the `C3` branch this group is the alternating subgroup `A3` of `S3`.

For a separable cubic, the Galois group lies in `A3` exactly when its discriminant is a square. The discriminant of the 2-division cubic has the same square class as the elliptic discriminant. Therefore

`Delta_min in Q^x / Q^{x2}`

has trivial square class.

Consequently, for every prime `ell`,

`ord_ell(Delta_min)` is even.

At `2` this is `0` because the conductor is odd and reduction is good. At each `ell|N`, semistability gives multiplicative Kodaira type `I_{n_ell}` with

`n_ell = ord_ell(Delta_min)`,

so every `n_ell` is even.

## C2. Tamagawa valuation

For split multiplicative type `I_n`, the component group is cyclic of order `n`; hence

`c_ell = n_ell`.

For nonsplit multiplicative type `I_n`, Frobenius acts by inversion on the geometric cyclic component group `Z/nZ`. The rational component group is the fixed subgroup, of order

`gcd(2,n)`.

Since `n_ell` is even in the `C3` branch,

- split multiplicative: `ord_2(c_ell)=ord_2(n_ell)>=1`;
- nonsplit multiplicative: `c_ell=2`, hence `ord_2(c_ell)=1`.

Thus every bad prime contributes a positive 2-adic Tamagawa valuation in the `C3` branch, and the exact sum is

`sum_{ell|N} ord_2(c_ell)
 = sum_{ell|N, split mult} ord_2(n_ell)
   + #{ell|N : nonsplit mult}`.

## C3. Compatibility with complete splitting of `2N`

Theorem A independently proves that every `ell|N` splits completely in `L=Q(E[2])`. This is compatible with the even `I_{n_ell}` condition: locally, full rational 2-torsion forces the multiplicative mod-2 representation to be trivial rather than merely reducible.

## Consequence for the direct-length frontier

In the `C3` branch the target right-hand side is already reduced by WP05 to

`len_Z2 Sha(E/Q)[2^infinity] + sum_{ell|N} ord_2(c_ell)`.

WP11 makes the Tamagawa summand completely explicit in terms of the multiplicative reduction data above. Therefore the genuinely unknown arithmetic quantity in this branch is reduced to the invariant Sha length together with the analytic-to-arithmetic equality itself.

This is a structural reduction only. No equality with the WP00 complex leading term is asserted here.