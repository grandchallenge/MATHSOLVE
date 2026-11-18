import PNPAbove.WP16

namespace PNPAbove.WP17
open MIPRE MIPRE.CL MIPRE.Cost Kronecker Matrix
open scoped Classical

/-! # The unconditional diagonal game-value theorem

Unlike WP16's conditional no-go, this theorem does not require every
sampled diagonal to admit an accepted answer. It proves that on a synchronous
game supported only on the question diagonal, **a deterministic classical
strategy is globally optimal even when some questions are unwinnable**.
-/

/-- A diagonal question is feasible iff there exists a winning equal answer. -/
noncomputable def feasible {X A : Type*} [Fintype X] [Fintype A]
    [DecidableEq A] (G : SynchronousGame X A) (x : X) : Prop :=
  ∃ a : A, G.D x x a a = true

/-- Numerical upper bound: sum of the sampling masses of all feasible
diagonal questions. The source game distribution and predicate are unchanged. -/
noncomputable def feasibleMass {X A : Type*} [Fintype X] [Fintype A]
    [DecidableEq A] (G : SynchronousGame X A) : ℝ := by
  classical
  exact ∑ x, G.μ x x * (if feasible G x then (1:ℝ) else 0)

/-- Every nonempty answer alphabet admits a canonical winning answer on
feasible questions, and an arbitrary answer on infeasible questions. -/
noncomputable def chooseAnswer {X A : Type*} [Fintype X] [Fintype A]
    [DecidableEq A] [Nonempty A] (G : SynchronousGame X A) (x : X) : A := by
  classical
  exact if h : feasible G x then Classical.choose h else Classical.choice inferInstance

theorem chooseAnswer_spec {X A : Type*} [Fintype X] [Fintype A]
    [DecidableEq A] [Nonempty A] (G : SynchronousGame X A) (x : X)
    (hx : feasible G x) : G.D x x (chooseAnswer G x) (chooseAnswer G x) = true := by
  classical
  simp only [chooseAnswer, dif_pos hx]
  exact Classical.choose_spec hx

/-- The chosen equal answer succeeds exactly on feasible diagonal questions. -/
theorem chooseAnswer_iff {X A : Type*} [Fintype X] [Fintype A]
    [DecidableEq A] [Nonempty A] (G : SynchronousGame X A) (x : X) :
    G.D x x (chooseAnswer G x) (chooseAnswer G x) = true ↔ feasible G x := by
  constructor
  · intro h
    exact ⟨chooseAnswer G x, h⟩
  · exact chooseAnswer_spec G x

/-- A fixed-question pair's Born-rule outcome weights sum to exactly one. -/
theorem born_rule_sum_one {X A : Type*} [Fintype X] [Fintype A]
    [DecidableEq A] (G : SynchronousGame X A)
    (S : TensorProductStrategy G.toGame) (x : X) :
    ∑ a, ∑ b,
      (star S.ψ ⬝ᵥ ((S.PA.M x a ⊗ₖ S.PB.M x b) *ᵥ S.ψ)).re = (1:ℝ) := by
  simpa [Complex.re_sum] using congrArg Complex.re (S.sum_dotProduct_kronecker x x)

/-- The diagonal winning probability of an arbitrary tensor-product
quantum strategy is bounded by 1 on feasible questions and is 0 otherwise. -/
theorem conditional_quantum_upper {X A : Type*} [Fintype X] [Fintype A]
    [DecidableEq A] (G : SynchronousGame X A)
    (S : TensorProductStrategy G.toGame) (x : X) :
    (∑ a, ∑ b, G.μ x x * (if G.D x x a b then (1:ℝ) else 0) *
      (star S.ψ ⬝ᵥ ((S.PA.M x a ⊗ₖ S.PB.M x b) *ᵥ S.ψ)).re) ≤
      G.μ x x * (if feasible G x then 1 else 0) := by
  classical
  by_cases hx : feasible G x
  · simp only [if_pos hx, mul_one]
    calc
      (∑ a, ∑ b, G.μ x x * (if G.D x x a b then (1:ℝ) else 0) *
        (star S.ψ ⬝ᵥ ((S.PA.M x a ⊗ₖ S.PB.M x b) *ᵥ S.ψ)).re)
        ≤ ∑ a, ∑ b, G.μ x x *
          (star S.ψ ⬝ᵥ ((S.PA.M x a ⊗ₖ S.PB.M x b) *ᵥ S.ψ)).re := by
          apply Finset.sum_le_sum
          intro a _
          apply Finset.sum_le_sum
          intro b _
          have hnonneg := S.re_dotProduct_nonneg x x a b
          have hμ := G.μ_nonneg x x
          by_cases hd : G.D x x a b
          · simp [hd]
          · simpa [hd] using mul_nonneg hμ hnonneg
      _ = G.μ x x * (∑ a, ∑ b,
          (star S.ψ ⬝ᵥ ((S.PA.M x a ⊗ₖ S.PB.M x b) *ᵥ S.ψ)).re) := by
          simp_rw [Finset.mul_sum]
      _ = G.μ x x := by rw [born_rule_sum_one G S x, mul_one]
  · have hD : ∀ a b, G.D x x a b = false := by
      intro a b
      by_cases hab : a = b
      · subst b
        by_contra htrue
        have hval : G.D x x a a = true := Bool.eq_true_of_ne_false htrue
        exact hx ⟨a,hval⟩
      · exact G.synchronous x a b hab
    simp [hx, hD]

/-- For a diagonal-only question law, quantum strategies have value at most
the total mass of feasible questions; this bound permits infeasible samples. -/
theorem quantum_upper_feasibleMass {X A : Type*} [Fintype X] [Fintype A]
    [DecidableEq A] (G : SynchronousGame X A)
    (hdiag : ∀ x y, x ≠ y → G.μ x y = 0)
    (S : TensorProductStrategy G.toGame) : S.value ≤ feasibleMass G := by
  classical
  change (∑ x, ∑ y, ∑ a, ∑ b,
    G.μ x y * (if G.D x y a b then (1:ℝ) else 0) *
      (star S.ψ ⬝ᵥ ((S.PA.M x a ⊗ₖ S.PB.M y b) *ᵥ S.ψ)).re) ≤ _
  unfold feasibleMass
  calc
    (∑ x, ∑ y, ∑ a, ∑ b,
      G.μ x y * (if G.D x y a b then (1:ℝ) else 0) *
      (star S.ψ ⬝ᵥ ((S.PA.M x a ⊗ₖ S.PB.M y b) *ᵥ S.ψ)).re)
      = ∑ x, ∑ a, ∑ b,
          G.μ x x * (if G.D x x a b then (1:ℝ) else 0) *
          (star S.ψ ⬝ᵥ ((S.PA.M x a ⊗ₖ S.PB.M x b) *ᵥ S.ψ)).re := by
        apply Finset.sum_congr rfl
        intro x _
        apply Finset.sum_eq_single x
        · intro y _ hy
          simp [hdiag x y (Ne.symm hy)]
        · intro h
          exact False.elim (h (Finset.mem_univ x))
    _ ≤ ∑ x, G.μ x x * (if feasible G x then (1:ℝ) else 0) := by
        apply Finset.sum_le_sum
        intro x _
        exact conditional_quantum_upper G S x


/-- Feasibility is exactly the Boolean decision outcome of the selected
question-dependent classical answer. -/
theorem chooseAnswer_indicator {X A : Type*} [Fintype X] [Fintype A]
    [DecidableEq A] [Nonempty A] (G : SynchronousGame X A) (x : X) :
    (if G.D x x (chooseAnswer G x) (chooseAnswer G x) then (1:ℝ) else 0) =
    (if feasible G x then (1:ℝ) else 0) := by
  classical
  by_cases hx : feasible G x
  · simp [hx, chooseAnswer_spec G x hx]
  · have hn : G.D x x (chooseAnswer G x) (chooseAnswer G x) = false := by
      cases hd : G.D x x (chooseAnswer G x) (chooseAnswer G x) with
      | false => rfl
      | true => exact False.elim (hx ⟨chooseAnswer G x,hd⟩)
    simp [hx,hn]

/-- Even if some sampled diagonal questions have no winning answers, the
question-dependent classical strategy attains *precisely* feasible mass. -/
theorem chosenValue_eq_feasibleMass {X A : Type*} [Fintype X] [Fintype A]
    [DecidableEq A] [Nonempty A] (G : SynchronousGame X A)
    (hdiag : ∀ x y, x ≠ y → G.μ x y = 0) :
    (WP16.chosenStrategy G (chooseAnswer G)).value = feasibleMass G := by
  classical
  rw [WP16.chosenStrategy_value]
  unfold feasibleMass
  apply Finset.sum_congr rfl
  intro x _
  have hsingle : (∑ y, G.μ x y *
      (if G.D x y (chooseAnswer G x) (chooseAnswer G y) then (1:ℝ) else 0)) =
      G.μ x x * (if G.D x x (chooseAnswer G x) (chooseAnswer G x) then 1 else 0) := by
    apply Finset.sum_eq_single x
    · intro y _ hy
      simp [hdiag x y (Ne.symm hy)]
    · intro hx
      exact False.elim (hx (Finset.mem_univ x))
  rw [hsingle, chooseAnswer_indicator G x]

/-- The feasible question mass is nonnegative because the original question
probabilities are nonnegative. -/
theorem feasibleMass_nonneg {X A : Type*} [Fintype X] [Fintype A]
    [DecidableEq A] (G : SynchronousGame X A) : 0 ≤ feasibleMass G := by
  classical
  unfold feasibleMass
  apply Finset.sum_nonneg
  intro x _
  by_cases hx : feasible G x
  · simpa [hx] using G.μ_nonneg x x
  · simp [hx]

/-- Exact quantum optimum for any native synchronous game with strictly
diagonal question support, without assuming any question is feasible. -/
theorem quantumValue_eq_feasibleMass {X A : Type*} [Fintype X] [Fintype A]
    [DecidableEq A] [Nonempty A] (G : SynchronousGame X A)
    (hdiag : ∀ x y, x ≠ y → G.μ x y = 0) :
    quantumValue G.toGame = feasibleMass G := by
  apply le_antisymm
  · exact Real.iSup_le (fun S => quantum_upper_feasibleMass G hdiag S)
      (feasibleMass_nonneg G)
  · calc
      feasibleMass G = (WP16.chosenStrategy G (chooseAnswer G)).value :=
        (chosenValue_eq_feasibleMass G hdiag).symm
      _ ≤ syncValue G := le_ciSup (WP15.source_strategies_bddAbove G) _
      _ ≤ quantumValue G.toGame := syncValue_le_quantumValue G

/-- The original synchronous optimum, attained by deterministic classical
answers, equals the original entangled optimum for *every* diagonal-support
game, including games with unsatisfiable diagonal questions. -/
theorem diagonal_quantum_no_advantage {X A : Type*} [Fintype X] [Fintype A]
    [DecidableEq A] [Nonempty A] (G : SynchronousGame X A)
    (hdiag : ∀ x y, x ≠ y → G.μ x y = 0) :
    syncValue G = quantumValue G.toGame := by
  apply le_antisymm (syncValue_le_quantumValue G)
  rw [quantumValue_eq_feasibleMass G hdiag]
  calc
    feasibleMass G = (WP16.chosenStrategy G (chooseAnswer G)).value :=
      (chosenValue_eq_feasibleMass G hdiag).symm
    _ ≤ syncValue G := le_ciSup (WP15.source_strategies_bddAbove G) _

/-- In the specific original WP14 shared-CL sampler, even an *arbitrary*
replacement source-compatible synchronous decision predicate cannot yield
quantum versus classical/synchronous value separation. There is no
feasibility assumption on accepted diagonal answers. -/
theorem wp14_unconditional_quantum_no_advantage (n T : Nat)
    (D : WP14.conditionalVerifier.Questions n → WP14.conditionalVerifier.Questions n →
      Verifier.Answers T → Verifier.Answers T → Bool)
    (hSync : ∀ x a b, a ≠ b → D x x a b = false) :
    syncValue (WP16.wp14WithDecision n T D hSync) =
      quantumValue (WP16.wp14WithDecision n T D hSync).toGame := by
  letI : Nonempty (Verifier.Answers T) := ⟨WP15.emptyAnswer T⟩
  exact diagonal_quantum_no_advantage _
    (WP16.wp14WithDecision_off_diagonal n T D hSync)


/-- In every original commuting strategy, the tracial outcome probabilities
on a fixed question pair sum to exactly one. -/
theorem commuting_born_sum_one {X A : Type*} [Fintype X] [Fintype A]
    [DecidableEq A] (G : SynchronousGame X A)
    (S : CommutingStrategy G) (x : X) :
    ∑ a, ∑ b, (S.τ (S.P.M x a * S.P.M x b)).re = (1:ℝ) := by
  have hs : ∑ a, ∑ b, S.τ (S.P.M x a * S.P.M x b) = 1 := by
    have h1 : ∀ a, ∑ b, S.τ (S.P.M x a * S.P.M x b) = S.τ (S.P.M x a) :=
      fun a => by
        rw [← map_sum, ← Finset.mul_sum, S.P.normalized, mul_one]
    simp_rw [h1]
    rw [← map_sum, S.P.normalized, S.τ.map_one]
  simpa [Complex.re_sum] using congrArg Complex.re hs

/-- For any original commuting strategy, diagonal winning probability is
bounded by one if the question is feasible, and zero if infeasible. -/
theorem commuting_conditional_upper {X A : Type*} [Fintype X] [Fintype A]
    [DecidableEq A] (G : SynchronousGame X A)
    (S : CommutingStrategy G) (x : X) :
    (∑ a, ∑ b, G.μ x x * (if G.D x x a b then (1:ℝ) else 0) *
      (S.τ (S.P.M x a * S.P.M x b)).re) ≤
      G.μ x x * (if feasible G x then 1 else 0) := by
  classical
  by_cases hx : feasible G x
  · simp only [if_pos hx, mul_one]
    calc
      (∑ a, ∑ b, G.μ x x * (if G.D x x a b then (1:ℝ) else 0) *
        (S.τ (S.P.M x a * S.P.M x b)).re)
        ≤ ∑ a, ∑ b, G.μ x x * (S.τ (S.P.M x a * S.P.M x b)).re := by
          apply Finset.sum_le_sum
          intro a _
          apply Finset.sum_le_sum
          intro b _
          have hre := S.τ.re_nonneg_mul (S.P.selfAdjoint x a) (S.P.projective x a)
            (S.P.selfAdjoint x b) (S.P.projective x b)
          have hμ := G.μ_nonneg x x
          by_cases hd : G.D x x a b
          · simp [hd]
          · simpa [hd] using mul_nonneg hμ hre
      _ = G.μ x x * (∑ a, ∑ b,
          (S.τ (S.P.M x a * S.P.M x b)).re) := by
          simp_rw [Finset.mul_sum]
      _ = G.μ x x := by rw [commuting_born_sum_one G S x, mul_one]
  · have hD : ∀ a b, G.D x x a b = false := by
      intro a b
      by_cases hab : a = b
      · subst b
        by_contra htrue
        have hval : G.D x x a a = true := Bool.eq_true_of_ne_false htrue
        exact hx ⟨a,hval⟩
      · exact G.synchronous x a b hab
    simp [hx,hD]

/-- Exact source commuting-strategy upper bound for any diagonal law,
without any feasibility assumption on individual sampled questions. -/
theorem commuting_upper_feasibleMass {X A : Type*} [Fintype X] [Fintype A]
    [DecidableEq A] (G : SynchronousGame X A)
    (hdiag : ∀ x y, x ≠ y → G.μ x y = 0)
    (S : CommutingStrategy G) : S.value ≤ feasibleMass G := by
  classical
  change (∑ x, ∑ y, ∑ a, ∑ b,
    G.μ x y * (if G.D x y a b then (1:ℝ) else 0) *
      (S.τ (S.P.M x a * S.P.M y b)).re) ≤ _
  unfold feasibleMass
  calc
    (∑ x, ∑ y, ∑ a, ∑ b,
      G.μ x y * (if G.D x y a b then (1:ℝ) else 0) *
      (S.τ (S.P.M x a * S.P.M y b)).re)
      = ∑ x, ∑ a, ∑ b,
          G.μ x x * (if G.D x x a b then (1:ℝ) else 0) *
          (S.τ (S.P.M x a * S.P.M x b)).re := by
        apply Finset.sum_congr rfl
        intro x _
        apply Finset.sum_eq_single x
        · intro y _ hy
          simp [hdiag x y (Ne.symm hy)]
        · intro h
          exact False.elim (h (Finset.mem_univ x))
    _ ≤ ∑ x, G.μ x x * (if feasible G x then (1:ℝ) else 0) := by
        apply Finset.sum_le_sum
        intro x _
        exact commuting_conditional_upper G S x

/-- Exact original commuting optimum, with no assumption that the sampled
diagonal answer predicates are satisfiable. -/
theorem commValue_eq_feasibleMass {X A : Type*} [Fintype X] [Fintype A]
    [DecidableEq A] [Nonempty A] (G : SynchronousGame X A)
    (hdiag : ∀ x y, x ≠ y → G.μ x y = 0) :
    commValue G = feasibleMass G := by
  apply le_antisymm
  · exact Real.iSup_le (fun S => commuting_upper_feasibleMass G hdiag S)
      (feasibleMass_nonneg G)
  · calc
      feasibleMass G = (WP16.chosenStrategy G (chooseAnswer G)).value :=
        (chosenValue_eq_feasibleMass G hdiag).symm
      _ ≤ syncValue G := le_ciSup (WP15.source_strategies_bddAbove G) _
      _ ≤ commValue G := syncValue_le_commValue G

/-- Full original no-gap theorem: on **all** diagonal-supported synchronous
games with nonempty answers, classical/synchronous, tensor-product quantum,
and commuting values agree. Their common value may be less than 1. -/
theorem diagonal_all_values_equal {X A : Type*} [Fintype X] [Fintype A]
    [DecidableEq A] [Nonempty A] (G : SynchronousGame X A)
    (hdiag : ∀ x y, x ≠ y → G.μ x y = 0) :
    syncValue G = quantumValue G.toGame ∧
      quantumValue G.toGame = commValue G := by
  constructor
  · exact diagonal_quantum_no_advantage G hdiag
  · rw [quantumValue_eq_feasibleMass G hdiag, commValue_eq_feasibleMass G hdiag]

/-- WP14's unchanged original diagonal sampler rules out a quantum/synchronous
**and** a commuting/synchronous value gap for every replacement synchronous
predicate, even if some diagonal questions are impossible to win. -/
theorem wp14_unconditional_all_values_equal (n T : Nat)
    (D : WP14.conditionalVerifier.Questions n → WP14.conditionalVerifier.Questions n →
      Verifier.Answers T → Verifier.Answers T → Bool)
    (hSync : ∀ x a b, a ≠ b → D x x a b = false) :
    syncValue (WP16.wp14WithDecision n T D hSync) =
      quantumValue (WP16.wp14WithDecision n T D hSync).toGame ∧
    quantumValue (WP16.wp14WithDecision n T D hSync).toGame =
      commValue (WP16.wp14WithDecision n T D hSync) := by
  letI : Nonempty (Verifier.Answers T) := ⟨WP15.emptyAnswer T⟩
  exact diagonal_all_values_equal _
    (WP16.wp14WithDecision_off_diagonal n T D hSync)

end PNPAbove.WP17
