# Chapter 8 — The Free Particle and Wave Packets

## TL;DR

- A single plane wave $e^{i(kx - \omega t)}$ cannot be normalized — a particle with perfectly sharp momentum is completely delocalized.
- Superposing a range of plane waves via Fourier transform produces a normalizable, localized wave packet.
- The packet's *envelope* moves at the group velocity $v_g = d\omega/dk = \hbar k_0/m$, which equals the classical particle velocity; the internal oscillations move at the phase velocity $v_{ph} = \omega/k_0 = \hbar k_0/2m$, exactly half as fast.
- Dispersion ($d^2\omega/dk^2 \neq 0$) causes the packet to spread; the Gaussian packet's width grows as $\sigma_x(t) = \sqrt{\sigma_0^2 + (\hbar t / 2m\sigma_0)^2}$.
- The +1 simulation assembles a Gaussian wave packet from its Fourier components and shows propagation, spreading, and the carrier oscillation moving at twice the envelope speed.

---

## Learning Objectives

By the end of this chapter you can:

1. **Explain** (Understand) why the free-particle plane wave $e^{ikx}$ cannot be normalized, and connect this to the uncertainty principle. [Bloom: Understand]
2. **Construct** (Apply) a normalizable wave packet by Fourier superposition, and compute $\phi(k)$ given $\Psi(x, 0)$. [Bloom: Apply]
3. **Derive** (Analyze) the phase velocity $v_{ph} = \omega/k$ and group velocity $v_g = d\omega/dk$ for the free-particle dispersion relation, and show $v_g = 2\,v_{ph}$. [Bloom: Analyze]
4. **Apply** (Apply) the Gaussian spreading formula to compute how long it takes a packet of given initial width to spread to a specified larger width. [Bloom: Apply]
5. **Predict and check** (Evaluate) the time evolution of a simulated wave packet, verifying that $\sigma_p$ is constant while $\sigma_x$ grows, and that the ratio $\sigma_x(t)\sigma_p/(\hbar/2)$ exceeds $1$ for $t > 0$. [Bloom: Evaluate]

---

## Opening: The Embarrassment of the Plane Wave

Set up the free-particle Schrödinger equation. There is no potential anywhere, just a particle in empty space. You separate variables and find stationary states. The mathematics is almost too easy — a second-order ODE with constant coefficients:

$$-\frac{\hbar^2}{2m}\frac{d^2\psi}{dx^2} = E\psi,$$

and the solutions are $\psi_k(x) = A e^{ikx}$ with $E = \hbar^2 k^2/2m$ for any real $k$. Elegant. Every value of $k$ is allowed. Every momentum $p = \hbar k$ is a valid solution. The time-dependent version:

$$\Psi_k(x, t) = A\,e^{i(kx - \omega t)}, \qquad \omega = \frac{\hbar k^2}{2m}.$$

Now try to normalize it. Compute $|\Psi_k|^2$:

$$|\Psi_k|^2 = |A|^2.$$

Constant. Everywhere. Independent of $x$ and $t$. The probability density is the same at $x = 0$ and at $x = 10^{10}$ light-years. Integrate over all space:

$$\int_{-\infty}^{\infty} |A|^2\,dx = |A|^2 \cdot \infty.$$

This diverges for any non-zero $A$. The plane wave $e^{ikx}$ cannot be normalized on $(-\infty, \infty)$. A free particle with perfectly sharp momentum $p = \hbar k$ and perfectly sharp energy $E = \hbar^2 k^2/2m$ is everywhere at once.

This is not a mathematical accident. Look at the uncertainty principle: $\sigma_x \sigma_p \geq \hbar/2$. If $\sigma_p = 0$ — perfectly sharp momentum — then $\sigma_x = \infty$. The particle is maximally delocalized. Non-normalizability is the mathematical form of infinite position uncertainty.

So what do we do? We build something that can be normalized, by superposing many plane waves with *nearby* momenta. That superposition is a **wave packet**, and it is the physically realizable free particle.

---

## Core Development

### The Wave Packet by Fourier Superposition

The most general solution to the free-particle Schrödinger equation is not a single plane wave but a superposition of all of them:

$$\Psi(x, t) = \frac{1}{\sqrt{2\pi}}\int_{-\infty}^{\infty} \phi(k)\,e^{i(kx - \omega(k)t)}\,dk, \qquad \omega(k) = \frac{\hbar k^2}{2m}.$$

The function $\phi(k)$ is the **Fourier amplitude**, also called the **momentum-space wave function**. It tells you how much of each plane wave $e^{ikx}$ goes into the superposition. The factor $1/\sqrt{2\pi}$ keeps the normalization consistent.

At $t = 0$, this is just the Fourier transform relationship:

$$\Psi(x, 0) = \frac{1}{\sqrt{2\pi}}\int_{-\infty}^{\infty} \phi(k)\,e^{ikx}\,dk, \qquad \phi(k) = \frac{1}{\sqrt{2\pi}}\int_{-\infty}^{\infty} \Psi(x, 0)\,e^{-ikx}\,dx.$$

Given any initial wave function $\Psi(x, 0)$, you compute $\phi(k)$ by Fourier transform, then time-evolve by attaching the phase factor $e^{-i\omega(k)t}$. The free-particle time evolution is exact.

The physics of $\phi(k)$: by the Born rule applied in momentum space, $|\phi(k)|^2\,dk$ is the probability that a momentum measurement returns a value between $\hbar k$ and $\hbar(k + dk)$. The momentum distribution is determined entirely by $\phi(k)$ and does not change with time — $\phi(k)$ acquires a phase $e^{-i\omega(k)t}$ but $|\phi(k)|^2$ is time-independent.

**Why is the packet normalizable?** If $\phi(k)$ is localized near $k_0$ with spread $\Delta k$, the Fourier transform theorem guarantees that $\Psi(x, 0)$ is localized near $x_0$ with spread $\Delta x \sim 1/\Delta k$. A localized function is normalizable. The superposition turns the un-normalizable plane waves into a normalizable packet by allowing them to interfere constructively in one region and destructively everywhere else.

### Phase Velocity and Group Velocity

A single plane wave $e^{i(kx - \omega t)}$ has a fixed-phase surface — a crest — at $kx - \omega t = \text{const}$. That surface moves at

$$v_{ph} = \frac{\omega}{k}.$$

This is the **phase velocity**: the speed of the wavefronts. For a free non-relativistic particle with $\omega = \hbar k^2/2m$:

$$v_{ph} = \frac{\hbar k}{2m} = \frac{p}{2m}.$$

Compare to the classical velocity $v_{cl} = p/m$. The phase velocity is *half* the classical velocity. This is already surprising — the "wave" is slower than the particle it supposedly describes.

But the particle is not the crest of a single wave. The particle is the *envelope* of the wave packet. To find how the envelope moves, consider a wave packet peaked at $k_0$ with a narrow distribution $\phi(k)$. The integral

$$\Psi(x, t) = \frac{1}{\sqrt{2\pi}}\int \phi(k)\,e^{i(kx - \omega(k)t)}\,dk$$

is dominated by $k$ near $k_0$. Taylor-expand $\omega(k)$ around $k_0$:

$$\omega(k) = \omega_0 + \omega'_0(k - k_0) + \tfrac{1}{2}\omega''_0(k-k_0)^2 + \cdots$$

where $\omega_0 = \omega(k_0)$, $\omega'_0 = d\omega/dk|_{k_0}$, $\omega''_0 = d^2\omega/dk^2|_{k_0}$. Substitute:

$$\Psi(x, t) \approx \frac{e^{i(k_0 x - \omega_0 t)}}{\sqrt{2\pi}}\int \phi(k)\,e^{i(k-k_0)(x - \omega'_0 t)}\,e^{-\frac{i}{2}\omega''_0(k-k_0)^2 t}\,dk.$$

The first exponential is a carrier wave oscillating at $(k_0, \omega_0)$ — it moves at $v_{ph} = \omega_0/k_0$. The integral over the rest is the *envelope function*, evaluated at the shifted argument $x - \omega'_0 t$. At $t = 0$ the envelope is centered at $x = 0$; at time $t$ it is centered at $x = \omega'_0 t$. The envelope moves at the **group velocity**:

$$\boxed{v_g = \frac{d\omega}{dk}\bigg|_{k_0}.}$$

For the free particle, $\omega = \hbar k^2/2m$, so $d\omega/dk = \hbar k/m$, and:

$$v_g = \frac{\hbar k_0}{m} = \frac{p_0}{m}.$$

This is the classical particle velocity. Good — the packet's center of mass moves like a classical particle.

**The ratio.** For the free particle:

$$\frac{v_g}{v_{ph}} = \frac{\hbar k_0/m}{\hbar k_0/2m} = 2.$$

The group velocity is exactly twice the phase velocity. This means: if you watch a wave packet in the simulation, the internal oscillations (the carrier wave) travel at $v_{ph}$, while the envelope (the blob of probability) travels at $2v_{ph}$. You can see individual wave crests moving through the packet, entering from behind and emerging at the front. This is counterintuitive and real.

The phase velocity has no direct physical meaning for particle motion; it is the speed of the phase front of the carrier. The group velocity is the physically meaningful speed — it is where you find the particle, and it matches classical mechanics.

### Dispersion and Wave Packet Spreading

If $\omega(k)$ were exactly linear in $k$ — say $\omega = v_g k$ — then the envelope would move without distortion: every Fourier component moves at the same speed. That is the non-dispersive case (light in vacuum, $\omega = ck$, is an example).

For the free particle, $\omega = \hbar k^2/2m$ is quadratic. The second derivative $\omega'' = d^2\omega/dk^2 = \hbar/m \neq 0$. Different Fourier components travel at slightly different group velocities (higher $k$ components move faster). Over time they drift apart and the packet spreads.

The spreading can be computed exactly for a Gaussian initial condition. Take

$$\Psi(x, 0) = \left(\frac{1}{\pi\sigma_0^2}\right)^{1/4} \exp\!\left(-\frac{x^2}{2\sigma_0^2}\right) \exp(ik_0 x),$$

a Gaussian with position-space width $\sigma_0$ and mean wavenumber $k_0$. Its Fourier transform is

$$\phi(k) = \left(\frac{\sigma_0^2}{\pi}\right)^{1/4} \exp\!\left(-\frac{\sigma_0^2(k-k_0)^2}{2}\right),$$

also Gaussian with width $\Delta k = 1/(2\sigma_0)$ in $k$-space (saturating the uncertainty principle at $t = 0$: $\sigma_x\sigma_p = \sigma_0 \cdot \hbar/(2\sigma_0) \cdot \sqrt{2}/\sqrt{2} = \hbar/2$).

Attach the time-evolution phase $e^{-i\omega(k)t}$ and perform the Gaussian integral exactly by completing the square. The result is:

$$|\Psi(x, t)|^2 = \frac{1}{\sigma(t)\sqrt{\pi}}\exp\!\left(-\frac{(x - v_g t)^2}{\sigma(t)^2}\right),$$

where

$$\boxed{\sigma(t) = \sigma_0\sqrt{1 + \left(\frac{\hbar t}{2m\sigma_0^2}\right)^2}.}$$

Equivalently, in terms of the position-space standard deviation $\sigma_x(t) = \sigma(t)/\sqrt{2}$:

$$\sigma_x(t)^2 = \sigma_x(0)^2 + \left(\frac{\hbar t}{2m\sigma_x(0)}\right)^2.$$

Several things are worth noting:

1. **The center moves classically.** $|\Psi|^2$ is a Gaussian centered at $x = v_g t = (\hbar k_0/m)t$. The expectation value of position follows Newton's first law.

2. **The momentum distribution does not change.** $|\phi(k)|^2$ is time-independent. $\sigma_p = \hbar\Delta k = \hbar/(2\sigma_0)$ is constant. Only the position distribution spreads.

3. **The spreading is dispersion, not the uncertainty principle.** The uncertainty principle says $\sigma_x\sigma_p \geq \hbar/2$ at every instant. It says nothing about whether $\sigma_x$ must grow. Spreading happens because $d^2\omega/dk^2 \neq 0$. A light pulse in vacuum ($d^2\omega/dk^2 = 0$) does not spread at all. The harmonic oscillator coherent state (Chapter 7) does not spread even though $d^2\omega/dk^2 \neq 0$ there — the restoring potential cancels the dispersion. For the free particle, there is no restoring force, so the spreading is unavoidable.

4. **The packet ceases to be a minimum-uncertainty state.** At $t = 0$, $\sigma_x\sigma_p = \hbar/2$ exactly (the Gaussian starts at the bound). For $t > 0$, $\sigma_x$ grows while $\sigma_p$ stays fixed, so $\sigma_x\sigma_p > \hbar/2$. The spreading takes the packet away from the minimum.

### The Spreading Timescale

Define the **doubling time** $t_{2x}$ as the time for $\sigma_x$ to grow to $\sqrt{2}\,\sigma_x(0)$. From $\sigma_x(t)^2 = \sigma_x(0)^2 + (\hbar t/2m\sigma_x(0))^2$:

$$t_{2x} = \frac{2m\sigma_x(0)^2}{\hbar}.$$

This controls how "quantum" a system behaves on accessible timescales. For an electron localized to $\sigma_x(0) = 1$ Å $= 10^{-10}$ m:

$$t_{2x} = \frac{2 \times 9.109\times10^{-31}\,\text{kg} \times (10^{-10}\,\text{m})^2}{1.055\times10^{-34}\,\text{J·s}} \approx 1.7\times10^{-16}\,\text{s}.$$

About 170 attoseconds — spreading is essentially instantaneous at atomic scales. For a 1 mg grain of sand with $\sigma_x(0) = 1\,\mu\text{m}$:

$$t_{2x} = \frac{2 \times 10^{-6}\,\text{kg} \times (10^{-6}\,\text{m})^2}{10^{-34}\,\text{J·s}} \approx 2\times10^{22}\,\text{s},$$

which is more than a trillion times the age of the universe. Quantum spreading is experimentally observable only for quantum-scale objects; macroscopic objects are classical for this reason.

---

## Worked Example: Spreading Time of an Electron Wave Packet

**The lesson.**

An electron in a quantum dot of diameter $d = 10\,\text{nm}$ is localized to $\sigma_x(0) = 2\,\text{nm}$ (the dot confines it, but the actual wave function has a width of about $d/5$). The confining potential is suddenly removed. How long before the wave packet doubles in spatial width?

**The setup.** We use the free-particle spreading formula:

$$t_{2x} = \frac{2m_e\,[\sigma_x(0)]^2}{\hbar}.$$

**Numbers in.** With $m_e = 9.109\times10^{-31}\,\text{kg}$, $\sigma_x(0) = 2\times10^{-9}\,\text{m}$, $\hbar = 1.055\times10^{-34}\,\text{J·s}$:

$$t_{2x} = \frac{2\times(9.109\times10^{-31})\times(2\times10^{-9})^2}{1.055\times10^{-34}} = \frac{2\times9.109\times4\times10^{-49}}{1.055\times10^{-34}}.$$

Numerator: $2 \times 9.109 \times 4 = 72.87$, so numerator $= 72.87\times10^{-49} = 7.287\times10^{-48}$. Denominator: $1.055\times10^{-34}$.

$$t_{2x} = \frac{7.287\times10^{-48}}{1.055\times10^{-34}} \approx 6.9\times10^{-14}\,\text{s} \approx 69\,\text{fs}.$$

The packet doubles in about 70 femtoseconds — well within the range of ultrafast laser spectroscopy. An ultrafast pump-probe experiment can watch this spreading in real time.

**The limit.** The formula $t_{2x} = 2m\sigma_x(0)^2/\hbar$ says the doubling time scales as $\sigma_x(0)^2$. Make the dot twice as narrow ($\sigma_x(0) = 1\,\text{nm}$): $t_{2x} \approx 17\,\text{fs}$. Make it twice as wide ($\sigma_x(0) = 4\,\text{nm}$): $t_{2x} \approx 280\,\text{fs}$. The packet spreads faster the more tightly it is initially confined — because tight confinement means a broad momentum distribution, and broader momentum spread means the components travel at more different speeds.

Also note: the doubling time is independent of $k_0$ (the mean momentum). A fast packet and a slow packet of the same width spread at the same rate. The mean momentum determines where the packet goes; the width determines how fast it smears.

---

## Common Misconceptions

**"The particle travels at the phase velocity."** The phase velocity $v_{ph} = \omega/k = \hbar k/2m$ is the speed of wavefronts — lines of constant phase — inside the packet. It is half the classical velocity. But the *particle* (the packet envelope, the probability maximum) travels at the group velocity $v_g = \hbar k/m$, which equals the classical velocity. If you bet on the phase velocity, you will always predict the particle arrives at half the actual time.

**"Non-normalizable means non-physical and therefore useless."** Plane waves cannot be normalized, but they are indispensable. They are the energy eigenstates of the free Hamiltonian, the building blocks of the Fourier decomposition, and the states that scattering cross sections are computed from. The physically realizable state is the wave packet; the plane wave is the basis element. A Fourier series is not "wrong" because $\sin(nx)$ does not satisfy a normalization condition.

**"The momentum distribution spreads too."** It does not. $|\phi(k)|^2$ is constant in time. The packet spreads in position because the Fourier components drift apart in space — but each component's amplitude is unchanged. If you measured momentum at $t = 0$ and again at $t = 1000t_{2x}$, the two histograms would be identical (within statistical fluctuations). This is also why $\sigma_p$ is constant: it is determined by $|\phi(k)|^2$, which does not change.

**"Spreading is caused by the uncertainty principle."** This conflates two different statements. The uncertainty principle says $\sigma_x\sigma_p \geq \hbar/2$ at every instant — a constraint on the state's width. It says nothing about dynamics. Spreading is caused by dispersion: $d^2\omega/dk^2 \neq 0$ means different Fourier components travel at different speeds, and over time they separate. A system where $d^2\omega/dk^2 = 0$ (light in vacuum) does not spread. A system with a restoring potential (Chapter 7's coherent state) does not spread despite having $\sigma_x\sigma_p = \hbar/2$ at all times. Dispersion is the cause; uncertainty is the constraint.

**"A faster-moving packet spreads more quickly."** The spreading rate depends on $\sigma_x(0)$ and $m$, not on $k_0$ or $v_g$. A fast packet with the same initial width as a slow packet spreads at the same rate. The group velocity translates the packet; the spreading time $t_{2x} = 2m\sigma_x(0)^2/\hbar$ is independent of translation speed.

---

## Exercises

**Warm-up**

1. *[Non-normalizability of plane waves; connection to uncertainty principle]* The plane wave $\psi_k(x) = e^{ikx}$ has $|\psi_k|^2 = 1$ everywhere. (a) Show that $\int_{-L}^{L}|\psi_k|^2\,dx = 2L$, so normalization requires $A = 1/\sqrt{2L}$ on a finite interval $[-L, L]$. (b) Take $L \to \infty$. What happens to $A$? (c) Using $\sigma_p = 0$ (the plane wave has definite momentum) and the Kennard inequality $\sigma_x\sigma_p \geq \hbar/2$, explain why the position uncertainty must be infinite. Connect this to the non-normalizability. *Difficulty: warm-up.*

2. *[Fourier pair: computing $\phi(k)$ from $\Psi(x,0)$]* A wave packet has initial profile $\Psi(x, 0) = N e^{-|x|/a}e^{ik_0 x}$ for real constants $a, k_0$, and normalization constant $N$. (a) Find $N$ such that $\int|\Psi|^2\,dx = 1$. (b) Compute $\phi(k) = (1/\sqrt{2\pi})\int\Psi(x,0)e^{-ikx}\,dx$. (c) Sketch $|\phi(k)|^2$ and identify the peak position and approximate width. *Difficulty: warm-up.*

3. *[Phase vs. group velocity]* For the free particle with $\omega = \hbar k^2/2m$: (a) compute $v_{ph}$ and $v_g$ for $k_0 = 5\,\text{nm}^{-1}$ and $m = m_e = 9.109\times10^{-31}\,\text{kg}$; express your answer in m/s. (b) Verify that $v_g = 2v_{ph}$. (c) The electron's classical kinetic energy is $K = m_e v_g^2/2$. Verify that $\hbar\omega(k_0) = K$. *Difficulty: warm-up.*

**Application**

4. *[Spreading formula; quantum dot example]* A conduction electron in a semiconductor is localized to $\sigma_x(0) = 5\,\text{nm}$, effective mass $m^* = 0.067\,m_e$. (a) Compute the doubling time $t_{2x}$. (b) Compute $\sigma_x(t)$ at $t = 1\,\text{ps}$. (c) The electron's de Broglie thermal wavelength at $T = 300\,\text{K}$ is $\lambda_{th} = h/\sqrt{2\pi m^* k_B T} \approx 30\,\text{nm}$. Is the packet still smaller than $\lambda_{th}$ at $t = 1\,\text{ps}$? *Difficulty: application.*

5. *[Group velocity and classical motion]* A neutron (mass $m_n = 1.675\times10^{-27}\,\text{kg}$) has de Broglie wavelength $\lambda = 1.8\,\text{Å} = 1.8\times10^{-10}\,\text{m}$ (cold neutron, typical of a reactor source). (a) Compute $k_0 = 2\pi/\lambda$, $v_g$, and $v_{ph}$. (b) The neutron travels 1 m from the reactor to a detector. Compute the transit time using $v_g$, and the time you would incorrectly predict using $v_{ph}$. (c) A neutron interferometer requires both paths to be within the coherence length of the packet. If $\sigma_p/\hbar = \Delta k = 10^6\,\text{m}^{-1}$, estimate the coherence length $\ell_c \sim 1/\Delta k$ and the time it takes the packet to spread by an amount equal to $\ell_c$. *Difficulty: application.*

6. *[Optimal wave packet width]* For a given propagation time $t$ and particle mass $m$, there is an initial width $\sigma_{opt}$ that minimizes the final width $\sigma_x(t)$. (a) Write $\sigma_x(t)^2 = \sigma_0^2 + (\hbar t/2m\sigma_0)^2$ as a function of $\sigma_0$. (b) Minimize over $\sigma_0$ to find $\sigma_{opt} = \sqrt{\hbar t/2m}$. (c) Compute $\sigma_{opt}$ for an electron at $t = 1\,\text{fs}$. What does this suggest about why atoms at the Bohr radius are "natural" in size? *Difficulty: application.*

**Synthesis**

7. *[Spreading as the opposite of the HO coherent state]* In Chapter 7, a coherent state of the harmonic oscillator is a Gaussian wave packet that propagates without spreading. In this chapter, the free-particle Gaussian spreads. In both cases, $\sigma_p$ is constant. Write a careful two-paragraph explanation of why the HO coherent state does not spread while the free-particle packet does — invoking the dispersion relation and the role of the potential. Do not quote formulas without interpreting them. *Difficulty: synthesis.*

8. *[Building a sinc packet]* Let $\phi(k) = 1/\sqrt{2\Delta k}$ for $|k - k_0| \leq \Delta k$ and zero otherwise. (a) Compute $\Psi(x, 0) = (1/\sqrt{2\pi})\int\phi(k)e^{ikx}\,dk$ analytically. Express your answer in terms of $\text{sinc}(\Delta k \cdot x) = \sin(\Delta k\cdot x)/(\Delta k\cdot x)$. (b) Compare the uncertainty product $\sigma_x\sigma_p$ for the sinc packet to that of the Gaussian with the same $\Delta k$. Which is larger? Why? (c) In simulation, observe the sinc packet's sidelobes: explain physically why they exist. *Difficulty: synthesis.*

**Challenge**

9. *[The spreading formula from the stationary-phase approximation]* The stationary-phase approximation gives the packet center at $x_{center}(t) = (d\omega/dk)|_{k_0}\cdot t$. Go one step further: keep the second-order term $\omega''_0(k-k_0)^2 t/2$ in the Taylor expansion. (a) Show that the Gaussian integral with this quadratic phase produces a complex width $\Delta(t) = \sigma_x(0)^2 + i\hbar t/2m$. (b) Show that $|\Psi(x,t)|^2$ is a Gaussian with width $|\Delta(t)|$, and derive $\sigma_x(t) = |\Delta(t)| = \sigma_x(0)\sqrt{1 + (\hbar t/2m\sigma_x(0)^2)^2}$, matching the formula quoted in the chapter. (c) The imaginary part of $\Delta(t)$ contributes a **chirp** to the phase of $\Psi(x,t)$: the local wavevector $k(x, t) = k_0 + (x - v_g t)/|\Delta(t)|^2 \cdot \hbar t/2m$ varies across the packet. Explain qualitatively why this chirp appears and what it means for the interference structure of the spreading packet. *Difficulty: challenge.*

---

## Still Puzzling

The spreading formula is exact for the free Gaussian packet — not an approximation. But the derivation assumed the Taylor expansion of $\omega(k)$ terminates at second order. For the free particle, $\omega = \hbar k^2/2m$ is exactly quadratic, so the Taylor expansion is exact and the formula is exact. For a general dispersion relation, higher-order terms produce deviations from Gaussian spreading — the packet develops non-Gaussian tails. This is a live problem in ultrafast optics, where the cubic dispersion term in glass causes measurable pulse distortion.

Is spreading *always* inevitable for a free particle? The answer is yes for any normalizable initial state with finite energy — the spreading formula holds generally, not just for Gaussians. However, certain engineered initial conditions (Airy beams, accelerating wave packets) can resist spreading in specific directions while trading off in others. These are active research topics in both quantum optics and atomic physics.

The formula $v_g = d\omega/dk$ can, in principle, exceed $c$ in media with anomalous dispersion near absorption resonances. In those cases, $v_g$ is no longer the signal velocity or energy transport velocity. For the free non-relativistic particle, $v_g = p/m < c$ always, and this complication does not arise. Volume 2 treats the relativistic free particle, where the dispersion relation changes and $v_{ph} > c$ while $v_g < c$ simultaneously.

---

## The +1 — Simulation Exercise: Watching a Wave Packet Spread

The deliverable: `08-wave-packet.html`. A wave-packet simulator showing a Gaussian packet propagating, spreading, and exhibiting the carrier-envelope separation.

### Part A — CLAUDE.md physics rules for this chapter

Add this stanza to your existing `CLAUDE.md`:

````markdown
## Chapter 8 — Free Particle and Wave Packets

PHYSICS
- Free-particle dispersion: omega(k) = hbar * k^2 / (2 * m_e).
  Units: hbar = 1 (natural units), m = 1, OR use SI: hbar = 1.055e-34, m = m_e = 9.109e-31.
  Prefer hbar = 1, m = 1 for the simulation to keep numbers manageable.
- Time evolution via FFT: compute phi(k) by forward FFT of psi(x, 0);
  multiply by exp(-i * omega(k) * t); inverse FFT to get psi(x, t).
  This is EXACT for the free particle (no Crank-Nicolson needed here).
- Gaussian initial condition:
    psi(x, 0) = (1 / (pi * sigma0^2))^(1/4) * exp(-x^2 / (2 * sigma0^2)) * exp(i * k0 * x)
- Spreading formula (analytic): sigma_x(t)^2 = sigma_x(0)^2 + (hbar * t / (2 * m * sigma_x(0)))^2
  Display analytic sigma_x(t) alongside numerical sigma_x(t) — they must agree.
- Group velocity: v_g = hbar * k0 / m. Phase velocity: v_ph = hbar * k0 / (2 * m). v_g = 2 * v_ph.
- sigma_p is CONSTANT in time (momentum distribution does not spread).
- sigma_x * sigma_p = hbar / 2 at t = 0 (Gaussian starts at bound).
  For t > 0, sigma_x * sigma_p > hbar / 2.
- Carrier phase: the carrier wave moves at v_ph = v_g / 2. Phase crests inside the
  envelope should appear to move FASTER than the envelope (v_g > v_ph means the
  envelope outruns the crests --- check the visualization direction).
  WAIT: v_g = 2 * v_ph means the envelope moves FASTER, so crests enter from the back.

DISPLAY
- Three panels: Re(psi), Im(psi), |psi|^2.
- Side panel: sigma_x(t) numeric vs. analytic sigma_x(t) curve.
- sigma_x * sigma_p / (hbar/2) --- reads 1.000 at t = 0, grows thereafter.
- Sliders: sigma0 (initial width), k0 (mean wavenumber), time t (or animated).
- Momentum-space panel: |phi(k)|^2 --- static, confirming sigma_p is constant.
````

### Part B — The simulation prompt

````markdown
SHOW.
Free-particle wave packet: a Gaussian initial state

  psi(x, 0) = (1 / (pi * sigma0^2))^(1/4) * exp(-x^2 / (2 * sigma0^2)) * exp(i * k0 * x)

evolves under the free Schrödinger equation with dispersion omega(k) = hbar * k^2 / (2 * m).
Use natural units: hbar = 1, m = 1 (or allow the user to set m in eV units).

Physics to display:
  - The packet moves at group velocity v_g = k0 / m.
  - The carrier oscillations inside the envelope move at v_ph = k0 / (2m) = v_g / 2.
    Phase crests should appear to move slower than the envelope.
  - The packet spreads: sigma_x(t) = sigma0 * sqrt(1 + (t / (2 * m * sigma0^2))^2).
  - The momentum distribution |phi(k)|^2 does NOT change in time.
  - sigma_x * sigma_p / (hbar/2) = 1.0 at t = 0; grows for t > 0.

SAY.
Produce a single file 08-wave-packet.html.

Layout (1000 px wide):
  Left column (650 px):
    Four stacked SVG panels sharing an x-axis (x from -50 to +100 in natural units):
      1. Re(psi(x, t)) in orange, signed, scaled to fit panel
      2. Im(psi(x, t)) in gray dashed, signed
      3. |psi(x, t)|^2 in blue filled
      4. |phi(k)|^2 in green filled, on a k-axis from -5k0 to 5k0
    Below: time slider (0 to 50 in natural units, step 0.1), Play/Pause button.
    Annotation on panel 3: a vertical dashed line at the envelope center x = v_g * t,
    labeled "envelope center."

  Right column (350 px):
    Sliders: sigma0 (0.5 to 5), k0 (1 to 10).
    Live readouts:
      v_g = k0 / m,  v_ph = k0 / (2m)
      sigma_x(t) numeric (Simpson's rule on |psi|^2)
      sigma_x(t) analytic (formula)
      sigma_p (constant; verify it matches initial value)
      sigma_x * sigma_p / (hbar / 2)  --- prominent display, reads 1.000 at t = 0
    A plot of sigma_x(t) vs. t: numeric points overlaid on the analytic curve.

CONSTRAIN.
  - D3 v7 from CDN. SVG only. Vanilla JS. N = 1024 grid points.
  - Time evolution via FFT: psi(x, t) = IFFT[phi(k) * exp(-i * omega(k) * t)].
    Use a pure-JS FFT (Cooley-Tukey, built inline). Comment the convention.
  - Panel 1–3 share x-axis and update together on each animation frame.
  - Panel 4 (momentum space) updates only when sigma0 or k0 changes (not each frame).
  - Carrier-vs-envelope visibility: ensure k0 is large enough relative to sigma0 that
    individual oscillations are visible inside the envelope in panel 1 and 2.
    Default: sigma0 = 2, k0 = 5 (about 10 oscillations visible inside the envelope).

VERIFY.
  (a) At t = 0: sigma_x = sigma0 / sqrt(2) (analytic and numeric agree to < 1%).
  (b) At t = 2 * m * sigma0^2 (the doubling time): sigma_x = sqrt(2) * sigma_x(0).
      Numeric value must match analytic within 2%.
  (c) sigma_p constant across all t: verify by computing it numerically at t = 0
      and t = 10 * t_double and confirming < 1% change.
  (d) The phase crests (peaks of Re psi) move at v_ph = k0 / 2m. Add a marker on
      a crest at t = 0 and verify it has moved by v_ph * delta_t after delta_t steps.
  (e) Normalization integral = 1.000 at all times (Simpson's rule).

List failure modes you have guarded against:
  - FFT wraparound (x-axis runs off the grid boundary): ensure packet center stays
    in the middle third of the grid for the full animation range.
  - Wrong FFT convention: forward = sum psi_n exp(-i k_m x_n) dx / sqrt(2pi).
  - Group vs. phase velocity confusion: the envelope center must move at v_g, not v_ph.
  - Normalization drift: FFT-based propagation is unitary; verify |sum |psi|^2 dx - 1| < 1e-6.
  - sigma_p computed incorrectly (using position-space derivative vs. momentum-space integral).
````

### Part C — Exploration tasks

**Task 1 — Phase vs. envelope.** Set $\sigma_0 = 2$, $k_0 = 5$. Press Play. Watch the orange (Re $\psi$) panel. Pick a bright crest inside the envelope. Does the crest move forward faster or slower than the blue $|\psi|^2$ peak? Measure: advance time by $\delta t = 1$. The blue peak moves by $v_g \cdot \delta t = 5$. The crest moves by $v_{ph} \cdot \delta t = 2.5$. The envelope outruns its own crests. Write one sentence interpreting what this means for the particle's position.

**Task 2 — Spreading rate.** Reset $t = 0$. Set $\sigma_0 = 1$, $k_0 = 5$. Record $\sigma_x$ at $t = 0$. Now advance to $t = 2$ (the analytic doubling time $t_{2x} = 2m\sigma_0^2 = 2$). Confirm $\sigma_x \approx \sqrt{2}\,\sigma_x(0)$. Now set $\sigma_0 = 2$. The new doubling time is $t_{2x} = 8$. Advance to $t = 8$ and confirm. The wider packet spreads four times more slowly (doubling time $\propto \sigma_0^2$). Write down: if you double the initial width, by what factor does the doubling time change?

**Task 3 — Momentum is constant.** Watch the green panel (momentum space) while the animation runs. Confirm that $|\phi(k)|^2$ does not change. Now read $\sigma_p$ from the right panel at $t = 0$, $t = 5$, and $t = 20$. They should match. This confirms: the spreading is purely a position-space phenomenon; momentum is unchanged by free propagation.

**Task 4 — The ratio exceeds one.** Read $\sigma_x\sigma_p/(\hbar/2)$ at $t = 0$ (should be $1.000$). Advance time. The ratio should grow. At what time (in units of $t_{2x}$) does the ratio reach $\sqrt{2}$? Derive this analytically from $\sigma_x(t) = \sigma_0\sqrt{1 + (t/t_{2x})^2}$ and confirm in the simulation.

**Task C — Extension.** Change the initial packet to a **double Gaussian**: $\psi(x, 0) \propto e^{-(x-d)^2/2\sigma_0^2}e^{ik_0 x} + e^{-(x+d)^2/2\sigma_0^2}e^{ik_0 x}$ for some $d > 0$. At $t = 0$ there are two separated peaks. Predict: as time advances, what happens when the two spreading packets overlap? Run the simulation and compare the $|\psi|^2$ pattern to your prediction. Is there interference? What determines whether the overlap is constructive or destructive at a given point?

### Part D — Extension prompt

````markdown
Add a "dispersion relation explorer" panel below the existing four panels.

The panel shows:
  Left: A user-selectable dispersion relation omega(k):
    1. Free particle (quantum): omega = k^2 / (2m)  [the chapter's case]
    2. Relativistic: omega = sqrt(k^2 + m^2)  [in natural units c = 1]
    3. Linear (non-dispersive): omega = k  [e.g., photon in vacuum]
    4. Capillary waves: omega = k^(3/2)
  Right: A plot of v_ph = omega / k and v_g = d omega / dk vs k, both on the same axis.
  Annotation: highlight v_ph and v_g at k = k0 with vertical dotted lines.

For each selection, update the main animation to use the chosen dispersion relation.
The case 3 (linear) should show a packet that does NOT spread.
The case 4 (capillary) should show a packet where v_g > v_ph (anomalous dispersion).

After implementing, run the four cases with sigma0 = 2, k0 = 5 for t = 20 natural units.
Report sigma_x(t=20) for each case and explain which dispersion relation spreads fastest
and why, in terms of |d^2 omega / dk^2|.
````

---

## References

- Fitzpatrick, R. (2015). *Introductory Quantum Mechanics*. University of Texas at Austin. §2.11 "Evolution of Wave-Packets." Full Taylor-expansion derivation of $\sigma_x(t)$ formula and doubling time $t_2 \sim m(\Delta x)^2/\hbar$; electron example states "doubling time is only about $10^{-16}$ s." Available via Physics LibreTexts. [verify]
- Likharev, K. K. (2012). *Essential Graduate Physics — Quantum Mechanics*. Stony Brook University. §2.2 "Free Particle: Wave Packets." Equations (2.33) give $v_g = v_0$ (classical) and $v_{ph} = v_g/2$; equations (2.39)–(2.40) give spreading formula $(\delta x')^2 = (\delta x)^2 + (\hbar t/2m)^2/(\delta x)^2$; propagator $G(x,t;x_0,0)$ derived at equations (2.47)–(2.49). Available via Physics LibreTexts. [verify]
- Griffiths, D. J. & Schroeter, D. F. (2018). *Introduction to Quantum Mechanics* (3rd ed.). Cambridge University Press. §2.4 "The Free Particle." Standard reference for plane-wave non-normalizability and wave-packet construction.
- Darwin, C. G. (1927). Free motion in the wave mechanics. *Proceedings of the Royal Society A*, 117(776), 258–293. Original calculation of wave-packet spreading for an electron. [verify]
- Schwartz, M. (n.d.). *Lecture 11: Wavepackets and Dispersion*. Harvard Physics 253b. https://scholar.harvard.edu/files/schwartz/files/lecture11-wavepackets.pdf. Concise derivation of phase vs. group velocity. [verify]
- Pramana Editorial (2010). Understanding the spreading of a Gaussian wave packet. *Pramana — Journal of Physics*, 74(6), 867–874. Indian Academy of Sciences. Detailed pedagogical treatment of the spreading formula. [verify]
