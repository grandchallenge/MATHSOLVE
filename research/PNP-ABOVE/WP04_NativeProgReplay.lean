import Init
/-! PNP-ABOVE WP04. Standalone implementation of the MIPRE.Cost native
Data/Prog/Eval signatures and a fuel-limited executable evaluator.
Source: vidick/MIPRE-formalization commit
5926bdff5db621f44682a101007ef2fe3ae8d970,
MIPRE/Foundations/Cost/Basic.lean. This independent file does not import
the upstream library and does not execute the quantum compressor. -/
namespace PNPAbove.WP04

inductive Data where
  | nil
  | cons : Data → Data → Data
  deriving DecidableEq, BEq, Repr, Inhabited

def Data.size : Data → Nat
  | .nil => 1
  | .cons a b => a.size + b.size + 1

inductive Prog where
  | var (i : Nat)
  | nil
  | const (d : Data)
  | cons (h t : Prog)
  | elim (i : Nat) (n c : Prog)
  | let_ (e b : Prog)
  | loop (b : Prog)
  deriving DecidableEq, BEq, Repr, Inhabited

abbrev Env := List Data
def Env.get (env : Env) (i : Nat) : Data := env.getD i .nil

/-- Upstream cost and loop transition rules, reproduced as a specification. -/
inductive Eval : Env → Prog → Data → Nat → Prop
  | var (env : Env) (i : Nat) :
      Eval env (.var i) (env.get i) ((env.get i).size + 1)
  | nil (env : Env) : Eval env .nil .nil 1
  | const (env : Env) (d : Data) : Eval env (.const d) d d.size
  | cons {env : Env} {h t : Prog} {a b : Data} {s u : Nat} :
      Eval env h a s → Eval env t b u →
      Eval env (.cons h t) (.cons a b) (s + u + 1)
  | elim_nil {env : Env} {i : Nat} {n c : Prog} {r : Data} {t : Nat} :
      env.get i = .nil → Eval env n r t →
      Eval env (.elim i n c) r (t + 1)
  | elim_cons {env : Env} {i : Nat} {n c : Prog} {a b r : Data} {t : Nat} :
      env.get i = .cons a b → Eval (a :: b :: env) c r t →
      Eval env (.elim i n c) r (t + 1)
  | let_ {env : Env} {e b : Prog} {v r : Data} {s t : Nat} :
      Eval env e v s → Eval (v :: env) b r t →
      Eval env (.let_ e b) r (s + t + 1)
  | loop_nil {env : Env} {b : Prog} {t : Nat} :
      Eval env b .nil t → Eval env (.loop b) .nil (t + 1)
  | loop_stop {env : Env} {b : Prog} {r : Data} {t : Nat} :
      Eval env b (.cons .nil r) t → Eval env (.loop b) r (t + 1)
  | loop_step {env : Env} {b : Prog} {x y v r : Data} {s t : Nat} :
      Eval env b (.cons (.cons x y) v) s →
      Eval (v :: env.tail) (.loop b) r t →
      Eval env (.loop b) r (s + t + 1)

/-- Fuel counts interpreter recursion, not the source cost units. -/
def runFuel : Nat → Env → Prog → Option (Data × Nat)
  | 0, _, _ => none
  | fuel + 1, env, p =>
    match p with
    | .var i => some (env.get i, (env.get i).size + 1)
    | .nil => some (.nil, 1)
    | .const d => some (d, d.size)
    | .cons h t => do
        let (a,s) ← runFuel fuel env h
        let (b,u) ← runFuel fuel env t
        pure (.cons a b, s+u+1)
    | .elim i n c =>
        match env.get i with
        | .nil => do
            let (r,t) ← runFuel fuel env n
            pure (r,t+1)
        | .cons a b => do
            let (r,t) ← runFuel fuel (a :: b :: env) c
            pure (r,t+1)
    | .let_ e b => do
        let (v,s) ← runFuel fuel env e
        let (r,t) ← runFuel fuel (v :: env) b
        pure (r,s+t+1)
    | .loop b =>
        match runFuel fuel env b with
        | none => none
        | some (.nil,t) => some (.nil,t+1)
        | some (.cons flag v,s) =>
            match flag with
            | .nil => some (v,s+1)
            | .cons _ _ => do
                let (r,t) ← runFuel fuel (v :: env.tail) (.loop b)
                pure (r,s+t+1)

def d : Data := .cons .nil .nil
def stopBody : Prog := .cons .nil (.var 0)
def stepBody : Prog :=
  .elim 0 (.cons .nil .nil) (.cons (.cons .nil .nil) .nil)

#guard runFuel 12 [d] (.var 0) == some (d,4)
#guard runFuel 12 [d] (.var 9) == some (.nil,2)
#guard runFuel 12 [d] (.const d) == some (d,3)
#guard runFuel 12 [d] (.cons (.const d) .nil) == some (.cons d .nil,5)
#guard runFuel 12 [d] (.elim 0 (.const d) (.var 0)) == some (.nil,3)
#guard runFuel 12 [.nil] (.elim 0 (.const d) (.var 0)) == some (d,4)
#guard runFuel 12 [d] (.let_ (.var 0) (.var 0)) == some (d,9)
#guard runFuel 12 [d] (.loop stopBody) == some (d,7)
#guard runFuel 12 [d] (.loop stepBody) == some (.nil,12)
#guard runFuel 1 [d] (.loop stepBody) == none

example (x : Data) : Eval [x] (.var 0) x (x.size+1) := by
  simpa [Env.get] using (Eval.var [x] 0)

example : Eval [d] (.loop stopBody) d 7 := by
  unfold stopBody
  apply Eval.loop_stop
  simpa [d, Data.size, Env.get] using
    (Eval.cons (Eval.nil [d]) (Eval.var [d] 0))

#eval runFuel 12 [d] (.loop stepBody)
end PNPAbove.WP04
