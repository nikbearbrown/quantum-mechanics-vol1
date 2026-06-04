# Research Notes: Chapter 07 — The Harmonic Oscillator

**Corresponding chapter:** chapters/07-the-harmonic-oscillator.md (not yet written)
**Generated:** 2026-06-03

---

## Chapter summary (capability built)

By the end of this chapter the student can: (1) factor the harmonic-oscillator Hamiltonian into ladder operators â₊ and â₋ using the single commutator [â₋, â₊] = 1; (2) derive the complete spectrum E_n = (n + 1/2)ℏω from the non-negativity of Ĥ alone, without solving any differential equation; (3) compute expectation values ⟨x⟩, ⟨p⟩, ⟨x²⟩, ⟨p²⟩ algebraically using â₊ and â₋; (4) write down the normalized Hermite-polynomial eigenfunctions and count their nodes; (5) explain zero-point energy and why the ground state does not sit at the potential minimum; (6) build and run a simulation of the quantum harmonic oscillator showing static eigenstates, coherent-state sloshing, and two-state superposition beating at frequency ω.

**Primary source:** _lib_qmsri-03-the-harmonic-oscillator.md (the rich local draft — this chapter maps directly to that source).

---

## A. Conceptual foundations

### A1. The ladder operators and their derivation from the commutator

**Explanation.** Define:

â₊ = (1/√(2ℏmω))(−ip̂ + mωx̂)
â₋ = (1/√(2ℏmω))(+ip̂ + mωx̂)

Compute â₋â₊ by expanding the product and using [x̂, p̂] = iℏ. The cross-terms give iℏ × (p̂x̂ − x̂p̂) = −iℏ × (iℏ) = ℏ. After cleanup:

â₋â₊ = Ĥ/(ℏω) + 1/2, equivalently Ĥ = ℏω(â₋â₊ − 1/2) = ℏω(â₊â₋ + 1/2)

Subtracting the two orderings gives the single key commutator [â₋, â₊] = 1. This commutator is the entire algebraic content of the problem. All energies, all eigenstates, all expectation values follow from it.

**Common misconception.** Students sometimes write [â₋, â₊] = ±1 without tracking order, or confuse â₊â₋ and â₋â₊. The distinction matters for the Hamiltonian: Ĥ = ℏω(â₊â₋ + 1/2), where the lower operator acts first. A wrong ordering shifts all energies by ±ℏω.

**Worked example (from _lib_qmsri-03, "The trick").**
Verify [â₋, â₊] from the definition. Write out â₋â₊ − â₊â₋ explicitly:
â₋â₊ = (1/2ℏmω)(ip̂ + mωx̂)(−ip̂ + mωx̂) = (1/2ℏmω)[p̂² + m²ω²x̂² + imω(x̂p̂ − p̂x̂)]
The cross-term is imω·[x̂, p̂] = imω·iℏ = −mωℏ. So â₋â₊ = (p̂² + m²ω²x̂²)/(2ℏmω) + 1/2 = Ĥ/(ℏω) + 1/2.
Similarly â₊â₋ = Ĥ/(ℏω) − 1/2. Difference: [â₋, â₊] = 1. ✓

**Sources.**
- _lib_qmsri-03, "The trick" section (lines 28–52): complete derivation
- Griffiths, *Introduction to Quantum Mechanics*, §2.3 (canonical reference)
- Walet, N., *Quantum Mechanics* (Manchester), §7 and §9: ladder operators as formalism

### A2. Why the ladder terminates downward: zero-point energy

**Explanation.** The Hamiltonian Ĥ = p̂²/(2m) + (1/2)mω²x̂² is a sum of squares of Hermitian operators. Therefore ⟨Ĥ⟩ = ⟨p̂²⟩/(2m) + (1/2)mω²⟨x̂²⟩ ≥ 0 in any state. But â₋ reduces energy by ℏω each time it is applied. The only way to stop the descent without contradiction is if there exists a ground state |0⟩ that â₋ kills: â₋|0⟩ = 0. Acting with Ĥ = ℏω(â₊â₋ + 1/2) on this state: Ĥ|0⟩ = ℏω(â₊·0 + 1/2)|0⟩ = (1/2)ℏω|0⟩. So E₀ = ℏω/2.

The zero-point energy is not zero. A particle confined to any potential well cannot simultaneously have zero kinetic and zero potential energy; the uncertainty principle (σ_x · σ_p ≥ ℏ/2) requires a finite spread in both x and p, and hence finite kinetic energy.

**Common misconception.** The most common error is saying "zero-point energy comes from ΔE·Δt ≥ ℏ/2" — the time-energy uncertainty relation. That is a different inequality with a different physical content. Zero-point energy comes from the Kennard position-momentum inequality. Do not conflate them.

**Worked example.** Liquid helium does not solidify at atmospheric pressure even at T → 0 K, because zero-point kinetic energy of helium atoms (m ≈ 4 u, confined to ~3 Å spacing) exceeds the interatomic binding energy. σ_x ~ 1.5 Å → σ_p ~ ℏ/(2·1.5 Å) → KE_ZPE ~ σ_p²/(2m) ≈ 6 meV, comparable to the He–He well depth (~1 meV at the minimum). This is why helium is a quantum liquid at low temperature and requires 25 atm to solidify.

**Sources.**
- _lib_qmsri-03, "Why the ladder terminates downward" (lines 70–86): complete argument including Casimir and liquid helium examples
- Lamoreaux, S.K., PRL 78, 5 (1997): first 5%-accuracy measurement of Casimir force — direct consequence of zero-point energy

### A3. The spectrum E_n = (n + 1/2)ℏω and normalized ladder relations

**Explanation.** From [Ĥ, â₊] = ℏω â₊ (derived from [â₋, â₊] = 1): if |n⟩ has energy E_n, then â₊|n⟩ has energy E_n + ℏω. The spectrum is:

E_n = (n + 1/2)ℏω, n = 0, 1, 2, …

Equally spaced with gap ℏω. Normalized ladder actions:

â₊|n⟩ = √(n+1) |n+1⟩
â₋|n⟩ = √n |n−1⟩

The √(n+1) and √n factors are determined by requiring ⟨n+1|n+1⟩ = 1 after acting with â₊, using â₋â₊ = Ĥ/(ℏω) + 1/2.

**Common misconception.** Students often write â₊|n⟩ = |n+1⟩ without the √(n+1) prefactor. This seems harmless until you compute ⟨x²⟩ or build a coherent state, where the prefactors are essential. In the HCl vibrational spectrum, the equal spacing means only Δn = ±1 transitions are dipole-allowed (selection rule from ⟨m|x̂|n⟩ ∝ δ_{m,n±1}).

**Worked example.** Compute â₊(â₋|n⟩) = â₊(√n|n−1⟩) = √n · √n|n⟩ = n|n⟩. So â₊â₋|n⟩ = n|n⟩, confirming the number operator n̂ = â₊â₋ with eigenvalue n. Then Ĥ|n⟩ = ℏω(n̂ + 1/2)|n⟩ = (n + 1/2)ℏω|n⟩. ✓

**Sources.**
- _lib_qmsri-03, "Climbing the ladder" and "The whole spectrum" (lines 56–104): complete derivation
- Griffiths §2.3: canonical undergraduate derivation with identical notation

### A4. Hermite-polynomial eigenfunctions in position space

**Explanation.** The ground-state wave function comes from solving â₋|0⟩ = 0 in position space:

(ℏ ∂_x + mωx)ψ₀(x) = 0 → dψ₀/ψ₀ = −(mω/ℏ)x dx

Integrating and normalizing: ψ₀(x) = (mω/πℏ)^(1/4) exp(−mωx²/2ℏ)

A Gaussian, saturating σ_xσ_p = ℏ/2. Higher states follow by applying â₊ repeatedly:

ψ_n(x) = (mω/πℏ)^(1/4) · (1/√(2ⁿ n!)) · H_n(ξ) · e^(−ξ²/2)

where ξ = √(mω/ℏ)·x and H_n is the n-th Hermite polynomial:
H₀ = 1, H₁ = 2ξ, H₂ = 4ξ² − 2, H₃ = 8ξ³ − 12ξ
Recursion: H_{n+1}(ξ) = 2ξ H_n(ξ) − 2n H_{n-1}(ξ)

The n-th eigenstate has exactly n nodes (zero crossings). The ground state has none.

**Common misconception.** Students expect the probability density |ψ_n|² to peak near the classical turning points (as it does for large n). For small n, particularly n = 0, it peaks at x = 0 — the opposite of classical intuition. Only at large n does |ψ_n|² average to the classical distribution (correspondence principle). Also: about 16% of the ground-state probability density lies outside the classical turning points x = ±√(ℏ/mω) — tunneling into the forbidden region is present even in the ground state.

**Worked example.** Verify H₂ from the recursion: H₂(ξ) = 2ξ H₁(ξ) − 2·1·H₀(ξ) = 2ξ·2ξ − 2·1 = 4ξ² − 2. Nodes: 4ξ² − 2 = 0 → ξ = ±1/√2 — two nodes. ✓ Verify H₃: H₃ = 2ξ(4ξ²−2) − 4·1·2ξ = 8ξ³ − 4ξ − 8ξ = 8ξ³ − 12ξ. Three roots. ✓

**Sources.**
- _lib_qmsri-03, "What the eigenstates look like" (lines 109–143): derivation of ψ₀, ψ_n, node counting, tunneling fraction
- Griffiths §2.3–2.4
- DLMF §18 (Digital Library of Mathematical Functions): Hermite polynomials — authoritative reference for recursion and normalization

### A5. Expectation values without integrals; stationary eigenstates do not oscillate

**Explanation.** Express x̂ and p̂ in terms of ladder operators:

x̂ = √(ℏ/2mω)(â₊ + â₋)
p̂ = i√(mℏω/2)(â₊ − â₋)

Then ⟨n|x̂|n⟩ = 0 (â₊|n⟩ ∝ |n+1⟩ and â₋|n⟩ ∝ |n−1⟩, both orthogonal to |n⟩).
Similarly ⟨n|p̂|n⟩ = 0. For ⟨x̂²⟩: expand (â₊+â₋)², keep only diagonal terms â₊â₋ and â₋â₊:
⟨n|x̂²|n⟩ = (ℏ/2mω)(2n+1) → σ_x = √((2n+1)ℏ/2mω).
Similarly σ_p = √((2n+1)mℏω/2). Product: σ_xσ_p = (n+1/2)ℏ.

For n = 0: σ_xσ_p = ℏ/2 — exactly the minimum. Ground state saturates the uncertainty bound.

Crucially: energy eigenstates are stationary. |Ψ_n(x,t)|² = |ψ_n(x)|² (the time-dependent phase cancels in the modulus squared). A harmonic oscillator in an energy eigenstate does NOT slosh. The probability density is static. Oscillation emerges only in superpositions of eigenstates, where the phase factors beat at (E_{n₂}−E_{n₁})/ℏ.

**Common misconception.** This is the chapter's most important misconception to destroy: "the quantum harmonic oscillator oscillates." Energy eigenstates do not oscillate. The classical oscillation reappears in two-state superpositions and, most cleanly, in coherent states (see _lib_qmsri-03, "Eigenstates do not oscillate" section, lines 172–189). If the simulation shows a static eigenstate "sloshing," there is a bug.

**Worked example.** Two-state superposition |Ψ⟩ = (1/√2)(|0⟩ + |1⟩). Probability density:
|Ψ(x,t)|² = (1/2)(|ψ₀|² + |ψ₁|²) + Re[ψ₀ψ₁* e^{−i(E₀−E₁)t/ℏ}]
The cross-term beats at (E₁−E₀)/ℏ = ω — exactly the classical frequency. But the packet also distorts in shape (unlike a coherent state). This is the visualization that the simulation must show.

**Sources.**
- _lib_qmsri-03, "Expectation values without integrals" (lines 146–168) and "Eigenstates do not oscillate — and this is crucial to understand" (lines 171–189)
- _lib_qmsri-03, "The quantum state that sloshes cleanly" (lines 197–219): coherent states

---

## B. Domain examples and cases

**Vibrational spectroscopy.** A diatomic molecule (e.g., HCl, N₂, CO) in its equilibrium configuration vibrates like a harmonic oscillator (V'' at the minimum sets mω²). The equally spaced energy levels E_n = (n+1/2)ℏω and the Δn = ±1 selection rule produce a single sharp absorption line in the IR spectrum — a "ruler" in frequency space. N₂ has ω ≈ 4.45×10¹⁴ rad/s; E_0 = ℏω/2 ≈ 0.15 eV; the first excited vibrational state is above room temperature (kT ≈ 0.025 eV << ℏω ≈ 0.29 eV), so at 300 K essentially all molecules are in the vibrational ground state.

**Laser physics (coherent states).** Glauber (Nobel 2005) showed that ideal laser modes are in coherent states — eigenstates of â₋. The photon number distribution is Poisson with mean ⟨n⟩ = |α|². The minimum-uncertainty Gaussian wave packet riding its classical orbit without spreading. The coherent state |α⟩ with amplitude α rotates in phase space at frequency ω under Ĥ, tracing a circle of radius |α|.

**LIGO and squeezed light.** LIGO operates at the "standard quantum limit" set by the shot noise of the coherent state. To push below it, LIGO now uses squeezed states of light — minimum-uncertainty states where σ_x·σ_p = ℏ/2 but with σ_x < σ_ground at the cost of σ_p > σ_ground. This is the harmonic oscillator algebra applied to photon quadratures.

**Quantum field theory.** The QHO ladder operators are the template for creation and annihilation operators in QFT. A field mode of frequency ω is a harmonic oscillator; â₊ creates one photon (or phonon), â₋ destroys one. The vacuum is the state annihilated by all â₋ operators. The Casimir force between plates is the difference in zero-point energies of field modes with vs. without the plates — measured by Lamoreaux (1997) to ~5%.

**Zero-point energy in liquid helium.** As noted above under A2. Also: solid ³He and ⁴He, quantum crystals, He bubbles in metals — all systems where ZPE dominates thermodynamics at low T.

---

## C. Connections and dependencies

**Prerequisite chapters:**
- Ch 1 (wave function, Born rule, uncertainty principle in Kennard form)
- Ch 2–3 (TISE, Schrödinger equation as eigenvalue problem)
- Ch 4 (Dirac notation, operators, commutators — [x̂, p̂] = iℏ is the input to the ladder construction)

**Forward connections:**
- Ch 8 (free particle, wave packets): coherent states in Ch 7 are Gaussian wave packets that remain Gaussian under the oscillator potential; the spreading vs. non-spreading contrast is pedagogically valuable.
- Ch 9+ (angular momentum): the ladder operator method is reused for L̂₊, L̂₋ with [L̂₋, L̂₊] = 2ℏL̂_z (different algebra, same method).
- QFT (out of scope for Vol 1 but worth a pointer): â₊, â₋ become photon creation/annihilation; the vacuum is the HO ground state.

**Mathematical dependencies:**
- Gaussian integrals (for ψ₀ normalization)
- Hermite polynomial recursion (for ψ_n in position space)
- Fourier analysis (coherent state in energy basis is Poisson; connection to Ch 8)

---

## D. Current state of the field

**Completely settled.**
- The ladder operator derivation of the spectrum, the exact Hermite-polynomial eigenfunctions, coherent states (Glauber 1963), and squeezed states are all textbook-settled since the 1960s.
- The Casimir force measurement (Lamoreaux 1997) is settled at the 1% level after corrections for surface roughness and finite conductivity.

**Contested / open.**
- The vacuum energy catastrophe: applying harmonic-oscillator zero-point energy to all quantum field modes up to the Planck scale gives a vacuum energy density ~10¹²⁰ times the observed cosmological constant. This is the largest discrepancy between theory and observation in all of physics. It is mentioned in _lib_qmsri-03 "Still puzzling" section (line 399) and should be mentioned in the chapter as an honest open problem, not swept under the rug.

**Key references.**
- Griffiths §2.3: ladder operator method, authoritative undergraduate source
- Sakurai & Napolitano, *Modern Quantum Mechanics*, §2.3: same method, slightly more formal
- Glauber, R.J., Phys. Rev. 130, 2529 (1963); 131, 2766 (1963): original coherent state papers — Nobel Prize 2005
- Lamoreaux, S.K., PRL 78, 5 (1997): Casimir force measurement
- DLMF §18: Hermite polynomials

---

## E. Teaching considerations

**Ordering.** The algebraic (ladder) approach should come entirely before the position-space (differential equation) approach. Students who solve the differential equation first lose the motivation for the algebraic shortcut. The local source (_lib_qmsri-03) takes exactly this order — follow it.

**Key simulation exercise (from _lib_qmsri-03).** Three-panel simulation: (A) ψ_n(x) stacked at energy E_n inside parabolic V(x); (B) |ψ(x,t)|² animated; (C) phase-space ⟨x⟩(t) vs ⟨p⟩(t). Three modes: Eigenstate (static), Coherent state (sloshing), Superposition (beating). The most important visual is the contrast between a static eigenstate (panel B does not animate) and a coherent state (panel B sloshes). See simulation spec at _lib_qmsri-03 lines 234–359.

**Biggest teaching traps.**
1. "The oscillator oscillates": eigenstates are stationary. Must be demonstrated in simulation before stated algebraically.
2. Missing √(n+1) factors in â₊|n⟩: these matter for calculating ⟨x²⟩, coherent state superposition, etc.
3. Confusing HO ground state ψ₀ (Gaussian) with the free-particle Gaussian from Ch 1: they look identical but the HO Gaussian is an energy eigenstate; the free-particle Gaussian is not.
4. Hermite polynomial overflow at large n: recursion is numerically unstable above n ≈ 15 in double precision. Cap simulation at n = 15; see _lib_qmsri-03 CLAUDE.md physics rules (lines 277–314).

**Conceptual arc.** The chapter should build toward the punchline: the commutator [â₋, â₊] = 1 is the skeleton on which quantum field theory is built. One commutator, derived from [x̂, p̂] = iℏ, contains the entire spectrum of every system describable as a collection of harmonic oscillators — from vibrational modes to photons to phonons.

---

## F. Library files relevant to this chapter

- **`_lib_qmsri-03-the-harmonic-oscillator.md`** (primary and nearly complete): this is the rich chapter draft. The notes chapter (Ch 7) should be written by digesting this source as the primary document. Key sections:
  - "The trick" (lines 28–52): ladder operator derivation
  - "Climbing the ladder" (lines 55–62): commutator → energy spectrum
  - "Why the ladder terminates downward" (lines 70–86): zero-point energy
  - "The whole spectrum" (lines 90–104): E_n = (n+1/2)ℏω, normalized relations
  - "What the eigenstates look like" (lines 109–143): Hermite polynomials, node counting, 16% tunneling
  - "Expectation values without integrals" (lines 146–168): algebraic shortcut
  - "Eigenstates do not oscillate — and this is crucial" (lines 171–189): kill the misconception
  - "The quantum state that sloshes cleanly" (lines 197–219): coherent states, Glauber
  - Simulation spec (lines 234–359)
  - Exercises (lines 405–431)
- **`_lib_qmsri-01-the-wave-function.md`**: The Gaussian wave function from Ch 1 is the same shape as ψ₀; use this connection to link the two chapters.

---

## G. Gaps and flags

1. **Coherent states.** The local source (_lib_qmsri-03 lines 197–219) covers coherent states well. The Chapter 7 draft should decide how deeply to go: at minimum, define |α⟩, show it is an eigenstate of â₋, and demonstrate the sloshing in the simulation. The Poisson distribution of photon number and the connection to laser physics are important but may be marked as "optional depth" for a foundational chapter.

2. **Squeezed states.** _lib_qmsri-03 mentions squeezed states and LIGO (lines 218–219) but does not derive them. This is appropriate for Ch 7: mention as an extension, do not derive.

3. **Connection to QFT.** _lib_qmsri-03 "The ladder again, differently" (lines 224–229) is the right pointer. Keep it as a brief "where this leads" paragraph.

4. **Wigner function.** The extension prompt in _lib_qmsri-03 (lines 377–393) asks for a Wigner-function 4th panel. This is pedagogically excellent (Wigner function has negative values for non-classical states like |n≥1⟩) but is genuinely advanced. Mark as optional extension.

5. **Numerical stability of Hermite recursion.** This is flagged in the simulation physics rules (_lib_qmsri-03 lines 278–280): cap n at 15, use scaled Hermites for n > 10. This must appear in the simulation spec for Ch 7, verbatim from the source.

6. **HCl spectrum worked example.** The local source mentions HCl at line 96 but does not provide numbers. The chapter should include: ω(HCl) ≈ 5.63×10¹⁴ rad/s (fundamental), ℏω ≈ 0.37 eV, IR absorption at λ ≈ 3.4 μm — a concrete calculation to anchor the abstract spectrum.
