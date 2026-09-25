import MathSolve.UnionClosed.FunctionalPreorderD005
import Mathlib.Tactic

/-!
# UC-001 / UC-P04: closure-system obstruction to universal D003 representation

WP07-D005 proves Frankl abundance for complements of exact D003
functional-preorder ideal families. This module tests the proposed universal
representation bridge. The result is negative: every such complement family is
closed under literal set intersection, while a concrete three-point
union-closed family need not be.

The module also records the exact complement duality that survives universally:
union closure on a carried finite family becomes intersection closure after
carrier-relative complementation. This identifies finite closure systems,
rather than exact functional-preorder representations, as the next UC-P04
interface.
-/

namespace MathSolve.UnionClosed.WP08

open Finset

universe u

variable {α : Type u} [DecidableEq α]

open MathSolve.UnionClosed.WP07

/-- Literal binary intersection closure of a finite set family. -/
def IsInterClosed (F : Family α) : Prop :=
  ∀ A ∈ F, ∀ B ∈ F, A ∩ B ∈ F

/-- Carrier-relative complementation turns union closure into literal
intersection closure. -/
theorem complementFamilyOn_interClosed_of_unionClosed
    {F : Family α} {U : Finset α}
    (hUnion : IsUnionClosed F) :
    IsInterClosed (complementFamilyOn F U) := by
  classical
  intro A hA B hB
  rw [complementFamilyOn] at hA hB
  rcases Finset.mem_image.mp hA with ⟨S, hS, rfl⟩
  rcases Finset.mem_image.mp hB with ⟨T, hT, rfl⟩
  have hUnionST : S ∪ T ∈ F := hUnion S hS T hT
  rw [complementFamilyOn]
  refine Finset.mem_image.mpr ⟨S ∪ T, hUnionST, ?_⟩
  ext x
  by_cases hxU : x ∈ U <;>
    by_cases hxS : x ∈ S <;>
      by_cases hxT : x ∈ T <;>
        simp [hxU, hxS, hxT]

/-- Dually, carrier-relative complementation turns literal intersection closure
into union closure. -/
theorem complementFamilyOn_unionClosed_of_interClosed
    {F : Family α} {U : Finset α}
    (hInter : IsInterClosed F) :
    IsUnionClosed (complementFamilyOn F U) := by
  classical
  intro A hA B hB
  rw [complementFamilyOn] at hA hB
  rcases Finset.mem_image.mp hA with ⟨S, hS, rfl⟩
  rcases Finset.mem_image.mp hB with ⟨T, hT, rfl⟩
  have hInterST : S ∩ T ∈ F := hInter S hS T hT
  rw [complementFamilyOn]
  refine Finset.mem_image.mpr ⟨S ∩ T, hInterST, ?_⟩
  ext x
  by_cases hxU : x ∈ U <;>
    by_cases hxS : x ∈ S <;>
      by_cases hxT : x ∈ T <;>
        simp [hxU, hxS, hxT]

/-- Complementing twice inside a carrier recovers a family whose members all
lie inside that carrier. -/
theorem complementFamilyOn_involutive
    {F : Family α} {U : Finset α}
    (hsub : ∀ S ∈ F, S ⊆ U) :
    complementFamilyOn (complementFamilyOn F U) U = F := by
  classical
  ext A
  constructor
  · intro hA
    rw [complementFamilyOn] at hA
    rcases Finset.mem_image.mp hA with ⟨T, hT, hAeq⟩
    rw [complementFamilyOn] at hT
    rcases Finset.mem_image.mp hT with ⟨S, hS, rfl⟩
    have hdouble : U \ (U \ S) = S :=
      sdiff_sdiff_eq_self_of_subset (hsub S hS)
    rw [hdouble] at hAeq
    rw [← hAeq]
    exact hS
  · intro hA
    rw [complementFamilyOn]
    refine Finset.mem_image.mpr ⟨U \ A, ?_, ?_⟩
    · rw [complementFamilyOn]
      exact Finset.mem_image.mpr ⟨A, hA, rfl⟩
    · exact sdiff_sdiff_eq_self_of_subset (hsub A hA)

/-- On an explicit carrier, union closure of a finite family is exactly
intersection closure of its carrier-relative complement. -/
theorem unionClosed_iff_complement_interClosed
    {F : Family α} {U : Finset α}
    (hsub : ∀ S ∈ F, S ⊆ U) :
    IsUnionClosed F ↔ IsInterClosed (complementFamilyOn F U) := by
  constructor
  · exact complementFamilyOn_interClosed_of_unionClosed
  · intro hInter
    have hUnionDouble :
        IsUnionClosed (complementFamilyOn (complementFamilyOn F U) U) :=
      complementFamilyOn_unionClosed_of_interClosed hInter
    rw [complementFamilyOn_involutive hsub] at hUnionDouble
    exact hUnionDouble

/-- A finite closure system on an explicit carrier: all members lie in the
carrier, the carrier itself is closed, and the family is intersection-closed. -/
def IsClosureSystemOn (F : Family α) (U : Finset α) : Prop :=
  (∀ S ∈ F, S ⊆ U) ∧ U ∈ F ∧ IsInterClosed F

/-- Every member of a carrier-relative complement family lies in the carrier. -/
theorem complementFamilyOn_members_subset
    {F : Family α} {U : Finset α} :
    ∀ S ∈ complementFamilyOn F U, S ⊆ U := by
  classical
  intro S hS x hx
  rw [complementFamilyOn] at hS
  rcases Finset.mem_image.mp hS with ⟨T, hT, rfl⟩
  exact (Finset.mem_sdiff.mp hx).1

/-- Any union-closed family containing the empty set produces a finite closure
system after carrier-relative complementation. -/
theorem complementFamilyOn_closureSystem_of_unionClosed
    {F : Family α} {U : Finset α}
    (hempty : (∅ : Finset α) ∈ F)
    (hUnion : IsUnionClosed F) :
    IsClosureSystemOn (complementFamilyOn F U) U := by
  refine ⟨complementFamilyOn_members_subset, ?_, ?_⟩
  · exact ground_mem_complementFamilyOn (F := F) (U := U) hempty
  · exact complementFamilyOn_interClosed_of_unionClosed hUnion

/-- Exact D003 functional-preorder ideal families are themselves union-closed. -/
theorem functionalPreorderIdealFamily_union_closed
    {F : Family α} {U : Finset α}
    (h : IsFunctionalPreorderIdealFamilyOn F U) :
    IsUnionClosed F := by
  rcases h with ⟨S, hU, hF⟩
  subst U
  subst F
  intro A hA B hB
  rw [S.mem_idealFamily_iff] at hA hB ⊢
  constructor
  · intro x hx
    simp only [Finset.mem_union] at hx ⊢
    rcases hx with hxA | hxB
    · exact hA.1 hxA
    · exact hB.1 hxB
  · intro x hx y hy hle
    simp only [Finset.mem_union] at hx ⊢
    rcases hx with hxA | hxB
    · exact Or.inl (hA.2 hxA hy hle)
    · exact Or.inr (hB.2 hxB hy hle)

/-- Therefore every D003 complement family is also intersection-closed. -/
theorem complementFamilyOn_interClosed_of_functionalPreorder
    {F : Family α} {U : Finset α}
    (h : IsFunctionalPreorderIdealFamilyOn F U) :
    IsInterClosed (complementFamilyOn F U) :=
  complementFamilyOn_interClosed_of_unionClosed
    (functionalPreorderIdealFamily_union_closed h)

/-- Necessary structural condition for the exact WP07 representation class:
represented families are closed under both union and literal intersection. -/
theorem complementOfFunctionalPreorderIdealFamily_latticeClosed
    {G : Family α}
    (hG : IsComplementOfFunctionalPreorderIdealFamily G) :
    IsUnionClosed G ∧ IsInterClosed G := by
  rcases hG with ⟨F, U, hF, rfl⟩
  exact ⟨
    complementFamilyOn_unionClosed_of_functionalPreorder hF,
    complementFamilyOn_interClosed_of_functionalPreorder hF
  ⟩

/-! ## Exact three-point obstruction -/

abbrev p04AB : Finset Chain3 := {Chain3.a, Chain3.b}
abbrev p04BC : Finset Chain3 := {Chain3.b, Chain3.c}
abbrev p04B : Finset Chain3 := {Chain3.b}

/-- A concrete union-closed family on three points. It contains the empty set
and full carrier, so its failure of D003 representability is not an endpoint
artifact. -/
abbrev p04Counterexample : Family Chain3 :=
  {∅, p04AB, p04BC, Chain3.ground}

/-- The concrete family is union-closed. -/
theorem p04Counterexample_unionClosed :
    IsUnionClosed p04Counterexample := by
  intro A hA B hB
  simp only [p04Counterexample, Finset.mem_insert, Finset.mem_singleton] at hA hB ⊢
  rcases hA with rfl | rfl | rfl | rfl <;>
    rcases hB with rfl | rfl | rfl | rfl <;>
    native_decide

/-- The concrete family is nontrivial. -/
theorem p04Counterexample_nontrivial :
    IsNontrivial p04Counterexample := by
  refine ⟨Chain3.b, ?_⟩
  exact (mem_support_iff p04Counterexample Chain3.b).2
    ⟨p04AB, by native_decide, by native_decide⟩

/-- The concrete family itself satisfies the Frankl half-frequency conclusion. -/
theorem p04Counterexample_frankl :
    IsFranklAbundant p04Counterexample := by
  refine ⟨Chain3.b, ?_, ?_⟩
  · exact (mem_support_iff p04Counterexample Chain3.b).2
      ⟨p04AB, by native_decide, by native_decide⟩
  · native_decide

/-- The concrete family contains both endpoint sets. -/
theorem p04Counterexample_endpoints :
    (∅ : Finset Chain3) ∈ p04Counterexample ∧
      Chain3.ground ∈ p04Counterexample := by
  native_decide

/-- Its decisive obstruction is literal intersection:
`{a,b} ∩ {b,c} = {b}`, but `{b}` is absent. -/
theorem p04Counterexample_not_interClosed :
    ¬ IsInterClosed p04Counterexample := by
  intro hInter
  have hAB : p04AB ∈ p04Counterexample := by native_decide
  have hBC : p04BC ∈ p04Counterexample := by native_decide
  have hMeet := hInter p04AB hAB p04BC hBC
  have hEq : p04AB ∩ p04BC = p04B := by native_decide
  rw [hEq] at hMeet
  have hNot : p04B ∉ p04Counterexample := by native_decide
  exact hNot hMeet

/-- The explicit three-point union-closed family is not an exact D003
functional-preorder complement family. -/
theorem p04Counterexample_not_functionalPreorderRepresentable :
    ¬ IsComplementOfFunctionalPreorderIdealFamily p04Counterexample := by
  intro hRep
  exact p04Counterexample_not_interClosed
    (complementOfFunctionalPreorderIdealFamily_latticeClosed hRep).2

/-- The proposed universal exact-representation subroute to UC-P04 is false. -/
theorem p04_no_universal_exact_functionalPreorder_representation :
    ¬ (∀ G : Family Chain3,
        IsUnionClosed G →
          IsComplementOfFunctionalPreorderIdealFamily G) := by
  intro hUniversal
  exact p04Counterexample_not_functionalPreorderRepresentable
    (hUniversal p04Counterexample p04Counterexample_unionClosed)

end MathSolve.UnionClosed.WP08
