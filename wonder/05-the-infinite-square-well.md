# Chapter 5 — The Infinite Square Well
*How boundary conditions became the engine of quantization.*

In 1993, physicists at IBM's Almaden Research Center spent several days doing something that sounds more like watchmaking than physics: nudging individual iron atoms, one at a time, across a copper surface with the tip of a scanning tunneling microscope. They corralled 48 of them into a ring — a little structure they named a quantum corral — and then they imaged the electron density trapped inside the fence. And what they saw was not the smooth puddle of charge you might expect. It was a bull's-eye: concentric rings, a standing-wave pattern frozen into the probability density, exactly what the Schrödinger equation predicts for an electron penned into a circular region.

Here is the part to sit with. Crommie, Lutz, and Eigler did not *put* the rings there. The walls imposed them. Confine an electron and it can only occupy the modes that fit inside the container — and those modes look like standing waves because they *are* standing waves. The allowed energies come out discrete because only certain spatial frequencies can satisfy the geometry at the boundary. Nobody assumed the quantization, nobody postulated it, nobody inserted it by hand. It dropped out of the mathematics of being confined. You build the fence; nature does the quantizing.

This chapter works through the one-dimensional version of that same argument — the infinite square well — where the geometry is stripped down enough to carry the whole derivation in closed form, every step, from the Schrödinger equation to the energy spectrum to the dynamics of superpositions. The point is not to memorize the formulas at the end. The point is to *watch* — slowly, one move at a time — exactly where the discreteness comes from.

<!-- → [IMAGE: the Crommie–Lutz–Eigler STM image of the quantum corral (1993) — 48 iron atoms arranged in a ring on copper, with the standing-wave rings of electron density visible inside; caption should note this is a direct image of quantum confinement, not a schematic] -->

![the Crommie–Lutz–Eigler STM image of the quantum corral (1993) — 48 iron atoms arranged in a ring on copper, with the standing-wave rings…](../images/05-the-infinite-square-well-fig-01.png)
*Figure 5.1 — the Crommie–Lutz–Eigler STM image of the quantum corral (1993) — 48 iron atoms arranged in a ring on copper, with the standing-wave rings…*

---

## The Guitar String Analogy, and Why It Breaks Down

You already know this physics in your hands, even if you have never written it down. A guitar string fixed at both ends sounds a fundamental note and its integer harmonics. The reason is purely geometrical: a mode lives only if it vanishes at both pinned endpoints. A half-wavelength fits. A full wavelength fits. Three half-wavelengths fit. But one-and-a-third half-wavelengths *cannot* vanish at both walls at once — it contradicts itself at the boundary and collapses. So the surviving frequencies are exactly the ones that fit, and the fitting condition is discrete. That is your whole intuition for quantization, and you got it for free from a guitar.

The analogy with a quantum particle in a box runs deep, and then it stops cold, and you have to know where. For the guitar string, the modes are literal physical displacements of a real medium — the string is actually moving in space. For the electron, the "wave" is the wave function $\psi(x)$, a complex-valued function whose squared modulus gives the probability of finding the particle at $x$. *Nothing is vibrating.* There is no medium. The wave is not a wave in space at all; it is a wave of probability amplitude over the space of possible positions. The boundary conditions are the same mathematical structure — that part of the analogy is exact — but what is doing the waving could not be more different.

With that distinction firmly in hand, the calculation marches along exactly like the guitar-string argument, only dressed in quantum clothing.

---

## The Setup

The infinite square well potential is

$$V(x) = \begin{cases} 0 & 0 < x < L, \\ \infty & x \leq 0 \text{ or } x \geq L. \end{cases}$$

Where the potential is infinite, the wave function has to vanish. And this is not an extra assumption we are sneaking in — it is what $V = \infty$ *forces* in the time-independent Schrödinger equation. Suppose $\psi \neq 0$ somewhere that $V = \infty$. Then in the equation $-(\hbar^2/2m)\psi'' + V\psi = E\psi$, the term $V\psi$ blows up to infinity while the right side $E\psi$ stays finite. Infinity cannot equal a finite number. So $\psi$ must be zero outside the well, and since $\psi$ has to be continuous, it must also vanish right at the edges:

$$\psi(0) = 0, \qquad \psi(L) = 0.$$

These are the boundary conditions. They are the walls, rewritten in the language of the wave function.

Inside the well, $V = 0$, and the TISE reduces to the bare bones:

$$-\frac{\hbar^2}{2m}\frac{d^2\psi}{dx^2} = E\psi.$$

Now we ask the only question that matters: which values of $E$ are allowed?

<!-- → [FIGURE: diagram of the infinite square well potential — V = ∞ for x ≤ 0 and x ≥ L shown as vertical walls, V = 0 between; the first three eigenstates drawn as sine curves offset to their respective energy levels; the n² energy spacing should be visible by eye] -->

![diagram of the infinite square well potential — V = ∞ for x ≤ 0 and x ≥ L shown as vertical walls, V = 0 between](../images/05-the-infinite-square-well-fig-02.png)
*Figure 5.2 — diagram of the infinite square well potential — V = ∞ for x ≤ 0 and x ≥ L shown as vertical walls, V = 0 between*

---

## The Derivation in Eight Steps

**Can $E$ be negative?** Let's check, because we should not assume it can't. If $E < 0$, write $\kappa^2 = -2mE/\hbar^2 > 0$. The equation turns into $\psi'' = \kappa^2\psi$, whose general solution is $\psi = Ae^{\kappa x} + Be^{-\kappa x}$ — a sum of real exponentials. But a sum of real exponentials cannot vanish at *both* $x = 0$ and $x = L$ unless $A = B = 0$, which is no particle at all. And $E = 0$ is no better: there the equation is $\psi'' = 0$, so $\psi = ax + b$, a straight line, and the boundary conditions pin both constants to zero. So negative and zero energies are dead ends. Only $E > 0$ gives anything alive.

**The general solution for $E > 0$.** Define $k = \sqrt{2mE}/\hbar > 0$. Now the TISE reads $\psi'' = -k^2\psi$ — the equation of a spatial oscillator, the same shape as a swinging pendulum — with general solution

$$\psi(x) = A\sin(kx) + B\cos(kx).$$

And notice: at this point *any* positive $k$ is allowed. Nothing is quantized yet. The continuum is still wide open.

**Apply the boundary condition at $x = 0$.** Substitute: $\psi(0) = A\sin(0) + B\cos(0) = B = 0$. So the cosine term dies, and the solution shrinks to $\psi(x) = A\sin(kx)$. Still no quantization — $k$ is still free.

**Apply the boundary condition at $x = L$.** Now the second wall speaks: $\psi(L) = A\sin(kL) = 0$. Either $A = 0$ — no particle, discard it — or

$$\sin(kL) = 0.$$

*This* single equation is where quantization walks in the door. A sine vanishes only at integer multiples of $\pi$. So $kL = n\pi$ for $n = 1, 2, 3, \ldots$ The continuous infinity of allowed $k$ values has just collapsed, in one stroke, to a discrete ladder labeled by an integer. Watch it happen at exactly this step — nowhere earlier, nowhere later.

And I want to be emphatic about this, because it is the whole moral of the chapter. This is not a postulate. It is not an assumption about angular momentum, not a new law bolted on to fix a problem. It is the *only* way a sine wave can vanish at both walls at the same time. Bohr had to *postulate* quantization in 1913. Schrödinger *derived* it in 1926 — from a differential equation and two boundary conditions, and nothing else.

**The wave vectors and energy levels.** The allowed wave vectors are $k_n = n\pi/L$. Since $E = \hbar^2 k^2/2m$:

$$\boxed{E_n = \frac{n^2\pi^2\hbar^2}{2mL^2}, \qquad n = 1, 2, 3, \ldots}$$

The energies climb as $n^2$. The first few ratios: $E_1 : E_2 : E_3 : E_4 = 1 : 4 : 9 : 16$. And nothing — nothing at all — is allowed in the gaps between these values. (Quick housekeeping: $n = 0$ gives $k_0 = 0$ and $\psi = A\sin(0) = 0$, no particle, excluded. And negative $n$? Then $\sin(-n\pi x/L) = -\sin(n\pi x/L)$, which gives the identical probability density — it is the same physical state up to an unobservable sign, nothing new.)

**Normalization.** The unnormalized eigenstate is $A\sin(n\pi x/L)$. Demand $\int_0^L|\psi_n|^2\,dx = 1$, and use $\int_0^L\sin^2(n\pi x/L)\,dx = L/2$ (which follows from $\sin^2\theta = (1-\cos2\theta)/2$, integrated over a whole number of half-periods):

$$A^2 \cdot \frac{L}{2} = 1 \implies A = \sqrt{\frac{2}{L}}.$$

The normalized eigenstates are

$$\boxed{\psi_n(x) = \sqrt{\frac{2}{L}}\,\sin\!\left(\frac{n\pi x}{L}\right), \quad 0 \leq x \leq L; \qquad \psi_n(x) = 0 \text{ elsewhere.}}$$

---

## What the Spectrum Looks Like Physically

Numbers make this real. For an electron in a well of width $L = 1$ nm, the ground-state energy is

$$E_1 = \frac{\pi^2(1.055\times10^{-34})^2}{2(9.109\times10^{-31})(10^{-9})^2} \approx 6.0\times10^{-20}\ \text{J} \approx 0.377\ \text{eV.}$$

So $E_2 \approx 1.51$ eV and $E_3 \approx 3.39$ eV. Now appreciate the scale of those numbers: these are energies right in the thick of chemistry and optics. A visible photon carries roughly 2 eV. Room-temperature thermal jostling is $k_BT \approx 0.025$ eV. The spacings between our levels are *huge* compared to that thermal energy — which means the quantum structure is not some delicate effect you have to coddle into existence. At this scale it dominates.

Now run the same formula on a 1 g marble in a 1 cm box, just to feel the contrast:

$$E_1 \approx \frac{\pi^2(10^{-34})^2}{2(10^{-3})(10^{-2})^2} \approx 5\times10^{-62}\ \text{J} \approx 3\times10^{-43}\ \text{eV.}$$

That is twenty orders of magnitude below anything any instrument could ever resolve. The quantum discreteness is genuinely there, in principle — and genuinely invisible, in practice. So the classical limit is not a philosophical posture you adopt; it is a number you compute. Do the arithmetic and the quantum world simply vanishes beneath the noise.

<!-- → [TABLE: E_n for n = 1 to 5 for three systems — electron in 1 nm well, electron in 10 nm well, proton in 1 nm well; columns: n, E_n (eV), E_n/E_1; shows how the spectrum scales with L² and m, and makes the classical limit for the proton visible] -->

There is a lovely piece of structure in the eigenstates worth pointing out. The state $\psi_n$ has exactly $n - 1$ interior nodes — zeros strictly inside $(0, L)$, not counting the walls. $\psi_1$: one half-period, no interior zeros. $\psi_2$: two half-periods, one interior zero at $x = L/2$. $\psi_n$: $n$ half-periods, $n - 1$ zeros. And here is the chain that makes it physics rather than trivia: more nodes means shorter wavelength, which means higher spatial frequency, which means higher momentum ($p = \hbar k_n = n\pi\hbar/L$), which means higher energy. Node counting is Fourier logic made visible to the eye. Count the wiggles and you have read off the energy ordering.

---

## Orthonormality — a Three-Line Proof

The eigenstates satisfy $\langle\psi_m|\psi_n\rangle = \delta_{mn}$ — they are orthonormal. And the proof leans on exactly one trigonometric identity:

$$\sin\alpha\sin\beta = \frac{1}{2}\bigl[\cos(\alpha-\beta) - \cos(\alpha+\beta)\bigr].$$

Apply it to $\langle\psi_m|\psi_n\rangle = (2/L)\int_0^L\sin(m\pi x/L)\sin(n\pi x/L)\,dx$:

$$\langle\psi_m|\psi_n\rangle = \frac{1}{L}\int_0^L\!\left[\cos\!\left(\frac{(m-n)\pi x}{L}\right) - \cos\!\left(\frac{(m+n)\pi x}{L}\right)\right]dx.$$

Now read off the two cases. For $m \neq n$: both integrands are cosines stretched over a whole number of full periods on $[0, L]$, and a cosine over complete periods integrates to zero. So $\langle\psi_m|\psi_n\rangle = 0$ — distinct eigenstates are perpendicular. For $m = n$: the first cosine becomes $\cos(0) = 1$, which integrates to $L$, while the second is still a cosine over $n$ full periods and dies. So $\langle\psi_n|\psi_n\rangle = 1$ — each is normalized. Done, in three lines.

No numerical eigensolver. No Gram-Schmidt. No computer at all. This is exact, analytic, and it follows straight out of classical Fourier analysis — which Fourier established in 1822 for the heat equation, more than a century before quantum mechanics existed. The mathematics of standing waves on a bounded interval was already complete, sitting on the shelf. All quantum mechanics had to add was the physical interpretation of what those standing waves mean.

---

## Why the Ground State Cannot Be Still

Here is a fact that should bother you at first: the lowest allowed energy is $E_1 = \pi^2\hbar^2/2mL^2$, and that is strictly *greater than zero*. The particle cannot have $E = 0$. It cannot, in other words, just sit quietly at rest. Why on earth not?

The Heisenberg uncertainty principle tells you why, and the argument is clean enough to do in your head. Suppose $E = 0$. Then the kinetic energy is zero, so the momentum is zero, so the momentum *uncertainty* $\sigma_p = 0$ — a particle with no spread in momentum at all. But the particle is trapped in a box of width $L$, so its position uncertainty cannot exceed the box: $\sigma_x \leq L$. Now feed both into the Kennard inequality $\sigma_x\sigma_p \geq \hbar/2$: you get $L \cdot 0 \geq \hbar/2$, which says $0 \geq \hbar/2$. That is false. So the assumption that started it — $E = 0$ — must be false. A particle pinned in space simply cannot also have perfectly definite (zero) momentum. The uncertainty principle forbids the still ground state.

And this is not some quantum eccentricity — it is the wave nature of matter, plain and simple. A guitar string stretched dead flat has zero energy and zero frequency, sure. But the *lowest non-trivial mode* — the fundamental — has a positive frequency and therefore positive energy. The same logic governs any wave confined to a finite domain. There is always a floor above zero.

Let's make it quantitative. For the ground state, $\sigma_p = \pi\hbar/L$ (from $\langle p^2\rangle = \pi^2\hbar^2/L^2$ with $\langle p\rangle = 0$ by symmetry), and $\sigma_x \approx 0.181L$. So $\sigma_x\sigma_p \approx 0.568\hbar \approx 1.136 \times (\hbar/2)$ — about 14% above the absolute minimum the uncertainty principle permits. Which is a striking result on its own: the ground state of the infinite well sits remarkably close to the most tightly localized state quantum mechanics will ever allow. It is nearly the best you can do.

<!-- → [FIGURE: ground-state and first-excited-state wave functions ψ₁ and ψ₂, and their probability densities |ψ₁|² and |ψ₂|², all four curves on the same x-axis from 0 to L; labels should indicate node count and the zero-point energy E₁ > 0; useful for making the zero-node / one-node distinction visually clear] -->

![ground-state and first-excited-state wave functions ψ₁ and ψ₂, and their probability densities |ψ₁|² and |ψ₂|², all four curves on the same…](../images/05-the-infinite-square-well-fig-03.png)
*Figure 5.3 — ground-state and first-excited-state wave functions ψ₁ and ψ₂, and their probability densities |ψ₁|² and |ψ₂|², all four curves on the same…*

---

## Time Evolution and the Sloshing State

The eigenstates $\psi_n$ are stationary states — their probability densities $|\psi_n|^2$ never change in time. The full time-dependent wave function for one eigenstate is $\Psi_n(x,t) = \psi_n(x)e^{-iE_n t/\hbar}$, where the time factor is a pure phase rotation, and that phase cancels itself the moment you form $|\Psi_n|^2 = |\psi_n|^2$. Nothing moves.

So where does motion come from? Only from superposing two or more eigenstates with *different* energies. Take the equal-weight blend of the first two:

$$\Psi(x,t) = \frac{1}{\sqrt{2}}\,\psi_1(x)\,e^{-iE_1 t/\hbar} + \frac{1}{\sqrt{2}}\,\psi_2(x)\,e^{-iE_2 t/\hbar}.$$

The probability density works out to

$$|\Psi(x,t)|^2 = \frac{1}{2}\!\left[\psi_1^2 + \psi_2^2 + 2\,\psi_1\psi_2\cos\!\left(\frac{(E_2-E_1)t}{\hbar}\right)\right].$$

The first two terms just sit there, static. But the cross term breathes, oscillating at angular frequency $\omega = (E_2 - E_1)/\hbar = 3E_1/\hbar$. So the period is

$$T = \frac{2\pi\hbar}{E_2 - E_1} = \frac{h}{3E_1}.$$

For the 1 nm electron, with $E_1 \approx 6.0\times10^{-20}$ J, that comes out to $T \approx 3.66$ femtoseconds. The probability distribution swings from one side of the well to the other and back on a timescale of a few femtoseconds. That is fast — but it is real, and modern ultrafast experiments can chase dynamics on exactly this clock.

**Where is the particle, on average?** Compute $\langle x\rangle(t) = \int_0^L x|\Psi(x,t)|^2\,dx$. Because both $\psi_1$ and $\psi_2$ are symmetric about $L/2$, each on its own contributes $\langle x\rangle_{1} = \langle x\rangle_{2} = L/2$ — dead center. So all the *motion* has to live in the cross term:

$$\langle x\rangle(t) = \frac{L}{2} + \cos\!\left(\frac{(E_2-E_1)t}{\hbar}\right)\int_0^L x\,\psi_1(x)\,\psi_2(x)\,dx.$$

The cross integral takes an integration by parts. Expand $\psi_1\psi_2$ with the product-to-sum identity, integrate $\int_0^L x\cos(n\pi x/L)\,dx$ by parts, and the result is

$$\int_0^L x\,\psi_1\psi_2\,dx = -\frac{16L}{9\pi^2} \approx -0.180\,L.$$

So

$$\langle x\rangle(t) = \frac{L}{2} - \frac{16L}{9\pi^2}\cos\!\left(\frac{(E_2-E_1)t}{\hbar}\right).$$

Read off the story. At $t = 0$, $\cos(0) = 1$, giving $\langle x\rangle(0) \approx L/2 - 0.180L \approx 0.320L$. The initial state is *left-heavy*: the probability piles up near $x = L/4$, because $\psi_1 + \psi_2$ — a half-sine added to a full-sine — has its constructive bulge in the left half of the well. And since $d\langle x\rangle/dt|_{t=0} = 0$ (the cosine is sitting at a turning point), the center of mass starts from rest, then drifts rightward, reaching $\langle x\rangle \approx 0.680L$ at the half-period before swinging back. The total swing is about $0.360L$ — better than a third of the way across the box.

Through all of this commotion, the energy expectation value is

$$\langle\hat{H}\rangle = \frac{1}{2}E_1 + \frac{1}{2}E_2 \approx \frac{0.377 + 1.508}{2} \approx 0.943\ \text{eV.}$$

Flat. Constant. The probability is sloshing back and forth like water in a tilting tank, and the energy never moves a hair. The $|c_n|^2$ — the weights on each eigenstate — are fixed by the initial state and frozen for all time. What evolves is the *relative phase* between the two terms, which slides the interference pattern in $|\Psi|^2$ around while leaving the energy budget untouched. Sloshing probability, motionless energy. That pairing is the heart of the chapter.

<!-- → [CHART: three-panel animation schematic — (1) |Ψ(x,t)|² at t = 0, t = T/4, t = T/2, t = 3T/4, showing the probability density sloshing left to right; (2) ⟨x⟩(t) as a function of time, oscillating between 0.320L and 0.680L; (3) ⟨H⟩(t) as a flat line — visually emphasizing that energy is constant while position expectation oscillates] -->

![three-panel animation schematic — (1) |Ψ(x,t)|² at t = 0, t = T/4, t = T/2, t = 3T/4, showing the probability density sloshing left to right](../images/05-the-infinite-square-well-fig-04.png)
*Figure 5.4 — three-panel animation schematic — (1) |Ψ(x,t)|² at t = 0, t = T/4, t = T/2, t = 3T/4, showing the probability density sloshing left to right*

---

## The Fourier Structure Underneath

The eigenstates $\{\psi_n\}$ form a complete orthonormal basis for square-integrable functions on $[0, L]$ that vanish at the endpoints. "Complete" is the powerful word: *any* such function can be expanded in them.

$$f(x) = \sum_{n=1}^{\infty} c_n\,\psi_n(x), \qquad c_n = \int_0^L\psi_n(x)\,f(x)\,dx.$$

This is just the Fourier sine series wearing a physicist's hat. The coefficients $c_n$ are projections — inner products of the initial state onto each eigenstate, picking off "how much of $\psi_n$ is in there." So given any initial condition $\Psi(x, 0)$, you find the $c_n$ by integration, then attach the time-evolution phases and let each piece spin:

$$\Psi(x,t) = \sum_{n=1}^{\infty} c_n\,\psi_n(x)\,e^{-iE_n t/\hbar}.$$

Each eigenstate twirls at its own angular frequency $E_n/\hbar$. When two or more are present with different energies, the relative phases between them keep evolving, and the result is interference that reshapes $|\Psi|^2$ over time — the sloshing, generalized.

Now pin down a subtle point. The probability of measuring energy $E_n$ is $|c_n|^2$. Notice what falls out of that: the $|c_n|^2$ are set once, by the initial state, and they do not change in time — so as far as *energy* measurements go, the $c_n$ have only one observable consequence, and it is frozen. The phases of the $c_n$ matter only for *position and momentum* measurements, where the cross terms in $|\Psi|^2$ — the interference terms — carry the relative-phase information. Energy sees the magnitudes; position and momentum see the phases.

And here is a consequence that points straight at the classical world. A narrow initial state, bunched up near a single point, needs *many* nonzero $c_n$ — because representing a sharp spike as a sum of smooth sine waves takes a great many harmonics. Many harmonics means many distinct frequencies, which means many beat frequencies between pairs of eigenstates, which means rapid dephasing of the initial spatial structure. A particle started tightly localized near $x = L/4$ will *not* stay near $x = L/4$; it spreads, sloshes, and eventually smears out to nearly uniform. The classical limit corresponds to packets so heavy and slow that this dephasing timescale stretches out to something astronomical — effectively forever. Which is why a thrown baseball does not visibly slosh across its allowed region: it does, in principle, on a timescale longer than the universe has existed.

---

## What Comes Next

The infinite square well hands you clean answers precisely *because* its walls are perfectly rigid. No wave function leaks through $V = \infty$; no energy tunnels out. But real quantum systems — semiconductor quantum wells, quantum dots, atoms held in optical-lattice traps — have *finite* barriers, and there the wave function does seep in, and through. The discrete levels of a finite-depth well are qualitatively cousins of the infinite-well levels, but shifted downward, and — this is the new twist — finite in number: a well of depth $V_0$ and width $L$ supports only finitely many bound states. Crank $V_0 \to \infty$ and those levels climb back up toward the infinite-well values from below. The infinite well is the clean limiting case of the messy real thing.

And there is a question the infinite well pointedly does *not* answer, and I will not pretend it does. Why is the probability interpretation correct in the first place, and what does it actually mean for the wave function to "collapse" when you measure? Solving the TISE tells you nothing about that. It is the measurement problem, and it sits at the foundation of quantum mechanics in a way the Schrödinger equation simply does not resolve. Chapter 3 laid out Born's rule as a postulate, and a postulate it remains. What the infinite well *does* show — and this is no small thing — is that Born's rule, married to the Schrödinger equation, makes predictions that come out experimentally exact. The Davisson–Germer diffraction, the quantum corral, the energy levels of semiconductor quantum wells measured spectroscopically by Dingle and colleagues in 1974 — all of them confirm that the quantization we derived here is not a mathematical accident. The walls impose it, and nature, checked to many decimal places, obeys.

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

---

## Running Project — Build the 1D Quantum Sandbox

**This chapter adds:** the heart of the eigensolver — the real, symmetric, tridiagonal Hamiltonian built from the central-difference stencil ($H_{jj} = 2t_k + V_j$, $H_{j,j\pm1} = -t_k$ with $t_k = \hbar^2/2mh^2$), its diagonalization into $\{E_n,\psi_n\}$, and the **golden test** that validates the whole machine against $E_n = n^2\pi^2\hbar^2/2mL^2$, i.e. $E_n/E_1 = n^2$ with no fitting parameters.

### Exercise R1 — When to Use AI
**The judgment:** In this chapter's project work, AI assistance is appropriate for:
- Assembling the tridiagonal matrix from $t_k$, the diagonal $2t_k + V_j$, and the off-diagonals $-t_k$ over the interior $(N-2)$ points — *Why AI works here:* it is filling a banded matrix from a stated stencil, and the golden test gives an exact pass/fail.
- Wiring `math.eigs()` (or a Numerov shooter) and sorting eigenvalues ascending — *Why AI works here:* calling a library and sorting is boilerplate; the ratios $E_n/E_1$ tell you instantly whether it worked.
**The tell:** You are using AI well when you have an independent way to check the output — here, $E_2/E_1 = 4.000$, $E_3/E_1 = 9.000$ to three decimals, independent of any physical constant.

### Exercise R2 — When NOT to Use AI
**The judgment:** These tasks require your judgment; AI output here can't be trusted without redoing the work:
- The factor in the kinetic coefficient — diagonal $\hbar^2/mh^2 = 2t_k$ vs off-diagonal $-t_k = -\hbar^2/2mh^2$, and $h^2$ not $h$ in the denominator — *Why AI fails here:* confusing $2t_k$ with $t_k$ is a factor-of-2 error that makes $E_1$ wrong while leaving $E_2/E_1 = 4$ intact; using $h$ instead of $h^2$ makes $E_1$ scale as $1/N$ instead of $1/N^2$. Both produce a clean-looking spectrum the AI will not flag.
- Whether the returned eigenvectors carry physics normalization ($\sum|\psi_j|^2 h = 1$) — *Why AI fails here:* `math.eigs` returns Euclidean-normalized vectors; without the $1/\sqrt h$ correction the indicator reads $1/h \approx 250$, and the AI may "fix" it by the wrong power of $h$.
**The tell:** If you could not explain the result without the AI — if the AI is your *reason* rather than your *tool* — it did work that should have been yours.
**Physics-judgment connection:** This trains the golden discipline of the whole book — checking a numerical spectrum against the analytic $E_n = n^2 E_1$ before believing it, which catches the factor-of-2 and $h$-vs-$h^2$ errors that a plausible-looking plot hides.

### Exercise R3 — LLM Exercise
**What you're building this chapter:** the tridiagonal Hamiltonian builder, the eigensolver, and the golden-test validation table.
**Tool:** Claude Project — the Hamiltonian builder is the load-bearing module every later potential reuses, so it belongs in persistent project context.
**The Prompt:**
```
Using the Chapter 0 CLAUDE.md, constants.js, grid.js, and observables.js as
binding context, build 05-infinite-well-eigensolver.html plus a reusable
hamiltonian.js.

hamiltonian.js exports buildTridiagonal(V, h, m): given a potential array V of
length N and spacing h, build the (N−2)×(N−2) interior Hamiltonian with
  t_k = ℏ²/(2 m h²),
  diagonal H[j][j]   = 2 t_k + V[j],
  off-diagonal H[j][j±1] = −t_k.
(Boundary points j=0, N−1 are excluded → Dirichlet ψ_0 = ψ_{N−1} = 0.)
Diagonalize with math.eigs (math.js from CDN; this is an approved addition).
Sort eigenvalues ascending; normalize each eigenvector so Σ_j|ψ_j|² h = 1
(divide the Euclidean eigenvector by √h, NOT h).

05-...html: set V = 0 inside [0, L] with hard walls, L = 2 nm, m = m_e,
N = 500. Plot V(x) (red), energy levels as green horizontal lines, |ψ_n|²
offset to E_n. Show a validation TABLE: for n = 1..5, columns
  E_n analytic (eV) | E_n numerical (eV) | E_n/E_1 numerical | fractional error.
Analytic E_n = n²π²ℏ²/(2 m_e L²).

THE GOLDEN TEST: assert E_2/E_1, E_3/E_1, E_4/E_1 equal 4, 9, 16 to three
decimals, and fractional error on E_1 < 1e-4. Report pass/fail explicitly.
Do NOT tune any constant to make the table match — if it fails, diagnose
whether it is the t_k factor (2t_k vs t_k), the h-vs-h² denominator, or the
eigenvector normalization (√h).
```
**What this produces:** `hamiltonian.js` (reused by every potential from Chapter 6 on) and `05-infinite-well-eigensolver.html` with the golden-test table.
**How to adapt:** *Your system:* for >20 states keep `math.eigs`; for 3–5 states a Numerov shooter avoids the library. *ChatGPT/Gemini:* paste the dependency files. *Claude Project:* put `hamiltonian.js` in Project knowledge — it is the spine of the solver.
**Builds on:** the ψ array and normalization from Chapter 3, the grid from Chapter 2.  **Next:** Chapter 6 feeds this builder an arbitrary $V(x)$ for finite wells and barriers.

### Exercise R4 — CLI Exercise
**What you're building this chapter:** the eigensolver with the golden test wired as an automated assertion.
**Tool:** Claude Code — it can run the diagonalization and assert the $n^2$ ratios, failing loudly if the Hamiltonian factor is wrong.
**Skill level:** Advanced
**Setup — confirm:**
- [ ] `hamiltonian.js`, `grid.js`, `constants.js`, `observables.js`
- [ ] math.js available (CDN in the browser, or `npm i mathjs` for the script)
- [ ] The CLAUDE.md rule that every spectrum ships with an analytic self-check
**The Task:**
```
Read hamiltonian.js. Write a Node script golden-test.js that builds the
infinite-well Hamiltonian (V = 0, L = 2 nm, m = m_e, N = 500), diagonalizes it,
normalizes eigenvectors to Σ|ψ_j|² h = 1, and asserts:
  (1) E_2/E_1, E_3/E_1, E_4/E_1, E_5/E_1 = 4, 9, 16, 25 to 3 decimals;
  (2) |E_1_num − E_1_analytic| / E_1_analytic < 1e-4;
  (3) Σ_j|ψ_1_j|² h = 1.000 ± 1e-3 and orthogonality |⟨ψ_1|ψ_2⟩| < 1e-8.
Print the full n=1..5 comparison table. Do NOT adjust constants or tolerances
to force a pass. If it fails, print which diagnostic (t_k factor, h², or √h
normalization) is the likely cause. Append to PROJECT.md under "Verified":
"Ch5 GOLDEN TEST: E_n/E_1 = 4/9/16/25 ✓, E_1 err = <v>".
```
**Expected output:** `golden-test.js`, a printed comparison table, an explicit PASS, and a `PROJECT.md` line marking the golden test.
**What to inspect:** the ratios must be 4/9/16/25 *and* $E_1$ must match the analytic value — the ratios alone pass even with an $h$-vs-$h^2$ error, so the absolute $E_1$ check is what catches it.
**If it goes wrong:** if ratios are perfect but $E_1$ is off by exactly 2×, the diagonal used $t_k$ instead of $2t_k$; if $E_1$ scales as $1/N$ rather than $1/N^2$ as you vary $N$, the denominator used $h$ not $h^2$. Diagnose by the symptom, then fix the stencil.
**CLAUDE.md / AGENTS.md note:** add: "The infinite-well golden test ($E_n/E_1 = n^2$ AND $E_1$ matching analytic to <1e-4) must pass before any other potential is trusted. It is the regression gate for the eigensolver."

### Exercise R5 — AI Validation Exercise
**What you're validating:** the tridiagonal Hamiltonian and eigensolver against the analytic infinite-well spectrum — the golden test itself.
**Validation type:** Numerical result
**Risk level:** High — this is the module every other potential reuses, and the factor-of-2 / $h$-vs-$h^2$ errors are exactly the kind that pass a visual check.
**Setup:** use your own R3/R4 artifacts; the analytic spectrum $E_n = n^2\pi^2\hbar^2/2m_eL^2$ is the fixed ground truth.
**The Validation Task:** Evaluate against this checklist; mark Pass / Fail / Cannot determine with reasoning.
```
Validation Checklist — Tridiagonal Hamiltonian and the golden test
□ Correctness: diagonal = 2t_k + V_j and off-diagonal = −t_k with t_k = ℏ²/(2mh²)?
□ Completeness: does it show absolute E_n AND the E_n/E_1 ratios AND orthogonality?
□ Scope: did it build the full N×N matrix instead of the (N−2)×(N−2) interior block?
□ Physics criterion 1: E_2/E_1 = 4.000, E_3/E_1 = 9.000 to three decimals?
□ Physics criterion 2: E_1 matches n²π²ℏ²/(2m_eL²) to < 1e-4 fractional error?
□ Failure-mode check: any of —
  - factor-of-2 (diagonal used t_k not 2t_k): ratios pass but E_1 is 2× wrong
  - h-vs-h² in t_k: E_1 scales as 1/N instead of 1/N²
  - unnormalized eigenvectors (Σ|ψ_j|² h reads 250 = 1/h instead of 1)
  - ratios "correct" because the AI hardcoded n² instead of computing E_n
```
**What to do with findings:** pass → use it, and lock it as the regression gate; one fail → diagnose by symptom (ratios-pass-but-E₁-wrong ⇒ factor of 2; wrong $N$-scaling ⇒ $h$ vs $h^2$), fix the stencil, re-run; multiple fails / cannot-determine → rebuild the $5\times5$ Hamiltonian by hand for $N=7$ (Exercise 1 in the capstone) and compare entry by entry.
**AI Use Disclosure (mandatory, two sentences):**
> *1:* The AI built the tridiagonal Hamiltonian and called the eigensolver, producing the energies and eigenfunctions.
> *2:* The AI could not determine whether the kinetic factor and eigenvector normalization were correct from the code alone — I confirmed it by checking the spectrum against $E_n = n^2E_1$ and the absolute $E_1$ against the analytic value.
**Physics-judgment connection:** this *is* the golden test — checking a computed spectrum against the analytic $E_n = n^2E_1$ with no fitted parameters, the single most important verification discipline in the entire project.
