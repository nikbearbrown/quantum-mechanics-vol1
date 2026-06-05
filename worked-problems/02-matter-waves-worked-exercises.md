# Worked Exercises: Matter Waves — de Broglie, Davisson–Germer, and the Double Slit
*Chapter 2 of Quantum Mechanics — Volume 1*

> These exercises follow a research-backed sequence: full worked example → matched practice → completion problem → error-recognition → transfer → interleaved review. Each section builds on the previous. Do not skip ahead.

## Prerequisites

- The de Broglie relation $\lambda = h/p$ in its three forms: $\lambda = h/\sqrt{2mK}$ (kinetic energy), $\lambda = h/\sqrt{2meV}$ (accelerating voltage), and the electron shortcut $\lambda_\text{electron} \approx 1.226\ \text{nm}/\sqrt{V}$.
- Bragg's law $2d\sin\theta = n\lambda$ as used to reconstruct the Davisson–Germer peak, and awareness of the inner-potential correction inside a crystal.
- The constants $h = 6.626\times10^{-34}$ J·s, $m_e = 9.109\times10^{-31}$ kg, $1$ eV $= 1.602\times10^{-19}$ J, and the relativistic momentum $p = \sqrt{(K/c)^2 + 2m_eK}$ with $c = 3.0\times10^8$ m/s.

---

## Part A — Full Worked Example

**What this demonstrates:** How to reconstruct the Davisson–Germer diffraction peak from first principles — a parameter-free prediction built from independently measured quantities ($h$, $m_e$, $d$).

**The problem:** Electrons are accelerated through $V = 54$ V (the exact Davisson–Germer voltage) and scatter from the (111) planes of nickel, with plane spacing $d = 0.091$ nm. Compute the de Broglie wavelength, apply Bragg's law to find the first-order Bragg angle, and explain why the predicted angle differs slightly from the observed 50° peak.

**The solution:**

**Step 1 — Apply the de Broglie relation via the momentum.** For a non-relativistic electron accelerated from rest through $V = 54$ V, the kinetic energy is $K = eV = 54$ eV $= 54\times1.602\times10^{-19}$ J $= 8.65\times10^{-18}$ J. The momentum is
$$p = \sqrt{2m_eK} = \sqrt{2(9.109\times10^{-31})(8.65\times10^{-18})} = 3.970\times10^{-24}\ \text{kg·m/s}.$$
*Why:* De Broglie reversed the photon relation $p = h/\lambda$ to assert that any particle of momentum $p$ has wavelength $\lambda = h/p$; for an accelerated electron the momentum comes from $K = p^2/2m$ with $K = eV$. *Check:* The units $\sqrt{\text{kg}\cdot\text{J}} = \sqrt{\text{kg}\cdot\text{kg·m}^2/\text{s}^2} = \text{kg·m/s}$ — correct for momentum.

**Step 2 — Convert momentum to wavelength.**
$$\lambda = \frac{h}{p} = \frac{6.626\times10^{-34}}{3.970\times10^{-24}} = 1.669\times10^{-10}\ \text{m} \approx 0.167\ \text{nm}.$$
*Why:* This is de Broglie's wavelength — a property of the electron's *state of motion*, not its physical size (the classical electron radius is eight orders of magnitude smaller). *Check:* The electron shortcut gives $\lambda \approx 1.226/\sqrt{54} = 1.226/7.35 = 0.167$ nm — exact agreement, confirming the calculation.

**Step 3 — Apply Bragg's law for first-order diffraction.** With $n = 1$, $d = 0.091$ nm:
$$\sin\theta_\text{Bragg} = \frac{n\lambda}{2d} = \frac{0.167}{2\times0.091} = \frac{0.167}{0.182} = 0.918.$$
$$\theta_\text{Bragg} = \arcsin(0.918) \approx 66.6°.$$
*Why:* The electrons diffract from regular atomic planes exactly as X-rays do; constructive interference requires the path-length difference $2d\sin\theta$ to equal a whole wavelength, which is why a wavelength comparable to $d$ is required to see diffraction at all. *Check:* $\sin\theta = 0.918 < 1$, so a real angle exists; if $\lambda$ had exceeded $2d$, no first-order peak would be possible — a useful guard.

**Step 4 — Relate the Bragg angle to the observed scattering angle and identify the discrepancy.** The Bragg angle (measured from the crystal planes) converts in the Davisson–Germer scattering geometry to a scattering angle of roughly 47°, near the observed 50°. The residual difference arises because electrons entering the nickel crystal experience an attractive *inner potential* that slightly accelerates them and shortens their wavelength inside the crystal.
*Why:* The de Broglie wavelength outside the crystal is not the wavelength inside it; the inner potential raises the kinetic energy in the metal, shortening $\lambda$ and shifting the predicted peak. Correcting for it brings prediction and observation into exact agreement. *Check:* The discrepancy is small (a few degrees) and in the right direction — a shorter internal wavelength shifts the Bragg condition slightly, consistent with a modest inner potential.

**Final answer:** $\lambda = 0.167$ nm; the first-order Bragg angle is $\theta_\text{Bragg} \approx 66.6°$, corresponding to a scattering angle near 47°, close to the observed 50°; the small residual is the inner-potential correction, not a failure of de Broglie.

**What made this work:** The central concept is that the de Broglie wavelength $\lambda = h/p$ of a few-tens-of-eV electron lands in the ångström range — precisely the spacing between atoms in a crystal — so Bragg's law, developed for X-rays, applies without modification. The prediction uses three independently measured quantities ($h$, $m_e$, $d$) and a voltage, compared against an angle from an unrelated experiment. A naive approach that forgets the wavelength must be comparable to $d$ — or that uses the *kinetic energy* directly in $\lambda = h/K$ instead of the *momentum* $\lambda = h/p$ — gives a nonsensical wavelength and no diffraction.

**Self-explanation prompt:** Explain in your own words why an electron accelerated through only a few hundred volts can diffract from a crystal, while a baseball cannot — referencing $\lambda = h/p$ and the physical spacing the wave must match.

---

## Part B — Matched Practice Problem

**What this demonstrates:** The same de Broglie + Bragg reconstruction with a different voltage and a different crystal plane.

**The problem:** Electrons are accelerated through $V = 100$ V and scatter from a crystal whose relevant planes have spacing $d = 0.123$ nm. (a) Compute the de Broglie wavelength, both from $\lambda = h/\sqrt{2meV}$ and as a cross-check from the electron shortcut $1.226/\sqrt{V}$. (b) Find the first-order Bragg angle. (c) Identify one physical reason the experimentally observed peak might differ slightly from your Bragg prediction.

Work it in the same four steps: momentum from $K = eV$; wavelength; Bragg angle from $\sin\theta = \lambda/2d$; the inner-potential correction.

**Stuck?** Begin with the shortcut $\lambda \approx 1.226/\sqrt{100} = 0.1226$ nm to get an immediate sanity value, then confirm it with the full $\lambda = h/\sqrt{2meV}$ calculation.

*Instructor note: No solution is provided for Part B. Students should complete it independently using the structure of Part A as a model.*

---

## Part C — Completion Problem

**The problem:** A thermal neutron has kinetic energy $K \approx k_BT$ at room temperature $T = 293$ K. Compute its de Broglie wavelength and compare it to typical crystal plane spacings (0.1–0.3 nm). Use $k_B = 1.38\times10^{-23}$ J/K and $m_n = 1.675\times10^{-27}$ kg.

**Step 1 — Find the kinetic energy.**
$$K = k_BT = (1.38\times10^{-23})(293) = 4.04\times10^{-21}\ \text{J}.$$
*Why:* A thermal neutron is in thermal equilibrium with its surroundings, so its characteristic kinetic energy is set by the thermal scale $k_BT$ — the same scale that governed blackbody occupation in Chapter 1.

**Step 2 — Express the de Broglie wavelength in terms of $K$.** Since $K = p^2/2m$, the momentum is $p = \sqrt{2m_nK}$, and
$$\lambda = \frac{h}{p} = \frac{h}{\sqrt{2m_nK}}.$$
*Why:* This is the kinetic-energy form of the de Broglie relation; for a *neutral* particle there is no accelerating-voltage form, so we must go through the kinetic energy directly.

**Step 3 — [BLANK] Compute the momentum $p = \sqrt{2m_nK}$.**

*Your work here:*

_______________________________________________

*Why (your explanation):*

_______________________________________________

**Step 4 — [BLANK] Compute the wavelength $\lambda = h/p$ and convert to nm.**

*Your work here:*

_______________________________________________

*Why (your explanation):*

_______________________________________________

**Step 5 — Compare to crystal spacings.** Your wavelength should come out near $\lambda \approx 0.15$ nm — squarely inside the 0.1–0.3 nm range of crystal plane spacings, and comparable to the 0.167 nm Davisson–Germer electron wavelength. This is exactly why neutron diffraction is a workable materials-science technique: the thermal-neutron wavelength naturally matches interatomic spacings.

**Final answer:** $p = \sqrt{2m_nK} = \sqrt{2(1.675\times10^{-27})(4.04\times10^{-21})} = 3.68\times10^{-24}$ kg·m/s, giving $\lambda = h/p = 6.626\times10^{-34}/3.68\times10^{-24} = 1.80\times10^{-10}$ m $\approx 0.18$ nm — comparable to crystal spacings.

**Self-explanation prompt:** Explain why a *thermal* neutron (not a fast one) is the right tool for crystal diffraction, connecting the thermal energy scale $k_BT$ to the requirement that $\lambda$ match interatomic spacing.

---

## Part D — Error-Recognition Problem

> **Use this section only after completing Parts A–C.**

**The problem:** A student computes the de Broglie wavelength of an electron in a 200 kV transmission electron microscope, accelerated through $V = 2.0\times10^5$ V.

**Step 1 (correct):** The kinetic energy is $K = eV = 2.0\times10^5$ eV $= 200$ keV $= 3.20\times10^{-14}$ J.

**Step 2 (correct):** The rest energy of the electron is $m_ec^2 = 511$ keV, so $K = 200$ keV is a substantial fraction of $m_ec^2$ — relativistic effects are not negligible here.

**⚠ Step 3 (contains an error):** "I'll use the non-relativistic momentum, since it's simpler: $p = \sqrt{2m_eK} = \sqrt{2(9.109\times10^{-31})(3.20\times10^{-14})} = 7.64\times10^{-23}$ kg·m/s. Then $\lambda = h/p = 6.626\times10^{-34}/7.64\times10^{-23} = 8.67\times10^{-12}$ m $= 0.0087$ nm. This is the microscope's resolution-limiting wavelength."

**Step 4 (correct-looking):** "Since shorter wavelength means finer resolution, the microscope can resolve features down to roughly this wavelength by the Rayleigh criterion."

**Your tasks:**
1. Identify the error in Step 3 and explain why it is wrong.
2. Write the corrected Step 3.
3. State the physical principle that Step 3 violates.
4. Describe a check or test that would catch this class of error.

*Answers:*
1. **The error:** The student used the non-relativistic momentum $p = \sqrt{2m_eK}$ even after Step 2 established that $K = 200$ keV is a large fraction of the rest energy $m_ec^2 = 511$ keV. At these energies the non-relativistic formula understates $p$, which *overstates* $\lambda$. The de Broglie relation $\lambda = h/p$ is still correct — but it must be fed the *relativistic* momentum.
2. **Corrected Step 3:** Use $p = \sqrt{(K/c)^2 + 2m_eK}$:
$$p = \sqrt{\left(\frac{3.20\times10^{-14}}{3.0\times10^8}\right)^2 + 2(9.109\times10^{-31})(3.20\times10^{-14})}.$$
The first term is $(1.067\times10^{-22})^2 = 1.14\times10^{-44}$; the second is $5.83\times10^{-44}$; the sum is $6.97\times10^{-44}$, so $p = 8.35\times10^{-22}$ kg·m/s. Then $\lambda = h/p = 6.626\times10^{-34}/8.35\times10^{-22} = 7.9\times10^{-13}$ m $= 0.0079$ nm — about 9% shorter than the non-relativistic value.
3. **Principle violated:** $\lambda = h/p$ requires the *correct* (relativistic) momentum when the kinetic energy is comparable to the rest energy $m_ec^2$. Using a non-relativistic $p$ where relativistic $p$ is needed is precisely the de Broglie misconception flagged for this topic.
4. **A check to catch this:** Compare $K$ to $m_ec^2 = 511$ keV. If $K \gtrsim 0.1\,m_ec^2$, the relativistic correction exceeds ~1% and must be included. Equivalently, compute both wavelengths and report the percentage difference; a 9% error in a resolution specification is not negligible.

**Why this error is common:** Students reach for the simpler $\lambda = h/\sqrt{2mK}$ by habit and forget to check whether the kinetic energy is small compared to the rest energy — the relativistic regime arrives quietly, with no error message, just a wavelength that is silently 9% too long.

---

## Part E — Transfer Problem

**The problem:** A $\text{C}_{60}$ buckyball (mass $\approx 720$ amu, $1$ amu $= 1.66\times10^{-27}$ kg) effuses from an oven at $T = 900$ K in Zeilinger's diffraction experiment — a mesoscopic object never analyzed in the worked examples above. (a) Estimate the most probable speed using $\tfrac{1}{2}mv^2 = \tfrac{3}{2}k_BT$. (b) Compute the de Broglie wavelength $\lambda = h/(mv)$. (c) The grating had 50 nm slits. By what factor is $\lambda$ smaller than the slit spacing, and what does this tell you about the experimental sensitivity required to see fringes?

**Hint (use only if stuck after 10 minutes):** First find $v = \sqrt{3k_BT/m}$ with $m = 720\times1.66\times10^{-27}$ kg $= 1.20\times10^{-24}$ kg. You should get $v \approx 190$ m/s and $\lambda \approx 2.5$ pm — about 20,000 times smaller than the 50 nm slits.

**Reflection prompt:** (1) The de Broglie relation $\lambda = h/p$ applies to *everything* with momentum; what single quantity in $\lambda = h/p$ makes the buckyball's wavelength so much smaller than an electron's at comparable energy? (2) Why does a wavelength thousands of times smaller than the slit still produce a measurable fringe pattern, and what does that demand of the detector resolution?

---

## Part F — Interleaved Review

**Problem F1.** Compute the de Broglie wavelength of a 70 kg person walking at 1 m/s, and express it as a fraction of a proton radius ($\sim 10^{-15}$ m). Use your result to explain, via Bohr's correspondence principle, why quantum interference is "present but utterly invisible" for human-scale objects.
*Chapter this draws from: Chapter 2 (Matter Waves).*

**Problem F2.** A photon and an electron each have energy 2.0 eV. (a) For the photon, use $E = h\nu$ and $\lambda = c/\nu$ — or equivalently the Chapter 1 shortcut $hc = 1240$ eV·nm — to find the photon wavelength. (b) For the electron, use the de Broglie relation $\lambda = h/\sqrt{2m_eK}$ with $K = 2.0$ eV. (c) Comment on why the two wavelengths differ so dramatically even at the same energy.
*Chapter this draws from: Chapter 1 (Why Classical Physics Failed) — the photon energy relation $E = h\nu$ and the $hc = 1240$ eV·nm shortcut.*

**Problem F3 (discrimination).** An electron and a 2.0 eV photon are each said to "scatter from graphite." For the electron at 54 eV you are asked for its wavelength; for the photon you are reminded of the chapter's Compton formula $\Delta\lambda = \frac{h}{m_ec}(1-\cos\theta)$. A student computes the *Compton wavelength* $h/(m_ec) = 2.426$ pm and reports it as "the de Broglie wavelength of the electron." Decide whether this is correct, and identify which wavelength belongs to which physics.
*Note to instructor: intentionally ambiguous — the Compton setup and the word "electron" cue students to grab $h/(m_ec)$, but the Compton wavelength is a fixed property of the electron's rest mass appearing in photon scattering, NOT the de Broglie wavelength $\lambda = h/p$ of a moving electron (which is 0.167 nm at 54 eV). The two differ by nearly two orders of magnitude.*

**After F1–F3:** Reflect on how you told the three wavelengths apart — de Broglie ($h/p$, depends on motion), photon ($hc/E$), and Compton ($h/m_ec$, fixed by rest mass). Which surface cue (an energy, the word "scatter," a mention of graphite) nearly led you to the wrong formula, and what fixed quantity distinguishes the Compton wavelength from the de Broglie wavelength?

---

## Instructor Notes

**Common errors to watch for:**
- Using kinetic energy in place of momentum: writing $\lambda = h/K$ or $\lambda = h/\sqrt{K}$ instead of $\lambda = h/\sqrt{2mK}$ — a missing factor of $2m$ inside the root.
- Failing to switch to relativistic momentum when $K$ is comparable to $m_ec^2$ (the Part D misconception), silently producing a wavelength that is several percent too long.
- Confusing the de Broglie wavelength $h/p$ with the Compton wavelength $h/m_ec$ — the former depends on the particle's motion, the latter is fixed by its rest mass.

**Signs a student needs to return to the chapter:**
- They describe the de Broglie wavelength as "the physical size of the electron" rather than a property of its state of motion (the chapter is explicit that $\lambda$ exceeds the classical electron radius by eight orders of magnitude).
- They claim a single electron in the Tonomura experiment "really goes through one slit" and the fringes come from electron–electron interaction (the chapter rules this out — there was only ever one electron in the apparatus).

**Scaffolding adjustments:** *If a student struggles with Part A,* have them first verify the electron shortcut $\lambda \approx 1.226/\sqrt{V}$ nm against the full $\lambda = h/\sqrt{2meV}$ at $V = 54$, 100, and 400 V before attempting Bragg's law, so the wavelength step is solid. *If a student finishes Part F quickly,* have them redo the 200 kV TEM calculation and quantify exactly what percentage error in the microscope's resolution specification would result from ignoring the relativistic correction.

**Domain adaptation note:** For any matter-wave problem, the first decision is *which momentum* to use — non-relativistic $\sqrt{2mK}$ for slow particles, relativistic $\sqrt{(K/c)^2 + 2mK}$ when $K$ approaches $mc^2$ — because $\lambda = h/p$ is exact but only as good as the momentum you feed it.
