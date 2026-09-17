# HC-R021-P4 — Co-supported extension repair of the theta-square local mixed obstruction

**Campaign:** `HC-001`  
**Restricted target:** `HC-R021-A8-CM4-C2`  
**Parent development revision:** `1c43cdf49b26ebef984c9dcb5564ba683f1c7469`  
**State:** `TRANSVERSE_SUPPORT_EXTENSIONS_PRUNED__TWO_COSUPPORTED_CHANNELS_KILL_LOCAL_BIVECTOR_CLASS`  
**Date:** 2026-09-16

## 1. Purpose

Continue the extension escape left open by `HC-R021-L048`.

There are two distinct cases.

1. If the auxiliary `L047` theta blocks have supports which are transverse to a chosen correction curve, arbitrary iterated extensions are locally invisible at a general point of that curve and cannot repair the `L048` obstruction.
2. If two ordinary double-theta blocks are deliberately placed on the same theta divisor as a corrected block, there is an explicit local two-channel extension whose full pure-bivector characteristic class is nullhomotopic.

Thus `L048` closes the generic/transverse extension repair but not the co-supported one. The remaining issue is globalizing the two local extension channels with the required line-bundle twists.

## 2. Transverse-support extensions cannot help

Let `C_j` be a corrected `L047` block with support divisor `Delta_j` and correction curve `C subset Delta_j`. Let the other blocks have theta supports `Delta_i` such that `C` is not contained in any `Delta_i`, `i != j`.

At a general point

```text
x in C minus union_(i!=j) Delta_i
```

every other theta-square block is acyclic in a neighbourhood of `x`: its theta equation is invertible, hence its defining dual map is an isomorphism.

Therefore any finite filtered object whose associated graded consists of the `L047` blocks restricts near `x` to the single corrected block `C_j`. Extension classes involving the other blocks restrict to zero because one endpoint is zero in the local derived category.

Consequently the local characteristic class is exactly that of `C_j`, and `L048a` applies unchanged.

### HC-R021-L049a — locality no-go

Any iterated extension of `L047` blocks for which a correction curve is not contained in the other block supports still fails simultaneous mixed vanishing on that curve.

Hence a successful extension repair must be deliberately co-supported.

## 3. Corrected local cone in minimal form

Retain the local notation of `L048`:

```text
R regular local,
I=(t,u,v),
C = Cone(I^vee -> I),
```

where the map is the theta square `t^2`.

After cancelling the unique unit pair in the free cone model of `L048`, `C` has the minimal free model

```text
C^-2 = R,
C^-1 = R^5,
C^0  = R^5,
C^1  = R,
```

with

```text
d^-2 = (v,-u,t,0,0)^T,                              (3.1)
```

```text
d^-1 =
[  t     0    -v   0   0 ]
[  0     t     u   0   0 ]
[ -u^2  -uv    0   t   0 ]
[ -uv   -v^2   0   0   t ]
[  0     0     0  -v   u ],                         (3.2)
```

and

```text
d^0 = (0,0,-v,u,-t).                                 (3.3)
```

## 4. Full local bivector class of the corrected cone

For a constant bivector `pi`, write

```text
alpha = pi(dt,du),
beta  = pi(dt,dv),
gamma = pi(du,dv).                                   (4.1)
```

The Atiyah-square/HKR calculation on (3.1)-(3.3) gives

```text
chi_pi^-2
 = (2 beta,-2 alpha,-3 gamma u,-3 gamma v,0)^T,      (4.2)

chi_pi^-1
 = (-3 gamma u,-3 gamma v,0,2 beta,-2 alpha).        (4.3)
```

The `gamma` part is already nullhomotopic on the corrected cone. One explicit degree-one homotopy has only the two nonzero entries

```text
H_(3,2)=3,
H_(4,1)=-3                                             (4.4)
```

in the middle `R^5 -> R^5` component, using one-based indexing. Thus the local Ext class is entirely controlled by the two residue directions `alpha,beta`, as anticipated by `L048`.

## 5. Two ordinary co-supported theta blocks

Let

```text
B = [ R --t^2--> R ]
```

in degrees `-1,0`. This is the local model of the ordinary double-`D` block

```text
O_(2D)(D).
```

Take two copies `B_1,B_2` and define degree-one extension cocycles `e_1,e_2:B_i -> C[1]` by

```text
x_1=(1,0,0,0,t)^T,   y_1=1,
x_2=(0,1,0,0,t)^T,   y_2=1,                         (5.1)
```

where `x_i:B_i^-1 -> C^0` and `y_i:B_i^0 -> C^1`.

The cocycle condition is

```text
d^0 x_i + y_i t^2=0,
```

which holds because the final entry of each `x_i` is `t`.

Let `G` be the two-step extension with associated graded

```text
C direct_sum B_1 direct_sum B_2
```

and extension class `(e_1,e_2)`.

As a free complex,

```text
G^-2 = R,
G^-1 = R^5 direct_sum R^2,
G^0  = R^5 direct_sum R^2,
G^1  = R,
```

with

```text
d_G^-2 = (d_C^-2,0,0)^T,                            (5.2)
```

```text
d_G^-1 =
[ d_C^-1  x_1  x_2 ]
[    0     t^2   0  ]
[    0      0   t^2 ],                               (5.3)
```

and

```text
d_G^0 = (d_C^0,1,1).                                 (5.4)
```

Direct multiplication gives `d_G^2=0`.

## 6. HC-R021-L049b — exact local nullhomotopy

### Statement

For every constant bivector `pi` in the local coordinates `t,u,v,w`, the pure-bivector characteristic class of `G` vanishes in

```text
Ext_R^2(G,G).
```

### Proof

The differential is independent of `w`, so bivector components containing `partial_w` contribute zero. It is enough to treat the basis coefficients `alpha,beta,gamma` in (4.1).

The Atiyah-square calculation on (5.2)-(5.4) gives the same two displayed components as (4.2)-(4.3), embedded in the first five coordinates, with zero entries on the two auxiliary block coordinates.

It suffices to give degree-one homotopies for the three basis bivectors. Write a homotopy as

```text
p:G^-2 -> G^-1,
H:G^-1 -> G^0,
q:G^0 -> G^1,
```

so that

```text
chi^-2 = d_G^-1 p + H d_G^-2,
chi^-1 = d_G^0 H + q d_G^-1.                         (6.1)
```

All unspecified entries below are zero, and indices are one-based.

### `alpha=1`, `beta=gamma=0`

Take

```text
p_7=-2,
H_(5,3)=2,
H_(6,5)=-2,
H_(7,3)=2t,
q=0.                                                 (6.2)
```

Substitution into (6.1) gives exactly the `alpha` characteristic map.

### `beta=1`, `alpha=gamma=0`

Take

```text
p_6=2,
H_(5,3)=-2,
H_(6,3)=-2t,
H_(6,4)=2,
q=0.                                                 (6.3)
```

Substitution gives exactly the `beta` characteristic map.

### `gamma=1`, `alpha=beta=0`

Take

```text
H_(3,2)=3,
H_(4,1)=-3,
p=q=0.                                              (6.4)
```

This is the homotopy already present on the corrected cone.

By linearity, every constant bivector is nullhomotopic.

QED.

## 7. Interpretation

The two auxiliary ordinary blocks do exactly what the residue calculation suggests.

Modulo the maximal ideal, the two extension columns in (5.3) map the two auxiliary degree-`-1` generators onto the two corrected degree-zero coordinates carrying the `beta` and `alpha` residues. The constants in (5.4) simultaneously remove the terminal degree-one residue. Thus the two-dimensional local obstruction surviving `L048` becomes a boundary.

This is not merely the necessary factorization condition of `L021`: the explicit homotopies (6.2)-(6.4) prove actual local vanishing of the full pure-bivector characteristic class.

## 8. Globalization data

The local repair uses co-supported ordinary `D` blocks. Globally, near a correction curve

```text
C = D intersect H intersect A,
```

the corrected object is built from

```text
E=I_C(D).
```

Its twisted Koszul resolution has terms

```text
P^-2 = O(-H-A),
P^-1 = O(-H) direct_sum O(-A) direct_sum O(D-H-A),
P^0  = O direct_sum O(D-H) direct_sum O(D-A).        (8.1)
```

After the theta-square unit cancellation, the two local residue coordinates used by `e_1,e_2` globalize with numerical line classes

```text
2D-H,
2D-A,                                                (8.2)
```

while the terminal extension component has class

```text
M := H+A-D.                                          (8.3)
```

In the RM normal form

```text
D=(1,1),
H=(a,b),
A=(a^2,b^2),
ab=1,
a+b=tau,
0<a<1<b,
tau>=3,
```

these classes have weights

```text
2D-H = (2-a,2-b),
2D-A = (2-a^2,2-b^2),
M    = (a+a^2-1,b+b^2-1).                            (8.4)
```

For `tau>=3`, each has one positive and one negative RM block, hence ambient cohomological index `2`; in particular none has an ambient `H^0` section. Therefore the local repair does **not** globalize as a naive global chain map between the displayed line-bundle resolutions.

This does not yet prove that the required global `Ext^1` classes are absent: a hyper-Ext class can be represented by local degree-one maps patched by lower-degree Cech data, and its residue along the correction curve is the relevant invariant.

## 9. Exact next global question

The extension problem has now been reduced to a precise restriction/local-to-global map.

For the ordinary double-`D` block

```text
B_D=O_(2D)(D)
```

and one corrected theta-square block `C_corr`, determine the image of

```text
Ext_X^1(B_D,C_corr)
 -> Ext_R^1(B,C)                                     (9.1)
```

at the generic point of a correction curve, and dually for

```text
Ext_X^1(C_corr,B_D).
```

A successful global repair requires two classes whose generic residues span the two local coordinates used in (5.1), together with opposite classes realizing the homotopies for both mixed RM directions.

If the image of (9.1) has rank less than two on the correction curve, the co-supported escape closes. If it has rank two, the next step is to assemble the global two-channel extension and compute its gerby/ordinary-direction actions.

## 10. Claim boundary

```text
HC-R021-L049a = proved_in_solve_package_not_certified
transverse_support_extension_escape = false
HC-R021-L049b = proved_in_solve_package_not_certified
two_cosupported_double_D_blocks_kill_local_pure_bivector_obstruction = true
naive_global_line_bundle_chain_map = blocked_by_index2_classes
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

- `HC-R021-L021`: extension factorization framework;
- `HC-R021-L022`: complementary RM characteristic-plane geometry;
- `HC-R021-L047`: direct beta-prime theta-square construction;
- `HC-R021-L048`: local corrected-cone mixed obstruction;
- standard Koszul resolutions and the Atiyah-square representative for the HKR characteristic action on a free complex.
