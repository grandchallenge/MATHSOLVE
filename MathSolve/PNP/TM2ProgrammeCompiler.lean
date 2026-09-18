import MathSolve.PNP.TM2ProgrammeControl

/-!
# Concrete FinTM2-to-Programme machine

This file constructs the actual Programme machine used by the forward half of
`PNP-BRIDGE-MODEL-001`.

The construction is deliberately operational.  Source stacks are represented by
finite provenance tokens on one Programme work tape per TM2 stack.  One source
`stepAux` path is executed by finite control over statement occurrences:

* `push` moves the selected stack head left and writes the generated provenance
  token in a second transition;
* `peek` decodes the selected head token without changing the tape;
* `pop` decodes, erases, and moves the selected stack head right;
* `load`, `branch`, and `goto` are finite-control updates;
* `halt` maps the represented output-stack head through the imported output
  alphabet equivalence to the Programme accept/reject terminals.

Startup copies the exact read-only Boolean input to the designated input-stack
work tape, then rewinds both heads to zero before entering the source main
statement.

This file constructs the machine only.  The relational invariant and bounded
simulation theorem are proved separately.
-/

namespace MathSolve.PNP

noncomputable section

open Turing

/-- Read one represented source stack head from the selected Programme work tape. -/
def tm2ReadSourceHead? {decision : List Bool → Bool}
    (source : ImportedTM2Witness decision) (k : source.tm.K)
    (readWork : Fin (tm2WorkTapeCount source) → TM2ProgrammeSymbol source.tm) :
    Option (source.tm.Γ k) :=
  match readWork (tm2TapeEquiv source k) with
  | none => none
  | some token => tm2TokenValue? source k token

/-- Preserve every work-head cell. -/
def tm2PreserveWork {decision : List Bool → Bool}
    (source : ImportedTM2Witness decision)
    (readWork : Fin (tm2WorkTapeCount source) → TM2ProgrammeSymbol source.tm) :
    Fin (tm2WorkTapeCount source) → TM2ProgrammeSymbol source.tm :=
  readWork

/-- Replace only the currently scanned cell of source stack `k`. -/
def tm2WriteSelected {decision : List Bool → Bool}
    (source : ImportedTM2Witness decision)
    (readWork : Fin (tm2WorkTapeCount source) → TM2ProgrammeSymbol source.tm)
    (k : source.tm.K) (symbol : TM2ProgrammeSymbol source.tm) :
    Fin (tm2WorkTapeCount source) → TM2ProgrammeSymbol source.tm :=
  Function.update readWork (tm2TapeEquiv source k) symbol

/-- Move only the Programme work head assigned to source stack `k`. -/
def tm2MoveSelected {decision : List Bool → Bool}
    (source : ImportedTM2Witness decision) (k : source.tm.K) (move : HeadMove) :
    Fin (tm2WorkTapeCount source) → HeadMove :=
  Function.update (fun _ => HeadMove.stay) (tm2TapeEquiv source k) move

/-- Descend to the unique unary child of an accessible statement occurrence. -/
def tm2UnaryChildCode {decision : List Bool → Bool}
    (source : ImportedTM2Witness decision) (code : TM2StatementCode source.tm)
    (child : Turing.TM2.Stmt source.tm.Γ source.tm.Λ source.tm.σ)
    (hchild : child ∈ Turing.TM2.stmts₁ code.2.1) :
    TM2StatementCode source.tm :=
  TM2StatementCode.descend source.tm code child hchild

/-- Boolean decoded from the represented output-stack head, when valid. -/
def tm2OutputBit? {decision : List Bool → Bool}
    (source : ImportedTM2Witness decision)
    (readWork : Fin (tm2WorkTapeCount source) → TM2ProgrammeSymbol source.tm) :
    Option Bool :=
  (tm2ReadSourceHead? source source.tm.k₁ readWork).map source.outputAlphabet

/-- Recover the source stack selected by a generated push provenance token. -/
def tm2PushTokenStack? {decision : List Bool → Bool}
    (source : ImportedTM2Witness decision)
    (token : TM2ProvenanceToken source.tm) : Option source.tm.K :=
  match token with
  | .inl _ => none
  | .inr generated =>
      match generated.1.2.1 with
      | .push k _ _ => some k
      | _ => none

/-- A neutral action that preserves all work-head cells and positions. -/
def tm2StayAction {decision : List Bool → Bool}
    (source : ImportedTM2Witness decision)
    (next : TM2ProgrammeControl source)
    (readWork : Fin (tm2WorkTapeCount source) → TM2ProgrammeSymbol source.tm) :
    ProgrammeAction (TM2ProgrammeControl source) (TM2ProgrammeSymbol source.tm)
      (tm2WorkTapeCount source) where
  nextState := next
  inputMove := .stay
  write := tm2PreserveWork source readWork
  workMove := fun _ => .stay

/-- Execute one finite-control TM2 statement primitive. -/
def tm2RunAction {decision : List Bool → Bool}
    (source : ImportedTM2Witness decision)
    (code : TM2StatementCode source.tm) (state : source.tm.σ)
    (readWork : Fin (tm2WorkTapeCount source) → TM2ProgrammeSymbol source.tm) :
    ProgrammeAction (TM2ProgrammeControl source) (TM2ProgrammeSymbol source.tm)
      (tm2WorkTapeCount source) := by
  classical
  generalize hstmt : code.2.1 = stmt
  cases stmt with
  | push k valueFn nextStmt =>
      have hnext : nextStmt ∈ Turing.TM2.stmts₁ code.2.1 := by
        rw [hstmt]
        simp [Turing.TM2.stmts₁]
      let nextCode := tm2UnaryChildCode source code nextStmt hnext
      let token : TM2ProvenanceToken source.tm := Sum.inr (code, state)
      exact {
        nextState := tm2ControlPushWrite source nextCode state token
        inputMove := .stay
        write := tm2PreserveWork source readWork
        workMove := tm2MoveSelected source k .left
      }
  | peek k updateState nextStmt =>
      have hnext : nextStmt ∈ Turing.TM2.stmts₁ code.2.1 := by
        rw [hstmt]
        simp [Turing.TM2.stmts₁]
      let nextCode := tm2UnaryChildCode source code nextStmt hnext
      exact tm2StayAction source
        (tm2ControlRun source nextCode
          (updateState state (tm2ReadSourceHead? source k readWork)))
        readWork
  | pop k updateState nextStmt =>
      have hnext : nextStmt ∈ Turing.TM2.stmts₁ code.2.1 := by
        rw [hstmt]
        simp [Turing.TM2.stmts₁]
      let nextCode := tm2UnaryChildCode source code nextStmt hnext
      exact {
        nextState := tm2ControlRun source nextCode
          (updateState state (tm2ReadSourceHead? source k readWork))
        inputMove := .stay
        write := tm2WriteSelected source readWork k none
        workMove := tm2MoveSelected source k .right
      }
  | load updateState nextStmt =>
      have hnext : nextStmt ∈ Turing.TM2.stmts₁ code.2.1 := by
        rw [hstmt]
        simp [Turing.TM2.stmts₁]
      let nextCode := tm2UnaryChildCode source code nextStmt hnext
      exact tm2StayAction source
        (tm2ControlRun source nextCode (updateState state)) readWork
  | branch predicate trueStmt falseStmt =>
      by_cases hp : predicate state = true
      · have htrue : trueStmt ∈ Turing.TM2.stmts₁ code.2.1 := by
          rw [hstmt]
          simp [Turing.TM2.stmts₁]
        exact tm2StayAction source
          (tm2ControlRun source
            (tm2UnaryChildCode source code trueStmt htrue) state)
          readWork
      · have hfalse : falseStmt ∈ Turing.TM2.stmts₁ code.2.1 := by
          rw [hstmt]
          simp [Turing.TM2.stmts₁]
        exact tm2StayAction source
          (tm2ControlRun source
            (tm2UnaryChildCode source code falseStmt hfalse) state)
          readWork
  | goto nextLabel =>
      exact tm2StayAction source
        (tm2ControlRun source (TM2StatementCode.root source.tm (nextLabel state)) state)
        readWork
  | halt =>
      exact tm2StayAction source
        (match tm2OutputBit? source readWork with
         | some true => tm2ControlAccept source
         | _ => tm2ControlReject source)
        readWork

/-- Total Programme transition function implementing startup and TM2 execution. -/
def tm2ProgrammeTransition {decision : List Bool → Bool}
    (source : ImportedTM2Witness decision) :
    TM2ProgrammeControl source →
      Option Bool →
      (Fin (tm2WorkTapeCount source) → TM2ProgrammeSymbol source.tm) →
      ProgrammeAction (TM2ProgrammeControl source) (TM2ProgrammeSymbol source.tm)
        (tm2WorkTapeCount source)
  | control, inputSymbol, readWork =>
      if hcopy : control = tm2ControlCopy source then
        match inputSymbol with
        | some bit => {
            nextState := tm2ControlCopy source
            inputMove := .right
            write := tm2WriteSelected source readWork source.tm.k₀ (some (Sum.inl bit))
            workMove := tm2MoveSelected source source.tm.k₀ .right
          }
        | none => {
            nextState := tm2ControlRewind source
            inputMove := .left
            write := tm2PreserveWork source readWork
            workMove := tm2MoveSelected source source.tm.k₀ .left
          }
      else if hrewind : control = tm2ControlRewind source then
        match inputSymbol with
        | some _ => {
            nextState := tm2ControlRewind source
            inputMove := .left
            write := tm2PreserveWork source readWork
            workMove := tm2MoveSelected source source.tm.k₀ .left
          }
        | none => {
            nextState := tm2ControlInitialRun source
            inputMove := .right
            write := tm2PreserveWork source readWork
            workMove := tm2MoveSelected source source.tm.k₀ .right
          }
      else
        match control with
        | Sum.inr (Sum.inr (Sum.inl (code, state))) =>
            tm2RunAction source code state readWork
        | Sum.inr (Sum.inr (Sum.inr (Sum.inl (nextCode, state, token)))) =>
            match tm2PushTokenStack? source token with
            | some k => {
                nextState := tm2ControlRun source nextCode state
                inputMove := .stay
                write := tm2WriteSelected source readWork k (some token)
                workMove := fun _ => .stay
              }
            | none =>
                tm2StayAction source (tm2ControlReject source) readWork
        | _ => tm2StayAction source control readWork

/--
Concrete Programme machine compiled from a fixed imported finite TM2 witness.

The push-write administrative state is completed by the transition definition
below after the selected stack index is recoverable from the stored next
statement.  The full simulation theorem is the next proof obligation.
-/
def tm2ProgrammeMachine {decision : List Bool → Bool}
    (source : ImportedTM2Witness decision) : ProgrammeMachine where
  State := TM2ProgrammeControl source
  Symbol := TM2ProgrammeSymbol source.tm
  blank := tm2ProgrammeBlank source.tm
  workTapeCount := tm2WorkTapeCount source
  start := tm2ControlCopy source
  accept := tm2ControlAccept source
  reject := tm2ControlReject source
  accept_ne_reject := tm2ControlAccept_ne_reject source
  transition := tm2ProgrammeTransition source

#print axioms tm2ProgrammeMachine

end

end MathSolve.PNP
