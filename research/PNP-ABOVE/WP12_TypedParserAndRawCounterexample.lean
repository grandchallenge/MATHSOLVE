import PNPAbove.WP11
namespace PNPAbove.WP12
open MIPRE MIPRE.Cost

/-- An independent *structurally recursive* evaluator for the source language's
loop-free fragment. The loop case is an irrelevant dummy on this fragment. -/
def evalValue : Prog → Env → Data
  | .var i, env => env.get i
  | .nil, _ => .nil
  | .const d, _ => d
  | .cons a b, env => .cons (evalValue a env) (evalValue b env)
  | .elim i a b, env =>
      match env.get i with
      | .nil => evalValue a env
      | .cons h t => evalValue b (h :: t :: env)
  | .let_ a b, env => evalValue b (evalValue a env :: env)
  | .loop _, _ => .nil

/-- Evaluation of a loop-free source program always agrees with the
structural evaluator in any raw source environment. -/
theorem evalValue_sound : ∀ p : Prog, ∀ env : Env,
    WP11.LoopFree p → ∃ t, Eval env p (evalValue p env) t := by
  intro p
  induction p with
  | var i =>
      intro env hp
      exact ⟨_, Eval.var env i⟩
  | nil =>
      intro env hp
      exact ⟨1, Eval.nil env⟩
  | const d =>
      intro env hp
      exact ⟨_, Eval.const env d⟩
  | cons a b iha ihb =>
      intro env hp
      obtain ⟨ta, ha⟩ := iha env hp.1
      obtain ⟨tb, hb⟩ := ihb env hp.2
      exact ⟨_, Eval.cons ha hb⟩
  | elim i a b iha ihb =>
      intro env hp
      cases he : env.get i with
      | nil =>
          obtain ⟨t, ht⟩ := iha env hp.1
          exact ⟨t+1, by simpa [evalValue, he] using (Eval.elim_nil he ht)⟩
      | cons h t =>
          obtain ⟨u, hu⟩ := ihb (h :: t :: env) hp.2
          exact ⟨u+1, by simpa [evalValue, he] using (Eval.elim_cons he hu)⟩
  | let_ a b iha ihb =>
      intro env hp
      obtain ⟨t, ht⟩ := iha env hp.1
      obtain ⟨u, hu⟩ := ihb (evalValue a env :: env) hp.2
      exact ⟨t+u+1, by simpa [evalValue] using (Eval.let_ ht hu)⟩
  | loop b ih =>
      intro env hp
      cases hp

/-- Native acceptance reduces to a value equality for the original WP08
program, in the actual source Eval relation. -/
theorem accepts_iff_evalValue (n : Nat) (x y a b : BitStr) :
    WP08.identityDecider.Accepts n x y a b ↔
      evalValue WP08.identityDeciderProg [WP08.sample n x y a b] = encode true := by
  obtain ⟨t, hsource⟩ :=
    evalValue_sound WP08.identityDeciderProg [WP08.sample n x y a b]
      WP11.identityDecider_loopfree
  constructor
  · intro hacc
    change ∃ t, Eval [WP08.sample n x y a b]
      WP08.identityDeciderProg (encode true) t at hacc
    obtain ⟨u, hu⟩ := hacc
    exact (Eval.deterministic hsource hu).1
  · intro h
    change ∃ t, Eval [WP08.sample n x y a b]
      WP08.identityDeciderProg (encode true) t
    exact ⟨t, h ▸ hsource⟩


/-- The original WP08 parser for a canonical encoded bit string succeeds
exactly when its source list has the designated length. -/
theorem checkBits_value (idx k : Nat) (env : Env) (xs : BitStr)
    (he : env.get idx = encode xs) :
    evalValue (WP08.checkBits idx k) env =
      (if xs.length = k then encode true else encode false) := by
  induction k generalizing idx env xs with
  | zero =>
      cases xs with
      | nil => simp [WP08.checkBits, evalValue, WP08.yes, WP08.no, he,
          SizedEncoding.encode, Data.ofList]
      | cons b xs => simp [WP08.checkBits, evalValue, WP08.no, he,
          SizedEncoding.encode, Data.ofList]
  | succ k ih =>
      cases xs with
      | nil => simp [WP08.checkBits, evalValue, WP08.no, he,
          SizedEncoding.encode, Data.ofList]
      | cons b xs =>
          cases b with
          | false =>
              have hrec := ih 1 (.nil :: encode xs :: env) xs (by simp [Env.get])
              simpa [WP08.checkBits, evalValue, WP08.no, he,
                SizedEncoding.encode, Data.ofList, Data.ofBool] using hrec
          | true =>
              have hrec := ih 3 (.nil :: .nil :: (.cons .nil .nil) :: encode xs :: env)
                xs (by simp [Env.get])
              simpa [WP08.checkBits, evalValue, WP08.no, he,
                SizedEncoding.encode, Data.ofList, Data.ofBool] using hrec


/-- An encoded binary natural is nil precisely at zero. -/
theorem encode_nat_nil_iff (n : Nat) : (encode n : Data) = .nil ↔ n = 0 := by
  constructor
  · intro h
    have hzero : (encode (0 : Nat) : Data) = .nil := by decide
    have heq : (encode n : Data) = encode (0 : Nat) := by simpa only [hzero] using h
    exact encode_injective heq
  · intro h
    subst n
    rfl

/-- The nonzero-index, empty-answer raw tuple is accepted iff both
canonical bitstring questions have exactly nine bits. -/
theorem identity_value_raw_good (nh nt : Data) (x y : BitStr) :
    evalValue WP08.identityDeciderProg
      [.cons (.cons nh nt) (.cons (encode x) (.cons (encode y) (.cons .nil .nil)))] =
    (if x.length = 9 ∧ y.length = 9 then encode true else encode false) := by
  let e : Env := [ .nil, .nil, encode y, .cons .nil .nil, encode x,
    .cons (encode y) (.cons .nil .nil), nh, nt, .cons nh nt,
    .cons (encode x) (.cons (encode y) (.cons .nil .nil)),
    .cons (.cons nh nt) (.cons (encode x) (.cons (encode y) (.cons .nil .nil))) ]
  have hx : evalValue (WP08.checkBits 4 9) e =
      (if x.length = 9 then encode true else encode false) :=
    checkBits_value 4 9 e x (by simp [e, Env.get])
  have hy : evalValue (WP08.checkBits 5 9) (.nil :: .nil :: encode true :: e) =
      (if y.length = 9 then encode true else encode false) :=
    checkBits_value 5 9 (.nil :: .nil :: encode true :: e) y (by simp [e, Env.get])
  change
    (match evalValue (WP08.checkBits 4 9) e with
     | .nil => encode false
     | .cons h t =>
         evalValue (WP08.checkBits 5 9)
           (h :: t :: evalValue (WP08.checkBits 4 9) e :: e)) =
      (if x.length = 9 ∧ y.length = 9 then encode true else encode false)
  rw [hx]
  by_cases hlen : x.length = 9
  · simpa [hlen, SizedEncoding.encode, Data.ofBool] using hy
  · simp [hlen, SizedEncoding.encode, Data.ofBool]

/-- A raw nil natural-index field rejects regardless of the remaining data. -/
theorem raw_zero (x y a b : Data) :
    evalValue WP08.identityDeciderProg
      [.cons .nil (.cons x (.cons y (.cons a b)))] = encode false := by
  rfl

/-- Any nonempty first answer is rejected, even with malformed other fields. -/
theorem raw_bad_first_answer (nh nt x y ah tailA b : Data) :
    evalValue WP08.identityDeciderProg
      [.cons (.cons nh nt) (.cons x (.cons y (.cons (.cons ah tailA) b)))] =
      encode false := by
  rfl

/-- Any nonempty second answer is rejected when the first is empty. -/
theorem raw_bad_second_answer (nh nt x y bh bt : Data) :
    evalValue WP08.identityDeciderProg
      [.cons (.cons nh nt) (.cons x (.cons y (.cons .nil (.cons bh bt))))] =
      encode false := by
  rfl

/-- Source parser agreement on all *typed* game questions. -/
theorem identity_value_typed (n : Nat) (x y a b : BitStr) :
    evalValue WP08.identityDeciderProg [WP08.sample n x y a b] =
      (if n ≠ 0 ∧ x.length = 9 ∧ y.length = 9 ∧ a = [] ∧ b = []
       then encode true else encode false) := by
  cases hnat : (encode n : Data) with
  | nil =>
      have hn : n = 0 := (encode_nat_nil_iff n).mp hnat
      have hv := raw_zero (encode x) (encode y) (encode a) (encode b)
      have hval : evalValue WP08.identityDeciderProg [WP08.sample n x y a b] =
          encode false := by
        simpa only [WP08.sample, encode_prod, hnat,
                  show (encode ([] : BitStr) : Data) = .nil from rfl] using hv
      simpa [hn] using hval
  | cons nh nt =>
      have hn : n ≠ 0 := by
        intro h
        exact Data.noConfusion ((encode_nat_nil_iff n).mpr h ▸ hnat)
      cases a with
      | nil =>
          cases b with
          | nil =>
              have hv := identity_value_raw_good nh nt x y
              have hval : evalValue WP08.identityDeciderProg [WP08.sample n x y [] []] =
                  (if x.length = 9 ∧ y.length = 9 then encode true else encode false) := by
                simpa only [WP08.sample, encode_prod, hnat,
                  show (encode ([] : BitStr) : Data) = .nil from rfl] using hv
              simpa [hn] using hval
          | cons bb bs =>
              have hv := raw_bad_second_answer nh nt (encode x) (encode y)
                (encode bb) (encode bs)
              have hval : evalValue WP08.identityDeciderProg
                    [WP08.sample n x y [] (bb::bs)] = encode false := by
                simpa only [WP08.sample, encode_prod, hnat,
                  show (encode ([] : BitStr) : Data) = .nil from rfl,
                  show (encode (bb::bs) : Data) = .cons (encode bb) (encode bs) from rfl] using hv
              simpa [hn] using hval
      | cons aa as =>
          have hv := raw_bad_first_answer nh nt (encode x) (encode y)
            (encode aa) (encode as) (encode b)
          have hval : evalValue WP08.identityDeciderProg
                [WP08.sample n x y (aa::as) b] = encode false := by
            simpa only [WP08.sample, encode_prod, hnat,
              show (encode (aa::as) : Data) = .cons (encode aa) (encode as) from rfl] using hv
          simpa [hn] using hval


/-- Full intended *typed* parser semantics of the actual imported MIPRE Decider. -/
theorem accepts_iff_typed_spec (n : Nat) (x y a b : BitStr) :
    WP08.identityDecider.Accepts n x y a b ↔
      n ≠ 0 ∧ x.length = 9 ∧ y.length = 9 ∧ a = [] ∧ b = [] := by
  rw [accepts_iff_evalValue, identity_value_typed]
  by_cases h : n ≠ 0 ∧ x.length = 9 ∧ y.length = 9 ∧ a = [] ∧ b = []
  · simp [h]
  · simp [h, SizedEncoding.encode, Data.ofBool]

/-- This source parser is not a total *canonical binary numeral* validator.
The one-bit noncanonical encoding [false] decodes as zero, but is nonempty. -/
def noncanonicalZeroIndex : Data := .cons .nil .nil

theorem noncanonical_zero_decodes :
    (decode noncanonicalZeroIndex : Option Nat) = some 0 := by
  decide

theorem noncanonical_zero_not_encoded :
    noncanonicalZeroIndex ≠ (encode (0 : Nat) : Data) := by
  decide

/-- This accepted raw index is not the encoder output of *any* Nat. -/
theorem noncanonical_zero_not_any_nat (n : Nat) :
    noncanonicalZeroIndex ≠ (encode n : Data) := by
  intro h
  have hd : (decode noncanonicalZeroIndex : Option Nat) = some n := by
    rw [h]
    exact SizedEncoding.decode_encode n
  rw [noncanonical_zero_decodes] at hd
  have hn : n = 0 := (Option.some.inj hd).symm
  subst n
  exact noncanonical_zero_not_encoded h

def malformedZeroIndexGame : Data :=
  .cons noncanonicalZeroIndex
    (.cons (encode WP08.zeroNine)
      (.cons (encode WP08.zeroNine) (.cons .nil .nil)))

/-- An actual source evaluation *accepts* this noncanonical numeral
with two valid nine-bit questions and empty answers. -/
theorem malformed_zero_index_is_accepted :
    ∃ t, Eval [malformedZeroIndexGame] WP08.identityDeciderProg (encode true) t := by
  obtain ⟨t, h⟩ :=
    evalValue_sound WP08.identityDeciderProg [malformedZeroIndexGame]
      WP11.identityDecider_loopfree
  have hv : evalValue WP08.identityDeciderProg [malformedZeroIndexGame] = encode true := by
    have hraw := identity_value_raw_good .nil .nil WP08.zeroNine WP08.zeroNine
    simpa [malformedZeroIndexGame, noncanonicalZeroIndex, WP08.zeroNine] using hraw
  exact ⟨t, hv ▸ h⟩

/-- The same malformed counterexample has a genuine successful
uniformly bounded run in the source-native fuel interpreter. -/
theorem malformed_zero_index_fuel_accepts :
    ∃ t, WP09.runFuel (WP11.staticCost WP08.identityDeciderProg + 1)
      [malformedZeroIndexGame] WP08.identityDeciderProg = some (encode true, t) := by
  obtain ⟨r,t,hbound,hrun⟩ := WP11.identityDecider_uniform_fuel malformedZeroIndexGame
  have heval := WP09.runFuel_sound _ _ _ _ _ hrun
  obtain ⟨u,haccepted⟩ := malformed_zero_index_is_accepted
  have hresult : r = encode true := (Eval.deterministic heval haccepted).1
  exact ⟨t, hresult ▸ hrun⟩

end PNPAbove.WP12
