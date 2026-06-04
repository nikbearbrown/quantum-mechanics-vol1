# Research Notes: Chapter 01 — Why Classical Physics Failed

**Corresponding chapter:** chapters/01-why-classical-physics-failed.md (not yet written)
**Generated:** 2026-06-03

---

## Chapter summary (capability built)

By the end of this chapter the student can explain, with equations, why classical physics predicted infinite energy from a hot object (Rayleigh–Jeans → ultraviolet catastrophe) and why experiments said otherwise (Planck 1900, E = hν). They can also explain why classical wave theory predicted that intensity should control the energy of ejected photoelectrons, why experiments said frequency controls it instead, and how Einstein's 1905 photon hypothesis resolves both puzzles. The chapter introduces the photon as a quantized packet of light energy and gives students their first worked calculation tying frequency, work function, and stopping potential.

---

## A. Conceptual foundations

### 1. The blackbody and the ultraviolet catastrophe

**Explanation.** A blackbody absorbs all incident radiation and re-emits it with a spectral distribution that depends only on its temperature T — not on its composition. Experimentally (Lummer & Pringsheim, late 1890s), the spectral radiance peaks at a wavelength that shifts with temperature (Wien's displacement law: λ_max T = 2.898 × 10⁻³ m·K) and falls to zero at both long and short wavelengths.

Classical derivation (Rayleigh 1900, Jeans 1905): Count electromagnetic modes in a cavity as harmonic oscillators. Each mode gets average thermal energy kT (equipartition). The number of modes per unit volume in frequency interval dν is 8πν²/c³. The energy density spectral distribution is therefore:
$$u(\nu, T) = \frac{8\pi\nu^2}{c^3} k_B T \quad \text{(Rayleigh–Jeans law)}$$
This agrees with experiment at low frequencies (long wavelengths) but diverges as ν → ∞ (short wavelengths): ∫u dν → ∞. This is the **ultraviolet catastrophe** — classical physics predicts a hot object should radiate infinite total energy. No experiment has ever seen this; the error is in the theory.

Planck (December 1900, published 1901): Forced the formula to match data by assuming oscillator energies are not continuous but restricted to discrete multiples of hν, where h = 6.626 × 10⁻³⁴ J·s. The resulting distribution:
$$u(\nu, T) = \frac{8\pi h\nu^3}{c^3} \cdot \frac{1}{e^{h\nu/k_BT} - 1}$$
This reduces to Rayleigh–Jeans at low ν (where e^{hν/kT} ≈ 1 + hν/kT) and falls exponentially at high ν, matching experiment perfectly at all temperatures. Planck later said he used quantization as "a mathematical trick" and expected future experiments to rule it out; they did not.

**Common misconception.** "Planck knew he was discovering quantization of light." He did not. He quantized the energies of the cavity wall oscillators, not the electromagnetic field itself. That step — light as discrete photons — came from Einstein five years later.

**Worked example — Planck vs. Rayleigh–Jeans at T = 3000 K, ν = 3 × 10¹⁵ Hz (UV).**
- hν = (6.626 × 10⁻³⁴)(3 × 10¹⁵) = 1.99 × 10⁻¹⁸ J = 12.4 eV.
- kT = (1.381 × 10⁻²³)(3000) = 4.14 × 10⁻²⁰ J = 0.259 eV.
- hν/kT = 12.4/0.259 ≈ 47.9, so e^{hν/kT} ≈ 7 × 10²⁰.
- Planck u(ν): proportional to ν³ × 1/(e^{hν/kT} − 1) ≈ ν³ × 10⁻²¹ → essentially zero.
- Rayleigh–Jeans u(ν): proportional to ν² × kT → enormous and growing.
- Conclusion: at UV frequencies, classical theory is off by ~21 orders of magnitude for this temperature.

**Sources.**
- [Wikipedia: Ultraviolet catastrophe](https://en.wikipedia.org/wiki/Ultraviolet_catastrophe)
- [Wikipedia: Planck's law](https://en.wikipedia.org/wiki/Planck%27s_law)
- [Britannica: Planck's radiation law](https://www.britannica.com/science/Plancks-radiation-law)
- [LibreTexts: The Ultraviolet Catastrophe](https://chem.libretexts.org/Bookshelves/Physical_and_Theoretical_Chemistry_Textbook_Maps/The_Live_Textbook_of_Physical_Chemistry_(Peverati)/16:_The_Motivation_for_Quantum_Mechanics/16.03:_The_Ultraviolet_Catastrophe)
- _lib_quantum-physics-for-beginners.md (Chapter 3 / "Plank pulls a math trick"): good popular narrative; use for framing only — some details imprecise (calls Planck's Nobel "1919" — actual: 1918, awarded 1919, for "discovery of energy quanta").

---

### 2. The photoelectric effect and the photon

**Explanation.** Hertz (1887): ultraviolet light hitting a metal surface causes it to emit electrons (initially called "sparks"). Subsequent investigations (Lenard, 1902) established the key experimental facts that wave theory cannot explain:
1. Electrons are only emitted if ν > ν_threshold, regardless of intensity. Below threshold, no electrons, ever, no matter how bright the light.
2. Above threshold, the maximum kinetic energy of ejected electrons depends on ν but NOT on intensity. Doubling the brightness doubles the number of electrons, not their energy.
3. Emission is instantaneous (within nanoseconds); classical wave theory predicts a build-up time that, at low intensities, could be seconds or longer.

Einstein (1905, *Annalen der Physik*): proposed that light energy is not continuously distributed but arrives in discrete packets (photons), each with energy E = hν. A single photon of energy hν is absorbed by a single electron; the electron uses some energy (the **work function** Φ) to escape the surface; the rest becomes kinetic energy:
$$K_{\max} = hν - \Phi = eV_{\text{stop}}$$
where V_stop is the stopping potential (the reverse voltage needed to bring the fastest electrons to rest). Einstein won the 1921 Nobel Prize for this work (awarded in 1922).

Millikan (1914–1916) set out to disprove Einstein's equation and ended up confirming it with exquisite precision. He measured V_stop vs. ν for several metals, confirmed linearity, and extracted h/e from the slope — matching Planck's h to within experimental error. The slope of V_stop vs. ν is universally h/e = 4.136 × 10⁻¹⁵ eV·s, regardless of which metal is used.

Work functions of common metals (eV): Cs = 2.1, Na = 2.3, Al = 4.1, Cu = 4.7, Au = 5.1, Pt = 6.35. (These are needed for worked examples and the simulation.)

**Common misconception.** "Brighter light means more energetic electrons." No — intensity controls the rate (number per second) of photon arrivals, not each photon's energy. A very bright red light ejects no electrons from sodium (hν < Φ); a very dim UV lamp ejects electrons immediately (hν > Φ), each with the same maximum kinetic energy as under a bright UV lamp.

**Worked example — stopping potential for UV on sodium.**
- ν = 1.0 × 10¹⁵ Hz (UV, λ ≈ 300 nm).
- E_photon = hν = (6.626 × 10⁻³⁴)(1.0 × 10¹⁵) = 6.626 × 10⁻¹⁹ J = 4.14 eV.
- Work function of Na: Φ = 2.28 eV.
- K_max = 4.14 − 2.28 = 1.86 eV.
- Stopping potential: V_stop = K_max / e = 1.86 V.
- Check: if ν is halved to 5 × 10¹⁴ Hz (visible green), E_photon = 2.07 eV < Φ → no emission.

**Sources.**
- [Einstein's Nobel Prize (1921)](https://www.nobelprize.org/prizes/physics/1921/einstein/facts/)
- [APS Physics: Millikan's Measurement of Planck's Constant (1916)](https://link.aps.org/doi/10.1103/Physics.18.12)
- [Chemistry LibreTexts: Photoelectric Effect](https://chem.libretexts.org/Courses/BethuneCookman_University/B-CU:CH-331_Physical_Chemistry_I/CH-331_Text/CH-331_Text/01:_The_Dawn_of_the_Quantum_Theory/1.3:_Photoelectric_Effect_Explained_with_Quantum_Hypothesis)
- _lib_quantum-physics-for-beginners.md (Chapter 6, "The True Secret of Light"): accurate narrative of Einstein/Hertz/Lenard/Compton sequence; use for framing.
- Townsend text §1.3 ("Photons: The Particle Nature of Light") — Townsend's Chapter 1 covers photoelectric and Compton effects before switching to single-photon anticoincidence experiments.

---

### 3. Wave–particle duality of light (pre-matter-waves)

**Explanation.** After Einstein 1905 and Compton 1923 (X-ray scattering from graphite valence electrons, Δλ = (h/m_e c)(1 − cos θ) — Compton wavelength h/m_e c = 2.426 × 10⁻¹² m), it was unavoidable: light has both wave properties (Young's double-slit, interference, diffraction — well-established from 1801) and particle properties (photoelectric effect, Compton scattering). The modern view is that a photon travels as a probability amplitude obeying Maxwell's equations; upon detection it localizes like a particle.

**Common misconception.** "Wave-particle duality means light is sometimes a wave and sometimes a particle, switching between them." Modern quantum mechanics does not support this toggling picture. The wave function (or probability amplitude) is always the fundamental description; the "particle" appearance is the result of a detection/measurement event.

**Worked example.** Compton scattering: an X-ray of wavelength λ = 0.071 nm (≈17.5 keV) scatters off a free electron at θ = 90°. Wavelength shift: Δλ = (h/m_e c)(1 − cos 90°) = 2.426 × 10⁻¹² m = 0.00243 nm. Scattered wavelength: 0.0734 nm. The electron recoil energy: E_recoil = hc/λ − hc/λ' ≈ 0.49 keV. Compton received the Nobel Prize in 1927 for this.

**Sources.** [Wikipedia: Compton scattering](https://en.wikipedia.org/wiki/Compton_scattering); _lib_quantum-physics-for-beginners.md Chapter 6.

---

### 4. Planck's constant h — the central constant of quantum mechanics

**Explanation.** h = 6.62607015 × 10⁻³⁴ J·s (exact, SI 2019 redefinition). ℏ = h/2π = 1.054571817 × 10⁻³⁴ J·s. In eV units: h = 4.136 × 10⁻¹⁵ eV·s, ℏ = 6.582 × 10⁻¹⁶ eV·s. hc = 1240 eV·nm — an extremely useful combination (photon energy from wavelength in nm: E = 1240/λ(nm) eV).

h sets the scale at which quantum behavior becomes important. For objects where action scales (energy × time, or momentum × length) are comparable to h, quantum effects dominate. For macroscopic objects, h is negligible.

**Common misconception.** "Planck's constant has units of energy." It has units of action (energy × time = momentum × length = J·s). Energy is hν where ν is frequency; h alone is not an energy.

**Sources.** NIST CODATA 2018 values: [physics.nist.gov/constants](https://physics.nist.gov/cgi-bin/cuu/Value?h); Townsend text, front matter constants table (OCR confirmed: h = 6.626 × 10⁻³⁴ J·s = 4.136 × 10⁻¹⁵ eV·s; ℏ = 1.055 × 10⁻³⁴ J·s = 6.582 × 10⁻¹⁶ eV·s).

---

### 5. What "quantization" means physically

**Explanation.** Classical oscillators in a thermal field can have any energy continuously. Quantization means the oscillator can only gain or lose energy in chunks of hν. At high temperatures (kT >> hν) the chunks are negligible compared to thermal energy, so classical statistics recover — this is why Rayleigh–Jeans works at long wavelengths. At low temperatures or high frequencies (kT << hν), the system cannot "afford" to populate even one quantum, so the energy density drops exponentially — this cures the ultraviolet catastrophe. The ratio hν/kT is the critical parameter.

**Common misconception.** "Quantization means everything comes in indivisible units forever." Quantization is a constraint on *exchanges* of energy, not on the state of the field. A classical electromagnetic wave with many photons can still look continuous; quantization only becomes obvious in the discrete-photon regime.

**Sources.** Planck's law Wikipedia article; Britannica Planck's radiation law.

---

## B. Domain examples and cases

### Case 1 — The Sun as a blackbody
The Sun's surface is approximately T = 5778 K. Wien's law: λ_max = 2.898 × 10⁻³ / 5778 ≈ 501 nm — peak in the green part of the visible spectrum. This matches the known solar spectrum peak and is why evolution tuned human color vision to this region. The Rayleigh–Jeans law predicts infinite UV intensity from the Sun — manifestly wrong.

### Case 2 — Millikan's 1916 photoelectric measurement
Millikan used a freshly scraped sodium surface in a vacuum. His plot of V_stop vs. ν for different frequencies of light gave a straight line. Slope = h/e = 4.124 × 10⁻¹⁵ V·s (within 0.5% of the accepted h/e). This measurement convinced the Nobel committee that Einstein's 1905 equation was correct — Millikan personally doubted the photon picture but the data were unambiguous. Reference: Millikan, R.A. (1916). "A direct photoelectric determination of Planck's h." *Phys. Rev.* 7(3), 355–388.

### Case 3 — Compton scattering (1923)
Arthur Holly Compton at Washington University, St. Louis. X-rays scattered from graphite. Observed wavelength shift consistent with elastic photon-electron collision, not with classical wave scattering (which would predict no wavelength shift). Nobel Prize 1927. Published: Compton, A.H. (1923). "A quantum theory of the scattering of X-rays by light elements." *Phys. Rev.* 21(5), 483–502.

### Failure case — Classical explanation of the photoelectric threshold
Classical wave theory predicts that at any frequency, sufficient intensity should eventually deliver enough energy to eject an electron (by "bathing" the surface). This prediction is unambiguously falsified: below the threshold frequency, no electrons are emitted at any intensity, ever, even after days of illumination. This is the clearest single experimental refutation of classical wave optics in the domain.

---

## C. Connections and dependencies

**Prerequisites.** Students need: electromagnetic waves (frequency, wavelength, ν = c/λ), basic energy concepts (kinetic energy, potential energy, eV as a unit), and Chapter 0's simulation workflow. No prior QM required.

**Unlocks.**
- Chapter 2 (matter waves): de Broglie's 1924 argument uses E = hν from this chapter.
- Chapter 3 (wave function): the Born rule for |ψ|² as probability density is the extension of the photon probability idea introduced here.
- Chapter 5 (operators/commutators): the quantization condition is the prototype of eigenvalue problems.

**Adjacent chapters.** Ch 1 and Ch 2 form a natural pair: Ch 1 is "light has particle properties," Ch 2 is "particles have wave properties." Together they establish wave–particle duality before the Schrödinger equation is introduced in Ch 3.

---

## D. Current state of the field

**Settled.** The photoelectric effect, blackbody spectrum, and Compton scattering are textbook physics — no ambiguity. h is now an exact defined constant (2019 SI redefinition). The history (Planck 1900, Einstein 1905, Millikan 1916, Compton 1923) is well-documented and not contested.

**Contested / ongoing.** The interpretation of wave–particle duality remains actively debated among physicists and philosophers (Copenhagen, many-worlds, pilot-wave, QBism), but the experimental facts are not in dispute. This chapter should not wade into interpretational debates — save for Ch 3+.

**Key references (verified).**
- Planck, M. (1901). "Ueber das Gesetz der Energieverteilung im Normalspectrum." *Ann. d. Phys.* 4, 553. (The original blackbody paper.)
- Einstein, A. (1905). "Über einen die Erzeugung und Verwandlung des Lichtes betreffenden heuristischen Gesichtspunkt." *Ann. d. Phys.* 17, 132–148. (The photoelectric effect paper.)
- Millikan, R.A. (1916). "A direct photoelectric determination of Planck's h." *Phys. Rev.* 7(3), 355–388. [doi:10.1103/PhysRev.7.355]
- Compton, A.H. (1923). "A quantum theory of the scattering of X-rays." *Phys. Rev.* 21, 483. [doi:10.1103/PhysRev.21.483]
- [APS Physics Milestones: Millikan 1916](https://link.aps.org/doi/10.1103/Physics.18.12) — good summary.

**Recent developments.** The 2019 SI redefinition made h exact at 6.62607015 × 10⁻³⁴ J·s, ending the era of experimental determination of h. This is a clean pedagogical fact to note in the chapter.

---

## E. Teaching considerations

**Where students get stuck.**
1. **The threshold confusion:** students think increasing intensity should eventually knock out electrons even below threshold. The corpuscular/photon picture must be drilled: one photon → one electron; if hν < Φ, no single photon can do the job regardless of how many arrive.
2. **The "h" unit confusion:** students confuse h (J·s) with energy (J). Emphasize: h is action, hν is energy.
3. **Planck vs. Einstein scope:** students conflate "Planck quantized the oscillators" with "Einstein said light itself is quantized." These are different claims; Planck resisted Einstein's step for years.
4. **eV arithmetic:** students struggle converting between J and eV mid-calculation. The trick hc = 1240 eV·nm should be introduced here as a computational shortcut.

**Analogies.**
- The threshold effect is like a coin-operated turnstile: coins (photons) must individually be large enough (hν > Φ) to turn the mechanism. Pouring in more small coins (high intensity, low frequency) never works — each coin is still too small. (Analogy from standard QM pedagogy; not a citation needed.)
- Quantization as "staircase" vs. classical "ramp": energy can only change in discrete steps hν, not continuously. At high T, the steps are tiny compared to kT and the staircase looks like a ramp — classical limit recovered.

**Exercises (with Bloom level).**
- **Remember:** State the two experimental facts about the photoelectric effect that classical wave theory cannot explain. (Bloom: Remember)
- **Understand:** Explain in words why the Rayleigh–Jeans law diverges at high frequencies. What physical assumption causes the divergence? (Bloom: Understand)
- **Apply (calculation):** Light of wavelength 200 nm strikes a copper surface (Φ = 4.7 eV). Calculate the photon energy, the maximum kinetic energy of ejected electrons, and the stopping potential. (Bloom: Apply)
- **Apply (calculation):** At T = 6000 K, compute the ratio u_Planck(ν)/u_RJ(ν) at ν = 3 × 10¹⁵ Hz. By what factor does Planck predict less energy than Rayleigh–Jeans? (Bloom: Apply)
- **Analyze:** In Millikan's experiment, why does the slope of the V_stop vs. ν graph give h/e, not h? What additional measurement is needed to extract h alone? (Bloom: Analyze)
- **LLM Exercise — blackbody simulation:** Build a D3 v7 simulation showing u(ν, T) for both Planck and Rayleigh–Jeans on the same axes, with a slider for T (1000–10000 K). Add a slider for a vertical cursor showing hν/kT. The two curves should agree at low ν and diverge at high ν. Verification: at T = 5778 K, the Planck peak should be near ν ≈ 6 × 10¹⁴ Hz (λ ≈ 500 nm). (Bloom: Create)

---

## F. Library files relevant to this chapter

- `/Users/bear/Documents/CoWork/bear-textbooks/books/quantum-mechanics-vol1/pantry/_lib_quantum-physics-for-beginners.md` — Chapter 3 ("Plank pulls a math trick") and Chapter 6 ("The True Secret of Light"): popular narrative of blackbody problem and photoelectric effect. Accurate enough for framing and hook material; too imprecise for equation-level details (use Wikipedia/Britannica/original papers for those).
- Townsend text §1.3 (photons, particle nature of light) and §1.4 (probability and quantum nature) — located by grep; OCR confirms chapter titles. Exact page content requires reading the file at those sections (grep found section headers at lines 184–185 of the txt).

---

## G. Gaps and flags

**FLAG — Hertz discovery date precision.** The popular source says 1887 for Hertz discovering the photoelectric effect. This is correct: H.R. Hertz, *Ann. d. Phys.* 31 (1887), 983. Confirm this date in any standard history source before writing.

**FLAG — Millikan Nobel date.** The Nobel Prize in Physics for Millikan was awarded in 1923 "for his work on the elementary charge of electricity and on the photoelectric effect." Do not confuse with Einstein's 1921 Nobel (photoelectric theory) or Compton's 1927 Nobel (Compton scattering). All three within six years — a striking fact for the hook.

**GAP — Simulation for this chapter.** No LLM Exercise prompt is specified in the existing library files for Ch 1. The chapter author should write a blackbody/Planck vs. Rayleigh-Jeans simulation prompt using the four-move structure from Ch 0. A photoelectric-effect simulation (stopping potential slider vs. frequency, variable metal work function) is a second natural exercise. Both should be added.

**GAP — Compton scattering treatment.** This chapter covers the UV catastrophe and photoelectric effect as the two "classical failures." Compton scattering (1923) is a third classical failure and is mentioned in the Townsend text Ch 1 and the popular lib source. The chapter author should decide whether to treat Compton here or defer to a sidebar — it requires relativistic kinematics and may clutter the main narrative.

**GAP — Wien's displacement law.** λ_max T = 2.898 × 10⁻³ m·K is the experimental relationship that preceded Planck; it should be stated as a given and then shown to follow from ∂B(λ,T)/∂λ = 0 applied to the Planck formula. This derivation is a good exercise. Current notes state the law but flag that the chapter needs it explicitly.
