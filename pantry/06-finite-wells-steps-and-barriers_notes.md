# Research Notes: Chapter 06 — Finite Wells, Steps, and Barriers

**Corresponding chapter:** chapters/06-finite-wells-steps-and-barriers.md (not yet written)
**Generated:** 2026-06-03

---

## Chapter summary (capability built)

By the end of this chapter the student can: (1) set up and solve the transcendental matching conditions for the finite square well to find the finite number of bound states; (2) derive and apply reflection and transmission coefficients R and T for a potential step in both the E < V₀ and E > V₀ regimes, verifying R + T = 1; (3) write the exact transmission formula for a rectangular barrier, evaluate it numerically for given parameters, and sketch how T varies with E and with barrier width L; (4) connect the exponential suppression in the thick-barrier limit to the WKB Gamow factor from Chapter 11 of the source library (_lib_qmsri-11). The simulation deliverable is an interactive browser tool where the student sets V₀, L, and E and watches T and the wave function change in real time.

---

## A. Conceptual foundations

### A1. The finite square well: bound states and transcendental matching

**Explanation.** The finite square well has V = −V₀ inside |x| < L/2 and V = 0 outside. Bound states satisfy E < 0 (taking V = 0 outside as reference) or equivalently E < V₀ if V₀ is defined as a positive depth. Inside the well the solution oscillates (sinusoidal); outside it decays exponentially. Continuity of ψ and dψ/dx at both walls yields two transcendental equations, one for even-parity states and one for odd-parity states:

- Even: κ = k tan(kL/2), where k = √(2m(E+V₀))/ℏ inside, κ = √(−2mE)/ℏ outside
- Odd: κ = −k cot(kL/2)

These have no closed-form solution; they are solved graphically by plotting both sides as functions of E. The number of bound states is finite and always at least one (unlike the 3D spherical well, which can have zero). As V₀ → ∞, the energy eigenvalues recover the infinite-square-well results.

**Common misconception.** Students expect the finite well to have infinitely many bound states (by analogy with the infinite well). In fact, the number is finite: N ≈ (L/π)·√(2mV₀)/ℏ, rounded up. A well that is too shallow or too narrow for a second level will have exactly one bound state. Students also confuse the depth V₀ with the bound-state energy E: bound state energies are negative (or between 0 and V₀, depending on sign convention), not equal to V₀.

**Worked example.** An electron in a well of width L = 1 nm and depth V₀ = 10 eV. Compute k = √(2mₑ(V₀−|E|))/ℏ and κ = √(2mₑ|E|)/ℏ for trial E. Plot κ vs. k tan(kL/2); crossing points are bound-state energies. Numerically: approximately 2 bound states (one even, one odd) fit below V₀ = 10 eV in 1 nm.

**Sources.**
- PhysicsLibreTexts, "3.4: Finite Square Well" (UCD Physics 9HE): https://phys.libretexts.org/Courses/University_of_California_Davis/UCD:_Physics_9HE_-_Modern_Physics/03:_One-Dimensional_Potentials/3.4:_Finite_Square_Well
- Herman, R.L., "PHY 444 — Finite Square Well," UNCW lecture notes (Fall 2021): https://people.uncw.edu/hermanr/qm/Finite_Square_Well.pdf
- Skrzypczyk, "The finite square well: Root Finding & Quantum Mechanics," UBC tutorial: https://phas.ubc.ca/~rozali/Tutorial2.pdf
- Research application: Alhaidari et al., "A study of bound states for square potential wells with position-dependent mass," arXiv:quant-ph/0608102 (academic extension)
- ResearchGate: "Solving the Schrödinger Equation for a Finite Square Well: Application to Deuteron Bound State Energy," 2024: https://www.researchgate.net/publication/384764182

### A2. The potential step: reflection when E > V₀

**Explanation.** Consider V = 0 for x < 0 and V = V₀ for x > 0, with a particle incident from the left. Two cases:

Case 1 (E > V₀): both regions have oscillatory solutions. Let k₀ = √(2mE)/ℏ (region I) and k₁ = √(2m(E−V₀))/ℏ (region II). Matching ψ and ψ' at x = 0 (no reflected wave in region II):

- R = ((k₀ − k₁)/(k₀ + k₁))²
- T = 4k₁k₀/(k₀ + k₁)²
- R + T = 1 (verified by probability current conservation)

The particle is partially reflected even though E > V₀. This is pure wave behavior with no classical analogue.

Case 2 (E < V₀): k₁ becomes imaginary, κ = √(2m(V₀−E))/ℏ. The wave function decays exponentially into the barrier region; R = 1 (total reflection). The evanescent tail penetrates but carries no net current.

**Common misconception.** Classical intuition says a particle with E > V₀ always transmits (R = 0). Quantum mechanically, R is non-zero whenever there is an abrupt change in k, regardless of sign of V₀ − E. Even a potential step downward (V₀ < 0) reflects partially. This surprises students because the particle "has enough energy" — but the reflection arises from the wave-mechanical impedance mismatch, not from energy considerations.

**Worked example.** Hydrogen atom beam (m = 1 u = 1.67×10⁻²⁷ kg) hitting a 2 meV step at E = 5 meV. k₀ = √(2×1.67×10⁻²⁷×5×10⁻³×1.6×10⁻¹⁹)/ℏ, k₁ same with (E−V₀) = 3 meV. R = ((k₀−k₁)/(k₀+k₁))² ≈ 0.03; T ≈ 0.97. Even at E/V₀ = 2.5, 3% is reflected.

**Sources.**
- Walet, N., "6.2: Potential step," Quantum Mechanics (Walet), Physics LibreTexts: https://phys.libretexts.org/Bookshelves/Quantum_Mechanics/Quantum_Mechanics_(Walet)/06:_Scattering_from_Potential_Steps_and_Square_Barriers/6.02:_Potential_step
- York University tutorial, "2.5. Particle incident on a potential step and Quantum Mechanical Tunneling": https://www-users.york.ac.uk/~pjd113/notebooks/2_5_particle_incident_on_a_potential_step.html
- Brocku PPLATO, "PHYS 11.1: Reflection and transmission at steps and barriers": https://www.physics.brocku.ca/PPLATO/h-flap/phys11_1.html
- Academic treatment of paradoxical reflection: arXiv:0808.0610 (Goussev, "Paradoxical Reflection in Quantum Mechanics")

### A3. The rectangular barrier: tunneling and the transmission amplitude

**Explanation.** For a rectangular barrier of height V₀ and width L, with particle energy E < V₀ incident from the left, the exact transmission coefficient is:

T_exact = [1 + (V₀² sinh²(κL)) / (4E(V₀−E))]⁻¹

where κ = √(2m(V₀−E))/ℏ. In the thick-barrier limit κL ≫ 1, sinh(κL) ≈ exp(κL)/2, so:

T_exact ≈ [16E(V₀−E)/V₀²] · e^(−2κL)

The WKB approximation (from _lib_qmsri-11) gives T_WKB = e^(−2κL), recovering the exponential correctly but missing the smooth prefactor 16E(V₀−E)/V₀².

For E > V₀ (over-barrier): k₂ = √(2m(E−V₀))/ℏ, and the exact formula becomes T = [1 + (V₀² sin²(k₂L)) / (4E(E−V₀))]⁻¹. Resonances (T = 1) occur when k₂L = nπ, i.e., the barrier width equals an integer number of half-wavelengths.

**Common misconception.** Students believe tunneling "violates energy conservation" or that the particle has negative kinetic energy inside the barrier. Neither is true. The particle enters the barrier with total energy E; inside, the wave function is a real exponential, not an oscillatory solution — but this is a solution to the Schrödinger equation for a particle with energy E in a region where E < V. Energy is conserved. The particle simply has a non-zero probability amplitude in the classically forbidden region.

**Worked example.** Electron (mₑ = 9.109×10⁻³¹ kg), E = 1 eV, V₀ = 5 eV, L = 5 Å.
- κ = √(2mₑ×4 eV)/ℏ = √(2×9.109×10⁻³¹×4×1.6×10⁻¹⁹)/(1.055×10⁻³⁴) ≈ 1.026×10¹⁰ m⁻¹ ≈ 1.026 Å⁻¹
- κL = 1.026 × 5 = 5.13; sinh(5.13) ≈ 84.5; sinh²(κL) ≈ 7139
- T_exact = [1 + (25 × 7139)/(4×1×4)]⁻¹ = [1 + 11155]⁻¹ ≈ 8.96×10⁻⁵
- T_WKB = e^(−2×5.13) = e^(−10.26) ≈ 3.49×10⁻⁵
- Prefactor check: 16E(V₀−E)/V₀² = 16×1×4/25 = 2.56; T_exact/T_WKB ≈ 2.57. Consistent.

**Sources.**
- Wikipedia, "Rectangular potential barrier": https://en.wikipedia.org/wiki/Rectangular_potential_barrier (derivation section; reliable for this standard result)
- GMU PHYS 590 Study Guide on potential barrier: http://physics.gmu.edu/~dmaria/590%20Web%20Page/public_html/qm_topics/potential/barrier/STUDY-GUIDE.htm
- Griffiths, D.J., *Introduction to Quantum Mechanics*, §2.6 (canonical undergraduate source; formulae verified against _lib_qmsri-11)
- _lib_qmsri-11 (local): exact formula quoted at lines 106–110 of the source; WKB comparison at lines 109–110

### A4. Probability current as the basis for R and T

**Explanation.** R and T are defined via probability current J = (ℏ/m)·Im(ψ* dψ/dx), not via |amplitude|². For the potential step:

- J_inc = ℏk₀|A₀|²/m
- J_ref = ℏk₀|B₀|²/m (negative, moving left)
- J_trans = ℏk₁|A₁|²/m

R = |J_ref|/J_inc = |B₀/A₀|²; T = J_trans/J_inc = (k₁/k₀)|A₁/A₀|²

The factor k₁/k₀ in T is essential: the transmitted amplitude is NOT simply |A₁/A₀|², because probability current is proportional to both |ψ|² and to the particle's speed (∝ k). This is the most common single-step mistake in student calculations.

**Common misconception.** Writing T = |A₁/A₀|² rather than T = (k₁/k₀)|A₁/A₀|². Without the k ratio, R + T ≠ 1 for a step, which is an immediate flag.

**Worked example.** From the step derivation: A₁ = 2k₀/(k₀+k₁) · A₀. So |A₁/A₀|² = 4k₀²/(k₀+k₁)². Then T = (k₁/k₀)·4k₀²/(k₀+k₁)² = 4k₀k₁/(k₀+k₁)². R = (k₀−k₁)²/(k₀+k₁)². Verify R+T = [(k₀−k₁)²+4k₀k₁]/(k₀+k₁)² = (k₀+k₁)²/(k₀+k₁)² = 1. ✓

**Sources.**
- Walet 6.2 (as above): equations (6.9)–(6.15) give exact formulas with k₁/k₀ factor made explicit
- Fitzpatrick, "Introductory Quantum Mechanics," Ch. 2 (UT Austin): standard derivation via probability current

### A5. The finite number of bound states in a finite well

**Explanation.** The finite square well always has at least one bound state (a general result for symmetric 1D potentials). The total count is determined by how many times the graphical solution curves κ = k tan(kL/2) and κ = −k cot(kL/2) intersect. Each crossing represents one energy level. As V₀ increases, new levels emerge; each new even level appears before each new odd level. The condition for the n-th level to just appear (threshold) is approximately V₀·L² = n²π²ℏ²/(8m).

**Common misconception.** Students conflate the finite number of bound states with "the particle can escape." Even with a finite number of bound states, those that exist are genuinely bound — probability decays exponentially outside. The issue is that, unlike the infinite well, the parameter space (V₀, L) must be large enough to support a second, third, etc. level.

**Worked example.** Deuteron: proton-neutron system, m_reduced ≈ 938/2 MeV/c², V₀ ≈ 35 MeV, L ≈ 2 fm (nuclear range). Threshold condition for second bound state: V₀·L² ≥ 4π²ℏ²/(8m_reduced). Plugging numbers: the deuteron is just barely bound in a single l=0 state and has no l=0 excited state — consistent with experiment. This makes the finite square well directly relevant to nuclear physics.

**Sources.**
- ResearchGate: "Solving the Schrödinger Equation for a Finite Square Well: Application to Deuteron Bound State Energy" (2024): https://www.researchgate.net/publication/384764182
- Herman UNCW lecture notes (as above)

---

## B. Domain examples and cases

**Scanning Tunneling Microscope (STM).** A metal tip is held ~4–6 Å above a conducting surface. Electrons tunnel through the vacuum gap (barrier height ≈ work function ~4–5 eV). The tunneling current I ∝ e^(−2κd); when d changes by 1 Å, I changes by a factor of e² ≈ 7. This exponential transduction makes sub-angstrom height resolution possible. Reference: Binnig & Rohrer, PRL 49, 57 (1982) — Nobel Prize 1986.

**Alpha decay (connection to WKB).** The Coulomb barrier in heavy nuclei is a non-rectangular barrier; the exact T_WKB formula requires integrating κ(r) = √(2m(V(r)−E))/ℏ over the classically forbidden region (Gamow factor). The rectangular barrier exact formula is the pedagogical entry point; the WKB generalization is developed fully in _lib_qmsri-11 and will be Chapter 11 in this textbook.

**Flash memory (Fowler-Nordheim tunneling).** Writing a bit in flash memory drives electrons through a thin (~10 nm) SiO₂ gate oxide by applying a large electric field, which tilts the rectangular-ish oxide barrier into a triangular shape. The triangular-barrier Gamow factor governs write speed and data retention time. This is the same physics as the rectangular barrier, but with a linearly varying V(x) instead of constant V₀.

**Resonant tunneling diode (double-barrier).** When two barriers sandwich a quantum well, resonant tunneling occurs: T → 1 at discrete energies where the well supports a quasi-bound state. This is the quantum dot / resonant tunneling diode architecture. The effect is not covered in this chapter (Chapter 6) but is a natural extension visible in the simulation.

**Nuclear fusion in stars.** Proton-proton fusion at solar-core temperatures (~1 keV) requires tunneling through the Coulomb barrier (~1 MeV). The Gamow peak — where the thermal Boltzmann factor and the tunneling suppression together are maximized — determines where fusion occurs. Again, exact rectangular-barrier formula provides the conceptual scaffold; Coulomb-barrier case is in _lib_qmsri-11.

---

## C. Connections and dependencies

**Prerequisite chapters (within this textbook):**
- Ch 1 (wave function, Born rule, probability current): the definition J = (ℏ/m)Im(ψ* ∂ψ/∂x) is used to define R and T.
- Ch 2–3 (TISE, infinite square well, finite well boundary conditions): the matching procedure at a discontinuity in V is introduced here.
- Ch 5 (infinite square well): transcendental vs. closed-form energy levels contrast.

**Forward connections:**
- Ch 8 (free particle, wave packets): the plane-wave solutions used here as incoming waves are non-normalizable for the same reason as in Ch 8; the scattering setup is the stationary approximation to a wave packet problem.
- Ch 11 in the QMSRI source (_lib_qmsri-11, future Ch 11 of this textbook): WKB generalizes the rectangular-barrier exponential suppression to arbitrary V(x). The Gamow factor γ = ∫κ dx recovers T_WKB = e^(−2κL) for rectangular barriers as a special case.
- Ch 9+ (hydrogen atom, 3D wells): bound-state counting in spherical wells is the 3D analog.

**Mathematical prerequisites:**
- Ordinary differential equations (matching conditions)
- Hyperbolic functions (sinh, cosh for sub-barrier)
- Probability current definition (from Ch 1)

---

## D. Current state of the field

**Settled.**
- The exact formulae for R, T for the step and rectangular barrier are textbook-settled since the 1920s. No controversy.
- The finite square well transcendental equation and its graphical/numerical solution are completely established.
- The connection to WKB (T_WKB = e^(−2γ) as the thick-barrier limit of T_exact) is settled; see Griffiths §9.3 and _lib_qmsri-11.

**Contested / active.**
- Tunneling time: at least four competing definitions (dwell time, phase time, Büttiker-Landauer time, Larmor clock time) give different answers and the question of which is "the" tunneling time remains open. Recent attosecond-streaking experiments (e.g., Eckle et al., Science 2008; Satya Sainadh et al., Nature 2019) measure "something" but the theoretical interpretation is debated. This chapter should note the issue without pretending to resolve it. See _lib_qmsri-11 "Still puzzling" section.
- Superluminal tunneling claims: some experiments report apparent group velocities exceeding c in tunneling. This is an artifact of pulse reshaping, not signal transmission; settled in the quantum information community but still generates popular-press confusion.

**Key references.**
- Griffiths, D.J., *Introduction to Quantum Mechanics*, 3rd ed., §2.5–2.6 (finite well), §2.7 (free particle/scattering)
- Bohm, D., *Quantum Theory* (1951), Ch. 11: early clean treatment
- Walet, N., *Quantum Mechanics* (Manchester): §6.2–6.3 (source used in this notes file)
- Wikipedia, "Rectangular potential barrier" — reliable derivation, spot-checked against _lib_qmsri-11 formulae

**Recent developments (pedagogical).**
- Simulation-based pedagogy for the step and barrier is now standard; PhET "Quantum Tunneling" simulation is widely used. For this textbook's simulation-first approach, the deliverable is a Crank-Nicolson wave-packet simulation layered on top of the analytic stationary results.

---

## E. Teaching considerations

**Ordering.** The QMSRI-11 source (WKB) treats tunneling from the WKB angle first. For this textbook's Chapter 6, the ordering is reversed: exact rectangular barrier first (clean algebra, exact formula), then WKB as approximation in Ch 11. This is pedagogically better for undergraduates: exact before approximate.

**Simulation first.** The chapter should begin with a simulation that shows: (a) a wave packet hitting a step and partially reflecting, (b) varying E from below V₀ to above V₀ and watching R drop and T rise, (c) varying L for the barrier and watching T change exponentially. The analytic derivation then explains what the student has already seen.

**Biggest teaching traps.**
1. The k ratio in T = (k₁/k₀)|A₁/A₀|²: must be derived from probability current, not just amplitude.
2. Reflection from a step when E > V₀: counterintuitive; needs emphasis.
3. Tunneling does not violate energy conservation: the evanescent wave is a solution with energy E, not a particle borrowing energy.
4. Finite vs. infinite number of bound states: make graphical solution the primary tool.

**Worked problems to assign.**
- Numerical: given V₀, L, E, compute T_exact and T_WKB for an electron; compare ratio to 16E(V₀−E)/V₀².
- Graphical: plot the transcendental equation for the finite well and count bound states as V₀ increases from 0 to 5× threshold.
- Conceptual: explain why R + T = 1 is a consequence of probability current conservation, not an additional assumption.

**Simulation deliverable (Chapter 6).** Single HTML file with: (1) stationary T(E) plot (exact + WKB on log y-axis); (2) wave-function profile showing oscillatory/evanescent regions; (3) animated Gaussian wave packet hitting the barrier (Crank-Nicolson, same physics as _lib_qmsri-11 Mode C). Parameters: V₀, L sliders; E/energy slider or momentum slider.

---

## F. Library files relevant to this chapter

- **`_lib_qmsri-11-the-wkb-approximation-and-tunneling.md`** (primary): The exact rectangular-barrier T formula is quoted at lines 106–110; WKB Gamow factor at lines 98–104; Crank-Nicolson simulation spec (Mode C) at lines 237–395. This library file is the main technical source for the barrier physics and simulation architecture.
- **`_lib_qmsri-01-the-wave-function.md`**: Probability current definition (lines 103–106), normalization and continuity equation. Needed for the R + T = 1 derivation.
- **`_lib_qmsri-02-the-time-independent-schrodinger-equation.md`** (not read, but referenced in outline): Infinite square well boundary conditions; the finite well is the direct extension.

---

## G. Gaps and flags

1. **Deuteron application:** The transcendental equation applied to the deuteron (proton-neutron bound state) would be a compelling physics example. Needs nuclear radius and effective potential depth checked against current nuclear data (nuclear radius ≈ 1.2 A^(1/3) fm formula). The ResearchGate 2024 paper on this specific application should be fetched and verified before writing.

2. **Exact T formula sign check for E > V₀:** The formula switches from sinh to sin; students often apply the E < V₀ formula when E > V₀. The chapter must clearly box both cases separately.

3. **Tunneling time:** This chapter should note the open problem (see _lib_qmsri-11 "Still puzzling") without resolving it. Do not assign a specific tunneling time in exercises.

4. **R + T = 1 proof:** Should be done explicitly, deriving it from J_inc = J_ref + J_trans, not just stated. This is a synthesis exercise.

5. **Connection to Ch 8:** The stationary scattering solutions (plane waves in each region) are "not normalizable" for the same reason the free-particle plane wave is not normalizable (Ch 8). A brief forward pointer is appropriate.

6. **Simulation spec:** The Crank-Nicolson simulation architecture from _lib_qmsri-11 (Mode C, lines 237–395) should be adapted directly for this chapter's simulation. Key parameters: 500 spatial grid points, absorbing boundaries, Thomas tridiagonal solve. Do not re-derive; cite the library file.
