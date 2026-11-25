import MathSolve.PNP.ProgrammeTM2StepSimulation
import MathSolve.PNP.ProgrammeStep

/-!
# Actual terminal transition of the reverse Programme-to-TM2 simulator

On a represented accepting or rejecting Programme state, the concrete FinTM2
machine must not simulate a further source transition.  Instead, its next TM2
step selects the raw-input cleanup phase; the finite result selector agrees
with the source Programme machine's terminal output.  These are literal
facts about the executable stepAux program, not a substituted output oracle.

Termination of the entire cleanup sweep and its budget is separate work.
-/

namespace MathSolve.PNP

noncomputable section

open Turing

/-- Literal post-step target of the first terminal-to-cleanup transition. -/
def programmeTM2TerminalEntry (M : ProgrammeMachine)
    (target : (programmeTM2Machine M).Cfg) : (programmeTM2Machine M).Cfg :=
  { l := some (.cleanRaw)
    var := { target.var with mode := .cleanRaw }
    stk := target.stk }

/-- An accepting represented Programme state enters cleanup in exactly one
actual FinTM2 transition. -/
theorem programmeTM2_step_accept_enters_cleanup
    {M : ProgrammeMachine} {input : List Bool}
    {source : ProgrammeConfig M} {target : (programmeTM2Machine M).Cfg}
    (hrep : ProgrammeTM2Represents M input source target)
    (haccept : source.state = M.accept) :
    (programmeTM2Machine M).step target =
      some (programmeTM2TerminalEntry M target) := by
  rcases target with ⟨l, v, S⟩
  rcases hrep with ⟨hlabel, _, hcontrol, _, _⟩
  cases l with
  | none => simp at hlabel
  | some label =>
      have hl : label = ProgrammeTM2Mode.run := Option.some.inj hlabel
      subst label
      have hc : v.control = M.accept := hcontrol.trans haccept
      simp [Turing.FinTM2.step, Turing.TM2.step,
        programmeTM2Machine, programmeTM2Program,
        programmeTM2TerminalEntry, hc]

/-- A rejecting represented Programme state enters the same cleanup mode,
without accidentally following the ordinary nonterminal transition. -/
theorem programmeTM2_step_reject_enters_cleanup
    {M : ProgrammeMachine} {input : List Bool}
    {source : ProgrammeConfig M} {target : (programmeTM2Machine M).Cfg}
    (hrep : ProgrammeTM2Represents M input source target)
    (hreject : source.state = M.reject) :
    (programmeTM2Machine M).step target =
      some (programmeTM2TerminalEntry M target) := by
  rcases target with ⟨l, v, S⟩
  rcases hrep with ⟨hlabel, _, hcontrol, _, _⟩
  cases l with
  | none => simp at hlabel
  | some label =>
      have hl : label = ProgrammeTM2Mode.run := Option.some.inj hlabel
      subst label
      have hc : v.control = M.reject := hcontrol.trans hreject
      have hn : v.control ≠ M.accept := by
        rw [hc]
        exact M.accept_ne_reject.symm
      simp [Turing.FinTM2.step, Turing.TM2.step,
        programmeTM2Machine, programmeTM2Program,
        programmeTM2TerminalEntry, hc, hn]

/-- The finite Boolean result computed by the cleanup code agrees exactly with
the source machine's terminal output, for both accepting and rejecting states. -/
theorem programmeTM2_terminal_result_agrees_with_source
    {M : ProgrammeMachine} {input : List Bool}
    {source : ProgrammeConfig M} {target : (programmeTM2Machine M).Cfg}
    (hrep : ProgrammeTM2Represents M input source target)
    (hterm : source.state = M.accept ∨ source.state = M.reject) :
    M.output source = some (programmeTM2TerminalResult M target.var) := by
  have hc := hrep.2.2.1
  rcases hterm with ha | hr
  · have hva : target.var.control = M.accept := hc.trans ha
    simp [ProgrammeMachine.output, programmeTM2TerminalResult, ha, hva]
  · have hne : source.state ≠ M.accept := by
      rw [hr]
      exact M.accept_ne_reject.symm
    have hvr : target.var.control = M.reject := hc.trans hr
    have hvne : target.var.control ≠ M.accept := by
      rw [hvr]
      exact M.accept_ne_reject.symm
    simp [ProgrammeMachine.output, programmeTM2TerminalResult,
      hr, hne, hvr, hvne]

#print axioms programmeTM2_step_accept_enters_cleanup
#print axioms programmeTM2_step_reject_enters_cleanup
#print axioms programmeTM2_terminal_result_agrees_with_source

end
end MathSolve.PNP
