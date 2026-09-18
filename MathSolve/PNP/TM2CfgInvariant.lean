import MathSolve.PNP.ProgrammeStep
import MathSolve.PNP.TM2ProgrammeInvariant

/-!
# Source-configuration relation for the TM2-to-Programme compiler

This relation is the endpoint of the structural `TM2.stepAux` simulation.

* a live TM2 label is represented by the corresponding root statement control;
* a halted TM2 configuration is represented by a Programme terminal selected
  from the represented output stack head;
* every source stack remains related to its uniquely assigned Programme tape.

The relation is deliberately total on halted source configurations.  Malformed
or empty source output stacks map to Programme reject.  The imported
`outputsFun` witness later specializes the halt configuration to the canonical
single-symbol Boolean output.
-/

namespace MathSolve.PNP

noncomputable section

open Turing

/-- Terminal Programme control selected from a source TM2 output stack. -/
def tm2HaltControl {decision : List Bool → Bool}
    (source : ImportedTM2Witness decision)
    (stackFamily : ∀ k, List (source.tm.Γ k)) :
    TM2ProgrammeControl source :=
  match (stackFamily source.tm.k₁).head?.map source.outputAlphabet with
  | some true => tm2ControlAccept source
  | _ => tm2ControlReject source

/-- Relate a source TM2 configuration to a concrete Programme configuration. -/
def TM2CfgRepresented {decision : List Bool → Bool}
    (source : ImportedTM2Witness decision)
    (sourceCfg : source.tm.Cfg)
    (targetCfg : ProgrammeConfig (tm2ProgrammeMachine source)) : Prop :=
  TM2StacksRepresented source sourceCfg.stk targetCfg ∧
    match sourceCfg.l with
    | some label =>
        targetCfg.state =
          tm2ControlRun source (TM2StatementCode.root source.tm label) sourceCfg.var
    | none =>
        targetCfg.state = tm2HaltControl source sourceCfg.stk

/-- Build the live-label endpoint relation from the stack-family invariant. -/
theorem TM2CfgRepresented.live {decision : List Bool → Bool}
    (source : ImportedTM2Witness decision)
    (label : source.tm.Λ) (state : source.tm.σ)
    (stackFamily : ∀ k, List (source.tm.Γ k))
    (cfg : ProgrammeConfig (tm2ProgrammeMachine source))
    (hstacks : TM2StacksRepresented source stackFamily cfg)
    (hstate :
      cfg.state =
        tm2ControlRun source (TM2StatementCode.root source.tm label) state) :
    TM2CfgRepresented source
      { l := some label, var := state, stk := stackFamily } cfg := by
  exact ⟨hstacks, hstate⟩

/-- Build the halted endpoint relation from the stack-family invariant. -/
theorem TM2CfgRepresented.halt {decision : List Bool → Bool}
    (source : ImportedTM2Witness decision)
    (state : source.tm.σ)
    (stackFamily : ∀ k, List (source.tm.Γ k))
    (cfg : ProgrammeConfig (tm2ProgrammeMachine source))
    (hstacks : TM2StacksRepresented source stackFamily cfg)
    (hstate : cfg.state = tm2HaltControl source stackFamily) :
    TM2CfgRepresented source
      { l := none, var := state, stk := stackFamily } cfg := by
  exact ⟨hstacks, hstate⟩

/-- The selected halt control is always one of the two Programme terminals. -/
theorem tm2HaltControl_terminal {decision : List Bool → Bool}
    (source : ImportedTM2Witness decision)
    (stackFamily : ∀ k, List (source.tm.Γ k)) :
    tm2HaltControl source stackFamily = tm2ControlAccept source ∨
      tm2HaltControl source stackFamily = tm2ControlReject source := by
  unfold tm2HaltControl
  split <;> simp

/-- A Programme configuration representing a halted TM2 configuration is terminal. -/
theorem TM2CfgRepresented.halted_terminal {decision : List Bool → Bool}
    (source : ImportedTM2Witness decision)
    {sourceCfg : source.tm.Cfg}
    {targetCfg : ProgrammeConfig (tm2ProgrammeMachine source)}
    (hrep : TM2CfgRepresented source sourceCfg targetCfg)
    (hhalt : sourceCfg.l = none) :
    targetCfg.state = (tm2ProgrammeMachine source).accept ∨
      targetCfg.state = (tm2ProgrammeMachine source).reject := by
  have hstate := hrep.2
  rw [hhalt] at hstate
  rcases tm2HaltControl_terminal source sourceCfg.stk with h | h
  · left
    simpa [tm2ProgrammeMachine] using hstate.trans h
  · right
    simpa [tm2ProgrammeMachine] using hstate.trans h

/-- The target side of a represented halted source configuration has no successor. -/
theorem TM2CfgRepresented.halted_step_none {decision : List Bool → Bool}
    (source : ImportedTM2Witness decision)
    (input : List Bool)
    {sourceCfg : source.tm.Cfg}
    {targetCfg : ProgrammeConfig (tm2ProgrammeMachine source)}
    (hrep : TM2CfgRepresented source sourceCfg targetCfg)
    (hhalt : sourceCfg.l = none) :
    (tm2ProgrammeMachine source).step input targetCfg = none := by
  exact (tm2ProgrammeMachine source).step_eq_none_of_terminal input targetCfg
    (TM2CfgRepresented.halted_terminal source hrep hhalt)

/-- Canonical singleton Boolean output selects exactly the corresponding
Programme terminal control. -/
theorem tm2HaltControl_singleton {decision : List Bool → Bool}
    (source : ImportedTM2Witness decision)
    (stackFamily : ∀ k, List (source.tm.Γ k))
    (result : Bool)
    (hout :
      stackFamily source.tm.k₁ = [source.outputAlphabet.invFun result]) :
    tm2HaltControl source stackFamily =
      if result then tm2ControlAccept source else tm2ControlReject source := by
  subst hout
  simp [tm2HaltControl]

/-- A represented canonical halted Boolean output has the exact Programme output. -/
theorem TM2CfgRepresented.halted_output {decision : List Bool → Bool}
    (source : ImportedTM2Witness decision)
    {sourceCfg : source.tm.Cfg}
    {targetCfg : ProgrammeConfig (tm2ProgrammeMachine source)}
    (hrep : TM2CfgRepresented source sourceCfg targetCfg)
    (hhalt : sourceCfg.l = none)
    (result : Bool)
    (hout :
      sourceCfg.stk source.tm.k₁ = [source.outputAlphabet.invFun result]) :
    (tm2ProgrammeMachine source).output targetCfg = some result := by
  have hstate := hrep.2
  rw [hhalt] at hstate
  have hcontrol := tm2HaltControl_singleton source sourceCfg.stk result hout
  cases result <;>
    simp [ProgrammeMachine.output, tm2ProgrammeMachine,
      hstate.trans hcontrol]

#print axioms tm2HaltControl_terminal
#print axioms TM2CfgRepresented.halted_terminal
#print axioms TM2CfgRepresented.halted_step_none
#print axioms tm2HaltControl_singleton
#print axioms TM2CfgRepresented.halted_output

end

end MathSolve.PNP
