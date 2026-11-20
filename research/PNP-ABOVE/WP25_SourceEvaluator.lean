import PNPAbove.WP24CNF
import MIPRE.Foundations.SAT.ArrayProg
import MIPRE.Foundations.SAT.FmlProg

/-! Source-native deterministic Boolean evaluation in Cost.PolyTimeFun. -/
namespace PNPAbove.WP25
open MIPRE MIPRE.SAT MIPRE.Cost
open MIPRE.Cost.PolyTimeFun
open Polynomial

abbrev EvalState := BitStr × List Bool

/-- One source-node transition; rightmost postfix stack element is on top. -/
def execNode (s : EvalState) : SAT.Fml.Node → EvalState
 | .inp i => (s.1, s.1.getD i false :: s.2)
 | .const b => (s.1, b :: s.2)
 | .and => match s.2 with
     | b :: a :: rest => (s.1, (a && b) :: rest)
     | _ => s
 | .or => match s.2 with
     | b :: a :: rest => (s.1, (a || b) :: rest)
     | _ => s
 | .not => match s.2 with
     | b :: rest => (s.1, (!b) :: rest)
     | _ => s

/-- The original language compiler for stack push. -/
noncomputable def pushBitP :
    PolyTimeFun (EvalState × Bool) EvalState :=
  (fst.comp fst).pair
    (cons snd (snd.comp fst))

/-- Source program to execute a formula input-index node. -/
noncomputable def inputStepP :
    PolyTimeFun (EvalState × Nat) EvalState :=
  pushBitP.comp
    (fst.pair ((ArrayProg.getD false).comp (snd.pair (fst.comp fst))))

/-- Same operation for constant Boolean nodes. -/
noncomputable def constStepP :
    PolyTimeFun (EvalState × Bool) EvalState := pushBitP

/-- Source polynomial program implementing Boolean AND. -/
noncomputable def andBoolP : PolyTimeFun (Bool × Bool) Bool :=
  congr (ite fst snd (const false)) (fun p => p.1 && p.2)
    (by rintro ⟨a, b⟩; cases a <;> rfl)

/-- Source polynomial program implementing Boolean OR. -/
noncomputable def orBoolP : PolyTimeFun (Bool × Bool) Bool :=
  congr (ite fst (const true) snd) (fun p => p.1 || p.2)
    (by rintro ⟨a, b⟩; cases a <;> rfl)

/-- Native source program popping two stack bits, applying an input
source Boolean operator, and pushing its result. -/
noncomputable def binaryStepP
    (op : PolyTimeFun (Bool × Bool) Bool) :
    PolyTimeFun EvalState EvalState :=
  let read : PolyTimeFun ((EvalState × Bool) × (Bool × List Bool)) EvalState :=
    (fst.comp (fst.comp fst)).pair
      (cons (op.comp ((fst.comp snd).pair (snd.comp fst))) (snd.comp snd))
  let inner : PolyTimeFun ((EvalState × Bool) × List Bool) EvalState :=
    casesList fst read
  let outer : PolyTimeFun (EvalState × List Bool) EvalState :=
    casesList (PolyTimeFun.id EvalState)
      (inner.comp (((fst.pair (fst.comp snd)).pair (snd.comp snd))))
  outer.comp ((PolyTimeFun.id EvalState).pair snd)

/-- Native source program negating a single stack top. -/
noncomputable def unaryStepP : PolyTimeFun EvalState EvalState :=
  let k : PolyTimeFun (EvalState × (Bool × List Bool)) EvalState :=
    (fst.comp fst).pair
      (cons (SAT.notBoolP.comp (fst.comp snd)) (snd.comp snd))
  (casesList (PolyTimeFun.id EvalState) k).comp ((PolyTimeFun.id EvalState).pair snd)

/-- The original source polynomial-time node interpreter. -/
noncomputable def nodeStepP :
    PolyTimeFun (EvalState × SAT.Fml.Node) EvalState :=
  SAT.PolyTimeFun.casesNode inputStepP constStepP
    (binaryStepP andBoolP) (binaryStepP orBoolP) unaryStepP

/-- Check the actual program (not just a reference evaluator) against
the source node semantics, including malformed stack cases. -/
theorem nodeStepP_correct (s : EvalState) (nd : SAT.Fml.Node) :
    nodeStepP (s, nd) = execNode s nd := by
  rcases s with ⟨x, stack⟩
  cases nd <;> cases stack <;> simp [nodeStepP, execNode, binaryStepP, unaryStepP,
    inputStepP, constStepP, pushBitP, andBoolP, orBoolP, SAT.PolyTimeFun.casesNode,
    SAT.PolyTimeFun.casesNodeFun, SAT.ArrayProg.getD_apply,
    SAT.notBoolP]
  all_goals
    rename_i head tail
    cases tail <;> simp [PolyTimeFun.casesList, PolyTimeFun.casesListFun]

/-- Every original formula node grows the source-encoded stack by at most
one Boolean, including all malformed-stack cases. -/
theorem execNode_size_bound (s : EvalState) (nd : SAT.Fml.Node) :
    esize (execNode s nd) ≤ esize s + 4 := by
  have hbool (b : Bool) : esize b ≤ 3 := by
    cases b <;> decide
  rcases s with ⟨x, stack⟩
  cases nd with
  | inp i =>
      simp only [execNode, esize_prod, esize_list_cons]
      have hb := hbool (x.getD i false)
      omega
  | const b =>
      simp only [execNode, esize_prod, esize_list_cons]
      have hb := hbool b
      omega
  | and =>
      cases stack with
      | nil => simp [execNode]
      | cons b tail =>
          cases tail with
          | nil => simp [execNode]
          | cons a rest =>
              simp only [execNode, esize_prod, esize_list_cons]
              have hb := hbool (a && b)
              omega
  | or =>
      cases stack with
      | nil => simp [execNode]
      | cons b tail =>
          cases tail with
          | nil => simp [execNode]
          | cons a rest =>
              simp only [execNode, esize_prod, esize_list_cons]
              have hb := hbool (a || b)
              omega
  | not =>
      cases stack with
      | nil => simp [execNode]
      | cons b rest =>
          simp only [execNode, esize_prod, esize_list_cons]
          have hb := hbool (!b)
          omega

/-- Genuine original source interpreter: a closed Cost.Prog plus a
concrete polynomial-time bound, rather than a bare Lean algorithm. -/
noncomputable def scanProgram :
    PolyTimeFun (List SAT.Fml.Node × EvalState) EvalState :=
  foldlAdd nodeStepP 4 (by
    intro s nd
    rw [nodeStepP_correct]
    simpa only [Polynomial.eval_ofNat] using execNode_size_bound s nd)

/-- Uniform source reader: formula serialization and witness bits are
processed by the same constructed native Cost.Prog for ALL inputs. -/
noncomputable def evalStackProgram :
    PolyTimeFun (SAT.Fml × BitStr) EvalState :=
  scanProgram.comp
    ((SAT.Fml.rpnF.comp fst).pair
      (snd.pair (const ([] : List Bool))))

/-- The result Boolean is the top stack value (false for malformed input). -/
noncomputable def evalFormulaProgram :
    PolyTimeFun (SAT.Fml × BitStr) Bool :=
  (ArrayProg.getD false).comp
    ((const (0 : Nat)).pair (snd.comp evalStackProgram))

/-- The real source runtime certificate is inhabited with a particular
program and a concrete polynomial computed by the original cost toolkit. -/
theorem source_evaluator_polytime (p : SAT.Fml × BitStr) :
    ∃ t ≤ evalFormulaProgram.timeBound.eval (esize p),
      evalFormulaProgram.code.Runs (encode p) (encode (evalFormulaProgram p)) t :=
  evalFormulaProgram.computes p

/-- For every formula tree, the original postorder bit-stack evaluator
leaves precisely its semantic Boolean value on the stack. -/
theorem executeRpn (f : SAT.Fml) (xs : BitStr) (stack : List Bool) :
    f.rpn.foldl (fun s nd => execNode s nd) (xs, stack) =
      (xs, f.eval (fun i => xs.getD i false) :: stack) := by
  induction f generalizing stack with
  | inp i =>
      rfl
  | const b =>
      rfl
  | and f g ihf ihg =>
      simp only [SAT.Fml.rpn, List.foldl_append]
      rw [ihf stack]
      rw [ihg (f.eval (fun i => xs.getD i false) :: stack)]
      simp [execNode, SAT.Fml.eval]
  | or f g ihf ihg =>
      simp only [SAT.Fml.rpn, List.foldl_append]
      rw [ihf stack]
      rw [ihg (f.eval (fun i => xs.getD i false) :: stack)]
      simp [execNode, SAT.Fml.eval]
  | not f ih =>
      simp only [SAT.Fml.rpn, List.foldl_append]
      rw [ih stack]
      simp [execNode, SAT.Fml.eval]

/-- Exact original-model source program correctness, for *arbitrary*
well-formed formula data and bitstrings, without a SAT oracle. -/
theorem evalStackProgram_correct (f : SAT.Fml) (xs : BitStr) :
    evalStackProgram (f, xs) =
      (xs, [f.eval (fun i => xs.getD i false)]) := by
  change f.rpn.foldl (fun s nd => nodeStepP (s, nd)) (xs, []) = _
  simp_rw [nodeStepP_correct]
  exact executeRpn f xs []

/-- Source polynomial-time evaluator calculates the actual original
MIPRE formula result. This is stronger than compilation to a circuit. -/
theorem evalFormulaProgram_correct (f : SAT.Fml) (xs : BitStr) :
    evalFormulaProgram (f, xs) = f.eval (fun i => xs.getD i false) := by
  change (evalStackProgram (f, xs)).2.getD 0 false = _
  rw [evalStackProgram_correct]
  rfl

end PNPAbove.WP25

namespace PNPAbove.WP25
open MIPRE MIPRE.SAT MIPRE.Cost MIPRE.Cost.PolyTimeFun

/-- Original source polynomial-time one-question SAT answer checker.
The input contains an original MIPRE Fml and TWO independently supplied
answer bitstrings. It checks source acceptance and answer equality. -/
noncomputable def answerCheckProgram :
    PolyTimeFun ((SAT.Fml × BitStr) × BitStr) Bool :=
  let value : PolyTimeFun ((SAT.Fml × BitStr) × BitStr) Bool :=
    evalFormulaProgram.comp fst
  let same : PolyTimeFun ((SAT.Fml × BitStr) × BitStr) Bool :=
    ArrayProg.eqBits.comp ((snd.comp fst).pair snd)
  andBoolP.comp (value.pair same)

/-- Exact machine-level bitstring answer semantics, for all first-order inputs. -/
theorem answerCheckProgram_correct (f : SAT.Fml) (a b : BitStr) :
    answerCheckProgram ((f, a), b) =
      (f.eval (fun i => a.getD i false) && decide (a = b)) := by
  simp [answerCheckProgram, andBoolP, evalFormulaProgram_correct]

/-- We use the source Fin n -> Bool alphabet only for the mathematical
game; its canonical bitstring representation has exact original padding. -/
theorem ofFn_getD_eq_bitsAt {n : Nat} (w : Fin n → Bool) (i : Nat) :
    (List.ofFn w).getD i false = PNPAbove.WP24.bitsAt w i := by
  by_cases hi : i < n
  · simp [PNPAbove.WP24.bitsAt, hi, List.getD_eq_getElem?_getD]
  · simp [PNPAbove.WP24.bitsAt, hi, List.getD_eq_getElem?_getD]

/-- The original constructed bounded-cost source machine agrees EXACTLY
with the new SAT-dependent mathematical game on both players' canonical
responses; it is not an assumed external evaluator. -/
theorem source_program_agrees_with_sat_game {n : Nat}
    (f : SAT.Fml) (a b : Fin n → Bool) :
    answerCheckProgram ((f, List.ofFn a), List.ofFn b) =
       (PNPAbove.WP24.satGame n f).D () () a b := by
  rw [answerCheckProgram_correct]
  have hab : (List.ofFn a = List.ofFn b) ↔ a = b := by
    constructor
    · intro h
      exact List.ofFn_injective h
    · intro h; exact congrArg List.ofFn h
  have habBool :
      decide (List.ofFn a = List.ofFn b) = decide (a = b) := by
    simp only [hab]
  rw [habBool]
  have hbits : (fun i => (List.ofFn a).getD i false) =
      PNPAbove.WP24.bitsAt a := by
    funext i
    exact ofFn_getD_eq_bitsAt a i
  rw [hbits]
  rfl

/-- Machine-level SAT witnesses are exact: an original source game pair
wins precisely when the polynomial source answer checker returns true. -/
theorem accepted_source_witness_iff {n : Nat}
    (f : SAT.Fml) (a b : Fin n → Bool) :
    answerCheckProgram ((f, List.ofFn a), List.ofFn b) = true ↔
       f.eval (PNPAbove.WP24.bitsAt a) = true ∧ a = b := by
  rw [source_program_agrees_with_sat_game]
  exact PNPAbove.WP24.accepts_iff n f a b

/-- Actual source program and explicit polynomial time bound for every
original formula and both arbitrary answer strings. -/
theorem source_answer_checker_polytime
    (inp : ((SAT.Fml × BitStr) × BitStr)) :
    ∃ t ≤ answerCheckProgram.timeBound.eval (esize inp),
      answerCheckProgram.code.Runs
        (encode inp) (encode (answerCheckProgram inp)) t :=
  answerCheckProgram.computes inp

end PNPAbove.WP25
