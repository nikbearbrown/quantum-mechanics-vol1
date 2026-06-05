# Worked Exercises: Capstone — A 1D Quantum Sandbox

*Chapter 11 of Quantum Mechanics — Volume 1*

> These exercises follow a research-backed sequence: full worked example → matched practice → completion problem → error-recognition → transfer → interleaved review. Each section builds on the previous. Do not skip ahead.

## Prerequisites

- You can discretize the TISE on a grid: the central-difference Hamiltonian is tridiagonal with diagonal $2t_k + V_j$ and off-diagonal $-t_k$, where $t_k = \hbar^2/(2mh^2)$ — and you know the diagonal is $2t_k$, not $t_k$.
- You know why a time-stepper must be **unitary**: $e^{-i\hat Ht/\hbar}$ preserves the norm exactly, explicit Euler does not (its update matrix has eigenvalue modulus $\sqrt{1 + (\Delta t E_k/\hbar)^2} > 1$), and Crank–Nicolson / split-step are unitary by construction.
- You can read the **normalization indicator** $\sum_j|\psi_j|^2 h$ as a correctness check (must stay $1.000 \pm 0.001$), and you know the split-step FFT $k$-grid requires the sign-flip $k_m = (2\pi/Nh)\cdot(m$ for $m<N/2$, else $m-N)$.

## Part A — Full Worked Example

**What this demonstrates:** That an explicit/forward-Euler stepper is non-unitary and amplifies the norm every step, while the Crank–Nicolson Cayley update is exactly unitary — and that the normalization indicator detects the difference numerically within a handful of steps.

**The problem:** Time-evolve a single energy eigenstate $\Psi^0 = \psi_E$ (with $\hat H\psi_E = E\psi_E$) by one time step $\Delta t$ using (i) explicit Euler and (ii) Crank–Nicolson. For each, compute the exact factor by which the norm $\|\Psi\|^2$ changes per step, then evaluate it numerically for an electron in a well where $E = 0.376$ eV and $\Delta t = 0.01$ fs. Decide which stepper the normalization indicator certifies.

**The solution:**

**Step 1 — Write each update as a matrix acting on the eigenstate.** Explicit Euler: $\Psi^{n+1} = (\mathbf I - \tfrac{i\Delta t}{\hbar}\mathbf H)\Psi^n$. Crank–Nicolson: $(\mathbf I + \tfrac{i\Delta t}{2\hbar}\mathbf H)\Psi^{n+1} = (\mathbf I - \tfrac{i\Delta t}{2\hbar}\mathbf H)\Psi^n$, i.e. $\Psi^{n+1} = (\mathbf I + \tfrac{i\Delta t}{2\hbar}\mathbf H)^{-1}(\mathbf I - \tfrac{i\Delta t}{2\hbar}\mathbf H)\Psi^n$.

*Why:* On an eigenstate, every $\mathbf H$ becomes a scalar $E$, so each update matrix becomes a complex number multiplying $\Psi^n$ — and the per-step norm factor is just $|{\rm that\ number}|^2$.
*Check:* Both updates reduce to scalars on an eigenstate; this is the cleanest case in which to read off stability, exactly the setup the chapter's "Why explicit Euler is forbidden" argument uses.

**Step 2 — Compute the Euler per-step norm factor.** On the eigenstate, the Euler multiplier is $\mu_E = 1 - i\,\Delta t E/\hbar$, so

$$\frac{\|\Psi^{n+1}\|^2}{\|\Psi^n\|^2} = |\mu_E|^2 = 1 + \left(\frac{\Delta t E}{\hbar}\right)^2 > 1.$$

*Why:* $|1 - ix|^2 = 1 + x^2$ for real $x$; the imaginary part forced by the $-i$ in the Schrödinger equation pushes the modulus above 1, so the norm grows every step regardless of how small $\Delta t$ is.
*Check:* As $\Delta t \to 0$ the growth factor $\to 1$ but never equals 1 for $E \neq 0$ — the instability is unconditional, matching the chapter's claim that "explicit Euler is unconditionally unstable."

**Step 3 — Compute the Crank–Nicolson per-step norm factor.** On the eigenstate, the multiplier is $\mu_{CN} = \dfrac{1 - i\Delta t E/2\hbar}{1 + i\Delta t E/2\hbar}$, so

$$|\mu_{CN}|^2 = \frac{1 + (\Delta t E/2\hbar)^2}{1 + (\Delta t E/2\hbar)^2} = 1\quad\text{exactly.}$$

*Why:* Numerator and denominator are complex conjugates (because $\mathbf H$ is Hermitian, so $E$ is real), giving equal moduli — the Cayley transform of a Hermitian operator is unitary, so the norm is preserved to machine precision for any $\Delta t$.
*Check:* $|\mu_{CN}| = 1$ means the normalization indicator reads exactly $1.000$ every frame — the signature of a correct (unitary) stepper.

**Step 4 — Put in numbers.** Convert: $E = 0.376\ \text{eV} = 6.02\times10^{-20}\ \text{J}$, $\hbar = 1.055\times10^{-34}\ \text{J·s}$, $\Delta t = 0.01\ \text{fs} = 1.0\times10^{-17}\ \text{s}$. Then

$$\frac{\Delta t E}{\hbar} = \frac{(1.0\times10^{-17})(6.02\times10^{-20})}{1.055\times10^{-34}} \approx 5.71\times10^{-3}.$$

Euler per step: $|\mu_E|^2 = 1 + (5.71\times10^{-3})^2 \approx 1 + 3.26\times10^{-5}$. Over 50 steps the norm grows by $\approx (1+3.26\times10^{-5})^{50} - 1 \approx 1.6\times10^{-3}$ — already past the $0.001$ tolerance. Crank–Nicolson per step: exactly $1.000$.

*Why:* A small per-step growth compounds; 50 steps of a $1.0000326\times$ amplifier pushes the indicator above $1.001$, which is the chapter's stated detection threshold ("if it reads above 1.001 after ten steps... the time-stepper is wrong"). With realistic eigenstate superpositions the highest-energy components ($E_k$ large) blow up far faster.
*Check:* Dimensionally $\Delta t E/\hbar$ is (s)(J)/(J·s) = dimensionless — a phase, as it must be. The Euler norm drift is positive (creates probability); a complex absorbing potential would instead make it negative.

**Final answer:** Per step, explicit Euler multiplies $\|\Psi\|^2$ by $1 + (\Delta t E/\hbar)^2 \approx 1.0000326 > 1$ (norm climbs above $1.001$ within $\sim$50 steps for this $E$, faster for high-energy components), while Crank–Nicolson multiplies by exactly $1.000$. The normalization indicator certifies Crank–Nicolson and condemns Euler.

**What made this work:** The central concept is **unitarity of the propagator** $e^{-i\hat Ht/\hbar}$ and its Cayley approximation. The naive failure is to assume that a "small" time step makes explicit Euler "good enough" — but the modulus $|1 - i\Delta t E/\hbar|^2 = 1 + (\Delta t E/\hbar)^2$ exceeds 1 for **every** $\Delta t > 0$, so the error is in the *structure* of the method, not its step size. Crank–Nicolson works because conjugate numerator/denominator give $|\mu| = 1$ identically. The normalization indicator is the on-screen sensor that turns this abstract fact into an immediate, visible failure.

**Self-explanation prompt:** Explain why making $\Delta t$ ten times smaller does not rescue explicit Euler — and why the normalization indicator is a *sufficient* test to reject a stepper even before you check whether the dynamics look physically reasonable.

## Part B — Matched Practice Problem

**What this demonstrates:** The same unitarity analysis applied to a **different non-unitary scheme** (implicit/backward Euler) and contrasted with the unitary split-step Fourier method — different surface, same principle.

**The problem:** Consider **implicit (backward) Euler**: $(\mathbf I + \tfrac{i\Delta t}{\hbar}\mathbf H)\Psi^{n+1} = \Psi^n$, so on an eigenstate $\Psi^{n+1} = (1 + i\Delta t E/\hbar)^{-1}\Psi^n$.

(a) Compute the per-step norm factor $|\mu|^2$ and show it is **less than 1** for $E \neq 0$ (this scheme *destroys* probability). (b) Explain what the normalization indicator would read after many steps and why "the norm decays smoothly" is still a failure, not a feature. (c) For the split-step Fourier method, each of the three sub-steps multiplies $\psi$ by a phase of modulus exactly 1; argue from this alone that split-step is unitary, and state the one implementation detail (the FFT $k$-grid) that, if wrong, breaks the dynamics even though the norm stays near 1.

**Stuck?** $|1 + ix|^{-1}|^2 = 1/(1 + x^2) < 1$ for real $x \neq 0$ — backward Euler is the mirror image of forward Euler, damping instead of amplifying. For (c), recall that a complex absorbing potential is the *only* legitimate reason the split-step norm should drop; an undamped free packet must hold the norm at $1.000$.

*Instructor note: No solution is provided for Part B. Carry out all three parts and predict the normalization-indicator behavior for each scheme before checking against any code.*

## Part C — Completion Problem

**What this demonstrates:** Constructing and validating the tridiagonal eigensolver Hamiltonian for the infinite square well, with two middle steps left blank.

**The problem:** Build the interior Hamiltonian for an infinite square well, $V_j = 0$, on $[0,L]$ with $N$ grid points, and verify the eigenvalue ratios match $E_n/E_1 = n^2$ — the golden test.

**Step 1 — Set the grid and hopping coefficient (complete).** Spacing $h = L/(N-1)$. Kinetic hopping coefficient $t_k = \hbar^2/(2mh^2)$.
*Why:* The central-difference stencil $\psi''(x_j) \approx (\psi_{j+1} - 2\psi_j + \psi_{j-1})/h^2$ turns the second derivative into nearest-neighbor coupling of strength $t_k$.

**Step 2 — Place the entries with Dirichlet boundaries (complete).** Build only the $(N-2)\times(N-2)$ interior block:
```
For j = 1 to N-2:
  H[j,j]   = 2*t_k + V[j]   // = 2*t_k since V_j = 0
  H[j,j+1] = -t_k
  H[j-1,j] = -t_k
```
*Why:* Omitting the boundary rows/columns enforces $\psi_0 = \psi_{N-1} = 0$ (hard walls); the diagonal is $2t_k$, **not** $t_k$ — confusing them puts $E_1$ off by a factor of two.

**Step 3 — [BLANK] Diagonalize and extract the lowest eigenvalues, then form the ratios $E_n/E_1$.**
*Your work here:*

_______________________________________________

*Why (your explanation):*

_______________________________________________

**Step 4 — [BLANK] State the numerical correctness check that needs NO physical constants, and what it certifies.**
*Your work here:*

_______________________________________________

*Why (your explanation):*

_______________________________________________

**Step 5 — Confirm the absolute scale (complete).** With $L = 2$ nm, $m = m_e$, $N = 500$, the analytic ground state is $E_1 = \pi^2\hbar^2/(2m_eL^2) \approx 0.094$ eV, and the numerical $E_1$ should agree to fractional error below $10^{-5}$. Also verify normalization $\sum_j|\psi_j|^2 h = 1.000$ after dividing each eigenvector by $\sqrt{h}$.

**Final answer:** $E_n/E_1 = 4.000, 9.000, 16.000, 25.000$ to three decimals (units-independent), and $E_1 \approx 0.094$ eV with fractional error $< 10^{-5}$ — the infinite-well golden test passes.

**Self-explanation prompt:** Explain why the ratio test $E_n/E_1 = n^2$ certifies the eigenvalue *algorithm* even if your value of $\hbar$ in eV is wrong, and what additional error only the absolute-scale check $E_1 \approx 0.094$ eV can catch.

## Part D — Error-Recognition Problem

> **Use this section only after completing Parts A–C.**

**The problem:** A student writes the split-step Fourier time-stepper and reports that the free-particle Gaussian packet "evolves correctly — the norm stays at 1.000 for the first ten steps."

**Step 1 (correct).** Half potential step: `psi[j] *= exp(-i*V[j]*dt/(2*hbar))`. With $V = 0$ this is the identity, fine.

**Step 2 (correct).** FFT the array: `psi_hat = FFT(psi)`. Then the kinetic phase will be applied in Fourier space.

**Step 3 (⚠ contains an error).** "Apply the kinetic phase using the raw FFT index $m$ directly as the wave vector: for each $m$, set $k = 2\pi m/(Nh)$ and `psi_hat[m] *= exp(-i*hbar*k^2*dt/(2*m_particle))`. Since $k^2$ is always positive, the sign of $k$ doesn't matter, so I don't need the wrap-around correction for $m \geq N/2$."

**Step 4 (correct-looking).** Inverse FFT and second half potential step: `psi = IFFT(psi_hat); psi[j] *= exp(-i*V[j]*dt/(2*hbar))`. "The norm is preserved because every multiplier has modulus 1, so this is unitary and correct."

**Your tasks:**
1. Identify the exact numerical-method misconception in Step 3 (the claim "$k^2$ is positive so the sign doesn't matter").
2. Write the correct $k_m$ mapping with the sign flip for $m \geq N/2$, and show that the raw index gives the *wrong magnitude* of $k$ (not just the wrong sign) for the upper half of the array.
3. Explain why Step 4's reasoning ("norm preserved, therefore correct") is true but insufficient — the norm can stay at $1.000$ while the dynamics are wrong.
4. Predict the symptom: per the chapter, when does the corruption become visible, and where in the wave function does it first appear?

**Why this error is common:** The student reasons that since the kinetic energy depends on $k^2$ the sign of $k$ is irrelevant — but the raw index $m$ for $m \geq N/2$ corresponds to a **small negative** $k_m = (m-N)\cdot 2\pi/Nh$, so $k_m^2$ is small, whereas the raw index gives a **large** $k^2$; the magnitudes differ, giving the wrong kinetic energy to every high-index component, and because each multiplier still has modulus 1 the norm check passes while the high-frequency tails corrupt and then spread.

## Part E — Transfer Problem

**What this demonstrates:** The unitarity-and-normalization discipline transfers to a numerical method **not** built in this chapter — propagation by direct exponentiation of a small Hamiltonian.

**The problem (context not in the chapter):** Instead of Crank–Nicolson or split-step, a colleague proposes evolving a small ($N=4$) tridiagonal system by literally diagonalizing $\mathbf H = \mathbf U\,\mathrm{diag}(E_k)\,\mathbf U^\dagger$ once, then computing the **exact** propagator $\Psi(t) = \mathbf U\,\mathrm{diag}(e^{-iE_k t/\hbar})\,\mathbf U^\dagger\,\Psi(0)$ at any $t$ in one shot (the "spectral propagator").

(a) Argue from $|e^{-iE_k t/\hbar}| = 1$ that this propagator is exactly unitary for any $t$ — no time step, no accumulation of error. (b) State the normalization check you would still run, and why it can only fail if $\mathbf U$ is not properly orthonormal (i.e. the eigenvectors were not normalized). (c) Explain the trade-off versus split-step: why does this method become impractical for the $N = 500$ grids the sandbox actually uses, even though it is "exact"?

**Hint (use only if stuck after 10 minutes):** The eigenvalues $E_k$ of a Hermitian $\mathbf H$ are real, so each $e^{-iE_kt/\hbar}$ sits on the unit circle — the same reason Crank–Nicolson's $\mu_{CN}$ has modulus 1, just done all at once. The catch is cost: diagonalizing a dense $N\times N$ matrix is $O(N^3)$, prohibitive in a browser for $N = 500$, whereas split-step is $O(N\log N)$ per step via the FFT.

**Reflection prompt:**
1. All three correct methods (Crank–Nicolson, split-step, spectral) are unitary for the *same* underlying reason. State that reason in one sentence.
2. The spectral propagator is "exact" yet the chapter still recommends split-step for production runs. What does this tell you about why "most accurate" and "right tool" are not the same judgment?

## Part F — Interleaved Review

**Problem F1.** Run the split-step free-particle evolution ($V = 0$) on a Gaussian packet with center $x_0$, width $a$, and mean wavenumber $k_0$. Using the analytic results, predict the centroid $x_0 + (\hbar k_0/m)t$ and the width $\sigma(t)^2 = a^2/2 + \hbar^2 t^2/(2m^2 a^2)$ at $t = 5$ fs, and state the two correctness checks you would apply (centroid/width within 1%, and the normalization indicator pinned at $1.000$).
*Chapter this draws from: Chapter 11.*

**Problem F2.** From a **numerical** harmonic-oscillator ground state (set $V_j = \tfrac12 m\omega^2 x_j^2$), compute $\sigma_x$ and $\sigma_p$ via $\sigma_x^2 = \langle x^2\rangle - \langle x\rangle^2$ and $\langle p^2\rangle = -\hbar^2\sum_j\psi_j^*(d^2\psi/dx^2)_j\,h$, and verify the uncertainty product $\sigma_x\sigma_p = \hbar/2$ — the Kennard bound saturated. Explain, using the minimum-uncertainty-state result, why this particular eigenstate (and not the well's ground state) hits the bound exactly.
*Chapter this draws from: Operators and Uncertainty (Chapter 9), the Kennard/Robertson bound.*

**Problem F3.** Your time-evolution run shows the normalization indicator slowly decreasing from $1.000$ to $0.94$ over the simulation window. Determine whether this is a bug or correct physics.
*Note to instructor: this problem is intentionally ambiguous — a decreasing norm is a failure if the stepper is plain split-step / Crank–Nicolson on a real potential (implicit Euler crept in, or probability is leaking), but it is **correct physics** if a complex absorbing potential $-i\gamma(|x|-x_{\rm abs})^2$ was added near the edges (probability genuinely flows out of the domain). The student must ask which potential is in play before declaring a bug — the same indicator reading means opposite things depending on context.*

**Closing reflection:** F1 checked a unitary stepper against an analytic spreading law; F2 reached back to the Kennard bound from Chapter 9; F3 forced you to read the normalization indicator in context. Which of these checks is purely numerical (independent of physical constants) and which require the right value of $\hbar$ and $m$ to be meaningful?

## Instructor Notes

**Common errors:**
- Using explicit/forward Euler (or any non-unitary stepper), so the norm blows up — caught by the normalization indicator reading above $1.001$ within ten steps.
- A wrong FFT momentum-grid ordering/sign (using the raw index $m$ instead of the wrapped $k_m$ for $m \geq N/2$), which corrupts high-frequency components while the norm check still passes.
- Feeding a Euclidean-normalized eigenvector ($\sum|\psi_j|^2 = 1$) into a physics-normalized observable, giving a factor-of-$1/h$ error (indicator reads $\sim$250 for $h = 0.004$ nm) — fix by dividing by $\sqrt h$.

**Signs a student needs to return:**
- They declare the sandbox "correct" because the output "looks right," without running the golden test $E_n/E_1 = n^2$ with no fitting parameters.
- They ignore normalization drift, treating the indicator as decoration rather than the primary unitarity sensor — or conversely, they flag absorbing-potential decay as a bug.

**Scaffolding adjustments:** A student stuck on Part A should first verify the Euler instability for a *single* eigenstate by hand (the scalar $|1 - i\Delta tE/\hbar|^2$) before reasoning about a full wave-packet superposition. A student who finishes Part F quickly should add the Numerov $O(h^6)$ method and compare its $\delta E_5/E_5$ against central-difference $O(h^2)$ at fixed $N$, confirming the accuracy-versus-cost trade-off.

**Domain adaptation note:** For a computational-physics or numerical-methods course, foreground the linear-algebra framing — unitarity as the spectral-radius condition $|\mu_k| = 1$, Crank–Nicolson as a Cayley transform, split-step as operator splitting with Trotter error — so the quantum content becomes a worked instance of stable PDE time-stepping.
