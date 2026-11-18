import PNPAbove.WP13

namespace PNPAbove.WP14
open MIPRE MIPRE.Cost MIPRE.CL
open Finset

/-- The first coordinate of the common seed controls all remaining eight
stages. Every stage consumes its own nonempty singleton register. -/
def tailChain : (xs : List (Fin 9)) → Bool → CLFun 𝔽₂ (Fin 9) xs.length
  | [], _ => .zero
  | i :: is, enabled =>
      .cons {i} (if enabled then RegLinear.id {i} else 0)
        (fun _ => tailChain is enabled)

/-- All eight remaining coordinate registers; no padding or dummy stages. -/
def tailCoordinates : List (Fin 9) := [1,2,3,4,5,6,7,8]

def conditionalNineCL : CLFun 𝔽₂ (Fin 9) 9 :=
  .cons {0} (RegLinear.id {0})
    (fun v => tailChain tailCoordinates (decide (v 0 = 1)))

/-- The nine factors form a partition independent of the prefix choices. -/
theorem tailChain_exactlyOn (is : List (Fin 9)) (hen : is.Nodup) (enabled : Bool) :
    (tailChain is enabled).ExactlyOn is.toFinset := by
  induction is with
  | nil => rfl
  | cons i is ih =>
      have hi : i ∉ is := (List.nodup_cons.mp hen).1
      have his : is.Nodup := (List.nodup_cons.mp hen).2
      change ({i} : Finset (Fin 9)) ⊆ (i :: is).toFinset ∧
        ∀ v, (tailChain is enabled).ExactlyOn ((i :: is).toFinset \ {i})
      constructor
      · simp
      · intro v
        have hdiff : (i :: is).toFinset \ ({i} : Finset (Fin 9)) = is.toFinset := by
          ext x
          constructor
          · intro hx
            rcases (Finset.mem_sdiff.mp hx) with ⟨hm, hne⟩
            rcases Finset.mem_insert.mp (by simpa only [List.toFinset_cons] using hm) with heq | hmem
            · exact False.elim (hne (by simpa [heq]))
            · exact hmem
          · intro hx
            apply Finset.mem_sdiff.mpr
            constructor
            · simpa only [List.toFinset_cons] using Finset.mem_insert_of_mem hx
            · simp only [Finset.mem_singleton]
              intro hxi
              exact hi (by simpa [hxi] using hx)
        simpa only [hdiff] using ih his

theorem conditionalNineCL_exactlyOn : conditionalNineCL.ExactlyOn (Finset.univ : Finset (Fin 9)) := by
  change ({0} : Finset (Fin 9)) ⊆ Finset.univ ∧
    ∀ (v : Fin 9 → 𝔽₂), (tailChain tailCoordinates (decide (v 0 = 1))).ExactlyOn (Finset.univ \ {0})
  constructor
  · exact Finset.subset_univ _
  · intro v
    have ht := tailChain_exactlyOn tailCoordinates (by decide) (decide (v 0 = 1))
    have heq : tailCoordinates.toFinset = Finset.univ \ ({0} : Finset (Fin 9)) := by decide
    simpa only [← heq] using ht

/-- Every stage has a singleton factor, including every later stage. -/
theorem conditionalNineCL_factor_nonempty (j : Nat) (hj : 1 ≤ j) (h9 : j ≤ 9)
    (u : Fin 9 → 𝔽₂) : (conditionalNineCL.factorOfPrefix (j-1) u).Nonempty := by
  interval_cases j <;>
    simp [conditionalNineCL, tailChain, tailCoordinates, Finset.Nonempty, Finset.singleton_ne_empty]


/-- The prefix selects a genuinely different *linear* map at stage two. -/
theorem second_linear_off (y : Fin 9 → 𝔽₂) :
    (conditionalNineCL.mapOfPrefix 1 (0 : Fin 9 → 𝔽₂)) y = 0 := by
  simp [conditionalNineCL, tailChain, tailCoordinates]

theorem second_linear_on (y : Fin 9 → 𝔽₂) :
    (conditionalNineCL.mapOfPrefix 1 (1 : Fin 9 → 𝔽₂)) y =
      proj ({1} : Finset (Fin 9)) y := by
  simp [conditionalNineCL, tailChain, tailCoordinates]

/-- Changing only the first prefix bit changes the actual second-stage map. -/
theorem conditional_map_distinct :
    conditionalNineCL.mapOfPrefix 1 (0 : Fin 9 → 𝔽₂) ≠
      conditionalNineCL.mapOfPrefix 1 (1 : Fin 9 → 𝔽₂) := by
  intro h
  have hv := congrArg (fun f => f (1 : Fin 9 → 𝔽₂)) h
  rw [second_linear_off, second_linear_on] at hv
  have hv1 := congrFun hv (1 : Fin 9)
  simp at hv1

/-- A precise certificate that every one of the nine stages owns a distinct
nonempty register, rather than adding eight empty padding levels. -/
theorem factor_singleton (j : Nat) (hj : 1 ≤ j) (h9 : j ≤ 9)
    (u : Fin 9 → 𝔽₂) :
    conditionalNineCL.factorOfPrefix (j-1) u =
      ({⟨j-1, by omega⟩} : Finset (Fin 9)) := by
  interval_cases j <;> simp [conditionalNineCL, tailChain, tailCoordinates]


/-! ### Finite source-native sampler query compiler. -/
/-- The literal source encoding of nine Boolean zero bits. -/
def allZero : BitStr := List.replicate 9 false

def bitmap (i : Nat) : BitStr := List.ofFn (fun j : Fin 9 => j.val = i)

def sourceZero : Data := encode allZero

def sourceBitmap (i : Nat) : Data := encode (bitmap i)

/-- A source program that copies exactly `k` raw Boolean cells and appends
`pad` literal false cells. The source itself has no high-level list primitive. -/
def copyPrefixPad : (k pad idx : Nat) → Prog
  | 0, pad, _ => .const (encode (List.replicate pad false : BitStr))
  | k+1, pad, idx =>
      .elim idx (.const (encode (List.replicate (k+1+pad) false : BitStr)))
        (.cons (.var 0) (copyPrefixPad k pad 1))

/-- Conditional marginal: first seed bit gates all later output bits. -/
def marginalCode (j idx : Nat) : Prog :=
  if j = 0 then .const sourceZero
  else
    .elim idx (.const sourceZero)
      (.elim 0 (.const sourceZero)
        (.cons (.const (encode true)) (copyPrefixPad (j-1) (9-j) 3)))

/-- Inspect the Boolean value at fixed raw bit position `k` and return
`mask` iff true, otherwise the nine-bit zero list. -/
def maskIfBit : (idx k : Nat) → Data → Prog
  | idx, 0, mask =>
      .elim idx (.const sourceZero)
        (.elim 0 (.const sourceZero) (.const mask))
  | idx, k+1, mask =>
      .elim idx (.const sourceZero) (maskIfBit 1 k mask)

/-- Stage one reads its input bit; every later stage additionally requires
its (source-encoded) first prefix bit to be true. -/
def linearCode (j idxU idxY : Nat) : Prog :=
  if j = 0 then .const sourceZero
  else if j = 1 then maskIfBit idxY 0 (sourceBitmap 0)
  else
    .elim idxU (.const sourceZero)
      (.elim 0 (.const sourceZero)
        (maskIfBit (idxY+4) (j-1) (sourceBitmap (j-1))))

/-- Literal binary numeral dispatch: source `.elim` branches over 0–9
canonical LSB-first bitlists. Invalid representations take the nil branch. -/
def numeralDispatch : (fuel idx offset : Nat) → BitStr → (Nat → Nat → Prog) → Prog
  | 0, _, _, _, _ => .nil
  | fuel+1, idx, off, pre, emit =>
      .elim idx
        (match (List.range 10).find? (fun j => Nat.bits j == pre) with
         | some j => emit j off
         | none => .nil)
        (.elim 0
          (numeralDispatch fuel 1 (off+2) (pre ++ [false]) emit)
          (numeralDispatch fuel 3 (off+4) (pre ++ [true]) emit))

/-- The five fields `(kind, player, j, u, y)` are parsed from native pairs.
`offset` tracks exact de-Bruijn index shifts introduced by numeric dispatch. -/
def kindCode (kind offset : Nat) : Prog :=
  if kind = 0 then .const (encode (9 : Nat))
  else
    .elim (1+offset) .nil
      (.elim 1 .nil
        (.elim 1 .nil
          (numeralDispatch 5 2 0 [] (fun j off =>
            if kind = 1 then marginalCode j off
            else if kind = 2 then linearCode j off (off+1)
            else if kind = 3 then .const (sourceBitmap (j-1))
            else .nil))))

/-- Full source program, *not* a proof-only semantic oracle. -/
def conditionalSamplerProg : Prog :=
  .elim 0 .nil
    (.elim 1 .nil (numeralDispatch 4 0 0 [] kindCode))

/- Canonical query execution probes, not substituted for quantified proofs. -/
#guard WP12.evalValue conditionalSamplerProg
  [encode ((3:Nat), Sampler.Query.dimension)] == encode (9:Nat)
#guard WP12.evalValue conditionalSamplerProg
  [encode ((3:Nat), Sampler.Query.marginal Player.alice 9
    ([true,true,false,true,false,true,true,false,true] : BitStr))] ==
      encode ([true,true,false,true,false,true,true,false,true] : BitStr)
#guard WP12.evalValue conditionalSamplerProg
  [encode ((3:Nat), Sampler.Query.marginal Player.alice 9
    ([false,true,true,true,true,true,true,true,true] : BitStr))] == encode allZero
#guard WP12.evalValue conditionalSamplerProg
  [encode ((3:Nat), Sampler.Query.linear Player.alice 5
    ([true,false,false,false,false,false,false,false,false] : BitStr)
    ([false,false,false,false,true,false,false,false,false] : BitStr))] ==
      sourceBitmap 4
#guard WP12.evalValue conditionalSamplerProg
  [encode ((3:Nat), Sampler.Query.factor Player.bob 7
    ([true,false,false,false,false,false,false,false,false] : BitStr))] ==
      sourceBitmap 6



/-- Executable structural scoping checker, with a separately proved
reflection lemma into the original protected `Prog.WellScoped` predicate. -/
def scopedB : Nat → Prog → Bool
  | n, .var i => decide (i < n)
  | _, .nil | _, .const _ => true
  | n, .cons a b => scopedB n a && scopedB n b
  | n, .elim i a b => decide (i < n) && scopedB n a && scopedB (n+2) b
  | n, .let_ a b => scopedB n a && scopedB (n+1) b
  | n, .loop a => decide (0 < n) && scopedB n a

theorem scopedB_sound (n : Nat) (p : Prog) : scopedB n p = true → p.WellScoped n := by
  induction p generalizing n with
  | var i => simp [scopedB, Prog.WellScoped]
  | nil => simp [scopedB, Prog.WellScoped]
  | const d => simp [scopedB, Prog.WellScoped]
  | cons a b ha hb =>
      simp only [scopedB, Bool.and_eq_true, Prog.WellScoped]
      rintro ⟨h1,h2⟩
      exact ⟨ha n h1, hb n h2⟩
  | elim i a b ha hb =>
      simp only [scopedB, Bool.and_eq_true, Prog.WellScoped, decide_eq_true_eq]
      rintro ⟨⟨hi,h1⟩,h2⟩
      exact ⟨hi, ha n h1, hb (n+2) h2⟩
  | let_ a b ha hb =>
      simp only [scopedB, Bool.and_eq_true, Prog.WellScoped]
      rintro ⟨h1,h2⟩
      exact ⟨ha n h1, hb (n+1) h2⟩
  | loop a ih =>
      simp only [scopedB, Bool.and_eq_true, Prog.WellScoped, decide_eq_true_eq]
      rintro ⟨hn,ha⟩
      exact ⟨hn, ih n ha⟩

#guard scopedB 1 conditionalSamplerProg

set_option maxRecDepth 8192 in
set_option maxRecDepth 8192 in
theorem conditionalSamplerProg_closed : conditionalSamplerProg.WellScoped 1 := by
  apply scopedB_sound
  decide

/- The native dimension query is correct for every index (including zero). -/
set_option maxRecDepth 8192 in
theorem eval_dimension (n : Nat) :
    WP12.evalValue conditionalSamplerProg [encode (n, Sampler.Query.dimension)] =
      encode (9 : Nat) := by
  have hfind : (List.range 10).find? (fun j => (Nat.bits j).isEmpty) = some 0 := by decide
  simp [conditionalSamplerProg, kindCode, numeralDispatch,
    WP12.evalValue, Sampler.Query.toTuple, SizedEncoding.encode,
    Data.ofList, hfind]

/-- Canonical numeral dispatch identities, all checked by kernel reduction. -/
@[simp] theorem find_nat_0 :
    (List.range 10).find? (fun k => Nat.bits k == ([] : BitStr)) = some 0 := by decide
@[simp] theorem find_nat_1 :
    (List.range 10).find? (fun k => Nat.bits k == ([true] : BitStr)) = some 1 := by decide
@[simp] theorem find_nat_2 :
    (List.range 10).find? (fun k => Nat.bits k == ([false, true] : BitStr)) = some 2 := by decide
@[simp] theorem find_nat_3 :
    (List.range 10).find? (fun k => Nat.bits k == ([true, true] : BitStr)) = some 3 := by decide
@[simp] theorem find_nat_4 :
    (List.range 10).find? (fun k => Nat.bits k == ([false, false, true] : BitStr)) = some 4 := by decide
@[simp] theorem find_nat_5 :
    (List.range 10).find? (fun k => Nat.bits k == ([true, false, true] : BitStr)) = some 5 := by decide
@[simp] theorem find_nat_6 :
    (List.range 10).find? (fun k => Nat.bits k == ([false, true, true] : BitStr)) = some 6 := by decide
@[simp] theorem find_nat_7 :
    (List.range 10).find? (fun k => Nat.bits k == ([true, true, true] : BitStr)) = some 7 := by decide
@[simp] theorem find_nat_8 :
    (List.range 10).find? (fun k => Nat.bits k == ([false, false, false, true] : BitStr)) = some 8 := by decide
@[simp] theorem find_nat_9 :
    (List.range 10).find? (fun k => Nat.bits k == ([true, false, false, true] : BitStr)) = some 9 := by decide

set_option maxRecDepth 8192 in
set_option maxHeartbeats 600000 in
theorem eval_factor_one (n : Nat) (w : Player) (u : BitStr) :
    WP12.evalValue conditionalSamplerProg
      [encode (n, Sampler.Query.factor w 1 u)] = sourceBitmap 0 := by
  simp [conditionalSamplerProg, kindCode, numeralDispatch,
    WP12.evalValue, Sampler.Query.toTuple, SizedEncoding.encode,
    Data.ofList, Data.ofBool]

/-- Source-level bit inspector correctness for every canonical input length;
no finite 512-case extrapolation or untrusted interpreter is used. -/
theorem maskIfBit_value (idx k : Nat) (mask : Data) (env : Env) (bs : BitStr)
    (h : env.get idx = encode bs) (hk : k < bs.length) :
    WP12.evalValue (maskIfBit idx k mask) env =
      (if bs.getD k false then mask else sourceZero) := by
  induction k generalizing bs env idx with
  | zero =>
      cases bs with
      | nil => simp at hk
      | cons b bs =>
          cases b <;>
            simp [maskIfBit, WP12.evalValue, h, SizedEncoding.encode,
              Data.ofList, Data.ofBool, List.getD]
  | succ k ih =>
      cases bs with
      | nil => simp at hk
      | cons b bs =>
          have hnew : Env.get ([encode b, encode bs] ++ env) 1 = encode bs := by rfl
          have hk' : k < bs.length := by simpa using hk
          have hr := ih 1 ([encode b, encode bs] ++ env) bs hnew hk'
          simp only [maskIfBit, WP12.evalValue, h,
            show (encode (b :: bs) : Data) = .cons (encode b) (encode bs) from rfl,
            Env.get_cons_zero, Env.get_cons_succ]
          exact hr

set_option maxRecDepth 8192 in
set_option maxHeartbeats 800000 in
theorem eval_factor_all (n : Nat) (w : Player) (j : Nat) (u : BitStr)
    (hj : 1 ≤ j) (hj9 : j ≤ 9) :
    WP12.evalValue conditionalSamplerProg
      [encode (n, Sampler.Query.factor w j u)] = sourceBitmap (j - 1) := by
  interval_cases j <;>
    simp [conditionalSamplerProg, kindCode, numeralDispatch,
      WP12.evalValue, Sampler.Query.toTuple, SizedEncoding.encode,
      Data.ofList, Data.ofBool]




/-- Nine-bit conditional-prefix output in direct bit-list form. -/
def gatedPrefix (j : Nat) (bs : BitStr) : BitStr :=
  if bs.headD false then bs.take j ++ List.replicate (9-j) false else allZero

/-- Linear result represented as one sparse nine-bit vector. -/
def gatedLinear (j : Nat) (u y : BitStr) : BitStr :=
  if (j = 1 ∨ u.headD false) ∧ y.getD (j-1) false
  then bitmap (j-1) else allZero

/-- Exact source constructor-spine recursion for arbitrarily chosen input bits. -/
theorem copyPrefixPad_value (k pad idx : Nat) (env : Env) (bs : BitStr)
    (h : env.get idx = encode bs) (hk : k ≤ bs.length) :
    WP12.evalValue (copyPrefixPad k pad idx) env =
      encode (bs.take k ++ List.replicate pad false : BitStr) := by
  induction k generalizing bs env idx with
  | zero => rfl
  | succ k ih =>
      cases bs with
      | nil => simp at hk
      | cons b bs =>
          have hnew : Env.get (encode b :: encode bs :: env) 1 = encode bs := by rfl
          have hk' : k ≤ bs.length := by simpa using hk
          have hr := ih 1 (encode b :: encode bs :: env) bs hnew hk'
          simp only [copyPrefixPad, WP12.evalValue, h,
            show (encode (b :: bs) : Data) = .cons (encode b) (encode bs) from rfl]
          simpa [SizedEncoding.encode, Data.ofList] using congrArg (Data.cons (encode b)) hr

/-- Every legal native marginal is computed by the source data manipulator. -/
theorem marginalCode_value (j idx : Nat) (env : Env) (bs : BitStr)
    (hj : 1 ≤ j) (hj9 : j ≤ 9) (hlen : bs.length = 9)
    (h : env.get idx = encode bs) :
    WP12.evalValue (marginalCode j idx) env = encode (gatedPrefix j bs) := by
  obtain ⟨k, rfl⟩ : ∃ k, j = k+1 := ⟨j-1, by omega⟩
  cases bs with
  | nil => simp at hlen
  | cons b bs =>
      cases b with
      | false =>
          simp only [marginalCode, if_neg (Nat.succ_ne_zero k), WP12.evalValue, h,
            show (encode (false :: bs) : Data) = .cons (encode false) (encode bs) from rfl]
          simp [sourceZero, gatedPrefix, allZero, WP12.evalValue,
            show (encode false : Data) = .nil from rfl]
      | true =>
          have hk' : k ≤ bs.length := by
            simp only [List.length_cons] at hlen
            omega
          have hr := copyPrefixPad_value k (9-(k+1)) 3
            ([.nil,.nil,encode true,encode bs] ++ env) bs (by rfl) hk'
          simp only [marginalCode, if_neg (Nat.succ_ne_zero k), WP12.evalValue, h,
            show (encode (true :: bs) : Data) = .cons (encode true) (encode bs) from rfl]
          change Data.cons (encode true)
            (WP12.evalValue (copyPrefixPad k (9-(k+1)) 3)
              ([.nil,.nil,encode true,encode bs] ++ env)) =
              Data.cons (encode true) (encode (bs.take k ++ List.replicate (9-(k+1)) false))
          exact congrArg (Data.cons (encode true)) hr

/-- Encoding commutes with a Boolean branch; no output bit is invented. -/
theorem encode_if {p : Prop} [Decidable p] (a b : BitStr) :
    (encode (if p then a else b) : Data) =
    (if p then (encode a : Data) else encode b) := by
  split_ifs <;> rfl

/-- Source query for every conditional linear map, at all legal stages. -/
theorem linearCode_value (j idxU idxY : Nat) (env : Env) (u y : BitStr)
    (hj : 1 ≤ j) (hj9 : j ≤ 9) (hu : u.length = 9) (hy : y.length = 9)
    (hU : env.get idxU = encode u) (hY : env.get idxY = encode y) :
    WP12.evalValue (linearCode j idxU idxY) env =
      encode (gatedLinear j u y) := by
  have hj0 : j ≠ 0 := by omega
  by_cases h1 : j = 1
  · subst j
    have hm := maskIfBit_value idxY 0 (sourceBitmap 0) env y hY (by omega)
    change WP12.evalValue (if (1:Nat) = 0 then .const sourceZero
      else maskIfBit idxY 0 (sourceBitmap 0)) env =
      encode (gatedLinear 1 u y)
    simp only [if_neg (by decide : (1:Nat) ≠ 0)]
    simpa only [gatedLinear, true_or, true_and, Nat.reduceSub,
      encode_if, sourceBitmap, sourceZero] using hm
  · cases u with
    | nil => simp at hu
    | cons b bs =>
        cases b with
        | false =>
            have hR : WP12.evalValue (linearCode j idxU idxY) env = sourceZero := by
              simp only [linearCode, if_neg hj0, if_neg h1, WP12.evalValue, hU,
                show (encode (false :: bs) : Data) = .cons .nil (encode bs) from rfl]
              simp only [Env.get_cons_zero]
            rw [hR]
            simp [gatedLinear, h1, sourceZero, allZero]
        | true =>
            have hnew : Env.get (.nil :: .nil :: encode true :: encode bs :: env)
                (idxY + 4) = encode y := by
              simpa only [Env.get_cons_succ] using hY
            have hm := maskIfBit_value (idxY+4) (j-1) (sourceBitmap (j-1))
              (.nil :: .nil :: encode true :: encode bs :: env) y hnew (by omega)
            have hR : WP12.evalValue (linearCode j idxU idxY) env =
                (if y.getD (j-1) false then sourceBitmap (j-1) else sourceZero) := by
              simp only [linearCode, if_neg hj0, if_neg h1, WP12.evalValue, hU,
                show (encode (true :: bs) : Data) = .cons (encode true) (encode bs) from rfl]
              change WP12.evalValue (maskIfBit (idxY+4) (j-1) (sourceBitmap (j-1)))
                (.nil :: .nil :: encode true :: encode bs :: env) =
                (if y.getD (j-1) false then sourceBitmap (j-1) else sourceZero)
              exact hm
            rw [hR]
            simp [gatedLinear, encode_if, sourceBitmap, sourceZero]

/- All stages, all players, all nine-bit marginal queries: exact source. -/
set_option maxRecDepth 8192 in
set_option maxHeartbeats 1000000 in
theorem eval_marginal_all (n : Nat) (w : Player) (j : Nat) (z : BitStr)
    (hj : 1 ≤ j) (hj9 : j ≤ 9) (hz : z.length = 9) :
    WP12.evalValue conditionalSamplerProg
      [encode (n, Sampler.Query.marginal w j z)] = encode (gatedPrefix j z) := by
  interval_cases j <;>
    simp [conditionalSamplerProg, kindCode, numeralDispatch,
      WP12.evalValue, Sampler.Query.toTuple, SizedEncoding.encode,
      Data.ofList, Data.ofBool]
  all_goals apply marginalCode_value _ _ _ _ (by omega) (by omega) hz (by rfl)

/- All conditional stage-linear queries, including arbitrary valid prefix inputs. -/
set_option maxRecDepth 8192 in
set_option maxHeartbeats 1000000 in
theorem eval_linear_all (n : Nat) (w : Player) (j : Nat) (u y : BitStr)
    (hj : 1 ≤ j) (hj9 : j ≤ 9) (hu : u.length = 9) (hy : y.length = 9) :
    WP12.evalValue conditionalSamplerProg
      [encode (n, Sampler.Query.linear w j u y)] = encode (gatedLinear j u y) := by
  interval_cases j <;>
    simp [conditionalSamplerProg, kindCode, numeralDispatch,
      WP12.evalValue, Sampler.Query.toTuple, SizedEncoding.encode,
      Data.ofList, Data.ofBool]
  all_goals apply linearCode_value _ _ _ _ _ _ (by omega) (by omega) hu hy (by rfl) (by rfl)

/-- Closed-form semantic marginal: coordinate zero always survives; all later
coordinates survive only when the first seed bit is one. -/
def semanticMarginal (j : Nat) (x : Fin 9 → 𝔽₂) : Fin 9 → 𝔽₂ :=
  fun i => if i.val < j ∧ (i.val = 0 ∨ x 0 = 1) then x i else 0

set_option maxRecDepth 8192 in
set_option maxHeartbeats 1000000 in
theorem conditional_marginal_formula (j : Nat) (hj : 1 ≤ j) (hj9 : j ≤ 9)
    (x : Fin 9 → 𝔽₂) :
    (conditionalNineCL.truncate j).eval x = semanticMarginal j x := by
  interval_cases j <;> by_cases h : x 0 = 1 <;>
    funext i <;> fin_cases i <;>
      simp [conditionalNineCL, tailChain, tailCoordinates, semanticMarginal,
        RegLinear.id_apply, proj_apply, Finset.mem_singleton, h, apply_ite]

set_option maxRecDepth 8192 in
set_option maxHeartbeats 1000000 in
theorem semantic_marginal_bits (j : Nat) (hj : 1 ≤ j) (hj9 : j ≤ 9)
    (x : Fin 9 → 𝔽₂) :
    toBits (semanticMarginal j x) = gatedPrefix j (toBits x) := by
  interval_cases j <;> by_cases h : x 0 = 1 <;>
    simp [toBits, semanticMarginal, gatedPrefix, allZero, h, List.ofFn_succ]

/-- Every valid conditional stage is a singleton projection; its enabling
bit is the first bit of the prefix at stages two through nine. -/
theorem linear_stage_formula (j : Nat) (hj : 1 ≤ j) (hj9 : j ≤ 9)
    (u y : Fin 9 → 𝔽₂) :
    (conditionalNineCL.mapOfPrefix (j-1) u) y =
      (if j = 1 ∨ u 0 = 1 then proj ({⟨j-1, by omega⟩} : Finset (Fin 9)) y else 0) := by
  interval_cases j <;> by_cases h : u 0 = 1 <;>
    simp [conditionalNineCL, tailChain, tailCoordinates,
      RegLinear.id_apply, proj_apply, dite_eq_ite, h, apply_ite]

set_option maxRecDepth 8192 in
set_option maxHeartbeats 1000000 in
theorem semantic_linear_bits (j : Nat) (hj : 1 ≤ j) (hj9 : j ≤ 9)
    (u y : Fin 9 → 𝔽₂) :
    toBits ((conditionalNineCL.mapOfPrefix (j-1) u) y) =
      gatedLinear j (toBits u) (toBits y) := by
  rw [linear_stage_formula j hj hj9 u y]
  interval_cases j <;> by_cases h : u 0 = 1 <;>
    simp [toBits, gatedLinear, bitmap, allZero, proj_apply,
      List.ofFn_succ, h, Finset.mem_singleton] <;>
      split_ifs <;> simp_all

/-- Every source factor bitmap equals the actual singleton coordinate factor. -/
theorem semantic_factor_bits (j : Nat) (hj : 1 ≤ j) (hj9 : j ≤ 9)
    (u : Fin 9 → 𝔽₂) :
    indicatorBits (conditionalNineCL.factorOfPrefix (j-1) u) = bitmap (j-1) := by
  rw [factor_singleton j hj hj9 u]
  simp [indicatorBits, bitmap, List.ofFn, Finset.mem_singleton, Fin.ext_iff]

/-- Executable no-loop certificate, reflected into the actual source predicate. -/
def loopFreeB : Prog → Bool
  | .var _ | .nil | .const _ => true
  | .cons a b | .elim _ a b | .let_ a b => loopFreeB a && loopFreeB b
  | .loop _ => false

theorem loopFreeB_sound (p : Prog) : loopFreeB p = true → WP11.LoopFree p := by
  induction p with
  | var i => simp [loopFreeB, WP11.LoopFree]
  | nil => simp [loopFreeB, WP11.LoopFree]
  | const d => simp [loopFreeB, WP11.LoopFree]
  | cons a b ha hb =>
      simp only [loopFreeB, Bool.and_eq_true, WP11.LoopFree]
      rintro ⟨h1,h2⟩
      exact ⟨ha h1, hb h2⟩
  | elim i a b ha hb =>
      simp only [loopFreeB, Bool.and_eq_true, WP11.LoopFree]
      rintro ⟨h1,h2⟩
      exact ⟨ha h1, hb h2⟩
  | let_ a b ha hb =>
      simp only [loopFreeB, Bool.and_eq_true, WP11.LoopFree]
      rintro ⟨h1,h2⟩
      exact ⟨ha h1, hb h2⟩
  | loop a ih => simp [loopFreeB, WP11.LoopFree]

#guard loopFreeB conditionalSamplerProg

set_option maxRecDepth 8192 in
theorem conditionalSamplerProg_loopFree : WP11.LoopFree conditionalSamplerProg := by
  apply loopFreeB_sound
  decide

/-- The source program terminates on every raw `Data` input. -/
theorem conditionalSamplerProg_halts_raw (d : Data) :
    ∃ r t, Eval [d] conditionalSamplerProg r t :=
  WP11.loopfree_terminates _ conditionalSamplerProg_loopFree [d]

/-- Converts the explicit structural source result to an actual original
`MIPRE.Cost.Eval` run; no independent replacement semantics are assumed. -/
theorem sourceRuns {d r : Data}
    (h : WP12.evalValue conditionalSamplerProg [d] = r) :
    ∃ t, conditionalSamplerProg.Runs d r t := by
  obtain ⟨t,ht⟩ := WP12.evalValue_sound conditionalSamplerProg [d]
    conditionalSamplerProg_loopFree
  exact ⟨t, h ▸ ht⟩

/-- Full-depth, genuinely conditional nine-level sampler. Every field of the
actual upstream `Sampler 9` record has a source-level proof. -/
def conditionalSampler : Sampler 9 where
  prog := conditionalSamplerProg
  closed := conditionalSamplerProg_closed
  dim := fun _ => 9
  cl := fun _ _ => conditionalNineCL
  cl_exactlyOn := fun _ _ => conditionalNineCL_exactlyOn
  runs_dimension := fun n => sourceRuns (eval_dimension n)
  runs_marginal := by
    intro n w j z hj hj9 hz
    have hval : toBits ((conditionalNineCL.truncate j).eval (ofBits 9 z)) =
        gatedPrefix j z := by
      rw [conditional_marginal_formula j hj hj9]
      rw [semantic_marginal_bits j hj hj9]
      rw [toBits_ofBits hz]
    simpa only [hval] using (sourceRuns (eval_marginal_all n w j z hj hj9 hz))
  runs_linear := by
    intro n w j u y hj hj9 hu hy
    have huLen : u.length = 9 := by
      obtain ⟨x,rfl⟩ := hu
      exact length_toBits _
    have hval : toBits ((conditionalNineCL.mapOfPrefix (j-1)
        (ofBits 9 u)) (ofBits 9 y)) = gatedLinear j u y := by
      rw [semantic_linear_bits j hj hj9]
      rw [toBits_ofBits huLen, toBits_ofBits hy]
    simpa only [hval] using
      (sourceRuns (eval_linear_all n w j u y hj hj9 huLen hy))
  runs_factor := by
    intro n w j u hj hj9 hu
    have hval : indicatorBits (conditionalNineCL.factorOfPrefix (j-1) (ofBits 9 u)) =
        bitmap (j-1) := semantic_factor_bits j hj hj9 _
    simpa only [hval, sourceBitmap] using (sourceRuns (eval_factor_all n w j u hj hj9))
  halts := fun n d => by
    obtain ⟨r,t,he⟩ := conditionalSamplerProg_halts_raw (.cons (encode n) d)
    exact ⟨r,t,he⟩
