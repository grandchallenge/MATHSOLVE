import PNPAbove.WP37Parity

namespace PNPAbove.WP37
universe u v
variable {V : Type u} {E : Type v} [DecidableEq V] [DecidableEq E] [Fintype V] [Fintype E]
set_option linter.unusedSectionVars false

def assignOn (S : Finset E) : Assignment E := fun e => decide (e ∈ S)

theorem assignOn_empty : assignOn (∅ : Finset E) = fun _ => false := by
  funext e
  simp [assignOn]

theorem assignOn_insert {S : Finset E} {e : E} (he : e ∉ S) :
    assignOn (insert e S) = flip (assignOn S) e := by
  funext f
  by_cases h : f = e
  · subst f
    simp [assignOn,flip,he]
  · simp [assignOn,flip,h]

theorem assignment_support (a : Assignment E) :
    assignOn (Finset.univ.filter fun e => a e = true) = a := by
  funext e
  cases h : a e <;> simp [assignOn,h]

/-- The entire two-way flip law class is determined by the values at zero
and its fixed incidence relation. No higher-order logical interaction in
one equation remains hidden from that data. -/
theorem flip_law_extensional {I : V → E → Prop} {P Q : V → Predicate E}
    (hP : FlipLaw I P) (hQ : FlipLaw I Q)
    (hzero : ∀ v, P v (fun _ => false) ↔ Q v (fun _ => false)) :
    ∀ v a, P v a ↔ Q v a := by
  classical
  have hS : ∀ S : Finset E, ∀ v, P v (assignOn S) ↔ Q v (assignOn S) := by
    intro S
    induction S using Finset.induction_on with
    | empty => simpa only [assignOn_empty] using hzero
    | insert e S he ih =>
      intro v
      rw [assignOn_insert he]
      by_cases h : I v e
      · rw [(hP v e _).1 h,(hQ v e _).1 h,ih v]
      · rw [(hP v e _).2 h,(hQ v e _).2 h,ih v]
  intro v a
  simpa only [assignment_support] using hS (Finset.univ.filter fun e => a e = true) v

noncomputable def zeroCharge (P : V → Predicate E) (v : V) : ZMod 2 := by
  classical
  exact if P v (fun _ => false) then 0 else 1

/-- Exact classification: every constraint family satisfying the two-way
flip law is a family of affine equations over F₂. Conversely every such
parity family satisfies the two-way law. -/
theorem flip_law_iff_affine (I : V → E → Prop) [DecidableRel I] (P : V → Predicate E) :
    FlipLaw I P ↔ ∃ c : V → ZMod 2, ∀ v a, P v a ↔ ParityConstraint I c v a := by
  classical
  constructor
  · intro h
    refine ⟨zeroCharge P,flip_law_extensional h (parity_flip_law I (zeroCharge P)) ?_⟩
    intro v
    unfold ParityConstraint parity zeroCharge
    simp [bit]
  · rintro ⟨c,hc⟩ v e a
    have h := parity_flip_law I c v e a
    constructor
    · intro hi
      rw [hc v (flip a e),hc v a]
      exact h.1 hi
    · intro hi
      rw [hc v (flip a e),hc v a]
      exact h.2 hi

end PNPAbove.WP37
