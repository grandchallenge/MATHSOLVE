import PNPAbove.WP46Batch

namespace PNPAbove.WP47
open MIPRE MIPRE.Cost MIPRE.Cost.PolyTimeFun Polynomial
open WP46

variable {α γ : Type} [SizedEncoding α] [SizedEncoding γ]

/-- The original verifier ignores the boundary advice. Acceptance must
still be checked for the original joint input. -/
noncomputable def conditionedVerifier (W : PolyTimeFun (γ × BitStr) Bool) :
    PolyTimeFun ((BitStr × γ) × BitStr) Bool :=
  W.comp ((snd.comp fst).pair snd)

theorem conditionedVerifier_correct (W : PolyTimeFun (γ × BitStr) Bool)
    (b : BitStr) (x : γ) (w : BitStr) :
    conditionedVerifier W ((b,x),w) = W (x,w) := rfl

/-- Hardcode the boundary assignment, not a solution to the joint problem.
The native hardcode primitive charges its exact encoded size and copy cost. -/
theorem discharge_boundary (W : PolyTimeFun (γ × BitStr) Bool)
    (B : Nat) (b : BitStr) (x : γ)
    (h : LocalCheap (conditionedVerifier W) B (b,x)) :
    LocalCheap W (2^(esize b+35)*(esize b+esize x+4)*B) x := by
  obtain ⟨c,w,t,hc,hr,hv,hB⟩ := h
  rw [encode_prod] at hr
  refine ⟨hardcode c (encode b),w,t+esize b+esize x+3,
    hardcode_wellScoped hc _,hardcode_time hc hr,?_ ,?_⟩
  · exact hv
  · rw [hardcode_size,show (encode b : Data).size = esize b from rfl,
      show esize c+esize b+35 = (esize b+35)+esize c by omega,pow_add]
    calc
      2^(esize b+35)*2^(esize c)*(t+esize b+esize x+3+1)
          ≤ 2^(esize b+35)*2^(esize c)*((esize b+esize x+4)*(t+1)) := by
            apply Nat.mul_le_mul_left
            nlinarith
      _ = (2^(esize b+35)*(esize b+esize x+4))*(2^(esize c)*(t+1)) := by ring
      _ ≤ _ := Nat.mul_le_mul_left _ hB

theorem localCheap_mono (V : PolyTimeFun (γ × BitStr) Bool)
    (B C : Nat) (x : γ) (h : LocalCheap V B x) (hBC : B ≤ C) :
    LocalCheap V C x := by
  obtain ⟨c,w,t,hc,hr,hv,ht⟩ := h
  exact ⟨c,w,t,hc,hr,hv,ht.trans hBC⟩

theorem boundary_description_bound (b : BitStr) :
    2^(esize b+35) ≤ 2^36*(2^b.length)^4 := by
  calc
    2^(esize b+35) ≤ 2^(4*b.length+36) :=
      Nat.pow_le_pow_right (by decide) (by have h := esize_bitStr_le b; omega)
    _ = _ := by rw [pow_add,Nat.mul_comm 4 b.length,pow_mul]; ring

/-- Fixed decomposition and lifting programs are allowed to depend on
the chosen boundary. Only one good boundary is required on each input. -/
theorem interface_weighted_bound
    (V : PolyTimeFun (α × BitStr) Bool)
    (W : PolyTimeFun (γ × BitStr) Bool)
    (D : PolyTimeFun (BitStr × γ) (List α))
    (J : PolyTimeFun ((BitStr × γ) × List BitStr) BitStr)
    (lift : ∀ b x ws, BatchGood V (D (b,x)) ws → W (x,J ((b,x),ws)) = true) :
    ∃ q : Polynomial Nat, ∀ (B : Nat) (b : BitStr) (x : γ),
      (∀ a ∈ D (b,x), LocalCheap V B a) →
      LocalCheap W (2^(esize b+35)*(esize b+esize x+4)*
        q.eval (B+esize b+esize x+1)) x := by
  have hl : ∀ z ws, BatchGood V (D z) ws →
      conditionedVerifier W (z,J (z,ws)) = true := by
    rintro ⟨b,x⟩ ws h
    exact lift b x ws h
  obtain ⟨q,hq⟩ := decomposable_weighted_bound V (conditionedVerifier W) D J hl
  refine ⟨q,?_⟩
  intro B b x h
  have hh := discharge_boundary W _ b x (hq B (b,x) h)
  simpa only [esize_prod,Nat.add_assoc] using hh

/-- A superpolynomial joint obstruction cannot be explained solely by
logarithmically many interface bits and polynomially cheap conditioned
components, provided the uniform lifting contract holds. -/
theorem small_interface_solves
    (V : PolyTimeFun (α × BitStr) Bool)
    (W : PolyTimeFun (γ × BitStr) Bool)
    (D : PolyTimeFun (BitStr × γ) (List α))
    (J : PolyTimeFun ((BitStr × γ) × List BitStr) BitStr)
    (lift : ∀ b x ws, BatchGood V (D (b,x)) ws → W (x,J ((b,x),ws)) = true)
    (p r : Polynomial Nat)
    (h : ∀ x, WP45.HasWitness W x → ∃ b : BitStr,
      2^b.length ≤ r.eval (esize x) ∧
      ∀ a ∈ D (b,x), LocalCheap V (p.eval (esize x)) a) :
    ∃ S : PolyTimeFun γ BitStr, WP45.Solves W S := by
  obtain ⟨q,hq⟩ := interface_weighted_bound V W D J lift
  apply (WP45.weightedBound_iff_solver_native W).1
  refine ⟨C (2^36) * r^4 * (4*r+X+5) * q.comp (p+4*r+X+2),?_⟩
  intro x hx
  obtain ⟨b,hb,ha⟩ := h x hx
  let n := esize x
  have hlen : b.length ≤ r.eval n :=
    (Nat.le_of_lt b.length.lt_two_pow_self).trans hb
  have hsize : esize b ≤ 4*r.eval n+1 := by
    have hs := esize_bitStr_le b
    omega
  have hdesc := (boundary_description_bound b).trans
    (Nat.mul_le_mul_left _ (Nat.pow_le_pow_left hb 4))
  have hcopy : esize b+n+4 ≤ 4*r.eval n+n+5 := by omega
  have harg : p.eval n+esize b+n+1 ≤ p.eval n+4*r.eval n+n+2 := by omega
  have htime := polynomial_eval_mono q harg
  change LocalCheap W _ x
  apply localCheap_mono W _ _ x (hq (p.eval n) b x ha)
  simp only [Polynomial.eval_mul,Polynomial.eval_C,Polynomial.eval_pow,
    Polynomial.eval_add,Polynomial.eval_X,Polynomial.eval_ofNat,Polynomial.eval_comp]
  exact Nat.mul_le_mul (Nat.mul_le_mul hdesc hcopy) htime

/-- If the joint score exceeds the stated budget, every proposed
boundary must leave at least one component over its individual budget. -/
theorem interface_bad_component
    (V : PolyTimeFun (α × BitStr) Bool)
    (W : PolyTimeFun (γ × BitStr) Bool)
    (D : PolyTimeFun (BitStr × γ) (List α))
    (J : PolyTimeFun ((BitStr × γ) × List BitStr) BitStr)
    (lift : ∀ b x ws, BatchGood V (D (b,x)) ws → W (x,J ((b,x),ws)) = true) :
    ∃ q : Polynomial Nat, ∀ (B : Nat) (b : BitStr) (x : γ),
      ¬ LocalCheap W (2^(esize b+35)*(esize b+esize x+4)*
        q.eval (B+esize b+esize x+1)) x →
      ∃ a ∈ D (b,x), ¬ LocalCheap V B a := by
  classical
  obtain ⟨q,hq⟩ := interface_weighted_bound V W D J lift
  refine ⟨q,?_⟩
  intro B b x hn
  by_contra hh
  apply hn
  apply hq
  intro a ha
  by_contra hb
  exact hh ⟨a,ha,hb⟩

end PNPAbove.WP47
