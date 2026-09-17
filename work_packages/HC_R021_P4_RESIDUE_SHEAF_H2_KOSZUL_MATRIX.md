# HC-R021-P4 — Residue sheaf and exact single-row n=1 Koszul matrix

**Campaign:** `HC-001`  
**Restricted target:** `HC-R021-A8-CM4-C2`  
**Parent development revision:** `f24f937b169ffd50bb90d924cc014cf99a1ccb52`  
**State:** `RESIDUE_SHEAF_IDENTIFIED__N1_MATRIX_REDUCED_TO_SINGLE_H2_KOSZUL_ROW__RANK2_NOT_YET_DECIDED`  
**Date:** 2026-09-16

## 1. Purpose

Refine the fixed-scale boundary of `HC-R021-L051`.

The remaining co-supported globalization question from `L049-L051` is not an unspecified collection of cup products. At a correction curve

```text
C = D intersect H intersect A
```

inside the corrected `D`-theta block, the two generic local extension residues form the dual-normal bundle, twisted by the `2D` source weight. Hence the residue sheaf is

```text
R_res = O_C(2D-H) direct_sum O_C(2D-A).
```

Moreover, for each of these two summands, the complete-intersection Koszul resolution has the property that every ambient line-bundle term is nondegenerate of Mumford index `2`. Therefore the hypercohomology spectral sequence has exactly one nonzero row, namely `H^2`.

Thus the exact `n=1` problem is a finite four-term complex of ordinary `H^2` vector spaces with differentials given by multiplication by the chosen theta sections of `D,H,A`.

This package does not assert that the resulting generic residue rank is `2`.

## 2. Geometric setup

Retain the notation of `L049-L051`.

Let `X` be the abelian fourfold source factor, and let

```text
D=(1,1),
H=(a,b),
A=(a^2,b^2),
ab=1,
a+b=tau,
0<a<1<b,
tau>=3.
```

Let `t,h,a_sec` denote chosen sections cutting the three smooth divisors of numerical classes `D,H,A`, and assume their intersection

```text
C=(t=h=a_sec=0)
```

is a smooth complete-intersection curve.

The corrected local theta-square model at a generic point of `C` is the model of `L048-L049` with local regular parameters

```text
t,u,v,w
```

where `u` and `v` are local equations for the `H` and `A` divisors, respectively.

The two local extension residues that survive before the co-supported repair are the two normal coordinates corresponding to `u` and `v`.

## 3. HC-R021-L052a — residue sheaf

### Statement

The two-dimensional generic local residue space globalizes along `C` as

```text
R_res
 = O_C(2D) tensor N^vee_(C/D)
 = O_C(2D-H) direct_sum O_C(2D-A).                 (3.1)
```

### Proof

Inside the smooth `D` divisor, the curve `C` is the regular complete intersection of the restrictions of the `H` and `A` divisors. Therefore

```text
N_(C/D) = O_C(H) direct_sum O_C(A),
N^vee_(C/D) = O_C(-H) direct_sum O_C(-A).           (3.2)
```

The local `L049` extension residues are the two coefficients dual to the normal generators `u,v`. The ordinary co-supported double-`D` block is represented by

```text
B_D = [ O(-D) --t^2--> O(D) ].
```

The local residue column starts at the degree `-1` source term `O(-D)` and lands in the two corrected degree-zero coordinates whose numerical line classes are `D-H` and `D-A`. Consequently the two Hom weights are

```text
(D-H)-(-D)=2D-H,
(D-A)-(-D)=2D-A.                                    (3.3)
```

These are precisely `O_C(2D)` times the two dual normal lines in (3.2). Changes of regular generators `u,v` act by the transition functions of the conormal bundle, so the identification is intrinsic.

QED.

### Consequence

Any two global co-supported extension classes whose generic residues span the fibre of `R_res` kill the two local `alpha,beta` residue directions of `L049b`. Conversely, a generic residue image of rank less than two cannot realize the two-channel local repair.

## 4. Koszul resolution for a residue line

For a line bundle `L` on `X`, the restriction `L|_C` has the standard Koszul resolution

```text
0 -> L-D-H-A
   -> (L-D-H) direct_sum (L-D-A) direct_sum (L-H-A)
   -> (L-D) direct_sum (L-H) direct_sum (L-A)
   -> L
   -> L|_C -> 0.                                    (4.1)
```

The differentials are the standard alternating Koszul matrices whose entries are multiplication by the fixed sections

```text
t in H^0(D),
h in H^0(H),
a_sec in H^0(A).                                    (4.2)
```

We apply (4.1) to

```text
L_H := 2D-H,
L_A := 2D-A.                                         (4.3)
```

## 5. Index-two chamber

For a class

```text
P=xD+yH+zA
```

its two RM weights are

```text
lambda_1(P)=x+y a+z a^2,
lambda_2(P)=x+y b+z b^2.                             (5.1)
```

Each RM block has complex dimension two. Thus if the two weights have opposite signs, the corresponding nondegenerate line bundle has Mumford index `2`.

Since

```text
a+b=tau,
ab=1,
tau>=3,
```

we have

```text
0<a<=(3-sqrt(5))/2<1/2,
b>= (3+sqrt(5))/2>2.                                (5.2)
```

### 5.1 The `L_H` complex

The eight line classes occurring in (4.1) are

```text
2D-H,
D-H,
2D-2H,
2D-H-A,
D-2H,
D-H-A,
2D-2H-A,
D-2H-A.                                             (5.3)
```

Their first RM weights reduce to

```text
2-a,
1-a,
2(1-a),
(1-a)(a+2),
1-2a,
1-a-a^2,
2-2a-a^2,
1-2a-a^2.                                           (5.4)
```

All are positive on the interval (5.2). The smallest endpoint constraint is

```text
1-2a-a^2>0
```

which holds because `a<(sqrt(2)-1)` and `(3-sqrt(5))/2 < sqrt(2)-1`.

The corresponding second weights are obtained by replacing `a` by `b`; each is negative for `b>2`.

Hence every line bundle in (5.3) is nondegenerate of index `2`.

### 5.2 The `L_A` complex

The eight line classes are

```text
2D-A,
D-A,
2D-H-A,
2D-2A,
D-H-A,
D-2A,
2D-H-2A,
D-H-2A.                                             (5.5)
```

Their first RM weights are

```text
2-a^2,
1-a^2,
2-a-a^2,
2(1-a^2),
1-a-a^2,
1-2a^2,
2-a-2a^2,
(1+a)(1-2a).                                        (5.6)
```

Again all are positive for (5.2), while replacing `a` by `b>2` makes every weight negative. Thus every line bundle in (5.5) is also nondegenerate of index `2`.

### HC-R021-L052b

Every ambient line bundle in both residue Koszul resolutions has cohomology in degree `2` only.

This is an exact fixed-scale statement; no asymptotic positivity is used.

## 6. Exact `n=1` matrix

Apply ambient cohomology to (4.1). By `L052b`, all rows except `q=2` in the hypercohomology spectral sequence vanish.

Thus for each `L` in `{L_H,L_A}` the entire calculation is the four-term complex

```text
K_L:
H^2(L-D-H-A)
 -> H^2(L-D-H) direct_sum H^2(L-D-A) direct_sum H^2(L-H-A)
 -> H^2(L-D) direct_sum H^2(L-H) direct_sum H^2(L-A)
 -> H^2(L).                                          (6.1)
```

The matrices in (6.1) are precisely multiplication by `t,h,a_sec`, with the ordinary Koszul signs.

Because `L|_C` is a sheaf on a curve, the first map in (6.1) is injective and the last map is surjective. The only cohomology of (6.1) is

```text
H^0(C,L|_C)
```

at the first middle position and

```text
H^1(C,L|_C)
```

at the second middle position. In particular,

```text
H^0(C,L|_C)
 = ker(d_2)/im(d_3).                                 (6.2)
```

Equation (6.1), for `L=L_H` and `L=L_A`, is the exact `n=1` theta cup-product matrix required by `L051` at the level of the two residue summands.

## 7. Dimensions are explicit but do not determine the middle rank

For `P=xD+yH+zA`, principal normalization gives

```text
chi(P)=Nm(P)^2,
Nm(P)
 = x^2 + xy tau + xz(tau^2-2) + y^2 + yz tau + z^2. (7.1)
```

Since all terms have index `2`,

```text
h^2(P)=chi(P)=Nm(P)^2.                               (7.2)
```

For example,

```text
h^2(2D-H)=(2tau-5)^2,
h^2(2D-A)=(2tau^2-9)^2,
h^2(H+A-D)=(tau^2-5)^2,                             (7.3)
```

as already recorded in `L050`.

All remaining dimensions in (6.1) follow from (7.1). However, dimensions alone do not determine the middle cohomology. The actual `n=1` multiplication maps remain section-dependent.

## 8. Fixed-scale nonzero multiplication is available after translation

There is nevertheless one stronger fixed-scale input than was used in `L051`.

For any edge in (6.1) obtained by multiplying an index-two line bundle `P` by one of the principal theta sections `Theta_0 in {D,H,A}`, the pair

```text
(P, Theta_0)
```

satisfies the pair-index condition:

```text
i(P)=2,
i(Theta_0)=0,
i(P+Theta_0)=2.                                  (8.1)
```

Nathan Grieve, *Index conditions and cup-product maps on abelian varieties*, Corollary 5.3(a), proves that for a pair satisfying the pair-index condition there exists a degree-zero translation for which the fixed-scale cup-product map is nonzero. Equivalently, in the associated translation family the zero locus of that cup product is a proper closed subset.

Therefore each individual edge of (6.1) can be made nonzero at `n=1`, and finitely many such individual nonvanishing conditions may be imposed simultaneously on a nonempty open set of the relevant translation parameters.

This does **not** imply that the middle cohomology (6.2) has the dimension required for rank-two residue globalization. Grieve's theorem controls individual cup-product maps, not the determinant/minor of the coupled Koszul matrix.

## 9. Quantifier relevant to the campaign

`HC-R021-A8-CM4-C2` fixes a source datum of Markman's type and then transports a nonzero Weil component over the selected connected PEL component. The source construction is not tied to one explicit numerical period matrix or one fixed choice of theta characteristics for the translated correction divisors.

Consequently an admissible special source choice can be useful, provided it still satisfies the source hypotheses and the resulting object supplies the required deformation input. A statement that a residue vanishes only for generic translations is therefore insufficient to close the lane; conversely, one explicit admissible source point with a nonzero rank-two minor is enough to keep this construction viable at first order.

## 10. Sharpened frontier

The old boundary

```text
MISSING_FIXED_SCALE_RM_THETA_CUP_PRODUCT_MATRIX
```

is now replaced by the more precise problem

```text
MISSING_MIDDLE_MINOR_OF_TWO_SINGLE_ROW_H2_KOSZUL_COMPLEXES.   (10.1)
```

The objects to evaluate are explicitly (6.1) for

```text
L=2D-H,
L=2D-A.
```

The decisive geometric question is whether two global extension classes can be chosen whose images in the generic fibre of

```text
R_res=O_C(2D-H) direct_sum O_C(2D-A)
```

span both summands.

A proof that the relevant middle minor is nonzero at one admissible source choice leaves the co-supported globalization route viable. A proof that its rank is always less than two closes the route.

## 11. Claim boundary

```text
HC-R021-L052a = proved_in_solve_package_not_certified
residue_sheaf = O_C(2D-H) direct_sum O_C(2D-A)
HC-R021-L052b = proved_in_solve_package_not_certified
both_residue_Koszul_complexes_have_only_H2_ambient_row = true
exact_n1_matrix_shape = explicit_four_term_H2_Koszul_complex
individual_n1_edges_can_be_nonzero_after_translation = source_theorem
rank2_middle_minor = open
cosupported_global_extension = open
second_factor_rank20 = open
all_orders_transport = open
HC-R021-P4 = open
restricted_target_proved = false
full_hodge_conjecture_proved = false
```

## 12. Inputs

- `HC-R021-L049`: local two-channel co-supported nullhomotopy;
- `HC-R021-L050`: global hyper-Ext reduction and RM index-two dimensions;
- `HC-R021-L051`: fixed-scale cup-product boundary;
- Nathan Grieve, *Index conditions and cup-product maps on abelian varieties*, International Journal of Mathematics 25 (2014), arXiv:1308.1970, especially Proposition 5.2 and Corollary 5.3(a);
- Mumford's index theorem and the standard Koszul resolution of a regular complete intersection.
