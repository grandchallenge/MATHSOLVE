import PNPAbove.WP21Total

namespace PNPAbove.WP21
open MIPRE MIPRE.Cost

set_option maxRecDepth 8192
set_option maxHeartbeats 1000000

def nativeBaseEnv (nh nt : Data) (x y a b : BitStr) : Env :=
  let abtail : Data := .cons (encode a) (encode b)
  let ytail : Data := .cons (encode y) abtail
  let xtail : Data := .cons (encode x) ytail
  [encode a, encode b, encode y, abtail, encode x, ytail,
   nh, nt, .cons nh nt, xtail, .cons (.cons nh nt) xtail]

theorem source_shape (nh nt : Data) (x y a b : BitStr) :
    WP12.evalValue maskedParityDeciderProg
      [.cons (.cons nh nt)
        (.cons (encode x) (.cons (encode y)
          (.cons (encode a) (encode b))))] =
    WP12.evalValue
      (requireBits 4 9 (requireBits 5 9
        (requireBits 6 1 (requireBits 10 1 readAndDecide))))
      (nativeBaseEnv nh nt x y a b) := by rfl

theorem requireBits_bad (idx k : Nat) (env : Env) (xs : BitStr) (s : Prog)
    (he : env.get idx = encode xs) (hne : xs.length ≠ k) :
    WP12.evalValue (requireBits idx k s) env = encode false := by
  simp [requireBits, WP12.evalValue, reject,
    WP12.checkBits_value idx k env xs he, hne, SizedEncoding.encode,
    Data.ofBool]

theorem requireBits_good (idx k : Nat) (env : Env) (xs : BitStr) (s : Prog)
    (he : env.get idx = encode xs) (hlen : xs.length = k) :
    WP12.evalValue (requireBits idx k s) env =
      WP12.evalValue s (.nil :: .nil :: encode true :: env) := by
  simp [requireBits, WP12.evalValue, reject,
    WP12.checkBits_value idx k env xs he, hlen, SizedEncoding.encode,
    Data.ofBool]

theorem raw_x_bad (nh nt : Data) (x y a b : BitStr)
    (h : x.length ≠ 9) :
    WP12.evalValue maskedParityDeciderProg
      [.cons (.cons nh nt)
        (.cons (encode x) (.cons (encode y)
          (.cons (encode a) (encode b))))] = encode false := by
  rw [source_shape]
  apply requireBits_bad 4 9 _ x
  · simp [nativeBaseEnv, Env.get]
  · exact h

theorem raw_y_bad (nh nt : Data) (x y a b : BitStr)
    (hx : x.length = 9) (hy : y.length ≠ 9) :
    WP12.evalValue maskedParityDeciderProg
      [.cons (.cons nh nt)
        (.cons (encode x) (.cons (encode y)
          (.cons (encode a) (encode b))))] = encode false := by
  rw [source_shape]
  rw [requireBits_good 4 9 _ x _ (by simp [nativeBaseEnv, Env.get]) hx]
  apply requireBits_bad 5 9 _ y
  · simp [nativeBaseEnv, Env.get]
  · exact hy


theorem typed_x_bad (n : Nat) (x y a b : BitStr) (hx : x.length ≠ 9) :
    WP12.evalValue maskedParityDeciderProg [WP08.sample n x y a b] =
      encode false := by
  cases hnat : (encode n : Data) with
  | nil =>
      simp [WP08.sample, maskedParityDeciderProg, WP12.evalValue, hnat, reject,
        encode_prod]
  | cons nh nt =>
      simpa only [WP08.sample, encode_prod, hnat] using raw_x_bad nh nt x y a b hx

theorem typed_y_bad (n : Nat) (x y a b : BitStr)
    (hx : x.length = 9) (hy : y.length ≠ 9) :
    WP12.evalValue maskedParityDeciderProg [WP08.sample n x y a b] =
      encode false := by
  cases hnat : (encode n : Data) with
  | nil =>
      simp [WP08.sample, maskedParityDeciderProg, WP12.evalValue, hnat, reject,
        encode_prod]
  | cons nh nt =>
      simpa only [WP08.sample, encode_prod, hnat] using raw_y_bad nh nt x y a b hx hy

theorem decider_accepts_length (n : Nat) (x y a b : BitStr)
    (h : maskedParityDecider.Accepts n x y a b) :
    x.length = 9 ∧ y.length = 9 := by
  have hv := (accepts_iff_source_value n x y a b).mp h
  have hneq : (encode false : Data) ≠ encode true := by decide
  have hx : x.length = 9 := by
    by_contra hb
    exact hneq ((typed_x_bad n x y a b hb).symm.trans hv)
  refine ⟨hx, ?_⟩
  by_contra hy
  exact hneq ((typed_y_bad n x y a b hx hy).symm.trans hv)

end PNPAbove.WP21
