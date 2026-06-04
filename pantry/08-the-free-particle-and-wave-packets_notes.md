# Research Notes: Chapter 08 — The Free Particle and Wave Packets

**Corresponding chapter:** chapters/08-the-free-particle-and-wave-packets.md (not yet written)
**Generated:** 2026-06-03

---

## Chapter summary (capability built)

By the end of this chapter the student can: (1) write the free-particle plane-wave solution e^{i(kx−ωt)} and explain why it cannot be normalized on (−∞, ∞); (2) build a normalizable wave packet by Fourier superposition and explain what φ(k) represents; (3) derive phase velocity v_ph = ω/k and group velocity v_g = dω/dk for the free-particle dispersion relation ω = ℏk²/2m, and show v_g = 2v_ph; (4) state and apply the Gaussian packet spreading formula σ_x(t)² = σ_x(0)² + (ℏt/2mσ_x(0))²; (5) compute the spreading time for a given initial width; (6) run a simulation that assembles a wave packet from its Fourier components and shows the packet propagate, spread, and preserve the σ_xσ_p = ℏ/2 equality at t = 0 while σ_xσ_p grows with t.

---

## A. Conceptual foundations

### A1. Plane waves are non-normalizable; the wave packet resolves this

**Explanation.** The free-particle TISE has solutions ψ_k(x) = A e^{ikx} with energy E = ℏ²k²/2m for any real k. The full time-dependent solution is:

Ψ_k(x,t) = A e^{i(kx − ωt)}, ω = ℏk²/2m

The probability density is |Ψ_k|² = |A|² — constant everywhere, independent of x and t. The integral ∫|Ψ_k|²dx diverges for any non-zero A. Plane waves cannot satisfy the normalization condition ∫|ψ|²dx = 1.

This is not a mathematical accident. A plane wave with definite momentum p = ℏk has σ_p = 0, so by the uncertainty principle σ_x = ∞. A particle with perfectly definite momentum is completely delocalized in position — it cannot be localized at all. The non-normalizability is the mathematical statement of this physical fact.

The resolution: build a wave packet by superposing plane waves with a range of k values:

Ψ(x,t) = (1/√2π) ∫ φ(k) e^{i(kx − ω(k)t)} dk

where φ(k) is the Fourier amplitude. If φ(k) is localized (e.g., a Gaussian centered at k₀ with width Δk), then Ψ(x,t) is normalizable and localized. φ(k) is the momentum-space wave function: |φ(k)|² is the probability density for finding momentum p = ℏk.

**Common misconception.** Students often think plane waves are unphysical and therefore unimportant. In fact, plane waves are the eigenstates of the free-particle Hamiltonian; the wave packet is the physical superposition, and the plane waves are the basis. The machinery of Fourier decomposition is central to everything — wave packets in scattering, Bloch waves in crystals, Green's functions. The correct view is: plane waves are indispensable mathematical building blocks, but not physical states on their own.

**Worked example.** Square packet: φ(k) = 1/√(2Δk) for |k − k₀| < Δk, else 0. Then:

Ψ(x,0) = (1/√2π) · (1/√(2Δk)) · ∫_{k₀−Δk}^{k₀+Δk} e^{ikx} dk = (1/√π) · (sinc(Δk·x)/√Δk) · e^{ik₀x}

The sinc envelope has width ~1/Δk, and the product Δx · Δk ~ π, consistent with σ_x · σ_p ≥ ℏ/2 (the sinc packet does not saturate the bound; the Gaussian does).

**Sources.**
- Likharev, K.K., "2.2: Free Particle - Wave Packets," *Essential Graduate Physics QM* (Stony Brook), Physics LibreTexts: https://phys.libretexts.org/Bookshelves/Quantum_Mechanics/Essential_Graduate_Physics_-_Quantum_Mechanics_(Likharev)/02:_1D_Wave_Mechanics/2.02:_Free_Particle-_Wave_Packets (verified: full derivation including propagator, group velocity, spreading formula)
- Walet, N., "6.1: Non-normalizable Wavefunctions," *Quantum Mechanics* (Manchester), Physics LibreTexts: same textbook as used for Ch 6 potential step material
- Fitzpatrick, R., "2.11: Evolution of Wave-Packets," *Introductory QM* (UT Austin), Physics LibreTexts: https://phys.libretexts.org/Bookshelves/Quantum_Mechanics/Introductory_Quantum_Mechanics_(Fitzpatrick)/02:_Wave-Particle_Duality/2.11:_Evolution_of_Wave-Packets (verified: full Taylor-expansion derivation of σ(t))
- _lib_qmsri-01-the-wave-function.md (local): plane wave discussed at the end of exercises (lines 394–399) as Ch 1's "challenge" problem; this chapter resolves that challenge

### A2. Phase velocity vs. group velocity; v_g = 2v_ph for a free particle

**Explanation.** A plane wave e^{i(kx−ωt)} has a fixed-phase surface at x = ωt/k + const, moving at:

v_ph = ω/k (phase velocity)

For the free particle: ω = ℏk²/2m, so v_ph = ℏk/2m = p/2m. This is half the classical particle velocity.

The wave packet as a whole moves at the group velocity:

v_g = dω/dk|_{k=k₀} = ℏk₀/m = p₀/m

For the free particle: v_g = ℏk/m = p/m. This is the classical particle velocity. Good.

The ratio: v_g/v_ph = 2. Group velocity is exactly twice phase velocity for a free non-relativistic particle.

This has a physical interpretation: the phase of the carrier oscillation advances at v_ph; the envelope (the probability density peak) moves at v_g = 2v_ph. If you watch a wave packet moving to the right, the individual oscillations inside the envelope appear to travel twice as fast as the envelope itself. This is visible in simulation and counterintuitive.

**Common misconception.** Students often think the particle "travels at the phase velocity." It does not. The phase velocity is the speed of the wavefronts (lines of constant phase); it has no direct physical meaning for particle motion. The group velocity equals the classical particle velocity and is the physically meaningful speed. For light in vacuum, ω = ck so v_ph = v_g = c (no dispersion). For matter waves, ω ∝ k² so v_g ≠ v_ph.

**Worked example.** Electron with kinetic energy E = 1 eV. Momentum p = √(2mₑE) = √(2 × 9.109×10⁻³¹ × 1.6×10⁻¹⁹) ≈ 5.40×10⁻²⁵ kg·m/s. Classical velocity v₀ = p/mₑ ≈ 5.93×10⁵ m/s ≈ 0.002c. Wave number k₀ = p/ℏ ≈ 5.12×10⁹ m⁻¹. Group velocity v_g = ℏk₀/mₑ = p/mₑ ≈ 5.93×10⁵ m/s. ✓ Phase velocity v_ph = ω/k₀ = ℏk₀/2mₑ ≈ 2.97×10⁵ m/s — half v_g. ✓

**Sources.**
- Fitzpatrick 2.11 (verified above): Equations for v_gr and v_ph explicitly derived; v_gr = p/m, v_ph = ω/k₀ = p/2m for de Broglie waves
- Likharev 2.2 (verified above): Equations (2.33) give v_gr = v₀ (classical), v_ph = v_gr/2
- Harvard lecture notes: Schwartz, M., "Lecture 11: Wavepackets and Dispersion" (Harvard Physics): https://scholar.harvard.edu/files/schwartz/files/lecture11-wavepackets.pdf (covers phase vs group velocity clearly)
- GWU: "Gaussian Wave Packet in Free Space": https://blogs.gwu.edu/doring/gaussian-wave-packet-in-free-space/
- UVA Galileo & Einstein: "50. Group Velocity and Wave Packet Spread": https://galileoandeinstein.phys.virginia.edu/Elec_Mag/2022_Lectures/EM_50_Group_Velocity.html

### A3. Dispersion and wave packet spreading; the Gaussian packet

**Explanation.** Dispersion means ω(k) is not linear in k. The free-particle dispersion relation ω = ℏk²/2m has d²ω/dk² = ℏ/m ≠ 0. This means different Fourier components travel at different group velocities (dω/dk depends on k), so the packet spreads.

For an initially Gaussian wave packet with width σ_x(0) = δx:

φ(k) ∝ exp{−(k−k₀)² / (2δk)²}, with δk = 1/(2δx)  [the uncertainty relation saturated at t=0]

The exact time evolution gives (Fitzpatrick 2.11, Equation for σ²(t)):

σ_x(t)² = (δx)² + (α²t² / (4(δx)²))

where α = d²ω/dk²|_{k₀} = ℏ/m for de Broglie waves. Therefore:

σ_x(t)² = (δx)² + (ℏt / 2mδx)²

or equivalently (Likharev form):

(δx')² = (δx)² + (ℏt/2m)² / (δx)²

The packet remains Gaussian at all times. The probability density is:

|Ψ(x,t)|² ∝ (1/σ(t)) exp{−(x − x₀ − v_g t)² / (2σ_x(t)²)}

A Gaussian centered at x₀ + v_g t, moving at the group velocity, with width growing in time.

Key properties:
- σ_p = ℏδk = ℏ/(2δx) is constant: the momentum distribution does not spread (φ(k) is time-independent up to a phase).
- σ_x grows: the packet spreads spatially.
- σ_x(t) · σ_p > ℏ/2 for t > 0: the packet ceases to be a minimum-uncertainty state as it spreads.

**Common misconception.** Students think "the uncertainty principle forces spreading." This conflates two things. The uncertainty principle says σ_xσ_p ≥ ℏ/2 at any instant; it does not say σ_x must grow. An HO coherent state (Ch 7) has σ_x constant at all times despite being a quantum state. Spreading is a consequence of dispersion (d²ω/dk² ≠ 0), not of the uncertainty principle itself. A free particle spreads because its dispersion is quadratic. A light pulse in vacuum does not spread because ω = ck is linear (d²ω/dk² = 0).

**Worked example (doubling time).** Electron initially localized to δx = 1 Å (atomic scale). Doubling time:

t_2 ~ m(δx)² / ℏ = (9.109×10⁻³¹ kg × (10⁻¹⁰ m)²) / (1.055×10⁻³⁴ J·s) ≈ 8.6×10⁻¹⁷ s

About 86 attoseconds. An electron localized to atomic dimensions spreads to twice that width in under 100 as. In contrast, a 1 mg grain of sand localized to 1 μm: t_2 ~ 10⁻³ × 10⁻¹² / 10⁻³⁴ ~ 10¹⁹ s — far longer than the age of the universe. Quantum spreading is only measurable for quantum-scale particles.

**Sources.**
- Fitzpatrick 2.11 (verified): Equations for σ²(t) (the key formula derived fully); doubling time t_2 ~ m(Δx)²/ℏ stated explicitly; atomic electron example: "the doubling time is only about 10⁻¹⁶ s"
- Likharev 2.2 (verified): Equations (2.39)–(2.40), spreading formula in the form (δx')² = (δx)² + (ℏt/2m)²/(δx)²; discussion of optimal initial width; electron example: 1 cm after 1 second
- Pramana article: "Understanding the spreading of a Gaussian wave packet," IAS: https://www.ias.ac.in/article/fulltext/pram/074/06/0867-0874
- arXiv:2403.13857: "Simulation of Gaussian Wave Packets used to Illustrate Elementary Quantum Mechanics Scenarios" (2024): recent pedagogical simulation paper

### A4. The free-particle propagator and the Fourier decomposition as a superposition principle

**Explanation.** The solution to the free-particle TISE with arbitrary initial conditions Ψ(x,0) is obtained by:
1. Fourier-transform to get φ(k) = (1/√2π) ∫ Ψ(x,0) e^{−ikx} dx
2. Attach time-evolution phases: Ψ(x,t) = (1/√2π) ∫ φ(k) e^{i(kx − ℏk²t/2m)} dk

This integral is the exact solution for any φ(k). For a Gaussian φ(k), it evaluates analytically to the spreading Gaussian above.

The propagator G(x,t;x₀,0) = (m/2πiℏt)^{1/2} exp{−m(x−x₀)²/(2iℏt)} (Likharev 2.2, equation (2.49)) is the Green's function of the free Schrödinger equation — the wave function of a particle initially at x₀. Its spreading ∝ t^{1/2} is mathematically identical to classical diffusion (but the diffusion coefficient is imaginary, giving oscillatory rather than dissipative behavior).

**Common misconception.** Students sometimes think the Fourier integral decomposition is an approximation. It is exact for the free particle (ω = ℏk²/2m is quadratic in k, so the Taylor expansion around k₀ terminates at second order — Likharev footnote 8). For a general potential V(x), the decomposition into energy eigenstates is still exact in principle but computationally more complex.

**Worked example.** Verify that for a Gaussian φ(k) ∝ exp{−(k−k₀)²/4δk²}, the time-evolved wave function is:

Ψ(x,t) ∝ exp{i(k₀x − ω₀t)} · exp{−(x − v_g t)² / (4Δ(t))}

where Δ(t) = (δx)² + i(ℏt/2m), a complex time-dependent width. The real part gives the spreading; the imaginary part gives an additional phase chirp (which does not affect |Ψ|² but shows up in the phase structure visible in simulation).

**Sources.**
- Likharev 2.2 (verified): Full derivation of Gaussian wave packet evolution (equations 2.26–2.40), propagator G (equations 2.47–2.49), Gaussian integral completion method
- Fitzpatrick 2.11 (verified): Taylor expansion of phase φ(k) around k₀ to second order; exact integration for Gaussian; σ²(t) formula

### A5. The stationary phase approximation and wave packet group velocity as a general principle

**Explanation.** The group velocity formula v_g = dω/dk is not specific to the free particle. For any dispersion relation ω(k), the packet envelope moves at v_g = dω/dk evaluated at the peak k₀ of φ(k). This is derived from the stationary-phase approximation (where the phase k·x − ω(k)·t is stationary with respect to k at the packet's center):

d/dk [kx − ω(k)t]|_{k=k₀} = 0 → x = (dω/dk)|_{k₀} · t → x/t = v_g

Spreading is controlled by d²ω/dk² (the second derivative, which makes different k-components move at different group velocities). For the free particle d²ω/dk² = ℏ/m. For light in glass (normal dispersion), d²ω/dk² > 0 — pulse broadening in optical fibers. For anomalous dispersion, d²ω/dk² < 0 — pulse compression.

**Common misconception.** Students think group velocity is always the signal velocity or the energy transport velocity. For anomalous dispersion near absorption resonances, the group velocity can exceed c or become negative; in those cases the group velocity is not the signal velocity. For the free-particle case covered here, the group velocity equals the classical particle velocity and is unambiguously the physically correct speed.

**Sources.**
- Fitzpatrick 2.11 (verified): stationary phase argument explicit; Taylor expansion to second order
- Likharev 2.2 (verified): same argument, eq. (2.32); v_ph and v_gr explicitly compared
- UBC Physics 200 notes: "Group Velocity and Phase Velocity": https://phas.ubc.ca/~mav/p200/groupandphase.pdf
- UVA lecture (verified above): group velocity and dispersion with worked examples

---

## B. Domain examples and cases

**Electron microscopy.** An electron beam in a TEM has a de Broglie wavelength λ = h/p. At 100 keV, λ ≈ 3.7 pm — smaller than atomic diameters. The beam is a highly collimated wave packet with very small Δx/x but finite Δk. Chromatic aberration (energy spread → spread in k → wave-packet spreading during transit through the column) limits resolution. Understanding packet spreading is directly relevant to EM instrument design.

**Neutron interferometry.** Cold neutrons (energy ~25 meV, λ ~ 1.8 Å) have de Broglie wave packets coherent over ~10 cm (long coherence length due to narrow energy selection). The COW experiment (Collella, Overhauser, Werner, 1975) observed gravitational phase shifts in neutron interferometry — the wave packet is large enough to be in a gravitational potential gradient. Packet spreading is negligible over the transit time (milliseconds); the coherence length is the relevant scale.

**Ultrafast laser pulses.** A 10 fs laser pulse at 800 nm has Δλ/λ ~ 0.05, so Δk/k ~ 0.05 and the pulse is bandwidth-limited. In glass (normal dispersion), group velocity dispersion (GVD = d²ω/dk²) spreads the pulse. The spreading formula is formally identical to the quantum mechanical one: σ_t(z)² = σ_t(0)² + (GVD·z/σ_t(0))² — an optical fiber is the quantum free-particle situation scaled to optical parameters.

**Quantum dots and confined electrons.** An electron confined to a quantum dot of diameter ~10 nm has σ_x ~ 5 nm. Its momentum spread σ_p ~ ℏ/(2·5 nm) ≈ 10⁻²⁶ kg·m/s. If the confining potential is removed, the wave packet spreads on a timescale t_2 ~ mσ_x²/ℏ ~ 9×10⁻³¹ × (5×10⁻⁹)² / 10⁻³⁴ ≈ 2×10⁻¹³ s ~ 200 fs. Measurable with ultrafast spectroscopy.

**Wave packets in nuclear physics.** An alpha particle emitted in alpha decay starts as a wave packet localized inside the nucleus (radius ~10 fm). After tunneling through the Coulomb barrier (Ch 6 and 11), it propagates as a free-particle wave packet that spreads as it moves away from the nucleus. The spreading time at nuclear scales is ~10⁻²⁰ s, essentially instantaneous on any macroscopic scale — the detected particle is effectively a classical projectile long before reaching the detector.

---

## C. Connections and dependencies

**Prerequisite chapters:**
- Ch 1 (wave function, Born rule, probability current, Fourier duality of x and p, uncertainty principle as σ_xσ_p ≥ ℏ/2 from the Gaussian)
- Ch 2–3 (TISE, separation of variables)
- Ch 5 (momentum operator, plane waves as eigenstates of p̂)
- Ch 6 (scattering: plane waves used as incoming states; wave packet as the physical realization of that scattering setup)

**Forward connections:**
- Ch 7 (harmonic oscillator coherent states): the coherent state is a Gaussian wave packet that does NOT spread — contrast with the free-particle case here. Both start as Gaussians; the presence of the restoring force prevents spreading in the oscillator.
- Ch 9+ (3D quantum mechanics, angular momentum): wave packets in 3D have the same Gaussian spreading; the group velocity formula generalizes.
- Crank-Nicolson simulation (Ch 6 and 11): the wave-packet simulation of scattering uses the same packet construction. Ch 8 provides the free-particle reference against which to check that the CN solver conserves norm in the absence of a potential.

**Mathematical dependencies:**
- Fourier transforms (key tool throughout)
- Gaussian integrals (completing the square)
- Taylor expansion of ω(k) around k₀
- Complex exponentials

---

## D. Current state of the field

**Completely settled.**
- The free-particle wave packet theory (Fourier decomposition, group velocity, spreading formula) is textbook-settled since Schrödinger (1926) and Darwin (1927). No controversy.
- The phase vs. group velocity distinction for matter waves is settled; v_g = p/m (classical) and v_ph = p/2m (non-classical).
- The Gaussian spreading formula σ(t)² = σ(0)² + (ℏt/2mσ(0))² is exact for the free particle (not an approximation).

**Open / interesting pedagogical question.**
- Is spreading inevitable? For free particles, yes. But arXiv:1209.0711 ("Is the Spreading of Quantum Mechanical Wave Packets Indeed Inevitable?") discusses systems (e.g., with specific potentials) where spreading can be suppressed or reversed. This is beyond undergraduate scope but worth a footnote.

**Key references.**
- Fitzpatrick, R., "2.11: Evolution of Wave-Packets," *Introductory QM* (UT Austin): primary source for Taylor-expansion derivation and σ(t) formula — verified against this research file
- Likharev, K.K., "2.2: Free Particle - Wave Packets," *Essential Graduate Physics QM*: primary source for propagator, Gaussian integral completion, spreading formula — verified
- Griffiths, D.J., *Introduction to Quantum Mechanics*, §2.4: same material, standard reference
- Schwartz, M., Harvard Physics 253b Lecture 11: "Wavepackets and Dispersion" — concise, correct
- Darwin, C.G., Proc. R. Soc. A 117, 258 (1927): original wave-packet spreading calculation for an electron

---

## E. Teaching considerations

**Ordering within the chapter.** Start with the non-normalizability of the plane wave (connecting to Ch 1's challenge problem, _lib_qmsri-01 lines 394–399). Introduce φ(k) as the Fourier amplitude and show normalizability of the packet. Then derive group vs. phase velocity from first principles. Then give the spreading formula — derive it for the Gaussian, state it as a result for general narrow φ(k). Close with worked numerical examples.

**Simulation deliverable.** Build a JavaScript/D3 simulation that:
1. Shows a Gaussian wave packet |Ψ(x,t)|² moving and spreading over time.
2. Allows σ_x(0), k₀ sliders.
3. Plots σ_x(t) vs. t alongside the analytic formula √((δx)² + (ℏt/2mδx)²).
4. Shows the momentum-space profile |φ(k)|² — static (does not spread).
5. Displays σ_xσ_p/( ℏ/2) — equals 1 at t = 0, grows with t.
6. Shows the carrier oscillation inside the envelope at frequency ω = ℏk₀²/2m; visible that it moves at v_ph = ω/k₀ while the envelope moves at v_g = 2v_ph.

The simulation from Ch 1 (_lib_qmsri-01's "01-probability-explorer.html") showed static wave functions. This chapter's simulation adds time evolution — the logical next step.

**Biggest teaching traps.**
1. "Group velocity = signal velocity always": false for anomalous dispersion; but true for free particle and should be stated carefully.
2. "Spreading is caused by the uncertainty principle": spreading is caused by dispersion (d²ω/dk² ≠ 0). The uncertainty principle says σ_xσ_p ≥ ℏ/2 at all times but does not say σ_x must increase.
3. "The momentum distribution spreads too": it does not. φ(k) is time-independent (up to a phase); |φ(k)|² is constant. Only the position-space wave function spreads.
4. "A plane wave travels at v_ph = ℏk/2m — so the particle moves at half its classical velocity": the plane wave is not a localized particle. The particle (wave packet) moves at v_g = ℏk/m = classical velocity.
5. "Non-normalizable means non-physical": plane waves are essential mathematical tools (eigenstates of p̂) even though they are not normalizable. The wave packet is physical; the plane wave is a basis element.

**Key exercises.**
- Given σ_x(0) = 1 Å and m = mₑ: compute σ_x at t = 10⁻¹⁶ s. How does this compare to the atomic diameter?
- Show that v_g = 2v_ph for the free particle and explain what this means for the visual appearance of the packet in simulation.
- A Gaussian packet has σ_xσ_p = ℏ/2 at t = 0. At what time t* has σ_x doubled? Express t* in terms of m, ℏ, σ_x(0). (Answer: t* = √3·mσ_x(0)²/ℏ.)
- In a simulation, set k₀ large (fast packet) and σ_x small (wide momentum spread). Observe rapid spreading. Then set σ_x large (narrow momentum spread). Observe slow spreading. Explain why.

**Connection to Ch 7.** The critical contrast: in Ch 7, a coherent-state Gaussian does not spread (the HO potential creates a restoring force that cancels the free-particle spreading). Placing the Ch 7 simulation and Ch 8 simulation side by side makes this concrete.

---

## F. Library files relevant to this chapter

- **`_lib_qmsri-01-the-wave-function.md`** (primary local source):
  - "The Gaussian saturates the bound" section (lines 172–201): the Gaussian wave packet is introduced with σ_x = a/√2 and σ_p = ℏ/(√2 a), deriving σ_xσ_p = ℏ/2. This is the t = 0 initial condition for the Ch 8 spreading.
  - Exercise 10 (lines 394–399): challenge problem asking about the non-normalizability of e^{ikx} and proposing "wave packets as building blocks" — Ch 8 resolves this.
  - LLM Exercise Part D (lines 335–355): time slider for free-particle evolution of a Gaussian — the Ch 8 simulation extends this to full spreading visualization.
  - Momentum-space panel from _lib_qmsri-01's extension (lines 335–355): |φ(p)|² static for Gaussian — Ch 8 uses this explicitly.

- **`_lib_qmsri-03-the-harmonic-oscillator.md`**: Coherent states (lines 197–219) provide the contrast case: a Gaussian that rides the classical orbit without spreading. The comparison between free-particle Gaussian (spreads) and coherent-state Gaussian (doesn't) is the key pedagogical contrast between Ch 8 and Ch 7.

---

## G. Gaps and flags

1. **Relativistic corrections.** The chapter covers non-relativistic free particle (ω = ℏk²/2m). For electrons at energies above ~10 keV, the relativistic dispersion ω = √(m²c⁴ + ℏ²k²c²)/ℏ − mc²/ℏ becomes relevant. This is beyond Vol 1 scope but should be flagged in a footnote.

2. **3D wave packets.** The chapter treats 1D. The 3D free-particle wave packet is a direct product of three 1D Gaussians, each spreading independently. The spreading formula applies per dimension. Flag this as an extension without full derivation.

3. **Propagator / Green's function.** Likharev 2.2 derives the free-particle propagator G(x,t;x₀,0) = (m/2πiℏt)^{1/2} exp{−m(x−x₀)²/(2iℏt)} as the "kernel" connecting initial to final wave function. This is a beautiful result (structural analog of diffusion Green's function) but may be beyond the level of a foundations Ch 8. Include as "optional depth."

4. **Spreading formula derivation.** The exact derivation (complete the square in the Gaussian integral) is available in both Fitzpatrick 2.11 and Likharev 2.2 (verified). The chapter should include the full derivation, not just state the formula, because the technique (Gaussian integral with complex exponent) recurs throughout QM.

5. **Optimal width.** Likharev derives that for a given propagation time t, there is an optimal initial width (δx)_opt = √(ℏt/m) that minimizes the final width. This is a nice insight but secondary.

6. **Simulation tech note.** The free-particle time evolution can be computed exactly by FFT: φ(k) × exp(−iℏk²t/2m) then inverse FFT. This is exact (no Crank-Nicolson approximation needed for the free particle), and much faster than CN. The simulation deliverable for Ch 8 should use FFT time evolution; the CN solver is reserved for Ch 6 and 11 where V(x) ≠ 0. This should be specified in the chapter's CLAUDE.md physics rules.

7. **The "paradox" of v_ph < classical velocity.** The phase velocity v_ph = p/2m is less than the classical velocity v_cl = p/m. A naive reading suggests the wave is "slower than the particle." The resolution is that the particle's motion corresponds to the envelope (group velocity), not the phase. This deserves a dedicated paragraph.
