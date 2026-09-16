# HC-R021-P4 — The genus-four Schottky defect survives the union and partial-normalization secant constructions

**Campaign:** `HC-001`  
**Restricted target:** `HC-R021-A8-CM4-C2`  
**Parent development revision:** `ba074bfc92d892f8050fc3f814349bdf614b3675`  
**State:** `GENUS4_FULL_SUPPORT_SECANT_OBJECTS_HAVE_AT_LEAST_ONE_EXTRA_COMMUTATIVE_OBSTRUCTION__POINT_NORMALIZATION_CANNOT_CANCEL`  
**Date:** 2026-09-16

## 1. Purpose

Decide the finite `PN-SCHOTTKY-A1` question left by `L041`.

The answer is negative for a structural reason. The one-dimensional Schottky obstruction of a `W_2` component remains nonzero after deleting finitely many points, whereas every difference between Markman's coherent union ideal and the partial-normalization object is supported at those finite intersection points.

Consequently neither the point components of the coherent construction nor the conductor quotient of the partial normalization can cancel the Schottky obstruction.

This proves that the genus-four full-support secant objects have strictly larger object obstruction rank than their Chern-character contraction rank.

## 2. Setup

Use Markman Example 8.2.3 in dimension four with `a_3=1`.

For a positive secant parameter `d`, the coherent object is

```text
F_d=I_Z(Theta),
```

where `Z` contains

```text
d+1
```

generic translates

```text
S_i=tau_(t_i)(W_2),
0<=i<=d,
```

and a zero-dimensional correction. The distinct `S_i` meet only in finite sets of points.

The alternative object is

```text
F'_d=[O_X -> nu_*O_(Ztilde)](Theta),        (2.1)
```

where `nu` partially normalizes four of the six points in each pairwise intersection. Markman proves

```text
ch(F'_d)=ch(F_d).                           (2.2)
```

Let `P` be the union of:

- all pairwise intersection points of the `S_i`;
- the zero-dimensional correction points in the coherent presentation;
- all points at which `nu` differs from the identity.

Set

```text
U:=X\P.
```

Then the surfaces

```text
S_i^o:=S_i\P
```

are pairwise disjoint in `U`, and both constructions restrict there to the same ordinary rank-one ideal geometry:

```text
F_d|_U ~= I_(union S_i^o/U)(Theta),
F'_d|_U ~= I_(union S_i^o/U)(Theta).        (2.3)
```

## 3. The W2 Schottky obstruction survives puncturing

Fix one component

```text
S=W_2(C)
```

and let

```text
N:=N_(S/X).
```

`L041` identifies a polarization-preserving commutative first-order deformation

```text
xi_Sch
```

normal to the genus-four Jacobian locus, with nonzero embedded/object obstruction

```text
o_Sch in H^1(S,N) subset gr Ext^2_X(I_S,I_S).   (3.1)
```

Let

```text
P_S:=P cap S,
S^o:=S\P_S.
```

Since `S` is a smooth surface and `N` is locally free, the depth of `N` at every closed point is two. Therefore local cohomology with support in the finite set satisfies

```text
H^0_(P_S)(S,N)=0,
H^1_(P_S)(S,N)=0.                           (3.2)
```

The localization exact sequence then gives an injection

```text
H^1(S,N) -> H^1(S^o,N|_(S^o)).             (3.3)
```

Hence

```text
o_Sch|_(S^o) !=0.                           (3.4)
```

Thus deleting finitely many points cannot make the Schottky obstruction disappear.

## 4. Coherent union ideal

Restrict the object obstruction of `F_d` to `U` and then to a neighborhood of `S_i^o`. By locality of the characteristic obstruction and (2.3), its normal-bundle associated-graded component is exactly the punctured obstruction (3.4) for that translated `W_2` component.

Therefore

```text
ob_(F_d)(xi_Sch,i) !=0                      (4.1)
```

for the corresponding Schottky-normal ppav direction of the translated polarization geometry.

In particular the point corrections in the coherent support cannot cancel the obstruction, because they vanish after restriction to `U` while (3.4) does not.

## 5. Partial-normalization object

Exactly the same restriction argument applies to `F'_d`.

The truncation triangle from `L041`

```text
I_Z -> F'_d(-Theta) -> Q[-1] -> I_Z[1]     (5.1)
```

has finite-length `Q` supported inside `P`. Hence

```text
Q|_U=0,
F'_d|_U ~= I_Z|_U(Theta).                   (5.2)
```

If

```text
ob_(F'_d)(xi_Sch,i)=0,
```

then its restriction to `U` would vanish. Equation (5.2) would then force the restriction of the union-ideal obstruction to vanish, contradicting (3.4).

Thus

```text
boxed[ ob_(F'_d)(xi_Sch,i) !=0 ].           (5.3)
```

This proves `PN-SCHOTTKY-A1`: the conductor extension at the normalization points cannot cancel the global Schottky-normal obstruction.

Equivalently, any Yoneda boundary produced solely through

```text
Ext^2(Q,I_Z) x Hom(I_Z,Q)
```

is invisible after restriction to `U`; it therefore cannot equal the Schottky class, whose restriction is nonzero.

## 6. Contraction rank of the genus-four secant class

For `a_3=1`, Markman's Chern character is

```text
w_d
 = 1+Theta-(d/2)Theta^2-(d/6)Theta^3+d^2[pt].   (6.1)
```

The Hochschild degree-two space decomposes as

```text
HT^2(X)
 = H^2(O_X)
   direct_sum H^1(T_X)
   direct_sum H^0(Lambda^2 T_X),            (6.2)
```

with dimensions `6+16+6=28`.

For the commutative summand, contraction with `w_d` vanishes precisely when the infinitesimal complex-structure deformation preserves `Theta`. This kernel has dimension ten, so the commutative contribution has rank six.

For the gerby-plus-Poisson summands, the lowest-degree equation is

```text
alpha-(d/2)(pi contraction Theta^2)=0,      (6.3)
```

which determines the gerby class `alpha` uniquely from the bivector `pi`. The higher-degree equations follow from the standard contraction identity

```text
pi contraction Theta^m
 = binom(m,2)(pi contraction Theta^2) Theta^(m-2)/1
```

with the normalizations in (6.1). Hence this sector has a six-dimensional kernel inside a twelve-dimensional domain and therefore rank six.

Consequently

```text
rank(c_(w_d))=12,
dim ker(c_(w_d))=16.                        (6.4)
```

The same rank holds for the derived-dual class because duality only changes the signs of the odd Chern-character components.

## 7. HC-R021-L042 — strict genus-four secant defect

### Statement

For every positive integer `d` in Markman's genus-four Example 8.2.3:

1. the coherent secant ideal `F_d=I_Z(Theta)` has a nonzero Schottky-normal object obstruction which lies in the Chern-character contraction kernel;
2. the partial-normalization object `F'_d` with the same Chern character has the same unavoidable Schottky-normal obstruction after restriction away from its finite conductor set;
3. the contraction rank of their common Chern character is `12`.

Therefore

```text
rank(ob_(F_d)) >=13,
rank(ob_(F'_d))>=13.                        (7.1)
```

Neither genus-four full-support secant construction is rank-minimal.

### Proof

Sections 3-6.

QED.

## 8. Consequence for the pure-odd target construction L040

`L040` remains valid: derived-dual extraction provides explicit perfect objects on the pure odd secant rays and an explicit `T_split` on `2 beta'`.

However, choosing the genus-four `F_d` or `F'_d` as the underlying full-support secant object does not individually produce a rank-minimal sector. Each carries at least one extra commutative obstruction invisible to its secant Chern character.

Duality does not remove this defect: an object deforms in a given ambient direction if and only if its derived dual does. Thus the split dual pair

```text
E_d direct_sum E_d^vee[1]
```

inherits the same Schottky defect.

A rank-20 target object built from `L040` must therefore use **non-split cross-sector cancellation** of these extra commutative defects.

## 9. Exact surviving question

The target contraction kernel is

```text
K_beta=span(k_1,...,k_8).
```

The Schottky argument proves an extra obstruction somewhere in the ten-dimensional ppav tangent kernel of each individual polarization sector. It does **not yet determine whether that normal line intersects the six-dimensional simultaneous `(D,H)`-preserving subspace `span(k_1,...,k_6)`**.

This is now the decisive incidence problem:

```text
RM-SCHOTTKY-A1:
  determine
  T_(D,H) RM  intersect  T_Jacobian
  inside the ten-dimensional ppav tangent space.
```

If the six-dimensional simultaneous RM tangent is not contained in the Jacobian tangent hyperplane, then at least one of `k_1,...,k_6` is obstructed on every standard genus-four secant block, and the split target object of `L040` has obstruction rank strictly greater than `20`.

If it is contained, the Schottky defect lies outside the target kernel and does not by itself prevent rank `20`.

## 10. Current disposition

```text
HC-R021-L042 = proved_in_solve_package_not_certified
coherent_genus4_secant_contraction_rank = 12
partial_normalization_genus4_secant_contraction_rank = 12
coherent_genus4_secant_obstruction_rank_lower_bound = 13
partial_normalization_genus4_secant_obstruction_rank_lower_bound = 13
PN-SCHOTTKY-A1 = negative_point_corrections_cannot_cancel
L040_explicit_target_object = remains_valid
RM-SCHOTTKY-A1 = next_finite_incidence_problem
second_factor_rank20_exists = open
all_orders_transport = open
HC-R021-P4 = open
restricted_target_proved = false
full_hodge_conjecture_proved = false
```

## 11. Sources and inputs

- `HC-R021-L039-L041`;
- Eyal Markman, arXiv:2502.03415v2, Example 8.2.3, especially equations (8.2.2), (8.2.6), and the genus-four Chern-character computation;
- Luigi Lombardi and Sofia Tirabassi, arXiv:1410.7986, Theorem 1.1, Theorem 1.4, Corollary 1.5;
- local cohomology/depth for a locally free sheaf on a smooth surface punctured at finitely many points;
- locality of the characteristic obstruction under restriction.
