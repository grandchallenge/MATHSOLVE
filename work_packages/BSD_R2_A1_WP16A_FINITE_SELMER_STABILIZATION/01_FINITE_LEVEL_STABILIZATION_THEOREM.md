# Finite-level `2^n`-Selmer stabilization theorem

## Setup

Let `E/Q` lie in the selected `BSD-R2-A1` class. Use the protected inputs:

- `rank E(Q) = 1`;
- `#E(Q)_tors` is odd;
- `Sha(E/Q)` is finite.

For each integer `n >= 1`, use the Kummer exact sequence

`0 -> E(Q)/2^n E(Q) -> Sel_{2^n}(E/Q) -> Sha(E/Q)[2^n] -> 0`

and define

`s_n(E) := ord_2 #Sel_{2^n}(E/Q) - n`.

No Birch-Swinnerton-Dyer leading-term identity is assumed below.

## Lemma 1 — exact Mordell-Weil quotient

For every `n >= 1`,

`#(E(Q)/2^n E(Q)) = 2^n`.

### Proof

By Mordell-Weil and the protected rank-one input,

`E(Q) ~= Z direct_sum T`,

where `T = E(Q)_tors` is finite. Protected WP05 proves `#T` is odd.

Because `gcd(2^n,#T)=1`, multiplication by `2^n` is an automorphism of `T`. Hence

`T/2^n T = 0`.

Therefore

`E(Q)/2^n E(Q) ~= (Z/2^n Z) direct_sum (T/2^n T) ~= Z/2^n Z`,

so its order is exactly `2^n`. QED.

## Theorem 2 — finite-level Selmer/Sha identity

For every `n >= 1`,

`#Sel_{2^n}(E/Q) = 2^n #Sha(E/Q)[2^n]`,

and consequently

`s_n(E) = ord_2 #Sha(E/Q)[2^n]`.

### Proof

The Kummer exact sequence is a short exact sequence of finite groups in the selected class. Lemma 1 gives the exact order of its left term. Multiplicativity of cardinality in a short exact sequence gives

`#Sel_{2^n}(E/Q)`

`= #(E(Q)/2^n E(Q)) * #Sha(E/Q)[2^n]`

`= 2^n #Sha(E/Q)[2^n]`.

Taking `ord_2` gives

`ord_2 #Sel_{2^n}(E/Q) = n + ord_2 #Sha(E/Q)[2^n]`.

Subtracting `n` proves

`s_n(E) = ord_2 #Sha(E/Q)[2^n]`. QED.

## Lemma 3 — eventual stabilization of the finite Sha layers

Let

`A := Sha(E/Q)[2^infinity]`.

There exists an integer `m >= 0` such that for every `n >= max(1,m)`,

`Sha(E/Q)[2^n] = A`.

### Proof

Protected WP05 gives finiteness of `Sha(E/Q)`, hence its `2`-primary subgroup `A` is finite. A finite `2`-primary abelian group has finite exponent, say dividing `2^m` for some `m >= 0`.

Every element killed by `2^n` is `2`-primary, so

`Sha(E/Q)[2^n] = A[2^n]`.

For `n >= m`, multiplication by `2^n` kills every element of `A`; hence `A[2^n]=A`. Therefore `Sha(E/Q)[2^n]=A` for all sufficiently large `n`. QED.

## Lemma 4 — cardinality valuation equals `Z_2`-length

For a finite `2`-primary abelian group `A`, regarded as a finite `Z_2`-module,

`len_Z2(A) = ord_2 #A`.

### Proof

By the structure theorem for finite abelian `2`-groups,

`A ~= direct_sum_{i=1}^r Z/2^{a_i}Z`

for integers `a_i >= 1`, with the empty sum allowed when `A=0`.

Length and cardinality are additive/multiplicative across the direct sum:

`len_Z2(A) = sum_i a_i`,

while

`#A = product_i 2^{a_i} = 2^{sum_i a_i}`.

Thus `ord_2 #A = sum_i a_i = len_Z2(A)`. QED.

## Theorem 5 — stabilization to the full `2`-primary Sha length

The sequence `s_n(E)` is eventually constant and

`lim_{n -> infinity} s_n(E) = len_Z2 Sha(E/Q)[2^infinity]`.

More precisely, if `2^m` annihilates `Sha(E/Q)[2^infinity]`, then for every `n >= max(1,m)`,

`s_n(E) = len_Z2 Sha(E/Q)[2^infinity]`.

### Proof

By Theorem 2,

`s_n(E) = ord_2 #Sha(E/Q)[2^n]`.

By Lemma 3, the finite subgroup on the right is eventually the full group

`A = Sha(E/Q)[2^infinity]`.

Hence for all sufficiently large `n`,

`s_n(E) = ord_2 #A`.

Lemma 4 identifies the stable value with `len_Z2 A`. Since an eventually constant integer sequence has that value as its limit, the theorem follows. QED.

## Corollary 6 — exact reformulation of the selected target

Recall

`delta_2(E) := ord_2(L'(E,1)/(Omega_E Reg_E)) - sum_{ell|N} ord_2(c_ell)`.

Within the selected class, the unresolved equality

`delta_2(E) = len_Z2 Sha(E/Q)[2^infinity]`

is equivalent to

`delta_2(E) = lim_{n -> infinity} s_n(E)`.

### Proof

Theorem 5 proves that the two right-hand sides are equal using only the protected rank-one/finiteness/torsion inputs and Kummer exactness. Substitution gives an equivalence of statements. No BSD equality is used to establish the substitution. QED.

## Dependency and claim audit

The proof uses no parity argument and no modulo-square statement. It therefore retains the complete nonnegative integer `2`-primary length rather than only its parity.

It uses no odd-prime theorem, no `p>2` specialization, no numerical stabilization, no Selmer-complex normalization, and no statement only valid up to a unit.

The theorem changes the representation of the remaining unknown integer. It does not determine that integer analytically. Accordingly

`BSD-R2-A1 = SELECTED_RESEARCH_TARGET_UNPROVED`

remains unchanged.

## WP16B interface exported by WP16A

Any WP16B integral object is acceptable only if it realizes, with exact equality and explicit local conditions, the stable integer

`lim_n (ord_2 #Sel_{2^n}(E/Q) - n)`.

This is the invariant that the subsequent determinant/Fitting/Selmer-complex formalism must match. No particular formalism is selected in WP16A.