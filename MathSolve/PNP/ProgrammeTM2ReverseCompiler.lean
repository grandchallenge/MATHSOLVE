import MathSolve.PNP.ProgrammeTM2RunTransfer
import MathSolve.PNP.ProgrammeTM2TerminalRun
import MathSolve.PNP.TM2ForwardCompiler

/-!
# Quantitative Programme-to-FinTM2 compiler

This file composes exact reverse initialization, one-for-one Programme-step
simulation, canonical terminal cleanup, and the locked affine runtime contract.
Together with the constructive forward compiler, it closes the machine-model
bridge without asserting any P-versus-NP result.
-/

namespace MathSolve.PNP

noncomputable section

/-- Exact affine runtime budget used by the concrete reverse compiler. -/
def programmeTM2Runtime {decision : List Bool → Bool}
    (source : ProgrammeDecider decision) : BinaryRuntimeCost :=
  fun input =>
    (2 * source.machine.workTapeCount + 9) +
      3 * input.length +
      (2 * source.machine.workTapeCount + 3) * source.runtime input

/-- The concrete reverse FinTM2 computes the same Boolean decision function
within the explicit affine translated runtime. -/
theorem programmeTM2Machine_outputs {decision : List Bool → Bool}
    (source : ProgrammeDecider decision) (input : List Bool) :
    Turing.TM2OutputsInTime
      (programmeTM2Machine source.machine)
      input
      (some [decision input])
      (programmeTM2Runtime source input) := by
  let M := source.machine
  rcases source.outputs input with
    ⟨terminal, ⟨sourceRun⟩, hterminalStep, houtput⟩
  rcases programmeTM2_initialization_run M input with ⟨hinit⟩
  rcases programmeTM2_transfer_run M input sourceRun with
    ⟨target, htarget, ⟨hsim⟩⟩
  have hterminal :
      terminal.state = M.accept ∨ terminal.state = M.reject :=
    programmeTerminal_of_step_none M input terminal hterminalStep
  rcases programmeTM2_terminal_cleanup_run
      (result := decision input) htarget hterminal houtput with
    ⟨hcleanup⟩
  have hrun :=
    StateTransition.EvalsToInTime.trans
      (programmeTM2Machine M).step
      (2 * input.length + 3) sourceRun.steps
      (Turing.initList (programmeTM2Machine M) input)
      (programmeTM2ReadyInitCfg M input)
      (some target)
      hinit hsim
  have hall :=
    StateTransition.EvalsToInTime.trans
      (programmeTM2Machine M).step
      (2 * input.length + 3 + sourceRun.steps)
      (programmeTM2CleanupRuntime M input.length sourceRun.steps)
      (Turing.initList (programmeTM2Machine M) input)
      target
      (some
        (Turing.haltList (programmeTM2Machine M) [decision input]))
      hrun hcleanup
  have hactual :
      2 * input.length + 3 + sourceRun.steps +
          programmeTM2CleanupRuntime M input.length sourceRun.steps =
        (2 * M.workTapeCount + 9) +
          3 * input.length +
          (2 * M.workTapeCount + 3) * sourceRun.steps := by
    unfold programmeTM2CleanupRuntime
    ring
  have hmul :
      (2 * M.workTapeCount + 3) * sourceRun.steps ≤
        (2 * M.workTapeCount + 3) * source.runtime input :=
    Nat.mul_le_mul_left (2 * M.workTapeCount + 3) sourceRun.steps_le_m
  have hbudget :
      (2 * M.workTapeCount + 9) +
          3 * input.length +
          (2 * M.workTapeCount + 3) * sourceRun.steps ≤
        programmeTM2Runtime source input := by
    unfold programmeTM2Runtime M
    exact Nat.add_le_add_left hmul
      ((2 * M.workTapeCount + 9) + 3 * input.length)
  have hwithin :
      StateTransition.EvalsToInTime
        (programmeTM2Machine M).step
        (Turing.initList (programmeTM2Machine M) input)
        (some
          (Turing.haltList (programmeTM2Machine M) [decision input]))
        (programmeTM2Runtime source input) := by
    rw [hactual] at hall
    exact programmeTM2_evalsToInTime_mono hall hbudget
  simpa [Turing.TM2OutputsInTime] using hwithin

/-- Concrete exact-runtime TM2 decider emitted by the reverse compiler. -/
def programmeTM2TimedDecider {decision : List Bool → Bool}
    (source : ProgrammeDecider decision) :
    ImportedTM2TimedDecider decision where
  tm := programmeTM2Machine source.machine
  inputAlphabet := Equiv.refl Bool
  outputAlphabet := Equiv.refl Bool
  runtime := programmeTM2Runtime source
  outputsFun := by
    intro input
    simpa [Computability.encodeBool] using
      programmeTM2Machine_outputs source input

/-- The concrete reverse runtime is already written in the exact affine shape
required by the bridge contract. -/
theorem programmeTM2Runtime_affine {decision : List Bool → Bool}
    (source : ProgrammeDecider decision) :
    AffineSimulationOverhead source.runtime (programmeTM2Runtime source) := by
  refine
    ⟨2 * source.machine.workTapeCount + 9,
      3,
      2 * source.machine.workTapeCount + 3,
      ?_⟩
  intro input
  exact le_rfl

/-- Construct the quantitative Programme-to-imported-FinTM2 compiler required
by `PNP-BRIDGE-MODEL-001`. -/
theorem programmeToTM2Compiler_constructive :
    ProgrammeToTM2Compiler := by
  intro decision source
  exact ⟨programmeTM2TimedDecider source, programmeTM2Runtime_affine source⟩

/-- Exact class-extensional consequence of the two concrete machine compilers. -/
theorem importedTM2_iff_programmePolyTime_constructive
    (decision : List Bool → Bool) :
    ImportedTM2ComputableInPolyTime decision ↔
      ProgrammeComputableInPolyTime decision :=
  importedTM2_iff_programmePolyTime
    tm2ToProgrammeCompiler_constructive
    programmeToTM2Compiler_constructive
    decision

#print axioms programmeTM2Machine_outputs
#print axioms programmeTM2Runtime_affine
#print axioms programmeToTM2Compiler_constructive
#print axioms importedTM2_iff_programmePolyTime_constructive

end

end MathSolve.PNP
