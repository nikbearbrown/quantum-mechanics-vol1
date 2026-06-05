# Worked Exercises: The Wave Function and Born's Rule
*Chapter 3 of Quantum Mechanics — Volume 1*

> These exercises follow a research-backed sequence: full worked example → matched practice → completion problem → error-recognition → transfer → interleaved review. Each section builds on the previous. Do not skip ahead.

## Prerequisites

- The Born rule: $|\psi(x,t)|^2$ is a probability *density* (per unit length), and $P(\text{particle in }[a,b]) = \int_a^b|\psi|^2\,dx$, with the normalization $\int_{-\infty}^{\infty}|\psi|^2\,dx = 1$.
- Expectation values $\langle x\rangle = \int x|\psi|^2\,dx$ and $\langle p\rangle = \int \psi^*(-i\hbar\,\partial_x)\psi\,dx$, the spreads $\sigma_x = \sqrt{\langle x^2\rangle - \langle x\rangle^2}$ and $\sigma_p$, and the Kennard inequality $\sigma_x\sigma_p \geq \hbar/2$.
- That all directional/momentum information lives in the phase: a real $\psi$ has zero probability current $J = (\hbar/m)\,\text{Im}(\psi^*\,\partial_x\psi)$.

---

## Part A — Full Worked Example

**What this demonstrates:** How to normalize a wave function and extract a genuine probability from the probability *density* — the chapter's central distinction.

**The problem:** Take the un-normalized wave function $\tilde\psi(x) = e^{-|x|/a}$ for real $a > 0$ (the chapter's worked example). (1) Find the normalization constant $A$ so that $\psi = A\,e^{-|x|/a}$ satisfies $\int|\psi|^2\,dx = 1$. (2) Compute the probability of finding the particle in the interval $[-a, a]$. (3) Evaluate $|\psi(0)|^2$ for $a = 0.5$ nm and explain why a value greater than 1 violates nothing.

**The solution:**

**Step 1 — Set up the normalization integral, splitting at the absolute value.**
$$A^2\int_{-\infty}^{\infty}e^{-2|x|/a}\,dx = 2A^2\int_0^{\infty}e^{-2x/a}\,dx.$$
*Why:* The Born rule demands $\int|\psi|^2\,dx = 1$, and $|\psi|^2 = A^2 e^{-2|x|/a}$. The split at $x = 0$ is mandatory because $e^{-|x|/a} \neq e^{-x/a}$ for $x < 0$; by symmetry the two halves are equal, giving the factor of 2. *Check:* The integrand $e^{-2|x|/a}$ is even and decays — the integral converges, as it must for a normalizable state.

**Step 2 — Evaluate and solve for $A$.**
$$2A^2\int_0^{\infty}e^{-2x/a}\,dx = 2A^2\cdot\frac{a}{2} = A^2 a = 1 \implies A = \frac{1}{\sqrt{a}}.$$
*Why:* $\int_0^\infty e^{-2x/a}dx = a/2$. Setting the total probability to 1 fixes $A$ uniquely (up to an unobservable global phase). *Check the units:* $x$ and $a$ in nm, so $A$ is in nm$^{-1/2}$ and $|\psi|^2 = A^2 e^{-2|x|/a}$ is in nm$^{-1}$ — correct for a one-dimensional probability density.

**Step 3 — Compute the probability in $[-a, a]$ by integrating the density.**
$$P = A^2\int_{-a}^{a}e^{-2|x|/a}\,dx = \frac{1}{a}\cdot 2\int_0^{a}e^{-2x/a}\,dx = \frac{2}{a}\cdot\frac{a}{2}\left(1 - e^{-2}\right) = 1 - e^{-2}.$$
$$P = 1 - e^{-2} \approx 1 - 0.135 = 0.865.$$
*Why:* A probability — a real dimensionless number between 0 and 1 — is obtained only by *integrating* the density over a region, never by reading the density at a point. This is the whole content of the Born rule. *Check:* $0 < 0.865 < 1$, and the interval $[-a,a]$ contains the peak of the distribution, so a probability near 87% is plausible; the remaining ~14% lives in the tails $|x| > a$.

**Step 4 — Evaluate the density at the origin and interpret a value above 1.** At $x = 0$, $|\psi(0)|^2 = A^2 = 1/a$. For $a = 0.5$ nm:
$$|\psi(0)|^2 = \frac{1}{0.5\ \text{nm}} = 2\ \text{nm}^{-1}.$$
*Why:* $|\psi|^2$ is a probability *per unit length*, like population per square kilometer — not a headcount. It carries units of nm$^{-1}$ and is not required to be $\leq 1$. Expecting $|\psi|^2 \leq 1$ everywhere is a unit confusion. *Check:* The dimension is nm$^{-1}$, not dimensionless, so comparing it to the pure number 1 is meaningless — exactly the point the chapter stresses.

**Final answer:** $A = 1/\sqrt{a}$; $P(-a \leq x \leq a) = 1 - e^{-2} \approx 0.865$; $|\psi(0)|^2 = 2$ nm$^{-1}$ for $a = 0.5$ nm, which is a perfectly valid density despite exceeding 1.

**What made this work:** The central concept is that $|\psi|^2$ is a *density*, not a probability — to get a probability you integrate it over a region, and the density itself can exceed 1 because it carries units of inverse length. A naive approach that reads "the probability the particle is at $x = 0$" off the value $|\psi(0)|^2 = 2$ commits a unit error (a density is not a probability) and, worse, would conclude the wave function is "impossible" because 2 > 1 — the single most common first mistake the chapter warns against.

**Self-explanation prompt:** Explain, using the population-density analogy from the chapter, why $|\psi(0)|^2 = 2$ nm$^{-1}$ is no more paradoxical than a city block having a population density of 50,000 people per km$^2$.

---

## Part B — Matched Practice Problem

**What this demonstrates:** The same normalize-then-integrate procedure with a different functional form.

**The problem:** Consider the un-normalized wave function $\tilde\psi(x) = e^{-x^2/(2a^2)}$ (a real Gaussian, no momentum factor) for real $a > 0$. (1) Find the normalization constant $A$ so that $\psi = A\,e^{-x^2/(2a^2)}$ satisfies $\int|\psi|^2\,dx = 1$. (You may use $\int_{-\infty}^{\infty}e^{-x^2/a^2}\,dx = a\sqrt{\pi}$.) (2) Compute the probability of finding the particle within $[-a, a]$, leaving it in terms of the error function if needed, or estimate it numerically. (3) Evaluate $|\psi(0)|^2$ for $a = 0.5$ nm and confirm it is a valid density even if it exceeds 1.

Work it in the same four steps: set up $\int|\psi|^2\,dx = 1$; solve for $A$ (checking units); integrate the density over $[-a,a]$; evaluate and interpret $|\psi(0)|^2$.

**Stuck?** Start from $A^2\int_{-\infty}^{\infty}e^{-x^2/a^2}\,dx = 1$ and use the given Gaussian integral to read off $A$ immediately; remember $A$ should carry units of nm$^{-1/2}$.

*Instructor note: No solution is provided for Part B. Students should complete it independently using the structure of Part A as a model.*

---

## Part C — Completion Problem

**The problem:** For the infinite-square-well ground state $\psi_1(x) = \sqrt{2/L}\,\sin(\pi x/L)$ on $[0, L]$ (zero elsewhere), compute $\langle x\rangle$ and explain why $\langle p\rangle = 0$, then find $\sigma_x$.

**Step 1 — Confirm normalization and set up $\langle x\rangle$.** The state is already normalized: $\int_0^L (2/L)\sin^2(\pi x/L)\,dx = 1$. The expectation of position is
$$\langle x\rangle = \int_0^L x\,|\psi_1|^2\,dx = \frac{2}{L}\int_0^L x\,\sin^2\!\left(\frac{\pi x}{L}\right)dx.$$
*Why:* $\langle x\rangle$ is the centroid (mean) of the probability distribution $|\psi_1|^2$, each position weighted by how probable it is — the ordinary statistical mean.

**Step 2 — Use symmetry to evaluate $\langle x\rangle$.** The density $|\psi_1|^2 = (2/L)\sin^2(\pi x/L)$ is symmetric about the center $x = L/2$ of the well. Therefore
$$\langle x\rangle = \frac{L}{2}.$$
*Why:* For any distribution symmetric about a point, the mean sits at that point of symmetry — no integration needed once the symmetry is recognized.

**Step 3 — [BLANK] Explain why $\langle p\rangle = 0$ for this standing wave.** (Use $\hat p = -i\hbar\,\partial_x$ and the fact that $\psi_1$ is real-valued.)

*Your work here:*

_______________________________________________

*Why (your explanation):*

_______________________________________________

**Step 4 — [BLANK] Compute $\langle x^2\rangle$ and then $\sigma_x = \sqrt{\langle x^2\rangle - \langle x\rangle^2}$.** (You may use $\langle x^2\rangle = L^2(1/3 - 1/(2\pi^2))$ for this state.)

*Your work here:*

_______________________________________________

*Why (your explanation):*

_______________________________________________

**Step 5 — Assemble the result.** With $\langle x\rangle = L/2$ and $\langle x^2\rangle = L^2(1/3 - 1/(2\pi^2))$,
$$\sigma_x = \sqrt{L^2\left(\tfrac{1}{3} - \tfrac{1}{2\pi^2}\right) - \tfrac{L^2}{4}} = L\sqrt{\tfrac{1}{12} - \tfrac{1}{2\pi^2}} \approx 0.181\,L.$$
For $L = 10$ nm this is $\sigma_x \approx 1.81$ nm — matching the chapter's value for this state.

**Final answer:** $\langle x\rangle = L/2$; $\langle p\rangle = 0$ because $\psi_1$ is real, so its probability current vanishes and there is no net motion in either direction; $\sigma_x = L\sqrt{1/12 - 1/(2\pi^2)} \approx 0.181\,L$ ($\approx 1.81$ nm for $L = 10$ nm).

**Self-explanation prompt:** Explain why a standing wave with $\langle p\rangle = 0$ is *not* a particle "sitting still" — what does $\sigma_p > 0$ tell you about the spread of momentum measurements even though the average is zero?

---

## Part D — Error-Recognition Problem

> **Use this section only after completing Parts A–C.**

**The problem:** A student is asked to find $\langle x\rangle$ for the wave function $\psi(x) = N\,x\,e^{-x^2/(2a^2)}$ on $(-\infty, \infty)$, where $N$ is a normalization constant and $a > 0$.

**Step 1 (correct):** This $\psi$ is an *odd* function of $x$ (it is $x$ times an even Gaussian), so $|\psi|^2 = N^2 x^2 e^{-x^2/a^2}$ is even.

**Step 2 (correct):** Normalization requires $N^2\int_{-\infty}^{\infty}x^2 e^{-x^2/a^2}\,dx = 1$, which fixes $N$ to a positive real number (its exact value will not be needed for $\langle x\rangle$).

**⚠ Step 3 (contains an error):** "To find the average position, I integrate $\psi$ against $x$ directly: $\langle x\rangle = \int_{-\infty}^{\infty} x\,\psi(x)\,dx = N\int_{-\infty}^{\infty} x^2 e^{-x^2/(2a^2)}\,dx$. This integral is positive, so $\langle x\rangle > 0$."

**Step 4 (correct-looking):** "Since the result is a clean positive number, the particle is on average displaced to the right of the origin."

**Your tasks:**
1. Identify the error in Step 3 and explain why it is wrong.
2. Write the corrected Step 3.
3. State the physical principle that Step 3 violates.
4. Describe a check or test that would catch this class of error.

*Answers:*
1. **The error:** The student computed $\int x\,\psi\,dx$ — using $\psi$ itself instead of the probability density $|\psi|^2 = \psi^*\psi$. The Born rule weights position by the *density* $|\psi|^2$, not by $\psi$. (Here $\psi$ is real so the dropped factor is $\psi^*$, but the formula $\langle x\rangle = \int\psi^* x\psi\,dx$ requires the conjugate in general.) The student's integral $\int x\psi\,dx = N\int x^2 e^{-x^2/2a^2}dx$ is not an expectation value at all.
2. **Corrected Step 3:** $\langle x\rangle = \int_{-\infty}^{\infty} x\,|\psi|^2\,dx = N^2\int_{-\infty}^{\infty} x\cdot x^2 e^{-x^2/a^2}\,dx = N^2\int_{-\infty}^{\infty} x^3 e^{-x^2/a^2}\,dx$. The integrand $x^3 e^{-x^2/a^2}$ is *odd*, so the integral over the symmetric domain is exactly 0. Thus $\langle x\rangle = 0$.
3. **Principle violated:** The Born rule — expectation values are computed with the probability density $|\psi|^2 = \psi^*\psi$, i.e. $\langle x\rangle = \int\psi^* x\psi\,dx$, *not* $\int x\psi\,dx$. Treating $\psi$ as though it were the probability density (and dropping $\psi^*$) is exactly the misconception the chapter flags.
4. **A check to catch this:** Use symmetry as a sanity test before integrating. Since $|\psi|^2$ is even (symmetric about $x = 0$), $\langle x\rangle$ *must* be 0 by symmetry — any nonzero answer signals a setup error. More generally, confirm the integrand of $\langle x\rangle$ is $x|\psi|^2$ and carries units that integrate to nm.

**Why this error is common:** Students conflate the amplitude $\psi$ with the probability density $|\psi|^2$ and forget the complex conjugate $\psi^*$ in $\langle x\rangle = \int\psi^* x\psi\,dx$ — the chapter calls confusing $\psi$ with $|\psi|^2$ "the single most common first mistake."

---

## Part E — Transfer Problem

**The problem:** A particle is described by the symmetric "double Gaussian" $\psi(x) \propto e^{-(x-d)^2/(2\sigma^2)} + e^{-(x+d)^2/(2\sigma^2)}$ with $d = 2$ nm and $\sigma = 0.5$ nm — a two-peaked state never worked through in the examples above. (a) Without doing any integral, state the value of $\langle x\rangle$ and justify it by symmetry. (b) Argue that the probability of finding the particle within $\pm 0.5$ nm of the origin is *small*, even though $\langle x\rangle$ sits exactly at the origin. (c) Explain in one sentence what this reveals about using $\langle x\rangle$ as a prediction for a single position measurement.

**Hint (use only if stuck after 10 minutes):** The density $|\psi|^2$ has two peaks at $x = \pm d = \pm 2$ nm, with very little weight near $x = 0$ because the Gaussians (width $\sigma = 0.5$ nm) barely reach the origin from $\pm 2$ nm away. The mean of a two-peaked symmetric distribution lands in the empty valley between the peaks.

**Reflection prompt:** (1) How can the average position $\langle x\rangle = 0$ be a place the particle is almost *never* found? (2) What additional statistic ($\sigma_x$, or the full $|\psi|^2$) would you report to avoid being misled by the centroid alone?

---

## Part F — Interleaved Review

**Problem F1.** A particle has the Gaussian wave function $\psi(x) = (\pi a^2)^{-1/4}\,e^{-x^2/(2a^2)}\,e^{ik_0 x}$ with $a = 1$ nm and $k_0 = 10$ nm$^{-1}$. (a) Compute $\sigma_x$ and $\sigma_p$ using the chapter's results $\sigma_x = a/\sqrt2$ and $\sigma_p = \hbar/(\sqrt2\,a)$. (b) Form the product $\sigma_x\sigma_p$ and confirm it equals $\hbar/2$ exactly. (c) State why the Gaussian, and only the Gaussian, saturates the Kennard bound.
*Chapter this draws from: Chapter 3 (The Wave Function and Born's Rule).*

**Problem F2.** The state of definite momentum is the plane wave $\psi(x) \propto e^{ik_0 x}$ with spatial period $\lambda = 2\pi/k_0$. (a) Using the de Broglie relation, identify the momentum $p$ associated with this plane wave in terms of $k_0$ and $\hbar$. (b) Explain why this plane wave "extends over all space" and therefore cannot be normalized on $(-\infty,\infty)$, connecting it to the chapter's remark that localizing a particle requires superposing a *range* of momenta.
*Chapter this draws from: Chapter 2 (Matter Waves) — the de Broglie relation $\lambda = h/p = 2\pi\hbar/p$ and the plane wave $e^{ipx/\hbar}$.*

**Problem F3 (discrimination).** A student is given $\psi(x) = N\,e^{-x^2/(2a^2)}\,e^{ik_0 x}$ with $k_0 = 5$ nm$^{-1}$ and asked, "What is the central wavelength of this state, and what is the probability of finding the particle in the central nanometer?" The student computes the de Broglie wavelength $\lambda = 2\pi/k_0$ and reports *that* as the answer to the probability question. Decide which part of the question is a Chapter 2 (de Broglie wavelength) task and which is a Chapter 3 (Born-rule probability) task, and answer each correctly.
*Note to instructor: intentionally ambiguous — the presence of $e^{ik_0 x}$ and the word "wavelength" cue the de Broglie method, but the *probability* sub-question requires integrating $|\psi|^2$ over the interval (Born rule), which is unrelated to $\lambda = 2\pi/k_0$. The wavelength is $\lambda = 2\pi/5 \approx 1.26$ nm; the probability requires $\int_{-0.5}^{0.5}|\psi|^2\,dx$ after normalizing.*

**After F1–F3:** Reflect on how you separated "find the wavelength" (a de Broglie / phase question from Chapter 2) from "find the probability" (a Born-rule / $|\psi|^2$ question from Chapter 3) in F3. Which surface feature — the oscillating factor $e^{ik_0 x}$, the word "wavelength," the word "probability" — pointed to which chapter's method?

---

## Instructor Notes

**Common errors to watch for:**
- Treating $\psi$ as the probability (computing $\int x\psi\,dx$ or reading $\psi$ off as a probability) instead of using $|\psi|^2 = \psi^*\psi$, and dropping the complex conjugate $\psi^*$ in $\langle x\rangle = \int\psi^* x\psi\,dx$ (the Part D misconception).
- Forgetting to normalize before computing a probability or expectation value — using a $\tilde\psi$ whose $\int|\tilde\psi|^2\,dx \neq 1$.
- Reading the value of the density $|\psi|^2$ at a point as a probability, and panicking when it exceeds 1 — a unit confusion (density is per unit length, not dimensionless).

**Signs a student needs to return to the chapter:**
- They claim a wave function is "impossible" because $|\psi|^2 > 1$ somewhere (the chapter's $e^{-|x|/a}$ example has $|\psi(0)|^2 = 2$ nm$^{-1}$ and is perfectly valid).
- They report a nonzero $\langle x\rangle$ for a state whose $|\psi|^2$ is symmetric about the origin (a symmetry check should immediately flag this).

**Scaffolding adjustments:** *If a student struggles with Part A,* have them first carry units through explicitly — write nm above every $x$ and $a$, confirm $A$ comes out in nm$^{-1/2}$ and $|\psi|^2$ in nm$^{-1}$ — before attempting any probability integral. *If a student finishes Part F quickly,* have them verify by direct Fourier transform that the Gaussian's momentum-space wave function $\phi(p)$ is itself a Gaussian centered at $\hbar k_0$ with width $\hbar/a$, confirming it saturates the Kennard bound from the momentum side too.

**Domain adaptation note:** In any Born-rule problem, the first move is to confirm the state is normalized and that you are integrating $x\,|\psi|^2$ (density, with the conjugate built in) — never $x\,\psi$ — because the difference between $\psi$ and $|\psi|^2$ is the defining content of this chapter.
