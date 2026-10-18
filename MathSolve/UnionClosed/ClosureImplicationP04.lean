import MathSolve.UnionClosed.PosetIdealP04
import Mathlib.Data.Finset.Lattice.Fold
import Mathlib.Tactic

/-!
# UC-001 / WP08-D003: closure operators and finite implication normal form

This module crosses the next structural boundary after the finite-poset result.

For an arbitrary finite closure system on an explicit carrier `U`, it defines
the canonical closure operator as the intersection of all closed supersets.
It proves extensivity, monotonicity, idempotence, exact recovery of closed
members as fixed points, and an exact finite implication-basis representation.

It then isolates the first genuinely non-poset mechanism on three points:
the single binary implication `{a,b} -> c`.  Its model family is a closure
system but is not union-closed, so it cannot arise from any finite basis of
unary implications.  Erasing the forced conclusion `c` from the full closed
set also leaves the closure system, showing exactly why the D002
maximal-element erasure argument does not transfer verbatim.

The example still has a rare element and therefore its carrier-relative
complement satisfies the Frankl-facing conclusion.  No universal closure-system
rare-element theorem is claimed.
-/

namespace MathSolve.UnionClosed.WP08

open Finset
open MathSolve.UnionClosed.WP07

universe u

variable {α : Type u} [DecidableEq α]

/-- The canonical closure of `A`: the carrier elements lying in every closed
member of `F` that contains `A`. -/
noncomputable def closureOf
    (F : Family α) (U A : Finset α) : Finset α := by
  classical
  exact U.filter fun x =>
    ∀ C ∈ F, A ⊆ C → x ∈ C

@[simp] theorem mem_closureOf_iff
    {F : Family α} {U A : Finset α} {x : α} :
    x ∈ closureOf F U A ↔
      x ∈ U ∧ ∀ C ∈ F, A ⊆ C → x ∈ C := by
  classical
  simp [closureOf]

/-- The canonical closure always lies in its explicit carrier. -/
theorem closureOf_subset
    {F : Family α} {U A : Finset α} :
    closureOf F U A ⊆ U := by
  intro x hx
  exact (mem_closureOf_iff.mp hx).1

/-- Closure is extensive for subsets of the carrier. -/
theorem subset_closureOf
    {F : Family α} {U A : Finset α}
    (hA : A ⊆ U) :
    A ⊆ closureOf F U A := by
  intro x hxA
  rw [mem_closureOf_iff]
  refine ⟨hA hxA, ?_⟩
  intro C hC hAC
  exact hAC hxA

/-- Closure is monotone in its argument. -/
theorem closureOf_mono
    {F : Family α} {U A B : Finset α}
    (hAB : A ⊆ B) :
    closureOf F U A ⊆ closureOf F U B := by
  intro x hx
  rw [mem_closureOf_iff] at hx ⊢
  refine ⟨hx.1, ?_⟩
  intro C hC hBC
  exact hx.2 C hC (hAB.trans hBC)

/-- The canonical closure is idempotent on subsets of the carrier. -/
theorem closureOf_idempotent
    {F : Family α} {U A : Finset α}
    (hA : A ⊆ U) :
    closureOf F U (closureOf F U A) = closureOf F U A := by
  apply Finset.Subset.antisymm
  · intro x hx
    rw [mem_closureOf_iff] at hx ⊢
    refine ⟨hx.1, ?_⟩
    intro C hC hAC
    have hClosureC : closureOf F U A ⊆ C := by
      intro y hy
      exact (mem_closureOf_iff.mp hy).2 C hC hAC
    exact hx.2 C hC hClosureC
  · exact subset_closureOf closureOf_subset

/-- In a finite closure system, the canonical closure of a carried set is
itself a closed member. -/
theorem closureOf_mem_of_closureSystem
    {F : Family α} {U A : Finset α}
    (h : IsClosureSystemOn F U)
    (hA : A ⊆ U) :
    closureOf F U A ∈ F := by
  classical
  let C : Family α := F.filter (fun S => A ⊆ S)
  have hUC : U ∈ C := by
    change U ∈ F.filter (fun S => A ⊆ S)
    exact Finset.mem_filter.mpr ⟨h.2.1, hA⟩
  have hC : C.Nonempty := ⟨U, hUC⟩
  have hCinF : ∀ S ∈ C, S ∈ F := by
    intro S hS
    exact (Finset.mem_filter.mp hS).1
  have hInfMem : C.inf' hC id ∈ F := by
    exact Finset.inf'_mem
      (↑F : Set (Finset α))
      (by
        intro X hX Y hY
        exact h.2.2 X hX Y hY)
      C hC id hCinF
  have hEq : closureOf F U A = C.inf' hC id := by
    apply Finset.Subset.antisymm
    · refine (Finset.le_inf'_iff hC id).2 ?_
      intro S hSC x hx
      have hxClosure := (mem_closureOf_iff.mp hx).2
      have hSF : S ∈ F := (Finset.mem_filter.mp hSC).1
      have hAS : A ⊆ S := (Finset.mem_filter.mp hSC).2
      exact hxClosure S hSF hAS
    · intro x hx
      rw [mem_closureOf_iff]
      constructor
      · exact (Finset.inf'_le id hUC) hx
      · intro S hSF hAS
        have hSC : S ∈ C := by
          change S ∈ F.filter (fun T => A ⊆ T)
          exact Finset.mem_filter.mpr ⟨hSF, hAS⟩
        exact (Finset.inf'_le id hSC) hx
  rw [hEq]
  exact hInfMem

/-- Closed members are exactly fixed points of the canonical closure operator. -/
theorem mem_iff_closureOf_eq
    {F : Family α} {U A : Finset α}
    (h : IsClosureSystemOn F U)
    (hA : A ⊆ U) :
    A ∈ F ↔ closureOf F U A = A := by
  constructor
  · intro hAF
    apply Finset.Subset.antisymm
    · intro x hx
      exact (mem_closureOf_iff.mp hx).2 A hAF Finset.Subset.rfl
    · exact subset_closureOf hA
  · intro hEq
    have hClosed := closureOf_mem_of_closureSystem h hA
    rwa [hEq] at hClosed

/-- A finite implication `P -> q`: whenever all premises in `P` are present,
the conclusion `q` is present. -/
abbrev Implication (α : Type u) := Finset α × α

/-- A set models every implication in a finite basis. -/
def ModelsImplicationBasis
    (B : Finset (Implication α)) (S : Finset α) : Prop :=
  ∀ imp ∈ B, imp.1 ⊆ S → imp.2 ∈ S

/-- The canonical finite implication basis of a carried family: all implications
over `U` valid in every member of `F`. -/
noncomputable def canonicalImplicationBasis
    (F : Family α) (U : Finset α) : Finset (Implication α) := by
  classical
  exact (U.powerset.product U).filter fun imp =>
    ∀ C ∈ F, imp.1 ⊆ C → imp.2 ∈ C

@[simp] theorem mem_canonicalImplicationBasis_iff
    {F : Family α} {U P : Finset α} {q : α} :
    (P, q) ∈ canonicalImplicationBasis F U ↔
      P ⊆ U ∧ q ∈ U ∧
        ∀ C ∈ F, P ⊆ C → q ∈ C := by
  classical
  simp [canonicalImplicationBasis, and_assoc]

/-- Every finite closure system is represented exactly by its finite canonical
implication basis. -/
theorem closureSystem_mem_iff_models_canonicalBasis
    {F : Family α} {U S : Finset α}
    (h : IsClosureSystemOn F U) :
    S ∈ F ↔
      S ⊆ U ∧ ModelsImplicationBasis (canonicalImplicationBasis F U) S := by
  constructor
  · intro hSF
    refine ⟨h.1 S hSF, ?_⟩
    intro imp himp hPrem
    rcases imp with ⟨P, q⟩
    have hv := (mem_canonicalImplicationBasis_iff.mp himp).2.2
    exact hv S hSF hPrem
  · rintro ⟨hSU, hModels⟩
    have hEq : closureOf F U S = S := by
      apply Finset.Subset.antisymm
      · intro x hx
        have hxU : x ∈ U := (mem_closureOf_iff.mp hx).1
        have hImp : (S, x) ∈ canonicalImplicationBasis F U := by
          rw [mem_canonicalImplicationBasis_iff]
          refine ⟨hSU, hxU, ?_⟩
          intro C hCF hSC
          exact (mem_closureOf_iff.mp hx).2 C hCF hSC
        exact hModels (S, x) hImp Finset.Subset.rfl
      · exact subset_closureOf hSU
    exact (mem_iff_closureOf_eq h hSU).2 hEq

/-! ## Unary implication systems -/

/-- Models of a finite unary implication basis on an explicit carrier. -/
noncomputable def unaryModelFamilyOn
    (U : Finset α) (B : Finset (α × α)) : Family α := by
  classical
  exact U.powerset.filter fun S =>
    ∀ imp ∈ B, imp.1 ∈ S → imp.2 ∈ S

@[simp] theorem mem_unaryModelFamilyOn_iff
    {U S : Finset α} {B : Finset (α × α)} :
    S ∈ unaryModelFamilyOn U B ↔
      S ⊆ U ∧ ∀ imp ∈ B, imp.1 ∈ S → imp.2 ∈ S := by
  classical
  simp [unaryModelFamilyOn]

/-- Model families of unary implications are union-closed. -/
theorem unaryModelFamilyOn_unionClosed
    {U : Finset α} {B : Finset (α × α)} :
    IsUnionClosed (unaryModelFamilyOn U B) := by
  classical
  intro A hA C hC
  rw [mem_unaryModelFamilyOn_iff] at hA hC ⊢
  constructor
  · exact Finset.union_subset hA.1 hC.1
  · intro imp himp hx
    rcases Finset.mem_union.mp hx with hxA | hxC
    · exact Finset.mem_union.mpr (Or.inl (hA.2 imp himp hxA))
    · exact Finset.mem_union.mpr (Or.inr (hC.2 imp himp hxC))

/-- Exact representation by some finite basis of unary implications. -/
def IsUnaryImplicationRepresentableOn
    (F : Family α) (U : Finset α) : Prop :=
  ∃ B : Finset (α × α), F = unaryModelFamilyOn U B

/-- Any family represented by unary implications is union-closed. -/
theorem unaryImplicationRepresentable_unionClosed
    {F : Family α} {U : Finset α}
    (h : IsUnaryImplicationRepresentableOn F U) :
    IsUnionClosed F := by
  rcases h with ⟨B, rfl⟩
  exact unaryModelFamilyOn_unionClosed

/-! ## First genuinely non-unary closure mechanism -/

abbrev d003A : Finset Chain3 := {Chain3.a}
abbrev d003B : Finset Chain3 := {Chain3.b}
abbrev d003C : Finset Chain3 := {Chain3.c}
abbrev d003AC : Finset Chain3 := {Chain3.a, Chain3.c}
abbrev d003BC : Finset Chain3 := {Chain3.b, Chain3.c}

/-- Models of the single binary implication `{a,b} -> c`.  Equivalently this
is every subset of the three-point carrier except `{a,b}`. -/
abbrev binaryImplicationClosure : Family Chain3 :=
  {∅, d003A, d003B, d003C, d003AC, d003BC, Chain3.ground}

/-- Exact semantic characterization by one binary implication. -/
theorem binaryImplicationClosure_characterization :
    ∀ S : Finset Chain3,
      S ∈ binaryImplicationClosure ↔
        S ⊆ Chain3.ground ∧
          (p04AB ⊆ S → Chain3.c ∈ S) := by
  native_decide

/-- The one-binary-implication family is a finite closure system. -/
theorem binaryImplicationClosure_isClosureSystem :
    IsClosureSystemOn binaryImplicationClosure Chain3.ground := by
  constructor
  · intro S hS
    exact (binaryImplicationClosure_characterization S).mp hS |>.1
  · constructor
    · native_decide
    · intro A hA B hB
      rw [binaryImplicationClosure_characterization] at hA hB ⊢
      constructor
      · exact Finset.inter_subset_left.trans hA.1
      · intro hPrem
        have hPremA : p04AB ⊆ A :=
          hPrem.trans Finset.inter_subset_left
        have hPremB : p04AB ⊆ B :=
          hPrem.trans Finset.inter_subset_right
        exact Finset.mem_inter.mpr ⟨hA.2 hPremA, hB.2 hPremB⟩

/-- It is not union-closed: `{a}` and `{b}` are closed but `{a,b}` is not. -/
theorem binaryImplicationClosure_not_unionClosed :
    ¬ IsUnionClosed binaryImplicationClosure := by
  intro hUnion
  have hA : d003A ∈ binaryImplicationClosure := by native_decide
  have hB : d003B ∈ binaryImplicationClosure := by native_decide
  have hAB := hUnion d003A hA d003B hB
  have hUnionEq : d003A ∪ d003B = p04AB := by native_decide
  rw [hUnionEq] at hAB
  have hNot : p04AB ∉ binaryImplicationClosure := by native_decide
  exact hNot hAB

/-- Therefore this closure system cannot be represented by any finite unary
implication basis. -/
theorem binaryImplicationClosure_not_unaryRepresentable :
    ¬ IsUnaryImplicationRepresentableOn
      binaryImplicationClosure Chain3.ground := by
  intro hRep
  exact binaryImplicationClosure_not_unionClosed
    (unaryImplicationRepresentable_unionClosed hRep)

/-- The D002 erasure mechanism fails verbatim at the forced conclusion:
erasing `c` from the full closed set produces the forbidden premise
`{a,b}`. -/
theorem binaryImplicationClosure_forcedConclusion_erasure_fails :
    Chain3.ground ∈ binaryImplicationClosure ∧
      Chain3.ground.erase Chain3.c = p04AB ∧
      p04AB ∉ binaryImplicationClosure := by
  native_decide

/-- The minimal binary extension still has a rare carrier element. -/
theorem binaryImplicationClosure_exists_rare :
    ∃ x ∈ Chain3.ground,
      2 * freq binaryImplicationClosure x ≤ binaryImplicationClosure.card := by
  refine ⟨Chain3.a, ?_, ?_⟩ <;> native_decide

/-- Consequently the complement of this first genuinely non-unary closure
system still satisfies the restricted Frankl-facing conclusion. -/
theorem binaryImplicationClosure_complement_frankl :
    IsUnionClosed
        (complementFamilyOn binaryImplicationClosure Chain3.ground) ∧
      IsNontrivial
        (complementFamilyOn binaryImplicationClosure Chain3.ground) ∧
      IsFranklAbundant
        (complementFamilyOn binaryImplicationClosure Chain3.ground) := by
  have hClosure := binaryImplicationClosure_isClosureSystem
  have hEmpty : (∅ : Finset Chain3) ∈ binaryImplicationClosure := by
    native_decide
  have hAbundant :
      IsFranklAbundant
        (complementFamilyOn binaryImplicationClosure Chain3.ground) :=
    complementFamilyOn_abundant_of_exists_rare
      hClosure.1 hEmpty binaryImplicationClosure_exists_rare
  refine ⟨
    complementFamilyOn_unionClosed_of_interClosed hClosure.2.2,
    ?_,
    hAbundant
  ⟩
  rcases hAbundant with ⟨x, hx, _⟩
  exact ⟨x, hx⟩

end MathSolve.UnionClosed.WP08
