import MIPRE.Foundations.Cost.Basic
/-!
PNP-ABOVE WP05: genuine upstream MIPRE.Cost.Prog / Eval import.
Primary source vidick/MIPRE-formalization at
5926bdff5db621f44682a101007ef2fe3ae8d970.
Unlike WP04, no copies of Data, Prog or Eval are declared here.
The fuel-based interpreter is independent; its correctness relative to the
upstream Eval relation is tested on examples, not yet proved generally.
-/
namespace PNPAbove.WP05
open MIPRE.Cost

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

#guard decide (runFuel 12 [d] (.var 0) = some (d,4))
#guard decide (runFuel 12 [d] (.var 9) = some (.nil,2))
#guard decide (runFuel 12 [d] (.const d) = some (d,3))
#guard decide (runFuel 12 [d] (.cons (.const d) .nil) = some (.cons d .nil,5))
#guard decide (runFuel 12 [d] (.elim 0 (.const d) (.var 0)) = some (.nil,3))
#guard decide (runFuel 12 [.nil] (.elim 0 (.const d) (.var 0)) = some (d,4))
#guard decide (runFuel 12 [d] (.let_ (.var 0) (.var 0)) = some (d,9))
#guard decide (runFuel 12 [d] (.loop stopBody) = some (d,7))
#guard decide (runFuel 12 [d] (.loop stepBody) = some (.nil,12))
#guard decide (runFuel 1 [d] (.loop stepBody) = none)

example (x : Data) : Eval [x] (.var 0) x (x.size+1) := by
  simpa [Env.get] using (Eval.var [x] 0)

example : Eval [d] (.loop stopBody) d 7 := by
  unfold stopBody
  apply Eval.loop_stop
  simpa [d, Data.size, Env.get] using
    (Eval.cons (Eval.nil [d]) (Eval.var [d] 0))

#eval runFuel 12 [d] (.loop stepBody)
end PNPAbove.WP05
