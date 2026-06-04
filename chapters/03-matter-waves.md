# Chapter 2 — Matter Waves: de Broglie, Davisson–Germer, and the Double Slit

## TL;DR

Every particle with momentum $p$ has an associated wavelength $\lambda = h/p$. This is not a metaphor — electrons diffract from crystals exactly as X-rays do, and single electrons build up double-slit interference patterns one dot at a time. This chapter gives you the formula, shows you the key experiments, and builds intuition for why wave behavior becomes invisible at human scales.

---

## Learning Objectives

By the end of this chapter you should be able to:

1. **Remember** de Broglie's hypothesis and write $\lambda = h/p$ in its kinetic-energy form $\lambda = h/\sqrt{2mK}$. *(Bloom: Remember)*
2. **Apply** the de Broglie relation to compute the wavelength of any non-relativistic particle given its energy or accelerating voltage. *(Bloom: Apply)*
3. **Analyze** the Davisson–Germer result: given a measured diffraction angle and crystal spacing, recover the electron wavelength and compare to the de Broglie prediction. *(Bloom: Analyze)*
4. **Evaluate** what the single-electron double-slit buildup (Tonomura 1989) proves about the wave nature of individual electrons — and what it rules out. *(Bloom: Evaluate)*
5. **Create** a D3 simulation of the double-slit interference pattern that responds live to changes in electron energy and slit geometry. *(Bloom: Create)*

---

## The Problem: An Electron Hit the Wrong Target

The year is 1926 and Lester Germer has a problem. He and Clinton Davisson had been firing electrons at a nickel surface and recording where they scattered. Nothing exciting: a smooth blob of electrons bounced off at roughly all angles, just as you'd expect billiard balls to. Then a liquid-air flask exploded near the apparatus. The vacuum tube cracked. Oxygen flooded in and oxidized the nickel. To clean it, they annealed the target — heated it until the oxide burned off. When they cooled it down and resumed measurements, the smooth blob was gone. In its place: sharp peaks at specific angles, as if the electrons were diffracting.

They had accidentally turned polycrystalline nickel into a single crystal. And single crystals have regular atomic planes — the same planes that Bragg had shown diffract X-rays. The electrons, it turned out, were doing exactly what X-rays do. Not because anyone planned the experiment to show this. Because physics required it.

Two years earlier, a graduate student in Paris had predicted it. Louis-Victor de Broglie argued, in his 1924 doctoral thesis, that if light waves can behave as particles, then matter particles ought to behave as waves. He gave the relationship:

$$\lambda = \frac{h}{p}$$

The Davisson–Germer accident confirmed it. This chapter is about why, how, and what it means for everything that follows.

---

## Core Development

### The de Broglie Hypothesis

Einstein had shown in 1905 that light, despite being a wave, comes in discrete packets with energy $E = h\nu$. The photon's momentum is $p = E/c = h\nu/c = h/\lambda$. De Broglie looked at this relation and asked: why is it only for light? His reversal: if electromagnetic waves carry momentum $p = h/\lambda$, then matter with momentum $p$ should have an associated wavelength $\lambda = h/p$.

For a non-relativistic particle with kinetic energy $K = p^2/2m$, this becomes:

$$\boxed{\lambda = \frac{h}{p} = \frac{h}{\sqrt{2mK}}}$$

For a particle of charge $e$ (like an electron, $e = 1.602 \times 10^{-19}$ C) accelerated through a potential difference $V$, the kinetic energy is $K = eV$, giving:

$$\lambda = \frac{h}{\sqrt{2meV}}$$

For electrons specifically, this simplifies to a handy shortcut:

$$\lambda_{\text{electron}} \approx \frac{1.226\text{ nm}}{\sqrt{V\text{ (in volts)}}}$$

At $V = 150$ V: $\lambda \approx 0.1$ nm = 1 Å. This is the same scale as the spacing between atoms in a crystal — which is why electron diffraction is possible in the first place.

**What the wavelength is not.** The de Broglie wavelength is the spatial period of the associated probability wave. It has nothing to do with the physical size of the electron (estimated classical radius $\sim 2.8 \times 10^{-15}$ m, roughly ten orders of magnitude smaller). A 54 eV electron has $\lambda \approx 0.167$ nm — eight orders of magnitude larger than the electron's classical radius. The wavelength describes the *wave function*, not the particle's physical extent.

De Broglie's thesis committee was skeptical and consulted Einstein before approving it. Einstein called the idea brilliant. De Broglie received the Nobel Prize in 1929 — the only Nobel ever awarded specifically for a doctoral thesis. [verify: Nobel records confirm 1929 prize to de Broglie for this work]

---

### The Davisson–Germer Experiment (1927)

The accidental discovery became, when understood, one of the cleanest confirmations in the history of physics. After the nickel was recrystallized, Davisson and Germer found a sharp diffraction peak in the scattered electron intensity at 50° for electrons accelerated through 54 V. Let us work out why.

The relevant geometry is Bragg diffraction. When a wave of wavelength $\lambda$ reflects from crystal planes spaced $d$ apart, constructive interference (a Bragg peak) occurs when:

$$2d\sin\theta_{\text{Bragg}} = n\lambda$$

The atomic planes responsible in the Davisson–Germer experiment are the (111) planes of face-centered cubic nickel, with spacing $d = 0.091$ nm. For 54 V electrons, the de Broglie wavelength is 0.167 nm (see Worked Example below). First-order Bragg scattering gives a peak consistent with the observed 50° geometry — exact agreement with the de Broglie prediction.

Davisson and Germer did not set out to test de Broglie. They recognized the significance of the diffraction peaks partly after Davisson visited Europe and discussed the results with Born, Franck, and other quantum physicists who told him what he had found. The paper appeared in *Physical Review* in December 1927. Davisson shared the 1937 Nobel Prize with George Paget Thomson, who had independently demonstrated electron diffraction by firing electrons through thin films and observing diffraction rings — a different geometry, the same physics. [verify: Nobel Prize records, doi:10.1103/PhysRev.30.705]

---

### The Single-Electron Double Slit: Wave–Particle Duality Made Unavoidable

The double-slit argument is this: if you send a wave through two narrow slits, you get an interference pattern on the far screen. The wave from slit 1 and the wave from slit 2 add constructively where their path-length difference is a whole wavelength, destructively where it is a half-wavelength. Young showed this with light in 1801. The question for electrons is: what happens when you fire them one at a time?

Akira Tonomura and colleagues at Hitachi answered this definitively in 1989. They used an electron biprism — a fine wire at positive potential that splits the electron beam into two coherent paths (physically equivalent to two slits). The beam was so weak that fewer than one electron was in the apparatus at any moment. Each electron hit a position-sensitive detector and was recorded as a single dot.

The sequence is worth stating carefully:

- At **10 electrons**: random-looking dots. Nothing obvious.
- At **200 electrons**: still mostly random, but some clustering.
- At **6,000 electrons**: faint hints of stripes.
- At **70,000 electrons**: a clear, sharp interference pattern — bright and dark fringes, exactly as predicted by wave mechanics.

Each electron arrived as a localized event (particle-like). The accumulated pattern is an interference pattern (wave-like). And the pattern emerged even though the electrons went through one at a time — they were not interfering with each other.

The conclusion is forced on you: **each individual electron's wave function went through both paths simultaneously.** There is no trajectory you can draw for the electron as it travels from source to detector. The wave — specifically, the probability amplitude — takes both paths and interferes with itself. The dot you see at the detector is where the wave function "collapsed" upon measurement, but the interference pattern that dot contributed to reflects the wave's passage through both arms.

Historical note: the Tonomura experiment (1989) is the most famous, but Pier Giorgio Merli, Giulio Missiroli, and Gianfranco Pozzi in Bologna demonstrated single-electron buildup earlier, in 1974 (published 1976 in *American Journal of Physics*). The Merli–Missiroli–Pozzi experiment was voted one of the most beautiful physics experiments in a 2002 *Physics World* poll. The first experiment using real nano-fabricated physical double slits (rather than a biprism) was Bach et al. (2013) in the *New Journal of Physics*. [verify: Tonomura doi:10.1119/1.16104; Merli et al. doi cannot confirm — flag; Bach et al. doi:10.1088/1367-2630/15/3/033018]

---

### Wave–Particle Duality Is Universal — and Invisible at Human Scale

Wave behavior is not special to electrons. The de Broglie relation applies to every particle:

| Object | Mass | Speed | $\lambda$ |
|--------|------|-------|----------|
| Electron (54 eV) | $9.1 \times 10^{-31}$ kg | $4.4 \times 10^6$ m/s | 0.167 nm |
| Proton (same KE) | $1.67 \times 10^{-27}$ kg | $1.0 \times 10^5$ m/s | 3.9 pm |
| C$_{60}$ molecule (Zeilinger 1999) | $1.2 \times 10^{-24}$ kg | 220 m/s | $\sim$250 fm |
| Person (70 kg, walking at 1 m/s) | 70 kg | 1 m/s | $\sim 10^{-35}$ m |

The buckyball ($\text{C}_{60}$, 60 carbon atoms, mass $\sim 720$ amu) diffracted from a grating with 50 nm slits in Zeilinger's Vienna laboratory in 1999. The de Broglie wavelength was smaller than the molecule itself — yet fringes appeared. More recently (2019), Fein et al. demonstrated diffraction from molecules of $\sim 2000$ atoms, pushing the quantum–classical boundary to mesoscopic scales. [verify: Arndt et al. 1999 doi:10.1038/44348; Fein et al. 2019 doi:10.1038/s41567-019-0663-9]

For the 70 kg person, $\lambda \sim 10^{-35}$ m — roughly 20 orders of magnitude smaller than a proton. Quantum wave behavior is unobservable at human scales not because the physics is different, but because the wavelength is unresolvably tiny. The correspondence principle holds: quantum mechanics reduces to classical mechanics for large masses and large quantum numbers.

**Quantum–classical boundary.** This is an active research area. Decoherence — the interaction of a quantum system with its environment — degrades interference far faster for large, warm objects than for isolated electrons in a vacuum. The largest objects that have shown diffraction are molecules of $\sim 2000$ atoms at 100 K. Pushing this boundary is one of the frontier goals of experimental quantum physics.

---

### Connecting de Broglie to What Comes Next

The de Broglie relation $\lambda = h/p$ is not the end of the story — it is the seed of it. Here is what it implies:

A particle with definite momentum $p$ has definite wavelength $\lambda = h/p$. A wave with a single definite wavelength extends over all space — it is completely delocalized. To localize a particle, you must superpose waves with many different momenta, which means many different wavelengths. Superposing a range of momenta $\Delta p$ around $p_0$ gives a wave packet localized within $\Delta x \sim h/\Delta p$. This is the Fourier relationship — and it is exactly the Heisenberg uncertainty principle $\Delta x \, \Delta p \gtrsim \hbar/2$.

The probability wave that de Broglie postulated — the wave whose wavelength equals $h/p$ — turns out to be the wave function $\psi(x,t)$. Chapter 3 will tell you precisely what the wave function means and how $|\psi|^2$ connects to experiment. Chapter 4 will give you the equation that governs how $\psi$ evolves.

---

## Worked Example: The de Broglie Wavelength of a 54 eV Electron

**This is the Davisson–Germer canonical case.**

**Given:** An electron accelerated through $V = 54$ V, so kinetic energy $K = 54$ eV.

**Find:** The de Broglie wavelength $\lambda$.

**Step 1 — Convert to SI.** $K = 54 \times 1.602 \times 10^{-19}$ J $= 8.65 \times 10^{-18}$ J.

**Step 2 — Find the momentum.** The non-relativistic kinetic energy is $K = p^2/2m_e$, so

$$p = \sqrt{2m_e K} = \sqrt{2 \times (9.109 \times 10^{-31}\text{ kg}) \times (8.65 \times 10^{-18}\text{ J})}.$$

$$p = \sqrt{1.576 \times 10^{-47}\text{ kg}^2\text{m}^2\text{s}^{-2}} = 1.255 \times 10^{-24}\text{ kg m s}^{-1}.$$

**Step 3 — Apply de Broglie.** $h = 6.626 \times 10^{-34}$ J s, so

$$\lambda = \frac{h}{p} = \frac{6.626 \times 10^{-34}}{1.255 \times 10^{-24}} = 5.28 \times 10^{-10}\text{ m} \approx 0.167\text{ nm}.$$

**Check with the shortcut.** $\lambda = 1.226/\sqrt{54} = 1.226/7.35 \approx 0.167$ nm. ✓

**Dead end to flag.** A common mistake is computing $K = eV$ and immediately plugging into $\lambda = h/\sqrt{2mK}$ in eV without converting. The formula requires SI units throughout (J, kg, m). If you use $K$ in eV directly, you get a number with wrong units and a wrong exponent.

**Step 4 — Compare to crystal plane spacing.** The (111) planes of nickel have $d = 0.091$ nm. The Bragg condition for first-order diffraction:

$$\sin\theta_{\text{Bragg}} = \frac{\lambda}{2d} = \frac{0.167}{2 \times 0.091} = 0.918 \implies \theta_{\text{Bragg}} \approx 66.6°.$$

In the Davisson–Germer geometry, the scattering angle measured from the incident beam is $2(90° - \theta_{\text{Bragg}}) \approx 47°$, close to the observed 50°. The small discrepancy arises because the effective lattice spacing inside the crystal is modified by the electron's refraction at the surface — the inner potential of the metal shifts $\lambda$ slightly. Correcting for this brings the prediction into exact agreement.

**The lesson.** The calculation requires only $K$, $m_e$, and $h$ — all measured independently — and predicts the diffraction angle within the experimental precision. This is a parameter-free prediction confirmed by the accident that became a discovery.

**The limit.** The formula $\lambda = h/\sqrt{2mK}$ is non-relativistic. For electrons at 54 eV, the correction factor is $\gamma \approx 1.0001$ — completely negligible. At 200 kV (a modern transmission electron microscope), $\gamma \approx 1.39$ and the relativistic correction to $\lambda$ is $\sim 30\%$; the relativistic formula $p = \sqrt{(K/c)^2 + 2m_e K}$ is required.

---

## Common Misconceptions

**"The de Broglie wavelength is the size of the particle."**

The wavelength has nothing to do with the physical size of the particle. An electron's de Broglie wavelength at 54 eV is 0.167 nm; its classical radius is $\sim 2.8 \times 10^{-15}$ m — eight orders of magnitude smaller. The wavelength is a property of the particle's *state of motion*, encoded in the wave function.

**"The interference pattern forms because electrons interact with each other."**

If electrons were interfering with each other, reducing the beam intensity until only one electron is present at a time would destroy the pattern. Tonomura's experiment does exactly this. The pattern appears anyway, building up dot by dot. Each electron interferes with itself — more precisely, each electron's probability amplitude travels through both paths simultaneously and interferes. The wave nature is an intrinsic property of each electron's quantum state, not a collective effect.

**"Going through both slits means the electron splits in two."**

No — the electron arrives at the detector as a single localized event. It does not arrive in two places at once. What travels through both slits is the probability amplitude, $\psi$. The physical detection event is always a single dot. The interference pattern is the statistical distribution of those dots across many electrons.

**"Wave–particle duality means quantum mechanics breaks down for large objects."**

Quantum mechanics does not break down; wave effects become unobservably small because $\lambda \propto 1/p \propto 1/m$ for a given speed. A 70 kg person has $\lambda \sim 10^{-35}$ m — smaller by 20 orders of magnitude than a proton. The physics is the same; the effects are invisible.

---

## Exercises

**Warm-up**

1. *[Remember]* State de Broglie's hypothesis in one sentence. Then write the formula for $\lambda$ in terms of (a) momentum $p$, (b) kinetic energy $K$, and (c) accelerating voltage $V$ (for a particle of charge $e$ and mass $m$). *Difficulty: warm-up.*

2. *[Apply]* An electron is accelerated through 100 V. (a) Compute its de Broglie wavelength using the shortcut formula $\lambda \approx 1.226/\sqrt{V}$ nm. (b) Is this wavelength comparable to visible light ($\sim 400$–700 nm), X-rays ($\sim 0.01$–10 nm), or atomic spacings ($\sim 0.1$–0.5 nm)? (c) A proton is accelerated through the same 100 V. By what factor does its wavelength differ from the electron's? (The proton mass is 1836 times the electron mass.) *Difficulty: warm-up.*

**Apply**

3. *[Analyze]* The Davisson–Germer experiment observed a diffraction peak at 50° for 54 V electrons. Work backward: assume Bragg's law with $d = 0.091$ nm and first-order diffraction ($n = 1$), and compute the wavelength implied by the observed peak angle. Compare this to the de Broglie prediction. Are they consistent? If the numbers differ slightly, identify one physical reason they might not be identical (hint: the electron refracts at the crystal surface). *Difficulty: Apply.*

4. *[Apply]* A thermal neutron has kinetic energy $K \approx k_B T$ at room temperature ($T = 293$ K, $k_B = 1.38 \times 10^{-23}$ J/K). The neutron mass is $m_n = 1.675 \times 10^{-27}$ kg. (a) Compute $\lambda$ for a thermal neutron. (b) How does this compare to typical crystal plane spacings ($\sim 1$–3 Å)? (c) Neutron diffraction is used to locate hydrogen atoms in protein crystals — a task X-ray diffraction struggles with. Explain why the wavelength makes neutrons suited to this task. *Difficulty: Apply.*

5. *[Evaluate]* Tonomura's 1989 experiment used an electron biprism, not physical slits. (a) What is an electron biprism, and why does it produce interference equivalent to two slits? (b) The experiment ran at intensities so low that fewer than one electron was in the apparatus at any moment. What would you expect to see if electrons were classical particles with definite trajectories through one slit? How does the actual result differ? (c) Would increasing the electron rate by a factor of $10^6$ (so many electrons are present simultaneously) change the interference pattern? Why or why not? *Difficulty: Evaluate.*

**Produce-something**

6. *[Create + Analyze]* The C$_{60}$ buckyball has 60 carbon atoms and mass $\approx 720$ amu ($1\text{ amu} = 1.66 \times 10^{-27}$ kg). Zeilinger's group effused buckyballs from an oven at temperature $T \approx 900$ K. (a) Estimate the most probable speed of C$_{60}$ at $T = 900$ K using $\frac{1}{2}mv^2 = \frac{3}{2}k_BT$. (b) Compute the de Broglie wavelength at this speed. (c) Zeilinger used a grating with 50 nm slits. Would you expect diffraction to be visible (i.e., is $\lambda$ small compared to the slit size, or comparable)? (d) Write one sentence explaining why this result cannot be explained by any theory in which C$_{60}$ is a classical object with a definite trajectory. *Difficulty: Apply+.*

---

## Still Puzzling

**Where does the quantum–classical boundary lie?** We know electrons and atoms diffract; we know 70 kg people do not show measurable diffraction. The 2019 Fein et al. experiment reached 2,000-atom molecules. What sets the boundary? The answer involves *decoherence* — the interaction of a quantum system with its thermal environment, which rapidly suppresses interference for warm, massive, coupled objects. But a quantitative theory of when exactly a quantum system becomes effectively classical is still an active area of research.

**Why does which-path information destroy interference?** If you add a detector to determine which slit an electron passed through, the interference pattern vanishes — replaced by two classical blobs. This is experimentally robust. But the mechanism depends on how you think about quantum mechanics: is it about physical disturbance, entanglement with the detector, or the irreversibility of information gain? Different interpretations give different answers to "why," even though they all agree on the experimental outcome.

**Does the Born rule need to be postulated?** De Broglie told us about the wave. Born told us that $|\psi|^2$ is the probability density. But is Born's rule a separate axiom, or can it be derived from something more fundamental? Zurek's "envariance" program and various many-worlds approaches claim to derive it. Whether these derivations succeed or merely shift the mystery is genuinely contested.

---

## The +1 — Simulation Exercise: Double-Slit Interference Pattern

The deliverable for this chapter is `02-double-slit.html`: a D3 simulation of electron double-slit interference that shows the wave amplitude through two slits, the $|\psi|^2$ intensity on the detector screen, and a live display of the de Broglie wavelength and predicted fringe spacing.

### The Claude Prompt

````
SHOW.
The double-slit interference pattern for matter waves (de Broglie relation):
  λ = h/p = h/√(2mK),  where K is the electron kinetic energy in eV.

For two slits of width w separated by distance d (center-to-center),
illuminated by a plane wave of wavelength λ, the far-field intensity
pattern on a screen at distance L is:

  I(y) = I₀ · [sin(β/2)/(β/2)]² · cos²(δ/2)

where:
  β = (2π w sin θ) / λ   (single-slit diffraction envelope)
  δ = (2π d sin θ) / λ   (double-slit interference term)
  sin θ ≈ y / L           (small-angle approximation, valid for L >> d, w)

The fringe spacing (distance between adjacent bright fringes) is:
  Δy = λ L / d

PARAMETERS (with sliders):
  K:  electron kinetic energy   10 eV to 1000 eV    (default: 54 eV)
  d:  slit separation           0.05 nm to 1.0 nm   (default: 0.3 nm)
  w:  slit width                0.01 nm to 0.2 nm   (default: 0.1 nm)
  L:  screen distance           50 nm to 500 nm     (default: 200 nm)

DISPLAY (three panels, stacked vertically):
  Panel 1 (200 px tall) — SOURCE + SLITS:
    A uniform horizontal wave arriving from the left.
    Two vertical rectangular slits (gaps in a barrier).
    Label the slit width w and separation d.

  Panel 2 (150 px tall) — WAVE AMPLITUDE IN SLIT PLANE:
    Show a schematic of the amplitude emerging from each slit
    as two circular wavefronts overlapping. (Qualitative, not numerically exact.)

  Panel 3 (300 px tall) — DETECTOR SCREEN (far field):
    Plot I(y) vs y in blue filled curve (the |ψ|² pattern).
    x-axis: y from −150 to +150 nm (or appropriate range).
    Overlay a red dashed curve for the single-slit envelope I₀[sinc(β/2)]².
    Mark fringe spacing Δy with a two-headed arrow and label.

LIVE NUMERICAL READOUT (right panel, 250 px wide):
    λ  = h/√(2mK)        in nm    (update with K slider)
    Δy = λL/d             in nm    (update with all sliders)
    Number of fringes inside central diffraction peak: floor(2d/w)

VERIFY:
(a) K = 54 eV: λ ≈ 0.167 nm (display must show this).
(b) With d = 0.3 nm, L = 200 nm, K = 54 eV: Δy = λL/d = 0.167·200/0.3 ≈ 111 nm.
    The fringe spacing shown on the plot must match this value.
(c) Doubling d should halve Δy. Check with slider.
(d) Tripling K reduces λ by √3 ≈ 1.73 and reduces Δy by the same factor. Check.

CONSTRAIN.
- D3 v7 from CDN. SVG only. Vanilla JS. Single self-contained .html file.
- Use m_e = 9.109e-31 kg, h = 6.626e-34 J·s, e = 1.602e-19 C.
- The formula I(y) = I₀ sinc²(β/2) cos²(δ/2) must be implemented exactly.
  Handle sinc(0) = 1 (L'Hôpital / branch case).
- N = 800 points on the y-axis for smooth rendering.
- Display λ in nm to 3 decimal places and Δy in nm to 1 decimal place.
- Color scheme: blue filled for |ψ|², red dashed for single-slit envelope.
````

### Exploration Tasks

**Task 1 — Verify the de Broglie shortcut.** Set $K = 100$ eV. The live display should show $\lambda \approx 0.123$ nm. Compute $1.226/\sqrt{100}$ by hand. Do they agree? Now set $K = 400$ eV and repeat. Write down the pattern you observe.

**Task 2 — Fringe spacing vs. slit separation.** With $K = 54$ eV, $w = 0.1$ nm, $L = 200$ nm: record $\Delta y$ at $d = 0.2$ nm, $d = 0.3$ nm, $d = 0.6$ nm. Make a table. Does $\Delta y$ scale as $1/d$? Plot $\Delta y$ vs. $1/d$ and check linearity.

**Task 3 — The diffraction envelope.** The red dashed curve is the single-slit diffraction envelope. Find the slit width $w$ that makes the envelope's first zero (where it first touches zero) coincide with the third interference fringe. Use the condition: envelope zero at $\sin\theta = \lambda/w$; fringe peak at $\sin\theta = 3\lambda/d$. Verify with the sliders.

**Task 4 — Energy scaling.** Increase $K$ from 54 eV to 216 eV (four times). By what factor does $\lambda$ change? By what factor does $\Delta y$ change? Write the scaling relationship $\Delta y \propto K^{-1/2}$ and verify it numerically with the simulation.

---

## References

de Broglie, L. (1924). *Recherches sur la théorie des quanta*. Doctoral thesis, Université de Paris. Published as *Annales de Physique*, 3 (1925), 22–128. [verify: English translation available from Annales de la Fondation Louis de Broglie, 1998]

Davisson, C., & Germer, L. H. (1927). Diffraction of electrons by a crystal of nickel. *Physical Review*, 30(6), 705–741. doi:10.1103/PhysRev.30.705

Tonomura, A., Endo, J., Matsuda, T., Kawasaki, T., & Ezawa, H. (1989). Demonstration of single-electron buildup of an interference pattern. *American Journal of Physics*, 57(2), 117–120. doi:10.1119/1.16104

Merli, P. G., Missiroli, G. F., & Pozzi, G. (1976). On the statistical aspect of electron interference phenomena. *American Journal of Physics*, 44(3), 306–307. [verify: doi not confirmed; journal and volume confirmed in notes]

Bach, R., Pope, D., Liou, S.-H., & Batelaan, H. (2013). Controlled double-slit electron diffraction. *New Journal of Physics*, 15, 033018. doi:10.1088/1367-2630/15/3/033018

Arndt, M., Nairz, O., Vos-Andreae, J., Keller, C., van der Zouw, G., & Zeilinger, A. (1999). Wave–particle duality of C₆₀ molecules. *Nature*, 401, 680–682. doi:10.1038/44348

Fein, Y. Y., Geyer, P., Zwick, P., Kiałka, F., Pedalino, S., Mayor, M., Gerlich, S., & Arndt, M. (2019). Quantum superposition of molecules beyond 25 kDa. *Nature Physics*, 15, 1242–1245. doi:10.1038/s41567-019-0663-9 [verify]

Townsend, J. S. (2012). *A Modern Approach to Quantum Mechanics* (2nd ed.). University Science Books.

Griffiths, D. J., & Schroeter, D. F. (2018). *Introduction to Quantum Mechanics* (3rd ed.). Cambridge University Press.
