# Chapter 5 — The Infinite Square Well
*How boundary conditions became the engine of quantization.*

In 1993, physicists at IBM's Almaden Research Center spent several days nudging individual iron atoms across a copper surface with the tip of a scanning tunneling microscope. One at a time, they arranged 48 atoms into a ring — a structure they called a quantum corral — and then imaged the electron density trapped inside. What they saw was not a smooth puddle of charge. It was a bull's-eye of concentric rings, a standing-wave pattern in the probability density, exactly what the Schrödinger equation predicts for an electron confined to a circular domain.

Crommie, Lutz, and Eigler did not put the rings in. The walls imposed them. Confine an electron, and it can only inhabit modes that fit the container. The modes look like standing waves because they are standing waves. The allowed energies are discrete because only certain spatial frequencies satisfy the geometry at the boundaries. The quantization was not assumed, postulated, or inserted by hand. It fell out of the mathematics of confinement.

This chapter works through the one-dimensional version of the same argument — the infinite square well — where the geometry is simple enough to carry the derivation completely, in closed form, from the Schrödinger equation to the energy spectrum to the dynamics of superpositions. The goal is not to memorize formulas. It is to see, step by step, exactly where the discreteness comes from.

<!-- → [IMAGE: the Crommie–Lutz–Eigler STM image of the quantum corral (1993) — 48 iron atoms arranged in a ring on copper, with the standing-wave rings of electron density visible inside; caption should note this is a direct image of quantum confinement, not a schematic] -->

---

## The Guitar String Analogy, and Why It Breaks Down

A guitar string fixed at both ends vibrates at a fundamental frequency and its integer harmonics. The reason is purely geometrical: a mode survives only if it vanishes at both fixed endpoints. A half-wavelength fits. A full wavelength fits. Three half-wavelengths fit. But one-and-a-third half-wavelengths cannot simultaneously vanish at both walls — it contradicts itself at the boundary and collapses. The surviving frequencies are those that fit, and the fitting condition is discrete.

The analogy with a quantum particle in a box goes this deep and then stops. For the guitar string, the modes are literal physical displacements of a medium. For the electron, the "wave" is the wave function $\psi(x)$ — a complex-valued function whose squared modulus gives the probability of finding the particle at position $x$. No medium is vibrating. The wave is not a wave in space; it is a wave of probability amplitude in the space of possible positions. The boundary conditions are the same mathematical structure, but the physical meaning of what is waving is entirely different.

With that distinction noted, the calculation proceeds exactly like the guitar string argument, dressed in quantum language.

---

## The Setup

The infinite square well potential is

$$V(x) = \begin{cases} 0 & 0 < x < L, \\ \infty & x \leq 0 \text{ or } x \geq L. \end{cases}$$

Where the potential is infinite, the wave function must vanish. This is not an additional assumption; it is what $V = \infty$ forces in the time-independent Schrödinger equation (TISE). If $\psi \neq 0$ where $V = \infty$, the equation $-(\hbar^2/2m)\psi'' + V\psi = E\psi$ cannot be satisfied: the left side would be infinite while the right side is finite. So the wave function is zero outside the well, and by the requirement that $\psi$ be continuous:

$$\psi(0) = 0, \qquad \psi(L) = 0.$$

These are the boundary conditions. They are the walls, expressed in the language of the wave function.

Inside the well, $V = 0$, and the TISE is simply

$$-\frac{\hbar^2}{2m}\frac{d^2\psi}{dx^2} = E\psi.$$

Now ask: what values of $E$ are allowed?

<!-- → [FIGURE: diagram of the infinite square well potential — V = ∞ for x ≤ 0 and x ≥ L shown as vertical walls, V = 0 between; the first three eigenstates drawn as sine curves offset to their respective energy levels; the n² energy spacing should be visible by eye] -->

---

## The Derivation in Eight Steps

**Can $E$ be negative?** If $E < 0$, write $\kappa^2 = -2mE/\hbar^2 > 0$. The equation becomes $\psi'' = \kappa^2\psi$, with general solution $\psi = Ae^{\kappa x} + Be^{-\kappa x}$ — a sum of real exponentials. This cannot vanish at both $x = 0$ and $x = L$ unless $A = B = 0$, which means no particle. If $E = 0$, the equation is $\psi'' = 0$, so $\psi = ax + b$; the boundary conditions force both constants to zero. So $E < 0$ and $E = 0$ are excluded. Only $E > 0$ gives a non-trivial solution.

**The general solution for $E > 0$.** Define $k = \sqrt{2mE}/\hbar > 0$. The TISE reads $\psi'' = -k^2\psi$ — the equation of a spatial oscillator — with general solution

$$\psi(x) = A\sin(kx) + B\cos(kx).$$

At this point, any positive $k$ is allowed. No quantization yet.

**Apply the boundary condition at $x = 0$.** Substituting: $\psi(0) = A\sin(0) + B\cos(0) = B = 0$. The cosine term is killed. The solution reduces to $\psi(x) = A\sin(kx)$. Still no quantization.

**Apply the boundary condition at $x = L$.** Now: $\psi(L) = A\sin(kL) = 0$. Either $A = 0$ — no particle, discarded — or

$$\sin(kL) = 0.$$

This single equation is where quantization enters. A sine vanishes only at integer multiples of $\pi$. So $kL = n\pi$ for $n = 1, 2, 3, \ldots$ The continuous set of all positive real $k$ has collapsed to a discrete ladder indexed by a positive integer.

This is not a postulate. It is not an assumption about angular momentum or a new law inserted to fix a problem. It is the only way a sine wave can vanish at both walls simultaneously. Bohr postulated quantization in 1913; Schrödinger derived it in 1926 from a differential equation and two boundary conditions.

**The wave vectors and energy levels.** The allowed wave vectors are $k_n = n\pi/L$. Since $E = \hbar^2 k^2/2m$:

$$\boxed{E_n = \frac{n^2\pi^2\hbar^2}{2mL^2}, \qquad n = 1, 2, 3, \ldots}$$

The energies scale as $n^2$. The first few ratios: $E_1 : E_2 : E_3 : E_4 = 1 : 4 : 9 : 16$. Nothing lives between these values. For $n = 0$: $k_0 = 0$ gives $\psi = A\sin(0) = 0$ — no particle, excluded. For negative $n$: $\sin(-n\pi x/L) = -\sin(n\pi x/L)$, which produces the same probability density as positive $n$ — it is the same physical state up to an unobservable sign.

**Normalization.** The unnormalized eigenstate is $A\sin(n\pi x/L)$. Requiring $\int_0^L|\psi_n|^2\,dx = 1$ and using $\int_0^L\sin^2(n\pi x/L)\,dx = L/2$ (from the identity $\sin^2\theta = (1-\cos2\theta)/2$, integrated over a whole number of half-periods):

$$A^2 \cdot \frac{L}{2} = 1 \implies A = \sqrt{\frac{2}{L}}.$$

The normalized eigenstates are

$$\boxed{\psi_n(x) = \sqrt{\frac{2}{L}}\,\sin\!\left(\frac{n\pi x}{L}\right), \quad 0 \leq x \leq L; \qquad \psi_n(x) = 0 \text{ elsewhere.}}$$

---

## What the Spectrum Looks Like Physically

For an electron in a well of width $L = 1$ nm, the ground-state energy is

$$E_1 = \frac{\pi^2(1.055\times10^{-34})^2}{2(9.109\times10^{-31})(10^{-9})^2} \approx 6.0\times10^{-20}\ \text{J} \approx 0.377\ \text{eV.}$$

So $E_2 \approx 1.51$ eV, $E_3 \approx 3.39$ eV. These are energies on the scale of chemistry and optics — visible photons carry roughly 2 eV, and room-temperature thermal energy is $k_BT \approx 0.025$ eV. The level spacings are large compared to thermal fluctuations, so quantum effects are not merely relevant — they dominate.

For contrast, compute the ground-state energy of a 1 g marble in a 1 cm box:

$$E_1 \approx \frac{\pi^2(10^{-34})^2}{2(10^{-3})(10^{-2})^2} \approx 5\times10^{-62}\ \text{J} \approx 3\times10^{-43}\ \text{eV.}$$

This is twenty orders of magnitude below anything measurable. The quantum discreteness is present in principle and invisible in practice. The classical limit is not a philosophical choice; it is a calculation.

<!-- → [TABLE: E_n for n = 1 to 5 for three systems — electron in 1 nm well, electron in 10 nm well, proton in 1 nm well; columns: n, E_n (eV), E_n/E_1; shows how the spectrum scales with L² and m, and makes the classical limit for the proton visible] -->

The eigenstate $\psi_n$ has exactly $n - 1$ interior nodes — zeros strictly inside $(0, L)$, not counting the walls. $\psi_1$: one half-period, no interior zeros. $\psi_2$: two half-periods, one interior zero at $x = L/2$. $\psi_n$: $n$ half-periods, $n - 1$ zeros. More nodes means shorter wavelength, higher spatial frequency, higher momentum ($p = \hbar k_n = n\pi\hbar/L$), higher energy. Node counting is Fourier logic made visual.

---

## Orthonormality — a Three-Line Proof

The eigenstates satisfy $\langle\psi_m|\psi_n\rangle = \delta_{mn}$ — they are orthonormal. The proof requires only one trigonometric identity:

$$\sin\alpha\sin\beta = \frac{1}{2}\bigl[\cos(\alpha-\beta) - \cos(\alpha+\beta)\bigr].$$

Apply it to $\langle\psi_m|\psi_n\rangle = (2/L)\int_0^L\sin(m\pi x/L)\sin(n\pi x/L)\,dx$:

$$\langle\psi_m|\psi_n\rangle = \frac{1}{L}\int_0^L\!\left[\cos\!\left(\frac{(m-n)\pi x}{L}\right) - \cos\!\left(\frac{(m+n)\pi x}{L}\right)\right]dx.$$

For $m \neq n$: both integrands are cosines over an integer number of full periods on $[0, L]$; both integrals vanish. $\langle\psi_m|\psi_n\rangle = 0$. For $m = n$: the first cosine becomes $\cos(0) = 1$, integrating to $L$; the second is a cosine over $n$ full periods, integrating to zero. So $\langle\psi_n|\psi_n\rangle = 1$.

No numerical eigensolver. No Gram-Schmidt. This is exact, analytic, and follows directly from classical Fourier analysis. Fourier established it in 1822 for the heat equation — more than a century before quantum mechanics existed. The mathematics of standing waves on a bounded interval was already fully worked out; what quantum mechanics added was the physical interpretation.

---

## Why the Ground State Cannot Be Still

The lowest energy is $E_1 = \pi^2\hbar^2/2mL^2 > 0$. The particle cannot have $E = 0$.

The Heisenberg uncertainty principle explains why. If $E = 0$, then the kinetic energy is zero, the momentum is zero, and therefore the momentum uncertainty $\sigma_p = 0$. But the particle is confined to a box of width $L$, so its position uncertainty satisfies $\sigma_x \leq L$. The Kennard inequality $\sigma_x\sigma_p \geq \hbar/2$ then gives $L \cdot 0 \geq \hbar/2$, which is false. A particle with zero momentum uncertainty cannot also be confined in space. The uncertainty principle forbids $E = 0$.

This is not a peculiarity of quantum mechanics — it is a consequence of the wave nature of matter. A guitar string stretched flat has zero energy and zero frequency. The minimum non-trivial mode has positive frequency, positive energy. The same logic applies to any wave confined in a finite domain.

Quantitatively: for the ground state, $\sigma_p = \pi\hbar/L$ (computed from $\langle p^2\rangle = \pi^2\hbar^2/L^2$ with $\langle p\rangle = 0$ by symmetry), and $\sigma_x \approx 0.181L$. So $\sigma_x\sigma_p \approx 0.568\hbar \approx 1.136 \times (\hbar/2)$ — about 14% above the minimum allowed by the uncertainty principle. The ground state of the infinite well is close to the most tightly localized state quantum mechanics permits.

<!-- → [FIGURE: ground-state and first-excited-state wave functions ψ₁ and ψ₂, and their probability densities |ψ₁|² and |ψ₂|², all four curves on the same x-axis from 0 to L; labels should indicate node count and the zero-point energy E₁ > 0; useful for making the zero-node / one-node distinction visually clear] -->

---

## Time Evolution and the Sloshing State

The eigenstates $\psi_n$ are stationary states — their probability densities $|\psi_n|^2$ do not change in time. The full time-dependent wave function for an eigenstate is $\Psi_n(x,t) = \psi_n(x)e^{-iE_n t/\hbar}$; the time-dependent factor is a pure phase rotation, which cancels when you compute $|\Psi_n|^2 = |\psi_n|^2$.

Dynamics only appear when you superpose two or more eigenstates with different energies. Take the equal-weight combination of the first two:

$$\Psi(x,t) = \frac{1}{\sqrt{2}}\,\psi_1(x)\,e^{-iE_1 t/\hbar} + \frac{1}{\sqrt{2}}\,\psi_2(x)\,e^{-iE_2 t/\hbar}.$$

The probability density is

$$|\Psi(x,t)|^2 = \frac{1}{2}\!\left[\psi_1^2 + \psi_2^2 + 2\,\psi_1\psi_2\cos\!\left(\frac{(E_2-E_1)t}{\hbar}\right)\right].$$

The first two terms are static; the cross term oscillates at angular frequency $\omega = (E_2 - E_1)/\hbar = 3E_1/\hbar$. The period is

$$T = \frac{2\pi\hbar}{E_2 - E_1} = \frac{h}{3E_1}.$$

For the 1 nm electron, $E_1 \approx 6.0\times10^{-20}$ J, giving $T \approx 3.66$ femtoseconds. The probability distribution oscillates from one side of the well to the other on a timescale measured in femtoseconds.

**Where is the particle, on average?** Compute $\langle x\rangle(t) = \int_0^L x|\Psi(x,t)|^2\,dx$. Since both $\psi_1$ and $\psi_2$ are symmetric about $L/2$, their individual contributions give $\langle x\rangle_{1} = \langle x\rangle_{2} = L/2$. Only the cross term contributes a time-varying piece:

$$\langle x\rangle(t) = \frac{L}{2} + \cos\!\left(\frac{(E_2-E_1)t}{\hbar}\right)\int_0^L x\,\psi_1(x)\,\psi_2(x)\,dx.$$

The cross integral requires integration by parts. Using the product-to-sum identity to expand $\psi_1\psi_2$ and then integrating $\int_0^L x\cos(n\pi x/L)\,dx$ by parts, the result is

$$\int_0^L x\,\psi_1\psi_2\,dx = -\frac{16L}{9\pi^2} \approx -0.180\,L.$$

So

$$\langle x\rangle(t) = \frac{L}{2} - \frac{16L}{9\pi^2}\cos\!\left(\frac{(E_2-E_1)t}{\hbar}\right).$$

At $t = 0$, $\cos(0) = 1$, giving $\langle x\rangle(0) \approx L/2 - 0.180L \approx 0.320L$. The initial state is left-heavy: the probability distribution peaks near $x = L/4$, because $\psi_1 + \psi_2$ — a half-sine plus a full-sine — has its constructive peak in the left half of the well. Since $d\langle x\rangle/dt|_{t=0} = 0$ (the cosine is at a turning point), the center of mass starts at rest and then moves rightward, reaching $\langle x\rangle \approx 0.680L$ at half-period before returning. The total swing is about $0.360L$.

Throughout all of this, the energy expectation value is

$$\langle\hat{H}\rangle = \frac{1}{2}E_1 + \frac{1}{2}E_2 \approx \frac{0.377 + 1.508}{2} \approx 0.943\ \text{eV.}$$

Constant. The probability is sloshing; the energy is not. The $|c_n|^2$ — the weights on each eigenstate — are fixed by the initial state and do not change in time. What evolves is the relative phase between the terms, which modulates the interference pattern in $|\Psi|^2$ but leaves the energy budget unchanged.

<!-- → [CHART: three-panel animation schematic — (1) |Ψ(x,t)|² at t = 0, t = T/4, t = T/2, t = 3T/4, showing the probability density sloshing left to right; (2) ⟨x⟩(t) as a function of time, oscillating between 0.320L and 0.680L; (3) ⟨H⟩(t) as a flat line — visually emphasizing that energy is constant while position expectation oscillates] -->

---

## The Fourier Structure Underneath

The eigenstates $\{\psi_n\}$ form a complete orthonormal basis for square-integrable functions on $[0, L]$ that vanish at the endpoints. Any such function can be expanded:

$$f(x) = \sum_{n=1}^{\infty} c_n\,\psi_n(x), \qquad c_n = \int_0^L\psi_n(x)\,f(x)\,dx.$$

This is the Fourier sine series. The coefficients $c_n$ are projections — inner products of the initial state onto each eigenstate. Given any initial condition $\Psi(x, 0)$, find the $c_n$ by integration, then attach the time-evolution phases:

$$\Psi(x,t) = \sum_{n=1}^{\infty} c_n\,\psi_n(x)\,e^{-iE_n t/\hbar}.$$

Each eigenstate rotates at its own angular frequency $E_n/\hbar$. When two or more eigenstates are present with different energies, the relative phases between them evolve, and the result is interference that changes $|\Psi|^2$ over time — the sloshing.

The probability of measuring energy $E_n$ is $|c_n|^2$. Note what this means: the $|c_n|^2$ are set by the initial state, they do not change in time, and they are the only observable consequences of the $c_n$ as far as energy measurements are concerned. The phases matter only for position and momentum measurements, where the cross terms in $|\Psi|^2$ — the interference terms — carry information about relative phase.

A narrow initial state, concentrated near one point, requires many $c_n$ to be nonzero — because representing a sharp feature as a sum of sine waves requires many harmonics. Many harmonics means many distinct frequencies, many beat frequencies between pairs of eigenstates, and therefore rapid dephasing of the initial spatial structure. A particle initially localized near $x = L/4$ will not stay near $x = L/4$; it will spread, slosh, and eventually become nearly uniform. The classical limit corresponds to packets so heavy and slow that the dephasing timescale is astronomically long — effectively infinite.

---

## What Comes Next

The infinite square well gives clean answers because its walls are perfectly rigid. No wave function leaks through $V = \infty$; no energy can tunnel out. Real quantum systems — semiconductor quantum wells, quantum dots, atoms in optical lattice traps — have finite barriers, and wave functions do penetrate them. The discrete energy levels of a finite-depth well are qualitatively similar to those of the infinite well but shifted downward, and they are finite in number: a well of depth $V_0$ and width $L$ supports only finitely many bound states. As $V_0 \to \infty$, those levels approach the infinite-well values from below.

The question the infinite well leaves open — why is the probability interpretation correct, and what does it mean for the wave function to "collapse" upon measurement — is not answered by solving the TISE. That is the measurement problem, and it sits at the foundation of quantum mechanics in a way that the Schrödinger equation does not resolve. Chapter 3 laid out Born's rule as a postulate; it remains a postulate. What the infinite well does show is that Born's rule, combined with the Schrödinger equation, makes predictions that are experimentally exact. The Davisson–Germer diffraction, the quantum corral, the energy levels of semiconductor quantum wells measured spectroscopically by Dingle and colleagues in 1974 — all confirm that the quantization derived here is not a mathematical artifact. The walls impose it, and nature obeys.

---

## Exercises

**Warm-up**

1. *Difficulty: Warm-up — tests command of the eight-step derivation.*
   Starting from the TISE with $V = 0$ inside $[0, L]$: (a) Write the general solution $\psi(x) = A\sin(kx) + B\cos(kx)$. (b) Apply $\psi(0) = 0$ to determine $B$. (c) Apply $\psi(L) = 0$ and explain why $\sin(kL) = 0$ leads to a discrete spectrum while the case $A = 0$ is discarded. (d) Write $k_n$, $E_n$, and the normalized $\psi_n(x)$. At which step does quantization first appear?
   *Tests: ability to trace the origin of discreteness to the boundary conditions, not to a postulate.*

2. *Difficulty: Warm-up — tests the $n^2$ energy scaling.*
   For an electron in a well of width $L = 2$ nm: (a) Compute $E_1$, $E_2$, $E_3$ in eV. (b) Verify $E_2/E_1 = 4$ and $E_3/E_1 = 9$ to three significant figures. (c) Compare these to $k_BT = 0.025$ eV at room temperature — are quantum effects significant? (d) If $L$ is doubled to 4 nm, by what factor does $E_1$ change?
   *Tests: numerical command of the spectrum and the $L^{-2}$ scaling.*

3. *Difficulty: Warm-up — tests the trigonometric orthonormality proof.*
   Verify $\langle\psi_1|\psi_2\rangle = 0$ directly, using the identity $\sin\alpha\sin\beta = \frac{1}{2}[\cos(\alpha-\beta)-\cos(\alpha+\beta)]$. Show all steps. Then verify $\langle\psi_1|\psi_1\rangle = 1$ by the same method.
   *Tests: whether the student can carry out the exact analytic proof without numerical methods.*

**Application**

4. *Difficulty: Application — connects zero-point energy to the uncertainty principle.*
   (a) Argue from the Kennard inequality that a particle confined to $[0, L]$ cannot have $E = 0$. What does $E = 0$ imply for $\sigma_p$, and why does that contradict $\sigma_x \leq L$? (b) Compute $\sigma_p$ for the ground state by evaluating $\langle p\rangle = 0$ and $\langle p^2\rangle = \int_0^L\psi_1(-\hbar^2\partial_x^2)\psi_1\,dx$. (c) Use the result $\langle x^2\rangle = L^2(1/3 - 1/2\pi^2)$ to compute $\sigma_x$ for the ground state. Verify $\sigma_x\sigma_p \geq \hbar/2$ and find the ratio.
   *Tests: ability to turn the zero-point energy argument into a quantitative check.*

5. *Difficulty: Application — extends superposition dynamics to a different pair of states.*
   A particle is prepared in $\Psi(x,0) = \frac{1}{\sqrt{2}}(\psi_1 + \psi_3)$. (a) Write $\Psi(x,t)$. (b) Compute $|\Psi(x,t)|^2$ and identify the oscillation frequency of the cross term. (c) Compute $\langle\hat{H}\rangle$. (d) Is $\langle x\rangle = L/2$ for all $t$? Argue from the parity of $\psi_1$ and $\psi_3$ about $x = L/2$.
   *Tests: whether the student can generalize the sloshing argument to a different superposition.*

6. *Difficulty: Application — tests expansion coefficients and the projection integral.*
   An initial state is given as $\Psi(x,0) = Bx(L-x)$ for $0 \leq x \leq L$, normalized so $\int_0^L|\Psi|^2\,dx = 1$. (a) Find $B$. (b) Show that $c_n = 0$ for all even $n$ using the symmetry of $\Psi(x,0)$ about $x = L/2$ and the parity of $\psi_n$. (c) Compute $c_1 = \int_0^L\psi_1(x)\,Bx(L-x)\,dx$ by direct integration. Check that $|c_1|^2 \approx 0.999$.
   *Tests: command of the Fourier expansion and recognition of symmetry as a labor-saving tool.*

**Synthesis**

7. *Difficulty: Synthesis — requires carrying out the full sloshing calculation.*
   For $\Psi(x,t) = \frac{1}{\sqrt{2}}(\psi_1 e^{-iE_1 t/\hbar} + \psi_2 e^{-iE_2 t/\hbar})$: (a) Derive $\langle x\rangle(t) = L/2 - (16L/9\pi^2)\cos((E_2-E_1)t/\hbar)$ by computing the cross integral $\int_0^L x\psi_1\psi_2\,dx$ via integration by parts, showing all steps. (b) State the maximum and minimum values of $\langle x\rangle(t)$. (c) Confirm that $d\langle x\rangle/dt|_{t=0} = 0$ and give the physical interpretation. (d) What is the initial direction of the sloshing just after $t = 0$?
   *Tests: full quantitative command of the two-state dynamics; the student must produce the integration, not recall the result.*

8. *Difficulty: Synthesis — connects the spectrum to a photon emission calculation.*
   An electron in a 1 nm well emits a photon and drops from $n = 3$ to $n = 1$. (a) Compute the photon energy $E_3 - E_1$ in eV. (b) Compute the photon wavelength. Is it visible, UV, or IR? (c) A GaAs quantum-well laser uses an effective electron mass $m^* \approx 0.067\,m_e$. What well width produces emission at $\lambda = 650$ nm (red light)?
   *Tests: ability to run the formula backward to design a system with a target emission wavelength.*

**Challenge**

9. *Difficulty: Challenge — requires relativistic correction and instrument-design reasoning.*
   A modern 200 kV transmission electron microscope accelerates electrons through $V = 2.0\times10^5$ V. (a) Compute the de Broglie wavelength using the non-relativistic formula $\lambda = h/\sqrt{2m_eK}$. (b) The relativistic momentum is $p = \sqrt{(K/c)^2 + 2m_eK}$; compute the relativistic $\lambda$. (c) By what percentage does the relativistic correction change $\lambda$? (d) If the non-relativistic wavelength were used to set the microscope's resolution specification, how would the specification be in error, and in which direction?
   *Tests: relativistic extension of the de Broglie relation and its practical consequence for instrument design.*

---

## LLM Exercises

The following exercises are designed to be worked with a large language model as a thinking partner — not to get the answer, but to check reasoning, expose failure modes, and push at the edges of what the chapter established.

1. Ask an LLM to derive the quantized energy levels of the infinite square well from scratch, starting only from the TISE and the boundary conditions. Read the derivation carefully. At which step does it introduce quantization? Is it a postulate or a consequence? Compare its route to the eight steps above.

2. The chapter claims that the cross integral $\int_0^L x\,\psi_1(x)\psi_2(x)\,dx = -16L/(9\pi^2)$. Ask an LLM to verify this by carrying out the integration by parts in detail. Check every step. If it gets a different sign or coefficient, locate the error.

3. Ask an LLM: "If I prepare an electron in the ground state of a 1 nm infinite square well, and then suddenly double the well width to 2 nm, what happens?" It should compute the overlap integrals $c_n = \langle\psi_n^{(2\text{nm})}|\psi_1^{(1\text{nm})}\rangle$ and identify which eigenstates of the new well have nonzero weight. Ask it to explain why $c_n = 0$ for even $n$ by symmetry. Evaluate whether its symmetry argument is correct.

4. Ask an LLM to explain the Gibbs phenomenon — the ringing artifact that appears when a truncated Fourier series tries to represent a function with a discontinuity — and why it appears in the "draw your own $\psi$" simulation when $n_\text{max}$ is small. Ask whether the Gibbs ringing constitutes a physical prediction or a mathematical artifact, and whether it would matter for a probability distribution.

5. The chapter's sloshing calculation says that for $c_1 = c_2 = 1/\sqrt{2}$ with both coefficients real and positive, the initial state is left-heavy and $\langle x\rangle$ first moves rightward. Ask an LLM to verify this, and then ask it what happens if you change $c_2$ to $-1/\sqrt{2}$ (i.e., flip the sign of the second coefficient). Does the initial direction of sloshing change? Does the energy expectation value change? Use its answer to probe whether it understands the difference between the phase of a coefficient and its magnitude.

---

## References

Schrödinger, E. (1926). Quantisierung als Eigenwertproblem. *Annalen der Physik*, 79, 361–376. (First derivation of quantized energy levels from the wave equation and boundary conditions.)

Bohr, N. (1913). On the constitution of atoms and molecules. *Philosophical Magazine*, 26, 1–25. (The original quantization postulate; the contrast with Schrödinger's derivation is the conceptual hinge of this chapter.)

Griffiths, D. J., & Schroeter, D. F. (2018). *Introduction to Quantum Mechanics* (3rd ed.). Cambridge University Press. §2.2.

Crommie, M. F., Lutz, C. P., & Eigler, D. M. (1993). Confinement of electrons to quantum corrals on a metal surface. *Science*, 262(5131), 218–220. (The quantum corral; the opening image of this chapter.)

Dingle, R., Wiegmann, W., & Henry, C. H. (1974). Quantum states of confined carriers in very thin AlGaAs–GaAs heterostructures. *Physical Review Letters*, 33(14), 827–830. (First spectroscopic confirmation of discrete energy levels in a semiconductor quantum well.)

Esaki, L., & Tsu, R. (1970). Superlattice and negative differential conductivity in semiconductors. *IBM Journal of Research and Development*, 14(1), 61–65. (Proposed that quantum-well energy levels would be tunable by controlling $L$.)

Fourier, J. B. J. (1822). *Théorie analytique de la chaleur*. Firmin Didot. (The Fourier sine series, established for heat conduction more than a century before quantum mechanics.)

Stein, E. M., & Shakarchi, R. (2003). *Fourier Analysis: An Introduction*. Princeton University Press. Ch. 2–4. (Orthogonality, completeness, and convergence of the trigonometric basis.)
