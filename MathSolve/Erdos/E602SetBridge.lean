import Mathlib

/-!
Erdos #602: Mathlib finite-overlap bridge. No singleton-intersection
restriction, and no claim about the unrestricted conjecture.
The predicates below match the definition shapes of the pinned Formal
Conjectures provider, but that provider is not imported by MATHSOLVE.
-/

namespace MathSolve.Erdos602

open Set

universe u v

variable {I : Type u} {X : Type v}

def EscapesEveryList (s : Set X) : Prop :=
  ∀ l : List X, ∃ x : X, x ∈ s ∧ x ∉ l

theorem finite_iff_exists_list_cover (s : Set X) :
    s.Finite ↔ ∃ l : List X, ∀ x : X, x ∈ s → x ∈ l := by
  classical
  constructor
  · intro hs
    refine ⟨hs.toFinset.toList, ?_⟩
    intro x hx
    exact Finset.mem_toList.mpr ((hs.mem_toFinset).mpr hx)
  · rintro ⟨l, hl⟩
    apply l.toFinset.finite_toSet.subset
    intro x hx
    exact List.mem_toFinset.mpr (hl x hx)

theorem escapesEveryList_iff_infinite (s : Set X) :
    EscapesEveryList s ↔ s.Infinite := by
  classical
  constructor
  · intro h hs
    obtain ⟨l, hl⟩ := (finite_iff_exists_list_cover s).mp hs
    obtain ⟨x, hx, hnot⟩ := h l
    exact hnot (hl x hx)
  · intro h l
    by_contra hnot
    apply h
    apply (finite_iff_exists_list_cover s).mpr
    refine ⟨l, ?_⟩
    intro x hx
    by_contra hnotx
    exact hnot ⟨x, hx, hnotx⟩

/-- A source-parallel predicate, not an import of upstream source identity. -/
def IsMonochromatic (f : X → Fin 2) (s : Set X) : Prop :=
  ∀ x ∈ s, ∀ y ∈ s, f x = f y

def HasPropertyB (I : Type u) (A : I → Set X) : Prop :=
  ∃ f : X → Fin 2, ∀ i, ¬ IsMonochromatic f (A i)

/-- The diagonal is explicitly excluded from each finite overlap union. -/
def Deleted (A : I → Set X) (P : I → Set I) (i : I) : Set X :=
  ⋃ j ∈ P i \ {i}, A i ∩ A j

def Residual (A : I → Set X) (P : I → Set I) (i : I) : Set X :=
  A i \ Deleted A P i

theorem deleted_finite (A : I → Set X) (P : I → Set I)
    (hP : ∀ i, (P i).Finite)
    (hInter : ∀ i j, i ≠ j → (A i ∩ A j).Finite)
    (i : I) : (Deleted A P i).Finite := by
  classical
  unfold Deleted
  have hP' : (P i \ {i}).Finite := (hP i).subset Set.diff_subset
  apply hP'.biUnion
  intro j hj
  have hij : i ≠ j := by
    intro heq
    exact hj.2 (by simpa [heq])
  exact hInter i j hij

/-- Every intersecting pair has an orientation; incoming overlap partners
belong to a finite set. Directed cycles are permitted. -/
theorem essentialDisjoint_of_finiteIncoming
    (A : I → Set X) (R : I → I → Prop) (P : I → Set I)
    (hInf : ∀ i, (A i).Infinite)
    (hP : ∀ i, (P i).Finite)
    (hInter : ∀ i j, i ≠ j → (A i ∩ A j).Finite)
    (hOrient : ∀ i j, i ≠ j → (A i ∩ A j).Nonempty → R i j ∨ R j i)
    (hPrev : ∀ i j x, R i j → x ∈ A i → x ∈ A j → i ∈ P j) :
    (∀ i, (Residual A P i).Infinite) ∧
      (∀ i j, i ≠ j → ∀ x, ¬ (x ∈ Residual A P i ∧
        x ∈ Residual A P j)) := by
  classical
  constructor
  · intro i
    change (A i \ Deleted A P i).Infinite
    exact (hInf i).diff (deleted_finite A P hP hInter i)
  · intro i j hij x hboth
    rcases hboth with ⟨⟨hxi, hnoti⟩, ⟨hxj, hnotj⟩⟩
    have hintersection : (A i ∩ A j).Nonempty := ⟨x, hxi, hxj⟩
    rcases hOrient i j hij hintersection with hir | hri
    · apply hnotj
      change x ∈ ⋃ k ∈ P j \ {j}, A j ∩ A k
      apply Set.mem_iUnion.mpr
      refine ⟨i, Set.mem_iUnion.mpr ⟨?_, ⟨hxj, hxi⟩⟩⟩
      exact ⟨hPrev i j x hir hxi hxj, by simp [Ne.symm hij]⟩
    · apply hnoti
      change x ∈ ⋃ k ∈ P i \ {i}, A i ∩ A k
      apply Set.mem_iUnion.mpr
      refine ⟨j, Set.mem_iUnion.mpr ⟨?_, ⟨hxi, hxj⟩⟩⟩
      exact ⟨hPrev j i x hri hxj hxi, by simp [hij]⟩

theorem propertyB_of_disjoint_infinite (A : I → Set X)
    (hInf : ∀ i, (A i).Infinite)
    (hDisj : ∀ i j, i ≠ j → ∀ x, ¬ (x ∈ A i ∧ x ∈ A j)) :
    HasPropertyB I A := by
  classical
  have htwo : ∀ i, ∃ a b : X, a ∈ A i ∧ b ∈ A i ∧ a ≠ b := by
    intro i
    obtain ⟨a, ha⟩ := (hInf i).nonempty
    obtain ⟨b, hb⟩ := ((hInf i).diff (Set.finite_singleton a)).nonempty
    have hba : b ≠ a := by
      simpa only [Set.mem_singleton_iff] using hb.2
    exact ⟨a, b, ha, hb.1, hba.symm⟩
  choose a b ha hb hab using htwo
  let f : X → Fin 2 := fun x => if ∃ i, x = b i then 1 else 0
  refine ⟨f, fun i hmono => ?_⟩
  have hkey : ∀ i j, a i ≠ b j := by
    intro i j h
    by_cases hij : i = j
    · subst j
      exact hab i h
    · exact hDisj i j hij (a i) ⟨ha i, h ▸ hb j⟩
  have hfa : f (a i) = 0 := by
    change (if ∃ j, a i = b j then (1 : Fin 2) else 0) = 0
    apply if_neg
    rintro ⟨j, hj⟩
    exact hkey i j hj
  have hfb : f (b i) = 1 := by
    change (if ∃ j, b i = b j then (1 : Fin 2) else 0) = 1
    exact if_pos ⟨i, rfl⟩
  have h : f (a i) = f (b i) := hmono (a i) (ha i) (b i) (hb i)
  rw [hfa, hfb] at h
  exact (by decide : (0 : Fin 2) ≠ 1) h

theorem propertyB_of_finiteIncoming
    (A : I → Set X) (R : I → I → Prop) (P : I → Set I)
    (hInf : ∀ i, (A i).Infinite)
    (hP : ∀ i, (P i).Finite)
    (hInter : ∀ i j, i ≠ j → (A i ∩ A j).Finite)
    (hOrient : ∀ i j, i ≠ j → (A i ∩ A j).Nonempty → R i j ∨ R j i)
    (hPrev : ∀ i j x, R i j → x ∈ A i → x ∈ A j → i ∈ P j) :
    HasPropertyB I A := by
  obtain ⟨hInfR, hDisjR⟩ :=
    essentialDisjoint_of_finiteIncoming A R P hInf hP hInter hOrient hPrev
  obtain ⟨f, hf⟩ := propertyB_of_disjoint_infinite (Residual A P) hInfR hDisjR
  refine ⟨f, fun i hmono => hf i ?_⟩
  intro x hx y hy
  exact hmono x hx.1 y hy.1

#print axioms finite_iff_exists_list_cover
#print axioms escapesEveryList_iff_infinite
#print axioms essentialDisjoint_of_finiteIncoming
#print axioms propertyB_of_finiteIncoming

end MathSolve.Erdos602
