import MathSolve.PNP.ProgrammeTM2StackBudget
import MathSolve.PNP.ProgrammeTM2Cleanup
import MathSolve.PNP.TM2ForwardCompiler

/-! Complete reverse compiler from the actual execution and cleanup proofs. -/
namespace MathSolve.PNP
noncomputable section
open Turing

/-- Explicit original input-length and source-step budget, including all
initialization, run, terminal dispatch, cleanup, and output steps. -/
def programmeTM2ReverseCost (M : ProgrammeMachine) (n t : Nat) : Nat :=
  2*n+3+t+(2*M.workTapeCount+4)*(n+(M.workTapeCount+1)*t+1)+2

theorem programmeTM2_reverse_outputs {M : ProgrammeMachine} {input : List Bool}
    {result : Bool} {bound : Nat} (hrun : M.RunsInTime input result bound) :
    Nonempty (StateTransition.EvalsToInTime (programmeTM2Machine M).step
      (Turing.initList (programmeTM2Machine M) input)
      (some (Turing.haltList (programmeTM2Machine M) [result]))
      (programmeTM2ReverseCost M input.length bound)) := by
  rcases hrun with ⟨cfg,⟨hs⟩,hhalt,hout⟩
  have hterm : cfg.state = M.accept ∨ cfg.state = M.reject := by
    by_contra h
    simp [ProgrammeMachine.step,h] at hhalt
  rcases programmeTM2_simulates_from_init_budget hs with ⟨target,hrep,⟨ht⟩,hb,ho⟩
  rcases programmeTM2_terminal_cleanup_run hrep hterm hb ho with ⟨bit,hbit,⟨hc⟩⟩
  have he : bit = result := Option.some.inj (hbit.symm.trans hout)
  subst bit
  have hall := StateTransition.EvalsToInTime.trans (programmeTM2Machine M).step
    (2*input.length+3+bound)
    ((2*M.workTapeCount+4)*(input.length+(M.workTapeCount+1)*bound+1)+2)
    _ _ _ ht hc
  exact ⟨by simpa [programmeTM2ReverseCost, Nat.add_assoc] using hall⟩

/-- Machine-dependent constants are fixed independently of input length. -/
theorem programmeTM2ReverseCost_affine (M : ProgrammeMachine) (n t : Nat) :
    programmeTM2ReverseCost M n t =
      (2*M.workTapeCount+9)+(2*M.workTapeCount+6)*n+
        ((2*M.workTapeCount+4)*(M.workTapeCount+1)+1)*t := by
  unfold programmeTM2ReverseCost
  ring

/-- Construct the timed imported witness for the same Boolean decision. -/
def programmeTM2TimedDecider {decision : List Bool → Bool}
    (source : ProgrammeDecider decision) : ImportedTM2TimedDecider decision where
  toTM2ComputableAux := programmeTM2Aux source.machine
  runtime := fun input => programmeTM2ReverseCost source.machine input.length (source.runtime input)
  outputsFun := by
    intro input
    rcases programmeTM2_reverse_outputs (source.outputs input) with ⟨h⟩
    simpa [programmeTM2Aux, Turing.TM2OutputsInTime, Computability.encodeBool] using h

/-- The reverse compiler discharges the locked affine-overhead contract. -/
theorem programmeToTM2Compiler_constructive : ProgrammeToTM2Compiler := by
  intro decision source
  let w := source.machine.workTapeCount
  refine ⟨programmeTM2TimedDecider source, 2*w+9, 2*w+6, (2*w+4)*(w+1)+1, ?_⟩
  intro input
  exact le_of_eq (programmeTM2ReverseCost_affine source.machine input.length (source.runtime input))

/-- Both concrete model compilers give the unconditional class equivalence. -/
theorem importedTM2_iff_programmePolyTime_constructive (decision : List Bool → Bool) :
    ImportedTM2ComputableInPolyTime decision ↔ ProgrammeComputableInPolyTime decision :=
  importedTM2_iff_programmePolyTime tm2ToProgrammeCompiler_constructive programmeToTM2Compiler_constructive decision

#print axioms programmeTM2_reverse_outputs
#print axioms programmeTM2ReverseCost_affine
#print axioms programmeToTM2Compiler_constructive
#print axioms importedTM2_iff_programmePolyTime_constructive
end
end MathSolve.PNP
