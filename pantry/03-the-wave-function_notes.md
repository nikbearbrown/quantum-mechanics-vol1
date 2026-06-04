# Research Notes: Chapter 03 — The Wave Function

**Corresponding chapter:** chapters/03-the-wave-function.md (not yet written)
**Generated:** 2026-06-03

---

## Chapter summary (capability built)

By the end of this chapter the student can: (1) state Born's rule precisely, distinguishing a probability *density* from a probability; (2) normalize a given wave function by computing the normalization constant; (3) compute the probability of finding a particle in an interval [a, b] via integration of |ψ|²; (4) evaluate expectation values ⟨x⟩ and ⟨p⟩; (5) explain why ψ must be complex and what the imaginary part carries; (6) recognize the probability current and the continuity equation as the structural reason normalization is preserved.

The simulation deliverable (`01-probability-explorer.html`) makes ⟨x⟩, ⟨p⟩, σ_x, σ_p, and the uncertainty-principle ratio live and interactive across a gallery of wave functions.

---

## A. Conceptual foundations

### A1. |ψ|² is a probability *density*, not a probability

**Explanation.** The Born rule states that P(particle in [a,b]) = ∫_a^b |ψ(x,t)|² dx. The integrand |ψ(x,t)|² has units of (length)⁻¹ — it is a density, just as a population map gives people per km², not a headcount at a point. Reading a probability from the *value* of |ψ|² at a single point is a unit error.

**Common misconception.** Students often say "the particle is at the peak of |ψ|²." The peak gives the most probable *region* per unit length; the actual probability of finding the particle in a region requires integration. Relatedly, because |ψ|² is a density it can exceed 1 — this alarms students until the units argument is made explicit.

**Worked example.** Let ψ(x) = A e^{−|x|/a} for real a > 0.
- Normalization: ∫_{−∞}^{∞} |ψ|² dx = 2A² ∫_0^{∞} e^{−2x/a} dx = 2A² · (a/2) = A²a = 1, so A = 1/√a.
- P(particle in [−a, a]) = ∫_{−a}^{a} (1/a) e^{−2|x|/a} dx = 2∫_0^a (1/a) e^{−2x/a} dx = 1 − e^{−2} ≈ 0.865.
- Peak value |ψ(0)|² = 1/a. For a = 0.5 nm, this is 2 nm⁻¹ — greater than 1, valid because it is per nm, not dimensionless.

**Sources.** Born (1926), Z. Phys. 38:803 (the original paper, with the famous footnote changing ψ to |ψ|²; Born received the Nobel in 1954 for this). Griffiths, *Introduction to Quantum Mechanics*, 3rd ed. (2018), §1.1–1.3. Lib file: _lib_qmsri-01, §"What are we even looking at?" and §"Normalization, and a calculation worth doing in full."

---

### A2. ψ is forced to be complex — the imaginary part is physics, not convention

**Explanation.** The TDSE reads iℏ ∂ψ/∂t = Ĥψ. If ψ were real, ∂ψ/∂t would be real, but iℏ times something real is purely imaginary — the equation cannot balance. Therefore the dynamics themselves force ψ into the complex plane. The imaginary part is not a mathematical convenience; it carries phase information (momentum, interference, direction of travel). The orange Re ψ and gray Im ψ panels in the simulation both have to be non-trivial for any moving wave packet; Im ψ ≡ 0 is a bug flag.

**Common misconception.** "We use complex numbers for convenience; the physics is all in Re ψ." False — discarding Im ψ destroys the physics. A wave packet with k₀ > 0 has Re ψ and Im ψ 90° out of phase; setting Im ψ = 0 at any moment immediately gives wrong dynamics on the next time step.

**Worked example.** Take ψ(x) = A e^{−x²/(2a²)} e^{ik₀x}.
- Re ψ = A e^{−x²/(2a²)} cos(k₀x) — oscillates, positive and negative.
- Im ψ = A e^{−x²/(2a²)} sin(k₀x) — also oscillates, 90° shifted.
- |ψ|² = A² e^{−x²/a²} — a smooth Gaussian, no oscillation.
The oscillation of Re ψ and Im ψ encodes the momentum k₀; |ψ|² hides it.

**Sources.** Lib file: _lib_qmsri-01, §"Why is ψ complex at all?" Feynman, Leighton & Sands, *Feynman Lectures on Physics*, Vol. III, §1-1 (the fundamental mystery framing). Ballentine, *Quantum Mechanics: A Modern Development* (2014), §3.1.

---

### A3. Normalization is preserved by the Schrödinger equation (the continuity equation)

**Explanation.** If ψ is normalized at t = 0, does it stay normalized? Yes — and the proof reveals the probability current J = (ℏ/m) Im(ψ* ∂ψ/∂x). The continuity equation ∂|ψ|²/∂t + ∂J/∂x = 0 governs the flow of probability density exactly as mass conservation governs fluid flow. Integrating over all x and using ψ → 0 at ±∞ gives d/dt ∫|ψ|² dx = 0.

**Common misconception.** "Normalization must be re-imposed at each time step." For an exact analytic solution or a unitary numerical scheme (e.g., Crank-Nicolson), normalization is automatic. It fails only when a non-unitary integrator (explicit Euler) is used or when probability leaks at grid boundaries. The normalization indicator in the simulation is a diagnostic for these bugs, not a correction step.

**Worked example.** For a real ψ, J = (ℏ/m) Im(ψ ∂ψ/∂x) = 0, because ψ ∂ψ/∂x is purely real. Therefore a real ψ has zero probability current everywhere — it cannot represent a particle with net momentum in one direction. A moving wave packet must be complex.

**Sources.** Lib file: _lib_qmsri-01, §"Normalization, and a calculation worth doing in full." Griffiths (2018), §1.4. Sakurai & Napolitano, *Modern Quantum Mechanics*, 3rd ed. (2021), §1.6.

---

### A4. Expectation values — ⟨x⟩ and ⟨p⟩

**Explanation.** ⟨x⟩ = ∫ x |ψ|² dx is the centroid of the probability distribution. ⟨p⟩ = ∫ ψ* (−iℏ ∂/∂x) ψ dx — a derivative operator in position space — follows from the Fourier transform relationship: in momentum space, ⟨p⟩ = ∫ p |φ(p)|² dp; translating to position space via Parseval's theorem turns multiplication by p into differentiation by x. The sign matters: p̂ = −iℏ ∂/∂x; for k₀ > 0, ⟨p⟩ = ℏk₀ > 0.

**Common misconception.** Students attempt ⟨p⟩ = ∫ p |ψ(x)|² dx — a formula that only works in momentum space and is meaningless in position space (there is no "p" as a function of x in the integrand). The operator sandwiching ψ* (p̂) ψ is not optional.

**Worked example.** For the Gaussian ψ = (πa²)^{−1/4} e^{−x²/(2a²)} e^{ik₀x}:
- ⟨x⟩ = 0 (symmetric).
- ⟨p⟩ = ℏk₀ (the x/a² term is odd and integrates to zero).
- ⟨p²⟩ = ℏ²(1/(2a²) + k₀²) → σ_p = ℏ/(√2 a).
- ⟨x²⟩ = a²/2 → σ_x = a/√2.
- σ_x σ_p = (a/√2)(ℏ/(√2 a)) = ℏ/2. The Gaussian saturates the uncertainty bound.

**Sources.** Lib file: _lib_qmsri-01, §"What do you actually measure?" and §"The Gaussian saturates the bound." Griffiths (2018), §1.5–1.6.

---

### A5. The Kennard (uncertainty) inequality — preparation, not disturbance

**Explanation.** The inequality σ_x σ_p ≥ ℏ/2 is a statement about the *shape of ψ*, not about measurement disturbing the particle. Prepare N copies of state ψ; measure position on N/2 of them, momentum on the other N/2. No single particle is measured twice. The product of the resulting standard deviations cannot be less than ℏ/2. The reason is Fourier analysis: a function narrow in x must be broad in its Fourier transform (p-space), and vice versa.

**Common misconception.** "The uncertainty principle says measuring position disturbs momentum." This confuses the Kennard inequality (about preparation) with the Heisenberg measurement-disturbance relation (about back-action). Ozawa (2003) showed the measurement-disturbance relation has a *different* form and a different (tighter) bound than ℏ/2. Erhart et al. (2012) and Rozema et al. (2012) tested the Ozawa form experimentally.

**Worked example.** The infinite-well ground state has σ_x = L√(1/12 − 1/(2π²)) ≈ 0.181 L and σ_p = πℏ/L, giving σ_x σ_p ≈ 0.568 ℏ ≥ ℏ/2. The ratio σ_x σ_p /(ℏ/2) ≈ 1.136 — the simulation's live readout confirms this. The Gaussian alone gives exactly 1.000.

**Sources.** Kennard (1927), Z. Phys. 44:326. Ozawa, M. (2003), Phys. Rev. A 67, 042105. Erhart et al. (2012), Nature Physics 8, 185. Rozema et al. (2012), Phys. Rev. Lett. 109, 100404. Lib file: _lib_qmsri-01, §"The uncertainty principle, properly."

---

## B. Domain examples and cases

**B1. Gaussian wave packet** — the canonical example of a minimum-uncertainty state (σ_x σ_p = ℏ/2). Sliders: width a, central momentum k₀. Free evolution: σ_x grows as √(1 + (ℏt/(2mσ_x(0)))²) · σ_x(0); σ_p stays constant; the uncertainty ratio exceeds 1.000 for t > 0.

**B2. Infinite-well eigenstates** — real-valued ψ_n(x) = √(2/L) sin(nπx/L). Probability current J = 0 everywhere (ψ is real); ⟨p⟩ = 0 (standing wave — equal superposition of ±p). Uncertainty ratio ≈ 1.136 for n = 1; grows with n. The simulation confirms: for the standing wave the momentum expectation is zero despite the particle having energy.

**B3. Double Gaussian** — ψ ∝ e^{−(x−d)²/(2σ²)} + e^{−(x+d)²/(2σ²)}. ⟨x⟩ = 0 by symmetry even though |ψ|² peaks at x = ±d. Illustrates that ⟨x⟩ can be in a region of *low* probability density — a useful antidote to naive use of the expectation value as a "most likely position."

**B4. Square pulse** — discontinuous ψ has a Fourier transform decaying as 1/p, so ∫ p² |φ(p)|² dp diverges: σ_p = ∞, uncertainty ratio undefined. A real discontinuity in ψ (not a numerical artifact) must cause σ_p to diverge. The simulation should label this "undefined," not display a large finite number.

**B5. Dimensional analysis checkpoint** — for a = 0.5 nm, |ψ(0)|² = 1/a = 2 nm⁻¹ > 1. Valid because it is per nm. Students who expect |ψ|² ≤ 1 are conflating a density with a probability.

---

## C. Connections and dependencies

**Prerequisites:**
- Chapter 0 (simulation intro): the student has already seen the blue |ψ|² blob and the orange Re ψ curve, and dragged the spread slider. This chapter names what they saw.
- Calculus: integration by substitution; integration by parts (needed for the normalization proof and for ⟨p⟩).
- Complex numbers: modulus, argument, Euler's formula e^{iθ} = cos θ + i sin θ.

**Unlocks:**
- Chapter 4: the stationary-state phase e^{−iEt/ℏ} is only meaningful once ψ is understood as complex.
- Chapter 5: the superposition |Ψ(t)|² = ½[|ψ₁|² + |ψ₂|² + 2ψ₁ψ₂cos(ωt)] requires the student to know how to evaluate |ψ|² for a sum.
- Chapter 6 (harmonic oscillator): coherent states; the Gaussian minimum-uncertainty state appears again as the ground-state displaced by ladder operators.

**Adjacent chapters:**
- Ch 3 (this book's numbering) maps to _lib_qmsri-01 (the sibling's Ch 1).
- The probability current connects forward to scattering (tunneling) in later chapters.

---

## D. Current state of the field

**Settled.**
- Born's rule as a postulate: universally accepted for all practical purposes. Every precision test of quantum mechanics (QED, atomic clocks, quantum optics, condensed matter) rests on it implicitly.
- The Kennard inequality: proven rigorously (Robertson generalization to arbitrary observables: Robertson 1929, Phys. Rev. 34:163).

**Contested / open.**
- *Derivation* of Born's rule from more primitive axioms: Zurek's "envariance" approach (Zurek 2003, Rev. Mod. Phys. 75:715) and many-worlds branch-counting (Deutsch 1999; Wallace 2012) claim derivations but remain debated. The lib file explicitly flags this as unsettled and declines to take a position — the chapter should do the same.
- Ozawa vs. Heisenberg measurement-disturbance: active experimental and theoretical literature (2012–present). The correct formulation is not the naive Heisenberg-microscope story.

**Key references.**
- Born, M. (1926). Z. Phys. 38, 803.
- Kennard, E. H. (1927). Z. Phys. 44, 326.
- Robertson, H. P. (1929). Phys. Rev. 34, 163.
- Ozawa, M. (2003). Phys. Rev. A 67, 042105.
- Griffiths, D. J. & Schroeter, D. F. (2018). *Introduction to Quantum Mechanics* (3rd ed.). Cambridge. [Ch. 1]
- Ballentine, L. E. (2014). *Quantum Mechanics: A Modern Development* (2nd ed.). World Scientific. [§3.1]

---

## E. Teaching considerations

**Simulation-first sequencing.** The student has already watched the blue blob in Ch 0 before reading this chapter. The chapter's opening gambit — "now I will tell you what it is" — works precisely because curiosity was seeded earlier. Do not front-load definitions before the puzzle.

**The normalization proof as a two-for-one.** The proof that ∫|ψ|² dx is constant produces the probability current J as a free byproduct. This should be presented as a surprise gift, not a detour. The CLAUDE.md snippet for the simulation explicitly uses the normalization indicator as a bug detector — teach it as such.

**The sign of p̂.** σ_x σ_p /(ℏ/2) = 0.500 for a Gaussian is the canonical LLM failure mode: dividing by ℏ instead of ℏ/2. The sign of p̂ = −iℏ ∂/∂x is another common error: ⟨p⟩ < 0 for k₀ > 0 is the red flag. Both need to be pre-empted in CLAUDE.md.

**Density vs. probability — the population analogy.** Population per km² vs. total city population is the most effective non-physics analogy found in the lib file (Figure 1.1). Lead with it.

**Misconception ordering.** Address in this order: (1) |ψ|² is a density not a probability; (2) ψ is not the particle; (3) ψ must be complex; (4) the uncertainty principle is about preparation not disturbance. Each misconception is harder to unlearn if encountered before the preceding one is cleared.

**Common student confusions to anticipate:**
- Normalizing |ψ|² instead of ψ (computing ∫|ψ|⁴ dx = 1 by mistake).
- Forgetting the |·| in |ψ|² when ψ is complex (computing ψ² instead of ψ*ψ).
- Applying the position-space Born rule in momentum space, or vice versa.
- Believing ⟨x⟩ is the most probable position (it is the *average* position).

---

## F. Library files relevant to this chapter

- **Primary:** `/pantry/_lib_qmsri-01-the-wave-function.md` — the full drafted chapter text. Contains: Born rule derivation, complexity argument, normalization proof with probability current, ⟨x⟩ and ⟨p⟩ calculation, uncertainty principle discussion, Gaussian minimum-uncertainty calculation, full LLM exercise prompt, exercises (warm-up through challenge).
- **Secondary:** `/pantry/_lib_qmsri-02-the-time-independent-schrodinger-equation.md` — the ground-state uncertainty calculation (σ_x σ_p ≈ 0.568 ℏ for n = 1) provides a concrete non-Gaussian example for the uncertainty ratio live readout.
- **Optional:** `/pantry/_lib_quantum-physics-for-beginners.md` — not yet examined; may contain alternative framings for introductory students.

---

## G. Gaps and flags

1. **Born rule derivation status.** The lib file explicitly declines to take a position on whether Born's rule can be derived (Zurek, many-worlds). The chapter should preserve this intellectual honesty, but needs a one-sentence policy statement so the chapter author does not feel compelled to resolve it.

2. **Multi-particle ψ.** The lib file notes that J has a beautiful interpretation for a single particle in 1D, and that the many-particle generalization "holds but the geometric intuition is harder" — but does not show it. Flag for later volumes; this chapter should confine itself to single-particle, 1D.

3. **Square-pulse σ_p divergence.** The lib file calls labeling σ_p "undefined" for a discontinuous ψ "honest but not the most pedagogically satisfying move." Consider a brief explanatory sentence: "the Fourier transform of a square pulse decays as 1/p, making ∫ p²|φ|² dp diverge — this is a real mathematical fact, not a numerical artifact."

4. **Momentum operator sign derivation.** The lib file gives the Fourier-transform motivation for p̂ = −iℏ ∂/∂x but does not derive it from first principles. For undergraduates this is fine, but a footnote pointing to the de Broglie relation or the Fourier-transform route would be useful.

5. **No exercises cross-reference to simulation outputs.** Several exercises (e.g., Ex. 9, ranking uncertainty ratios) explicitly invite use of the simulation. Ensure the simulation is available before the exercises are assigned — the simulation is the *primary* computational tool for this chapter.

6. **Boundary between Ch 3 and Ch 4.** The last paragraph of the lib file ("Chapter 2: you now know what ψ means…") bridges to the TISE. Make sure the chapter 3 → chapter 4 bridge in the new book's numbering scheme matches — the lib treats this as Ch 1 → Ch 2.
