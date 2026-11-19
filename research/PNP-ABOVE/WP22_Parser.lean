import PNPAbove.WP22Evaluator

namespace PNPAbove.WP22
open MIPRE MIPRE.Cost PNPAbove.WP21
set_option maxRecDepth 8192
set_option maxHeartbeats 1000000

/-- All four original source bit-list guards are passed. The resulting
source evaluation equals the exact finite Boolean acceptance expression. -/
theorem raw_good (nh nt : Data) (x y a b : BitStr)
    (hx : x.length = 9) (hy : y.length = 9)
    (ha : a.length = 1) (hb : b.length = 1) :
    WP12.evalValue maskedParityDeciderProg
      [.cons (.cons nh nt)
        (.cons (encode x) (.cons (encode y)
          (.cons (encode a) (encode b))))] =
    encode (leafRule [b[0]!,a[0]!,y[8]!,y[0]!,x[8]!,x[0]!]) := by
  rw [source_shape]
  rw [requireBits_good 4 9 _ x _ (by simp [nativeBaseEnv, Env.get]) hx]
  rw [requireBits_good 5 9 _ y _ (by simp [nativeBaseEnv, Env.get]) hy]
  rw [requireBits_good 6 1 _ a _ (by simp [nativeBaseEnv, Env.get]) ha]
  rw [requireBits_good 10 1 _ b _ (by simp [nativeBaseEnv, Env.get]) hb]
  apply readAndDecide_value
  all_goals simp [nativeBaseEnv, Env.get]


/-- A malformed first answer is rejected by the third source guard. -/
theorem raw_a_bad (nh nt : Data) (x y a b : BitStr)
    (hx : x.length = 9) (hy : y.length = 9)
    (ha : a.length ≠ 1) :
    WP12.evalValue maskedParityDeciderProg
      [.cons (.cons nh nt)
        (.cons (encode x) (.cons (encode y)
          (.cons (encode a) (encode b))))] = encode false := by
  rw [source_shape]
  rw [requireBits_good 4 9 _ x _ (by simp [nativeBaseEnv, Env.get]) hx]
  rw [requireBits_good 5 9 _ y _ (by simp [nativeBaseEnv, Env.get]) hy]
  apply requireBits_bad 6 1 _ a
  · simp [nativeBaseEnv, Env.get]
  · exact ha

/-- A malformed second answer is rejected by the fourth source guard. -/
theorem raw_b_bad (nh nt : Data) (x y a b : BitStr)
    (hx : x.length = 9) (hy : y.length = 9)
    (ha : a.length = 1) (hb : b.length ≠ 1) :
    WP12.evalValue maskedParityDeciderProg
      [.cons (.cons nh nt)
        (.cons (encode x) (.cons (encode y)
          (.cons (encode a) (encode b))))] = encode false := by
  rw [source_shape]
  rw [requireBits_good 4 9 _ x _ (by simp [nativeBaseEnv, Env.get]) hx]
  rw [requireBits_good 5 9 _ y _ (by simp [nativeBaseEnv, Env.get]) hy]
  rw [requireBits_good 6 1 _ a _ (by simp [nativeBaseEnv, Env.get]) ha]
  apply requireBits_bad 10 1 _ b
  · simp [nativeBaseEnv, Env.get]
  · exact hb

/-- Source evaluator rejects the zero index on any typed fields. -/
theorem typed_zero (x y a b : BitStr) :
    WP12.evalValue maskedParityDeciderProg [WP08.sample 0 x y a b] =
      encode false := by
  rfl

/-- All well-formed typed inputs compute the exact six-bit predicate. -/
theorem typed_good (n : Nat) (x y a b : BitStr)
    (hn : n ≠ 0) (hx : x.length = 9) (hy : y.length = 9)
    (ha : a.length = 1) (hb : b.length = 1) :
    WP12.evalValue maskedParityDeciderProg [WP08.sample n x y a b] =
      encode (leafRule [b[0]!, a[0]!, y[8]!, y[0]!, x[8]!, x[0]!]) := by
  cases hnat : (encode n : Data) with
  | nil =>
      exact False.elim (hn ((WP12.encode_nat_nil_iff n).mp hnat))
  | cons nh nt =>
      simpa only [WP08.sample, encode_prod, hnat] using
        raw_good nh nt x y a b hx hy ha hb

/-- Bad first answer rejection is universal over all typed question bits. -/
theorem typed_a_bad (n : Nat) (x y a b : BitStr)
    (hx : x.length = 9) (hy : y.length = 9) (ha : a.length ≠ 1) :
    WP12.evalValue maskedParityDeciderProg [WP08.sample n x y a b] =
      encode false := by
  cases hnat : (encode n : Data) with
  | nil =>
      have hn : n = 0 := (WP12.encode_nat_nil_iff n).mp hnat
      simpa [hn] using typed_zero x y a b
  | cons nh nt =>
      simpa only [WP08.sample, encode_prod, hnat] using
        raw_a_bad nh nt x y a b hx hy ha

/-- Bad second answer rejection is universal over all typed question bits. -/
theorem typed_b_bad (n : Nat) (x y a b : BitStr)
    (hx : x.length = 9) (hy : y.length = 9)
    (ha : a.length = 1) (hb : b.length ≠ 1) :
    WP12.evalValue maskedParityDeciderProg [WP08.sample n x y a b] =
      encode false := by
  cases hnat : (encode n : Data) with
  | nil =>
      have hn : n = 0 := (WP12.encode_nat_nil_iff n).mp hnat
      simpa [hn] using typed_zero x y a b
  | cons nh nt =>
      simpa only [WP08.sample, encode_prod, hnat] using
        raw_b_bad nh nt x y a b hx hy ha hb


/-- Universal, typed original-source acceptance truth-table theorem,
including every invalid length and zero-index input. -/
theorem typed_value_spec (n : Nat) (x y a b : BitStr) :
    WP12.evalValue maskedParityDeciderProg [WP08.sample n x y a b] =
      encode (if n ≠ 0 ∧ x.length = 9 ∧ y.length = 9 ∧
        a.length = 1 ∧ b.length = 1
        then leafRule [b[0]!,a[0]!,y[8]!,y[0]!,x[8]!,x[0]!]
        else false) := by
  by_cases hn : n = 0
  · subst n
    simpa using typed_zero x y a b
  by_cases hx : x.length = 9
  · by_cases hy : y.length = 9
    · by_cases ha : a.length = 1
      · by_cases hb : b.length = 1
        · simpa [hn, hx, hy, ha, hb] using typed_good n x y a b hn hx hy ha hb
        · simpa [hn, hx, hy, ha, hb] using typed_b_bad n x y a b hx hy ha hb
      · simpa [hn, hx, hy, ha] using typed_a_bad n x y a b hx hy ha
    · simpa [hn, hx, hy] using typed_y_bad n x y a b hx hy
  · simpa [hn, hx] using typed_x_bad n x y a b hx

end PNPAbove.WP22
