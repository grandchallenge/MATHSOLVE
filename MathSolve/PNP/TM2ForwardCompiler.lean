import MathSolve.PNP.TM2ProgrammeRewindRun
import MathSolve.PNP.ModelBridge

/-!
# Quantitative FinTM2-to-Programme compiler

This file composes the exact startup execution proof with the fixed-step
relational simulation and the imported polynomial-time witness.  The resulting
Programme decider has runtime

`2 * input.length + 2 + tm2ProgrammeStepFactor * source.time(input.length)`.

No asymptotic substitution is used in the machine-level theorem.
-/

namespace MathSolve.PNP

noncomputable section

/-- Exact target runtime used by the concrete forward compiler. -/
def tm2ProgrammeRuntime {decision : List Bool → Bool}
    (source : ImportedTM2Witness decision) : BinaryRuntimeCost :=
  fun input =>
    2 * input.length + 2 +
      tm2ProgrammeStepFactor source.tm * importedTM2Runtime source input

/-- The concrete Programme compiler computes exactly the same Boolean decision
function within the explicit translated runtime. -/
theorem tm2ProgrammeMachine_outputs {decision : List Bool → Bool}
    (source : ImportedTM2Witness decision) (input : List Bool) :
    (tm2ProgrammeMachine source).RunsInTime input (decision input)
      (tm2ProgrammeRuntime source input) := by
  have hsource :
      StateTransition.EvalsToInTime source.tm.step
        (Turing.initList source.tm
          (input.map source.inputAlphabet.invFun))
        (some
          (Turing.haltList source.tm
            [source.outputAlphabet.invFun (decision input)]))
        (source.time.eval input.length) := by
    simpa [Turing.TM2OutputsInTime, Computability.encodeBool] using
      source.outputsFun input
  have hready :
      TM2CfgRepresented source
        (Turing.initList source.tm
          (input.map source.inputAlphabet.invFun))
        (tm2ProgrammeReadyConfig source input) :=
    tm2ProgrammeReadyConfig_represents_init source input
  rcases fixedStepRelationalSimulation_transfer
      (tm2Programme_fixedStepSimulation source input)
      hready hsource with
    ⟨targetCfg, htarget, ⟨hsim⟩⟩
  rcases tm2Programme_startup_run source input with ⟨hstartup⟩
  have hrun :=
    StateTransition.EvalsToInTime.trans
      ((tm2ProgrammeMachine source).step input)
      (2 * input.length + 2)
      (tm2ProgrammeStepFactor source.tm * source.time.eval input.length)
      ((tm2ProgrammeMachine source).init input)
      (tm2ProgrammeReadyConfig source input)
      (some targetCfg)
      hstartup hsim
  have htime :
      StateTransition.EvalsToInTime
        ((tm2ProgrammeMachine source).step input)
        ((tm2ProgrammeMachine source).init input)
        (some targetCfg)
        (tm2ProgrammeRuntime source input) := by
    simpa [tm2ProgrammeRuntime, importedTM2Runtime,
      Nat.add_comm, Nat.add_left_comm, Nat.add_assoc] using hrun
  have hhalt :
      (Turing.haltList source.tm
        [source.outputAlphabet.invFun (decision input)]).l = none := rfl
  have hnone :
      (tm2ProgrammeMachine source).step input targetCfg = none :=
    TM2CfgRepresented.halted_step_none source input htarget hhalt
  have houtStack :
      (Turing.haltList source.tm
        [source.outputAlphabet.invFun (decision input)]).stk source.tm.k₁ =
        [source.outputAlphabet.invFun (decision input)] := by
    simp [Turing.haltList]
  have hout :
      (tm2ProgrammeMachine source).output targetCfg = some (decision input) :=
    TM2CfgRepresented.halted_output source htarget hhalt
      (decision input) houtStack
  exact ⟨targetCfg, ⟨htime⟩, hnone, hout⟩

/-- Concrete Programme decider emitted by the forward compiler. -/
def tm2ProgrammeDecider {decision : List Bool → Bool}
    (source : ImportedTM2Witness decision) :
    ProgrammeDecider decision where
  machine := tm2ProgrammeMachine source
  runtime := tm2ProgrammeRuntime source
  outputs := tm2ProgrammeMachine_outputs source

/-- The concrete forward runtime has exactly the affine overhead required by the
bridge contract. -/
theorem tm2ProgrammeRuntime_affine {decision : List Bool → Bool}
    (source : ImportedTM2Witness decision) :
    AffineSimulationOverhead
      (importedTM2Runtime source)
      (tm2ProgrammeRuntime source) := by
  refine ⟨2, 2, tm2ProgrammeStepFactor source.tm, ?_⟩
  intro input
  simp [tm2ProgrammeRuntime]
  omega

/-- Construct the quantitative imported-FinTM2 to Programme compiler required
by `PNP-BRIDGE-MODEL-001`. -/
theorem tm2ToProgrammeCompiler_constructive :
    TM2ToProgrammeCompiler := by
  intro decision source
  exact ⟨tm2ProgrammeDecider source, tm2ProgrammeRuntime_affine source⟩

#print axioms tm2ProgrammeMachine_outputs
#print axioms tm2ProgrammeRuntime_affine
#print axioms tm2ToProgrammeCompiler_constructive

end

end MathSolve.PNP
