import PNPAbove.WP37Native

namespace PNPAbove.WP37
open MIPRE MIPRE.Cost MIPRE.SAT
open scoped BigOperators

noncomputable def extend (n : Nat) (a : Assignment (Fin n × Fin n)) : Assignment Nat := by
  classical
  exact fun i => if h : ∃ e : Fin n × Fin n, edgeIndex e = i
    then a (Classical.choose h) else false

theorem induced_extend (n : Nat) (a : Assignment (Fin n × Fin n)) :
    induced n (extend n a) = a := by
  classical
  funext e
  have h : ∃ f : Fin n × Fin n, edgeIndex f = edgeIndex e := ⟨e,rfl⟩
  have he := edgeIndex_injective n (Classical.choose_spec h)
  simp [extend,induced,he]

def preSupport (n : Nat) (F : Finset Nat) : Finset (Fin n × Fin n) :=
  Finset.univ.filter fun e => edgeIndex e ∈ F

theorem preSupport_card (n : Nat) (F : Finset Nat) :
    (preSupport n F).card ≤ F.card := by
  classical
  have hh : (preSupport n F).image edgeIndex ⊆ F := by
    intro x hx
    obtain ⟨e,he,rfl⟩ := Finset.mem_image.mp hx
    exact (Finset.mem_filter.mp he).2
  rw [← Finset.card_image_of_injective (preSupport n F) (edgeIndex_injective n)]
  exact Finset.card_le_card hh

theorem extend_agreement (n : Nat) (F : Finset Nat)
    (a b : Assignment (Fin n × Fin n))
    (h : ∀ e ∈ preSupport n F, a e = b e) :
    ∀ i ∈ F, extend n a i = extend n b i := by
  classical
  intro i hi
  unfold extend
  split
  · rename_i he
    have hc : Classical.choose he ∈ preSupport n F := by
      simp [preSupport,Classical.choose_spec he,hi]
    exact h _ hc
  · rename_i he
    rfl

theorem support_pullback (n : Nat) (Q : Predicate Nat) (F : Finset Nat)
    (h : Depends Q F) :
    Depends (fun a => Q (extend n a)) (preSupport n F) := by
  intro a b hab
  exact h _ _ (extend_agreement n F a b hab)

theorem derivation_pullback {V : Type*} [DecidableEq V] (n : Nat)
    (P : V → Predicate Nat) (w : Nat) (Q : Predicate Nat)
    (h : Derivation P w Q) :
    Derivation (fun v a => P v (extend n a)) w (fun a => Q (extend n a)) := by
  induction h with
  | initial v Q F hd hw h =>
    exact .initial v _ _ (support_pullback n Q F hd)
      (le_trans (preSupport_card n F) hw) (fun a => h (extend n a))
  | @combine Q R U F hQ hR hd hw h ihQ ihR =>
    exact .combine _ ihQ ihR (support_pullback n U F hd)
      (le_trans (preSupport_card n F) hw) (fun a => h (extend n a))

theorem native_constraints_pullback (q : Nat) (root : Fin (2^q)) :
    (fun v (a : Assignment (Fin (2^q) × Fin (2^q))) =>
      (nativeConstraint q root v).eval (extend (2^q) a) = true) =
    ParityConstraint completeInc (charge root) := by
  funext v a
  apply propext
  rw [nativeConstraint_eval,induced_extend]

/-- The original SAT formula family needs high semantic support even
when proof lines can use arbitrary natural-number variable identifiers,
including identifiers absent from the input. Fixing unused variables to
false cannot increase support or destroy a sound binary derivation. -/
theorem native_semantic_width (q : Nat) (root : Fin (2^q)) (k : Nat)
    (hk : 1 ≤ k) (hN : 3*k ≤ 2^q) :
    ¬ Derivation (fun v (a : Assignment Nat) => (nativeConstraint q root v).eval a = true)
      (k*k) (fun _ => False) := by
  intro h
  have hp := derivation_pullback (2^q) _ _ _ h
  rw [native_constraints_pullback] at hp
  exact complete_quadratic_width root k hk (by simpa using hN) hp

end PNPAbove.WP37
