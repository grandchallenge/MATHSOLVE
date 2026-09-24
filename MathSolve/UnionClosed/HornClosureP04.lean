import MathSolve.UnionClosed.PosetIdealP04
import Mathlib.Tactic

/-!
# UC-001 / WP08-D003: Horn closure systems and the erasure boundary

WP08-D002 extends the Frankl-facing theorem from functional preorders to all
finite posets by erasing a maximal element.  This module isolates the exact
property used by that proof, extends it to a broad Horn-implication class, and
then gives a smallest non-unary obstruction to the erasure mechanism.

The positive criterion is conclusion-freeness: if a ground element never
appears as the conclusion of a Horn implication, deleting it from any model
preserves all implications.  Hence that element is rare and becomes abundant
after carrier-relative complementation.

The obstruction is a three-point cyclic binary Horn closure system.  It is a
pointed finite closure system and has rare elements, but no ground element is
erasable.  Thus the single-element erasure injection from D002 cannot be the
universal UC-P04 mechanism.
-/

namespace MathSolve.UnionClosed.WP08

open Finset

universe u

variable {α : Type u} [DecidableEq α]

/-- An element is erasable from a finite family when deleting it from every
member that contains it stays inside the family. -/
def IsErasableIn (F : Family α) (x : α) : Prop :=
  ∀ I ∈ F, x ∈ I → I.erase x ∈ F

/-- Erasability alone is sufficient for rarity.  This abstracts the counting
step used by the maximal-element argument in WP08-D002. -/
theorem rare_of_erasable
    {F : Family α} {x : α}
    (hErase : IsErasableIn F x) :
    2 * freq F x ≤ F.card := by
  classical
  let C : Family α := F.filter (fun I => x ∈ I)
  let E : Family α := C.image (fun I => I.erase x)

  have hinj : Set.InjOn (fun I : Finset α => I.erase x) ↑C := by
    simpa [C] using (erase_injective_on_containing (F := F) (m := x))

  have hcardE : E.card = C.card := by
    dsimp [E]
    exact Finset.card_image_iff.mpr hinj

  have hCsub : C ⊆ F := by
    intro I hI
    change I ∈ F.filter (fun J => x ∈ J) at hI
    exact (Finset.mem_filter.mp hI).1

  have hEsub : E ⊆ F := by
    intro I hI
    change I ∈ C.image (fun J => J.erase x) at hI
    rcases Finset.mem_image.mp hI with ⟨J, hJC, rfl⟩
    have hJF : J ∈ F := hCsub hJC
    have hxJ : x ∈ J := by
      change J ∈ F.filter (fun K => x ∈ K) at hJC
      exact (Finset.mem_filter.mp hJC).2
    exact hErase J hJF hxJ

  have hdisj : Disjoint C E := by
    refine Finset.disjoint_left.mpr ?_
    intro I hIC hIE
    change I ∈ C.image (fun J => J.erase x) at hIE
    rcases Finset.mem_image.mp hIE with ⟨J, hJC, hJI⟩
    have hxI : x ∈ I := by
      change I ∈ F.filter (fun K => x ∈ K) at hIC
      exact (Finset.mem_filter.mp hIC).2
    rw [← hJI] at hxI
    simpa using hxI

  have hUnionSub : C ∪ E ⊆ F := by
    intro I hI
    rcases Finset.mem_union.mp hI with hIC | hIE
    · exact hCsub hIC
    · exact hEsub hIE

  have hcardUnion : (C ∪ E).card = C.card + E.card :=
    Finset.card_union_of_disjoint hdisj
  have hle : (C ∪ E).card ≤ F.card := Finset.card_le_card hUnionSub

  unfold freq
  change 2 * C.card ≤ F.card
  calc
    2 * C.card = C.card + C.card := by omega
    _ = C.card + E.card := by rw [hcardE]
    _ = (C ∪ E).card := hcardUnion.symm
    _ ≤ F.card := hle

/-- A closure system that also contains the empty set.  This is the natural
dual object for a union-closed family whose full carrier is present. -/
def IsPointedClosureSystemOn (F : Family α) (U : Finset α) : Prop :=
  IsClosureSystemOn F U ∧ (∅ : Finset α) ∈ F

/-- An erasable carrier element in a pointed closure system immediately gives
the Frankl conclusion for the complementary union-closed family. -/
theorem pointedClosure_complement_frankl_of_erasable
    {F : Family α} {U : Finset α} {x : α}
    (hC : IsPointedClosureSystemOn F U)
    (hxU : x ∈ U)
    (hErase : IsErasableIn F x) :
    IsUnionClosed (complementFamilyOn F U) ∧
      IsNontrivial (complementFamilyOn F U) ∧
      IsFranklAbundant (complementFamilyOn F U) := by
  have hRare : 2 * freq F x ≤ F.card := rare_of_erasable hErase
  have hAbundant :
      IsFranklAbundant (complementFamilyOn F U) :=
    complementFamilyOn_abundant_of_exists_rare
      (F := F) (U := U)
      hC.1.1
      hC.2
      ⟨x, hxU, hRare⟩
  refine ⟨
    complementFamilyOn_unionClosed_of_interClosed hC.1.2.2,
    ?_,
    hAbundant
  ⟩
  rcases hAbundant with ⟨y, hy, _⟩
  exact ⟨y, hy⟩

/-! ## Horn implication systems -/

/-- A finite Horn implication with a finite premise and one conclusion. -/
structure HornImplication (α : Type u) where
  premise : Finset α
  conclusion : α
deriving DecidableEq

/-- A set satisfies `A -> b` when containing the whole premise `A` forces
the conclusion `b`. -/
def SatisfiesImplication
    (I : Finset α) (h : HornImplication α) : Prop :=
  h.premise ⊆ I → h.conclusion ∈ I

/-- Simultaneous satisfaction of a finite Horn basis. -/
def ModelsHorn
    (H : Finset (HornImplication α)) (I : Finset α) : Prop :=
  ∀ h ∈ H, SatisfiesImplication I h

/-- The models of a Horn basis restricted to an explicit finite carrier. -/
noncomputable def hornModelFamilyOn
    (U : Finset α) (H : Finset (HornImplication α)) : Family α := by
  classical
  exact U.powerset.filter (fun I => ModelsHorn H I)

@[simp] theorem mem_hornModelFamilyOn_iff
    {U I : Finset α} {H : Finset (HornImplication α)} :
    I ∈ hornModelFamilyOn U H ↔ I ⊆ U ∧ ModelsHorn H I := by
  classical
  simp only [hornModelFamilyOn, Finset.mem_filter, Finset.mem_powerset]

/-- Horn model families are intersection-closed. -/
theorem hornModelFamily_interClosed
    {U : Finset α} {H : Finset (HornImplication α)} :
    IsInterClosed (hornModelFamilyOn U H) := by
  intro A hA B hB
  rw [mem_hornModelFamilyOn_iff] at hA hB ⊢
  constructor
  · intro x hx
    exact hA.1 (Finset.mem_inter.mp hx).1
  · intro h hh hprem
    apply Finset.mem_inter.mpr
    constructor
    · exact hA.2 h hh (fun y hy => (Finset.mem_inter.mp (hprem hy)).1)
    · exact hB.2 h hh (fun y hy => (Finset.mem_inter.mp (hprem hy)).2)

/-- Every rule conclusion lies in the explicit carrier. -/
def ConclusionsInCarrier
    (U : Finset α) (H : Finset (HornImplication α)) : Prop :=
  ∀ h ∈ H, h.conclusion ∈ U

/-- Every Horn premise is nonempty.  This is exactly what makes the empty set a
model. -/
def PremisesNonempty
    (H : Finset (HornImplication α)) : Prop :=
  ∀ h ∈ H, h.premise.Nonempty

/-- A variable is conclusion-free when no rule derives it. -/
def ConclusionFree
    (H : Finset (HornImplication α)) (x : α) : Prop :=
  ∀ h ∈ H, h.conclusion ≠ x

/-- The full carrier models every Horn basis whose conclusions stay in the
carrier. -/
theorem hornModelFamily_ground_mem
    {U : Finset α} {H : Finset (HornImplication α)}
    (hConcl : ConclusionsInCarrier U H) :
    U ∈ hornModelFamilyOn U H := by
  rw [mem_hornModelFamilyOn_iff]
  refine ⟨Finset.Subset.rfl, ?_⟩
  intro h hh hprem
  exact hConcl h hh

/-- If all premises are nonempty, the empty set is a Horn model. -/
theorem hornModelFamily_empty_mem
    {U : Finset α} {H : Finset (HornImplication α)}
    (hPrem : PremisesNonempty H) :
    (∅ : Finset α) ∈ hornModelFamilyOn U H := by
  rw [mem_hornModelFamilyOn_iff]
  constructor
  · simp
  · intro h hh hprem
    rcases hPrem h hh with ⟨y, hy⟩
    have : y ∈ (∅ : Finset α) := hprem hy
    simpa using this

/-- Under the natural carrier and nonempty-premise conditions, Horn models form
a pointed finite closure system. -/
theorem hornModelFamily_pointedClosureSystem
    {U : Finset α} {H : Finset (HornImplication α)}
    (hConcl : ConclusionsInCarrier U H)
    (hPrem : PremisesNonempty H) :
    IsPointedClosureSystemOn (hornModelFamilyOn U H) U := by
  refine ⟨⟨?_, hornModelFamily_ground_mem hConcl, hornModelFamily_interClosed⟩,
    hornModelFamily_empty_mem hPrem⟩
  intro I hI
  exact (mem_hornModelFamilyOn_iff.mp hI).1

/-- Deleting a conclusion-free variable preserves every Horn implication. -/
theorem erase_preserves_Horn_of_conclusionFree
    {H : Finset (HornImplication α)} {I : Finset α} {x : α}
    (hModel : ModelsHorn H I)
    (hFree : ConclusionFree H x) :
    ModelsHorn H (I.erase x) := by
  intro h hh hprem
  have hpremI : h.premise ⊆ I := by
    intro y hy
    exact Finset.mem_of_mem_erase (hprem hy)
  have hcI : h.conclusion ∈ I := hModel h hh hpremI
  exact Finset.mem_erase.mpr ⟨hFree h hh, hcI⟩

/-- Conclusion-free variables are erasable from the Horn model family. -/
theorem hornModel_erasable_of_conclusionFree
    {U : Finset α} {H : Finset (HornImplication α)} {x : α}
    (hFree : ConclusionFree H x) :
    IsErasableIn (hornModelFamilyOn U H) x := by
  intro I hI hxI
  rw [mem_hornModelFamilyOn_iff] at hI ⊢
  constructor
  · intro y hy
    exact hI.1 (Finset.mem_of_mem_erase hy)
  · exact erase_preserves_Horn_of_conclusionFree hI.2 hFree

/-- Positive Horn extension: any pointed Horn closure system with a
conclusion-free carrier variable satisfies the complementary Frankl
half-frequency conclusion. -/
theorem hornModel_complement_frankl_of_conclusionFree
    {U : Finset α} {H : Finset (HornImplication α)} {x : α}
    (hxU : x ∈ U)
    (hConcl : ConclusionsInCarrier U H)
    (hPrem : PremisesNonempty H)
    (hFree : ConclusionFree H x) :
    IsUnionClosed (complementFamilyOn (hornModelFamilyOn U H) U) ∧
      IsNontrivial (complementFamilyOn (hornModelFamilyOn U H) U) ∧
      IsFranklAbundant (complementFamilyOn (hornModelFamilyOn U H) U) := by
  exact pointedClosure_complement_frankl_of_erasable
    (hornModelFamily_pointedClosureSystem hConcl hPrem)
    hxU
    (hornModel_erasable_of_conclusionFree hFree)

/-! ## Three-point cyclic binary obstruction -/

abbrev hornA : Finset Chain3 := {Chain3.a}
abbrev hornB : Finset Chain3 := {Chain3.b}
abbrev hornC : Finset Chain3 := {Chain3.c}

/-- The smallest symmetric closure-system fixture with only the empty set,
singletons, and the full carrier. -/
abbrev cyclicBinaryClosure : Family Chain3 :=
  {∅, hornA, hornB, hornC, Chain3.ground}

/-- Explicit three binary Horn implications:
`ab -> c`, `bc -> a`, and `ca -> b`. -/
def CyclicBinaryHornClosed (I : Finset Chain3) : Prop :=
  ({Chain3.a, Chain3.b} ⊆ I → Chain3.c ∈ I) ∧
    ({Chain3.b, Chain3.c} ⊆ I → Chain3.a ∈ I) ∧
    ({Chain3.c, Chain3.a} ⊆ I → Chain3.b ∈ I)

/-- On the three-point carrier, the explicit closure family is exactly the
model class of the cyclic binary implications. -/
theorem cyclicBinaryClosure_iff_models :
    ∀ I : Finset Chain3,
      I ⊆ Chain3.ground →
        (I ∈ cyclicBinaryClosure ↔ CyclicBinaryHornClosed I) := by
  native_decide

/-- The cyclic binary fixture is a pointed finite closure system. -/
theorem cyclicBinaryClosure_pointed :
    IsPointedClosureSystemOn cyclicBinaryClosure Chain3.ground := by
  native_decide

/-- Every carrier element is blocked from single-element erasure: deleting any
element from the full closed set leaves a forbidden two-element set. -/
theorem cyclicBinaryClosure_no_erasable :
    ∀ x ∈ Chain3.ground, ¬ IsErasableIn cyclicBinaryClosure x := by
  native_decide

/-- Despite having no erasable carrier element, the fixture still has rare
elements.  Thus erasability is sufficient but not necessary for the desired
frequency inequality. -/
theorem cyclicBinaryClosure_has_rare :
    ∃ x ∈ Chain3.ground,
      2 * freq cyclicBinaryClosure x ≤ cyclicBinaryClosure.card := by
  native_decide

/-- The single-element erasure mechanism cannot be universal for pointed finite
closure systems. -/
theorem not_every_pointedClosureSystem_has_erasable :
    ¬ (∀ F : Family Chain3,
        IsPointedClosureSystemOn F Chain3.ground →
          ∃ x ∈ Chain3.ground, IsErasableIn F x) := by
  intro hUniversal
  obtain ⟨x, hxU, hxErase⟩ :=
    hUniversal cyclicBinaryClosure cyclicBinaryClosure_pointed
  exact cyclicBinaryClosure_no_erasable x hxU hxErase

/-- The complementary union-closed fixture nevertheless satisfies Frankl
abundance, showing that a more general matching or charging argument must
replace literal erasure beyond the D002/Horn conclusion-free regime. -/
theorem cyclicBinaryClosure_complement_frankl :
    IsUnionClosed (complementFamilyOn cyclicBinaryClosure Chain3.ground) ∧
      IsNontrivial (complementFamilyOn cyclicBinaryClosure Chain3.ground) ∧
      IsFranklAbundant
        (complementFamilyOn cyclicBinaryClosure Chain3.ground) := by
  have hRare := cyclicBinaryClosure_has_rare
  have hAbundant :
      IsFranklAbundant
        (complementFamilyOn cyclicBinaryClosure Chain3.ground) :=
    complementFamilyOn_abundant_of_exists_rare
      (F := cyclicBinaryClosure) (U := Chain3.ground)
      cyclicBinaryClosure_pointed.1.1
      cyclicBinaryClosure_pointed.2
      hRare
  refine ⟨
    complementFamilyOn_unionClosed_of_interClosed
      cyclicBinaryClosure_pointed.1.2.2,
    ?_,
    hAbundant
  ⟩
  rcases hAbundant with ⟨x, hx, _⟩
  exact ⟨x, hx⟩

end MathSolve.UnionClosed.WP08
