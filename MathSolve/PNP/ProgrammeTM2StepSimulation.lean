import MathSolve.PNP.ProgrammeTM2Representation
import MathSolve.PNP.ProgrammeStep

/-!
# One-step Programme-to-TM2 simulation

This file isolates the counted-step boundary of the reverse compiler. A
nonterminal represented Programme configuration enters the concrete run
statement and the whole finite statement tree is one counted TM2 step.
-/

namespace MathSolve.PNP

noncomputable section

open Turing

/-- Concrete target configuration produced by the simulator statement for one
nonterminal Programme transition. -/
def programmeTM2RunStepTarget (M : ProgrammeMachine)
    (target : (programmeTM2Machine M).Cfg) :
    (programmeTM2Machine M).Cfg :=
  Turing.TM2.stepAux (programmeTM2RunTransition M) target.var target.stk

/-- At a represented nonterminal run configuration, the concrete reverse
machine takes exactly one counted TM2 step into its run-transition target. -/
theorem programmeTM2_step_run_nonterminal
    {M : ProgrammeMachine} {input : List Bool}
    {source : ProgrammeConfig M} {target : (programmeTM2Machine M).Cfg}
    (hrep : ProgrammeTM2Represents M input source target)
    (haccept : source.state ≠ M.accept) (hreject : source.state ≠ M.reject) :
    (programmeTM2Machine M).step target =
      some (programmeTM2RunStepTarget M target) := by
  rcases hrep with ⟨hlabel, hmode, hcontrol, _, _⟩
  rcases target with ⟨lbl, st, ss⟩
  change lbl = some (.run) at hlabel
  subst lbl
  change st.control = source.state at hcontrol
  simp only [Turing.FinTM2.step, Turing.TM2.step]
  simp [programmeTM2Machine, programmeTM2Program,
    programmeTM2RunStepTarget, hcontrol, haccept, hreject]
  rfl

#print axioms programmeTM2_step_run_nonterminal

end

end MathSolve.PNP
