# HC-R021-P4 — PEL family coverage and global flat normalized class

**Campaign:** `HC-001`  
**Restricted target:** `HC-R021-A8-CM4-C2`  
**Parent protected revision:** `20358ac7630b4c9a6033e352a3a9a425f82bd3fb`  
**State:** `G6_FAMILY_COVERAGE_BOUND__G3_OPEN`  
**Date:** 2026-09-16

## 1. Purpose

Discharge the global-family interface `HC-R021-P4-G6` left open by the familywise Perry reduction `HC-R021-L002`.

Perry's theorem applies to a specified smooth proper algebraic family carrying the relevant normalized Chern character as a **global flat rational section** which remains Hodge. Markman's source proves the Hodge-theoretic invariance on a period domain; this package binds that analytic period-domain statement to an algebraic level-moduli family.

This does **not** prove weak equivariant semiregularity (`P4-G3`) and therefore does not close `HC-R021-P4`.

## 2. Markman's period component

Let

```text
V_Z := H^1(X,Z) direct_sum H^1(X-hat,Z)
```

with its natural symmetric pairing and let

```text
B subset H^ev(X,Q)
```

be the secant subspace associated to the CM field `K` and the chosen source datum.

Markman defines

```text
Spin(V_R)_B
```

as the subgroup fixing every point of `B`. Lemma 9.1.1 identifies its image in the orthogonal group with the product of the relevant special-unitary groups; in particular it commutes with the `K`-action.

For nonzero `t in K_-`, Markman defines the connected component

```text
Omega_B,t
```

as an adjoint orbit of `Spin(V_R)_B`. Section 9.2 proves that it parametrizes polarized abelian varieties of Weil type

```text
((A,I), eta, Xi_t)
```

with the fixed `K`-action and polarization type. In the source genus-four construction, the component through `X x X-hat` is the split-Weil component used by `HC-R021-A8-CM4-C2`.

Thus the selected target component is already represented analytically by one connected Hermitian symmetric/PEL period component.

## 3. Algebraic level cover

The rational `K`-action can be made integral after clearing finitely many denominators: choose an order

```text
O subset K
```

whose action preserves a finite-index lattice in `V_Q`. Likewise scale the rational polarization, if necessary, to a fixed integral polarization type. These finite-index/scaling choices do not alter the rational Hodge class or the connected complex period domain.

Choose a full level `ell >= 3` compatible with the polarization and the `O`-action. Standard PEL moduli theory gives a smooth quasi-projective fine moduli space after passing to a sufficiently small/neat level subgroup, together with a universal abelian scheme

```text
pi : A_univ -> S_PEL
```

carrying the prescribed endomorphism and polarization structures.

Analytically, a connected component of this level moduli space is an arithmetic quotient

```text
S_PEL(C) ~= Gamma \ Omega_B,t
```

for a sufficiently small arithmetic subgroup `Gamma` of the special-unitary group associated to the fixed integral PEL datum. If necessary, replace the PEL component by the connected arithmetic cover corresponding to

```text
Gamma subset rho(Spin(V_Q)_{eta,B}).
```

This is still an algebraic finite-level cover of the same connected PEL component; the universal abelian scheme is obtained by pullback.

Every polarized Weil-type abelian variety in the selected connected component admits a compatible full level structure after choosing a level basis. Hence the forgetful map from the level cover reaches every point quantified by the selected component, and in particular every point of its Hodge-generic locus `C_CM4`.

## 4. Monodromy invariance of the normalized class

Let `E_0` be the Markman/Orlov source object and let

```text
kappa_0 := kappa(E_0).
```

Proposition 10.2.1(1) of Markman proves that `kappa_0` is

```text
Spin(V)_{eta,B}-invariant.
```

Corollary 7.2.5 identifies the group fixing `B` after scalar extension with the `(eta,B)`-stabilizer, while Section 9 identifies the real period-domain group with the real `B`-stabilizer. Consequently the arithmetic monodromy subgroup `Gamma` chosen in Section 3 acts trivially on `kappa_0`.

The constant local system on `Omega_B,t` therefore has the constant section `kappa_0`, and `Gamma`-invariance lets it descend to a global flat rational section

```text
kappa_flat in H^0(S_PEL, R^ev pi_* Q).
```

This is stronger than merely saying that parallel transport exists along individual paths: the section is single-valued on the algebraic level-moduli base.

## 5. Hodge type on every fiber

Markman proves that the flat deformations of `kappa(E_0)` remain of Hodge type under every deformation of `(X x X-hat,eta)` as an abelian variety of Weil type. Equivalently, on the connected period component `Omega_B,t`, the invariant section above has Hodge type on every point.

After descending to `S_PEL`, `kappa_flat` is therefore a global flat section which is Hodge on every fiber of `pi`.

This is exactly the global-section hypothesis used by Perry's familywise theorem in `HC-R021-L002`.

## 6. HC-R021-L014 — G6 closure

### Statement

For the selected CM4 connected Weil-type deformation component there exists a connected smooth algebraic level-moduli cover

```text
pi : A_univ -> S_PEL
```

with the following properties:

1. every point of `C_CM4` has a lift to `S_PEL(C)`;
2. the source point `A_0=X x X-hat` has a lift after choosing level structure;
3. the flat deformation of `kappa(E_0)` descends to a global flat rational section `kappa_flat` of the even cohomology local system;
4. `kappa_flat` is of Hodge type on every fiber.

Hence the family/moduli coverage obligation `HC-R021-P4-G6` is discharged.

### Proof

Sections 2-5. The algebraic-family statement is the standard PEL/full-level realization of the polarized Weil-type period component; the global flatness is the additional nontrivial point and follows from Markman's exact `Spin(V)_{eta,B}` invariance of `kappa(E_0)` together with the choice of arithmetic monodromy inside that stabilizer.

QED.

## 7. Consequence for Route G

The equivariant Perry route is now

```text
G1/G2  finite-equivariant same-ray representatives        [AVAILABLE]
   |
   +--> G3  weak G-semiregularity of a useful object      [OPEN]
            |
            +--> G4 transport finite symmetry             [THEOREM INTERFACE]
                     |
                     +--> G5 apply Perry familywise        [CONDITIONAL ON G3]
                              |
                              +--> G6 algebraic family +
                                   global flat class        [CLOSED BY L014]
```

Thus `G6` is no longer an independent blocker. The substantive Route-G frontier is `G3`.

## 8. Scope and firewalls

This package does not prove:

- weak `G`-semiregularity;
- algebraicity of `kappa_flat` away from the source fiber;
- `D20 != empty`;
- the restricted HC-R021 theorem;
- the universal Hodge conjecture.

The statement that `kappa_flat` is Hodge is not the statement that it is algebraic. Perry is invoked only after `G3` is supplied.

## 9. Current disposition

```text
HC-R021-L014 = proved_in_solve_package_not_certified
P4_G6_family_coverage = complete_by_L014
global_flat_kappa_section = available_on_level_PEL_cover
P4_G3_weak_equivariant_semiregularity = open
D20_nonempty = open
HC-R021-P4 = open
restricted_target_proved = false
full_hodge_conjecture_proved = false
```

## 10. Sources

- Eyal Markman, arXiv:2509.23079, Corollary 7.2.5, Proposition 8.0.1, Sections 9.1-9.2, Proposition 10.2.1, Corollary 10.2.3, and Lemma 11.2.8.
- J. S. Milne, *Shimura Varieties and Moduli*, especially the full-level universal abelian-family discussion and PEL moduli interpretation.
- standard PEL Shimura theory for polarized abelian varieties with endomorphism and sufficiently small level structure.
