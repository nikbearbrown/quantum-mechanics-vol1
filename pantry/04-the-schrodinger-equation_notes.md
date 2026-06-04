# Research Notes: Chapter 04 — The Schrödinger Equation

**Corresponding chapter:** chapters/04-the-schrodinger-equation.md (not yet written)
**Generated:** 2026-06-03

---

## Chapter summary (capability built)

By the end of this chapter the student can: (1) apply separation of variables to the time-dependent Schrödinger equation when V = V(x); (2) identify the separation constant E as energy; (3) write down a stationary state ψ_n(x) e^{−iE_n t/ℏ} and explain why its probability density is time-independent; (4) distinguish a stationary state from a general superposition; (5) write the general time-evolved state as a sum over eigenstates with rotating phases.

The simulation deliverable (`02-infinite-well.html`) makes the rotating phase and the sloshing of superpositions visible, while ⟨H⟩ stays constant as a verifiable check.

---

## A. Conceptual foundations

### A1. Separation of variables and the eigenvalue problem

**Explanation.** The TDSE is iℏ ∂Ψ/∂t = ĤΨ with Ĥ = −(ℏ²/2m) ∂²/∂x² + V(x). When V = V(x) (no explicit time dependence), the ansatz Ψ(x,t) = ψ(x) φ(t) separates the equation into two ODEs. Dividing by ψφ yields:

  iℏ φ'(t)/φ(t) = Ĥψ(x)/ψ(x)

The left side is a function of t only; the right side is a function of x only; therefore both equal a constant E. The time equation gives φ(t) = e^{−iEt/ℏ}. The spatial equation Ĥψ = Eψ is the time-independent Schrödinger equation (TISE) — an eigenvalue problem for ψ with eigenvalue E.

**Common misconception.** Students often believe separation of variables finds *all* solutions. It finds only the separable solutions — the stationary states. The completeness theorem (eigenstates of a self-adjoint operator form a basis for the relevant function space) guarantees that every solution is a superposition of stationary states, but this is a separate mathematical fact that must be stated explicitly.

**Worked example.** Suppose ψ(x) = √(2/L) sin(πx/L) (the ground state of an infinite well, anticipating Ch 5). The full time-dependent state is Ψ(x,t) = √(2/L) sin(πx/L) e^{−iE₁t/ℏ}. Compute |Ψ(x,t)|²:

  |Ψ(x,t)|² = (2/L) sin²(πx/L) |e^{−iE₁t/ℏ}|² = (2/L) sin²(πx/L)

The time factor has modulus 1; it vanishes from |Ψ|². The probability density is static — this is what "stationary" means.

**Sources.** Lib file: _lib_qmsri-02, §"Separating the problem." Griffiths (2018), §2.1. Shankar, *Principles of Quantum Mechanics*, 2nd ed. (1994), §5.1.

---

### A2. The separation constant E is energy

**Explanation.** The separation constant E is not just a mathematical label. In position representation, the expectation value of the Hamiltonian for a stationary state ψ_n e^{−iEt/ℏ} is ⟨H⟩ = ∫ ψ_n* Ĥ ψ_n dx = E_n ∫ |ψ_n|² dx = E_n. The variance is ⟨H²⟩ − ⟨H⟩² = 0: every energy measurement on a stationary state returns E_n with certainty. E is therefore the definite energy of the stationary state. For a superposition, ⟨H⟩ = Σ |c_n|² E_n — a weighted average, constant in time because the weights |c_n|² do not depend on t.

**Common misconception.** Students sometimes believe that e^{−iEt/ℏ} being complex means the energy is somehow imaginary or uncertain. It is not. The complex phase carries the time dependence; the energy E is a real eigenvalue. If E were complex the norm ∫|Ψ|² dx would grow or decay — inconsistent with the continuity equation proved in Ch 3.

**Worked example.** Show ⟨H⟩ is constant for a two-state superposition. Let Ψ = c₁ψ₁ e^{−iE₁t/ℏ} + c₂ψ₂ e^{−iE₂t/ℏ}, with |c₁|² + |c₂|² = 1. Then:

  ⟨H⟩ = ⟨Ψ|Ĥ|Ψ⟩ = |c₁|² E₁ + |c₂|² E₂

The cross terms involve ⟨ψ₁|ψ₂⟩ = 0 (orthogonality of eigenstates). So ⟨H⟩ = |c₁|² E₁ + |c₂|² E₂, independent of t. The simulation enforces this: ⟨H⟩ must be constant to four decimal places; drift is flagged red.

**Sources.** Lib file: _lib_qmsri-02, §"Separating the problem" and §"What 'stationary' actually means." Griffiths (2018), §2.1. Sakurai & Napolitano (2021), §1.4.

---

### A3. The phase e^{−iEt/ℏ} rotates but is not observable alone; relative phases are observable

**Explanation.** A stationary state Ψ_n = ψ_n(x) e^{−iEt/ℏ} has |Ψ_n|² = |ψ_n(x)|², independent of t. An overall (global) phase e^{iα} applied to any state is unobservable — it cancels in all expectation values and probability densities. However, the *relative* phase between two terms in a superposition is observable. In Ψ = (1/√2)(ψ₁ e^{−iE₁t/ℏ} + ψ₂ e^{−iE₂t/ℏ}), the relative phase is e^{−i(E₂−E₁)t/ℏ}; this is what drives the sloshing interference term.

**Common misconception.** "The wave function is rotating in time, so physics changes." For a single stationary state, no — the observable |Ψ|² is static. "Rotation of the phase" only becomes visible when two or more states with *different* E_n are superimposed. The simulation confirms: a single eigenstate shows static |Ψ(x,t)|²; adding a second eigenstate immediately produces oscillating ⟨x⟩(t).

**Worked example.** Set c₁ = c₂ = 1/√2, θ₁ = θ₂ = 0. Then:

  |Ψ(x,t)|² = ½ [ψ₁² + ψ₂² + 2ψ₁ψ₂ cos((E₂−E₁)t/ℏ)]

At t = 0: |Ψ|² = ½(ψ₁ + ψ₂)². At t = T/2 (half period): |Ψ|² = ½(ψ₁ − ψ₂)². The probability distribution has literally flipped from one half of the well to the other. Set θ₂ = π: the sloshing starts on the opposite side — the *relative* phase sets the initial shape.

**Sources.** Lib file: _lib_qmsri-02, §"What 'stationary' actually means." Griffiths (2018), §2.1.

---

### A4. The general solution is a superposition of stationary states

**Explanation.** Given a complete orthonormal set of energy eigenstates {ψ_n} with eigenvalues {E_n}, any initial state Ψ(x,0) can be expanded as Ψ(x,0) = Σ c_n ψ_n(x) with c_n = ⟨ψ_n|Ψ(x,0)⟩. The time-evolved state is then Ψ(x,t) = Σ c_n ψ_n(x) e^{−iE_n t/ℏ}. Each eigenstate rotates at its own angular frequency ω_n = E_n/ℏ. The interaction between different frequencies produces beats — the observable dynamics of non-stationary states.

**Common misconception.** "Solving the TISE is the end of the problem." The TISE gives the stationary states and their energies, but the dynamics of a general state require (1) expanding the initial condition in the eigenbasis and (2) letting each component accrue its phase. The two steps are distinct. Students who conflate them compute ψ_n(x) correctly and then forget to attach e^{−iE_n t/ℏ} or to sum.

**Worked example.** For the infinite well with Ψ(x,0) = √(2/L) sin(πx/L) [the ground state, as a trivial check]: c₁ = 1, all others = 0. Then Ψ(x,t) = √(2/L) sin(πx/L) e^{−iE₁t/ℏ}. Static |Ψ|², static ⟨x⟩ = L/2. For a non-trivial check: Ψ(x,0) ∝ sin(πx/L) + sin(2πx/L); the projection gives c₁ = c₂ = 1/√2 (after normalization); the time-evolved state sloshes between left and right halves of the well.

**Sources.** Lib file: _lib_qmsri-02, §"Building states from eigenstates." Griffiths (2018), §2.1. Stein & Shakarchi, *Fourier Analysis: An Introduction* (2003), Ch. 4 (completeness proof for the sine basis).

---

### A5. The completeness claim is classical mathematics (Fourier), not quantum postulation

**Explanation.** The claim "any state is a superposition of energy eigenstates" is not a new quantum postulate — it is the spectral theorem applied to the self-adjoint operator Ĥ on the relevant Hilbert space. For the infinite well, the eigenstates are sine functions, and their completeness is the Fourier sine series theorem established by Fourier in 1822 for the heat equation. The quantum version adds only the interpretation of the coefficients (probability amplitudes) and the time-evolution phase. Students who treat completeness as quantum mysticism have missed this mathematical fact.

**Common misconception.** "There might be states that cannot be expressed in terms of energy eigenstates." No — completeness is a theorem for L²([0,L]) with Dirichlet boundary conditions. Every normalizable state that vanishes at the walls is expandable in the sine basis. The convergence rate (how many terms are needed) depends on the smoothness of the state: smooth states converge rapidly, states with kinks converge as 1/n.

**Worked example.** A state with a sharp corner (tent function) at x = L/4 requires many terms. The simulation's "draw your own ψ" feature (described in Ch 5) makes this visible: at n_max = 5 the reconstruction is poor; at n_max = 20 it is visually indistinguishable. This is classical Fourier analysis, visible in real time.

**Sources.** Fourier, J. B. J. (1822). *Théorie analytique de la chaleur*. Stein & Shakarchi (2003), Ch. 4. Von Neumann, J. (1932). *Mathematische Grundlagen der Quantenmechanik* (modern spectral theory foundation). Lib file: _lib_qmsri-02, §"A note on completeness."

---

## B. Domain examples and cases

**B1. Single stationary state** — ψ_n e^{−iE_n t/ℏ}. The simulation's first verification task: set c₁ = 1, all others = 0. |Ψ(x,t)|² is static. ⟨x⟩ = L/2. ⟨H⟩ = E₁. The wave function rotates in the complex plane; the observable does not move.

**B2. Equal superposition of n = 1 and n = 2** — the canonical sloshing state. Period T = 2πℏ/(E₂ − E₁) = h/(3E₁) ≈ 3.66 fs for a 1 nm electron. The simulation makes this vivid: ⟨x⟩(t) oscillates; ⟨H⟩ stays pinned at (E₁ + E₂)/2.

**B3. Adiabatic context (from grad notes)** — if the well width expands slowly from L to 2L, a particle in the ground state n = 1 remains in the ground state of the *new* Hamiltonian but with a different energy. This is the adiabatic theorem. Not needed at this level, but a useful bridge to Ch 11 (WKB/tunneling). The grad note (qm.md §4.4, "particle in an infinite well") shows the adiabatic phase derivation.

**B4. Heat equation structural analogy** — the heat equation ∂_t u = D ∂²_{xx} u with Dirichlet BC has spatial eigenfunctions sin(nπx/L) identical to the TISE's. The time evolution differs: e^{−Dk_n²t} (decay, irreversible) vs. e^{−iE_n t/ℏ} (rotation, unitary). The imaginary unit in the TISE is what makes quantum mechanics unitary (probability-conserving) rather than dissipative. Ex. 2.9 in the lib file makes this structural comparison explicit and is worth including as a synthesis exercise.

**B5. Photon emission** — when an electron drops from n = 3 to n = 1 in a 1 nm well, the emitted photon has energy E₃ − E₁ = 9E₁ − E₁ = 8E₁ ≈ 3.02 eV, wavelength λ = hc/(8E₁) ≈ 411 nm (near UV/violet). This connects the abstract energy spectrum to a measurable optical quantity.

---

## C. Connections and dependencies

**Prerequisites:**
- Chapter 3 (The Wave Function): Born rule, normalization, |ψ|² as density, complex ψ, expectation values. The stationary-state phase e^{−iEt/ℏ} is only meaningful once ψ is understood as complex (Ch 3's core lesson).
- Ordinary differential equations: second-order linear ODEs with constant coefficients (needed to solve ψ'' = −k²ψ inside the well, introduced fully in Ch 5).
- Basic Fourier series: the completeness argument invokes it; the simulation extension ("draw your own ψ") makes it visual.

**Unlocks:**
- Chapter 5 (Infinite Square Well): Ch 4 provides the separation machinery; Ch 5 applies it to the infinite well and computes the eigenstates and energies explicitly.
- Chapter 6 (Harmonic Oscillator): the same separation leads to the harmonic oscillator TISE; the ladder-operator method solves it without fighting the ODE.
- All later chapters: the pattern "separate → TISE → eigenstates → time-evolve by phase-rotating each component" is the template for every exactly solvable system in the book.

**Adjacent chapters:**
- Ch 4 (this chapter) maps to the first section of _lib_qmsri-02 ("Separating the problem," "The TISE, written out").
- The "what 'stationary' actually means" and "building states from eigenstates" sections of the lib file are shared between Ch 4 and Ch 5 — they belong more naturally in Ch 4 as conceptual foundation, with Ch 5 as the worked application.

---

## D. Current state of the field

**Settled.**
- The TDSE and the separation-of-variables method: foundational, settled since Schrödinger (1926).
- Completeness of the eigenstate basis for confining potentials: mathematical theorem, established by spectral theory of self-adjoint operators (von Neumann 1932; see also Reed & Simon, *Methods of Modern Mathematical Physics*, Vol. 2, 1975).
- Conservation of ⟨H⟩ for time-independent Hamiltonians: follows from unitarity of time evolution (Schrödinger equation is a unitary flow on Hilbert space).

**Contested / open.**
- None at this level. The TISE and separation of variables are not contested.

**Key references.**
- Schrödinger, E. (1926). Ann. Phys. 79, 361 (the original TDSE paper). English translation in Schrödinger, *Collected Papers on Wave Mechanics* (1928).
- Griffiths, D. J. & Schroeter, D. F. (2018). §2.1.
- Shankar, R. (1994). *Principles of Quantum Mechanics*, §5.1.
- Stein, E. M. & Shakarchi, R. (2003). *Fourier Analysis: An Introduction*. Princeton. Ch. 4.
- Von Neumann, J. (1932). *Mathematische Grundlagen der Quantenmechanik*. Springer.

---

## E. Teaching considerations

**The "separation constant" naming.** The constant E should be named and motivated as energy from the first time it appears. Students who see it only as a mathematical constant miss the physical content. The lib file does this correctly: it names E immediately and explains why both sides of the separated equation must equal the same constant.

**Phase convention.** The phase is e^{−iEt/ℏ}, not e^{+iEt/ℏ}. The sign matters: the wrong sign flips the sloshing direction in the simulation (a verifiable check). The CLAUDE.md snippet flags this explicitly. Students who confuse the sign will see the probability density slosh in the wrong direction.

**"Stationary" does not mean "motionless wave function."** The wave function rotates in the complex plane; only |Ψ|² is stationary. This distinction is critical. A good simulation move: show Re Ψ and Im Ψ spinning (they are not static!) while |Ψ|² stays fixed. The lib file has this in §"What 'stationary' actually means."

**Energy conservation as a simulation check.** ⟨H⟩ must be exactly constant (to numerical precision) for any state. If it drifts, the time evolution is wrong. This is both a physical fact and a practical debugging criterion. Build it into the simulation interface as a live readout with a red/green indicator.

**The two-step structure.** Always present separation as two distinct steps: (1) solve the TISE to get {ψ_n, E_n}; (2) expand the initial condition and phase-rotate each component. Students who conflate these steps skip step (2) and compute only the stationary state that matches the initial condition, missing the dynamics of superpositions entirely.

**Common student confusions to anticipate:**
- Believing that any ψ(x,0) is automatically a stationary state.
- Forgetting to attach e^{−iE_n t/ℏ} to each term when writing Ψ(x,t).
- Confusing the global phase (unobservable) with the relative phase (observable and drives sloshing).
- Thinking ⟨H⟩ depends on time.

---

## F. Library files relevant to this chapter

- **Primary:** `/pantry/_lib_qmsri-02-the-time-independent-schrodinger-equation.md` — the full drafted chapter text for the sibling book's Ch 2. Contains: separation of variables, TISE written out, the infinite well derivation, stationary-state argument, completeness/Fourier discussion, sloshing calculation, LLM exercise prompt, exercises 2.1–2.10.
- **Secondary:** `/pantry/_lib_qmsri-01-the-wave-function.md` — the continuity equation and normalization proof belong in Ch 3, but the stationary-state verification exercise (Exercise 4 in the lib) draws on both chapters.
- **Optional:** `/books/physics-quantum-mechanics-sri/pantry/qm.md` — grad-level treatment; most relevant excerpt is §4.4 (adiabatic theorem, infinite-well example, lines ~1930–1990). Also confirms standard time-evolution formula Ψ(x,t) = Σ c_n ψ_n(x) e^{−iE_n t/ℏ} at lines ~919 and ~637.

---

## G. Gaps and flags

1. **Chapter boundary: where does Ch 4 end and Ch 5 begin?** The lib file's Ch 2 covers both the separation-of-variables method (Ch 4 of the new book) and the infinite-well solution (Ch 5 of the new book). The chapter author must decide where to split. Recommended split: Ch 4 ends after the completeness argument and the formula Ψ(x,t) = Σ c_n ψ_n e^{−iE_n t/ℏ} is established as a general principle; Ch 5 begins with "now apply this to the specific case V(x) = infinite well."

2. **The completeness theorem.** The lib file says "it is a theorem" and cites Stein & Shakarchi. This is correct but students may want a more accessible reference. Consider adding: Körner, T. W. (1988). *Fourier Analysis*. Cambridge. Ch. 1–3 (accessible proof of Fourier series completeness).

3. **Continuous vs. discrete spectrum.** The lib file mentions that confining potentials give a discrete spectrum and non-confining potentials give continuous or mixed spectra, but does not develop this. For Ch 4 it is enough to flag it; the finite well (Ch 7 or later) will develop the scattering states. Don't leave students thinking all spectra are discrete.

4. **Negative energy solutions.** For the infinite well, E < 0 gives e^{κx} solutions that blow up and are excluded — the lib file mentions E > 0 implicitly but does not discuss E ≤ 0 explicitly. This is worth a footnote, especially for students who will encounter the finite well where E < 0 bound states are interesting.

5. **The simulation's ⟨H⟩ drift flag.** The CLAUDE.md snippet says "⟨H⟩ drift > 10⁻³ relative is a bug." Make sure this threshold is stated in the chapter's tech notes so students know what acceptable numerical precision looks like.
