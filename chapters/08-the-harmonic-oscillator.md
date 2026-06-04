# Chapter 7 — The Quantum Harmonic Oscillator

## TL;DR

- The harmonic oscillator hides inside every physical system near a stable equilibrium — from diatomic molecules to laser cavities to the vacuum of space.
- Factor the Hamiltonian into ladder operators $\hat{a}_\pm$; derive the entire spectrum $E_n = (n + \tfrac{1}{2})\hbar\omega$ from a single commutator $[\hat{a}_-, \hat{a}_+] = 1$, without solving any differential equation.
- The ground state has energy $\hbar\omega/2 \neq 0$; the uncertainty principle forbids it from sitting still.
- Energy eigenstates are frozen — they do not oscillate. Oscillation belongs to superpositions.
- The +1 simulation shows eigenstates frozen and coherent states sloshing, side by side.

---

## Learning Objectives

By the end of this chapter you will be able to:

1. **Derive** the ladder operators $\hat{a}_\pm$ from $[\hat{x},\hat{p}] = i\hbar$ and show that $[\hat{a}_-,\hat{a}_+] = 1$. *(Analyze — Bloom level 4)*
2. **Apply** the ladder commutator to derive the complete energy spectrum $E_n = (n + \tfrac{1}{2})\hbar\omega$ and explain why the ladder terminates downward. *(Apply — Bloom level 3)*
3. **Compute** expectation values $\langle x \rangle$, $\langle p \rangle$, $\langle x^2 \rangle$, $\langle p^2 \rangle$ algebraically using $\hat{a}_\pm$, without evaluating any integral. *(Apply — Bloom level 3)*
4. **Explain** why energy eigenstates of the oscillator are stationary — why classical oscillation emerges only in superpositions or coherent states — and identify this visually in a simulation. *(Understand — Bloom level 2)*
5. **Construct** a simulation showing eigenstates, coherent-state sloshing, and two-state interference, and verify the beating frequency matches $(E_{n_2} - E_{n_1})/\hbar$. *(Create — Bloom level 6)*

---

## Scene

In 1900, Max Planck was trying to fix a formula. The ultraviolet catastrophe — the prediction of classical statistical mechanics that a black body should radiate infinite power — was embarrassing. Planck found that if he assumed each cavity mode could only exchange energy in discrete chunks of size $\hbar\omega$, the formula worked. He called this a "mathematical trick" and did not believe the discreteness was real.

He was describing the quantum harmonic oscillator without knowing it.

Each electromagnetic mode of a cavity is a harmonic oscillator. The energy $E = (n + \tfrac{1}{2})\hbar\omega$ of that mode — with its equally spaced levels — is exactly what Planck was computing, minus the zero-point term he dropped. When Einstein and Debye later explained the specific heat of solids, they again used harmonic oscillators — phonons, quantized vibrations of a crystal lattice. When Dirac quantized the electromagnetic field in 1927, he again wrote down creation and annihilation operators $\hat{a}_+$ and $\hat{a}_-$, now for photons. When LIGO detected gravitational waves in 2015, the signal processing relied on squeezed states — non-classical states of the harmonic oscillator algebra applied to light.

One system, one algebra. The harmonic oscillator is not an example in quantum mechanics. It is quantum mechanics, in the simplest form that contains everything.

---

## Core Development

### Why Every Potential Is a Harmonic Oscillator (Near the Bottom)

Any smooth potential $V(x)$ with a minimum at $x = x_0$ can be Taylor-expanded:

$$V(x) = V(x_0) + V'(x_0)(x - x_0) + \frac{1}{2}V''(x_0)(x - x_0)^2 + \cdots$$

At a minimum, $V'(x_0) = 0$. For small oscillations, the cubic and higher terms are negligible. What remains is a constant (set to zero by redefining the energy zero) plus a quadratic:

$$V(x) \approx \frac{1}{2}V''(x_0)\,(x - x_0)^2 = \frac{1}{2}m\omega^2(x - x_0)^2$$

where $\omega = \sqrt{V''(x_0)/m}$ is the oscillation frequency determined by the curvature of $V$ at its minimum. Every stable equilibrium, for every system, for every potential, produces the same Hamiltonian. That universality is why solving the harmonic oscillator once solves infinitely many different physical problems.

The Hamiltonian is:

$$\hat{H} = \frac{\hat{p}^2}{2m} + \frac{1}{2}m\omega^2\hat{x}^2. \tag{7.1}$$

---

### The Trick: Factoring $\hat{H}$

Define two operators:

$$\hat{a}_\pm = \frac{1}{\sqrt{2\hbar m\omega}}\!\left(\mp i\hat{p} + m\omega\hat{x}\right). \tag{7.2}$$

These are called the **raising** ($\hat{a}_+$) and **lowering** ($\hat{a}_-$) operators. Compute the product $\hat{a}_-\hat{a}_+$:

$$\hat{a}_-\hat{a}_+ = \frac{1}{2\hbar m\omega}\!\left(i\hat{p} + m\omega\hat{x}\right)\!\left(-i\hat{p} + m\omega\hat{x}\right).$$

Expand. The $\hat{p}^2$ and $m^2\omega^2\hat{x}^2$ terms give $(\hat{p}^2 + m^2\omega^2\hat{x}^2)/(2\hbar m\omega) = \hat{H}/(\hbar\omega)$. The cross terms are $im\omega(\hat{p}\hat{x} - \hat{x}\hat{p}) = im\omega \cdot (-i\hbar) = m\omega\hbar$, which contributes $m\omega\hbar/(2\hbar m\omega) = 1/2$. So:

$$\hat{a}_-\hat{a}_+ = \frac{\hat{H}}{\hbar\omega} + \frac{1}{2}. \tag{7.3}$$

Equivalently, $\hat{H} = \hbar\omega(\hat{a}_-\hat{a}_+ - \tfrac{1}{2})$. By the same calculation with the order reversed, $\hat{a}_+\hat{a}_- = \hat{H}/(\hbar\omega) - \tfrac{1}{2}$, giving $\hat{H} = \hbar\omega(\hat{a}_+\hat{a}_- + \tfrac{1}{2})$.

Subtract the two orderings:

$$\boxed{[\hat{a}_-, \hat{a}_+] = 1.} \tag{7.4}$$

This is the algebraic content of the entire problem. Everything that follows — every energy level, every eigenstate relation, every expectation value — is a consequence of this one commutator. Memorize it. It will appear again in Chapter 10 (angular momentum ladder operators), in quantum field theory (creation and annihilation operators), and in the description of every boson in nature.

---

### Climbing the Ladder

Suppose $|n\rangle$ is an energy eigenstate with energy $E_n$: $\hat{H}|n\rangle = E_n|n\rangle$. Ask what energy $\hat{a}_+|n\rangle$ has.

From $[\hat{a}_-,\hat{a}_+] = 1$ and $\hat{H} = \hbar\omega(\hat{a}_+\hat{a}_- + \tfrac{1}{2})$, derive the commutators:

$$[\hat{H},\hat{a}_+] = \hbar\omega\,\hat{a}_+, \quad [\hat{H},\hat{a}_-] = -\hbar\omega\,\hat{a}_-.$$

(Verification: $[\hat{H},\hat{a}_+] = \hbar\omega[\hat{a}_+\hat{a}_-,\hat{a}_+] = \hbar\omega(\hat{a}_+[\hat{a}_-,\hat{a}_+]) = \hbar\omega\hat{a}_+$, using $[\hat{a}_+\hat{a}_-,\hat{a}_+] = \hat{a}_+[\hat{a}_-,\hat{a}_+] + [\hat{a}_+,\hat{a}_+]\hat{a}_- = \hat{a}_+$.)

Now compute $\hat{H}(\hat{a}_+|n\rangle)$:

$$\hat{H}(\hat{a}_+|n\rangle) = (\hat{a}_+\hat{H} + [\hat{H},\hat{a}_+])|n\rangle = \hat{a}_+(E_n|n\rangle) + \hbar\omega\,\hat{a}_+|n\rangle = (E_n + \hbar\omega)\,\hat{a}_+|n\rangle.$$

So $\hat{a}_+|n\rangle$ is an eigenstate with energy $E_n + \hbar\omega$. The operator $\hat{a}_+$ raises the energy by exactly $\hbar\omega$. By the same argument, $\hat{a}_-|n\rangle$ is an eigenstate with energy $E_n - \hbar\omega$. The operators form a ladder — apply $\hat{a}_+$ repeatedly to climb up one rung at a time, apply $\hat{a}_-$ to descend.

---

### Why the Ladder Terminates Downward: Zero-Point Energy

The Hamiltonian $\hat{H} = \hat{p}^2/(2m) + \tfrac{1}{2}m\omega^2\hat{x}^2$ is a sum of squares of Hermitian operators. Its expectation value in any state is non-negative:

$$\langle\hat{H}\rangle = \frac{\langle\hat{p}^2\rangle}{2m} + \frac{m\omega^2}{2}\langle\hat{x}^2\rangle \geq 0.$$

But $\hat{a}_-$ subtracts $\hbar\omega$ each time it is applied. The descent cannot continue forever without violating $\langle\hat{H}\rangle \geq 0$. The only resolution: there exists a lowest state $|0\rangle$ — the **ground state** — such that

$$\hat{a}_-|0\rangle = 0. \tag{7.5}$$

Applying $\hat{H} = \hbar\omega(\hat{a}_+\hat{a}_- + \tfrac{1}{2})$ to this state:

$$\hat{H}|0\rangle = \hbar\omega\!\left(\hat{a}_+\underbrace{(\hat{a}_-|0\rangle)}_{=\,0} + \frac{1}{2}|0\rangle\right) = \frac{1}{2}\hbar\omega\,|0\rangle.$$

The ground-state energy is

$$\boxed{E_0 = \frac{1}{2}\hbar\omega.} \tag{7.6}$$

This is the **zero-point energy**. It is not zero, and it cannot be made zero. The classical ground state would be a particle at rest at the bottom of the well — zero kinetic energy, zero potential energy, zero total energy. The quantum ground state cannot do this: the uncertainty principle $\sigma_x\sigma_p \geq \hbar/2$ demands that a state localized near $x = 0$ must have a spread in momentum, and hence non-zero kinetic energy. The zero-point energy is the price of confinement.

This is not a theoretical curiosity. Liquid helium does not solidify at atmospheric pressure at any temperature, because the zero-point kinetic energy of helium atoms ($m \approx 4$ u, confined to inter-atom spacing $\sim 3$ Å) exceeds the interatomic binding energy. The atoms cannot "settle down." The Casimir force between two conducting plates — an attractive force, measured by Lamoreaux in 1997 to within 5% of the predicted value — arises from the difference between the zero-point energies of electromagnetic modes in the presence and absence of the plates. Zero-point energy has an invoice you can read in the lab.

---

### The Complete Spectrum

From $|0\rangle$, apply $\hat{a}_+$ once: get $|1\rangle$ with energy $E_0 + \hbar\omega = \tfrac{3}{2}\hbar\omega$. Apply again: $|2\rangle$ with energy $\tfrac{5}{2}\hbar\omega$. The pattern is clear:

$$\boxed{E_n = \left(n + \frac{1}{2}\right)\hbar\omega, \quad n = 0, 1, 2, \ldots} \tag{7.7}$$

The spectrum is **equally spaced** with gap $\hbar\omega$. This equal spacing is not a coincidence — it is forced by the commutator $[\hat{a}_-,\hat{a}_+] = 1$, which makes the ladder uniform.

The physical signature: diatomic molecules vibrate near the bottom of their potential well, and their infrared spectra show sharp absorption lines at frequency $\omega$. For HCl, $\omega \approx 5.63 \times 10^{14}$ rad/s, giving $\hbar\omega \approx 0.37$ eV and an absorption wavelength of $\lambda \approx 3.4\ \mu$m. All adjacent vibrational levels are equally spaced; a photon can only drive a $\Delta n = \pm 1$ transition (selection rule from $\langle m|\hat{x}|n\rangle \propto \delta_{m,n\pm 1}$, derived below). The spectrum is a ruler in frequency space.

**Normalized ladder relations.** The states $|n\rangle$ are normalized: $\langle n|n\rangle = 1$. What is the normalization of $\hat{a}_+|n\rangle$? Compute:

$$\langle(\hat{a}_+|n\rangle),(\hat{a}_+|n\rangle)\rangle = \langle n|\hat{a}_-\hat{a}_+|n\rangle = \langle n|\!\left(\frac{\hat{H}}{\hbar\omega} + \frac{1}{2}\right)\!|n\rangle = \left(\frac{E_n}{\hbar\omega} + \frac{1}{2}\right) = n + 1.$$

So $\hat{a}_+|n\rangle$ has norm $\sqrt{n+1}$, and the normalized relation is:

$$\hat{a}_+|n\rangle = \sqrt{n+1}\,|n+1\rangle, \quad \hat{a}_-|n\rangle = \sqrt{n}\,|n-1\rangle. \tag{7.8}$$

Do not drop the $\sqrt{n+1}$ and $\sqrt{n}$ factors. They are essential for computing expectation values and for building coherent states. An implicit $\hat{a}_+|n\rangle = |n+1\rangle$ will give wrong answers.

---

### What the Eigenstates Look Like

Algebra gives the spectrum without touching a wave function. But it is worth seeing the eigenstates explicitly.

In position space, the condition $\hat{a}_-|0\rangle = 0$ becomes a differential equation. Substituting $\hat{p} = -i\hbar\,\partial_x$:

$$\frac{1}{\sqrt{2\hbar m\omega}}\!\left(\hbar\frac{\partial}{\partial x} + m\omega x\right)\psi_0(x) = 0.$$

Separate variables: $d\psi_0/\psi_0 = -(m\omega/\hbar)x\,dx$. Integrate and normalize:

$$\psi_0(x) = \left(\frac{m\omega}{\pi\hbar}\right)^{1/4}\exp\!\left(-\frac{m\omega x^2}{2\hbar}\right). \tag{7.9}$$

A Gaussian. The ground state of the harmonic oscillator is the same minimum-uncertainty Gaussian from Chapter 1: $\sigma_x\sigma_p = \hbar/2$ exactly, saturating the Kennard bound. This is not a coincidence — it will be shown below.

Higher states are generated by applying $\hat{a}_+$ to $\psi_0$. Each application multiplies the Gaussian by a polynomial one degree higher in $x$. Those polynomials are the **Hermite polynomials** $H_n(\xi)$ where $\xi = \sqrt{m\omega/\hbar}\,x$:

$$\psi_n(x) = \left(\frac{m\omega}{\pi\hbar}\right)^{1/4}\frac{1}{\sqrt{2^n n!}}\,H_n(\xi)\,e^{-\xi^2/2}, \tag{7.10}$$

with

$$H_0 = 1,\quad H_1 = 2\xi,\quad H_2 = 4\xi^2 - 2,\quad H_3 = 8\xi^3 - 12\xi,$$

and the recursion $H_{n+1}(\xi) = 2\xi H_n(\xi) - 2n H_{n-1}(\xi)$.

Two things to notice:

First, the $n$-th eigenstate has exactly $n$ nodes. The ground state has none. The first excited state has one. This is the same counting rule as the infinite square well.

Second, the probability density $|\psi_n(x)|^2$ behaves oppositely to the classical distribution for small $n$. A classical harmonic oscillator spends most of its time near the turning points (where it slows down) and least time at the bottom (where it moves fastest). The quantum ground state peaks at the bottom and falls off toward the turning points. Only at large $n$ — the correspondence principle regime — does $|\psi_n|^2$ averaged over a few oscillations converge to the classical distribution.

One more fact: roughly $16\%$ of the ground-state probability density lies outside the classical turning points $x = \pm\sqrt{\hbar/m\omega}$. Tunneling is not exotic; it is present in the very first eigenstate. The quantum harmonic oscillator tunnels into its own classically forbidden region by default.

---

### Expectation Values Without Integrals

Here is one of the great payoffs of the ladder approach. Express $\hat{x}$ and $\hat{p}$ in terms of $\hat{a}_\pm$:

$$\hat{x} = \sqrt{\frac{\hbar}{2m\omega}}\!\left(\hat{a}_+ + \hat{a}_-\right), \quad \hat{p} = i\sqrt{\frac{m\hbar\omega}{2}}\!\left(\hat{a}_+ - \hat{a}_-\right). \tag{7.11}$$

(These follow directly from the definition of $\hat{a}_\pm$ in equation (7.2).)

**$\langle x \rangle$ in an energy eigenstate:** $\hat{a}_+|n\rangle \propto |n+1\rangle$ and $\hat{a}_-|n\rangle \propto |n-1\rangle$, both orthogonal to $|n\rangle$:

$$\langle n|\hat{x}|n\rangle = \sqrt{\frac{\hbar}{2m\omega}}\!\left(\langle n|\hat{a}_+|n\rangle + \langle n|\hat{a}_-|n\rangle\right) = 0. \tag{7.12}$$

No integral evaluated. Same logic gives $\langle n|\hat{p}|n\rangle = 0$.

**$\langle x^2 \rangle$:** Write $\hat{x}^2 = (\hbar/2m\omega)(\hat{a}_+ + \hat{a}_-)^2$. Expand:

$$(\hat{a}_+ + \hat{a}_-)^2 = \hat{a}_+^2 + \hat{a}_-^2 + \hat{a}_+\hat{a}_- + \hat{a}_-\hat{a}_+.$$

The terms $\hat{a}_+^2|n\rangle \propto |n+2\rangle$ and $\hat{a}_-^2|n\rangle \propto |n-2\rangle$ are orthogonal to $|n\rangle$ and contribute nothing to the diagonal. The surviving terms are $\hat{a}_+\hat{a}_-$ (eigenvalue $n$) and $\hat{a}_-\hat{a}_+$ (eigenvalue $n+1$):

$$\langle n|\hat{x}^2|n\rangle = \frac{\hbar}{2m\omega}(n + n + 1) = \frac{\hbar(2n+1)}{2m\omega}. \tag{7.13}$$

Since $\langle x \rangle = 0$, this is also $\sigma_x^2$. Similarly, $\sigma_p^2 = (m\hbar\omega/2)(2n+1)$.

The uncertainty product:

$$\sigma_x\sigma_p = \sqrt{\frac{\hbar(2n+1)}{2m\omega}} \cdot \sqrt{\frac{m\hbar\omega(2n+1)}{2}} = \frac{(2n+1)\hbar}{2} = \left(n + \frac{1}{2}\right)\hbar. \tag{7.14}$$

For $n = 0$: $\sigma_x\sigma_p = \hbar/2$ — the minimum allowed by the Kennard inequality, saturated exactly. For $n \geq 1$, the product is $(n + \tfrac{1}{2})\hbar > \hbar/2$. The ground state is the unique eigenstate of the harmonic oscillator that saturates the uncertainty bound.

The off-diagonal matrix element: $\langle m|\hat{x}|n\rangle = \sqrt{\hbar/2m\omega}\,(\sqrt{n+1}\,\delta_{m,n+1} + \sqrt{n}\,\delta_{m,n-1})$. This is zero unless $m = n \pm 1$ — the selection rule for dipole transitions mentioned above.

---

### Eigenstates Do Not Oscillate

Here is the misconception that must be killed before the simulation is built.

A harmonic oscillator is, classically, an oscillator. You expect the quantum version to oscillate. But form the time-dependent eigenstate:

$$\Psi_n(x,t) = \psi_n(x)\,e^{-iE_n t/\hbar}.$$

The time dependence is a phase factor. Compute the probability density:

$$|\Psi_n(x,t)|^2 = |\psi_n(x)|^2 \cdot \underbrace{|e^{-iE_n t/\hbar}|^2}_{=\,1} = |\psi_n(x)|^2. \tag{7.15}$$

Static. The phase rotates in the complex plane at rate $E_n/\hbar$, but the probability density — everything you can measure with a position detector — does not change at all. An energy eigenstate sits still. If quantum mechanics contained only eigenstates, classical oscillation would never emerge.

This is not a flaw. It is a definition. Energy eigenstates are **stationary states**. The oscillation is a property of *superpositions*, where phase factors at different frequencies beat against each other.

Take the two-state superposition $|\Psi\rangle = (1/\sqrt{2})(|0\rangle + |1\rangle)$. The probability density is:

$$|\Psi(x,t)|^2 = \frac{1}{2}\!\left(|\psi_0|^2 + |\psi_1|^2\right) + \mathrm{Re}\!\left[\psi_0\psi_1^*\,e^{-i(E_0 - E_1)t/\hbar}\right].$$

The cross-term beats at frequency $(E_1 - E_0)/\hbar = \omega$ — exactly the classical oscillation frequency. The packet sloshes, but it also distorts: it is not a rigid Gaussian sliding back and forth, but a shape that deforms as it moves.

The simulation exercise for this chapter will show you an eigenstate and a superposition side by side. The eigenstate panel will be static; the superposition panel will slosh. If you see the eigenstate panel animating, there is a bug in the simulation.

---

### The Quantum State That Sloshes Cleanly: Coherent States

A **coherent state** $|\alpha\rangle$ is defined as an eigenstate of the lowering operator:

$$\hat{a}_-|\alpha\rangle = \alpha\,|\alpha\rangle \tag{7.16}$$

for any complex number $\alpha$. Coherent states are not energy eigenstates. They are superpositions of infinitely many $|n\rangle$ states, with Poisson-distributed photon numbers: the probability of finding $n$ quanta is

$$P(n) = e^{-|\alpha|^2}\frac{|\alpha|^{2n}}{n!}, \quad \langle n\rangle = |\alpha|^2. \tag{7.17}$$

The energy is uncertain, but the packet evolves cleanly. Under $\hat{H}$, a coherent state remains a coherent state:

$$\langle\hat{x}(t)\rangle = \sqrt{\frac{2\hbar}{m\omega}}\,|\alpha|\cos(\omega t - \arg\alpha), \quad \langle\hat{p}(t)\rangle = -\sqrt{2m\hbar\omega}\,|\alpha|\sin(\omega t - \arg\alpha). \tag{7.18}$$

Position and momentum oscillate sinusoidally at frequency $\omega$, just as a classical oscillator. And the wave packet keeps its shape: $\sigma_x\sigma_p = \hbar/2$ at all times. The coherent state is the minimum-uncertainty Gaussian packet riding its classical orbit indefinitely, without spreading.

In the energy basis:

$$|\alpha\rangle = e^{-|\alpha|^2/2}\sum_{n=0}^\infty \frac{\alpha^n}{\sqrt{n!}}\,|n\rangle. \tag{7.19}$$

For $|\alpha| = 0$: $|\alpha\rangle = |0\rangle$, the ground state. For $|\alpha| \to \infty$: a large amplitude oscillating close to the classical limit.

Roy Glauber introduced coherent states in their modern form in 1963, in the context of laser light. An ideal laser produces electromagnetic field modes in coherent states. The photon-count statistics of ideal laser light are Poisson — not because lasers are classical, but because Poisson is the photon-number distribution of a coherent state. Glauber received the Nobel Prize in 2005 for this connection. The harmonic oscillator algebra is not a metaphor for laser physics; it is laser physics.

---

### Where the Ladder Leads

Before the simulation, step back and see what this chapter has built.

One commutator: $[\hat{a}_-,\hat{a}_+] = 1$. From it: a complete, equally spaced spectrum. From the spectrum: selection rules, zero-point energy, coherent states, uncertainty products. From the definition $\hat{a}_-|0\rangle = 0$: the ground-state wave function.

The method — factor the Hamiltonian into a pair of operators whose commutator is a scalar, then use that commutator to derive everything algebraically — is not specific to this problem. In Chapter 10, the angular momentum operators $\hat{L}_\pm$ obey $[\hat{L}_-,\hat{L}_+] = -2\hbar\hat{L}_z$, a different algebra but the same logic. In quantum field theory, $\hat{a}_+$ becomes a creation operator that adds one particle to the vacuum; $\hat{a}_-$ is the annihilation operator. The vacuum $|0\rangle$ is the state that $\hat{a}_-$ kills. A state of $n$ photons is $(\hat{a}_+)^n/\sqrt{n!}$ applied to the vacuum. The commutator $[\hat{a},\hat{a}^\dagger] = 1$ is the first line of quantum electrodynamics.

This chapter is the template for all of that.

---

## Worked Example: Ladder Operator Action on $|n\rangle$

**The lesson.** Use the normalized ladder relations to compute the action of $\hat{a}_+$ on $|n\rangle$, verify the normalization, and then use $\hat{a}_\pm$ to evaluate $\langle n|\hat{x}^2|n\rangle$ without any integral.

**Part A: $\hat{a}_+$ action and normalization.**

Given the normalized relation $\hat{a}_+|n\rangle = \sqrt{n+1}\,|n+1\rangle$, apply $\hat{a}_-$ to recover:

$$\hat{a}_-\!\left(\hat{a}_+|n\rangle\right) = \hat{a}_-\!\left(\sqrt{n+1}\,|n+1\rangle\right) = \sqrt{n+1} \cdot \sqrt{n+1}\,|n\rangle = (n+1)|n\rangle.$$

Also from equation (7.3): $\hat{a}_-\hat{a}_+ = \hat{H}/(\hbar\omega) + \tfrac{1}{2}$, so $\hat{a}_-\hat{a}_+|n\rangle = (E_n/\hbar\omega + \tfrac{1}{2})|n\rangle = (n + \tfrac{1}{2} + \tfrac{1}{2})|n\rangle = (n+1)|n\rangle$. Consistent. $\checkmark$

Confirm normalization: $\langle \hat{a}_+|n\rangle, \hat{a}_+|n\rangle \rangle = \langle n|\hat{a}_-\hat{a}_+|n\rangle = n+1$, so the norm is $\sqrt{n+1}$, and dividing out gives the unit-normalized state $|n+1\rangle$. Exactly as claimed in (7.8).

**Part B: $\langle n|\hat{x}^2|n\rangle$ by pure algebra.**

Write $\hat{x} = \ell(\hat{a}_+ + \hat{a}_-)$ where $\ell = \sqrt{\hbar/2m\omega}$ is the oscillator length. Then:

$$\hat{x}^2 = \ell^2(\hat{a}_+ + \hat{a}_-)^2 = \ell^2(\hat{a}_+^2 + \hat{a}_+\hat{a}_- + \hat{a}_-\hat{a}_+ + \hat{a}_-^2).$$

Evaluate each term between $\langle n|$ and $|n\rangle$:
- $\langle n|\hat{a}_+^2|n\rangle = \sqrt{n+1}\sqrt{n+2}\langle n|n+2\rangle = 0$ (orthogonality).
- $\langle n|\hat{a}_-^2|n\rangle = \sqrt{n}\sqrt{n-1}\langle n|n-2\rangle = 0$.
- $\langle n|\hat{a}_+\hat{a}_-|n\rangle = \langle n|\hat{n}|n\rangle = n$.
- $\langle n|\hat{a}_-\hat{a}_+|n\rangle = \langle n|(n+1)|n\rangle = n+1$.

Sum: $\langle n|\hat{x}^2|n\rangle = \ell^2(n + n + 1) = \ell^2(2n+1) = \hbar(2n+1)/(2m\omega)$.

This is the result stated in equation (7.13), obtained without evaluating a single Gaussian integral.

**Part C: Application to HCl.**

For HCl with $\omega \approx 5.63 \times 10^{14}$ rad/s and reduced mass $\mu \approx 1.63 \times 10^{-27}$ kg:

- Zero-point energy: $E_0 = \tfrac{1}{2}\hbar\omega = \tfrac{1}{2} \times 1.055 \times 10^{-34} \times 5.63 \times 10^{14} \approx 2.97 \times 10^{-20}$ J $\approx 0.185$ eV.
- Level spacing: $\hbar\omega \approx 0.37$ eV.
- Thermal energy at 300 K: $k_BT \approx 0.025$ eV.

Since $k_BT \ll \hbar\omega$, essentially all HCl molecules are in the vibrational ground state at room temperature. The infrared absorption spectrum shows the $n = 0 \to 1$ transition at $\lambda = hc/(\hbar\omega) \approx 3.4\ \mu$m — exactly what is observed.

**The limit.** Dropping the $\sqrt{n+1}$ factors in the ladder relations is a common error that seems harmless until you compute something. For instance, $\langle n|\hat{x}^2|n\rangle = \ell^2(2n+1)$ — but if you mistakenly write $\hat{a}_+|n\rangle = |n+1\rangle$ (no prefactor), you compute $\langle n|\hat{a}_-\hat{a}_+|n\rangle = \langle n|n\rangle = 1$ for the $\hat{a}_-\hat{a}_+$ term instead of $n+1$, giving $\langle\hat{x}^2\rangle = \ell^2 \cdot 2$ regardless of $n$ — which is wrong for every $n \neq \tfrac{1}{2}$ and predicts no zero-point energy in the uncertainty product. The prefactors are not decorative.

---

## Common Misconceptions

**"The quantum harmonic oscillator oscillates."** No. Energy eigenstates are stationary: $|\Psi_n(x,t)|^2 = |\psi_n(x)|^2$, independent of time. The probability density does not move. What oscillates is the phase of the wave function — not anything you can measure with a position detector. Classical oscillation emerges only in superpositions of eigenstates. If you hear someone say "the particle is oscillating in the $n = 1$ state," they are wrong.

**"$\hat{a}_+|n\rangle = |n+1\rangle$."** Missing the $\sqrt{n+1}$ prefactor. The correct relation is $\hat{a}_+|n\rangle = \sqrt{n+1}\,|n+1\rangle$. The error propagates into every expectation value that uses $\hat{a}_\pm$.

**"Zero-point energy comes from $\Delta E \cdot \Delta t \geq \hbar/2$."** No. It comes from the Kennard inequality $\sigma_x\sigma_p \geq \hbar/2$. The time-energy relation is a separate statement with different content and a different proof. Confusing them is one of the most persistent errors in popular quantum mechanics.

**"The HO ground state is the same Gaussian as the free-particle wave packet."** They look identical — both are $\exp(-\text{const} \times x^2)$ — but they are physically different objects. The free-particle Gaussian from Chapter 1 is not an energy eigenstate; it spreads over time. The harmonic-oscillator ground state is an energy eigenstate; it stays a Gaussian forever (under the HO Hamiltonian). The difference is the potential $V(x)$ acting as a restoring force that prevents spreading.

**"The correspondence principle says quantum mechanics becomes classical at large $n$."** More precisely: at large $n$, the *averaged* quantum probability density converges to the classical distribution. Pointwise, $|\psi_n|^2$ still oscillates $n$ times across the well. The correspondence principle operates on averages, not on the wave function itself.

---

## Exercises

**Warm-up**

1. *[Tests: commutator algebra, ladder operator definitions]* Starting from $[\hat{x},\hat{p}] = i\hbar$ and the definitions $\hat{a}_\pm = (1/\sqrt{2\hbar m\omega})(\mp i\hat{p} + m\omega\hat{x})$, verify $[\hat{a}_-,\hat{a}_+] = 1$ by explicit calculation. Show every step. *Difficulty: warm-up.*

2. *[Tests: Hermite polynomial recursion, node counting]* Using $H_{n+1}(\xi) = 2\xi H_n(\xi) - 2n H_{n-1}(\xi)$ with $H_0 = 1$, $H_1 = 2\xi$, compute $H_2$, $H_3$, and $H_4$. For each, find all real roots and verify the count matches $n$. *Difficulty: warm-up.*

3. *[Tests: stationary state, time evolution]* Write $|\Psi_n(x,t)|^2$ for the harmonic oscillator eigenstate and show algebraically that it is independent of $t$. Then write one sentence explaining what "stationary state" means physically — not mathematically. *Difficulty: warm-up.*

**Application**

4. *[Tests: zero-point energy, level spacing, room-temperature occupancy]* Nitrogen N$_2$ has vibrational frequency $\omega \approx 4.45 \times 10^{14}$ rad/s and reduced mass $\mu \approx 1.16 \times 10^{-26}$ kg. (a) Compute $E_0 = \hbar\omega/2$ in eV. (b) Compare to $k_BT$ at 300 K. (c) What fraction of N$_2$ molecules are in the vibrational ground state at room temperature? (Use the Boltzmann factor $e^{-\hbar\omega/k_BT}$ for the excited-state population.) *Difficulty: application.*

5. *[Tests: ladder algebra for expectation values, selection rules]* Using $\hat{x} = \sqrt{\hbar/2m\omega}(\hat{a}_+ + \hat{a}_-)$ and the normalized relations (7.8): (a) Compute $\langle m|\hat{x}|n\rangle$ for general $m, n$. For which values of $m - n$ is this non-zero? (b) Compute $\langle n|\hat{x}^3|n\rangle$ without integrals. (Hint: expand $(\hat{a}_+ + \hat{a}_-)^3$ and use orthogonality.) *Difficulty: application.*

6. *[Tests: coherent state, Poisson distribution, eigenvalue of $\hat{a}_-$]* For the coherent state $|\alpha\rangle = e^{-|\alpha|^2/2}\sum_n (\alpha^n/\sqrt{n!})|n\rangle$: (a) Verify directly that $\hat{a}_-|\alpha\rangle = \alpha|\alpha\rangle$ by substituting the expansion and using (7.8). (b) Compute $\langle\hat{n}\rangle = \langle\alpha|\hat{a}_+\hat{a}_-|\alpha\rangle$ and show it equals $|\alpha|^2$. (c) Show the photon-number variance equals $|\alpha|^2$ — the Poisson signature. *Difficulty: application.*

7. *[Tests: uncertainty product for eigenstates]* (a) Using equations (7.13) and its momentum analogue, compute $\sigma_x\sigma_p$ for $n = 0, 1, 2, 5$. (b) At which $n$ is the Kennard inequality saturated? (c) As $n \to \infty$, $\sigma_x\sigma_p \to n\hbar$. Does the uncertainty bound become less restrictive for large $n$? Explain. *Difficulty: application.*

**Synthesis**

8. *[Tests: tunneling fraction, position-space integrals from ladder algebra]* The classical turning points for the ground state are $x = \pm x_0$ where $x_0 = \sqrt{\hbar/m\omega}$. (a) Using the explicit ground-state wave function (7.9), compute the probability that the particle is found outside $[-x_0, x_0]$. Express as $1 - \mathrm{erf}(1)$. (b) Evaluate numerically and verify the "~16%" claim in the text. (c) Compute $x_0$ in nm for HCl and compare to the bond length (~0.13 nm). *Difficulty: synthesis.*

9. *[Tests: superposition, beating frequency, parity argument]* Consider the superposition $|\Psi\rangle = (|0\rangle + |2\rangle)/\sqrt{2}$. (a) Write down $|\Psi(x,t)|^2$ and identify the beating frequency. (b) Is the beating frequency $\omega$ or $2\omega$? (c) At $t = \pi/\omega$, what is $|\Psi(x,t)|^2$? Compare to the initial $|\Psi(x,0)|^2$. (d) By a parity argument, explain why $\langle\hat{x}(t)\rangle = 0$ for all $t$ in this superposition, even though the probability density oscillates. *Difficulty: synthesis.*

**Challenge**

10. *[Tests: coherent state time evolution, connection to classical mechanics]* Show that the coherent state $|\alpha\rangle$ evolved under $\hat{H}$ for time $t$ gives $e^{-i\omega t/2}|\alpha e^{-i\omega t}\rangle$ — a coherent state with amplitude rotated by $-\omega t$ in the complex plane, up to a global phase. (Hint: expand $|\alpha\rangle$ in the energy basis and act with $e^{-i\hat{H}t/\hbar}$.) Use this to derive equations (7.18) for $\langle\hat{x}(t)\rangle$ and $\langle\hat{p}(t)\rangle$. *Difficulty: challenge.*

---

## Still Puzzling

The Casimir effect computes a *difference* of zero-point energies — with plates minus without — and the result is finite and measurable. The machinery works.

Now apply the same harmonic-oscillator algebra to every mode of every quantum field, up to the Planck scale ($E_\text{Planck} \approx 10^{19}$ GeV). Sum the zero-point energies. The result is $\sim 10^{120}$ times larger than the observed cosmological constant. This is the largest quantitative discrepancy between a theoretical prediction and an experimental measurement in the history of physics.

Nobody knows how to fix it. The same algebra that gives you the Casimir force and the infrared spectrum of HCl gives you this catastrophic prediction when applied naively to all field modes. The cure presumably involves a cancellation mechanism (supersymmetry, for instance, pairs bosons and fermions whose zero-point energies cancel) or a breakdown of the effective field theory description at some scale far below the Planck energy. Whether either of those actually resolves the problem is unknown.

The honest statement: the harmonic oscillator is one of the most successful models in all of physics, and one of the places where scaling it up naively gives a result that is wrong by 120 orders of magnitude. Carrying both of those facts simultaneously is part of doing physics.

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
(a) Eigenstate n=3 in Panel B: count 3 visible peaks in |ψ₃|². Confirm
    4 peaks (n+1 lobes, but boundary behavior means 3 interior peaks).
    Actually: |ψ_3|² has 4 lobes (n+1). Confirm.
(b) Coherent state |α|=1, arg(α)=0 at t=0: <x>(0) = √(2ℏ/mω) = √2
    in natural units. Verify within 1%.
(c) Superposition (n₁=0, n₂=1): beating at ω. Run for t = 2π/ω;
    the density at t=2π/ω must match t=0. Verify period.
(d) Uncertainty product for n=0: σ_x · σ_p = ℏ/2 = 0.5 in natural units.
    Compute numerically and verify ≈ 0.500.
````

### Exploration tasks

**Task 1 — Eigenstates are frozen.** In Eigenstate mode, select $n = 0$. Press Play. The Panel B display does not change. Now switch to Coherent state with $|\alpha| = 1$. Press Play. The packet oscillates. Record the period; verify it matches $T = 2\pi/\omega$.

**Task 2 — Climbing the ladder.** In Eigenstate mode, step through $n = 0$ to $n = 5$. For each, count the lobes in $|\psi_n|^2$ (Panel B). Confirm the lobe count is always $n + 1$. Also observe that $\sigma_x$ grows as $\sqrt{2n+1}$ — the wave function spreads as you go up the ladder.

**Task 3 — Coherent state orbit.** In Coherent state mode, set $|\alpha| = 0$. The Phase-space panel shows a dot at the origin. Increase $|\alpha|$ to 1, then 2, then 3. The orbit in Panel C traces a circle of growing radius. At $|\alpha| = 0$, the coherent state is the ground state: a dot, not a circle. At $|\alpha| = 3$, the orbit amplitude in $x$ is $\langle x\rangle_\text{max} = \sqrt{2\hbar/m\omega} \cdot |\alpha| = \sqrt{2} \cdot 3 \approx 4.24$ in natural units. Verify.

**Task 4 — Superposition beating.** In Superposition mode, select $n_1 = 0, n_2 = 1$ (equal mix). Observe beating at $\omega$. Switch to $n_1 = 0, n_2 = 2$. Does it still beat? At what frequency? Compare to the general rule: beating at $(n_2 - n_1)\omega$.

**Task 5 — The $n_1 = 0, n_2 = 2$ symmetry surprise.** Select $n_1 = 0, n_2 = 2$. Both $\psi_0$ and $\psi_2$ are even-parity functions. Their cross term $\psi_0\psi_2$ is even in $x$. Therefore $\langle x(t)\rangle = 0$ for all $t$ — the packet does not drift, it "breathes." Verify in Panel C: the phase-space orbit is a radial oscillation (dot oscillating along the origin axis) rather than a circle. Write one sentence explaining why parity forbids a non-zero $\langle x\rangle$.

---

## References

- Griffiths, D. J., *Introduction to Quantum Mechanics*, 3rd ed., §2.3–2.4. Canonical undergraduate source; notation follows this text. `[verify]`
- Sakurai, J. J. and Napolitano, J., *Modern Quantum Mechanics*, 3rd ed., §2.3. Same method, slightly more formal operator language.
- Glauber, R. J., "The Quantum Theory of Optical Coherence," *Physical Review* **130**, 2529 (1963); "Coherent and Incoherent States of the Radiation Field," *Physical Review* **131**, 2766 (1963). Original coherent state papers; Nobel Prize 2005. `[verify — confirm journal volumes and page numbers]`
- Lamoreaux, S. K., "Demonstration of the Casimir Force in the 0.6 to 6 μm Range," *Physical Review Letters* **78**, 5 (1997). First ~5% measurement of the Casimir force — direct consequence of zero-point energy.
- DLMF §18 (Digital Library of Mathematical Functions), National Institute of Standards and Technology. Hermite polynomials — authoritative reference for recursion and normalization. https://dlmf.nist.gov/18
- _lib_qmsri-03-the-harmonic-oscillator.md (local pantry, primary source for this chapter). Rich draft covering ladder operators through coherent states and simulation spec; all major sections adapted from this source.
- Bohm, D., *Quantum Theory* (1951), Ch. 13. Early treatment of the harmonic oscillator with clear physical discussion of zero-point energy.
