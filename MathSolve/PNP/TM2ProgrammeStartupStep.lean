import MathSolve.PNP.TM2ProgrammeRunStep

/-!
# Exact Programme startup-step normal forms

Proof-facing names for the four administrative copy/rewind actions used before
the compiled Programme enters the imported TM2 root statement.
-/

namespace MathSolve.PNP

noncomputable section

/-- Copy one concrete Boolean input cell to the represented source input stack. -/
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
def tm2CopyDoneAction {decision : List Bool → Bool}
    (source : ImportedTM2Witness decision)
    (readWork : Fin (tm2WorkTapeCount source) → TM2ProgrammeSymbol source.tm) :
    ProgrammeAction (TM2ProgrammeControl source) (TM2ProgrammeSymbol source.tm)
      (tm2WorkTapeCount source) where
  nextState := tm2ControlRewind source
  inputMove := .left
  write := tm2PreserveWork source readWork
  workMove := tm2MoveSelected source source.tm.k₀ .left

/-- Rewind across one concrete Boolean input cell. -/
def tm2RewindBitAction {decision : List Bool → Bool}
    (source : ImportedTM2Witness decision)
    (readWork : Fin (tm2WorkTapeCount source) → TM2ProgrammeSymbol source.tm) :
    ProgrammeAction (TM2ProgrammeControl source) (TM2ProgrammeSymbol source.tm)
      (tm2WorkTapeCount source) where
  nextState := tm2ControlRewind source
  inputMove := .left
  write := tm2PreserveWork source readWork
  workMove := tm2MoveSelected source source.tm.k₀ .left

/-- Leave rewind mode at the blank cell immediately left of input position zero. -/
def tm2RewindDoneAction {decision : List Bool → Bool}
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

theorem tm2ProgrammeTransition_copy_some {decision : List Bool → Bool}
    (source : ImportedTM2Witness decision) (bit : Bool)
    (readWork : Fin (tm2WorkTapeCount source) → TM2ProgrammeSymbol source.tm) :
    tm2ProgrammeTransition source (tm2ControlCopy source) (some bit) readWork =
      tm2CopyBitAction source bit readWork := by
  simp [tm2ProgrammeTransition, tm2ControlCopy, tm2CopyBitAction]

theorem tm2ProgrammeTransition_copy_none {decision : List Bool → Bool}
    (source : ImportedTM2Witness decision)
    (readWork : Fin (tm2WorkTapeCount source) → TM2ProgrammeSymbol source.tm) :
    tm2ProgrammeTransition source (tm2ControlCopy source) none readWork =
      tm2CopyDoneAction source readWork := by
  simp [tm2ProgrammeTransition, tm2ControlCopy, tm2CopyDoneAction]

theorem tm2ProgrammeTransition_rewind_some {decision : List Bool → Bool}
    (source : ImportedTM2Witness decision) (bit : Bool)
    (readWork : Fin (tm2WorkTapeCount source) → TM2ProgrammeSymbol source.tm) :
    tm2ProgrammeTransition source (tm2ControlRewind source) (some bit) readWork =
      tm2RewindBitAction source readWork := by
  simp [tm2ProgrammeTransition, tm2ControlCopy, tm2ControlRewind,
    tm2RewindBitAction]

theorem tm2ProgrammeTransition_rewind_none {decision : List Bool → Bool}
    (source : ImportedTM2Witness decision)
    (readWork : Fin (tm2WorkTapeCount source) → TM2ProgrammeSymbol source.tm) :
    tm2ProgrammeTransition source (tm2ControlRewind source) none readWork =
      tm2RewindDoneAction source readWork := by
  simp [tm2ProgrammeTransition, tm2ControlCopy, tm2ControlRewind,
    tm2RewindDoneAction]

theorem tm2ProgrammeMachine_step_copy_some {decision : List Bool → Bool}
    (source : ImportedTM2Witness decision) (input : List Bool)
    (cfg : ProgrammeConfig (tm2ProgrammeMachine source))
    (bit : Bool)
    (hstate : cfg.state = tm2ControlCopy source)
    (hread : programmeInputRead input cfg.inputHead = some bit) :
    (tm2ProgrammeMachine source).step input cfg =
      some (cfg.afterAction (tm2CopyBitAction source bit cfg.readWork)) := by
  rw [(tm2ProgrammeMachine source).step_eq_some_afterAction input cfg]
  · simp [ProgrammeMachine.actionAt, tm2ProgrammeMachine, hstate, hread,
      tm2ProgrammeTransition_copy_some]
  · simpa [tm2ProgrammeMachine, hstate] using tm2ControlCopy_ne_accept source
  · simpa [tm2ProgrammeMachine, hstate] using tm2ControlCopy_ne_reject source

theorem tm2ProgrammeMachine_step_copy_none {decision : List Bool → Bool}
    (source : ImportedTM2Witness decision) (input : List Bool)
    (cfg : ProgrammeConfig (tm2ProgrammeMachine source))
    (hstate : cfg.state = tm2ControlCopy source)
    (hread : programmeInputRead input cfg.inputHead = none) :
    (tm2ProgrammeMachine source).step input cfg =
      some (cfg.afterAction (tm2CopyDoneAction source cfg.readWork)) := by
  rw [(tm2ProgrammeMachine source).step_eq_some_afterAction input cfg]
  · simp [ProgrammeMachine.actionAt, tm2ProgrammeMachine, hstate, hread,
      tm2ProgrammeTransition_copy_none]
  · simpa [tm2ProgrammeMachine, hstate] using tm2ControlCopy_ne_accept source
  · simpa [tm2ProgrammeMachine, hstate] using tm2ControlCopy_ne_reject source

theorem tm2ProgrammeMachine_step_rewind_some {decision : List Bool → Bool}
    (source : ImportedTM2Witness decision) (input : List Bool)
    (cfg : ProgrammeConfig (tm2ProgrammeMachine source))
    (bit : Bool)
    (hstate : cfg.state = tm2ControlRewind source)
    (hread : programmeInputRead input cfg.inputHead = some bit) :
    (tm2ProgrammeMachine source).step input cfg =
      some (cfg.afterAction (tm2RewindBitAction source cfg.readWork)) := by
  rw [(tm2ProgrammeMachine source).step_eq_some_afterAction input cfg]
  · simp [ProgrammeMachine.actionAt, tm2ProgrammeMachine, hstate, hread,
      tm2ProgrammeTransition_rewind_some]
  · simpa [tm2ProgrammeMachine, hstate] using tm2ControlRewind_ne_accept source
  · simpa [tm2ProgrammeMachine, hstate] using tm2ControlRewind_ne_reject source

theorem tm2ProgrammeMachine_step_rewind_none {decision : List Bool → Bool}
    (source : ImportedTM2Witness decision) (input : List Bool)
    (cfg : ProgrammeConfig (tm2ProgrammeMachine source))
    (hstate : cfg.state = tm2ControlRewind source)
    (hread : programmeInputRead input cfg.inputHead = none) :
    (tm2ProgrammeMachine source).step input cfg =
      some (cfg.afterAction (tm2RewindDoneAction source cfg.readWork)) := by
  rw [(tm2ProgrammeMachine source).step_eq_some_afterAction input cfg]
  · simp [ProgrammeMachine.actionAt, tm2ProgrammeMachine, hstate, hread,
      tm2ProgrammeTransition_rewind_none]
  · simpa [tm2ProgrammeMachine, hstate] using tm2ControlRewind_ne_accept source
  · simpa [tm2ProgrammeMachine, hstate] using tm2ControlRewind_ne_reject source

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
