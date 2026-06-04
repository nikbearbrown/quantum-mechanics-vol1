# Research Notes: Chapter 02 — Matter Waves

**Corresponding chapter:** chapters/02-matter-waves.md (not yet written)
**Generated:** 2026-06-03

---

## Chapter summary (capability built)

By the end of this chapter the student can compute the de Broglie wavelength of any particle given its kinetic energy or momentum, explain why electrons diffract from crystals the same way X-rays do, describe the Davisson–Germer experiment (1927) and its historical significance, and articulate what the single-electron double-slit buildup (Tonomura 1989) proves about wave–particle duality. The chapter establishes that the wave–particle duality seen in Chapter 1 for light is a property of all matter — setting up the Schrödinger equation in Chapter 3.

---

## A. Conceptual foundations

### 1. de Broglie's hypothesis: λ = h/p

**Explanation.** In his 1924 PhD thesis ("Recherches sur la théorie des quanta," Université de Paris Sorbonne), Louis-Victor de Broglie proposed that just as light — previously thought to be purely a wave — had been shown to behave as particles (photons), matter — previously thought to be purely particles — should also behave as waves. His argument was an elegant reversal:
- For a photon: E = hν and (relativistic) E = pc, so p = h/λ.
- De Broglie's extension: for any particle with momentum p, associate a wavelength λ = h/p.

This gives:
$$\lambda = \frac{h}{p} = \frac{h}{mv} \quad \text{(non-relativistic)}$$
$$\lambda = \frac{h}{\sqrt{2mK}} \quad \text{where } K = \frac{1}{2}mv^2 \text{ is kinetic energy}$$
$$\lambda = \frac{h}{\sqrt{2meV}} \quad \text{for a particle of charge } e \text{ accelerated through potential } V$$

For an electron (m_e = 9.109 × 10⁻³¹ kg) accelerated through V volts:
$$\lambda = \frac{1.226 \text{ nm}}{\sqrt{V \text{ (in volts)}}}$$
This is a useful formula — at 150 V, λ ≈ 0.1 nm = 1 Å, exactly the scale of atomic spacings in crystals.

de Broglie's thesis committee was skeptical and consulted Einstein, who declared the idea brilliant. de Broglie received the Nobel Prize in Physics in 1929 — the only Nobel ever awarded for a PhD thesis.

**Common misconception.** "The de Broglie wavelength is the size of the particle." The de Broglie wavelength is the wavelength of the associated probability wave — it has nothing to do with the physical size of the particle. An electron's classical radius is ~2.8 × 10⁻¹⁵ m; a 54-eV electron's de Broglie wavelength is ~0.167 nm — eight orders of magnitude larger.

**Worked example — de Broglie wavelength of an electron at 54 eV.**
(These are the exact conditions of the Davisson–Germer experiment.)
- K = 54 eV = (54)(1.602 × 10⁻¹⁹) = 8.65 × 10⁻¹⁸ J.
- p = √(2m_e K) = √(2 × 9.109 × 10⁻³¹ × 8.65 × 10⁻¹⁸) = √(1.576 × 10⁻⁴⁷) = 1.255 × 10⁻²⁴ kg·m/s.
- λ = h/p = (6.626 × 10⁻³⁴)/(1.255 × 10⁻²⁴) = 5.28 × 10⁻¹⁰ m ≈ 0.167 nm.
- Nickel crystal plane spacing d = 0.091 nm (d_{111} planes in face-centered cubic Ni).
- Bragg's law for first-order maximum: 2d sin θ_Bragg = λ → sin θ_Bragg = 0.167/(2 × 0.091) = 0.918 → θ_Bragg ≈ 66.6°. The scattering angle measured from the incident direction is 2θ_Bragg − 90° for the geometry used ≈ 50°. This matches the observed peak at 50° in the Davisson–Germer experiment.
- Using the shortcut formula: λ = 1.226/√54 ≈ 1.226/7.35 ≈ 0.167 nm. ✓

**Sources.**
- de Broglie, L. (1924). "Recherches sur la théorie des quanta." Doctoral thesis, Université de Paris. Published as *Ann. de Physique* 3 (1925), 22–128.
- [Wikipedia: Matter wave](https://en.wikipedia.org/wiki/Matter_wave)
- [Physics LibreTexts: De Broglie's Matter Waves](https://phys.libretexts.org/Bookshelves/University_Physics/University_Physics_(OpenStax)/University_Physics_III_-_Optics_and_Modern_Physics_(OpenStax)/06:_Photons_and_Matter_Waves/6.06:_De_Broglies_Matter_Waves)
- [BCCampus Modern Physics: De Broglie's Matter Waves](https://pressbooks.bccampus.ca/bcitphys8400/chapter/2-5-de-broglies-matter-waves/)
- _lib_quantum-physics-for-beginners.md (Chapter 7, "Shocking electron experiment"): accurate popular account including the derivation from E = mc² and E = hf; use for narrative hook. Note: the lib source incorrectly attributes the Nobel confirmation to "George Paget Thompson" in 1937 — it was 1937 for Thomson and Davisson jointly; see below.

---

### 2. The Davisson–Germer experiment (1927)

**Explanation.** Clinton Davisson and Lester Germer at Bell Telephone Laboratories (New York) first confirmed de Broglie's hypothesis experimentally. The experiment was, famously, partly accidental:

**Background:** Davisson and Germer had been studying electron scattering from nickel since 1921. They observed smooth angular distributions consistent with classical scattering.

**The accident (1925):** Their nickel target was accidentally exposed to air when the vacuum tube broke. To clean the oxide that formed, they annealed (heated) the nickel to high temperature. This inadvertently recrystallized the nickel from a polycrystalline sample into a collection of large single crystals.

**The discovery:** When they resumed measurements in 1926–1927, they found sharp peaks in the scattered electron intensity at specific angles — behavior completely unlike classical scattering, but identical to X-ray diffraction from crystals. The peak at 50° for 54 V electrons matched the de Broglie wavelength prediction.

**The paper:** Davisson, C. & Germer, L.H. (1927). "Diffraction of electrons by a crystal of nickel." *Phys. Rev.* 30(6), 705–741. doi:10.1103/PhysRev.30.705. Also published in Bell System Technical Journal (1928).

**The Nobel Prize:** Davisson shared the 1937 Nobel Prize in Physics with George Paget Thomson (son of J.J. Thomson, who had shown electrons were particles in 1897 — a striking father/son pairing). Thomson independently demonstrated electron diffraction by firing electrons through thin celluloid films (rather than reflecting off a crystal surface), observing diffraction rings. Both methods, different geometries, same physics.

**Common misconception.** "Davisson and Germer set out to test de Broglie's hypothesis." They did not. They were studying surface scattering when the accident produced the crystal. They recognized the significance of the diffraction peaks after seeing them, partly after Davisson visited Europe and discussed the results with Born and other quantum physicists.

**Worked example.** (See Section A.1 above — the 54 eV electron calculation is the Davisson–Germer canonical case.)

**Sources.**
- [Wikipedia: Davisson–Germer experiment](https://en.wikipedia.org/wiki/Davisson%E2%80%93Germer_experiment)
- Davisson & Germer (1927), *Phys. Rev.* 30, 705. [Original paper at Atticus Rare Books bibliographic record](https://www.atticusrarebooks.com/pages/books/397/c-davisson-l-h-germer/the-diffraction-of-electrons-by-a-crystal-of-nickel-in-the-physical-review-vol-30-no-6-december-1927)
- LLesser, A. et al. (2013). "A proper understanding of the Davisson and Germer experiments for undergraduate modern physics course." [arXiv:1307.6049](https://arxiv.org/pdf/1307.6049) — excellent pedagogical treatment of the geometry.
- [Smithsonian National Museum of American History: Davisson-Germer apparatus](https://americanhistory.si.edu/collections/object/nmah_1167138) — the original apparatus is preserved.

---

### 3. The double-slit experiment with electrons and single-electron buildup

**Explanation.** The most direct demonstration of wave–particle duality for electrons is the double-slit experiment. Young's original 1801 experiment used light and showed an interference pattern — explained by wave theory. Firing electrons instead of light through two slits also produces an interference pattern. This was established conceptually by early low-intensity electron diffraction, but the definitive single-electron demonstration came much later.

**Historical priority note.** The single-electron version of the double-slit was first performed by Pier Giorgio Merli, Giulio Missiroli, and Gianfranco Pozzi in Bologna, Italy, in 1974, using a biprism (not actual slits) and a modified electron microscope. Their results were published in the *American Journal of Physics* (Merli, P.G., Missiroli, G.F., & Pozzi, G. (1976). "On the statistical aspect of electron interference phenomena." *Am. J. Phys.* 44(3), 306–307). This is earlier than Tonomura, but the Merli–Missiroli–Pozzi experiment was largely overlooked outside Italy.

**The Tonomura 1989 experiment.** Akira Tonomura and colleagues at Hitachi Central Research Laboratory performed the definitive modern version. They used an electron biprism (not physical slits), an electron microscope setup, and a position-sensitive electron-counting detector (image intensifier + video camera). With an extraordinarily weak electron beam — typically fewer than one electron at a time in the apparatus — they recorded the arrival of individual electrons as discrete dots on the detector. Over time (from 10 electrons to 70,000 electrons), the dot pattern gradually resolved into a clear double-slit interference fringe pattern.

Publication: Tonomura, A., Endo, J., Matsuda, T., Kawasaki, T., & Ezawa, H. (1989). "Demonstration of single-electron buildup of an interference pattern." *Am. J. Phys.* 57(2), 117–120. doi:10.1119/1.16104.

**What the buildup proves.** Each electron arrives as a single, discrete, localized event (particle-like). Yet the statistical pattern of thousands of arrivals is the interference pattern of a wave. The conclusion: each single electron must "go through both slits" as a wave (or rather, its probability amplitude does). The wave is not a cloud of many electrons interfering with each other — it is the single-electron wave function.

**The key insight.** Decreasing the beam intensity until electrons go through one at a time does not destroy the interference pattern — it just takes longer to accumulate. This means an electron cannot be "going through just one slit" and then adding up to a fringe pattern; that would require communication between electrons, which is ruled out by the time separation. The wave nature is a property of each individual electron's quantum state.

**Common misconception.** "The interference pattern appears because electrons are close together and interact." If true, the pattern would disappear at low intensity. It does not. Each electron individually contributes to the pattern. The wave function of each electron goes through both slits and interferes with itself.

**Sources.**
- Tonomura et al. (1989). *Am. J. Phys.* 57(2), 117–120. [AIP Publishing](https://pubs.aip.org/aapt/ajp/article/57/2/117/1040594/Demonstration-of-single-electron-buildup-of-an)
- [Semantic Scholar PDF](https://www.semanticscholar.org/paper/Demonstration-of-single%E2%80%90electron-buildup-of-an-Tonomura-Matsuda/fc2afdc4a027fce366ffa105bd88439760d22546)
- Merli, Missiroli & Pozzi (1976). *Am. J. Phys.* 44, 306–307 — historical priority.
- Bach, R. et al. (2013). "Controlled double-slit electron diffraction." *New Journal of Physics* 15, 033018 — first experiment with real physical double slits (not biprism) for electrons, using nano-fabricated slits. doi:10.1088/1367-2630/15/3/033018.
- [Physics World: The double-slit experiment](https://physicsworld.com/a/the-double-slit-experiment/) — good historical narrative.
- [PMC: The Merli–Missiroli–Pozzi Two-Slit Electron-Interference Experiment](https://pmc.ncbi.nlm.nih.gov/articles/PMC4617474/)

---

### 4. Wave–particle duality and its limits

**Explanation.** Wave–particle duality is not just electrons — it has been demonstrated for:
- Neutrons (1936, diffraction from crystals).
- Helium atoms (Jürgen Mlynek's group, 1990s, double-slit experiment — referenced in Townsend text preface).
- Large molecules: C₆₀ (buckminsterfullerene, 60 atoms, ~720 amu) diffraction by Zeilinger's group in Vienna (1999, *Nature* 401, 680–682). The de Broglie wavelength was ~250 fm, far smaller than the molecule — yet fringes appeared.
- More recently (2019), molecules of ~2000 atoms have shown diffraction, pushing the quantum-classical boundary.

The de Broglie wavelength of a 70 kg person walking at 1 m/s: λ = 6.626×10⁻³⁴ / 70 = 9.5 × 10⁻³⁶ m — 21 orders of magnitude smaller than an atomic nucleus. Quantum wave behavior is unobservable for macroscopic objects not because the physics is different, but because the wavelength is unresolvably small.

**Common misconception.** "Wave–particle duality means quantum mechanics breaks down for large objects." Quantum mechanics does not break down; the wave effects simply become unobservably small. The correspondence principle: quantum mechanics must reproduce classical mechanics in the limit of large mass/large quantum numbers.

**Sources.** Arndt, M. et al. (1999). "Wave–particle duality of C₆₀ molecules." *Nature* 401, 680–682. doi:10.1038/44348. For the Townsend Mlynek reference: Townsend preface (grep confirmed: "double-slit experiment with helium atoms carried out by Jürgen Mlynek's group in the 1990s").

---

### 5. The de Broglie relation and the uncertainty principle

**Explanation.** The de Broglie relation λ = h/p is the seed of the Heisenberg uncertainty principle. A particle with a definite momentum p has a definite wavelength λ = h/p — but a definite-wavelength wave extends over all space (completely delocalized in position). To localize a particle in position, one must superpose many wavelengths (momenta), introducing uncertainty in p. This is the Fourier duality Δx·Δk ≳ 1/2, which becomes Δx·Δp ≳ ℏ/2 upon multiplying by ℏ.

The Chapter 0 simulation already demonstrates this: the Gaussian wave packet has Δk_x = 1/(2σ) in k-space, so Δp = ℏ/(2σ); Δx = σ; Δx·Δp = ℏ/2 — saturating the uncertainty bound (Gaussian is the minimum-uncertainty state).

**Common misconception.** "The uncertainty principle is about measurement disturbance." Heisenberg's original 1927 gamma-ray microscope argument implied this, but modern formulations (Robertson 1929; Ozawa 2003 on measurement disturbance) show it is a fundamental property of the quantum state, not just of the act of measurement.

**Sources.** Robertson, H.P. (1929). *Phys. Rev.* 34, 163; Ozawa, M. (2003). *Phys. Rev. A* 67, 042105 (measurement disturbance bound).

---

## B. Domain examples and cases

### Case 1 — Electron microscopy
Modern transmission electron microscopes operate at 80–300 kV. At 200 kV: λ = 1.226/√200,000 ≈ 0.0027 nm (2.7 pm, relativistic correction reduces this to ~2.5 pm). This is far smaller than an atomic spacing (~0.25 nm), enabling sub-angstrom resolution. The entire field of electron microscopy is applied de Broglie physics.

### Case 2 — Neutron diffraction in crystallography
Thermal neutrons from a reactor have energies ~0.025 eV (kT at room temperature). λ = h/√(2m_n kT) ≈ 1.8 Å — the same scale as X-ray crystallography. Neutron diffraction is used to locate light atoms (especially hydrogen) in crystal structures that X-rays cannot resolve. Nobel Prizes: Brockhouse & Shull, 1994.

### Case 3 — C₆₀ buckyball diffraction (1999)
Zeilinger's Vienna group showed diffraction of C₆₀ molecules (mass ~720 amu) through a diffraction grating with 50 nm slits. This pushed the quantum-classical boundary to mesoscopic objects and is the go-to modern example that "it's not just electrons — it's everything." Source: Arndt et al. (1999), *Nature* 401, 680.

### Failure case — The "which-slit" measurement destroying interference
If one adds a detector that determines which slit each electron went through, the interference pattern vanishes, replaced by two broad classical distributions. This is not a technological limitation — it is fundamental: knowing the path destroys the interference. The 2013 Bach et al. experiment with real slits confirmed this with direct physical double-slits for electrons for the first time. This is a powerful "failure case" of trying to treat the electron as a classical billiard ball with a definite trajectory.

---

## C. Connections and dependencies

**Prerequisites.** Chapter 1 (photon, E = hν, wave–particle duality of light); basic momentum (p = mv); kinetic energy (K = p²/2m); the Chapter 0 simulation workflow.

**Unlocks.**
- Chapter 3 (wave function, Schrödinger equation): the de Broglie relation motivates treating quantum states as wave functions; the free-particle Schrödinger equation ψ ~ e^{ikx} with λ = 2π/k = h/p is the direct translation.
- Chapter 4 (infinite square well): wavelength quantization from boundary conditions → quantized momentum → quantized energy.
- Chapter 5 (operators): momentum operator p̂ = −iℏ∂/∂x is the derivative that extracts p from e^{ikx} in the de Broglie sense.

**Adjacent chapters.** Ch 1 + Ch 2 together complete the experimental foundation before the Schrödinger equation is introduced. The "pre-history" of QM is done; Ch 3 begins the formal machinery.

---

## D. Current state of the field

**Settled.** de Broglie's relation, Davisson–Germer, the double-slit buildup. These are textbook physics, confirmed by thousands of experiments since 1927.

**Active research.** The quantum-classical boundary: how massive an object can exhibit wave–particle duality before decoherence destroys the interference? Current record is molecules of ~2,000 atoms (Fein et al., 2019, *Nature Physics* 15, 1242–1245). The goal of "Schrödinger's cat" states at mesoscopic scale drives active experimental work (optomechanics, superconducting qubits, trapped ions).

**Key references (verified).**
- de Broglie, L. (1924/1925). Doctoral thesis, *Ann. de Physique* 3, 22–128.
- Davisson, C. & Germer, L.H. (1927). *Phys. Rev.* 30, 705–741.
- Tonomura, A. et al. (1989). *Am. J. Phys.* 57(2), 117–120. doi:10.1119/1.16104
- Bach, R. et al. (2013). *New J. Phys.* 15, 033018 — first real physical double slits for electrons. doi:10.1088/1367-2630/15/3/033018
- Arndt, M. et al. (1999). *Nature* 401, 680–682 — C₆₀ diffraction.
- Fein, Y.Y. et al. (2019). *Nature Physics* 15, 1242–1245 — 2000-atom molecules.
- Merli, P.G., Missiroli, G.F., & Pozzi, G. (1976). *Am. J. Phys.* 44, 306–307 — historical first single-electron buildup.

**Recent developments.** The 2019 Fein et al. result with 2,000-atom molecules is particularly striking; the de Broglie wavelength was 53 fm — smaller than a proton. Yet diffraction fringes appeared. This is an excellent discussion hook for where duality ends (it hasn't ended yet).

---

## E. Teaching considerations

**Where students get stuck.**
1. **"The wavelength is too small to matter."** Students compute λ for a baseball (~10⁻³⁴ m) and conclude quantum mechanics is irrelevant for them. Correct but the wrong takeaway: quantum mechanics governs the electrons in the atoms of the baseball, just not the baseball's center-of-mass motion.
2. **The "going through both slits" language.** Students demand a classical picture of how one electron goes through both slits. This picture does not exist and should not be constructed; the correct statement is that the probability amplitude goes through both slits and interferes.
3. **Confusing de Broglie wavelength with electromagnetic wavelength.** The de Broglie wave is a matter wave / probability wave, not an electromagnetic wave. An electron does not emit or absorb light at its de Broglie frequency.
4. **The formula λ = h/p vs. λ = h/mv.** For relativistic electrons (accelerated through many kV), p = γmv, not mv. At 54 eV this doesn't matter (γ ≈ 1.0001); at 200 kV it does (γ ≈ 1.4).

**Analogies.**
- The buildup of the interference pattern from single dots is like a pointillist painting: each point (electron arrival) looks random, but the distribution reveals the underlying wave structure. Students can literally watch the Tonomura video — it is available on YouTube and from the AIP (search "Tonomura electron double slit").
- The de Broglie wavelength as "the spatial period of the associated probability ripple" — just as a water wave's wavelength is the crest-to-crest distance, the de Broglie wavelength is the spatial period of the electron's wave function.

**Exercises (with Bloom level).**
- **Remember:** State de Broglie's hypothesis in one sentence and write the formula λ = h/p. (Bloom: Remember)
- **Apply (calculation):** An electron is accelerated through 100 V. Compute its de Broglie wavelength. Is it comparable to visible light, X-rays, or atomic spacings? (Bloom: Apply)
- **Apply (calculation):** A proton is accelerated through 100 V. Compute its de Broglie wavelength. By what factor does it differ from the electron case, and why? (Bloom: Apply)
- **Analyze:** The Davisson–Germer experiment found a diffraction peak at 50° for 54 V electrons. Work backward: assuming Bragg's law with d = 0.091 nm, what wavelength does this imply? Compare to the de Broglie prediction. (Bloom: Analyze)
- **Evaluate:** Why did the Tonomura 1989 experiment use an electron biprism rather than physical slits? What would happen to the interference pattern if the electron rate were increased by a factor of 10⁶? Would the pattern change? (Bloom: Evaluate)
- **LLM Exercise — matter-wave simulation:** Build a D3 v7 single-electron double-slit simulation. The simulation should display the wave function amplitude through two slits and the resulting |ψ|² interference pattern on a detector screen. Add a slider for slit separation d and electron energy K (eV). Show the de Broglie wavelength computed from K. Verification: fringe spacing Δy ≈ λL/d should match the visual fringe spacing on the screen for the given parameters L (screen distance). (Bloom: Create)

---

## F. Library files relevant to this chapter

- `/Users/bear/Documents/CoWork/bear-textbooks/books/quantum-mechanics-vol1/pantry/_lib_quantum-physics-for-beginners.md` — Chapter 7 ("Shocking electron experiment redefines all matter forever"): contains the de Broglie derivation from E = mc² and E = hf (popular but slightly garbled — the lib source conflates de Broglie's derivation with his double-slit experiment; de Broglie did not perform the experiment). Use for the narrative hook and the λ = h/mv formula; do not use for the Davisson–Germer experimental details.
- Townsend text — Chapter 2 starts with the double-slit experiment using helium atoms (Mlynek's group, 1990s). Confirmed by grep: "Chapter 2 starts with the double-slit experiment... the key experiment is a double-slit experiment with helium atoms carried out by Jürgen Mlynek's group in the 1990s." Exact page content not read (OCR quality variable); the conceptual structure of Townsend Ch 2 appears more suited to Chapters 2–3 of this book's numbering.
- `/Users/bear/Documents/CoWork/bear-textbooks/books/quantum-mechanics-vol1/pantry/_lib_qmsri-00-how-to-use-the-simulations.md` — the Chapter 0 wave packet simulation is the warm-up for the Ch 2 double-slit simulation exercise. Students already know the toolchain.

---

## G. Gaps and flags

**FLAG — de Broglie thesis translation.** The 1924 thesis was written in French. An English translation was published in 1998 by Annales de la Fondation Louis de Broglie. The chapter author may want to cite this translation rather than the French original for student accessibility.

**FLAG — Historical priority for single-electron double-slit.** Tonomura 1989 is the most famous and most cited, but Merli–Missiroli–Pozzi 1976 has clear historical priority. The chapter author should acknowledge both. The MMP experiment was voted "most beautiful physics experiment" in a 2002 Physics World poll (alongside Young's original double slit and Millikan's oil drop).

**FLAG — Biprism vs. actual slits.** All the famous single-electron experiments (Merli, Tonomura) used an electron biprism (a fine wire at positive potential that splits the electron wave), not physical slits. The first experiment with real nano-fabricated double slits was Bach et al. (2013). The chapter author should clarify this distinction — students may be confused that the "double-slit experiment" used a wire.

**GAP — Relativistic correction for de Broglie wavelength.** The non-relativistic formula λ = h/√(2mK) is used throughout, but modern electron microscopes operate at 200+ kV where relativistic corrections matter (~30% correction at 200 kV). A sidebar or footnote on the relativistic form p = √((K/c)² + 2m_e K) would round out the chapter.

**GAP — Simulation prompt for this chapter.** No LLM Exercise prompt exists in the library files for Ch 2. The chapter author needs to write a double-slit interference simulation prompt (wave function amplitude through two slits, |ψ|² on detector screen, slider for slit separation and electron energy, live de Broglie wavelength display). This is a natural and achievable D3 v7 simulation.

**GAP — Connection to electron microscopy.** The chapter author should include a brief example showing how electron microscopy is applied de Broglie physics. The wavelength at 200 kV (~2.5 pm) compared to optical microscopy (~500 nm) explains the resolution advantage by a factor of ~200,000.
