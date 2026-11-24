import MathSolve.PNP.ProgrammeTM2InitRun
import MathSolve.PNP.ProgrammeTM2StepSimulation

/-!
# Reverse initialization followed by the first simulated Programme step

`programmeTM2ReadyInitCfg_represents` is already kernel-proved in
`ProgrammeTM2InitRun`. Re-declaring it on import conflicts with that theorem.
This module now composes the exact initialization path with the native
nonterminal transition. The remaining one-step representation-preservation
invariant, iteration, and terminal cleanup are separate obligations.
-/

namespace MathSolve.PNP

noncomputable section
open Turing

/-- The target Programme simulator performs initialization and its first
nonterminal Programme step in at most `2 * input.length + 4` native FinTM2
steps, from the actual raw binary input. No result/output correctness is
inferred until the next-state representation-preservation lemma is proved. -/
theorem programmeTM2_initial_first_step_run
    (M : ProgrammeMachine) (input : List Bool)
    (haccept : M.start ≠ M.accept) (hreject : M.start ≠ M.reject) :
    Nonempty
      (StateTransition.EvalsToInTime
        (programmeTM2Machine M).step
        (Turing.initList (programmeTM2Machine M) input)
        (some (programmeTM2RunStepTarget M (programmeTM2ReadyInitCfg M input)))
        (2 * input.length + 4)) := by
  rcases programmeTM2_initialization_run M input with ⟨hinit⟩
  have hrep : ProgrammeTM2Represents M input (M.init input)
      (programmeTM2ReadyInitCfg M input) :=
    programmeTM2ReadyInitCfg_represents M input
  have hs : (programmeTM2Machine M).step
      (programmeTM2ReadyInitCfg M input) =
      some (programmeTM2RunStepTarget M (programmeTM2ReadyInitCfg M input)) :=
    programmeTM2_step_run_nonterminal hrep
      (by simpa only [ProgrammeMachine.init] using haccept)
      (by simpa only [ProgrammeMachine.init] using hreject)
  have hstep := programmeTM2_one_step_in_time hs
  have hboth := StateTransition.EvalsToInTime.trans
    (programmeTM2Machine M).step
    (2 * input.length + 3) 1
    (Turing.initList (programmeTM2Machine M) input)
    (programmeTM2ReadyInitCfg M input)
    (some (programmeTM2RunStepTarget M (programmeTM2ReadyInitCfg M input)))
    hinit hstep
  exact ⟨by simpa [Nat.add_assoc] using hboth⟩

#print axioms programmeTM2ReadyInitCfg_represents
#print axioms programmeTM2_initial_first_step_run

end
end MathSolve.PNP
