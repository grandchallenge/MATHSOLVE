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
    simp only [Function.update_same]
    cases hstack : stackFamily k with
    | nil =>
        have hk := hrep k
        rw [hstack] at hk
        convert TM2StackRepresented.pop_empty source k
          (cfg.work (tm2TapeEquiv source k))
          (cfg.workHead (tm2TapeEquiv source k)) hk using 1 <;>
          simp [ProgrammeConfig.afterAction, tm2PopAction,
            tm2MoveSelected, tm2WriteSelected, HeadMove.apply]
    | cons value values =>
        have hk := hrep k
        rw [hstack] at hk
        convert TM2StackRepresented.pop source k
          (cfg.work (tm2TapeEquiv source k))
          (cfg.workHead (tm2TapeEquiv source k))
          value values hk using 1 <;>
          simp [ProgrammeConfig.afterAction, tm2PopAction,
            tm2MoveSelected, tm2WriteSelected, HeadMove.apply]
  · have htape :
        tm2TapeEquiv source j ≠ tm2TapeEquiv source k := by
      intro h
      exact hj ((tm2TapeEquiv source).injective h)
    have hjrep := hrep j
    rw [Function.update_noteq (Ne.symm hj)]
    convert hjrep using 1 <;>
      simp [ProgrammeConfig.afterAction, tm2PopAction,
        tm2MoveSelected, tm2WriteSelected, ProgrammeConfig.readWork,
        HeadMove.apply, htape, Function.update_eq_self]

#print axioms TM2StacksRepresented.afterPopAction

end

end MathSolve.PNP
