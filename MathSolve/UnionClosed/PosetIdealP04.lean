import MathSolve.UnionClosed.FunctionalPreorderP04
import Mathlib.Order.Preorder.Finite
import Mathlib.Tactic

/-!
# UC-001 / WP08-D002: arbitrary finite poset ideal extension

WP07 obtains a Frankl-facing theorem from the stronger average-rarity theorem
for order ideals of functional preorders.  This module removes the functional
self-map restriction at the level actually needed by the complement endgame.

For any nonempty finite carrier in a partial order, choose a maximal carrier
element `m`.  Erasing `m` maps every order ideal containing `m` injectively
to an order ideal omitting `m`.  Therefore at most half of all order ideals
contain `m`.  Carrier-relative complementation turns that rare maximal element
into an abundant element of the corresponding family of upper sets.

This proves a genuine extension of the WP07 half-frequency conclusion.  It does
not claim that the stronger WP07 average-rarity inequality extends to arbitrary
finite posets, and it still does not represent arbitrary finite closure systems.
-/

namespace MathSolve.UnionClosed.WP08

open Finset

universe u

variable {α : Type u} [DecidableEq α] [PartialOrder α]

/-- A downward order ideal of the ambient partial order, restricted to the
explicit finite carrier `U`. -/
def IsPosetIdealOn (U I : Finset α) : Prop :=
  I ⊆ U ∧
    ∀ ⦃x⦄, x ∈ I → ∀ ⦃y⦄, y ∈ U → y ≤ x → y ∈ I

/-- The finite family of all downward order ideals on `U`. -/
noncomputable def posetIdealFamily (U : Finset α) : Family α := by
  classical
  exact U.powerset.filter (fun I => IsPosetIdealOn U I)

/-- Membership in the explicit family is exactly the local order-ideal
predicate. -/
@[simp] theorem mem_posetIdealFamily_iff
    {U I : Finset α} :
    I ∈ posetIdealFamily U ↔ IsPosetIdealOn U I := by
  classical
  simp only [posetIdealFamily, Finset.mem_filter, Finset.mem_powerset]
  constructor
  · exact fun h => h.2
  · intro h
    exact ⟨h.1, h⟩

/-- Every member of the poset-ideal family lies in its explicit carrier. -/
theorem posetIdealFamily_members_subset
    {U : Finset α} :
    ∀ I ∈ posetIdealFamily U, I ⊆ U := by
  intro I hI
  exact (mem_posetIdealFamily_iff.mp hI).1

/-- The empty set is always an order ideal. -/
theorem posetIdealFamily_empty_mem
    {U : Finset α} :
    (∅ : Finset α) ∈ posetIdealFamily U := by
  rw [mem_posetIdealFamily_iff]
  constructor
  · simp
  · intro x hx
    simp at hx

/-- The full carrier is always an order ideal. -/
theorem posetIdealFamily_ground_mem
    {U : Finset α} :
    U ∈ posetIdealFamily U := by
  rw [mem_posetIdealFamily_iff]
  exact ⟨Finset.Subset.rfl, by
    intro x hx y hy hle
    exact hy⟩

/-- Arbitrary finite-poset order ideals are closed under intersection. -/
theorem posetIdealFamily_interClosed
    {U : Finset α} :
    IsInterClosed (posetIdealFamily U) := by
  intro A hA B hB
  rw [mem_posetIdealFamily_iff] at hA hB ⊢
  constructor
  · intro x hx
    exact hA.1 (Finset.mem_inter.mp hx).1
  · intro x hx y hy hle
    have hxA : x ∈ A := (Finset.mem_inter.mp hx).1
    have hxB : x ∈ B := (Finset.mem_inter.mp hx).2
    exact Finset.mem_inter.mpr ⟨hA.2 hxA hy hle, hB.2 hxB hy hle⟩

/-- Arbitrary finite-poset order ideals are also closed under union. -/
theorem posetIdealFamily_unionClosed
    {U : Finset α} :
    IsUnionClosed (posetIdealFamily U) := by
  intro A hA B hB
  rw [mem_posetIdealFamily_iff] at hA hB ⊢
  constructor
  · intro x hx
    rcases Finset.mem_union.mp hx with hxA | hxB
    · exact hA.1 hxA
    · exact hB.1 hxB
  · intro x hx y hy hle
    rcases Finset.mem_union.mp hx with hxA | hxB
    · exact Finset.mem_union.mpr (Or.inl (hA.2 hxA hy hle))
    · exact Finset.mem_union.mpr (Or.inr (hB.2 hxB hy hle))

/-- Removing a maximal carrier element from an order ideal leaves an order
ideal.  Maximality is exactly what prevents downward closure from requiring the
removed element back. -/
theorem erase_maximal_isPosetIdealOn
    {U I : Finset α} {m : α}
    (hm : Maximal (fun x => x ∈ U) m)
    (hI : IsPosetIdealOn U I) :
    IsPosetIdealOn U (I.erase m) := by
  constructor
  · intro x hx
    exact hI.1 (Finset.mem_of_mem_erase hx)
  · intro x hx y hyU hyx
    have hxI : x ∈ I := Finset.mem_of_mem_erase hx
    have hxne : x ≠ m := (Finset.mem_erase.mp hx).1
    have hyI : y ∈ I := hI.2 hxI hyU hyx
    have hyne : y ≠ m := by
      intro hym
      subst y
      have hxU : x ∈ U := hI.1 hxI
      have hxm : x ≤ m := hm.2 hxU hyx
      exact hxne (le_antisymm hxm hyx)
    exact Finset.mem_erase.mpr ⟨hyne, hyI⟩

/-- Family-level form of maximal-element erasure. -/
theorem erase_maximal_mem_posetIdealFamily
    {U I : Finset α} {m : α}
    (hm : Maximal (fun x => x ∈ U) m)
    (hI : I ∈ posetIdealFamily U) :
    I.erase m ∈ posetIdealFamily U := by
  rw [mem_posetIdealFamily_iff] at hI ⊢
  exact erase_maximal_isPosetIdealOn hm hI

/-- Erasure of a fixed element is injective on finite sets that contain that
element. -/
theorem erase_injective_on_containing
    {F : Family α} {m : α} :
    Set.InjOn (fun I : Finset α => I.erase m)
      ↑(F.filter (fun I => m ∈ I)) := by
  intro A hA B hB hEq
  have hmA : m ∈ A := (Finset.mem_filter.mp hA).2
  have hmB : m ∈ B := (Finset.mem_filter.mp hB).2
  ext x
  by_cases hxm : x = m
  · subst x
    simp [hmA, hmB]
  · have hxEq : x ∈ A.erase m ↔ x ∈ B.erase m := by
      rw [hEq]
    simpa [hxm] using hxEq

/-- Every nonempty finite poset-ideal family has a rare carrier element.  A
maximal carrier element occurs in at most half of all order ideals. -/
theorem posetIdealFamily_exists_rare
    {U : Finset α}
    (hU : U.Nonempty) :
    ∃ m ∈ U,
      2 * freq (posetIdealFamily U) m ≤ (posetIdealFamily U).card := by
  classical
  obtain ⟨m, hm⟩ := U.exists_maximal hU
  refine ⟨m, hm.1, ?_⟩

  let C : Family α :=
    (posetIdealFamily U).filter (fun I => m ∈ I)
  let E : Family α :=
    C.image (fun I => I.erase m)

  have hinj : Set.InjOn (fun I : Finset α => I.erase m) ↑C := by
    simpa [C] using
      (erase_injective_on_containing
        (F := posetIdealFamily U) (m := m))

  have hcardE : E.card = C.card := by
    dsimp [E]
    exact Finset.card_image_iff.mpr hinj

  have hCsub : C ⊆ posetIdealFamily U := by
    intro I hI
    change I ∈ (posetIdealFamily U).filter (fun J => m ∈ J) at hI
    exact (Finset.mem_filter.mp hI).1

  have hEsub : E ⊆ posetIdealFamily U := by
    intro I hI
    change I ∈ C.image (fun J => J.erase m) at hI
    rcases Finset.mem_image.mp hI with ⟨J, hJC, rfl⟩
    have hJF : J ∈ posetIdealFamily U := hCsub hJC
    exact erase_maximal_mem_posetIdealFamily hm hJF

  have hdisj : Disjoint C E := by
    refine Finset.disjoint_left.mpr ?_
    intro I hIC hIE
    change I ∈ C.image (fun J => J.erase m) at hIE
    rcases Finset.mem_image.mp hIE with ⟨J, hJC, hJI⟩
    have hmI : m ∈ I := by
      change I ∈ (posetIdealFamily U).filter (fun J => m ∈ J) at hIC
      exact (Finset.mem_filter.mp hIC).2
    rw [← hJI] at hmI
    simpa using hmI

  have hUnionSub : C ∪ E ⊆ posetIdealFamily U := by
    intro I hI
    rcases Finset.mem_union.mp hI with hIC | hIE
    · exact hCsub hIC
    · exact hEsub hIE

  have hcardUnion : (C ∪ E).card = C.card + E.card :=
    Finset.card_union_of_disjoint hdisj

  have hle : (C ∪ E).card ≤ (posetIdealFamily U).card :=
    Finset.card_le_card hUnionSub

  unfold freq
  change 2 * C.card ≤ (posetIdealFamily U).card
  calc
    2 * C.card = C.card + C.card := by omega
    _ = C.card + E.card := by rw [hcardE]
    _ = (C ∪ E).card := hcardUnion.symm
    _ ≤ (posetIdealFamily U).card := hle

/-- Complements of all finite-poset order ideals are union-closed. -/
theorem posetIdeal_complement_unionClosed
    {U : Finset α} :
    IsUnionClosed (complementFamilyOn (posetIdealFamily U) U) :=
  complementFamilyOn_unionClosed_of_interClosed posetIdealFamily_interClosed

/-- WP08-D002 Frankl-facing extension: complements of all order ideals of any
nonempty finite partial order satisfy the half-frequency conclusion. -/
theorem posetIdeal_complement_frankl
    {U : Finset α}
    (hU : U.Nonempty) :
    IsUnionClosed (complementFamilyOn (posetIdealFamily U) U) ∧
      IsNontrivial (complementFamilyOn (posetIdealFamily U) U) ∧
      IsFranklAbundant (complementFamilyOn (posetIdealFamily U) U) := by
  have hrare := posetIdealFamily_exists_rare (U := U) hU
  have hAbundant :
      IsFranklAbundant (complementFamilyOn (posetIdealFamily U) U) :=
    complementFamilyOn_abundant_of_exists_rare
      (F := posetIdealFamily U) (U := U)
      posetIdealFamily_members_subset
      posetIdealFamily_empty_mem
      hrare
  refine ⟨posetIdeal_complement_unionClosed, ?_, hAbundant⟩
  rcases hAbundant with ⟨x, hx, _⟩
  exact ⟨x, hx⟩

end MathSolve.UnionClosed.WP08
