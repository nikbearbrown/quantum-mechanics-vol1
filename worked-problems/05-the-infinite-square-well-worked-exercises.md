# Worked Exercises: The Infinite Square Well

*Chapter 5 of Quantum Mechanics — Volume 1*

> These exercises follow a research-backed sequence: full worked example → matched practice → completion problem → error-recognition → transfer → interleaved review. Each section builds on the previous. Do not skip ahead.

## Prerequisites

- You can write the general solution of the TISE inside the well, $\psi(x) = A\sin(kx) + B\cos(kx)$ with $k = \sqrt{2mE}/\hbar$, and know that $V = \infty$ forces $\psi(0) = \psi(L) = 0$.
- You know the quantized spectrum $E_n = n^2\pi^2\hbar^2/2mL^2$ and the normalized eigenstates $\psi_n(x) = \sqrt{2/L}\,\sin(n\pi x/L)$, with $\psi_n$ carrying exactly $n-1$ interior nodes.
- You can attach time-evolution phases $e^{-iE_n t/\hbar}$ to eigenstates and compute $|\Psi|^2$ for a superposition, recognizing that energy eigenstates are stationary and only superpositions slosh.

---

## Part A — Full Worked Example

**What this demonstrates:** How the boundary conditions of confinement, applied step by step to the TISE, collapse a continuous family of solutions into a discrete energy ladder — and how to put a real number on the ground-state energy.

**The problem:** An electron is confined to a one-dimensional infinite square well of width $L = 0.5$ nm (half the chapter's headline 1 nm well). Derive the allowed energies from the TISE and boundary conditions, then compute $E_1$ in eV and the photon wavelength emitted in the $n=2 \to n=1$ transition.

**The solution:**

**Step 1 — Write the interior solution and exclude $E \leq 0$.** Inside the well $V = 0$, so the TISE is $-(\hbar^2/2m)\psi'' = E\psi$. For $E < 0$ the equation reads $\psi'' = \kappa^2\psi$ with real exponential solutions that cannot vanish at both walls without being identically zero; $E = 0$ gives $\psi = ax+b$, also forced to zero. So only $E > 0$ survives, giving $\psi(x) = A\sin(kx) + B\cos(kx)$, $k = \sqrt{2mE}/\hbar$.
*Why:* The wave function must be continuous and vanish where $V = \infty$; real exponentials and straight lines have no way to be zero at two distinct points except trivially.
*Check:* $k$ has units $\sqrt{\text{kg}\cdot\text{J}}/(\text{J}\cdot\text{s}) = \text{m}^{-1}$. Good — a wave vector.

**Step 2 — Impose the boundary condition at $x = 0$.** $\psi(0) = A\sin 0 + B\cos 0 = B = 0$. The cosine is killed; $\psi(x) = A\sin(kx)$.
*Why:* The left wall is the first half of the confinement condition $\psi(0) = 0$.
*Check:* $\sin(kx)$ already vanishes at $x = 0$ for any $k$ — consistent, no quantization yet.

**Step 3 — Impose the boundary condition at $x = L$ and read off quantization.** $\psi(L) = A\sin(kL) = 0$. Discarding $A = 0$ (no particle), we need $\sin(kL) = 0$, i.e. $kL = n\pi$, so $k_n = n\pi/L$, $n = 1, 2, 3, \ldots$
*Why:* A sine vanishes only at integer multiples of $\pi$ — this single equation is where the continuous spectrum of $k$ collapses to a discrete ladder. Quantization enters here, from geometry, not a postulate.
*Check:* $n = 0$ gives $\psi \equiv 0$ (no particle), correctly excluded; negative $n$ duplicates the physical state.

**Step 4 — Convert to energy and plug in numbers.** Since $E = \hbar^2 k^2/2m$,
$$E_n = \frac{n^2\pi^2\hbar^2}{2mL^2}.$$
For $n=1$, $m = m_e = 9.109\times10^{-31}$ kg, $L = 0.5\times10^{-9}$ m:
$$E_1 = \frac{\pi^2(1.055\times10^{-34})^2}{2(9.109\times10^{-31})(0.5\times10^{-9})^2} \approx 2.41\times10^{-19}\ \text{J} \approx 1.51\ \text{eV}.$$
*Why:* The $n^2$ scaling and the $L^{-2}$ scaling are the fingerprints of confinement; halving $L$ from the chapter's 1 nm well quadruples $E_1$ (the chapter's 1 nm value was $0.377$ eV; $4 \times 0.377 = 1.51$ eV). ✓
*Check:* The ratios come out $E_1:E_2:E_3 = 1:4:9$, the required $n^2$ pattern.

**Step 5 — Compute the emission wavelength.** The $n=2\to n=1$ photon carries $E_2 - E_1 = (4-1)E_1 = 3E_1 = 4.53$ eV. Then
$$\lambda = \frac{hc}{E_2 - E_1} = \frac{1240\ \text{eV·nm}}{4.53\ \text{eV}} \approx 274\ \text{nm}.$$
*Why:* Energy conservation: the photon takes exactly the level gap. The $3E_1$ spacing comes from $2^2 - 1^2 = 3$.
*Check:* 274 nm is ultraviolet — physically sensible for an electron tightly confined to half a nanometre, where gaps run to several eV.

**Final answer:** $E_1 \approx 1.51$ eV; the $n=2\to n=1$ transition emits a photon of wavelength $\approx 274$ nm (UV).

**What made this work:** The central concept is that *quantization is forced by the boundary conditions, not assumed*. The naive approach — treating $E$ as a free continuous parameter the way you would for a classical particle in a box — never produces discrete levels, because nothing in classical mechanics requires the "wave" to vanish at the walls. Only when you demand that a sine vanish at both $x=0$ and $x=L$ simultaneously does the integer $n$ appear. Skipping the second boundary condition (or applying only the energy formula by rote) hides exactly the step where physics happens.

**Self-explanation prompt:** In your own words, explain why applying the boundary condition at $x = L$ — and not the one at $x = 0$ — is the step that produces discreteness. What would change if the well had only one wall?

---

## Part B — Matched Practice Problem

**The problem:** A proton ($m_p = 1.673\times10^{-27}$ kg) is confined to a one-dimensional infinite square well of width $L = 1$ nm. Derive the allowed energies from the TISE and boundary conditions, then compute $E_1$ in eV and the photon wavelength emitted in the $n=3 \to n=1$ transition.

Work it with the same five subgoals:

**Step 1 — Write the interior solution and exclude $E \leq 0$.**

**Step 2 — Impose the boundary condition at $x = 0$.**

**Step 3 — Impose the boundary condition at $x = L$ and read off quantization.**

**Step 4 — Convert to energy and plug in numbers.**

**Step 5 — Compute the emission wavelength.**

**Stuck?** The proton is about 1836 times heavier than the electron, so for the same width the energies are about 1836 times smaller than the electron case — expect $E_1$ in the sub-meV range, and a far longer (infrared or beyond) emission wavelength. Use $E_3 - E_1 = (9-1)E_1 = 8E_1$.

*Instructor note: No solution is provided for Part B. Compare your structure against Part A and verify your numbers with the $n^2$ ratios and a dimensional check on $E_1$.*

---

## Part C — Completion Problem

**The problem:** An electron sits in the equal-weight superposition $\Psi(x,0) = \frac{1}{\sqrt 2}(\psi_2 + \psi_3)$ of the second and third eigenstates of a well of width $L$. Find the period of the probability-density oscillation and the constant energy expectation $\langle\hat H\rangle$.

**Step 1 — Write the time-dependent state.** Each eigenstate carries its own phase:
$$\Psi(x,t) = \frac{1}{\sqrt 2}\,\psi_2(x)\,e^{-iE_2 t/\hbar} + \frac{1}{\sqrt 2}\,\psi_3(x)\,e^{-iE_3 t/\hbar}.$$
*Why:* Time evolution attaches $e^{-iE_n t/\hbar}$ to each stationary state; the relative phase between the two terms is what will produce dynamics.

**Step 2 — Form the probability density.** Expanding $|\Psi|^2$,
$$|\Psi(x,t)|^2 = \frac{1}{2}\Big[\psi_2^2 + \psi_3^2 + 2\psi_2\psi_3\cos\!\big(\tfrac{(E_3-E_2)t}{\hbar}\big)\Big].$$
*Why:* The two static terms carry no time dependence; only the cross term oscillates, at angular frequency $\omega = (E_3 - E_2)/\hbar$. This is the sloshing.

**Step 3 — [BLANK] Find the oscillation period $T$ in terms of $E_1$.**
*Your work here:*
_______________________________________________
*Why (your explanation):*
_______________________________________________

**Step 4 — [BLANK] Compute the energy expectation $\langle\hat H\rangle$.**
*Your work here:*
_______________________________________________
*Why (your explanation):*
_______________________________________________

**Step 5 — Sanity-check against the chapter's two-state result.** For the chapter's $\psi_1+\psi_2$ state the gap was $E_2 - E_1 = 3E_1$, giving $T = h/3E_1$. Here the gap is $E_3 - E_2 = (9-4)E_1 = 5E_1$, so the sloshing is faster (shorter period) and the energy expectation sits higher up the ladder. Confirm your Step 3 and Step 4 reproduce $T = h/5E_1$ and $\langle\hat H\rangle = \tfrac12(E_2+E_3) = \tfrac{13}{2}E_1$.

**Final answer:** $T = 2\pi\hbar/(E_3 - E_2) = h/5E_1$; $\langle\hat H\rangle = \tfrac12 E_2 + \tfrac12 E_3 = \tfrac{13}{2}E_1$, constant in time.

**Self-explanation prompt:** Explain why $\langle\hat H\rangle$ stays constant while $|\Psi|^2$ visibly sloshes. Which quantities are frozen by the initial state, and which evolve?

---

## Part D — Error-Recognition Problem

> **Use this section only after completing Parts A–C.**

**The problem:** A student computes the energy levels of an electron in an $L = 2$ nm infinite square well and the $n=1$ to $n=4$ spectrum.

**Step 1 — Interior solution.** With $V = 0$ inside, $\psi(x) = A\sin(kx)$ after applying $\psi(0)=0$, $k = \sqrt{2mE}/\hbar$. *(correct)*

**Step 2 — Boundary condition at $x = L$.** $\sin(kL) = 0 \Rightarrow k_n = n\pi/L$, $n = 1,2,3,\ldots$ *(correct)*

**Step 3 — ⚠ Convert to energy.** "Since $E = \hbar^2 k^2/2m$ and $k_n = n\pi/L$, the energy is $E_n = n\pi^2\hbar^2/2mL^2$, so the levels scale linearly with $n$: $E_1 : E_2 : E_3 : E_4 = 1:2:3:4$."

**Step 4 — Spectrum.** "Therefore the gaps are equal: $E_2 - E_1 = E_3 - E_2 = E_4 - E_3$, an evenly spaced ladder, and the $n=2\to1$ and $n=4\to3$ transitions emit identical photons." *(follows from Step 3, looks tidy)*

**Your tasks:**
1. Identify the exact error in Step 3 and state the correct energy formula.
2. Explain the physical/mathematical reason the error is wrong — what happens to the $k_n^2$ in $E = \hbar^2 k^2/2m$?
3. Correct the spectrum: write the true ratios $E_1:E_2:E_3:E_4$.
4. Show how the error propagates into Step 4 — are the gaps really equal, and do those two transitions emit identical photons?

**Why this error is common:** Students carry over the equal-spacing intuition from the harmonic oscillator (or from a half-remembered "$E \propto n$") and forget that squaring $k_n = n\pi/L$ inside $E = \hbar^2 k^2/2m$ makes the well's spectrum scale as $n^2$, not $n$.

---

## Part E — Transfer Problem

**The problem:** Consider a particle confined not to a line segment but to a one-dimensional *ring* of circumference $L$ (a particle on a circle, $V = 0$ everywhere along the ring). Here the boundary condition is not "$\psi$ vanishes at walls" — there are no walls — but *periodicity*: $\psi(x + L) = \psi(x)$. Starting from the same TISE $-(\hbar^2/2m)\psi'' = E\psi$, derive the allowed energies. How do they differ from the infinite square well's spectrum, and what is the key qualitative change (think about degeneracy and the lowest allowed energy)?

**Hint (use only if stuck after 10 minutes):** Write the general solution as $\psi(x) = Ae^{ikx} + Be^{-ikx}$ and impose $\psi(x+L) = \psi(x)$, which forces $e^{ikL} = 1$, i.e. $kL = 2\pi n$ with $n = 0, \pm1, \pm2, \ldots$ Note that $n$ and $-n$ now give *distinct* states (rightward vs leftward circulation) at the *same* energy.

**Reflection prompt:**
1. Why does periodicity allow $n = 0$ (a constant, nonzero $\psi$) when the infinite square well forbade it? What does the $n=0$ state mean physically?
2. The infinite well's levels are non-degenerate; the ring's excited levels are doubly degenerate. Trace this difference back to which boundary condition each system imposes.

---

## Part F — Interleaved Review

**Problem F1.** An electron in an infinite square well of width $L = 1$ nm is prepared in the ground state $\psi_1$. (a) Compute $\langle p\rangle$ and argue from symmetry. (b) Using $p = \hbar k_1 = \pi\hbar/L$ for the characteristic momentum, estimate the ground-state kinetic energy and compare to $E_1 \approx 0.377$ eV. (c) Explain in one sentence why $E_1 > 0$ is required by the uncertainty principle. *Chapter this draws from: [Chapter 5]*

**Problem F2.** A photon of wavelength $\lambda = 274$ nm (the emission found in Part A) is sent through a double-slit apparatus. (a) Compute the photon's momentum $p = h/\lambda$ and energy. (b) The de Broglie relation $p = \hbar k$ links a particle's momentum to a wave vector. For an *electron* of the same wavelength 274 nm, compute its kinetic energy and compare it to the photon's energy — why are they so different for the same wavelength? *Chapter this draws from: [Chapter 4 — Matter Waves and the de Broglie Relation]*

**Problem F3.** A particle of mass $m$ is in a one-dimensional region of width $L$ with $V = 0$ inside. You are told only that "the allowed energies are discrete and the lowest state has nonzero energy." Determine, from this information alone, whether the system is an infinite square well or a finite square well — and if you cannot tell, explain what additional measurement would distinguish them. *Note to instructor: intentionally ambiguous — both an infinite well and a sufficiently deep finite well have discrete levels with a nonzero ground state; the discriminator is whether the spectrum is infinite and exactly $\propto n^2$ (infinite well) or finite in number with levels shifted below $n^2\pi^2\hbar^2/2mL^2$ (finite well, Chapter 6).*

**Closing reflection:** Across F1–F3 you used the same eigenvalue/boundary-condition machinery for confinement, momentum-energy conversion, and model discrimination. Write two sentences on what stayed constant in the method and what changed with the physical setup.

---

## Instructor Notes

**Common errors:**
- Writing $E_n \propto n$ (linear) instead of $E_n \propto n^2$ — the squaring of $k_n$ inside $E = \hbar^2 k^2/2m$ is the most frequent slip (see Part D).
- Allowing $n = 0$ as a physical state of the infinite well, or miscounting interior nodes (the correct count is $n-1$, not $n$).
- Dropping the normalization constant $\sqrt{2/L}$ or writing $\sqrt{1/L}$, which corrupts every probability and expectation value.

**Signs a student needs to return:**
- They quote $E_n = n^2\pi^2\hbar^2/2mL^2$ correctly but cannot say *which step* of the derivation produced the integer $n$.
- They believe $|\Psi|^2$ of a single eigenstate oscillates in time (confusing the phase rotation $e^{-iE_n t/\hbar}$ with observable dynamics).

**Scaffolding adjustments:** If a student struggles with Part A, have them redo Step 3 in isolation: hand them $\psi(x) = A\sin(kx)$ and ask only "for which $k$ does this vanish at $x=L$?" — isolate the quantization step. If a student finishes Part F quickly, ask them to compute the actual $E_1$ for the finite-well case of F3 in the deep-well limit and show it approaches the infinite-well value from below.

**Domain adaptation note:** Replace the electron-in-a-nanowell setting with a particle in a circular quantum corral (the chapter's opening Crommie–Lutz–Eigler image) to show the same boundary-condition logic in two dimensions with Bessel-function radial modes.
