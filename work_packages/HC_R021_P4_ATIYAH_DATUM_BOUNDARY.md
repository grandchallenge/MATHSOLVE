# HC-R021-P4-A0 — Object-specific datum boundary for the Atiyah-rank route

**Campaign:** `HC-001`  
**Restricted target:** `HC-R021-A8-CM4-C2`  
**Parent protected revision:** `09f63de8ec7a6833bdea0c3d007a76a55ee00a72`  
**State:** `SOURCE_FAMILY_IDENTIFIED__REPRESENTATIVE_BINDING_REQUIRED`  
**Date:** 2026-09-16

## 1. Result

The direct Atiyah-rank route cannot assign a single value to

```text
rank(ob_E')
```

from Markman Example 11.2.7 as published, because that example does not define one canonical coherent sheaf `E'`.

It defines a family of admissible glued sheaves by several existential/generic choices. The Chern character is fixed on that family, but the object-specific Yoneda algebra and hence the obstruction homomorphism are not determined by the Chern character.

Therefore the next direct-route obligation is not yet “compute one missing matrix.” It is:

```text
P4-A0:
  either bind one concrete admissible gluing datum E'_star,
  or prove the eight L007 Yoneda relations uniformly for every admissible
  Example 11.2.7 gluing datum under a stated open/generic condition.
```

Only after `P4-A0` is discharged is `P4-A1 = compute rank(ob_E'_star)` an exact representative-specific calculation.

## 2. What the source fixes

Markman fixes the cohomological target ray

```text
beta' = g^*Theta - (q/6)(g^-1)^*(Theta^3)
```

and requires a coherent sheaf with Chern character an integer multiple of that class.

The construction fixes the following structural pattern:

1. choose a sufficiently large positive integer `d`;
2. choose a positive integer `N` such that

```text
(N/6)(d g^*(Theta^3) - q (g^-1)^*(Theta^3))
```

is represented by a curve `C'`;
3. start from a simple coherent secant sheaf `F'` with

```text
ch(F') = Theta - (d/6)Theta^3;
```

4. choose `N` generic translates of `g^*F'` satisfying the stated transversality condition with `C'`;
5. choose a line bundle `L` on `C'` of suitable degree;
6. choose isomorphisms of one-dimensional fibers at every intersection point and glue.

The output satisfies

```text
ch(E') = N beta'
```

and can be chosen simple.

## 3. What the source does not fix

The published Example 11.2.7 does not specify:

- a unique `d`;
- a unique `N`;
- an explicit curve `C'` representing the required class;
- the translation parameters of the `N` secant constituents;
- the line bundle `L` beyond a degree condition;
- the individual fiber-identification scalars;
- an explicit presentation of the resulting self-Ext algebra.

Consequently it does not specify a unique isomorphism class of `E'`.

This is not a defect in Markman's construction. The paper only needs existence of a coherent sheaf on the correct secant ray for the cohomological nonzero-Weil criterion. The present campaign asks a finer deformation-theoretic question that depends on the actual object.

## 4. HC-R021-L008 — Chern data do not determine the A1 obstruction map

### Statement

Let `E` range over the admissible Example 11.2.7 gluing family with

```text
ch(E) = N beta'.
```

The semiregularity compatibility theorem determines the common cohomological constraint

```text
ker(ob_E) subset ker(c_beta'),
```

and `HC-R021-L006` determines the right-hand side exactly as an eight-dimensional subspace.

However, neither the Chern character nor the published construction data determine the values

```text
ev_E(k_i) in Ext^2(E,E),  i=1,...,8.
```

Those values depend on the actual object and its gluing morphism. Hence the published source does not determine a unique numerical value of `rank(ob_E)`.

### Proof

The obstruction map

```text
ob_E : HT^2(X) -> Ext^2(E,E)
```

is the degree-two component of the Hochschild action on the object `E`; its codomain, multiplication, and image are object-specific.

The Chern character enters only after composing with the semiregularity map:

```text
HT^2(X) --ob_E--> Ext^2(E,E) --sigma_E--> H_Omega^{-2}(X),
```

whose composite is contraction with `ch(E)`.

Thus equality of Chern characters fixes the composite `sigma_E o ob_E`, but does not recover `ob_E` itself. In particular, cohomological cancellation

```text
k_i contraction ch(E) = 0
```

only implies

```text
ob_E(k_i) in ker(sigma_E),
```

not `ob_E(k_i)=0`.

Example 11.2.7 leaves the gluing choices listed in Section 3 unspecified, so no single self-Ext algebra or gluing morphism is selected from which those eight object-specific classes can be evaluated.

QED.

## 5. Two valid continuations

### Route A0-R — bind a representative

Supply a concrete admissible datum

```text
D_star = (d,N,C', {T_j}, L, {phi_p})
```

with exact equations or a content-addressed algebraic description sufficient to reconstruct

```text
0 -> E'_star -> (direct_sum_j T_j) direct_sum i_*L -> direct_sum_p k_p -> 0.
```

Then compute the eight `HC-R021-L007` Yoneda classes for that exact object.

A positive result for `E'_star` is enough for Markman's existential Question 11.2.2, provided all other source hypotheses are verified for the bound datum.

### Route A0-U — prove uniform generic vanishing

Avoid selecting one representative by proving that, on a stated nonempty open subset of the admissible gluing-parameter space,

```text
ev_E(k_i)=0,  i=1,...,8.
```

This is stronger than necessary but would make `rank(ob_E)=20` independent of the remaining generic choices on that open set.

Any uniform argument must use the actual gluing triangle; Chern-character additivity alone is insufficient.

## 6. Relation to the eight-relation reduction

`HC-R021-L007` remains valid for every individual admissible object `E` with the fixed cohomological class: once an object is fixed,

```text
rank(ob_E)=20
```

if and only if all eight displayed kernel generators vanish under its Hochschild action.

`HC-R021-L008` changes only the ordering of proof obligations:

```text
L006  exact common contraction kernel
  |
  +--> L007  objectwise eight-relation criterion
          |
          +--> P4-A0  bind one object OR prove uniform generic vanishing
                  |
                  +--> P4-A1  evaluate the eight relations / rank ob
                          |
                          +--> P4-A2  all-orders obstruction-image stability
```

## 7. Evidentiary boundary

The current source record is sufficient to prove `L007` and `L008`, but it is not sufficient to decide the eight Yoneda classes of a single object because no single object is selected.

This is a substantive evidentiary boundary, not an infrastructure failure and not a governance stop. Recovery within scope consists of constructing/binding an admissible representative or proving a uniform theorem over the gluing parameter space.

No MATHCERT handoff is warranted at this stage.

## 8. Current disposition

```text
HC-R021-L008 = proved_in_solve_package_not_certified
source_defines_unique_E_prime = false
source_defines_admissible_gluing_family = true
common_contraction_kernel_dimension = 8
P4_A0 = open
P4_A1 = blocked_on_A0_for_representative_specific_computation
Markman_Question_11_2_2 = open
HC-R021-P4 = open
restricted_target_proved = false
full_hodge_conjecture_proved = false
```

## 9. Sources

- Eyal Markman, *Secant sheaves on abelian n-folds with real multiplication and Weil classes on abelian 2n-folds with complex multiplication*, arXiv:2509.23079; Question 11.2.2 and Example 11.2.7.
- `work_packages/HC_R021_P4_CONTRACTION_RANK.md` for `HC-R021-L006`.
- `work_packages/HC_R021_P4_ATIYAH_RANK_REDUCTION.md` for `HC-R021-L007`.
