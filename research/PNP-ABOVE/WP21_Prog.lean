import PNPAbove.WP21Masked

/-!
An original imported MIPRE.Cost.Prog implementation of a support-masked,
answer-sensitive CHSH decider. Inputs are the original five-field encodings.
The syntactic parser rejects noncanonical questions and answers, requiring
two length-nine bit lists and two length-one bit lists.
-/
namespace PNPAbove.WP21
open MIPRE MIPRE.Cost
open PNPAbove.WP20

def reject : Prog := .const (encode false)

/-- Validate a canonical, exactly-k-bit encoded list and enter its success
continuation. In the successful branch the surrounding environment indices
are shifted by three (one let binding and one successful elim binding). -/
def requireBits (idx k : Nat) (success : Prog) : Prog :=
  .let_ (WP08.checkBits idx k)
    (.elim 0 reject (.elim 0 success reject))

/-- Read the k-th Boolean cell of an encoded bit list as native Data.
The validity guard is separate; the fallback on malformed input is nil. -/
def readBit : Nat → Nat → Prog
  | idx, 0 => .elim idx .nil (.var 0)
  | idx, k + 1 => .elim idx .nil (readBit 1 k)

/-- The six extracted Booleans are listed b,a,y8,y0,x8,x0.
All noncanonical cases are rejected by the prior guards. -/
def leafRule : List Bool → Bool
  | [b,a,y8,y0,x8,x0] =>
      (!x8 && !y0) && decide (a.xor b = (x0 && y8))
  | _ => false

/-- Finite branching native source program: each elim inspects one previously
extracted Boolean; success branches insert exactly two de Bruijn variables. -/
def truthTree : List Nat → List Bool → Nat → Prog
  | [], chosen, _ => .const (encode (leafRule chosen.reverse))
  | i :: is, chosen, offset =>
      .elim (offset + i)
        (truthTree is (false :: chosen) offset)
        (truthTree is (true :: chosen) (offset + 2))

/-- At the entry to this block, source x,y,a,b occupy de Bruijn indices
16,14,12,13. The six let bindings extract the required individual bits. -/
def readAndDecide : Prog :=
  .let_ (readBit 16 0)
    (.let_ (readBit 17 8)
      (.let_ (readBit 16 0)
        (.let_ (readBit 17 8)
          (.let_ (readBit 16 0)
            (.let_ (readBit 18 0)
              (truthTree [0,1,2,3,4,5] [] 0))))))

/-- Five-field original input parser. Nonpositive n and malformed tuple
shapes are rejected. No unbounded loops or noncanonical answers are accepted. -/
def maskedParityDeciderProg : Prog :=
  .elim 0 reject
    (.elim 0 reject
      (.elim 3 reject
        (.elim 1 reject
          (.elim 1 reject
            (requireBits 4 9
              (requireBits 5 9
                (requireBits 6 1
                  (requireBits 10 1 readAndDecide))))))))

/- Exact syntactic-program guards. -/
#guard decide ((WP08.runFuel 1000
  [WP08.sample 2 (List.replicate 9 false) (List.replicate 9 false)
    [false] [false]] maskedParityDeciderProg).map Prod.fst = some (encode true))
#guard decide ((WP08.runFuel 1000
  [WP08.sample 2 (List.replicate 9 false) (List.replicate 9 false)
    [false] [true]] maskedParityDeciderProg).map Prod.fst = some (encode false))

end PNPAbove.WP21
