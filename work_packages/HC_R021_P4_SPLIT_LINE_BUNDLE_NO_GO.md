# HC-R021-P4 — Split line-bundle no-go for the mixed D20 relations

**Campaign:** `HC-001`  
**Restricted target:** `HC-R021-A8-CM4-C2`  
**Parent protected revision:** `20358ac7630b4c9a6033e352a3a9a425f82bd3fb`  
**State:** `SPLIT_LINE_BUNDLE_ROUTE_PRUNED__NONTRIVIAL_EXTENSION_REQUIRED`  
**Date:** 2026-09-16

## 1. Purpose

Strengthen the explicit rank-22 control `HC-R021-L015` to a structural no-go statement.

The issue is not the particular integral `K_0` presentation chosen there. No nonzero split perfect complex assembled from shifted line bundles can satisfy all eight `HC-R021-L007` relations. Once a line bundle kills the six ordinary simultaneous-polarization directions, the two mixed directions have strictly nonzero characteristic action.

Thus a positive `D20` construction must use genuinely nontrivial extension/gluing data, or leave the split line-bundle class entirely.

## 2. RM basis and the mixed generators

Use the real-multiplication normal form of `HC-R021-L006`:

```text
D = U + V,
H = a U + b V,
U = x_1 y_1 + x_2 y_2,
V = x_3 y_3 + x_4 y_4,
ab = 1,
a,b > 0,
a != b,
c = -q/6,
q > 0.
```

The six ordinary kernel generators are

```text
k_1 = y_1 t_1,
k_2 = y_2 t_2,
k_3 = y_1 t_2 + y_2 t_1,
k_4 = y_3 t_3,
k_5 = y_4 t_4,
k_6 = y_3 t_4 + y_4 t_3.
```

The two mixed generators of `ker(c_beta')` are

```text
k_7 = t_1 wedge t_2 - 6 c a^2 b (y_1 wedge y_2)
    = t_1 wedge t_2 + q a (y_1 wedge y_2),

k_8 = t_3 wedge t_4 - 6 c a b^2 (y_3 wedge y_4)
    = t_3 wedge t_4 + q b (y_3 wedge y_4).
```

The final equalities use `ab=1` and `c=-q/6`.

## 3. Line-bundle characteristic action

For a line bundle `L` with first Chern class `ell`, `HC-R021-L015` records the degree-two characteristic action

```text
ev_L(alpha,xi,pi)
  = alpha + xi contraction ell + (1/2) pi contraction ell^2
```

in `Ext^2(L,L)=H^2(O_X)`.

Shifting a line bundle does not change this self-characteristic action.

## 4. Killing k1,...,k6 forces the Chern class into the two-block span

Write a general `(1,1)` class as

```text
ell = sum_(i,j=1)^4 m_ij x_i y_j.
```

Assume

```text
ev_L(k_i)=0,  i=1,...,6.
```

For `k_1=y_1 t_1`, contraction with `ell` gives

```text
y_1 wedge (sum_j m_1j y_j)=0,
```

so every entry in row `1` except `m_11` vanishes. The same argument with `k_2,k_4,k_5` shows that `ell` is diagonal.

For

```text
k_3 = y_1 t_2 + y_2 t_1,
```

the remaining action is a nonzero scalar multiple of

```text
(m_22-m_11) y_1 wedge y_2,
```

hence `m_11=m_22`. Similarly `k_6` gives `m_33=m_44`.

Therefore

```text
ell = A U + B V
```

for scalars `A,B`. Since `ell=c_1(L)` is a real integral `(1,1)` class, `A,B` are real.

This is the exact annihilator, inside `H^(1,1)`, of the six ordinary directions.

## 5. HC-R021-L016 — the mixed directions cannot vanish on a line bundle

### Statement

Let `L` be a line bundle on the source abelian fourfold. If

```text
ev_L(k_i)=0,  i=1,...,6,
```

then

```text
ev_L(k_7) = (q a + A^2) y_1 wedge y_2 != 0,
ev_L(k_8) = (q b + B^2) y_3 wedge y_4 != 0,
```

where `c_1(L)=A U+B V`.

In particular no line bundle annihilates all eight generators of `ker(c_beta')`.

### Proof

By Section 4, `ell=A U+B V`.

Under the contraction conventions fixed in `HC-R021-L006` and `HC-R021-L015`,

```text
(1/2)(t_1 wedge t_2) contraction ell^2
  = A^2 y_1 wedge y_2,

(1/2)(t_3 wedge t_4) contraction ell^2
  = B^2 y_3 wedge y_4.
```

Using the expressions for `k_7,k_8` from Section 2 gives the two displayed formulas.

Because

```text
q>0,
a>0,
b>0,
A^2>=0,
B^2>=0,
```

both coefficients are strictly positive. Hence neither mixed class vanishes.

QED.

## 6. Corollary — no split line-bundle complex lies in D20

Let

```text
P = direct_sum_j L_j[n_j]
```

be a nonzero split perfect complex whose summands are shifted line bundles.

The characteristic action on a direct sum is block diagonal. If all eight `k_i` lay in `ker(ev_P)`, then every `k_i` would lie in `ker(ev_Lj)` for every summand `L_j`. Section 5 shows this is impossible for any nonzero line-bundle summand.

Therefore

```text
span(k_1,...,k_8) not_subset ker(ev_P)
```

for every nonzero split complex of shifted line bundles. In particular, no such split complex can satisfy

```text
ker(ob_P)=ker(c_beta')
```

or provide a rank-20 `D20` point on the beta-prime ray.

This includes, but is strictly stronger than, the explicit rank-22 control `P_beta` of `HC-R021-L015`.

## 7. Consequence for the active search

The direct perfect-complex engineering problem is now sharper:

```text
split line-bundle realizations                     [PRUNED BY L016]
        |
        v
non-formal complex / coherent gluing
with nonzero extension data                         [REQUIRED]
        |
        +--> preserve the six ordinary relations
        |
        +--> make k_7 and k_8 nullhomotopic
        |
        v
D20 / rank-20 object                                [OPEN]
```

The mixed cancellation needed by `beta'` cannot occur termwise on real line bundles. It must arise from the derived differential, extension classes, or genuinely higher-rank/non-line-bundle geometry.

This also explains why Chern-character cancellation alone is too weak: the required negative contribution to the mixed obstruction is visible only after passing beyond a split line-bundle model.

## 8. Scope

This result does **not** rule out:

- a non-split complex of line bundles whose differential supplies the required nullhomotopies;
- a coherent Example 11.2.7 gluing;
- a higher-rank bundle or semihomogeneous object with non-scalar Atiyah data;
- weak equivariant semiregularity in an invariant category;
- Route G through a non-naive translation-plus-twist symmetry.

It rules out only split sums of shifted line bundles as positive `D20` objects.

## 9. Current disposition

```text
HC-R021-L016 = proved_in_solve_package_not_certified
split_line_bundle_D20_route = pruned
all_six_ordinary_relations_on_line_bundle => both_mixed_relations_nonzero
nontrivial_extension_or_non_line_bundle_geometry = required_for_positive_route
D20_nonempty = open
P4_G3 = open
HC-R021-P4 = open
restricted_target_proved = false
full_hodge_conjecture_proved = false
```

## 10. Sources

- `work_packages/HC_R021_P4_CONTRACTION_RANK.md` (`HC-R021-L006`).
- `work_packages/HC_R021_P4_ATIYAH_RANK_REDUCTION.md` (`HC-R021-L007`).
- `work_packages/HC_R021_P4_SIX_COMMUTATIVE_DIRECTIONS.md` (`HC-R021-L013`).
- `work_packages/HC_R021_P4_LINE_BUNDLE_CONTROL.md` (`HC-R021-L015`).
- Standard Atiyah-class/HKR characteristic action for a line bundle on an abelian variety.
