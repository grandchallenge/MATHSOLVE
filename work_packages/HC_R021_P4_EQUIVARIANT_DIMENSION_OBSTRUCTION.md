# HC-R021-P4 — Invariant-Ext dimension obstruction for a transitive translation symmetry

**Campaign:** `HC-001`  
**Restricted target:** `HC-R021-A8-CM4-C2`  
**Parent protected revision:** `09f63de8ec7a6833bdea0c3d007a76a55ee00a72`  
**State:** `NAIVE_TRANSITIVE_SYMMETRY_PRUNED_OUTSIDE_SMALL_RANGE`  
**Date:** 2026-09-16

## 1. Purpose

Test the most direct attempt to combine Route A with Markman's successful sixfold equivariant strategy: choose the `N` translated divisorial constituents in Example 11.2.7 as one orbit of a finite translation group and descend the glued sheaf to the quotient.

The result is a sharp dimension obstruction. In the broad parameter range this symmetry does not make the invariant obstruction space small enough; for `qN>=4` it is too large even for injective semiregularity on the full invariant `Ext^2`.

## 2. Setup

Let `E` be an admissible simple Example 11.2.7 gluing on the abelian fourfold `X` with

```text
ch(E) = N [D - (q/6) H^3],
D = g^*Theta,
H = (g^-1)^*Theta.
```

Assume a finite subgroup

```text
G subset X
```

acts by translations, permutes the `N` divisorial constituents transitively, preserves the full curve/line-bundle/gluing datum, and supplies a `G`-linearization of `E`.

Assume also that the divisorial support of a constituent has polarization class `D`, which is principal because `D=g^*Theta` and `g` is an automorphism.

## 3. Orbit size

### HC-R021-L011a

The translation stabilizer of a constituent's divisorial support is trivial. Hence

```text
|G| = N.
```

### Proof

If translation by `x in X` preserves the divisorial support `Z`, then

```text
tau_x^* O_X(Z) ~= O_X(Z).
```

Thus `x` belongs to the kernel of the polarization homomorphism associated with `O_X(Z)`. Its first Chern class is `D`, a principal polarization class, so this kernel is trivial. Therefore the translation orbit has cardinality `|G|`.

By assumption that the orbit is exactly the `N` constituent supports, `|G|=N`.

QED.

## 4. Descent and invariant Ext

Translations by a nonzero point act freely on an abelian variety. Let

```text
pi : X -> Xbar := X/G
```

be the degree-`N` finite etale quotient.

A `G`-linearized coherent sheaf descends to a coherent sheaf `Ebar` on `Xbar` with

```text
E ~= pi^* Ebar.
```

Because `G` is finite in characteristic zero,

```text
Ext^i_X(E,E)^G ~= Ext^i_Xbar(Ebar,Ebar).
```

The simplicity of `E` implies

```text
dim Hom_Xbar(Ebar,Ebar)=1.
```

Since `Xbar` is again an abelian fourfold, `K_Xbar=O_Xbar`, and Serre duality gives

```text
ext^4(Ebar,Ebar)=1,
ext^3(Ebar,Ebar)=ext^1(Ebar,Ebar).
```

Hence

```text
ext^2(Ebar,Ebar)
  = chi(Ebar,Ebar) + 2 ext^1(Ebar,Ebar) - 2
  >= chi(Ebar,Ebar) - 2.
```

## 5. HC-R021-L011 — invariant-Ext lower bound

Set

```text
I := integral_X D H^3.
```

Then

```text
dim Ext^2_X(E,E)^G >= (N q/3) I - 2 >= 8 q N - 2.
```

### Proof

`HC-R021-L004` gives

```text
chi_X(E,E) = (N^2 q/3) I.
```

For the finite etale degree-`N` quotient and `E=pi^*Ebar`, Riemann-Roch/base change gives

```text
chi_X(E,E) = N chi_Xbar(Ebar,Ebar).
```

Therefore

```text
chi_Xbar(Ebar,Ebar) = (N q/3) I.
```

Combining with the previous section yields

```text
dim Ext^2_X(E,E)^G
 = ext^2_Xbar(Ebar,Ebar)
 >= (N q/3) I - 2.
```

Khovanskii-Teissier for the ample principal classes `D,H` gives `I>=24`, so

```text
dim Ext^2_X(E,E)^G >= 8qN-2.
```

QED.

## 6. Consequences

### 6.1 Dimension forcing of Route A

Because the ambient Hochschild source is translation-invariant, equivariance gives

```text
Im(ob_E) subset Ext^2(E,E)^G.
```

A mere dimension estimate could force

```text
rank(ob_E) <= 20
```

only if

```text
dim Ext^2(E,E)^G <= 20.
```

The lower bound above makes this possible only if

```text
8qN - 2 <= 20,
qN <= 2.
```

Thus, outside the exceptional range `qN<=2`, transitive finite symmetry cannot prove `D20` nonempty merely by shrinking the invariant target dimension.

### 6.2 Full invariant semiregularity

The ordinary degree-two semiregularity target on an abelian fourfold has dimension `28`. If

```text
qN >= 4,
```

then

```text
dim Ext^2(E,E)^G >= 30,
```

so the semiregularity map cannot be injective on the full invariant `Ext^2`.

Accordingly, the direct analogue of the earlier sixfold proof via full invariant-`Ext^2` semiregularity is impossible for this transitive-orbit gluing whenever `qN>=4`.

The boundary case `qN=3` is not decided by dimension alone, and `qN<=2` remains potentially compatible with the dimension-forcing argument.

## 7. Scope

This does **not** rule out:

- the restricted rank-20 condition `D20` for a nonsymmetric or differently symmetric gluing;
- a finite autoequivalence group involving both translations and degree-zero twists rather than a pure transitive translation action on the constituents;
- weak equivariant semiregularity in a formulation whose obstruction group is strictly smaller than the full translation-invariant `Ext^2`;
- a direct calculation of the eight `L007` relations;
- Route A through a special point of `D20`.

It rules out only the naive transplantation of the successful sixfold argument in which the `N` constituents are one free translation orbit and smallness of the invariant `Ext^2` is expected to do the work automatically.

## 8. Current disposition

```text
HC-R021-L011 = proved_in_solve_package_not_certified
transitive_translation_orbit_size = N
invariant_Ext2_lower_bound = 8qN-2
invariant_dimension_forces_rank20_only_if_qN_le_2
full_invariant_semiregularity_impossible_if_qN_ge_4
D20_nonempty = open
weak_G_semiregularity_general = open
HC-R021-P4 = open
restricted_target_proved = false
full_hodge_conjecture_proved = false
```

## 9. Sources

- Eyal Markman, arXiv:2509.23079, Example 11.2.7.
- Eyal Markman, arXiv:2502.03415, Sections 8.3 and 9.3 for the earlier successful finite-translation strategy.
- `work_packages/HC_R021_P4_SEMIREGULARITY_DIAGNOSTICS.md` (`HC-R021-L004`).
