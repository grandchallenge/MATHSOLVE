# Theorem — square-class information cannot determine the exact `2`-primary BSD length

Let `E/Q` satisfy the protected `BSD-R2-A1` hypotheses.

Define

`A_2(E) := ord_2(L'(E,1)/(Omega_E Reg_E))`

and

`T_2(E) := sum_{ell|N} ord_2(c_ell)`.

The selected target is

`A_2(E) = len_Z2 Sha(E/Q)[2^infinity] + T_2(E)`.

We prove what a BSD statement only modulo rational squares can and cannot determine.

## 1. No rational 2-primary torsion

Protected WP05 proves that irreducibility of `E[2]` implies `#E(Q)_tors` is odd.

For completeness, the elementary reason is: a rational point of order divisible by `2` yields, after multiplication by the appropriate power of `2`, a nonzero rational point of order `2`. That spans a `G_Q`-stable line in `E[2]`, contradicting irreducibility.

Hence

`ord_2(#E(Q)_tors)=0`.

## 2. Finite Sha and the Cassels–Tate pairing

The protected WP05 rank-one interface gives finiteness of `Sha(E/Q)` under analytic rank one.

Protected MATHFORGE `118ae1b5c2fc2630f53000921b742c610c50db16` admits the Poonen–Stoll Cassels–Tate interface:

- the Cassels–Tate pairing is nondegenerate on `Sha_nd`;
- for an elliptic curve it is alternating.

Because `Sha(E/Q)` is finite, its maximal divisible subgroup is zero. Therefore there is a nondegenerate alternating pairing

`< , > : Sha(E/Q) x Sha(E/Q) -> Q/Z`.

## 3. Finite-group lemma: an alternating nondegenerate group has square order

Let `G` be a finite abelian group with a nondegenerate alternating pairing into `Q/Z`.

Decompose `G` into its primary parts. Distinct primary parts are orthogonal, so it suffices to treat a finite abelian `p`-group.

Choose `x` of maximal order `p^n`. Nondegeneracy gives `y` such that `<x,y>` has exact order `p^n`; otherwise `p^(n-1)x` would pair trivially with every element. Maximality gives `ord(y)<=p^n`, while the order of `<x,y>` forces `ord(y)>=p^n`, so `ord(y)=p^n`.

Let `H=<x,y>`. If `a x = b y`, pairing with `x` gives

`b<y,x>=0`.

Since `<y,x>` has exact order `p^n`, `p^n|b`, hence `b y=0` and also `a x=0`. Thus

`H ~= Z/p^n Z x Z/p^n Z`.

The restriction of the pairing to `H` is nondegenerate. Consequently

`G = H direct_sum H^perp`.

Induction on `#G` shows every primary part has square cardinality. Therefore `#G` is a square.

Applying this to `Sha(E/Q)` gives

`#Sha(E/Q) = s^2`

for an integer `s`, and in particular

`len_Z2 Sha(E/Q)[2^infinity] = ord_2(#Sha(E/Q))`

is an even nonnegative integer.

## 4. What BSD modulo rational squares says at `2`

The rank-one BSD leading-term expression has arithmetic side

`#Sha(E/Q) * product_{ell|N} c_ell / (#E(Q)_tors)^2`

in the protected WP00/WP05 normalization.

Suppose only that this equality is known in

`Q^x/(Q^x)^2`.

Applying `ord_2` modulo `2` gives

`A_2(E) = ord_2(#Sha(E/Q)) + T_2(E) - 2 ord_2(#E(Q)_tors)   (mod 2)`.

The first term is even by Section 3 and the last term is zero by Section 1. Therefore

`A_2(E) = T_2(E) (mod 2)`.

Equivalently, the defect

`delta_2(E) := A_2(E) - T_2(E)`

is even.

## 5. Why this cannot close `BSD-R2-A1`

The selected target requires the integer equality

`delta_2(E) = len_Z2 Sha(E/Q)[2^infinity]`.

Both sides are even, but parity does not determine their magnitude. The possible Sha lengths

`0, 2, 4, 6, ...`

all have the same residue modulo `2`.

Thus even an **absolute** proof of the rank-one BSD formula modulo rational squares would leave an unbounded even-integer ambiguity in the exact `2`-primary Sha length.

A theorem that merely transports the modulo-square statement between twists is weaker still: without an absolute seed it does not establish even the parity statement for an arbitrary selected curve.

## Theorem `BSD-A1-SQ001`

For the selected class, BSD modulo rational squares can determine at most the parity relation

`A_2(E) = T_2(E) (mod 2)`.

It cannot by itself determine the exact selected integer equality.

**Status:** `PROVED_IN_PACKAGE_FROM_PROTECTED_INTERFACES`.

## Firewall

This theorem is an information-loss result. It does not assert that the modulo-square BSD statement is known for every selected curve, and it does not assert that no stronger theorem exists. It only proves that square-class information, even if supplied, is structurally insufficient to recover the exact unsquared `2`-primary length.