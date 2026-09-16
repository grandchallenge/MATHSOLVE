# HC-R021-P4 — Three-divisor two-term complex has unavoidable rank 22

**Campaign:** `HC-001`  
**Restricted target:** `HC-R021-A8-CM4-C2`  
**Parent development revision:** `9656185afab9f2d21e5b84b54267632582c87e67`  
**State:** `THREE_DIVISOR_TWO_TERM_FAMILY_RANK_22__INDEX2_BRIDGE_REQUIRED`  
**Date:** 2026-09-16

## 1. Purpose

Decide the three-divisor non-split candidate left open after `HC-R021-L024`.

The candidate starts from the exact Chern-character identity

```text
A ch(B_D) + q ch(B_H) - ch(B_J)
  = 2q(tau+q) beta',
```

where

```text
J := D+qH,
A := 1+q tau+q^2,
tau := Tr_(F/Q)(f^4),
B_L := i_(2L),* O_(2L)(L),
ch(B_L)=2L+(1/3)L^3.
```

The split object is known not to solve the mixed rank problem. The unresolved question was whether a nonzero differential connecting these three divisor blocks could make the two mixed classes `k_7,k_8` into boundaries.

The answer is negative for the entire natural two-term locally free realization of this identity: **every differential has obstruction rank exactly `22`**. The reason is spectral rather than generic. The off-diagonal Hom bundles have no degree-two cohomology, so the nonzero diagonal `H^2(O_X)` components of the mixed characteristic action have nowhere to die in the hyper-Ext spectral sequence.

This does not rule out longer complexes with added `K_0`-zero bridge terms, higher-rank/semihomogeneous terms, torsion bridge objects, or other genuinely derived constructions.

## 2. RM normal form

Use the notation of `HC-R021-L006` and `L016`:

```text
D = U+V,
H = aU+bV,
ab=1,
a,b>0,
a!=b,

tau=a+b,

beta' = D-(q/6)H^3,

k_7 = t_1 wedge t_2 + q a (y_1 wedge y_2),
k_8 = t_3 wedge t_4 + q b (y_3 wedge y_4).
```

Here

```text
U=x_1 y_1+x_2 y_2,
V=x_3 y_3+x_4 y_4.
```

On the source special case `q` is a positive integer. Set

```text
J=D+qH=(1+qa)U+(1+qb)V,
A=1+q(a+b)+q^2=(1+qa)(1+qb).
```

The coefficient `A` is the norm

```text
A = Nm_(F/Q)(1+q f^4)
```

under the two real embeddings. In the integral source datum it is a positive integer, as required for the multiplicity below.

## 3. The exact three-divisor Chern identity

For the symmetric divisor block

```text
B_L := i_(2L),* O_(2L)(L),
```

the standard divisor sequence

```text
0 -> O_X(-L) -> O_X(L) -> B_L -> 0
```

gives

```text
ch(B_L)=exp(L)-exp(-L)=2L+(1/3)L^3
```

on the fourfold.

### HC-R021-L025a — Chern identity

One has

```text
A ch(B_D)+q ch(B_H)-ch(B_J)
 = 2q(tau+q) beta'.
```

### Proof

The degree-two part is immediate:

```text
2(AD+qH-J)
 = 2(A-1)D
 = 2q(tau+q)D.
```

For degree six it remains to prove

```text
A D^3 + q H^3 - J^3
 = -q^2(tau+q) H^3.
```

Equivalently, after expanding `J=D+qH` and dividing by `-q`,

```text
3D^2H + 3qDH^2
 = (tau+q)D^3 + (1+q tau)H^3.       (3.1)
```

Because `U` and `V` each have complex rank two,

```text
U^3=V^3=0.
```

Hence

```text
D^3       = 3(U^2V+UV^2),
D^2H      = (b+2a)U^2V + (a+2b)UV^2,
DH^2      = (2ab+a^2)U^2V + (2ab+b^2)UV^2,
H^3       = 3(a^2b U^2V + ab^2 UV^2).
```

Using `ab=1` and `tau=a+b`, the coefficients of `U^2V` and `UV^2` on the two sides of (3.1) agree separately. This proves the identity.

QED.

A useful arithmetic check is

```text
h^0(X,O_X(J)) = J^4/4! = ((1+qa)(1+qb))^2 = A^2,
```

using ampleness and the principal-polarization normalization. This coincidence is not used in the no-go proof below.

## 4. Natural two-term locally free realization

Resolve each divisor block by its two line bundles and collect signs. Define

```text
P_0 := O_X(D)^A
       direct_sum O_X(H)^q
       direct_sum O_X(-J),

P_1 := O_X(-D)^A
       direct_sum O_X(-H)^q
       direct_sum O_X(J).
```

Let

```text
d : P_0 -> P_1
```

be **any** bundle morphism, and let

```text
E_d := [P_0 --d--> P_1]
```

with `P_0` in cohomological degree `0` and `P_1` in degree `1`.

Then

```text
[E_d]=[P_0]-[P_1]
      = A Delta(D)+q Delta(H)-Delta(J),
```

where `Delta(L)=[O(L)]-[O(-L)]`. Therefore `L025a` gives

```text
ch(E_d)=2q(tau+q) beta'.             (4.1)
```

This family contains the split realization and every non-split realization obtained by inserting arbitrary allowed line-bundle maps between these two terms.

## 5. Off-diagonal degree-two cohomology vanishes

The line bundles occurring as matrix entries of

```text
Hom(P_0,P_1)
```

have first Chern classes among

```text
-2D,
-(D+H),
qH,
-2H,
J-H=D+(q-1)H,
2J.
```

The same list with opposite signs occurs in `Hom(P_1,P_0)`.

Because `q>=1` and `D,H` are ample, each nonzero class in the list is ample or anti-ample; in particular `J-H=D+(q-1)H` is ample.

On an abelian fourfold:

- if `L` is ample, `H^i(X,L)=0` for `i>0`;
- if `L` is anti-ample, Serre duality and `K_X=O_X` give `H^i(X,L)=0` for `i<4`.

Consequently

```text
H^2(X, Hom(P_0,P_1)) = 0,
H^2(X, Hom(P_1,P_0)) = 0.             (5.1)
```

This is independent of the differential `d`.

## 6. Hyper-Ext survival of the diagonal H^2 component

Filter the endomorphism complex of `E_d` by internal complex degree. Its local-to-global/hypercohomology spectral sequence has first page

```text
E_1^(p,q) = H^q(X, Hom^p(P_,P_)),
```

with only

```text
p=-1,0,1.
```

The diagonal term contributing to total degree two is

```text
E_1^(0,2)
 = H^2(X, End(P_0) direct_sum End(P_1)).
```

By (5.1),

```text
E_1^(-1,2)=E_1^(1,2)=0.
```

Hence the horizontal `d_1` neither enters nor leaves `E_1^(0,2)`. No higher differential can meet it because the internal-degree range is only `-1,0,1`. Therefore

```text
E_infinity^(0,2)=E_1^(0,2).           (6.1)
```

Thus a nonzero diagonal degree-two cohomology component of a characteristic obstruction cannot be made nullhomotopic by changing `d`.

This is the precise obstruction missed by the Chern-character identity: the trace can cancel in cohomology while the object-level diagonal `H^2` class survives the endomorphism spectral sequence.

## 7. Both mixed directions survive for every differential

For a line bundle with

```text
c_1(L)=rU+sV,
```
`HC-R021-L016` gives

```text
ev_(O(L))(k_7)=(qa+r^2) y_1 wedge y_2,
ev_(O(L))(k_8)=(qb+s^2) y_3 wedge y_4.      (7.1)
```

The same formulas hold for `O(-L)` because the mixed bivector term is quadratic in `c_1(L)` and the gerby term is unchanged.

For the three classes:

```text
D : (r,s)=(1,1),
H : (r,s)=(a,b),
J : (r,s)=(1+qa,1+qb).
```

All coefficients in (7.1) are strictly positive.

Take a nonzero mixed combination

```text
k=lambda k_7 + mu k_8.
```

On any `O(D)` diagonal summand its degree-two component is

```text
lambda(qa+1) y_1 wedge y_2
 + mu(qb+1) y_3 wedge y_4.             (7.2)
```

Since `y_1 wedge y_2` and `y_3 wedge y_4` are linearly independent and the two scalar coefficients are nonzero, (7.2) vanishes only when

```text
lambda=mu=0.
```

By (6.1), this diagonal class survives to `Ext^2(E_d,E_d)`. Hence

```text
ker(ob_(E_d)) intersect span(k_7,k_8)=0.     (7.3)
```

for every differential `d`.

## 8. The six ordinary directions lift for every differential

It remains to determine whether the rank can exceed `22`.

By `HC-R021-L013`, each of

```text
k_1,...,k_6
```

is a first-order commutative deformation direction preserving both `D` and `H`. It therefore also preserves

```text
J=D+qH.
```

Thus every line-bundle summand of `P_0` and `P_1` deforms along each `k_i`.

A nonzero matrix entry of `d` is a global section of one of the **ample** Hom bundles appearing in Section 5; anti-ample entries have no global sections and are identically zero. For every such ample Hom bundle `M`,

```text
H^1(X,M)=0.
```

Therefore every chosen section lifts over the first-order deformation once its source and target line bundles are lifted. Zero entries lift as zero. Entry by entry, the entire differential `d` lifts.

Hence the two-term complex `E_d` itself deforms along all six ordinary directions:

```text
ob_(E_d)(k_i)=0,  1<=i<=6.             (8.1)
```

Combining (7.3) and (8.1), and using the semiregularity compatibility inclusion from `L006/L007`,

```text
ker(ob_(E_d)) subset ker(c_beta')
                    = span(k_1,...,k_8),
```

we obtain

```text
ker(ob_(E_d))=span(k_1,...,k_6).
```

Therefore

```text
rank(ob_(E_d))=28-6=22.                (8.2)
```

## 9. HC-R021-L025 — three-divisor two-term no-go

### Statement

Let

```text
E_d=[P_0 -> P_1]
```

be any two-term locally free complex of Section 4, with arbitrary differential. Then

```text
ch(E_d)=2q(tau+q) beta',
ker(ob_(E_d))=span(k_1,...,k_6),
rank(ob_(E_d))=22.
```

In particular no non-split differential in the natural three-divisor realization can kill either mixed obstruction direction sufficiently to produce a rank-20 second factor.

### Proof

`L025a` and Section 4 give the Chern character. Sections 5-7 prove that no nonzero vector in `span(k_7,k_8)` can lie in the obstruction kernel for any differential. Section 8 proves that all six ordinary directions do lie in the kernel. The common contraction kernel has dimension eight by `L006`, and semiregularity compatibility gives the reverse containment needed to exclude further kernel directions. Thus the kernel has dimension six and the rank is `22`.

QED.

## 10. Structural lesson: a successful complex needs an index-two bridge

The proof identifies a sharper engineering requirement than “make the complex non-split.”

For a filtered locally free model whose associated-graded terms already carry nonzero diagonal mixed `H^2` actions, a nullhomotopy must have access to an off-diagonal contribution capable of hitting that degree-two graded piece. In the present two-term model this would require nonzero degree-two cohomology in a reverse/off-diagonal Hom complex.

The three-divisor line-bundle geometry has none:

```text
H^2(Hom(P_0,P_1))
 = H^2(Hom(P_1,P_0))
 = 0.
```

Thus the next positive construction must introduce a genuinely new bridge, for example:

1. a longer complex with adjacent terms whose reverse Hom has index-two cohomology;
2. a higher-rank or semihomogeneous bundle with non-scalar Atiyah action;
3. a torsion/intersection object whose Ext geometry supplies the missing degree-two boundary;
4. an autoequivalence image of an independently established rank-20 class.

The arithmetic identity remains potentially useful, but its natural two-term divisor resolution is exhausted.

## 11. Scope and firewall

`L025` does **not** prove:

- that every perfect complex of line bundles on the `beta'` ray has rank `>20`;
- that a longer complex with `K_0`-zero bridge terms cannot work;
- that higher-rank/semihomogeneous terms cannot work;
- that torsion or intersection-supported bridge terms cannot work;
- that no other contraction-rank-20 derived orbit can reach `beta'`;
- all-orders algebraicity transport;
- `HC-R021`;
- the Hodge conjecture.

It closes exactly the natural two-term non-split realization of the three-divisor identity.

## 12. Current disposition

```text
HC-R021-L025 = proved_in_solve_package_not_certified
three_divisor_Chern_identity = proved
three_divisor_two_term_rank = 22_for_every_differential
three_divisor_two_term_rank20 = impossible
six_ordinary_relations = vanish_for_every_differential
mixed_span_intersection_kernel = zero
index2_bridge_or_different_geometry = required
second_factor_rank20_exists = open
all_orders_transport = open
HC-R021-P4 = open
restricted_target_proved = false
full_hodge_conjecture_proved = false
```

## 13. Inputs

- `HC-R021-L006` for the exact rank-20 contraction map and eight-dimensional kernel;
- `HC-R021-L007` for the objectwise eight-relation criterion and semiregularity compatibility;
- `HC-R021-L013` for the six simultaneous commutative deformation directions;
- `HC-R021-L016` for the mixed characteristic action on a line bundle;
- standard Kodaira/IT0 vanishing on an abelian variety and Serre duality;
- the hypercohomology spectral sequence for the endomorphism complex of a bounded locally free complex.
