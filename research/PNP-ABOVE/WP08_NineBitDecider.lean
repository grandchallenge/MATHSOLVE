import MIPRE.Foundations.Verifier

/-!
PNP-ABOVE WP08: actual imported MIPRE.Cost.Prog for the finite nine-bit
identity-game DECIDER component. Source MIPRE commit:
5926bdff5db621f44682a101007ef2fe3ae8d970.

Input convention: encode (n,x,y,a,b); n is a positive binary index,
x and y are canonical bit strings of exactly nine bits, and both
answers are empty. The proof burden for an actual nine-level CL
SAMPLER remains separate; this is not a Verifier 9 construction.
-/

namespace PNPAbove.WP08
open MIPRE
open MIPRE.Cost

def yes : Prog := .const (encode true)
def no : Prog := .const (encode false)

/-- Recognize a canonically encoded bit list of exactly k bits.
The parser accepts a bit encoding only if its head is nil (false)
or cons nil nil (true), and the tail has the required structure.
The index is a de Bruijn environment variable. -/
def checkBits (index : Nat) : Nat → Prog
  | 0 => .elim index yes no
  | k + 1 =>
      .elim index no
        (.elim 0
          (checkBits 1 k)
          (.elim 0 (.elim 1 (checkBits 3 k) no) no))

/-- Parse right-nested five-field tuple, require nonzero index,
empty answers, and two length-nine canonical questions.
The environment indices track each successive elim binding. -/
def identityDeciderProg : Prog :=
  .elim 0 no
    (.elim 0 no
      (.elim 3 no
        (.elim 1 no
          (.elim 1 no
            (.elim 0
              (.elim 1
                (.let_ (checkBits 4 9)
                  (.elim 0 no (checkBits 5 9)))
                no)
              no)))))

/-- The parser is well scoped whenever its input variable is bound. -/
theorem checkBits_wellScoped (k : Nat) :
    ∀ (idx n : Nat), idx < n → (checkBits idx k).WellScoped n := by
  induction k with
  | zero =>
      intro idx n h
      simp [checkBits, Prog.WellScoped, yes, no, h]
  | succ k ih =>
      intro idx n h
      simp only [checkBits, Prog.WellScoped]
      refine ⟨h, ?_, ?_⟩
      · simp [no, Prog.WellScoped]
      · refine ⟨by omega, ih 1 (n+2) (by omega), ?_⟩
        refine ⟨by omega, ?_, ?_⟩
        · refine ⟨by omega, ih 3 (n+4) (by omega), ?_⟩
          simp [no, Prog.WellScoped]
        · simp [no, Prog.WellScoped]

/-- Actual upstream decider structure, not a copied data type. -/
def identityDecider : MIPRE.Decider :=
  ⟨identityDeciderProg, by
    simp [identityDeciderProg, Prog.WellScoped, no, checkBits_wellScoped]⟩

/-- Independently fuel-bounded test evaluator for imported Prog.
Fuel is the recursion budget; its Nat result counts source Eval costs. -/
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

def zeroNine : BitStr := List.replicate 9 false
def alternatingNine : BitStr :=
  [true,false,true,false,true,false,true,false,true]
def eightBits : BitStr := List.replicate 8 false
def tenBits : BitStr := List.replicate 10 false

def sample (n : Nat) (x y a b : BitStr) : Data :=
  encode (n,x,y,a,b)

def output (n : Nat) (x y a b : BitStr) : Option Data :=
  (runFuel 96 [sample n x y a b] identityDeciderProg).map Prod.fst

-- Valid inputs, both possible nine-bit patterns and positive indices.
#guard decide (output 2 zeroNine zeroNine [] [] = some (encode true))
#guard decide (output 2 alternatingNine zeroNine [] [] = some (encode true))
#guard decide (output 10 zeroNine alternatingNine [] [] = some (encode true))
-- Input boundary: zero index, wrong lengths, and nonempty answers.
#guard decide (output 0 zeroNine zeroNine [] [] = some (encode false))
#guard decide (output 2 eightBits zeroNine [] [] = some (encode false))
#guard decide (output 2 tenBits zeroNine [] [] = some (encode false))
#guard decide (output 2 zeroNine eightBits [] [] = some (encode false))
#guard decide (output 2 zeroNine tenBits [] [] = some (encode false))
#guard decide (output 2 zeroNine zeroNine [true] [] = some (encode false))
#guard decide (output 2 zeroNine zeroNine [] [false] = some (encode false))
-- Malformed tuple and insufficient fuel: distinct rejection/timeout cases.
#guard decide ((runFuel 96 [.nil] identityDeciderProg).map Prod.fst =
  some (encode false))
#guard decide (runFuel 1 [sample 2 zeroNine zeroNine [] []] identityDeciderProg = none)

/-- Enumerate all nine-bit vectors; the sampler's diagonal support has 512 points. -/
def vectorNine (k : Nat) : BitStr :=
  (List.range 9).map (fun i => Nat.testBit k i)

def allDiagonalChecks : Bool :=
  (List.range 512).all fun k =>
    decide (output 2 (vectorNine k) (vectorNine k) [] [] = some (encode true))

-- A malformed head has the right list length, but is not a canonical Bool.
def malformedHead : Data :=
  .cons (.cons .nil (.cons .nil .nil)) (encode eightBits)

def malformedQuestionData : Data :=
  .cons (encode (2 : Nat))
    (.cons malformedHead
      (.cons (encode zeroNine)
        (.cons (encode ([] : BitStr)) (encode ([] : BitStr)))))

#guard allDiagonalChecks
#guard decide ((runFuel 96 [malformedQuestionData] identityDeciderProg).map Prod.fst =
  some (encode false))

#eval esize identityDeciderProg
#eval runFuel 96 [sample 2 zeroNine alternatingNine [] []] identityDeciderProg
end PNPAbove.WP08
