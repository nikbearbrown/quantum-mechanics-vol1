# Research Notes: Chapter 10 — Measurement and the Qubit

**Corresponding chapter:** chapters/10-measurement-and-the-qubit.md (not yet written)
**Generated:** 2026-06-03

---

## Chapter summary (capability built)

By the end of this chapter, students can: state the measurement postulate precisely (outcomes = eigenvalues; probability = |⟨aₙ|ψ⟩|²; post-measurement collapse to |aₙ⟩); apply it to a two-state system to predict full measurement statistics; compute the Bloch vector for any qubit state; and connect the abstract formalism to the concrete Stern-Gerlach / spin-½ experiment.

---

## A. Conceptual foundations

### The measurement postulate (three-part statement)

For a Hermitian observable Â with eigenstates {|aₙ⟩} and eigenvalues {aₙ}:

1. **Outcomes are eigenvalues.** A measurement of Â can only return one of the eigenvalues aₙ — nothing else.
2. **Born rule.** The probability of getting outcome aₙ, when the system is in state |ψ⟩, is:
     P(aₙ) = |⟨aₙ|ψ⟩|²
3. **Collapse (state update).** Immediately after measurement returns aₙ, the state is |aₙ⟩ (or the projection onto the degenerate subspace if aₙ is degenerate).

The Born rule is stated geometrically: P(aₙ) is the squared magnitude of the projection of |ψ⟩ onto the eigenket |aₙ⟩. This unifies all probability calculations under one formula.

Source: _lib_qmsri-04, §"Operators and Hermiticity" (spectral theorem and Born rule); §"Commutators and why they matter."

### The two-state system — why it is the right starting point

A qubit is the simplest non-trivial quantum system: two-dimensional Hilbert space, two possible measurement outcomes, all probability calculations done with 2×2 matrices and 2-component complex vectors. It is rich enough to exhibit:

- Superposition
- Interference (via the phase φ)
- Measurement collapse
- Non-commuting observables and their uncertainty relations
- Time evolution as unitary rotation (Larmor precession)

...and every calculation is doable by hand. The qubit is the pedagogical anchor before the formalism is applied to the full infinite-dimensional wave-function case.

Source: _lib_qmsri-04, §"The qubit."

### State parametrization and the Bloch sphere

Every normalized pure qubit state is:

  |ψ⟩ = cos(θ/2)|0⟩ + e^{iφ} sin(θ/2)|1⟩,   θ ∈ [0,π], φ ∈ [0, 2π)

Two real parameters — every state of a qubit lives on a sphere (the Bloch sphere). The factor of θ/2 (not θ) is mandatory: it ensures the state space double-covers the sphere (spinor double cover of SO(3)).

The Bloch vector:
  r = (⟨σ_x⟩, ⟨σ_y⟩, ⟨σ_z⟩) = (sin θ cos φ, sin θ sin φ, cos θ)

For pure states |r|² = 1 exactly (runtime sanity check: |r|² within 1e-6 of 1).

Pauli matrices (verify signs at startup — common LLM failure):
  σ_x = [[0,1],[1,0]],  σ_y = [[0,−i],[i,0]],  σ_z = [[1,0],[0,−1]]

For each: M† = M (Hermitian) and M² = I (squares to identity). σ_y sign errors are the most common single failure mode.

Source: _lib_qmsri-04, §"The qubit" (complete derivation of Bloch vector, σ_y warning, double-cover discussion).

### Canonical example: Stern-Gerlach and spin-½

The spin-½ particle is the physical realization of the qubit. In a Stern-Gerlach apparatus, particles pass through an inhomogeneous magnetic field along axis ẑ. The force deflects particles into two beams: spin-up (+ℏ/2) and spin-down (−ℏ/2). This is the Born rule in action: the observable is Ŝ_z = (ℏ/2)σ_z, the eigenvalues are ±ℏ/2, and the probabilities are |⟨↑|ψ⟩|² and |⟨↓|ψ⟩|².

Sequential Stern-Gerlach experiments (z-axis, then x-axis, then z-axis again) are the standard demonstration that measurement collapses the state and that S_x and S_z do not commute: [σ_x, σ_z] = −2iσ_y.

The basis states:
  σ_z eigenstates: |0⟩ = |↑⟩, |1⟩ = |↓⟩
  σ_x eigenstates: |+x⟩ = (|0⟩+|1⟩)/√2, |−x⟩ = (|0⟩−|1⟩)/√2
  σ_y eigenstates: |+y⟩ = (|0⟩+i|1⟩)/√2, |−y⟩ = (|0⟩−i|1⟩)/√2

Source: _lib_qmsri-04, §"The qubit"; qm.md, §1 (Stern-Gerlach experiments, Townsend Ch. 1).

### Measurement statistics — worked example

**Setup:** |ψ⟩ = α|0⟩ + β|1⟩ with |α|² + |β|² = 1. Measure σ_z.

Eigenvalues: +1 (eigenstate |0⟩), −1 (eigenstate |1⟩).

Probabilities:
  P(σ_z = +1) = |⟨0|ψ⟩|² = |α|²
  P(σ_z = −1) = |⟨1|ψ⟩|² = |β|²

Sanity check: P(+1) + P(−1) = |α|² + |β|² = 1. ✓

Post-measurement states:
  if outcome +1: state collapses to |0⟩
  if outcome −1: state collapses to |1⟩

Expectation value: ⟨σ_z⟩ = (+1)|α|² + (−1)|β|² = |α|² − |β|² = cos θ.
Variance: σ²_{σz} = ⟨σ_z²⟩ − ⟨σ_z⟩² = 1 − cos²θ = sin²θ.
Standard deviation: σ_{σz} = sin θ.

**Now measure σ_x instead.** The σ_x eigenstates are |±x⟩ = (|0⟩ ± |1⟩)/√2.

  P(σ_x = +1) = |⟨+x|ψ⟩|² = |α + β|²/2
  P(σ_x = −1) = |⟨−x|ψ⟩|² = |α − β|²/2

For the specific case α = 1/√2, β = e^{iφ}/√2 (equatorial state, θ = π/2):
  P(σ_z = +1) = P(σ_z = −1) = 1/2
  ⟨σ_z⟩ = 0, σ_{σz} = 1

This state has maximal uncertainty in σ_z. Meanwhile ⟨σ_x⟩ = cos φ and σ_{σx} = sin φ — the distribution in x depends on the azimuthal phase φ. The phase is observable through measurement of a non-commuting observable.

Source: _lib_qmsri-04, §"The qubit" (Bloch vector calculations in full, Table on state-dependent Robertson bounds).

### Robertson bound for qubit observables

[σ_x, σ_z] = −2iσ_y → Robertson: σ_{σx} σ_{σz} ≥ |⟨σ_y⟩| = |sin θ sin φ|.

State-dependent bound (key teaching point — the bound is not a fixed number):

| State (θ, φ) | ⟨σ_y⟩ | σ_{σx} | σ_{σz} | product | bound |
|---|---|---|---|---|---|
| |0⟩ (θ=0) | 0 | 1 | 0 | 0 | 0 |
| |+x⟩ (θ=π/2, φ=0) | 0 | 0 | 1 | 0 | 0 |
| |+y⟩ (θ=π/2, φ=π/2) | 1 | 1 | 1 | 1 | 1 — saturated |

The σ_y eigenstate saturates the σ_x / σ_z bound: a state certain in ŷ is maximally uncertain in x̂ and ẑ. This is geometrically transparent on the Bloch sphere.

Source: _lib_qmsri-04, §"Commutators and why they matter" (Robertson for Paulis); Table on Robertson states.

### Collapse and its operational meaning

Collapse is not a claim about ontology — it is a description of the state-update rule. After obtaining outcome aₙ, all subsequent measurements on *that same particle* should be predicted using |aₙ⟩, not the original |ψ⟩. In an ensemble interpretation: the sub-ensemble that gave outcome aₙ is now characterized by state |aₙ⟩.

Sequential measurement illustration: prepare |+x⟩, measure σ_z, get +1 with probability ½. The post-measurement state is |0⟩. Now measure σ_z again: get +1 with probability 1. The first measurement erased the x-coherence. This is collapse, made concrete.

Source: _lib_qmsri-04, §"The qubit."

### The Bloch sphere — preview of time evolution

Under Ĥ = (ℏω/2)(B_x σ_x + B_y σ_y + B_z σ_z), time evolution is:

  |ψ(t)⟩ = U(t)|ψ(0)⟩,  U(t) = cos(ωt/2)I − i sin(ωt/2)(n̂·σ)

(Using (n̂·σ)² = I from Pauli anticommutation.) This rotates the Bloch vector around n̂ at angular velocity ω — Larmor precession. In NMR/MRI: the spin precesses around the static field. In quantum computing: controlled RF pulses implement single-qubit gates.

Time evolution is deferred to later chapters; include only as a forward reference here to motivate the Bloch sphere geometry.

Source: _lib_qmsri-04, §"Time evolution as rotation."

---

## B. Domain examples and cases

### Stern-Gerlach sequences

Canonical sequential measurements to cover:

1. **Z then Z:** No surprise. The second Z measurement always returns the same outcome as the first. Collapse is stable.
2. **Z then X:** After measuring Z and getting |0⟩, measure X. Get +1 or −1 with equal probability ½. The Z-eigenstate is a superposition in the X-eigenbasis.
3. **Z then X then Z:** Now the Z outcome is again random. The intermediate X measurement "destroyed" the Z information. This is the non-commutativity of σ_x and σ_z made physically tangible.

### NMR / MRI (Larmor precession)

The spin-½ proton in a static magnetic field B₀ẑ has Hamiltonian Ĥ = −γ(ℏ/2)B₀σ_z, where γ is the gyromagnetic ratio. The Bloch vector precesses around ẑ at the Larmor frequency ω_L = γB₀. A transverse RF pulse (at ω_L) rotates the vector into the xy-plane — the "flip." The subsequent free precession and relaxation are the MRI signal. This is the most consequential real-world application of the qubit formalism.

### Quantum computing preview

A qubit in a quantum computer is physically realized as a superconducting Josephson junction, a trapped ion, or a photon polarization state. Single-qubit gates are unitary 2×2 matrices: the Hadamard gate H = (σ_x + σ_z)/√2 sends |0⟩ → |+x⟩, implementing the σ_z → σ_x basis change. The σ_y eigenstate is |+y⟩ = (|0⟩ + i|1⟩)/√2, which requires a global phase that is invisible in single-qubit measurements but visible in two-qubit interference.

### Specific numerical worked example (for the chapter)

State: |ψ⟩ = (√3/2)|0⟩ + (i/2)|1⟩. Then α = √3/2, β = i/2, |α|² = 3/4, |β|² = 1/4.

Measure σ_z:
  P(+1) = 3/4, P(−1) = 1/4. ⟨σ_z⟩ = 3/4 − 1/4 = 1/2.

Bloch vector: θ satisfies cos θ = 1/2 → θ = π/3. φ: e^{iφ} sin(θ/2) = β/... need consistent parametrization. Check: this is θ = π/3, φ = π/2 (σ_y positive direction). ⟨σ_x⟩ = sin(π/3) cos(π/2) = 0, ⟨σ_y⟩ = sin(π/3) sin(π/2) = √3/2.

Post-measurement (if +1): collapse to |0⟩. Post-measurement (if −1): collapse to |1⟩.

Measure σ_x on this state:
  P(σ_x = +1) = |⟨+x|ψ⟩|² = |(√3/2 + i/2)/√2|² = (3/4 + 1/4)/2 = 1/2.
  P(σ_x = −1) = 1/2.

Verify Robertson: σ_{σx} = 1, σ_{σz} = √(1 − (1/2)²) = √3/2. Product = √3/2. Bound = |⟨σ_y⟩| = √3/2. Saturated.

---

## C. Connections and dependencies

- **Ch 9 (Operators and Uncertainty):** Ch 10 is the direct application of Ch 9's framework to the simplest non-trivial system. The measurement postulate was introduced abstractly in Ch 9; Ch 10 makes it concrete.
- **Ch 1–3 (Wave function, TISE, bound states):** The infinite-well and harmonic-oscillator energy measurements are the continuous-variable analogue of the discrete qubit measurements in Ch 10. The Born rule is the same postulate.
- **Ch 11 (Sandbox):** The sandbox's eigenfunction viewer is the continuous-variable implementation of the same "list the eigenstates, compute overlaps, predict measurement outcomes" algorithm that Ch 10 teaches for the qubit.
- **Quantum computing (later volumes):** The qubit is the elementary unit of quantum computation. Entanglement (Bell states, two-qubit measurements) and quantum gates extend the Ch 10 framework. Flag as a bridge.
- **qm.md (Feiguin notes):** §1.4 "Measurement outcomes" and §1.5 "Time evolution operator" are aligned with Ch 10 content. The Stern-Gerlach discussion in qm.md (citing Townsend Ch. 1) gives an additional source for the sequential-measurement narrative.

---

## D. Current state of the field

The measurement postulate as stated is the standard Copenhagen formulation. It is not experimentally challenged — the predictions are confirmed to extraordinary precision. The active research concerns interpretation, not predictions:

1. **Collapse / decoherence.** The collapse rule is effective but not fundamental in many interpretations. Decoherence theory (Zurek 2003, *Rev. Mod. Phys.* 75, 715) explains why macroscopic superpositions are unobservable without invoking an axiom of collapse. Do not enter this debate in Ch 10; mention it as "Still Puzzling."
2. **Quantum non-demolition (QND) measurement.** A measurement is QND if it does not disturb the observable being measured (only its conjugate). Spin σ_z measurements with a Stern-Gerlach apparatus are QND for σ_z. Active research in quantum sensing and metrology. Brief mention appropriate.
3. **Weak measurement.** Post-selection on rare outcomes allows "weak values" outside the eigenvalue range. Aharonov, Albert, Vaidman (1988). Advanced topic; one footnote.
4. **Bloch sphere for mixed states.** Mixed states (density matrices) correspond to points *inside* the Bloch sphere, |r| < 1. The maximally mixed state (I/2) is at the center. This is the Ch 10 extension to two-qubit entanglement and reduced density matrices.

---

## E. Teaching considerations

### Common misconceptions

1. **"The state collapses to α|0⟩ + β|1⟩ → one of the terms."** Wrong framing. Collapse is to the eigenstate of the *measured observable*, which may not be |0⟩ or |1⟩ if you measured σ_x.
2. **"Only the probability density |ψ|² matters; the phase is irrelevant."** The phase φ in e^{iφ}β is physically observable when you measure a non-commuting observable. The Bloch sphere makes this concrete: different φ at fixed θ give different ⟨σ_x⟩ and ⟨σ_y⟩.
3. **"The Bloch sphere represents the particle's position in space."** It represents the state-space geometry for a two-level system. Not position.
4. **θ vs θ/2.** The factor of θ/2 in the state is the most common parameter error. Test: θ = π must give |1⟩, which requires cos(π/2) = 0 and sin(π/2) = 1. If θ/2 is omitted, θ = π/2 gives |1⟩ instead of the equatorial state.

### Simulation anchor

The `04-bloch-sphere.html` simulation from Ch 4 (in _lib_qmsri-04's LLM Exercise) implements:
- Static state mode (Bloch vector from θ, φ sliders; Pauli expectation values as bar charts).
- Measurement-statistics mode (N independent copies, two Pauli measurements, Robertson bound comparison).

This simulation is the natural anchor for Ch 10. The exploration tasks in _lib_qmsri-04 (§"Robertson is about the state, not the apparatus") directly operationalize the Ch 10 capability: set θ = π/2, φ = π/2 (σ_y eigenstate), measure σ_x and σ_z on N = 1000 copies, confirm both histograms are 50/50, confirm product = 1 ≥ Robertson bound = |⟨σ_y⟩| = 1.

### Key pedagogical moves

1. **Start with a 2×2 matrix.** Do every computation — eigenvalues, eigenvectors, probabilities, expectation values — explicitly with matrices. The generalization to infinite-dimensional Hilbert space is then conceptually trivial.
2. **Use the ensemble protocol every time.** "Prepare N copies; measure on independent copies; compare histogram to Born-rule predictions." Never say "measure the same particle twice."
3. **Draw the Bloch sphere.** The geometric picture (north pole = |0⟩, south = |1⟩, equator = equal superpositions, phase = longitude) is more durable than the algebra.
4. **Sequential measurements as narrative.** Z→X→Z is a story: certainty, uncertainty, reset. Students remember narratives.

---

## F. Library files relevant to this chapter

- **Primary:** `/pantry/_lib_qmsri-04-formalism-dirac-notation-and-operators.md` — §"The qubit" (state parametrization, Bloch sphere, full Bloch vector derivation, Robertson for Paulis, σ_y failure mode, time evolution as rotation, LLM Exercise for `04-bloch-sphere.html`). This is the direct source for essentially all of Ch 10.
- **Supporting (measurement postulate framing):** `/pantry/_lib_qmsri-01-the-wave-function.md` — §"What do you actually measure?" and §"The uncertainty principle, properly." Provides the continuous-variable version of the same postulate that Ch 10 applies discretely.
- **Supplementary:** `/books/physics-quantum-mechanics-sri/pantry/qm.md` — §1.4 (measurement outcomes), §1.5 (time evolution), §1 introduction (Stern-Gerlach). Townsend Ch. 1–2 as cited in qm.md.
- **Simulation:** `04-bloch-sphere.html` (described in _lib_qmsri-04 LLM Exercise). Already spec'd with static, time-evolution, and measurement-statistics modes. No new simulation needed for Ch 10.

---

## G. Gaps and flags

1. **Two-qubit entanglement.** The Bloch sphere covers only single qubits. The natural next step — Bell states, |r| < 1 for reduced density matrices, entanglement entropy — is not in _lib_qmsri-04 (the extension prompt mentions it as a bridge, but the main text does not cover it). Flag for a later chapter or appendix.
2. **Decoherence and collapse mechanism.** The chapter postulates collapse without explaining *why* or *when* it occurs. Decoherence (environment-induced superselection) is the modern partial answer but is graduate-level. One "Still Puzzling" paragraph is appropriate.
3. **Continuous-variable measurement postulate.** For position, the eigenvalue spectrum is continuous and the post-measurement state is δ(x − x₀), which is not normalizable. The chapter should acknowledge this subtlety (position measurement is an idealization) without getting stuck on it.
4. **The σ_y sign.** Every time σ_y appears in code or simulation, a runtime check Hermitian/squares-to-I must be present. This is the most common LLM failure mode and is explicitly flagged in _lib_qmsri-04's CLAUDE.md amendment.
5. **Phase conventions.** Some texts write |ψ⟩ = α|0⟩ + β|1⟩ with no restriction on α; others require α real and non-negative by convention. The _lib_qmsri-04 parametrization uses cos(θ/2) (real and non-negative by construction). The chapter should commit to one and state it.
