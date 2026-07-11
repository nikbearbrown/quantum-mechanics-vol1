# Simulation Ideas — quantum-mechanics-vol1

Medhavy-register "Claude Code + Manim" workflow reels.

---

## Sim-01 — Classical Simulations: Photoelectric / Compton / UV Catastrophe (3-sim reel)
- Source: `quantum-mechanics-vol1/chapters/01-why-classical-physics-failed.md`
- Topic: CLAUDE CODE · MANIM
- Physical rule: K_max=hν−φ; Δλ=(h/m_e c)(1−cosθ); Planck vs Rayleigh-Jeans
- Concrete numbers: Na φ=2.28 eV, 700/546/300 nm photons; λ_C=2.426 pm at 0°/90°/180°; T=3000 K blackbody
- Visual artifact: photon-threshold arrows; Compton collision panels; Planck vs RJ curves
- Two testable predictions: P1: 546 nm blocked by Na (E=2.27<2.28 eV); P2: Compton Δλ doubles from 90° to 180°
- Sim slug: medhavy-ch1-classical-sims
- Status: BUILT — `quantum-mechanics-vol1/youtube/medhavy-ch1-classical-sims/medhavy-ch1-classical-sims-review.mp4`
- Watch: `open /Users/bear/Documents/CoWork/bear-textbooks/books/quantum-mechanics-vol1/youtube/medhavy-ch1-classical-sims/medhavy-ch1-classical-sims-review.mp4`

---

## Sim-02 — Infinite Square Well: Energy Ladder and n² Spectrum
- Source: `quantum-mechanics-vol1/chapters/05-the-infinite-square-well.md`
- Topic: CLAUDE CODE · MANIM
- Physical rule: E_n = n²π²ℏ²/(2mL²); boundary conditions force discrete k_n = nπ/L
- Concrete numbers: L=2 nm, m=m_e; E₁≈0.094 eV, E₂≈0.376 eV, E₃≈0.846 eV; ratios 1:4:9:16
- Visual artifact: energy ladder with sine eigenstates; change L and watch E₁ shift as 1/L²
- Two testable predictions: P1: E₂/E₁ = 4.000 exactly (n² spacing); P2: halving L from 2 nm to 1 nm quadruples E₁ from 0.094 eV to 0.376 eV
- Sim slug: medhavy-vol1-pib-spectrum

---

## Sim-03 — Quantum Harmonic Oscillator: Ladder and Zero-Point Energy
- Source: `quantum-mechanics-vol1/chapters/07-the-harmonic-oscillator.md`
- Topic: CLAUDE CODE · MANIM
- Physical rule: E_n = ℏω(n + 1/2); ground state energy ℏω/2 ≠ 0; equally spaced levels
- Concrete numbers: ω = 10¹⁴ rad/s → ℏω ≈ 0.066 eV; ground state 0.033 eV; spacing uniform at ℏω
- Visual artifact: parabolic potential with equally-spaced energy rungs; highlight the non-zero E₀
- Two testable predictions: P1: E₁ − E₀ = E₂ − E₁ = ℏω exactly (uniform spacing); P2: lowest rung at ℏω/2 > 0
- Sim slug: medhavy-vol1-harmonic-ladder

---

## Sim-04 — Wave Packet Spreading: Dispersion in Free Space
- Source: `quantum-mechanics-vol1/chapters/08-the-free-particle-and-wave-packets.md`
- Topic: CLAUDE CODE · MANIM
- Physical rule: σ(t)² = σ₀²/2 + ℏ²t²/(2m²σ₀²); width grows as √(1 + (ℏt/mσ₀²)²)
- Concrete numbers: σ₀=1 nm electron; spreading time τ=mσ₀²/ℏ ≈ 8.6 fs; at t=τ width is σ₀√2
- Visual artifact: Gaussian envelope moving right and visibly broadening over several τ
- Two testable predictions: P1: centroid moves at v = ℏk₀/m (group velocity); P2: at t=τ the packet width exactly doubles (σ=√2 σ₀)
- Sim slug: medhavy-vol1-packet-spread

---

## Sim-05 — 1D Quantum Sandbox: Eigensolver Benchmark
- Source: `quantum-mechanics-vol1/chapters/11-capstone-a-1d-quantum-sandbox.md`
- Topic: CLAUDE CODE · MANIM
- Physical rule: Tridiagonal Hamiltonian H_jj = 2t_k + V_j; H_{j±1,j} = −t_k; t_k = ℏ²/(2mh²)
- Concrete numbers: L=2 nm, N=500 grid points; analytic E₁=0.094 eV; ratio E₂/E₁ must equal 4.000
- Visual artifact: energy level diagram overlaid on the potential; dots at analytic vs numerical levels show near-perfect agreement
- Two testable predictions: P1: E₂/E₁ = 4.000 ± 0.001 (ratio independent of units); P2: fractional error in E₁ < 10⁻⁵ for N=500
- Sim slug: medhavy-vol1-sandbox-benchmark
