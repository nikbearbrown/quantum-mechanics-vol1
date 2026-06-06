# Chapter 4 — The Schrödinger Equation and Stationary States

In January 1926, Erwin Schrödinger sought a wave equation for matter. He had been reading de Broglie's 1924 thesis, which argued that particles have wave properties, and he required the equation to reproduce the Bohr energy levels of hydrogen as a consequence rather than a postulate. Within six months he submitted four foundational papers to *Annalen der Physik*. At the center of all of them is

$$i\hbar\,\frac{\partial \Psi}{\partial t} = \hat{H}\,\Psi.$$

This is the time-dependent Schrödinger equation (TDSE). It is a partial differential equation, first order in time and second order in space. When the potential $V$ is time-independent — as it is for the infinite square well, the harmonic oscillator, the hydrogen atom, and nearly every system in this book — the equation can be solved by a standard separation-of-variables method. This chapter develops that method and the stationary-state solutions it produces.

---

## Separation of Variables

The full TDSE in one dimension is

$$i\hbar\,\frac{\partial \Psi}{\partial t} = -\frac{\hbar^2}{2m}\,\frac{\partial^2 \Psi}{\partial x^2} + V(x)\,\Psi.$$

The left side involves only the time derivative; the right side mixes a spatial derivative with $V(x)$. They are coupled, and that coupling is what makes the equation a PDE.

The guess — called the product ansatz — is to try $\Psi(x, t) = \psi(x)\,\phi(t)$. Substitute:

$$i\hbar\,\psi(x)\,\phi'(t) = \phi(t)\,\hat{H}\psi(x).$$

Divide both sides by $\psi(x)\phi(t)$:

$$i\hbar\,\frac{\phi'(t)}{\phi(t)} = \frac{\hat{H}\psi(x)}{\psi(x)}.$$

The left side is a function of $t$ only; the right side is a function of $x$ only. For the two to be equal at every $x$ and every $t$, both sides must equal the same constant. Call that constant $E$.

We now have two separate ordinary differential equations:

$$i\hbar\,\phi'(t) = E\,\phi(t), \tag{4.1}$$

$$\hat{H}\,\psi(x) = E\,\psi(x). \tag{4.2}$$

Equation (4.1) is trivial: it says $\phi(t) = e^{-iEt/\hbar}$, a phase rotating at angular frequency $E/\hbar$. This is a universal form, the same regardless of the potential or the energy level.

Equation (4.2) is the **time-independent Schrödinger equation** (TISE):

$$\boxed{-\frac{\hbar^2}{2m}\,\frac{d^2\psi}{dx^2} + V(x)\,\psi(x) = E\,\psi(x).}$$

This is an eigenvalue problem: find the functions $\psi$ such that $\hat{H}$ acting on $\psi$ returns $\psi$ multiplied by a constant. Those functions are the **stationary states** (or energy eigenstates), and the constants $E$ are the **energy eigenvalues**. The time evolution has been completely factored out — a rotating phase attached to each state — and all the interesting physics now lives in the spatial equation.

---

## What the Constant $E$ Actually Means

The letter $E$ was not chosen arbitrarily. It is the energy, in a precise and operational sense. For any state $\Psi$, the expectation value of the Hamiltonian is

$$\langle \hat{H} \rangle = \int \Psi^*(x,t)\,\hat{H}\,\Psi(x,t)\,dx.$$

For a stationary state $\Psi_n = \psi_n(x)\,e^{-iE_n t/\hbar}$, plug in. The phase $e^{+iE_n t/\hbar}$ from the complex conjugate and the phase $e^{-iE_n t/\hbar}$ from the state multiply to 1. The eigenvalue equation $\hat{H}\psi_n = E_n\psi_n$ pulls $E_n$ out of the integral, and normalization sets $\int|\psi_n|^2\,dx = 1$. The result:

$$\langle \hat{H} \rangle = E_n.$$

That is more than just the average energy. The variance is also zero: $\langle \hat{H}^2\rangle - \langle \hat{H}\rangle^2 = 0$. Every single energy measurement on a particle in state $\psi_n$ returns exactly $E_n$ — no spread, no uncertainty, no distribution. That is what it means to be an eigenstate of an operator. The particle is in a state with a definite energy.

There is also a consistency check. If $E$ were complex with a nonzero imaginary part, the factor $|e^{-iEt/\hbar}|^2 = e^{2\,\mathrm{Im}(E)\,t/\hbar}$ would cause the probability to grow or decay over time, and conservation of probability forbids that. Self-adjoint Hamiltonians — which is what you get with real potentials and physical boundary conditions — have only real eigenvalues. The $E_n$ are always real numbers.

---

## Stationary in What Sense

The full stationary state is

$$\Psi_n(x, t) = \psi_n(x)\,e^{-iE_n t/\hbar}.$$

The probability density is

$$|\Psi_n(x, t)|^2 = |\psi_n(x)|^2\cdot|e^{-iE_n t/\hbar}|^2 = |\psi_n(x)|^2.$$

The time dependence is gone. The probability of finding the particle in any region is constant in time. That is what "stationary" means.

What "stationary" does *not* mean is that the wave function itself is time-independent. $\Psi_n$ is a complex function rotating in the complex plane at angular frequency $E_n/\hbar$. Its real part goes as $\psi_n(x)\cos(E_n t/\hbar)$ and its imaginary part as $-\psi_n(x)\sin(E_n t/\hbar)$. They oscillate 90 degrees out of phase, like the two components of a clock hand. The wave function is a clock; the probability density is the clock's shadow on the floor. The shadow does not move, but the clock is spinning.

The simulation for this chapter makes this visible. For a single eigenstate, the Re $\Psi$ and Im $\Psi$ panels animate while the $|\Psi|^2$ panel sits frozen. If $|\Psi|^2$ moves when only one eigenstate is populated, the phase is not canceling correctly and the code is wrong.

---

## Why the Laser Cavity Is the Same Problem

Consider a laser cavity: two mirrors facing each other with a gain medium between them. The cavity produces a single, monochromatic, phase-coherent beam at specific frequencies, and not others, because it only sustains standing waves that fit exactly between the mirrors. A wave that does not vanish at both mirror surfaces destroys itself on each round trip through destructive interference. A wave that does vanish at both surfaces builds up coherently. The cavity selects, from a continuous range of possible frequencies, the discrete set that satisfies its boundary conditions.

Quantization in quantum mechanics is this same phenomenon at atomic scales and with a different wave equation. The confining potential supplies the walls; only the spatial modes satisfying the boundary conditions survive; those modes are the stationary states; their discrete spatial frequencies correspond to discrete energies. The Schrödinger equation is the wave equation that determines which modes fit.

---

## Global Phase and Relative Phase

Multiplying the entire wave function by $e^{i\alpha}$ for any real $\alpha$ — a global phase — leaves all observable quantities unchanged. The factor cancels in every probability density $|\Psi|^2$ and every expectation value. States are therefore defined only up to a global phase.

The rotating phase $e^{-iE_n t/\hbar}$ in a stationary state is a global phase for that single state, so it too is unobservable. A stationary state is stationary precisely because the rotating phase carries no measurable information.

When two stationary states are combined, the situation changes. Form the superposition

$$\Psi(x, t) = c_1\,\psi_1(x)\,e^{-iE_1 t/\hbar} + c_2\,\psi_2(x)\,e^{-iE_2 t/\hbar}.$$

The probability density is

$$|\Psi|^2 = |c_1|^2|\psi_1|^2 + |c_2|^2|\psi_2|^2 + 2\,\mathrm{Re}\!\left[c_1^*c_2\,\psi_1^*\psi_2\,e^{-i(E_2-E_1)t/\hbar}\right].$$

The first two terms are frozen. The third oscillates at angular frequency $\omega_{12} = (E_2 - E_1)/\hbar$ — the beat frequency between the two levels. This is the interference term, and it is the signature of superposition. Two states with different energies rotate at different rates; the angle between them in the complex plane grows steadily; and the resulting interference pattern shifts continuously across space. That is the sloshing.

The energy expectation value, by contrast, does not slosh. For any superposition:

$$\langle \hat{H}\rangle = \sum_n |c_n|^2\,E_n.$$

This is a weighted average of the eigenvalues with weights $|c_n|^2$. The cross terms that carry the time dependence vanish by orthogonality of the eigenstates, so the result is exactly time-independent. The probability distribution oscillates across the well while the total energy remains constant — quantum energy conservation expressed in this language.

---

## Worked Example — A Single Eigenstate Against a Superposition

Take the ground state of the infinite square well (details in Chapter 5):

$$\psi_1(x) = \sqrt{\frac{2}{L}}\,\sin\!\left(\frac{\pi x}{L}\right), \quad 0 \leq x \leq L.$$

Its stationary state is $\Psi_1(x,t) = \psi_1(x)\,e^{-iE_1 t/\hbar}$, and the probability density follows as:

$$|\Psi_1(x,t)|^2 = \frac{2}{L}\sin^2\!\left(\frac{\pi x}{L}\right).$$

No $t$. The expectation of position:

$$\langle x\rangle = \int_0^L x\cdot\frac{2}{L}\sin^2\!\left(\frac{\pi x}{L}\right)dx = \frac{L}{2},$$

by symmetry. This value sits fixed for all time.

Now mix in the first excited state:

$$\Psi(x,t) = \frac{1}{\sqrt{2}}\,\psi_1(x)\,e^{-iE_1 t/\hbar} + \frac{1}{\sqrt{2}}\,\psi_2(x)\,e^{-iE_2 t/\hbar}.$$

Since both $\psi_1$ and $\psi_2$ are real, the probability density becomes:

$$|\Psi(x,t)|^2 = \frac{1}{2}\!\left[\psi_1^2 + \psi_2^2 + 2\,\psi_1\psi_2\,\cos\!\left(\frac{(E_2-E_1)t}{\hbar}\right)\right].$$

Now $|\Psi|^2$ oscillates, and the probability sloshes back and forth across the well at the beat frequency. The "stationary" property is gone — not through any error, but because a superposition of eigenstates at different energies is genuinely not a stationary state. Stationarity is the privilege of a pure energy eigenstate, and pure energy eigenstates are special.

---

## Building a General Solution

Suppose $\hat{H}$ comes with a complete, orthonormal set of eigenstates $\{\psi_n\}$ and eigenvalues $\{E_n\}$. "Complete" means that any physically reasonable wave function can be built as a superposition of the $\psi_n$; "orthonormal" means $\langle\psi_m|\psi_n\rangle = \delta_{mn}$. For the self-adjoint operators of quantum mechanics, both properties are guaranteed by the spectral theorem of functional analysis — a result of mathematics, not a fresh quantum postulate.

The completeness of the eigenstates for the infinite well is the Fourier sine series theorem, which Fourier proved (for the heat equation) in 1822. The quantum application adds only the probabilistic interpretation and the phase rotation; the completeness itself is a century older than quantum mechanics. There is no quantum mystery here, only old mathematics in new clothing.

Given an initial state $\Psi(x, 0)$, expand it:

$$\Psi(x, 0) = \sum_n c_n\,\psi_n(x), \qquad c_n = \int \psi_n^*(x)\,\Psi(x, 0)\,dx.$$

Because the basis is orthonormal, each projection is exact and unique. We then hang the time-evolution phases on the terms:

$$\Psi(x, t) = \sum_n c_n\,\psi_n(x)\,e^{-iE_n t/\hbar}.$$

This is the complete general solution of the TDSE for any time-independent potential. There are three steps: solve the eigenvalue problem to find $\{\psi_n, E_n\}$; project the initial condition to find $\{c_n\}$; attach the rotating phases. Step one is the hard one. Steps two and three are a calculation.

Stopping at step one gives the stationary states but misses everything that happens when the particle is not in a pure eigenstate. Finding the eigenstates completes the setup, not the problem.

---

## The +1 — Simulation Exercise

### Part A — `CLAUDE.md` snippet for this chapter

Add this stanza to your existing `CLAUDE.md`:

````markdown
## Chapter 4 — Separation of Variables and Stationary States

- Phase convention: exp(−i E t/ℏ). NOT exp(+i E t/ℏ). The sign is
  fixed by the TDSE; reversing it reverses the sloshing direction.
- A stationary state Ψ_n = ψ_n(x) exp(−i E_n t/ℏ) has |Ψ_n|² = |ψ_n|² —
  no time dependence. Verify: the |Ψ|² panel must be visibly frozen
  for a single eigenstate. If it oscillates, the code is wrong.
- ⟨H⟩ = Σ |c_n|² E_n, exactly constant in time. If it drifts by more
  than 0.1% over one sloshing period, flag it red in the UI.
- Complex storage: Ψ is always stored as {re, im} pairs. Dropping Im Ψ
  breaks the phase and turns a rotating complex exponential into a cosine.
- Re Ψ and Im Ψ panels spin for a single eigenstate; |Ψ|² stays frozen.
  If both panels look the same, Im Ψ has been lost.
````

### Part B — The simulation prompt

````markdown
SHOW.
Time-dependent Schrödinger equation for a particle in a potential V(x):
  iℏ ∂Ψ/∂t = ĤΨ,  Ĥ = −(ℏ²/2m) ∂²/∂x² + V(x).
Separation of variables when V = V(x):
  Ψ(x, t) = ψ(x) e^(−iEt/ℏ)  [stationary state, one eigenstate]
General state:
  Ψ(x, t) = Σ_n c_n ψ_n(x) e^(−i E_n t/ℏ)
Energy eigenvalues (infinite square well):
  E_n = n² π² ℏ² / (2 m L²),  n = 1, 2, 3, …
Eigenstates: ψ_n(x) = √(2/L) sin(nπx/L) for 0 ≤ x ≤ L, zero elsewhere.
Energy expectation: ⟨H⟩ = Σ |c_n|² E_n = constant.

Use the existing CLAUDE.md (with the Chapter 4 stanza) and DESIGN.md.

SAY.
Produce a single file `04-stationary-states.html`.

Layout (stacked top to bottom):
  1. THREE-PANEL WAVE FUNCTION VIEW (each 120 px tall, shared x-axis):
     Top:    Re Ψ(x, t)   — orange, animated
     Middle: Im Ψ(x, t)   — gray dashed, animated
     Bottom: |Ψ(x, t)|²   — blue filled, animated
  2. CONTROLS (below panels):
     - Eigenstate selector: c_1, c_2, c_3, c_4 (real magnitudes 0–1).
     - Phase sliders θ_1, θ_2, θ_3, θ_4 (0 to 2π).
     - Normalise automatically: display renormalized |c_n|².
     - L slider (1 to 20 nm). Mass dropdown {electron, proton}.
     - Pause/play, time speed × 1, × 5, × 20.
  3. NUMERICAL READOUTS (right panel):
     - ∫|Ψ|² dx (must read 1.000)
     - ⟨H⟩ in eV (constant; red if drift > 0.1%)
     - ⟨x⟩(t) in nm (live, animated)
     - E_1, E_2, E_3 in eV
     - "Stationary?" indicator: green "YES" if only one c_n ≠ 0,
       red "NO" otherwise.

CONSTRAIN.
- D3 v7 from CDN. SVG only. Vanilla JS.
- N = 300 grid points on x ∈ [0, L].
- Time evolution: Ψ(x, t) = Σ c_n ψ_n(x) exp(−i E_n t/ℏ). Analytic.
  Do NOT numerically integrate the TDSE.
- Phase sign: exp(−i E_n t/ℏ). Verify: with c_1 = 1 only, both
  Re Ψ and Im Ψ must visibly oscillate, while |Ψ|² stays frozen.
- Complex storage: {re, im} float arrays, never collapsed to real.

VERIFY.
After writing the file, give me three checks:
(a) c_1 = 1, all others 0: Re Ψ oscillates, Im Ψ oscillates (90° offset),
    |Ψ|² is frozen (does not animate). "Stationary?" reads YES.
(b) c_1 = c_2 = 1/√2, θ_1 = θ_2 = 0: |Ψ|² oscillates, ⟨x⟩(t) oscillates,
    ⟨H⟩ is constant. "Stationary?" reads NO.
(c) Change θ_2 from 0 to π with c_1 = c_2 = 1/√2: the initial shape of
    |Ψ|² flips (from left-heavy to right-heavy). Explain in the code
    comment why: the relative phase θ₂ − θ₁ = π converts (ψ₁ + ψ₂)²
    into (ψ₁ − ψ₂)² at t = 0.

List known LLM failure modes and confirm guards:
  - Im Ψ identically zero (lost complex part).
  - |Ψ|² animating for a single eigenstate (phase not canceling correctly).
  - ⟨H⟩ drifting over time.
  - Wrong phase sign, flipping Re/Im oscillation.
  - "Stationary?" hardcoded YES regardless of coefficients.
````

### Part C — Exploration tasks

**The frozen clock.** Set $c_1 = 1$, all others zero. Play the animation. Watch Re $\Psi$ and Im $\Psi$ oscillate at frequency $E_1/\hbar$ — they are the two components of a rotating clock hand, 90 degrees out of phase. Watch $|\Psi|^2$ not move. Write one sentence: the rotating phase multiplies $\psi_n(x)$ uniformly, so $|\psi_n|^2\cdot|e^{-iE_n t/\hbar}|^2 = |\psi_n|^2$ regardless of $t$.

**The sloshing pair.** Switch to $c_1 = c_2 = 1/\sqrt{2}$, $\theta_1 = \theta_2 = 0$. Observe $|\Psi(x,t)|^2$ oscillating back and forth. Read $\langle x\rangle(t)$ — it swings. Read $\langle H\rangle$ — it does not move. Write two sentences: (1) what the probability distribution is doing, (2) what the energy is not doing.

**Phase flipping.** With $c_1 = c_2 = 1/\sqrt{2}$, change $\theta_2$ from 0 to $\pi$. The initial shape of $|\Psi|^2$ flips from left-heavy to right-heavy. Explain: at $t = 0$, the state is proportional to $\psi_1 + e^{i\theta_2}\psi_2$; flipping $\theta_2$ by $\pi$ changes $\psi_1 + \psi_2$ to $\psi_1 - \psi_2$, which has a completely different spatial shape, because $\psi_1$ and $\psi_2$ have their antinodes in different places.

**Energy precision.** Try $c_1 = 0.6$, $c_2 = 0.8$. After normalization, $|c_1|^2 + |c_2|^2 = 1$. Read $\langle H\rangle$. Consider: a single energy measurement would return $E_1$ with probability 0.36 or $E_2$ with probability 0.64. After the measurement, the state collapses to a single eigenstate, the interference term disappears, and $|\Psi|^2$ stops oscillating.

---

## References

- Schrödinger, E. (1926). Quantisierung als Eigenwertproblem. *Annalen der Physik*, 79, 361–376. (First paper on the wave equation. English translation in: Schrödinger, E. *Collected Papers on Wave Mechanics*, Blackie and Son, 1928.)
- Griffiths, D.J., & Schroeter, D.F. (2018). *Introduction to Quantum Mechanics* (3rd ed.). Cambridge University Press. §2.1.
- Shankar, R. (1994). *Principles of Quantum Mechanics* (2nd ed.). Plenum. §5.1.
- von Neumann, J. (1932). *Mathematische Grundlagen der Quantenmechanik*. Springer. (Modern spectral theory and self-adjointness; English translation: *Mathematical Foundations of Quantum Mechanics*, Princeton University Press, 1955.)
- Stein, E.M., & Shakarchi, R. (2003). *Fourier Analysis: An Introduction*. Princeton University Press. Ch. 4.
- Reed, M., & Simon, B. (1975). *Methods of Modern Mathematical Physics, Vol. 2: Fourier Analysis, Self-Adjointness*. Academic Press.

---

*Chapter 5 follows: the infinite square well is the simplest potential with walls. We solve the TISE for $V = 0$ inside and $V = \infty$ at the boundaries, find the sine-function eigenstates and $n^2$-spaced energy levels, and use the results as the concrete basis for everything in this chapter.*

---

## Running Project — Build the 1D Quantum Sandbox

**This chapter adds:** the spectral time-evolution engine for stationary states — the phase-rotation update $\Psi(x,t) = \sum_n c_n\psi_n(x)\,e^{-iE_nt/\hbar}$ — plus the conserved-energy diagnostic $\langle\hat H\rangle = \sum_n|c_n|^2 E_n$ that must stay constant, and the "stationary means $|\Psi|^2$ is frozen" invariant the eigensolver mode relies on.

### Exercise R1 — When to Use AI
**The judgment:** In this chapter's project work, AI assistance is appropriate for:
- Writing the per-frame phase update that multiplies each eigenstate coefficient by $e^{-iE_nt/\hbar}$ and sums to $\Psi(x,t)$ — *Why AI works here:* it is mechanical complex arithmetic over arrays, checkable against the invariant that $|\Psi_n|^2$ is frozen for a single eigenstate.
- Drafting the $\langle\hat H\rangle = \sum_n|c_n|^2 E_n$ readout and a "Stationary? YES/NO" indicator — *Why AI works here:* both are simple reductions with an exact expected behavior you can verify.
**The tell:** You are using AI well when you have an independent way to check the output — here, a single-eigenstate $|\Psi|^2$ that does not move, and an $\langle\hat H\rangle$ that does not drift.

### Exercise R2 — When NOT to Use AI
**The judgment:** These tasks require your judgment; AI output here can't be trusted without redoing the work:
- The sign of the evolution phase $e^{-iE_nt/\hbar}$ — *Why AI fails here:* the wrong sign ($+iEt/\hbar$) reverses the sloshing direction of a superposition; the animation still looks like quantum dynamics, so only your knowledge that the TDSE fixes the sign catches it.
- Whether $|\Psi|^2$ should animate — *Why AI fails here:* a phase-cancellation bug makes a single eigenstate's $|\Psi|^2$ flicker; the AI may "stabilize" it by computing $|\psi_n|^2$ directly and bypassing the phase, hiding the bug rather than fixing it, which then breaks every multi-state superposition.
**The tell:** If you could not explain the result without the AI — if the AI is your *reason* rather than your *tool* — it did work that should have been yours.
**Physics-judgment connection:** This trains checking a time-stepper against a conservation law ($\langle\hat H\rangle$ constant) and against the stationary-state invariant ($|\Psi_n|^2$ time-independent) — the same checks the unitary stepper in Chapter 8 will need.

### Exercise R3 — LLM Exercise
**What you're building this chapter:** the spectral propagator that rotates eigenstate phases and the energy-conservation diagnostic.
**Tool:** Claude chat — built on the ψ array and observables from Chapter 3; self-contained.
**The Prompt:**
```
Using the Chapter 0 CLAUDE.md, constants.js, grid.js, and the observables.js
from Chapter 3 as binding context, build 04-stationary-states.html.

Eigenstates of the infinite well: ψ_n(x) = √(2/L) sin(nπx/L) on [0,L],
E_n = n²π²ℏ²/(2mL²). Let the user set real magnitudes c_1..c_4 and phases
θ_1..θ_4, then auto-normalize so Σ|c_n|² = 1.

Time evolution (ANALYTIC, spectral): each frame, form
  Ψ(x,t) = Σ_n c_n e^{iθ_n} ψ_n(x) e^{−i E_n t/ℏ}
as re[]/im[] arrays. Do NOT integrate the TDSE numerically — phase rotation
is exact. Phase sign is exp(−iE_n t/ℏ).

Display: three panels (Re Ψ, Im Ψ, |Ψ|², all animated); ⟨x⟩(t) live;
⟨H⟩ = Σ|c_n|² E_n in eV (flag red if it drifts > 0.1%); normalization (1.000);
a "Stationary?" indicator that reads YES only when exactly one c_n ≠ 0.

VERIFY in your answer: with c_1 = 1 alone, Re Ψ and Im Ψ oscillate but |Ψ|²
is FROZEN and "Stationary?" reads YES; with c_1 = c_2 = 1/√2, |Ψ|² sloshes,
⟨x⟩(t) swings, ⟨H⟩ stays constant, "Stationary?" reads NO.
```
**What this produces:** `04-stationary-states.html` and the reusable phase-rotation propagator the eigensolver mode reuses to animate any spectrum.
**How to adapt:** *Your system:* swap the well eigenstates for any $\{\psi_n, E_n\}$ the eigensolver returns later. *ChatGPT/Gemini:* paste the dependency files. *Claude Project:* keep the propagator in Project knowledge so Chapter 5's eigensolver can drive it.
**Builds on:** the ψ array and expectation values from Chapter 3.  **Next:** Chapter 5 generates the $\{\psi_n, E_n\}$ this propagator animates, by diagonalizing the Hamiltonian.

### Exercise R4 — CLI Exercise
**What you're building this chapter:** a propagator with an automated energy-conservation test over a full sloshing period.
**Tool:** Claude Code — it can step the state in time and assert $\langle\hat H\rangle$ stays flat, recording the drift in `PROJECT.md`.
**Skill level:** Intermediate
**Setup — confirm:**
- [ ] `observables.js` from Chapter 3
- [ ] `grid.js`, `constants.js`
- [ ] The CLAUDE.md phase-sign rule ($e^{-iE_nt/\hbar}$, not $+$)
**The Task:**
```
Implement a propagator evolve(coeffs, energies, psiBasis, x, h, t) returning
Ψ(x,t) as re[]/im[]. Write a Node script check-evolution.js that, for the
infinite-well superposition c_1 = c_2 = 1/√2 (L = 10 nm, electron, N = 500):
  (1) computes ⟨H⟩ at t = 0 and at 200 time steps spanning one period
      T = 2πℏ/(E_2 − E_1), asserting max drift < 0.1%;
  (2) confirms |Ψ|² at t = T matches t = 0 within 1e-3 (periodicity);
  (3) confirms ⟨x⟩(t) is NOT constant (it sloshes).
Print ⟨H⟩ drift and the period T in fs. Do NOT widen the drift tolerance.
Append to PROJECT.md under "Verified": "Ch4 evolution: ⟨H⟩ drift = <v>%, T = <v> fs".
```
**Expected output:** the propagator, `check-evolution.js`, a printed drift (well under 0.1%) and period, and a `PROJECT.md` line.
**What to inspect:** that $\langle\hat H\rangle$ drift is essentially zero (spectral evolution is exact) and that $T \approx 3.66$ fs for the 1 nm electron, or the appropriately scaled value for $L = 10$ nm.
**If it goes wrong:** if $\langle\hat H\rangle$ drifts, the code is recomputing $\langle\hat H\rangle$ via a noisy finite-difference $\hat H$ on the evolved state instead of using $\sum|c_n|^2E_n$ — for a spectral propagator the coefficients are fixed, so the energy must be exactly constant; use the coefficient form.
**CLAUDE.md / AGENTS.md note:** add: "Spectral evolution preserves $\sum|c_n|^2E_n$ exactly; any $\langle\hat H\rangle$ drift in spectral mode is a bug, not numerics."

### Exercise R5 — AI Validation Exercise
**What you're validating:** the spectral propagator and energy diagnostic from R3/R4.
**Validation type:** Code + Numerical result
**Risk level:** Medium — a phase-sign or energy bug here looks like plausible dynamics and would mislead every animation the sandbox shows.
**Setup:** use your own R3/R4 artifacts.
**The Validation Task:** Evaluate against this checklist; mark Pass / Fail / Cannot determine with reasoning.
```
Validation Checklist — Spectral time evolution and stationary states
□ Correctness: is the phase e^{−iE_n t/ℏ} (minus sign), giving the right slosh direction?
□ Completeness: does a single eigenstate leave |Ψ|² frozen while Re/Im Ψ rotate?
□ Scope: did it numerically integrate the TDSE when the spectral form was specified?
□ Physics criterion 1: ⟨H⟩ = Σ|c_n|²E_n stays constant (< 0.1% drift) under evolution?
□ Physics criterion 2: a two-state superposition is periodic with T = 2πℏ/(E_2−E_1)?
□ Failure-mode check: any of —
  - |Ψ|² animating for a single eigenstate (phase not canceling)
  - "Stationary?" hardcoded YES regardless of coefficients
  - ⟨H⟩ drifting (energy not conserved)
  - wrong phase sign, reversing the slosh
```
**What to do with findings:** pass → use it; one fail → fix the phase sign or switch $\langle\hat H\rangle$ to the coefficient form and re-run; multiple fails / cannot-determine → derive the two-state $|\Psi|^2$ by hand and confirm the slosh direction and period yourself.
**AI Use Disclosure (mandatory, two sentences):**
> *1:* The AI implemented the spectral phase-rotation propagator and the energy-conservation and stationarity indicators.
> *2:* The AI could not certify the phase sign or that a single eigenstate stays stationary from the code alone — I verified the frozen $|\Psi|^2$ and constant $\langle\hat H\rangle$ against the physics myself.
**Physics-judgment connection:** trains checking a time-stepper against a conservation law and a stationary-state invariant, the discipline the unitary stepper of Chapter 8 will demand at higher stakes.
