# Chapter 11 — Measurement, Superposition, and the Qubit

## TL;DR

- Every quantum measurement has only two possible kinds of output: a list of eigenvalues, and a probability for each — given by the squared overlap of the state with the corresponding eigenstate.
- After a measurement returns a particular outcome, the state updates to that outcome's eigenstate. This is collapse. It is not metaphysics — it is the state-update rule.
- The simplest system where all of this is visible by hand is the qubit: a two-dimensional Hilbert space, two possible outcomes per measurement, and every number computable with 2×2 matrices and complex arithmetic.
- The Stern-Gerlach experiment is the canonical physical realization: spin-½ in an inhomogeneous magnetic field splits into exactly two beams, weighted by the Born-rule probabilities.
- The Bloch sphere is a geometric picture of every possible qubit state. Time evolution — the Larmor precession you will compute fully in Vol. 2 — is a rotation on that sphere.

---

An afternoon in Göttingen, 1925. Werner Heisenberg is sick with hay fever, has fled to the island of Helgoland, and is staring at the problem that has been blocking him for months: how to write a theory of atomic transitions that uses only numbers you can actually measure, not electron orbits that nobody has ever seen.

He is about to invent matrix mechanics. But right now what he is staring at is a simpler, more visceral question: when you measure something quantum, what happens?

This chapter answers that question — carefully, completely, and with numbers you can compute.

---

## The measurement postulate

The formalism of Chapter 10 gave us Hermitian operators and the spectral theorem. Here is the payoff.

Let $\hat{A}$ be a Hermitian observable with discrete eigenvalues $\{a_n\}$ and orthonormal eigenstates $\{|a_n\rangle\}$. When you measure $\hat{A}$ on a system in state $|\psi\rangle$, three things happen — and only three:

**1. The only possible outcomes are eigenvalues.**
Nothing else can emerge from a measurement of $\hat{A}$. Not a value between $a_1$ and $a_2$. Not a superposition of results. Exactly one eigenvalue $a_n$, with nothing in between.

**2. The probability of getting $a_n$ is**

$$\boxed{P(a_n) = |\langle a_n|\psi\rangle|^2.}$$

This is the Born rule, restated in Dirac language. The inner product $\langle a_n|\psi\rangle$ is a complex number — the amplitude — and its modulus squared is the probability. Geometrically: $P(a_n)$ is the squared length of the projection of $|\psi\rangle$ onto the eigenket $|a_n\rangle$.

**3. Immediately after the measurement returns $a_n$, the state is $|a_n\rangle$.**

This is **collapse**. The state has been updated. Subsequent measurements on the same system should be predicted using $|a_n\rangle$, not the original $|\psi\rangle$.

These three statements together are the **measurement postulate**. They are a postulate — we take them as a starting point of the theory, confirmed by experiment, not derivable from the Schrödinger equation alone (though the ongoing attempt to derive them is what keeps interpretation theorists employed; more in "Still Puzzling").

Note what the postulate does not say. It does not say that a measurement disturbs the particle and thereby changes its state. The state update is not about disturbance; it is about information. After getting outcome $a_n$, we know the system returned $a_n$. The sub-ensemble of all experiments that produced $a_n$ is now characterized by state $|a_n\rangle$. That is what collapse means operationally.

The completeness of the eigenstates guarantees that the probabilities sum to 1:

$$\sum_n P(a_n) = \sum_n |\langle a_n|\psi\rangle|^2 = \langle\psi|\left(\sum_n |a_n\rangle\langle a_n|\right)|\psi\rangle = \langle\psi|\hat{I}|\psi\rangle = 1.$$

No probability leaks. No extra option is missing. The formalism is consistent.

---

## The two-state system — why start here

The abstract postulate is clean. The concrete version — where you can work through the algebra by hand and draw a picture — is the two-state system.

A **qubit** is a quantum system whose Hilbert space is $\mathbb{C}^2$: all two-component complex vectors. Pick a basis $\{|0\rangle, |1\rangle\}$. The most general normalized state is

$$|\psi\rangle = \alpha|0\rangle + \beta|1\rangle, \qquad \alpha,\beta \in \mathbb{C}, \qquad |\alpha|^2 + |\beta|^2 = 1.$$

Two real parameters determine the state (up to an irrelevant global phase). An electron's spin, a photon's polarization, a superconducting circuit's two lowest energy levels — all of these are physical qubits. The mathematics is the same for all of them.

The standard observables on a qubit are the three **Pauli operators**:

$$\sigma_x = \begin{pmatrix}0 & 1\\1 & 0\end{pmatrix}, \qquad \sigma_y = \begin{pmatrix}0 & -i\\i & 0\end{pmatrix}, \qquad \sigma_z = \begin{pmatrix}1 & 0\\0 & -1\end{pmatrix}.$$

Each is Hermitian ($\sigma_i^\dagger = \sigma_i$), each squares to the identity ($\sigma_i^2 = \hat{I}$), and each has eigenvalues $\pm 1$. Their commutators follow the pattern $[\sigma_i, \sigma_j] = 2i\epsilon_{ijk}\sigma_k$, so for example $[\sigma_x, \sigma_z] = -2i\sigma_y$ — they do not commute, which means measuring one after the other in different orders gives different results.

A word of warning about $\sigma_y$: the off-diagonal entry $-i$ in the upper-right is correct. This is the single most common sign error in qubit computations. The fact that $\sigma_y$ is Hermitian despite looking antisymmetric as a real matrix is not a contradiction — Hermitian means self-adjoint, meaning equal to its *conjugate* transpose. The transpose of $\sigma_y$ is $-\sigma_y$ (antisymmetric); the conjugate transpose of $\sigma_y$ is $+\sigma_y$ (Hermitian). The $i$ does the work. Any code doing qubit calculations should include a startup check: compute $\sigma_y^\dagger$ and verify it equals $\sigma_y$.

---

## The Stern-Gerlach experiment

Before the algebra, the physics.

In 1922, Otto Stern and Walther Gerlach passed silver atoms through an inhomogeneous magnetic field. Classical physics predicted a smear — a continuous distribution of deflections as the magnetic moment of the atom pointed in different directions. What they observed was something that made no classical sense: two discrete spots. [verify]

The magnetic field gradient exerts a force $F_z \propto \mu_z \cdot \partial B/\partial z$ along the field axis. The deflection is proportional to $\mu_z$, the component of the magnetic moment along $\hat{z}$. If angular momentum were classical, $\mu_z$ would be continuous and the pattern would be a smear. Instead: two spots, corresponding to $\mu_z = \pm\mu_B$ (for spin-½ particles). The Born rule is not abstract here. It is written in silver on a glass plate.

The observable is $\hat{S}_z = (\hbar/2)\sigma_z$. Its eigenvalues are $+\hbar/2$ (spin-up, $|0\rangle = |\!\uparrow\rangle$) and $-\hbar/2$ (spin-down, $|1\rangle = |\!\downarrow\rangle$). The measurement postulate says:

- If the atom enters in state $|\psi\rangle = \alpha|\!\uparrow\rangle + \beta|\!\downarrow\rangle$, the probability of hitting the upper spot is $|\alpha|^2$ and the probability of hitting the lower spot is $|\beta|^2$.
- If you block the upper spot and let the lower spot through, the remaining atoms are in state $|\!\downarrow\rangle$ — collapsed, certain.

**Sequential measurements.** This is where the postulate becomes viscerally real. Run three Stern-Gerlach devices in sequence:

1. **Z then Z.** Feed the atoms through a $\hat{z}$-apparatus. Let only the $+\hbar/2$ atoms through (blocking the lower beam). Now feed those through another $\hat{z}$-apparatus. Every atom hits the upper spot. Probability 1. Collapse is stable: if you already know the outcome of a $\hat{S}_z$ measurement, measuring $\hat{S}_z$ again gives the same result.

2. **Z then X.** After the first $\hat{z}$ apparatus selects $|\!\uparrow\rangle$, feed through an $\hat{x}$-apparatus — a Stern-Gerlach device tilted 90°. The $\hat{S}_x$ eigenstates are $|\pm x\rangle = (|\!\uparrow\rangle \pm |\!\downarrow\rangle)/\sqrt{2}$. What is $|\!\uparrow\rangle$ in this basis? It is $(|+x\rangle + |-x\rangle)/\sqrt{2}$. The Born-rule probabilities: $P(+x) = |{}_{}^{}\langle+x|\!\uparrow\rangle|^2 = 1/2$, $P(-x) = 1/2$. The $\hat{z}$-eigenstate is a superposition in the $\hat{x}$-eigenbasis — exactly equal superposition. The atom that was certainly spin-up in $z$ is now 50/50 in $x$.

3. **Z then X then Z.** Now after the $\hat{x}$ measurement, the state has collapsed to $|+x\rangle$ or $|-x\rangle$. Feed back into a $\hat{z}$-apparatus. Since $|+x\rangle = (|\!\uparrow\rangle + |\!\downarrow\rangle)/\sqrt{2}$, the $\hat{z}$ measurement again gives 50/50. The intermediate $\hat{x}$ measurement "erased" the $\hat{z}$ information. Measure $\hat{S}_z$, then measure $\hat{S}_x$ (which collapses to an $\hat{x}$ eigenstate), then measure $\hat{S}_z$ again: the Z certainty is gone.

This is not a failure of the apparatus. It is the non-commutativity of $\hat{S}_x$ and $\hat{S}_z$ made physically tangible. $[\sigma_x, \sigma_z] = -2i\sigma_y \neq 0$. You cannot simultaneously have definite values for both.

---

## State parametrization and the Bloch sphere

Every normalized qubit state (up to a global phase that has no physical consequences) can be written as

$$|\psi\rangle = \cos\!\left(\frac{\theta}{2}\right)|0\rangle + e^{i\phi}\sin\!\left(\frac{\theta}{2}\right)|1\rangle, \qquad \theta \in [0, \pi], \quad \phi \in [0, 2\pi).$$

The factor $\theta/2$ — not $\theta$ — is mandatory. Check it at the boundary cases: $\theta = 0$ gives $|0\rangle$ (as required); $\theta = \pi$ gives $e^{i\phi}|1\rangle$, which is $|1\rangle$ up to a global phase. At $\theta = \pi/2$ we get $(|0\rangle + e^{i\phi}|1\rangle)/\sqrt{2}$ — the equatorial states.

Each state corresponds to a unit vector on a sphere:

$$\vec{r} = \bigl(\langle\sigma_x\rangle,\ \langle\sigma_y\rangle,\ \langle\sigma_z\rangle\bigr) = (\sin\theta\cos\phi,\ \sin\theta\sin\phi,\ \cos\theta).$$

This is the **Bloch sphere**. North pole ($\theta=0$): state $|0\rangle$, spin-up, $\langle\sigma_z\rangle = +1$. South pole ($\theta=\pi$): state $|1\rangle$, spin-down, $\langle\sigma_z\rangle = -1$. Equator ($\theta=\pi/2$): all equal superpositions; $\langle\sigma_z\rangle = 0$. The azimuthal angle $\phi$ is the relative phase between $|0\rangle$ and $|1\rangle$ — and it is physically real. Different values of $\phi$ at the same $\theta$ give different $\langle\sigma_x\rangle$ and $\langle\sigma_y\rangle$, detectable by measuring those operators.

For pure states, $|\vec{r}|^2 = 1$ exactly. This is a useful runtime sanity check: compute the three expectation values numerically and verify their squared sum is within $10^{-6}$ of 1.

The factor of $\theta/2$ in the state is what produces $\theta$ on the sphere (via double-angle identities: $\cos\theta = \cos^2(\theta/2) - \sin^2(\theta/2)$). It also means a full $2\pi$ rotation of the Bloch vector — $\theta: 0 \to 2\pi$ at fixed $\phi$ — corresponds to only a $\pi$ rotation of the state vector, acquiring a factor of $-1$. This is the **spinor double cover** of $SO(3)$. The sign is invisible in the expectation values (which depend on $|\text{components}|^2$) but visible in interference. It is physically real: neutron interferometry has measured it. [verify]

**Preview of time evolution.** Under a Hamiltonian $\hat{H} = (\hbar\omega/2)\hat{n}\cdot\vec{\sigma}$ — as in a spin in a magnetic field — the Bloch vector precesses around $\hat{n}$ at angular velocity $\omega$. This is Larmor precession. The full derivation — using the Pauli anticommutation relation $(\hat{n}\cdot\vec{\sigma})^2 = \hat{I}$ to evaluate the matrix exponential $e^{-i\hat{H}t/\hbar}$ in closed form — is in Vol. 2. Here we note only the geometry: time evolution is a rotation on the Bloch sphere. The sphere is the picture; the dynamics is the rotation.

---

## Worked example: predicting measurement statistics

**The state.** Let

$$|\psi\rangle = \frac{\sqrt{3}}{2}|0\rangle + \frac{i}{2}|1\rangle.$$

Check normalization: $|\sqrt{3}/2|^2 + |i/2|^2 = 3/4 + 1/4 = 1$. Good.

In the Bloch parametrization: $\alpha = \cos(\theta/2) = \sqrt{3}/2$, so $\theta/2 = \pi/6$ and $\theta = \pi/3$. The coefficient of $|1\rangle$ is $e^{i\phi}\sin(\theta/2) = e^{i\phi} \cdot (1/2)$. Since $\beta = i/2 = e^{i\pi/2}/2$, we have $\phi = \pi/2$.

**Measuring $\sigma_z$.**

Eigenvalues: $+1$ with eigenstate $|0\rangle$, $-1$ with eigenstate $|1\rangle$.

$$P(\sigma_z = +1) = |\langle 0|\psi\rangle|^2 = \left|\frac{\sqrt{3}}{2}\right|^2 = \frac{3}{4}.$$

$$P(\sigma_z = -1) = |\langle 1|\psi\rangle|^2 = \left|\frac{i}{2}\right|^2 = \frac{1}{4}.$$

Sanity: $3/4 + 1/4 = 1$. The probabilities sum correctly.

Expectation value:

$$\langle\sigma_z\rangle = (+1)\cdot\frac{3}{4} + (-1)\cdot\frac{1}{4} = \frac{1}{2}.$$

Confirm from the Bloch vector: $\langle\sigma_z\rangle = \cos\theta = \cos(\pi/3) = 1/2$. Consistent.

Variance: $\sigma_{\sigma_z}^2 = \langle\sigma_z^2\rangle - \langle\sigma_z\rangle^2 = 1 - 1/4 = 3/4$, so $\sigma_{\sigma_z} = \sqrt{3}/2$.

**Post-measurement states.**

- If the result is $+1$: the state collapses to $|0\rangle$. A subsequent $\sigma_z$ measurement gives $+1$ with probability 1.
- If the result is $-1$: the state collapses to $|1\rangle$. A subsequent $\sigma_z$ measurement gives $-1$ with probability 1.

**Measuring $\sigma_x$ on the same initial state.**

The $\sigma_x$ eigenstates are $|\pm x\rangle = (|0\rangle \pm |1\rangle)/\sqrt{2}$.

$$P(\sigma_x = +1) = |\langle +x|\psi\rangle|^2 = \left|\frac{1}{\sqrt{2}}\cdot\frac{\sqrt{3}}{2} + \frac{1}{\sqrt{2}}\cdot\frac{i}{2}\right|^2 = \frac{1}{2}\left|\frac{\sqrt{3}+i}{2}\right|^2 = \frac{1}{2}\cdot\frac{3+1}{4} = \frac{1}{2}.$$

$$P(\sigma_x = -1) = \frac{1}{2}.$$

The state is a 50/50 superposition in the $\hat{x}$ direction: $\langle\sigma_x\rangle = 0$. On the Bloch sphere, $\langle\sigma_x\rangle = \sin\theta\cos\phi = \sin(\pi/3)\cos(\pi/2) = (\sqrt{3}/2)\cdot 0 = 0$. Consistent.

**Measuring $\sigma_y$ on the same initial state.**

The $\sigma_y$ eigenstates are $|{\pm}y\rangle = (|0\rangle \pm i|1\rangle)/\sqrt{2}$.

$$P(\sigma_y = +1) = |\langle +y|\psi\rangle|^2 = \left|\frac{1}{\sqrt{2}}\cdot\frac{\sqrt{3}}{2} + \frac{-i}{\sqrt{2}}\cdot\frac{i}{2}\right|^2 = \left|\frac{\sqrt{3}/2 + 1/2}{\sqrt{2}}\right|^2 = \frac{(\sqrt{3}+1)^2}{8} = \frac{4+2\sqrt{3}}{8} = \frac{2+\sqrt{3}}{4}.$$

Numerically: $(2 + 1.732)/4 \approx 0.933$. So $\langle\sigma_y\rangle \approx 0.933 - 0.067 = 0.866 = \sqrt{3}/2$.

From the Bloch vector: $\langle\sigma_y\rangle = \sin\theta\sin\phi = \sin(\pi/3)\sin(\pi/2) = \sqrt{3}/2$. Consistent.

**Verifying the Robertson bound.**

$[\sigma_x, \sigma_z] = -2i\sigma_y$, so the Robertson bound reads:

$$\sigma_{\sigma_x}\cdot\sigma_{\sigma_z} \geq \tfrac{1}{2}|\langle{-2i\sigma_y}\rangle| = |\langle\sigma_y\rangle| = \frac{\sqrt{3}}{2}.$$

We computed $\sigma_{\sigma_z} = \sqrt{3}/2$. For $\sigma_{\sigma_x}$: $\langle\sigma_x\rangle = 0$, $\langle\sigma_x^2\rangle = 1$ (since $\sigma_x^2 = \hat{I}$ and the state is normalized), so $\sigma_{\sigma_x} = 1$.

Product: $1 \cdot \sqrt{3}/2 = \sqrt{3}/2$. Bound: $\sqrt{3}/2$. They are equal — the bound is saturated. This is not a coincidence. The state we chose is the $\sigma_y$ eigenstate (as confirmed by $P(\sigma_y = +1) = (2+\sqrt{3})/4 \approx 0.933$). The $\sigma_y$ eigenstate saturates the $\sigma_x$/$\sigma_z$ Robertson bound. The geometric picture: a point on the Bloch sphere that is as far as possible in the $y$-direction is equidistant from all $x$-axis and $z$-axis eigenstates. Its $x$ and $z$ uncertainties are maximal and equal.

---

## The limit of the example

The example did everything right and hit a wall: we "verified" the Robertson bound at the $\sigma_y$ eigenstate, where the bound is saturated. What about a generic state?

Pick $\theta = \pi/4$, $\phi = 0$ — a state near the equator but tilted toward the north pole. Then $\langle\sigma_y\rangle = \sin(\pi/4)\sin(0) = 0$, so the Robertson bound gives $\sigma_{\sigma_x}\sigma_{\sigma_z} \geq 0$. That is trivially true for any non-negative numbers.

Does this mean $\sigma_x$ and $\sigma_z$ can both be zero on this state? No — computing explicitly shows $\sigma_{\sigma_x} = \sin(\pi/4) = 1/\sqrt{2}$ and $\sigma_{\sigma_z} = \sin(\pi/4) = 1/\sqrt{2}$, product $= 1/2$. The bound is satisfied but not saturated. The Robertson bound is state-dependent and is tight only at eigenstates of $[\hat{A}, \hat{B}]/(2i)$.

The takeaway: the Robertson bound is not a fixed number. It is a property of the state. The same observable pair $(\sigma_x, \sigma_z)$ has different bounds on different states. The simulator you build in this chapter's "+1" exercise makes this visible.

---

## Common misconceptions

**"The state collapses to α|0⟩ or β|1⟩ — one of the terms."**

This is wrong, but wrong in a specific way that is worth unpacking. If you measure $\sigma_z$, you get eigenstate $|0\rangle$ or $|1\rangle$ — fine. But if you measure $\sigma_x$, the state collapses to $|+x\rangle = (|0\rangle + |1\rangle)/\sqrt{2}$ or $|-x\rangle = (|0\rangle - |1\rangle)/\sqrt{2}$. Neither of these is "one of the terms" in the $\sigma_z$ basis expansion. Collapse is always to the eigenstate of the *observable you measured*, not to the basis vectors of an arbitrary expansion.

**"The relative phase $e^{i\phi}$ is unobservable."**

Dangerously wrong. The global phase of a state is unobservable — you can multiply $|\psi\rangle$ by $e^{i\gamma}$ without changing any measurement outcome. But the *relative* phase between $|0\rangle$ and $|1\rangle$ is very much observable: it determines $\langle\sigma_x\rangle$ and $\langle\sigma_y\rangle$. Two states with the same $|\alpha|$ and $|\beta|$ but different phases $\phi$ are physically distinct and can be distinguished by measuring $\sigma_x$ or $\sigma_y$. The Bloch sphere makes this geometric: same $\theta$, different $\phi$ — different longitude on the sphere, different physical predictions.

**"The Bloch sphere represents the particle's position in space."**

No. The Bloch sphere is a representation of the *state space* of a two-level system. The Bloch vector $\vec{r}$ lives in an abstract space where each direction corresponds to a different Pauli expectation value. It has nothing to do with the position of the particle. The electron you are tracking could be anywhere in the lab; its spin state is a point on the sphere.

**"θ/2 is a typo; it should be θ."**

No. Test it: $\theta = \pi$ in $\cos(\theta/2)|0\rangle + e^{i\phi}\sin(\theta/2)|1\rangle$ gives $\cos(\pi/2)|0\rangle + e^{i\phi}\sin(\pi/2)|1\rangle = e^{i\phi}|1\rangle$ — the south pole. If you use $\theta$ instead of $\theta/2$: at $\theta = \pi/2$ you get $|1\rangle$ (the south pole) instead of the equatorial state $(|0\rangle + e^{i\phi}|1\rangle)/\sqrt{2}$. The sphere is compressed by half and everything is wrong.

**"Measuring the particle twice gives the same result as measuring a single particle."**

The ensemble protocol is: prepare $N$ identical copies of $|\psi\rangle$; measure one observable on $N/2$ of them; measure a different observable on the other $N/2$. No copy is measured twice. The standard deviations you compute are properties of the ensemble, not of a sequence of measurements on a single particle. The Robertson bound is about the spread across many copies, each measured once.

---

## Exercises

**Warm-up**

1. *[Tests: Born rule application]* A qubit is in state $|\psi\rangle = (1/\sqrt{3})|0\rangle + (\sqrt{2}/\sqrt{3})|1\rangle$. (a) Verify normalization. (b) Find $P(\sigma_z = +1)$ and $P(\sigma_z = -1)$. (c) Find $\langle\sigma_z\rangle$. (d) If the result of the measurement is $-1$, what is the post-measurement state? What is $P(\sigma_z = +1)$ for a second measurement immediately after? *Difficulty: warm-up.*

2. *[Tests: Pauli matrix structure, eigenvalues]* (a) Find the eigenvalues and normalized eigenvectors of $\sigma_y$ by direct computation: write $\sigma_y\vec{v} = \lambda\vec{v}$ and solve. (b) Verify that the eigenvectors are $|+y\rangle = (|0\rangle + i|1\rangle)/\sqrt{2}$ and $|-y\rangle = (|0\rangle - i|1\rangle)/\sqrt{2}$. (c) Verify orthogonality: $\langle+y|-y\rangle = 0$. (d) Why does the $i$ in the eigenvector not make $\sigma_y$ non-Hermitian? *Difficulty: warm-up.*

3. *[Tests: Bloch sphere parametrization]* Identify the Bloch-sphere angles $(\theta, \phi)$ for each of the following states: (a) $|0\rangle$; (b) $|1\rangle$; (c) $(|0\rangle + |1\rangle)/\sqrt{2}$; (d) $(|0\rangle - |1\rangle)/\sqrt{2}$; (e) $(|0\rangle + i|1\rangle)/\sqrt{2}$. For each, compute the Bloch vector $\vec{r}$ and verify $|\vec{r}| = 1$. *Difficulty: warm-up.*

**Application**

4. *[Tests: measurement collapse, sequential measurements]* A qubit is prepared in state $|+x\rangle = (|0\rangle + |1\rangle)/\sqrt{2}$. (a) It is measured along $z$. Find $P(+1)$ and $P(-1)$. (b) The result is $+1$. The qubit is now measured along $x$. Find $P(+1)$ and $P(-1)$ for this second measurement. (c) If instead the result of step (a) had been $-1$, what would the second measurement (along $x$) give? (d) Explain in one sentence why the $x$-measurement result in step (b) is uncertain despite the initial state having definite $\sigma_x = +1$. *Difficulty: application.*

5. *[Tests: expectation value, Robertson bound]* For the state $|\psi\rangle = (|0\rangle + e^{i\pi/4}|1\rangle)/\sqrt{2}$ (equatorial state, $\phi = \pi/4$): (a) Compute $\langle\sigma_x\rangle$, $\langle\sigma_y\rangle$, $\langle\sigma_z\rangle$. (b) Compute the standard deviations $\sigma_{\sigma_x}$, $\sigma_{\sigma_y}$, $\sigma_{\sigma_z}$ using $\sigma_{\sigma_i}^2 = \langle\sigma_i^2\rangle - \langle\sigma_i\rangle^2 = 1 - \langle\sigma_i\rangle^2$. (c) Verify the Robertson bound for the pair $(\sigma_x, \sigma_z)$. Is it saturated? *Difficulty: application.*

6. *[Tests: phase distinguishability]* Two states: $|\psi_1\rangle = (|0\rangle + |1\rangle)/\sqrt{2}$ and $|\psi_2\rangle = (|0\rangle + i|1\rangle)/\sqrt{2}$. (a) For each state, compute $P(\sigma_z = +1)$ and $P(\sigma_z = -1)$. (b) For each state, compute $P(\sigma_x = +1)$ and $P(\sigma_x = -1)$. (c) For each state, compute $P(\sigma_y = +1)$ and $P(\sigma_y = -1)$. (d) Which measurement distinguishes $|\psi_1\rangle$ from $|\psi_2\rangle$? What does this tell you about the observability of the relative phase? *Difficulty: application.*

**Synthesis (Apply+)**

7. *[Tests: synthesis across measurement sequences]* Design a sequence of two Stern-Gerlach measurements on a qubit such that a particle entering in state $|0\rangle$ exits in a state with $P(\sigma_z = +1) = 1/2$. Specify which observable each apparatus measures, and compute the post-measurement state after each step. Is your answer unique? If not, exhibit two different sequences. *Difficulty: application/synthesis.*

8. *[Tests: produce — Bloch sphere calculation from scratch]* A qubit is in the state $|\psi\rangle = \cos(\pi/8)|0\rangle + e^{i\pi/3}\sin(\pi/8)|1\rangle$. Without using the Bloch-sphere formula directly, compute $\langle\sigma_x\rangle$, $\langle\sigma_y\rangle$, $\langle\sigma_z\rangle$ by evaluating the matrix products $\langle\psi|\sigma_i|\psi\rangle$ explicitly. Then extract $\theta$ and $\phi$ from the Bloch vector and compare to the angles in the state definition. *Difficulty: synthesis/produce.*

9. *[Tests: limits of the qubit model]* A professor says: "For a spin-½ particle, there are only two possible outcomes when I measure the spin along any axis. So the spin of a particle is just a coin flip." Write a two-paragraph response. In the first paragraph, explain what is physically correct. In the second paragraph, identify what is wrong or incomplete about the coin-flip analogy — specifically, what feature of the qubit the coin-flip model cannot capture. *Difficulty: synthesis.*

---

## Still puzzling

The measurement postulate is the most contested piece of quantum mechanics — not its predictions, which are confirmed to extraordinary precision, but its interpretation. What does it mean for the state to "collapse"? Several research programs are actively trying to answer this.

**Decoherence.** The collapse rule is effective but may not be fundamental. Decoherence theory (Zurek 2003) explains why macroscopic superpositions are unobservable: they become entangled with environmental degrees of freedom and lose their interference fringes on timescales far shorter than any observation can resolve. Decoherence explains why you never see a "cat in superposition" without invoking an axiom of collapse — the superposition becomes a classical mixture from the perspective of any local observer. But decoherence alone does not explain why one outcome, not the other, occurs in any given run. [contested]

**The Born rule.** In this book, $P(a_n) = |\langle a_n|\psi\rangle|^2$ is a postulate. Gleason's theorem (1957) shows it is the *unique* probability measure on Hilbert space consistent with non-contextuality — so in some sense it is forced. Zurek's "envariance" argument (2003, 2005) attempts to derive the Born rule from symmetry properties of entangled systems and environment. Many-worlds advocates (Deutsch 1999, Wallace 2010) try to derive it from decision-theoretic rationality. None of these derivations is universally accepted as complete or as definitively settling the question. [contested]

**Quantum non-demolition measurement.** A measurement is QND if it does not disturb the observable being measured — only its conjugate. A $\hat{S}_z$ Stern-Gerlach measurement is QND for $\hat{S}_z$ (the result is repeatable) but not for $\hat{S}_x$ (which the intermediate measurement destroys). QND measurement is central to precision sensing and quantum error correction in current experiments.

**Weak measurement.** If you measure an observable with a very weak coupling, you get a "weak value" — the result of a post-selected measurement that can be outside the range of the eigenvalues. Introduced by Aharonov, Albert, and Vaidman (1988), weak values have been observed experimentally and are connected to paradoxes like Leggett-Garg inequalities. The formalism extends the standard postulate rather than replacing it.

**The continuous-variable analogue.** The position operator has a continuous spectrum. The "eigenstate" of position is $\langle x|x_0\rangle = \delta(x - x_0)$, which is not normalizable. A position measurement that returns outcome $x_0$ collapses the state to a delta function — a mathematical idealization. In practice, position measurements have finite resolution. The post-measurement state is a narrow (but normalizable) wave packet, not literally a delta function. The postulate as stated for discrete systems is an approximation in the continuous case.

---

## The +1 — Simulation Exercise

The deliverable: `11-qubit-measurement.html` — an interactive Bloch sphere with measurement statistics.

### Part A — CLAUDE.md amendment

Add this stanza to your existing `CLAUDE.md` before running the simulation prompt:

````markdown
## Chapter 11 — Qubit Measurement and Bloch Sphere

- Pauli matrices EXACTLY as follows (verify at startup):
    sigma_x = [[0,1],[1,0]]
    sigma_y = [[0,-i],[i,0]]   ← UPPER-RIGHT is -i
    sigma_z = [[1,0],[0,-1]]
  For each M: compute M.dagger() (conjugate transpose) and verify M.dagger() === M.
  Compute M @ M and verify === I (identity). sigma_y sign error is failure mode #1.

- State parametrization: |psi> = cos(theta/2)|0> + exp(i*phi)*sin(theta/2)|1>.
  Factor of theta/2 (NOT theta) is mandatory.
  Test: theta=0 => |0>; theta=pi => |1>; theta=pi/2,phi=0 => (|0>+|1>)/sqrt(2).

- Born rule: P(outcome = a_n) = |<a_n|psi>|^2. NEVER P = |psi|^2 directly.
  Eigenstates for each Pauli:
    sigma_z: |+> = [1,0], |-> = [0,1]
    sigma_x: |+> = [1,1]/sqrt(2), |-> = [1,-1]/sqrt(2)
    sigma_y: |+> = [1,i]/sqrt(2), |-> = [1,-i]/sqrt(2)

- Bloch vector: r = (sin(theta)*cos(phi), sin(theta)*sin(phi), cos(theta)).
  Runtime check: |r|^2 within 1e-6 of 1. Display as three bar charts [-1, +1].

- Measurement simulation: N outcomes per operator sampled via inverse CDF
  (u uniform [0,1); +1 if u < P(+1), else -1). Compute sample std devs.
  Compare product to Robertson bound |<[A,B]>|/2 computed analytically.
  Label: "N independent measurements on N independent copies. No copy measured twice."

- Collapse: after user clicks "Measure", collapse the displayed state to the
  eigenstate corresponding to the sampled outcome. Show the collapsed state on
  the Bloch sphere. Add a "Reset to original state" button.
````

### Part B — The simulation prompt

````
SHOW.
The qubit measurement postulate:
  For observable A with eigenstates {|a_n>} and eigenvalues {a_n}:
  (1) Outcomes are eigenvalues only.
  (2) P(a_n) = |<a_n|psi>|^2.
  (3) Post-measurement state is |a_n>.
  Expectation value: <A> = sum_n a_n P(a_n) = <psi|A|psi>.
  Standard deviation: sigma_A^2 = <A^2> - <A>^2 = 1 - <A>^2  (for Paulis, since A^2 = I).

The qubit state parametrized as:
  |psi> = cos(theta/2)|0> + exp(i*phi)*sin(theta/2)|1>
  Bloch vector: r = (sin(theta)cos(phi), sin(theta)sin(phi), cos(theta))
  |r|^2 = 1 for all pure states.

Robertson bound: sigma_A * sigma_B >= (1/2)|<[A,B]>|.
  For sigma_x and sigma_z: [sigma_x, sigma_z] = -2i*sigma_y, so bound = |<sigma_y>|.

SAY.
Produce a single file `11-qubit-measurement.html`.

Layout (SVG 1200 x 700):

Left panel (500 x 700): Bloch sphere.
  - Translucent sphere silhouette (unit sphere, dashed outline at latitude and longitude circles).
  - Axes x, y, z labeled, ticks at +/-1.
  - State vector arrow from origin to Bloch vector; solid in front, dashed behind the sphere center plane.
  - Colored dots at key states: |0> (north), |1> (south), |+x>, |-x>, |+y>, |-y>.
  - Current state labeled with (theta, phi) values.
  - After measurement: collapsed state shown as a new arrow in red.

Center panel (300 x 700): Controls and numerical readouts.
  - theta slider (0 to pi), phi slider (0 to 2*pi). Current values shown.
  - Three bar charts: <sigma_x>, <sigma_y>, <sigma_z>, each in [-1, 1].
  - Normalization indicator: |alpha|^2 + |beta|^2 (must read 1.000).
  - "Measure sigma_z / sigma_x / sigma_y" buttons. On click: sample one outcome,
    display it prominently, collapse the Bloch vector to the eigenstate.
  - "Reset" button: return to pre-measurement state.

Right panel (400 x 700): Measurement statistics.
  - Two observable dropdowns (sigma_x / sigma_y / sigma_z).
  - N slider (100 to 5000).
  - "Run ensemble" button. On click: sample N outcomes for observable A on half
    and N outcomes for observable B on the other half, draw histograms.
  - Below histograms: sigma_A, sigma_B, sigma_A*sigma_B, Robertson bound |<[A,B]>|/2.
  - Ratio = product / bound (label: must be >= 1).
  - Label: "These are N independent measurements on N independent copies
    of the same state. No copy is measured twice."

CONSTRAIN.
- D3 v7 from CDN. SVG only. Vanilla JS. No 3D library.
- 3D Bloch sphere via orthographic projection (hand-rolled). View angle: 30 deg elevation, 20 deg azimuth.
- Runtime sanity checks at startup: sigma_y hermiticity, |r|^2 = 1, P(+)+P(-) = 1.
- Bloch sphere rotatable by mouse drag (optional; document as a bonus).

VERIFY.
After writing, confirm:
(a) State |0> (theta=0): sigma_z bar shows +1, others show 0. Single-shot measurement of sigma_z gives +1 with probability 1.
(b) State |+y> (theta=pi/2, phi=pi/2): sigma_y bar shows +1, sigma_x and sigma_z bars show 0. Ensemble with sigma_x and sigma_z at N=1000: both histograms approximately 50/50, product approximately 1, Robertson bound = |<sigma_y>| = 1.
(c) State |0> ensemble measurement of sigma_x and sigma_z: product = 0, Robertson bound = 0. Ratio undefined or labeled as ">= 1 trivially."
(d) Clicking "Measure sigma_x" on state |0> collapses to |+x> or |-x> randomly; subsequent sigma_x measure on the collapsed state gives same result with probability 1.
````

### Part C — Exploration tasks

**The Born rule is geometry.** Set the state to $|0\rangle$ (north pole). Slowly drag $\theta$ toward $\pi/2$ while watching the $\sigma_z$ bar chart. Note $\langle\sigma_z\rangle = \cos\theta$ decreasing from $+1$ toward $0$ and $P(\sigma_z = -1) = \sin^2(\theta/2)$ rising from 0 toward $1/2$. Now drag to the south pole: $P(\sigma_z = -1) = 1$. You have just watched the Born rule as a geometric projection.

**The phase is real.** Set $\theta = \pi/2$ (equatorial state). Drag $\phi$ from $0$ to $2\pi$. The $\langle\sigma_z\rangle$ bar stays at 0 throughout — the equatorial state always gives 50/50 on $\sigma_z$. But watch $\langle\sigma_x\rangle = \cos\phi$ and $\langle\sigma_y\rangle = \sin\phi$ rotate through their full ranges. The relative phase $\phi$ is invisible to $\sigma_z$ but fully visible to $\sigma_x$ and $\sigma_y$. This is the operational meaning of "the phase is observable."

**The Robertson bound is state-dependent.** Run the ensemble measurement for $(\sigma_x, \sigma_z)$ with $N = 2000$. First, at $\theta = 0$ (the north pole): product $\approx 0$, bound $= 0$. At $\theta = \pi/2, \phi = \pi/2$ (the $\sigma_y$ eigenstate): product $\approx 1$, bound $\approx 1$. At $\theta = \pi/4, \phi = 0$: product is somewhere in between. The bound is a property of the state — different states, different bounds.

**Sequential measurement and memory loss.** Click "Measure $\sigma_z$" on the initial state $|+x\rangle = (|0\rangle + |1\rangle)/\sqrt{2}$. Record the outcome. Now click "Measure $\sigma_x$" on the collapsed state. The result is random — the Z measurement erased the X information. Click "Reset" and re-run five times. Observe that the post-Z state always gives 50/50 on X, regardless of whether the Z result was $+1$ or $-1$.

---

## References

- Dirac, P.A.M. (1930). *The Principles of Quantum Mechanics*. Oxford University Press. [The measurement postulate in its original form; still worth reading for precision.]
- Sakurai, J.J. and Napolitano, J. (2021). *Modern Quantum Mechanics*, 3rd ed. Cambridge University Press. Ch. 1–2. [The spin-½ / Stern-Gerlach approach that directly motivates this chapter's presentation.]
- Townsend, J.S. (2012). *A Modern Approach to Quantum Mechanics*, 2nd ed. University Science Books. Ch. 1–3. [verify] [Pedagogically the closest to this chapter's philosophy; the sequential Stern-Gerlach sequence is from here.]
- Gerlach, W. and Stern, O. (1922). "Das magnetische Moment des Silberatoms." *Zeitschrift für Physik*, 9, 353–355. [verify] [The original Stern-Gerlach paper. The two-spot result is a direct measurement of the Born rule for spin-½.]
- Zurek, W.H. (2003). "Decoherence, einselection, and the quantum origins of the classical." *Reviews of Modern Physics*, 75, 715–775. [Decoherence as partial answer to the collapse question; cited in "Still Puzzling."]
- Aharonov, Y., Albert, D.Z., and Vaidman, L. (1988). "How the result of a measurement of a component of the spin of a spin-½ particle can turn out to be 100." *Physical Review Letters*, 60, 1351. [verify] [The original weak-measurement paper; cited in "Still Puzzling."]
- Werner, S.A., Colella, R., Overhauser, A.W., and Eagen, C.F. (1975). "Observation of the phase shift of a neutron due to precession in a magnetic field." *Physical Review Letters*, 35, 1053. [verify] [Neutron interferometry measurement of the spinor phase; directly confirms the $4\pi$ periodicity.]
- Gleason, A.M. (1957). "Measures on the closed subspaces of a Hilbert space." *Journal of Mathematics and Mechanics*, 6, 885–893. [verify] [The theorem that uniquely forces the Born rule; cited in "Still Puzzling."]
