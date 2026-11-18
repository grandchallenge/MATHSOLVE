import PNPAbove.WP15

namespace PNPAbove.WP16
open MIPRE MIPRE.CL MIPRE.Cost

/-! # Diagonal-support obstruction to a source-native nonlocal value gap -/

/-- The admitted WP14 sampler uses the very same conditional nine-stage
CL presentation for both players, so *every* off-diagonal question pair has
exactly zero probability in the original source distribution. -/
theorem wp14_dist_off_diagonal (n : Nat)
    (x y : Fin 9 → 𝔽₂) (hxy : x ≠ y) :
    WP14.conditionalSampler.dist n x y = 0 := by
  change clDist WP14.conditionalNineCL.eval WP14.conditionalNineCL.eval x y = 0
  have hzero :
      (Finset.univ.filter (fun z : Fin 9 → 𝔽₂ =>
        WP14.conditionalNineCL.eval z = x ∧ WP14.conditionalNineCL.eval z = y)) = ∅ := by
    ext z
    simp only [Finset.mem_filter, Finset.mem_univ, true_and]
    constructor
    · intro hz
      exact False.elim (hxy (hz.1.symm.trans hz.2))
    · intro hz
      simp at hz
  simp [clDist, hzero]

/-- The same diagonal support holds for the actual source-native verifier's
original synchronous game at every parameter and any answer budget. -/
theorem wp14_game_off_diagonal (n T : Nat)
    (x y : WP14.conditionalVerifier.Questions n) (hxy : x ≠ y) :
    (WP15.wp14Game n T).μ x y = 0 := by
  exact wp14_dist_off_diagonal n x y hxy


/-- A one-dimensional deterministic *question-dependent* strategy in the
original upstream synchronous game. Its answer can vary with the question. -/
def chosenStrategy {X A : Type*} [Fintype X] [Fintype A] [DecidableEq A]
    (G : SynchronousGame X A) (answer : X → A) : SyncStrategy G where
  d := 1
  d_pos := Nat.one_pos
  P :=
    { M := fun x a => if a = answer x then 1 else 0
      selfAdjoint := fun _ _ => by split_ifs <;> simp
      projective := fun _ _ => by split_ifs <;> simp
      normalized := fun _ => by simp [Finset.sum_ite_eq'] }

/-- Exact original Born-rule computation for the question-dependent
classical strategy, including all off-diagonal terms. -/
theorem chosenStrategy_value {X A : Type*} [Fintype X] [Fintype A]
    [DecidableEq A] (G : SynchronousGame X A) (answer : X → A) :
    (chosenStrategy G answer).value =
      ∑ x, ∑ y, G.μ x y * (if G.D x y (answer x) (answer y) then 1 else 0) := by
  rw [SyncStrategy.value_eq]
  refine Finset.sum_congr rfl fun x _ => Finset.sum_congr rfl fun y _ => ?_
  have hM : ∀ a b, ((chosenStrategy G answer).P.M x a *
      (chosenStrategy G answer).P.M y b).trace.re /
      ((chosenStrategy G answer).d : ℝ) =
      if a = answer x ∧ b = answer y then 1 else 0 := by
    intro a b
    show ((if a = answer x then
        (1 : Matrix (Fin (chosenStrategy G answer).d)
          (Fin (chosenStrategy G answer).d) ℂ) else 0) *
        (if b = answer y then 1 else 0)).trace.re /
        ((chosenStrategy G answer).d : ℝ) = _
    have hd : ((chosenStrategy G answer).d : ℝ) = 1 := by simp [chosenStrategy]
    have htr : (1 : Matrix (Fin (chosenStrategy G answer).d)
        (Fin (chosenStrategy G answer).d) ℂ).trace = 1 := by
      rw [Matrix.trace_one, Fintype.card_fin]
      simp [chosenStrategy]
    split_ifs <;> simp_all
  simp_rw [hM]
  simp [Finset.sum_ite_eq', ite_and]

/-- Core obstruction: for any native synchronous game supported only on
identical question pairs, if one diagonal answer is accepted for each
question then a question-dependent deterministic strategy wins perfectly. -/
theorem diagonal_support_perfect {X A : Type*} [Fintype X] [Fintype A]
    [DecidableEq A] (G : SynchronousGame X A)
    (hdiag : ∀ x y, x ≠ y → G.μ x y = 0)
    (answer : X → A) (hanswer : ∀ x, G.D x x (answer x) (answer x) = true) :
    (chosenStrategy G answer).value = 1 := by
  rw [chosenStrategy_value]
  calc
    (∑ x, ∑ y, G.μ x y * (if G.D x y (answer x) (answer y) then 1 else 0)) =
        ∑ x, ∑ y, G.μ x y := by
      apply Finset.sum_congr rfl
      intro x _
      apply Finset.sum_congr rfl
      intro y _
      by_cases hxy : x = y
      · subst y
        simp [hanswer x]
      · simp [hdiag x y hxy]
    _ = 1 := G.μ_sum_one

/-- A diagonal-supported native synchronous game with a diagonal answer
selector has exact synchronous value 1; no nonzero soundness gap. -/
theorem diagonal_syncValue_one {X A : Type*} [Fintype X] [Fintype A]
    [DecidableEq A] (G : SynchronousGame X A)
    (hdiag : ∀ x y, x ≠ y → G.μ x y = 0)
    (answer : X → A) (hanswer : ∀ x, G.D x x (answer x) (answer x) = true) :
    syncValue G = 1 := by
  apply le_antisymm (WP15.syncValue_le_one_source G)
  calc
    (1 : ℝ) = (chosenStrategy G answer).value :=
      (diagonal_support_perfect G hdiag answer hanswer).symm
    _ ≤ syncValue G := le_ciSup (WP15.source_strategies_bddAbove G) _

/-- The original tensor-product and commuting models have no value advantage
when a one-dimensional diagonal-answer strategy is already perfect. -/
theorem diagonal_quantumValue_one {X A : Type*} [Fintype X] [Fintype A]
    [DecidableEq A] (G : SynchronousGame X A)
    (hdiag : ∀ x y, x ≠ y → G.μ x y = 0)
    (answer : X → A) (hanswer : ∀ x, G.D x x (answer x) (answer x) = true) :
    quantumValue G.toGame = 1 := by
  apply le_antisymm (WP15.quantumValue_le_one_source _)
  calc
    (1 : ℝ) = syncValue G := (diagonal_syncValue_one G hdiag answer hanswer).symm
    _ ≤ quantumValue G.toGame := syncValue_le_quantumValue G

theorem diagonal_commValue_one {X A : Type*} [Fintype X] [Fintype A]
    [DecidableEq A] (G : SynchronousGame X A)
    (hdiag : ∀ x y, x ≠ y → G.μ x y = 0)
    (answer : X → A) (hanswer : ∀ x, G.D x x (answer x) (answer x) = true) :
    commValue G = 1 := by
  apply le_antisymm (WP15.commValue_le_one_source _)
  calc
    (1 : ℝ) = syncValue G := (diagonal_syncValue_one G hdiag answer hanswer).symm
    _ ≤ commValue G := syncValue_le_commValue G


/-- Replace the *decision predicate*, but keep the exact original WP14
synchronous question distribution. Every such replacement must prove its
own original synchrony condition; no proof is assumed for a new decider. -/
noncomputable def wp14WithDecision (n T : Nat)
    (D : WP14.conditionalVerifier.Questions n → WP14.conditionalVerifier.Questions n →
      Verifier.Answers T → Verifier.Answers T → Bool)
    (hSync : ∀ x a b, a ≠ b → D x x a b = false) :
    SynchronousGame (WP14.conditionalVerifier.Questions n) (Verifier.Answers T) where
  μ := (WP15.wp14Game n T).μ
  μ_nonneg := (WP15.wp14Game n T).μ_nonneg
  μ_sum_one := (WP15.wp14Game n T).μ_sum_one
  D := D
  synchronous := hSync

/-- Off-diagonal pairs remain impossible **for every new source-compatible
decider** if the old sampler is retained unchanged. -/
theorem wp14WithDecision_off_diagonal (n T : Nat)
    (D : WP14.conditionalVerifier.Questions n → WP14.conditionalVerifier.Questions n →
      Verifier.Answers T → Verifier.Answers T → Bool)
    (hSync : ∀ x a b, a ≠ b → D x x a b = false)
    (x y : WP14.conditionalVerifier.Questions n) (hxy : x ≠ y) :
    (wp14WithDecision n T D hSync).μ x y = 0 :=
  wp14_game_off_diagonal n T x y hxy

/-- No-go for a decider-only repair: at any parameter and answer budget,
**any** synchronous replacement decision predicate allowing at least one
accepted equal answer for each diagonal question has exact native values
one in the classical, tensor-product and commuting models. -/
theorem wp14_decider_only_no_gap (n T : Nat)
    (D : WP14.conditionalVerifier.Questions n → WP14.conditionalVerifier.Questions n →
      Verifier.Answers T → Verifier.Answers T → Bool)
    (hSync : ∀ x a b, a ≠ b → D x x a b = false)
    (answer : WP14.conditionalVerifier.Questions n → Verifier.Answers T)
    (hwin : ∀ x, D x x (answer x) (answer x) = true) :
    syncValue (wp14WithDecision n T D hSync) = 1 ∧
    quantumValue (wp14WithDecision n T D hSync).toGame = 1 ∧
    commValue (wp14WithDecision n T D hSync) = 1 := by
  have hd := wp14WithDecision_off_diagonal n T D hSync
  exact ⟨diagonal_syncValue_one _ hd answer hwin,
    diagonal_quantumValue_one _ hd answer hwin,
    diagonal_commValue_one _ hd answer hwin⟩


/-- Even diagonal questions that are *never sampled* do not need to admit a
winning answer. Only positive-probability diagonal questions matter. -/
theorem diagonal_support_perfect_on_support {X A : Type*} [Fintype X] [Fintype A]
    [DecidableEq A] (G : SynchronousGame X A)
    (hdiag : ∀ x y, x ≠ y → G.μ x y = 0)
    (answer : X → A)
    (hanswer : ∀ x, G.μ x x ≠ 0 → G.D x x (answer x) (answer x) = true) :
    (chosenStrategy G answer).value = 1 := by
  rw [chosenStrategy_value]
  calc
    (∑ x, ∑ y, G.μ x y * (if G.D x y (answer x) (answer y) then 1 else 0)) =
        ∑ x, ∑ y, G.μ x y := by
      apply Finset.sum_congr rfl
      intro x _
      apply Finset.sum_congr rfl
      intro y _
      by_cases hxy : x = y
      · subst y
        by_cases hm : G.μ x x = 0
        · simp [hm]
        · simp [hanswer x hm]
      · simp [hdiag x y hxy]
    _ = 1 := G.μ_sum_one

/-- Source-model exact no-gap theorem under the weakest relevant pointwise
condition: every *sampled* diagonal question admits a deterministic answer. -/
theorem diagonal_values_one_on_support {X A : Type*} [Fintype X] [Fintype A]
    [DecidableEq A] (G : SynchronousGame X A)
    (hdiag : ∀ x y, x ≠ y → G.μ x y = 0)
    (answer : X → A)
    (hanswer : ∀ x, G.μ x x ≠ 0 → G.D x x (answer x) (answer x) = true) :
    syncValue G = 1 ∧ quantumValue G.toGame = 1 ∧ commValue G = 1 := by
  have hperfect := diagonal_support_perfect_on_support G hdiag answer hanswer
  have hs : syncValue G = 1 := by
    apply le_antisymm (WP15.syncValue_le_one_source G)
    calc
      (1 : ℝ) = (chosenStrategy G answer).value := hperfect.symm
      _ ≤ syncValue G := le_ciSup (WP15.source_strategies_bddAbove G) _
  exact ⟨hs,
    le_antisymm (WP15.quantumValue_le_one_source _) (by
      calc
        (1 : ℝ) = syncValue G := hs.symm
        _ ≤ quantumValue G.toGame := syncValue_le_quantumValue G),
    le_antisymm (WP15.commValue_le_one_source _) (by
      calc
        (1 : ℝ) = syncValue G := hs.symm
        _ ≤ commValue G := syncValue_le_commValue G)⟩

/-- Necessary obstruction for a quantum-classical gap under the unchanged
WP14 sampler: every winning-answer selector must fail on some sampled
question. Replacing the decider alone while retaining pointwise diagonal
feasibility cannot yield a gap. -/
theorem wp14_decider_only_gap_obstruction (n T : Nat)
    (D : WP14.conditionalVerifier.Questions n → WP14.conditionalVerifier.Questions n →
      Verifier.Answers T → Verifier.Answers T → Bool)
    (hSync : ∀ x a b, a ≠ b → D x x a b = false)
    (hgap : syncValue (wp14WithDecision n T D hSync) <
      quantumValue (wp14WithDecision n T D hSync).toGame) :
    ¬∃ answer : WP14.conditionalVerifier.Questions n → Verifier.Answers T,
      ∀ x, (wp14WithDecision n T D hSync).μ x x ≠ 0 →
        D x x (answer x) (answer x) = true := by
  rintro ⟨answer,hwin⟩
  obtain ⟨hs,hq,_⟩ := diagonal_values_one_on_support
    (wp14WithDecision n T D hSync)
    (wp14WithDecision_off_diagonal n T D hSync) answer hwin
  rw [hs,hq] at hgap
  exact (lt_irrefl (1 : ℝ)) hgap

end PNPAbove.WP16
