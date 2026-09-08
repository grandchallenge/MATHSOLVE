# Theorem B — exact prime-to-2 Selmer and Sha control

Let `M/F` be a finite Galois extension of odd degree `d`, with group `G`, and let `E/F` be an elliptic curve. Fix `n>=1`.

## B1. Cohomology has no odd-degree defect on 2-primary coefficients

For any finite 2-primary `G`-module `A`, the groups `H^i(G,A)` for `i>0` are killed by `|G|=d`. They are also 2-primary. Since `gcd(d,2)=1`, multiplication by `d` is an automorphism of `A` and of every 2-primary quotient. Hence

`H^i(G,A)=0` for every `i>0`.

Apply this to `A=E[2^n](M)`. Inflation-restriction gives

`H^1(F,E[2^n]) ~= H^1(M,E[2^n])^G`.

The same argument applies locally at every place, with the decomposition subgroup in place of `G`; its order also divides the odd integer `d`.

## B2. Kummer subgroups descend exactly

Restriction induces

`E(F)/2^n E(F) -> (E(M)/2^n E(M))^G`.

This is an isomorphism.

### Injectivity

Suppose `P in E(F)` becomes `2^n Q` in `E(M)`. Taking the norm gives

`d P = 2^n N(Q)`.

Choose integers `a,b` with `ad + b 2^n = 1`. Then

`P = 2^n(a N(Q) + b P)`,

so `P` was already divisible by `2^n` in `E(F)`.

### Surjectivity

Let `[Q]` be a `G`-fixed class in `E(M)/2^nE(M)`. Then

`N(Q) = sum_{sigma in G} sigma Q`

lies in `E(F)`, and invariance gives

`[N(Q)] = d[Q]` in `E(M)/2^nE(M)`.

Choose `a` with `ad == 1 (mod 2^n)`. Then

`[Q] = res([aN(Q)])`.

The same norm argument works over every completion. Therefore the local Kummer conditions correspond exactly under the cohomological restriction isomorphisms.

## B3. Selmer control

By the global and local diagrams defining the finite-level Selmer group,

`Sel_{2^n}(E/F) ~= Sel_{2^n}(E/M)^G`.

There is no 2-primary restriction kernel or cokernel.

## B4. Sha control

The Kummer exact sequence is

`0 -> E(F)/2^nE(F) -> Sel_{2^n}(E/F) -> Sha(E/F)[2^n] -> 0`.

For finite 2-primary `G`-modules the invariants functor is exact, because its higher cohomology vanishes by B1. Combining the Kummer and Selmer isomorphisms gives

`Sha(E/F)[2^n] ~= Sha(E/M)[2^n]^G`.

Passing to the direct limit over `n` gives

`Sha(E/F)[2^infinity] ~= Sha(E/M)[2^infinity]^G`.

This statement does not require finiteness of the full 2-primary Sha group; if it is finite, it is an isomorphism of finite 2-groups.

## B5. Integral averaging decomposition

Assume now `G=C3=<sigma>` and let `X` be any 2-primary `C3`-module. Because `3` is a unit in `Z_2`, the operator

`e = (1 + sigma + sigma^2)/3`

is well-defined integrally on `X` and satisfies `e^2=e`.

Moreover,

`eX = X^{C3}`

and

`(1-e)X = ker(1+sigma+sigma^2)`.

Hence

`X = X^{C3} direct_sum ker(N)`

with `N=1+sigma+sigma^2`.

Applying this to finite-level Selmer and Sha groups over `L` gives exact direct decompositions whose invariant summands are the corresponding groups over `Q` by B3-B4. There is no intersection defect and no cokernel analogous to the quadratic `(1 +/- tau)/2` problem from WP06.

## Corollary for WP11

For `L=Q(E[2])` in the `C3` residual branch and every `n>=1`,

`Sel_{2^n}(E/Q) ~= Sel_{2^n}(E/L)^{C3}`,

`Sha(E/Q)[2^n] ~= Sha(E/L)[2^n]^{C3}`,

and

`Sha(E/Q)[2^infinity] ~= Sha(E/L)[2^infinity]^{C3}`.

The `Q`-side 2-primary arithmetic is an exact direct summand of the `L`-side arithmetic.