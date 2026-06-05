# Worked Exercises: Operators and Uncertainty

*Chapter 9 of Quantum Mechanics — Volume 1*

> These exercises follow a research-backed sequence: full worked example → matched practice → completion problem → error-recognition → transfer → interleaved review. Each section builds on the previous. Do not skip ahead.

## Prerequisites

- You can compute an expectation value as $\langle\hat{A}\rangle = \int\psi^*(\hat{A}\psi)\,dx$ — using the operator sandwiched between $\psi^*$ and $\psi$, **not** $\int|\psi|^2\hat{A}\,dx$ (which is only correct for $\hat{A}=\hat{x}$).
- You know the momentum operator is $\hat{p} = -i\hbar\,\partial_x$, that the sign is load-bearing, and that the variance is $\sigma_A^2 = \langle\hat{A}^2\rangle - \langle\hat{A}\rangle^2$ (both terms required).
- You can state the canonical commutation relation $[\hat{x},\hat{p}] = i\hbar$ and the Robertson inequality $\sigma_A\sigma_B \geq \tfrac{1}{2}|\langle[\hat{A},\hat{B}]\rangle|$.

## Part A — Full Worked Example

**What this demonstrates:** That the uncertainty product $\sigma_x\sigma_p$ for a definite state can be computed directly from the canonical commutation relation and the operator-algebra shortcut $\hat{p}^2\psi = 2m\hat{H}\psi$, and that the result exceeds — but does not saturate — the Kennard bound $\hbar/2$ for a non-Gaussian state.

**The problem:** A particle is in the **second** excited state of an infinite square well on $[0,L]$, namely the $n=3$ eigenstate $\psi_3(x) = \sqrt{2/L}\,\sin(3\pi x/L)$. Compute $\sigma_x$, $\sigma_p$, their product, and the ratio $\sigma_x\sigma_p/(\hbar/2)$. Confirm the Robertson bound is satisfied and decide whether it is saturated.

**The solution:**

**Step 1 — Fix the position mean by symmetry.** The density $|\psi_3|^2 = (2/L)\sin^2(3\pi x/L)$ is symmetric about $x=L/2$, so

$$\langle x\rangle = \frac{L}{2}.$$

*Why:* The expectation value $\langle x\rangle = \int_0^L x\,|\psi_3|^2\,dx$ is the centroid of a density that is mirror-symmetric about the midpoint; the centroid of a symmetric density sits at the symmetry point.
*Check:* $\langle x\rangle = L/2$ lies inside $[0,L]$, as any position mean must. Units: length. Good.

**Step 2 — Compute the position variance using the general $n$ result.** From the chapter's higher-mode formula,

$$\sigma_x^2 = L^2\!\left(\frac{1}{12} - \frac{1}{2n^2\pi^2}\right).$$

At $n=3$: $\dfrac{1}{2\cdot 9\cdot\pi^2} = \dfrac{1}{18\pi^2} \approx 0.005629$, so

$$\sigma_x^2 = L^2(0.083333 - 0.005629) = 0.077704\,L^2, \qquad \sigma_x \approx 0.2788\,L.$$

*Why:* The well's eigenstates have $\langle x^2\rangle = L^2\!\left(\tfrac{1}{3} - \tfrac{1}{2n^2\pi^2}\right)$, and subtracting $\langle x\rangle^2 = L^2/4$ gives the displayed variance — the $\sigma_A^2 = \langle\hat A^2\rangle - \langle\hat A\rangle^2$ rule applied to $\hat x$.
*Check:* As $n\to\infty$, $\sigma_x^2 \to L^2/12$, the variance of a uniform distribution on $[0,L]$ — exactly what a highly oscillatory $\sin^2$ approaches. The $n=3$ value $0.0777\,L^2$ is below $1/12 \approx 0.0833\,L^2$, as it must be.

**Step 3 — Get the momentum mean and variance from the TISE shortcut.** The state is a standing wave (equal left/right superposition), so $\langle p\rangle = 0$. For $\langle p^2\rangle$, use $\hat H = \hat p^2/2m$ inside the well and $\hat H\psi_3 = E_3\psi_3$ with $E_3 = 9\pi^2\hbar^2/(2mL^2)$:

$$\hat p^2\psi_3 = 2m\hat H\psi_3 = 2mE_3\,\psi_3 = \left(\frac{3\hbar\pi}{L}\right)^2\psi_3 \;\Rightarrow\; \langle p^2\rangle = \left(\frac{3\hbar\pi}{L}\right)^2,\quad \sigma_p = \frac{3\hbar\pi}{L}.$$

*Why:* Acting with $\hat p^2$ on an energy eigenstate is the same as multiplying by $2mE_n$ — an operator-algebra shortcut that beats integrating $\psi_3^*(-\hbar^2\partial_x^2\psi_3)$ by hand. Since $\langle p\rangle = 0$, $\sigma_p^2 = \langle p^2\rangle$.
*Check:* Units of $\hbar\pi/L$ are (J·s)/m = kg·m/s = momentum. Good. $\sigma_p$ scales as $n$, so the $n=3$ momentum spread is three times the ground-state value $\hbar\pi/L$ — the more nodes, the sharper the curvature, the larger $\langle p^2\rangle$.

**Step 4 — Form the product and the ratio.**

$$\sigma_x\sigma_p \approx 0.2788\,L \cdot \frac{3\hbar\pi}{L} = 0.2788\cdot 3\pi\,\hbar \approx 2.628\,\hbar, \qquad \frac{\sigma_x\sigma_p}{\hbar/2} = \frac{2.628}{0.5} \approx 5.44.$$

*Why:* The $L$ cancels — the ratio is dimensionless and depends only on $n$. This is the Robertson/Kennard ratio that the chapter tracks.
*Check:* The chapter states the ratio grows as $(\pi/\sqrt{3})\,n \approx 1.814\,n$. At $n=3$ that predicts $\approx 5.44$. Match.

**Final answer:** $\sigma_x \approx 0.279\,L$, $\sigma_p = 3\hbar\pi/L$, $\sigma_x\sigma_p \approx 2.63\,\hbar$, ratio $\approx 5.44$. The Robertson bound $\sigma_x\sigma_p \geq \hbar/2$ is satisfied with enormous room to spare and is **not** saturated.

**What made this work:** The central concept is the **canonical commutation relation** $[\hat x,\hat p] = i\hbar$ feeding the **Robertson inequality** — but the computational engine is the operator-algebra shortcut $\hat p^2\psi_n = 2mE_n\psi_n$. A naive approach would try to integrate $\langle p^2\rangle = \int\psi_3^*(-\hbar^2\partial_x^2\psi_3)\,dx$ directly, which is more error-prone and obscures why $\sigma_p = n\hbar\pi/L$ scales linearly in $n$. Recognizing the eigenstate lets you read $\langle p^2\rangle$ off the energy. The non-saturation is not an accident: only the Gaussian saturates Kennard, and the hard walls forbid a Gaussian.

**Self-explanation prompt:** In your own words, why does $\sigma_p$ grow with $n$ while $\sigma_x$ approaches a finite ceiling — and why does that combination force the ratio to grow without bound?

## Part B — Matched Practice Problem

**What this demonstrates:** The same machinery — symmetry for $\langle x\rangle$, the variance formula, the TISE shortcut for $\langle p^2\rangle$, the Robertson ratio — applied to a **different surface**: an equal superposition rather than a pure eigenstate.

**The problem:** A particle in the infinite square well on $[0,L]$ is in the normalized superposition

$$\psi(x) = \frac{1}{\sqrt{2}}\bigl(\psi_1(x) + \psi_2(x)\bigr), \qquad \psi_n = \sqrt{2/L}\,\sin(n\pi x/L).$$

(a) Compute $\langle p^2\rangle$ using $\hat p^2\psi_n = (n\hbar\pi/L)^2\psi_n$ together with the orthonormality of $\psi_1,\psi_2$. (b) Compute $\langle p\rangle$ and explain whether symmetry still forces it to zero (careful — this state is **not** symmetric about $L/2$). (c) Form $\sigma_p$. (d) State, without finishing the position integrals, whether you expect the Robertson ratio to exceed $\hbar/2$, and why.

**Stuck?** $\langle p^2\rangle = \tfrac{1}{2}(\hbar\pi/L)^2 + \tfrac{1}{2}(2\hbar\pi/L)^2$ because the cross terms in $\langle\hat p^2\rangle$ vanish by orthogonality — but the cross terms in $\langle\hat p\rangle$ need not vanish, so check whether $\langle p\rangle = 0$ actually holds here.

*Instructor note: No solution is provided for Part B. Work it fully before consulting Part A's structure as a model.*

## Part C — Completion Problem

**What this demonstrates:** Computing the uncertainty product for the infinite-well **ground state** from scratch, with two of the middle steps left for you to complete.

**The problem:** For $\psi_1(x) = \sqrt{2/L}\,\sin(\pi x/L)$ on $[0,L]$, compute $\sigma_x$, $\sigma_p$, the product $\sigma_x\sigma_p$, and the ratio $\sigma_x\sigma_p/(\hbar/2)$.

**Step 1 — Fix the position mean (complete).** By symmetry of $\sin^2(\pi x/L)$ about $x=L/2$, $\langle x\rangle = L/2$.
*Why:* The probability density is mirror-symmetric about the midpoint, so its centroid is the midpoint.

**Step 2 — Get the momentum mean (complete).** The ground state is an equal superposition of $e^{i\pi x/L}$ and $e^{-i\pi x/L}$; the rightward and leftward contributions cancel, so $\langle p\rangle = 0$. (Direct check: the integrand $\sin(\pi x/L)\cos(\pi x/L) = \tfrac12\sin(2\pi x/L)$ integrates to zero over $[0,L]$.)
*Why:* A standing wave carries no net momentum; equal and opposite plane-wave components cancel in the mean.

**Step 3 — [BLANK] Compute the position variance.**
*Your work here:*

_______________________________________________

*Why (your explanation):*

_______________________________________________

**Step 4 — [BLANK] Compute the momentum variance via the TISE shortcut.**
*Your work here:*

_______________________________________________

*Why (your explanation):*

_______________________________________________

**Step 5 — Form the product and ratio (complete).** With $\sigma_x \approx 0.181\,L$ and $\sigma_p = \hbar\pi/L$,

$$\sigma_x\sigma_p \approx 0.181\,L\cdot\frac{\hbar\pi}{L} = 0.181\pi\,\hbar \approx 0.568\,\hbar, \qquad \frac{\sigma_x\sigma_p}{\hbar/2} \approx \frac{0.568}{0.5} \approx 1.136.$$

**Final answer:** $\sigma_x \approx 0.181\,L$, $\sigma_p = \hbar\pi/L$, $\sigma_x\sigma_p \approx 0.568\,\hbar$, ratio $\approx 1.136$. The bound is satisfied but not saturated.

**Self-explanation prompt:** The ground-state ratio is $1.136$, just above the floor of $1.000$, while the $n=3$ ratio (Part A) was $5.44$. Explain what the ground state has that higher modes lack — and why it is still not a Gaussian.

## Part D — Error-Recognition Problem

> **Use this section only after completing Parts A–C.**

**The problem:** A student computes the momentum spread for the Gaussian wave packet $\psi = Ne^{-x^2/2a^2}e^{ik_0 x}$ with $k_0 \neq 0$ and reports the uncertainty product.

**Step 1 (correct).** Position: $\langle x\rangle = 0$ by symmetry of $|\psi|^2$, and $\langle x^2\rangle = a^2/2$, so $\sigma_x^2 = a^2/2$, $\sigma_x = a/\sqrt{2}$.

**Step 2 (correct).** Momentum mean: $-i\hbar\partial_x\psi = \psi(i\hbar x/a^2 + \hbar k_0)$; integrating against $\psi^*$, the odd term vanishes and $\langle p\rangle = \hbar k_0$.

**Step 3 (⚠ contains an error).** "The momentum variance is the expectation of $\hat p^2$, which equals the square of the mean: $\sigma_p^2 = \langle p\rangle^2 = (\hbar k_0)^2$. So $\sigma_p = \hbar k_0$, and the product is $\sigma_x\sigma_p = (a/\sqrt 2)(\hbar k_0)$."

**Step 4 (correct-looking).** "Therefore the Robertson bound requires $(a/\sqrt 2)(\hbar k_0) \geq \hbar/2$, i.e. $a k_0 \geq 1/\sqrt 2$, which holds for the given parameters, so the packet respects the uncertainty principle."

**Your tasks:**
1. Identify the exact physics misconception in Step 3.
2. Compute $\langle p^2\rangle$ and $\sigma_p^2$ correctly (use $\hat p^2\psi = -\hbar^2\partial_x^2\psi$, or recall the Gaussian result), and state the correct $\sigma_p$.
3. Recompute $\sigma_x\sigma_p$ for the Gaussian and show it equals $\hbar/2$ exactly — independent of $k_0$.
4. Explain why Step 4's conclusion ("respects the uncertainty principle") happens to be true even though Step 3 is wrong, and why that coincidence is dangerous.

**Why this error is common:** Students conflate the variance $\sigma_p^2 = \langle p^2\rangle - \langle p\rangle^2$ with $\langle p\rangle^2$, dropping the $\langle p^2\rangle$ term entirely — and because the mistake leaves $\sigma_p$ a plausible positive number, it survives any check that does not test against the exact Gaussian saturation $\sigma_x\sigma_p = \hbar/2$.

## Part E — Transfer Problem

**What this demonstrates:** The Robertson inequality and the canonical commutation relation apply to **any** pair of conjugate observables — including ones not discussed in this chapter.

**The problem (context not in the chapter):** Consider the angular position $\hat\varphi$ and angular momentum $\hat L_z = -i\hbar\,\partial_\varphi$ of a particle confined to a ring, $\varphi \in [0, 2\pi)$. These satisfy $[\hat\varphi, \hat L_z] = i\hbar$ (formally, away from the $2\pi$ wraparound).

(a) Write the Robertson bound for $\sigma_\varphi\,\sigma_{L_z}$.
(b) For the $L_z$ eigenstate $\psi_m(\varphi) = e^{im\varphi}/\sqrt{2\pi}$ (definite angular momentum $\hbar m$), compute $\sigma_{L_z}$ and explain what the bound then says about $\sigma_\varphi$.
(c) The angular position $\varphi$ is bounded to $[0,2\pi)$, so $\sigma_\varphi$ cannot exceed roughly $\pi/\sqrt{3}$. Explain why this does **not** violate the bound you wrote in (a), drawing on how the chapter resolved the analogous plane-wave / Robertson tension for $\hat x,\hat p$.

**Hint (use only if stuck after 10 minutes):** Look at how the chapter handled the plane wave $e^{ik_0 x}$ as a $\hat p$ eigenstate: $\sigma_p = 0$ makes the right-hand side of Robertson zero, so any finite $\sigma_x$ satisfies it. The subtlety is that $e^{ik_0x}$ is not normalizable. For the ring, the wraparound at $2\pi$ means $[\hat\varphi,\hat L_z]$ is not exactly $i\hbar$ at the boundary — the bound's right-hand side picks up a correction.

**Reflection prompt:**
1. What feature do $\hat x,\hat p$ and $\hat\varphi,\hat L_z$ share that makes both governed by the same Robertson structure?
2. Why does confinement (the ring's finite circumference) make this case subtler than the line — and what does that tell you about treating $\sigma_x\sigma_p \geq \hbar/2$ as a rigid law versus a state-dependent bound?

## Part F — Interleaved Review

**Problem F1.** For the infinite-well superposition $\psi = \tfrac{1}{\sqrt 5}(\psi_1 + 2\psi_3)$ (note the coefficients $1/\sqrt5$ and $2/\sqrt5$, with $|1/\sqrt5|^2 + |2/\sqrt5|^2 = 1$): use $\hat p^2\psi_n = (n\hbar\pi/L)^2\psi_n$ and orthonormality to compute $\langle p^2\rangle$, then $\sigma_p$ (given $\langle p\rangle = 0$ for this real standing-wave combination). Confirm $\sigma_p$ lies between the $n=1$ and $n=3$ single-state values.
*Chapter this draws from: Chapter 9.*

**Problem F2.** The chapter's Robertson proof used Cauchy–Schwarz on $\|\hat A'|\psi\rangle\|\,\|\hat B'|\psi\rangle\|$. Before that step is even available, you need the **Born rule and the expansion of a state in an eigenbasis** introduced earlier: for a Hermitian $\hat A$ with eigenstates $|a_n\rangle$, write $|\psi\rangle = \sum_n c_n|a_n\rangle$ and show $\langle\hat A\rangle = \sum_n a_n|c_n|^2$ and $\langle\hat A^2\rangle = \sum_n a_n^2|c_n|^2$. Then express $\sigma_A^2$ as a weighted variance of the eigenvalues.
*Chapter this draws from: the probability/Born-rule and eigenstate-expansion material (Chapter 3, expectation values).*

**Problem F3.** A particle is in a state with $\langle x\rangle = 0$, $\langle p\rangle = 0$, $\sigma_x = a/\sqrt 2$, and $\sigma_p = \hbar/(a\sqrt 2)$. Determine whether the state must be the Gaussian minimum-uncertainty packet, or whether some other (non-Gaussian) state could produce these same four numbers.
*Note to instructor: this problem is intentionally ambiguous — saturating $\sigma_x\sigma_p = \hbar/2$ does force the Gaussian (the saturation condition $\hat A'|\psi\rangle = i\lambda\hat B'|\psi\rangle$ has only the Gaussian as a normalizable solution), but a student must recognize that the four moments alone do not pin down a unique state unless saturation is invoked. The discrimination is between "matches the first two moments" and "saturates the bound."*

**Closing reflection:** Across F1–F3 you used the TISE shortcut, the eigenbasis expansion of variance, and the saturation condition. Which of these is purely algebraic (true of any Hermitian operator pair) and which depends on the specific operators $\hat x,\hat p$?

## Instructor Notes

**Common errors:**
- Using the bound $\sigma_x\sigma_p \geq \hbar$ (off by a factor of 2) instead of $\hbar/2$ — usually from misremembering $\tfrac12|\langle[\hat x,\hat p]\rangle| = \tfrac12\hbar$, not $\hbar$.
- Computing the variance as $\langle\hat A\rangle^2$ rather than $\langle\hat A^2\rangle - \langle\hat A\rangle^2$ (dropping the $\langle\hat A^2\rangle$ term), which is invisible for $\langle p\rangle = 0$ states but corrupts any moving packet.
- A sign or factor error in $[\hat x,\hat p] = i\hbar$ — frequently from forgetting the product-rule term $-i\hbar\psi$ in $\hat p(\hat x\psi)$.

**Signs a student needs to return:**
- They report a ratio $\sigma_x\sigma_p/(\hbar/2)$ below 1 — a guaranteed sign of a missing term or a factor-of-2 slip, since the bound forbids it.
- They treat $\hat p = +i\hbar\partial_x$ and $\hat p = -i\hbar\partial_x$ as interchangeable, getting $\langle p\rangle < 0$ for a right-moving packet without noticing.

**Scaffolding adjustments:** A student stuck on Part A should first redo the $n=1$ ground-state case (Part C, with two steps already filled) before attempting $n=3$ — the TISE shortcut is identical and the arithmetic is lighter. A student who finishes Part F quickly should derive the large-$n$ asymptotic ratio $(\pi/\sqrt3)\,n$ from the general formulas for $\sigma_x$ and $\sigma_p$, and confirm $n=10$ gives $\approx 18.08$.

**Domain adaptation note:** For a chemistry-track section, replace the infinite-well examples with the vibrational levels of a diatomic molecule modeled as a harmonic oscillator, where the ground state saturates the Kennard bound exactly — preserving the operator algebra while grounding it in spectroscopy.
