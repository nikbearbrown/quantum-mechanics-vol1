# Worked Exercises: Why Classical Physics Failed — Blackbody, Photoelectric, and the Photon
*Chapter 1 of Quantum Mechanics — Volume 1*

> These exercises follow a research-backed sequence: full worked example → matched practice → completion problem → error-recognition → transfer → interleaved review. Each section builds on the previous. Do not skip ahead.

## Prerequisites

- The Planck distribution $u(\nu,T) = \frac{8\pi h\nu^3}{c^3}\cdot\frac{1}{e^{h\nu/k_BT}-1}$, the Rayleigh–Jeans law $u_{\text{RJ}} = \frac{8\pi\nu^2}{c^3}k_BT$, and the dimensionless parameter $x = h\nu/k_BT$ that governs which regime you are in.
- Einstein's photoelectric equation $K_\text{max} = h\nu - \Phi$, the stopping-potential relation $eV_\text{stop} = K_\text{max}$, and the shortcut $hc = 1240$ eV·nm.
- The constants $h = 6.626\times10^{-34}$ J·s, $k_B = 1.381\times10^{-23}$ J/K, and the conversion $1$ eV $= 1.602\times10^{-19}$ J.

---

## Part A — Full Worked Example

**What this demonstrates:** How the parameter $x = h\nu/k_BT$ decides whether the classical Rayleigh–Jeans law agrees with the Planck distribution or fails catastrophically.

**The problem:** A tungsten filament at $T = 3000$ K (the same temperature used in the chapter's "Twenty Orders of Magnitude" example) emits across the spectrum. Compare the Planck and Rayleigh–Jeans predictions for the spectral energy density at *two* frequencies: a near-infrared frequency $\nu_1 = 3\times10^{13}$ Hz and an ultraviolet frequency $\nu_2 = 3\times10^{15}$ Hz. At which frequency is classical physics still trustworthy, and by what factor does it fail at the other?

**The solution:**

**Step 1 — Reduce the comparison to the average-energy ratio.** Both formulas share the identical mode density $8\pi\nu^2/c^3$, so the ratio is just the ratio of average energies per mode:
$$\frac{u_\text{Planck}}{u_\text{RJ}} = \frac{h\nu/k_BT}{e^{h\nu/k_BT}-1} = \frac{x}{e^x - 1}.$$
*Why:* The Rayleigh–Jeans law assigns $k_BT$ to every mode (continuous equipartition); Planck assigns $\langle E\rangle = h\nu/(e^{h\nu/k_BT}-1)$ because the oscillators hold only discrete multiples of $h\nu$. The geometric mode-counting cancels. *Check:* As $x\to 0$, $e^x - 1 \to x$ and the ratio $\to 1$ — Planck reduces to Rayleigh–Jeans, as the chapter requires.

**Step 2 — Compute $x$ at the infrared frequency $\nu_1$.** First $k_BT = (1.381\times10^{-23})(3000) = 4.14\times10^{-20}$ J $= 0.259$ eV. Then
$$x_1 = \frac{h\nu_1}{k_BT} = \frac{(6.626\times10^{-34})(3\times10^{13})}{4.14\times10^{-20}} = \frac{1.988\times10^{-20}}{4.14\times10^{-20}} = 0.480.$$
*Why:* $x = h\nu/k_BT$ is the only quantity that controls the ratio; everything reduces to comparing $h\nu$ (the photon energy, $0.124$ eV here) against the thermal energy scale $k_BT$. *Check:* $h\nu_1 = 0.124$ eV is below $k_BT = 0.259$ eV, so $x_1 < 1$ — we expect near-agreement.

**Step 3 — Evaluate the ratio at $\nu_1$.** With $x_1 = 0.480$:
$$\frac{u_\text{Planck}}{u_\text{RJ}} = \frac{0.480}{e^{0.480}-1} = \frac{0.480}{1.616 - 1} = \frac{0.480}{0.616} = 0.779.$$
*Why:* When $x \lesssim 1$, the exponential is still close to its linear expansion, so the discrete sum and the continuous integral differ only modestly. This is the long-wavelength regime where the chapter says classical physics "was already correct." *Check:* The ratio is below 1 but of order unity — Rayleigh–Jeans overestimates by about 28%, not by orders of magnitude. Sensible for $x < 1$.

**Step 4 — Compute $x$ at the ultraviolet frequency $\nu_2$.** Now $\nu_2 = 3\times10^{15}$ Hz is 100 times larger, so $x_2 = 100\,x_1 = 48.0$ (matching the chapter's $x \approx 47.9$ for this case):
$$x_2 = \frac{(6.626\times10^{-34})(3\times10^{15})}{4.14\times10^{-20}} = 48.0.$$
*Why:* The photon energy is now $h\nu_2 = 12.4$ eV, nearly 50 times $k_BT$. A single UV photon carries far more than the thermal budget, so almost no modes are excited. *Check:* $x_2 \gg 1$ — we expect catastrophic disagreement, the ultraviolet catastrophe region.

**Step 5 — Evaluate the ratio at $\nu_2$.** With $x_2 = 48.0$, $e^{48.0}\approx 7\times10^{20}$:
$$\frac{u_\text{Planck}}{u_\text{RJ}} = \frac{48.0}{e^{48.0}-1} \approx \frac{48.0}{7\times10^{20}} \approx 7\times10^{-20}.$$
*Why:* The exponential $e^{-x}$ suppression "kills the polynomial," exactly as the chapter states. The Planck curve falls off exponentially while Rayleigh–Jeans grows like $\nu^2$ without bound. *Check:* Twenty orders of magnitude — matching the chapter's worked example to the digit. The classical prediction is not approximately wrong; it is completely wrong.

**Final answer:** At $\nu_1 = 3\times10^{13}$ Hz ($x_1 = 0.48$), Rayleigh–Jeans is trustworthy to within ~28% ($u_\text{Planck}/u_\text{RJ} = 0.78$). At $\nu_2 = 3\times10^{15}$ Hz ($x_2 = 48$), it fails by a factor of $\sim 7\times10^{-20}$ — twenty orders of magnitude.

**What made this work:** The central concept is that quantization of oscillator energy in units of $h\nu$ replaces the continuous equipartition value $k_BT$ with the Planck average energy, and the single dimensionless ratio $x = h\nu/k_BT$ decides everything. A naive approach — plugging numbers into both full formulas and dividing the spectral densities directly — wastes effort and obscures the physics, because the $8\pi\nu^2/c^3$ mode density is identical in both and cancels. The failure of classical physics is not about mode counting (which "is not wrong"); it is entirely about how energy is distributed among modes.

**Self-explanation prompt:** In your own words, explain why the boundary $h\nu \sim k_BT$ (i.e. $x\approx 1$) marks the place where quantization "starts to matter," and why no amount of cooling or heating moves a *fixed* frequency permanently into the classical regime.

---

## Part B — Matched Practice Problem

**What this demonstrates:** The same $x = h\nu/k_BT$ analysis at a different temperature and frequency.

**The problem:** The Sun's photosphere is at $T = 5778$ K. Compare the Planck and Rayleigh–Jeans predictions at a visible frequency $\nu = 6\times10^{14}$ Hz (green-ish light) and at a far-ultraviolet frequency $\nu = 6\times10^{15}$ Hz. At which frequency is the classical law trustworthy, and by what factor does it fail at the other?

Work it in the same five steps: reduce to the average-energy ratio $x/(e^x-1)$; compute $k_BT$; compute $x$ at each frequency; evaluate the ratio at each. Report both ratios and state the order of magnitude of the discrepancy.

**Stuck?** Start by computing $k_BT$ in both joules and eV at $T = 5778$ K, then form $x = h\nu/k_BT$ at each frequency before touching the exponential.

*Instructor note: No solution is provided for Part B. Students should complete it independently using the structure of Part A as a model.*

---

## Part C — Completion Problem

**The problem:** Ultraviolet light of wavelength $\lambda = 250$ nm strikes a clean potassium surface. The work function of potassium is $\Phi = 2.3$ eV (from the chapter's work-function table). Find the stopping potential $V_\text{stop}$, and determine whether green light at $\lambda = 546$ nm would eject any electrons at all.

**Step 1 — Convert wavelength to photon energy.** Using the shortcut $hc = 1240$ eV·nm:
$$E = \frac{1240\ \text{eV}\cdot\text{nm}}{250\ \text{nm}} = 4.96\ \text{eV}.$$
*Why:* Einstein's light quanta carry energy $E = h\nu = hc/\lambda$; the shortcut $hc = 1240$ eV·nm folds in $h$ and $c$ so the photon energy comes straight out in eV.

**Step 2 — Identify the relevant energy balance.** A single photon is absorbed by a single electron. The photon energy splits into the work function (energy to escape the metal) plus the leftover kinetic energy:
$$K_\text{max} = h\nu - \Phi = E - \Phi.$$
*Why:* Because each photon "acts alone," there is a one-photon-one-electron event; the work function $\Phi$ is the threshold energy needed to pull the electron free, and only the excess becomes kinetic energy.

**Step 3 — [BLANK] Compute $K_\text{max}$ for the 250 nm light.**

*Your work here:*

_______________________________________________

*Why (your explanation):*

_______________________________________________

**Step 4 — [BLANK] Convert $K_\text{max}$ to the stopping potential.** (Hint: use $eV_\text{stop} = K_\text{max}$.)

*Your work here:*

_______________________________________________

*Why (your explanation):*

_______________________________________________

**Step 5 — Test the green light at $\lambda = 546$ nm.** The photon energy is
$$E_\text{green} = \frac{1240}{546} = 2.27\ \text{eV},$$
which is *below* the potassium work function $\Phi = 2.3$ eV. Since $h\nu < \Phi$, no electron escapes — not one, at any intensity. Sub-threshold photons cannot be added up; each acts alone and none has enough energy.

**Final answer:** For 250 nm light, $K_\text{max} = 4.96 - 2.3 = 2.66$ eV, so $V_\text{stop} = 2.66$ V. For 546 nm green light, no photoemission occurs because $E_\text{green} = 2.27$ eV $< \Phi = 2.3$ eV.

**Self-explanation prompt:** Explain why doubling the *intensity* of the 250 nm beam would double the number of ejected electrons per second but leave $V_\text{stop}$ exactly unchanged — and why this is impossible to reconcile with a wave picture of light.

---

## Part D — Error-Recognition Problem

> **Use this section only after completing Parts A–C.**

**The problem:** A student analyzes the photoelectric effect for sodium ($\Phi = 2.28$ eV) illuminated by $\lambda = 300$ nm ultraviolet light, and is then asked what happens if the light intensity is increased tenfold.

**Step 1 (correct):** Photon energy $E = 1240/300 = 4.13$ eV.

**Step 2 (correct):** Maximum kinetic energy $K_\text{max} = h\nu - \Phi = 4.13 - 2.28 = 1.85$ eV, so $V_\text{stop} = 1.85$ V.

**⚠ Step 3 (contains an error):** "Now increase the intensity by a factor of ten. Intensity is the energy delivered per unit area per unit time, so a tenfold brighter beam delivers ten times more energy to each electron. Therefore each ejected electron now carries $K_\text{max} = 10 \times 1.85 = 18.5$ eV, and the new stopping potential is $V_\text{stop} = 18.5$ V."

**Step 4 (correct-looking):** "The threshold wavelength, where $K_\text{max} = 0$, is $\lambda_0 = hc/\Phi = 1240/2.28 = 544$ nm, so any light above 544 nm ejects nothing."

**Your tasks:**
1. Identify the error in Step 3 and explain why it is wrong.
2. Write the corrected Step 3.
3. State the physical principle that Step 3 violates.
4. Describe a check or test that would catch this class of error.

*Answers:*
1. **The error:** The student treats the photoelectric effect as wave-intensity-dependent — assuming more total energy in the beam means more energy per electron. But intensity controls only the *number* of photons arriving per second, not the energy of each photon. The kinetic energy of each ejected electron depends solely on $h\nu$ (and hence on frequency/wavelength), not on intensity.
2. **Corrected Step 3:** Increasing the intensity tenfold delivers ten times as many photons per second, so ten times as many electrons are ejected per second. But each photon still carries $E = 4.13$ eV, so each electron still has $K_\text{max} = 1.85$ eV and $V_\text{stop}$ remains $1.85$ V.
3. **Principle violated:** Einstein's light-quantum hypothesis — light energy arrives in discrete packets $E = h\nu$, each absorbed by a single electron acting alone. Energy is *not* continuously distributed across the beam in proportion to intensity.
4. **A check to catch this:** Ask whether the predicted quantity should depend on photon *number* or photon *energy*. $V_\text{stop}$ and $K_\text{max}$ depend on per-photon energy (frequency); current/electron-count depends on intensity. Equivalently, sanity-check against the chapter's Millikan result: the slope $dV_\text{stop}/d\nu = h/e = 4.136\times10^{-15}$ V·s is fixed and never depends on intensity.

**Why this error is common:** Classical intuition says "brighter light pushes harder," so students instinctively tie kinetic energy to intensity rather than to the photon energy $h\nu$ — the very intuition the photoelectric effect was the experiment that overturned.

---

## Part E — Transfer Problem

**The problem:** The cosmic microwave background fills all of space with blackbody radiation at $T = 2.725$ K — a system never used in the chapter. (a) At what frequency $\nu_\text{max}$ does its Planck spectrum peak, using Wien's displacement law $\nu_\text{max} = 2.821\,k_BT/h$? (b) At a frequency of $\nu = 1\times10^{12}$ Hz, compute $x = h\nu/k_BT$ and decide whether the Rayleigh–Jeans law would be a good approximation there. (c) Radio astronomers historically measured the CMB at low microwave frequencies (a few GHz) and got sensible answers from the Rayleigh–Jeans law. Use your value of $x$ to explain why classical physics works there even though it failed for the hot poker.

**Hint (use only if stuck after 10 minutes):** Compute $k_BT$ at $T = 2.725$ K first ($\approx 3.76\times10^{-23}$ J). For part (b) a frequency of $10^{12}$ Hz sits near the CMB peak; for the few-GHz radio band, $\nu$ is hundreds of times smaller, so $x \ll 1$ and Rayleigh–Jeans is excellent.

**Reflection prompt:** (1) The same Rayleigh–Jeans law that produces the ultraviolet catastrophe gives correct answers for radio observations of the CMB — what single quantity decides which outcome you get? (2) How does this illustrate the chapter's claim that classical physics "agrees with measurement at long wavelengths" rather than being globally wrong?

---

## Part F — Interleaved Review

**Problem F1.** A platinum surface has the largest work function in the chapter's table, $\Phi = 6.35$ eV. What is the longest wavelength of light (the threshold wavelength $\lambda_0$) that can eject electrons from platinum? Express your answer in nm and state which region of the spectrum it falls in.
*Chapter this draws from: Chapter 1 (Why Classical Physics Failed).*

**Problem F2.** Before any of the quantum results, the chapter recalls that the cavity mode density $8\pi\nu^2/c^3$ "is a geometric fact about standing waves in a box." Using only this mode density and the classical equipartition value $k_BT$ per mode (the framing the chapter uses to *set up* the catastrophe), write the Rayleigh–Jeans spectral energy density and explain in one sentence why integrating it over all frequencies gives infinity.
*Chapter this draws from: the classical-physics framing within Chapter 1 (the Rayleigh–Jeans / equipartition setup that precedes Planck).*

**Problem F3 (discrimination).** A monochromatic source emits light of frequency $\nu = 5\times10^{14}$ Hz onto a metal, and you are told the metal sits in a cavity at temperature $T = 2000$ K. A student is asked for "the relevant energy" and computes $\langle E\rangle = h\nu/(e^{h\nu/k_BT}-1)$, the Planck average energy per mode. Is this the right quantity for predicting whether an electron is ejected from the metal? Decide which physics applies — blackbody thermal occupation or the single-photon photoelectric energy $E = h\nu$ — and justify your choice.
*Note to instructor: intentionally ambiguous — the temperature and cavity language cue blackbody/Planck reasoning, but the question about ejecting an electron is governed by the single-photon energy $E = h\nu$ compared to the work function, not the thermal average occupation. The correct quantity is $E = h\nu = 2.07$ eV.*

**After F1–F3:** Reflect on how you decided which framework each problem required. What surface feature (a temperature, a wavelength, a "stopping potential," the word "catastrophe") cued you toward Planck thermal occupation versus single-photon photoemission? Where did a surface feature mislead you?

---

## Instructor Notes

**Common errors to watch for:**
- Tying photoelectric kinetic energy or stopping potential to intensity rather than to photon energy $h\nu$ (the Part D misconception).
- Forgetting that $x = h\nu/k_BT$ is dimensionless and instead comparing raw frequencies to temperatures, or computing $k_BT$ in the wrong units (mixing J and eV mid-calculation).
- Confusing the spectral peak in frequency with the peak in wavelength — $\nu_\text{max}$ from Wien's law does *not* convert to $\lambda_\text{max}$ via $\lambda = c/\nu$, because $d\nu \neq d\lambda$.

**Signs a student needs to return to the chapter:**
- They claim the ultraviolet catastrophe is a flaw in the mode counting $8\pi\nu^2/c^3$ (it is not — the chapter is explicit that mode counting is correct; the failure is in continuous equipartition).
- They believe a 10,000-watt red lamp can eventually eject electrons from a metal whose threshold lies in the UV (it cannot — sub-threshold photons never add up).

**Scaffolding adjustments:** *If a student struggles with Part A,* have them first tabulate $x/(e^x-1)$ at $x = 0.1, 1, 5, 48$ to *see* the transition from ~1 to ~$10^{-20}$ before plugging in any physical numbers. *If a student finishes Part F quickly,* have them derive Wien's $\nu_\text{max} = 2.821\,k_BT/h$ by setting $\partial u/\partial\nu = 0$ on the Planck distribution and solving the transcendental equation $x = 3(1-e^{-x})$ numerically.

**Domain adaptation note:** In any blackbody or photon problem, the first move is to form the dimensionless ratio of the relevant energy ($h\nu$) to the relevant scale ($k_BT$ for thermal occupation, $\Phi$ for photoemission) — that ratio, not raw magnitudes, tells you which regime and which physics applies.
