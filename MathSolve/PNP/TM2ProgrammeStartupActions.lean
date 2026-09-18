import MathSolve.PNP.TM2ProgrammeInitialization
import MathSolve.PNP.TM2ProgrammeRunStep

/-!
# Proof-facing startup actions for the forward TM2 compiler

The concrete compiler already implements a copy/rewind prefix.  These names and
normalization lemmas expose its four administrative transition cases without
changing machine semantics.
-/

namespace MathSolve.PNP

noncomputable section

/-- Copy one visible input bit to the source input-stack work tape. -/
def tm2CopyBitAction {decision : List Bool → Bool}
    (source : ImportedTM2Witness decision) (bit : Bool)
    (readWork : Fin (tm2WorkTapeCount source) → TM2ProgrammeSymbol source.tm) :
    ProgrammeAction (TM2ProgrammeControl source) (TM2ProgrammeSymbol source.tm)
      (tm2WorkTapeCount source) where
  nextState := tm2ControlCopy source
  inputMove := .right
  write := tm2WriteSelected source readWork source.tm.k₀ (some (.inl bit))
  workMove := tm2MoveSelected source source.tm.k₀ .right

/-- Leave copy mode after the first blank input cell. -/
def tm2CopyEndAction {decision : List Bool → Bool}
    (source : ImportedTM2Witness decision)
    (readWork : Fin (tm2WorkTapeCount source) → TM2ProgrammeSymbol source.tm) :
    ProgrammeAction (TM2ProgrammeControl source) (TM2ProgrammeSymbol source.tm)
      (tm2WorkTapeCount source) where
  nextState := tm2ControlRewind source
  inputMove := .left
  write := tm2PreserveWork source readWork
  workMove := tm2MoveSelected source source.tm.k₀ .left

/-- Rewind one visible input position. -/
def tm2RewindBitAction {decision : List Bool → Bool}
    (source : ImportedTM2Witness decision)
    (readWork : Fin (tm2WorkTapeCount source) → TM2ProgrammeSymbol source.tm) :
    ProgrammeAction (TM2ProgrammeControl source) (TM2ProgrammeSymbol source.tm)
      (tm2WorkTapeCount source) where
  nextState := tm2ControlRewind source
  inputMove := .left
  write := tm2PreserveWork source readWork
  workMove := tm2MoveSelected source source.tm.k₀ .left

/-- Leave rewind mode at the blank cell immediately left of the finite input. -/
def tm2RewindEndAction {decision : List Bool → Bool}
    (source : ImportedTM2Witness decision)
    (readWork : Fin (tm2WorkTapeCount source) → TM2ProgrammeSymbol source.tm) :
    ProgrammeAction (TM2ProgrammeControl source) (TM2ProgrammeSymbol source.tm)
      (tm2WorkTapeCount source) where
  nextState := tm2ControlInitialRun source
  inputMove := .right
  write := tm2PreserveWork source readWork
  workMove := tm2MoveSelected source source.tm.k₀ .right

theorem tm2ControlCopy_ne_accept {decision : List Bool → Bool}
    (source : ImportedTM2Witness decision) :
    tm2ControlCopy source ≠ tm2ControlAccept source := by
  intro h
  cases h

theorem tm2ControlCopy_ne_reject {decision : List Bool → Bool}
    (source : ImportedTM2Witness decision) :
    tm2ControlCopy source ≠ tm2ControlReject source := by
  intro h
  cases h

theorem tm2ControlRewind_ne_accept {decision : List Bool → Bool}
    (source : ImportedTM2Witness decision) :
    tm2ControlRewind source ≠ tm2ControlAccept source := by
  intro h
  cases h

theorem tm2ControlRewind_ne_reject {decision : List Bool → Bool}
    (source : ImportedTM2Witness decision) :
    tm2ControlRewind source ≠ tm2ControlReject source := by
  intro h
  cases h

theorem tm2ControlRewind_ne_copy {decision : List Bool → Bool}
    (source : ImportedTM2Witness decision) :
    tm2ControlRewind source ≠ tm2ControlCopy source := by
  intro h
  cases h

theorem tm2ProgrammeTransition_copy_some {decision : List Bool → Bool}
    (source : ImportedTM2Witness decision) (bit : Bool)
    (readWork : Fin (tm2WorkTapeCount source) → TM2ProgrammeSymbol source.tm) :
    tm2ProgrammeTransition source (tm2ControlCopy source) (some bit) readWork =
      tm2CopyBitAction source bit readWork := by
  simp [tm2ProgrammeTransition, tm2CopyBitAction]

theorem tm2ProgrammeTransition_copy_none {decision : List Bool → Bool}
    (source : ImportedTM2Witness decision)
    (readWork : Fin (tm2WorkTapeCount source) → TM2ProgrammeSymbol source.tm) :
    tm2ProgrammeTransition source (tm2ControlCopy source) none readWork =
      tm2CopyEndAction source readWork := by
  simp [tm2ProgrammeTransition, tm2CopyEndAction]

theorem tm2ProgrammeTransition_rewind_some {decision : List Bool → Bool}
    (source : ImportedTM2Witness decision) (bit : Bool)
    (readWork : Fin (tm2WorkTapeCount source) → TM2ProgrammeSymbol source.tm) :
    tm2ProgrammeTransition source (tm2ControlRewind source) (some bit) readWork =
      tm2RewindBitAction source readWork := by
  simp [tm2ProgrammeTransition, tm2ControlRewind_ne_copy source,
    tm2RewindBitAction]

theorem tm2ProgrammeTransition_rewind_none {decision : List Bool → Bool}
    (source : ImportedTM2Witness decision)
    (readWork : Fin (tm2WorkTapeCount source) → TM2ProgrammeSymbol source.tm) :
    tm2ProgrammeTransition source (tm2ControlRewind source) none readWork =
      tm2RewindEndAction source readWork := by
  simp [tm2ProgrammeTransition, tm2ControlRewind_ne_copy source,
    tm2RewindEndAction]

/-- Exact Programme step for one visible input bit in copy mode. -/
theorem tm2ProgrammeMachine_step_copy_some {decision : List Bool → Bool}
    (source : ImportedTM2Witness decision) (input : List Bool)
    (cfg : ProgrammeConfig (tm2ProgrammeMachine source)) (bit : Bool)
    (hstate : cfg.state = tm2ControlCopy source)
    (hread : programmeInputRead input cfg.inputHead = some bit) :
    (tm2ProgrammeMachine source).step input cfg =
      some (cfg.afterAction (tm2CopyBitAction source bit cfg.readWork)) := by
  rw [(tm2ProgrammeMachine source).step_eq_some_afterAction input cfg]
  · simp [ProgrammeMachine.actionAt, tm2ProgrammeMachine, hstate, hread,
      tm2ProgrammeTransition_copy_some]
  · simpa [tm2ProgrammeMachine, hstate] using
      tm2ControlCopy_ne_accept source
  · simpa [tm2ProgrammeMachine, hstate] using
      tm2ControlCopy_ne_reject source

/-- Exact Programme step leaving copy mode at the first blank. -/
theorem tm2ProgrammeMachine_step_copy_none {decision : List Bool → Bool}
    (source : ImportedTM2Witness decision) (input : List Bool)
    (cfg : ProgrammeConfig (tm2ProgrammeMachine source))
    (hstate : cfg.state = tm2ControlCopy source)
    (hread : programmeInputRead input cfg.inputHead = none) :
    (tm2ProgrammeMachine source).step input cfg =
      some (cfg.afterAction (tm2CopyEndAction source cfg.readWork)) := by
  rw [(tm2ProgrammeMachine source).step_eq_some_afterAction input cfg]
  · simp [ProgrammeMachine.actionAt, tm2ProgrammeMachine, hstate, hread,
      tm2ProgrammeTransition_copy_none]
  · simpa [tm2ProgrammeMachine, hstate] using
      tm2ControlCopy_ne_accept source
  · simpa [tm2ProgrammeMachine, hstate] using
      tm2ControlCopy_ne_reject source

/-- Exact Programme step for one visible input bit in rewind mode. -/
theorem tm2ProgrammeMachine_step_rewind_some {decision : List Bool → Bool}
    (source : ImportedTM2Witness decision) (input : List Bool)
    (cfg : ProgrammeConfig (tm2ProgrammeMachine source)) (bit : Bool)
    (hstate : cfg.state = tm2ControlRewind source)
    (hread : programmeInputRead input cfg.inputHead = some bit) :
    (tm2ProgrammeMachine source).step input cfg =
      some (cfg.afterAction (tm2RewindBitAction source cfg.readWork)) := by
  rw [(tm2ProgrammeMachine source).step_eq_some_afterAction input cfg]
  · simp [ProgrammeMachine.actionAt, tm2ProgrammeMachine, hstate, hread,
      tm2ProgrammeTransition_rewind_some]
  · simpa [tm2ProgrammeMachine, hstate] using
      tm2ControlRewind_ne_accept source
  · simpa [tm2ProgrammeMachine, hstate] using
      tm2ControlRewind_ne_reject source

/-- Exact Programme step leaving rewind mode at the left blank. -/
theorem tm2ProgrammeMachine_step_rewind_none {decision : List Bool → Bool}
    (source : ImportedTM2Witness decision) (input : List Bool)
    (cfg : ProgrammeConfig (tm2ProgrammeMachine source))
    (hstate : cfg.state = tm2ControlRewind source)
    (hread : programmeInputRead input cfg.inputHead = none) :
    (tm2ProgrammeMachine source).step input cfg =
      some (cfg.afterAction (tm2RewindEndAction source cfg.readWork)) := by
  rw [(tm2ProgrammeMachine source).step_eq_some_afterAction input cfg]
  · simp [ProgrammeMachine.actionAt, tm2ProgrammeMachine, hstate, hread,
      tm2ProgrammeTransition_rewind_none]
  · simpa [tm2ProgrammeMachine, hstate] using
      tm2ControlRewind_ne_accept source
  · simpa [tm2ProgrammeMachine, hstate] using
      tm2ControlRewind_ne_reject source

#print axioms tm2ProgrammeTransition_copy_some
#print axioms tm2ProgrammeTransition_copy_none
#print axioms tm2ProgrammeTransition_rewind_some
#print axioms tm2ProgrammeTransition_rewind_none
#print axioms tm2ProgrammeMachine_step_copy_some
#print axioms tm2ProgrammeMachine_step_copy_none
#print axioms tm2ProgrammeMachine_step_rewind_some
#print axioms tm2ProgrammeMachine_step_rewind_none

end

end MathSolve.PNP
