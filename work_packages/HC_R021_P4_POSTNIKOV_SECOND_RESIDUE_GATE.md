# HC-R021-P4 — Postnikov reduction of the second co-supported residue

**Campaign:** `HC-001`  
**Restricted target:** `HC-R021-A8-CM4-C2`  
**Parent development revision:** `b43dbd15ed8025f894b916b8cd88bfdd1c269864`  
**State:** `SECOND_LOCALIZABLE_RESIDUE_FACTORS_THROUGH_M_KERNEL__FIXED_SCALE_INJECTIVITY_OPEN`  
**Date:** 2026-09-17

## 1. Purpose

Refine `HC-R021-L052` before treating the two residue-sheaf Koszul rows as the image of the global extension group.

The residue sheaf

```text
R_res ~= O_C(2D-H) direct_sum O_C(2D-A)
```

is the correct local target, but a global class in `Ext^1(B_D,C_corr)` does not map to an arbitrary section of that sheaf. The corrected cone has a nontrivial codimension-three dual cohomology sheaf. The resulting Postnikov transgression is the gate through which any genuinely derived second residue must pass.

The main result below identifies that gate with the line bundle

```text
M := H+A-D
```

on the correction curve and writes its exact fixed-scale `n=1` cup-product matrix.

## 2. Setup

Let

```text
C = D cap H cap A
```

be a smooth complete-intersection correction curve in the abelian fourfold `X`, and set

```text
E := I_C(D).
```

Let

```text
B := B_D = O_(2D)(D)
```

with locally free resolution

```text
0 -> O(-D) --t^2--> O(D) -> B -> 0,
```

where `t` is the theta section cutting out `D`.

The corrected theta-square cone is

```text
C_corr := Cone(E^vee -> E),
```

where the degree-zero morphism is induced by `t^2`.

## 3. Cohomology sheaves of the derived dual

The ideal sequence

```text
0 -> I_C -> O_X -> O_C -> 0
```

and the regular-embedding identity

```text
Ext_X^j(O_C,O_X)=0, j != 3,
Ext_X^3(O_C,O_X) ~= det N_(C/X)
                  ~= O_C(D+H+A)
```

give

```text
H^0(RHom(I_C,O_X)) ~= O_X,
H^2(RHom(I_C,O_X)) ~= O_C(D+H+A),
```

with all other cohomology sheaves zero.

After twisting by `O(-D)`, therefore,

```text
H^0(E^vee) ~= O(-D),
H^2(E^vee) ~= G := O_C(H+A).                         (3.1)
```

The map `E^vee -> E` induces on degree-zero cohomology exactly

```text
O(-D) --t^2--> I_C(D).
```

Consequently `C_corr` has precisely two cohomology sheaves,

```text
H^0(C_corr) ~= F := I_C(D)/t^2 O(-D),
H^1(C_corr) ~= G := O_C(H+A).                         (3.2)
```

Equivalently there is a Postnikov triangle

```text
F -> C_corr -> G[-1] -> F[1].                        (3.3)
```

The connecting morphism is a generally nontrivial class in `Ext_X^2(G,F)`.

## 4. The localizable part of the derived channel

The truncation triangle for `E^vee` is

```text
O(-D) -> E^vee -> G[-2] -> O(-D)[1].                 (4.1)
```

Applying `RHom(B,-)` gives the exact segment

```text
Ext_X^2(B,O(-D))
 -> Ext_X^2(B,E^vee)
 -> Hom_X(B,G)
 -> Ext_X^3(B,O(-D)).                                 (4.2)
```

The sheaf `mathcal Ext_X^2(B,O(-D))` vanishes because `B` has projective dimension one. Hence every class in the first term of (4.2) is a positive-Cech-degree class. It restricts to zero in the Ext group of the generic local ring along `C`.

Therefore every component of `Ext_X^2(B,E^vee)` which can contribute a nonzero **generic local residue** factors through

```text
Hom_X(B,G).                                           (4.3)
```

Since `t^2` vanishes on `C`, applying `Hom(-,G)` to the two-term resolution of `B` gives

```text
Hom_X(B,G)
 ~= H^0(C,G(-D))
 ~= H^0(C,O_C(H+A-D)).                                (4.4)
```

Define

```text
M := H+A-D.                                           (4.5)
```

Thus a second localizable global residue can exist only if

```text
H^0(C,M|_C) != 0.                                    (4.6)
```

This condition is necessary, not sufficient: a section must also survive the connecting map in (4.2) and the subsequent map `Ext^2(B,E^vee) -> Ext^2(B,E)` from `L050`.

In particular,

```text
H^0(C,M|_C)=0
=> generic residue rank <= 1
=> the two-channel co-supported repair cannot globalize. (4.7)
```

## 5. Exact `n=1` Koszul matrix for the M-channel

Resolve `M|_C` by the Koszul complex of the fixed theta sections

```text
t in H^0(D),
h in H^0(H),
a_sec in H^0(A).
```

The four terms are

```text
K^-3 = O(-2D),

K^-2 = O(A-2D)
        direct_sum O(H-2D)
        direct_sum O(-D),

K^-1 = O(H+A-2D)
        direct_sum O(A-D)
        direct_sum O(H-D),

K^0  = O(H+A-D).                                      (5.1)
```

The first two summands of `K^-2`, every summand of `K^-1`, and `K^0` have RM index `2`. The summands `O(-2D)` and `O(-D)` have index `4`.

Hence the only contribution to total hypercohomological degree zero is the kernel of the index-two row

```text
mu_M:
H^2(A-2D) direct_sum H^2(H-2D)
 ->
H^2(H+A-2D) direct_sum H^2(A-D) direct_sum H^2(H-D). (5.2)
```

With the standard Koszul signs,

```text
mu_M(x,y)
 = (-h cup x - a_sec cup y,
     t cup x,
     t cup y).                                        (5.3)
```

There is no incoming index-two term and no higher differential can enter or leave the bidegree contributing to `H^0(C,M|_C)`. Therefore

```text
boxed:
H^0(C,M|_C) ~= ker(mu_M).                             (5.4)
```

This is the exact fixed-scale `n=1` matrix which gates the genuinely derived second residue.

## 6. Exact dimensions

For an RM class

```text
P=xD+yH+zA
```

use

```text
Nm(P)
 = x^2 + x y tau + x z (tau^2-2)
   + y^2 + y z tau + z^2,
```

and `h^2(P)=Nm(P)^2` for the index-two classes above.

The source dimensions of (5.2) are

```text
h^2(A-2D) = (2 tau^2-9)^2,
h^2(H-2D) = (2 tau-5)^2.                             (6.1)
```

The target dimensions are

```text
h^2(H+A-2D) = (tau-2)^2 (2 tau+5)^2,
h^2(A-D)    = (tau^2-4)^2,
h^2(H-D)    = (tau-2)^2.                             (6.2)
```

Thus

```text
dim(target)-dim(source)
 = tau^4 + 4 tau^3 - 14 tau^2 - 4 tau + 14.          (6.3)
```

This is positive for every `tau>=3`. Consequently maximal rank for `mu_M` means **injective**, and then (4.7) closes the co-supported escape.

Dimension counts alone do not prove injectivity.

## 7. Source arithmetic strengthens tau >= 3

For the source case of Example 11.2.7, `hat_eta(f)=g^*` with `g` an automorphism of `X`, `Nm_F/Q(f)=1`, and `f^2 != 1`.

Because `g^*` preserves the integral first-homology lattice, every eigenvalue of `g^*`, in particular each real embedding of `f`, is an algebraic integer. Hence `f` is an algebraic integer. Norm one makes it a unit, so

```text
s := Tr_F/Q(f) in Z.
```

Since `F` is real quadratic and `f != +/-1`, the polynomial

```text
T^2-sT+1
```

has two distinct real roots and therefore `|s|>=3`.

The campaign parameter is

```text
tau = Tr_F/Q(f^4)
    = s^4 - 4 s^2 + 2.                               (7.1)
```

Therefore the actual automorphism source satisfies

```text
boxed: tau >= 47}.                                    (7.2)
```

This strengthens all previous numerical inequalities, but it still does not determine the rank of (5.3).

## 8. Relation to L052

`L052` correctly identifies the two local residue line bundles

```text
2D-H,
2D-A
```

and their single-row `H^2` Koszul complexes. What it does **not** by itself prove is that arbitrary classes in those two curve-level residue spaces lift to global `Ext^1(B,C_corr)`.

The Postnikov calculation above supplies the missing filter:

```text
second generic local residue
 -> localizable part of Ext^2(B,E^vee)
 -> H^0(C,M|_C)
 = ker(mu_M).                                        (8.1)
```

Thus the first fixed-scale rank test should be `mu_M`, not the two residue rows independently.

If `mu_M` is injective, the lane is closed immediately. If `ker(mu_M)` is nonzero, one must then evaluate the Postnikov connecting map and the map to `Ext^2(B,E)` before claiming rank two.

## 9. Fixed-scale literature boundary

Grieve's fixed-scale theory identifies such cup products with fiberwise evaluations of vector bundles and gives useful nonvanishing criteria after translation. It does not give a general fixed-`n=1` maximal-rank theorem. His examples explicitly show that fixed-scale cup products satisfying the pair-index condition can vanish on a positive-dimensional locus.

Therefore the positivity of the dimension gap in (6.3) is not evidence that (5.3) is injective for the chosen theta sections.

The exact remaining datum is now smaller than `L051`/`L052`:

```text
rank(mu_M) for the chosen theta sections t,h,a_sec.  (9.1)
```

A proof that `mu_M` is injective closes the co-supported escape. A nonzero kernel only keeps the lane alive provisionally and triggers the Postnikov-transgression calculation.

## 10. Claim boundary

```text
HC-R021-L053 = proved_in_solve_package_not_certified
corrected_cone_cohomology_sheaves = F_in_degree_0__G_in_degree_1
second_localizable_residue_gate = H0_C(H_plus_A_minus_D)
H0_C(H_plus_A_minus_D) = kernel_of_mu_M
mu_M_source_dimension = (2tau^2-9)^2 + (2tau-5)^2
mu_M_target_minus_source = tau^4+4tau^3-14tau^2-4tau+14 > 0
source_automorphism_case_tau_lower_bound = 47
mu_M_rank = open
postnikov_survival_if_kernel_nonzero = open
global_Ext1_residue_rank = open
cosupported_global_extension = open
second_factor_rank20 = open
all_orders_transport = open
HC-R021-P4 = open
restricted_target_proved = false
full_hodge_conjecture_proved = false
```

This is a Solve-package result and not a MATHCERT disposition.

## 11. Inputs

- `HC-R021-L049`: explicit two-channel local co-supported repair;
- `HC-R021-L050`: global hyper-Ext reduction;
- `HC-R021-L052`: residue sheaf and the two residue-line `H^2` Koszul rows;
- Eyal Markman, arXiv:2509.23079v1, Corollary 11.2.6, Example 11.2.7, Lemma 11.2.8;
- Nathan Grieve, *Index conditions and cup-product maps on abelian varieties*, arXiv:1308.1970v3, especially Proposition 5.2, Corollary 5.3, and Sections 7.1-7.2;
- standard duality for regular embeddings, Koszul resolutions, and local-to-global Ext spectral sequences.
