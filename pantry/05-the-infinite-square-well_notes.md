# Research Notes: Chapter 05 — The Infinite Square Well

**Corresponding chapter:** chapters/05-the-infinite-square-well.md (not yet written)
**Generated:** 2026-06-03

---

## Chapter summary (capability built)

By the end of this chapter the student can: (1) apply boundary conditions to the infinite square well and derive the quantized energies E_n = n²π²ℏ²/(2mL²); (2) write down and normalize the eigenstates ψ_n(x) = √(2/L) sin(nπx/L); (3) verify orthonormality using trigonometric identities; (4) expand an initial state in the eigenstate basis by computing the projection integrals c_n = ⟨ψ_n|Ψ(x,0)⟩; (5) time-evolve the superposition analytically; (6) compute ⟨x⟩(t) for a two-state superposition and identify the oscillation frequency.

The simulation deliverable (`02-infinite-well.html`) makes the sloshing of |Ψ(x,t)|² visible, with live ⟨x⟩(t) and ⟨H⟩ readouts confirming the physics.

---

## A. Conceptual foundations

### A1. Boundary conditions quantize the spectrum — quantization is not assumed

**Explanation.** Inside the well (V = 0), the TISE gives ψ'' = −k²ψ with general solution ψ(x) = A sin(kx) + B cos(kx). Any k works — there is no quantization yet. Applying ψ(0) = 0 eliminates B (the cosine term). Applying ψ(L) = 0 requires sin(kL) = 0, which holds only for kL = nπ (n = 1, 2, 3, …). The continuous family of allowed k values collapses to a discrete set. Quantization is a consequence of asking the wave function to be continuous at the walls — not a postulate about angular momentum.

This is the key "oh" moment of the chapter: Bohr's rule (1913) was a postulate; Schrödinger's equation (1926) shows it was a consequence. Boundary conditions create discrete spectra exactly as they do for a guitar string.

**Common misconception.** "Quantization is a postulate of quantum mechanics." No — for the infinite well, it falls out of the mathematics of waves in a box. Students who absorbed Bohr's model first are especially prone to treating quantization as fundamental rather than derived.

**Worked example.** Step-by-step:
1. Inside: ψ'' = −k²ψ, k = √(2mE)/ℏ. General solution: ψ = A sin(kx) + B cos(kx).
2. At x = 0: ψ(0) = B = 0. Now ψ = A sin(kx).
3. At x = L: ψ(L) = A sin(kL) = 0. A ≠ 0 (trivial solution excluded), so sin(kL) = 0.
4. Therefore kL = nπ → k_n = nπ/L → E_n = ℏ²k_n²/(2m) = n²π²ℏ²/(2mL²).
5. For n = 0: ψ ≡ 0 (no particle). For n < 0: sin(−nπx/L) = −sin(nπx/L), same physical state. So n = 1, 2, 3, … covers all distinct states.

**Sources.** Lib file: _lib_qmsri-02, §"The infinite square well — eight steps." Griffiths (2018), §2.2. Bohr (1913), *Phil. Mag.* 26, 1 (the original quantization postulate, for contrast).

---

### A2. The energy spectrum scales as n² — numerical consequences

**Explanation.** E_n = n²E₁ with E₁ = π²ℏ²/(2mL²). The spectrum is 1, 4, 9, 16, 25, … times E₁ — nothing in between. For an electron in a 1 nm well: E₁ ≈ 0.377 eV, E₂ ≈ 1.508 eV, E₃ ≈ 3.39 eV. Level spacings are in the optical range. For a marble in a 1 cm box: E₁ ~ 10⁻⁵⁸ eV — unmeasurably small; quantum discreteness disappears. The classical limit is the limit m → ∞ or L → ∞, not a separate postulate.

**Common misconception.** "Quantum mechanics is always relevant at small scales." Relevance depends on E_n/(k_BT). For a nanometer-scale quantum well, E₁ ≫ k_BT at room temperature (~0.025 eV) — quantum effects dominate. For a proton in a 1 nm well, E₁ ≈ 0.377/1836 eV ≈ 2 × 10⁻⁴ eV — smaller but still potentially relevant at low temperature. The criterion is the dimensionless ratio E_n/(k_BT), not just the size of the object.

**Worked example.** An electron in a 1 nm well emits a photon and drops from n = 3 to n = 1. Energy of photon: E₃ − E₁ = (9 − 1)E₁ = 8 × 0.377 eV ≈ 3.02 eV. Wavelength: λ = hc/(3.02 eV) ≈ 411 nm. This is violet light, near the edge of the visible spectrum — connecting the abstract energy formula to a measurable color.

Scaling check: for L = 2 nm (double the width), E₁ scales as 1/L² → E₁(2 nm) = 0.377/4 ≈ 0.094 eV. The n² scaling gives E₂/E₁ = 4, E₃/E₁ = 9, exactly.

**Sources.** Lib file: _lib_qmsri-02, §"What the energy scale tells us." Esaki & Tsu (1970), *IBM J. Res. Dev.* 14, 61 (semiconductor quantum-well proposal — the experiment that showed quantum-well energy levels are real and tunable). Griffiths (2018), §2.2.

---

### A3. Eigenstates are orthonormal — the trigonometric argument

**Explanation.** The normalized eigenstates are ψ_n(x) = √(2/L) sin(nπx/L). Orthonormality:

  ⟨ψ_m|ψ_n⟩ = (2/L) ∫₀ᴸ sin(mπx/L) sin(nπx/L) dx = δ_mn

The proof uses the product-to-sum identity sin α sin β = ½[cos(α − β) − cos(α + β)]. For m ≠ n, both cosines integrate over an integer number of half-periods on [0, L] and give zero. For m = n, the first cosine becomes 1 (integrating to L) and the second integrates to zero. No numerical eigensolver, no Gram-Schmidt — the orthogonality falls from a single trigonometric identity. This is the calculation the chapter asks students to do themselves (Ex. 2.2 in the lib).

**Common misconception.** "Orthogonality must be verified numerically, or imposed by Gram-Schmidt." No — the analytic argument from the product-to-sum identity is exact. The CLAUDE.md snippet for the simulation explicitly prohibits Gram-Schmidt; using it hides this clean mathematical fact.

**Worked example.** Verify ⟨ψ₁|ψ₂⟩ = 0:
  (2/L) ∫₀ᴸ sin(πx/L) sin(2πx/L) dx
  = (1/L) ∫₀ᴸ [cos(πx/L) − cos(3πx/L)] dx
  = (1/L) [L/π sin(πx/L) − L/(3π) sin(3πx/L)]₀ᴸ = 0.
Both sin terms vanish at x = 0 and x = L. Verify ⟨ψ₁|ψ₁⟩ = 1: the (cos 0) = 1 term gives (1/L)·L = 1. ✓

**Sources.** Lib file: _lib_qmsri-02, §"Building states from eigenstates." Griffiths (2018), §2.2. Stein & Shakarchi (2003), Ch. 2.

---

### A4. Zero-point energy — required by the uncertainty principle

**Explanation.** The ground-state energy E₁ = π²ℏ²/(2mL²) > 0. This is not a quantum anomaly — it is forced by the uncertainty principle. If E = 0, then p = 0 → σ_p = 0. But the particle is confined to [0, L] so σ_x ≤ L. Then σ_x σ_p ≤ L · 0 = 0 < ℏ/2 — violating the Kennard inequality. The uncertainty principle *requires* a positive minimum energy for any confined particle.

Quantitatively: for the ground state, σ_x = L√(1/12 − 1/(2π²)) ≈ 0.181 L and σ_p = πℏ/L, giving σ_x σ_p ≈ 0.568 ℏ ≥ ℏ/2. The ratio ≈ 1.136 (the simulation confirms this live for n = 1, L = 10 nm). The ground state is not far from the uncertainty bound — it is nearly as localized as quantum mechanics allows.

**Common misconception.** "Zero-point energy is a mysterious quantum property with no classical analogue." The concept has a perfectly clear Fourier-analysis origin: confine a wave, the smallest non-trivial mode has a non-zero frequency, and kinetic energy scales as frequency squared. The guitar string analogy works: a guitar string under tension that is fixed at both ends has a minimum non-zero frequency (the fundamental) — it cannot vibrate at zero frequency while being non-trivially displaced.

**Worked example.** Derive σ_p for the ground state using p̂ = −iℏ ∂/∂x:
  ⟨p⟩ = (2/L) ∫₀ᴸ sin(πx/L) (−iℏ)(π/L) cos(πx/L) dx
       = (−iℏπ/L²) ∫₀ᴸ sin(2πx/L) dx = 0.
[Odd-symmetry argument: the integral of sin over one full period is zero.]
  ⟨p²⟩ = (2/L) ∫₀ᴸ sin(πx/L) (−ℏ²)(−π²/L²) sin(πx/L) dx = ℏ²π²/L².
  σ_p = √⟨p²⟩ = πℏ/L.

**Sources.** Lib file: _lib_qmsri-02, §"What the ground state tells us about zero." Griffiths (2018), §2.2. The zero-point energy of the quantum harmonic oscillator (½ℏω) generalizes this — see Ch 6.

---

### A5. Superpositions and the sloshing probability density — the beat frequency

**Explanation.** A general state Ψ(x,t) = Σ c_n ψ_n(x) e^{−iE_n t/ℏ}. For the simplest non-trivial case c₁ = c₂ = 1/√2:

  |Ψ(x,t)|² = ½[ψ₁² + ψ₂² + 2ψ₁ψ₂ cos((E₂−E₁)t/ℏ)]

The cross term oscillates at angular frequency ω = (E₂ − E₁)/ℏ = 3E₁/ℏ. Because ψ₁ = √(2/L) sin(πx/L) peaks at x = L/2 and ψ₂ = √(2/L) sin(2πx/L) peaks at x = L/4 and 3L/4, the cross term shifts probability between the two halves of the well. The probability density sloshes left and right with period T = 2πℏ/(E₂ − E₁) = h/(3E₁).

For an electron in a 1 nm well: T ≈ 3.66 fs — the simulation shows this sloshing and the student can measure the period from the ⟨x⟩(t) plot.

⟨x⟩(t) = L/2 + (some oscillating term) — the average position oscillates even though the energy is constant. The energy of the state is ⟨H⟩ = (E₁ + E₂)/2 ≈ 0.942 eV and is exactly constant throughout.

**Common misconception.** "The sloshing means the particle's energy is changing." No — ⟨H⟩ is constant; the time-independent weights |c_n|² are constants. The sloshing is a *phase* phenomenon — the relative phase between ψ₁ e^{−iE₁t/ℏ} and ψ₂ e^{−iE₂t/ℏ} evolves, shifting the interference pattern. The particle's where is changing; its energy is not.

**Worked example.** Compute ⟨x⟩(t) for the two-state superposition with c₁ = c₂ = 1/√2:
  ⟨x⟩(t) = ½ ∫₀ᴸ x [ψ₁² + ψ₂² + 2ψ₁ψ₂ cos(ωt)] dx
           = ½(⟨x⟩₁ + ⟨x⟩₂) + cos(ωt) ∫₀ᴸ x ψ₁(x) ψ₂(x) dx
  where ⟨x⟩₁ = ⟨x⟩₂ = L/2 (by symmetry of both eigenstates).
  The cross integral: ∫₀ᴸ x · (2/L) sin(πx/L) sin(2πx/L) dx.
  Using product-to-sum: = (1/L) ∫₀ᴸ x [cos(πx/L) − cos(3πx/L)] dx.
  Both integrals by parts yield non-zero results; the net cross integral = −16L/(9π²).
  Therefore: ⟨x⟩(t) = L/2 − (16L/(9π²)) cos(ωt) ≈ L/2 − 0.181L cos(ωt).
  The amplitude of oscillation is ≈ 0.181L; ⟨x⟩ oscillates between about 0.319L and 0.681L.

**Sources.** Lib file: _lib_qmsri-02, §"What 'stationary' actually means." Griffiths (2018), §2.2 (Problem 2.5 in Griffiths is essentially this calculation). Sakurai & Napolitano (2021), §1.4.

---

## B. Domain examples and cases

**B1. Quantum-well lasers** — the infinite-well energy spectrum is the idealized version of what semiconductor quantum-well lasers exploit. By controlling L, manufacturers tune the emission wavelength. Esaki & Tsu (1970) proposed the semiconductor superlattice; Dingle et al. (1974) confirmed discrete quantum-well energy levels spectroscopically. By the 1990s, quantum-well lasers were in every CD player. This is the experimental anchor for the n²π²ℏ²/(2mL²) formula.

**B2. Cold atoms in optical lattices** — laser-cooled atoms in periodic optical potentials realize nearly ideal box-like confinement. Spectroscopic measurements of energy-level spacings confirm the TISE prediction with corrections only from the finite depth and anharmonicity of the optical potential. A cleaner realization of the ideal well than any semiconductor. (Jaksch et al. 1998; Greiner et al. 2002.)

**B3. STM quantum corrals** — electrons confined to nanoscale rings and ellipses on metal surfaces, visualized by scanning tunneling microscopy. Crommie, Lutz & Eigler (1993) showed standing-wave patterns in the electron density consistent with quantum confinement. Not an infinite square well geometry, but the same physical principle.

**B4. Energy level table for different masses and lengths.**

| System | m (kg) | L (m) | E₁ (eV) | Quantum? |
|---|---|---|---|---|
| Electron, 1 nm well | 9.11×10⁻³¹ | 10⁻⁹ | 0.377 | Yes (≫ k_BT) |
| Electron, 1 cm box | 9.11×10⁻³¹ | 10⁻² | 3.77×10⁻¹⁵ | No |
| Proton, 1 nm well | 1.67×10⁻²⁷ | 10⁻⁹ | 2.05×10⁻⁴ | Borderline |
| C₆₀, 10 nm trap | ~1.2×10⁻²⁴ | 10⁻⁸ | ~4×10⁻¹⁰ | No |
| Marble, 1 cm box | ~10⁻³ | 10⁻² | ~10⁻⁵⁸ | Absolutely not |

The dimensionless ratio E₁/(k_BT) at room temperature (k_BT ≈ 0.025 eV) separates quantum from classical.

**B5. Node counting** — ψ_n has exactly n − 1 nodes inside the well (zeros strictly interior to (0, L)). The ground state has none; it is a positive half-sine. The first excited state has one node at x = L/2. Higher states have more nodes and more rapid oscillation — higher spatial frequency = higher momentum = higher kinetic energy. This is the spatial Fourier logic made concrete: wavelength λ_n = 2L/n, momentum p_n = h/λ_n = nπℏ/L, energy E_n = p_n²/(2m) = n²π²ℏ²/(2mL²).

---

## C. Connections and dependencies

**Prerequisites:**
- Chapter 3 (The Wave Function): Born rule, normalization, complex ψ. The expansion c_n = ⟨ψ_n|Ψ⟩ requires knowing what an inner product means.
- Chapter 4 (The Schrödinger Equation): separation of variables, TISE as eigenvalue problem, time-evolution formula Ψ(x,t) = Σ c_n ψ_n e^{−iE_n t/ℏ}, completeness. Chapter 5 is the first worked example of all of this.
- Trigonometric identities: product-to-sum formula sin α sin β = ½[cos(α − β) − cos(α + β)]. Must be in hand before the orthogonality proof.
- Integration by parts: needed for computing c_n from a non-eigenstate initial condition.

**Unlocks:**
- Chapter 6 (Harmonic Oscillator): the same pattern — TISE, boundary conditions (here algebraic via ladder operators instead of spatial), orthonormal eigenstates, superpositions and coherent states.
- Chapter 7 (Finite Square Well): the infinite well is the limiting case of the finite well as V₀ → ∞. Understanding the infinite well first makes the finite-well boundary matching (with exponential tails) less mysterious.
- All scattering chapters: the plane-wave solutions (not normalizable) are the V = 0 version of the infinite-well solutions without the boundary conditions. The relationship between standing waves and traveling waves becomes clear.

**Adjacent chapters:**
- Ch 5 (this chapter) maps to the §"Infinite square well — eight steps," §"What the ground state tells us about zero," §"Building states from eigenstates," and §"What 'stationary' actually means" sections of _lib_qmsri-02.
- The "draw your own ψ" simulation feature (Ch 5 extension) makes the Fourier completeness result from Ch 4 visually concrete.

---

## D. Current state of the field

**Settled.**
- The energy spectrum E_n = n²π²ℏ²/(2mL²) and eigenstates ψ_n = √(2/L) sin(nπx/L): derived from the Schrödinger equation, experimentally confirmed in semiconductor quantum wells and cold-atom systems.
- Zero-point energy: observed directly in the ground-state energies of confined systems. The Casimir effect (1948) — attractive force between uncharged metal plates due to vacuum fluctuations — is a macroscopic consequence of zero-point energy.
- Orthonormality of {ψ_n}: mathematical theorem, confirmed numerically to arbitrary precision.

**Contested / open.**
- Interpretation of the zero-point energy in the many-body/quantum field theory context (cosmological constant problem, vacuum energy) — not relevant at this pedagogical level. Flag as a pointer to Vol. 3 or beyond.
- The infinite square well is not a realizable physical system (infinitely hard walls). Real systems (finite well, harmonic oscillator, hydrogen atom) have finite potentials. The infinite well's virtue is pedagogical: it gives clean, exact, closed-form solutions with no approximation needed.

**Key references.**
- Schrödinger, E. (1926). Ann. Phys. 79, 361.
- Esaki, L. & Tsu, R. (1970). IBM J. Res. Dev. 14, 61.
- Dingle, R., Wiegmann, W. & Henry, C. H. (1974). Phys. Rev. Lett. 33, 827.
- Crommie, M. F., Lutz, C. P. & Eigler, D. M. (1993). Science 262, 218 (quantum corral).
- Jaksch, D. et al. (1998). Phys. Rev. Lett. 81, 3108 (cold atoms in optical lattices, theoretical).
- Greiner, M. et al. (2002). Nature 415, 39 (Mott insulator to superfluid transition, optical lattice).
- Griffiths, D. J. & Schroeter, D. F. (2018). §2.2.
- Stein, E. M. & Shakarchi, R. (2003). *Fourier Analysis: An Introduction*. Princeton. Ch. 4.

---

## E. Teaching considerations

**The eight-step derivation as a template.** The lib file's §"Infinite square well — eight steps" presents the derivation in a numbered, traceable sequence. This structure is deliberate: students should be able to reproduce the derivation in their own words. The eight steps are: (1) write the TISE inside the well; (2) identify the ODE; (3) write the general solution; (4) apply BC at x = 0; (5) apply BC at x = L; (6) identify quantization; (7) compute E_n; (8) normalize. Each step is mechanical once you know to do it. The "oh" moment is step 6 — name it explicitly.

**The guitar-string analogy.** Boundary conditions → discrete frequencies → discrete energies. A guitar string fixed at both ends can only vibrate at frequencies f_n = n/(2L) × (wave speed). A quantum particle in a box can only have energies E_n = n² × E₁. The analogy is exact, not approximate: both arise from the same mathematics (Sturm-Liouville problem on a finite interval). Lean on this; it makes quantization feel earned rather than mysterious.

**Simulation design for sloshing.** The lib file's simulation prompt specifies: c₁ = c₂ = 1/√2, θ₁ = θ₂ = 0 → ⟨x⟩ first decreases (slosh left) for the −i convention (e^{−iEt/ℏ}). Setting θ₂ = π reverses the initial slosh direction. Students should test this and explain it from the formula: at t = 0, |Ψ|² = ½(ψ₁ + ψ₂)² vs. ½(ψ₁ − ψ₂)². The initial shape of |Ψ|² is entirely determined by the relative phase θ₂ − θ₁.

**⟨H⟩ constancy as the conceptual anchor.** The most important thing to hammer: ⟨H⟩ = Σ |c_n|² E_n = constant. The sloshing moves probability around the well; the energy budget does not change. This dissociation between spatial probability and energy is a genuinely non-classical feature. In classical mechanics, if the ball moves to one side, it has more potential energy; in the well (V = 0 inside), moving probability left or right changes nothing about the energy.

**Convergence of the eigenstate expansion.** When students "draw their own ψ" in the simulation, they see the reconstruction improve with n_max. A smooth Gaussian needs n_max ~ 10; a tent function (sharp corner) needs n_max ~ 30. A step function (discontinuous) converges extremely slowly (Gibbs phenomenon). This is a live demonstration of the mathematical principle that smoother functions have faster-decaying Fourier coefficients — a preview of the connection between regularity and spectral behavior.

**Common student confusions to anticipate:**
- Failing to exclude n = 0 (zero particle) and n < 0 (duplicate states) from the spectrum.
- Confusing the normalization constant √(2/L) with the amplitude of the wave function.
- Evaluating |c_n|² instead of c_n when computing the projection (forgetting to take the inner product, not the norm squared).
- Believing the energy changes when the probability distribution sloshes.
- Confusing the period T = h/(E₂ − E₁) with the angular frequency ω = (E₂ − E₁)/ℏ.

---

## F. Library files relevant to this chapter

- **Primary:** `/pantry/_lib_qmsri-02-the-time-independent-schrodinger-equation.md` — the full drafted chapter text. Contains: the eight-step infinite-well derivation, energy scale table, orthonormality proof, completeness and Fourier discussion, sloshing calculation with the explicit cross-term integral, zero-point energy argument, LLM exercise prompt (with 5 verification checks and known failure modes), exercises 2.1–2.10.
- **Secondary:** `/pantry/_lib_qmsri-01-the-wave-function.md` — the Gaussian and infinite-well uncertainty ratios (σ_x σ_p /(ℏ/2) = 1.000 for Gaussian; ≈ 1.136 for n = 1) bridge Ch 3 and Ch 5. Exercise 4 in the lib file (compute ⟨x⟩, ⟨x²⟩, σ_x for the ground state) spans both chapters.
- **Optional:** `/books/physics-quantum-mechanics-sri/pantry/qm.md` — grad-level notes use the infinite well only in the adiabatic context (§4.4, lines ~1935–1990). Not needed for this chapter but useful for the chapter author to know the higher-level usage.

---

## G. Gaps and flags

1. **The cross-integral calculation for ⟨x⟩(t).** The lib file states the sloshing result but does not show the full computation of the cross integral ∫₀ᴸ x ψ₁ψ₂ dx. This is a rich calculation that students should do at least once. Include it as an Application exercise (comparable to Griffiths Ex. 2.5). The result −16L/(9π²) should appear in the notes.

2. **What happens for n_max > 2 superpositions.** The two-state case is the canonical example, but a five-state equal superposition has 10 distinct beat frequencies — the pattern is no longer a simple sinusoid. This is the "dephasing" phenomenon mentioned at the end of the lib chapter. A note or exercise here would connect to why macroscopic objects don't quantum-slosh: many energy levels → many frequencies → rapid dephasing.

3. **Projection formula for non-eigenstate initial conditions.** The lib file states c_n = ⟨ψ_n|Ψ(x,0)⟩ but does not show a worked example of computing c_n for a non-trivial initial state (e.g., a Gaussian centered at L/4). The simulation's "draw your own" feature does this numerically; a hand-calculation example for at least one simple state (e.g., a tent function) would be pedagogically valuable.

4. **Finite vs. infinite well.** The lib file does not discuss what changes when V = V₀ < ∞. A one-paragraph flag pointing to the finite well (later chapter) would help students understand that the infinite well is an idealization — real quantum dots and semiconductor wells have finite barriers, and electrons can tunnel out.

5. **Parity.** The eigenstates alternate between even (n = 1, 3, 5, …) and odd (n = 2, 4, 6, …) with respect to the center of the well x = L/2. This parity selection rule is implicit in the orthogonality proof and explicit in the node-counting argument, but the lib file does not name it "parity." Naming it here previews the parity symmetry discussion in later chapters (harmonic oscillator, hydrogen atom).

6. **Experimental section needs updating.** The lib file cites Esaki & Tsu (1970) and mentions "quantum-well laser work through the 1980s and 1990s." For a book published in 2026, add a sentence noting that quantum-dot systems (3D confinement, discrete spectrum in all three dimensions) are now a mature technology in LED displays, solar cells, and single-photon sources. Refs: Ekimov & Onushchenko (1984, semiconductor quantum dots); Brus (1984); Bruchez et al. (1998, biomedical quantum dots).

7. **Simulation phase-convention check.** The CLAUDE.md snippet specifies: for c₁ = c₂ = 1/√2, θ₁ = θ₂ = 0, ⟨x⟩(t) should *first decrease* (slosh left) under the −i convention. Verify this against the cross-integral result: the coefficient is −16L/(9π²) < 0, meaning ⟨x⟩(0) = L/2 and the initial slope d⟨x⟩/dt has the sign of −sin(0) × (negative coefficient), giving an initial *increase* (slosh right) at t = 0⁺. Double-check this sign against the lib file's simulation verification criteria — the lib says "first decrease (slosh left)" which may correspond to a specific choice of which eigenstate is called ψ₁ vs. ψ₂ and the sign of the cross integral. This needs resolution before the simulation is built.
