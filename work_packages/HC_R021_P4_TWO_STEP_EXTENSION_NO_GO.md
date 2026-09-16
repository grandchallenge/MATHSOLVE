# HC-R021-P4 — Two-step extension criterion and same-divisor extension no-go

**Campaign:** `HC-001`  
**Restricted target:** `HC-R021-A8-CM4-C2`  
**Parent development revision:** `361003b82613637a5287b457396203111ff7bc43`  
**State:** `TWO_STEP_FACTORIZATION_CRITERION__SAME_DIVISOR_PIC0_EXTENSIONS_PRUNED`  
**Date:** 2026-09-16

## 1. Purpose

Test the most economical non-formal repair of the rank-22 split/divisor controls: replace a direct sum of two divisor-supported blocks by a nontrivial extension and ask whether the extension differential can make a nonzero mixed degree-two ambient obstruction nullhomotopic.

The answer is negative for the natural same-divisor blocks used by the current constructions. The result does not rule out extensions between genuinely different supports or extensions involving curve/point quotients.

## 2. Necessary factorization criterion for a two-step extension

Let `A,B` be objects in a fixed dg enhancement and let

```text
e in Ext^1(B,A)
```

define a two-step filtered object `E` with associated graded `A direct_sum B`.

Let `xi in HH^2(X)` be an ambient deformation direction. Write

```text
o_A := ob_A(xi) in Ext^2(A,A),
o_B := ob_B(xi) in Ext^2(B,B).
```

If

```text
ob_E(xi)=0,
```

then the degree-two associated-graded class `(o_A,o_B)` must be killed by the first differential in the endomorphism spectral sequence of the two-step filtration.

That first differential is induced by the extension class `e`. Hence there must exist

```text
c in Ext^1(A,B)
```

such that, up to the fixed sign convention of the enhancement,

```text
e c = o_A,
c e = o_B.
```

Only the existence of such an opposite class is used below. Possible higher/off-diagonal terms can create additional obstructions; they cannot remove this necessary condition.

### HC-R021-L021a — two-step factorization necessity

For a two-step extension to kill a degree-two ambient obstruction which is nonzero on both associated-graded blocks, the two diagonal obstruction classes must factor through one pair of opposite Ext-one classes as above.

## 3. Same smooth divisor blocks

Let

```text
i : S -> X
```

be a smooth ample divisor in the abelian fourfold `X`, with normal bundle

```text
N := N_(S/X)=O_S(S).
```

Let `L_A,L_B` be line bundles on `S` which extend to ambient line bundles on `X`, and set

```text
A=i_*L_A,
B=i_*L_B,
M=L_A tensor L_B^(-1).
```

Because `S` is a Cartier divisor, the ambient two-term resolution of `i_*L_B` has defining equation acting by zero after restriction to `S`. Consequently there is an exact splitting at the level needed here:

```text
Ext^1_X(B,A)
 = H^1(S,M)
   direct_sum H^0(S,M tensor N),
```

and likewise

```text
Ext^1_X(A,B)
 = H^1(S,M^(-1))
   direct_sum H^0(S,M^(-1) tensor N).
```

The second summand is the normal Koszul generator. The product of two normal-degree-one classes is zero because the regular immersion has codimension one: there is no `Lambda^2 N` term.

## 4. Distinct generic Picard-zero twists

Assume now that

```text
M in Pic^0(S)
```

is the restriction of a nontrivial degree-zero line bundle on `X`.

For a nontrivial `P in Pic^0(X)`, all cohomology groups `H^j(X,P)` vanish. Since `S` is ample, Serre duality plus Kodaira/IT0 vanishing gives

```text
H^j(X,P(-S))=0,  j<4.
```

The exact sequence

```text
0 -> P(-S) -> P -> P|_S -> 0
```

therefore gives

```text
H^1(S,M)=0.
```

The same argument applies to `M^(-1)`.

Hence both opposite Ext-one spaces consist entirely of their normal summands:

```text
Ext^1_X(B,A)=H^0(S,M tensor N),
Ext^1_X(A,B)=H^0(S,M^(-1) tensor N).
```

For every

```text
e in Ext^1(B,A),
c in Ext^1(A,B),
```

the two diagonal Yoneda products vanish:

```text
e c=0,
c e=0.
```

Therefore no nonzero degree-two obstruction on the two graded blocks can satisfy the factorization condition of `L021a`.

## 5. Identical block

If `M=O_S`, then the self-Ext algebra of an ambiently extended line bundle on a smooth Cartier divisor is represented by the Koszul algebra

```text
RHom_X(i_*L,i_*L)
 ~= RGamma(S, O_S direct_sum N[-1])
```

with the usual exterior/Koszul product. In particular its degree-one product is graded anti-commutative:

```text
e c = - c e
```

for `e,c in Ext^1(i_*L,i_*L)`.

For a self-extension the two associated-graded obstruction classes are the same class `o`. The factorization requirement would therefore be

```text
e c=o,
c e=o.
```

Over characteristic zero this implies

```text
o=-o,
```

hence `o=0`.

Thus a self-extension cannot kill a nonzero ambient degree-two obstruction which is already present on the underlying divisor block.

## 6. HC-R021-L021 — same-divisor extension no-go

### Statement

Let `S` be a smooth ample divisor and let the graded pieces be ambiently extended line bundles on `S` with the same numerical Chern class, differing at most by degree-zero twists.

Then a two-step extension of those blocks cannot make a nonzero common degree-two ambient obstruction vanish:

1. for distinct generic degree-zero twists, both opposite Ext-one groups are purely normal and every opposite Yoneda product is zero;
2. for identical blocks, opposite degree-one products differ by sign, so they cannot both equal the same nonzero diagonal obstruction.

Therefore the mixed rank-22 failure of the natural smooth-divisor blocks cannot be repaired merely by taking successive extensions among same-support Picard-zero twists.

### Proof

Sections 2-5.

QED.

## 7. Consequences for the current constructions

The result prunes two tempting repairs.

### 7.1 Split line-bundle/divisor control

`HC-R021-L015` and the subsequent divisor-block experiments cannot be repaired by replacing repeated same-support summands with arbitrary two-step extensions among generic `Pic^0` twists.

### 7.2 Divisor elementary-transform candidate

The source bundle

```text
V = direct_sum_j O_S(D) tensor P_j
```

in `HC-R021-L020` uses pairwise generic degree-zero twists. Any non-formality introduced solely by successive extensions among those summands is therefore insufficient to kill the surviving mixed obstructions.

This does not decide the actual elementary transform

```text
E_div -> V -> Q_C direct_sum Q_0,
```

because its non-formality also involves the codimension-two/zero-dimensional quotient. The opposite class relevant there lies in an Ext group involving `Q_C direct_sum Q_0`, not merely another divisor block.

## 8. Refined frontier

After `L021`, a positive second-factor rank-20 construction must use at least one of:

1. extension data between genuinely different divisor supports;
2. the curve/point quotient geometry of the elementary transform `L020`;
3. a higher-rank bundle on a divisor whose internal Atiyah data is not a successive extension of same-Chern-character line blocks;
4. a genuinely non-formal perfect complex with different associated-graded Chern classes.

The smallest next calculation is the elementary-transform factorization problem. Writing

```text
Q := Q_C direct_sum Q_0,
0 -> E_div -> V --rho--> Q -> 0,
```

and viewing `E_div` as the two-step object with graded pieces `Q[-1]` and `V`, vanishing of a mixed obstruction requires an opposite class

```text
c in Ext^2_X(Q,V)
```

whose Yoneda compositions with `rho` reproduce the mixed obstruction classes on `Q` and `V`. This is now the exact finite-dimensional target.

## 9. Claim boundary

```text
HC-R021-L021 = proved_in_solve_package_not_certified
two_step_factorization_condition = necessary
same_divisor_generic_Pic0_extensions_repair_mixed_obstruction = false
same_divisor_self_extensions_repair_nonzero_common_obstruction = false
L020_elementary_transform_mixed_k7_k8 = open
second_factor_rank20 = open
HC-R021-P4 = open
restricted_target_proved = false
full_hodge_conjecture_proved = false
```

## 10. Sources and inputs

- standard filtered-object/endormorphism spectral sequence for a two-step extension;
- Koszul resolution of a smooth Cartier divisor;
- vanishing of cohomology of nontrivial degree-zero line bundles on an abelian variety;
- Kodaira/IT0 vanishing for an ample line bundle on an abelian variety;
- `HC-R021-L015`, `L016`, and `L020`.
