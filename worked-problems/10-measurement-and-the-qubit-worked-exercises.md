# Worked Exercises: Measurement, Superposition, and the Qubit

*Chapter 10 of Quantum Mechanics — Volume 1*

> These exercises follow a research-backed sequence: full worked example → matched practice → completion problem → error-recognition → transfer → interleaved review. Each section builds on the previous. Do not skip ahead.

## Prerequisites

- You can state the Born rule $P(a_n) = |\langle a_n|\psi\rangle|^2$ — the **squared modulus** of the amplitude, projected onto the eigenstate of the measured observable, not $|\psi|^2$ in the computational basis.
- You know the Pauli matrices $\sigma_x = \begin{psmallmatrix}0&1\\1&0\end{psmallmatrix}$, $\sigma_y = \begin{psmallmatrix}0&-i\\i&0\end{psmallmatrix}$ (upper-right $-i$), $\sigma_z = \begin{psmallmatrix}1&0\\0&-1\end{psmallmatrix}$, their eigenvalues $\pm1$, and that $\sigma_i^2 = I$.
- You can write a normalized qubit state as $|\psi\rangle = \cos(\theta/2)|0\rangle + e^{i\phi}\sin(\theta/2)|1\rangle$ (the half-angle $\theta/2$ is mandatory) with Bloch vector $\vec r = (\sin\theta\cos\phi, \sin\theta\sin\phi, \cos\theta)$.

## Part A — Full Worked Example

**What this demonstrates:** How to extract complete measurement statistics — outcome probabilities, expectation values, and post-measurement collapse — for all three Pauli observables on a single qubit state, using the Born rule as a projection onto each observable's eigenbasis.

**The problem:** A qubit is in the state

$$|\psi\rangle = \frac{1}{\sqrt 2}|0\rangle + \frac{1}{\sqrt 2}\,e^{i\pi/2}|1\rangle = \frac{1}{\sqrt 2}|0\rangle + \frac{i}{\sqrt 2}|1\rangle.$$

Find (a) the Bloch angles $(\theta,\phi)$, (b) $P(\sigma_z = \pm1)$ and $\langle\sigma_z\rangle$, (c) $P(\sigma_x = \pm1)$ and $\langle\sigma_x\rangle$, (d) $P(\sigma_y = \pm1)$ and $\langle\sigma_y\rangle$, and (e) the post-measurement state after each possible $\sigma_y$ outcome.

**The solution:**

**Step 1 — Read off the Bloch angles.** Match $|\psi\rangle$ to $\cos(\theta/2)|0\rangle + e^{i\phi}\sin(\theta/2)|1\rangle$: $\cos(\theta/2) = 1/\sqrt2$ gives $\theta/2 = \pi/4$, so $\theta = \pi/2$; the $|1\rangle$ coefficient is $e^{i\pi/2}/\sqrt2$, so $\phi = \pi/2$.

*Why:* Identifying $(\theta,\phi)$ locates the state on the Bloch sphere and lets us cross-check every expectation value against $\vec r = (\sin\theta\cos\phi, \sin\theta\sin\phi, \cos\theta)$.
*Check:* $\theta = \pi/2$ puts the state on the equator (equal superposition); $\phi = \pi/2$ aligns it with the $+y$ axis. So this should be the $|+y\rangle$ state — we will confirm.

**Step 2 — Measure $\sigma_z$ via projection onto $\{|0\rangle,|1\rangle\}$.**

$$P(\sigma_z = +1) = |\langle 0|\psi\rangle|^2 = \left|\frac{1}{\sqrt2}\right|^2 = \frac12, \qquad P(\sigma_z = -1) = |\langle 1|\psi\rangle|^2 = \left|\frac{i}{\sqrt2}\right|^2 = \frac12.$$

So $\langle\sigma_z\rangle = (+1)\tfrac12 + (-1)\tfrac12 = 0$.

*Why:* The Born rule takes the squared modulus of the amplitude; the phase $e^{i\pi/2}=i$ has modulus 1, so it contributes nothing to a $\sigma_z$ probability — the relative phase is invisible to $\sigma_z$.
*Check:* Bloch: $\langle\sigma_z\rangle = \cos\theta = \cos(\pi/2) = 0$. Consistent. And $P(+1)+P(-1)=1$.

**Step 3 — Measure $\sigma_x$ via projection onto $|\pm x\rangle = (|0\rangle \pm |1\rangle)/\sqrt2$.**

$$P(\sigma_x = +1) = |\langle +x|\psi\rangle|^2 = \left|\frac{1}{\sqrt2}\cdot\frac{1}{\sqrt2} + \frac{1}{\sqrt2}\cdot\frac{i}{\sqrt2}\right|^2 = \left|\frac{1+i}{2}\right|^2 = \frac{1+1}{4} = \frac12.$$

Likewise $P(\sigma_x = -1) = \tfrac12$, so $\langle\sigma_x\rangle = 0$.

*Why:* $\langle +x|\psi\rangle = \tfrac{1}{\sqrt2}(\langle 0| + \langle 1|)|\psi\rangle$; we project onto the $\sigma_x$ eigenstate, **not** the computational basis. The modulus squared of $(1+i)/2$ is $|1+i|^2/4 = 2/4$.
*Check:* Bloch: $\langle\sigma_x\rangle = \sin\theta\cos\phi = \sin(\pi/2)\cos(\pi/2) = 0$. Consistent.

**Step 4 — Measure $\sigma_y$ via projection onto $|\pm y\rangle = (|0\rangle \pm i|1\rangle)/\sqrt2$.**

$$P(\sigma_y = +1) = |\langle +y|\psi\rangle|^2 = \left|\frac{1}{\sqrt2}\cdot\frac{1}{\sqrt2} + \frac{-i}{\sqrt2}\cdot\frac{i}{\sqrt2}\right|^2 = \left|\frac{1 + 1}{2}\right|^2 = 1.$$

So $P(\sigma_y = -1) = 0$ and $\langle\sigma_y\rangle = +1$.

*Why:* $\langle +y| = \tfrac{1}{\sqrt2}(\langle 0| - i\langle 1|)$ — note the **conjugate** $-i$ in the bra. Then $(-i)(i) = +1$, so the two terms add constructively to give probability 1. This state is exactly $|+y\rangle$.
*Check:* Bloch: $\langle\sigma_y\rangle = \sin\theta\sin\phi = \sin(\pi/2)\sin(\pi/2) = 1$. Consistent, and confirms Step 1's prediction. Also $|\vec r|^2 = 0^2 + 1^2 + 0^2 = 1$ — a valid pure state.

**Step 5 — Apply the collapse rule for $\sigma_y$.** A $\sigma_y$ measurement returns $+1$ with probability 1 and collapses the state to $|+y\rangle$ — which is where it already was. The outcome $-1$ never occurs ($P=0$), so there is no $|-y\rangle$ post-measurement branch.

*Why:* The third measurement postulate says the post-measurement state is the eigenstate $|a_n\rangle$ of the obtained outcome. A $\sigma_y$ eigenstate is stable under $\sigma_y$ measurement — repeated $\sigma_y$ gives $+1$ every time.
*Check:* If we instead measured $\sigma_z$ on $|+y\rangle$, we would get $\pm1$ at 50/50 and collapse to $|0\rangle$ or $|1\rangle$, destroying the definite $\sigma_y$ value — exactly the Stern–Gerlach memory-loss behavior.

**Final answer:** $(\theta,\phi) = (\pi/2,\pi/2)$; $\langle\sigma_z\rangle = \langle\sigma_x\rangle = 0$ (both 50/50); $\langle\sigma_y\rangle = +1$ (definite). The state is $|+y\rangle$, the north pole of the $y$-axis, and a $\sigma_y$ measurement leaves it unchanged.

**What made this work:** The central concept is the **Born rule as projection onto the measured observable's eigenbasis** — $P(a_n) = |\langle a_n|\psi\rangle|^2$. The naive failure is to compute $|\psi|^2$ in the computational basis ($\tfrac12$ for both $|0\rangle$ and $|1\rangle$) and report that for every observable, which gives the right answer for $\sigma_z$ by luck but the wrong answer for $\sigma_y$ (where the truth is a definite $+1$, not 50/50). The phase $e^{i\pi/2}$ is invisible to $\sigma_z$ but completely determines $\sigma_y$ — that is the operational meaning of "the relative phase is real."

**Self-explanation prompt:** Explain why the same state gives a coin-flip on $\sigma_z$ and $\sigma_x$ but a certain outcome on $\sigma_y$ — and what that says about which "direction" of measurement this state is aligned with.

## Part B — Matched Practice Problem

**What this demonstrates:** The same measurement-statistics machinery — Bloch angles, Born-rule projection onto each Pauli eigenbasis, expectation values, collapse — applied to a state that is **not** a Pauli eigenstate (different surface).

**The problem:** A qubit is in

$$|\psi\rangle = \frac{\sqrt3}{2}|0\rangle - \frac12|1\rangle.$$

(a) Verify normalization and find $(\theta,\phi)$ (watch the sign of the $|1\rangle$ coefficient: $-\tfrac12 = e^{i\pi}\cdot\tfrac12$). (b) Compute $P(\sigma_z=\pm1)$ and $\langle\sigma_z\rangle$. (c) Compute $P(\sigma_x=\pm1)$ and $\langle\sigma_x\rangle$ by projecting onto $|\pm x\rangle$. (d) Compute $\langle\sigma_y\rangle$ and confirm it against the Bloch formula. (e) State the post-measurement state for each $\sigma_x$ outcome.

**Stuck?** For (a), $\cos(\theta/2) = \sqrt3/2$ gives $\theta = \pi/3$, and the real negative coefficient means $\phi = \pi$, not $\phi = 0$ — the minus sign is a relative phase of $\pi$, which will show up in $\langle\sigma_x\rangle$.

*Instructor note: No solution is provided for Part B. Work all five parts and cross-check every expectation value against $\vec r = (\sin\theta\cos\phi, \sin\theta\sin\phi, \cos\theta)$ yourself.*

## Part C — Completion Problem

**What this demonstrates:** Computing $\sigma_x$ measurement statistics for a generic real-coefficient state, with two middle steps left blank.

**The problem:** For $|\psi\rangle = \cos(\theta/2)|0\rangle + \sin(\theta/2)|1\rangle$ with $\theta = 2\pi/3$ (so $\phi = 0$), find $P(\sigma_x=\pm1)$, $\langle\sigma_x\rangle$, and confirm against the Bloch vector.

**Step 1 — Evaluate the amplitudes (complete).** $\theta/2 = \pi/3$, so $\cos(\theta/2) = 1/2$ and $\sin(\theta/2) = \sqrt3/2$. Thus $|\psi\rangle = \tfrac12|0\rangle + \tfrac{\sqrt3}{2}|1\rangle$.
*Why:* The half-angle $\theta/2$ is what enters the state; $\theta = 2\pi/3$ gives $\theta/2 = \pi/3$, a standard-angle pair $(1/2, \sqrt3/2)$.

**Step 2 — Write the $\sigma_x$ eigenstates (complete).** $|\pm x\rangle = (|0\rangle \pm |1\rangle)/\sqrt2$, with eigenvalues $\pm1$.
*Why:* $\sigma_x$ measurement projects onto its own eigenbasis $\{|+x\rangle,|-x\rangle\}$, not the computational basis — this is the Born-rule projection rule.

**Step 3 — [BLANK] Compute $P(\sigma_x = +1)$ via $|\langle +x|\psi\rangle|^2$.**
*Your work here:*

_______________________________________________

*Why (your explanation):*

_______________________________________________

**Step 4 — [BLANK] Compute $P(\sigma_x = -1)$ and form $\langle\sigma_x\rangle$.**
*Your work here:*

_______________________________________________

*Why (your explanation):*

_______________________________________________

**Step 5 — Cross-check with the Bloch vector (complete).** $\langle\sigma_x\rangle = \sin\theta\cos\phi = \sin(2\pi/3)\cos 0 = \tfrac{\sqrt3}{2}\approx 0.866$.

**Final answer:** $P(\sigma_x=+1) = \tfrac{1}{2}(1 + \tfrac{\sqrt3}{2}) \approx 0.933$, $P(\sigma_x=-1) \approx 0.067$, $\langle\sigma_x\rangle = \sqrt3/2 \approx 0.866$, matching the Bloch formula.

**Self-explanation prompt:** This state is mostly $|1\rangle$ in the $\sigma_z$ basis but strongly $+1$ in $\sigma_x$. Explain geometrically (using $\theta = 2\pi/3$ on the Bloch sphere) why a state in the southern hemisphere can still favor $\sigma_x = +1$.

## Part D — Error-Recognition Problem

> **Use this section only after completing Parts A–C.**

**The problem:** A student computes the probability of measuring $\sigma_x = +1$ on the state $|\psi\rangle = \tfrac{\sqrt3}{2}|0\rangle + \tfrac{i}{2}|1\rangle$ (the chapter's worked-example state).

**Step 1 (correct).** Normalization: $|\sqrt3/2|^2 + |i/2|^2 = 3/4 + 1/4 = 1$. Good. The $\sigma_x$ eigenstates are $|\pm x\rangle = (|0\rangle \pm |1\rangle)/\sqrt2$.

**Step 2 (correct).** The amplitude for $+x$ is $\langle +x|\psi\rangle = \tfrac{1}{\sqrt2}(\langle 0| + \langle 1|)|\psi\rangle = \tfrac{1}{\sqrt2}\!\left(\tfrac{\sqrt3}{2} + \tfrac{i}{2}\right)$.

**Step 3 (⚠ contains an error).** "The probability is the amplitude itself: $P(\sigma_x = +1) = \langle +x|\psi\rangle = \tfrac{1}{\sqrt2}\!\left(\tfrac{\sqrt3}{2} + \tfrac{i}{2}\right) = \tfrac{\sqrt3 + i}{2\sqrt2}$. This is a complex number, so I take its real part as the probability: $P(\sigma_x=+1) = \sqrt3/(2\sqrt2) \approx 0.612$."

**Step 4 (correct-looking).** "Then $P(\sigma_x = -1) = 1 - 0.612 = 0.388$, and $\langle\sigma_x\rangle = (+1)(0.612) + (-1)(0.388) = 0.224$, a plausible value between $-1$ and $+1$."

**Your tasks:**
1. Identify the exact misconception in Step 3 (what does the Born rule actually do to the amplitude?).
2. Compute $P(\sigma_x = +1)$ correctly as $|\langle +x|\psi\rangle|^2$, showing the modulus-squared explicitly.
3. Recompute $P(\sigma_x=-1)$ and $\langle\sigma_x\rangle$, and compare to the chapter's result $\langle\sigma_x\rangle = 0$.
4. Explain why Step 4's $\langle\sigma_x\rangle = 0.224$ "looks reasonable" yet is wrong, and what check (Bloch vector) would have caught it immediately.

**Why this error is common:** Students use the amplitude $c = \langle a_n|\psi\rangle$ directly (or its real part) as the probability instead of $|c|^2$, forgetting that the Born rule takes the **squared modulus** — and because the bogus result still lands in $[0,1]$ and sums to 1, it passes a casual sanity check while violating the Bloch-vector cross-check.

## Part E — Transfer Problem

**What this demonstrates:** The measurement postulate — eigenvalue outcomes, Born-rule probabilities, collapse — applies to **any** two-level system, including photon polarization, which the chapter mentions only in passing.

**The problem (context not developed in the chapter):** A single photon is in the polarization state $|\psi\rangle = \cos(22.5°)|H\rangle + \sin(22.5°)|V\rangle$, where $|H\rangle,|V\rangle$ are horizontal/vertical polarization (the computational basis). A polarizer oriented at angle $\alpha$ measures the observable with eigenstates $|\alpha\rangle = \cos\alpha\,|H\rangle + \sin\alpha\,|V\rangle$ ("pass") and $|\alpha_\perp\rangle = -\sin\alpha\,|H\rangle + \cos\alpha\,|V\rangle$ ("block").

(a) For a polarizer at $\alpha = 45°$, compute the probability the photon passes, $P = |\langle\alpha|\psi\rangle|^2$. (b) Show this reproduces **Malus's law** $P = \cos^2(\alpha - \theta_{\text{pol}})$ where $\theta_{\text{pol}} = 22.5°$ is the photon's polarization angle. (c) If the photon passes, what is its state immediately afterward, and what does a **second** polarizer at $90°$ then transmit?

**Hint (use only if stuck after 10 minutes):** This is the qubit measurement postulate with $|0\rangle \to |H\rangle$, $|1\rangle\to|V\rangle$, and a real rotation by $\alpha$. The pass probability is $\cos^2$ of the angle between the state and the polarizer axis. After passing, collapse to $|\alpha\rangle$ — exactly the Stern–Gerlach "select the upper beam" step, but for light. The second polarizer then measures the collapsed state, just like Z-then-X.

**Reflection prompt:**
1. What is the photon-polarization analogue of the Stern–Gerlach "Z then X then Z" memory-loss sequence, and why does inserting a $45°$ polarizer between crossed polarizers let light through?
2. The Born rule here is Malus's law, a classical-optics result known since 1809. What does the quantum postulate add that the classical wave picture does not — and where does collapse enter?

## Part F — Interleaved Review

**Problem F1.** A qubit is in $|\psi\rangle = \cos(\pi/8)|0\rangle + e^{i\pi/3}\sin(\pi/8)|1\rangle$. Compute the full Bloch vector $(\langle\sigma_x\rangle, \langle\sigma_y\rangle, \langle\sigma_z\rangle)$ using $\theta = \pi/4$, $\phi = \pi/3$, and verify $|\vec r| = 1$. Then state $P(\sigma_z = -1)$.
*Chapter this draws from: Chapter 10.*

**Problem F2.** For the same state in F1, the Robertson bound for the pair $(\sigma_x,\sigma_z)$ is $\sigma_{\sigma_x}\sigma_{\sigma_z} \geq \tfrac12|\langle[\sigma_x,\sigma_z]\rangle| = |\langle\sigma_y\rangle|$ (since $[\sigma_x,\sigma_z] = -2i\sigma_y$). Using $\sigma_{\sigma_i}^2 = 1 - \langle\sigma_i\rangle^2$ (because $\sigma_i^2 = I$), compute $\sigma_{\sigma_x}$ and $\sigma_{\sigma_z}$, form their product, and confirm it meets or exceeds $|\langle\sigma_y\rangle|$.
*Chapter this draws from: the Robertson inequality and canonical commutation structure (Chapter 9, Operators and Uncertainty).*

**Problem F3.** You are told a qubit gives $\langle\sigma_z\rangle = 0$ when measured many times. Determine which state(s) this could be, and whether knowing $\langle\sigma_z\rangle = 0$ is enough to predict the outcomes of a $\sigma_x$ measurement.
*Note to instructor: this problem is intentionally ambiguous — $\langle\sigma_z\rangle = 0$ specifies only $\theta = \pi/2$ (the equator), leaving $\phi$ free, so $\sigma_x$ statistics range from definite ($\phi=0$, giving $\langle\sigma_x\rangle = +1$) to 50/50 ($\phi = \pi/2$, the $|+y\rangle$ state). The student must recognize that one expectation value does not fix the state, and that the relative phase $\phi$ — invisible to $\sigma_z$ — controls $\sigma_x$.*

**Closing reflection:** F1 used the Born rule on a qubit; F2 brought in the Robertson bound from the previous chapter; F3 forced you to confront how much (how little) one expectation value reveals. Which of these three would change if you only knew the state up to a **global** phase versus a **relative** phase?

## Instructor Notes

**Common errors:**
- Using the amplitude $c = \langle a_n|\psi\rangle$ (or its real part) instead of $|c|^2$ for a measurement probability.
- Forgetting to normalize a superposition before reading probabilities — or normalizing in the computational basis but then projecting onto the wrong (computational) basis for $\sigma_x$ and $\sigma_y$.
- Confusing the Bloch polar angle $\theta$ with the state half-angle $\theta/2$, which places the south pole at $\theta = \pi/2$ instead of $\theta = \pi$.

**Signs a student needs to return:**
- They report measurement probabilities that do not sum to 1, or that are complex/negative — a sure sign the modulus-squared step was skipped.
- They claim $\langle\sigma_y\rangle$ has the wrong sign, traceable to writing $\sigma_y$ with $+i$ in the upper-right corner instead of $-i$.

**Scaffolding adjustments:** A student stuck on Part A should first do the $|0\rangle$ and $|+x\rangle$ cases by hand (Bloch poles/equator) to see the Born projection in its simplest form before tackling the complex-phase state. A student who finishes Part F quickly should compute the full Robertson ratio for the $|+y\rangle$ state and confirm it saturates the $(\sigma_x,\sigma_z)$ bound at exactly 1, as the chapter's worked example shows.

**Domain adaptation note:** For a quantum-computing-track section, recast every example as a single-qubit gate-and-measure circuit (state preparation, basis rotation, computational-basis readout), preserving the Born-rule projection while framing it in the language students will meet in qiskit or cirq.
