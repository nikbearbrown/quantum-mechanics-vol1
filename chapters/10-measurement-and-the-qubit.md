# Chapter 10 — Measurement, Superposition, and the Qubit

In this chapter we examine what happens when we make a measurement in quantum mechanics. The question is a practical one: when we run an experiment and get a result, what rules governed that outcome? We will state those rules precisely, apply them to two-level systems called qubits, and examine what the formalism says — and does not say — about what happens to the system during a measurement.

---

## The Measurement Postulate

Let $\hat{A}$ be a Hermitian observable with discrete eigenvalues $\{a_n\}$ and orthonormal eigenstates $\{|a_n\rangle\}$. When we measure $\hat{A}$ on a system in state $|\psi\rangle$, three things happen:

**1.** The only possible outcomes are the eigenvalues $a_n$. Nothing in between them, no superposition of them — exactly one.

**2.** The probability of getting $a_n$ is

$$\boxed{P(a_n) = |\langle a_n|\psi\rangle|^2.}$$

This is the Born rule. The inner product $\langle a_n|\psi\rangle$ is a complex amplitude, and its modulus squared is the probability. Geometrically, $P(a_n)$ is the squared projection of $|\psi\rangle$ onto $|a_n\rangle$.

**3.** Immediately after the measurement returns $a_n$, the state is $|a_n\rangle$.

This is collapse. It is not a metaphor but a state-update rule.

The probabilities sum to 1 by the completeness of the eigenstates:

$$\sum_n P(a_n) = \sum_n |\langle a_n|\psi\rangle|^2 = \langle\psi|\!\left(\sum_n |a_n\rangle\langle a_n|\right)\!|\psi\rangle = \langle\psi|\hat{I}|\psi\rangle = 1.$$

Nothing leaks. The interpretation of collapse is contested. The practical content, however, is settled: after obtaining outcome $a_n$, we predict all subsequent measurements using $|a_n\rangle$.

---

## The Two-State System

The simplest system in which all of this is computable by hand is the qubit, a two-dimensional complex Hilbert space $\mathbb{C}^2$. We choose a basis $\{|0\rangle, |1\rangle\}$. The most general normalized state is

$$|\psi\rangle = \alpha|0\rangle + \beta|1\rangle, \qquad \alpha, \beta \in \mathbb{C}, \qquad |\alpha|^2 + |\beta|^2 = 1.$$

Two real parameters specify the state, up to a global phase. An electron's spin, a photon's polarization, the two lowest energy levels of a superconducting circuit — all are physical qubits, and the mathematics is identical for all of them.

The standard observables on a qubit are the Pauli operators:

$$\sigma_x = \begin{pmatrix}0 & 1\\1 & 0\end{pmatrix}, \qquad \sigma_y = \begin{pmatrix}0 & -i\\i & 0\end{pmatrix}, \qquad \sigma_z = \begin{pmatrix}1 & 0\\0 & -1\end{pmatrix}.$$

Each is Hermitian, each squares to the identity, and each has eigenvalues $\pm 1$. Their commutators are $[\sigma_i, \sigma_j] = 2i\epsilon_{ijk}\sigma_k$, so for example $[\sigma_x, \sigma_z] = -2i\sigma_y \neq 0$. They do not commute, which means measuring one after another in different orders gives different results.

A word of caution about $\sigma_y$: the upper-right entry is $-i$, not $+i$. This is the single most common sign error in qubit calculations. The matrix is Hermitian even though it looks antisymmetric as a real matrix, because Hermitian means equal to the *conjugate* transpose. The transpose of $\sigma_y$ is $-\sigma_y$, but the conjugate transpose is $+\sigma_y$, and the $i$ is what makes that work. Any code doing qubit calculations should check $\sigma_y^\dagger = \sigma_y$ at startup.

---

## The Stern-Gerlach Experiment

In 1922, Otto Stern and Walther Gerlach passed silver atoms through an inhomogeneous magnetic field. Classical physics predicted a smear — a continuous spread of deflections matching the continuous range of magnetic-moment orientations. What they saw instead was two discrete spots.

The field gradient exerts a force proportional to $\mu_z$, the component of the magnetic moment along the field axis. If angular momentum were classical, $\mu_z$ would be continuous and the deposit on the plate would be a streak. Instead there were two spots, at $\mu_z = \pm\mu_B$. The Born rule is not abstract here. It is written in silver.

The observable is $\hat{S}_z = (\hbar/2)\sigma_z$, with eigenvalues $\pm\hbar/2$. An atom in state $|\psi\rangle = \alpha|\!\uparrow\rangle + \beta|\!\downarrow\rangle$ hits the upper spot with probability $|\alpha|^2$ and the lower with $|\beta|^2$. If we let only the upper beam through, the remaining atoms are in state $|\!\uparrow\rangle$ — collapsed, certain, ready to be used again.

The interesting physics shows up in sequences. Consider three arrangements:

**Z then Z.** Select the $|\!\uparrow\rangle$ beam from a first Z apparatus and feed it into a second. Every atom hits the upper spot, with probability 1. Once we know the outcome of a $\hat{S}_z$ measurement, measuring $\hat{S}_z$ again gives the same result — collapse is stable.

**Z then X.** The $\hat{S}_x$ eigenstates are $|\pm x\rangle = (|\!\uparrow\rangle \pm |\!\downarrow\rangle)/\sqrt{2}$. An atom in $|\!\uparrow\rangle$ is an equal superposition of both $\hat{S}_x$ eigenstates, so a subsequent X measurement comes out 50/50. The atom that was certainly spin-up in Z is completely uncertain in X.

**Z then X then Z.** After the X measurement, the state collapses to $|+x\rangle$ or $|-x\rangle$. Either way, that state is a 50/50 superposition in Z, since $|+x\rangle = (|\!\uparrow\rangle + |\!\downarrow\rangle)/\sqrt{2}$. The final Z measurement is again random. The intermediate X measurement erased the Z information. Measure Z, then X, then Z, and the Z certainty is gone.

This is not instrumental imprecision. It is $[\sigma_x, \sigma_z] \neq 0$ made physically tangible. We cannot hold definite values for both observables at once.

---

## The Bloch Sphere

Every normalized qubit state, up to a global phase, can be written as

$$|\psi\rangle = \cos\!\left(\frac{\theta}{2}\right)|0\rangle + e^{i\phi}\sin\!\left(\frac{\theta}{2}\right)|1\rangle, \qquad \theta \in [0, \pi], \quad \phi \in [0, 2\pi).$$

The factor $\theta/2$ — not $\theta$ — is required. We can check it: at $\theta = 0$ we get $|0\rangle$; at $\theta = \pi$ we get $e^{i\phi}|1\rangle$, which is $|1\rangle$ up to a global phase; and at $\theta = \pi/2$ we get the equatorial state $(|0\rangle + e^{i\phi}|1\rangle)/\sqrt{2}$. Use $\theta$ instead of $\theta/2$ and the south pole appears at $\theta = \pi/2$ rather than $\theta = \pi$, throwing everything off.

Each state corresponds to a point on the unit sphere through its Bloch vector:

$$\vec{r} = \bigl(\langle\sigma_x\rangle,\, \langle\sigma_y\rangle,\, \langle\sigma_z\rangle\bigr) = (\sin\theta\cos\phi,\, \sin\theta\sin\phi,\, \cos\theta).$$

North pole ($\theta = 0$): state $|0\rangle$, $\langle\sigma_z\rangle = +1$. South pole ($\theta = \pi$): state $|1\rangle$, $\langle\sigma_z\rangle = -1$. Equator ($\theta = \pi/2$): equal superpositions, $\langle\sigma_z\rangle = 0$. The azimuthal angle $\phi$ is the relative phase between $|0\rangle$ and $|1\rangle$, and it is physically real: different values of $\phi$ at the same $\theta$ give different $\langle\sigma_x\rangle$ and $\langle\sigma_y\rangle$, detectable by the right measurement. The global phase is unobservable; the relative phase is not.

For pure states, $|\vec{r}|^2 = 1$ exactly. This makes a useful runtime check: compute the three expectation values and confirm the Bloch vector has unit length.

The factor $\theta/2$ in the state produces $\theta$ on the sphere through double-angle identities. It also means that a full $2\pi$ rotation of the state vector corresponds to only a $\pi$ rotation of the Bloch vector — the state picks up a factor of $-1$, invisible in expectation values but visible in interference. Neutron interferometry has measured it.

---

## Worked Example — Predicting Measurement Statistics

Let

$$|\psi\rangle = \frac{\sqrt{3}}{2}|0\rangle + \frac{i}{2}|1\rangle.$$

Check normalization: $3/4 + 1/4 = 1$. In the Bloch parametrization: $\cos(\theta/2) = \sqrt{3}/2$ gives $\theta = \pi/3$; the coefficient of $|1\rangle$ is $i/2 = e^{i\pi/2}/2$, so $\phi = \pi/2$.

**Measuring $\sigma_z$.**

$$P(\sigma_z = +1) = |\langle 0|\psi\rangle|^2 = 3/4, \qquad P(\sigma_z = -1) = |\langle 1|\psi\rangle|^2 = 1/4.$$

Expectation value: $\langle\sigma_z\rangle = (+1)(3/4) + (-1)(1/4) = 1/2$. From the Bloch vector: $\langle\sigma_z\rangle = \cos\theta = \cos(\pi/3) = 1/2$. Consistent. Variance: $\sigma_{\sigma_z}^2 = 1 - (1/2)^2 = 3/4$.

Post-measurement states: if $+1$, collapse to $|0\rangle$; subsequent $\sigma_z$ gives $+1$ with probability 1. If $-1$, collapse to $|1\rangle$; subsequent $\sigma_z$ gives $-1$ with probability 1.

**Measuring $\sigma_x$.**

The $\sigma_x$ eigenstates are $|\pm x\rangle = (|0\rangle \pm |1\rangle)/\sqrt{2}$.

$$P(\sigma_x = +1) = |\langle +x|\psi\rangle|^2 = \left|\frac{1}{\sqrt{2}}\cdot\frac{\sqrt{3}}{2} + \frac{1}{\sqrt{2}}\cdot\frac{i}{2}\right|^2 = \frac{3+1}{8} = \frac{1}{2}.$$

So $\langle\sigma_x\rangle = 0$. From the Bloch vector: $\sin\theta\cos\phi = \sin(\pi/3)\cos(\pi/2) = 0$. Consistent.

**Measuring $\sigma_y$.**

The $\sigma_y$ eigenstates are $|{\pm}y\rangle = (|0\rangle \pm i|1\rangle)/\sqrt{2}$.

$$P(\sigma_y = +1) = \left|\frac{1}{\sqrt{2}}\cdot\frac{\sqrt{3}}{2} + \frac{-i}{\sqrt{2}}\cdot\frac{i}{2}\right|^2 = \left|\frac{\sqrt{3}/2 + 1/2}{\sqrt{2}}\right|^2 = \frac{(\sqrt{3}+1)^2}{8} = \frac{2+\sqrt{3}}{4} \approx 0.933.$$

So $\langle\sigma_y\rangle \approx 0.933 - 0.067 = \sqrt{3}/2$. Bloch vector: $\sin(\pi/3)\sin(\pi/2) = \sqrt{3}/2$. Consistent.

**The Robertson bound.**

$[\sigma_x, \sigma_z] = -2i\sigma_y$, so the bound on $\sigma_{\sigma_x}\sigma_{\sigma_z}$ is $|\langle\sigma_y\rangle| = \sqrt{3}/2$. We computed $\sigma_{\sigma_z} = \sqrt{3}/2$. For $\sigma_{\sigma_x}$: $\langle\sigma_x\rangle = 0$ and $\sigma_x^2 = \hat{I}$, so $\sigma_{\sigma_x} = 1$.

Product: $1 \cdot \sqrt{3}/2 = \sqrt{3}/2$. Bound: $\sqrt{3}/2$. They are equal — the Robertson bound is saturated. This state is the $\sigma_y$ eigenstate (confirmed by $P(\sigma_y = +1) \approx 0.933$). The $\sigma_y$ eigenstate maximizes the product $\sigma_{\sigma_x}\sigma_{\sigma_z}$ for the $(\sigma_x, \sigma_z)$ pair, because a point on the Bloch sphere lying entirely along the $y$-axis is equidistant from all $x$-axis and $z$-axis eigenstates.

**What changes for a generic state.** Pick $\theta = \pi/4$, $\phi = 0$. Then $\langle\sigma_y\rangle = 0$, and the Robertson bound gives $\sigma_{\sigma_x}\sigma_{\sigma_z} \geq 0$ — trivially satisfied by any non-negative numbers. Computing explicitly: $\sigma_{\sigma_x} = \sigma_{\sigma_z} = 1/\sqrt{2}$, product $= 1/2$, bound $= 0$. The bound holds but is not tight. The Robertson bound is a property of the state, not a fixed number. The simulation exercise makes this visible.

---

## Chapter 10 — Qubit Measurement and Bloch Sphere

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
(a) State |0> (theta=0): sigma_z bar shows +1, others show 0. Single-shot measurement
    of sigma_z gives +1 with probability 1.
(b) State |+y> (theta=pi/2, phi=pi/2): sigma_y bar shows +1, sigma_x and sigma_z bars
    show 0. Ensemble with sigma_x and sigma_z at N=1000: both histograms approximately
    50/50, product approximately 1, Robertson bound = |<sigma_y>| = 1.
(c) State |0> ensemble measurement of sigma_x and sigma_z: product = 0, Robertson
    bound = 0. Ratio undefined or labeled as ">= 1 trivially."
(d) Clicking "Measure sigma_x" on state |0> collapses to |+x> or |-x> randomly;
    subsequent sigma_x measure on the collapsed state gives same result with probability 1.
````

### Part C — Exploration tasks

**The Born rule is geometry.** Set the state to $|0\rangle$ (north pole). Slowly drag $\theta$ toward $\pi/2$ while watching the $\sigma_z$ bar chart. Note $\langle\sigma_z\rangle = \cos\theta$ decreasing from $+1$ toward $0$ and $P(\sigma_z = -1) = \sin^2(\theta/2)$ rising from 0 toward $1/2$. Drag to the south pole: $P(\sigma_z = -1) = 1$. You are watching the Born rule as a geometric projection.

**The phase is real.** Set $\theta = \pi/2$. Drag $\phi$ from $0$ to $2\pi$. The $\langle\sigma_z\rangle$ bar stays at 0 throughout — an equatorial state always gives 50/50 on $\sigma_z$. But watch $\langle\sigma_x\rangle = \cos\phi$ and $\langle\sigma_y\rangle = \sin\phi$ rotate through their full ranges. The relative phase $\phi$ is invisible to $\sigma_z$ but fully visible to $\sigma_x$ and $\sigma_y$. This is the operational meaning of "the phase is observable."

**The Robertson bound is state-dependent.** Run the ensemble measurement for $(\sigma_x, \sigma_z)$ with $N = 2000$. At $\theta = 0$: product $\approx 0$, bound $= 0$. At $\theta = \pi/2, \phi = \pi/2$: product $\approx 1$, bound $\approx 1$. At $\theta = \pi/4, \phi = 0$: somewhere in between. The bound moves with the state.

**Sequential measurement and memory loss.** Click "Measure $\sigma_z$" on the initial state $|+x\rangle$. Record the outcome. Click "Measure $\sigma_x$" on the collapsed state. The result is random — the Z measurement erased the X information. Reset and repeat five times. The post-Z state always gives 50/50 on X, regardless of whether Z returned $+1$ or $-1$.

---

## References

- Dirac, P.A.M. (1930). *The Principles of Quantum Mechanics*. Oxford University Press.
- Sakurai, J.J. and Napolitano, J. (2021). *Modern Quantum Mechanics*, 3rd ed. Cambridge University Press. Ch. 1–2.
- Townsend, J.S. (2012). *A Modern Approach to Quantum Mechanics*, 2nd ed. University Science Books. Ch. 1–3.
- Gerlach, W. and Stern, O. (1922). "Das magnetische Moment des Silberatoms." *Zeitschrift für Physik*, 9, 353–355.
- Zurek, W.H. (2003). "Decoherence, einselection, and the quantum origins of the classical." *Reviews of Modern Physics*, 75, 715–775.
- Aharonov, Y., Albert, D.Z., and Vaidman, L. (1988). "How the result of a measurement of a component of the spin of a spin-½ particle can turn out to be 100." *Physical Review Letters*, 60, 1351.
- Werner, S.A., Colella, R., Overhauser, A.W., and Eagen, C.F. (1975). "Observation of the phase shift of a neutron due to precession in a magnetic field." *Physical Review Letters*, 35, 1053.
- Gleason, A.M. (1957). "Measures on the closed subspaces of a Hilbert space." *Journal of Mathematics and Mechanics*, 6, 885–893.

---

*The story continues in Volume 4: entanglement. Two qubits whose joint state cannot be written as a product of individual qubit states — the Bell states — violate the CHSH inequality, ruling out local hidden variables. The measurement postulate for composite systems, partial traces, and density matrices.*

