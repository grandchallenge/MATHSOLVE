import MathSolve.PNP.TM2ProgrammeFamilyOps
import MathSolve.PNP.TM2StatementCost
import MathSolve.PNP.TM2CfgInvariant

/-!
# Structural simulation of one TM2 stepAux traversal

A mathlib TM2 machine step evaluates one finite statement tree with `stepAux`.
The Programme compiler exposes the same tree one primitive at a time.  This file
proves the structural bridge between those two granularities.

The result is deliberately local to a single statement occurrence.  Machine-wide
one-step and whole-run simulation are subsequent composition layers.
-/

namespace MathSolve.PNP

noncomputable section

open Turing

/-- Widen the advertised upper bound of an existing timed evaluation. -/
def evalsToInTime_mono {σ : Type*} {f : σ → Option σ}
    {a : σ} {b : Option σ} {m n : Nat}
    (h : StateTransition.EvalsToInTime f a b m)
    (hmn : m ≤ n) :
    StateTransition.EvalsToInTime f a b n :=
  ⟨h.toEvalsTo, h.steps_le_m.trans hmn⟩

/-- Under exact stack representation, the compiler's output-bit decoder sees
exactly the mapped head of the source output stack. -/
theorem TM2StacksRepresented.outputBit?_eq {decision : List Bool → Bool}
    (source : ImportedTM2Witness decision)
    {stackFamily : ∀ k, List (source.tm.Γ k)}
    {cfg : ProgrammeConfig (tm2ProgrammeMachine source)}
    (hrep : TM2StacksRepresented source stackFamily cfg) :
    tm2OutputBit? source cfg.readWork =
      (stackFamily source.tm.k₁).head?.map source.outputAlphabet := by
  unfold tm2OutputBit?
  rw [TM2StacksRepresented.readSourceHead?_eq_head?
    source hrep source.tm.k₁]

/-- Every represented accessible TM2 statement traversal is simulated by the
compiled Programme machine within its structural statement cost. -/
theorem tm2StepAux_simulates {decision : List Bool → Bool}
    (source : ImportedTM2Witness decision) (input : List Bool)
    (stmt : Turing.TM2.Stmt source.tm.Γ source.tm.Λ source.tm.σ) :
    ∀ (code : TM2StatementCode source.tm)
      (state : source.tm.σ)
      (stackFamily : ∀ k, List (source.tm.Γ k))
      (cfg : ProgrammeConfig (tm2ProgrammeMachine source)),
      code.2.1 = stmt →
      TM2StacksRepresented source stackFamily cfg →
      cfg.state = tm2ControlRun source code state →
      ∃ targetCfg,
        TM2CfgRepresented source
          (Turing.TM2.stepAux stmt state stackFamily) targetCfg ∧
        Nonempty
          (StateTransition.EvalsToInTime
            ((tm2ProgrammeMachine source).step input)
            cfg (some targetCfg)
            (tm2ProgrammeStatementCost stmt)) := by
  classical
  induction stmt with
  | push k valueFn nextStmt ih =>
      intro code state stackFamily cfg hcode hstacks hstate
      have hnext : nextStmt ∈ Turing.TM2.stmts₁ code.2.1 := by
        rw [hcode]
        exact Finset.mem_insert_of_mem Turing.TM2.stmts₁_self
      let nextCode :=
        tm2UnaryChildCode source code nextStmt hnext
      let token : TM2ProvenanceToken source.tm := .inr (code, state)
      let moved :=
        cfg.afterAction
          (tm2PushMoveAction source k nextCode state token cfg.readWork)
      have hstep₁raw :=
        tm2ProgrammeMachine_step_run source input cfg code state hstate
      rw [tm2RunAction_push source code state cfg.readWork
        k valueFn nextStmt hcode hnext] at hstep₁raw
      have hstep₁ :
          (tm2ProgrammeMachine source).step input cfg = some moved := by
        simpa [moved, nextCode, token] using hstep₁raw
      have hmovedState :
          moved.state =
            tm2ControlPushWrite source nextCode state token := by
        rfl
      have htoken :
          tm2PushTokenStack? source token = some k := by
        simpa [token] using
          tm2PushTokenStack?_generated
            source code state k valueFn nextStmt hcode
      let written :=
        moved.afterAction
          (tm2CompletePushAction source k nextCode state token moved.readWork)
      have hstep₂raw :=
        tm2ProgrammeMachine_step_pushWrite source input moved
          k nextCode state token hmovedState htoken
      have hstep₂ :
          (tm2ProgrammeMachine source).step input moved = some written := by
        simpa [written] using hstep₂raw
      have hwrittenStacks :
          TM2StacksRepresented source
            (Function.update stackFamily k (valueFn state :: stackFamily k))
            written := by
        simpa [moved, written, nextCode, token] using
          TM2StacksRepresented.afterPushActions source code state
            k valueFn nextStmt hcode nextCode hstacks
      have hwrittenState :
          written.state = tm2ControlRun source nextCode state := by
        rfl
      rcases ih nextCode state
          (Function.update stackFamily k (valueFn state :: stackFamily k))
          written rfl hwrittenStacks hwrittenState with
        ⟨targetCfg, htarget, ⟨hchild⟩⟩
      have htime₁ :=
        programme_one_step_in_time hstep₁
      have htime₂ :=
        programme_one_step_in_time hstep₂
      have htime₁₂ :
          StateTransition.EvalsToInTime
            ((tm2ProgrammeMachine source).step input)
            cfg (some written) 2 := by
        simpa using
          StateTransition.EvalsToInTime.trans
            ((tm2ProgrammeMachine source).step input)
            1 1 cfg moved (some written) htime₁ htime₂
      have htime :=
        StateTransition.EvalsToInTime.trans
          ((tm2ProgrammeMachine source).step input)
          2 (tm2ProgrammeStatementCost nextStmt)
          cfg written (some targetCfg) htime₁₂ hchild
      refine ⟨targetCfg, ?_, ⟨?_⟩⟩
      · simpa [Turing.TM2.stepAux] using htarget
      · simpa [tm2ProgrammeStatementCost, Nat.add_comm,
          Nat.add_left_comm, Nat.add_assoc] using htime
  | peek k updateState nextStmt ih =>
      intro code state stackFamily cfg hcode hstacks hstate
      have hnext : nextStmt ∈ Turing.TM2.stmts₁ code.2.1 := by
        rw [hcode]
        exact Finset.mem_insert_of_mem Turing.TM2.stmts₁_self
      let nextCode :=
        tm2UnaryChildCode source code nextStmt hnext
      have hread :=
        TM2StacksRepresented.readSourceHead?_eq_head?
          source hstacks k
      let nextState :=
        updateState state (stackFamily k).head?
      let nextCfg :=
        cfg.afterAction
          (tm2StayAction source
            (tm2ControlRun source nextCode nextState) cfg.readWork)
      have hstepRaw :=
        tm2ProgrammeMachine_step_run source input cfg code state hstate
      rw [tm2RunAction_peek source code state cfg.readWork
        k updateState nextStmt hcode hnext] at hstepRaw
      have hstep :
          (tm2ProgrammeMachine source).step input cfg = some nextCfg := by
        simpa [nextCfg, nextCode, nextState, hread] using hstepRaw
      have hnextStacks :
          TM2StacksRepresented source stackFamily nextCfg := by
        simpa [nextCfg, nextCode, nextState] using
          TM2StacksRepresented.afterStayAction source hstacks
            (tm2ControlRun source nextCode nextState)
      have hnextState :
          nextCfg.state = tm2ControlRun source nextCode nextState := by
        rfl
      rcases ih nextCode nextState stackFamily nextCfg rfl
          hnextStacks hnextState with
        ⟨targetCfg, htarget, ⟨hchild⟩⟩
      have htime₁ := programme_one_step_in_time hstep
      have htime :=
        StateTransition.EvalsToInTime.trans
          ((tm2ProgrammeMachine source).step input)
          1 (tm2ProgrammeStatementCost nextStmt)
          cfg nextCfg (some targetCfg) htime₁ hchild
      refine ⟨targetCfg, ?_, ⟨?_⟩⟩
      · simpa [Turing.TM2.stepAux, nextState] using htarget
      · simpa [tm2ProgrammeStatementCost, Nat.add_comm,
          Nat.add_left_comm, Nat.add_assoc] using htime
  | pop k updateState nextStmt ih =>
      intro code state stackFamily cfg hcode hstacks hstate
      have hnext : nextStmt ∈ Turing.TM2.stmts₁ code.2.1 := by
        rw [hcode]
        exact Finset.mem_insert_of_mem Turing.TM2.stmts₁_self
      let nextCode :=
        tm2UnaryChildCode source code nextStmt hnext
      have hread :=
        TM2StacksRepresented.readSourceHead?_eq_head?
          source hstacks k
      let nextState :=
        updateState state (stackFamily k).head?
      let nextCfg :=
        cfg.afterAction
          (tm2PopAction source k nextCode nextState cfg.readWork)
      have hstepRaw :=
        tm2ProgrammeMachine_step_run source input cfg code state hstate
      rw [tm2RunAction_pop source code state cfg.readWork
        k updateState nextStmt hcode hnext] at hstepRaw
      have hstep :
          (tm2ProgrammeMachine source).step input cfg = some nextCfg := by
        simpa [nextCfg, nextCode, nextState, hread] using hstepRaw
      have hnextStacks :
          TM2StacksRepresented source
            (Function.update stackFamily k (stackFamily k).tail)
            nextCfg := by
        simpa [nextCfg] using
          TM2StacksRepresented.afterPopAction source
            k nextCode nextState hstacks
      have hnextState :
          nextCfg.state = tm2ControlRun source nextCode nextState := by
        rfl
      rcases ih nextCode nextState
          (Function.update stackFamily k (stackFamily k).tail)
          nextCfg rfl hnextStacks hnextState with
        ⟨targetCfg, htarget, ⟨hchild⟩⟩
      have htime₁ := programme_one_step_in_time hstep
      have htime :=
        StateTransition.EvalsToInTime.trans
          ((tm2ProgrammeMachine source).step input)
          1 (tm2ProgrammeStatementCost nextStmt)
          cfg nextCfg (some targetCfg) htime₁ hchild
      refine ⟨targetCfg, ?_, ⟨?_⟩⟩
      · simpa [Turing.TM2.stepAux, nextState] using htarget
      · simpa [tm2ProgrammeStatementCost, Nat.add_comm,
          Nat.add_left_comm, Nat.add_assoc] using htime
  | load updateState nextStmt ih =>
      intro code state stackFamily cfg hcode hstacks hstate
      have hnext : nextStmt ∈ Turing.TM2.stmts₁ code.2.1 := by
        rw [hcode]
        exact Finset.mem_insert_of_mem Turing.TM2.stmts₁_self
      let nextCode :=
        tm2UnaryChildCode source code nextStmt hnext
      let nextState := updateState state
      let nextCfg :=
        cfg.afterAction
          (tm2StayAction source
            (tm2ControlRun source nextCode nextState) cfg.readWork)
      have hstepRaw :=
        tm2ProgrammeMachine_step_run source input cfg code state hstate
      rw [tm2RunAction_load source code state cfg.readWork
        updateState nextStmt hcode hnext] at hstepRaw
      have hstep :
          (tm2ProgrammeMachine source).step input cfg = some nextCfg := by
        simpa [nextCfg, nextCode, nextState] using hstepRaw
      have hnextStacks :
          TM2StacksRepresented source stackFamily nextCfg := by
        simpa [nextCfg, nextCode, nextState] using
          TM2StacksRepresented.afterStayAction source hstacks
            (tm2ControlRun source nextCode nextState)
      have hnextState :
          nextCfg.state = tm2ControlRun source nextCode nextState := by
        rfl
      rcases ih nextCode nextState stackFamily nextCfg rfl
          hnextStacks hnextState with
        ⟨targetCfg, htarget, ⟨hchild⟩⟩
      have htime₁ := programme_one_step_in_time hstep
      have htime :=
        StateTransition.EvalsToInTime.trans
          ((tm2ProgrammeMachine source).step input)
          1 (tm2ProgrammeStatementCost nextStmt)
          cfg nextCfg (some targetCfg) htime₁ hchild
      refine ⟨targetCfg, ?_, ⟨?_⟩⟩
      · simpa [Turing.TM2.stepAux, nextState] using htarget
      · simpa [tm2ProgrammeStatementCost, Nat.add_comm,
          Nat.add_left_comm, Nat.add_assoc] using htime
  | branch predicate trueStmt falseStmt ihTrue ihFalse =>
      intro code state stackFamily cfg hcode hstacks hstate
      cases hp : predicate state with
      | false =>
          have hnext : falseStmt ∈ Turing.TM2.stmts₁ code.2.1 := by
            rw [hcode]
            exact Finset.mem_insert_of_mem
              (Finset.mem_union_right _ Turing.TM2.stmts₁_self)
          let nextCode :=
            tm2UnaryChildCode source code falseStmt hnext
          let nextCfg :=
            cfg.afterAction
              (tm2StayAction source
                (tm2ControlRun source nextCode state) cfg.readWork)
          have hstepRaw :=
            tm2ProgrammeMachine_step_run source input cfg code state hstate
          rw [tm2RunAction_branch_false source code state cfg.readWork
            predicate trueStmt falseStmt hcode hnext hp] at hstepRaw
          have hstep :
              (tm2ProgrammeMachine source).step input cfg = some nextCfg := by
            simpa [nextCfg, nextCode] using hstepRaw
          have hnextStacks :
              TM2StacksRepresented source stackFamily nextCfg := by
            simpa [nextCfg, nextCode] using
              TM2StacksRepresented.afterStayAction source hstacks
                (tm2ControlRun source nextCode state)
          have hnextState :
              nextCfg.state = tm2ControlRun source nextCode state := by
            rfl
          rcases ihFalse nextCode state stackFamily nextCfg rfl
              hnextStacks hnextState with
            ⟨targetCfg, htarget, ⟨hchild⟩⟩
          have htime₁ := programme_one_step_in_time hstep
          have htime :=
            StateTransition.EvalsToInTime.trans
              ((tm2ProgrammeMachine source).step input)
              1 (tm2ProgrammeStatementCost falseStmt)
              cfg nextCfg (some targetCfg) htime₁ hchild
          have hbound :
              tm2ProgrammeStatementCost falseStmt + 1 ≤
                1 + max (tm2ProgrammeStatementCost trueStmt)
                  (tm2ProgrammeStatementCost falseStmt) := by
            omega
          refine ⟨targetCfg, ?_, ⟨?_⟩⟩
          · simpa [Turing.TM2.stepAux, hp] using htarget
          · exact evalsToInTime_mono htime hbound
      | true =>
          have hnext : trueStmt ∈ Turing.TM2.stmts₁ code.2.1 := by
            rw [hcode]
            exact Finset.mem_insert_of_mem
              (Finset.mem_union_left _ Turing.TM2.stmts₁_self)
          let nextCode :=
            tm2UnaryChildCode source code trueStmt hnext
          let nextCfg :=
            cfg.afterAction
              (tm2StayAction source
                (tm2ControlRun source nextCode state) cfg.readWork)
          have hstepRaw :=
            tm2ProgrammeMachine_step_run source input cfg code state hstate
          rw [tm2RunAction_branch_true source code state cfg.readWork
            predicate trueStmt falseStmt hcode hnext hp] at hstepRaw
          have hstep :
              (tm2ProgrammeMachine source).step input cfg = some nextCfg := by
            simpa [nextCfg, nextCode] using hstepRaw
          have hnextStacks :
              TM2StacksRepresented source stackFamily nextCfg := by
            simpa [nextCfg, nextCode] using
              TM2StacksRepresented.afterStayAction source hstacks
                (tm2ControlRun source nextCode state)
          have hnextState :
              nextCfg.state = tm2ControlRun source nextCode state := by
            rfl
          rcases ihTrue nextCode state stackFamily nextCfg rfl
              hnextStacks hnextState with
            ⟨targetCfg, htarget, ⟨hchild⟩⟩
          have htime₁ := programme_one_step_in_time hstep
          have htime :=
            StateTransition.EvalsToInTime.trans
              ((tm2ProgrammeMachine source).step input)
              1 (tm2ProgrammeStatementCost trueStmt)
              cfg nextCfg (some targetCfg) htime₁ hchild
          have hbound :
              tm2ProgrammeStatementCost trueStmt + 1 ≤
                1 + max (tm2ProgrammeStatementCost trueStmt)
                  (tm2ProgrammeStatementCost falseStmt) := by
            omega
          refine ⟨targetCfg, ?_, ⟨?_⟩⟩
          · simpa [Turing.TM2.stepAux, hp] using htarget
          · exact evalsToInTime_mono htime hbound
  | goto nextLabel =>
      intro code state stackFamily cfg hcode hstacks hstate
      let nextCfg :=
        cfg.afterAction
          (tm2StayAction source
            (tm2ControlRun source
              (TM2StatementCode.root source.tm (nextLabel state)) state)
            cfg.readWork)
      have hstepRaw :=
        tm2ProgrammeMachine_step_run source input cfg code state hstate
      rw [tm2RunAction_goto source code state cfg.readWork
        nextLabel hcode] at hstepRaw
      have hstep :
          (tm2ProgrammeMachine source).step input cfg = some nextCfg := by
        simpa [nextCfg] using hstepRaw
      have hnextStacks :
          TM2StacksRepresented source stackFamily nextCfg := by
        simpa [nextCfg] using
          TM2StacksRepresented.afterStayAction source hstacks
            (tm2ControlRun source
              (TM2StatementCode.root source.tm (nextLabel state)) state)
      have hnextState :
          nextCfg.state =
            tm2ControlRun source
              (TM2StatementCode.root source.tm (nextLabel state)) state := by
        rfl
      have htarget :
          TM2CfgRepresented source
            { l := some (nextLabel state), var := state, stk := stackFamily }
            nextCfg :=
        TM2CfgRepresented.live source (nextLabel state) state
          stackFamily nextCfg hnextStacks hnextState
      refine ⟨nextCfg, ?_, ⟨?_⟩⟩
      · simpa [Turing.TM2.stepAux] using htarget
      · simpa [tm2ProgrammeStatementCost] using
          programme_one_step_in_time hstep
  | halt =>
      intro code state stackFamily cfg hcode hstacks hstate
      have hout :=
        TM2StacksRepresented.outputBit?_eq source hstacks
      have hcontrol :
          (match tm2OutputBit? source cfg.readWork with
           | some true => tm2ControlAccept source
           | _ => tm2ControlReject source) =
            tm2HaltControl source stackFamily := by
        rw [hout]
        rfl
      let nextCfg :=
        cfg.afterAction
          (tm2StayAction source
            (tm2HaltControl source stackFamily) cfg.readWork)
      have hstepRaw :=
        tm2ProgrammeMachine_step_run source input cfg code state hstate
      rw [tm2RunAction_halt source code state cfg.readWork hcode] at hstepRaw
      have hafter :
          cfg.afterAction
              (tm2StayAction source
                (match tm2OutputBit? source cfg.readWork with
                 | some true => tm2ControlAccept source
                 | _ => tm2ControlReject source)
                cfg.readWork) =
            cfg.afterAction
              (tm2StayAction source
                (tm2HaltControl source stackFamily) cfg.readWork) :=
        congrArg
          (fun control =>
            cfg.afterAction (tm2StayAction source control cfg.readWork))
          hcontrol
      have hstep :
          (tm2ProgrammeMachine source).step input cfg = some nextCfg := by
        exact hstepRaw.trans (by
          simpa [nextCfg] using congrArg some hafter)
      have hnextStacks :
          TM2StacksRepresented source stackFamily nextCfg := by
        simpa [nextCfg] using
          TM2StacksRepresented.afterStayAction source hstacks
            (tm2HaltControl source stackFamily)
      have hnextState :
          nextCfg.state = tm2HaltControl source stackFamily := by
        rfl
      have htarget :
          TM2CfgRepresented source
            { l := none, var := state, stk := stackFamily } nextCfg :=
        TM2CfgRepresented.halt source state stackFamily nextCfg
          hnextStacks hnextState
      refine ⟨nextCfg, ?_, ⟨?_⟩⟩
      · simpa [Turing.TM2.stepAux] using htarget
      · simpa [tm2ProgrammeStatementCost] using
          programme_one_step_in_time hstep

#print axioms TM2StacksRepresented.outputBit?_eq
#print axioms tm2StepAux_simulates

end

end MathSolve.PNP
