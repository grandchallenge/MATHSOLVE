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
    exact hj.2 (by simp [heq])
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
      exact ⟨hPrev i j x hir hxi hxj, hij⟩
    · apply hnoti
      change x ∈ ⋃ k ∈ P i \ {i}, A i ∩ A k
      apply Set.mem_iUnion.mpr
      refine ⟨j, Set.mem_iUnion.mpr ⟨?_, ⟨hxi, hxj⟩⟩⟩
      exact ⟨hPrev j i x hri hxj hxi, Ne.symm hij⟩

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

/-- A countable index family of infinite sets with finite pairwise
intersections has Property B. The family members need not be countable,
and intersections of cardinality one are permitted.

Choose an injection from the index type into the natural numbers. Every
index then has only finitely many lower-ranked predecessors, which
supplies the finite-incoming orientation needed above. -/
theorem propertyB_of_countableIndex [Countable I]
    (A : I → Set X)
    (hInf : ∀ i, (A i).Infinite)
    (hInter : ∀ i j, i ≠ j → (A i ∩ A j).Finite) :
    HasPropertyB I A := by
  classical
  obtain ⟨rank, hrank⟩ := Countable.exists_injective_nat I
  let P : I → Set I := fun i => rank ⁻¹' Set.Iio (rank i)
  have hP : ∀ i, (P i).Finite := by
    intro i
    exact (Set.finite_Iio (rank i)).preimage hrank.injOn
  have hOrient :
      ∀ i j, i ≠ j → (A i ∩ A j).Nonempty →
        rank i < rank j ∨ rank j < rank i := by
    intro i j hij _
    rcases lt_trichotomy (rank i) (rank j) with hlt | heq | hgt
    · exact Or.inl hlt
    · exact False.elim (hij (hrank heq))
    · exact Or.inr hgt
  have hPrev :
      ∀ i j x, rank i < rank j →
        x ∈ A i → x ∈ A j → i ∈ P j := by
    intro i j _ hij _ _
    exact hij
  exact propertyB_of_finiteIncoming A (fun i j => rank i < rank j)
    P hInf hP hInter hOrient hPrev

/-- The exact *mathematical hypothesis shape* of the pinned upstream
`erdos_602.variants.countable_index` statement (specialized to natural
indices), proved without using the intersection-cardinality restriction.
This uses MATHSOLVE's source-parallel `HasPropertyB` declaration;
the upstream formal-conjectures file is not imported. -/
theorem countable_index_source_parallel
    (A : ℕ → Set X)
    (hMembers : ∀ i, (A i).Countable ∧ (A i).Infinite)
    (hInter : ∀ i j, i ≠ j → (A i ∩ A j).Finite)
    (_hNoSingleton : ∀ i j, i ≠ j →
      Set.ncard (A i ∩ A j) ≠ 1) :
    HasPropertyB ℕ A := by
  exact propertyB_of_countableIndex A (fun i => (hMembers i).2) hInter

#print axioms propertyB_of_countableIndex
#print axioms countable_index_source_parallel

/-- Families partitioned into *countable overlap components* have
Property B, even when the overall index type is uncountable. The
partition label type `C` is completely arbitrary and need not be
countable. There are no overlaps between distinct labels.

The result formalizes the componentwise-ranking part of the locally
countable overlap-graph corollary. Constructing countable components
from countable vertex neighborhoods is a separate obligation. -/
theorem propertyB_of_countableOverlapComponents
    {C : Type*} (A : I → Set X) (part : I → C)
    (hInf : ∀ i, (A i).Infinite)
    (hInter : ∀ i j, i ≠ j → (A i ∩ A j).Finite)
    (hCount : ∀ c, (Set.Countable {i : I | part i = c}))
    (hComponents : ∀ i j, i ≠ j → (A i ∩ A j).Nonempty →
      part i = part j) :
    HasPropertyB I A := by
  classical
  have hrankExists :
      ∀ c : C, ∃ e : I → ℕ,
        Set.InjOn e {i : I | part i = c} := by
    intro c
    exact Set.countable_iff_exists_injOn.mp (hCount c)
  choose code hcode using hrankExists
  let rank (i : I) : ℕ := code (part i) i
  let P (i : I) : Set I :=
    {j | part j = part i ∧ rank j < rank i}
  have hrankInj (i j : I) (hp : part i = part j)
      (heq : rank i = rank j) : i = j := by
    change code (part i) i = code (part j) j at heq
    rw [← hp] at heq
    apply hcode (part i)
    · exact rfl
    · exact hp.symm
    · exact heq
  have hP : ∀ i, (P i).Finite := by
    intro i
    apply Set.Finite.of_injOn (f := code (part i))
      (t := Set.Iio (rank i))
    · intro j hj
      change code (part i) j < rank i
      have hlt : rank j < rank i := hj.2
      simpa only [rank, hj.1] using hlt
    · intro j hj k hk heq
      exact hcode (part i) hj.1 hk.1 heq
    · exact Set.finite_Iio (rank i)
  have hOrient :
      ∀ i j, i ≠ j → (A i ∩ A j).Nonempty →
        (part i = part j ∧ rank i < rank j) ∨
        (part j = part i ∧ rank j < rank i) := by
    intro i j hij hnonempty
    have hp := hComponents i j hij hnonempty
    rcases lt_trichotomy (rank i) (rank j) with hlt | heq | hgt
    · exact Or.inl ⟨hp, hlt⟩
    · exact False.elim (hij (hrankInj i j hp heq))
    · exact Or.inr ⟨hp.symm, hgt⟩
  have hPrev :
      ∀ i j x, (part i = part j ∧ rank i < rank j) →
        x ∈ A i → x ∈ A j → i ∈ P j := by
    intro i j _ hr _ _
    exact hr
  exact propertyB_of_finiteIncoming A
    (fun i j => part i = part j ∧ rank i < rank j)
    P hInf hP hInter hOrient hPrev

#print axioms propertyB_of_countableOverlapComponents

/-- In a graph with countable neighbor sets, each connected component
is countable. The proof enumerates all finite-distance layers from an
arbitrary vertex, not the full ambient vertex type. -/
private theorem simpleGraph_component_countable
    {V : Type*} (G : SimpleGraph V)
    (hLocal : ∀ v, (G.neighborSet v).Countable) :
    ∀ c : G.ConnectedComponent, c.supp.Countable := by
  let layer (u : V) : ℕ → Set V := fun n =>
    Nat.rec ({u} : Set V)
      (fun _ s => ⋃ v ∈ s, G.neighborSet v) n
  have hLayer (u : V) : ∀ n, (layer u n).Countable := by
    intro n
    induction n with
    | zero =>
        change ({u} : Set V).Countable
        exact Set.countable_singleton u
    | succ n ih =>
        change (⋃ v ∈ layer u n, G.neighborSet v).Countable
        exact ih.biUnion (fun v _ => hLocal v)
  have hPathLayer (u v : V) (h : G.Reachable u v) :
      ∃ n, v ∈ layer u n := by
    have hh : Relation.ReflTransGen G.Adj u v :=
      (G.reachable_iff_reflTransGen u v).mp h
    induction hh with
    | refl =>
        refine ⟨0, ?_⟩
        change u ∈ ({u} : Set V)
        exact Set.mem_singleton u
    | tail hprev hadj ih =>
        obtain ⟨n, hn⟩ := ih ((G.reachable_iff_reflTransGen u _).mpr hprev)
        refine ⟨n + 1, ?_⟩
        change _ ∈ ⋃ w ∈ layer u n, G.neighborSet w
        exact Set.mem_iUnion.mpr
          ⟨_, Set.mem_iUnion.mpr ⟨hn, hadj⟩⟩
  have hReachCount (u : V) :
      (Set.Countable {v : V | G.Reachable u v}) := by
    have hall : (⋃ n : ℕ, layer u n).Countable :=
      Set.countable_iUnion (hLayer u)
    apply hall.mono
    intro v hv
    obtain ⟨n, hn⟩ := hPathLayer u v hv
    exact Set.mem_iUnion.mpr ⟨n, hn⟩
  intro c
  induction c using SimpleGraph.ConnectedComponent.ind with
  | _ u =>
      apply (hReachCount u).mono
      intro v hv
      change G.connectedComponentMk v = G.connectedComponentMk u at hv
      exact SimpleGraph.ConnectedComponent.exact hv.symm

/-- Full locally countable overlap-graph theorem from the original
ERDOS-602-ESSENTIAL-DISJOINTNESS-001 handoff. The total index type I
may be uncountable. The only local graph assumption is that each set
meets countably many *other indexed sets*.

Combined with finite distinct pairwise intersections and infinitude,
the family has Property B. Neither the no-singleton condition nor
countability of individual members is required. -/
theorem propertyB_of_locallyCountableOverlaps
    (A : I → Set X)
    (hInf : ∀ i, (A i).Infinite)
    (hInter : ∀ i j, i ≠ j → (A i ∩ A j).Finite)
    (hCount : ∀ i, (Set.Countable
      {j : I | i ≠ j ∧ (A i ∩ A j).Nonempty})) :
    HasPropertyB I A := by
  classical
  let G : SimpleGraph I :=
    { Adj := fun i j => i ≠ j ∧ (A i ∩ A j).Nonempty
      symm := by
        intro i j hij
        exact ⟨hij.1.symm, by simpa only [Set.inter_comm] using hij.2⟩
      loopless := ⟨fun i h => h.1 rfl⟩ }
  have hLocal : ∀ i, (G.neighborSet i).Countable := by
    intro i
    change (Set.Countable
      {j : I | i ≠ j ∧ (A i ∩ A j).Nonempty})
    exact hCount i
  have hCC : ∀ c : G.ConnectedComponent, c.supp.Countable :=
    simpleGraph_component_countable G hLocal
  have hSame :
      ∀ i j, i ≠ j → (A i ∩ A j).Nonempty →
        G.connectedComponentMk i = G.connectedComponentMk j := by
    intro i j hij hn
    exact SimpleGraph.ConnectedComponent.connectedComponentMk_eq_of_adj
      (show G.Adj i j from ⟨hij, hn⟩)
  exact propertyB_of_countableOverlapComponents A
    G.connectedComponentMk hInf hInter
    (fun c => by change c.supp.Countable; exact hCC c)
    hSame

#print axioms propertyB_of_locallyCountableOverlaps

#print axioms finite_iff_exists_list_cover
#print axioms escapesEveryList_iff_infinite
#print axioms essentialDisjoint_of_finiteIncoming
#print axioms propertyB_of_finiteIncoming

end MathSolve.Erdos602
