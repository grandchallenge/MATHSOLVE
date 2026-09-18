import MathSolve.PNP.TM2ProgrammeLocal
import MathSolve.PNP.ProgrammeStep

/-!
# Exact Programme step from an executing TM2 control

This file is a proof-facing normalization layer for the structural
`TM2.stepAux` simulation.  It shows that a Programme configuration whose
control is `tm2ControlRun code state` takes exactly the `tm2RunAction`
selected by that source statement occurrence.
-/

namespace MathSolve.PNP

noncomputable section

/-- Run control is distinct from startup copy control. -/
theorem tm2ControlRun_ne_copy {decision : List Bool → Bool}
    (source : ImportedTM2Witness decision)
    (code : TM2StatementCode source.tm) (state : source.tm.σ) :
    tm2ControlRun source code state ≠ tm2ControlCopy source := by
  intro h
  cases h

/-- Run control is distinct from startup rewind control. -/
theorem tm2ControlRun_ne_rewind {decision : List Bool → Bool}
    (source : ImportedTM2Witness decision)
    (code : TM2StatementCode source.tm) (state : source.tm.σ) :
    tm2ControlRun source code state ≠ tm2ControlRewind source := by
  intro h
  cases h

/-- Push-write control is distinct from startup copy control. -/
theorem tm2ControlPushWrite_ne_copy {decision : List Bool → Bool}
    (source : ImportedTM2Witness decision)
    (code : TM2StatementCode source.tm) (state : source.tm.σ)
    (token : TM2ProvenanceToken source.tm) :
    tm2ControlPushWrite source code state token ≠ tm2ControlCopy source := by
  intro h
  cases h

/-- Push-write control is distinct from startup rewind control. -/
theorem tm2ControlPushWrite_ne_rewind {decision : List Bool → Bool}
    (source : ImportedTM2Witness decision)
    (code : TM2StatementCode source.tm) (state : source.tm.σ)
    (token : TM2ProvenanceToken source.tm) :
    tm2ControlPushWrite source code state token ≠ tm2ControlRewind source := by
  intro h
  cases h

/-- The total compiler transition normalizes to `tm2RunAction` on run control. -/
theorem tm2ProgrammeTransition_run {decision : List Bool → Bool}
    (source : ImportedTM2Witness decision)
    (code : TM2StatementCode source.tm) (state : source.tm.σ)
    (inputSymbol : Option Bool)
    (readWork : Fin (tm2WorkTapeCount source) → TM2ProgrammeSymbol source.tm) :
    tm2ProgrammeTransition source (tm2ControlRun source code state)
      inputSymbol readWork =
      tm2RunAction source code state readWork := by
  simp [tm2ProgrammeTransition, tm2ControlRun_ne_copy source code state,
    tm2ControlRun_ne_rewind source code state]

/-- The action selected by the concrete Programme machine at a represented run
configuration is exactly the source-statement action. -/
theorem tm2ProgrammeMachine_actionAt_run {decision : List Bool → Bool}
    (source : ImportedTM2Witness decision) (input : List Bool)
    (cfg : ProgrammeConfig (tm2ProgrammeMachine source))
    (code : TM2StatementCode source.tm) (state : source.tm.σ)
    (hstate : cfg.state = tm2ControlRun source code state) :
    (tm2ProgrammeMachine source).actionAt input cfg =
      tm2RunAction source code state cfg.readWork := by
  simp [ProgrammeMachine.actionAt, tm2ProgrammeMachine, hstate,
    tm2ProgrammeTransition_run]

/-- One represented run control takes exactly one deterministic Programme step
to the configuration obtained by applying `tm2RunAction`. -/
theorem tm2ProgrammeMachine_step_run {decision : List Bool → Bool}
    (source : ImportedTM2Witness decision) (input : List Bool)
    (cfg : ProgrammeConfig (tm2ProgrammeMachine source))
    (code : TM2StatementCode source.tm) (state : source.tm.σ)
    (hstate : cfg.state = tm2ControlRun source code state) :
    (tm2ProgrammeMachine source).step input cfg =
      some (cfg.afterAction (tm2RunAction source code state cfg.readWork)) := by
  rw [(tm2ProgrammeMachine source).step_eq_some_afterAction input cfg]
  · rw [tm2ProgrammeMachine_actionAt_run source input cfg code state hstate]
  · simpa [tm2ProgrammeMachine, hstate] using
      tm2ControlRun_ne_accept source code state
  · simpa [tm2ProgrammeMachine, hstate] using
      tm2ControlRun_ne_reject source code state

/-- Proof-facing spelling of the valid second half of a two-transition push. -/
def tm2CompletePushAction {decision : List Bool → Bool}
    (source : ImportedTM2Witness decision) (k : source.tm.K)
    (nextCode : TM2StatementCode source.tm) (state : source.tm.σ)
    (token : TM2ProvenanceToken source.tm)
    (readWork : Fin (tm2WorkTapeCount source) → TM2ProgrammeSymbol source.tm) :
    ProgrammeAction (TM2ProgrammeControl source) (TM2ProgrammeSymbol source.tm)
      (tm2WorkTapeCount source) where
  nextState := tm2ControlRun source nextCode state
  inputMove := .stay
  write := tm2WriteSelected source readWork k (some token)
  workMove := fun _ => .stay

/-- A valid push-write control normalizes to the proof-facing completion action. -/
theorem tm2ProgrammeTransition_pushWrite {decision : List Bool → Bool}
    (source : ImportedTM2Witness decision)
    (k : source.tm.K)
    (nextCode : TM2StatementCode source.tm) (state : source.tm.σ)
    (token : TM2ProvenanceToken source.tm)
    (inputSymbol : Option Bool)
    (readWork : Fin (tm2WorkTapeCount source) → TM2ProgrammeSymbol source.tm)
    (htoken : tm2PushTokenStack? source token = some k) :
    tm2ProgrammeTransition source
      (tm2ControlPushWrite source nextCode state token)
      inputSymbol readWork =
      tm2CompletePushAction source k nextCode state token readWork := by
  simp [tm2ProgrammeTransition,
    tm2ControlPushWrite_ne_copy source nextCode state token,
    tm2ControlPushWrite_ne_rewind source nextCode state token,
    tm2CompletePushAction, htoken]

/-- The concrete Programme machine takes the valid second push transition exactly. -/
theorem tm2ProgrammeMachine_step_pushWrite {decision : List Bool → Bool}
    (source : ImportedTM2Witness decision) (input : List Bool)
    (cfg : ProgrammeConfig (tm2ProgrammeMachine source))
    (k : source.tm.K)
    (nextCode : TM2StatementCode source.tm) (state : source.tm.σ)
    (token : TM2ProvenanceToken source.tm)
    (hstate : cfg.state = tm2ControlPushWrite source nextCode state token)
    (htoken : tm2PushTokenStack? source token = some k) :
    (tm2ProgrammeMachine source).step input cfg =
      some (cfg.afterAction
        (tm2CompletePushAction source k nextCode state token cfg.readWork)) := by
  rw [(tm2ProgrammeMachine source).step_eq_some_afterAction input cfg]
  · simp [ProgrammeMachine.actionAt, tm2ProgrammeMachine, hstate,
      tm2ProgrammeTransition_pushWrite, htoken]
  · simpa [tm2ProgrammeMachine, hstate] using
      tm2ControlPushWrite_ne_accept source nextCode state token
  · simpa [tm2ProgrammeMachine, hstate] using
      tm2ControlPushWrite_ne_reject source nextCode state token

/-- Package one exact transition equality as a one-step `EvalsToInTime` witness. -/
theorem programme_one_step_in_time
    {M : ProgrammeMachine} {input : List Bool}
    {cfg cfg' : ProgrammeConfig M}
    (hstep : M.step input cfg = some cfg') :
    StateTransition.EvalsToInTime (M.step input) cfg (some cfg') 1 := by
  refine { steps := 1, evals_in_steps := ?_, steps_le_m := le_rfl }
  simpa [Function.iterate_one, flip] using hstep

#print axioms tm2ControlPushWrite_ne_copy
#print axioms tm2ControlPushWrite_ne_rewind
#print axioms tm2ProgrammeTransition_run
#print axioms tm2ProgrammeMachine_actionAt_run
#print axioms tm2ProgrammeMachine_step_run
#print axioms tm2ProgrammeTransition_pushWrite
#print axioms tm2ProgrammeMachine_step_pushWrite

end

end MathSolve.PNP
