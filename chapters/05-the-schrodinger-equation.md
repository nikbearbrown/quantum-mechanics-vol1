# Chapter 4 — The Schrödinger Equation and Stationary States

## TL;DR

- The time-dependent Schrödinger equation can be cracked open by a product ansatz when the potential is time-independent — separation of variables converts one hard PDE into two manageable ODEs.
- The separation constant *is* the energy, in a precise sense: a particle in a stationary state returns that value with certainty in every energy measurement.
- A stationary state carries a rotating phase $e^{-iEt/\hbar}$ that is invisible in $|\Psi|^2$ — the probability density is frozen while the wave function spins.
- The general solution is a superposition of stationary states, each phase-rotating at its own rate; relative phases drive all observable dynamics.
- The completeness of the eigenstate basis is not a quantum postulate — it is classical mathematics, Fourier's theorem in disguise.

---

It is 1926, and Erwin Schrödinger is in a rented villa in Arosa, Switzerland, with a notebook, a mystery woman, and a problem. He has been reading de Broglie's 1924 thesis, which says matter has wave-like properties. Schrödinger's question is: if matter is a wave, what is its wave equation?

He tries several forms. He knows the answer has to reproduce the Bohr energy levels for hydrogen — not as a postulate, but as a *consequence*. After several weeks of false starts, he finds it. He writes a paper in January 1926, submits it to *Annalen der Physik*, and within weeks sends in a second paper, a third, a fourth. In the space of six months he produces four foundational papers in quantum mechanics. The equation at the center of all of them is

$$i\hbar\,\frac{\partial \Psi}{\partial t} = \hat{H}\,\Psi.$$

This chapter is about what that equation means and what you can do with it — specifically, what you can do with it when the potential $V(x)$ does not depend on time, which covers nearly every system you will encounter in this book.

---

## Learning Objectives

By the end of this chapter you will be able to:

1. **Apply** separation of variables to the TDSE when $V = V(x)$ and produce the time-independent Schrödinger equation (TISE) as an eigenvalue problem. *(Apply — Bloom Level 3)*

2. **Explain** why the separation constant must be interpreted as energy, using the expectation value $\langle \hat{H} \rangle$ as the argument. *(Understand — Bloom Level 2)*

3. **Identify** a stationary state and explain why $|\Psi_n(x,t)|^2$ is time-independent even though $\Psi_n$ is not. *(Understand — Bloom Level 2)*

4. **Construct** the general time-evolved state $\Psi(x,t) = \sum_n c_n\,\psi_n(x)\,e^{-iE_n t/\hbar}$ from an initial condition and eigenbasis. *(Apply — Bloom Level 3)*

5. **Distinguish** the global phase (unobservable) from the relative phase (observable, drives all dynamics). *(Analyze — Bloom Level 4)*

---

## Scene Opening

Walk into a basement laser lab. On the optical table is a cavity — two mirrors facing each other — with a gain medium inside. A pump beam goes in. Light comes out in a single, monochromatic, phase-coherent stream. The laser's output has a definite frequency, a definite wavelength, a definite energy per photon.

Why does the cavity produce light at specific frequencies and not others? Because it only sustains modes — standing waves — that fit perfectly between the mirrors. A wave that does not vanish at both mirror surfaces destructively interferes with itself on each round trip and dies. A wave that *does* vanish at both surfaces adds constructively, building to the high amplitude you see exit the cavity.

The laser cavity is doing exactly what the Schrödinger equation does: it is selecting, from a continuous range of possible frequencies, the discrete set that satisfies the boundary conditions. Quantization in quantum mechanics is the same phenomenon, at a smaller scale, dressed in different language. The atom or the box has walls (or a confining potential), and only certain spatial modes survive. Those modes are the stationary states. Their discrete frequencies are the discrete energies. The Schrödinger equation is the wave equation that tells you which modes fit.

---

## Core Development

### The Time-Dependent Schrödinger Equation

The TDSE in one dimension with potential $V(x,t)$ is

$$i\hbar\,\frac{\partial \Psi}{\partial t} = \hat{H}\,\Psi, \qquad \hat{H} = -\frac{\hbar^2}{2m}\,\frac{\partial^2}{\partial x^2} + V(x,t).$$

Here $\hat{H}$ is the **Hamiltonian operator** — the quantum-mechanical avatar of the classical energy. It acts on the wave function $\Psi(x,t)$ to produce a new function. The TDSE is a first-order PDE in $t$ and a second-order PDE in $x$, and the two derivatives are coupled. In general, solving it is hard.

One case simplifies the problem dramatically: when the potential depends only on position, not on time — when $V = V(x)$. Most systems of interest have this property. The infinite well, the harmonic oscillator, the hydrogen atom: all have static potentials. We restrict to this case for the rest of the chapter.

### Separation of Variables

When $V = V(x)$, try the **product ansatz**:

$$\Psi(x, t) = \psi(x)\,\phi(t).$$

Substitute into the TDSE:

$$i\hbar\,\psi(x)\,\phi'(t) = \phi(t)\,\hat{H}\psi(x).$$

Divide both sides by $\psi(x)\phi(t)$ (assuming neither is zero):

$$i\hbar\,\frac{\phi'(t)}{\phi(t)} = \frac{\hat{H}\psi(x)}{\psi(x)}.$$

The left side is a function of $t$ only. The right side is a function of $x$ only. They are equal for all $x$ and all $t$. The only way that can happen is if both sides equal the same constant. Call it $E$.

This gives two separate ordinary differential equations:

$$\text{Time equation:} \qquad i\hbar\,\phi'(t) = E\,\phi(t), \tag{4.1}$$

$$\text{Spatial equation:} \qquad \hat{H}\,\psi(x) = E\,\psi(x). \tag{4.2}$$

The time equation (4.1) is solved by inspection:

$$\phi(t) = e^{-iEt/\hbar}. \tag{4.3}$$

This is a complex exponential — a phase rotating at angular frequency $E/\hbar$. It is universal: the same form regardless of the potential, regardless of the particular energy level. All the physics is in the spatial equation (4.2).

Equation (4.2) is the **time-independent Schrödinger equation** (TISE):

$$\boxed{-\frac{\hbar^2}{2m}\,\frac{d^2\psi}{dx^2} + V(x)\,\psi(x) = E\,\psi(x).} \tag{4.4}$$

This is an **eigenvalue problem**: find the functions $\psi$ such that $\hat{H}$ acting on $\psi$ returns $\psi$ times a constant. Those functions are the **energy eigenstates** (or **stationary states**); the constants $E$ are the **energy eigenvalues**.

The trick has converted a PDE with coupled derivatives into an ODE. The time evolution is trivial — a rotating phase. All the interesting structure — which values of $E$ are allowed, what the corresponding $\psi$'s look like — lives in the spatial problem.

### The Separation Constant Is Energy

The constant $E$ is not just a mathematical label. It has a direct physical meaning: it is the energy of the stationary state, in a precise sense.

For any state $\Psi$, the expectation value of the Hamiltonian is

$$\langle \hat{H} \rangle = \int \Psi^*(x,t)\,\hat{H}\,\Psi(x,t)\,dx.$$

For a stationary state $\Psi_n(x,t) = \psi_n(x)\,e^{-iE_n t/\hbar}$, plug in:

$$\langle \hat{H} \rangle = \int \psi_n^*\,e^{+iE_n t/\hbar}\,\hat{H}\,\psi_n\,e^{-iE_n t/\hbar}\,dx = \int \psi_n^*(x)\,E_n\,\psi_n(x)\,dx = E_n\int|\psi_n|^2\,dx = E_n.$$

The phase factors cancel. $\hat{H}\psi_n = E_n\psi_n$ is the eigenvalue equation. The normalization $\int|\psi_n|^2\,dx = 1$ brings the integral to 1. Result: $\langle \hat{H} \rangle = E_n$, exactly.

Moreover, the variance vanishes: $\langle \hat{H}^2\rangle - \langle \hat{H}\rangle^2 = 0$. Every energy measurement on a particle in state $\psi_n$ returns $E_n$ with certainty — no spread, no distribution, just the single value. That is what it means to be an eigenstate of $\hat{H}$.

There is also a constraint on $E$ worth noting: if $E$ were complex, the norm $\int|\Psi|^2\,dx$ would grow or decay exponentially in time (from $|e^{-iEt/\hbar}|^2 = e^{2\,\mathrm{Im}(E)\,t/\hbar}$), violating the continuity equation and probability conservation established in the previous chapter. Self-adjoint Hamiltonians with real potentials have only real eigenvalues, which is why $E_n$ is always real.

### What "Stationary" Means — and Does Not Mean

The full time-dependent stationary state is

$$\Psi_n(x, t) = \psi_n(x)\,e^{-iEt/\hbar}. \tag{4.5}$$

The probability density is

$$|\Psi_n(x, t)|^2 = |\psi_n(x)|^2\,|e^{-iEt/\hbar}|^2 = |\psi_n(x)|^2.$$

Since $|e^{-i\theta}|^2 = 1$ for any real $\theta$, the probability density is time-independent. This is what "stationary" means: the observable $|\Psi|^2$ does not change, so the probability of finding the particle anywhere does not change.

What "stationary" does not mean: the wave function is not time-independent. $\Psi_n(x,t)$ is a complex function that rotates in the complex plane at angular frequency $E_n/\hbar$. If you could measure $\mathrm{Re}\,\Psi$ and $\mathrm{Im}\,\Psi$ separately, you would see them spinning — $\mathrm{Re}\,\Psi_n$ going as $\psi_n(x)\cos(E_n t/\hbar)$, $\mathrm{Im}\,\Psi_n$ going as $-\psi_n(x)\sin(E_n t/\hbar)$, each oscillating at the same frequency, ninety degrees out of phase. The wave function is a clock; the probability density is the clock's shadow on the floor, which does not move.

The simulation for this chapter makes this visible. For a single eigenstate, the Re and Im panels spin while the $|\Psi|^2$ panel stays frozen. This is not a numerical artifact; it is the physics.

### The Role of Global vs. Relative Phase

A global phase — multiplying the entire wave function by $e^{i\alpha}$ for any real $\alpha$ — is unobservable. It cancels in every probability density $|\Psi|^2$ and every expectation value $\langle \hat{O}\rangle = \langle\Psi|\hat{O}|\Psi\rangle$. This is why we say quantum states are defined only up to a global phase.

The rotating phase $e^{-iE_n t/\hbar}$ in a stationary state is a global phase — for that single state, it is unobservable.

The moment you form a superposition of two stationary states, the situation changes completely. The *relative* phase between the two components is observable. Consider

$$\Psi(x, t) = c_1\,\psi_1(x)\,e^{-iE_1 t/\hbar} + c_2\,\psi_2(x)\,e^{-iE_2 t/\hbar}.$$

The probability density is

$$|\Psi|^2 = |c_1|^2|\psi_1|^2 + |c_2|^2|\psi_2|^2 + 2\,\mathrm{Re}\!\left[c_1^*c_2\,\psi_1^*\psi_2\,e^{-i(E_2-E_1)t/\hbar}\right].$$

The first two terms are time-independent. The third term oscillates at angular frequency $\omega_{12} = (E_2 - E_1)/\hbar$ — the **beat frequency** between the two levels. This oscillation is the signature of superposition. A single stationary state has no interference term; only when two (or more) stationary states combine does the wave function produce observable dynamics.

The quantity $e^{-i(E_2-E_1)t/\hbar}$ is the relative phase. At $t = 0$, both states point in the same direction in the complex plane (if $c_1, c_2$ are real and positive). As $t$ increases, they rotate at different rates, and the angle between them grows. When the relative phase has advanced by $\pi$, the interference term has flipped sign — probability has redistributed across space. When the relative phase has advanced by $2\pi$, the pattern repeats. That is the sloshing, made algebraic.

### The General Solution — From Initial Condition to Future

Suppose $\hat{H}$ has a complete, orthonormal set of eigenstates $\{\psi_n\}$ with eigenvalues $\{E_n\}$. "Complete" means any physically reasonable wave function on the relevant domain can be written as a sum of the $\psi_n$. "Orthonormal" means $\langle\psi_m|\psi_n\rangle = \delta_{mn}$. Both properties are guaranteed for the self-adjoint operators that quantum mechanics uses — they follow from the spectral theorem of functional analysis, which is not a new quantum postulate but a mathematical theorem established in its modern form by von Neumann in 1932.

Given an initial state $\Psi(x, 0)$, expand it in the eigenbasis:

$$\Psi(x, 0) = \sum_n c_n\,\psi_n(x), \qquad c_n = \langle\psi_n|\Psi(x,0)\rangle = \int \psi_n^*(x)\,\Psi(x, 0)\,dx. \tag{4.6}$$

Each coefficient $c_n$ is the inner product — the projection of the initial state onto the $n$-th eigenstate. The orthonormality of the basis makes this projection exact and unique.

Now attach the time-evolution phase to each eigenstate independently:

$$\Psi(x, t) = \sum_n c_n\,\psi_n(x)\,e^{-iE_n t/\hbar}. \tag{4.7}$$

This is the complete, general solution of the TDSE (for time-independent $V$). The recipe has three steps:

1. **Solve the TISE** $\hat{H}\psi_n = E_n\psi_n$ to find $\{\psi_n, E_n\}$.
2. **Project the initial condition** onto the eigenbasis to find $\{c_n\}$.
3. **Phase-rotate** each component: $c_n\psi_n(x) \to c_n\psi_n(x)\,e^{-iE_n t/\hbar}$.

Step 1 is the hard one; step 2 is an integral; step 3 is trivial. But all three steps are necessary. Students who do only step 1 — finding the eigenstates — have found the stationary states but missed the dynamics of a general state.

Note on the completeness claim. For the infinite square well (the next chapter), the eigenstates are sine functions and their completeness is the Fourier sine series theorem, established by Fourier in 1822 for the heat equation. The quantum application adds only the probabilistic interpretation and the phase rotation; the mathematics of completeness is a century older than quantum mechanics. Treating "any state is a superposition of energy eigenstates" as quantum mysticism misidentifies where the physics begins and the mathematics ends.

### Energy Conservation

For the general state (4.7), the expectation value of the Hamiltonian is

$$\langle \hat{H}\rangle = \int \Psi^*(x,t)\,\hat{H}\,\Psi(x,t)\,dx = \sum_{m,n} c_m^*c_n\,e^{i(E_m - E_n)t/\hbar}\int\psi_m^*\,\hat{H}\psi_n\,dx.$$

Using $\hat{H}\psi_n = E_n\psi_n$ and $\langle\psi_m|\psi_n\rangle = \delta_{mn}$:

$$\langle \hat{H}\rangle = \sum_n |c_n|^2\,E_n. \tag{4.8}$$

The time factors $e^{i(E_m-E_n)t/\hbar}$ survive only when $m = n$, where they equal 1. The cross terms vanish by orthogonality. The result is a weighted average of the eigenvalues, with weights $|c_n|^2$, and it is exactly time-independent: the energy expectation value never changes under Schrödinger evolution.

This is the quantum-mechanical statement of energy conservation for a closed system with a time-independent Hamiltonian. The simulation enforces it: $\langle H\rangle$ must stay constant to four decimal places; drift above $0.1\%$ flags a bug in the time-evolution code.

### Continuous vs. Discrete Spectra

For the infinite well (Chapter 5), the potential confines the particle: $V\to\infty$ at the walls. The boundary conditions force quantization: only discrete values of $E$ admit normalizable solutions. The spectrum is purely discrete.

For potentials that confine at large $|x|$ but are finite — the harmonic oscillator, the hydrogen atom — the spectrum is again discrete (countably infinite bound states, each with a definite energy).

For potentials that go to a constant at large $|x|$ (e.g., $V = 0$ for $|x| \to \infty$ and a bump or well in between), there are both bound states (discrete spectrum, $E < V_\infty$) and scattering states (continuous spectrum, $E > V_\infty$). The free particle is the limiting case: no confinement, purely continuous spectrum, non-normalizable plane waves.

This chapter focuses on the discrete case, which covers the systems in Chapters 5 through 8. The continuous case — tunneling, reflection, transmission — arrives in Chapter 7.

---

## Worked Example — A Stationary State's Probability Density Is Time-Independent

**The lesson.** Take the simplest possible stationary state: the ground state of an infinite square well, which we will compute fully in Chapter 5. For now, assume:

$$\psi_1(x) = \sqrt{\frac{2}{L}}\,\sin\!\left(\frac{\pi x}{L}\right), \quad 0 \leq x \leq L; \qquad \psi_1(x) = 0 \text{ elsewhere.}$$

The full time-dependent state is

$$\Psi_1(x, t) = \sqrt{\frac{2}{L}}\,\sin\!\left(\frac{\pi x}{L}\right)\,e^{-iE_1 t/\hbar}.$$

The probability density:

$$|\Psi_1(x, t)|^2 = \frac{2}{L}\,\sin^2\!\left(\frac{\pi x}{L}\right)\cdot|e^{-iE_1 t/\hbar}|^2 = \frac{2}{L}\,\sin^2\!\left(\frac{\pi x}{L}\right).$$

No $t$. The probability of finding the particle in any interval $[a, b]$ is constant:

$$P([a,b]) = \int_a^b \frac{2}{L}\sin^2\!\left(\frac{\pi x}{L}\right)dx \quad \text{(independent of } t\text{)}.$$

The expectation value of position:

$$\langle x\rangle = \int_0^L x\cdot\frac{2}{L}\sin^2\!\left(\frac{\pi x}{L}\right)dx = \frac{L}{2}$$

by the symmetry of $\sin^2(\pi x/L)$ about $x = L/2$. This value does not change with time.

**The limit.** Now form a two-state superposition and watch the time-independence evaporate. Let

$$\Psi(x, t) = \frac{1}{\sqrt{2}}\,\psi_1(x)\,e^{-iE_1 t/\hbar} + \frac{1}{\sqrt{2}}\,\psi_2(x)\,e^{-iE_2 t/\hbar}.$$

The probability density:

$$|\Psi(x,t)|^2 = \frac{1}{2}|\psi_1|^2 + \frac{1}{2}|\psi_2|^2 + \mathrm{Re}\!\left[\psi_1^*\psi_2\,e^{-i(E_2-E_1)t/\hbar}\right].$$

Since $\psi_1$ and $\psi_2$ are real:

$$|\Psi(x,t)|^2 = \frac{1}{2}\!\left[\psi_1^2 + \psi_2^2 + 2\,\psi_1\psi_2\,\cos\!\left(\frac{(E_2-E_1)t}{\hbar}\right)\right].$$

Now $|\Psi|^2$ oscillates in time. The "stationary" property is gone the moment two eigenstates with different energies mix. This is not a contradiction — neither $\psi_1$ nor $\psi_2$ is wrong, and neither is the superposition. The stationary state property is a property of a *pure energy eigenstate*, not of an arbitrary wave function.

---

## Common Misconceptions

**"Separation of variables finds all solutions."** It finds the separable (stationary-state) solutions. The full claim — that every solution is a superposition of separable solutions — requires completeness of the eigenbasis, which is a separate theorem. Separation gives you the building blocks; completeness says the building blocks span everything.

**"The phase $e^{-iEt/\hbar}$ is imaginary, so $E$ must be complex."** The phase is complex; the energy is real. If $E$ were complex with nonzero imaginary part, $|\Psi|^2$ would not integrate to 1 for all time. Real eigenvalues are guaranteed by the self-adjointness of $\hat{H}$ with a real potential.

**"A stationary state does not change in time."** The probability density $|\Psi|^2$ is stationary; the wave function $\Psi = \psi e^{-iEt/\hbar}$ is not. The real and imaginary parts of $\Psi$ oscillate. Only $|\Psi|^2$ is frozen.

**"$\langle H\rangle$ changes when the probability sloshes."** It does not. $\langle H\rangle = \sum_n|c_n|^2 E_n$ depends only on the squared amplitudes $|c_n|^2$, which do not depend on $t$. Sloshing is a phase phenomenon; the energy budget is unchanged throughout.

**"Every wave function is a stationary state."** A general initial condition $\Psi(x,0)$ is almost never a single eigenstate. It is a superposition, and superpositions are not stationary.

---

## Exercises

**Warm-up**

1. *[Tests: separation-of-variables mechanics]* Write the TDSE with $V = V(x)$ and insert the ansatz $\Psi(x,t) = \psi(x)\phi(t)$. Divide through by $\psi\phi$ and explain in one sentence why both sides must equal a constant. Name the constant and write the two ODEs that result. *(Difficulty: warm-up.)*

2. *[Tests: interpretation of the separation constant]* A particle is in a state $\Psi = \psi_3(x)\,e^{-iE_3 t/\hbar}$, where $\psi_3$ is the $n=3$ eigenstate with eigenvalue $E_3$. (a) Compute $\langle\hat{H}\rangle$. (b) Compute the variance $\langle\hat{H}^2\rangle - \langle\hat{H}\rangle^2$. (c) If you measured the particle's energy, what would you get, and how certain is that outcome? *(Difficulty: warm-up.)*

3. *[Tests: the global vs. relative phase distinction]* Two wave functions differ only by an overall phase: $\Psi_1 = \psi(x)\,e^{-iEt/\hbar}$ and $\Psi_2 = e^{i\pi/3}\,\psi(x)\,e^{-iEt/\hbar}$. (a) Compute $|\Psi_1|^2$ and $|\Psi_2|^2$. (b) Compute $\langle x\rangle$ for both. (c) Argue in one sentence that no measurement can distinguish $\Psi_1$ from $\Psi_2$. *(Difficulty: warm-up.)*

**Application**

4. *[Tests: applying the general solution formula]* An electron is in an infinite well of width $L$. At $t = 0$, its wave function is $\Psi(x, 0) = \frac{1}{\sqrt{3}}\psi_1(x) + \sqrt{\frac{2}{3}}\psi_2(x)$. (a) Write down $\Psi(x, t)$. (b) Compute $\langle\hat{H}\rangle$. (c) Show $\langle\hat{H}\rangle$ is time-independent. (d) Write $|\Psi(x,t)|^2$ and identify the oscillating term. What is its angular frequency? *(Difficulty: application.)*

5. *[Tests: when "stationary" fails]* A student claims: "The wave function of an electron in a hydrogen atom is a stationary state, so nothing changes over time." (a) In what sense is this exactly right? (b) In what sense is it exactly wrong — what is changing? (c) The student then says: "If I put the electron in a superposition of two hydrogen energy levels, the wave function will stop being a stationary state and the electron will start emitting light." Identify what is correct and what is incomplete in this claim. *(Difficulty: application.)*

6. *[Tests: energy conservation in a superposition]* A particle is in the state $\Psi(x,t) = c_1\psi_1 e^{-iE_1 t/\hbar} + c_2\psi_2 e^{-iE_2 t/\hbar} + c_3\psi_3 e^{-iE_3 t/\hbar}$ with $|c_1|^2 = 0.5$, $|c_2|^2 = 0.3$, $|c_3|^2 = 0.2$. (a) Compute $\langle\hat{H}\rangle$ in terms of $E_1, E_2, E_3$. (b) Show this is constant by computing $d\langle\hat{H}\rangle/dt$. (c) If you measure the energy once, what are the possible outcomes and their probabilities? (d) After the measurement, what is the state? *(Difficulty: application.)*

**Synthesis**

7. *[Tests: structural comparison between QM and the heat equation]* The heat equation is $\partial_t u = D\,\partial_{xx} u$ with boundary conditions $u(0,t) = u(L,t) = 0$. (a) Apply separation of variables and find the spatial eigenfunctions. Compare them to the TISE eigenstates for the infinite well. (b) The time-dependent part of each solution is $e^{-Dk_n^2 t}$ for the heat equation versus $e^{-iE_n t/\hbar}$ for the Schrödinger equation. What is the key structural difference, and what does it imply about whether probability (or heat) is conserved? (c) In one sentence: why does the imaginary unit in the TDSE make quantum mechanics unitary (probability-preserving) rather than dissipative? *(Difficulty: synthesis.)*

8. *[Tests: constructing initial conditions and projecting onto eigenstates]* Suppose the initial state in a well of width $L$ is $\Psi(x,0) = Ax(L-x)$ for $0 \leq x \leq L$ (a parabola that vanishes at both walls). (a) Normalize: find $A$ such that $\int_0^L|\Psi|^2\,dx = 1$. (b) The expansion coefficient is $c_n = \int_0^L\psi_n(x)\,\Psi(x,0)\,dx$. Show that $c_n = 0$ for all even $n$, and explain why using the symmetry of the parabola and the parity of the sine eigenstates. (c) Write down $\Psi(x,t)$ as a series, keeping only the dominant terms. *(Difficulty: synthesis.)*

---

## Still Puzzling

The separation-of-variables trick is presented here as a technique for finding separable solutions, with completeness invoked as a separate theorem to justify that these solutions span everything. A deeper question is: why should $\hat{H}$ be self-adjoint, and what exactly does "self-adjoint" require when the domain of $\hat{H}$ is the set of square-integrable functions that vanish at the walls? The answer involves functional analysis (specifically, the theory of extensions of symmetric operators) and is treated carefully in Reed and Simon's *Methods of Modern Mathematical Physics*, Volumes 1 and 2. At this level, it is enough to know that physical Hamiltonians are self-adjoint, that self-adjoint operators have real eigenvalues and complete eigenbases, and that the theorem is not circular.

The claim that the completeness of the Fourier sine basis is "classical mathematics" from Fourier's 1822 work is a slight compression. Fourier showed the basis works for heat-conduction problems; the rigorous proof that the sine series converges in $L^2$ to any square-integrable function (on a bounded interval with Dirichlet boundary conditions) came later, through Parseval's theorem and Hilbert-space completeness arguments that Hilbert and others developed in the early twentieth century. Fourier's result was right; its proof took another century.

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

**The frozen square.** Set $c_1 = 1$, all others zero. Play the animation. Watch Re $\Psi$ and Im $\Psi$ spin like the hands of a clock — they oscillate at frequency $E_1/\hbar$. Watch $|\Psi|^2$ not move. Write one sentence explaining why: the phase of Re $\Psi$ and the phase of Im $\Psi$ rotate together, so $|\mathrm{Re}\,\Psi|^2 + |\mathrm{Im}\,\Psi|^2 = |\Psi|^2$ stays constant.

**The sloshing pair.** Switch to $c_1 = c_2 = 1/\sqrt{2}$, $\theta_1 = \theta_2 = 0$. Observe $|\Psi(x,t)|^2$ oscillating. Read $\langle x\rangle(t)$ and notice it swings. Now read $\langle H\rangle$: it does not move. Write two sentences: (1) what is happening to the probability distribution, (2) what is not happening to the energy.

**Phase flipping.** With $c_1 = c_2 = 1/\sqrt{2}$, change $\theta_2$ from 0 to $\pi$. Watch the initial shape of $|\Psi|^2$ flip from left-heavy to right-heavy. Explain: at $t = 0$, the state is proportional to $\psi_1 + e^{i\theta_2}\psi_2$; changing $\theta_2$ by $\pi$ changes $\psi_1 + \psi_2$ to $\psi_1 - \psi_2$, which has a completely different spatial shape.

**Energy precision.** Try $c_1 = 0.6$, $c_2 = 0.8$ (after normalization, $|c_1|^2 + |c_2|^2 = 1$). Read $\langle H\rangle$. Now measure: if you measured the particle's energy, what value would you get, and with what probability? The measurement would collapse the state — after the measurement you would have a stationary state, and $|\Psi|^2$ would stop oscillating.

---

## References

- Schrödinger, E. (1926). Quantisierung als Eigenwertproblem [Quantization as an eigenvalue problem]. *Annalen der Physik*, 79, 361–376. [verify] (First paper on the wave equation. English translation in: Schrödinger, E. *Collected Papers on Wave Mechanics*, Blackie and Son, 1928.)
- Griffiths, D. J., & Schroeter, D. F. (2018). *Introduction to Quantum Mechanics* (3rd ed.). Cambridge University Press. §2.1.
- Shankar, R. (1994). *Principles of Quantum Mechanics* (2nd ed.). Plenum. §5.1.
- von Neumann, J. (1932). *Mathematische Grundlagen der Quantenmechanik*. Springer. (Modern spectral theory and self-adjointness; English translation: *Mathematical Foundations of Quantum Mechanics*, Princeton University Press, 1955.)
- Stein, E. M., & Shakarchi, R. (2003). *Fourier Analysis: An Introduction*. Princeton University Press. Ch. 4. (Completeness of the Fourier sine basis in $L^2$.)
- Reed, M., & Simon, B. (1975). *Methods of Modern Mathematical Physics, Vol. 2: Fourier Analysis, Self-Adjointness*. Academic Press. (Rigorous treatment of self-adjointness and spectral theory for quantum-mechanical operators.)
