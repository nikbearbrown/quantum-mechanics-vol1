# Worked Exercises: Finite Wells, Steps, and Barriers

*Chapter 6 of Quantum Mechanics — Volume 1*

> These exercises follow a research-backed sequence: full worked example → matched practice → completion problem → error-recognition → transfer → interleaved review. Each section builds on the previous. Do not skip ahead.

## Prerequisites

- You can compute $\kappa = \sqrt{2m(V_0 - E)}/\hbar$ for the classically forbidden region and $k = \sqrt{2mE}/\hbar$ for an allowed region, and you know that below a barrier the wave function is a decaying exponential, not an oscillation.
- You know the exact rectangular-barrier transmission $T_\text{exact} = [1 + V_0^2\sinh^2(\kappa L)/4E(V_0-E)]^{-1}$, its thick-barrier limit $T \approx \frac{16E(V_0-E)}{V_0^2}e^{-2\kappa L}$, and the WKB form $T_\text{WKB} = e^{-2\kappa L}$.
- You can use probability current to define $R$ and $T$ for a step, know $R + T = 1$ always, and that for a step $T \neq |C/A|^2$ unless $k_0 = k_1$.

---

## Part A — Full Worked Example

**What this demonstrates:** How to compute exact tunneling transmission through a rectangular barrier, identify when the thick-barrier limit applies, and verify it against WKB through the analytic prefactor — the chapter's central tunneling calculation.

**The problem:** An electron ($m_e = 9.109\times10^{-31}$ kg) with kinetic energy $E = 2$ eV strikes a rectangular barrier of height $V_0 = 6$ eV and width $L = 4$ Å. Compute $\kappa$, $T_\text{exact}$, $T_\text{WKB}$, and confirm their ratio equals the prefactor $16E(V_0-E)/V_0^2$.

**The solution:**

**Step 1 — Compute the decay constant in the forbidden region.** With $V_0 - E = 4$ eV $= 4\times1.602\times10^{-19}$ J,
$$\kappa = \frac{\sqrt{2m_e(V_0-E)}}{\hbar} = \frac{\sqrt{2(9.109\times10^{-31})(4)(1.602\times10^{-19})}}{1.055\times10^{-34}} \approx 1.025\times10^{10}\ \text{m}^{-1} = 1.025\ \text{Å}^{-1}.$$
*Why:* Inside the barrier $E < V_0$, so the kinetic energy is negative and the solution decays as $e^{-\kappa x}$; $\kappa$ sets the penetration depth $1/\kappa \approx 0.98$ Å.
*Check:* $\kappa$ has units m$^{-1}$ — an inverse length, as a decay constant must. The value matches the chapter's worked example (same $V_0 - E = 4$ eV gives the same $\kappa$). ✓

**Step 2 — Form the dimensionless barrier strength $\kappa L$.** $\kappa L = 1.025\ \text{Å}^{-1} \times 4\ \text{Å} = 4.10$. Since $\kappa L \gg 1$, the thick-barrier limit is valid.
*Why:* When $\kappa L \gg 1$, $\sinh(\kappa L) \approx e^{\kappa L}/2$ and the exponential dominates the transmission. $\kappa L$ is the exponent that controls everything.
*Check:* $\kappa L$ is dimensionless (Å$^{-1}\times$Å). ✓

**Step 3 — Evaluate $\sinh(\kappa L)$ and the exact transmission.** $\sinh(4.10) = (e^{4.10} - e^{-4.10})/2 \approx (60.34 - 0.0166)/2 \approx 30.16$. Then
$$T_\text{exact} = \left[1 + \frac{V_0^2\sinh^2(\kappa L)}{4E(V_0-E)}\right]^{-1} = \left[1 + \frac{36\times(30.16)^2}{4\times2\times4}\right]^{-1} = \left[1 + \frac{36\times909.6}{32}\right]^{-1}.$$
The bracket is $1 + 1023 = 1024$, so $T_\text{exact} \approx 9.8\times10^{-4}$.
*Why:* The exact formula contains the full dependence on $V_0$, $L$, and $E$; the $\sinh^2$ carries the exponential suppression.
*Check:* $T \ll 1$ but nonzero — a particle with $E < V_0$ still gets through, the quantum signature of tunneling. ✓

**Step 4 — Compute the WKB transmission.** $T_\text{WKB} = e^{-2\kappa L} = e^{-8.20} \approx 2.74\times10^{-4}$.
*Why:* WKB captures the exponential suppression $e^{-2\kappa L}$ exactly; it omits only the smooth prefactor.
*Check:* $T_\text{WKB} < T_\text{exact}$, as expected since the prefactor here exceeds 1. ✓

**Step 5 — Verify the ratio against the analytic prefactor.** $T_\text{exact}/T_\text{WKB} = 9.8\times10^{-4}/2.74\times10^{-4} \approx 3.58$. The predicted prefactor is
$$\frac{16E(V_0-E)}{V_0^2} = \frac{16\times2\times4}{36} = \frac{128}{36} \approx 3.56.$$
*Why:* In the thick-barrier limit $T_\text{exact} \approx \frac{16E(V_0-E)}{V_0^2}e^{-2\kappa L}$, so the ratio must equal exactly that prefactor — this is the chapter's consistency check.
*Check:* $3.58 \approx 3.56$ (small rounding from the $\sinh$ approximation) — agreement, as it must be. ✓

**Final answer:** $\kappa \approx 1.025$ Å$^{-1}$, $T_\text{exact} \approx 9.8\times10^{-4}$, $T_\text{WKB} \approx 2.7\times10^{-4}$, ratio $\approx 3.56 = 16E(V_0-E)/V_0^2$.

**What made this work:** The central concept is that *the transmission through a barrier is exponentially small but never zero*, and that WKB nails the exponent while the prefactor lives in the algebra of matching conditions. The naive classical approach says a particle with $E < V_0$ reflects completely ($T = 0$) — full stop — and that is simply wrong: the wave equation requires nonzero amplitude in the forbidden region, and a finite barrier lets that amplitude reach the far side. Forgetting that $\kappa L \gg 1$ matters (using $\sinh \approx \kappa L$ from the *thin*-barrier limit) would overstate $T$ by orders of magnitude.

**Self-explanation prompt:** Explain why doubling $L$ from 4 Å to 8 Å does *not* halve $T$ but instead squares the small number $e^{-2\kappa L}$. Roughly how many orders of magnitude does $T$ drop?

---

## Part B — Matched Practice Problem

**The problem:** A scanning tunneling microscope tip hovers above a gold surface with work function $\phi \approx 5.0$ eV, acting as a barrier for electrons. Treat the vacuum gap of width $L = 6$ Å as a rectangular barrier of height $V_0 = 5.0$ eV for an electron with $E = 1.0$ eV. Compute $\kappa$, $T_\text{exact}$, $T_\text{WKB}$, confirm the ratio equals the prefactor, and then find the factor by which the tunneling current changes if the gap shrinks by 1 Å (to 5 Å).

Work it with the same five subgoals:

**Step 1 — Compute the decay constant in the forbidden region.**

**Step 2 — Form the dimensionless barrier strength $\kappa L$.**

**Step 3 — Evaluate $\sinh(\kappa L)$ and the exact transmission.**

**Step 4 — Compute the WKB transmission.**

**Step 5 — Verify the ratio against the analytic prefactor, then compute the current change for a 1 Å gap reduction.**

**Stuck?** For the gap-change part, the current is proportional to $T \approx (\text{prefactor})\,e^{-2\kappa L}$, so the ratio of currents at 5 Å vs 6 Å is approximately $e^{-2\kappa(5)}/e^{-2\kappa(6)} = e^{+2\kappa\,(1\,\text{Å})}$. This is the chapter's "factor of 7 to 10 per ångström" sensitivity that makes atomic-resolution imaging possible.

*Instructor note: No solution is provided for Part B. Check your $\kappa$ against the chapter's STM examples ($\sim 1$ Å$^{-1}$ for few-eV barriers) and confirm your ratio equals $16E(V_0-E)/V_0^2$.*

---

## Part C — Completion Problem

**The problem:** A particle of mass $m$ strikes a potential step ($V = 0$ for $x<0$, $V = V_0$ for $x>0$) with energy $E = 3V_0$ (so $E > V_0$). Find the reflection coefficient $R$ and confirm $R + T = 1$ using probability current.

**Step 1 — Write the wave functions and wave vectors.** In region I, $\psi_I = Ae^{ik_0 x} + Be^{-ik_0 x}$ with $k_0 = \sqrt{2mE}/\hbar$; in region II only a transmitted wave $\psi_{II} = Ce^{ik_1 x}$ with $k_1 = \sqrt{2m(E-V_0)}/\hbar$.
*Why:* Above the step both regions are classically allowed, so both solutions oscillate; there is no wave incident from the right, so region II has no $e^{-ik_1 x}$ term.

**Step 2 — Match $\psi$ and $\psi'$ at $x = 0$ and solve the amplitude ratios.** Continuity gives $A + B = C$ and $k_0(A - B) = k_1 C$. Solving, $B/A = (k_0 - k_1)/(k_0 + k_1)$ and $C/A = 2k_0/(k_0 + k_1)$.
*Why:* The wave function and its derivative must be continuous where $V$ is finite; these two conditions fix the two ratios.

**Step 3 — [BLANK] Evaluate $k_1/k_0$ for $E = 3V_0$ and compute $R = |B/A|^2$.**
*Your work here:*
_______________________________________________
*Why (your explanation):*
_______________________________________________

**Step 4 — [BLANK] Compute $T$ using probability current ($T = \frac{k_1}{k_0}|C/A|^2$) and verify $R + T = 1$.**
*Your work here:*
_______________________________________________
*Why (your explanation):*
_______________________________________________

**Step 5 — Interpret physically.** Even though $E = 3V_0$ — three times the step height — $R$ is small but nonzero. Classically a particle with $E > V_0$ transmits completely; the quantum reflection comes purely from the abrupt change in $k$ at the boundary, like an impedance mismatch in a transmission line. Confirm your $R$ is a small positive number and that $R + T = 1$ exactly.

**Final answer:** With $k_1/k_0 = \sqrt{(E-V_0)/E} = \sqrt{2/3}$, $R = \left(\frac{1-\sqrt{2/3}}{1+\sqrt{2/3}}\right)^2 \approx 0.0102$, $T \approx 0.9898$, and $R + T = 1$.

**Self-explanation prompt:** Explain why using $T = |C/A|^2$ (without the $k_1/k_0$ factor) would *break* $R + T = 1$. What physical quantity does the $k_1/k_0$ factor restore?

---

## Part D — Error-Recognition Problem

> **Use this section only after completing Parts A–C.**

**The problem:** A student analyzes an electron with $E = 2$ eV hitting a barrier of height $V_0 = 6$ eV and width $L = 4$ Å — and is asked about the wave function *inside* the barrier.

**Step 1 — Identify the regime.** $E < V_0$, so the barrier region is classically forbidden; $\kappa = \sqrt{2m(V_0-E)}/\hbar \approx 1.025$ Å$^{-1}$. *(correct)*

**Step 2 — Region I and region III.** Oscillatory: $\psi_I = Ae^{ikx} + Be^{-ikx}$, $\psi_{III} = Fe^{ikx}$ with $k = \sqrt{2mE}/\hbar$. *(correct)*

**Step 3 — ⚠ Wave function inside the barrier.** "Since the electron does not have enough energy to be in the barrier, the wave function inside is oscillatory but with a smaller amplitude: $\psi_{II} = C\sin(\kappa x) + D\cos(\kappa x)$. The probability density there is essentially zero because the particle is classically forbidden from that region."

**Step 4 — Transmission.** "Because $|\psi_{II}|^2 \approx 0$ throughout the barrier, almost nothing reaches region III, so $T$ is extremely small — about $10^{-3}$." *(the number happens to be right)*

**Your tasks:**
1. Identify the exact error in Step 3 and write the correct form of $\psi_{II}$.
2. Explain the physics: in the forbidden region $E < V_0$, what kind of function solves the TISE — oscillatory or exponential — and why?
3. Correct the claim that the probability density inside the barrier is "essentially zero." Is there nonzero probability density inside? Is there net current?
4. Step 4 gets the right order of magnitude for $T$ by accident. Explain how a fundamentally wrong picture of $\psi_{II}$ can still yield a plausible $T$, and why that makes the error dangerous.

**Why this error is common:** Students reflexively associate "wave function" with "oscillation" (as in the infinite well) and forget that where $E < V_0$ the TISE becomes $\psi'' = +\kappa^2\psi$, whose solutions are *real exponentials* $e^{\pm\kappa x}$ — decaying, not oscillating — and that a nonzero decaying tail still carries real probability density across the barrier.

---

## Part E — Transfer Problem

**The problem:** An alpha particle is trapped inside a uranium-238 nucleus behind a Coulomb barrier — the chapter's Gamow problem. Model the barrier crudely as a single rectangular barrier of height $V_0 = 30$ MeV and width $L = 20$ fm, with an alpha particle of energy $E = 5$ MeV and mass $m_\alpha \approx 6.64\times10^{-27}$ kg. Estimate $\kappa$ (use $\hbar c = 197$ MeV·fm and $m_\alpha c^2 \approx 3727$ MeV to keep the units clean) and the WKB transmission $T_\text{WKB} = e^{-2\kappa L}$. Comment on why a small change in $E$ produces an enormous change in the decay rate.

**Hint (use only if stuck after 10 minutes):** Work in natural nuclear units: $\kappa = \sqrt{2m_\alpha c^2 (V_0 - E)}/(\hbar c)$ in fm$^{-1}$. With $V_0 - E = 25$ MeV, $\kappa = \sqrt{2\times3727\times25}/197$ fm$^{-1}$. Then $T_\text{WKB} = e^{-2\kappa L}$ — expect an astronomically small number, consistent with billion-year half-lives.

**Reflection prompt:**
1. The chapter states that a factor of two in alpha energy produces ~24 orders of magnitude difference in half-life. Using your expression for $\kappa(E)$, explain why the dependence is so violent — what is exponentiated?
2. The rectangular-barrier model is a caricature of the real Coulomb barrier. Which feature of the true barrier (its shape, its width's energy-dependence) does the rectangular model miss, and would a proper treatment make the energy sensitivity stronger or weaker?

---

## Part F — Interleaved Review

**Problem F1.** A finite square well has depth $V_0 = 4$ eV and width $L = 0.5$ nm for an electron. (a) Compute the dimensionless parameter $z_0 = (L/2\hbar)\sqrt{2mV_0}$. (b) Estimate the number of bound states from $N \approx \lceil z_0/(\pi/2)\rceil$. (c) Will this well always have at least one bound state no matter how shallow? Explain from the graphical (quarter-circle intersecting $z\tan z$) picture. *Chapter this draws from: [Chapter 6]*

**Problem F2.** An electron is confined to an *infinite* square well of width $L = 0.5$ nm. (a) Compute $E_1$, $E_2$, $E_3$ in eV. (b) Now imagine lowering the walls to the finite depth of F1 ($V_0 = 4$ eV). Argue whether the finite-well levels lie above or below the infinite-well values, and why. (c) As $V_0 \to \infty$, what happens to the finite-well penetration depth $1/\kappa$? *Chapter this draws from: [Chapter 5 — The Infinite Square Well]*

**Problem F3.** You are told a one-dimensional potential supports exactly three discrete bound states and a continuum of scattering states above some energy. Determine whether this is a finite square well or an infinite square well — and if you cannot decide, state the distinguishing feature. *Note to instructor: intentionally ambiguous — the infinite well supports infinitely many bound states and no continuum, whereas a finite well supports a finite number (here three) plus a scattering continuum; the phrase "continuum of scattering states" is the tell that it must be the finite well, but a student who fixates on "discrete bound states" alone may guess wrong.*

**Closing reflection:** F1–F3 moved between bound-state counting, the infinite-well limit, and model discrimination. Write two sentences naming what the finite well adds to the infinite-well picture (penetration, finite level count) and what carries over unchanged.

---

## Instructor Notes

**Common errors:**
- Using oscillatory $\sin/\cos$ instead of decaying exponentials $e^{\pm\kappa x}$ in the classically forbidden region $E < V_0$ (see Part D).
- Computing step transmission as $T = |C/A|^2$ without the $k_1/k_0$ probability-current factor, which silently breaks $R + T = 1$.
- Claiming a particle with $E > V_0$ transmits with $R = 0$ (classical intuition), or that a particle with $E < V_0$ has $T = 0$ exactly.

**Signs a student needs to return:**
- They assert the probability density inside a barrier is zero "because the region is classically forbidden."
- They cannot explain why $R + T = 1$ must hold and treat it as a coincidence rather than a conservation law from probability current.

**Scaffolding adjustments:** If a student struggles with Part A, strip it to just Step 1 and Step 3 with the numbers handed in, so they practice the $\kappa \to \sinh(\kappa L) \to T$ pipeline without the prefactor check. If a student finishes Part F fast, have them reduce $V_0$ in F1 numerically until the second bound state disappears and find the threshold $z_0 = \pi/2$.

**Domain adaptation note:** Recast the barrier problem as a resonant-tunneling diode (two barriers separated by a well) to show how engineered double barriers produce transmission resonances ($T = 1$) used in real devices.
