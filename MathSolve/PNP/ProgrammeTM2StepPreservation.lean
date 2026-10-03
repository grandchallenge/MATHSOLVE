import MathSolve.PNP.ProgrammeTM2TapeEffects
import MathSolve.PNP.ProgrammeStep

/-!
# Preservation of the Programme/TM2 representation across one run step

The source-side arithmetic is separated from the simulator stack algebra:
input motion reindexes offsets, and a work action writes the scanned cell then
moves the head.  The final theorem composes these facts with the operational
normal form.
-/

namespace MathSolve.PNP

noncomputable section

open Turing

/-- Tape-level input movement corresponding to one Programme head action. -/
def programmeTM2ApplyInputTape
    (move : HeadMove) (T : Turing.Tape (Option Bool)) :
    Turing.Tape (Option Bool) :=
  match move with
  | .left => T.move Turing.Dir.left
  | .stay => T
  | .right => T.move Turing.Dir.right

/-- Pointwise input representation is preserved when both source and target
heads take the same move. -/
theorem programmeTM2ApplyInputTape_nth_afterAction
    {M : ProgrammeMachine} (input : List Bool)
    (source : ProgrammeConfig M)
    (action : ProgrammeAction M.State M.Symbol M.workTapeCount)
    (T : Turing.Tape (Option Bool))
    (hrel : ∀ offset : Int,
      T.nth offset =
        programmeInputRead input (source.inputHead + offset))
    (offset : Int) :
    (programmeTM2ApplyInputTape action.inputMove T).nth offset =
      programmeInputRead input
        ((source.afterAction action).inputHead + offset) := by
  cases hmove : action.inputMove with
  | left =>
      rw [show programmeTM2ApplyInputTape action.inputMove T =
          T.move Turing.Dir.left by simp [programmeTM2ApplyInputTape, hmove]]
      rw [Turing.Tape.move_left_nth]
      rw [hrel (offset - 1)]
      apply congrArg (programmeInputRead input)
      simp [ProgrammeConfig.afterAction, hmove, HeadMove.apply]
      omega
  | stay =>
      rw [show programmeTM2ApplyInputTape action.inputMove T = T by
        simp [programmeTM2ApplyInputTape, hmove]]
      rw [hrel offset]
      apply congrArg (programmeInputRead input)
      simp [ProgrammeConfig.afterAction, hmove, HeadMove.apply]
  | right =>
      rw [show programmeTM2ApplyInputTape action.inputMove T =
          T.move Turing.Dir.right by simp [programmeTM2ApplyInputTape, hmove]]
      rw [Turing.Tape.move_right_nth]
      rw [hrel (offset + 1)]
      apply congrArg (programmeInputRead input)
      simp [ProgrammeConfig.afterAction, hmove, HeadMove.apply]
      omega

/-- Pointwise work-tape representation is preserved by the exact
write-then-move action. -/
theorem programmeTM2ApplyWorkTape_nth_afterAction
    {M : ProgrammeMachine}
    (source : ProgrammeConfig M)
    (action : ProgrammeAction M.State M.Symbol M.workTapeCount)
    (tape : Fin M.workTapeCount)
    (T : Turing.Tape M.Symbol)
    (hrel : ∀ offset : Int,
      T.nth offset =
        source.work tape (source.workHead tape + offset))
    (offset : Int) :
    (programmeTM2ApplyWorkTape M action tape T).nth offset =
      (source.afterAction action).work tape
        ((source.afterAction action).workHead tape + offset) := by
  cases hmove : action.workMove tape with
  | left =>
      simp only [programmeTM2ApplyWorkTape, hmove,
        Turing.Tape.move_left_nth, Turing.Tape.write_nth]
      by_cases hz : offset - 1 = 0
      · rw [if_pos hz]
        have hcoord :
            (source.workHead tape - 1) + offset =
              source.workHead tape := by omega
        simp [ProgrammeConfig.afterAction, hmove, HeadMove.apply,
          hcoord, Function.update]
      · rw [if_neg hz]
        rw [hrel (offset - 1)]
        have hcoord :
            (source.workHead tape - 1) + offset ≠
              source.workHead tape := by omega
        simp [ProgrammeConfig.afterAction, hmove, HeadMove.apply,
          Function.update, hcoord]
        congr 1
        omega
  | stay =>
      simp only [programmeTM2ApplyWorkTape, hmove,
        Turing.Tape.write_nth]
      by_cases hz : offset = 0
      · subst offset
        simp [ProgrammeConfig.afterAction, hmove, HeadMove.apply,
          Function.update]
      · rw [if_neg hz]
        rw [hrel offset]
        have hcoord :
            source.workHead tape + offset ≠ source.workHead tape := by
          omega
        simp [ProgrammeConfig.afterAction, hmove, HeadMove.apply,
          Function.update, hcoord]
  | right =>
      simp only [programmeTM2ApplyWorkTape, hmove,
        Turing.Tape.move_right_nth, Turing.Tape.write_nth]
      by_cases hz : offset + 1 = 0
      · rw [if_pos hz]
        have hcoord :
            (source.workHead tape + 1) + offset =
              source.workHead tape := by omega
        simp [ProgrammeConfig.afterAction, hmove, HeadMove.apply,
          hcoord, Function.update]
      · rw [if_neg hz]
        rw [hrel (offset + 1)]
        have hcoord :
            (source.workHead tape + 1) + offset ≠
              source.workHead tape := by omega
        simp [ProgrammeConfig.afterAction, hmove, HeadMove.apply,
          Function.update, hcoord]
        congr 1
        omega

#print axioms programmeTM2ApplyInputTape_nth_afterAction
#print axioms programmeTM2ApplyWorkTape_nth_afterAction

end

end MathSolve.PNP
