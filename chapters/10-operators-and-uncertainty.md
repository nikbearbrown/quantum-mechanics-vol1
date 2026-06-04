# Chapter 9 — Operators and Uncertainty

## TL;DR

- Every measurable physical quantity corresponds to a **Hermitian operator**; Hermiticity is what forces measurement outcomes to be real numbers.
- The momentum operator in position space is $\hat{p} = -i\hbar\,\partial_x$; the minus sign and the $i$ are not conventions but requirements for Hermiticity.
- Expectation values are $\langle\hat{A}\rangle = \int\psi^*\hat{A}\psi\,dx$; standard deviations $\sigma_A = \sqrt{\langle\hat{A}^2\rangle - \langle\hat{A}\rangle^2}$ quantify spread.
- The commutator $[\hat{x}, \hat{p}] = i\hbar$ is the algebraic statement distinguishing quantum mechanics from classical mechanics; it implies $\sigma_x\sigma_p \geq \hbar/2$.
- The Gaussian ground state saturates the bound: $\sigma_x\sigma_p = \hbar/2$ exactly; every other normalizable state does strictly worse. The +1 simulation re-opens the Chapter 1 probability explorer and verifies the bound for both the Gaussian and the infinite-square-well ground state.

---

## Learning Objectives

By the end of this chapter you can:

1. **Explain** (Understand) why observables must correspond to Hermitian operators, and prove that $\hat{p} = -i\hbar\partial_x$ is Hermitian using integration by parts. [Bloom: Understand]
2. **Compute** (Apply) the expectation value $\langle\hat{A}\rangle$ and variance $\sigma_A^2$ for a given state and operator, both by direct integral and by operator algebra. [Bloom: Apply]
3. **Derive** (Analyze) $[\hat{x}, \hat{p}] = i\hbar$ by acting on a test function with both orderings, tracking every product-rule term. [Bloom: Analyze]
4. **Prove** (Analyze) the position–momentum uncertainty relation $\sigma_x\sigma_p \geq \hbar/2$ from the canonical commutation relation via the Robertson inequality. [Bloom: Analyze]
5. **Verify** (Evaluate) that the infinite-square-well ground state satisfies but does not saturate the bound, and explain why only the Gaussian does. [Bloom: Evaluate]

---

## Opening: The Machine That Spits Out Numbers

A student runs an experiment in 1926. She has an electron. She prepares it in exactly the same state — same apparatus, same procedure — a thousand times. Each time she measures its position. She gets a thousand different numbers. She makes a histogram.

That histogram has a shape — a mean, a spread. The mean $\langle x\rangle$ is the average position across those thousand measurements. The spread $\sigma_x$ is the standard deviation. These are properties not of any single measurement but of the state the electron was prepared in.

Now she does the experiment again, another thousand copies of the same state, and measures momentum instead of position. Another histogram, another mean $\langle p\rangle$, another spread $\sigma_p$.

Here is what she discovers: $\sigma_x$ and $\sigma_p$ are not independent. No matter how she prepares the state, the product $\sigma_x\sigma_p$ is always at least $\hbar/2$. She cannot make both arbitrarily small at once. This is not about her measurement apparatus. It is not about the photon used to locate the electron kicking it. She measures position on half the copies and momentum on the other half — no copy is measured twice. The limitation is in the state itself, before any measurement begins.

The question is: why? What mathematical structure in the theory produces this bound? The answer is operators.

---

## Core Development

### Operators as Observables

In quantum mechanics, every physical observable is represented by a linear operator on the Hilbert space of wave functions. A **linear operator** $\hat{A}$ maps wave functions to wave functions:

$$\hat{A}:\psi(x) \mapsto (\hat{A}\psi)(x),$$

with the linearity requirement $\hat{A}(\alpha\psi + \beta\phi) = \alpha\hat{A}\psi + \beta\hat{A}\phi$ for any complex $\alpha, \beta$.

Why operators? Because the Born rule says measurement outcomes are numbers, but quantum states encode continuous distributions, and extracting a number from a distribution requires a rule. The expectation value $\langle\hat{A}\rangle$ is that rule: it gives the average of many identical measurements on identically prepared states.

The specific requirement is **Hermiticity**. An operator $\hat{A}$ is Hermitian (self-adjoint) if, for any two normalizable wave functions $\psi$ and $\phi$,

$$\langle\phi|\hat{A}\psi\rangle \equiv \int_{-\infty}^{\infty}\phi^*(x)\,(\hat{A}\psi)(x)\,dx = \int_{-\infty}^{\infty}(\hat{A}\phi)^*(x)\,\psi(x)\,dx \equiv \langle\hat{A}\phi|\psi\rangle.$$

Three consequences:

**Real eigenvalues.** If $\hat{A}|a\rangle = a|a\rangle$, then $\langle a|\hat{A}|a\rangle = a$. The Hermitian property forces $a = a^*$, so $a$ is real. Measurement outcomes must be real numbers; this is why observables are Hermitian operators.

**Orthogonal eigenstates.** Eigenstates with distinct eigenvalues are orthogonal: $\langle a|a'\rangle = 0$ for $a \neq a'$. (Proof: compute $\langle a'|\hat{A}|a\rangle = a\langle a'|a\rangle$ two ways — using Hermiticity and the eigenvalue equation — then subtract.)

**Complete eigenbasis (spectral theorem).** The eigenstates form a complete orthonormal set, so any state can be expanded as $|\psi\rangle = \sum_n c_n|a_n\rangle$ with $c_n = \langle a_n|\psi\rangle$. The probability of getting outcome $a_n$ is $|c_n|^2$. This is the Born rule, rewritten in operator language.

### The Momentum Operator Is Hermitian

The position operator is simple: $(\hat{x}\psi)(x) = x\psi(x)$. Multiplication by $x$. Hermitian by inspection, since $x$ is real.

The momentum operator is less obvious:

$$\hat{p} = -i\hbar\frac{\partial}{\partial x}.$$

The factors $-i$ and $\hbar$ are not decorative. Let us check Hermiticity. Compute $\langle\phi|\hat{p}\psi\rangle$:

$$\langle\phi|\hat{p}\psi\rangle = \int_{-\infty}^{\infty}\phi^*(x)\left(-i\hbar\frac{\partial\psi}{\partial x}\right)dx.$$

Integrate by parts. The boundary term $\phi^*\psi\,\big|_{-\infty}^{\infty}$ vanishes because any normalizable $\psi$ and $\phi$ go to zero at $\pm\infty$:

$$= \int_{-\infty}^{\infty}\left(i\hbar\frac{\partial\phi^*}{\partial x}\right)\psi\,dx = \int_{-\infty}^{\infty}\left(-i\hbar\frac{\partial\phi}{\partial x}\right)^*\psi\,dx = \langle\hat{p}\phi|\psi\rangle.$$

Hermitian. The factor of $-i$ is what makes it work. Without the $-i$, the derivative $\partial_x$ would be anti-Hermitian (it would pick up a minus sign from integration by parts), and its eigenvalues would be imaginary — not measurable.

Why is this the momentum operator? The cleanest answer is Fourier analysis. The Fourier transform relates the position-space wave function $\psi(x)$ to the momentum-space wave function $\phi(p)$ by $\psi(x) = (1/\sqrt{2\pi\hbar})\int\phi(p)e^{ipx/\hbar}\,dp$. Differentiate both sides with respect to $x$:

$$\frac{\partial\psi}{\partial x} = \frac{1}{\sqrt{2\pi\hbar}}\int\phi(p)\cdot\frac{ip}{\hbar}\,e^{ipx/\hbar}\,dp.$$

So $-i\hbar\,\partial_x\psi = (1/\sqrt{2\pi\hbar})\int p\,\phi(p)\,e^{ipx/\hbar}\,dp$. The operator $-i\hbar\partial_x$ acting in position space produces the same thing as multiplication by $p$ acting in momentum space. Differentiation is the position-space representation of the momentum observable.

### Expectation Values and Standard Deviations

Given a Hermitian operator $\hat{A}$ and a normalized state $\psi$, the **expectation value** is

$$\langle\hat{A}\rangle = \int_{-\infty}^{\infty}\psi^*(x)\,(\hat{A}\psi)(x)\,dx.$$

For position: $\langle\hat{x}\rangle = \int x|\psi|^2\,dx$ (this is just the centroid of the probability density — the same formula as the mean of any probability distribution).

For momentum: $\langle\hat{p}\rangle = \int\psi^*(-i\hbar\partial_x\psi)\,dx$.

The sign matters. For a wave packet moving to the right with $k_0 > 0$, the real part of $\psi$ oscillates and the imaginary part lags by a quarter cycle (Chapter 1). Differentiating $\psi = Ne^{-x^2/2\sigma^2}e^{ik_0 x}$ gives $\partial_x\psi = \psi(-x/\sigma^2 + ik_0)$, so:

$$-i\hbar\partial_x\psi = \psi\left(\frac{i\hbar x}{\sigma^2} + \hbar k_0\right).$$

The $i\hbar x/\sigma^2$ term integrates to zero (odd times the symmetric $|\psi|^2$). What remains:

$$\langle\hat{p}\rangle = \hbar k_0\int|\psi|^2\,dx = \hbar k_0 > 0.$$

A rightward-moving packet has positive expectation value of momentum. If you use $+i\hbar\partial_x$ instead, you get $-\hbar k_0$ — wrong sign, wrong direction. The minus sign in $\hat{p} = -i\hbar\partial_x$ is essential for the physics to be consistent.

The **variance** of an observable in state $\psi$ is

$$\sigma_A^2 = \langle\hat{A}^2\rangle - \langle\hat{A}\rangle^2 = \langle(\hat{A} - \langle\hat{A}\rangle)^2\rangle.$$

The standard deviation $\sigma_A$ is its square root. This is the spread of measurement outcomes across many identically prepared copies of the state — not the uncertainty in any single measurement.

### The Canonical Commutation Relation

The **commutator** of two operators is

$$[\hat{A}, \hat{B}] \equiv \hat{A}\hat{B} - \hat{B}\hat{A}.$$

If this is zero, the operators commute: they share a common eigenbasis and can both be assigned definite values simultaneously. If it is nonzero, they cannot.

For $\hat{x}$ and $\hat{p}$, we compute the commutator by acting on a test function $\psi(x)$:

$$[\hat{x}, \hat{p}]\psi = \hat{x}(\hat{p}\psi) - \hat{p}(\hat{x}\psi).$$

First term: $\hat{p}\psi = -i\hbar\partial_x\psi$, then $\hat{x}$ multiplies by $x$:

$$\hat{x}(\hat{p}\psi) = x\cdot(-i\hbar\partial_x\psi) = -i\hbar x\frac{\partial\psi}{\partial x}.$$

Second term: $\hat{x}\psi = x\psi$, then apply $\hat{p} = -i\hbar\partial_x$ to the *product* $x\psi$:

$$\hat{p}(\hat{x}\psi) = -i\hbar\frac{\partial}{\partial x}(x\psi) = -i\hbar\left(\psi + x\frac{\partial\psi}{\partial x}\right) = -i\hbar\psi - i\hbar x\frac{\partial\psi}{\partial x}.$$

The product rule generates an extra term $-i\hbar\psi$. Subtract:

$$[\hat{x},\hat{p}]\psi = \left(-i\hbar x\frac{\partial\psi}{\partial x}\right) - \left(-i\hbar\psi - i\hbar x\frac{\partial\psi}{\partial x}\right) = i\hbar\psi.$$

Since this holds for any test function $\psi$:

$$\boxed{[\hat{x}, \hat{p}] = i\hbar.}$$

This is the **canonical commutation relation**. It is the single algebraic identity that separates quantum mechanics from classical mechanics — in classical mechanics, position and momentum Poisson-commute, $\{x, p\} = 1$, with no factor of $i\hbar$. The Bohr correspondence principle says $[\cdot, \cdot]/i\hbar \to \{\cdot, \cdot\}$ as $\hbar \to 0$, connecting the two structures.

The commutator is nonzero, so $\hat{x}$ and $\hat{p}$ share no common eigenbasis. No state can be simultaneously an eigenstate of both. Any state with a definite position is a Dirac delta — infinitely spread in momentum. Any state with a definite momentum is a plane wave — infinitely spread in position. The incompatibility is intrinsic to the algebra.

### The Robertson Inequality and the Uncertainty Principle

Here is the theorem, proved without any appeal to measurement disturbance.

**Robertson inequality (1929).** For any two Hermitian operators $\hat{A}$, $\hat{B}$ and any state $\psi$:

$$\sigma_A\,\sigma_B \geq \frac{1}{2}\bigl|\langle[\hat{A}, \hat{B}]\rangle\bigr|.$$

**Proof.** Define shifted operators $\hat{A}' = \hat{A} - \langle\hat{A}\rangle$ and $\hat{B}' = \hat{B} - \langle\hat{B}\rangle$. Their variances satisfy $\sigma_A^2 = \|\hat{A}'|\psi\rangle\|^2$ and $\sigma_B^2 = \|\hat{B}'|\psi\rangle\|^2$. By the Cauchy-Schwarz inequality:

$$\sigma_A^2\sigma_B^2 = \|\hat{A}'|\psi\rangle\|^2\,\|\hat{B}'|\psi\rangle\|^2 \geq \bigl|\langle\psi|\hat{A}'\hat{B}'|\psi\rangle\bigr|^2.$$

Decompose $\hat{A}'\hat{B}'$ into symmetric and antisymmetric parts:

$$\hat{A}'\hat{B}' = \tfrac{1}{2}\{\hat{A}', \hat{B}'\} + \tfrac{1}{2}[\hat{A}', \hat{B}'].$$

The anticommutator $\{\hat{A}', \hat{B}'\}$ is Hermitian, so $\langle\{\hat{A}',\hat{B}'\}\rangle$ is real. The commutator $[\hat{A}',\hat{B}'] = [\hat{A},\hat{B}]$ is anti-Hermitian (since both $\hat{A},\hat{B}$ are Hermitian), so $\langle[\hat{A},\hat{B}]\rangle$ is purely imaginary. Their squares add in modulus:

$$|\langle\hat{A}'\hat{B}'\rangle|^2 = \tfrac{1}{4}\langle\{\hat{A}',\hat{B}'\}\rangle^2 + \tfrac{1}{4}|\langle[\hat{A},\hat{B}]\rangle|^2.$$

Both terms are non-negative. Drop the anticommutator term (a legitimate lower bound — we are making the bound weaker, not tighter):

$$\sigma_A^2\sigma_B^2 \geq \tfrac{1}{4}|\langle[\hat{A},\hat{B}]\rangle|^2.$$

Take the square root:

$$\sigma_A\sigma_B \geq \tfrac{1}{2}|\langle[\hat{A},\hat{B}]\rangle|. \qquad \square$$

Plug in $\hat{A} = \hat{x}$, $\hat{B} = \hat{p}$, $[\hat{x},\hat{p}] = i\hbar$:

$$\sigma_x\,\sigma_p \geq \frac{1}{2}|i\hbar| = \frac{\hbar}{2}.$$

This is the **Kennard inequality** (Kennard proved it in 1927; Robertson gave the general form in 1929). It is a theorem, not a postulate. It follows from the canonical commutation relation $[\hat{x},\hat{p}] = i\hbar$ and the Cauchy-Schwarz inequality. No experiment is performed in the proof. No measurement disturbs anything. The bound is a property of the state $\psi$ — determined before any measurement takes place.

**The Kennard interpretation (what the inequality actually says).** Prepare one million copies of the state $\psi$. Measure position on 500,000 of them and compute the sample standard deviation $\sigma_x$. Measure momentum on the other 500,000 and compute $\sigma_p$. Their product satisfies $\sigma_x\sigma_p \geq \hbar/2$. No copy is measured twice. The bound is established by the *preparation*, not the *measurement*.

This is distinct from Heisenberg's 1927 microscope story, in which observing a particle with a photon kicks its momentum. That story gives correct intuition for a different — and measurably distinct — inequality: the error-disturbance relation (formalized by Ozawa in 2003 [verify], tested by Erhart et al. in 2012 [verify]). The two inequalities have different mathematical forms and different experimental proofs. Do not conflate them.

---

## Worked Example: $\sigma_x\sigma_p$ for the Infinite-Square-Well Ground State

**The lesson.**

We computed $\sigma_x\sigma_p = \hbar/2$ for the Gaussian in Chapter 1. Let us do it for a different state — the ground state of the infinite square well — and show the bound is satisfied but not saturated.

**The state.** On $0 \leq x \leq L$:

$$\psi_1(x) = \sqrt{\frac{2}{L}}\sin\!\left(\frac{\pi x}{L}\right).$$

**Step 1: Compute $\langle x\rangle$.** By symmetry of $\sin^2(\pi x/L)$ around $x = L/2$:

$$\langle x\rangle = \frac{2}{L}\int_0^L x\sin^2\!\left(\frac{\pi x}{L}\right)dx = \frac{L}{2}.$$

(The integral evaluates to $L^2/4$ using $\sin^2\theta = (1 - \cos 2\theta)/2$ and integrating by parts.)

**Step 2: Compute $\langle x^2\rangle$.** Using $\int_0^L x^2\sin^2(\pi x/L)\,dx$ (integration by parts twice, or the known formula):

$$\langle x^2\rangle = \frac{L^2}{3} - \frac{L^2}{2\pi^2} = L^2\!\left(\frac{1}{3} - \frac{1}{2\pi^2}\right).$$

**Step 3: Position standard deviation.**

$$\sigma_x^2 = \langle x^2\rangle - \langle x\rangle^2 = L^2\!\left(\frac{1}{3} - \frac{1}{2\pi^2}\right) - \frac{L^2}{4} = L^2\!\left(\frac{1}{12} - \frac{1}{2\pi^2}\right).$$

Numerically: $1/12 \approx 0.0833$, $1/(2\pi^2) \approx 0.0507$, so $\sigma_x^2 \approx 0.0326\,L^2$, giving $\sigma_x \approx 0.181\,L$.

**Step 4: Compute $\langle p\rangle$.**

$$\langle p\rangle = \int_0^L\psi_1^*(x)\left(-i\hbar\frac{d}{dx}\right)\psi_1(x)\,dx = \frac{2}{L}\int_0^L \sin\!\left(\frac{\pi x}{L}\right)\cdot\left(-i\hbar\frac{\pi}{L}\right)\cos\!\left(\frac{\pi x}{L}\right)dx.$$

The integrand is $\sin\theta\cos\theta = \tfrac{1}{2}\sin 2\theta$, integrated from $0$ to $L$ (one full period). It integrates to zero. $\langle p\rangle = 0$.

This makes physical sense: the ground state is a standing wave, equal superposition of a right-moving plane wave $e^{i\pi x/L}$ and a left-moving wave $e^{-i\pi x/L}$. Equal positive and negative momentum contributions cancel in the average.

**Step 5: Compute $\langle p^2\rangle$.**

Here is a shortcut. The ground state $\psi_1$ satisfies the TISE $\hat{H}\psi_1 = E_1\psi_1$ with $E_1 = \hbar^2\pi^2/(2mL^2)$. Inside the well, $\hat{H} = \hat{p}^2/2m$, so $\hat{p}^2\psi_1 = 2mE_1\psi_1 = (\hbar\pi/L)^2\psi_1$. Therefore:

$$\langle p^2\rangle = \int\psi_1^*\hat{p}^2\psi_1\,dx = \left(\frac{\hbar\pi}{L}\right)^2\int|\psi_1|^2\,dx = \left(\frac{\hbar\pi}{L}\right)^2.$$

**Step 6: Momentum standard deviation.**

$$\sigma_p^2 = \langle p^2\rangle - \langle p\rangle^2 = \left(\frac{\hbar\pi}{L}\right)^2 - 0 = \left(\frac{\hbar\pi}{L}\right)^2, \qquad \sigma_p = \frac{\hbar\pi}{L}.$$

**Step 7: The product.**

$$\sigma_x\sigma_p \approx 0.181\,L \cdot \frac{\hbar\pi}{L} = 0.181\pi\,\hbar \approx 0.568\,\hbar.$$

Since $\hbar/2 = 0.5\,\hbar$, the product is $\approx 0.568\,\hbar > 0.5\,\hbar$. The Kennard bound is satisfied. The ratio is $\sigma_x\sigma_p/(\hbar/2) \approx 1.136$.

**The limit.** Why doesn't the square-well ground state saturate the bound? Because the bound is saturated *only* by the Gaussian wave function (minimum-uncertainty state). The saturation condition requires that $\hat{A}'|\psi\rangle = i\lambda\hat{B}'|\psi\rangle$ for some real constant $\lambda$ — that is, the Cauchy-Schwarz inequality must hold with equality, which requires the two vectors $\hat{A}'|\psi\rangle$ and $\hat{B}'|\psi\rangle$ to be proportional. For $\hat{A}' = \hat{x} - \langle x\rangle$ and $\hat{B}' = \hat{p} - \langle p\rangle$, this condition translates to a differential equation whose only normalizable solution is the Gaussian. The square-well ground state has hard walls that force $\psi(0) = \psi(L) = 0$ — it cannot be a Gaussian. Its product $\sigma_x\sigma_p$ is strictly above $\hbar/2$.

The simulation check: open `01-probability-explorer.html` from Chapter 1, select the infinite-well, set $n = 1$, $L = 10\,\text{nm}$. Read $\sigma_x\sigma_p/(\hbar/2)$. It should read approximately $1.136$. This is the same calculation, done numerically.

---

## Common Misconceptions

**"The uncertainty principle is about measurement disturbing the particle."** Heisenberg's 1927 microscope thought experiment is physically illuminating but describes a different statement — the error-disturbance relation. The Kennard inequality ($\sigma_x\sigma_p \geq \hbar/2$) is about preparation, verified across an ensemble of independently prepared copies with no copy measured twice. The distinction has been tested experimentally (Erhart et al. 2012). State this clearly and do not return to the microscope story.

**"Hermitian means symmetric — the matrix is equal to its transpose."** This is true only for real matrices. The Pauli matrix $\sigma_y = \bigl(\begin{smallmatrix}0 & -i\\ i & 0\end{smallmatrix}\bigr)$ is Hermitian because its *conjugate* transpose equals itself. Its ordinary transpose is $-\sigma_y$. For complex operators, the adjoint is $\hat{A}^\dagger = (\hat{A}^T)^*$: transpose then conjugate. Dropping the conjugation is the most common sign error in qubit calculations.

**"$\langle p\rangle = 0$ means the particle has no momentum."** The square-well ground state has $\langle p\rangle = 0$ but $\sigma_p = \hbar\pi/L \neq 0$. Individual measurements of momentum return $\pm\hbar\pi/L$ with equal probability. The mean is zero because equal probabilities of positive and negative outcomes cancel. $\langle p\rangle = 0$ means the state has no preferred direction of motion, not that the particle is at rest. This is the standing-wave interpretation: equal amplitudes of left- and right-moving components.

**"Commuting operators always have the same eigenstates."** Commuting operators share a *common eigenbasis*, but individual eigenstates can be degenerate. If $\hat{A}$ has a degenerate eigenvalue $a$ (multiple linearly independent eigenstates with the same eigenvalue), then the eigenstates of $\hat{B}$ within that degenerate subspace may differ from the eigenstates of $\hat{A}$. The precise statement: $[\hat{A},\hat{B}] = 0$ guarantees there *exists* a simultaneous eigenbasis, not that every eigenstate of $\hat{A}$ is automatically one of $\hat{B}$.

**"The bound $\sigma_x\sigma_p \geq \hbar/2$ is the tightest possible."** The Robertson inequality drops the anticommutator term, making it weaker than it could be. The Schrödinger inequality (1930) retains that term and is tighter: $\sigma_x^2\sigma_p^2 \geq \tfrac{1}{4}|\langle\{\hat{x}',\hat{p}'\}\rangle|^2 + \tfrac{1}{4}\hbar^2$. The Robertson bound is a lower bound on the Schrödinger bound, which is itself a lower bound on the variance product. For the Gaussian, the anticommutator term happens to be zero, so both bounds agree and both are saturated. For other states, the Schrödinger bound is strictly tighter.

---

## Exercises

**Warm-up**

1. *[Hermiticity of the momentum operator]* Prove that $\hat{p} = -i\hbar\partial_x$ is Hermitian using integration by parts. State explicitly: (a) what boundary condition on $\psi$ and $\phi$ is required for the boundary term to vanish; (b) why this condition holds for any physically normalizable state; (c) what would go wrong with the Hermitian proof if you replaced $\hat{p}$ by the real operator $\hat{p}_{real} = \hbar\partial_x$ (without the $-i$). *Difficulty: warm-up.*

2. *[Canonical commutation relation]* Derive $[\hat{x}, \hat{p}] = i\hbar$ step by step, applying both operators to a test function $\psi(x)$. Show every product-rule term explicitly. (a) At which step does the constant $i\hbar$ emerge? (b) What would $[\hat{x},\hat{p}]$ be if $\hat{p}$ were defined as $\hat{p}' = +i\hbar\partial_x$ instead? (c) Compute $[\hat{p},\hat{x}]$ and verify it equals $-i\hbar$. *Difficulty: warm-up.*

3. *[Expectation values and standard deviations]* For the state $\psi(x) = (1/\pi a^2)^{1/4}e^{-x^2/2a^2}e^{ik_0 x}$ with $a = 2\,\text{nm}$ and $k_0 = 3\,\text{nm}^{-1}$: (a) without computing integrals, state $\langle x\rangle$ and $\langle p\rangle$ and justify each in one sentence; (b) write down the integrals for $\langle x^2\rangle$ and $\langle p^2\rangle$ and use the results from Chapter 1 to evaluate them; (c) compute $\sigma_x$, $\sigma_p$, and their product. *Difficulty: warm-up.*

**Application**

4. *[Infinite-square-well uncertainty: higher modes]* For the $n$th eigenstate $\psi_n(x) = \sqrt{2/L}\sin(n\pi x/L)$ on $[0,L]$: (a) show that $\langle p\rangle = 0$ for all $n$ (not just $n = 1$); (b) use the fact that $\hat{p}^2\psi_n = (n\hbar\pi/L)^2\psi_n$ to find $\sigma_p = n\hbar\pi/L$; (c) compute $\sigma_x$ for general $n$ (the formula is $\sigma_x^2 = L^2(1/12 - 1/(2n^2\pi^2))$; verify for $n = 1$); (d) find the limit of $\sigma_x\sigma_p/(\hbar/2)$ as $n \to \infty$ and interpret it. *Difficulty: application.*

5. *[Operator algebra shortcut]* For any state $\psi$ and any Hermitian operator $\hat{A}$ with eigenvalue equation $\hat{A}\psi = \lambda\psi$ (i.e., $\psi$ is an eigenstate of $\hat{A}$): (a) show that $\langle\hat{A}\rangle = \lambda$ and $\langle\hat{A}^2\rangle = \lambda^2$, so $\sigma_A = 0$; (b) the Robertson inequality then gives $\sigma_A\sigma_B \geq \tfrac{1}{2}|\langle[\hat{A},\hat{B}]\rangle|$ for any $\hat{B}$. If $\hat{A} = \hat{p}$ and $\psi = e^{ik_0 x}$ (a plane wave), what does the Robertson inequality say about $\sigma_x$? Does this contradict normalizability? (c) Resolve the apparent contradiction: why does the Robertson inequality still hold even when $\psi$ is not normalizable? *Difficulty: application.*

6. *[Robertson for Pauli operators — the qubit preview]* The Pauli matrices $\sigma_x, \sigma_y, \sigma_z$ satisfy $[\sigma_x, \sigma_z] = -2i\sigma_y$. Consider the qubit state $|\psi\rangle = \cos(\theta/2)|0\rangle + \sin(\theta/2)|1\rangle$ (taking $\phi = 0$ on the Bloch sphere). (a) Compute $\langle\sigma_y\rangle$ for this state. (b) Write down the Robertson bound $\sigma_{\sigma_x}\sigma_{\sigma_z} \geq |\langle\sigma_y\rangle|$. (c) At $\theta = \pi/2$ (equatorial state), compute $\langle\sigma_x\rangle$, $\langle\sigma_x^2\rangle$, $\sigma_{\sigma_x}$, and likewise for $\sigma_z$. Verify the bound. (d) At which $\theta$ is the bound saturated, and what is the state then? *Difficulty: application.*

**Synthesis**

7. *[The minimum-uncertainty state]* The Gaussian wave function is the unique minimum-uncertainty state for $\hat{x}$ and $\hat{p}$. The saturation condition for Cauchy-Schwarz is that $\hat{A}'|\psi\rangle = c\hat{B}'|\psi\rangle$ for some complex constant $c$. (a) Set $\hat{A}' = \hat{x} - \langle x\rangle$ and $\hat{B}' = \hat{p} - \langle p\rangle$, and write this as a differential equation for $\psi(x)$. (b) Show the solution is a Gaussian: $\psi(x) \propto e^{-\alpha(x-x_0)^2}e^{ik_0 x}$ for some complex $\alpha$. (c) For saturation of the Robertson bound (rather than the Schrödinger bound), $c$ must be purely imaginary: $c = i\lambda$ with $\lambda \in \mathbb{R}$. Show that this forces $\text{Re}(\alpha) > 0$ — the Gaussian must decay, not grow. *Difficulty: synthesis.*

8. *[Ehrenfest's theorem]* Ehrenfest's theorem says $d\langle\hat{x}\rangle/dt = \langle\hat{p}\rangle/m$ and $d\langle\hat{p}\rangle/dt = -\langle\partial V/\partial x\rangle$. (a) Derive the first relation by differentiating $\langle\hat{x}\rangle = \int x|\psi|^2\,dx$ with respect to time and using the Schrödinger equation. (b) Derive the second by differentiating $\langle\hat{p}\rangle = \int\psi^*(-i\hbar\partial_x\psi)\,dx$ with respect to time and using the Schrödinger equation with potential $V(x)$. (c) For the free particle ($V = 0$): what do these two relations say about the motion of $\langle x\rangle$ and $\langle p\rangle$? Connect this to the group-velocity result from Chapter 8. *Difficulty: synthesis.*

**Challenge**

9. *[The Schrödinger uncertainty relation]* (a) In the Robertson proof, the dropped anticommutator term $\tfrac{1}{4}\langle\{\hat{x}',\hat{p}'\}\rangle^2$ is non-negative. Show this explicitly. (b) Retain it to obtain the Schrödinger bound: $\sigma_x^2\sigma_p^2 \geq \tfrac{1}{4}|\langle\{\hat{x}',\hat{p}'\}\rangle|^2 + \hbar^2/4$. (c) For the Gaussian state, compute $\langle\{\hat{x}',\hat{p}'\}\rangle$ directly and show it equals zero — confirming that the anticommutator term vanishes and Robertson $=$ Schrödinger for the Gaussian. (d) For the infinite-square-well ground state, show the anticommutator term is non-zero (you need not compute it exactly; argue by contradiction using the fact that the state does not saturate Robertson). *Difficulty: challenge.*

---

## Still Puzzling

The Robertson inequality drops the anticommutator term, making it a weaker bound than necessary. The Schrödinger (1930) inequality retains that term. For most states and most pairs of observables, the Schrödinger bound is strictly tighter. The question of which states achieve equality in the Schrödinger bound — and whether there is a physical characterization of them — is still discussed in the research literature.

The Kennard–Robertson framework measures uncertainty through variance. But variance is not the only reasonable measure of spread. The entropic uncertainty relations of Maassen and Uffink (1988) replace $\sigma_A^2$ with the Shannon entropy $H(A)$ of the measurement distribution, giving $H(x) + H(p) \geq \log(e\pi\hbar)$. Entropic bounds are in some ways tighter (they apply to non-Gaussian states where variance is not the most informative measure of spread) and are central to quantum information theory and cryptography. They are graduate-level content, but worth naming here.

The error-disturbance relations (Ozawa 2003, Erhart et al. 2012, Rozema et al. 2012) are a genuinely different class of inequality, describing what happens when you measure one observable and ask how much the act of measurement disturbs a subsequent measurement of the other. Their experimental tests required weak measurements and quantum tomography — techniques beyond the scope of this volume. The distinction between preparation uncertainty (Robertson) and disturbance uncertainty (Ozawa-type) is conceptually important and not yet part of most undergraduate curricula.

---

## The +1 — Simulation Exercise: Expectation Values and the Uncertainty Bound

The deliverable uses the existing `01-probability-explorer.html` from Chapter 1. No new file is required; the Chapter 1 simulation already displays $\sigma_x$, $\sigma_p$, and the ratio $\sigma_x\sigma_p/(\hbar/2)$.

### Part A — CLAUDE.md amendment for this chapter

````markdown
## Chapter 9 — Operators and Uncertainty

PHYSICS CHECKS
- Momentum operator: p̂ = −iℏ ∂_x. Sign is load-bearing.
  For a wave packet with k₀ > 0, ⟨p̂⟩ > 0 must hold.
- Expectation value computed as: <A> = integral psi* (A psi) dx.
  Not as integral |psi|^2 A dx (that would only be correct for A = x).
- Variance: sigma_A^2 = <A^2> - <A>^2. Both terms required.
- Canonical commutation check: [x̂, p̂] psi = iℏ psi.
  If your code implements [x̂, p̂] on a grid, the output should be iℏ * psi
  pointwise (up to grid errors at boundaries). Build this as a startup assertion.
- The ratio sigma_x * sigma_p / (ℏ/2):
    Gaussian: must read 1.000.
    Infinite-well n=1, L=10 nm: must read ≈ 1.136.
    Infinite-well n→∞: approaches π/sqrt(3) ≈ 1.814 asymptotically.
  These are verification targets, not adjustable parameters.
````

### Part B — Exploration tasks using the existing simulation

**Task 1 — Saturating the bound with the Gaussian.** Open `01-probability-explorer.html`. Select the Gaussian wave function, $a = 1\,\text{nm}$, $k_0 = 5\,\text{nm}^{-1}$. Read: $\sigma_x \approx 0.707\,\text{nm}$, $\sigma_p \approx 0.707\,\hbar/\text{nm}$, ratio $\approx 1.000$. Now slide $a$ from $0.2$ to $4\,\text{nm}$. $\sigma_x$ scales with $a$; $\sigma_p$ scales inversely. The ratio stays locked at $1.000$. Write: what does this confirm about the Gaussian being the minimum-uncertainty state?

**Task 2 — The infinite well exceeds the bound.** Switch to the infinite-well eigenstate, $n = 1$, $L = 10\,\text{nm}$. Read $\sigma_x \approx 1.81\,\text{nm}$, $\sigma_p \approx 0.314\,\hbar/\text{nm}$ (since $\sigma_p = \pi\hbar/L$ and $\pi/10\,\text{nm} = 0.314\,\text{nm}^{-1}$), ratio $\approx 1.136$. Compare with the analytical calculation from the worked example in this chapter. Do they match to within $1\%$?

**Task 3 — Higher modes and the bound.** Still in the infinite-well mode. Step $n$ from $1$ to $10$. Record the ratio $\sigma_x\sigma_p/(\hbar/2)$ for each $n$. Plot or tabulate. Does the ratio grow, converge, or oscillate? From exercise 4 you derived $\sigma_x\sigma_p/(\hbar/2) \to \pi/\sqrt{3} \approx 1.814$ as $n \to \infty$. Does the simulation approach this limit? At what $n$ are you within $5\%$ of the limit?

**Task 4 — The sign of momentum.** Select the Gaussian with $k_0 = +5\,\text{nm}^{-1}$. Read $\langle p\rangle$: it should be positive (approximately $5\,\hbar/\text{nm}$). Change $k_0$ to $-5\,\text{nm}^{-1}$. Now $\langle p\rangle$ should be negative. The magnitude of $\sigma_p$ is unchanged; only the sign of the mean flips. This verifies that $\hat{p} = -i\hbar\partial_x$ gives the correct sign for both directions of motion.

### Part C — New simulation prompt (optional extension)

If you want a Chapter 9-specific simulation for the commutator and Robertson bound:

````markdown
SHOW.
The canonical commutation relation [x̂, p̂] = iℏ and its consequence for uncertainty.

Build a simulation that computes expectation values and variances
for user-selectable wave functions, and displays:
  - <x>, <x^2>, sigma_x
  - <p>, <p^2>, sigma_p
  - sigma_x * sigma_p / (ℏ / 2)   [the uncertainty ratio]
  - A visual of the Robertson bound: a point (sigma_x, sigma_p) on a log-log
    plot, with the boundary curve sigma_x * sigma_p = ℏ/2 drawn.

Wave functions (dropdown):
  1. Gaussian with sliders a, k0.
  2. Infinite-well eigenstate n on [0, L] with sliders n (integer 1-10), L.
  3. Superposition: alpha * psi_1 + beta * psi_2 in the infinite well,
     with sliders for alpha, beta (normalized).

The log-log plot should show:
  - The Robertson boundary (hyperbola sigma_x * sigma_p = ℏ/2) as a solid curve.
  - The current state as a dot. Gaussian: on the curve. Well: above the curve.
  - As you increase n in the well, the dot moves up and right.

SAY.
Produce a single file 09-operators-and-uncertainty.html.

CONSTRAIN.
  - D3 v7 from CDN. SVG only. N = 500 grid points.
  - sigma_x, sigma_x^2: compute via Simpson's rule on x |psi|^2 and x^2 |psi|^2.
  - sigma_p, sigma_p^2: compute via FFT to momentum space, Simpson on p |phi|^2 and p^2 |phi|^2.
  - The commutator check: for any psi, [x̂, p̂] psi should numerically equal iℏ psi
    pointwise. Display max deviation from iℏ as a "commutator residual" --- should
    read ≈ 0 (up to grid discretization).
  - The Robertson-boundary plot must show the Gaussian point on the curve (ratio 1.000)
    and the well n=1 point above it (ratio ≈ 1.136). Label both.

VERIFY.
  (a) Gaussian a = 1 nm, k0 = 0: sigma_x = 1/sqrt(2) nm, sigma_p = ℏ/(sqrt(2) nm), ratio = 1.000.
  (b) Well n=1, L=10 nm: sigma_x ≈ 1.81 nm, sigma_p ≈ π ℏ / 10 nm ≈ 0.314 ℏ/nm, ratio ≈ 1.136.
  (c) Well n=10, L=10 nm: ratio closer to π/sqrt(3) ≈ 1.814.
  (d) Commutator residual < 1e-3 ℏ for N = 500.
````

---

## References

- Kennard, E. H. (1927). Zur Quantenmechanik einfacher Bewegungstypen. *Zeitschrift für Physik*, 44(4-5), 326–352. Original proof of $\sigma_x\sigma_p \geq \hbar/2$ from the wave-mechanical formalism. [verify]
- Robertson, H. P. (1929). The uncertainty principle. *Physical Review*, 34(1), 163–164. General proof of $\sigma_A\sigma_B \geq \tfrac{1}{2}|\langle[\hat{A},\hat{B}]\rangle|$ for any two Hermitian operators. [verify]
- Schrödinger, E. (1930). Zum Heisenbergschen Unschärfeprinzip. *Sitzungsberichte der Preussischen Akademie der Wissenschaften*, Physikalisch-mathematische Klasse, 296–303. The tighter inequality retaining the anticommutator term. [verify]
- Griffiths, D. J. & Schroeter, D. F. (2018). *Introduction to Quantum Mechanics* (3rd ed.). Cambridge University Press. §1.6 "The Uncertainty Principle," §3.5 "Generalized Statistical Interpretation." Standard undergraduate treatment.
- Ozawa, M. (2003). Universally valid reformulation of the Heisenberg uncertainty principle on noise and disturbance in measurement. *Physical Review A*, 67(4), 042105. Formalization of the error-disturbance relation distinct from Robertson. [verify]
- Erhart, J., Sponar, S., Sulyok, G., Badurek, G., Ozawa, M., & Hasegawa, Y. (2012). Experimental demonstration of a universally valid error-disturbance uncertainty relation in spin measurements. *Nature Physics*, 8, 185–189. Experimental test of the Ozawa inequality. [verify]
- Maassen, H. & Uffink, J. B. M. (1988). Generalized entropic uncertainty relations. *Physical Review Letters*, 60(12), 1103–1106. Entropic uncertainty bounds tighter than variance-based Robertson for non-Gaussian states. [verify]
- Townsend, J. S. (2012). *A Modern Approach to Quantum Mechanics* (2nd ed.). University Science Books. §3.5 "The Generalized Uncertainty Principle." Second source for operator-algebraic derivation. [verify]
