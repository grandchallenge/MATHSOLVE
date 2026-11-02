import MIPRE.Foundations.Cost.Encoding

/-!
PNP-ABOVE WP08: actual upstream Cost.Prog finite-nine-bit query-pair and
answer-checking *component* programs, at pinned vidick/MIPRE-formalization
5926bdff5db621f44682a101007ef2fe3ae8d970.
No copy of native Data, Prog, Eval or SizedEncoding. This is not yet a
CL.Sampler 9 object or a full normal-form Verifier 9, nor a quantum compressor.
-/
namespace PNPAbove.WP08
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


/-- One native program converts the input encoded nine-bit seed z to
the diagonal encoded question pair (z,z). -/
def diagonalPair : Prog := .cons (.var 0) (.var 0)

/-- Exactly k list nodes at index i. The encoded Bool element in each
node is assumed canonical when testing encoded BitStr values. -/
def lengthCheck (i : Nat) : Nat → Prog → Prog → Prog
  | 0, yes, no => .elim i yes no
  | k+1, yes, no => .elim i no (lengthCheck 1 k yes no)

/-- Read native encoded input (n,x,y,a,b). On canonical encodings,
accept iff n is positive, |x|=|y|=9 and both answers are empty.
Malformed noncanonical question *elements* are not validated. -/
def identityAnswerCheck : Prog :=
  .elim 0 .nil (
    .elim 1 .nil (
      .elim 1 .nil (
        .elim 1 .nil (
          .elim 0 (
            .elim 1 (
              .elim 6 .nil (
                lengthCheck 6 9
                  (lengthCheck 22 9 (.const (encode true)) .nil)
                  .nil
              )
            ) .nil
          ) .nil
        )
      )
    )
  )

/-- Canonical sequence of all 512 possible nine-bit inputs, low bit first. -/
def nineBits (m : Nat) : MIPRE.Cost.BitStr :=
  (List.range 9).map (fun i => decide (Nat.testBit m i))

def trueResult : Data := encode true
def check (n : Nat) (x y a b : MIPRE.Cost.BitStr) : Option (Data × Nat) :=
  runFuel 50 [encode (n,x,y,a,b)] identityAnswerCheck

#guard (List.range 512).all fun m =>
  let z := nineBits m
  z.length == 9 && runFuel 4 [encode z] diagonalPair ==
    some (encode (z,z), 2 * (esize z + 1) + 1)

#guard (List.range 512).all fun m =>
  let z := nineBits m
  (check 2 z z [] []).map Prod.fst == some trueResult

#guard (List.range 512).all fun m =>
  let z := nineBits m
  (check 2 z z [true] []).map Prod.fst == some .nil

#guard (check 0 (nineBits 0) (nineBits 0) [] []).map Prod.fst == some .nil
#guard (check 2 (List.replicate 8 false) (nineBits 0) [] []).map Prod.fst == some .nil
#guard (check 2 (nineBits 0) (List.replicate 10 false) [] []).map Prod.fst == some .nil

/-- A source-native Eval witness for the diagonal pair-building program.
The runtime cost is exactly two copies plus one constructor. -/
theorem diagonal_pair_eval (z : MIPRE.Cost.BitStr) :
    Eval [encode z] diagonalPair (encode (z,z))
      (2 * (esize z + 1) + 1) := by
  change Eval [encode z] (.cons (.var 0) (.var 0))
    (.cons (encode z) (encode z)) _
  convert (Eval.cons (Eval.var [encode z] 0) (Eval.var [encode z] 0)) using 1 <;>
    simp [Env.get, esize] <;> omega

#eval ((List.range 512).map nineBits).length
#eval (check 2 (nineBits 511) (nineBits 511) [] []).map Prod.fst

end PNPAbove.WP08
