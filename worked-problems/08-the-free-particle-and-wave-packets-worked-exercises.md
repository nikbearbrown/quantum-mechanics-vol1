# Worked Exercises: The Free Particle and Wave Packets

*Chapter 8 of Quantum Mechanics — Volume 1*

> These exercises follow a research-backed sequence: full worked example → matched practice → completion problem → error-recognition → transfer → interleaved review. Each section builds on the previous. Do not skip ahead.

## Prerequisites

- You know a single plane wave $\psi_k = Ae^{ikx}$ has $|\psi_k|^2 = |A|^2$ everywhere and cannot be normalized on the real line, and that a normalizable free particle is a *wave packet* — a superposition of plane waves with nearby momenta.
- You know the dispersion relation $\omega(k) = \hbar k^2/2m$, the phase velocity $v_{ph} = \omega/k = \hbar k/2m$, the group velocity $v_g = d\omega/dk = \hbar k_0/m$, and that $v_g = 2v_{ph}$ for matter waves.
- You know the Gaussian packet spreads as $\sigma(t) = \sigma_0\sqrt{1 + (\hbar t/2m\sigma_0^2)^2}$, with doubling time $t_{2x} = 2m\sigma_0^2/\hbar$ independent of $k_0$, while $|\phi(k)|^2$ stays constant.

---

## Part A — Full Worked Example

**What this demonstrates:** How to compute the group velocity, phase velocity, and spreading of a free Gaussian wave packet, and how to read off the chapter's signature result $v_g = 2v_{ph}$ together with a real doubling-time number.

**The problem:** An electron is released from a quantum dot, initially localized to $\sigma_x(0) = \sigma_0 = 3$ nm with mean wavenumber $k_0 = 4\ \text{nm}^{-1} = 4\times10^9\ \text{m}^{-1}$, and the confining potential is switched off. Find $v_g$, $v_{ph}$, verify $v_g = 2v_{ph}$, and compute the doubling time $t_{2x}$ and the width $\sigma_x(t)$ at $t = 100$ fs.

**The solution:**

**Step 1 — Compute the group velocity (the physical speed).** $v_g = \hbar k_0/m_e$:
$$v_g = \frac{(1.055\times10^{-34})(4\times10^9)}{9.109\times10^{-31}} \approx 4.63\times10^{5}\ \text{m/s}.$$
*Why:* The group velocity is $d\omega/dk$ at $k_0$; it is the speed of the $|\Psi|^2$ envelope — the physically meaningful speed, equal to the classical $p_0/m$.
*Check:* $v_g \ll c$, so the non-relativistic treatment is fine. Units: $(\text{J·s})(\text{m}^{-1})/\text{kg} = \text{m/s}$. ✓

**Step 2 — Compute the phase velocity and verify the factor of two.** $v_{ph} = \hbar k_0/2m_e = v_g/2 \approx 2.31\times10^{5}$ m/s. Directly, $v_g/v_{ph} = (\hbar k_0/m)/(\hbar k_0/2m) = 2$.
*Why:* For the free-particle dispersion $\omega = \hbar k^2/2m$, the crests move at half the envelope speed. This is the chapter's headline: the envelope outruns its own internal wiggles, and crests are born at the back and die at the front.
*Check:* $v_g = 2v_{ph}$ exactly — independent of $k_0$ or mass, a property of the quadratic dispersion. ✓

**Step 3 — Compute the doubling time.** $t_{2x} = 2m_e\sigma_0^2/\hbar$:
$$t_{2x} = \frac{2(9.109\times10^{-31})(3\times10^{-9})^2}{1.055\times10^{-34}} = \frac{2(9.109\times10^{-31})(9\times10^{-18})}{1.055\times10^{-34}} \approx 1.55\times10^{-13}\ \text{s} \approx 155\ \text{fs}.$$
*Why:* The doubling time — when $\sigma_x$ has grown by $\sqrt2$ — is set entirely by $\sigma_0$ and $m$, *not* by $k_0$. A faster electron and a slower one of the same width spread at the same rate.
*Check:* Scaling against the chapter's $\sigma_0 = 2$ nm electron giving $t_{2x}\approx 69$ fs: $(3/2)^2 = 2.25$, and $69\times2.25 \approx 155$ fs. ✓ ($t_{2x}\propto\sigma_0^2$.)

**Step 4 — Evaluate the width at $t = 100$ fs.** Using $\sigma(t) = \sigma_0\sqrt{1 + (\hbar t/2m\sigma_0^2)^2}$, note $\hbar t/2m\sigma_0^2 = t/t_{2x} = 100/155 = 0.645$:
$$\sigma_x(100\ \text{fs}) = 3\ \text{nm}\times\sqrt{1 + (0.645)^2} = 3\sqrt{1 + 0.416} = 3\times1.190 \approx 3.57\ \text{nm}.$$
*Why:* The packet stays Gaussian but its width grows; at $t = t_{2x}$ the factor is exactly $\sqrt2$, and at $t < t_{2x}$ it is less.
*Check:* At $t = t_{2x} = 155$ fs the formula would give $3\sqrt2 \approx 4.24$ nm; our 100 fs value (3.57 nm) is sensibly below that. ✓

**Final answer:** $v_g \approx 4.63\times10^5$ m/s, $v_{ph} \approx 2.31\times10^5$ m/s ($v_g = 2v_{ph}$), $t_{2x} \approx 155$ fs, and $\sigma_x(100\ \text{fs}) \approx 3.57$ nm.

**What made this work:** The central concept is that *the envelope, not the crests, is the particle* — the group velocity is the physical speed and the phase velocity is an internal property of the wave structure. The naive approach of identifying the particle's speed with the phase velocity $v_{ph} = \omega/k$ gives exactly half the right answer and would, for instance, mispredict a time-of-flight by a factor of two. Equally, the spreading is governed by $\sigma_0$ and $m$ through $t_{2x}$, *not* by the mean momentum $k_0$ — so trying to "slow the spreading" by changing $k_0$ fails entirely.

**Self-explanation prompt:** Explain why the doubling time depends on $\sigma_0^2$ but not on $k_0$. What does this say about a tightly confined packet versus a loosely confined one of the same momentum?

---

## Part B — Matched Practice Problem

**The problem:** A conduction electron in GaAs has effective mass $m^* = 0.067\,m_e$ and is released from a region of initial width $\sigma_0 = 5$ nm with mean wavenumber $k_0 = 2\ \text{nm}^{-1}$. Find $v_g$, $v_{ph}$, verify $v_g = 2v_{ph}$, compute the doubling time $t_{2x}$, and the width $\sigma_x(t)$ at $t = 1$ ps.

Work it with the same four subgoals:

**Step 1 — Compute the group velocity (the physical speed).**

**Step 2 — Compute the phase velocity and verify the factor of two.**

**Step 3 — Compute the doubling time.**

**Step 4 — Evaluate the width at $t = 1$ ps.**

**Stuck?** Use $m = m^* = 0.067\times9.109\times10^{-31}$ kg everywhere — the small effective mass makes $v_g$ large *and* $t_{2x}$ short (both scale inversely with $m$). For the width at 1 ps, first compute $t_{2x}$, then form the dimensionless ratio $t/t_{2x}$ and use $\sigma(t) = \sigma_0\sqrt{1 + (t/t_{2x})^2}$.

*Instructor note: No solution is provided for Part B. Confirm $v_g = 2v_{ph}$ holds independent of the effective mass, and that your $t_{2x}$ scales as $\sigma_0^2/m$ relative to Part A.*

---

## Part C — Completion Problem

**The problem:** Find the initial width $\sigma_\text{opt}$ that *minimizes* the packet's width at a fixed later time $t$, for a particle of mass $m$. (This is the chapter's optimization: too narrow a start spreads fast; too wide a start is already broad.)

**Step 1 — Write the width-squared as a function of $\sigma_0$.** From the spreading law,
$$\sigma_x(t)^2 = \sigma_0^2 + \left(\frac{\hbar t}{2m\sigma_0}\right)^2.$$
*Why:* The first term is the starting width; the second is the dispersive growth, which *increases* as $\sigma_0$ shrinks. The two terms pull in opposite directions, so there is a minimum.

**Step 2 — Set up the minimization.** Treat $\sigma_x(t)^2$ as a function of $\sigma_0$ at fixed $t$ and differentiate, setting $\frac{d}{d\sigma_0}\sigma_x(t)^2 = 0$:
$$\frac{d}{d\sigma_0}\left[\sigma_0^2 + \frac{(\hbar t/2m)^2}{\sigma_0^2}\right] = 0.$$
*Why:* The optimal $\sigma_0$ balances the two competing terms; calculus locates the trade-off point exactly.

**Step 3 — [BLANK] Carry out the differentiation and solve for $\sigma_\text{opt}$.**
*Your work here:*
_______________________________________________
*Why (your explanation):*
_______________________________________________

**Step 4 — [BLANK] Evaluate $\sigma_\text{opt}$ for an electron at $t = 1$ fs and comment on the scale.**
*Your work here:*
_______________________________________________
*Why (your explanation):*
_______________________________________________

**Step 5 — Interpret the result.** The optimal width $\sigma_\text{opt} = \sqrt{\hbar t/2m}$ is the width at which "already broad" exactly balances "spreads fast." For an electron at $t = 1$ fs this lands on a sub-nanometre, atomic-scale length — suggesting why atomic-physics length scales are what they are. Confirm your Step 3 gives $\sigma_\text{opt} = \sqrt{\hbar t/2m}$.

**Final answer:** $\sigma_\text{opt} = \sqrt{\hbar t/2m}$; for an electron at $t = 1$ fs, $\sigma_\text{opt} = \sqrt{(1.055\times10^{-34})(10^{-15})/(2\times9.109\times10^{-31})} \approx 2.4\times10^{-10}$ m $\approx 0.24$ nm (a few atomic radii).

**Self-explanation prompt:** Explain why making the packet *too* narrow at $t=0$ is counterproductive if you want it narrow at a later time $t$. What is the physical trade-off being balanced?

---

## Part D — Error-Recognition Problem

> **Use this section only after completing Parts A–C.**

**The problem:** A student analyzes a cold neutron ($m_n = 1.675\times10^{-27}$ kg) with de Broglie wavelength $\lambda = 1.8$ Å travelling 1 m to a detector, and predicts the transit time.

**Step 1 — Wavenumber.** $k_0 = 2\pi/\lambda = 2\pi/(1.8\times10^{-10}\ \text{m}) \approx 3.49\times10^{10}\ \text{m}^{-1}$. *(correct)*

**Step 2 — A speed from the dispersion relation.** "The wave's speed is $\omega/k = \hbar k_0/2m_n$. With $\hbar k_0/2m_n = (1.055\times10^{-34})(3.49\times10^{10})/(2\times1.675\times10^{-27}) \approx 1099$ m/s." *(arithmetic correct)*

**Step 3 — ⚠ Transit time.** "The neutron's speed is the phase velocity $v_{ph} = \omega/k \approx 1099$ m/s, so the transit time over 1 m is $t = (1\ \text{m})/(1099\ \text{m/s}) \approx 910\ \mu\text{s}$. This is the time the neutron takes to reach the detector."

**Step 4 — Consistency.** "Checking energy: $K = \tfrac12 m_n v^2 = \tfrac12(1.675\times10^{-27})(1099)^2 \approx 1.0\times10^{-21}$ J. This matches a cold neutron." *(the number looks plausible)*

**Your tasks:**
1. Identify the exact error in Step 3 and name which velocity governs the neutron's arrival at the detector.
2. Explain the physics: which speed — phase or group — is the speed of the *particle* (the probability envelope), and what is the relation between the two for matter waves?
3. Correct the transit time: compute $v_g = \hbar k_0/m_n$ and the true transit time, and state by what factor the student's answer was wrong.
4. Step 4's energy check used the wrong speed too. Recompute $K$ with $v_g$ and show that it now equals $\hbar^2 k_0^2/2m_n$ — the correct consistency relation.

**Why this error is common:** Students see "$\omega/k$" labelled "velocity" in the dispersion relation and identify it as the particle's speed, forgetting that for matter waves the particle is the *envelope*, which moves at the group velocity $v_g = d\omega/dk = 2v_{ph}$ — so using $v_{ph}$ predicts a transit time exactly twice too long.

---

## Part E — Transfer Problem

**The problem:** A short pulse of light travels through an *optical fibre* whose dispersion relation near the carrier frequency is $\omega(k) = ck/n(k)$, where the refractive index $n(k)$ depends weakly on $k$ (the fibre is *dispersive*, unlike vacuum). (a) For light in *vacuum*, $\omega = ck$ exactly — compute $v_g$, $v_{ph}$, and $d^2\omega/dk^2$, and explain why a vacuum light pulse does *not* spread. (b) In a real fibre with $d^2\omega/dk^2 \neq 0$, argue qualitatively whether the pulse spreads, and connect this to the free electron's spreading. (c) Why is fibre dispersion a practical limit on data rates in optical communication?

**Hint (use only if stuck after 10 minutes):** Spreading is controlled by $d^2\omega/dk^2$ (group-velocity dispersion), *not* by the uncertainty principle — the chapter is explicit about this. In vacuum $\omega = ck$ is linear, so $d^2\omega/dk^2 = 0$ and $v_g = v_{ph} = c$: every Fourier component travels at the same speed, so the pulse keeps its shape forever. The free electron has $\omega = \hbar k^2/2m$ (quadratic), so $d^2\omega/dk^2 = \hbar/m \neq 0$ and it spreads.

**Reflection prompt:**
1. The chapter contrasts the free electron (spreads), the vacuum photon (no spreading), and the harmonic-oscillator coherent state (no spreading despite a dispersive system). What single quantity decides whether a packet spreads, and why does the oscillator escape it?
2. For an optical fibre, would you choose a *wider* or *narrower* initial pulse to minimize spreading over a fixed transmission distance — and how does this map onto the $\sigma_\text{opt}$ result of Part C?

---

## Part F — Interleaved Review

**Problem F1.** A free electron has $k_0 = 5\ \text{nm}^{-1}$. (a) Compute $v_{ph}$ and $v_g$ in m/s and verify $v_g = 2v_{ph}$. (b) Compute the classical kinetic energy $K = \tfrac12 m_e v_g^2$ and verify it equals $\hbar\omega(k_0) = \hbar^2 k_0^2/2m_e$. (c) Explain why a single plane wave of this $k_0$ cannot be normalized, and what it would mean for the electron's position. *Chapter this draws from: [Chapter 8]*

**Problem F2.** An electron is in the ground state of an *infinite square well* of width $L = 1$ nm. (a) Compute the characteristic momentum $p = \hbar k_1 = \pi\hbar/L$ and the ground-state energy $E_1$. (b) Unlike the free particle, this eigenstate *is* normalizable — explain what makes the difference (walls vs free space). (c) If the walls were suddenly removed at $t = 0$, the formerly bound electron would become a free wave packet — qualitatively, would it spread, and on roughly what timescale (use $\sigma_0 \sim L$)? *Chapter this draws from: [Chapter 5 — The Infinite Square Well]*

**Problem F3.** You are told a quantum state has a *time-independent* $|\phi(k)|^2$ (momentum distribution frozen) but a *time-dependent* position width. Decide whether this describes a free particle spreading or a harmonic-oscillator coherent state, and if you cannot tell from this alone, state the distinguishing observation. *Note to instructor: intentionally ambiguous — both the free Gaussian and the coherent state have constant $|\phi(k)|^2$, but the free packet's $\sigma_x$ grows monotonically while the coherent state's $\sigma_x$ stays fixed (it does not spread); a student must realize that "time-dependent width" alone points to the free particle, and that the coherent state's width is actually constant.*

**Closing reflection:** F1–F3 reused the Fourier/dispersion machinery across free propagation, confinement, and a discrimination puzzle. Write two sentences on what stays invariant during free evolution ($|\phi(k)|^2$, $\langle p\rangle$, energy) and what changes ($\sigma_x$, the position distribution).

---

## Instructor Notes

**Common errors:**
- Confusing phase velocity with group velocity — identifying the particle's speed as $v_{ph} = \omega/k$ instead of $v_g = d\omega/dk = 2v_{ph}$ (see Part D), which mispredicts arrival times by a factor of two.
- Forgetting that a free wave packet spreads in time (treating $\sigma_x$ as fixed), or attributing the spreading to the uncertainty principle rather than to dispersion $d^2\omega/dk^2 \neq 0$.
- Trying to normalize a single plane wave on the real line, or believing it is normalizable "in the limit."

**Signs a student needs to return:**
- They claim $\sigma_p$ must grow as the packet spreads "to keep $\sigma_x\sigma_p = \hbar/2$" (confusing an instantaneous constraint with time evolution).
- They expect the doubling time to depend on $k_0$, or cannot say why it depends only on $\sigma_0$ and $m$.

**Scaffolding adjustments:** If a student struggles with Part A, isolate the velocity comparison (Steps 1–2) using only $v_g = \hbar k_0/m$ and $v_{ph} = \hbar k_0/2m$ before touching the spreading formula. If a student finishes Part F fast, have them compute the chapter's marble result ($\sigma_0 = 1\ \mu$m, $m = 1$ mg) and confirm $t_{2x}$ exceeds hundreds of millions of years, making the classical limit a number.

**Domain adaptation note:** Replace the electron quantum dot with a Bose–Einstein condensate released from an optical trap, where the same free-expansion spreading law governs the cloud's growth and is imaged directly in time-of-flight experiments.
