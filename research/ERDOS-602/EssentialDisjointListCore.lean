import Init.Data.List.Lemmas

/-!
Erdos #602: a kernel-checkable, Mathlib-independent finitary core.
This does not prove the unrestricted Property B question.
An abstract binary relation orients each intersecting pair; every vertex
has a finite list of incoming intersection neighbours, and each pair
intersection is contained in a finite list of points.
-/

universe u v
namespace Erdos602ListCore

variable {I : Type u} {X : Type v}

/-- Finitary infinitude without Mathlib: each finite list misses a point. -/
def EscapesEveryList (s : X → Prop) : Prop :=
  ∀ l : List X, ∃ x : X, s x ∧ x ∉ l

/-- Delete the explicitly listed pair-overlap witnesses at each vertex. -/
def residual (A : I → X → Prop) (P : I → List I)
    (W : I → I → List X) (i : I) (x : X) : Prop :=
  A i x ∧ x ∉ (P i).flatMap (fun j => W i j)

/-- Finite-in-neighbour orientations of finite-overlap families admit
pairwise disjoint residuals, each still escaping every finite list.
The relation need not be transitive or well-founded. -/
theorem essentialDisjoint_of_finiteInNeighbours
    (A : I → X → Prop) (P : I → List I)
    (W : I → I → List X) (R : I → I → Prop)
    (hinf : ∀ i, EscapesEveryList (A i))
    (horient : ∀ i j, i ≠ j → R i j ∨ R j i)
    (hprev : ∀ i j x, R i j → A i x → A j x → i ∈ P j)
    (hfinite : ∀ i j x, i ≠ j → A i x → A j x → x ∈ W i j) :
    (∀ i, EscapesEveryList (residual A P W i)) ∧
      (∀ i j, i ≠ j → ∀ x, ¬ (residual A P W i x ∧ residual A P W j x)) := by
  constructor
  · intro i l
    obtain ⟨x, hx, hxnot⟩ := hinf i (l ++ (P i).flatMap (fun j => W i j))
    refine ⟨x, ⟨hx, ?_⟩, ?_⟩
    · intro hforbidden
      exact hxnot (List.mem_append.mpr (Or.inr hforbidden))
    · intro hl
      exact hxnot (List.mem_append.mpr (Or.inl hl))
  · intro i j hij x hboth
    rcases hboth with ⟨⟨hAi, hnoti⟩, ⟨hAj, hnotj⟩⟩
    rcases horient i j hij with hijR | hjiR
    · apply hnotj
      apply List.mem_flatMap_of_mem (hprev i j x hijR hAi hAj)
      exact hfinite j i x (Ne.symm hij) hAj hAi
    · apply hnoti
      apply List.mem_flatMap_of_mem (hprev j i x hjiR hAj hAi)
      exact hfinite i j x hij hAi hAj

#print axioms essentialDisjoint_of_finiteInNeighbours
/-- Same predicate shape as the pinned formal-conjectures provider. -/
def IsMonochromatic (f : X → Fin 2) (s : X → Prop) : Prop :=
  ∀ x, s x → ∀ y, s y → f x = f y

/-- A point outside every finite list can be paired with a distinct point. -/
private theorem twoPoints (s : X → Prop) (h : EscapesEveryList s) :
    ∃ a b, s a ∧ s b ∧ a ≠ b := by
  obtain ⟨a, ha, _⟩ := h []
  obtain ⟨b, hb, hnot⟩ := h [a]
  refine ⟨a, b, ha, hb, ?_⟩
  intro heq
  apply hnot
  subst b
  simp

/-- Pairwise disjoint lists-infinite sets admit a nonmonochromatic colouring. -/
theorem propertyB_of_disjoint_residual
    (A : I → X → Prop)
    (hinf : ∀ i, EscapesEveryList (A i))
    (hdisj : ∀ i j, i ≠ j → ∀ x, ¬ (A i x ∧ A j x)) :
    ∃ f : X → Fin 2, ∀ i, ¬ IsMonochromatic f (A i) := by
  classical
  have htwo : ∀ i, ∃ p : X × X,
      A i p.1 ∧ A i p.2 ∧ p.1 ≠ p.2 := by
    intro i
    obtain ⟨a, b, ha, hb, hab⟩ := twoPoints (A i) (hinf i)
    exact ⟨(a, b), ha, hb, hab⟩
  let pair : I → X × X := fun i => Classical.choose (htwo i)
  have ha (i : I) : A i (pair i).1 := (Classical.choose_spec (htwo i)).1
  have hb (i : I) : A i (pair i).2 := (Classical.choose_spec (htwo i)).2.1
  have hab (i : I) : (pair i).1 ≠ (pair i).2 :=
    (Classical.choose_spec (htwo i)).2.2
  let f : X → Fin 2 := fun x => if ∃ i, x = (pair i).2 then 1 else 0
  refine ⟨f, fun i hmono => ?_⟩
  have hfa : f (pair i).1 = 0 := by
    simp only [f]
    split
    · rename_i hw
      obtain ⟨j, hij⟩ := hw
      by_cases heq : i = j
      · subst j
        exact False.elim ((hab i) hij)
      · exact False.elim (hdisj i j heq (pair i).1
          ⟨ha i, hij ▸ hb j⟩)
    · rfl
  have hfb : f (pair i).2 = 1 := by
    simp only [f]
    split
    · rfl
    · rename_i hnot
      exact False.elim (hnot ⟨i, rfl⟩)
  have eqcolors := hmono (pair i).1 (ha i) (pair i).2 (hb i)
  rw [hfa, hfb] at eqcolors
  exact absurd eqcolors (by decide)

/-- Full bounded Property B theorem. The no-singleton overlap condition is
not needed. Finite incoming overlaps and finite pairwise intersections are
witnessed by lists and therefore avoid any Mathlib dependency. -/
theorem propertyB_of_finiteInNeighbours
    (A : I → X → Prop) (P : I → List I)
    (W : I → I → List X) (R : I → I → Prop)
    (hinf : ∀ i, EscapesEveryList (A i))
    (horient : ∀ i j, i ≠ j → R i j ∨ R j i)
    (hprev : ∀ i j x, R i j → A i x → A j x → i ∈ P j)
    (hfinite : ∀ i j x, i ≠ j → A i x → A j x → x ∈ W i j) :
    ∃ f : X → Fin 2, ∀ i, ¬ IsMonochromatic f (A i) := by
  obtain ⟨hinfB, hdisjB⟩ :=
    essentialDisjoint_of_finiteInNeighbours A P W R hinf horient hprev hfinite
  obtain ⟨f, hf⟩ := propertyB_of_disjoint_residual
    (residual A P W) hinfB hdisjB
  refine ⟨f, fun i hmono => hf i ?_⟩
  intro x hx y hy
  exact hmono x hx.1 y hy.1

#print axioms propertyB_of_finiteInNeighbours
end Erdos602ListCore
