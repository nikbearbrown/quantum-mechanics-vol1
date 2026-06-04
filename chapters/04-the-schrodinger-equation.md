# Chapter 4 — The Schrödinger Equation and Stationary States

It is January 1926, and Erwin Schrödinger is in a rented villa in Arosa, Switzerland, with a notebook, a mystery woman, and a problem. He has been reading de Broglie's 1924 thesis, which says matter has wave properties. His question is: if matter is a wave, what is its wave equation?

He tries several forms. He knows the answer has to reproduce the Bohr energy levels for hydrogen — not as a postulate, but as a *consequence*. After weeks of false starts, he finds it. Within six months he submits four foundational papers to *Annalen der Physik*. At the center of all of them is

$$i\hbar\,\frac{\partial \Psi}{\partial t} = \hat{H}\,\Psi.$$

This is the time-dependent Schrödinger equation. It is a partial differential equation, first order in time, second order in space, and in general it is hard. But there is a case — the case where the potential does not depend on time — where you can crack it open with a single clever guess, and the hard PDE turns into a problem you can actually solve. That case covers nearly every system in this book: the infinite well, the harmonic oscillator, the hydrogen atom. All of them have static potentials. This chapter is about what happens when $V = V(x)$.

---

## The Trick

The full TDSE in one dimension is

$$i\hbar\,\frac{\partial \Psi}{\partial t} = -\frac{\hbar^2}{2m}\,\frac{\partial^2 \Psi}{\partial x^2} + V(x)\,\Psi.$$

The left side involves only the time derivative; the right side mixes a spatial derivative with $V(x)$. They are coupled, and that coupling is what makes it a PDE.

The guess — called the product ansatz — is: try $\Psi(x, t) = \psi(x)\,\phi(t)$. Substitute:

$$i\hbar\,\psi(x)\,\phi'(t) = \phi(t)\,\hat{H}\psi(x).$$

Divide both sides by $\psi(x)\phi(t)$:

$$i\hbar\,\frac{\phi'(t)}{\phi(t)} = \frac{\hat{H}\psi(x)}{\psi(x)}.$$

The left side is a function of $t$ only. The right side is a function of $x$ only. For these to be equal at every $x$ and every $t$, both sides must be constant. Call that constant $E$.

You now have two separate ordinary differential equations:

$$i\hbar\,\phi'(t) = E\,\phi(t), \tag{4.1}$$

$$\hat{H}\,\psi(x) = E\,\psi(x). \tag{4.2}$$

Equation (4.1) is trivial: it says $\phi(t) = e^{-iEt/\hbar}$, a phase rotating at angular frequency $E/\hbar$. Universal form, regardless of potential or energy level.

Equation (4.2) is the **time-independent Schrödinger equation** (TISE):

$$\boxed{-\frac{\hbar^2}{2m}\,\frac{d^2\psi}{dx^2} + V(x)\,\psi(x) = E\,\psi(x).}$$

This is an eigenvalue problem: find the functions $\psi$ such that $\hat{H}$ acting on $\psi$ returns $\psi$ multiplied by a constant. Those functions are the **stationary states** (or energy eigenstates); the constants $E$ are the **energy eigenvalues**. The time evolution has been completely factored out — a rotating phase attached to each state, and all the interesting physics lives in the spatial equation.

---

## What the Constant $E$ Actually Means

The letter $E$ was not chosen arbitrarily. It is the energy — in a precise, operational sense. For any state $\Psi$, the expectation value of the Hamiltonian is

$$\langle \hat{H} \rangle = \int \Psi^*(x,t)\,\hat{H}\,\Psi(x,t)\,dx.$$

For a stationary state $\Psi_n = \psi_n(x)\,e^{-iE_n t/\hbar}$, plug in. The phase $e^{+iE_n t/\hbar}$ from the complex conjugate and the phase $e^{-iE_n t/\hbar}$ from the state multiply to 1. The eigenvalue equation $\hat{H}\psi_n = E_n\psi_n$ pulls $E_n$ out of the integral. Normalization sets $\int|\psi_n|^2\,dx = 1$. The result:

$$\langle \hat{H} \rangle = E_n.$$

That is not just the average energy. The variance is also zero: $\langle \hat{H}^2\rangle - \langle \hat{H}\rangle^2 = 0$. Every single energy measurement on a particle in state $\psi_n$ returns exactly $E_n$ — no spread, no uncertainty, no distribution. That is what an eigenstate of an operator means. You are in a state with a definite energy.

There is also a consistency check: if $E$ were complex with nonzero imaginary part, the factor $|e^{-iEt/\hbar}|^2 = e^{2\,\mathrm{Im}(E)\,t/\hbar}$ would cause the probability to grow or decay over time. Conservation of probability forbids this. Self-adjoint Hamiltonians — which is what you get with real potentials and physical boundary conditions — have only real eigenvalues. The $E_n$ are always real numbers.

---

## Stationary in What Sense

The full stationary state is

$$\Psi_n(x, t) = \psi_n(x)\,e^{-iE_n t/\hbar}.$$

The probability density:

$$|\Psi_n(x, t)|^2 = |\psi_n(x)|^2\cdot|e^{-iE_n t/\hbar}|^2 = |\psi_n(x)|^2.$$

The time-dependence is gone. The probability of finding the particle in any region is constant. That is what "stationary" means.

What "stationary" does not mean: the wave function itself is not time-independent. $\Psi_n$ is a complex function that rotates in the complex plane at angular frequency $E_n/\hbar$. Its real part goes as $\psi_n(x)\cos(E_n t/\hbar)$; its imaginary part goes as $-\psi_n(x)\sin(E_n t/\hbar)$. They oscillate, 90 degrees out of phase, like the two components of a clock hand. The wave function is a clock. The probability density is the clock's shadow on the floor. The shadow does not move, but the clock is spinning.

The simulation for this chapter makes this visible. For a single eigenstate, the Re $\Psi$ and Im $\Psi$ panels animate; the $|\Psi|^2$ panel sits frozen. If $|\Psi|^2$ moves when only one eigenstate is populated, the phase is not canceling correctly and the code is wrong.

---

## Why the Laser Cavity Is the Same Problem

Walk into a basement laser lab. On the optical table is a cavity — two mirrors facing each other — with a gain medium inside. A pump beam goes in. A single, monochromatic, phase-coherent beam comes out.

Why specific frequencies and not others? Because the cavity only sustains modes — standing waves — that fit exactly between the mirrors. A wave that does not vanish at both mirror surfaces destructively interferes with itself on every round trip and dies out. A wave that does vanish at both surfaces builds up coherently, producing the output you see.

The cavity is selecting, from a continuous range of possible frequencies, the discrete set that satisfies its boundary conditions. Quantization in quantum mechanics is exactly this phenomenon, at a smaller scale and with a different wave equation. The confining potential provides the walls; only those spatial modes that satisfy the boundary conditions survive; those modes are the stationary states; their discrete frequencies are the discrete energies. The Schrödinger equation is the wave equation that tells you which modes fit.

---

## Global Phase and Relative Phase

A global phase — multiplying the entire wave function by $e^{i\alpha}$ for any real $\alpha$ — is unobservable. It cancels in every probability density $|\Psi|^2$ and every expectation value. States are defined only up to a global phase.

The rotating phase $e^{-iE_n t/\hbar}$ in a stationary state is a global phase for that single state. It is unobservable. This is precisely why a stationary state is stationary — the rotating phase carries no information you can measure.

The moment you put two stationary states together, everything changes. Form the superposition

$$\Psi(x, t) = c_1\,\psi_1(x)\,e^{-iE_1 t/\hbar} + c_2\,\psi_2(x)\,e^{-iE_2 t/\hbar}.$$

The probability density is

$$|\Psi|^2 = |c_1|^2|\psi_1|^2 + |c_2|^2|\psi_2|^2 + 2\,\mathrm{Re}\!\left[c_1^*c_2\,\psi_1^*\psi_2\,e^{-i(E_2-E_1)t/\hbar}\right].$$

The first two terms are frozen. The third oscillates at angular frequency $\omega_{12} = (E_2 - E_1)/\hbar$ — the beat frequency between the two levels. This is the interference term, and it is the signature of superposition. Two states with different energies rotate at different rates; the angle between them in the complex plane grows steadily; the interference pattern that results shifts continuously across space. That is the sloshing.

What is not the sloshing: the energy. The expectation value of the Hamiltonian in any superposition is

$$\langle \hat{H}\rangle = \sum_n |c_n|^2\,E_n.$$

This is a weighted average of the eigenvalues, with weights $|c_n|^2$. The cross terms — the ones that carry the time dependence — all vanish by orthogonality of the eigenstates. The result is exactly time-independent. The probability distribution sloshes back and forth across the box while the total energy never moves. It is conservation of energy, stated in the quantum language.

---

## Worked Example — A Single Eigenstate Against a Superposition

Take the ground state of the infinite square well (details in Chapter 5):

$$\psi_1(x) = \sqrt{\frac{2}{L}}\,\sin\!\left(\frac{\pi x}{L}\right), \quad 0 \leq x \leq L.$$

The stationary state is $\Psi_1(x,t) = \psi_1(x)\,e^{-iE_1 t/\hbar}$. The probability density:

$$|\Psi_1(x,t)|^2 = \frac{2}{L}\sin^2\!\left(\frac{\pi x}{L}\right).$$

No $t$. The expectation of position:

$$\langle x\rangle = \int_0^L x\cdot\frac{2}{L}\sin^2\!\left(\frac{\pi x}{L}\right)dx = \frac{L}{2},$$

by symmetry. This value sits fixed for all time.

Now mix in the first excited state:

$$\Psi(x,t) = \frac{1}{\sqrt{2}}\,\psi_1(x)\,e^{-iE_1 t/\hbar} + \frac{1}{\sqrt{2}}\,\psi_2(x)\,e^{-iE_2 t/\hbar}.$$

Since both $\psi_1$ and $\psi_2$ are real, the probability density becomes:

$$|\Psi(x,t)|^2 = \frac{1}{2}\!\left[\psi_1^2 + \psi_2^2 + 2\,\psi_1\psi_2\,\cos\!\left(\frac{(E_2-E_1)t}{\hbar}\right)\right].$$

Now $|\Psi|^2$ oscillates. The probability sloshes left and right across the well at the beat frequency. The "stationary" property has evaporated — not because anything went wrong, but because a superposition of eigenstates with different energies is genuinely not a stationary state. The stationary property belongs to a pure energy eigenstate, and pure energy eigenstates are special.

---

## Building a General Solution

Suppose $\hat{H}$ has a complete, orthonormal set of eigenstates $\{\psi_n\}$ with eigenvalues $\{E_n\}$. Complete means any physically reasonable wave function can be written as a superposition of the $\psi_n$. Orthonormal means $\langle\psi_m|\psi_n\rangle = \delta_{mn}$. Both properties are guaranteed for the self-adjoint operators that quantum mechanics uses — this follows from the spectral theorem of functional analysis, a mathematical theorem, not a new quantum postulate.

The completeness of the eigenstates for the infinite well is the Fourier sine series theorem. Fourier proved it (for the heat equation) in 1822. The quantum application adds only the probabilistic interpretation and the phase rotation; the completeness is a century older than quantum mechanics. There is no quantum mystery here, only old mathematics in new clothing.

Given an initial state $\Psi(x, 0)$, expand it:

$$\Psi(x, 0) = \sum_n c_n\,\psi_n(x), \qquad c_n = \int \psi_n^*(x)\,\Psi(x, 0)\,dx.$$

The orthonormality of the basis makes each projection exact and unique. Then attach the time-evolution phases:

$$\Psi(x, t) = \sum_n c_n\,\psi_n(x)\,e^{-iE_n t/\hbar}.$$

This is the complete general solution of the TDSE for any time-independent potential. Three steps: solve the eigenvalue problem to find $\{\psi_n, E_n\}$; project the initial condition to find $\{c_n\}$; attach the rotating phases. Step one is the hard one. Steps two and three are a calculation.

Students who stop at step one have found the stationary states but missed everything that happens when the particle is not in one. Finding the eigenstates is not the end of the problem; it is the end of the setup.

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

- Schrödinger, E. (1926). Quantisierung als Eigenwertproblem. *Annalen der Physik*, 79, 361–376. [verify] (First paper on the wave equation. English translation in: Schrödinger, E. *Collected Papers on Wave Mechanics*, Blackie and Son, 1928.)
- Griffiths, D.J., & Schroeter, D.F. (2018). *Introduction to Quantum Mechanics* (3rd ed.). Cambridge University Press. §2.1.
- Shankar, R. (1994). *Principles of Quantum Mechanics* (2nd ed.). Plenum. §5.1.
- von Neumann, J. (1932). *Mathematische Grundlagen der Quantenmechanik*. Springer. (Modern spectral theory and self-adjointness; English translation: *Mathematical Foundations of Quantum Mechanics*, Princeton University Press, 1955.)
- Stein, E.M., & Shakarchi, R. (2003). *Fourier Analysis: An Introduction*. Princeton University Press. Ch. 4.
- Reed, M., & Simon, B. (1975). *Methods of Modern Mathematical Physics, Vol. 2: Fourier Analysis, Self-Adjointness*. Academic Press.

---

*Chapter 5 follows: the infinite square well is the simplest potential with walls. We solve the TISE for $V = 0$ inside and $V = \infty$ at the boundaries, find the sine-function eigenstates and $n^2$-spaced energy levels, and use the results as the concrete basis for everything in this chapter.*
