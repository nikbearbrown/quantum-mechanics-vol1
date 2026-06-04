# Research Notes: Chapter 11 — Capstone: A 1D Quantum Sandbox

**Corresponding chapter:** chapters/11-capstone-a-1d-quantum-sandbox.md (not yet written)
**Generated:** 2026-06-03
**Chapter type:** NEW capstone project (synthesis, no direct local draft)

---

## Chapter summary (capability built)

Students build a configurable 1D Schrödinger solver — the "sandbox" — that: (1) accepts any user-defined potential V(x), finds bound-state energies and eigenfunctions via a numerical eigensolver, and displays them; and (2) time-evolves an initial wave packet via split-step Fourier or Crank-Nicolson. They then "defend the physics" by running a suite of validation checks against analytically known cases (infinite square well, harmonic oscillator, free particle). The chapter is a synthesis project, not a derivation exercise — it exercises every major tool from Chapters 1–10.

---

## A. Conceptual foundations

### What the sandbox is

A configurable 1D Schrödinger solver is a program that accepts:
- A spatial grid: N points on x ∈ [x_min, x_max], grid spacing h = (x_max − x_min)/(N−1).
- A potential V(x): a callable function or piecewise definition.
- A mode: (a) **Eigensolver** — find bound-state energies E_n and wavefunctions ψ_n(x); (b) **Time evolution** — given initial state ψ(x, 0), propagate to ψ(x, t) under Ĥ = −(ℏ²/2m)∂²_x + V(x).

The sandbox embodies the full arc of QM Vol. 1: the wave function is computed (Ch 1), shaped by a potential (Ch 2–5), its eigenstates found (Ch 2–5), and then observed via expectation values and uncertainties (Ch 9) or measurement statistics (Ch 10).

### The time-independent Schrödinger equation as a matrix eigenvalue problem

The TISE is −(ℏ²/2m) ψ''(x) + V(x)ψ(x) = E ψ(x). Discretize on a uniform grid:

  ψ''(x_j) ≈ [ψ_{j+1} − 2ψ_j + ψ_{j−1}] / h²   (central difference, O(h²))

This converts the TISE into a matrix eigenvalue problem H_matrix · ψ_vec = E · ψ_vec, where:

  H_matrix[j,j]   = ℏ²/(m h²) + V(x_j)      (diagonal: kinetic + potential)
  H_matrix[j,j±1] = −ℏ²/(2m h²)              (off-diagonal: kinetic coupling)

H_matrix is real, symmetric, tridiagonal. Diagonalizing it with a standard eigensolver (numpy.linalg.eigh, LAPACK dsyev, or JavaScript power-iteration / Lanczos) yields all N eigenvalues and eigenvectors. The lowest bound-state eigenvalues and the corresponding eigenvectors (normalized by ∑|ψ_j|²·h = 1) are the physical answers.

Sources: [Finite Difference Method — cupcake physics](https://cupcakephysics.com/computational%20physics/2014/11/02/the-finite-difference-method-and-schrodingers-equation.html); [Finite Difference Solution — Medium / Tayo](https://medium.com/modern-physics/finite-difference-solution-of-the-schrodinger-equation-c49039d161a8); [Liu Group Tutorial](https://liu-group.github.io/1D-PDE-BV/); [Chemistry LibreTexts — Numerov](https://chem.libretexts.org/Bookshelves/Physical_and_Theoretical_Chemistry_Textbook_Maps/Time_Dependent_Quantum_Mechanics_and_Spectroscopy_(Tokmakoff)/01:_Overview_of_Time-Independent_Quantum_Mechanics/1.05:_Numerically_Solving_the_Schrodinger_Equation).

### The Numerov method (higher-order eigensolver)

The standard central-difference formula is O(h²). The Numerov algorithm achieves O(h⁶) by including higher-order terms from paired forward/backward Taylor expansions. The recursion is:

  ψ_{n+1} = [2ψ_n(1 − 5h²f_n/12) − ψ_{n−1}(1 + h²f_{n−1}/12)] / (1 + h²f_{n+1}/12)

where f_n = (2m/ℏ²)(E − V(x_n)).

Numerov is used as a *shooting method*: guess E, integrate from both boundaries toward the center, and look for a match. The eigenvalues are found by bracketing the values of E where the log-derivative discontinuity at the matching point changes sign, then bisecting. This approach is slower than direct diagonalization but uses far less memory for large grids and naturally handles problems where only a few eigenvalues are needed.

Applications validated in the literature: harmonic oscillator, square well, linear potential, hydrogen radial equation. The algorithm was used by Blatt (1967) and is discussed in Griffiths computational supplements.

Sources: [Numerov method paper — arXiv:1403.7092](https://arxiv.org/pdf/1403.7092); [TCD notes — Bennett](https://www.maths.tcd.ie/~dbennett/js/schro.pdf); [TCD notes — Kavanal](https://www.maths.tcd.ie/~kavanal6/assets/docs/1d-schrodinger-equation.pdf); [Chemistry LibreTexts](https://chem.libretexts.org/Bookshelves/Physical_and_Theoretical_Chemistry_Textbook_Maps/Time_Dependent_Quantum_Mechanics_and_Spectroscopy_(Tokmakoff)/01:_Overview_of_Time-Independent_Quantum_Mechanics/1.05:_Numerically_Solving_the_Schrodinger_Equation).

### Split-step Fourier method (time evolution)

The time evolution operator for Ĥ = T̂ + V̂ (kinetic + potential) is e^{−iĤΔt/ℏ}. The kinetic and potential operators do not commute, so the exact exponential cannot be split directly. The Trotter-Suzuki decomposition gives:

  e^{−iĤΔt/ℏ} ≈ e^{−iV̂Δt/(2ℏ)} · e^{−iT̂Δt/ℏ} · e^{−iV̂Δt/(2ℏ)}  + O(Δt³)

The algorithm per step:
1. Apply half-step potential phase: ψ(x) ← e^{−iV(x)Δt/(2ℏ)} · ψ(x)  [pointwise multiplication in x-space]
2. FFT to k-space: ψ̃(k) = FFT[ψ(x)]
3. Apply full kinetic phase: ψ̃(k) ← e^{−iℏk²Δt/(2m)} · ψ̃(k)  [pointwise multiplication in k-space]
4. IFFT back: ψ(x) = IFFT[ψ̃(k)]
5. Apply second half-step potential phase: ψ(x) ← e^{−iV(x)Δt/(2ℏ)} · ψ(x)

Each step is a pointwise multiplication — O(N log N) via FFT. The method is **exactly unitary at each step** (each exponential factor is a complex number of modulus 1), so normalization is preserved to machine precision automatically.

Accuracy: O(Δt²) in time (from the Trotter splitting), spectral in space (FFT is exact for periodic functions on the grid). Stability: unconditionally stable — no CFL condition on Δt. Limitation: requires periodic boundary conditions (or absorbing boundaries implemented via a complex absorbing potential).

First used for quantum wave-packet propagation: Feit, Fleck, and Steiger (1982), *J. Comput. Phys.* 47, 412–433.

Sources: [MatterWaveX split-step guide](https://matterwavex.com/split-step-fourier-method-for-tdse/); [PyCav documentation](https://pycav.readthedocs.io/en/latest/api/pde/split_step.html); [SIAM J. Num. Anal. — Hardin & Tappert](https://epubs.siam.org/doi/10.1137/0723033); [arXiv boundary reflection suppression](https://arxiv.org/pdf/physics/0607120).

### Crank-Nicolson method (time evolution, alternative)

Crank-Nicolson (CN) discretizes the TDSE as:

  [I + iΔt/(2ℏ)·H_matrix] ψ^{n+1} = [I − iΔt/(2ℏ)·H_matrix] ψ^n

This is equivalent to applying the Cayley approximation U(Δt) ≈ (I − iH_matrixΔt/2ℏ)/(I + iH_matrixΔt/2ℏ), which is exactly unitary when H_matrix is Hermitian (the numerator and denominator are complex conjugates). Properties:

- **Unconditionally stable** (no restriction on Δt/h²).
- **Second-order accurate** in both time and space (O(Δt²) + O(h²)).
- **Exact unitarity at the discrete level** — norm preserved to machine precision.
- Each time step requires solving a tridiagonal linear system, O(N) via Thomas algorithm.

Boundary conditions: Dirichlet (ψ = 0 at walls) are natural for the tridiagonal system. Hard-wall (infinite well) and finite-well boundaries both fit.

Comparison to split-step: CN is O(N) per step vs O(N log N) for split-step, but requires constructing and inverting the tridiagonal matrix. For most undergraduate-scale grids (N ~ 500–2000), both methods are fast enough. Split-step is easier to implement without linear algebra libraries; CN is conceptually cleaner for the unitary structure of QM.

Sources: [arXiv:2410.10060 — Crank-Nicolson for TDSE](https://arxiv.org/html/2410.10060v1); [MatterWaveX CN guide](https://matterwavex.com/crank-nicolson-method-for-the-tdse/); [Wiley / Khan 2022](https://onlinelibrary.wiley.com/doi/10.1155/2022/6991067); CLAUDE.md in the textbook series already mandates CN for time evolution (from _lib_qmsri-00: "Use analytic time evolution where a closed form exists. Numerical PDE integration only with a unitary scheme (Crank-Nicolson), never explicit Euler.").

### Why not explicit Euler?

Explicit Euler applied to iℏ ∂_t ψ = Ĥψ gives ψ^{n+1} = ψ^n − (iΔt/ℏ)H_matrix ψ^n. The update matrix I − (iΔt/ℏ)H_matrix has eigenvalues 1 − iΔtE_n/ℏ, with modulus √(1 + (ΔtE_n/ℏ)²) > 1. Normalization grows exponentially — the scheme is unconditionally unstable. This is the failure mode flagged in _lib_qmsri-00 (§"Simulation core") and _lib_qmsri-01 (§"Normalization, and a calculation worth doing in full"). The sandbox must use CN or split-step.

---

## B. Domain examples and cases

### Validation case 1: Infinite square well (primary benchmark)

Analytic spectrum: E_n = n²π²ℏ²/(2mL²), n = 1, 2, 3, ...
Wavefunctions: ψ_n(x) = √(2/L) sin(nπx/L)

Numerical validation protocol:
1. Set V(x) = 0 for x ∈ (0, L), V = ∞ (very large number, e.g. 1e10 in units) at boundaries.
2. Run the eigensolver on N = 500 grid points.
3. Compute the fractional error δE_n = |E_n^{numerical} − E_n^{analytic}| / E_n^{analytic} for n = 1, 5, 10.
4. For the central difference scheme, expect δE_n ~ (nπh/L)²/12 (the leading O(h²) error, derived from the Taylor expansion of the second derivative). For n=1, N=500: δE ≈ (π/500)²/12 ≈ 3×10⁻⁷.
5. Verify normalization: ∑_j |ψ_j|² · h = 1 within 1e-4.
6. Verify orthogonality: |⟨ψ_n|ψ_m⟩| < 1e-10 for n ≠ m.

Sources: [cupcake physics — finite difference validation](https://cupcakephysics.com/computational%20physics/2014/11/02/the-finite-difference-method-and-schrodingers-equation.html); [Bucknell finite-difference square well](http://www.eg.bucknell.edu/~mligare/python_projects/quantum/finiteDifference_sw.html); [Physics LibreTexts — ISW](https://phys.libretexts.org/Bookshelves/Modern_Physics/Spiral_Modern_Physics_(D'Alessandris)/6:_The_Schrodinger_Equation/6.2:_Solving_the_1D_Infinite_Square_Well).

### Validation case 2: Harmonic oscillator

Analytic spectrum: E_n = ℏω(n + ½), n = 0, 1, 2, ...
Wavefunctions: Hermite-Gaussian functions; ground state ψ_0 ∝ exp(−x²/(2x₀²)) with x₀ = √(ℏ/mω).

Numerical validation:
1. Set V(x) = ½mω²x² on x ∈ [−6x₀, 6x₀], N = 500.
2. Confirm E₀ = ℏω/2, E₁ = 3ℏω/2, spacing uniform at ℏω.
3. Confirm ψ₀ has Gaussian shape; fit a Gaussian and compare width to x₀.
4. Verify ground-state uncertainty: σ_x σ_p = ℏ/2 (the harmonic oscillator ground state is a coherent state — the Gaussian saturates the bound). This connects directly to Ch 9.

### Validation case 3: Free particle (time evolution)

Set V(x) = 0 everywhere. Prepare ψ(x, 0) = Gaussian wave packet (Ch 0 / Ch 1 closed form). Run time evolution to t = T. Compare ψ(x, T) numerically to the analytic solution:

  σ(T)² = a²/2 + ℏ²T²/(2m²a²),  centroid at x = v_g T.

Checks: centroid agrees to <1%; σ(T) agrees to <1%; normalization = 1.000 throughout.

### Additional sandbox potentials (for exploration)

- **Finite square well:** bound states exist only for E < V₀. Students can dial V₀ and watch bound states appear/disappear, confirming at least one bound state always exists in 1D.
- **Double well:** two wells of depth V₀ separated by barrier of width d. Ground state is symmetric, first excited state antisymmetric; energy splitting decreases exponentially with d (tunnel splitting). Connection to the molecular H₂⁺ ion.
- **Linear potential (tilted well):** V(x) = Fx. Eigenstates are Airy functions; useful for verifying the Numerov shooting method.
- **Kronig-Penney (periodic potential):** array of square wells. Band structure appears. Preview of solid-state physics.

---

## C. Connections and dependencies (chapters 1–10 exercised by the sandbox)

| Sandbox feature | Chapter(s) exercised |
|---|---|
| ψ displayed as three panels: Re ψ, Im ψ, \|ψ\|² | Ch 1 (Born rule, normalization) |
| Normalization indicator ∫\|ψ\|²dx = 1.000 | Ch 1 (normalization preservation) |
| Potential V(x) displayed in red | Ch 2 (TISE, bound states) |
| Energy levels E_n as horizontal green lines | Ch 2–5 (eigenvalue problem) |
| Classical turning points | Ch 3–4 (tunneling, classically forbidden) |
| Eigensolver output: ψ_n(x) shapes | Ch 2–5 (harmonic oscillator, finite well) |
| Momentum-space display \|φ(p)\|² | Ch 1 (Fourier duality), Ch 9 (σ_p) |
| σ_x and σ_p computed for each eigenstate | Ch 9 (operators, Robertson bound) |
| Measurement simulation on eigenstate | Ch 10 (Born rule, collapse preview) |
| Time evolution: wave packet in potential | Ch 0 (free particle), Ch 6+ (bound-state dynamics) |
| Energy conservation check | Ch 2 (stationary states), Ch 9 (Hamiltonian expectation value) |

---

## D. Current state of the field

### Finite-difference eigensolvers

The matrix diagonalization approach (tridiagonal real-symmetric) is solved in O(N²) time by standard LAPACK routines (dsyev, dsyevd). For the undergraduate sandbox scale (N ~ 500), this is instantaneous. For large N or 2D/3D extensions, iterative methods (Lanczos, Arnoldi) are used.

The O(h²) accuracy of the standard central difference can be improved. The Numerov method gives O(h⁶) for the second derivative and is the standard choice when high accuracy with few grid points is needed. Reference implementations exist in Python (scipy.linalg.eigh), MATLAB, and JavaScript (hand-rolled). The arXiv paper (1507.03708) discusses Numerov with pseudo-delta potentials as a specialized variant.

The J. Chem. Ed. paper (Pfahnl 2022, [DOI:10.1021/acs.jchemed.2c00557](https://pubs.acs.org/doi/10.1021/acs.jchemed.2c00557)) describes a finite-difference approach specifically designed for visualization in undergraduate quantum chemistry, making it directly relevant as a pedagogical reference.

### Time-evolution methods

Split-step Fourier (SSFM) is the de facto standard for 1D wave-packet propagation in research and education. It is used in ultracold atom simulations (Gross-Pitaevskii equation), nonlinear fiber optics (nonlinear Schrödinger equation), and quantum optimal control. The method's O(N log N) scaling and automatic normalization conservation make it superior to finite-difference time-domain (FDTD) methods for smooth potentials.

Crank-Nicolson is preferred when the potential has hard boundaries (infinite wells) or when the code must avoid FFTs. It is the method mandated by the textbook's CLAUDE.md. Both methods are unconditionally stable and norm-conserving; neither is "wrong" — choice depends on boundary conditions and implementation convenience.

Absorbing boundary conditions (complex absorbing potential, CAP): add −iW(x) to V(x) near the grid edges to prevent reflection from the numerical boundary. Used in scattering calculations. Relevant if the sandbox extends to wave-packet scattering from a barrier.

---

## E. Teaching considerations

### The "defend the physics" rubric

The capstone requires students to run a validation suite and confirm:

1. **Units.** Every displayed quantity has correct units (eV or J for energies, nm for lengths, nm⁻¹ for momenta). Dimensionless ratios (E_n/E₁) should match analytic predictions exactly.
2. **Normalization.** ∫|ψ_n|² dx = 1 for every eigenstate. The normalization indicator must read 1.000 ± 0.001.
3. **Orthogonality.** |⟨ψ_n|ψ_m⟩| < 1e-8 for n ≠ m (up to round-off). Failure signals a bug in the eigensolver or grid.
4. **Energy eigenvalue accuracy.** Fractional error δE_n/E_n^{analytic} < 1% for n = 1..5 on the infinite square well. State the expected O(h²) scaling.
5. **Energy conservation under time evolution.** ⟨Ĥ⟩(t) = ∑_n |c_n|² E_n remains constant throughout the evolution (the Hamiltonian expectation value is conserved for a time-independent H). Verify to within 0.1%.
6. **Known-case check: infinite well.** Run the eigensolver on the infinite well, report E₁..E₅, compare to analytic. Report fractional errors. This is the primary validation.
7. **Known-case check: harmonic oscillator.** Verify E₀ = ℏω/2, equal spacing, Gaussian ground state.
8. **Known-case check: free-particle time evolution.** Compare σ(t) and centroid to the analytic formulas.

### The four-move prompt for the sandbox

Following the textbook's simulation protocol (Ch 0, _lib_qmsri-00):

- **Show.** The TISE in matrix form; the split-step algorithm; the analytic infinite-well spectrum for validation.
- **Say.** "Produce `11-quantum-sandbox.html`: a single HTML file with a configurable 1D Schrödinger solver with eigensolver and time-evolution modes."
- **Constrain.** D3 v7, SVG, N = 500–2000 selectable, CLAUDE.md rules (normalization indicator, no explicit Euler, units labeled). Eigensolver: matrix diagonalization (tridiagonal). Time evolution: Crank-Nicolson or split-step.
- **Verify.** Four checks: (a) infinite-well E₁..E₅ vs analytic; (b) normalization = 1.000; (c) Gaussian time evolution centroid vs v_g t; (d) energy conservation to 0.1%.

### Common failure modes (LLM-generated code)

1. **Using explicit Euler** — normalization explodes in < 100 steps. CLAUDE.md mandates CN or SSFM; add a runtime check that the normalization indicator stays within 1% at every frame.
2. **Wrong grid spacing in the second-derivative stencil** — h vs h² confusion in the diagonal elements. Validate by checking E₁ against the infinite-well analytic.
3. **Missing the factor of ℏ²/(2m) in the kinetic term** — energies off by this factor. Units check catches this immediately.
4. **Eigenvectors not renormalized** — LAPACK returns orthonormal vectors, but if the student implements their own power iteration, normalization may drift. Check ∑|ψ_j|²·h = 1.
5. **Boundary conditions at wall** — for the infinite well, ψ₀ = ψ_N = 0 must be enforced. Finite-well potentials need ψ → 0 far from the well, which requires a grid wide enough (typically 5–10 times the well width). Grid-too-narrow is a common bug.
6. **FFT convention in split-step** — the momentum grid in FFT convention runs from 0 to k_max in the first half and −k_max to 0 in the second half (aliased). The kinetic phase must use the FFT-shifted k values. Failure gives a complex wrong answer that may still look visually plausible for short times.
7. **No absorbing boundary** — in time-evolution mode, the wave packet hits the wall and reflects numerically. Either use an absorbing potential near the edges or make the grid wide enough that the packet doesn't reach the boundary in the simulation time.

### The project rubric (for "defending the physics")

| Criterion | Points | Check |
|---|---|---|
| Units correct on all displays | 10 | Read off E₁ in eV for ISW, compare to analytic |
| Normalization = 1.000 throughout | 15 | Normalization indicator in corner |
| Orthogonality of eigenstates | 10 | Compute ⟨ψ₁\|ψ₂⟩ numerically |
| ISW energy spectrum within 1% | 20 | E₁..E₅ table vs analytic |
| Harmonic oscillator energy spacing uniform | 15 | E₁−E₀ = E₂−E₁ = ℏω |
| Free-particle time evolution matches σ(t) | 15 | Compare σ at t = 5 fs and 20 fs |
| Energy conservation under TDSE | 10 | ⟨Ĥ⟩(t) stable to 0.1% |
| Exploration of non-standard potential | 5 | Any valid V(x) with physically sensible result |

---

## F. Library files relevant to this chapter

- **Primary (simulation toolchain):** `/pantry/_lib_qmsri-00-how-to-use-the-simulations.md` — §4 (Brutalist system: CLAUDE.md, DESIGN.md, PROJECT.md), §5 (four-move prompt), §6 (free-particle physics), §9 (LLM Exercise structure). The sandbox prompt must follow this four-move structure.
- **Primary (wave function foundations):** `/pantry/_lib_qmsri-01-the-wave-function.md` — §"Normalization," §"Probability current," §"The uncertainty principle, properly," §"The Gaussian saturates the bound." These define the validation criteria for the sandbox (normalization, σ_x σ_p for eigenstates).
- **Primary (operators):** `/pantry/_lib_qmsri-04-formalism-dirac-notation-and-operators.md` — §"Operators and Hermiticity" (spectral theorem — eigenstates form complete basis), §"Commutators" (Robertson bound to verify against sandbox). The sandbox's σ_x, σ_p outputs are the Ch 9 framework made numerical.
- **Web sources (numerical methods):**
  - [Chemistry LibreTexts — Numerov](https://chem.libretexts.org/Bookshelves/Physical_and_Theoretical_Chemistry_Textbook_Maps/Time_Dependent_Quantum_Mechanics_and_Spectroscopy_(Tokmakoff)/01:_Overview_of_Time-Independent_Quantum_Mechanics/1.05:_Numerically_Solving_the_Schrodinger_Equation)
  - [arXiv Numerov paper](https://arxiv.org/pdf/1403.7092)
  - [TCD finite-difference notes](https://www.maths.tcd.ie/~dbennett/js/schro.pdf)
  - [MatterWaveX split-step guide](https://matterwavex.com/split-step-fourier-method-for-tdse/)
  - [MatterWaveX Crank-Nicolson guide](https://matterwavex.com/crank-nicolson-method-for-the-tdse/)
  - [arXiv CN simulation](https://arxiv.org/html/2410.10060v1)
  - [J. Chem. Ed. — finite difference visualization](https://pubs.acs.org/doi/10.1021/acs.jchemed.2c00557)
  - [cupcake physics — finite difference tutorial](https://cupcakephysics.com/computational%20physics/2014/11/02/the-finite-difference-method-and-schrodingers-equation.html)
  - [Bucknell finite-difference code](http://www.eg.bucknell.edu/~mligare/python_projects/quantum/finiteDifference_sw.html)

---

## G. Gaps and flags (capstone-specific)

1. **JavaScript linear algebra.** The textbook stack is D3 v7, SVG, vanilla JS — no numpy, no scipy. Diagonalizing a 500×500 tridiagonal matrix in vanilla JS requires either a hand-rolled Jacobi iteration (slow, O(N³)) or importing a JS linear algebra library (math.js, numeric.js). The CLAUDE.md from Ch 0 says "Math.js and fft-js may be added later with explicit prompt approval." The Ch 11 prompt should explicitly authorize math.js for the eigensolver.

   **Alternative:** Use the Numerov shooting method instead of full diagonalization — it only requires bisection search and forward integration, which is pure arithmetic and easy in vanilla JS. Trade-off: Numerov finds eigenvalues one at a time (requires bracketing); diagonalization finds all at once. Recommendation: provide both options in the chapter, let students choose based on how many states they need.

2. **FFT in vanilla JS.** The split-step method requires an FFT. The CLAUDE.md already includes fft-js from CDN as a permitted library. Confirm the FFT convention: does fft-js return the correct k-grid ordering for the kinetic phase application? The k-space phase factor is e^{−iℏk²Δt/(2m)}; the k-values must be the FFT-shifted frequencies (fftfreq-style, not raw output indices). Flag this as a known failure mode and include a CLAUDE.md amendment for the Ch 11 prompt.

3. **Absorbing boundaries.** Without them, the wave packet reflects from the grid edge and creates spurious interference. For the capstone, either: (a) make the grid wide enough that reflection doesn't occur in the simulation time window; or (b) add a complex absorbing potential (CAP) W(x) = −iγ·max(0, (|x|−x_abs)²) near the edges. The CAP intentionally breaks unitarity near the edges to absorb outgoing flux. The normalization indicator will show a slow decrease — this is correct, not a bug. Students must understand the distinction.

4. **2D extension.** The natural next step (not in Ch 11) is a 2D solver (separable or fully 2D). Flag as a Volume 2 topic. The split-step method extends straightforwardly to 2D with two sequential FFT calls.

5. **Scattering.** Time-evolving a wave packet incident on a barrier produces transmission and reflection. Computing transmission coefficient T(E) requires averaging over the momentum distribution of the packet. This is beautiful but adds complexity beyond the capstone scope. Mark as an extension exercise.

6. **Performance.** Diagonalizing a 2000×2000 matrix in JavaScript takes several seconds. Warn students to use N = 500 for interactive exploration and N = 2000 only for accuracy benchmarks. The eigensolver should run on a "Compute" button press, not on every slider update.

7. **Analytic-vs-numerical comparison display.** The validation rubric requires comparing to analytic results. The sandbox should display both the numerical E_n and the analytic formula (where known) side by side. This requires the sandbox to know which potential is selected and whether an analytic solution exists. Implement via a "potential presets" menu with associated analytic formulas.

8. **Chapter sequencing risk.** Ch 11 is titled a capstone but comes after Ch 10 (qubit / measurement). The qubit material uses finite matrices; the sandbox uses continuous x-space. The conceptual bridge is: both are implementations of the same eigenvalue / Born-rule algorithm, one in 2D complex vector space, one in N-dimensional discretized function space. The chapter should make this bridge explicit, not assume students will see it.
