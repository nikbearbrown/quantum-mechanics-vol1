# Worked Exercises: The Quantum Harmonic Oscillator

*Chapter 7 of Quantum Mechanics — Volume 1*

> These exercises follow a research-backed sequence: full worked example → matched practice → completion problem → error-recognition → transfer → interleaved review. Each section builds on the previous. Do not skip ahead.

## Prerequisites

- You know the spectrum $E_n = (n+\tfrac12)\hbar\omega$ with ground-state (zero-point) energy $E_0 = \tfrac12\hbar\omega \neq 0$, and the ladder operators $\hat a_\pm = \frac{1}{\sqrt{2\hbar m\omega}}(\mp i\hat p + m\omega\hat x)$ with $[\hat a_-,\hat a_+]=1$.
- You can apply the normalized ladder relations $\hat a_+|n\rangle = \sqrt{n+1}\,|n+1\rangle$ and $\hat a_-|n\rangle = \sqrt{n}\,|n-1\rangle$, and the operator expressions $\hat x = \sqrt{\hbar/2m\omega}\,(\hat a_+ + \hat a_-)$, $\hat p = i\sqrt{m\hbar\omega/2}\,(\hat a_+ - \hat a_-)$.
- You know energy eigenstates are stationary ($|\Psi_n(x,t)|^2 = |\psi_n(x)|^2$, time-independent) and that classical-looking oscillation appears only in superpositions or coherent states.

---

## Part A — Full Worked Example

**What this demonstrates:** How to compute an expectation value in an energy eigenstate using ladder operators alone — no integrals, no Hermite polynomials — and how the zero-point energy enters numerically.

**The problem:** For the HCl molecule (the chapter's worked example, $\omega \approx 5.63\times10^{14}$ rad/s, reduced mass $\mu \approx 1.63\times10^{-27}$ kg), find the energy of the *first excited* vibrational state $E_1$ in eV, and compute $\langle\hat x^2\rangle$ and the rms displacement in the state $|n=1\rangle$ using ladder algebra.

**The solution:**

**Step 1 — Write the energy of the level, keeping the zero-point term.** From $E_n = (n+\tfrac12)\hbar\omega$,
$$E_1 = \left(1 + \tfrac12\right)\hbar\omega = \tfrac32\hbar\omega = \tfrac32(1.055\times10^{-34})(5.63\times10^{14}) \approx 8.91\times10^{-20}\ \text{J} \approx 0.556\ \text{eV}.$$
*Why:* The spectrum is *equally spaced* with gap $\hbar\omega$, but it sits on a floor of $\tfrac12\hbar\omega$ — the zero-point energy. $E_1 = \tfrac32\hbar\omega$, not $\hbar\omega$.
*Check:* The chapter gives $E_0 = \tfrac12\hbar\omega \approx 0.185$ eV; $E_1$ should be $0.185 + \hbar\omega = 0.185 + 0.37 = 0.555$ eV. ✓

**Step 2 — Express $\hat x^2$ in ladder operators.** Using $\hat x = \ell(\hat a_+ + \hat a_-)$ with $\ell = \sqrt{\hbar/2\mu\omega}$,
$$\hat x^2 = \ell^2(\hat a_+ + \hat a_-)^2 = \ell^2(\hat a_+^2 + \hat a_-^2 + \hat a_+\hat a_- + \hat a_-\hat a_+).$$
*Why:* Recasting $\hat x$ in ladder operators turns a position integral into pure bookkeeping on number states. The squared term must be expanded carefully because $\hat a_+$ and $\hat a_-$ do not commute.
*Check:* $\ell$ has units $\sqrt{\text{J·s}/(\text{kg}\cdot\text{s}^{-1})} = \sqrt{\text{m}^2} = $ m. ✓

**Step 3 — Apply the operators to $|1\rangle$ and keep only diagonal terms.** Acting on $|1\rangle$: $\hat a_+^2|1\rangle \propto |3\rangle$ and $\hat a_-^2|1\rangle \propto |{-1}\rangle = 0$-type terms connect to $|3\rangle$ and $|{-1}\rangle$, both orthogonal to $|1\rangle$, contributing nothing to $\langle 1|\hat x^2|1\rangle$. The surviving terms:
$$\hat a_+\hat a_-|1\rangle = \hat a_+(\sqrt1\,|0\rangle) = \sqrt1\sqrt1\,|1\rangle = 1|1\rangle,\qquad \hat a_-\hat a_+|1\rangle = \hat a_-(\sqrt2\,|2\rangle) = \sqrt2\sqrt2\,|1\rangle = 2|1\rangle.$$
*Why:* Only number-conserving terms ($\hat a_+\hat a_-$ and $\hat a_-\hat a_+$) keep the state in $|1\rangle$; $\hat a_\pm^2$ change $n$ by $\pm 2$ and drop out of the diagonal matrix element. The $\sqrt{n+1},\sqrt{n}$ prefactors are mandatory.
*Check:* $\hat a_+\hat a_- = \hat N$ gives the number $n=1$; $\hat a_-\hat a_+ = \hat N + 1$ gives $2$. The general result $\langle n|\hat x^2|n\rangle = \ell^2(n + n + 1) = \ell^2(2n+1)$ at $n=1$ gives $3\ell^2$. ✓

**Step 4 — Assemble $\langle\hat x^2\rangle$ and the rms displacement.** So $\langle 1|\hat x^2|1\rangle = \ell^2(1 + 2) = 3\ell^2 = \frac{3\hbar}{2\mu\omega}$. Numerically, $\ell = \sqrt{\hbar/2\mu\omega} = \sqrt{(1.055\times10^{-34})/(2\times1.63\times10^{-27}\times5.63\times10^{14})} \approx 6.7\times10^{-12}$ m $= 6.7$ pm (the chapter's value). Thus
$$x_\text{rms} = \sqrt{\langle\hat x^2\rangle} = \sqrt3\,\ell \approx 1.73\times6.7 \approx 11.6\ \text{pm}.$$
*Why:* The rms displacement grows as $\sqrt{2n+1}$ up the ladder — the wave function spreads as you climb, exactly the chapter's "$\sigma_x$ grows as $\sqrt{2n+1}$."
*Check:* For $n=0$ the formula gives $x_\text{rms} = \ell \approx 6.7$ pm, matching the chapter's ground-state value. ✓

**Final answer:** $E_1 = \tfrac32\hbar\omega \approx 0.556$ eV; $\langle\hat x^2\rangle = 3\ell^2 = 3\hbar/2\mu\omega$, so $x_\text{rms} = \sqrt3\,\ell \approx 11.6$ pm.

**What made this work:** The central concept is that *the ladder algebra replaces integration*: every expectation value of $\hat x^n$ or $\hat p^n$ in an eigenstate reduces to counting how $\hat a_\pm$ raise and lower number states, weighted by $\sqrt{n+1}$ and $\sqrt n$. The naive approach — writing $\hat x^2$ as a position integral over $H_1(\xi)^2 e^{-\xi^2}$ — works but is laborious and error-prone, and crucially, dropping the $\sqrt{n+1}/\sqrt n$ normalization prefactors (a very common slip) gives wrong numbers while still "looking like" ladder algebra.

**Self-explanation prompt:** Explain why the $\hat a_+^2$ and $\hat a_-^2$ terms contribute nothing to $\langle 1|\hat x^2|1\rangle$ but *would* contribute to $\langle 3|\hat x^2|1\rangle$. What selection rule does this illustrate?

---

## Part B — Matched Practice Problem

**The problem:** The H$_2$ molecule (from the chapter's molecule table, $\omega \approx 8.28\times10^{14}$ rad/s, treat reduced mass $\mu \approx m_p/2 \approx 8.37\times10^{-28}$ kg). Find the energy of the *second excited* vibrational state $E_2$ in eV, and compute $\langle\hat x^2\rangle$ and the rms displacement in the state $|n=2\rangle$ using ladder algebra.

Work it with the same four subgoals:

**Step 1 — Write the energy of the level, keeping the zero-point term.**

**Step 2 — Express $\hat x^2$ in ladder operators.**

**Step 3 — Apply the operators to $|2\rangle$ and keep only diagonal terms.**

**Step 4 — Assemble $\langle\hat x^2\rangle$ and the rms displacement.**

**Stuck?** For $|n=2\rangle$, the general result is $\langle 2|\hat x^2|2\rangle = \ell^2(2n+1) = 5\ell^2$. Compute $E_2 = \tfrac52\hbar\omega$ (not $2\hbar\omega$ — keep the half-quantum) and $\ell = \sqrt{\hbar/2\mu\omega}$ for the new $\omega,\mu$. The chapter lists $\hbar\omega \approx 0.54$ eV for H$_2$, so $E_2 = \tfrac52\times0.54$ eV.

*Instructor note: No solution is provided for Part B. Verify your $E_2$ uses $(n+\tfrac12)$ and that $\langle\hat x^2\rangle = \ell^2(2n+1)$ reduces to the chapter's ground-state $\ell^2$ when $n=0$.*

---

## Part C — Completion Problem

**The problem:** A quantum harmonic oscillator is prepared in the equal-weight superposition $|\Psi\rangle = \frac{1}{\sqrt2}(|0\rangle + |1\rangle)$ of the ground and first excited states. Find the beat frequency of $|\Psi(x,t)|^2$ and the energy expectation $\langle\hat H\rangle$.

**Step 1 — Write the time-dependent state.** Attach phases $e^{-iE_n t/\hbar}$ with $E_n = (n+\tfrac12)\hbar\omega$:
$$\Psi(x,t) = \frac{1}{\sqrt2}\Big[\psi_0(x)\,e^{-iE_0 t/\hbar} + \psi_1(x)\,e^{-iE_1 t/\hbar}\Big].$$
*Why:* Each eigenstate is stationary on its own; the relative phase $e^{-i(E_1-E_0)t/\hbar}$ between the two terms drives the dynamics.

**Step 2 — Form the probability density.** Expanding,
$$|\Psi(x,t)|^2 = \tfrac12\big(|\psi_0|^2 + |\psi_1|^2\big) + \psi_0\psi_1\cos\!\Big(\tfrac{(E_1-E_0)t}{\hbar}\Big).$$
*Why:* The two static terms are time-independent; the cross term oscillates at $(E_1-E_0)/\hbar$, the beat frequency.

**Step 3 — [BLANK] Evaluate $E_1 - E_0$ and write the beat frequency.**
*Your work here:*
_______________________________________________
*Why (your explanation):*
_______________________________________________

**Step 4 — [BLANK] Compute $\langle\hat H\rangle$ and state whether it changes in time.**
*Your work here:*
_______________________________________________
*Why (your explanation):*
_______________________________________________

**Step 5 — Connect to classical oscillation.** The chapter notes that the $(|0\rangle+|1\rangle)/\sqrt2$ packet beats at exactly the classical frequency $\omega$, and that $\langle x(t)\rangle$ sloshes (these are opposite-parity states). Confirm your Step 3 gives a beat frequency of exactly $\omega$ and that Step 4 gives a constant $\langle\hat H\rangle = \hbar\omega$.

**Final answer:** $E_1 - E_0 = \hbar\omega$, so the beat frequency is $\omega$ (the classical oscillation frequency); $\langle\hat H\rangle = \tfrac12 E_0 + \tfrac12 E_1 = \tfrac12(\tfrac12\hbar\omega) + \tfrac12(\tfrac32\hbar\omega) = \hbar\omega$, constant in time.

**Self-explanation prompt:** Explain why the $(|0\rangle+|1\rangle)/\sqrt2$ superposition has a sloshing $\langle x(t)\rangle$ but the $(|0\rangle+|2\rangle)/\sqrt2$ superposition does not. (Hint: parity of $\psi_0$, $\psi_1$, $\psi_2$.)

---

## Part D — Error-Recognition Problem

> **Use this section only after completing Parts A–C.**

**The problem:** A student computes the vibrational spectrum of CO ($\omega \approx 4.09\times10^{14}$ rad/s) and the photon emitted in the $n=2 \to n=1$ transition.

**Step 1 — Identify the Hamiltonian.** $\hat H = \hat p^2/2m + \tfrac12 m\omega^2\hat x^2$, an oscillator. *(correct)*

**Step 2 — Level spacing.** Adjacent levels are separated by $\hbar\omega$, so the spectrum is equally spaced. *(correct)*

**Step 3 — ⚠ Energy levels.** "The energy of level $n$ is $E_n = n\hbar\omega$, so $E_0 = 0$, $E_1 = \hbar\omega$, $E_2 = 2\hbar\omega$. The ground state has zero energy — the molecule at rest at the bottom of the potential."

**Step 4 — Emission photon.** "The $n=2\to n=1$ transition emits a photon of energy $E_2 - E_1 = 2\hbar\omega - \hbar\omega = \hbar\omega \approx 0.27$ eV." *(the gap comes out right!)*

**Your tasks:**
1. Identify the exact error in Step 3 and write the correct energy formula.
2. Explain the physics: why is $E_0 \neq 0$? Connect it to the uncertainty principle and to a measurable consequence the chapter names.
3. Correct the level energies $E_0$, $E_1$, $E_2$ for CO in eV (use $\hbar\omega \approx 0.27$ eV).
4. Step 4 gets the right photon energy despite the wrong spectrum. Explain why the *transition* energy is insensitive to the omitted $\tfrac12\hbar\omega$, and why that makes the error easy to miss.

**Why this error is common:** Students write $E_n = n\hbar\omega$ by analogy with "$n$ quanta of $\hbar\omega$" and omit the zero-point energy $\tfrac12\hbar\omega$; because the half-quantum cancels in every *transition* energy $E_m - E_n$, the mistake stays hidden until you ask for an absolute energy, the ground-state motion, or zero-point phenomena like the Casimir force or liquid helium.

---

## Part E — Transfer Problem

**The problem:** A single mode of the electromagnetic field in a laser cavity is, mathematically, a harmonic oscillator: $\hat H = \hbar\omega(\hat a^\dagger\hat a + \tfrac12)$, where $\hat a^\dagger$ is the photon creation operator and $|n\rangle$ is the state with $n$ photons. (a) Write the energy of the $n$-photon state and identify the vacuum energy. (b) An ideal laser produces light in a *coherent state* $|\alpha\rangle$ with $\hat a|\alpha\rangle = \alpha|\alpha\rangle$. Using the chapter's result $\langle n\rangle = |\alpha|^2$ and the Poisson weights $P(n) = e^{-|\alpha|^2}|\alpha|^{2n}/n!$, find the mean photon number and the most probable photon number for $|\alpha|^2 = 4$. (c) Why is the vacuum energy $\tfrac12\hbar\omega$ per mode physically real here, and what laboratory effect does it produce?

**Hint (use only if stuck after 10 minutes):** The field oscillator has *exactly* the same algebra as the mechanical oscillator — $[\hat a, \hat a^\dagger] = 1$ — so $E_n = (n+\tfrac12)\hbar\omega$ with vacuum energy $\tfrac12\hbar\omega$. For the Poisson distribution with mean $|\alpha|^2 = 4$, the mean is 4 and the most probable $n$ is the largest integer $\leq |\alpha|^2$. The chapter names the Casimir force (Lamoreaux 1997) as the measurable consequence of summed vacuum energies.

**Reflection prompt:**
1. The chapter says "the harmonic oscillator algebra is not an analogy for laser physics; it is laser physics." Explain what carries over *exactly* (not approximately) between the mechanical oscillator and the field mode.
2. Why does an ideal laser's photon-counting statistics being Poisson follow from the field being in a coherent state, rather than from the laser being "classical"?

---

## Part F — Interleaved Review

**Problem F1.** For the HCl molecule ($\omega \approx 5.63\times10^{14}$ rad/s), (a) compute the zero-point energy $E_0$ in eV and the level spacing $\hbar\omega$ in eV. (b) Compare $\hbar\omega$ to $k_BT \approx 0.025$ eV at 300 K — what fraction of HCl molecules are vibrationally excited at room temperature? (c) Compute the wavelength of the $n=0\to n=1$ absorption line and identify the band (the chapter says $\approx 3.4\ \mu$m). *Chapter this draws from: [Chapter 7]*

**Problem F2.** An electron in an *infinite square well* of width $L = 0.3$ nm is prepared in $\frac{1}{\sqrt2}(\psi_1 + \psi_2)$. (a) Find the beat period of $|\Psi(x,t)|^2$ in terms of $E_1$. (b) Compute $\langle\hat H\rangle$. (c) Contrast the well's $n^2$-spaced spectrum with the oscillator's equally spaced spectrum — for which system does a two-level superposition beat at a single clean frequency regardless of which two levels you pick? *Chapter this draws from: [Chapter 5 — The Infinite Square Well]*

**Problem F3.** You measure a one-dimensional bound quantum system and find its energy levels are *equally spaced*. Decide whether this is a harmonic oscillator or an infinite square well, and if you cannot tell from spacing alone, state what additional information settles it. *Note to instructor: intentionally ambiguous — equal spacing strongly suggests the oscillator ($E_n = (n+\tfrac12)\hbar\omega$), but a student must recognize that the infinite well is $\propto n^2$ (not equally spaced) and that the *low-lying* levels of neither match the other; the tell is whether spacing stays constant up the ladder (oscillator) or grows (well).*

**Closing reflection:** F1–F3 contrasted equally spaced (oscillator) and $n^2$-spaced (well) spectra and reused the same superposition-beating machinery. Write two sentences on what the ladder algebra buys you that direct integration does not, and where the two spectra diverge.

---

## Instructor Notes

**Common errors:**
- Writing $E_n = n\hbar\omega$ and omitting the zero-point energy $\tfrac12\hbar\omega$ (see Part D) — invisible in transition energies, fatal for absolute energies and ground-state physics.
- Dropping the ladder-operator normalization prefactors $\sqrt{n+1}$ and $\sqrt n$, or swapping them ($\sqrt n$ on the raising operator).
- Treating a single energy eigenstate as time-oscillating; $|\Psi_n(x,t)|^2$ is static because the phase $e^{-iE_n t/\hbar}$ cancels in the modulus.

**Signs a student needs to return:**
- They cannot say why $E_0 = \tfrac12\hbar\omega$ rather than zero, or attribute zero-point energy to "a math artifact."
- They expect the eigenstate-mode simulation panel to animate (confusing phase rotation with observable motion).

**Scaffolding adjustments:** If a student struggles with Part A, give them the general formula $\langle n|\hat x^2|n\rangle = \ell^2(2n+1)$ and have them *derive* it for $n=1$ by tracking $\hat a_+\hat a_-$ and $\hat a_-\hat a_+$ explicitly, so the $\sqrt{n+1}/\sqrt n$ bookkeeping is the focus. If a student finishes Part F fast, have them show the $(|0\rangle+|2\rangle)/\sqrt2$ superposition "breathes" rather than sloshes by computing $\langle x(t)\rangle = 0$ from parity.

**Domain adaptation note:** Swap the molecular vibration setting for a trapped-ion qubit, where the same ladder operators describe the ion's motional modes and laser-driven $\Delta n = \pm 1$ sideband transitions are the basis of ion-trap quantum gates.
