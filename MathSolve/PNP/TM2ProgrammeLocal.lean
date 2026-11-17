import MathSolve.PNP.TM2CfgInvariant

/-!
# Local operational facts for the TM2-to-Programme compiler

These lemmas isolate two repetitive proof obligations used by the structural
`stepAux` simulation:

* executable run and push-write controls are distinct from both terminals;
* a `tm2StayAction` changes finite control only and preserves every represented
  source stack exactly.

No source-step simulation theorem is asserted here.
-/

namespace MathSolve.PNP

noncomputable section

/-- Executing a source statement is never already in the accepting terminal. -/
theorem tm2ControlRun_ne_accept {decision : List Bool → Bool}
    (source : ImportedTM2Witness decision)
    (code : TM2StatementCode source.tm) (state : source.tm.σ) :
    tm2ControlRun source code state ≠ tm2ControlAccept source := by
  intro h
  cases h

/-- Executing a source statement is never already in the rejecting terminal. -/
theorem tm2ControlRun_ne_reject {decision : List Bool → Bool}
    (source : ImportedTM2Witness decision)
    (code : TM2StatementCode source.tm) (state : source.tm.σ) :
    tm2ControlRun source code state ≠ tm2ControlReject source := by
  intro h
  cases h

/-- The administrative second half of a push is not accepting. -/
theorem tm2ControlPushWrite_ne_accept {decision : List Bool → Bool}
    (source : ImportedTM2Witness decision)
    (code : TM2StatementCode source.tm) (state : source.tm.σ)
    (token : TM2ProvenanceToken source.tm) :
    tm2ControlPushWrite source code state token ≠ tm2ControlAccept source := by
  intro h
  cases h

/-- The administrative second half of a push is not rejecting. -/
theorem tm2ControlPushWrite_ne_reject {decision : List Bool → Bool}
    (source : ImportedTM2Witness decision)
    (code : TM2StatementCode source.tm) (state : source.tm.σ)
    (token : TM2ProvenanceToken source.tm) :
    tm2ControlPushWrite source code state token ≠ tm2ControlReject source := by
  intro h
  cases h

/-- A neutral compiler action changes only the Programme control state. -/
theorem afterAction_tm2StayAction_state {decision : List Bool → Bool}
    (source : ImportedTM2Witness decision)
    (cfg : ProgrammeConfig (tm2ProgrammeMachine source))
    (next : TM2ProgrammeControl source) :
    (cfg.afterAction (tm2StayAction source next cfg.readWork)).state = next := by
  rfl

/-- A neutral compiler action preserves all work-head positions. -/
theorem afterAction_tm2StayAction_workHead {decision : List Bool → Bool}
    (source : ImportedTM2Witness decision)
    (cfg : ProgrammeConfig (tm2ProgrammeMachine source))
    (next : TM2ProgrammeControl source) :
    (cfg.afterAction (tm2StayAction source next cfg.readWork)).workHead =
      cfg.workHead := by
  funext tape
  rfl

/-- A neutral compiler action writes each scanned cell back to itself, hence
preserves every whole work tape extensionally. -/
theorem afterAction_tm2StayAction_work {decision : List Bool → Bool}
    (source : ImportedTM2Witness decision)
    (cfg : ProgrammeConfig (tm2ProgrammeMachine source))
    (next : TM2ProgrammeControl source) :
    (cfg.afterAction (tm2StayAction source next cfg.readWork)).work = cfg.work := by
  funext tape
  change Function.update (cfg.work tape) (cfg.workHead tape)
      (cfg.work tape (cfg.workHead tape)) = cfg.work tape
  exact Function.update_eq_self _ _

/-- Therefore every source-stack representation is preserved by a neutral
compiler action. -/
theorem TM2StacksRepresented.afterStayAction {decision : List Bool → Bool}
    (source : ImportedTM2Witness decision)
    {stackFamily : ∀ k, List (source.tm.Γ k)}
    {cfg : ProgrammeConfig (tm2ProgrammeMachine source)}
    (hrep : TM2StacksRepresented source stackFamily cfg)
    (next : TM2ProgrammeControl source) :
    TM2StacksRepresented source stackFamily
      (cfg.afterAction (tm2StayAction source next cfg.readWork)) := by
  intro k
  have hk := hrep k
  rw [afterAction_tm2StayAction_workHead source cfg next,
    afterAction_tm2StayAction_work source cfg next]
  exact hk

#print axioms tm2ControlRun_ne_accept
#print axioms tm2ControlRun_ne_reject
#print axioms tm2ControlPushWrite_ne_accept
#print axioms tm2ControlPushWrite_ne_reject
#print axioms TM2StacksRepresented.afterStayAction

end

end MathSolve.PNP
