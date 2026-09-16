# HC-R021-P4 — Mixed-direction no-go for the Example 11.2.7 coherent gluing family

**Campaign:** `HC-001`  
**Restricted target:** `HC-R021-A8-CM4-C2`  
**Parent protected revision:** `20358ac7630b4c9a6033e352a3a9a425f82bd3fb`  
**State:** `COHERENT_EXAMPLE_11_2_7_D20_EMPTY__PERFECT_LANE_REMAINS`  
**Date:** 2026-09-16

## 1. Result

Let `E'` be any coherent sheaf obtained by the gluing construction of Markman Example 11.2.7, with

```text
ch(E') = N beta',
beta' = D - (q/6) H^3,
D = g^*Theta,
H = (g^-1)^*Theta.
```

Then the two mixed generators `k_7,k_8` of `ker(c_beta')` cannot both vanish under the object-level Hochschild action. Consequently

```text
rank(ob_E') > 20
```

for every such coherent gluing, and the determinantal locus `D20` inside the Example 11.2.7 coherent gluing stack is empty.

This refutes the **coherent gluing realization** of Route A. It does not refute the same-ray derived/perfect-complex lane allowed by Markman Lemma 11.2.8.

## 2. The two mixed deformation directions

Use the real-multiplication normal form of `HC-R021-L006`. The mixed kernel vectors are

```text
k_7 = pi_1 + q a alpha_1,
k_8 = pi_2 + q b alpha_2,
```

where

```text
pi_1 = t_1 wedge t_2,
pi_2 = t_3 wedge t_4,
alpha_1 = y_1 wedge y_2,
alpha_2 = y_3 wedge y_4,
a,b,q > 0,
ab = 1.
```

The bivectors `pi_1,pi_2` have rank two and complementary images

```text
V_1 := span(t_1,t_2),
V_2 := span(t_3,t_4),
V_1 intersect V_2 = 0.
```

The `alpha_i` components are gerby `H^2(O_X)` directions. On a sufficiently small affine/analytic neighborhood they are cohomologically trivial. Thus the local algebra deformation underlying `k_i` has first-order commutator controlled by `pi_i`.

## 3. First-order coisotropic-support lemma

### HC-R021-L019a

Let `U` be smooth, let

```text
A_epsilon
```

be a flat first-order deformation of `O_U` over `C[epsilon]/(epsilon^2)` whose commutator is

```text
[f,g]_* = epsilon {f,g}_pi
```

modulo `epsilon^2`, for a holomorphic Poisson bivector `pi`.

Let `M` be a coherent `O_U`-module which is generically a nonzero locally free module on its reduced support `Y`, and suppose `M` admits a flat deformation `M_epsilon` as an `A_epsilon`-module. Then the smooth locus of `Y` is coisotropic for `pi`.

### Proof

Work at a smooth generic point of `Y`, where `M` is faithful as an `O_Y`-module. Let `I` be the ideal of `Y` and take `f,g in I`.

Because `f` and `g` annihilate the special fiber `M`, their actions on `M_epsilon` have image in `epsilon M_epsilon`. Hence the composition of either two such actions lands in `epsilon^2 M_epsilon=0`, so

```text
[rho(f),rho(g)] = 0.
```

On the other hand the module relation gives

```text
[rho(f),rho(g)]
 = rho([f,g]_*)
 = epsilon rho({f,g}_pi).
```

Reducing the coefficient of `epsilon` to the special fiber shows that `{f,g}_pi` annihilates `M`; faithfulness on `Y` gives

```text
{I,I}_pi subset I.
```

This is exactly the coisotropic condition on the smooth locus of `Y`.

QED.

This is the first-order algebraic form of the standard coisotropic-support necessity for quantizable coherent modules (Gabber/involutivity in the formal setting).

## 4. Coisotropic curves for a rank-two constant bivector

Let `C` be a reduced curve in the abelian fourfold `X` and let `p` be a smooth point. Write

```text
T_p X = V_1 direct_sum V_2.
```

### HC-R021-L019b

If `C` is coisotropic at `p` for

```text
pi_1 = t_1 wedge t_2,
```

then

```text
T_p C subset V_1.
```

Likewise, coisotropy for `pi_2=t_3 wedge t_4` implies `T_p C subset V_2`.

### Proof

For `pi_1`, the kernel of

```text
pi_1^sharp : T_p^*X -> T_pX
```

is the annihilator of `V_1` and has dimension two. The conormal `N_p^*C` has dimension three. Coisotropy is

```text
pi_1^sharp(N_p^*C) subset T_pC.
```

Since the target line has dimension one, this requires

```text
dim(N_p^*C intersect ker(pi_1^sharp)) = 2,
```

so `ker(pi_1^sharp) subset N_p^*C`. Taking annihilators gives `T_pC subset V_1`. The converse dimension calculation is the usual rank-two hypersurface-in-leaf calculation. The proof for `pi_2` is identical.

QED.

In particular no nonzero tangent line can satisfy both conditions because `V_1 intersect V_2=0`.

## 5. Apply to the Example 11.2.7 gluing

Markman's coherent gluing has a triangle/local exact model

```text
0 -> E' -> A direct_sum i_*L -> Q -> 0,
```

where `A` is the direct sum of translated divisorial secant constituents, `i:C'->X` is the correction curve with a line bundle `L`, and `Q` is supported on the finite set of gluing points.

The construction requires `C'` to meet the translated divisor supports in a finite set and uses fiber identifications there. Choose a smooth point `p` on the reduced support of an irreducible component of `C'` away from all these finite intersections. On a sufficiently small neighborhood of `p`,

```text
E' ~= i_*L.
```

Assume first that

```text
ob_E'(k_7)=0.
```

The characteristic obstruction theorem (Lowen/Toda) identifies this with existence of a first-order deformation of the object in the category deformed by `k_7`; restricting to the neighborhood of `p` and trivializing the gerby `H^2(O)` component gives a flat local module deformation with Poisson part `pi_1`. `L019a` and `L019b` therefore imply

```text
T_pC' subset V_1.
```

If also

```text
ob_E'(k_8)=0,
```

the same argument gives

```text
T_pC' subset V_2.
```

Hence

```text
T_pC' subset V_1 intersect V_2 = 0,
```

contradicting that `p` is a smooth point of a curve.

Therefore at least one of

```text
ob_E'(k_7), ob_E'(k_8)
```

is nonzero for every Example 11.2.7 coherent gluing.

## 6. HC-R021-L019 — coherent D20 is empty

### Statement

For the entire admissible/simple coherent gluing family of Markman Example 11.2.7,

```text
D20 = empty.
```

Equivalently, no sheaf in that family satisfies

```text
ker(ob_E') = ker(c_beta')
```

or `rank(ob_E')=20`.

### Proof

`HC-R021-L007` says rank `20` requires all eight kernel generators, in particular `k_7,k_8`, to vanish under `ob_E'`. Section 5 proves simultaneous vanishing of the two mixed classes is impossible. Hence no point belongs to `D20`.

QED.

## 7. Consequences for the campaign

The coherent Route-A branch

```text
Example 11.2.7 gluing stack -> D20 nonempty
```

is refuted and should be closed as a route rather than left as an open search problem.

The following remain viable:

1. a genuinely non-formal object of `D^b(X)` with Chern character a nonzero integer multiple of `beta'`, as permitted by Markman Lemma 11.2.8;
2. a different coherent construction not containing an open curve-supported locus subject simultaneously to the two incompatible rank-two Poisson conditions.

By `HC-R021-L018`, any Perry weak-equivariant route still requires the second-factor rank-20/eight-relation property, so equivariance does not reopen the refuted Example 11.2.7 family.

## 8. Scope and firewall

This result does **not** prove:

- that no object of `D^b(X)` with Chern character proportional to `beta'` can have rank-20 obstruction map;
- that every conceivable coherent representative of the same Chern character is excluded;
- all-orders deformation or algebraicity transport;
- the restricted HC-R021 theorem;
- the universal Hodge conjecture.

The no-go uses the specific local structure of Example 11.2.7: away from the finite gluing set there is an open locus on which the object is a line bundle supported on the correction curve.

## 9. Current disposition

```text
HC-R021-L019 = proved_in_solve_package_not_certified
Example_11_2_7_coherent_D20 = empty
A0d_coherent_gluing = refuted
second_factor_rank20_exists_in_Db = open
nonformal_perfect_lane = open
G3_after_rank20 = open
HC-R021-P4 = open
restricted_target_proved = false
full_hodge_conjecture_proved = false
```

## 10. Sources

- Eyal Markman, arXiv:2509.23079, Question 11.2.2, Example 11.2.7, Lemma 11.2.8.
- Eyal Markman, arXiv:2502.03415, Example 8.2.4 for the genus-four secant building block.
- Yukinobu Toda, *Deformations and Fourier-Mukai transforms*, J. Differential Geom. 81 (2009), for the `H^2(O) + H^1(T) + H^0(Lambda^2 T)` first-order deformation framework.
- Wendy Lowen, *Hochschild cohomology, the characteristic morphism and derived deformations*, Compos. Math. 144 (2008), for the characteristic obstruction interpretation.
- Standard coisotropic-support necessity for modules over deformation quantizations (Gabber involutivity); Section 3 gives the elementary first-order argument needed here.
