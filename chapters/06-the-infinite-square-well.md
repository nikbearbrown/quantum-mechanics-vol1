# Chapter 5 — The Infinite Square Well

## TL;DR

- Quantization is not assumed — it falls out of asking a sine wave to vanish at both walls simultaneously. Boundary conditions are the engine; the discrete spectrum is the exhaust.
- The allowed energies scale as $n^2$: $E_n = n^2\pi^2\hbar^2/(2mL^2)$. The ratio $E_n/E_1 = n^2$ is exactly 1, 4, 9, 16, … — nothing in between.
- The eigenstates $\psi_n(x) = \sqrt{2/L}\,\sin(n\pi x/L)$ are orthonormal: a single trigonometric identity proves it without numerical computation.
- A general state is a superposition; time evolution phase-rotates each eigenstate independently; the result is sloshing probability at the beat frequency $(E_2-E_1)/\hbar$.
- The ground-state energy $E_1 > 0$ is required by the uncertainty principle — a confined particle cannot have zero kinetic energy.

---

In 1993, physicists at IBM's Almaden Research Center spent days nudging individual iron atoms across a copper surface with the tip of a scanning tunneling microscope. They arranged 48 atoms into a ring — a "quantum corral" — and then imaged the electron density inside. What they saw was not a smooth puddle of charge. It was a bull's-eye pattern of concentric rings, standing waves in the electron density, exactly as predicted by the Schrödinger equation for an electron confined to a circular domain.

The quantum corral is not an infinite square well — it is circular, not linear, and the walls are not infinite. But the physics is the same: confine an electron, and it can only exist in modes that fit the container. The modes look like standing waves because they are standing waves. The allowed energies are discrete because only certain spatial frequencies match the boundary conditions. Crommie, Lutz, and Eigler did not put the quantization in. The walls imposed it.

This chapter does the one-dimensional version. Same argument, cleaner geometry, closed-form answers.

---

## Learning Objectives

By the end of this chapter you will be able to:

1. **Apply** the boundary conditions of the infinite square well to the general TISE solution and derive the quantized wave vectors $k_n = n\pi/L$. *(Apply — Bloom Level 3)*

2. **Derive** and **use** the energy spectrum $E_n = n^2\pi^2\hbar^2/(2mL^2)$ and eigenstates $\psi_n(x) = \sqrt{2/L}\,\sin(n\pi x/L)$. *(Apply — Bloom Level 3)*

3. **Verify** orthonormality of the eigenstates using the product-to-sum trigonometric identity. *(Apply — Bloom Level 3)*

4. **Construct** a two-state time-evolved superposition, compute $\langle x\rangle(t)$, and identify the sloshing frequency and amplitude. *(Analyze — Bloom Level 4)*

5. **Explain** the zero-point energy $E_1 > 0$ as a consequence of the uncertainty principle, and simulate superpositions to observe energy conservation during sloshing. *(Evaluate — Bloom Level 5)*

---

## Scene Opening

A guitar string, tuned to A, is fixed to the bridge at one end and the nut at the other. Pluck it anywhere. The string vibrates. But listen carefully: the dominant sound is at 440 Hz — the fundamental frequency — with fainter overtones at 880 Hz, 1320 Hz, 1760 Hz, and so on. Integer multiples of the fundamental. Why those frequencies and not others?

The answer is geometry. A mode survives only if it fits the string: it must have a node at the bridge and a node at the nut. A half-wavelength must fit. Or a whole wavelength. Or a wavelength-and-a-half. But half-a-wavelength-and-a-third does not fit: the mode cannot be continuous at both fixed endpoints simultaneously, so it dies on contact with itself. The boundary conditions select the spectrum.

A particle in a box is the same argument, dressed in quantum language. The wave function $\psi(x)$ must vanish at both walls. The modes that survive are those that fit. Those modes are the eigenstates. Their discrete frequencies — or rather, their discrete energies — are the spectrum.

We have been building up to this argument for four chapters. Now we do it, step by step, without shortcuts.

---

## Core Development

### The Potential and What It Forces

The infinite square well potential is

$$V(x) = \begin{cases} 0 & 0 < x < L, \\ \infty & x \leq 0 \text{ or } x \geq L. \end{cases}$$

Where $V = \infty$, the wave function must vanish. This is not a separate assumption; it is what $V = \infty$ means in the Schrödinger equation. If $\psi \neq 0$ in a region where $V = \infty$, the TISE $-(\hbar^2/2m)\psi'' + V\psi = E\psi$ cannot balance: $V\psi$ would be infinite, but $E\psi$ and $-(\hbar^2/2m)\psi''$ are finite. So $\psi = 0$ outside $[0, L]$.

By continuity of the wave function (a requirement from the fact that $\psi$ must be square-integrable and the probability current $J \propto \psi^*\partial_x\psi$ must be finite):

$$\psi(0) = 0, \qquad \psi(L) = 0. \tag{5.1}$$

These are the **Dirichlet boundary conditions**. They are the walls made mathematical.

### The Eight Steps to a Spectrum

**Step 1: TISE inside the well.** Since $V = 0$ for $0 < x < L$, the time-independent Schrödinger equation is

$$-\frac{\hbar^2}{2m}\,\frac{d^2\psi}{dx^2} = E\,\psi.$$

**Step 2: What sign can $E$ have?** We can show $E > 0$ is required. If $E < 0$, define $\kappa^2 = -2mE/\hbar^2 > 0$. The equation becomes $\psi'' = \kappa^2\psi$, with general solution $\psi = Ae^{\kappa x} + Be^{-\kappa x}$. This cannot satisfy $\psi(0) = \psi(L) = 0$ with $A$ and $B$ both nonzero (the only solution is $A = B = 0$, the trivial case). So $E < 0$ gives no normalizable solution. If $E = 0$, the equation is $\psi'' = 0$, giving $\psi = ax + b$; applying $\psi(0) = 0$ gives $b = 0$, and $\psi(L) = aL = 0$ gives $a = 0$. Again the trivial solution. So $E = 0$ is excluded. Only $E > 0$ works.

**Step 3: The general solution for $E > 0$.** Define

$$k = \frac{\sqrt{2mE}}{\hbar}, \qquad k > 0.$$

The TISE reads $\psi'' = -k^2\psi$ — the equation of a spatial harmonic oscillator. The general solution:

$$\psi(x) = A\sin(kx) + B\cos(kx). \tag{5.2}$$

Any positive value of $k$ — any positive value of $E$ — satisfies this equation. No quantization yet. The boundary conditions have not been applied.

**Step 4: Apply the boundary condition at $x = 0$.**

$$\psi(0) = A\sin(0) + B\cos(0) = B = 0.$$

So $B = 0$. The cosine term is eliminated:

$$\psi(x) = A\sin(kx). \tag{5.3}$$

Still no quantization — any positive $k$ still works.

**Step 5: Apply the boundary condition at $x = L$.**

$$\psi(L) = A\sin(kL) = 0.$$

Either $A = 0$ (no particle, trivial) or

$$\sin(kL) = 0. \tag{5.4}$$

**Step 6: Quantization.** This is the "oh" moment. $\sin(kL) = 0$ holds only when $kL$ is an integer multiple of $\pi$:

$$kL = n\pi, \quad n = 1, 2, 3, \ldots$$

The continuous range of allowed $k$ — which was every positive real number — has collapsed to a discrete set, indexed by a positive integer. This is where the quantization enters, and exactly where it enters: not from a postulate about angular momentum or a new law of nature, but from asking the sine wave to vanish at both walls simultaneously. Bohr postulated quantization; Schrödinger derived it.

Why $n = 0$ does not count: $k_0 = 0$ gives $\psi = A\sin(0) = 0$ everywhere — no particle.

Why negative $n$ does not give new states: $\sin(-n\pi x/L) = -\sin(n\pi x/L)$, which is the same physical state as $+\sin(n\pi x/L)$ (identical $|\psi|^2$, just an overall sign difference, which is unobservable).

**Step 7: Energy levels.** From $k_n = n\pi/L$ and $E = \hbar^2 k^2/(2m)$:

$$\boxed{E_n = \frac{n^2\pi^2\hbar^2}{2mL^2}, \qquad n = 1, 2, 3, \ldots} \tag{5.5}$$

The energies scale as $n^2$. The first few ratios: $E_1 : E_2 : E_3 : E_4 = 1 : 4 : 9 : 16$. Nothing lives between these values. For an electron in a well of width $L = 1$ nm:

$$E_1 = \frac{\pi^2(1.055\times10^{-34})^2}{2(9.109\times10^{-31})(10^{-9})^2} \approx 6.03\times10^{-20}\ \text{J} \approx 0.377\ \text{eV}.$$

So $E_1 \approx 0.38$ eV, $E_2 \approx 1.51$ eV, $E_3 \approx 3.39$ eV. These are energies on the scale of chemistry and optics — visible photons carry roughly 2 eV, and thermal energy at room temperature is $k_BT \approx 0.025$ eV. A 1 nm quantum well has level spacings that are large compared to thermal energy. Quantum effects are not just relevant — they are dominant.

For contrast, a marble of mass $m = 1$ g in a box of $L = 1$ cm:

$$E_1 \approx \frac{\pi^2(10^{-34})^2}{2(10^{-3})(10^{-2})^2} \approx 5\times10^{-62}\ \text{J} \approx 3\times10^{-43}\ \text{eV}.$$

This is immeasurably small compared to any energy in the marble's environment. The quantum discreteness is there in principle; it is completely invisible in practice. The classical limit is not a philosophical choice — it is a calculation.

**Step 8: Normalization.** The unnormalized eigenstate is $\psi_n(x) = A\sin(n\pi x/L)$. Apply $\int_0^L|\psi_n|^2\,dx = 1$:

$$A^2\int_0^L\sin^2\!\left(\frac{n\pi x}{L}\right)dx = A^2\cdot\frac{L}{2} = 1 \implies A = \sqrt{\frac{2}{L}}.$$

(The integral uses $\sin^2\theta = (1-\cos 2\theta)/2$; over a whole number of half-periods, the cosine term integrates to zero.)

The normalized eigenstates are

$$\boxed{\psi_n(x) = \sqrt{\frac{2}{L}}\,\sin\!\left(\frac{n\pi x}{L}\right), \quad 0 \leq x \leq L;} \qquad \psi_n(x) = 0 \text{ elsewhere.} \tag{5.6}$$

### Counting Nodes

Each eigenstate $\psi_n$ has exactly $n-1$ zeros inside the open interval $(0, L)$ — that is, strictly interior nodes, not counting the walls. $\psi_1$: no interior nodes, one half-period sine filling the well. $\psi_2$: one node at $x = L/2$, two half-periods. $\psi_n$: $n$ half-periods fitted between the walls, with $n-1$ interior nodes.

More nodes means shorter wavelength. Shorter wavelength means higher spatial frequency. Higher spatial frequency means higher momentum (since $p = \hbar k = n\pi\hbar/L$) and higher kinetic energy ($E = p^2/2m = n^2\pi^2\hbar^2/2mL^2$). Node counting is a spatial Fourier logic: the $n$-th mode has exactly $n$ half-wavelengths fitting into the box.

### Orthonormality — the Trigonometric Proof

The eigenstates satisfy

$$\langle\psi_m|\psi_n\rangle = \int_0^L\psi_m(x)\,\psi_n(x)\,dx = \delta_{mn}. \tag{5.7}$$

(Since the $\psi_n$ are real-valued, $\psi_m^* = \psi_m$.)

**Proof.** Use the product-to-sum identity:

$$\sin\alpha\,\sin\beta = \frac{1}{2}\bigl[\cos(\alpha-\beta) - \cos(\alpha+\beta)\bigr].$$

So

$$\langle\psi_m|\psi_n\rangle = \frac{2}{L}\int_0^L\sin\!\left(\frac{m\pi x}{L}\right)\sin\!\left(\frac{n\pi x}{L}\right)dx = \frac{1}{L}\int_0^L\!\left[\cos\!\left(\frac{(m-n)\pi x}{L}\right) - \cos\!\left(\frac{(m+n)\pi x}{L}\right)\right]dx.$$

For $m \neq n$: both integrals are cosines over an integer number of half-periods on $[0, L]$, so both integrate to zero. $\langle\psi_m|\psi_n\rangle = 0$.

For $m = n$: the first cosine becomes $\cos(0) = 1$, integrating to $L$; the second is $\cos(2n\pi x/L)$, a cosine over $n$ complete periods, integrating to zero. So $\langle\psi_n|\psi_n\rangle = (1/L)\cdot L = 1$.

No numerical eigensolver. No Gram-Schmidt. A single trigonometric identity. This is why the simulation is forbidden from using Gram-Schmidt: it would conceal the fact that orthogonality is an analytic, exact result, not a computational approximation.

### Zero-Point Energy — Why the Ground State Cannot Be Still

The lowest energy is $E_1 = \pi^2\hbar^2/(2mL^2) > 0$. The particle cannot have $E = 0$.

The uncertainty principle gives the reason. If $E = 0$, then kinetic energy $= 0$, so momentum $= 0$, so $\sigma_p = 0$. But the particle is confined to $[0, L]$, so its position is known to within $L$: $\sigma_x \leq L$. The Kennard inequality $\sigma_x\sigma_p \geq \hbar/2$ then gives $L\cdot 0 = 0 \geq \hbar/2$, which is false. The uncertainty principle prohibits $E = 0$ for any confined particle. Zero-point energy is not a quantum anomaly — it is the uncertainty principle made quantitative.

Numerically, for the ground state: $\sigma_x = L\sqrt{1/12 - 1/(2\pi^2)} \approx 0.181\,L$ and $\sigma_p = \pi\hbar/L$ (computed below), giving $\sigma_x\sigma_p \approx 0.568\,\hbar \approx 1.136 \times (\hbar/2)$. The ground state satisfies the uncertainty bound with a ratio of about 1.136 — not far above the minimum of 1. The ground state of the infinite well is, in a precise sense, close to the most localized state quantum mechanics permits.

The guitar-string analogy holds here too: a guitar string fixed at both ends cannot vibrate at zero frequency without being completely flat (no displacement). The minimum non-trivial mode has a positive frequency. Zero frequency requires zero amplitude — no vibration, no particle.

### Completeness and Fourier Analysis

The eigenstates $\{\psi_n\}$ form a complete basis for square-integrable functions on $[0, L]$ that vanish at the endpoints. Any such function $f(x)$ can be written:

$$f(x) = \sum_{n=1}^{\infty} c_n\,\psi_n(x), \qquad c_n = \int_0^L\psi_n(x)\,f(x)\,dx. \tag{5.8}$$

This is the Fourier sine series. Fourier established it in 1822, analyzing heat conduction — more than a century before quantum mechanics. The coefficients $c_n$ are the inner products, the projections of $f$ onto each basis function.

Given an initial state $\Psi(x, 0)$, expand it in the eigenbasis (computing $c_n$ by the inner product), then attach the time-evolution phase to each term:

$$\Psi(x, t) = \sum_{n=1}^{\infty} c_n\,\psi_n(x)\,e^{-iE_n t/\hbar}. \tag{5.9}$$

This is the complete solution for any initial condition. Each eigenstate rotates at its own angular frequency $\omega_n = E_n/\hbar$. When two or more states with different energies are present, the relative phases evolve and observable dynamics emerge.

---

## Worked Example — The Two-State Superposition and Its Oscillating $\langle x\rangle$

**Setup.** Take the equal-weight superposition of the first two eigenstates:

$$\Psi(x, t) = \frac{1}{\sqrt{2}}\,\psi_1(x)\,e^{-iE_1 t/\hbar} + \frac{1}{\sqrt{2}}\,\psi_2(x)\,e^{-iE_2 t/\hbar}. \tag{5.10}$$

The coefficients $c_1 = c_2 = 1/\sqrt{2}$ are real and equal, both taken to be positive (this fixes the initial relative phase to zero).

**The probability density.** Since $\psi_1$ and $\psi_2$ are real:

$$|\Psi(x,t)|^2 = \frac{1}{2}\!\left[\psi_1^2 + \psi_2^2 + 2\,\psi_1\psi_2\,\cos\!\left(\frac{(E_2-E_1)t}{\hbar}\right)\right]. \tag{5.11}$$

The cross term oscillates at angular frequency $\omega = (E_2-E_1)/\hbar = 3E_1/\hbar$, since $E_2 = 4E_1$ and $E_1 = E_2 - 3E_1$. The period of oscillation is

$$T = \frac{2\pi\hbar}{E_2-E_1} = \frac{2\pi\hbar}{3E_1} = \frac{h}{3E_1}. \tag{5.12}$$

For the $L = 1$ nm electron: $E_1 \approx 6.03\times10^{-20}$ J, so $T = h/(3E_1) \approx 3.66\times10^{-15}$ s $= 3.66$ fs. The probability density swings from one side of the well to the other in about 3.7 femtoseconds.

**Computing $\langle x\rangle(t)$.** By symmetry, $\langle x\rangle_1 = \langle x\rangle_2 = L/2$ — both eigenstates are symmetric about the center of the well. So

$$\langle x\rangle(t) = \frac{L}{2} + \cos\!\left(\frac{(E_2-E_1)t}{\hbar}\right)\int_0^L x\,\psi_1(x)\,\psi_2(x)\,dx. \tag{5.13}$$

The cross integral $I = \int_0^L x\,\psi_1\psi_2\,dx$ needs to be computed. Using the product-to-sum identity:

$$I = \frac{2}{L}\int_0^L x\,\sin\!\left(\frac{\pi x}{L}\right)\sin\!\left(\frac{2\pi x}{L}\right)dx = \frac{1}{L}\int_0^L x\!\left[\cos\!\left(\frac{\pi x}{L}\right) - \cos\!\left(\frac{3\pi x}{L}\right)\right]dx.$$

Each integral has the form $\int_0^L x\cos(n\pi x/L)\,dx$. Integrate by parts: let $u = x$, $dv = \cos(n\pi x/L)\,dx$:

$$\int_0^L x\cos\!\left(\frac{n\pi x}{L}\right)dx = \left[\frac{xL}{n\pi}\sin\!\left(\frac{n\pi x}{L}\right)\right]_0^L - \frac{L}{n\pi}\int_0^L\sin\!\left(\frac{n\pi x}{L}\right)dx.$$

The first term vanishes at both limits (since $\sin(n\pi) = 0$ and $x = 0$ forces the other factor to zero). The second integral:

$$-\frac{L}{n\pi}\left[-\frac{L}{n\pi}\cos\!\left(\frac{n\pi x}{L}\right)\right]_0^L = \frac{L^2}{n^2\pi^2}\bigl[\cos(n\pi) - \cos(0)\bigr] = \frac{L^2}{n^2\pi^2}\bigl[(-1)^n - 1\bigr].$$

For $n = 1$: $\frac{L^2}{\pi^2}[(-1)-1] = -\frac{2L^2}{\pi^2}$.

For $n = 3$: $\frac{L^2}{9\pi^2}[(-1)-1] = -\frac{2L^2}{9\pi^2}$.

Therefore:

$$I = \frac{1}{L}\left[\left(-\frac{2L^2}{\pi^2}\right) - \left(-\frac{2L^2}{9\pi^2}\right)\right] = \frac{2L}{\pi^2}\!\left(-1 + \frac{1}{9}\right) = \frac{2L}{\pi^2}\cdot\!\left(-\frac{8}{9}\right) = -\frac{16L}{9\pi^2}. \tag{5.14}$$

The cross integral is negative: $I \approx -0.180\,L$.

**The result:**

$$\langle x\rangle(t) = \frac{L}{2} - \frac{16L}{9\pi^2}\cos\!\left(\frac{(E_2-E_1)t}{\hbar}\right). \tag{5.15}$$

**Reading the sign.** At $t = 0$: $\cos(0) = 1$, so

$$\langle x\rangle(0) = \frac{L}{2} - \frac{16L}{9\pi^2} \approx \frac{L}{2} - 0.180L \approx 0.320L.$$

The initial probability distribution is left-heavy: the particle is more likely to be found in the left half of the well at $t = 0$. This makes sense geometrically: at $t = 0$, $|\Psi|^2 = \frac{1}{2}(\psi_1 + \psi_2)^2$. The function $\psi_1 + \psi_2$ is the sum of a half-sine (peaked at $L/2$) and a full-sine (peaked at $L/4$ and negative at $3L/4$); the combined peak lands at $x \approx L/4$, pulling $\langle x\rangle$ left of center.

The time derivative at $t = 0$:

$$\frac{d\langle x\rangle}{dt}\bigg|_{t=0} = \frac{16L\omega}{9\pi^2}\sin(0) = 0.$$

So $\langle x\rangle$ starts at a turning point. Just after $t = 0$, $\sin(\omega t) > 0$, so $d\langle x\rangle/dt > 0$: the particle's average position moves rightward, toward $L/2$, and then overshoots to approximately $0.680L$ at half-period, before returning. The particle starts left-heavy and first sloshes right.

**A note on the sign convention and the simulation.** The research notes for this chapter flag a potential sign ambiguity: the lib-file simulation prompt specifies that $\langle x\rangle$ should "first decrease (slosh left)" for the $e^{-iEt/\hbar}$ convention. This is inconsistent with the calculation above, which shows that with $c_1 = c_2 = 1/\sqrt{2}$ (both real and positive), the initial state is left-heavy and $\langle x\rangle$ first increases (moves right). The discrepancy arises because the lib file appears to assume the initial $\langle x\rangle = L/2$, which holds only for a single eigenstate or a specially tuned superposition — not for this equal-coefficient initial condition. The calculation (5.15) is correct. [verify] Any simulation implementing $c_1 = c_2 = 1/\sqrt{2}$, $\theta_1 = \theta_2 = 0$, and the $e^{-iEt/\hbar}$ convention should show $\langle x\rangle(0) \approx 0.320L$ and initial rightward motion. If your simulation shows $\langle x\rangle(0) = L/2$ with initial leftward motion, check whether the phase convention has been accidentally flipped to $e^{+iEt/\hbar}$.

**The amplitude.** $\langle x\rangle(t)$ oscillates between $0.320L$ and $0.680L$, a total swing of $0.360L$. The center is $L/2$. The amplitude is $16L/(9\pi^2) \approx 0.180L$.

**Energy.** Throughout all of this, $\langle\hat{H}\rangle = (E_1 + E_2)/2 \approx (0.377 + 1.508)/2 \approx 0.943$ eV. Constant. The probability is sloshing; the energy is not. The particle is moving (in the sense that its probability distribution is shifting across the well) while carrying a fixed energy budget. This is genuinely non-classical: in a classical well with $V = 0$ inside, a particle that is moving carries kinetic energy and its energy budget is the same as its kinetic energy, which is fixed. But classically, where the particle *is* and what energy it *has* are related — they are the same observable (the particle is at a definite point and has a definite speed). Quantum mechanically, the where (probability distribution, encoded in $|\Psi|^2$) and the how much energy ($\langle\hat{H}\rangle$, encoded in the $|c_n|^2$) are distinct quantities that evolve independently.

---

## Common Misconceptions

**"Quantization is a postulate of quantum mechanics."** For the infinite well (and more generally, for any confining potential), quantization follows from the boundary conditions applied to the Schrödinger equation. It is a theorem, not an assumption. Bohr's 1913 postulation of discrete angular momenta was a hypothesis that fit the data; Schrödinger's 1926 wave equation showed it was a consequence.

**"$n = 0$ is the ground state."** $n = 0$ gives $\psi(x) = 0$ everywhere — no particle. The lowest state is $n = 1$, with energy $E_1 > 0$.

**"Negative $n$ gives additional states."** $\sin(-n\pi x/L) = -\sin(n\pi x/L)$: the probability density $|\psi_{-n}|^2 = |\psi_n|^2$ is identical. Negative $n$ does not add new states; it is the same state up to an unobservable global sign.

**"The sloshing means the particle's energy is changing."** $\langle\hat{H}\rangle = |c_1|^2 E_1 + |c_2|^2 E_2$ — constant, because $|c_n|^2$ does not depend on time. The sloshing is a phase effect: the relative phase between $c_1 e^{-iE_1 t/\hbar}$ and $c_2 e^{-iE_2 t/\hbar}$ evolves, changing the interference pattern in $|\Psi|^2$. The energy budget is unchanged.

**"The normalization constant $\sqrt{2/L}$ is the wave function's maximum value."** For $n = 1$, the maximum of $|\psi_1|$ is $\sqrt{2/L}$ (at $x = L/2$). But for $n = 2$, the maximum is also $\sqrt{2/L}$ (at $x = L/4$ and $3L/4$). The normalization constant is a fixed prefactor; the wave function's spatial shape — and hence where its maximum falls — is determined by the sine.

**"Orthogonality must be verified numerically."** The exact analytic proof from the product-to-sum identity takes three lines. Gram-Schmidt is not needed and conceals the mathematical structure. The exact orthogonality of the $\sin(n\pi x/L)$ functions is a theorem in classical Fourier analysis.

---

## Exercises

**Warm-up**

1. *[Tests: applying the eight-step derivation]* Starting from the TISE with $V = 0$ inside $[0, L]$: (a) Write the general solution $\psi(x) = A\sin(kx) + B\cos(kx)$. (b) Apply $\psi(0) = 0$ to determine $B$. (c) Apply $\psi(L) = 0$ and explain why $\sin(kL) = 0$ leads to a discrete spectrum while $A\sin(kL) = 0$ with $A = 0$ is excluded. (d) Write down $k_n$, $E_n$, and the normalized $\psi_n(x)$. At which step does quantization first appear? *(Difficulty: warm-up.)*

2. *[Tests: $n^2$ energy scaling and physical scale]* For an electron ($m = 9.109\times10^{-31}$ kg) in a well of width $L = 2$ nm: (a) Compute $E_1$, $E_2$, $E_3$ in eV. (b) Verify $E_2/E_1 = 4$ and $E_3/E_1 = 9$ to three significant figures. (c) How do these values compare to $k_BT = 0.025$ eV at room temperature — are quantum effects significant? (d) If $L$ were doubled to 4 nm, how would $E_1$ change? *(Difficulty: warm-up.)*

3. *[Tests: orthonormality via trigonometric identity]* Verify $\langle\psi_1|\psi_2\rangle = 0$ directly, using the product-to-sum identity $\sin\alpha\sin\beta = \frac{1}{2}[\cos(\alpha-\beta)-\cos(\alpha+\beta)]$. Show all steps. Then verify $\langle\psi_1|\psi_1\rangle = 1$ by the same method. *(Difficulty: warm-up.)*

**Application**

4. *[Tests: zero-point energy from uncertainty]* (a) Argue from the uncertainty principle that a particle confined to $[0,L]$ cannot have $E = 0$. Be precise: what does $E = 0$ imply for $\sigma_p$, and why does this contradict $\sigma_x \leq L$? (b) Compute $\sigma_p$ for the ground state using $\hat{p} = -i\hbar\,\partial_x$: show $\langle p\rangle = 0$ and $\langle p^2\rangle = \pi^2\hbar^2/L^2$, so $\sigma_p = \pi\hbar/L$. (c) Compute $\sigma_x$ for the ground state. (Hint: $\langle x\rangle = L/2$ by symmetry; use $\langle x^2\rangle = L^2(1/3 - 1/(2\pi^2))$.) Verify $\sigma_x\sigma_p \geq \hbar/2$. *(Difficulty: application.)*

5. *[Tests: time evolution of a superposition]* A particle is prepared in $\Psi(x,0) = \frac{1}{\sqrt{2}}(\psi_1 + \psi_3)$. (a) Write $\Psi(x,t)$. (b) Compute $|\Psi(x,t)|^2$ and identify the cross term and its oscillation frequency. (c) Compute $\langle\hat{H}\rangle$. (d) Is $\langle x\rangle = L/2$ for all $t$? Argue from the parity symmetry of $\psi_1$ and $\psi_3$ about $x = L/2$. *(Difficulty: application.)*

6. *[Tests: projection and expansion coefficients]* Suppose an initial state is given numerically as $\Psi(x,0) = Bx(L-x)$ for $0 \leq x \leq L$, with $B$ chosen so $\int_0^L|\Psi|^2\,dx = 1$. (a) Find $B$. (b) Show that $c_n = \langle\psi_n|\Psi(x,0)\rangle = 0$ for all even $n$, using the symmetry of $\Psi(x,0)$ about $x = L/2$ and the parity of $\psi_n$ about the same point. (c) Compute $c_1 = \int_0^L\psi_1(x)\,Bx(L-x)\,dx$ by direct integration. Check: $|c_1|^2 \approx 0.999$, confirming the parabola is almost entirely in the ground state. *(Difficulty: application.)*

**Synthesis and Produce**

7. *[Tests: computing ⟨x⟩(t) from first principles; produce a complete calculation]* For the superposition $\Psi(x,t) = \frac{1}{\sqrt{2}}(\psi_1 e^{-iE_1 t/\hbar} + \psi_2 e^{-iE_2 t/\hbar})$: (a) Show that $\langle x\rangle(t) = L/2 - (16L/9\pi^2)\cos((E_2-E_1)t/\hbar)$ by computing the cross integral $\int_0^L x\psi_1\psi_2\,dx$ via integration by parts. Show all steps. (b) What are the maximum and minimum values of $\langle x\rangle(t)$? (c) What is the physical meaning of the amplitude $16L/(9\pi^2)$? (d) Confirm that $d\langle x\rangle/dt |_{t=0} > 0$ and state the initial direction of sloshing. *(Difficulty: synthesis; you produce the full calculation.)*

8. *[Tests: connecting quantum discreteness to an observable]* An electron in a $L = 1$ nm well emits a photon and drops from $n = 3$ to $n = 1$. (a) Compute the photon energy $E_3 - E_1$ in eV. (b) Compute the photon wavelength $\lambda = hc/(E_3 - E_1)$. Is this in the visible range, UV, or IR? (c) Semiconductor quantum-well lasers tune the emission wavelength by adjusting $L$. What well width would produce emission at $\lambda = 650$ nm (red light), for a GaAs effective mass $m^* \approx 0.067\,m_e$? *(Difficulty: synthesis.)*

---

## Still Puzzling

The infinite square well's walls are literally infinite — an idealization that no physical system achieves. Real quantum dots, semiconductor wells, and optical lattice sites have finite barriers, and there are always some probability amplitudes that "leak" through the walls (tunneling) or extend into the barrier region. The infinite well is a limiting case: as the barrier height $V_0 \to \infty$, the finite-well energy levels approach the infinite-well values from below, and the wave-function tails in the barrier shrink to zero. Chapter 7 will do the finite-well calculation explicitly, and you will see how the infinite-well results are recovered as a limit.

The zero-point energy argument via the uncertainty principle gives the correct sign ($E_1 > 0$) but not the exact value ($E_1 = \pi^2\hbar^2/2mL^2$). The uncertainty principle says $E_1 \geq \hbar^2/(8mL^2)$ (using $\sigma_x \leq L/2$ and $E \sim p^2/2m \sim \sigma_p^2/2m$), which is weaker than the exact result by a factor of $\pi^2/2 \approx 5$. The exact result requires solving the TISE; the uncertainty-principle argument gives a lower bound. The distinction matters when a student asks whether they can use the uncertainty principle to estimate energies — they can, but only as an order-of-magnitude argument, not an exact calculation.

The convergence of the Fourier sine series for non-smooth initial conditions is slow (the "draw your own $\psi$" simulation makes this visible). If the initial state has a discontinuity, the series converges in $L^2$ — the integral of the squared difference goes to zero — but not pointwise at the discontinuity. At a jump, the series converges to the average of the left and right limits: the **Gibbs phenomenon**. This does not cause a physical problem (the particle's probability is not defined pointwise, only through integrals), but it looks like a ringing artifact in the simulation. It is real mathematics, not a numerical bug.

The sloshing period $T = h/(E_2 - E_1) = h/(3E_1) \approx 3.66$ fs for a 1 nm electron is so short that it has never been directly observed in a time-domain measurement of an infinite-square-well analog. In real systems (quantum dots, cold-atom traps), the sloshing is observable in certain contexts — but the direct correspondence to this clean two-state formula requires a system close enough to the ideal well that the higher-order corrections are negligible. That is an ongoing experimental challenge in quantum control.

---

## The +1 — Simulation Exercise

### Part A — `CLAUDE.md` snippet for this chapter

Add this stanza to your existing `CLAUDE.md`:

````markdown
## Chapter 5 — Infinite Square Well

- Eigenstates: ψ_n(x) = √(2/L) sin(nπx/L) for 0 ≤ x ≤ L, zero elsewhere.
  Closed form; do NOT use Gram-Schmidt or a numerical eigensolver.
- Energy levels: E_n = n² π² ℏ² / (2mL²). For L = 1 nm, electron:
  E_1 ≈ 0.377 eV, E_2 ≈ 1.508 eV, E_3 ≈ 3.39 eV.
  Verify E_n / E_1 = n² to 4 significant figures in displayed values.
- Boundary conditions: DIRICHLET (ψ = 0 at x = 0 and x = L).
  Never Neumann. The n=1 state must visibly vanish at both walls.
- Time evolution: ANALYTIC. Ψ(x,t) = Σ c_n ψ_n(x) exp(−iE_n t/ℏ).
  Do NOT numerically integrate the TDSE.
- Phase sign: exp(−iE_n t/ℏ). NOT exp(+iE_n t/ℏ).
- Sign check: c_1 = c_2 = 1/√2, θ_1 = θ_2 = 0.
  At t = 0: ⟨x⟩ ≈ 0.320 L (left of center, NOT L/2).
  Initial motion: rightward (⟨x⟩ increases from 0.320L toward L/2).
  If ⟨x⟩(0) = L/2, the phase convention is wrong.
- ⟨H⟩ = Σ |c_n|² E_n, exactly constant. Drift > 0.1% is a bug; flag red.
- Orthonormality: use the trig identity, not Gram-Schmidt.
````

### Part B — The simulation prompt

````markdown
SHOW.
Infinite square well: V(x) = 0 for 0 < x < L, V = ∞ elsewhere.
Eigenstates: ψ_n(x) = √(2/L) sin(nπx/L), n = 1, 2, 3, ...
Energies: E_n = n² π² ℏ² / (2mL²).
General time-evolved state:
  Ψ(x, t) = Σ_{n=1}^{n_max} c_n ψ_n(x) exp(−iE_n t/ℏ)
where c_n = |c_n| exp(iθ_n), normalized so Σ |c_n|² = 1.
Energy expectation: ⟨H⟩ = Σ |c_n|² E_n, constant in time.
For the sloshing check:
  ⟨x⟩(t) = L/2 − (16L/9π²) cos((E₂−E₁)t/ℏ)  [for c₁ = c₂ = 1/√2, real]
  At t = 0: ⟨x⟩ ≈ 0.320 L (left of center).

Use the existing CLAUDE.md (with the Chapter 5 stanza) and DESIGN.md.

SAY.
Produce a single file `05-infinite-well.html`.

Layout (four panels, top to bottom):

  1. ENERGY DIAGRAM (200 px tall):
     - Vertical red walls at x = 0 and x = L.
     - Horizontal lines at y = E_n for n = 1..5, labeled in eV.
     - Each ψ_n drawn as a curve offset to its energy level (textbook
       convention). Amplitude scaled to fit between adjacent levels.

  2. PROBABILITY DENSITY ANIMATION (200 px tall):
     - Blue filled |Ψ(x,t)|² curve, animated via requestAnimationFrame.
     - Shared x-axis with panel 1.
     - Thin orange vertical line at ⟨x⟩(t), updated each frame.

  3. SIDE PANEL — NUMERICAL READOUTS AND BAR CHART (300 px wide):
     - ⟨x⟩(t) in nm  [live]
     - ⟨H⟩ in eV     [constant; red if drift > 0.1%]
     - ∫|Ψ|² dx       [must read 1.000]
     - E_1, E_2, E_3 in eV
     - T_slosh = 2πℏ/(E_2−E_1) in fs
     - Bar chart: |c_n|² for n = 1..n_max

  4. CONTROLS (bottom):
     - c_1, c_2, c_3, c_4, c_5: magnitude sliders (0 to 1).
     - θ_1, θ_2, θ_3, θ_4, θ_5: phase sliders (0 to 2π).
     - Normalize Σ|c_n|² = 1 automatically; display renormalized values.
     - L slider (1 to 20 nm).
     - Mass dropdown {electron, proton}.
     - n_max slider (1 to 20).
     - Pause/play, reset, time-speed × 1/5/20.

CONSTRAIN.
- D3 v7 from CDN. SVG only. Vanilla JS.
- N = 200 grid points on x ∈ [0, L].
- Analytic eigenstates; no numerical eigensolver; no Gram-Schmidt.
- Time evolution: analytic. Complex storage: {re, im} float arrays.
- Phase sign: exp(−iE_n t/ℏ). The sign check must pass:
    c₁ = c₂ = 1/√2, θ₁ = θ₂ = 0 → ⟨x⟩(0) ≈ 0.320L, initial rightward motion.
    NOT ⟨x⟩(0) = L/2, NOT initial leftward motion.
    Document this explicitly in a code comment.

VERIFY.
After writing the file, give me five checks:
(a) For L = 1 nm, electron: E₁ = 0.377 eV, E₂ = 1.508 eV, E₃ = 3.39 eV.
    E₂/E₁ = 4.000, E₃/E₁ = 9.000 (to displayed precision).
(b) ψ_n has exactly n−1 internal nodes inside (0, L).
(c) c₁ = 1, others 0: |Ψ(x,t)|² visually frozen, ⟨x⟩ = L/2 constant,
    ⟨H⟩ = E₁. Re Ψ and Im Ψ oscillate visibly.
(d) c₁ = c₂ = 1/√2, θ₁ = θ₂ = 0: ⟨x⟩(0) ≈ 0.320L; initial rightward
    motion; period T ≈ 3.66 fs for L = 1 nm electron.
(e) ⟨H⟩ constant to 4 decimal places throughout the animation.

Known LLM failure modes — confirm guards:
  - Wrong phase sign (exp(+iEt/ℏ)): sloshing direction flips AND ⟨x⟩(0)
    becomes right-heavy instead of left-heavy.
  - ⟨x⟩(0) = L/2 asserted by symmetry (wrong for this superposition).
  - Gram-Schmidt hiding the trigonometric orthogonality.
  - Neumann boundary conditions (ψ' = 0 instead of ψ = 0 at walls).
  - E_n not scaling as n².
  - ⟨H⟩ drift over time.
  - Lost imaginary part (Im Ψ = 0 identically; time evolution broken).
````

### Part C — Exploration tasks

**Verify the $n^2$ spectrum.** Set $L = 1$ nm, electron. Read $E_1$, $E_2$, $E_3$ from the panel. Compute the ratios and confirm $E_n/E_1 = n^2$. Change $L$ to 2 nm and observe that all energies drop by a factor of 4 — the $L^{-2}$ scaling is the fastest way to tune a quantum well's spectrum.

**Watch a single eigenstate.** Set $c_1 = 1$, all others zero. Run the animation. $|\Psi(x,t)|^2$ does not change. The orange line (⟨x⟩) sits at $L/2$ and does not move. $\langle H\rangle$ stays at $E_1$. The wave function itself is rotating in the complex plane — you can see Re $\Psi$ and Im $\Psi$ oscillating — but the observable is frozen. Write one sentence explaining why.

**Slosh.** Set $c_1 = c_2 = 1/\sqrt{2}$, $\theta_1 = \theta_2 = 0$. Run. Confirm that $\langle x\rangle(0) \approx 0.320L$ (the probability starts left-heavy) and that the orange line initially moves right. Read the period from the time display or the oscillation of the orange line; confirm it is approximately 3.66 fs for the 1 nm electron. Note that $\langle H\rangle$ does not move throughout.

**Phase flipping.** With $c_1 = c_2 = 1/\sqrt{2}$, change $\theta_2$ from 0 to $\pi$. Watch the initial shape of $|\Psi|^2$ flip from left-heavy to right-heavy — the sloshing now starts at $\langle x\rangle(0) \approx 0.680L$ and moves left. Explain: at $t = 0$, the state is proportional to $\psi_1 + e^{i\pi}\psi_2 = \psi_1 - \psi_2$, which is concentrated in the right half of the well (since $\psi_2 < 0$ in the right half).

**Node counting.** Set $c_n = 1$ for $n = 3$, all others zero. Count the internal zeros of $|\Psi|^2$ (which equals $|\psi_3|^2$). Confirm you see exactly 2 interior nodes. Try $n = 5$: confirm 4 nodes. Then try a superposition $c_1 = c_4 = 1/\sqrt{2}$: the interference term means $|\Psi|^2$ no longer has a fixed node count — it sloshes. Record whether any persistent zeros appear.

**Draw your own $\psi$ (extension).** Use the "draw your own" canvas (if the extension is implemented). Draw a narrow bump centered at $x = L/4$. Watch the bar chart: many $c_n$ will be nonzero, because a bump at $L/4$ is not an eigenstate — it is a superposition of many. Increase $n_\mathrm{max}$ from 5 to 20 and watch the reconstruction improve. Then hit "play" and watch the bump disperse: more frequencies present means more beat frequencies, means faster dephasing of the spatial structure.

### Part D — Extension prompt

````markdown
Add a "Draw your own ψ(x, 0)" panel (fifth panel, below the controls).

Behavior:
  - 600 × 150 SVG canvas; user clicks and drags to sketch a real-valued
    ψ(x, 0). The curve is sampled at N = 200 grid points.
  - The curve is normalized: ∫|ψ|² dx = 1.
  - Compute c_n = ∫₀ᴸ ψ_n(x) ψ(x,0) dx by Simpson's rule,
    for n = 1 to n_max.
  - Update the bar chart and animate |Ψ(x,t)|².
  - Overlay a faint gray reconstruction Σ c_n ψ_n at t = 0,
    so the student sees how well the truncated basis captures the drawing.
  - n_max slider (1..30) controls truncation.

Verify by drawing a Gaussian centered at L/4:
  - At n_max = 5: reconstruction is visibly broader than the drawing.
  - At n_max = 20: visually indistinguishable from the drawing.
  - At n_max = 30: ⟨H⟩ should be noticeably larger than E₁ alone,
    because the narrow bump requires high-energy components.

Do not regress the four existing panels.
````

When you draw a narrow bump and watch it disperse — the coherent spatial structure dephasing into a broad, featureless distribution — you have seen the inverse of localization: many energy components, many beat frequencies, fast washout. A particle "found" at a single position is a superposition of many energies, and those energies cannot stay in phase for long.

---

## References

- Schrödinger, E. (1926). Quantisierung als Eigenwertproblem. *Annalen der Physik*, 79, 361–376. [verify] (First derivation of the TISE and the energy levels of the hydrogen atom by wave mechanics.)
- Bohr, N. (1913). On the constitution of atoms and molecules. *Philosophical Magazine*, 26, 1–25. (The original quantization postulate, against which Schrödinger's derivation should be compared.)
- Griffiths, D. J., & Schroeter, D. F. (2018). *Introduction to Quantum Mechanics* (3rd ed.). Cambridge University Press. §2.2.
- Esaki, L., & Tsu, R. (1970). Superlattice and negative differential conductivity in semiconductors. *IBM Journal of Research and Development*, 14(1), 61–65. (Proposed the semiconductor superlattice and argued that quantum-well energy levels would be tunable by controlling $L$.)
- Dingle, R., Wiegmann, W., & Henry, C. H. (1974). Quantum states of confined carriers in very thin $\mathrm{Al}_x\mathrm{Ga}_{1-x}\mathrm{As}$–$\mathrm{GaAs}$–$\mathrm{Al}_x\mathrm{Ga}_{1-x}\mathrm{As}$ heterostructures. *Physical Review Letters*, 33(14), 827–830. (First spectroscopic confirmation of discrete quantum-well energy levels in a semiconductor heterostructure.)
- Crommie, M. F., Lutz, C. P., & Eigler, D. M. (1993). Confinement of electrons to quantum corrals on a metal surface. *Science*, 262(5131), 218–220. (The quantum corral: standing-wave patterns in electron density in a nanoscale ring, the STM image that opens this chapter.)
- Stein, E. M., & Shakarchi, R. (2003). *Fourier Analysis: An Introduction*. Princeton University Press. Ch. 2 and Ch. 4. (Orthogonality and completeness of the trigonometric basis; the Fourier sine series on a bounded interval.)
- Fourier, J. B. J. (1822). *Théorie analytique de la chaleur*. Firmin Didot. [verify] (The original work establishing the Fourier sine series for heat conduction — predating quantum mechanics by more than a century.)
- Jaksch, D., Bruder, C., Cirac, J. I., Gardiner, C. W., & Zoller, P. (1998). Cold bosonic atoms in optical lattices. *Physical Review Letters*, 81(15), 3108–3111. (Theoretical treatment of cold atoms in optical lattices as nearly ideal quantum wells.)
- Greiner, M., Mandel, O., Esslinger, T., Hänsch, T. W., & Bloch, I. (2002). Quantum phase transition from a superfluid to a Mott insulator in a gas of ultracold atoms. *Nature*, 415, 39–44. (Experimental realization of atoms in optical lattice potential wells.)
