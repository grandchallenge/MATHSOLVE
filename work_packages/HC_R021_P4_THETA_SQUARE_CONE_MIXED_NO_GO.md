# HC-R021-P4 — Mixed-direction no-go for the direct beta-prime theta-square cone

**Campaign:** `HC-001`  
**Restricted target:** `HC-R021-A8-CM4-C2`  
**Parent development revision:** `5f06ea8d24669f65445d867f3f559bbcca8c3051`  
**State:** `L047_DIRECT_SUM_CONE_NOT_RANK20__LOCAL_TANGENCY_OBSTRUCTION_SURVIVES`  
**Date:** 2026-09-16

## 1. Purpose

Test the two mixed real-multiplication Hochschild directions `k_7,k_8` on the explicit non-split target-ray perfect complex `C_beta'` of `HC-R021-L047`.

The theta-square cone does remove part of the raw codimension-three Koszul obstruction, but it does not remove the characteristic tangency requirement along the complete-intersection correction curves. Consequently the direct-sum object `C_beta'` cannot annihilate both mixed directions and therefore cannot have obstruction rank `20`.

This package prunes the specific `L047` direct-sum construction. It does not rule out further cross-block extensions or other perfect complexes with the same Chern character.

## 2. Local model at a correction curve

Fix one block `C_j` of `L047` and one irreducible correction curve `C` in that block. At a general point of `C`, away from the transported Abel-Jacobi surface and all other correction curves, choose regular local parameters

```text
t,u,v,w
```

such that

```text
Delta_j = (t=0),
C = (t,u,v)=0.
```

Locally the block ideal is

```text
I=(t,u,v) subset R,
```

where `R` is the regular local ring of the fourfold at the chosen point. The theta-square morphism is induced by the tensor square of the section `t`:

```text
e:I^vee -> I.
```

Let

```text
s:R -> I,
1 |-> t.
```

Then in the derived category

```text
e = s o s^vee.                                      (2.1)
```

Set

```text
Q := I/(t) = (u,v) subset R/(t).
```

The octahedral axiom applied to `I^vee -> R -> I` gives the intrinsic triangle

```text
Q^vee[1] -> Cone(e) -> Q -> Q^vee[2].               (2.2)
```

Thus the derived correction is a hyperbolic/self-dual completion of the ordinary surface ideal `Q`. In particular, `L022` cannot simply be imported as a statement about a torsion-free sheaf; the characteristic action must be computed on the cone itself.

## 3. Free model of the cone

Use the truncated Koszul resolution of `I`. Put

```text
A = (v,-u,t)^T,

B = [ -u  -v   0
       t   0  -v
       0   t   u ].
```

Then

```text
0 -> R --A--> R^3 --B--> R^3 -> I -> 0             (3.1)
```

is exact, with augmentation `(t,u,v)`.

Lift `s` by the first basis vector of the terminal `R^3`. The composite `s o s^vee` is then represented on the free resolutions by

```text
E = diag(1,0,0).                                     (3.2)
```

With the standard cone convention, `F=Cone(e)` is represented by

```text
F^-2 = R,
F^-1 = R^3 direct_sum R^3,
F^0  = R^3 direct_sum R^3,
F^1  = R,
```

and differentials

```text
d^-2 = [ A ]
       [ 0 ],

d^-1 = [ B   E  ]
        [ 0  B^T ],

d^0  = [ 0  -A^T ].                                 (3.3)
```

Direct multiplication gives `d^-1 d^-2=0` and `d^0 d^-1=0`.

The entry `E_11=1` is the unique unit in the differential at the chosen generic point. Cancelling that contractible source-target pair produces a minimal free complex over the local ring; every remaining differential entry lies in the maximal ideal.

## 4. Bivector characteristic action

Let `pi` be a locally constant bivector. Write

```text
alpha := pi(dt,du),
beta  := pi(dt,dv),
gamma := pi(du,dv).                                  (4.1)
```

For a free complex with the trivial connection, the Atiyah class is represented by the exterior differential of the differential matrix. Hence, up to the universal nonzero normalization/sign convention in the HKR characteristic morphism, the pure bivector component is represented by

```text
chi_pi^n
 = sum_(i<j) pi^(ij)
   (partial_i d^(n+1) partial_j d^n
    - partial_j d^(n+1) partial_i d^n).              (4.2)
```

Substitution into (3.3) gives the only two possibly nonzero degree-two components

```text
chi_pi^-2
 = (-2 gamma, 2 beta, -2 alpha, 0,0,0)^T,           (4.3)

chi_pi^-1
 = (0,0,0,-2 gamma,2 beta,-2 alpha).                (4.4)
```

Only the vanishing pattern matters, so the overall factor and sign are immaterial.

## 5. HC-R021-L048a — local tangency necessity

### Statement

If the local characteristic class of `pi` on the theta-square cone vanishes in

```text
Ext_R^2(F,F),
```

then

```text
pi(dt,du)=0,
pi(dt,dv)=0.                                         (5.1)
```

Equivalently,

```text
pi^sharp(dt) in T_C.                                 (5.2)
```

### Proof

Cancel the unique unit pair `E_11=1` in (3.3). The resulting free complex is minimal, so after tensoring with the residue field all differentials are zero.

The cancelled source is the first basis vector of the dual `R^3` in degree `-1`; the cancelled target is the first basis vector of the primal `R^3` in degree `0`. Therefore the `gamma` entries in (4.3)-(4.4) lie on the cancelled coordinates. The `beta` and `alpha` entries lie on uncancelled coordinates.

Elementary elimination changes the uncancelled coordinates only by terms in the maximal ideal. Hence, modulo the maximal ideal, the degree-two endomorphism of the minimal complex still contains the residues

```text
(2 beta,-2 alpha)
```

in both surviving components.

A nullhomotopic degree-two endomorphism of a minimal complex reduces to zero over the residue field, because the reduced differential is zero. Therefore vanishing of the Ext class forces

```text
alpha=beta=0.
```

Since `T_C` is defined by `dt=du=dv=0` and `dt(pi^sharp(dt))=0` automatically, these two equalities are exactly

```text
pi^sharp(dt) in T_C.
```

QED.

### Scope

The lemma is one-way. It does not claim that the remaining `gamma` contribution is always nullhomotopic. The necessary tangency condition is sufficient for the no-go below.

## 6. Apply the two RM mixed directions

From `HC-R021-L006`, the two mixed kernel directions are, up to nonzero scalar normalization,

```text
k_7 = pi_1 + q a (y_1 wedge y_2),
pi_1 = t_1 wedge t_2,

k_8 = pi_2 + q b (y_3 wedge y_4),
pi_2 = t_3 wedge t_4,
```

with complementary real-multiplication planes

```text
V_1=span(t_1,t_2),
V_2=span(t_3,t_4),
V_1 intersect V_2=0.                                 (6.1)
```

On a sufficiently small affine/formal neighbourhood of the chosen point, the `H^2(O_X)` gerby components are locally trivial. Therefore, if the global obstruction of `k_i` vanished on the block, the local pure-bivector obstruction of `pi_i` would vanish.

By `L048a`,

```text
ob(k_7)=0 => pi_1^sharp(dt) in T_C,
ob(k_8)=0 => pi_2^sharp(dt) in T_C.                  (6.2)
```

These are exactly the two characteristic tangency conditions that appeared for the coherent elementary transform in `L022`, now derived directly from the perfect cone.

## 7. Complementary-plane contradiction

Choose the `D-H-A` complete-intersection correction curves of `L047` generally so that each irreducible curve generates `X` as an abelian variety, as in `L022`. This is compatible with the general complete-intersection choices already required in `L047`.

Suppose both mixed obstructions vanished on a block containing such a curve. At a general point set

```text
v_1=pi_1^sharp(dt) in V_1,
v_2=pi_2^sharp(dt) in V_2.
```

By (6.2), both lie in the one-dimensional tangent line `T_C`. Since `V_1 intersect V_2=0`, they cannot both be nonzero at the same point.

The zero loci of `v_1|_C` and `v_2|_C` are closed. Irreducibility of `C` therefore forces one characteristic vector to vanish identically on a dense open set and hence along `C`; say `v_1=0`. Then

```text
V_1 subset T_D
```

along `C`. The other characteristic vector cannot also vanish generically, because `V_1 direct_sum V_2=T_X` while `T_D` is a hyperplane. Thus `v_2` is generically nonzero and

```text
T_C subset V_2
```

on a dense open set.

As in `L022`, a complete algebraic curve whose tangent is contained generically in one fixed two-dimensional translation-invariant subspace cannot generate the fourfold: the abelian subvariety generated by `C-C` has tangent contained in that subspace and has dimension at most two. This contradicts the chosen generating correction curve.

The case `v_2=0` is symmetric.

Therefore a correction block cannot annihilate both `k_7` and `k_8`.

## 8. HC-R021-L048 — direct beta-prime cone is not rank 20

### Statement

Let `C_beta'` be the direct-sum perfect complex constructed in `L047`, with positive source parameter `q=p/s`. Since `p>0`, at least one block contains a correction curve. Choose the curves generally so that they generate `X`.

Then

```text
{k_7,k_8} is not a subset of ker(ob_(C_beta')).      (8.1)
```

Consequently

```text
ker(ob_(C_beta'))
 proper-subset ker(c_beta'),
```

and therefore

```text
rank(ob_(C_beta')) > 20.                             (8.2)
```

Hence the explicit direct-sum theta-square object of `L047` is not a rank-20 second factor.

### Proof

At least one summand has `r_j>0`. If both global mixed obstructions vanished on the direct sum, their projections to the diagonal `Ext^2(C_j,C_j)` component of every summand would vanish. Section 7 rules this out for any summand containing a generating correction curve.

Thus at least one of the eight basis vectors spanning `ker(c_beta')` is absent from `ker(ob_(C_beta'))`. Since semiregularity compatibility gives

```text
ker(ob_(C_beta')) subset ker(c_beta')
```

and `dim ker(c_beta')=8`, the inclusion is strict and the obstruction rank is strictly larger than `20`.

QED.

## 9. What the local calculation teaches

The theta-square dual cone is not equivalent to the ordinary divisor elementary transform. The codimension-three Koszul calculation shows precisely what the derived self-dual completion changes:

- the component detected by `gamma=pi(du,dv)` lies on the contractible cone pair at residue level and is not needed for the no-go;
- the two components involving the divisor conormal,
  `pi(dt,du)` and `pi(dt,dv)`, survive minimization;
- therefore the characteristic vector of the support divisor must still be tangent to the correction curve whenever the mixed obstruction vanishes.

So internal non-splitting and hyperbolic dual completion are not enough. Any successful correction geometry must avoid a generating curve on which both complementary RM characteristic directions impose incompatible tangency.

## 10. Surviving route after L048

`L048` prunes the direct sum `C_beta'` itself. It does not yet prune a genuinely coupled multi-block object.

The narrow remaining possibility suggested by the calculation is:

1. retain the exact target-ray K-class of `L047`;
2. replace the direct sum by cross-block extensions whose degree-one differentials couple the correction blocks;
3. require the resulting local minimal complex to make the surviving `alpha,beta` residue classes into boundaries;
4. check the extension-factorization constraints before any global construction.

This is the derived analogue of the `L021` necessary-factorization test. The next exact task is therefore to determine whether off-diagonal `Ext^1(C_i,C_j)` can alter the residue-level mixed obstruction at a correction curve. If locality/support forces the diagonal residue classes to survive every such extension, the entire `L047` K-class realization lane closes.

## 11. Claim boundary

```text
HC-R021-L048 = proved_in_solve_package_not_certified
L047_direct_sum_rank20 = false
L047_both_mixed_directions = impossible_for_general_generating_corrections
local_theta_square_cone_tangency_necessity = proved
cross_block_extension_escape = open
negative_Ext_for_L047 = no_longer_decisive_for_direct_sum
second_factor_rank20 = open
all_orders_transport = open
HC-R021-P4 = open
restricted_target_proved = false
full_hodge_conjecture_proved = false
```

This is a Solve-package result and not a MATHCERT disposition.

## 12. Inputs

- `HC-R021-L006`: exact eight-dimensional contraction kernel and the two complementary mixed RM directions;
- `HC-R021-L022`: characteristic-plane geometry and generating-curve contradiction for the coherent elementary transform;
- `HC-R021-L047`: direct target-ray theta-square cone construction;
- standard Atiyah-class representative for a free complex with trivial connection, and the HKR bivector characteristic action obtained by contracting the square of that Atiyah class.
