import MathSolve.PNP.TM2StepAuxSimulation
import MathSolve.PNP.RelationalStepSimulation

/-!
# One FinTM2 step as a bounded Programme simulation

This file lifts the structural `stepAux` theorem to the bundled FinTM2 step
function.  The initial Programme copy/rewind prefix is intentionally not part
of this relation; it is handled by the subsequent initialization theorem.
-/

namespace MathSolve.PNP

noncomputable section

open Turing

/-- One complete bundled FinTM2 step is simulated within the fixed machine-wide
Programme step factor. -/
theorem tm2Programme_fixedStepSimulation {decision : List Bool → Bool}
    (source : ImportedTM2Witness decision) (input : List Bool) :
    FixedStepRelationalSimulation
      source.tm.step
      ((tm2ProgrammeMachine source).step input)
      (TM2CfgRepresented source)
      (tm2ProgrammeStepFactor source.tm) := by
  constructor
  · intro sourceCfg sourceCfg' targetCfg hrep hstep
    rcases sourceCfg with ⟨label?, state, stackFamily⟩
    cases label? with
    | none =>
        simp [Turing.FinTM2.step, Turing.TM2.step] at hstep
    | some label =>
        have hstate :
            targetCfg.state =
              tm2ControlRun source
                (TM2StatementCode.root source.tm label) state := by
          simpa [TM2CfgRepresented] using hrep.2
        have hstacks :
            TM2StacksRepresented source stackFamily targetCfg := hrep.1
        have hsource :
            sourceCfg' =
              Turing.TM2.stepAux (source.tm.m label) state stackFamily := by
          simpa [Turing.FinTM2.step, Turing.TM2.step] using
            Option.some.inj hstep
        rcases tm2StepAux_simulates source input (source.tm.m label)
            (TM2StatementCode.root source.tm label)
            state stackFamily targetCfg rfl hstacks hstate with
          ⟨targetCfg', htarget, ⟨hrun⟩⟩
        subst sourceCfg'
        refine ⟨targetCfg', htarget, ⟨?_⟩⟩
        exact evalsToInTime_mono hrun
          (tm2ProgrammeRootCost_le_stepFactor source.tm label)
  · intro sourceCfg targetCfg hrep hhalt
    rcases sourceCfg with ⟨label?, state, stackFamily⟩
    cases label? with
    | none =>
        exact TM2CfgRepresented.halted_step_none source input hrep rfl
    | some label =>
        simp [Turing.FinTM2.step, Turing.TM2.step] at hhalt

#print axioms tm2Programme_fixedStepSimulation

end

end MathSolve.PNP
