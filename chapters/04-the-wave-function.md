# Chapter 3 — The Wave Function and Born's Rule

## TL;DR

The wave function $\psi(x,t)$ is not the particle and not a classical wave — it is a complex-valued function whose squared modulus gives the probability *density* for finding the particle at position $x$. Born's rule: $P(\text{particle in }[a,b]) = \int_a^b |\psi|^2\,dx$. The density $|\psi|^2$ can exceed 1, the imaginary part of $\psi$ is not optional, and normalization is preserved automatically by the Schrödinger equation.

---

## Learning Objectives

By the end of this chapter you should be able to:

1. **Remember** Born's rule precisely, distinguishing probability density from probability. *(Bloom: Remember)*
2. **Apply** Born's rule: given a wave function, compute the normalization constant and the probability of finding the particle in a specified interval. *(Bloom: Apply)*
3. **Analyze** why $\psi$ must be complex, and what the imaginary part carries physically. *(Bloom: Analyze)*
4. **Evaluate** the claim that "the uncertainty principle is about measurement disturbing the particle," and replace it with the correct Kennard inequality statement. *(Bloom: Evaluate)*
5. **Create** a D3 simulation that displays Re $\psi$, Im $\psi$, and $|\psi|^2$ for a gallery of wave functions and computes $\langle x\rangle$, $\langle p\rangle$, $\sigma_x$, $\sigma_p$ live. *(Bloom: Create)*

---

## The Blob You Already Watched

You have already seen it. In Chapter 0, there was a blue filled curve drifting across the screen. You dragged a slider and the curve spread. There was an orange curve inside it, oscillating, going negative. You probably had a feeling — somewhere between understanding and confusion — that you were looking at *something*, but you were not told what it was.

Now I want to tell you. Not by handing you a definition. By actually figuring out what the blob is forced to be.

---

## Core Development

### What Are We Looking at?

Here is the first thing to notice about the blue curve: it has units, and you probably never saw them labeled. If the particle moves along a line measured in nanometers, the blue curve is a number *per nanometer*. It is a density — like population per square kilometer, not a total population count. You cannot read off "the particle is here" from its value at a single point, any more than you can read the number of people in a city from a population density at one address. To get a probability, you have to integrate over a region.

That is the **Born rule**. Max Born introduced it in 1926 in a paper on quantum scattering. Given a wave function $\psi(x,t)$, the probability of finding the particle in the interval $[a, b]$ at time $t$ is:

$$\boxed{P\bigl(\text{particle in } [a,b]\bigr) = \int_a^b |\psi(x,t)|^2\,dx}$$

The density $|\psi(x,t)|^2$ can be larger than 1 — it is per unit length, not a dimensionless probability. Probability is what you get after you multiply by $dx$ and integrate. Confusing the value of the density at a point with a probability is the single most common first mistake; it is a unit error.

Born's original 1926 paper actually stated the probability was proportional to $\psi$ itself — not $|\psi|^2$. In a footnote added in proof, he corrected it to $|\psi|^2$. That footnote is one of the most consequential edits in the history of physics. Born received the Nobel Prize in 1954 for the statistical interpretation it introduced. [verify: Born, Z. Phys. 38, 803 (1926); Nobel records 1954]

---

### Why Is $\psi$ Complex at All?

If what we measure is $|\psi|^2$, and $|\psi|^2$ is real and non-negative, why not just use a real wave function? Why drag in complex numbers?

The answer is not a convention — it is forced. The time-dependent Schrödinger equation is:

$$i\hbar \frac{\partial \psi}{\partial t} = \hat{H} \psi.$$

That $i$ on the left side is not removable. Suppose $\psi$ were purely real. Then $\partial\psi/\partial t$ would be real, and $i\hbar \cdot (\text{real})$ would be purely imaginary. The equation would require a real right side to equal a purely imaginary left side — impossible unless everything is zero. The dynamics themselves force $\psi$ into the complex plane.

You saw this in Chapter 0. The orange curve (Re $\psi$) and the gray dashed curve (Im $\psi$) were both non-trivial, with Im $\psi$ leading Re $\psi$ by a quarter cycle. If you tried to set Im $\psi = 0$ and take one time step under the Schrödinger equation, the imaginary part would rebuild immediately. The phase is not a mathematical appendage — it carries the physics.

Concretely, consider the Gaussian wave packet with central momentum $\hbar k_0$:

$$\psi(x) = A\,e^{-x^2/(2a^2)}\,e^{ik_0 x}.$$

Then:
$$\text{Re}\,\psi = A\,e^{-x^2/(2a^2)}\cos(k_0 x), \qquad \text{Im}\,\psi = A\,e^{-x^2/(2a^2)}\sin(k_0 x).$$

Both oscillate; both carry the momentum information encoded in $k_0$. Meanwhile:

$$|\psi|^2 = A^2\,e^{-x^2/a^2} \quad \text{(a smooth Gaussian — the oscillations vanish)}.$$

The momentum $k_0$ is invisible in $|\psi|^2$. It lives entirely in the phase — in the relationship between Re $\psi$ and Im $\psi$. Discard the imaginary part and you cannot distinguish a wave packet moving right from one moving left.

---

### $\psi$ Is Not the Particle

This must be said carefully, because the mistake persists from freshman physics into research groups.

$\psi$ is not the particle. In any single run of the experiment, the particle is at one definite place when you measure its position. $\psi$ tells you the *distribution* of those places across many identically prepared experiments. Narrow $\psi$: repeated measurements cluster tightly. Wide $\psi$: they spread out.

The blue blob spreading on the screen in Chapter 0 was not a particle physically expanding. It was the probability distribution of position measurements becoming more uncertain. If you had one actual particle and measured its position at a late time (after the blob had spread), you would get one number — somewhere inside the wide distribution. Run the experiment ten thousand times with identical initial conditions; the histogram of results matches $|\psi|^2$.

That is the Born rule in practice. The blob was telling you the histogram.

---

### Normalization: The Particle Has to Be Somewhere

Because $|\psi|^2$ is a probability density, and the particle must be found *somewhere*, the total probability must equal one:

$$\int_{-\infty}^{\infty} |\psi(x,t)|^2\,dx = 1.$$

A wave function satisfying this is called **normalized**.

In practice, you often encounter $\psi$ written without a normalization constant — call it $\tilde{\psi}$. To normalize it, you compute:

$$N = \int_{-\infty}^{\infty} |\tilde{\psi}(x)|^2\,dx,$$

and then define $\psi = \tilde{\psi}/\sqrt{N}$. The normalized wave function satisfies $\int|\psi|^2\,dx = 1$.

**Does normalization stay?** If you normalize $\psi$ at $t = 0$, does $\int|\psi|^2\,dx$ remain 1 as time evolves? It must — otherwise the formalism would be incoherent. The proof that it does is worth doing in full, because it produces a beautiful and important byproduct.

Differentiate with respect to time:

$$\frac{d}{dt}\int_{-\infty}^{\infty}|\psi|^2\,dx = \int_{-\infty}^{\infty}\frac{\partial}{\partial t}(\psi^*\psi)\,dx.$$

By the product rule: $\partial_t(\psi^*\psi) = (\partial_t\psi^*)\psi + \psi^*(\partial_t\psi)$. Substitute the Schrödinger equation $i\hbar\,\partial_t\psi = \hat{H}\psi$ (with $\hat{H} = -(\hbar^2/2m)\partial_x^2 + V$) and its complex conjugate:

$$\partial_t\psi = \frac{1}{i\hbar}\hat{H}\psi, \qquad \partial_t\psi^* = -\frac{1}{i\hbar}\hat{H}\psi^*.$$

Substituting and collecting terms: the contributions from the potential $V(x)$ cancel exactly (they appear with opposite signs). Only the kinetic part survives:

$$\frac{\partial}{\partial t}(\psi^*\psi) = \frac{i\hbar}{2m}\left(\frac{\partial^2\psi^*}{\partial x^2}\,\psi - \psi^*\frac{\partial^2\psi}{\partial x^2}\right).$$

The right side is a perfect derivative in $x$:

$$\frac{\partial^2\psi^*}{\partial x^2}\,\psi - \psi^*\frac{\partial^2\psi}{\partial x^2} = \frac{\partial}{\partial x}\!\left(\frac{\partial\psi^*}{\partial x}\,\psi - \psi^*\frac{\partial\psi}{\partial x}\right).$$

(Differentiate the right side to verify — thirty seconds.) Define the **probability current**:

$$J(x,t) \equiv \frac{\hbar}{m}\,\mathrm{Im}\!\left(\psi^*\frac{\partial\psi}{\partial x}\right).$$

Then we have the **continuity equation**:

$$\frac{\partial|\psi|^2}{\partial t} = -\frac{\partial J}{\partial x}.$$

This is the same equation that governs the flow of any conserved quantity — mass, charge, energy. Probability flows like a fluid with current $J$. Integrate over all $x$:

$$\frac{d}{dt}\int_{-\infty}^{\infty}|\psi|^2\,dx = -\bigl[J(x,t)\bigr]_{-\infty}^{\infty}.$$

For any normalizable $\psi$, $J \to 0$ as $|x| \to \infty$. The right side is zero. Normalization is permanent.

The proof has a practical consequence: in the simulation, if $\int|\psi|^2\,dx$ drifts away from 1, something is wrong — either the time-stepping scheme is non-unitary (explicit Euler will do this), or probability is leaking at the grid boundaries. The normalization indicator is a bug detector, not something to be manually re-imposed at each step.

---

### What Do You Actually Measure? Expectation Values

Born's rule gives you the probability distribution for position. The **expectation value** of position — the average over many identically prepared experiments — is the centroid of that distribution:

$$\langle x\rangle = \int_{-\infty}^{\infty} x\,|\psi(x,t)|^2\,dx.$$

Each possible position is weighted by how probable it is. This is the mean of the probability distribution $|\psi|^2$.

The average momentum is less obvious. You cannot write $\langle p\rangle = \int p\,|\psi(x)|^2\,dp$ in position space, because $p$ is not a function of $x$. Momentum in position space is a derivative operator. The Fourier transform provides the justification: define $\phi(p,t)$ as the Fourier transform of $\psi(x,t)$. Then $|\phi(p,t)|^2$ is the probability density for momentum, and $\langle p\rangle = \int p\,|\phi|^2\,dp$. Translating this back to position space via Parseval's theorem turns multiplication by $p$ into differentiation — the **momentum operator** in position space is:

$$\hat{p} = -i\hbar\frac{\partial}{\partial x},$$

and the expectation value is:

$$\langle p\rangle = \int_{-\infty}^{\infty}\psi^*(x,t)\,\left(-i\hbar\frac{\partial}{\partial x}\right)\psi(x,t)\,dx.$$

The sign matters. For a wave packet moving to the right with $k_0 > 0$, this formula gives $\langle p\rangle = \hbar k_0 > 0$. Writing $\hat{p} = +i\hbar\,\partial_x$ by mistake flips the direction; the simulation catches this immediately.

---

### The Uncertainty Principle — About Shape, Not Disturbance

Define the standard deviations of the position and momentum distributions in the usual statistical way:

$$\sigma_x = \sqrt{\langle x^2\rangle - \langle x\rangle^2}, \qquad \sigma_p = \sqrt{\langle p^2\rangle - \langle p\rangle^2}.$$

The **Kennard inequality** — proved by E. H. Kennard in 1927 — states:

$$\sigma_x\,\sigma_p \geq \frac{\hbar}{2}.$$

This is a statement about the **shape of $\psi$**, not about any measurement process. The clearest way to see it: prepare ten thousand copies of the same state $\psi$. Measure position on five thousand of them (call the standard deviation $\sigma_x$). Measure momentum on the other five thousand (call the standard deviation $\sigma_p$). No single particle is measured twice. No disturbance occurs. Yet the product cannot be smaller than $\hbar/2$.

The reason is Fourier analysis. A function narrow in $x$ must be broad in its Fourier transform (momentum space), and vice versa. The inequality $\sigma_x\sigma_p \geq \hbar/2$ is the precise, rigorous quantification of that unavoidable relationship — with $\hbar/2$ pinning the exact bound.

A separate Heisenberg measurement-disturbance relation — which *is* about what happens when you measure — has a different form and a different bound. Ozawa (2003) formalized it; Erhart et al. (2012) and Rozema et al. (2012) tested it experimentally. The Kennard inequality and the measurement-disturbance relation are different animals. This chapter addresses the Kennard inequality only. [verify: Kennard, Z. Phys. 44, 326 (1927); Ozawa, Phys. Rev. A 67, 042105 (2003)]

**The Gaussian saturates the bound.** For $\psi(x) = (\pi a^2)^{-1/4}\,e^{-x^2/(2a^2)}\,e^{ik_0x}$, one computes:

$$\sigma_x = \frac{a}{\sqrt{2}}, \qquad \sigma_p = \frac{\hbar}{\sqrt{2}\,a}, \qquad \sigma_x\sigma_p = \frac{\hbar}{2}.$$

The product is exactly $\hbar/2$. Every other normalizable wave function gives a larger product. This is why the Gaussian wave packet appears throughout quantum mechanics — it is the tightest possible state, the one that balances position and momentum uncertainty as evenly as the physics permits.

Notice the trade-off: $\sigma_x \propto a$, $\sigma_p \propto 1/a$. Make the wave packet narrower in space (smaller $a$) and it becomes broader in momentum. The product stays at $\hbar/2$. This is not a technological limitation — you cannot engineer around it.

---

## Worked Example: Normalize a Wave Function and Compute a Probability

**Problem.** A particle on the real line has un-normalized wave function $\tilde{\psi}(x) = e^{-|x|/a}$ for a real constant $a > 0$. (a) Find the normalization constant $A$ so that $\psi(x) = A\tilde{\psi}(x)$ is normalized. (b) Compute the probability of finding the particle in $[-a, a]$.

---

**Part (a) — Normalization.**

We need:
$$\int_{-\infty}^{\infty}|A\,e^{-|x|/a}|^2\,dx = 1.$$

Since $\tilde{\psi}$ is real, $|\tilde{\psi}|^2 = e^{-2|x|/a}$. The function is symmetric about $x = 0$:

$$A^2 \int_{-\infty}^{\infty} e^{-2|x|/a}\,dx = 2A^2\int_0^{\infty}e^{-2x/a}\,dx.$$

**Dead end first.** A student might try to integrate $e^{-2|x|/a}$ over all of $\mathbb{R}$ directly without splitting at $x = 0$. The absolute value makes this fail — the integrand is not $e^{-2x/a}$ for $x < 0$. Split it.

Evaluating:

$$2A^2\int_0^{\infty}e^{-2x/a}\,dx = 2A^2\left[\frac{-a}{2}e^{-2x/a}\right]_0^{\infty} = 2A^2 \cdot \frac{a}{2} = A^2 a.$$

Setting $A^2 a = 1$ gives:

$$\boxed{A = \frac{1}{\sqrt{a}}}.$$

**Check units.** If $x$ is measured in nm, then $a$ has units of nm, and $A = 1/\sqrt{a}$ has units of nm$^{-1/2}$. Therefore $|\psi|^2 = A^2 e^{-2|x|/a}$ has units of nm$^{-1}$ — correct for a probability density in one dimension.

---

**Part (b) — Probability on $[-a, a]$.**

$$P(-a \leq x \leq a) = \int_{-a}^{a}|\psi(x)|^2\,dx = \frac{1}{a}\int_{-a}^{a}e^{-2|x|/a}\,dx = \frac{2}{a}\int_0^{a}e^{-2x/a}\,dx.$$

Evaluating:

$$\frac{2}{a}\left[\frac{-a}{2}e^{-2x/a}\right]_0^{a} = \frac{2}{a}\cdot\frac{a}{2}\left(1 - e^{-2}\right) = 1 - e^{-2} \approx 0.865.$$

$$\boxed{P(-a \leq x \leq a) \approx 86.5\%}$$

**Sanity check.** The result is between 0 and 1. The interval $[-a, a]$ contains the peak of $|\psi|^2$ (at $x = 0$), so a probability of about 86% is plausible — the remaining ~14% is in the tails $|x| > a$.

**What happens to $|\psi(0)|^2$?** At $x = 0$: $|\psi(0)|^2 = 1/a$. For $a = 0.5$ nm, this equals 2 nm$^{-1}$ — a number greater than 1. Does this violate anything? No. The density $|\psi|^2$ has units of nm$^{-1}$; it is not required to be $\leq 1$. Probability is dimensionless; probability *density* is not. Expecting $|\psi|^2 \leq 1$ is a unit confusion.

**The lesson.** Normalization is a two-step process: (1) compute $\int|\tilde{\psi}|^2\,dx$, (2) divide $\tilde{\psi}$ by the square root of that number. The probability in $[a,b]$ then follows by integration of the normalized $|\psi|^2$, not by reading off a value at a point.

**The limit.** This example has a real-valued $\psi$ with $J = 0$ everywhere — the particle has no net momentum flow. A real wave function cannot describe motion in a definite direction. To add momentum, one would multiply by $e^{ip_0 x/\hbar}$, making $\psi$ complex. The density $|\psi|^2$ would be unchanged, but $\langle p\rangle = p_0$.

---

## Common Misconceptions

**"$|\psi|^2$ must be less than or equal to 1."**

$|\psi|^2$ is a probability *density*, with units of inverse length. Probability densities are not bounded by 1 — only the integral over a region must be between 0 and 1. For the exponential above with $a = 0.5$ nm, $|\psi(0)|^2 = 2$ nm$^{-1}$. Correct; not alarming.

**"The particle is at the peak of $|\psi|^2$."**

The peak of $|\psi|^2$ is the most probable location *per unit length*. The probability of finding the particle in any finite interval requires integration. Moreover, $\langle x\rangle$ — the average position — can lie in a region of low probability density: for the double-Gaussian $\psi \propto e^{-(x-d)^2/(2\sigma^2)} + e^{-(x+d)^2/(2\sigma^2)}$, the average $\langle x\rangle = 0$ even though $|\psi(0)|^2$ is small and the peaks are at $\pm d$.

**"The uncertainty principle says measuring position disturbs momentum."**

This conflates the Kennard inequality with a measurement-disturbance statement. The Kennard inequality $\sigma_x\sigma_p \geq \hbar/2$ is a property of the *wave function's shape*, established before any measurement occurs. It holds even in a thought experiment where position and momentum are measured on separate, identically prepared particles. Heisenberg's 1927 gamma-ray microscope argument is a different (and in its original form, imprecise) claim.

**"Re $\psi$ is the 'real' wave function and Im $\psi$ is just added for math."**

The imaginary part is forced by the Schrödinger equation and carries the phase information — momentum, direction of travel, interference. Setting Im $\psi = 0$ at any moment and evolving forward gives wrong answers on the very next time step. The orange Re $\psi$ and gray Im $\psi$ in the simulation both have to be non-trivial for any moving wave packet.

**"Normalization must be re-imposed at each time step."**

For an exact analytic solution or a unitary numerical scheme (Crank–Nicolson), normalization is automatic — preserved by the Schrödinger equation. It fails only when a non-unitary integrator (e.g., explicit Euler) is used, or when probability leaks at grid boundaries. The normalization indicator in the simulation is a debugging tool, not a correction knob.

---

## Exercises

**Warm-up**

1. *[Tests: Born rule as density vs. probability]* A particle has wave function $\psi(x) = A\,e^{-|x|/a}$ for real $a > 0$. (a) Find $A$ such that $\int_{-\infty}^{\infty}|\psi|^2\,dx = 1$. (b) What is $P(-a \leq x \leq a)$? (c) The peak value $|\psi(0)|^2$ for $a = 0.5$ nm exceeds 1. Compute it and explain why this does not violate anything. *Difficulty: warm-up.*

2. *[Tests: complex structure of $\psi$, sign of momentum operator]* Let $\psi(x) = N\,e^{-x^2/(2a^2)}\,e^{ik_0 x}$ with $a = 1$ nm and $k_0 = -5$ nm$^{-1}$. (a) Sketch Re $\psi$, Im $\psi$, and $|\psi|^2$ on the same axis. Which curve is symmetric? Which oscillates? (b) Without computing the integral, determine the sign of $\langle p\rangle$ and the value of $\langle x\rangle$. Justify in one sentence each. *Difficulty: warm-up.*

3. *[Tests: normalization preservation, probability current]* For a real-valued wave function, show directly from $J = (\hbar/m)\,\mathrm{Im}(\psi^*\,\partial_x\psi)$ that $J = 0$ everywhere. Then state what this means physically: can a real $\psi$ describe a particle with net momentum in one direction? *Difficulty: warm-up.*

**Apply**

4. *[Tests: expectation values for a non-Gaussian state]* For the infinite-square-well ground state $\psi_1(x) = \sqrt{2/L}\,\sin(\pi x/L)$ on $[0, L]$: (a) Compute $\langle x\rangle$ and $\langle x^2\rangle$ by direct integration. (b) Compute $\sigma_x$. (c) Compute $\langle p\rangle$ using $\hat{p} = -i\hbar\,\partial_x$. Does the answer surprise you? Explain why $\langle p\rangle = 0$ makes physical sense for a standing wave. *Difficulty: Apply.*

5. *[Tests: Kennard inequality — preparation vs. disturbance]* A professor claims: "If I measure a particle's position very precisely, I must have disturbed its momentum. That is what the uncertainty principle says." Write a two-paragraph response. In the first paragraph, state what is physically correct. In the second, explain what is wrong and give the correct Kennard inequality statement. *Difficulty: Apply.*

6. *[Tests: units and dimensional reasoning]* A wave function is given numerically on a grid with $x$ in meters. The peak value of $|\psi|^2$ at $t = 0$ is $3.2 \times 10^9$ m$^{-1}$. (a) Is this a valid probability density? Why? (b) Estimate the probability of finding the particle within $\pm 0.1$ nm of the peak, assuming $|\psi|^2$ is roughly constant over that interval. (c) Someone says the wave function is "unnormalized by a factor of 2." What does this mean precisely, and what is the corrected peak density? *Difficulty: Apply.*

**Produce-something**

7. *[Tests: Born rule in momentum space]* Define $\phi(p) = (1/\sqrt{2\pi\hbar})\int_{-\infty}^{\infty}\psi(x)\,e^{-ipx/\hbar}\,dx$. For the Gaussian $\psi(x) = (\pi a^2)^{-1/4}\,e^{-x^2/(2a^2)}\,e^{ik_0 x}$, show by direct Fourier transform that $\phi(p)$ is itself a Gaussian centered at $p = \hbar k_0$ with width $\hbar/a$. Then compute $\int|\phi(p)|^2\,dp$ and verify it equals 1. *Difficulty: Apply+.*

8. *[Tests: combining normalization proof with physical interpretation]* The continuity equation says $\partial_t|\psi|^2 = -\partial_x J$. (a) Suppose $J(x,t) > 0$ in some interval $[a,b]$ and $J = 0$ outside. Sketch how $|\psi|^2$ evolves near $[a,b]$ over a short time $\delta t$. (b) Suppose $J > 0$ on the left half of the interval and $J < 0$ on the right half. Where does $|\psi|^2$ increase? Where does it decrease? (c) Use this reasoning to explain, without equations, why a wave packet moving to the right has $J > 0$ in the high-probability region. *Difficulty: synthesis.*

**Challenge**

9. *[Tests: limits of the formalism]* The plane wave $\psi(x) = e^{ikx}$ has $|\psi|^2 = 1$ everywhere. (a) Show it cannot be normalized on $(-\infty,\infty)$. (b) Compute $\langle p\rangle$ formally using $\hat{p} = -i\hbar\,\partial_x$. (c) In what sense is the plane wave a state of "definite momentum $\hbar k$"? In what sense is this statement physically problematic, given the Born rule? (d) Propose how plane waves could serve as building blocks for normalizable wave functions. (This is the direction Chapter 4 develops.) *Difficulty: challenge.*

---

## Still Puzzling

**Can Born's rule be derived?** The Born rule is taken as a postulate in this book — a law that must be assumed, not proved. Other research programs (Zurek's "envariance" argument, various many-worlds branch-counting schemes) claim to derive it from more primitive axioms. Whether these derivations succeed or merely relocate the mystery is genuinely contested among physicists. The chapter states the postulate honestly and does not pretend the argument is closed.

**What does it mean for $\psi$ to "collapse" on measurement?** Born's rule predicts the probability distribution for the result of a position measurement. After you measure and get a result $x_0$, what is $\psi$ then? The standard answer (Copenhagen) is that $\psi$ "collapses" to a state localized near $x_0$. This is convenient for subsequent calculations, but the physical mechanism — if there is one — remains deeply debated.

**Why does which-path information destroy interference?** If you detect which slit each electron passes through, the interference pattern vanishes, replaced by two classical blobs. The Born rule predicts the outcome but does not explain, at the level of mechanism, *why* the knowledge of the path removes the fringes. Different interpretations (Copenhagen, many-worlds, pilot wave) give different answers.

**Is the probability current $J$ really "flowing" probability?** The continuity equation $\partial_t|\psi|^2 + \partial_x J = 0$ has the form of a conservation law, and $J$ has all the mathematical properties of a current. But in a single-particle interpretation, what exactly is flowing? For one particle, $|\psi|^2$ is not a density of a fluid — it is a probability distribution. The fluid interpretation is evocative and useful; it is not unambiguous.

---

## The +1 — Simulation Exercise: The Probability Explorer

The deliverable for this chapter is `03-probability-explorer.html`: a wave-function gallery with three stacked SVG panels (Re $\psi$, Im $\psi$, $|\psi|^2$) and a live numerical panel showing $\langle x\rangle$, $\langle p\rangle$, $\sigma_x$, $\sigma_p$, and the ratio $\sigma_x\sigma_p/(\hbar/2)$ — which reads 1.000 for the Gaussian.

### The Claude Prompt

````
SHOW.
The Born rule for a one-dimensional particle:
  P(x, t) dx = |ψ(x, t)|² dx,  with ∫ |ψ|² dx = 1.
Position and momentum expectation values:
  ⟨x⟩  = ∫ x |ψ|² dx
  ⟨x²⟩ = ∫ x² |ψ|² dx
  ⟨p⟩  = ∫ ψ* (−i ℏ ∂/∂x) ψ dx
  ⟨p²⟩ = ∫ ψ* (−ℏ² ∂²/∂x²) ψ dx
  σ_x = √(⟨x²⟩ − ⟨x⟩²),  σ_p = √(⟨p²⟩ − ⟨p⟩²).
Uncertainty principle: σ_x σ_p ≥ ℏ/2, saturated by the Gaussian.

Wave function gallery (selectable by dropdown):
  1. Gaussian: ψ(x) = (1/(πa²))^(1/4) exp(−x²/(2a²)) exp(i k₀ x)
     — sliders: a (0.1 to 5 nm), k₀ (−20 to +20 nm⁻¹)
  2. Infinite-well eigenstate n (within 0 ≤ x ≤ L):
     ψ_n(x) = √(2/L) sin(nπx/L) for n = 1..10
     — sliders: n (1..10 integer), L (1 to 20 nm)
  3. Double Gaussian:
     ψ(x) ∝ exp(−(x−d)²/(2σ²)) + exp(−(x+d)²/(2σ²))
     — sliders: d (separation, 0.5 to 5 nm), σ (0.2 to 2 nm)
  4. Square pulse: ψ(x) = 1/√w for −w/2 < x < w/2, else 0
     — slider: w (0.5 to 10 nm)

SAY.
Produce a single file `03-probability-explorer.html`.

Layout:
  Left column (700 px wide):
    Three stacked SVG panels (each 130 px tall) sharing an x-axis:
      Top:    Re ψ(x)   in orange
      Middle: Im ψ(x)   in gray dashed
      Bottom: |ψ(x)|²   in blue filled
  Right column (300 px wide), live numerical readouts:
      ∫|ψ|² dx       (normalization indicator, must read 1.000)
      ⟨x⟩            (in nm)
      ⟨x²⟩           (in nm²)
      σ_x            (in nm)
      ⟨p⟩            (in ℏ/nm)
      ⟨p²⟩           (in (ℏ/nm)²)
      σ_p            (in ℏ/nm)
      σ_x σ_p / (ℏ/2)   (DIMENSIONLESS, prominent, large font)
  Below: wave-function dropdown + sliders that update based on selection.

CONSTRAIN.
- D3 v7 from CDN. SVG only. Vanilla JS. Single self-contained .html file.
- N = 500 grid points on x ∈ [−20 nm, +20 nm].
- ⟨x⟩, ⟨x²⟩, ∫|ψ|² via Simpson's rule.
- ⟨p⟩, ⟨p²⟩, σ_p via FFT (fft-js from CDN). FFT convention documented.
  Forward convention: sum_n ψ_n e^(−i k_m x_n) · Δx / √(2πℏ). Comment it.
- Complex storage: every ψ array is two parallel Float64Arrays (re, im).
  NEVER collapse to a real-only function.
- Momentum operator p̂ = −i ℏ ∂/∂x. Sign is critical: k₀ > 0 must give ⟨p⟩ > 0.
- The σ_x σ_p / (ℏ/2) display must read 1.000 for the Gaussian.
  If it reads 0.500, you divided by ℏ instead of ℏ/2 — fix.
- For the square pulse: σ_p diverges (Fourier transform decays as 1/p).
  Display the ratio as "undefined," not as a large finite number.
- Every numerical display must include units.

VERIFY.
After writing the file, provide four checks:
(a) Gaussian with a = 1 nm, k₀ = 10 nm⁻¹:
    σ_x = 1/√2 ≈ 0.707 nm; σ_p = ℏ/(√2 · 1 nm) ≈ 0.707 ℏ/nm; ratio = 1.000.
(b) Gaussian with a = 0.5 nm, k₀ = 10 nm⁻¹:
    σ_x = 0.354 nm; σ_p doubles; product unchanged; ratio = 1.000.
(c) Infinite-well n=1 in L=10 nm:
    ⟨x⟩ = 5 nm by symmetry;
    σ_x = L · √(1/12 − 1/(2π²)) ≈ 1.81 nm;
    σ_p = πℏ/L ≈ 0.314 ℏ/nm; ratio ≈ 1.136.
(d) Double Gaussian d = 2 nm, σ = 0.5 nm:
    ⟨x⟩ = 0 by symmetry; probability in [−0.5 nm, +0.5 nm] is small.

Then list known LLM failure modes and confirm which you have guarded against:
  - ψ vs. |ψ|² render swap (|ψ|² panel showing a signed curve).
  - Lost imaginary part (Im ψ = 0 for k₀ ≠ 0 Gaussian).
  - Sign error in p̂ (⟨p⟩ < 0 for k₀ > 0).
  - Simpson drift: ⟨x⟩ not at center for symmetric ψ.
  - FFT convention mismatch: σ_p off by √(2π) or √ℏ.
  - Missing units on numerical readouts.
  - σ_x σ_p / (ℏ/2) = 0.500 for Gaussian (dividing by ℏ not ℏ/2).
````

### Exploration Tasks

**Saturate the bound.** Select the Gaussian. Vary $a$ from 0.2 nm to 4 nm. Watch $\sigma_x$ change. Watch $\sigma_p$ change inversely. Watch $\sigma_x\sigma_p/(\hbar/2)$ stay locked at 1.000. Write down what this confirms about the relationship between the width in position space and the width in momentum space.

**Exceed the bound.** Switch to the infinite-well eigenstate, $n = 1$, $L = 10$ nm. The ratio should read approximately 1.136. Now run $n$ from 2 to 10. As $n$ grows, $\sigma_p$ grows (higher energy means larger momentum spread) while $\sigma_x$ changes little. Does $\sigma_x\sigma_p/(\hbar/2)$ grow without bound, approach a limit, or oscillate? Predict first, then check.

**The double-peaked trap.** Select the double Gaussian with $d = 2$ nm, $\sigma = 0.3$ nm. $\langle x\rangle$ reads 0. Look at $|\psi|^2$: the probability of finding the particle within $\pm 0.5$ nm of $x = 0$ is small — the peaks are at $\pm 2$ nm. Write one sentence explaining what this tells you about using $\langle x\rangle$ as a prediction for a single measurement.

**The square-pulse singularity.** Select the square pulse, width $w = 2$ nm. $\sigma_x$ is finite. $\sigma_p$ should display as "undefined." This is not a bug — the Fourier transform of a discontinuous square pulse decays as $1/p$, making $\int p^2|\phi(p)|^2\,dp$ diverge. The divergence is real physics; it reflects the infinite amount of momentum required to produce sharp edges in position space.

---

## References

Born, M. (1926). Zur Quantenmechanik der Stoßvorgänge. *Zeitschrift für Physik*, 38, 803–827. [The footnote changing $\psi$ to $|\psi|^2$ appears here.] [verify: journal, volume, page confirmed; Nobel records confirm 1954 prize]

Kennard, E. H. (1927). Zur Quantenmechanik einfacher Bewegungstypen. *Zeitschrift für Physik*, 44, 326–352. [verify]

Robertson, H. P. (1929). The uncertainty principle. *Physical Review*, 34, 163–164. [Generalization to arbitrary observables.] [verify: journal and year confirmed]

Ozawa, M. (2003). Universally valid reformulation of the Heisenberg uncertainty principle on noise and disturbance in measurement. *Physical Review A*, 67, 042105. doi:10.1103/PhysRevA.67.042105

Erhart, J., Sponar, S., Sulyok, G., Badurek, G., Ozawa, M., & Hasegawa, Y. (2012). Experimental demonstration of a universally valid error-disturbance uncertainty relation. *Nature Physics*, 8, 185–189. doi:10.1038/nphys2194 [verify]

Griffiths, D. J., & Schroeter, D. F. (2018). *Introduction to Quantum Mechanics* (3rd ed.). Cambridge University Press. §1.1–1.6.

Sakurai, J. J., & Napolitano, J. (2021). *Modern Quantum Mechanics* (3rd ed.). Cambridge University Press. §1.6.

Ballentine, L. E. (2014). *Quantum Mechanics: A Modern Development* (2nd ed.). World Scientific. §3.1.

Feynman, R. P., Leighton, R. B., & Sands, M. (1965). *The Feynman Lectures on Physics*, Vol. III. Addison-Wesley. §1-1. [The fundamental mystery framing.]
