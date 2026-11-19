import PNPAbove.WP19Strategies
import PNPAbove.WP19Law

namespace PNPAbove.WP19
open MIPRE MIPRE.CL MIPRE.Cost
open scoped Classical

/-! # WP19: exact source-native star support forbids any quantum value gap

This theorem is stronger than WP18's fixed-decider negative control. It
quantifies over **every** synchronous decision predicate on the original
WP18 asymmetrically sampled question law, with no answer-feasibility
hypothesis and no requirement that the optimum equal one. -/

/-- A mathematical replacement synchronous decision predicate retaining
the EXACT original source-native WP18 conditional-linear question law.
This does not pretend an arbitrary predicate has a Cost.Prog compiler. -/
noncomputable def wp18WithDecision (n T : Nat)
    (D : WP18.asymmetricVerifier.Questions n →
      WP18.asymmetricVerifier.Questions n →
      Verifier.Answers T → Verifier.Answers T → Bool)
    (hSync : ∀ x a b, a ≠ b → D x x a b = false) :
    SynchronousGame (WP18.asymmetricVerifier.Questions n)
      (Verifier.Answers T) where
  μ := (WP18.asymmetricGame n T).μ
  μ_nonneg := (WP18.asymmetricGame n T).μ_nonneg
  μ_sum_one := (WP18.asymmetricGame n T).μ_sum_one
  D := D
  synchronous := hSync

/-- The real original WP18 sampler question distribution is a star with
isolated diagonal edges in the bipartite question graph, at every n and T. -/
theorem wp18_starMatching (n T : Nat)
    (D : WP18.asymmetricVerifier.Questions n →
      WP18.asymmetricVerifier.Questions n →
      Verifier.Answers T → Verifier.Answers T → Bool)
    (hSync : ∀ x a b, a ≠ b → D x x a b = false) :
    StarMatching (wp18WithDecision n T D hSync) center := by
  intro x y hμ
  change WP18.asymmetricSampler.dist n x y ≠ 0 at hμ
  rcases question_support n x y hμ with ⟨hc,_⟩ | ⟨hxy,h1⟩
  · exact Or.inl hc
  · right
    refine ⟨hxy, ?_⟩
    by_contra hcentre
    change WP18.asymmetricSampler.dist n center x ≠ 0 at hcentre
    rcases question_support n center x hcentre with ⟨_,h0⟩ | ⟨hc,_⟩
    · have hne : (0 : 𝔽₂) = 1 := h0.symm.trans h1
      exact zero_ne_one hne
    · rw [← hc] at h1
      exact zero_ne_one h1

/-- ORIGINAL MIPRE GAME-VALUE THEOREM: any synchronous decision predicate
on the actual native WP18 sampler has exactly equal finite-dimensional
tensor-product quantum, tracial commuting, and synchronous optima. The
winning probability need not be 1. There is no diagonal-feasibility
assumption, and the decider is arbitrary as a mathematical predicate. -/
theorem wp18_arbitrary_decider_no_quantum_advantage (n T : Nat)
    (D : WP18.asymmetricVerifier.Questions n →
      WP18.asymmetricVerifier.Questions n →
      Verifier.Answers T → Verifier.Answers T → Bool)
    (hSync : ∀ x a b, a ≠ b → D x x a b = false) :
    quantumValue (wp18WithDecision n T D hSync).toGame =
      syncValue (wp18WithDecision n T D hSync) ∧
    commValue (wp18WithDecision n T D hSync) =
      syncValue (wp18WithDecision n T D hSync) := by
  letI : Nonempty (Verifier.Answers T) := ⟨WP15.emptyAnswer T⟩
  exact star_no_advantage _ center (wp18_starMatching n T D hSync)

/-- An exact, unconditional zero-gap conclusion for the original WP18
source question law, regardless of how the synchronous predicate changes. -/
theorem wp18_all_replacement_predicates_zero_gap (n T : Nat)
    (D : WP18.asymmetricVerifier.Questions n →
      WP18.asymmetricVerifier.Questions n →
      Verifier.Answers T → Verifier.Answers T → Bool)
    (hSync : ∀ x a b, a ≠ b → D x x a b = false) :
    quantumValue (wp18WithDecision n T D hSync).toGame -
      syncValue (wp18WithDecision n T D hSync) = 0 ∧
    commValue (wp18WithDecision n T D hSync) -
      syncValue (wp18WithDecision n T D hSync) = 0 := by
  obtain ⟨hq,hc⟩ := wp18_arbitrary_decider_no_quantum_advantage n T D hSync
  rw [hq,hc]
  exact ⟨sub_self _, sub_self _⟩

end PNPAbove.WP19
