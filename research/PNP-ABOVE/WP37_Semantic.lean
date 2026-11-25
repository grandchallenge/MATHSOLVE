import Mathlib.Data.Finset.Card
import Mathlib.Data.Fintype.Basic
import Mathlib.Tactic

set_option linter.unusedSectionVars false

namespace PNPAbove.WP37
universe u v
variable {V : Type u} {E : Type v} [DecidableEq V] [DecidableEq E]
abbrev Assignment (E : Type v) := E → Bool
abbrev Predicate (E : Type v) := Assignment E → Prop

def Entails (P : V → Predicate E) (S : Finset V) (Q : Predicate E) : Prop :=
  ∀ a, (∀ v ∈ S, P v a) → Q a

def Depends (Q : Predicate E) (F : Finset E) : Prop :=
  ∀ a b, (∀ e ∈ F, a e = b e) → (Q a ↔ Q b)

def flip (a : Assignment E) (e : E) : Assignment E :=
  fun f => if f = e then !a f else a f

def Boundary (I : V → E → Prop) (S : Finset V) (e : E) : Prop :=
  ∃ v ∈ S, I v e ∧ ∀ w ∈ S, I w e → w = v

def FlipLaw (I : V → E → Prop) (P : V → Predicate E) : Prop :=
  ∀ v e a, (I v e → (P v (flip a e) ↔ ¬ P v a)) ∧
    (¬ I v e → (P v (flip a e) ↔ P v a))

/-- Only one-way repair is required at a unique boundary variable.
The reverse toggle law is not needed. -/
def RepairLaw (I : V → E → Prop) (P : V → Predicate E) : Prop :=
  ∀ v e a, (I v e → ¬ P v a → P v (flip a e)) ∧
    (¬ I v e → (P v (flip a e) ↔ P v a))

theorem flip_implies_repair {I : V → E → Prop} {P : V → Predicate E}
    (h : FlipLaw I P) : RepairLaw I P :=
  fun v e a => ⟨fun he hn => ((h v e a).1 he).2 hn,(h v e a).2⟩

/-- A non-tautological disjunctive clause has the one-way repair property:
if it is false, flipping any occurring variable makes it true. -/
theorem clause_repair (I : V → E → Prop) (sign : V → E → Bool) :
    RepairLaw I (fun v a => ∃ e, I v e ∧ a e = sign v e) := by
  intro v e a
  constructor
  · intro hi hn
    have hne : a e ≠ sign v e := fun he => hn ⟨e,hi,he⟩
    refine ⟨e,hi,?_⟩
    have hh : ∀ b c : Bool, b ≠ c → (!b) = c := by decide
    simpa only [flip,ite_true] using hh (a e) (sign v e) hne
  · intro hi
    constructor
    · rintro ⟨f,hf,he⟩
      have hne : f ≠ e := fun h => hi (h ▸ hf)
      exact ⟨f,hf,by simpa [flip,hne] using he⟩
    · rintro ⟨f,hf,he⟩
      have hne : f ≠ e := fun h => hi (h ▸ hf)
      exact ⟨f,hf,by simpa [flip,hne] using he⟩

theorem entails_mono {P : V → Predicate E} {S T : Finset V} {Q : Predicate E}
    (h : S ⊆ T) (hS : Entails P S Q) : Entails P T Q :=
  fun a ha => hS a (fun v hv => ha v (h hv))

theorem entails_combine {P : V → Predicate E} {S T : Finset V} {Q R U : Predicate E}
    (hS : Entails P S Q) (hT : Entails P T R)
    (h : ∀ a, Q a → R a → U a) : Entails P (S ∪ T) U :=
  fun a ha => h a (hS a (fun v hv => ha v (Finset.mem_union_left _ hv)))
    (hT a (fun v hv => ha v (Finset.mem_union_right _ hv)))

/-- Minimal support in constraints forces all uniquely incident boundary
variables to occur in any semantic support of the conclusion. -/
theorem minimal_boundary_support
    {I : V → E → Prop} {P : V → Predicate E} (hflip : RepairLaw I P)
    {S : Finset V} {Q : Predicate E} {F : Finset E}
    (hS : Entails P S Q)
    (hmin : ∀ v ∈ S, ¬ Entails P (S.erase v) Q)
    (hF : Depends Q F) :
    ∀ e, Boundary I S e → e ∈ F := by
  classical
  intro e he
  by_contra hnot
  obtain ⟨v,hv,hI,huniq⟩ := he
  apply hmin v hv
  intro a ha
  by_cases hpa : P v a
  · apply hS a
    intro w hw
    by_cases h : w = v
    · simpa [h] using hpa
    · exact ha w (Finset.mem_erase.mpr ⟨h,hw⟩)
  · have hAll : ∀ w ∈ S, P w (flip a e) := by
      intro w hw
      by_cases h : w = v
      · subst w
        exact (hflip v e a).1 hI hpa
      · have hi : ¬ I w e := fun hh => h (huniq w hw hh)
        exact ((hflip w e a).2 hi).2 (ha w (Finset.mem_erase.mpr ⟨h,hw⟩))
    have hQ := hS (flip a e) hAll
    have hEq : ∀ f ∈ F, (flip a e) f = a f := by
      intro f hf
      have hne : f ≠ e := fun h => hnot (h ▸ hf)
      simp [flip,hne]
    exact (hF (flip a e) a hEq).1 hQ

/-- Proof lines can be arbitrary predicates, not merely clauses.
Each line has a claimed finite semantic support of size at most w.
Only unary/input and binary semantic inference are allowed. -/
inductive Derivation (P : V → Predicate E) (w : Nat) : Predicate E → Prop
  | initial (v : V) (Q : Predicate E) (F : Finset E) :
      Depends Q F → F.card ≤ w → (∀ a, P v a → Q a) → Derivation P w Q
  | combine {Q R U : Predicate E} (F : Finset E) :
      Derivation P w Q → Derivation P w R → Depends U F → F.card ≤ w →
      (∀ a, Q a → R a → U a) → Derivation P w U

def Small (P : V → Predicate E) (k : Nat) (Q : Predicate E) : Prop :=
  ∃ S : Finset V, S.card ≤ k ∧ Entails P S Q

theorem minimal_witness {P : V → Predicate E} {Q : Predicate E}
    (T : Finset V) (hT : Entails P T Q) :
    ∃ S ⊆ T, Entails P S Q ∧ ∀ v ∈ S, ¬ Entails P (S.erase v) Q := by
  classical
  induction T using Finset.strongInductionOn with
  | _ T ih =>
    by_cases h : ∃ v ∈ T, Entails P (T.erase v) Q
    · obtain ⟨v,hv,hv'⟩ := h
      obtain ⟨S,hS,hs,hmin⟩ := ih (T.erase v) (Finset.erase_ssubset hv) hv'
      exact ⟨S,hS.trans (Finset.erase_subset _ _),hs,hmin⟩
    · exact ⟨T,Finset.Subset.refl _,hT,fun v hv he => h ⟨v,hv,he⟩⟩

/-- The first transition from small to non-small entailment produces a
balanced deletion-minimal witness, even for arbitrarily strong binary
semantic inference between predicates. -/
theorem crossing_witness {P : V → Predicate E} {w k : Nat}
    (hk : 1 ≤ k) {Q : Predicate E}
    (hD : Derivation P w Q) (hlarge : ¬ Small P k Q) :
    ∃ (R : Predicate E) (F : Finset E) (S : Finset V),
      Depends R F ∧ F.card ≤ w ∧ k < S.card ∧ S.card ≤ 2*k ∧
      Entails P S R ∧ (∀ v ∈ S, ¬ Entails P (S.erase v) R) := by
  classical
  induction hD with
  | initial v Q F hF hw h =>
      exfalso
      apply hlarge
      refine ⟨{v},by simpa using hk,?_⟩
      intro a ha
      exact h a (ha v (by simp))
  | @combine Q R U F hq hr hF hw h ihq ihr =>
      by_cases hqs : Small P k Q
      · by_cases hrs : Small P k R
        · obtain ⟨S,hs,hS⟩ := hqs
          obtain ⟨T,ht,hT⟩ := hrs
          obtain ⟨M,hm,hM,hmin⟩ := minimal_witness (S∪T) (entails_combine hS hT h)
          refine ⟨U,F,M,hF,hw,?_,?_,hM,hmin⟩
          · by_contra hn
            exact hlarge ⟨M,by omega,hM⟩
          · have h1 := Finset.card_le_card hm
            have h2 := Finset.card_union_le S T
            omega
        · exact ihr hrs
      · exact ihq hqs

/-- A semantic lower bound, independent of representation and evaluation cost.
If all small subsystems are satisfiable and balanced subsystems have more
than w uniquely incident variables, no width-w binary semantic refutation
exists. -/
theorem no_narrow_semantic_refutation
    {I : V → E → Prop} {P : V → Predicate E} {w k : Nat}
    (hk : 1 ≤ k) (hflip : RepairLaw I P)
    (hsat : ∀ S : Finset V, S.card ≤ k → ∃ a, ∀ v ∈ S, P v a)
    (hexp : ∀ S : Finset V, k < S.card → S.card ≤ 2*k →
      ∀ F : Finset E, (∀ e, Boundary I S e → e ∈ F) → w < F.card) :
    ¬ Derivation P w (fun _ => False) := by
  intro hD
  have hl : ¬ Small P k (fun _ => False) := by
    rintro ⟨S,hs,hS⟩
    obtain ⟨a,ha⟩ := hsat S hs
    exact hS a ha
  obtain ⟨R,F,S,hF,hw,hl,hu,hS,hmin⟩ := crossing_witness hk hD hl
  exact (not_lt_of_ge hw) (hexp S hl hu F (minimal_boundary_support hflip hS hmin hF))

end PNPAbove.WP37
