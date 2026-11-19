import PNPAbove.WP20QuantumGlobal

namespace PNPAbove.WP20
open MIPRE MIPRE.CL MIPRE.Cost Finset
open scoped Classical

/-- Unrestricted deterministic classical two-prover game value for source
question distribution and mathematical answer-sensitive predicate. Each
prover may use a distinct arbitrary function of its own question. -/
noncomputable def deterministicValue (fA fB : Questions → Bool) : ℝ :=
  ∑ x : Questions, ∑ y : Questions,
    parityGame.μ x y *
       (if parityGame.D x y (fA x) (fB y) then (1:ℝ) else 0)

/-- Classical strategies with shared randomness form the convex hull of
deterministic local response pairs; optimizing a linear payoff is equivalent
to optimizing the deterministic functions directly. -/
noncomputable def classicalValue : ℝ :=
  ⨆ fA : Questions → Bool, ⨆ fB : Questions → Bool,
    deterministicValue fA fB

/-- Bind the *actual* original MIPRE synchronous game's CL distribution to
the uniform 512-source-seed expected deterministic outcome. -/
theorem deterministicValue_source (fA fB : Questions → Bool) :
    deterministicValue fA fB =
      (∑ z : Questions, classicalSeedWin fA fB z) / 512 := by
  change
    (∑ x : Questions, ∑ y : Questions,
      clDist aliceCL.eval bobCL.eval x y *
        (if parityAccept x y (fA x) (fB y) then (1:ℝ) else 0)) = _
  rw [clDist_payoff]
  rfl

/-- A full, uniform, all-512-seed classical CHSH upper bound. Independent
arbitrary functions for Alice and Bob are explicitly quantified, with no
shared-answer shortcut and no finite table enumeration of strategies. -/
theorem every_classical_strategy_le_three_quarters (fA fB : Questions → Bool) :
    deterministicValue fA fB ≤ (3/4:ℝ) := by
  rw [deterministicValue_source]
  exact source_classical_upper fA fB

/-- Supremum over all (possibly different) classical local answer functions
is at most 3/4; shared randomness does not improve a linear payoff. -/
theorem classicalValue_le_three_quarters :
    classicalValue ≤ (3/4:ℝ) := by
  unfold classicalValue
  refine Real.iSup_le (fun fA =>
    Real.iSup_le (fun fB => every_classical_strategy_le_three_quarters fA fB)
      (by norm_num)) (by norm_num)

/-- Exact source-native positive Bell inequality: a real two-dimensional
original MIPRE.SyncStrategy beats every unrestricted local classical strategy.
The quantum witness value is exactly 81/100, classical ≤3/4, hence the
explicit *strict* quantum/classical game-value gap ≥ 3/50. -/
theorem original_source_quantum_classical_gap :
    (3/50:ℝ) ≤ quantumValue parityGame.toGame - classicalValue ∧
    (3/50:ℝ) ≤ commValue parityGame - classicalValue ∧
    (0:ℝ) < quantumValue parityGame.toGame - classicalValue := by
  have hc := classicalValue_le_three_quarters
  obtain ⟨hq, hcomm⟩ := original_quantum_lower
  constructor
  · linarith
  constructor
  · linarith
  · linarith

end PNPAbove.WP20
