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


/-!
## Binary-prefix sharpness example

For each infinite binary stream, take its finite prefixes and add two
common marker points. Distinct branches share only finitely many prefixes;
the two common markers force Property B. As the ground type is countable
but there are uncountably many branches, infinite pairwise-disjoint
finite-deletion residuals are impossible. This refutes a proposed proof
strategy, **not** the unrestricted Erdős #602 conjecture.
-/
namespace BinaryPrefix

abbrev Ground := List Bool ⊕ Fin 2

def wordPrefix (s : ℕ → Bool) (n : ℕ) : List Bool :=
  List.ofFn (fun k : Fin n => s k.val)

@[simp]
private theorem prefix_length (s : ℕ → Bool) (n : ℕ) :
    (wordPrefix s n).length = n := by
  simp [wordPrefix]

def family (s : ℕ → Bool) : Set Ground :=
  {x | x = Sum.inr 0 ∨ x = Sum.inr 1 ∨
    ∃ n : ℕ, x = Sum.inl (wordPrefix s n)}

/-- An arbitrary member of the binary-wordPrefix family is countable. -/
theorem member_countable (s : ℕ → Bool) : (family s).Countable := by
  exact (Set.countable_univ).mono (Set.subset_univ _)

/-- The finite prefixes have distinct lengths, hence form an infinite
subset of each indexed member. -/
theorem member_infinite (s : ℕ → Bool) : (family s).Infinite := by
  have hinj : Function.Injective
      (fun n : ℕ => (Sum.inl (wordPrefix s n) : Ground)) := by
    intro n m h
    have hp : wordPrefix s n = wordPrefix s m := Sum.inl_injective h
    have hl := congrArg List.length hp
    simpa using hl
  apply Set.infinite_of_injective_forall_mem hinj
  intro n
  exact Or.inr (Or.inr ⟨n, rfl⟩)

/-- Distinct binary streams can share only a bounded number of
finite prefixes. The two extra common markers remain. -/
theorem distinct_inter_finite (s t : ℕ → Bool) (hst : s ≠ t) :
    (family s ∩ family t).Finite := by
  classical
  have hdiff : ∃ k : ℕ, s k ≠ t k := by
    by_contra h
    apply hst
    funext k
    by_contra hk
    exact h ⟨k, hk⟩
  obtain ⟨k, hk⟩ := hdiff
  let B : Set Ground :=
    Set.range (fun n : Fin (k + 1) => (Sum.inl (wordPrefix s n.val) : Ground)) ∪
      {Sum.inr 0, Sum.inr 1}
  have hB : B.Finite := by
    dsimp [B]
    exact (Set.finite_range _).union (by simp)
  apply hB.subset
  intro x hx
  rcases hx.1 with hzero | hone | ⟨n, hn⟩
  · simp [B, hzero]
  · simp [B, hone]
  · rcases hx.2 with hzero | hone | ⟨m, hm⟩
    · simp [hn] at hzero
    · simp [hn] at hone
    · have heq : wordPrefix s n = wordPrefix t m :=
        Sum.inl_injective (hn.symm.trans hm)
      have hnle : n ≤ k := by
        by_contra hle
        have hklt : k < n := by omega
        have hnm : n = m := by
          have hlen := congrArg List.length heq
          simpa using hlen
        subst m
        have hfun : (fun j : Fin n => s j.val) =
            (fun j : Fin n => t j.val) :=
          List.ofFn_injective heq
        exact hk (congrFun hfun ⟨k, hklt⟩)
      change x ∈ Set.range
        (fun n : Fin (k + 1) => (Sum.inl (wordPrefix s n.val) : Ground)) ∪
          {Sum.inr 0, Sum.inr 1}
      exact Or.inl ⟨⟨n, Nat.lt_succ_of_le hnle⟩, hn.symm⟩

/-- Every pair of distinct members shares the two *distinct* markers,
so no intersection has cardinality one. -/
theorem distinct_inter_not_one (s t : ℕ → Bool) (hst : s ≠ t) :
    Set.ncard (family s ∩ family t) ≠ 1 := by
  have hfin := distinct_inter_finite s t hst
  have htwo : 1 < Set.ncard (family s ∩ family t) :=
    (Set.one_lt_ncard hfin).mpr
      ⟨Sum.inr 0,
        ⟨Or.inl rfl, Or.inl rfl⟩,
        Sum.inr 1,
        ⟨Or.inr (Or.inl rfl), Or.inr (Or.inl rfl)⟩,
        by decide⟩
  exact ne_of_gt htwo

/-- The two shared marker points are always differently coloured.
This is a direct witness to Property B, independent of deletions. -/
theorem hasPropertyB : HasPropertyB (ℕ → Bool) family := by
  let colour : Ground → Fin 2 := fun x =>
    if x = Sum.inr 1 then 1 else 0
  refine ⟨colour, fun s hmono => ?_⟩
  have heq : colour (Sum.inr 0) = colour (Sum.inr 1) :=
    hmono (Sum.inr 0) (Or.inl rfl)
      (Sum.inr 1) (Or.inr (Or.inl rfl))
  have hne : colour (Sum.inr 0) ≠ colour (Sum.inr 1) := by
    decide
  exact hne heq

/-- Cantor's diagonal argument: the binary-stream index type is
uncountable. -/
theorem stream_not_countable : ¬ Countable (ℕ → Bool) := by
  intro h
  letI : Countable (ℕ → Bool) := h
  obtain ⟨f, hf⟩ := exists_surjective_nat (ℕ → Bool)
  let d : ℕ → Bool := fun n => !(f n n)
  obtain ⟨n, hn⟩ := hf d
  have hb : f n n = !(f n n) := by
    simpa [d] using congrArg (fun g : ℕ → Bool => g n) hn
  cases hbit : f n n <;> simp [hbit] at hb

/-- A countable ground type cannot support an uncountable indexed
family of pairwise disjoint, nonempty residual sets. In particular,
finite deletions cannot yield infinite pairwise disjoint residuals. -/
def HasFiniteDisjointResiduals {I : Type*} {X : Type*}
    (A : I → Set X) : Prop :=
  ∃ F : I → Set X, (∀ i, (F i).Finite) ∧
    (∀ i, (A i \ F i).Infinite) ∧
    (∀ i j, i ≠ j → ∀ x, ¬
      (x ∈ A i \ F i ∧ x ∈ A j \ F j))

theorem no_finite_disjoint_residuals {I : Type*} {X : Type*}
    [Countable X] (A : I → Set X) (hI : ¬ Countable I) :
    ¬ HasFiniteDisjointResiduals A := by
  classical
  rintro ⟨F, _hF, hInf, hDisj⟩
  have he : ∀ i, ∃ x : X, x ∈ A i \ F i := by
    intro i
    exact (hInf i).nonempty
  choose w hw using he
  have hinj : Function.Injective w := by
    intro i j heq
    by_contra hij
    have hwj : w i ∈ A j \ F j := by
      simpa only [heq] using hw j
    exact hDisj i j hij (w i) ⟨hw i, hwj⟩
  exact hI hinj.countable

theorem not_essentiallyDisjoint :
    ¬ HasFiniteDisjointResiduals family := by
  exact no_finite_disjoint_residuals family stream_not_countable

/-- All original Erdős #602 premises hold for this countable-ground,
uncountably indexed family, and Property B holds; nevertheless,
no finite deletions yield infinite pairwise-disjoint residual sets.
This disproves *universal essential disjointness*, not Property B. -/
theorem binaryPrefix_sharpness :
    (∀ s, (family s).Countable ∧ (family s).Infinite) ∧
    (∀ s t, s ≠ t → (family s ∩ family t).Finite) ∧
    (∀ s t, s ≠ t → Set.ncard (family s ∩ family t) ≠ 1) ∧
    HasPropertyB (ℕ → Bool) family ∧
    ¬ HasFiniteDisjointResiduals family := by
  exact ⟨fun s => ⟨member_countable s, member_infinite s⟩,
    distinct_inter_finite, distinct_inter_not_one,
    hasPropertyB, not_essentiallyDisjoint⟩

#print axioms distinct_inter_finite
#print axioms distinct_inter_not_one
#print axioms hasPropertyB
#print axioms stream_not_countable
#print axioms not_essentiallyDisjoint
#print axioms binaryPrefix_sharpness

end BinaryPrefix


#print axioms finite_iff_exists_list_cover
#print axioms escapesEveryList_iff_infinite
#print axioms essentialDisjoint_of_finiteIncoming
#print axioms propertyB_of_finiteIncoming


/-- Bernstein's lemma: an arbitrary sequence of infinite sets is
splittable, without any pairwise-intersection assumption.
At each step choose two fresh points outside the finitely many
previously used points. -/
theorem bernstein_nat (A : ℕ → Set X)
    (hInf : ∀ n, (A n).Infinite) : HasPropertyB ℕ A := by
  classical
  have fresh : ∀ (n : ℕ) (S : Finset X),
      ∃ a b : X, a ∈ A n ∧ b ∈ A n ∧
        a ∉ S ∧ b ∉ S ∧ a ≠ b := by
    intro n S
    obtain ⟨a, ha⟩ := ((hInf n).diff S.finite_toSet).nonempty
    obtain ⟨b, hb⟩ :=
      ((hInf n).diff (insert a S).finite_toSet).nonempty
    have hbn : b ∉ insert a S := hb.2
    have hb' : b ≠ a ∧ b ∉ S := by
      simpa only [Finset.mem_insert, not_or] using hbn
    exact ⟨a, b, ha.1, hb.1, ha.2, hb'.2, hb'.1.symm⟩
  choose a b ha hb haFresh hbFresh hab using fresh
  let used : ℕ → Finset X := fun n =>
    Nat.rec ∅ (fun k S => insert (a k S) (insert (b k S) S)) n
  let red (n : ℕ) : X := a n (used n)
  let blue (n : ℕ) : X := b n (used n)
  have hnext (n : ℕ) : used (n + 1) =
      insert (red n) (insert (blue n) (used n)) := rfl
  have hmono : Monotone used := by
    apply monotone_nat_of_le_succ
    intro n x hx
    rw [hnext]
    exact Finset.mem_insert_of_mem (Finset.mem_insert_of_mem hx)
  have hred (n : ℕ) : red n ∈ used (n + 1) := by
    rw [hnext]
    exact Finset.mem_insert_self _ _
  have hblue (n : ℕ) : blue n ∈ used (n + 1) := by
    rw [hnext]
    exact Finset.mem_insert_of_mem (Finset.mem_insert_self _ _)
  have hsep (n m : ℕ) : red n ≠ blue m := by
    intro heq
    rcases lt_trichotomy n m with hlt | he | hgt
    · have hmem := hmono (Nat.succ_le_of_lt hlt) (hred n)
      apply hbFresh m (used m)
      change blue m ∈ used m
      rw [← heq]
      exact hmem
    · subst m
      exact hab n (used n) heq
    · have hmem := hmono (Nat.succ_le_of_lt hgt) (hblue m)
      apply haFresh n (used n)
      change red n ∈ used n
      rw [heq]
      exact hmem
  let colour : X → Fin 2 := fun x => if ∃ n, x = blue n then 1 else 0
  refine ⟨colour, fun n hconst => ?_⟩
  have hr : colour (red n) = 0 := by
    apply if_neg
    rintro ⟨m, hm⟩
    exact hsep n m hm
  have hb' : colour (blue n) = 1 := if_pos ⟨n, rfl⟩
  have he := hconst (red n) (ha n (used n)) (blue n) (hb n (used n))
  rw [hr, hb'] at he
  exact (by decide : (0 : Fin 2) ≠ 1) he

/-- General countable-index Bernstein lemma, including empty index types. -/
theorem bernstein_countable [Countable I] (A : I → Set X)
    (hInf : ∀ i, (A i).Infinite) : HasPropertyB I A := by
  classical
  by_cases he : Nonempty I
  · letI : Nonempty I := he
    obtain ⟨e, hs⟩ := exists_surjective_nat I
    obtain ⟨f, hf⟩ := bernstein_nat (fun n => A (e n)) (fun n => hInf (e n))
    refine ⟨f, fun i => ?_⟩
    obtain ⟨n, hn⟩ := hs i
    simpa only [hn] using hf n
  · exact ⟨fun _ => 0, fun i => (he ⟨i⟩).elim⟩

#print axioms bernstein_nat
#print axioms bernstein_countable


/-!
## Minimal-transversal reduction

This route uses the forbidden singleton intersection itself. It does
not require an essentially disjoint family or a bound on overlap degree.
Existence of a minimal cover is a separate combinatorial obligation.
-/

/-- A vertex cover meets every member of the indexed family. -/
def IsCover (A : I → Set X) (T : Set X) : Prop :=
  ∀ i, (A i ∩ T).Nonempty

/-- Every selected point has a private witness edge. -/
def HasPrivateWitnesses (A : I → Set X) (T : Set X) : Prop :=
  ∀ x ∈ T, ∃ j, A j ∩ T = {x}

/-- Inclusion-minimal vertex covers are exactly covers with private
witness edges. No cardinality hypotheses are needed. -/
theorem minimalCover_iff_privateWitnesses (A : I → Set X) (T : Set X) :
    Minimal (IsCover A) T ↔ IsCover A T ∧ HasPrivateWitnesses A T := by
  classical
  constructor
  · intro h
    refine ⟨h.prop, ?_⟩
    intro x hx
    have hnot : ¬ IsCover A (T \ {x}) := by
      intro hc
      have he := h.eq_of_subset hc Set.diff_subset
      have hmem : x ∈ T \ {x} := he.symm ▸ hx
      exact hmem.2 (Set.mem_singleton x)
    have hj : ∃ j, ¬ (A j ∩ (T \ {x})).Nonempty := by
      by_contra hh
      apply hnot
      intro j
      by_contra hn
      exact hh ⟨j, hn⟩
    obtain ⟨j, hj⟩ := hj
    obtain ⟨y, hy⟩ := h.prop j
    have unique (z : X) (hz : z ∈ A j ∩ T) : z = x := by
      by_contra hne
      exact hj ⟨z, hz.1, hz.2, fun hs => hne (Set.mem_singleton_iff.mp hs)⟩
    have hyx := unique y hy
    refine ⟨j, ?_⟩
    ext z
    constructor
    · intro hz
      exact Set.mem_singleton_iff.mpr (unique z hz)
    · intro hz
      have he := Set.mem_singleton_iff.mp hz
      rw [he, ← hyx]
      exact hy
  · rintro ⟨hcover, hw⟩
    refine ⟨hcover, ?_⟩
    intro S hS hsub x hx
    obtain ⟨j, hj⟩ := hw x hx
    obtain ⟨y, hy⟩ := hS j
    have hmem : y ∈ A j ∩ T := ⟨hy.1, hsub hy.2⟩
    rw [hj] at hmem
    have he := Set.mem_singleton_iff.mp hmem
    rw [← he]
    exact hy.2

/-- Lovasz's minimal-transversal argument, for arbitrary index and
ground types: if each edge has two distinct points and distinct edges
never intersect in a singleton, a minimal cover gives Property B.
Finiteness of intersections is not needed for this implication. -/
theorem propertyB_of_minimalCover (A : I → Set X) (T : Set X)
    (hTwo : ∀ i, ∃ x ∈ A i, ∃ y ∈ A i, x ≠ y)
    (hNoSingleton : ∀ i j, i ≠ j → ∀ x : X, A i ∩ A j ≠ {x})
    (hMin : Minimal (IsCover A) T) : HasPropertyB I A := by
  classical
  obtain ⟨hcover, hw⟩ := (minimalCover_iff_privateWitnesses A T).mp hMin
  have hnotContained : ∀ i, ¬ A i ⊆ T := by
    intro i hsub
    obtain ⟨x, hx⟩ := hcover i
    obtain ⟨j, hj⟩ := hw x hx.2
    have hxj : x ∈ A j := by
      have hmem : x ∈ A j ∩ T := by rw [hj]; exact Set.mem_singleton x
      exact hmem.1
    have hsingle : A i ∩ A j = {x} := by
      ext y
      constructor
      · intro hy
        have hmem : y ∈ A j ∩ T := ⟨hy.2, hsub hy.1⟩
        rwa [hj] at hmem
      · intro hy
        have he := Set.mem_singleton_iff.mp hy
        rw [he]
        exact ⟨hx.1, hxj⟩
    by_cases hij : i = j
    · subst j
      rw [Set.inter_self] at hsingle
      obtain ⟨a, ha, b, hb, hab⟩ := hTwo i
      rw [hsingle] at ha hb
      exact hab ((Set.mem_singleton_iff.mp ha).trans
        (Set.mem_singleton_iff.mp hb).symm)
    · exact hNoSingleton i j hij x hsingle
  let colour : X → Fin 2 := fun x => if x ∈ T then 1 else 0
  refine ⟨colour, fun i hmono => ?_⟩
  obtain ⟨x, hx⟩ := hcover i
  have hy : ∃ y ∈ A i, y ∉ T := by
    by_contra hh
    apply hnotContained i
    intro y hym
    by_contra hn
    exact hh ⟨y, hym, hn⟩
  obtain ⟨y, hym, hyn⟩ := hy
  have he := hmono x hx.1 y hym
  change (if x ∈ T then (1 : Fin 2) else 0) =
    (if y ∈ T then (1 : Fin 2) else 0) at he
  rw [if_pos hx.2, if_neg hyn] at he
  exact (by decide : (1 : Fin 2) ≠ 0) he

/-- A cover having finite traces on every edge contains a minimal
cover. Every nonempty decreasing chain has a covering intersection:
for a fixed edge, choose a chain member with the smallest trace
cardinality. Its nonempty finite trace survives the entire chain. -/
theorem minimalCover_of_finiteTraces (A : I → Set X) (T : Set X)
    (hcover : IsCover A T) (hfinite : ∀ i, (A i ∩ T).Finite) :
    ∃ S ⊆ T, Minimal (IsCover A) S := by
  classical
  let C : Set (Set X) := {S | IsCover A S ∧ S ⊆ T}
  have hT : T ∈ C := ⟨hcover, Set.Subset.rfl⟩
  obtain ⟨S, hST, hS⟩ := zorn_superset_nonempty C (by
    intro c hc hchain hne
    obtain ⟨U, hU⟩ := hne
    have hsub : ⋂₀ c ⊆ T := fun x hx =>
      (hc hU).2 (Set.mem_sInter.mp hx U hU)
    refine ⟨⋂₀ c, ⟨?_, hsub⟩, ?_⟩
    · intro i
      let P : ℕ → Prop := fun n => ∃ V ∈ c, (A i ∩ V).ncard = n
      have hP : ∃ n, P n := ⟨(A i ∩ U).ncard, U, hU, rfl⟩
      obtain ⟨V, hV, hcard⟩ := Nat.find_spec hP
      obtain ⟨x, hx⟩ := (hc hV).1 i
      refine ⟨x, hx.1, Set.mem_sInter.mpr ?_⟩
      intro W hW
      have hVW : V ⊆ W ∨ W ⊆ V := by
        by_cases he : V = W
        · exact Or.inl (he ▸ Set.Subset.rfl)
        · exact hchain hV hW he
      rcases hVW with h | h
      · exact h hx.2
      · have htrace : A i ∩ W ⊆ A i ∩ V :=
          fun _ hy => ⟨hy.1, h hy.2⟩
        have hle : (A i ∩ V).ncard ≤ (A i ∩ W).ncard := by
          rw [hcard]
          exact Nat.find_min' hP ⟨W, hW, rfl⟩
        have hfin : (A i ∩ V).Finite :=
          (hfinite i).subset (fun _ hy => ⟨hy.1, (hc hV).2 hy.2⟩)
        have he := Set.eq_of_subset_of_ncard_le htrace hle hfin
        have hmem : x ∈ A i ∩ W := he.symm ▸ hx
        exact hmem.2
    · intro W hW x hx
      exact Set.mem_sInter.mp hx W hW) T hT
  refine ⟨S, hST, hS.prop.1, ?_⟩
  intro U hU hUS
  have hUC : U ∈ C := ⟨hU, hUS.trans hST⟩
  exact hS.le_of_le hUC hUS

/-- The original no-singleton numerical hypothesis, together with
a finite-trace cover, gives Property B with no restriction on the
number of indices or a uniform bound on pairwise intersections. -/
theorem propertyB_of_finiteTraceCover (A : I → Set X) (T : Set X)
    (hInf : ∀ i, (A i).Infinite)
    (hNoSingleton : ∀ i j, i ≠ j → (A i ∩ A j).ncard ≠ 1)
    (hcover : IsCover A T) (hfinite : ∀ i, (A i ∩ T).Finite) :
    HasPropertyB I A := by
  obtain ⟨S, _, hS⟩ := minimalCover_of_finiteTraces A T hcover hfinite
  apply propertyB_of_minimalCover A S ?_ ?_ hS
  · intro i
    obtain ⟨x, hx⟩ := (hInf i).nonempty
    obtain ⟨y, hy⟩ := ((hInf i).diff (Set.finite_singleton x)).nonempty
    refine ⟨x, hx, y, hy.1, ?_⟩
    intro he
    exact hy.2 (Set.mem_singleton_iff.mpr he.symm)
  · intro i j hij x he
    exact hNoSingleton i j hij (by rw [he]; exact Set.ncard_singleton x)

#print axioms minimalCover_iff_privateWitnesses
#print axioms propertyB_of_minimalCover
#print axioms minimalCover_of_finiteTraces
#print axioms propertyB_of_finiteTraceCover


/-!
## Obstruction to the minimal-cover strategy

A cover whose complement is almost covered by finitely many edges
cannot have infinitely many private witnesses in an almost-disjoint
family. Doubling each point preserves minimal-cover existence but
rules out singleton intersections. The accompanying research record
uses these facts in a paper-level CH construction.
-/

/-- If only finitely many edges can witness singleton traces, an infinite
cover cannot be minimal. -/
theorem not_minimalCover_of_finitePrivateEdges
    (A : I → Set X) (T : Set X) (K : Set I)
    (hT : T.Infinite) (hK : K.Finite)
    (hWitness : ∀ j x, A j ∩ T = {x} → j ∈ K) :
    ¬ Minimal (IsCover A) T := by
  intro hMin
  have hw := ((minimalCover_iff_privateWitnesses A T).mp hMin).2
  let W (j : I) : Set X := {x | A j ∩ T = {x}}
  have hW (j : I) : (W j).Finite := by
    apply Set.Subsingleton.finite
    intro x hx y hy
    have hx' : A j ∩ T = {x} := hx
    have hy' : A j ∩ T = {y} := hy
    have he : ({x} : Set X) = {y} := hx'.symm.trans hy'
    have hm : x ∈ ({y} : Set X) := he ▸ Set.mem_singleton x
    exact Set.mem_singleton_iff.mp hm
  apply hT
  apply (hK.biUnion (fun j _ => hW j)).subset
  intro x hx
  obtain ⟨j, hj⟩ := hw x hx
  exact Set.mem_iUnion.mpr ⟨j, Set.mem_iUnion.mpr
    ⟨hWitness j x hj, hj⟩⟩

/-- If the complement of an infinite cover is contained, up to finitely
many points, in finitely many members of an almost-disjoint family,
the cover is not inclusion-minimal. This holds for every extension of
the family preserving the same finite-intersection hypotheses. -/
theorem not_minimalCover_of_almostCoveredCompl
    (A : I → Set X) (T : Set X) (K : Set I)
    (hInf : ∀ i, (A i).Infinite)
    (hInter : ∀ i j, i ≠ j → (A i ∩ A j).Finite)
    (hT : T.Infinite) (hK : K.Finite)
    (hAlmost : (Tᶜ \ ⋃ j ∈ K, A j).Finite) :
    ¬ Minimal (IsCover A) T := by
  classical
  apply not_minimalCover_of_finitePrivateEdges A T K hT hK
  intro j x hj
  by_contra hjK
  have hU : (⋃ k ∈ K, A j ∩ A k).Finite := by
    apply hK.biUnion
    intro k hk
    exact hInter j k (fun he => hjK (he.symm ▸ hk))
  apply hInf j
  apply ((Set.finite_singleton x).union (hU.union hAlmost)).subset
  intro y hy
  by_cases hyt : y ∈ T
  · left
    have hmem : y ∈ A j ∩ T := ⟨hy, hyt⟩
    rw [hj] at hmem
    exact hmem
  · right
    by_cases hmem : y ∈ ⋃ k ∈ K, A k
    · left
      obtain ⟨k, hk⟩ := Set.mem_iUnion.mp hmem
      obtain ⟨hkK, hyk⟩ := Set.mem_iUnion.mp hk
      exact Set.mem_iUnion.mpr ⟨k, Set.mem_iUnion.mpr
        ⟨hkK, ⟨hy, hyk⟩⟩⟩
    · exact Or.inr ⟨hyt, hmem⟩

/-- Replace each point by two indistinguishable copies. -/
def doubledFamily (A : I → Set X) (i : I) : Set (X × Fin 2) :=
  A i ×ˢ Set.univ

/-- A minimal cover of the doubled family projects to a minimal cover
of the original family: project both coverage and singleton witnesses. -/
theorem minimalCover_doubled_projects (A : I → Set X)
    (S : Set (X × Fin 2)) (hS : Minimal (IsCover (doubledFamily A)) S) :
    Minimal (IsCover A) (Prod.fst '' S) := by
  obtain ⟨hc, hw⟩ :=
    (minimalCover_iff_privateWitnesses (doubledFamily A) S).mp hS
  apply (minimalCover_iff_privateWitnesses A (Prod.fst '' S)).mpr
  constructor
  · intro i
    obtain ⟨p, hp⟩ := hc i
    exact ⟨p.1, hp.1.1, ⟨p, hp.2, rfl⟩⟩
  · intro x hx
    obtain ⟨p, hp, hpx⟩ := hx
    obtain ⟨j, hj⟩ := hw p hp
    have hpj : p ∈ doubledFamily A j ∩ S := by
      rw [hj]
      exact Set.mem_singleton p
    refine ⟨j, ?_⟩
    ext y
    constructor
    · intro hy
      obtain ⟨q, hq, hqy⟩ := hy.2
      have hqj : q ∈ doubledFamily A j ∩ S :=
        ⟨⟨hqy.symm ▸ hy.1, Set.mem_univ _⟩, hq⟩
      rw [hj] at hqj
      have he := Set.mem_singleton_iff.mp hqj
      exact Set.mem_singleton_iff.mpr
        (hqy.symm.trans ((congrArg Prod.fst he).trans hpx))
    · intro hy
      have he := Set.mem_singleton_iff.mp hy
      rw [he, ← hpx]
      exact ⟨hpj.1.1, ⟨p, hp, rfl⟩⟩

/-- The doubled family always has Property B, and its intersections
cannot have cardinality one. This is independent of minimal covers. -/
theorem doubled_propertyB_and_noSingleton (A : I → Set X)
    (hNonempty : ∀ i, (A i).Nonempty) :
    HasPropertyB I (doubledFamily A) ∧
      (∀ i j, (doubledFamily A i ∩ doubledFamily A j).ncard ≠ 1) := by
  constructor
  · refine ⟨Prod.snd, fun i hmono => ?_⟩
    obtain ⟨x, hx⟩ := hNonempty i
    exact (by decide : (0 : Fin 2) ≠ 1)
      (hmono (x, 0) ⟨hx, Set.mem_univ _⟩
        (x, 1) ⟨hx, Set.mem_univ _⟩)
  · intro i j
    have he : doubledFamily A i ∩ doubledFamily A j =
        (A i ∩ A j) ×ˢ (Set.univ : Set (Fin 2)) := by
      ext p
      simp [doubledFamily]
    rw [he, Set.ncard_prod, Set.ncard_univ]
    have hcard : Nat.card (Fin 2) = 2 := by simp
    rw [hcard]
    omega

#print axioms not_minimalCover_of_finitePrivateEdges
#print axioms not_minimalCover_of_almostCoveredCompl
#print axioms minimalCover_doubled_projects
#print axioms doubled_propertyB_and_noSingleton

end MathSolve.Erdos602
