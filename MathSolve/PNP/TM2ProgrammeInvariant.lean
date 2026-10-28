import MathSolve.PNP.TM2ProgrammeCompiler
import MathSolve.PNP.TM2StackOps

/-!
# Programme configuration invariant for the finite-TM2 compiler

This file packages the per-stack provenance representation into the concrete
Programme configuration and proves that the compiler's selected work-head read
returns exactly the source stack's `head?`.

No whole-step simulation claim is made here.
-/

namespace MathSolve.PNP

noncomputable section

open Turing

/-- Every source TM2 stack is represented on its uniquely assigned Programme
work tape at that tape's current head position. -/
def TM2StacksRepresented {decision : List Bool → Bool}
    (source : ImportedTM2Witness decision)
    (stackFamily : ∀ k, List (source.tm.Γ k))
    (cfg : ProgrammeConfig (tm2ProgrammeMachine source)) : Prop :=
  ∀ k,
    TM2StackRepresented source k
      (cfg.work (tm2TapeEquiv source k))
      (cfg.workHead (tm2TapeEquiv source k))
      (stackFamily k)

/-- Representation of an executing source statement occurrence. -/
def TM2RunRepresented {decision : List Bool → Bool}
    (source : ImportedTM2Witness decision)
    (code : TM2StatementCode source.tm) (state : source.tm.σ)
    (stackFamily : ∀ k, List (source.tm.Γ k))
    (cfg : ProgrammeConfig (tm2ProgrammeMachine source)) : Prop :=
  cfg.state = tm2ControlRun source code state ∧
    TM2StacksRepresented source stackFamily cfg

/-- A represented empty source stack reads Programme blank at its assigned head. -/
theorem TM2StacksRepresented.read_empty {decision : List Bool → Bool}
    (source : ImportedTM2Witness decision)
    {stackFamily : ∀ k, List (source.tm.Γ k)}
    {cfg : ProgrammeConfig (tm2ProgrammeMachine source)}
    (hrep : TM2StacksRepresented source stackFamily cfg)
    (k : source.tm.K) (hk : stackFamily k = []) :
    cfg.readWork (tm2TapeEquiv source k) = none := by
  have hstack := hrep k
  rw [hk] at hstack
  have hblank := TM2StackRepresented.empty_head source k
    (cfg.work (tm2TapeEquiv source k))
    (cfg.workHead (tm2TapeEquiv source k)) hstack
  exact hblank

/-- A represented nonempty source stack reads a token decoding to its exact head. -/
theorem TM2StacksRepresented.read_cons {decision : List Bool → Bool}
    (source : ImportedTM2Witness decision)
    {stackFamily : ∀ k, List (source.tm.Γ k)}
    {cfg : ProgrammeConfig (tm2ProgrammeMachine source)}
    (hrep : TM2StacksRepresented source stackFamily cfg)
    (k : source.tm.K) (value : source.tm.Γ k)
    (values : List (source.tm.Γ k))
    (hk : stackFamily k = value :: values) :
    ∃ token : TM2ProvenanceToken source.tm,
      cfg.readWork (tm2TapeEquiv source k) = some token ∧
      tm2TokenValue? source k token = some value := by
  have hstack := hrep k
  rw [hk] at hstack
  exact TM2StackRepresented.head_decode source k
    (cfg.work (tm2TapeEquiv source k))
    (cfg.workHead (tm2TapeEquiv source k))
    value values hstack

/-- The concrete compiler's selected work-head decoder is exactly source
`List.head?` under the stack-family representation invariant. -/
theorem TM2StacksRepresented.readSourceHead?_eq_head?
    {decision : List Bool → Bool}
    (source : ImportedTM2Witness decision)
    {stackFamily : ∀ k, List (source.tm.Γ k)}
    {cfg : ProgrammeConfig (tm2ProgrammeMachine source)}
    (hrep : TM2StacksRepresented source stackFamily cfg)
    (k : source.tm.K) :
    tm2ReadSourceHead? source k cfg.readWork = (stackFamily k).head? := by
  cases hk : stackFamily k with
  | nil =>
      have hblank := TM2StacksRepresented.read_empty source hrep k hk
      simp [tm2ReadSourceHead?, hblank, hk]
  | cons value values =>
      rcases TM2StacksRepresented.read_cons source hrep k value values hk with
        ⟨token, hread, hdecode⟩
      simp [tm2ReadSourceHead?, hread, hdecode, hk]

/-- Executing-state representation exposes the same exact stack-head decoder. -/
theorem TM2RunRepresented.readSourceHead?_eq_head?
    {decision : List Bool → Bool}
    (source : ImportedTM2Witness decision)
    {code : TM2StatementCode source.tm} {state : source.tm.σ}
    {stackFamily : ∀ k, List (source.tm.Γ k)}
    {cfg : ProgrammeConfig (tm2ProgrammeMachine source)}
    (hrep : TM2RunRepresented source code state stackFamily cfg)
    (k : source.tm.K) :
    tm2ReadSourceHead? source k cfg.readWork = (stackFamily k).head? :=
  TM2StacksRepresented.readSourceHead?_eq_head? source hrep.2 k

#print axioms TM2StacksRepresented.read_empty
#print axioms TM2StacksRepresented.read_cons
#print axioms TM2StacksRepresented.readSourceHead?_eq_head?
#print axioms TM2RunRepresented.readSourceHead?_eq_head?

end

end MathSolve.PNP
