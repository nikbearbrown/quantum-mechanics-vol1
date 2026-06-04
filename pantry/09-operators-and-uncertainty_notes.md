# Research Notes: Chapter 09 — Operators and Uncertainty

**Corresponding chapter:** chapters/09-operators-and-uncertainty.md (not yet written)
**Generated:** 2026-06-03

---

## Chapter summary (capability built)

By the end of this chapter, students can: represent a physical observable as a Hermitian operator; compute expectation values ⟨A⟩ = ⟨ψ|Â|ψ⟩ and variances σ_A² = ⟨Â²⟩ − ⟨Â⟩² for any state in their toolkit; derive [x̂, p̂] = iℏ by applying both sides to a test function; and verify the Robertson uncertainty bound σ_x σ_p ≥ ℏ/2, confirming that the Gaussian ground state saturates it.

---

## A. Conceptual foundations

### Operators as observables

A linear operator  on Hilbert space is a linear map from ℋ to itself. The physical postulate: every observable corresponds to a Hermitian (self-adjoint) operator, Â† = Â. Three consequences of Hermiticity are essential:

1. **Real eigenvalues.** If Â|a⟩ = a|a⟩, then ⟨a|Â|a⟩ = a and ⟨a|Â†|a⟩ = a* — Hermiticity forces a = a*, so measurement outcomes are real.
2. **Orthogonal eigenstates.** Eigenstates with distinct eigenvalues are orthogonal: ⟨a|a'⟩ = 0 for a ≠ a'.
3. **Spectral theorem / completeness.** The eigenstates form a complete orthonormal basis: Â = Σ_n a_n |a_n⟩⟨a_n|.

Source: _lib_qmsri-04, §"Operators and Hermiticity."

### The momentum operator and its Hermiticity

In the position representation, p̂ = −iℏ ∂_x. The factor of −i is not a convention — it is what makes the operator Hermitian. Without it, ∂_x would be anti-Hermitian and its eigenvalues imaginary (unphysical). Proof via integration by parts:

  ⟨φ|p̂ψ⟩ = ∫ φ*(x)(−iℏ ∂_x ψ) dx

Integrate by parts (boundary term vanishes for normalizable ψ):

  = ∫ (iℏ ∂_x φ*) ψ dx = ∫ (−iℏ ∂_x φ)* ψ dx = ⟨p̂φ|ψ⟩.

Hermitian confirmed. This step requires ψ, φ → 0 at x → ±∞, which holds for any physically normalizable state.

Source: _lib_qmsri-04, §"Operators and Hermiticity"; _lib_qmsri-01, §"What do you actually measure?"

### Expectation values

The expectation value of observable Â in state |ψ⟩:

  ⟨Â⟩ = ⟨ψ|Â|ψ⟩

In position representation:

  ⟨x̂⟩ = ∫ x |ψ(x)|² dx
  ⟨p̂⟩ = ∫ ψ*(x)(−iℏ ∂_x) ψ(x) dx

The sign in p̂ is critical: a wave packet moving right (positive k₀) must yield ⟨p̂⟩ > 0.

Source: _lib_qmsri-01, §"What do you actually measure?"; _lib_qmsri-04, §"The abstract state."

### Canonical commutation relation

The commutator [x̂, p̂] = x̂p̂ − p̂x̂. Apply to a test function ψ(x):

  [x̂, p̂]ψ = x(−iℏ ∂_x ψ) − (−iℏ ∂_x)(xψ)
            = −iℏ x ∂_x ψ + iℏ (ψ + x ∂_x ψ)
            = iℏ ψ

So [x̂, p̂] = iℏ. This is the algebraic statement that distinguishes QM from classical mechanics. Two operators commute iff they share a common eigenbasis — so position and momentum have no common eigenbasis. No state can simultaneously be an eigenstate of both.

Source: _lib_qmsri-04, §"Commutators and why they matter."

### Generalized uncertainty principle (Robertson 1929)

For any two Hermitian operators Â, B̂ and any state |ψ⟩:

  σ_A σ_B ≥ ½ |⟨[Â, B̂]⟩|

where σ_A = √(⟨Â²⟩ − ⟨Â⟩²). Derivation sketch (from _lib_qmsri-04):

1. Define shifted operators Â' = Â − ⟨Â⟩, B̂' = B̂ − ⟨B̂⟩.
2. σ_A² = ‖Â'|ψ⟩‖², σ_B² = ‖B̂'|ψ⟩‖².
3. Cauchy-Schwarz: σ_A² σ_B² ≥ |⟨Â'B̂'⟩|².
4. Decompose Â'B̂' = ½{Â',B̂'} + ½[Â',B̂']. The symmetric part contributes ¼⟨{Â',B̂'}⟩² (real, non-negative). The antisymmetric part contributes ¼|⟨[Â,B̂]⟩|² (from the purely imaginary commutator expectation value).
5. Drop the anticommutator term → Robertson bound.

For x̂, p̂: [x̂, p̂] = iℏ → ⟨[x̂,p̂]⟩ = iℏ → σ_x σ_p ≥ ℏ/2. This is the Kennard inequality (1927), independently proved.

**Critical pedagogical point:** the Robertson bound is a property of the *state*, not the measurement apparatus. Prepare 10⁶ copies of |ψ⟩; measure x̂ on half, p̂ on half; compute sample standard deviations. Their product satisfies the bound. No copy is measured twice. The bound is set before any measurement takes place. This is the Kennard interpretation, distinct from Heisenberg's original 1927 microscope story (measurement disturbance).

Sources: _lib_qmsri-04, §"Commutators and why they matter"; _lib_qmsri-01, §"The uncertainty principle, properly."

### The Gaussian saturates the bound

Ground-state Gaussian: ψ(x) = (πa²)^{−1/4} exp(−x²/2a²) exp(ik₀x).

- σ_x = a/√2 (direct computation of ⟨x²⟩ − ⟨x⟩² via Gaussian integrals).
- σ_p = ℏ/(a√2) (via p̂ = −iℏ ∂_x applied to the Gaussian, plus the Fourier route: the Fourier transform of a Gaussian is a Gaussian with width 1/a).
- Product: σ_x σ_p = (a/√2)(ℏ/a√2) = ℏ/2. Exactly at the bound.

The minimum-uncertainty state (MUS) / coherent state of the harmonic oscillator achieves this equality because the optimality condition for Robertson — that Â'|ψ⟩ = iλB̂'|ψ⟩ for real λ — is precisely satisfied by a Gaussian (this condition follows from the case of equality in Cauchy-Schwarz).

Source: _lib_qmsri-01, §"The Gaussian saturates the bound."

---

## B. Domain examples and cases

### Worked example: σ_x σ_p for the infinite-square-well ground state

State: ψ₁(x) = √(2/L) sin(πx/L), x ∈ [0, L].

⟨x⟩ = L/2 (by symmetry).
⟨x²⟩ = L²(1/3 − 1/(2π²)).  →  σ_x = L √(1/12 − 1/(2π²)) ≈ 0.181 L.
⟨p⟩ = 0 (standing wave: equal left- and right-moving amplitudes; verified by computing ∫ψ*(-iℏ∂_x)ψ dx which integrates an odd function to zero).
⟨p²⟩ = (πℏ/L)², since p̂²ψ₁ = (πℏ/L)²ψ₁ is the eigenvalue equation.  →  σ_p = πℏ/L.

Product: σ_x σ_p ≈ 0.181 L · πℏ/L ≈ 0.568 ℏ > ℏ/2. The bound is satisfied but not saturated — confirming that only the Gaussian achieves equality.

This is the key worked example for Ch 9. The simulation check: compute σ_x, σ_p numerically for the infinite-well state via the probability-explorer from Ch 1 (or equivalently via the Ch 11 sandbox) and verify the ratio σ_x σ_p/(ℏ/2) ≈ 1.136.

### The qubit version (forward reference to Ch 10)

For spin-½, the Robertson bound for σ_x and σ_z says σ_{σx} σ_{σz} ≥ |⟨σ_y⟩|. This is saturated at the σ_y eigenstate, where σ_{σx} = σ_{σz} = 1 and ⟨σ_y⟩ = 1. The bound is state-dependent, not a fixed number.

Source: _lib_qmsri-04, §"Commutators and why they matter," Table.

### Schrödinger uncertainty relation (tighter bound, optional)

Retaining the anticommutator term gives:
  σ_A² σ_B² ≥ ¼|⟨{Â',B̂'}⟩|² + ¼|⟨[Â,B̂]⟩|²

This is the Schrödinger (1930) relation, tighter than Robertson. The extra anticommutator term is non-negative and vanishes when the state minimizes Robertson. The distinction is pedagogically useful for Challenge exercises.

Source: _lib_qmsri-04, Exercise 4.10.

---

## C. Connections and dependencies

- **Ch 1 (Wave Function):** ⟨x⟩, ⟨p⟩, σ_x, σ_p already computed numerically for Gaussian states. Ch 9 gives the algebraic framework (operators, commutators) that explains why those computations work and proves the bound.
- **Ch 4 (Dirac Notation / Formalism):** The abstract framework in _lib_qmsri-04 is the direct source for Ch 9. The chapter is essentially a worked application of the formalism to x̂ and p̂.
- **Ch 10 (Qubit):** The Robertson bound for Pauli operators is the finite-dimensional parallel. Students should compute both the continuous (x,p) and discrete (σ_i, σ_j) cases.
- **Ch 11 (Sandbox):** The sandbox numerically verifies σ_x σ_p for any potential's eigenstates. Ch 9's worked example is the first test case.
- **Later (Angular Momentum):** L̂_x, L̂_y, L̂_z satisfy [L̂_x, L̂_y] = iℏL̂_z, so σ_{Lx} σ_{Ly} ≥ ½ℏ|⟨L̂_z⟩|. Same Robertson structure.
- **Harmonic oscillator (Ch 6–8 range):** Ladder operators â, â† satisfy [â, â†] = 1. The coherent states are minimum-uncertainty states of x̂ and p̂.

---

## D. Current state of the field

The Robertson (1929) and Kennard (1927) bounds are mathematically settled. The ongoing research frontier involves:

1. **Measurement-disturbance inequalities.** Heisenberg's original 1927 intuition about measurement kicking the system is formalized differently — as an error-disturbance relation. Ozawa's 2003 inequality (M. Ozawa, *Phys. Rev. A* 67, 042105) gives a different bound. Erhart et al. 2012 (*Nature Phys.* 8, 185) and Rozema et al. 2012 (*Phys. Rev. Lett.* 109, 100404) tested it experimentally. These are *different* from Robertson and should not be conflated. The chapter should name the distinction once.
2. **Entropic uncertainty relations.** Maassen-Uffink (1988, *Phys. Rev. Lett.* 60, 1103) gives uncertainty bounds in terms of Shannon entropy rather than variance: H(x) + H(p) ≥ log(eπℏ). These are tighter for non-Gaussian states. Graduate-level content; mention briefly in G. Gaps.
3. **Robertson bound tightness.** The bound is achieved only by Gaussian states (for x, p) or by eigenstates of the "right" combination (for finite-dimensional systems). This is well-established.

---

## E. Teaching considerations

### Common misconceptions to address

1. **"The uncertainty principle is about measurement disturbance."** No. The Kennard/Robertson bound is about the shape of the *prepared state*, established across an ensemble of independently prepared copies. Address once, definitively.
2. **"Hermitian means real matrix / symmetric matrix."** False for complex operators. σ_y is the canonical failure case: its transpose is −σ_y (antisymmetric), but its conjugate transpose is σ_y (Hermitian). Any code should include a runtime check Â† == Â.
3. **"⟨p⟩ = 0 means no momentum."** The standing wave ground state has ⟨p⟩ = 0 but σ_p = πℏ/L. Students confuse the mean with the spread.
4. **Commutator direction of the product rule.** Students frequently drop the product rule term when computing [x̂, p̂]ψ. The derivation must be done with a test function, step-by-step.

### Simulation anchor

The Ch 1 simulation (`01-probability-explorer.html`) already displays σ_x, σ_p, and the ratio σ_x σ_p/(ℏ/2). Ch 9 instructs students to re-open it and read off these values for the infinite-well n=1 state, then compute them analytically and compare. This grounds the abstract algebra in a simulation they have already used.

If time allows: a Ch 9-specific simulation showing the Robertson bound for the qubit (from `04-bloch-sphere.html`) in measurement-statistics mode — measuring σ_x and σ_z on N copies and comparing the product to |⟨σ_y⟩|.

### Derivation sequencing

Recommended order:
1. Show p̂ = −iℏ∂_x is Hermitian (integration by parts).
2. Derive [x̂, p̂] = iℏ (test function, product rule, all steps visible).
3. State Robertson; sketch derivation (Cauchy-Schwarz → anticommutator + commutator → drop anticommutator).
4. Plug in x̂, p̂ → σ_x σ_p ≥ ℏ/2.
5. Verify for the Gaussian (saturates) and the infinite-well ground state (exceeds).

---

## F. Library files relevant to this chapter

- **Primary:** `/pantry/_lib_qmsri-04-formalism-dirac-notation-and-operators.md` — §"Operators and Hermiticity," §"Commutators and why they matter," §"The qubit" (Robertson for σ_x, σ_z). This is the main source; the chapter drafts from it directly.
- **Supporting:** `/pantry/_lib_qmsri-01-the-wave-function.md` — §"The uncertainty principle, properly," §"The Gaussian saturates the bound," §"What do you actually measure?" These provide the wave-function-level derivations and the ensemble-protocol framing.
- **Optional:** `/books/physics-quantum-mechanics-sri/pantry/qm.md` — §1.6 "The generalized uncertainty principle" (Feiguin notes, Townsend Ch 3). Confirms the operator-algebraic derivation from a second source. Primary reference cited there: Townsend, *A Modern Approach to Quantum Mechanics*, 2nd ed., §3.5.

---

## G. Gaps and flags

1. **Sign convention on p̂.** The chapter must commit to p̂ = −iℏ ∂_x (not +iℏ ∂_x). The simulation (Ch 1) already uses this; confirm the sign matches throughout.
2. **Boundary conditions and Hermiticity.** The integration-by-parts proof requires ψ → 0 at ±∞. For the infinite square well, the boundary conditions at the walls serve the same role. Ch 9 should state this explicitly — it is a different, box-specific version of the same boundary-term argument.
3. **Degeneracy.** When eigenvalues coincide, eigenstates are not automatically orthogonal — Gram-Schmidt must be applied. Ch 9 should mention this in passing (Exercise 4.9 in _lib_qmsri-04 covers it explicitly).
4. **Entropic uncertainty relations.** The Maassen-Uffink bound is tighter than Robertson for non-Gaussian states and is the form used in quantum information. Flag as an advanced extension, not main chapter content.
5. **Ozawa / Erhart distinction.** One sentence or footnote in the chapter: "Robertson is about preparation, not measurement disturbance. For the latter, see Ozawa (2003) and Erhart et al. (2012)."
6. **The Schrödinger (tighter) uncertainty relation.** Explicitly covered in _lib_qmsri-04, Ex 4.10. Include in a Challenge exercise; mark as optional for the main narrative.
