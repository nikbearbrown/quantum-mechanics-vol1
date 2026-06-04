# Chapter 12 — Capstone: A 1D Quantum Sandbox

## TL;DR

- Every 1D quantum problem you have solved analytically in Chapters 2–10 can be solved numerically: find bound-state energies and eigenfunctions, or time-evolve a wave packet, for any potential you can write down.
- The eigensolver converts the TISE into a matrix eigenvalue problem — a real, symmetric, tridiagonal matrix whose eigenvalues are bound-state energies and whose eigenvectors are (discretized) wave functions.
- For time evolution, two unitary methods — split-step Fourier and Crank-Nicolson — propagate the wave function while exactly preserving normalization. Explicit Euler does not, and you must not use it.
- The D3/vanilla-JS environment has no built-in linear algebra. The sandbox offers two paths: Numerov shooting (pure arithmetic, no library, one eigenvalue at a time) or matrix diagonalization (requires math.js, finds all eigenvalues at once). You choose which path fits your needs.
- "Defending the physics" means running a suite of validation checks: units, normalization, orthogonality, and the infinite-square-well spectrum $E_n = n^2\pi^2\hbar^2/(2mL^2)$ as the primary benchmark.

---

The last chapter of Vol. 1 is a project chapter. There is no new postulate to state, no new analytic solution to find. What is new is the task: take everything you have built — Born rule, Schrödinger equation, bound states, wave packets, operators, uncertainty, the measurement postulate — and make it run on an arbitrary potential.

You are going to build a configurable 1D Schrödinger solver. When you are done, you should be able to type in a potential, press a button, and get back bound-state energies, wave functions, and (if you want) a time-evolving wave packet. You should then run the solver on a potential whose answer you know — the infinite square well — and verify that your numerical answer matches the analytic formula $E_n = n^2\pi^2\hbar^2/(2mL^2)$ to within 1%.

That verification step is not bureaucratic box-checking. It is the intellectual discipline that separates a physics program from a program that looks like physics. Every serious simulation in research goes through it. This chapter teaches you the habit.

---

## The two modes

The sandbox has two operational modes, and you should understand what each does before you build either one.

**Mode 1: Eigensolver.** Given a potential $V(x)$ defined on a spatial grid, find the bound-state energies $E_n$ and the corresponding eigenfunctions $\psi_n(x)$. The result is a list of pairs $(E_n, \psi_n)$, displayed as energy levels and wave-function plots.

**Mode 2: Time evolution.** Given an initial wave function $\psi(x, 0)$ and a potential $V(x)$, compute $\psi(x, t)$ for $t > 0$ by numerically solving the time-dependent Schrödinger equation $i\hbar\,\partial_t\psi = \hat{H}\psi$. The result is an animation of the probability density $|\psi(x,t)|^2$ drifting, spreading, bouncing, or tunneling, depending on the potential.

Both modes operate on the same spatial grid: $N$ uniformly spaced points $x_j = x_\mathrm{min} + j\,h$, $j = 0, \ldots, N-1$, with grid spacing $h = (x_\mathrm{max} - x_\mathrm{min})/(N-1)$. The wave function is a complex-valued array of length $N$. The potential is a real-valued array of length $N$.

---

## The TISE as a matrix eigenvalue problem

The time-independent Schrödinger equation is

$$-\frac{\hbar^2}{2m}\psi''(x) + V(x)\psi(x) = E\psi(x).$$

On the grid, the second derivative is approximated by the **central-difference stencil**:

$$\psi''(x_j) \approx \frac{\psi_{j+1} - 2\psi_j + \psi_{j-1}}{h^2} + O(h^2).$$

Substituting, the TISE at grid point $j$ becomes

$$-\frac{\hbar^2}{2m}\cdot\frac{\psi_{j+1} - 2\psi_j + \psi_{j-1}}{h^2} + V_j\psi_j = E\psi_j.$$

This is a linear equation in $\psi_{j-1}, \psi_j, \psi_{j+1}$. Writing it for every interior grid point simultaneously produces a matrix equation

$$\mathbf{H}\vec{\psi} = E\,\vec{\psi},$$

where the Hamiltonian matrix $\mathbf{H}$ is **real, symmetric, and tridiagonal**:

$$H_{jj} = \frac{\hbar^2}{mh^2} + V_j, \qquad H_{j,j\pm 1} = -\frac{\hbar^2}{2mh^2}.$$

The diagonal entries are kinetic energy ($\hbar^2/(mh^2)$ is twice the "hopping" coefficient) plus the local potential. The off-diagonal entries are the kinetic coupling between adjacent grid points — they are always negative and always equal $-\hbar^2/(2mh^2)$.

Boundary conditions: for the infinite square well or any hard-wall potential, enforce $\psi_0 = \psi_{N-1} = 0$ (Dirichlet). In the matrix this means omitting the first and last rows and columns — the interior $(N-2)\times(N-2)$ submatrix is what you diagonalize.

Diagonalizing $\mathbf{H}$ yields $N-2$ eigenvalues and eigenvectors. The lowest bound-state eigenvalues (positive $E_n < V_\infty$, where $V_\infty$ is the well depth or the boundary value) are the physical energies. The corresponding eigenvectors, normalized by $\sum_j |\psi_j|^2 \cdot h = 1$, are the discretized wave functions.

The error in the eigenvalues from the central-difference approximation scales as

$$\frac{\delta E_n}{E_n} \approx \frac{1}{12}\left(\frac{n\pi h}{L}\right)^2$$

for the $n$-th mode in a box of width $L$. For $N = 500$ points and $n = 1$: $\delta E_1/E_1 \approx (\pi/500)^2/12 \approx 3\times 10^{-7}$ — far below the 1% validation threshold. Even $N = 100$ gives $\delta E_1/E_1 \approx 8\times 10^{-5}$, still under 1%.

---

## Two paths to eigenvalues

The matrix eigensolver is the right tool for finding many eigenstates at once. But it requires either writing your own diagonalizer or loading a linear algebra library — and the textbook's D3/vanilla-JS environment does not include one by default.

Here are both options:

### Path A: Numerov shooting method (pure vanilla JS, no library)

The **Numerov method** improves the central-difference approximation of $\psi''$ to achieve $O(h^6)$ accuracy — four orders better — by including higher-order terms from paired Taylor expansions. Rewrite the TISE as $\psi'' = f(x)\psi$ where $f(x) = (2m/\hbar^2)(V(x) - E)$. The Numerov recursion is

$$\psi_{j+1} = \frac{2\psi_j\bigl(1 - \tfrac{5}{12}h^2 f_j\bigr) - \psi_{j-1}\bigl(1 + \tfrac{1}{12}h^2 f_{j-1}\bigr)}{1 + \tfrac{1}{12}h^2 f_{j+1}}.$$

Given $f_j = (2m/\hbar^2)(V_j - E)$ at each grid point, each recursion step is pure arithmetic — a handful of multiplications and divisions. No matrix, no library, no linear algebra.

Numerov is used as a **shooting method**:

1. **Guess** an energy $E$.
2. **Integrate** from the left boundary with initial conditions $\psi_0 = 0$, $\psi_1 = \epsilon$ (small, typically $10^{-6}$).
3. **Integrate** from the right boundary with $\psi_{N-1} = 0$, $\psi_{N-2} = \epsilon$.
4. **Match** at the midpoint: an eigenvalue occurs when the logarithmic derivatives from left and right agree — equivalently, when the **Wronskian** $\psi_\mathrm{left}(j_\mathrm{mid})\psi'_\mathrm{right}(j_\mathrm{mid}) - \psi_\mathrm{right}(j_\mathrm{mid})\psi'_\mathrm{left}(j_\mathrm{mid})$ changes sign as $E$ passes through an eigenvalue.
5. **Bracket** the sign change, then **bisect** to the desired precision.

The shooting method finds one eigenvalue per bisection run. To find $n$ eigenvalues, run $n$ separate bisection searches, bracketed by coarse sweeps over $E$ that locate the sign changes.

**Trade-offs.** Numerov shooting finds eigenvalues one at a time and requires careful bracketing (missing a bracket misses the eigenvalue). For three to five eigenstates, it is faster to implement than a full diagonalizer. For twenty or more eigenstates, the matrix method is more convenient. For the capstone, Numerov is the self-contained choice; loading math.js is the more powerful one.

### Path B: Matrix diagonalization with math.js

If you add `<script src="https://cdnjs.cloudflare.com/ajax/libs/mathjs/12.4.2/math.min.js"></script>` to the HTML head, you get access to `math.eigs()`, which diagonalizes a matrix. Your CLAUDE.md prompt should explicitly authorize this:

```
The eigensolver may use math.js for matrix diagonalization.
Load math.js from CDN: https://cdnjs.cloudflare.com/ajax/libs/mathjs/12.4.2/math.min.js
Use math.eigs(H_matrix) to get eigenvalues and eigenvectors.
Sort eigenvalues ascending. Normalize each eigenvector by sum_j |psi_j|^2 * h = 1.
```

With math.js, you construct the $N\times N$ tridiagonal matrix as a 2D array, call `math.eigs()`, and get back all eigenvalues and eigenvectors at once. Performance: for $N = 500$, this takes about 0.5–2 seconds in a browser; for $N = 2000$, several seconds. Run the diagonalizer on a "Compute" button press, not on every slider update.

**Recommendation for the capstone.** Build the Numerov shooter first — it exercises more numerical reasoning and requires no external library. If you want all eigenstates at once or find the bracketing tedious, add math.js as a second pass. The chapter's verification rubric works either way.

---

## Time evolution: two unitary methods

### The split-step Fourier method

The time-evolution operator for $\hat{H} = \hat{T} + \hat{V}$ is $e^{-i\hat{H}\Delta t/\hbar}$. Since $\hat{T}$ and $\hat{V}$ do not commute, you cannot split the exponential exactly. The **Trotter-Suzuki decomposition** gives a second-order approximation:

$$e^{-i\hat{H}\Delta t/\hbar} \approx e^{-i\hat{V}\Delta t/(2\hbar)} \cdot e^{-i\hat{T}\Delta t/\hbar} \cdot e^{-i\hat{V}\Delta t/(2\hbar)} + O(\Delta t^3).$$

The algorithm per time step:

1. **Half potential step.** For each grid point $j$: $\psi_j \leftarrow e^{-iV_j\Delta t/(2\hbar)}\psi_j$. Pointwise multiplication — $O(N)$.
2. **FFT.** $\hat{\psi}_k = \mathrm{FFT}[\psi_j]$. $O(N\log N)$.
3. **Full kinetic step.** For each wave-vector $k_m$: $\hat{\psi}_m \leftarrow e^{-i\hbar k_m^2\Delta t/(2m)}\hat{\psi}_m$. Pointwise multiplication — $O(N)$.
4. **IFFT.** $\psi_j = \mathrm{IFFT}[\hat{\psi}_m]$. $O(N\log N)$.
5. **Second half potential step.** $\psi_j \leftarrow e^{-iV_j\Delta t/(2\hbar)}\psi_j$.

Each phase factor $e^{i(\text{something real})}$ is a complex number of modulus exactly 1. Multiplying by it preserves the norm of each component. The FFT and IFFT are also norm-preserving. Therefore, the split-step method is **exactly unitary** — normalization $\int|\psi|^2\,dx$ is preserved to machine precision at every step, not approximately.

The accuracy is $O(\Delta t^2)$ from the Trotter splitting and spectral in space (the FFT represents any function periodic on the grid exactly). The method is unconditionally stable — there is no Courant condition restricting $\Delta t/h^2$. The split-step method was introduced for wave-packet propagation by Feit, Fleck, and Steiger in 1982 and has been the standard ever since. [verify]

**The FFT k-grid ordering — a mandatory flag.** When you call the FFT on an array of length $N$, the output indices $0, 1, \ldots, N-1$ correspond to wave vectors

$$k_m = \frac{2\pi m}{Nh}, \qquad m = 0, 1, \ldots, \frac{N}{2}-1, -\frac{N}{2}, \ldots, -1.$$

The second half of the output (indices $N/2$ through $N-1$) corresponds to *negative* wave vectors. If you apply the kinetic phase $e^{-i\hbar k_m^2\Delta t/(2m)}$ using the raw output index $m$ instead of the physical wave vector $k_m$, you will apply the wrong kinetic energy to the negative-$k$ components and get a wrong answer that may look visually plausible for short times before diverging.

The fix is to use `fftfreq`-style ordering. In JavaScript with fft-js from CDN, after calling `fft(psi_re, psi_im)`, the wave vectors are

```javascript
const k = Array.from({length: N}, (_, m) => {
  const raw = m < N/2 ? m : m - N;
  return 2 * Math.PI * raw / (N * h);
});
```

Then apply $e^{-i\hbar k[m]^2 \Delta t/(2m_\mathrm{particle})}$ using `k[m]`, not `m`. The CLAUDE.md amendment below includes this rule explicitly.

**Absorbing boundaries.** Without special treatment, the wave packet reaches the grid edge and reflects — creating spurious interference that has nothing to do with the physics. Two strategies:

- **Wide grid.** Make the grid wide enough (and $\Delta t$ small enough) that the packet does not reach the boundary in the simulation time window. For a free-particle wave packet with group velocity $v_g$, the boundary is reached at $t \approx (x_\mathrm{max} - x_0)/v_g$. Make the grid five to ten times wider than the packet's initial spread.
- **Complex absorbing potential (CAP).** Add $-iW(x)$ to $V(x)$ near both edges:
  $$W(x) = \begin{cases}\gamma(|x| - x_\mathrm{abs})^2 & |x| > x_\mathrm{abs}\\ 0 & \text{otherwise.}\end{cases}$$
  The imaginary part breaks the Hermiticity of $\hat{H}$ near the edges and damps the wave function. The normalization indicator $\int|\psi|^2\,dx$ will decrease over time when the packet enters the absorbing region — this is correct physics (the packet is "leaving" the domain), not a numerical error. Students should understand this distinction before using CAP.

For the capstone's validation exercises, the wide-grid strategy is simpler and safer for beginners.

### Crank-Nicolson (alternative, boundary-friendly)

The **Crank-Nicolson (CN)** scheme discretizes the TDSE as

$$\left[\hat{I} + \frac{i\Delta t}{2\hbar}\mathbf{H}\right]\psi^{n+1} = \left[\hat{I} - \frac{i\Delta t}{2\hbar}\mathbf{H}\right]\psi^n.$$

This is the **Cayley approximation** $U(\Delta t) \approx (I - \frac{i\Delta t}{2\hbar}H)^{-1}(I + \frac{i\Delta t}{2\hbar}H)^{-1}$... wait, more precisely, the left matrix is the forward factor and the right is the backward factor. Since $\mathbf{H}$ is Hermitian, the numerator and denominator of the Cayley form are complex conjugates, so the update matrix is exactly unitary. Normalization is preserved.

Properties:
- **Second-order accurate** in both time ($O(\Delta t^2)$) and space ($O(h^2)$).
- **Unconditionally stable** — no CFL condition.
- **Exactly unitary** for Hermitian $\mathbf{H}$.
- Each step requires solving a tridiagonal linear system $\mathbf{A}\psi^{n+1} = \mathbf{b}$, solvable in $O(N)$ via the Thomas algorithm.

CN is the method recommended by the book's `CLAUDE.md` baseline for time evolution. It is preferred for problems with hard walls (Dirichlet boundary conditions are natural for the tridiagonal system) and when you want to avoid FFTs. Split-step Fourier is easier for problems on large periodic domains.

**Why explicit Euler is forbidden.** The explicit Euler scheme updates $\psi^{n+1} = \psi^n - (i\Delta t/\hbar)\mathbf{H}\psi^n$. The update matrix is $\mathbf{I} - (i\Delta t/\hbar)\mathbf{H}$, whose eigenvalues are $1 - (i\Delta t E_n/\hbar)$, with modulus $\sqrt{1 + (\Delta t E_n/\hbar)^2} > 1$ for every $E_n \neq 0$. Normalization grows exponentially at every step — the scheme is unconditionally unstable, blows up in fewer than 100 steps for typical parameters, and must never be used for the Schrödinger equation. The normalization indicator in the corner of the sandbox will detect this immediately: if the indicator drifts above $1.001$, the time-stepper is wrong.

---

## The "defend the physics" rubric

Building the sandbox is half the project. The other half is demonstrating that it computes correct physics. Here is the validation checklist — each item has a specific numerical check.

### Check 1: Units

Every displayed quantity must carry correct units. This is not decoration; a program that displays energy in the wrong units is computing the wrong answer. Default choice for undergraduate quantum: $\hbar = 1.0545\times10^{-34}$ J·s, $m_e = 9.109\times10^{-31}$ kg, distances in nm, energies in eV. Alternatively, use atomic units ($\hbar = 1$, $m_e = 1$, $a_0 = 1$ bohr). Either is fine; commit to one and label every axis.

Sanity check: for an infinite square well of width $L = 1$ nm, the ground-state energy is $E_1 = \pi^2\hbar^2/(2m_e L^2)$. In SI units this is about $0.376$ eV. If your code reports $376$ eV or $0.000376$ eV, there is a units error.

### Check 2: Normalization

For every eigenstate the solver returns:

$$\sum_{j=0}^{N-1} |\psi_j|^2 \cdot h = 1.000 \pm 0.001.$$

If this fails, the eigenvectors came back unnormalized (some eigensolvers return unit-norm vectors in the Euclidean sense, not the $h$-weighted sense; check and rescale). The normalization indicator should always be visible in the corner.

During time evolution, the normalization indicator must stay within $\pm 0.001$ of $1.000$ at every frame. If it drifts, the time-stepper is broken.

### Check 3: Orthogonality

For any two eigenstates $\psi_n$ and $\psi_m$ with $n \neq m$:

$$\left|\sum_j \psi_j^{(n)*}\psi_j^{(m)} \cdot h\right| < 10^{-8}.$$

Violation signals a bug in the eigensolver or a floating-point overflow from un-normalized eigenvectors.

### Check 4: Infinite-square-well spectrum (primary benchmark)

Set $V(x) = 0$ for $x \in (0, L)$, $V = V_\infty$ (very large, e.g. $10^{10}$ in your energy units) at the boundaries (or enforce $\psi_0 = \psi_{N-1} = 0$ directly). Run the eigensolver with $N = 500$.

The analytic spectrum is

$$\boxed{E_n = \frac{n^2\pi^2\hbar^2}{2mL^2}, \qquad n = 1, 2, 3, \ldots}$$

Report a comparison table:

| $n$ | $E_n^\mathrm{analytic}$ (eV) | $E_n^\mathrm{numerical}$ (eV) | fractional error |
|---|---|---|---|
| 1 | $\ldots$ | $\ldots$ | $< 10^{-5}$ |
| 2 | $\ldots$ | $\ldots$ | $< 10^{-4}$ |
| 5 | $\ldots$ | $\ldots$ | $< 10^{-3}$ |
| 10 | $\ldots$ | $\ldots$ | $< 1\%$ |

The fractional error grows as $n^2$ (because the central-difference error for the $n$-th mode is $\propto (n\pi h/L)^2$). For $N = 500$ and $n = 1$ the error is around $3\times10^{-7}$; for $n = 10$ around $3\times10^{-5}$ — both well within the 1% threshold.

If the $n=1$ fractional error is around $1/N^2$, you have an $h$ vs. $h^2$ bug in the diagonal: the kinetic term should be $\hbar^2/(mh^2)$, not $\hbar^2/(mh)$.

### Check 5: Harmonic oscillator

Set $V(x) = \frac{1}{2}m\omega^2 x^2$ on a grid wide enough to contain the lowest ten states ($x \in [-6x_0, 6x_0]$ where $x_0 = \sqrt{\hbar/m\omega}$). The analytic spectrum:

$$E_n = \hbar\omega\!\left(n + \tfrac{1}{2}\right), \qquad n = 0, 1, 2, \ldots$$

Verify: (a) ground-state energy $E_0 = \hbar\omega/2$; (b) level spacing constant at $\hbar\omega$; (c) ground-state wave function shape Gaussian with width $x_0$; (d) ground-state uncertainty product $\sigma_x\sigma_p = \hbar/2$ (the harmonic oscillator ground state saturates the Kennard bound — a direct connection to Chapters 1 and 10).

### Check 6: Free-particle time evolution

Set $V(x) = 0$ everywhere. Initialize to a Gaussian wave packet:

$$\psi(x, 0) = \left(\frac{1}{\pi a^2}\right)^{1/4}\exp\!\left(-\frac{(x-x_0)^2}{2a^2}\right)\exp(ik_0 x).$$

The analytic time evolution gives a packet centered at $x(t) = x_0 + \hbar k_0 t/m$ with spreading width $\sigma(t)^2 = a^2/2 + \hbar^2 t^2/(2m^2 a^2)$.

Run for several spreading times. Compare the numerical centroid and width to the analytic formulas. Both should agree to within 1% if the grid is wide enough and the time step small enough.

### Check 7: Energy conservation

Under time evolution with any time-independent $V(x)$, the expectation value

$$\langle\hat{H}\rangle(t) = \sum_j \psi_j^*(t)\,(H_\mathrm{matrix}\,\vec{\psi}(t))_j\cdot h$$

should be constant. Compute it at $t = 0$ and at $t = T$. The fractional drift $|\langle\hat{H}\rangle(T) - \langle\hat{H}\rangle(0)|/|\langle\hat{H}\rangle(0)|$ should be below $0.1\%$ for the simulation time window.

If $\langle\hat{H}\rangle$ drifts upward, the time-stepper is not unitary — the most likely cause is explicit Euler.

---

## What each chapter contributed

The sandbox is an integration project. Here is the ledger:

| Sandbox feature | Chapter(s) |
|---|---|
| $\psi$ displayed as Re $\psi$, Im $\psi$, $|\psi|^2$ panels | Ch. 1 (Born rule, complex structure) |
| Normalization indicator $\int|\psi|^2\,dx = 1.000$ | Ch. 1 (continuity equation, preservation) |
| Potential $V(x)$ on a grid | Ch. 2 (TISE, stationary states) |
| Eigenvalue problem, bound states | Ch. 2–5 |
| Classical turning points marked | Ch. 3, 4 (tunneling, forbidden regions) |
| Eigenfunction shapes (ISW, HO) | Ch. 5, 7 (infinite well, harmonic oscillator) |
| Wave-packet initial condition | Ch. 8 (free particle, Gaussian wave packet) |
| Momentum display $|\phi(p)|^2$ | Ch. 1 (Fourier duality), Ch. 8 |
| $\sigma_x$, $\sigma_p$ from eigenstate | Ch. 9 (operators, Robertson bound) |
| $\langle\hat{H}\rangle$ computation | Ch. 9 (Hamiltonian expectation value) |
| Time evolution, wave packet dynamics | Ch. 8, Ch. 2 (stationary states sum) |
| Measurement statistics on eigenstate | Ch. 11 (Born rule, collapse preview) |

Nothing in the sandbox is new physics. Every feature is an application of a tool you already have. The synthesis is the point.

---

## The algorithm, in one place

Here is the full eigensolver algorithm in enough detail to write the code:

**Input:** grid $(x_j)_{j=0}^{N-1}$, spacing $h$, potential array $(V_j)$, constants $\hbar$, $m$, number of desired eigenvalues $n_\mathrm{eig}$.

**Step 1:** Construct $\mathbf{H}$.

```
t = hbar^2 / (2 * m * h^2)            # kinetic hopping coefficient
H[j, j]     = 2*t + V[j]              # diagonal
H[j, j+1]   = -t                      # upper off-diagonal
H[j+1, j]   = -t                      # lower off-diagonal
```

(Interior points $j = 1, \ldots, N-2$ only; the boundary rows/columns are removed to enforce $\psi_0 = \psi_{N-1} = 0$.)

**Step 2:** Diagonalize (math.js path).
```
const result = math.eigs(H);
const energies = result.values;   // array of N-2 eigenvalues
const vectors  = result.vectors;  // columns are eigenvectors
```
Sort by ascending energy. Take the first $n_\mathrm{eig}$ pairs.

**Step 3:** Normalize.
```
for each eigenvector psi_vec:
  norm = sum_j |psi_vec[j]|^2 * h
  psi_vec = psi_vec / sqrt(norm)
```

**Step 4:** Display.
- Energy levels as horizontal lines on the potential plot at height $E_n$.
- Wave function plots (Re $\psi$, $|\psi|^2$) offset vertically by $E_n$ for visual clarity.
- Numerical table: $E_n$, $\sigma_x$, $\sigma_p$, $\sigma_x\sigma_p/(\hbar/2)$.

---

## Worked example: the sandbox runs the sandbox

Let the sandbox solve the sandbox. Here is a concrete sequence you should be able to run end-to-end and reproduce the numbers.

**Setup.** Infinite square well, $L = 2$ nm, $m = m_e$, $N = 500$, energy unit eV.

The analytic energies:

$$E_n = \frac{n^2\pi^2\hbar^2}{2m_e L^2} = n^2 \times \frac{\pi^2 (1.0545\times10^{-34})^2}{2(9.109\times10^{-31})(2\times10^{-9})^2} \approx n^2 \times 0.0940\ \mathrm{eV}.$$

So $E_1 \approx 0.094$ eV, $E_2 \approx 0.376$ eV, $E_3 \approx 0.846$ eV, $E_4 \approx 1.503$ eV, $E_5 \approx 2.349$ eV.

**The ratio test.** The ratios $E_n/E_1$ should be exactly $n^2$: $E_2/E_1 = 4$, $E_3/E_1 = 9$, $E_4/E_1 = 16$, $E_5/E_1 = 25$. These ratios are dimensionless and do not depend on any physical constant or unit choice — they depend only on the numerics. If they are correct, the grid and eigenvalue algorithm are working. If $E_2/E_1 \approx 4.01$ or $\approx 3.99$, the fractional error is 0.25% — within spec. If it is $\approx 2$, you have an $n$ vs $n^2$ bug.

**The normalization test.** Compute $\sum_j |\psi_1^{(j)}|^2 \cdot h$ for the ground-state eigenvector returned by math.js. Before rescaling, this may be $1/h$ or $1$ depending on the solver's convention. After multiplying by $1/\sqrt{\text{norm}}$, it must read $1.000$.

**The limit.** Go to high modes. At $n = 20$, the fractional error in $E_{20}$ from the $O(h^2)$ central difference is $\approx (20\pi/500)^2/12 \approx 1.3\%$ — just over the 1% threshold. If you switch to the Numerov method (which achieves $O(h^6)$), the error at $n = 20$ with $N = 500$ drops to negligible. This is the payoff for understanding the difference between the methods.

---

## Common failure modes

**1. Explicit Euler time evolution.** Normalization blows up within 50 steps. The normalization indicator in the corner catches this immediately. Use Crank-Nicolson or split-step.

**2. The kinetic coefficient.** The diagonal element is $\hbar^2/(mh^2)$, not $\hbar^2/(2mh^2)$. Confusing $t = \hbar^2/(2mh^2)$ (the hopping coefficient) with the diagonal entry $2t$ is the most common bug. If $E_1$ is wrong by a factor of 2, this is why.

**3. Missing the $h^2$ in the denominator.** Writing `h` instead of `h*h` in the kinetic coefficient. If $E_1$ scales as $1/N$ instead of $1/N^2$, the grid spacing is wrong.

**4. Unnormalized eigenvectors.** math.js returns unit-norm vectors in the Euclidean sense: $\sum_j |\psi_j|^2 = 1$. The physics normalization requires $\sum_j |\psi_j|^2 \cdot h = 1$. Divide by $\sqrt{h}$ (not $h$!) to convert.

**5. FFT k-grid ordering.** As described above: indices $N/2$ through $N-1$ in the FFT output correspond to negative wave vectors. Apply the physical $k$ values (with the sign flip for the second half), not the raw index. If the time evolution looks correct for $t < 10$ steps and then goes wrong, this is likely the bug.

**6. Grid too narrow.** For bound-state problems, the wave function must decay to zero well before the boundary. For a harmonic oscillator, use $x_\mathrm{max} \geq 5x_0$. For a finite square well, use $x_\mathrm{max} \geq x_\mathrm{well-edge} + 5/\kappa$ where $\kappa = \sqrt{2m(V_0-E)}/\hbar$ is the tunneling decay constant. Failure: the eigenvalues are slightly wrong and the wave function looks truncated at the edge.

**7. Spurious reflection in time evolution.** The wave packet hits the grid boundary and bounces back. Make the grid wide enough (five to ten packet widths extra on each side) or add a complex absorbing potential.

**8. Performance.** math.js diagonalizing a 2000×2000 matrix takes 5–20 seconds. For interactive exploration, use $N = 500$. Put the eigensolver behind a "Compute" button, not on every slider event.

---

## Project rubric: defending the physics

Submit your sandbox (`12-quantum-sandbox.html`) and a brief write-up (200–400 words) documenting your validation results. The rubric:

| Criterion | Points | How to demonstrate |
|---|---|---|
| Units labeled correctly on all axes | 10 | Read off $E_1$ for ISW in eV; match to analytic formula |
| Normalization $\int|\psi|^2\,dx = 1.000 \pm 0.001$ | 15 | Screenshot normalization indicator for two eigenstates |
| Orthogonality $|\langle\psi_n|\psi_m\rangle| < 10^{-8}$ | 10 | Report computed value for $(n,m) = (1,2)$ and $(1,3)$ |
| ISW energy spectrum: fractional error $< 1\%$ for $n = 1\ldots5$ | 20 | Table of analytic vs. numerical energies |
| Harmonic oscillator: level spacing uniform to $< 1\%$ | 15 | Report $E_1 - E_0$, $E_2 - E_1$ in units of $\hbar\omega$ |
| Free-particle time evolution: centroid and width match analytic to $< 1\%$ | 15 | Plot of $\sigma(t)$ numerical vs analytic at three times |
| Energy conservation under TDSE to $< 0.1\%$ | 10 | Report $\langle\hat{H}\rangle$ at $t = 0$ and $t = T$ |
| Exploration of a non-standard potential | 5 | Any valid $V(x)$ with physically sensible output described in write-up |
| **Total** | **100** | |

---

## Still puzzling

**Why Crank-Nicolson and split-step give slightly different answers.** Both are second-order in time and unitary. But the leading error term is not the same. For smooth potentials without hard walls, split-step tends to be more accurate for a given $\Delta t$ because its spatial representation is spectral (the FFT represents the function exactly for a given $N$), while Crank-Nicolson still has $O(h^2)$ spatial errors. For hard-wall potentials (infinite well), the discontinuity at the boundary couples many Fourier modes and the spectral advantage of split-step disappears; CN is cleaner. The "right" method depends on the problem.

**What the eigensolver is actually doing.** Diagonalizing a real symmetric matrix is equivalent to finding a rotation in $\mathbb{R}^{N}$ that brings the matrix to diagonal form. For the tridiagonal Hamiltonian, LAPACK's `dsyev` routine uses a sequence of Householder reflections and QR iterations, each of which is a product of unitary matrices. The full algorithm is not obvious. Math.js wraps it without exposing the internals. If you want to understand what is happening, read Trefethen and Bau, *Numerical Linear Algebra* (1997), Ch. 29–31. [verify]

**Band structure and the Kronig-Penney model.** For a periodic potential (an array of square wells), the eigenstates of the infinite lattice are Bloch waves, not bound states. The spectrum forms energy bands separated by gaps. The sandbox as described finds bound states of a finite system; to compute band structure you need periodic boundary conditions (which changes the tridiagonal matrix to a circulant matrix) and Bloch's theorem. This is Vol. 2 material, but the sandbox's infrastructure is the same.

**2D extension.** The Schrödinger equation in two dimensions separates (for separable potentials $V(x,y) = V_x(x) + V_y(y)$) into two 1D problems. For a general 2D potential, the Hamiltonian matrix is $(N_x \cdot N_y) \times (N_x \cdot N_y)$ — a $250000\times250000$ matrix for $N_x = N_y = 500$. Full diagonalization is infeasible; iterative methods (Lanczos, Arnoldi) are needed. For time evolution, 2D split-step works cleanly with two sequential FFT passes. This too is Vol. 2.

**Scattering and the transmission coefficient.** Time-evolving a Gaussian packet incident on a barrier gives a transmitted pulse and a reflected pulse whose areas are $T$ and $R = 1-T$. Comparing to the analytic transmission coefficient $T(E)$ is beautiful but requires careful accounting: the packet has a distribution of momenta (a width $\sigma_k$ in $k$-space), so the numerical $T$ is an integral of $T(E)$ over the packet's momentum distribution. The sandbox can do this, but the interpretation requires a careful discussion — one worth leaving to a dedicated scattering chapter.

---

## The +1 — Simulation Exercise (The Capstone Build)

This chapter's "+1" is the sandbox itself. There is no separate toy to build — the sandbox is the project. The simulation prompt below is the deliverable.

### Part A — CLAUDE.md amendment

Before running the prompt, add this stanza to your `CLAUDE.md`:

````markdown
## Chapter 12 — 1D Quantum Sandbox

EIGENSOLVER RULES:
- Hamiltonian matrix is real, symmetric, tridiagonal.
  Diagonal: H[j,j] = hbar^2 / (m * h^2) + V[j].   ← Note: 2*(hbar^2/(2m*h^2))
  Off-diagonal: H[j,j±1] = -hbar^2 / (2*m*h^2).
- Boundary conditions: Dirichlet. ψ[0] = ψ[N-1] = 0.
  Build the (N-2) × (N-2) interior matrix only.
- If using math.js: load from CDN. Call math.eigs(H_interior).
  Sort eigenvalues ascending. Normalize eigenvectors by
    norm = sum_j |psi_j|^2 * h;  psi_j /= sqrt(norm).
- Validation: run infinite-square-well L=2nm at startup.
  E_1 analytic ≈ 0.094 eV (m=m_e). Report fractional error.

TIME EVOLUTION RULES:
- Use Crank-Nicolson OR split-step Fourier. NEVER explicit Euler.
- Explicit Euler test: if normalization indicator exceeds 1.005 after
  10 steps, abort and display "Time stepper error: use CN or SSFM."
- Split-step FFT k-grid: after FFT, wave vectors are
    k[m] = (2*pi / (N*h)) * (m < N/2 ? m : m - N)
  Apply kinetic phase exp(-i * hbar * k[m]^2 * dt / (2*m_particle)) using k[m], not m.
- Absorbing boundaries (optional): add -i*gamma*(|x|-x_abs)^2 to V
  near both edges if the packet reaches the wall. Normalization will
  decrease — this is correct, label it "flux absorbed at boundary."
- Energy conservation: compute <H> = sum_j psi_j* (H @ psi)_j * h
  at each frame. Display in the side panel. Should vary < 0.1%.

KNOWN FAILURE MODES:
(a) h vs h^2 in kinetic coefficient → E_1 ∝ 1/N (not 1/N^2). Validation catches it.
(b) Unnormalized eigenvectors → norm = 1/h instead of 1. Multiply eigenvector by 1/sqrt(h).
(c) Explicit Euler → norm blows up. Normalization indicator catches it.
(d) FFT k-ordering → wrong kinetic phase for k < 0 components. Pack correct k array.
(e) Grid too narrow → eigenstates truncated. Use grid width > 5*(well width + 1/kappa).
````

### Part B — The simulation prompt

````
SHOW.
The time-independent Schrödinger equation as a matrix eigenvalue problem:
  H_matrix * psi_vec = E * psi_vec
  Diagonal:    H[j,j]   = hbar^2 / (m * h^2) + V[j]
  Off-diagonal: H[j,j±1] = -hbar^2 / (2 * m * h^2)
  Boundary:    Dirichlet (psi[0] = psi[N-1] = 0).

Split-step Fourier time evolution (one step):
  1. psi[j] *= exp(-i * V[j] * dt / (2 * hbar))            [half V step]
  2. psi_hat = FFT(psi)
  3. psi_hat[m] *= exp(-i * hbar * k[m]^2 * dt / (2*m))   [full T step]
     where k[m] = (2*pi/(N*h)) * (m < N/2 ? m : m - N)
  4. psi = IFFT(psi_hat)
  5. psi[j] *= exp(-i * V[j] * dt / (2 * hbar))            [half V step]

Validation: infinite square well L, width L=2nm, m=m_e.
  E_n = n^2 * pi^2 * hbar^2 / (2 * m_e * L^2).
  E_1 ≈ 0.094 eV, E_2/E_1 = 4, E_3/E_1 = 9, E_4/E_1 = 16, E_5/E_1 = 25.

SAY.
Produce a single file `12-quantum-sandbox.html`.

Layout (SVG 1200 x 750):

Top: mode selector (two radio buttons: "Eigensolver" | "Time Evolution").

EIGENSOLVER MODE:
  Left panel (600 x 650): potential + eigenstates plot.
    - V(x) in red.
    - Energy levels E_n as horizontal green dashed lines.
    - Eigenfunctions |ψ_n(x)|^2 filled in blue, offset vertically by E_n.
    - Classical turning points as dots on the potential curve.
    - x-axis labeled in nm; y-axis labeled in eV.

  Right panel (600 x 650):
    - Potential preset menu: Infinite Square Well / Harmonic Oscillator /
      Finite Square Well / Double Well / Custom (text input for V(x)).
    - Sliders for potential parameters (well width L, depth V₀, omega, etc.).
    - N slider: 100, 250, 500, 1000 (run on button press for N > 250).
    - "Compute eigenstates" button.
    - Output table: n, E_n (eV), E_n/E_1, fractional error vs analytic (where known).
    - Normalization indicator per eigenstate: sum |psi_j|^2 * h.
    - sigma_x and sigma_p for displayed eigenstate (from expectation values).

TIME EVOLUTION MODE:
  Main panel (800 x 500): wave packet animation.
    - Three stacked SVG panels sharing x-axis:
        Top:    Re ψ(x,t)   in orange
        Middle: Im ψ(x,t)   in gray dashed
        Bottom: |ψ(x,t)|^2  in blue filled, with V(x) in red behind it.
    - Normalization indicator top-right corner (must stay 1.000±0.001).
    - <H> display (energy conservation check).

  Right panel (400 x 500): controls.
    - Initial state selector: Gaussian wave packet / Eigenstate superposition.
    - Gaussian sliders: x_0 (center), a (width), k_0 (wave vector).
    - Potential preset (same menu as eigensolver mode).
    - dt slider (0.01 to 1 fs). Grid width selector.
    - Play / Pause / Reset buttons.
    - Time display (in fs).

CONSTRAIN.
- D3 v7 from CDN. SVG only. Vanilla JS.
- N = 500 default. Eigensolver behind "Compute" button for N > 250.
- math.js from CDN for eigensolver.
- fft-js from CDN for split-step FFT (or implement the FFT manually).
- Default potential: infinite square well L = 2 nm.
- Absorbing boundaries optional; document if implemented.
- Energy units: eV. Length units: nm. Mass: m_e.
- Comments at every non-trivial physics step (the student must be able
  to read the code and understand the physics, not just the algorithm).

VERIFY.
After writing the file, confirm:
(a) Infinite square well L = 2 nm, N = 500: E_1 ≈ 0.094 eV, E_2/E_1 = 4,
    E_3/E_1 = 9. Fractional errors all below 0.01%.
(b) All eigenstates: normalization indicator reads 1.000 ± 0.001.
(c) Free-particle Gaussian time evolution: centroid advances at v_g = hbar*k_0/m_e;
    width sigma(t) increases from a/sqrt(2) per the analytic formula.
    At t = 10 fs with a = 0.5 nm, k_0 = 5 nm^-1: centroid moved by hbar*k_0*t/m_e.
(d) Energy conservation: <H> constant to 0.1% over 100 time steps.
````

### Part C — Exploration tasks

**Benchmark the solver.** Run the infinite-square-well eigensolver at $N = 100$, $250$, $500$. Record $E_1$ and compute the fractional error against the analytic value $0.094$ eV. Does the error decrease as $1/N^2$? (It should, because the central-difference approximation is $O(h^2) = O(1/N^2)$.) Record your results in a table.

**Watch bound states appear.** Switch to the finite square well preset. Set $V_0 = 1$ eV, $L = 1$ nm. Note how many bound states exist. Now increase $V_0$ to $2$ eV, $5$ eV, $10$ eV. Watch new bound states appear. Analytically, for a 1D finite well, at least one bound state always exists regardless of how shallow the well. Does your solver confirm this for $V_0 = 0.01$ eV?

**The double well.** Select the double-well preset with two wells of width $0.5$ nm separated by a barrier of width $0.3$ nm. Note the ground state (symmetric) and first excited state (antisymmetric). Their energy difference $\Delta E = E_1 - E_0$ is the tunnel splitting. Now double the barrier width to $0.6$ nm and watch $\Delta E$ decrease. The tunnel splitting decreases exponentially with barrier width — a direct consequence of quantum tunneling (Chapter 6). Does your simulation show this?

**Free particle spreading.** In time-evolution mode, set $V = 0$ and prepare a Gaussian with $a = 0.3$ nm, $k_0 = 10\ \mathrm{nm}^{-1}$. Run for $20$ fs. The analytic width: $\sigma(t) = \sqrt{(a^2/2) + (\hbar t)^2/(2m_e^2 a^2)}$. Read off $\sigma(t)$ numerically at $t = 5$, $10$, $15$ fs by fitting a Gaussian to $|\psi|^2$. Plot numerical vs. analytic. They should agree to within 1%.

**Scattering in time evolution.** Set $V(x) = V_0$ for $|x| < 0.2$ nm (a narrow barrier), $V_0 = 0.3$ eV. Prepare a wave packet centered at $x = -3$ nm, $k_0 = 5\ \mathrm{nm}^{-1}$ (kinetic energy $\approx 0.15$ eV $< V_0$). Watch the wave packet hit the barrier, split into a transmitted and reflected portion. Estimate $R$ and $T$ from the areas under $|\psi|^2$ after the packet has split. Compare to the analytic transmission coefficient for a square barrier (Chapter 6 formula). They will not match exactly (the packet is not a plane wave), but they should be in the same ballpark.

**Energy conservation as a diagnostic.** In time-evolution mode, intentionally switch to explicit Euler (if the code allows it as an option, or implement it as a test). Watch the normalization indicator climb above 1 within 20 steps. Then switch to Crank-Nicolson or split-step. The normalization indicator stays at 1.000. This is the most visceral demonstration of why the choice of time-stepper matters.

---

## References

- Feit, M.D., Fleck, J.A., Jr., and Steiger, A. (1982). "Solution of the Schrödinger equation by a spectral method." *Journal of Computational Physics*, 47, 412–433. [verify] [The original split-step Fourier method for quantum wave-packet propagation.]
- Koonin, S.E. and Meredith, D.C. (1990). *Computational Physics*. Addison-Wesley. [verify] [Ch. 3–4; the finite-difference Schrödinger solver as an undergraduate project, still one of the best treatments.]
- Press, W.H., Teukolsky, S.A., Vetterling, W.T., and Flannery, B.P. (2007). *Numerical Recipes*, 3rd ed. Cambridge University Press. Ch. 19, 20. [verify] [The Thomas algorithm for tridiagonal systems; TISE as an eigenvalue problem.]
- Blatt, J.M. (1967). "Practical points concerning the solution of the Schrödinger equation." *Journal of Computational Physics*, 1, 382–396. [verify] [Early treatment of the Numerov shooting method for bound-state eigenvalues; the primary Numerov reference.]
- Pfahnl, A.W. (2022). "Finite Difference Method for Visualizing Quantum Mechanics." *Journal of Chemical Education*, 99, 3647–3655. DOI: 10.1021/acs.jchemed.2c00557. [verify] [Finite-difference eigensolver designed specifically for visualization in undergraduate courses; directly relevant as a pedagogical reference.]
- Trefethen, L.N. and Bau, D. (1997). *Numerical Linear Algebra*. SIAM. Ch. 29–31. [verify] [The QR algorithm and its convergence; background for what math.js is doing under the hood.]
- Tokmakoff, A. *Time-Dependent Quantum Mechanics and Spectroscopy*. Chemistry LibreTexts. §1.5: "Numerically Solving the Schrödinger Equation." https://chem.libretexts.org/ [verify] [The Numerov method discussion, accessible and well-annotated.]
- Griffiths, D.J. and Schroeter, D.F. (2018). *Introduction to Quantum Mechanics*, 3rd ed. Cambridge University Press. Ch. 2. [The standard analytic reference for ISW, HO, and finite well that the sandbox validates against.]
