import MathSolve.PNP.TM2FixedStepSimulation

/-!
# Forward compiler initialization endpoint

This file defines the Programme configuration reached after the linear input
copy/rewind prefix and proves that it exactly represents mathlib's FinTM2
`initList` configuration.  The execution-time proof for reaching this endpoint
is a separate theorem.
-/

namespace MathSolve.PNP

noncomputable section

open Turing

/-- Work-tape contents after the exact Boolean input has been copied and rewound. -/
def tm2ProgrammeReadyWork {decision : List Bool → Bool}
    (source : ImportedTM2Witness decision) (input : List Bool) :
    Fin (tm2WorkTapeCount source) → Int → TM2ProgrammeSymbol source.tm :=
  fun tape =>
    if tape = tm2TapeEquiv source source.tm.k₀ then
      embedTM2TokenStack (input.map Sum.inl) 0
    else
      fun _ => none

/-- Programme configuration immediately before executing the imported TM2 root. -/
def tm2ProgrammeReadyConfig {decision : List Bool → Bool}
    (source : ImportedTM2Witness decision) (input : List Bool) :
    ProgrammeConfig (tm2ProgrammeMachine source) where
  state := tm2ControlInitialRun source
  inputHead := 0
  workHead := fun _ => 0
  work := tm2ProgrammeReadyWork source input

/-- The post-rewind Programme endpoint represents the exact imported FinTM2
initial configuration. -/
theorem tm2ProgrammeReadyConfig_represents_init
    {decision : List Bool → Bool}
    (source : ImportedTM2Witness decision) (input : List Bool) :
    TM2CfgRepresented source
      (Turing.initList source.tm
        (input.map source.inputAlphabet.invFun))
      (tm2ProgrammeReadyConfig source input) := by
  refine ⟨?_, ?_⟩
  · intro k
    by_cases hk : k = source.tm.k₀
    · subst k
      simpa [Turing.initList, tm2ProgrammeReadyConfig,
        tm2ProgrammeReadyWork] using
        inputTM2StackRepresented source input (0 : Int)
    · have htape :
          tm2TapeEquiv source k ≠
            tm2TapeEquiv source source.tm.k₀ := by
        intro h
        exact hk ((tm2TapeEquiv source).injective h)
      have hblankTape :
          embedTM2TokenStack ([] : List (TM2ProvenanceToken source.tm)) (0 : Int) =
            (fun _ => none) := by
        funext position
        simp [embedTM2TokenStack]
      simpa [Turing.initList, tm2ProgrammeReadyConfig,
        tm2ProgrammeReadyWork, hk, htape, hblankTape] using
        emptyTM2StackRepresented source k (0 : Int)
  · rfl

#print axioms tm2ProgrammeReadyConfig_represents_init

end

end MathSolve.PNP
