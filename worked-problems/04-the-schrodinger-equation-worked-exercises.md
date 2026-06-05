# Worked Exercises: The Schrödinger Equation and Stationary States
*Chapter 4 of Quantum Mechanics — Volume 1*

> These exercises follow a research-backed sequence: full worked example → matched practice → completion problem → error-recognition → transfer → interleaved review. Each section builds on the previous. Do not skip ahead.

## Prerequisites

- The time-dependent Schrödinger equation $i\hbar\,\partial_t\Psi = \hat H\Psi$, the product ansatz $\Psi(x,t) = \psi(x)\phi(t)$, and the separation that yields the universal time factor $\phi(t) = e^{-iEt/\hbar}$ and the TISE $\hat H\psi = E\psi$.
- The stationary state $\Psi_n(x,t) = \psi_n(x)\,e^{-iE_nt/\hbar}$, its frozen probability density $|\Psi_n|^2 = |\psi_n|^2$, and the energy result $\langle\hat H\rangle = E_n$ with zero variance.
- The superposition rule $\langle\hat H\rangle = \sum_n|c_n|^2 E_n$ (constant in time), the beat frequency $\omega_{12} = (E_2 - E_1)/\hbar$, and the infinite-well spectrum $E_n = n^2\pi^2\hbar^2/(2mL^2)$, $\psi_n = \sqrt{2/L}\sin(n\pi x/L)$.

---

## Part A — Full Worked Example

**What this demonstrates:** How separation of variables turns the hard time-dependent Schrödinger equation into the eigenvalue problem (TISE) plus a universal rotating phase, and what "stationary" then means.

**The problem:** For the infinite square well of width $L$ (the chapter's running example), take the ground state $\psi_1(x) = \sqrt{2/L}\sin(\pi x/L)$ on $[0,L]$. (1) Use separation of variables to write down the full time-dependent stationary state $\Psi_1(x,t)$. (2) Show its probability density $|\Psi_1|^2$ is time-independent. (3) Show that the energy expectation $\langle\hat H\rangle = E_1$ with zero variance, so every energy measurement returns exactly $E_1$.

**The solution:**

**Step 1 — Separate the time dependence.** The potential is static ($V = 0$ inside, $V = \infty$ at the walls), so the product ansatz $\Psi(x,t) = \psi(x)\phi(t)$ applies. Substituting into $i\hbar\,\partial_t\Psi = \hat H\Psi$ and dividing by $\psi\phi$ gives
$$i\hbar\,\frac{\phi'(t)}{\phi(t)} = \frac{\hat H\psi(x)}{\psi(x)} = E,$$
a function of $t$ alone equal to a function of $x$ alone, hence both equal a constant $E$.
*Why:* The left side depends only on $t$ and the right only on $x$; equality for all $x$ and $t$ forces both to a separation constant $E$ — this is the move that "factors out" the time evolution. *Check:* The construction is only valid because $V = V(x)$ is time-independent; for a static well the ansatz is exact.

**Step 2 — Solve the time equation and attach the phase.** The time equation $i\hbar\,\phi'(t) = E\phi(t)$ integrates to $\phi(t) = e^{-iEt/\hbar}$. With the ground-state energy $E_1 = \pi^2\hbar^2/(2mL^2)$, the full stationary state is
$$\Psi_1(x,t) = \sqrt{\frac{2}{L}}\,\sin\!\left(\frac{\pi x}{L}\right)\,e^{-iE_1 t/\hbar}.$$
*Why:* The phase $e^{-iEt/\hbar}$ is universal — the same form regardless of potential or energy level — and its sign is fixed by the TDSE (it is $-iEt/\hbar$, not $+$). *Check:* The phase has magnitude $|e^{-iE_1t/\hbar}| = 1$, so it cannot change the total probability — a necessary consistency condition.

**Step 3 — Compute the probability density and show it is frozen.**
$$|\Psi_1(x,t)|^2 = |\psi_1(x)|^2\cdot|e^{-iE_1t/\hbar}|^2 = \frac{2}{L}\sin^2\!\left(\frac{\pi x}{L}\right)\cdot 1 = \frac{2}{L}\sin^2\!\left(\frac{\pi x}{L}\right).$$
No $t$ appears.
*Why:* The rotating phase is a *global* phase for a single eigenstate; it multiplies $\psi_n$ uniformly and cancels in $|\Psi|^2$. This is exactly what "stationary" means — the probability distribution does not move, even though the wave function itself spins in the complex plane. *Check:* $\int_0^L|\Psi_1|^2\,dx = (2/L)\int_0^L\sin^2(\pi x/L)\,dx = (2/L)(L/2) = 1$ — normalized and time-independent.

**Step 4 — Compute the energy expectation and its variance.** For the stationary state,
$$\langle\hat H\rangle = \int\Psi_1^*\,\hat H\,\Psi_1\,dx.$$
The conjugate phase $e^{+iE_1t/\hbar}$ and the state phase $e^{-iE_1t/\hbar}$ multiply to 1; the eigenvalue equation $\hat H\psi_1 = E_1\psi_1$ pulls $E_1$ out; normalization gives
$$\langle\hat H\rangle = E_1\int|\psi_1|^2\,dx = E_1.$$
The variance is $\langle\hat H^2\rangle - \langle\hat H\rangle^2 = E_1^2 - E_1^2 = 0$.
*Why:* Because $\psi_1$ is an eigenstate of $\hat H$, acting with $\hat H$ just multiplies by $E_1$; an eigenstate has a *definite* energy with no spread. *Check:* Zero variance means every measurement returns exactly $E_1$ — the operational meaning of "a state with definite energy," matching the chapter.

**Final answer:** $\Psi_1(x,t) = \sqrt{2/L}\,\sin(\pi x/L)\,e^{-iE_1t/\hbar}$; $|\Psi_1|^2 = (2/L)\sin^2(\pi x/L)$ is time-independent; $\langle\hat H\rangle = E_1$ with zero variance, so every energy measurement yields exactly $E_1 = \pi^2\hbar^2/(2mL^2)$.

**What made this work:** The central concept is that separation of variables splits the time-dependent equation into a universal phase $e^{-iEt/\hbar}$ and an eigenvalue problem $\hat H\psi = E\psi$, and that the rotating phase is a *global* phase for a single eigenstate — unobservable, which is precisely why a stationary state is stationary. A naive approach that forgets the $e^{-iEt/\hbar}$ time factor (treating $\psi_n(x)$ as the full state) loses the distinction between a stationary state and a superposition, and would mispredict the dynamics the moment two eigenstates are combined.

**Self-explanation prompt:** Explain the chapter's image that "the wave function is a clock; the probability density is the clock's shadow on the floor" — why does the shadow stay still while the clock spins, and what breaks this once you mix in a second eigenstate?

---

## Part B — Matched Practice Problem

**What this demonstrates:** The same separation-of-variables and stationary-state analysis for a *higher* eigenstate.

**The problem:** For the same infinite square well of width $L$, take the *second excited state* $\psi_3(x) = \sqrt{2/L}\sin(3\pi x/L)$ with energy $E_3 = 9\pi^2\hbar^2/(2mL^2)$. (1) Write the full stationary state $\Psi_3(x,t)$ using separation of variables. (2) Show $|\Psi_3|^2$ is time-independent. (3) Show $\langle\hat H\rangle = E_3$ with zero variance, and state how many energy measurements out of 1000 would return a value other than $E_3$.

Work it in the same four steps: separate; attach the $e^{-iE_3t/\hbar}$ phase; compute $|\Psi_3|^2$ and show it is frozen; compute $\langle\hat H\rangle$ and the variance.

**Stuck?** The structure is identical to Part A — the only changes are $\psi_1\to\psi_3$ and $E_1\to E_3 = 9E_1$. The phase magnitude is still 1, so $|\Psi_3|^2$ must again be frozen.

*Instructor note: No solution is provided for Part B. Students should complete it independently using the structure of Part A as a model.*

---

## Part C — Completion Problem

**The problem:** Form the equal superposition $\Psi(x,t) = \frac{1}{\sqrt2}\psi_1(x)\,e^{-iE_1t/\hbar} + \frac{1}{\sqrt2}\psi_2(x)\,e^{-iE_2t/\hbar}$ of the infinite-well ground and first excited states. Show that $|\Psi|^2$ now oscillates in time, find the oscillation (beat) frequency, and show that the energy $\langle\hat H\rangle$ is nonetheless constant.

**Step 1 — Write the probability density of the superposition.** With $c_1 = c_2 = 1/\sqrt2$ and both $\psi_1, \psi_2$ real,
$$|\Psi|^2 = \tfrac{1}{2}\psi_1^2 + \tfrac{1}{2}\psi_2^2 + 2\cdot\tfrac{1}{2}\,\psi_1\psi_2\,\text{Re}\!\left[e^{-i(E_2-E_1)t/\hbar}\right].$$
*Why:* Expanding $|\Psi|^2 = \Psi^*\Psi$ produces the two "frozen" diagonal terms plus a cross term; the cross term carries the relative phase $e^{-i(E_2-E_1)t/\hbar}$ — the signature of superposition.

**Step 2 — Simplify the cross term.** Since $\text{Re}[e^{-i(E_2-E_1)t/\hbar}] = \cos((E_2-E_1)t/\hbar)$,
$$|\Psi(x,t)|^2 = \tfrac{1}{2}\left[\psi_1^2 + \psi_2^2 + 2\psi_1\psi_2\cos\!\left(\tfrac{(E_2-E_1)t}{\hbar}\right)\right].$$
*Why:* The two diagonal terms are time-independent; only the interference term oscillates, making the probability "slosh" left and right across the well.

**Step 3 — [BLANK] Identify the beat (oscillation) angular frequency $\omega_{12}$ of $|\Psi|^2$.**

*Your work here:*

_______________________________________________

*Why (your explanation):*

_______________________________________________

**Step 4 — [BLANK] Show that $\langle\hat H\rangle$ is constant in time and equal to $\tfrac{1}{2}(E_1 + E_2)$.** (Hint: use $\langle\hat H\rangle = \sum_n|c_n|^2 E_n$ and explain why the cross terms vanish.)

*Your work here:*

_______________________________________________

*Why (your explanation):*

_______________________________________________

**Step 5 — Interpret the result.** The probability density sloshes back and forth across the well at angular frequency $\omega_{12} = (E_2 - E_1)/\hbar$, while the total energy $\langle\hat H\rangle = \tfrac{1}{2}(E_1 + E_2)$ never changes. This is conservation of energy stated in quantum language: the distribution moves, the energy does not. The superposition is genuinely *not* a stationary state.

**Final answer:** $|\Psi|^2$ oscillates at $\omega_{12} = (E_2 - E_1)/\hbar$; $\langle\hat H\rangle = \tfrac{1}{2}(E_1 + E_2)$, constant in time because the off-diagonal cross terms vanish by orthogonality of $\psi_1$ and $\psi_2$.

**Self-explanation prompt:** Explain why the probability can slosh across the well while the energy stays perfectly fixed — what is the difference between "the distribution moves" and "the energy changes"?

---

## Part D — Error-Recognition Problem

> **Use this section only after completing Parts A–C.**

**The problem:** A student is asked for the energy of the superposition $\Psi(x,t) = \frac{1}{\sqrt2}\psi_1(x)\,e^{-iE_1t/\hbar} + \frac{1}{\sqrt2}\psi_2(x)\,e^{-iE_2t/\hbar}$ in the infinite well, and whether a single energy measurement is certain to return that value.

**Step 1 (correct):** The state is normalized: $|c_1|^2 + |c_2|^2 = \tfrac{1}{2} + \tfrac{1}{2} = 1$.

**Step 2 (correct):** Each $\psi_n$ is an eigenstate of $\hat H$ with $\hat H\psi_n = E_n\psi_n$, where $E_n = n^2\pi^2\hbar^2/(2mL^2)$.

**⚠ Step 3 (contains an error):** "Because $\Psi$ is built from $\psi_1$ and $\psi_2$, it is also an eigenstate of $\hat H$. Its energy eigenvalue is the average of the two: $E = \tfrac{1}{2}(E_1 + E_2)$. Therefore every energy measurement on this state returns exactly $\tfrac{1}{2}(E_1 + E_2)$, with no uncertainty."

**Step 4 (correct-looking):** "The expectation value of the energy is therefore $\langle\hat H\rangle = \tfrac{1}{2}(E_1 + E_2)$, which is constant in time."

**Your tasks:**
1. Identify the error in Step 3 and explain why it is wrong.
2. Write the corrected Step 3.
3. State the physical principle that Step 3 violates.
4. Describe a check or test that would catch this class of error.

*Answers:*
1. **The error:** The student assigned a *single, definite* energy eigenvalue $\tfrac{1}{2}(E_1+E_2)$ to a superposition. A superposition of eigenstates with different energies is **not** an eigenstate of $\hat H$ and has **no definite energy**. The value $\tfrac{1}{2}(E_1+E_2)$ is the *expectation* (average over many measurements), not the result of any single measurement.
2. **Corrected Step 3:** $\Psi$ is not an eigenstate of $\hat H$. A single energy measurement returns $E_1$ with probability $|c_1|^2 = \tfrac{1}{2}$ or $E_2$ with probability $|c_2|^2 = \tfrac{1}{2}$ — never the average. The variance is nonzero: $\langle\hat H^2\rangle - \langle\hat H\rangle^2 = \tfrac{1}{2}E_1^2 + \tfrac{1}{2}E_2^2 - \left[\tfrac{1}{2}(E_1+E_2)\right]^2 = \tfrac{1}{4}(E_2 - E_1)^2 \neq 0$.
3. **Principle violated:** Only an eigenstate of $\hat H$ has a definite energy (zero variance). The expectation $\langle\hat H\rangle = \sum_n|c_n|^2 E_n$ is a *weighted average* of eigenvalues, and a measurement collapses the state to one eigenstate, returning one of the $E_n$. Assigning a single energy to a superposition is exactly the chapter's flagged misconception.
4. **A check to catch this:** Compute the energy variance $\langle\hat H^2\rangle - \langle\hat H\rangle^2$. For a true eigenstate it is 0; here it is $\tfrac{1}{4}(E_2-E_1)^2 > 0$, immediately revealing that the energy is *not* definite. Equivalently, test whether $\hat H\Psi = (\text{const})\Psi$: it does not, because $\hat H\Psi = \tfrac{1}{\sqrt2}E_1\psi_1 e^{-iE_1t/\hbar} + \tfrac{1}{\sqrt2}E_2\psi_2 e^{-iE_2t/\hbar}$ is not proportional to $\Psi$.

**Why this error is common:** Students see that $\langle\hat H\rangle$ is a single number and a constant in time, and wrongly infer that the energy is therefore "definite" — conflating the average over many measurements with the certain result of one, the chapter's exact warning about superpositions having no definite energy.

---

## Part E — Transfer Problem

**The problem:** Consider a two-level system that is *not* a particle in a box — a single qubit (e.g. an electron spin in a magnetic field) with two energy eigenstates $|0\rangle$ and $|1\rangle$ of energies $E_0$ and $E_1$, prepared in the superposition $\Psi(t) = \tfrac{1}{\sqrt2}|0\rangle e^{-iE_0t/\hbar} + \tfrac{1}{\sqrt2}|1\rangle e^{-iE_1t/\hbar}$. (a) Write the probability of measuring energy $E_1$. (b) Show that any observable built only from $|0\rangle\langle0|$ and $|1\rangle\langle1|$ populations is time-independent, but an off-diagonal observable (a "coherence") oscillates at the beat frequency $\omega = (E_1 - E_0)/\hbar$. (c) Identify the qubit analog of the infinite well's "sloshing."

**Hint (use only if stuck after 10 minutes):** The population probabilities are $|c_0|^2 = |c_1|^2 = \tfrac{1}{2}$, both constant — the same frozen diagonal terms as the well. The time dependence lives entirely in the cross (coherence) term $c_0^* c_1\,e^{-i(E_1-E_0)t/\hbar}$, exactly the structure of the chapter's interference term, with $\omega_{12} = (E_1 - E_0)/\hbar$.

**Reflection prompt:** (1) The infinite-well superposition and the qubit superposition share the same mathematical skeleton — frozen populations, an oscillating coherence at the beat frequency. What single feature of *any* two-state superposition produces the oscillation? (2) In the qubit, what plays the role of the spatial "sloshing" of $|\Psi|^2$ across the box?

---

## Part F — Interleaved Review

**Problem F1.** For the infinite well of width $L = 10$ nm holding an electron, compute the beat period $T = 2\pi\hbar/(E_2 - E_1)$ of the $\psi_1 + \psi_2$ superposition. Use $E_n = n^2\pi^2\hbar^2/(2m_eL^2)$, so $E_2 - E_1 = 3\pi^2\hbar^2/(2m_eL^2)$. Express $T$ in femtoseconds.
*Chapter this draws from: Chapter 4 (The Schrödinger Equation and Stationary States).*

**Problem F2.** The chapter notes that the time factor $e^{-iEt/\hbar}$ makes a single eigenstate's $|\Psi|^2$ frozen because $|e^{-iEt/\hbar}|^2 = 1$. (a) For the ground-state stationary state $\Psi_1 = \psi_1(x)e^{-iE_1t/\hbar}$, compute $\langle x\rangle$ at $t = 0$ and at a later time $t$, and confirm it does not change. (b) Then compute $\langle p\rangle$ for this stationary state and explain, using the Born-rule machinery $\langle p\rangle = \int\Psi^*(-i\hbar\,\partial_x)\Psi\,dx$, why a real $\psi_1$ times a pure phase still gives $\langle p\rangle = 0$.
*Chapter this draws from: Chapter 3 (The Wave Function and Born's Rule) — expectation values $\langle x\rangle$, $\langle p\rangle$ with $\hat p = -i\hbar\,\partial_x$, and zero current for a real spatial profile.*

**Problem F3 (discrimination).** A student is told "an electron in the infinite well is in the state $\Psi$ and you measure its energy; what value do you get, and is the result certain?" but is *not* told whether $\Psi$ is a single eigenstate or a superposition. The state is written as $\Psi(x,t) = \sqrt{2/L}\sin(2\pi x/L)\,e^{-iE_2t/\hbar}$. Decide whether this requires the "definite energy" reasoning (single eigenstate) or the "weighted-average / collapse" reasoning (superposition), and answer accordingly.
*Note to instructor: intentionally ambiguous — the elaborate phrasing and the time-phase suggest a possibly non-trivial superposition, but the state IS a single eigenstate ($\psi_2$ times one phase), so the energy is definite, $E = E_2$, returned with certainty and zero variance. The discriminating skill is recognizing one eigenstate (definite energy) versus a sum of eigenstates (no definite energy).*

**After F1–F3:** Reflect on how you decided, in F3, whether the state was a single eigenstate or a superposition. What surface feature — a single $\sin(n\pi x/L)$ term versus a *sum* of such terms, one phase versus several — told you whether to apply "definite energy" or "weighted average and collapse"?

---

## Instructor Notes

**Common errors to watch for:**
- Assigning a single definite energy eigenvalue to a superposition (the Part D misconception) — confusing $\langle\hat H\rangle = \sum|c_n|^2 E_n$ with a certain measurement outcome.
- Omitting the $e^{-iE_nt/\hbar}$ time factor and treating $\psi_n(x)$ as the full state, which erases the distinction between a stationary state and a superposition.
- Getting the phase sign wrong ($e^{+iEt/\hbar}$ instead of $e^{-iEt/\hbar}$), which reverses the sloshing direction of a superposition — the sign is fixed by the TDSE.

**Signs a student needs to return to the chapter:**
- They claim $|\Psi|^2$ oscillates for a *single* eigenstate (it does not — the global phase cancels; only a superposition of *different* energies produces oscillation).
- They report zero energy variance for a two-state superposition (the variance is $\tfrac{1}{4}(E_2-E_1)^2$ for the equal mix — nonzero).

**Scaffolding adjustments:** *If a student struggles with Part A,* have them verify $|e^{-iEt/\hbar}|^2 = 1$ explicitly (writing the phase as $\cos(Et/\hbar) - i\sin(Et/\hbar)$ and squaring the modulus) before claiming $|\Psi_1|^2$ is frozen, so the cancellation is concrete rather than asserted. *If a student finishes Part F quickly,* have them derive the general superposition energy variance $\langle\hat H^2\rangle - \langle\hat H\rangle^2 = \sum_n|c_n|^2 E_n^2 - (\sum_n|c_n|^2 E_n)^2$ and show it is zero if and only if a single $|c_n| = 1$.

**Domain adaptation note:** For any stationary-state problem, the first decision is whether the state is a single eigenstate (definite energy, frozen $|\Psi|^2$, zero variance) or a superposition (no definite energy, oscillating $|\Psi|^2$ at beat frequencies, constant but probabilistic $\langle\hat H\rangle$) — that distinction governs every prediction you make.
