# Chapter 7 — The Quantum Harmonic Oscillator

Displace a guitar string sideways and let go. The restoring force is proportional to the displacement — Hooke's law — and simple harmonic motion follows. Now take *any* smooth potential with a minimum and Taylor-expand it about that minimum. The first derivative is gone, because that is what "minimum" means. The constant term only relocates the energy zero. What survives at leading order is a quadratic:

$$V(x) \approx \frac{1}{2}V''(x_0)\,(x-x_0)^2 = \frac{1}{2}m\omega^2(x-x_0)^2,$$

with $\omega = \sqrt{V''(x_0)/m}$ fixed by the curvature. Every stable equilibrium in every physical system, for small enough displacements, *is* a harmonic oscillator. The guitar string, the diatomic molecule, the mode of a laser cavity, the vibration of a crystal lattice, the quantized vacuum field — all collapse onto the same Hamiltonian:

$$\hat{H} = \frac{\hat{p}^2}{2m} + \frac{1}{2}m\omega^2\hat{x}^2. \tag{7.1}$$

This is not a special case. It is the generic case for any quantum system near equilibrium. Solve it once and you have solved every system in the class. The only question is how.

---

## The Trick

You could grind through it: write $\hat{p} = -i\hbar\,\partial_x$, plug into (7.1), and solve a second-order differential equation. That works, it produces Hermite polynomials, and I describe it below. But there is a better way — one that delivers the entire spectrum without a single differential equation.

Define two operators:

$$\hat{a}_\pm = \frac{1}{\sqrt{2\hbar m\omega}}\!\left(\mp i\hat{p} + m\omega\hat{x}\right). \tag{7.2}$$

These are the **raising** ($\hat{a}_+$) and **lowering** ($\hat{a}_-$) operators, or ladder operators. Multiply them out:

$$\hat{a}_-\hat{a}_+ = \frac{1}{2\hbar m\omega}\!\left(i\hat{p} + m\omega\hat{x}\right)\!\left(-i\hat{p} + m\omega\hat{x}\right).$$

The $\hat{p}^2$ and $m^2\omega^2\hat{x}^2$ terms reassemble into $\hat{H}/(\hbar\omega)$. The cross terms give $im\omega(\hat{p}\hat{x} - \hat{x}\hat{p}) = im\omega(-i\hbar) = m\omega\hbar$, contributing $1/2$. So:

$$\hat{a}_-\hat{a}_+ = \frac{\hat{H}}{\hbar\omega} + \frac{1}{2}, \qquad \hat{a}_+\hat{a}_- = \frac{\hat{H}}{\hbar\omega} - \frac{1}{2}.$$

Subtract:

$$\boxed{[\hat{a}_-, \hat{a}_+] = 1.} \tag{7.3}$$

This single commutator is the entire problem in algebraic form. Every energy level, every relation among eigenstates, every expectation value comes out of it. In quantum field theory the same relation — with $\hat{a}_-$ the annihilation operator and $\hat{a}_+$ the creation operator — opens quantum electrodynamics. Here it shows up in the simplest setting there is.

---

## Climbing the Ladder

Let $|n\rangle$ be an energy eigenstate, $\hat{H}|n\rangle = E_n|n\rangle$. From the commutator (7.3) and $\hat{H} = \hbar\omega(\hat{a}_+\hat{a}_- + \tfrac{1}{2})$ you can derive

$$[\hat{H}, \hat{a}_+] = \hbar\omega\,\hat{a}_+, \qquad [\hat{H}, \hat{a}_-] = -\hbar\omega\,\hat{a}_-.$$

Now ask what energy $\hat{a}_+|n\rangle$ carries:

$$\hat{H}(\hat{a}_+|n\rangle) = (\hat{a}_+\hat{H} + [\hat{H},\hat{a}_+])|n\rangle = (E_n + \hbar\omega)\,\hat{a}_+|n\rangle.$$

So $\hat{a}_+$ turns one eigenstate into another, $\hbar\omega$ higher; $\hat{a}_-$ produces one $\hbar\omega$ lower. The operators are a ladder: climb up one rung at a time, descend one rung at a time, every rung spaced exactly $\hbar\omega$ from the last.

The ladder cannot descend forever. The Hamiltonian (7.1) is a sum of squares of Hermitian operators, so $\langle\hat{H}\rangle \geq 0$ in every state. But $\hat{a}_-$ peels off $\hbar\omega$ each time, and if you could apply it without end you would eventually arrive at negative energy — impossible. The escape is a ground state $|0\rangle$ that the lowering operator annihilates:

$$\hat{a}_-|0\rangle = 0. \tag{7.4}$$

Apply $\hat{H} = \hbar\omega(\hat{a}_+\hat{a}_- + \tfrac{1}{2})$ to it:

$$\hat{H}|0\rangle = \hbar\omega\!\left(\hat{a}_+\underbrace{(\hat{a}_-|0\rangle)}_{=\,0} + \tfrac{1}{2}|0\rangle\right) = \tfrac{1}{2}\hbar\omega\,|0\rangle.$$

The ground-state energy is $E_0 = \hbar\omega/2$ — not zero, but $\hbar\omega/2$. Start from $|0\rangle$ and apply $\hat{a}_+$ repeatedly:

$$\boxed{E_n = \left(n + \frac{1}{2}\right)\hbar\omega, \quad n = 0, 1, 2, \ldots} \tag{7.5}$$

Equally spaced levels with gap $\hbar\omega$, and a ground state sitting $\hbar\omega/2$ above the classical floor of the potential. Not one differential equation was solved. The whole spectrum dropped out of one commutator plus the demand that energy never go negative.

---

## Zero-Point Energy Is Real

The ground-state energy $E_0 = \hbar\omega/2 \neq 0$ is not a technicality you can wave away. Classically the minimum energy of a harmonic oscillator is zero: the particle sits motionless at the bottom of the well. Quantum-mechanically the uncertainty principle forbids that. A particle pinned at $x = 0$ with $\sigma_x \to 0$ would need $\sigma_p \to \infty$ by the Kennard inequality $\sigma_x\sigma_p \geq \hbar/2$. The zero-point energy is the minimum kinetic energy that confinement extracts as a toll.

You can measure it. Liquid helium refuses to solidify at atmospheric pressure at any temperature, because the zero-point kinetic energy of helium atoms — squeezed into the interatomic spacing — exceeds the binding energy holding a lattice together. The atoms simply cannot settle. Helium is a quantum liquid *because* of zero-point motion, not in spite of it.

More directly still: the Casimir force between two conducting plates comes from the difference in zero-point energies of the electromagnetic modes with and without the plates present. Lamoreaux measured it in 1997 and matched the prediction to within five percent. Zero-point energy is not a bookkeeping artifact. It sends an invoice, and you can read it in the lab.

---

## The Normalized Ladder

The normalized eigenstates obey

$$\hat{a}_+|n\rangle = \sqrt{n+1}\,|n+1\rangle, \qquad \hat{a}_-|n\rangle = \sqrt{n}\,|n-1\rangle. \tag{7.6}$$

Those prefactors $\sqrt{n+1}$ and $\sqrt{n}$ are not garnish. Drop them and every expectation value you compute comes out wrong. They originate in the norm: $\hat{a}_+|n\rangle$ has norm $\sqrt{n+1}$ (since $\langle n|\hat{a}_-\hat{a}_+|n\rangle = n+1$), so dividing by the norm gives the unit-normalized $|n+1\rangle$.

Express $\hat{x}$ and $\hat{p}$ directly through the ladder:

$$\hat{x} = \sqrt{\frac{\hbar}{2m\omega}}\!\left(\hat{a}_+ + \hat{a}_-\right), \qquad \hat{p} = i\sqrt{\frac{m\hbar\omega}{2}}\!\left(\hat{a}_+ - \hat{a}_-\right). \tag{7.7}$$

Now expectation values in any eigenstate $|n\rangle$ become trivial. Since $\hat{a}_\pm|n\rangle$ is orthogonal to $|n\rangle$,

$$\langle n|\hat{x}|n\rangle = 0, \qquad \langle n|\hat{p}|n\rangle = 0.$$

For $\hat{x}^2$, write $\hat{x}^2 = (\hbar/2m\omega)(\hat{a}_+ + \hat{a}_-)^2$. The terms $\hat{a}_+^2$ and $\hat{a}_-^2$ link $|n\rangle$ to $|n\pm 2\rangle$ and drop out; what survives gives

$$\langle n|\hat{x}^2|n\rangle = \frac{\hbar}{2m\omega}\!\left(n + n + 1\right) = \frac{\hbar(2n+1)}{2m\omega}. \tag{7.8}$$

The uncertainty product:

$$\sigma_x\sigma_p = \left(n + \frac{1}{2}\right)\hbar. \tag{7.9}$$

At $n = 0$, $\sigma_x\sigma_p = \hbar/2$ — the Kennard inequality saturated exactly. The harmonic-oscillator ground state is the unique minimum-uncertainty state.

For the off-diagonal element, $\langle m|\hat{x}|n\rangle \propto \delta_{m,n\pm 1}$: position connects only states one quantum apart. That is the selection rule for dipole transitions — only $\Delta n = \pm 1$ is allowed — which is why the infrared vibrational spectrum of a diatomic molecule is a ruler: evenly spaced absorption lines at frequency $\omega$.

---

## What the Eigenstates Look Like

The algebra hands you the spectrum; the wave functions follow from $\hat{a}_-|0\rangle = 0$, which in position space reads

$$\left(\hbar\frac{\partial}{\partial x} + m\omega x\right)\psi_0(x) = 0.$$

Separate and normalize:

$$\psi_0(x) = \left(\frac{m\omega}{\pi\hbar}\right)^{1/4}\exp\!\left(-\frac{m\omega x^2}{2\hbar}\right). \tag{7.10}$$

A Gaussian — the same minimum-uncertainty shape from Chapter 3, but now serving as an energy eigenstate of the oscillator rather than a free-particle packet. The distinction matters. The free-particle Gaussian spreads in time because it is *not* an eigenstate of the free Hamiltonian. The oscillator ground state stays a Gaussian forever, because the potential supplies a restoring force that exactly offsets the urge to spread.

Higher states come from applying $\hat{a}_+$ to $\psi_0$. Each application multiplies the Gaussian by a polynomial one degree higher in $x$ — the Hermite polynomials $H_n(\xi)$ with $\xi = \sqrt{m\omega/\hbar}\,x$:

$$\psi_n(x) = \left(\frac{m\omega}{\pi\hbar}\right)^{1/4}\frac{1}{\sqrt{2^n n!}}\,H_n(\xi)\,e^{-\xi^2/2}, \tag{7.11}$$

with recursion $H_{n+1}(\xi) = 2\xi H_n(\xi) - 2n H_{n-1}(\xi)$, starting from $H_0 = 1$, $H_1 = 2\xi$.

Two things to note. First, $\psi_n$ has exactly $n$ nodes: none for the ground state, one for the first excited state — the same counting rule as the infinite square well. Second, roughly 16% of the ground-state probability lies *outside* the classical turning points $x = \pm\sqrt{\hbar/m\omega}$. Penetration into the classically forbidden region is not some exotic high-energy effect; it is already there in the very first eigenstate, a standard feature of the quantum ground state.

---

## Eigenstates Do Not Oscillate

Here is a misconception worth killing before the simulation runs.

A harmonic oscillator is, classically, an oscillator. You naturally expect the quantum version to oscillate. Build the time-dependent eigenstate:

$$\Psi_n(x,t) = \psi_n(x)\,e^{-iE_n t/\hbar}.$$

The probability density:

$$|\Psi_n(x,t)|^2 = |\psi_n(x)|^2 \cdot |e^{-iE_n t/\hbar}|^2 = |\psi_n(x)|^2.$$

Static. The phase rotates in the complex plane at frequency $E_n/\hbar$, but $|\Psi|^2$ — everything a position detector can register — never budges. Energy eigenstates are stationary states. If quantum mechanics held only eigenstates, classical oscillation would never appear at all.

Oscillation lives in superpositions. Take the equal mixture $|\Psi\rangle = (|0\rangle + |1\rangle)/\sqrt{2}$:

$$|\Psi(x,t)|^2 = \tfrac{1}{2}(|\psi_0|^2 + |\psi_1|^2) + \psi_0\psi_1\cos\!\left(\frac{(E_1-E_0)t}{\hbar}\right).$$

The cross term beats at $(E_1 - E_0)/\hbar = \omega$ — the classical oscillation frequency exactly. The packet sloshes, but it also deforms: not a rigid shape gliding back and forth, but a superposition whose interference pattern shifts continuously.

The simulation shows both at once. The eigenstate panel sits still; the superposition panel sloshes. If the eigenstate panel ever animates, the phase is not canceling and something is wrong.

---

## The State That Sloshes Cleanly

A **coherent state** $|\alpha\rangle$ is the eigenstate of the lowering operator:

$$\hat{a}_-|\alpha\rangle = \alpha\,|\alpha\rangle \tag{7.12}$$

for any complex $\alpha$. In the energy basis,

$$|\alpha\rangle = e^{-|\alpha|^2/2}\sum_{n=0}^\infty \frac{\alpha^n}{\sqrt{n!}}\,|n\rangle. \tag{7.13}$$

Coherent states are not energy eigenstates. They are superpositions of every $|n\rangle$ with Poisson weights $P(n) = e^{-|\alpha|^2}|\alpha|^{2n}/n!$ and mean quantum number $\langle n\rangle = |\alpha|^2$.

Under time evolution a coherent state stays coherent, its amplitude simply rotating:

$$\langle\hat{x}(t)\rangle = \sqrt{\frac{2\hbar}{m\omega}}\,|\alpha|\cos(\omega t - \arg\alpha), \qquad \langle\hat{p}(t)\rangle = -\sqrt{2m\hbar\omega}\,|\alpha|\sin(\omega t - \arg\alpha). \tag{7.14}$$

Position and momentum trace sinusoids at $\omega$, exactly like a classical oscillator. And the packet holds its shape — $\sigma_x\sigma_p = \hbar/2$ at all times. The coherent state is the minimum-uncertainty Gaussian riding its classical orbit indefinitely, never spreading.

Roy Glauber introduced coherent states in 1963 to describe laser light. An ideal laser produces field modes in coherent states. The photon-counting statistics of ideal laser light are Poisson — not because lasers are classical, but because Poisson is the photon-number distribution of a coherent state. The harmonic-oscillator algebra is not an analogy for laser physics; it *is* laser physics. Glauber got the 2005 Nobel Prize for the connection.

---

## Worked Example — Ladder Algebra for HCl

The HCl molecule vibrates near the bottom of its internuclear potential with $\omega \approx 5.63 \times 10^{14}$ rad/s and reduced mass $\mu \approx 1.63 \times 10^{-27}$ kg.

**Zero-point energy:**

$$E_0 = \tfrac{1}{2}\hbar\omega = \tfrac{1}{2}(1.055\times10^{-34})(5.63\times10^{14}) \approx 2.97\times10^{-20}\ \text{J} \approx 0.185\ \text{eV}.$$

**Level spacing:** $\hbar\omega \approx 0.37$ eV. Thermal energy at 300 K is $k_BT \approx 0.025$ eV. Since $k_BT \ll \hbar\omega$, essentially every HCl molecule sits in the vibrational ground state at room temperature. The infrared spectrum shows one absorption line at $\lambda = hc/(\hbar\omega) \approx 3.4\ \mu$m — exactly what is seen.

**Selection rule from ladder algebra.** The dipole matrix element is $\langle m|\hat{x}|n\rangle$. Write $\hat{x} = \ell(\hat{a}_+ + \hat{a}_-)$ with $\ell = \sqrt{\hbar/2\mu\omega}$. Then $\hat{a}_+|n\rangle \propto |n+1\rangle$ and $\hat{a}_-|n\rangle \propto |n-1\rangle$, both orthogonal to any $|m\rangle$ unless $m = n\pm 1$. Every other matrix element is zero:

$$\langle m|\hat{x}|n\rangle = \ell\!\left(\sqrt{n+1}\,\delta_{m,n+1} + \sqrt{n}\,\delta_{m,n-1}\right).$$

Only $\Delta n = \pm 1$ transitions are allowed. The vibrational spectrum is a single frequency, not a thicket of lines — a ruler in frequency space, confirmed by the HCl absorption spectrum.

**Expectation value $\langle\hat{x}^2\rangle$ for $n = 0$, no integrals.** From equation (7.8):

$$\langle 0|\hat{x}^2|0\rangle = \frac{\hbar}{2\mu\omega} = \ell^2.$$

The root-mean-square displacement of HCl in its ground state is $\ell = \sqrt{\hbar/2\mu\omega} \approx 6.7$ pm — about 5% of the 0.13 nm bond length. Small, but not zero, and not obtainable by the classical trick of setting $E = 0$.

---

## Where the Ladder Leads

One commutator: $[\hat{a}_-,\hat{a}_+] = 1$. Out of it: a complete, equally spaced spectrum, selection rules, zero-point energy, coherent states, minimum-uncertainty states. The method — factor the Hamiltonian into operators whose commutator is a scalar, then derive everything algebraically — is not confined to this problem.

In Chapter 10 the angular-momentum operators $\hat{L}_\pm$ obey a different algebra, but the logic is identical: a commutator with $\hat{L}_z$ sets the rung spacing, a non-negativity argument terminates the ladder, and the spectrum drops out with no differential equation. In quantum field theory $\hat{a}_+$ becomes the creation operator that adds a particle to the vacuum: the $n$-photon state is $(\hat{a}_+)^n/\sqrt{n!}$ acting on the vacuum, where the vacuum $|0\rangle$ is exactly the ground state killed by $\hat{a}_-$. The commutator $[\hat{a},\hat{a}^\dagger] = 1$ is the foundation of quantum electrodynamics. This chapter is the template for all of it.

<!-- → [TABLE: Harmonic oscillator parameters for selected diatomic molecules — HCl ω≈5.63e14 rad/s ℏω≈0.37 eV λ≈3.4 μm; N₂ ω≈4.45e14 rad/s ℏω≈0.29 eV; CO ω≈4.09e14 rad/s ℏω≈0.27 eV; H₂ ω≈8.28e14 rad/s ℏω≈0.54 eV] -->

---

## The +1 — Simulation Exercise

### The deliverable

`07-harmonic-oscillator.html` — a single self-contained HTML file with three modes: **Eigenstate** (static probability density for $n = 0, \ldots, 5$), **Coherent state** (sloshing wave packet), and **Superposition** (two-state beating). Three panels: wave function, probability density, and phase-space orbit $\langle x\rangle(t)$ vs. $\langle p\rangle(t)$.

### CLAUDE.md amendment for this chapter

````markdown
## Chapter 7 — The Quantum Harmonic Oscillator

HARMONIC OSCILLATOR PHYSICS RULES

1. HERMITE POLYNOMIALS via recursion:
     H_{n+1}(ξ) = 2ξ H_n(ξ) − 2n H_{n-1}(ξ), H_0 = 1, H_1 = 2ξ.
   Cache H_n across the spatial grid. Cap n ≤ 15 for numerical
   stability; naive recursion overflows double precision for n > 15
   near the turning points. Use scaled Hermites for n > 10.

2. NORMALIZATION: ψ_n(x) = (mω/πℏ)^(1/4) · (1/√(2ⁿ n!)) · H_n(ξ) · exp(−ξ²/2)
   ξ = √(mω/ℏ) x. Natural units ℏ = m = 1, ω slider.
   Precompute n! by lookup for n ≤ 15.

3. TIME EVOLUTION: Ψ(x,t) = Σ_n c_n ψ_n(x) exp(−i E_n t/ℏ)
   with E_n = (n + 1/2)ℏω. Store c_n as {re, im} pairs.
   Phase rotate each frame; sum to get Ψ(x,t); compute |Ψ|².

4. COHERENT STATE: c_n = exp(−|α|²/2) · αⁿ / √(n!).
   Truncate at n_max = ceil(|α|² + 5·√|α|²).
   Verify Σ|c_n|² = 1 within 1e-4 as a runtime sanity check.

5. EIGENSTATE PANEL MUST BE STATIC. If |Ψ_n(x,t)|² animates,
   there is a phase-cancellation bug. Plot ψ_n(x) (real, static).

6. TIME STEP: ωΔt ≤ 0.05 per frame. For ω = 5, Δt ≤ 0.01.

KNOWN FAILURE MODES:
(a) Hermite overflow at large n. Cap at n = 15.
(b) Forgetting to renormalize when ω slider changes.
(c) Phase sign errors for odd n (H_1 = 2ξ, positive at ξ > 0).
(d) Eigenstate panel animating — it must be static.
(e) Coherent state truncation mismatched to |α|².
(f) Confusing ψ and |ψ|² panels — label both axes.
````

### The simulation prompt

````markdown
SHOW.
The quantum harmonic oscillator Hamiltonian H = p²/2m + (1/2)mω²x²
with spectrum E_n = (n + 1/2)ℏω and eigenstates ψ_n(x) = Hermite-Gauss.

Three modes:
- EIGENSTATE: select n = 0..5; display static ψ_n(x) and static |ψ_n(x)|².
  The probability density panel must NOT animate. Classical turning points at
  ξ = ±√(2n+1) shown as vertical ticks.
- COHERENT STATE: select |α| (0..3) and arg(α) (0..2π); evolve and display
  |Ψ(x,t)|² sloshing at frequency ω. Mean <x>(t) traces a cosine; <p>(t)
  traces a sine.
- SUPERPOSITION: select n₁, n₂ (0..4) and coefficients (equal mix by default);
  display |Ψ(x,t)|² beating at frequency (E_{n₂}−E_{n₁})/ℏ = (n₂−n₁)·ω.

SAY.
Build `07-harmonic-oscillator.html`, a single self-contained HTML file.
D3 v7 from CDN. No other dependencies. Vanilla JS.

Layout: three panels in one SVG 1100 × 600.
- Panel A (left, 500px): wave function or Re Ψ plotted as a line.
  Behind it: parabolic V(x) as dashed curve; energy levels E_n as
  horizontal lines for n = 0..5; classical turning points for active n.
- Panel B (middle, 400px): |Ψ(x,t)|² as filled area.
- Panel C (right, 200px): phase-space inset — <x>(t) vs <p>(t), orbit
  traced as fading line, current position marked. For eigenstate: dot at
  origin. For coherent state: circle. For superposition: Lissajous.

Mode selector (three buttons) and sliders at top. Play/Pause/Reset below.
Natural units ℏ = m = 1. Spatial grid: 401 points on [−6, +6] in units
of √(ℏ/(mω)).

CONSTRAIN.
- Hermite polynomials by recursion; cap n ≤ 15; cache per frame.
- Eigenstates: STATIC. Verify |Ψ_n(x,t)|² has zero time dependence.
- Coherent state truncated at n_max = ceil(|α|² + 5√(|α|²)).
- Runtime checks to console every second:
  (i)  Σ|ψ_n(x_i)|² Δx = 1 within 0.001 for eigenstate.
  (ii) Σ|Ψ(x_i,t)|² Δx = 1 within 0.001 for coherent and superposition.
  (iii) For eigenstate, <x> and <p> within 0.01 of zero at all times.
- Plot parabolic potential in Panel A with range matching the turning
  points of the highest displayed level.
- Comments at every physics step.

VERIFY.
After writing:
(a) Eigenstate n=3 in Panel B: count 4 lobes in |ψ₃|² (n+1 lobes).
(b) Coherent state |α|=1, arg(α)=0 at t=0: <x>(0) = √2 in natural units.
    Verify within 1%.
(c) Superposition (n₁=0, n₂=1): beating at ω. Run for t = 2π/ω;
    density at t=2π/ω must match t=0. Verify period.
(d) Uncertainty product for n=0: σ_x · σ_p = 0.5 in natural units.
    Compute numerically and verify ≈ 0.500.
````

### Exploration tasks

**Task 1 — Eigenstates are frozen.** In Eigenstate mode, select $n = 0$. Press Play. Panel B does not change. Switch to Coherent state with $|\alpha| = 1$. Press Play. The packet oscillates. Record the period; verify it matches $T = 2\pi/\omega$.

**Task 2 — Climbing the ladder.** Step through $n = 0$ to $n = 5$. For each, count the lobes in $|\psi_n|^2$. Confirm the lobe count is always $n + 1$. Observe that $\sigma_x$ grows as $\sqrt{2n+1}$ — the wave function spreads as you go up the ladder.

**Task 3 — Coherent state orbit.** In Coherent state mode, set $|\alpha| = 0$. Panel C shows a dot at the origin — the coherent state is the ground state. Increase $|\alpha|$ to 1, 2, 3. The orbit in Panel C traces a circle of growing radius. At $|\alpha| = 3$, the amplitude is $\langle x\rangle_\text{max} = \sqrt{2}\cdot|\alpha| \approx 4.24$ in natural units. Verify.

**Task 4 — Superposition beating.** In Superposition mode, select $n_1 = 0, n_2 = 1$. Observe beating at $\omega$. Switch to $n_1 = 0, n_2 = 2$. Confirm beating at $2\omega$ (the level spacing is twice as large). Verify the general rule: beating frequency $(n_2 - n_1)\omega$.

**Task 5 — The parity surprise.** Select $n_1 = 0, n_2 = 2$. Both $\psi_0$ and $\psi_2$ are even-parity functions. Their cross term $\psi_0\psi_2$ is even in $x$, so $\langle x(t)\rangle = 0$ for all $t$ — the packet breathes rather than sloshes. Verify in Panel C: the orbit is a radial oscillation along the origin axis, not a circle. Write one sentence explaining why even-parity superpositions cannot have non-zero $\langle x\rangle$.

---

## References

- Griffiths, D.J., *Introduction to Quantum Mechanics*, 3rd ed., §2.3–2.4.
- Sakurai, J.J. and Napolitano, J., *Modern Quantum Mechanics*, 3rd ed., §2.3.
- Glauber, R.J., "The Quantum Theory of Optical Coherence," *Physical Review* **130**, 2529 (1963); "Coherent and Incoherent States of the Radiation Field," *Physical Review* **131**, 2766 (1963).
- Lamoreaux, S.K., "Demonstration of the Casimir Force in the 0.6 to 6 μm Range," *Physical Review Letters* **78**, 5 (1997).
- DLMF §18, National Institute of Standards and Technology. Hermite polynomials. https://dlmf.nist.gov/18

---

*Chapter 8 follows: the hydrogen atom. The Coulomb potential is not quadratic, so the harmonic oscillator algebra does not apply directly — but the method does. Angular momentum ladder operators will provide the quantum numbers $\ell$ and $m_\ell$; the radial equation provides the principal quantum number $n$. The spectrum $E_n = -13.6\ \text{eV}/n^2$ is the goal.*

---

## Running Project — Build the 1D Quantum Sandbox

**This chapter adds:** a second independent validation of the eigensolver — feed the tridiagonal Hamiltonian the quadratic potential $V_j = \tfrac12 m\omega^2 x_j^2$ and confirm it returns the equally spaced spectrum $E_n = (n+\tfrac12)\hbar\omega$, with the ground state Gaussian and $\sigma_x\sigma_p = \hbar/2$ — proving the solver is correct on a smooth potential, not just hard walls.

### Exercise R1 — When to Use AI
**The judgment:** In this chapter's project work, AI assistance is appropriate for:
- Writing the harmonic potential builder $V_j = \tfrac12 m\omega^2 x_j^2$ and feeding it to the existing eigensolver — *Why AI works here:* a one-line array fill into a module already validated by the golden test, with $E_n = (n+\tfrac12)\hbar\omega$ as the exact check.
- Drafting the level-spacing and $\sigma_x\sigma_p$ readouts — *Why AI works here:* simple reductions with exact targets (uniform spacing $\hbar\omega$; ground-state product exactly $\hbar/2$).
**The tell:** You are using AI well when you have an independent way to check the output — here, equal spacing $E_{n+1} - E_n = \hbar\omega$ and the Kennard-saturating ground state.

### Exercise R2 — When NOT to Use AI
**The judgment:** These tasks require your judgment; AI output here can't be trusted without redoing the work:
- Whether the grid is wide enough — at least $\pm 5x_0$ with $x_0 = \sqrt{\hbar/m\omega}$ — *Why AI fails here:* a grid that truncates the Gaussian tails pushes the eigenvalues slightly high and breaks the uniform spacing, but the spectrum still looks like a ladder; only checking the spacing against $\hbar\omega$ reveals it.
- Whether to validate against $(n+\tfrac12)\hbar\omega$ or accept "looks evenly spaced" — *Why AI fails here:* a half-quantum offset error (ground state at $\hbar\omega$ instead of $\hbar\omega/2$) is a physical-correctness call the AI may miss, since the *spacing* is unaffected.
**The tell:** If you could not explain the result without the AI — if the AI is your *reason* rather than your *tool* — it did work that should have been yours.
**Physics-judgment connection:** This trains checking a numerical spectrum against a different analytic ladder ($E_n = (n+\tfrac12)\hbar\omega$) and against a limiting/boundary condition (grid wide enough that the tails are not truncated).

### Exercise R3 — LLM Exercise
**What you're building this chapter:** the harmonic-oscillator validation of the eigensolver and the $\sigma_x\sigma_p$ ground-state check.
**Tool:** Claude chat — built on `hamiltonian.js` and `observables.js`; self-contained.
**The Prompt:**
```
Using the Chapter 0 CLAUDE.md, constants.js, grid.js, observables.js,
potentials.js, and hamiltonian.js as binding context, build
07-oscillator-validation.html.

Add to potentials.js: harmonic(x, m, omega) returns V_j = 0.5·m·omega²·x_j².
Feed it into buildTridiagonal, diagonalize, normalize eigenvectors to
Σ|ψ_j|² h = 1. Use a grid x ∈ [−x_max, +x_max] with x_max ≥ 6·x_0,
x_0 = √(ℏ/(mω)), and N = 600.

Display:
  - V(x) parabola (red), energy levels E_n (green), |ψ_n|² offset to E_n,
    for n = 0..6;
  - a TABLE: E_n numerical | E_n analytic (n+½)ℏω | spacing E_{n+1}−E_n vs ℏω;
  - σ_x, σ_p, and σ_x σ_p for the GROUND STATE (must read ℏ/2).

VALIDATE explicitly: level spacing uniform to within 1% of ℏω; ground-state
σ_x σ_p within 1% of ℏ/2; ground-state wave function Gaussian (no nodes).
If the spacing drifts at high n, tell me whether the grid is too narrow
(tails truncated) rather than nudging ω. Use m = m_e, ω = 1e14 rad/s.
```
**What this produces:** `07-oscillator-validation.html` and an extended `potentials.js`, demonstrating the eigensolver is correct on a smooth potential.
**How to adapt:** *Your system:* raise $x_\text{max}$ if high-$n$ spacing drifts. *ChatGPT/Gemini:* paste the dependency modules. *Claude Project:* the harmonic builder joins `potentials.js` in Project knowledge.
**Builds on:** the eigensolver and golden test from Chapter 5; the observables from Chapter 3.  **Next:** Chapter 8 adds time evolution so wave packets move in any $V(x)$.

### Exercise R4 — CLI Exercise
**What you're building this chapter:** an automated oscillator-spectrum test as a second eigensolver gate.
**Tool:** Claude Code — it can diagonalize the harmonic Hamiltonian and assert the ladder and uncertainty product.
**Skill level:** Advanced
**Setup — confirm:**
- [ ] `hamiltonian.js`, `potentials.js` (with `harmonic`), `observables.js`
- [ ] math.js available
- [ ] The Chapter 5 golden test already passing (the prerequisite gate)
**The Task:**
```
Read hamiltonian.js and potentials.js. Write a Node script
check-oscillator.js that builds the harmonic Hamiltonian (m = m_e,
ω = 1e14 rad/s, x_max = 6 x_0, N = 600), diagonalizes, normalizes
eigenvectors, and asserts:
  (1) E_0 = ½ℏω within 1% (the half-quantum, NOT ℏω);
  (2) spacing E_{n+1} − E_n = ℏω within 1% for n = 0..5;
  (3) ground-state σ_x σ_p within 1% of ℏ/2;
  (4) ground state has zero nodes (Gaussian).
Print the spacing table. If spacing drifts at high n, report whether widening
x_max fixes it (do this automatically and say so) — do NOT change ω.
Append to PROJECT.md under "Verified": "Ch7 oscillator: E_n=(n+½)ℏω ✓,
ground σ_xσ_p = <v>·(ℏ/2)".
```
**Expected output:** `check-oscillator.js`, a printed spacing table, an explicit PASS, and a `PROJECT.md` line.
**What to inspect:** the ground state at $\tfrac12\hbar\omega$ (not $\hbar\omega$), uniform spacing, and the $\sigma_x\sigma_p$ product landing on $\hbar/2$ — the same minimum-uncertainty signature the Gaussian gave in Chapter 3.
**If it goes wrong:** if the spacing is uniform but every level is offset, the half-quantum is mishandled — check $E_0$. If high-$n$ levels are systematically too high, the grid truncates the tails; widen $x_\text{max}$, do not retune $\omega$.
**CLAUDE.md / AGENTS.md note:** add: "The eigensolver must pass BOTH the infinite-well golden test (hard walls) AND the oscillator test (smooth potential, $E_n=(n+\tfrac12)\hbar\omega$) before any production spectrum is reported."

### Exercise R5 — AI Validation Exercise
**What you're validating:** the harmonic-oscillator spectrum and ground-state uncertainty from R3/R4.
**Validation type:** Numerical result
**Risk level:** Medium — a grid-truncation or half-quantum error is subtle and would undermine confidence in the solver on real (non-square) potentials.
**Setup:** use your own R3/R4 artifacts; ground truth is $E_n = (n+\tfrac12)\hbar\omega$.
**The Validation Task:** Evaluate against this checklist; mark Pass / Fail / Cannot determine with reasoning.
```
Validation Checklist — Harmonic oscillator eigensolver validation
□ Correctness: V_j = ½ m ω² x_j² fed into the SAME buildTridiagonal as the well?
□ Completeness: does it show both the spacing AND the ground-state σ_xσ_p?
□ Scope: is the grid ≥ ±5 x_0 so the tails are not truncated?
□ Physics criterion 1: E_0 = ½ℏω and spacing = ℏω within 1%?
□ Physics criterion 2: ground-state σ_x σ_p within 1% of ℏ/2 (Kennard saturated)?
□ Failure-mode check: any of —
  - half-quantum error (ground state at ℏω instead of ½ℏω)
  - grid too narrow (high-n eigenvalues too high, spacing drifts up)
  - eigenvectors unnormalized (σ_x σ_p off by a factor of h)
  - the AI quoting (n+½)ℏω instead of computing E_n from the matrix
```
**What to do with findings:** pass → use it as the second eigensolver gate; one fail → fix the grid width or normalization and re-run; multiple fails / cannot-determine → confirm by hand that $E_1 - E_0 = \hbar\omega$ for the lowest two computed levels.
**AI Use Disclosure (mandatory, two sentences):**
> *1:* The AI added the harmonic potential and ran it through the eigensolver, reporting the spectrum and ground-state uncertainty product.
> *2:* The AI could not determine whether the grid width was sufficient or the half-quantum was handled correctly — I verified $E_0 = \tfrac12\hbar\omega$, uniform spacing, and $\sigma_x\sigma_p = \hbar/2$ against the analytic results myself.
**Physics-judgment connection:** trains checking a numerical spectrum against a second analytic ladder and against a boundary condition (adequate grid width), proving the eigensolver is correct on a smooth potential and not just by coincidence on hard walls.
