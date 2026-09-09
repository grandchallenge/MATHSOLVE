# Proposition — exact meaning of `s_2(E/K)=1` in the WP09 lane

Let `E/Q` satisfy the selected `BSD-R2-A1` hypotheses and let

`K = Q(sqrt(D))`

be a WP09 auxiliary field. Put

`s_2(E/K) := dim_F2 Sel_2(E/K)`.

Then

`s_2(E/K) = 1 + dim_F2 Sha(E/K)[2]`.

Consequently,

`s_2(E/K)=1 <=> Sha(E/K)[2]=0`.

## Step 1 — rank of `E(K)`

WP09 gives

`L(E^D,1) != 0`.

The protected low-analytic-rank theorem interface `BSD-T-060` therefore gives

`rank E^D(Q)=0`.

The selected hypothesis gives `ord_{s=1}L(E,s)=1`, so the same interface gives

`rank E(Q)=1`.

For a quadratic extension,

`E(K) tensor Q ~= (E(Q) tensor Q) direct_sum (E^D(Q) tensor Q)`

through the plus/minus eigenspace decomposition for `Gal(K/Q)`. Therefore

`rank E(K)=1+0=1`.

## Step 2 — no rational 2-torsion over `K`

Let

`L = Q(E[2])`.

WP12 gives

`Gal(L/Q) ~= S3`.

If `K intersect L = Q`, then the image of `G_K` on `E[2]` remains `S3`. The natural two-dimensional `F_2` representation has no nonzero vector fixed by all of `S3`.

If `K` is contained in `L`, it is the unique quadratic subfield, so the image of `G_K` is `A3 ~= C3`. A generator of this subgroup has minimal polynomial

`X^2+X+1`

over `F_2`, hence has no eigenvalue `1` and no nonzero fixed vector.

Thus in either case

`E(K)[2]=0`.

## Step 3 — Kummer exact sequence

The standard 2-Selmer exact sequence is

`0 -> E(K)/2E(K) -> Sel_2(E/K) -> Sha(E/K)[2] -> 0`.

For a finitely generated abelian group,

`dim_F2 E(K)/2E(K) = rank E(K) + dim_F2 E(K)[2]`.

Steps 1 and 2 give

`dim_F2 E(K)/2E(K)=1`.

Taking `F_2` dimensions in the exact sequence yields

`s_2(E/K)=1+dim_F2 Sha(E/K)[2]`.

This proves the proposition.

## Consequence for the Chao Li route

The source hypothesis `s_2(E/K)=1` is not another expression of analytic rank one. In the WP09 lane it is exactly the additional assertion

`Sha(E/K)[2]=0`.

The selected `BSD-R2-A1` assumptions and WP09 do not supply that assertion. It may therefore not be silently inserted to invoke the source's rank-lowering obstruction theorem.

## Scope

No finiteness of the full group `Sha(E/K)` is needed for this finite 2-Selmer calculation. The proposition does not compute `Sha(E/Q)[2^infinity]`, a Tamagawa length, or a leading-term valuation.
