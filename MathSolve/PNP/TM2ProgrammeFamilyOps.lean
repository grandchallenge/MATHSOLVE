import MathSolve.PNP.TM2ProgrammeActions
import MathSolve.PNP.TM2ProgrammeInvariant

/-!
# Stack-family preservation for mutating Programme actions

This file lifts the exact single-stack tape identities to the full heterogeneous
TM2 stack family.  The first theorem covers source `pop`: only the selected
stack changes, and every nonselected Programme tape remains extensionally
unchanged.
-/

namespace MathSolve.PNP

noncomputable section

/-- One concrete Programme pop action represents exactly the source stack-family
update `S[k := (S k).tail]`. -/
theorem TM2StacksRepresented.afterPopAction {decision : List Bool → Bool}
    (source : ImportedTM2Witness decision)
    (k : source.tm.K)
    (nextCode : TM2StatementCode source.tm) (nextState : source.tm.σ)
    {stackFamily : ∀ j, List (source.tm.Γ j)}
    {cfg : ProgrammeConfig (tm2ProgrammeMachine source)}
    (hrep : TM2StacksRepresented source stackFamily cfg) :
    TM2StacksRepresented source
      (Function.update stackFamily k (stackFamily k).tail)
      (cfg.afterAction
        (tm2PopAction source k nextCode nextState cfg.readWork)) := by
  intro j
  by_cases hj : j = k
  · subst j
    simp only [Function.update_self]
    cases hstack : stackFamily k with
    | nil =>
        have hk := hrep k
        rw [hstack] at hk
        convert TM2StackRepresented.pop_empty source k
          (cfg.work (tm2TapeEquiv source k))
          (cfg.workHead (tm2TapeEquiv source k)) hk using 1 <;>
          simp [ProgrammeConfig.afterAction, tm2PopAction,
            tm2MoveSelected, tm2WriteSelected, HeadMove.apply] <;> rfl
    | cons value values =>
        have hk := hrep k
        rw [hstack] at hk
        convert TM2StackRepresented.pop source k
          (cfg.work (tm2TapeEquiv source k))
          (cfg.workHead (tm2TapeEquiv source k))
          value values hk using 1 <;>
          simp [ProgrammeConfig.afterAction, tm2PopAction,
            tm2MoveSelected, tm2WriteSelected, HeadMove.apply] <;> rfl
  · have htape :
        tm2TapeEquiv source j ≠ tm2TapeEquiv source k := by
      intro h
      exact hj ((tm2TapeEquiv source).injective h)
    have hjrep := hrep j
    rw [Function.update_of_ne hj]
    convert hjrep using 1 <;>
      simp [ProgrammeConfig.afterAction, tm2PopAction,
        tm2MoveSelected, tm2WriteSelected, ProgrammeConfig.readWork,
        HeadMove.apply, htape, Function.update_eq_self]

/-- The first push transition writes every currently scanned cell back to
itself, so its whole work-tape family is unchanged. -/
theorem afterAction_tm2PushMoveAction_work {decision : List Bool → Bool}
    (source : ImportedTM2Witness decision)
    (cfg : ProgrammeConfig (tm2ProgrammeMachine source))
    (k : source.tm.K)
    (nextCode : TM2StatementCode source.tm) (state : source.tm.σ)
    (token : TM2ProvenanceToken source.tm) :
    (cfg.afterAction
      (tm2PushMoveAction source k nextCode state token cfg.readWork)).work =
      cfg.work := by
  funext tape
  change Function.update (cfg.work tape) (cfg.workHead tape)
      (cfg.work tape (cfg.workHead tape)) = cfg.work tape
  exact Function.update_eq_self _ _

/-- The first push transition moves exactly the selected work head left. -/
theorem afterAction_tm2PushMoveAction_selectedHead
    {decision : List Bool → Bool}
    (source : ImportedTM2Witness decision)
    (cfg : ProgrammeConfig (tm2ProgrammeMachine source))
    (k : source.tm.K)
    (nextCode : TM2StatementCode source.tm) (state : source.tm.σ)
    (token : TM2ProvenanceToken source.tm) :
    (cfg.afterAction
      (tm2PushMoveAction source k nextCode state token cfg.readWork)).workHead
        (tm2TapeEquiv source k) =
      cfg.workHead (tm2TapeEquiv source k) - 1 := by
  simp [ProgrammeConfig.afterAction, tm2PushMoveAction,
    tm2MoveSelected, HeadMove.apply]

/-- The first push transition preserves every nonselected work-head position. -/
theorem afterAction_tm2PushMoveAction_otherHead
    {decision : List Bool → Bool}
    (source : ImportedTM2Witness decision)
    (cfg : ProgrammeConfig (tm2ProgrammeMachine source))
    (k j : source.tm.K) (hjk : j ≠ k)
    (nextCode : TM2StatementCode source.tm) (state : source.tm.σ)
    (token : TM2ProvenanceToken source.tm) :
    (cfg.afterAction
      (tm2PushMoveAction source k nextCode state token cfg.readWork)).workHead
        (tm2TapeEquiv source j) =
      cfg.workHead (tm2TapeEquiv source j) := by
  have htape : tm2TapeEquiv source j ≠ tm2TapeEquiv source k := by
    intro h
    exact hjk ((tm2TapeEquiv source).injective h)
  simp [ProgrammeConfig.afterAction, tm2PushMoveAction,
    tm2MoveSelected, HeadMove.apply, htape]

/-- The two concrete Programme push transitions represent exactly the source
stack-family update `S[k := valueFn state :: S k]`. -/
theorem TM2StacksRepresented.afterPushActions {decision : List Bool → Bool}
    (source : ImportedTM2Witness decision)
    (code : TM2StatementCode source.tm) (state : source.tm.σ)
    (k : source.tm.K) (valueFn : source.tm.σ → source.tm.Γ k)
    (nextStmt : Turing.TM2.Stmt source.tm.Γ source.tm.Λ source.tm.σ)
    (hstmt : code.2.1 = Turing.TM2.Stmt.push k valueFn nextStmt)
    (nextCode : TM2StatementCode source.tm)
    {stackFamily : ∀ j, List (source.tm.Γ j)}
    {cfg : ProgrammeConfig (tm2ProgrammeMachine source)}
    (hrep : TM2StacksRepresented source stackFamily cfg) :
    let token : TM2ProvenanceToken source.tm := .inr (code, state)
    let moved :=
      cfg.afterAction
        (tm2PushMoveAction source k nextCode state token cfg.readWork)
    let written :=
      moved.afterAction
        (tm2CompletePushAction source k nextCode state token moved.readWork)
    TM2StacksRepresented source
      (Function.update stackFamily k (valueFn state :: stackFamily k))
      written := by
  dsimp
  intro j
  by_cases hj : j = k
  · subst j
    simp only [Function.update_self]
    have hk := hrep k
    convert TM2StackRepresented.push_generated source code state k valueFn
      nextStmt
      (cfg.work (tm2TapeEquiv source k))
      (cfg.workHead (tm2TapeEquiv source k))
      (stackFamily k) hstmt hk using 1
    · simp [ProgrammeConfig.afterAction, tm2CompletePushAction,
        tm2PushMoveAction, tm2PreserveWork, tm2MoveSelected,
        tm2WriteSelected, HeadMove.apply, Function.update_eq_self]
    · simp [ProgrammeConfig.afterAction, tm2CompletePushAction,
        tm2PushMoveAction, tm2MoveSelected, HeadMove.apply]
  · have htape :
        tm2TapeEquiv source j ≠ tm2TapeEquiv source k := by
      intro h
      exact hj ((tm2TapeEquiv source).injective h)
    have hjrep := hrep j
    rw [Function.update_of_ne hj]
    convert hjrep using 1
    · simp [ProgrammeConfig.afterAction, tm2CompletePushAction,
        tm2PushMoveAction, tm2PreserveWork, tm2MoveSelected,
        tm2WriteSelected, ProgrammeConfig.readWork, htape,
        HeadMove.apply, Function.update_eq_self]
    · simp [ProgrammeConfig.afterAction, tm2CompletePushAction,
        tm2PushMoveAction, tm2MoveSelected, htape, HeadMove.apply]

#print axioms TM2StacksRepresented.afterPushActions
#print axioms TM2StacksRepresented.afterPopAction

end

end MathSolve.PNP
