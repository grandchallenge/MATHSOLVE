import PNPAbove.WP14

namespace PNPAbove.WP15
open MIPRE MIPRE.CL MIPRE.Cost

/-! # Exact original-game value: WP14 has a perfect classical strategy

This is a falsification certificate for any unqualified hardness promotion of
WP14's otherwise genuinely conditional, full-depth source sampler.
-/

/-- A one-dimensional deterministic strategy in the *original* upstream
synchronous game model. All players always return the fixed answer. -/
def fixedStrategy {X A : Type*} [Fintype X] [Fintype A] [DecidableEq A]
    (G : SynchronousGame X A) (a0 : A) : SyncStrategy G where
  d := 1
  d_pos := Nat.one_pos
  P :=
    { M := fun _ a => if a = a0 then 1 else 0
      selfAdjoint := fun _ a => by split_ifs <;> simp
      projective := fun _ a => by split_ifs <;> simp
      normalized := fun _ => by simp [Finset.sum_ite_eq'] }

/-- Its original Born-rule value is exactly the mass of queries that accept
this constant answer. This is a full source-game strategy, not a simulated
Boolean comparator. -/
theorem fixedStrategy_value {X A : Type*} [Fintype X] [Fintype A]
    [DecidableEq A] (G : SynchronousGame X A) (a0 : A) :
    (fixedStrategy G a0).value =
      ∑ x, ∑ y, G.μ x y * (if G.D x y a0 a0 then 1 else 0) := by
  rw [SyncStrategy.value_eq]
  refine Finset.sum_congr rfl fun x _ => Finset.sum_congr rfl fun y _ => ?_
  have hM : ∀ a b, ((fixedStrategy G a0).P.M x a * (fixedStrategy G a0).P.M y b).trace.re /
      ((fixedStrategy G a0).d : ℝ) = if a = a0 ∧ b = a0 then 1 else 0 := by
    intro a b
    show ((if a = a0 then (1 : Matrix (Fin (fixedStrategy G a0).d) (Fin (fixedStrategy G a0).d) ℂ) else 0) *
      (if b = a0 then 1 else 0)).trace.re / ((fixedStrategy G a0).d : ℝ) = _
    have hd : ((fixedStrategy G a0).d : ℝ) = 1 := by simp [fixedStrategy]
    have htr : (1 : Matrix (Fin (fixedStrategy G a0).d) (Fin (fixedStrategy G a0).d) ℂ).trace = 1 := by
      rw [Matrix.trace_one, Fintype.card_fin]
      simp [fixedStrategy]
    split_ifs <;> simp_all
  simp_rw [hM]
  simp [Finset.sum_ite_eq', ite_and]

/-- A genuine upper bound for the original synchronous game supremum. -/
theorem syncValue_le_one_source {X A : Type*} [Fintype X] [Fintype A]
    [DecidableEq A] (G : SynchronousGame X A) : syncValue G ≤ 1 :=
  Real.iSup_le (fun S => S.value_le_one) zero_le_one

/-- Every source synchronous strategy has value bounded by one. -/
theorem source_strategies_bddAbove {X A : Type*} [Fintype X] [Fintype A]
    [DecidableEq A] (G : SynchronousGame X A) :
    BddAbove (Set.range fun S : SyncStrategy G => S.value) := by
  refine ⟨1, ?_⟩
  rintro r ⟨S,rfl⟩
  exact S.value_le_one

/-- The original quantum and commuting suprema cannot exceed one. -/
theorem quantumValue_le_one_source {X Y A B : Type*} [Fintype X] [Fintype Y]
    [Fintype A] [Fintype B] (G : Game X Y A B) : quantumValue G ≤ 1 :=
  Real.iSup_le (fun S => S.value_le_one) zero_le_one

theorem commValue_le_one_source {X A : Type*} [Fintype X] [Fintype A]
    [DecidableEq A] (G : SynchronousGame X A) : commValue G ≤ 1 :=
  Real.iSup_le (fun S => S.value_le_one) zero_le_one

/-- A fully source-backed constant-answer certificate for **any** native
synchronous game: a fixed accepted answer on every question pair gives a
one-dimensional (thus classical) quantum strategy of value exactly one. -/
theorem constant_answer_perfect {X A : Type*} [Fintype X] [Fintype A] [DecidableEq A]
    (G : SynchronousGame X A) (a0 : A)
    (h : ∀ x y, G.D x y a0 a0 = true) :
    (fixedStrategy G a0).value = 1 := by
  rw [fixedStrategy_value]
  simp only [h, ite_true, mul_one]
  exact G.μ_sum_one

/-- The exact original synchronous optimum is 1: no entanglement advantage
or nonzero soundness gap is possible when one constant answer wins everywhere. -/
theorem syncValue_eq_one_of_constant {X A : Type*} [Fintype X] [Fintype A]
    [DecidableEq A] (G : SynchronousGame X A) (a0 : A)
    (h : ∀ x y, G.D x y a0 a0 = true) : syncValue G = 1 := by
  apply le_antisymm (syncValue_le_one_source G)
  calc
    (1 : ℝ) = (fixedStrategy G a0).value := (constant_answer_perfect G a0 h).symm
    _ ≤ syncValue G := le_ciSup (source_strategies_bddAbove G) _

/-- In the original tensor-product definition, the quantum optimum is also
exactly 1, because the source-constructed one-dimensional synchronous
strategy lifts without loss and quantum winning probabilities cannot exceed 1. -/
theorem quantumValue_eq_one_of_constant {X A : Type*} [Fintype X] [Fintype A]
    [DecidableEq A] (G : SynchronousGame X A) (a0 : A)
    (h : ∀ x y, G.D x y a0 a0 = true) : quantumValue G.toGame = 1 := by
  apply le_antisymm (quantumValue_le_one_source _)
  calc
    (1 : ℝ) = syncValue G := (syncValue_eq_one_of_constant G a0 h).symm
    _ ≤ quantumValue G.toGame := syncValue_le_quantumValue G

/-- The original commuting model likewise has value exactly one. -/
theorem commValue_eq_one_of_constant {X A : Type*} [Fintype X] [Fintype A]
    [DecidableEq A] (G : SynchronousGame X A) (a0 : A)
    (h : ∀ x y, G.D x y a0 a0 = true) : commValue G = 1 := by
  apply le_antisymm (commValue_le_one_source _)
  calc
    (1 : ℝ) = syncValue G := (syncValue_eq_one_of_constant G a0 h).symm
    _ ≤ commValue G := syncValue_le_commValue G

/-- Original WP14 verifier as a *source-native* synchronous nonlocal game,
for every positive parameter and every answer-length budget. -/
noncomputable def wp14Game (n T : Nat) : SynchronousGame
    (WP14.conditionalVerifier.Questions n) (Verifier.Answers T) :=
  WP14.conditionalVerifier.syncGame n T (WP14.conditionalVerifier_synchronous n)

/-- The empty answer is in every original answer alphabet, including T=0. -/
def emptyAnswer (T : Nat) : Verifier.Answers T :=
  ⟨[], by simp⟩

/-- The native, original question-pair predicate accepts the same empty answer
for every question pair at every positive index. -/
theorem every_question_accepts_empty (n T : Nat) (hn : n ≠ 0)
    (x y : WP14.conditionalVerifier.Questions n) :
    (wp14Game n T).D x y (emptyAnswer T) (emptyAnswer T) = true := by
  classical
  change decide (WP14.conditionalVerifier.decider.Accepts n
    (CL.toBits x) (CL.toBits y) [] []) = true
  exact decide_eq_true (WP14.conditionalVerifier_accepts_empty n hn x y)

/-- This is a constructive witness in the *original* formal game model, not
an inferred value from sampled finite queries. -/
theorem wp14_perfect_classical (n T : Nat) (hn : n ≠ 0) :
    (fixedStrategy (wp14Game n T) (emptyAnswer T)).value = 1 := by
  exact constant_answer_perfect (wp14Game n T) (emptyAnswer T)
    (every_question_accepts_empty n T hn)

/-- Source-native exact no-gap certificate, original synchronous value. -/
theorem wp14_syncValue_eq_one (n T : Nat) (hn : n ≠ 0) :
    syncValue (wp14Game n T) = 1 := by
  exact syncValue_eq_one_of_constant (wp14Game n T) (emptyAnswer T)
    (every_question_accepts_empty n T hn)

/-- Original tensor-product quantum optimum is already classically attained. -/
theorem wp14_quantumValue_eq_one (n T : Nat) (hn : n ≠ 0) :
    quantumValue (wp14Game n T).toGame = 1 := by
  exact quantumValue_eq_one_of_constant (wp14Game n T) (emptyAnswer T)
    (every_question_accepts_empty n T hn)

/-- Original commuting optimum is likewise classically attained. -/
theorem wp14_commValue_eq_one (n T : Nat) (hn : n ≠ 0) :
    commValue (wp14Game n T) = 1 := by
  exact commValue_eq_one_of_constant (wp14Game n T) (emptyAnswer T)
    (every_question_accepts_empty n T hn)

/-- There is exactly zero quantum-versus-synchronous advantage at every
positive index, even with an arbitrarily large permitted answer alphabet. -/
theorem wp14_zero_quantum_advantage (n T : Nat) (hn : n ≠ 0) :
    quantumValue (wp14Game n T).toGame - syncValue (wp14Game n T) = 0 := by
  rw [wp14_quantumValue_eq_one n T hn, wp14_syncValue_eq_one n T hn]
  norm_num

/-- The commuting-value relaxation adds no winning probability either. -/
theorem wp14_zero_commuting_advantage (n T : Nat) (hn : n ≠ 0) :
    commValue (wp14Game n T) - syncValue (wp14Game n T) = 0 := by
  rw [wp14_commValue_eq_one n T hn, wp14_syncValue_eq_one n T hn]
  norm_num

end PNPAbove.WP15
