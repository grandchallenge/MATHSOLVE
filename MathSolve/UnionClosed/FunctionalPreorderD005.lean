import MathSolve.UnionClosed.FunctionalPreorderD004
import Mathlib.Tactic

/-!
# UC-001 WP07 D005: complement duality for functional-preorder ideal families

This module proves the Frankl-facing complement theorem for the exact D003
functional-preorder class. It does not reuse WP06's `IsIdealFamilyOn`
hypothesis. Union closure is derived from intersection closure of preorder order
ideals; abundance is derived from the checked D004 average-rarity theorem by
finite double counting and exact complement-frequency identities.
-/

namespace MathSolve.UnionClosed.WP07

open Finset
open scoped BigOperators

universe u

variable {α : Type u} [DecidableEq α]

/-- Union closure for a finite family. -/
def IsUnionClosed (F : Family α) : Prop :=
  ∀ A ∈ F, ∀ B ∈ F, A ∪ B ∈ F

/-- Support of a finite family. -/
def support (F : Family α) : Finset α :=
  F.biUnion id

/-- Nontriviality for the Frankl-facing statement: nonempty support. -/
def IsNontrivial (F : Family α) : Prop :=
  (support F).Nonempty

/-- Frequency of an element in a finite family. -/
def freq (F : Family α) (x : α) : Nat :=
  (F.filter (fun A => x ∈ A)).card

/-- A family is Frankl-abundant if some supported element occurs in at least
half of its members. -/
def IsFranklAbundant (F : Family α) : Prop :=
  ∃ x ∈ support F, 2 * freq F x ≥ F.card

/-- Complement every member of `F` inside the fixed carrier `U`. -/
def complementFamilyOn (F : Family α) (U : Finset α) : Family α :=
  F.image fun S => U \ S

/-- Average abundance over a chosen carrier, stated over integers to keep
complement-cardinality arithmetic exact. -/
def IsAverageAbundantOn (F : Family α) (U : Finset α) : Prop :=
  (U.card : ℤ) * (F.card : ℤ) ≤
    (2 : ℤ) * (((F.sum fun S => S.card) : Nat) : ℤ)

/-- Support membership has the expected witness form. -/
theorem mem_support_iff (F : Family α) (x : α) :
    x ∈ support F ↔ ∃ S ∈ F, x ∈ S := by
  simp [support]

/-- The exact D003 class has a nonempty carrier. -/
theorem functionalPreorderIdealFamily_ground_nonempty
    {F : Family α} {U : Finset α}
    (h : IsFunctionalPreorderIdealFamilyOn F U) :
    U.Nonempty := by
  rcases h with ⟨S, hU, hF⟩
  rw [← hU]
  rcases S.nonempty with ⟨x⟩
  exact ⟨x.1, x.2⟩

/-- The empty set belongs to every exact D003 functional-preorder ideal family. -/
theorem functionalPreorderIdealFamily_empty_mem
    {F : Family α} {U : Finset α}
    (h : IsFunctionalPreorderIdealFamilyOn F U) :
    (∅ : Finset α) ∈ F := by
  rcases h with ⟨S, hU, hF⟩
  rw [hF, S.mem_idealFamily_iff]
  constructor
  · simp
  · intro x hx
    simp at hx

/-- Functional-preorder order ideals are closed under finite binary
intersection. This is the structural duality fact D005 needs; it is weaker than
and independent of WP06 subset-downward closure. -/
theorem functionalPreorderIdealFamily_inter_closed
    {F : Family α} {U : Finset α}
    (h : IsFunctionalPreorderIdealFamilyOn F U) :
    ∀ A ∈ F, ∀ B ∈ F, A ∩ B ∈ F := by
  rcases h with ⟨S, hU, hF⟩
  subst U
  subst F
  intro A hA B hB
  rw [S.mem_idealFamily_iff] at hA hB ⊢
  constructor
  · intro x hx
    exact hA.1 (Finset.mem_inter.mp hx).1
  · intro x hx y hy hle
    have hxA : x ∈ A := (Finset.mem_inter.mp hx).1
    have hxB : x ∈ B := (Finset.mem_inter.mp hx).2
    exact Finset.mem_inter.mpr ⟨hA.2 hxA hy hle, hB.2 hxB hy hle⟩

/-- If `S ⊆ U`, complementing twice inside `U` returns `S`. -/
theorem sdiff_sdiff_eq_self_of_subset
    {S U : Finset α} (hS : S ⊆ U) :
    U \ (U \ S) = S := by
  ext x
  by_cases hxU : x ∈ U
  · by_cases hxS : x ∈ S
    · simp [hxU, hxS]
    · simp [hxU, hxS]
  · have hxS : x ∉ S := by
      intro hx
      exact hxU (hS hx)
    simp [hxU, hxS]

/-- Complementing inside `U` is injective on subsets of `U`. -/
theorem sdiff_left_inj_of_subset
    {S T U : Finset α} (hS : S ⊆ U) (hT : T ⊆ U)
    (hEq : U \ S = U \ T) :
    S = T := by
  calc
    S = U \ (U \ S) := (sdiff_sdiff_eq_self_of_subset hS).symm
    _ = U \ (U \ T) := by rw [hEq]
    _ = T := sdiff_sdiff_eq_self_of_subset hT

/-- Complementation preserves the number of family members when all members lie
inside the chosen carrier. -/
theorem complementFamilyOn_card
    {F : Family α} {U : Finset α}
    (hsub : ∀ S ∈ F, S ⊆ U) :
    (complementFamilyOn F U).card = F.card := by
  classical
  unfold complementFamilyOn
  exact Finset.card_image_iff.mpr
    (by
      intro S hS T hT hEq
      exact sdiff_left_inj_of_subset (hsub S hS) (hsub T hT) hEq)

/-- Sum of set sizes in the complement family. -/
theorem sum_card_complementFamilyOn
    {F : Family α} {U : Finset α}
    (hsub : ∀ S ∈ F, S ⊆ U) :
    (complementFamilyOn F U).sum (fun S => S.card) =
      F.sum (fun S => U.card - S.card) := by
  classical
  unfold complementFamilyOn
  have hinj : Set.InjOn (fun S : Finset α => U \ S) ↑F := by
    intro S hS T hT hEq
    exact sdiff_left_inj_of_subset (hsub S hS) (hsub T hT) hEq
  calc
    (F.image fun S => U \ S).sum (fun S => S.card)
        = F.sum (fun S => (U \ S).card) := by
          rw [Finset.sum_image hinj]
    _ = F.sum (fun S => U.card - S.card) := by
          refine Finset.sum_congr rfl ?_
          intro S hS
          exact Finset.card_sdiff_of_subset (hsub S hS)

/-- Frequency duality: a carrier element is present in exactly the complements
of original members that omit it. -/
theorem freq_complementFamilyOn
    {F : Family α} {U : Finset α}
    (hsub : ∀ S ∈ F, S ⊆ U) {x : α} (hx : x ∈ U) :
    freq (complementFamilyOn F U) x = F.card - freq F x := by
  classical
  have hfilter :
      (complementFamilyOn F U).filter (fun A => x ∈ A) =
        (F.filter fun S => x ∉ S).image (fun S => U \ S) := by
    apply Finset.ext
    intro A
    constructor
    · intro hA
      have hAImage : A ∈ complementFamilyOn F U :=
        (Finset.mem_filter.mp hA).1
      have hxA : x ∈ A :=
        (Finset.mem_filter.mp hA).2
      rw [complementFamilyOn] at hAImage
      rcases Finset.mem_image.mp hAImage with ⟨S, hS, rfl⟩
      have hxNotS : x ∉ S := (Finset.mem_sdiff.mp hxA).2
      exact Finset.mem_image.mpr
        ⟨S, Finset.mem_filter.mpr ⟨hS, hxNotS⟩, rfl⟩
    · intro hA
      rcases Finset.mem_image.mp hA with ⟨S, hSf, rfl⟩
      have hS : S ∈ F := (Finset.mem_filter.mp hSf).1
      have hxNotS : x ∉ S := (Finset.mem_filter.mp hSf).2
      exact Finset.mem_filter.mpr
        ⟨by
            rw [complementFamilyOn]
            exact Finset.mem_image.mpr ⟨S, hS, rfl⟩,
          Finset.mem_sdiff.mpr ⟨hx, hxNotS⟩⟩
  unfold freq
  rw [hfilter]
  have hinj :
      Set.InjOn (fun S : Finset α => U \ S)
        ↑(F.filter fun S => x ∉ S) := by
    intro S hS T hT hEq
    exact sdiff_left_inj_of_subset
      (hsub S (Finset.mem_filter.mp hS).1)
      (hsub T (Finset.mem_filter.mp hT).1)
      hEq
  rw [Finset.card_image_iff.mpr hinj]
  have hsplit :=
    Finset.card_filter_add_card_filter_not
      (s := F) (p := fun S : Finset α => x ∈ S)
  omega

/-- Incidence double counting: total member size is the sum of element
frequencies over a carrier containing every member. -/
theorem sum_card_eq_sum_freq_on
    {F : Family α} {U : Finset α} (hsub : ∀ S ∈ F, S ⊆ U) :
    F.sum (fun S => S.card) = U.sum (fun x => freq F x) := by
  classical
  let r : Finset α → α → Prop := fun S x => x ∈ S
  have hdc :
      (∑ S ∈ F, (U.bipartiteAbove r S).card) =
        ∑ x ∈ U, (F.bipartiteBelow r x).card :=
    Finset.sum_card_bipartiteAbove_eq_sum_card_bipartiteBelow
      (r := r) (s := F) (t := U)
  calc
    F.sum (fun S => S.card)
        = ∑ S ∈ F, (U.bipartiteAbove r S).card := by
          refine Finset.sum_congr rfl ?_
          intro S hS
          have hEq : U.bipartiteAbove r S = S := by
            apply Finset.ext
            intro x
            constructor
            · intro hx
              exact (Finset.mem_filter.mp hx).2
            · intro hx
              exact Finset.mem_filter.mpr ⟨hsub S hS hx, hx⟩
          rw [hEq]
    _ = ∑ x ∈ U, (F.bipartiteBelow r x).card := hdc
    _ = U.sum (fun x => freq F x) := by
          refine Finset.sum_congr rfl ?_
          intro x hx
          simp [Finset.bipartiteBelow, freq, r]

/-- D004 average rarity guarantees at least one rare carrier element when the
carrier is nonempty. -/
theorem exists_rare_of_averageRare
    {F : Family α} {U : Finset α}
    (hsub : ∀ S ∈ F, S ⊆ U)
    (hU : U.Nonempty)
    (hrare : IsAverageRareOn F U) :
    ∃ x ∈ U, 2 * freq F x ≤ F.card := by
  classical
  rw [IsAverageRareOn, sum_card_eq_sum_freq_on hsub] at hrare
  by_contra hnone
  push_neg at hnone
  have hlt : U.card * F.card < 2 * (U.sum fun x => freq F x) := by
    calc
      U.card * F.card = U.sum (fun _ => F.card) := by
        simp [Finset.sum_const]
      _ < U.sum (fun x => 2 * freq F x) := by
        exact Finset.sum_lt_sum_of_nonempty hU (by
          intro x hx
          exact hnone x hx)
      _ = 2 * (U.sum fun x => freq F x) := by
        rw [Finset.mul_sum]
  omega

/-- The fixed carrier belongs to the complement family when the original family
contains the empty set. -/
theorem ground_mem_complementFamilyOn
    {F : Family α} {U : Finset α}
    (hempty : (∅ : Finset α) ∈ F) :
    U ∈ complementFamilyOn F U := by
  classical
  rw [complementFamilyOn]
  exact Finset.mem_image.mpr ⟨∅, hempty, by simp⟩

/-- The complement of an exact D003 functional-preorder ideal family is
union-closed, by intersection closure of the original order ideals. -/
theorem complementFamilyOn_unionClosed_of_functionalPreorder
    {F : Family α} {U : Finset α}
    (h : IsFunctionalPreorderIdealFamilyOn F U) :
    IsUnionClosed (complementFamilyOn F U) := by
  classical
  intro A hA B hB
  rw [complementFamilyOn] at hA hB
  rcases Finset.mem_image.mp hA with ⟨S, hS, rfl⟩
  rcases Finset.mem_image.mp hB with ⟨T, hT, rfl⟩
  have hInter : S ∩ T ∈ F :=
    functionalPreorderIdealFamily_inter_closed h S hS T hT
  rw [complementFamilyOn]
  refine Finset.mem_image.mpr ⟨S ∩ T, hInter, ?_⟩
  ext x
  by_cases hxU : x ∈ U
  · by_cases hxS : x ∈ S
    · by_cases hxT : x ∈ T <;> simp [hxU, hxS, hxT]
    · by_cases hxT : x ∈ T <;> simp [hxU, hxS, hxT]
  · simp [hxU]

/-- Average rarity is exactly average abundance after carrier-relative
complementation. -/
theorem complementFamilyOn_averageAbundant_of_averageRare
    {F : Family α} {U : Finset α}
    (hsub : ∀ S ∈ F, S ⊆ U)
    (hrare : IsAverageRareOn F U) :
    IsAverageAbundantOn (complementFamilyOn F U) U := by
  classical
  let total : ℤ := (U.card : ℤ) * (F.card : ℤ)
  let sizeF : ℤ := (((F.sum fun S => S.card) : Nat) : ℤ)
  have hAvg : (2 : ℤ) * sizeF ≤ total := by
    dsimp [total, sizeF]
    exact_mod_cast hrare
  have hsumZ :
      ((((complementFamilyOn F U).sum fun S => S.card) : Nat) : ℤ) =
        total - sizeF := by
    rw [sum_card_complementFamilyOn hsub]
    dsimp [total, sizeF]
    calc
      (((F.sum fun S => U.card - S.card) : Nat) : ℤ)
          = ∑ S ∈ F, (((U.card - S.card) : Nat) : ℤ) := by
            norm_cast
      _ = ∑ S ∈ F, ((U.card : ℤ) - (S.card : ℤ)) := by
            refine Finset.sum_congr rfl ?_
            intro S hS
            have hcard : S.card ≤ U.card := Finset.card_le_card (hsub S hS)
            rw [Nat.cast_sub hcard]
      _ = (F.card : ℤ) * (U.card : ℤ) -
            ∑ S ∈ F, (S.card : ℤ) := by
            rw [Finset.sum_sub_distrib]
            simp [Finset.sum_const]
      _ = (U.card : ℤ) * (F.card : ℤ) -
            (((F.sum fun S => S.card) : Nat) : ℤ) := by
            norm_cast
            ring_nf
  dsimp [IsAverageAbundantOn]
  rw [complementFamilyOn_card hsub, hsumZ]
  omega

/-- A rare carrier element becomes an abundant supported element after
complementation. -/
theorem complementFamilyOn_abundant_of_exists_rare
    {F : Family α} {U : Finset α}
    (hsub : ∀ S ∈ F, S ⊆ U)
    (hempty : (∅ : Finset α) ∈ F)
    (hrare : ∃ x ∈ U, 2 * freq F x ≤ F.card) :
    IsFranklAbundant (complementFamilyOn F U) := by
  classical
  rcases hrare with ⟨x, hxU, hxRare⟩
  refine ⟨x, ?_, ?_⟩
  · exact (mem_support_iff (complementFamilyOn F U) x).mpr
      ⟨U, ground_mem_complementFamilyOn (F := F) (U := U) hempty, hxU⟩
  · have hfreq_le : freq F x ≤ F.card := by
      unfold freq
      exact Finset.card_le_card (Finset.filter_subset _ _)
    rw [
      freq_complementFamilyOn (F := F) (U := U) hsub hxU,
      complementFamilyOn_card (F := F) (U := U) hsub
    ]
    omega

/-- D005 average-abundance theorem for the exact D003 class. -/
theorem d005_complement_averageAbundant
    {F : Family α} {U : Finset α}
    (h : IsFunctionalPreorderIdealFamilyOn F U) :
    IsAverageAbundantOn (complementFamilyOn F U) U :=
  complementFamilyOn_averageAbundant_of_averageRare
    (functionalPreorderIdealFamily_members_subset h)
    (d004_averageRarity F U h)

/-- D005 Frankl-facing theorem: complements of exact D003 functional-preorder
ideal families are union-closed, nontrivial, and Frankl-abundant. -/
theorem d005_complement_frankl
    {F : Family α} {U : Finset α}
    (h : IsFunctionalPreorderIdealFamilyOn F U) :
    IsUnionClosed (complementFamilyOn F U) ∧
      IsNontrivial (complementFamilyOn F U) ∧
      IsFranklAbundant (complementFamilyOn F U) := by
  classical
  have hsub := functionalPreorderIdealFamily_members_subset h
  have hrare : IsAverageRareOn F U := d004_averageRarity F U h
  have hexists : ∃ x ∈ U, 2 * freq F x ≤ F.card :=
    exists_rare_of_averageRare hsub
      (functionalPreorderIdealFamily_ground_nonempty h) hrare
  have hAbundant : IsFranklAbundant (complementFamilyOn F U) :=
    complementFamilyOn_abundant_of_exists_rare
      hsub (functionalPreorderIdealFamily_empty_mem h) hexists
  refine ⟨complementFamilyOn_unionClosed_of_functionalPreorder h, ?_, hAbundant⟩
  rcases hAbundant with ⟨x, hxSupport, _⟩
  exact ⟨x, hxSupport⟩

/-- Explicit representation predicate for the restricted complement class.
This does not assert that arbitrary union-closed families admit such a
representation. -/
def IsComplementOfFunctionalPreorderIdealFamily (G : Family α) : Prop :=
  ∃ F U, IsFunctionalPreorderIdealFamilyOn F U ∧
    G = complementFamilyOn F U

/-- Any family already represented as the complement of an exact D003 family
inherits the D005 restricted conclusion. -/
theorem complementOfFunctionalPreorderIdealFamily_frankl
    {G : Family α}
    (hG : IsComplementOfFunctionalPreorderIdealFamily G) :
    IsUnionClosed G ∧ IsNontrivial G ∧ IsFranklAbundant G := by
  rcases hG with ⟨F, U, hF, rfl⟩
  exact d005_complement_frankl hF

end MathSolve.UnionClosed.WP07
