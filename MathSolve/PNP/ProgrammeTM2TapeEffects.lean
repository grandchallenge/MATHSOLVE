import MathSolve.PNP.ProgrammeTM2Operational
import MathSolve.PNP.ProgrammeTM2TapeOps

/-!
# Tape effects of the reverse Programme-to-TM2 operational normal form

This file identifies the pure stack updates from `ProgrammeTM2Operational`
with ordinary two-way tape movement/write operations.  These lemmas are the
local algebra needed to prove preservation of `ProgrammeTM2Represents`.
-/

namespace MathSolve.PNP

noncomputable section

open Turing

/-- Input tape view of an arbitrary reverse-simulator state/stack pair. -/
def programmeTM2InputTapeOf (M : ProgrammeMachine)
    (s : ProgrammeTM2State M) (stk : ProgrammeTM2Stacks M) :
    Turing.Tape (Option Bool) :=
  programmeTM2InputTapeRaw s.inputSymbol
    (stk .inputLeft) (stk .inputRight)

/-- Work tape view of an arbitrary reverse-simulator state/stack pair. -/
def programmeTM2WorkTapeOf (M : ProgrammeMachine)
    (s : ProgrammeTM2State M) (stk : ProgrammeTM2Stacks M)
    (tape : Fin M.workTapeCount) : Turing.Tape M.Symbol :=
  programmeTM2WorkTapeRaw (M := M) (s.workSymbol tape)
    (stk (.workLeft tape)) (stk (.workRight tape))

/-- Freezing a state does not change its represented input tape. -/
theorem programmeTM2InputTapeOf_snapshot
    (M : ProgrammeMachine) (s : ProgrammeTM2State M)
    (stk : ProgrammeTM2Stacks M) :
    programmeTM2InputTapeOf M (s.snapshot M) stk =
      programmeTM2InputTapeOf M s stk := by
  rfl

/-- Freezing a state does not change any represented work tape. -/
theorem programmeTM2WorkTapeOf_snapshot
    (M : ProgrammeMachine) (s : ProgrammeTM2State M)
    (stk : ProgrammeTM2Stacks M) (tape : Fin M.workTapeCount) :
    programmeTM2WorkTapeOf M (s.snapshot M) stk tape =
      programmeTM2WorkTapeOf M s stk tape := by
  rfl

/-- The frozen action in a freshly snapshotted state is exactly the transition
selected from the visible observation before the snapshot. -/
theorem programmeTM2_snapshotAction_snapshot
    (M : ProgrammeMachine) (s : ProgrammeTM2State M) :
    ProgrammeTM2State.snapshotAction M (s.snapshot M) =
      M.transition s.control s.inputSymbol s.workSymbol := by
  rfl

/-- Input movement does not alter the frozen action fields. -/
theorem programmeTM2AfterInput_snapshotAction
    (M : ProgrammeMachine) (s : ProgrammeTM2State M)
    (stk : ProgrammeTM2Stacks M) :
    ProgrammeTM2State.snapshotAction M
        (programmeTM2AfterInputState M s stk) =
      ProgrammeTM2State.snapshotAction M s := by
  unfold programmeTM2AfterInputState ProgrammeTM2State.snapshotAction
  split <;> rfl

/-- A work-tape update does not alter the frozen action fields. -/
theorem programmeTM2AfterWork_snapshotAction
    (M : ProgrammeMachine) (tape : Fin M.workTapeCount)
    (s : ProgrammeTM2State M) (stk : ProgrammeTM2Stacks M) :
    ProgrammeTM2State.snapshotAction M
        (programmeTM2AfterWorkState M tape s stk) =
      ProgrammeTM2State.snapshotAction M s := by
  unfold programmeTM2AfterWorkState ProgrammeTM2State.snapshotAction
  split <;> rfl

/-- Exact input-tape effect of the frozen Programme input-head movement.

The hypothesis holds for the freshly snapshotted state used by the run
transition. -/
theorem programmeTM2AfterInput_inputTape
    (M : ProgrammeMachine) (s : ProgrammeTM2State M)
    (stk : ProgrammeTM2Stacks M)
    (hsymbol : s.snapshotInputSymbol = s.inputSymbol) :
    programmeTM2InputTapeOf M
        (programmeTM2AfterInputState M s stk)
        (programmeTM2AfterInputStacks M s stk) =
      match (ProgrammeTM2State.snapshotAction M s).inputMove with
      | .left => (programmeTM2InputTapeOf M s stk).move Turing.Dir.left
      | .stay => programmeTM2InputTapeOf M s stk
      | .right => (programmeTM2InputTapeOf M s stk).move Turing.Dir.right := by
  cases hmove : (ProgrammeTM2State.snapshotAction M s).inputMove
  · simpa [programmeTM2InputTapeOf, programmeTM2AfterInputState,
      programmeTM2AfterInputStacks, hmove, Function.update, hsymbol] using
      (programmeTM2InputTapeRaw_move_left s.inputSymbol
        (stk .inputLeft) (stk .inputRight))
  · simp [programmeTM2InputTapeOf, programmeTM2AfterInputState,
      programmeTM2AfterInputStacks, hmove]
  · simpa [programmeTM2InputTapeOf, programmeTM2AfterInputState,
      programmeTM2AfterInputStacks, hmove, Function.update, hsymbol] using
      (programmeTM2InputTapeRaw_move_right s.inputSymbol
        (stk .inputLeft) (stk .inputRight))

/-- Input movement leaves every work tape unchanged. -/
theorem programmeTM2AfterInput_workTape
    (M : ProgrammeMachine) (s : ProgrammeTM2State M)
    (stk : ProgrammeTM2Stacks M) (tape : Fin M.workTapeCount) :
    programmeTM2WorkTapeOf M
        (programmeTM2AfterInputState M s stk)
        (programmeTM2AfterInputStacks M s stk) tape =
      programmeTM2WorkTapeOf M s stk tape := by
  cases hmove : (ProgrammeTM2State.snapshotAction M s).inputMove <;>
    simp [programmeTM2WorkTapeOf, programmeTM2AfterInputState,
      programmeTM2AfterInputStacks, hmove, Function.update]

/-- Canonical tape-level effect of one frozen Programme work action. -/
def programmeTM2ApplyWorkTape (M : ProgrammeMachine)
    (action : ProgrammeAction M.State M.Symbol M.workTapeCount)
    (tape : Fin M.workTapeCount) (T : Turing.Tape M.Symbol) :
    Turing.Tape M.Symbol :=
  match action.workMove tape with
  | .left => (T.write (action.write tape)).move Turing.Dir.left
  | .stay => T.write (action.write tape)
  | .right => (T.write (action.write tape)).move Turing.Dir.right

/-- Updating one work tape has exactly the expected write-then-move effect on
that tape. -/
theorem programmeTM2AfterWork_workTape_self
    (M : ProgrammeMachine) (tape : Fin M.workTapeCount)
    (s : ProgrammeTM2State M) (stk : ProgrammeTM2Stacks M) :
    programmeTM2WorkTapeOf M
        (programmeTM2AfterWorkState M tape s stk)
        (programmeTM2AfterWorkStacks M tape s stk) tape =
      programmeTM2ApplyWorkTape M
        (ProgrammeTM2State.snapshotAction M s) tape
        (programmeTM2WorkTapeOf M s stk tape) := by
  cases hmove : (ProgrammeTM2State.snapshotAction M s).workMove tape
  · simpa [programmeTM2WorkTapeOf, programmeTM2ApplyWorkTape,
      programmeTM2AfterWorkState, programmeTM2AfterWorkStacks,
      ProgrammeTM2State.setWorkSymbol, hmove, Function.update] using
      (programmeTM2WorkTapeRaw_write_move_left
        (M := M) (s.workSymbol tape)
        ((ProgrammeTM2State.snapshotAction M s).write tape)
        (stk (.workLeft tape)) (stk (.workRight tape)))
  · simpa [programmeTM2WorkTapeOf, programmeTM2ApplyWorkTape,
      programmeTM2AfterWorkState, programmeTM2AfterWorkStacks,
      ProgrammeTM2State.setWorkSymbol, hmove, Function.update] using
      (programmeTM2WorkTapeRaw_write_stay
        (M := M) (s.workSymbol tape)
        ((ProgrammeTM2State.snapshotAction M s).write tape)
        (stk (.workLeft tape)) (stk (.workRight tape)))
  · simpa [programmeTM2WorkTapeOf, programmeTM2ApplyWorkTape,
      programmeTM2AfterWorkState, programmeTM2AfterWorkStacks,
      ProgrammeTM2State.setWorkSymbol, hmove, Function.update] using
      (programmeTM2WorkTapeRaw_write_move_right
        (M := M) (s.workSymbol tape)
        ((ProgrammeTM2State.snapshotAction M s).write tape)
        (stk (.workLeft tape)) (stk (.workRight tape)))

/-- Updating one work tape leaves every different work tape unchanged. -/
theorem programmeTM2AfterWork_workTape_ne
    (M : ProgrammeMachine) {tape other : Fin M.workTapeCount}
    (hne : other ≠ tape)
    (s : ProgrammeTM2State M) (stk : ProgrammeTM2Stacks M) :
    programmeTM2WorkTapeOf M
        (programmeTM2AfterWorkState M tape s stk)
        (programmeTM2AfterWorkStacks M tape s stk) other =
      programmeTM2WorkTapeOf M s stk other := by
  cases hmove : (ProgrammeTM2State.snapshotAction M s).workMove tape <;>
    simp [programmeTM2WorkTapeOf, programmeTM2AfterWorkState,
      programmeTM2AfterWorkStacks, ProgrammeTM2State.setWorkSymbol,
      hmove, Function.update, hne]

/-- Work-tape updates leave the represented input tape unchanged. -/
theorem programmeTM2AfterWork_inputTape
    (M : ProgrammeMachine) (tape : Fin M.workTapeCount)
    (s : ProgrammeTM2State M) (stk : ProgrammeTM2Stacks M) :
    programmeTM2InputTapeOf M
        (programmeTM2AfterWorkState M tape s stk)
        (programmeTM2AfterWorkStacks M tape s stk) =
      programmeTM2InputTapeOf M s stk := by
  cases hmove : (ProgrammeTM2State.snapshotAction M s).workMove tape <;>
    simp [programmeTM2InputTapeOf, programmeTM2AfterWorkState,
      programmeTM2AfterWorkStacks, ProgrammeTM2State.setWorkSymbol,
      hmove, Function.update]

/-- The work phase preserves the frozen action selected at its entry. -/
theorem programmeTM2WorkPhase_snapshotAction
    (M : ProgrammeMachine) (tapes : List (Fin M.workTapeCount))
    (s : ProgrammeTM2State M) (stk : ProgrammeTM2Stacks M) :
    ProgrammeTM2State.snapshotAction M
        (programmeTM2WorkPhase M tapes s stk).1 =
      ProgrammeTM2State.snapshotAction M s := by
  induction tapes generalizing s stk with
  | nil =>
      rfl
  | cons tape rest ih =>
      simp only [programmeTM2WorkPhase]
      rw [ih]
      exact programmeTM2AfterWork_snapshotAction M tape s stk

/-- The whole work phase leaves the input tape unchanged. -/
theorem programmeTM2WorkPhase_inputTape
    (M : ProgrammeMachine) (tapes : List (Fin M.workTapeCount))
    (s : ProgrammeTM2State M) (stk : ProgrammeTM2Stacks M) :
    programmeTM2InputTapeOf M
        (programmeTM2WorkPhase M tapes s stk).1
        (programmeTM2WorkPhase M tapes s stk).2 =
      programmeTM2InputTapeOf M s stk := by
  induction tapes generalizing s stk with
  | nil =>
      rfl
  | cons tape rest ih =>
      simp only [programmeTM2WorkPhase]
      calc
        programmeTM2InputTapeOf M
            (programmeTM2WorkPhase M rest
              (programmeTM2AfterWorkState M tape s stk)
              (programmeTM2AfterWorkStacks M tape s stk)).1
            (programmeTM2WorkPhase M rest
              (programmeTM2AfterWorkState M tape s stk)
              (programmeTM2AfterWorkStacks M tape s stk)).2 =
          programmeTM2InputTapeOf M
            (programmeTM2AfterWorkState M tape s stk)
            (programmeTM2AfterWorkStacks M tape s stk) :=
              ih _ _
        _ = programmeTM2InputTapeOf M s stk :=
              programmeTM2AfterWork_inputTape M tape s stk

/-- If a work tape does not occur in the remaining work phase, that phase
leaves its tape view unchanged. -/
theorem programmeTM2WorkPhase_workTape_of_not_mem
    (M : ProgrammeMachine) (tapes : List (Fin M.workTapeCount))
    (s : ProgrammeTM2State M) (stk : ProgrammeTM2Stacks M)
    (targetTape : Fin M.workTapeCount)
    (hnot : targetTape ∉ tapes) :
    programmeTM2WorkTapeOf M
        (programmeTM2WorkPhase M tapes s stk).1
        (programmeTM2WorkPhase M tapes s stk).2 targetTape =
      programmeTM2WorkTapeOf M s stk targetTape := by
  induction tapes generalizing s stk with
  | nil =>
      rfl
  | cons tape rest ih =>
      have hne : targetTape ≠ tape := by
        intro h
        subst targetTape
        exact hnot (by simp)
      have hnotRest : targetTape ∉ rest := by
        intro h
        exact hnot (by simp [h])
      simp only [programmeTM2WorkPhase]
      calc
        programmeTM2WorkTapeOf M
            (programmeTM2WorkPhase M rest
              (programmeTM2AfterWorkState M tape s stk)
              (programmeTM2AfterWorkStacks M tape s stk)).1
            (programmeTM2WorkPhase M rest
              (programmeTM2AfterWorkState M tape s stk)
              (programmeTM2AfterWorkStacks M tape s stk)).2 targetTape =
          programmeTM2WorkTapeOf M
            (programmeTM2AfterWorkState M tape s stk)
            (programmeTM2AfterWorkStacks M tape s stk) targetTape :=
              ih _ _ hnotRest
        _ = programmeTM2WorkTapeOf M s stk targetTape :=
              programmeTM2AfterWork_workTape_ne M hne s stk

/-- In a duplicate-free work phase, every listed tape receives exactly its one
frozen Programme write/head movement. -/
theorem programmeTM2WorkPhase_workTape_of_mem
    (M : ProgrammeMachine) (tapes : List (Fin M.workTapeCount))
    (hnodup : tapes.Nodup)
    (s : ProgrammeTM2State M) (stk : ProgrammeTM2Stacks M)
    (targetTape : Fin M.workTapeCount)
    (hmem : targetTape ∈ tapes) :
    programmeTM2WorkTapeOf M
        (programmeTM2WorkPhase M tapes s stk).1
        (programmeTM2WorkPhase M tapes s stk).2 targetTape =
      programmeTM2ApplyWorkTape M
        (ProgrammeTM2State.snapshotAction M s) targetTape
        (programmeTM2WorkTapeOf M s stk targetTape) := by
  induction tapes generalizing s stk with
  | nil =>
      simp at hmem
  | cons tape rest ih =>
      rw [List.nodup_cons] at hnodup
      rcases hnodup with ⟨htapeNot, hrestNodup⟩
      rcases List.mem_cons.mp hmem with hEq | hmemRest
      · subst targetTape
        simp only [programmeTM2WorkPhase]
        calc
          programmeTM2WorkTapeOf M
              (programmeTM2WorkPhase M rest
                (programmeTM2AfterWorkState M tape s stk)
                (programmeTM2AfterWorkStacks M tape s stk)).1
              (programmeTM2WorkPhase M rest
                (programmeTM2AfterWorkState M tape s stk)
                (programmeTM2AfterWorkStacks M tape s stk)).2 tape =
            programmeTM2WorkTapeOf M
              (programmeTM2AfterWorkState M tape s stk)
              (programmeTM2AfterWorkStacks M tape s stk) tape :=
                programmeTM2WorkPhase_workTape_of_not_mem
                  M rest _ _ tape htapeNot
          _ = programmeTM2ApplyWorkTape M
                (ProgrammeTM2State.snapshotAction M s) tape
                (programmeTM2WorkTapeOf M s stk tape) :=
                  programmeTM2AfterWork_workTape_self M tape s stk
      · have hne : targetTape ≠ tape := by
          intro h
          subst targetTape
          exact htapeNot hmemRest
        simp only [programmeTM2WorkPhase]
        calc
          programmeTM2WorkTapeOf M
              (programmeTM2WorkPhase M rest
                (programmeTM2AfterWorkState M tape s stk)
                (programmeTM2AfterWorkStacks M tape s stk)).1
              (programmeTM2WorkPhase M rest
                (programmeTM2AfterWorkState M tape s stk)
                (programmeTM2AfterWorkStacks M tape s stk)).2 targetTape =
            programmeTM2ApplyWorkTape M
              (ProgrammeTM2State.snapshotAction M
                (programmeTM2AfterWorkState M tape s stk))
              targetTape
              (programmeTM2WorkTapeOf M
                (programmeTM2AfterWorkState M tape s stk)
                (programmeTM2AfterWorkStacks M tape s stk) targetTape) :=
                  ih hrestNodup _ _ hmemRest
          _ = programmeTM2ApplyWorkTape M
                (ProgrammeTM2State.snapshotAction M s)
                targetTape
                (programmeTM2WorkTapeOf M s stk targetTape) := by
                  rw [programmeTM2AfterWork_snapshotAction M tape s stk]
                  rw [programmeTM2AfterWork_workTape_ne M hne s stk]

/-- The canonical finite work-tape enumeration updates every Programme work
tape exactly once. -/
theorem programmeTM2WorkPhase_finRange_workTape
    (M : ProgrammeMachine)
    (s : ProgrammeTM2State M) (stk : ProgrammeTM2Stacks M)
    (tape : Fin M.workTapeCount) :
    programmeTM2WorkTapeOf M
        (programmeTM2WorkPhase M (programmeTM2WorkTapes M) s stk).1
        (programmeTM2WorkPhase M (programmeTM2WorkTapes M) s stk).2 tape =
      programmeTM2ApplyWorkTape M
        (ProgrammeTM2State.snapshotAction M s) tape
        (programmeTM2WorkTapeOf M s stk tape) := by
  apply programmeTM2WorkPhase_workTape_of_mem
  · exact List.nodup_finRange M.workTapeCount
  · exact List.mem_finRange tape

#print axioms programmeTM2AfterInput_snapshotAction
#print axioms programmeTM2AfterWork_snapshotAction
#print axioms programmeTM2AfterInput_inputTape
#print axioms programmeTM2AfterInput_workTape
#print axioms programmeTM2AfterWork_workTape_self
#print axioms programmeTM2AfterWork_workTape_ne
#print axioms programmeTM2AfterWork_inputTape
#print axioms programmeTM2WorkPhase_snapshotAction
#print axioms programmeTM2WorkPhase_inputTape
#print axioms programmeTM2WorkPhase_workTape_of_not_mem
#print axioms programmeTM2WorkPhase_workTape_of_mem
#print axioms programmeTM2WorkPhase_finRange_workTape

end

end MathSolve.PNP
