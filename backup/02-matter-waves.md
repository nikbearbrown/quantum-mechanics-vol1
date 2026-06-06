# Chapter 2 — Matter Waves: de Broglie, Davisson–Germer, and the Double Slit
*The accident that proved every moving thing is also a wave.*

The year is 1926 and Lester Germer has a problem he doesn't yet recognize as a discovery. He and Clinton Davisson had been firing electrons at a nickel surface for months, recording where they scattered. The results were deeply uninteresting: a smooth, featureless blob of electrons bouncing off at all angles, exactly what you'd expect from billiard balls hitting a rough wall. Then a liquid-air flask exploded near the apparatus. The vacuum tube cracked. Oxygen flooded in, oxidized the nickel, and ruined weeks of work. To clean the surface, they annealed the target — heated it slowly until the oxide burned away. When they resumed measurements, the smooth blob was gone. In its place: sharp peaks at specific angles.

They had, by accident, converted polycrystalline nickel into a single crystal. A single crystal has regular atomic planes — the same orderly planes that William Lawrence Bragg had shown would diffract X-rays. The electrons, it turned out, were doing exactly what X-rays do when they scatter from a crystal lattice. Not because Davisson and Germer planned this experiment. Because physics required it.

Two years earlier, a doctoral student in Paris had predicted something like it. Louis-Victor de Broglie argued, in a thesis his committee nearly rejected, that if light waves can behave like particles — which Einstein had shown in 1905, invoking the photoelectric effect — then matter particles ought to behave like waves. The reasoning had a clean symmetry. Einstein showed electromagnetic waves carry momentum $p = h/\lambda$, where $h$ is Planck's constant. De Broglie simply reversed it: a particle with momentum $p$ should have an associated wavelength

$$\lambda = \frac{h}{p}.$$

The committee consulted Einstein before approving the thesis. Einstein called the idea brilliant. De Broglie received the Nobel Prize in 1929 — the only one ever awarded specifically for a doctoral thesis. The Davisson–Germer accident, understood in that light, was the confirmation. And the confirmation raised a question that turned out to be harder than the formula: what, exactly, is doing the waving?

<!-- → [IMAGE: photograph or schematic of the Davisson–Germer apparatus — showing the electron gun, rotatable detector, and nickel crystal target; caption should note the accidental annealing that converted the sample to a single crystal] -->

![photograph or schematic of the Davisson–Germer apparatus — showing the electron gun, rotatable detector, and nickel crystal target](../images/02-matter-waves-fig-01.png)
*Figure 2.1 — photograph or schematic of the Davisson–Germer apparatus — showing the electron gun, rotatable detector, and nickel crystal target*

---

## The Formula and What It Means

Start with what de Broglie actually wrote. For a non-relativistic particle with kinetic energy $K$ and mass $m$, momentum and energy are related by $K = p^2/2m$, so $p = \sqrt{2mK}$. Substituting:

$$\lambda = \frac{h}{\sqrt{2mK}}.$$

For a charged particle of charge $e$ accelerated from rest through a potential difference $V$, the kinetic energy is $K = eV$, giving

$$\lambda = \frac{h}{\sqrt{2meV}}.$$

For electrons specifically — you will find yourself computing this constantly — the numbers reduce to a useful shortcut:

$$\lambda_{\text{electron}} \approx \frac{1.226\text{ nm}}{\sqrt{V\text{ (in volts)}}}.$$

At 150 volts, $\lambda \approx 0.1$ nm. One tenth of a nanometer. One ångström. This is not a coincidence — it is approximately the spacing between atoms in a solid. If you want a wave to diffract from a crystal, its wavelength must be comparable to the crystal's spacing. X-rays can do this because their wavelengths are in the ångström range. The de Broglie formula tells you that electrons accelerated through a few hundred volts land in exactly the same range. This is why Davisson and Germer could see diffraction at all, and why Bragg's law — developed entirely for X-rays — worked without modification for electrons.

Here is what the wavelength is not: it is not the physical size of the electron. The classical electron radius is roughly $2.8 \times 10^{-15}$ m — eight orders of magnitude smaller than the 0.167 nm de Broglie wavelength of a 54 eV electron. The wavelength is a property of the electron's state of motion, not its physical extent. This distinction matters enormously when students first encounter the idea, because the intuitive picture — some small ball with ripples around it — is wrong. The wave and the particle are not separable components of the same thing. The wave *is* the thing, in the sense that it is the only object that evolves deterministically between observations.

<!-- → [TABLE: de Broglie wavelengths for several particles — columns: particle, mass, speed or energy, λ; rows: electron at 54 eV (the Davisson–Germer case), proton at same kinetic energy, C₆₀ buckyball at 900 K, 70 kg person walking at 1 m/s; the last row makes the classical limit visceral] -->

De Broglie's idea was not purely abstract. The argument has a logical structure worth tracing. Einstein's special relativity required that energy and momentum transform as a four-vector. De Broglie noticed that frequency and wave vector (the spatial frequency $1/\lambda$) also transform as a four-vector. For a photon, the relationship $E = h\nu$ connects these two four-vectors by the single constant $h$. De Broglie asserted that the same constant connects them for any particle. It was a symmetry argument, not an empirical fit. The experiments came later.

---

## The Davisson–Germer Experiment

Reconstruct the 1927 result from first principles, and you see exactly why it is convincing.

Davisson and Germer found a sharp diffraction peak at 50° for electrons accelerated through 54 V. The de Broglie wavelength at 54 eV is:

$$p = \sqrt{2 \times (9.109 \times 10^{-31}) \times (54 \times 1.602 \times 10^{-19})} = 3.970 \times 10^{-24}\text{ kg m s}^{-1}$$

$$\lambda = \frac{6.626 \times 10^{-34}}{3.970 \times 10^{-24}} \approx 0.167\text{ nm.}$$

The relevant crystal planes in nickel are the (111) planes of the face-centered cubic lattice, with spacing $d = 0.091$ nm. Bragg's law for first-order diffraction:

$$2d\sin\theta_{\text{Bragg}} = \lambda \implies \sin\theta_{\text{Bragg}} = \frac{0.167}{2 \times 0.091} = 0.918 \implies \theta_{\text{Bragg}} \approx 66.6°.$$

The scattering angle measured from the forward beam in the Davisson–Germer geometry converts to approximately 47° — close to the observed 50°. The small residual discrepancy is not a failure of de Broglie. It arises because electrons entering a metal crystal experience an attractive inner potential, which slightly accelerates them and shortens their wavelength inside the crystal. Correcting for this inner potential brings the prediction into exact agreement.

This is the structure of a successful quantitative test: a parameter-free prediction from quantities measured entirely independently ($h$, $m_e$, $d$), compared against an angle measured in an unrelated experiment that was not even designed to test this prediction. The agreement is not approximate. It is exact when the physics is accounted for completely.

Davisson and Germer did not fully understand what they had found until Davisson traveled to Europe and spoke with Max Born, James Franck, and others who had been digesting de Broglie's and Schrödinger's new wave mechanics. George Paget Thomson was doing similar experiments independently in Aberdeen, firing electrons through thin metal films and observing rings — Debye–Scherrer diffraction, the same geometry used for polycrystalline X-ray diffraction. Thomson and Davisson shared the 1937 Nobel Prize. (Davisson–Germer, *Physical Review* **30**, 705–740 (1927). doi:10.1103/PhysRev.30.705)

<!-- → [FIGURE: diagram of Bragg diffraction geometry applied to the Davisson–Germer case — showing incident and reflected electron beams, crystal planes separated by d = 0.091 nm, path-length difference of 2d sin θ, and the condition for constructive interference; contrast with a polycrystalline diffraction ring geometry for Thomson's version] -->

![diagram of Bragg diffraction geometry applied to the Davisson–Germer case — showing incident and reflected electron beams, crystal planes…](../images/02-matter-waves-fig-02.png)
*Figure 2.2 — diagram of Bragg diffraction geometry applied to the Davisson–Germer case — showing incident and reflected electron beams, crystal planes…*

There is a point of logic worth making explicit. The Davisson–Germer experiment does not prove that electrons *are* waves in some classical sense — that they are extended oscillations in a medium, the way sound is. What it proves is that electrons produce interference and diffraction phenomena that can only be calculated using wave mechanics. The distinction matters because the same electron that produces a diffraction peak arrives at the detector as a localized event — a single click, a single dot.

---

## Single Electrons, One at a Time

The hardest version of the experiment — and therefore the most instructive — is what Akira Tonomura and colleagues at Hitachi performed in 1989. They built a double-slit setup using an electron biprism: a fine wire held at positive potential that splits an electron beam into two coherent paths, physically equivalent to two slits. They reduced the beam intensity until fewer than one electron was in the apparatus at any moment. Each electron struck a position-sensitive detector and was recorded as a single localized dot.

Watch the pattern build:

At ten electrons, you see ten random-looking dots. Nothing suggests order. At two hundred electrons, there is faint clustering but no clear pattern. At six thousand, stripes begin to emerge. At seventy thousand, the result is unambiguous: a sharp, clean interference pattern of alternating bright and dark fringes — exactly the pattern predicted by treating the electron as a wave passing through both paths simultaneously.

The electrons did not interfere with each other. There was only ever one in the apparatus. Each electron arrived as a particle — a point — and contributed one dot to the pattern. Yet the distribution of those dots, accumulated over time, has the mathematical structure of wave interference. The conclusion is not optional: each individual electron's wave function passed through both arms of the apparatus simultaneously and interfered with itself. The dot on the detector is where the wave function collapsed upon measurement. The interference pattern is the accumulated probability, and that probability was determined by a wave that explored the full geometry on each individual pass.

Tonomura's 1989 paper is the most famous demonstration of this kind, but the first single-electron buildup was demonstrated by Pier Giorgio Merli, Giulio Missiroli, and Gianfranco Pozzi in Bologna in 1974 (published 1976 in *American Journal of Physics*). Their experiment was voted one of the most beautiful in physics in a 2002 *Physics World* poll. The first experiment using physically nano-fabricated real double slits — actual slits cut in a membrane, not a biprism — was Bach et al. in 2013. (Tonomura et al., *Am. J. Phys.* **57**, 117–120 (1989). doi:10.1119/1.16104; Bach et al., *New J. Phys.* **15**, 033018 (2013). doi:10.1088/1367-2630/15/3/033018)

<!-- → [CHART: sequence of detector images from the single-electron buildup — showing the pattern at approximately 10, 200, 6,000, and 70,000 electrons; this is the most important visual in the chapter and must show both the particle nature (individual dots) and wave nature (emerging fringes)] -->

![sequence of detector images from the single-electron buildup — showing the pattern at approximately 10, 200, 6,000, and 70,000 electrons](../images/02-matter-waves-fig-03.png)
*Figure 2.3 — sequence of detector images from the single-electron buildup — showing the pattern at approximately 10, 200, 6,000, and 70,000 electrons*

Here is what the experiment rules out, and this is the part students most need to hear carefully. It rules out any model in which the electron follows a definite trajectory through one slit or the other. If electrons had definite trajectories, reducing the rate to one at a time would change nothing — you would get two bright regions behind the two slits, and nothing in between. You do not get that. You get fringes extending well into the geometric shadow. The pattern depends on the separation of both slits, even though each electron can only be detected at one place.

There is a temptation to say: perhaps the electron really does go through one slit, but the act of not detecting it at the other slit somehow disturbs the outcome. This is not a live option. You can make the slits arbitrarily wide and the detector arbitrarily gentle, and the interference persists as long as you do not acquire information about which slit the electron used. What destroys interference is not physical disturbance — it is information.

---

## Why Human-Scale Objects Don't Diffract

The de Broglie relation applies to everything. Not just electrons. Not just quantum particles. Everything with momentum has an associated wavelength. The question is only whether that wavelength is large enough to matter.

A proton accelerated through the same 54 V has 1836 times the electron's mass. Its momentum at the same kinetic energy is $\sqrt{1836}$ times larger, so its wavelength is $\sqrt{1836} \approx 43$ times smaller: about 4 pm. Still in the range where crystal diffraction is possible — neutron and proton diffraction are real techniques used in materials science.

A $\text{C}_{60}$ buckyball — sixty carbon atoms, mass approximately 720 atomic mass units — was diffracted from a grating with 50 nm slits by Anton Zeilinger's group in Vienna in 1999. The de Broglie wavelength at the effusion temperature of 900 K comes out to roughly 2.5 pm (picometers) — smaller than the molecule itself. Yet fringes appeared. The 2019 experiments by Fein and colleagues pushed this to molecules of approximately 2,000 atoms. (Arndt et al., *Nature* **401**, 680–682 (1999). doi:10.1038/44348; Fein et al., *Nat. Phys.* **15**, 1242–1245 (2019). doi:10.1038/s41567-019-0663-9)

Now compute the wavelength of a 70 kg person walking at 1 m/s:

$$\lambda = \frac{6.626 \times 10^{-34}}{70 \times 1} \approx 10^{-35}\text{ m.}$$

This is roughly twenty orders of magnitude smaller than a proton. No physical slit, no crystal lattice, no instrument of any kind could resolve a wavelength this small. Quantum interference is not absent for large objects — it is present but utterly invisible. Quantum mechanics does not break down at human scales. It becomes indistinguishable from classical mechanics because the wavelengths are so small that no physically realizable grating or aperture could reveal the fringe structure.

This is Bohr's correspondence principle made concrete: quantum mechanics contains classical mechanics as a limiting case when the action of the system is much larger than $\hbar$. The de Broglie wavelength makes that limit quantitative and immediate. You do not need a philosophical argument. You just need to compute $h/p$.

<!-- → [INFOGRAPHIC: scale comparison — showing λ for electron at 54 eV (0.167 nm), thermal neutron (~1 Å), C₆₀ at 900 K (~2.5 pm), and 70 kg person walking (10⁻³⁵ m), placed on a logarithmic scale alongside reference lengths: proton radius, hydrogen atom, visible light wavelength, human hair; the goal is to make viscerally clear why quantum wavelengths are measurable for small particles and invisible for large ones] -->

---

## What the Wave Function Is Not Yet

De Broglie told you there is a wave. He did not tell you what it is a wave of. That is the harder question, and it was answered — provisionally, controversially — by Max Born in 1926, the same year Davisson's tube cracked. Born proposed that the wave function $\psi(x,t)$ is not a physical wave in space, like a water wave or a sound wave. Its square modulus, $|\psi(x,t)|^2$, is a probability density: the probability of finding the particle at position $x$ at time $t$ if you look.

This interpretation is not derivable from the de Broglie relation. It is a separate postulate, and it is the one that makes quantum mechanics genuinely strange. The wave function is a wave of probability amplitude — complex-valued, not directly observable, but real in the sense that it predicts observable interference.

The Tonomura experiment makes Born's rule visible. The interference pattern that builds up, dot by dot, is exactly the pattern $|\psi|^2$ predicts. The dots are random — you cannot predict where any individual electron will land. But their distribution, after many electrons, converges to $|\psi|^2$ computed from the wave equation. The randomness is not ignorance of hidden variables. It is, as far as anyone can tell, irreducible.

The connection between the de Broglie wavelength and the wave function $\psi$ is not an analogy. A state of definite momentum $p$ corresponds to a plane wave $\psi(x) \propto e^{ipx/\hbar}$ — a function that oscillates with spatial period $\lambda = h/p = 2\pi\hbar/p$. This is precisely de Broglie's wavelength, recovered as the spatial period of the quantum state. Chapter 3 takes up what the wave function means precisely, how it is normalized, and why $|\psi|^2$ gives probabilities. Chapter 4 gives the equation that governs how $\psi$ evolves.

One forward puzzle worth carrying into those chapters: a state of definite momentum has a perfectly definite wavelength. But a plane wave $e^{ipx/\hbar}$ extends over all space — it has no localization at all. To build a particle that is localized — one that sits in some finite region — you must superpose plane waves with many different momenta. Superposing a range of momenta $\Delta p$ produces localization within a spatial width $\Delta x \sim h/\Delta p$. This is not a theorem of quantum mechanics. It is a theorem of Fourier analysis, and it will become, in the next chapter, the Heisenberg uncertainty principle.

---

## Exercises

**Warm-up**

1. *Difficulty: Warm-up — tests command of the formula and unit conversions.*
   State de Broglie's hypothesis in one sentence. Then write $\lambda$ in terms of (a) momentum $p$, (b) kinetic energy $K$ for a particle of mass $m$, and (c) accelerating voltage $V$ for a particle of charge $e$ and mass $m$. Finally, use the electron shortcut $\lambda \approx 1.226/\sqrt{V}$ nm to compute $\lambda$ at $V = 54$ V, $V = 100$ V, and $V = 400$ V.
   *Tests: command of the three forms of the de Broglie relation and ability to apply the electron shortcut correctly.*

2. *Difficulty: Warm-up — tests understanding of what the wavelength is and is not.*
   A 54 eV electron has de Broglie wavelength $\lambda \approx 0.167$ nm. The classical electron radius is $r_e \approx 2.8 \times 10^{-15}$ m. By how many orders of magnitude does $\lambda$ exceed $r_e$? What does this tell you about the relationship between the electron's physical size and its wave behavior?
   *Tests: whether the student grasps that wavelength is a property of the state of motion, not the physical particle.*

3. *Difficulty: Warm-up — tests qualitative grasp of the classical limit.*
   Compute the de Broglie wavelength of a 70 kg person walking at 1 m/s and of a proton ($m_p = 1.673 \times 10^{-27}$ kg) moving at $10^5$ m/s. Express each in meters and then as a fraction of a proton radius ($\sim 10^{-15}$ m). Why is quantum interference unobservable for the person but not for the proton?
   *Tests: ability to apply $\lambda = h/p$ to macroscopic and nuclear-scale objects and to articulate the correspondence principle.*

**Application**

4. *Difficulty: Application — tests Bragg's law as used in Davisson–Germer.*
   Reconstruct the Davisson–Germer result quantitatively. Electrons are accelerated through 54 V and scatter from the (111) planes of nickel, with spacing $d = 0.091$ nm. (a) Compute $\lambda$ from the de Broglie relation. (b) Apply Bragg's law ($2d\sin\theta = n\lambda$, $n = 1$) to find the Bragg angle $\theta_{\text{Bragg}}$. (c) The observed peak in the Davisson–Germer geometry is near 50°. Identify one physical reason the calculated angle may differ slightly from the observed angle.
   *Tests: full quantitative execution of the Davisson–Germer argument, including awareness of the inner-potential correction.*

5. *Difficulty: Application — extends de Broglie to neutrons and materials science.*
   A thermal neutron has kinetic energy $K \approx k_B T$ at room temperature ($T = 293$ K, $k_B = 1.38 \times 10^{-23}$ J/K, $m_n = 1.675 \times 10^{-27}$ kg). (a) Compute $\lambda$ for a thermal neutron. (b) How does this compare to the Davisson–Germer electron wavelength and to typical crystal plane spacings (0.1–0.3 nm)? (c) Neutron diffraction can locate hydrogen atoms in protein crystals where X-ray diffraction struggles. Give a physical reason why neutrons are better suited to this task.
   *Tests: facility with the de Broglie formula for a different particle, and connection to real experimental technique.*

6. *Difficulty: Application — quantifies the molecular diffraction frontier.*
   The $\text{C}_{60}$ buckyball has mass $\approx 720$ amu ($1\text{ amu} = 1.66 \times 10^{-27}$ kg). Zeilinger's group effused buckyballs from an oven at $T \approx 900$ K. Estimate the most probable speed using $\frac{1}{2}mv^2 = \frac{3}{2}k_BT$ and compute $\lambda$. Compare $\lambda$ to the 50 nm slit spacing used in the experiment. Does the smallness of $\lambda$ relative to the slit surprise you? What does it tell you about the sensitivity of the detection technique required?
   *Tests: de Broglie calculation for a mesoscopic object, and intuition about why large-molecule diffraction is experimentally demanding.*

**Synthesis**

7. *Difficulty: Synthesis — connects Born's rule to the Tonomura buildup.*
   Tonomura's experiment records electrons one at a time, each as a single dot. (a) If electrons followed definite classical trajectories through one slit or the other, what pattern would accumulate on the detector? Draw or describe it. (b) The actual pattern is an interference fringe. What does this imply about each electron's wave function as it traverses the apparatus? (c) A student argues: "Maybe the electrons interact with the metal walls of the biprism and get deflected into fringes — no wave function needed." Design a modification of the experiment that would rule this out.
   *Tests: ability to reason from the experimental result back to wave function structure, and to construct falsifying arguments.*

8. *Difficulty: Synthesis — unifies de Broglie and Heisenberg via Fourier.*
   A particle with perfectly definite momentum $p$ has wave function $\psi(x) \propto e^{ipx/\hbar}$ — a plane wave extending over all space. (a) What is $\Delta x$ (the spatial uncertainty) for this state? What is $\Delta p$? (b) Now suppose you superpose plane waves over a momentum range $\Delta p$ centered on $p_0$. Argue qualitatively, using the Fourier relationship between a wave packet's width and its frequency content, that the resulting spatial width satisfies $\Delta x \sim h/\Delta p$. (c) Identify the chapter's statement that anticipates this result without yet calling it the uncertainty principle.
   *Tests: whether the student can connect the de Broglie wavelength to the uncertainty principle through the logic of wave superposition.*

**Challenge**

9. *Difficulty: Challenge — requires combining Bragg geometry with relativistic correction.*
   A modern 200 kV transmission electron microscope accelerates electrons through $2.0 \times 10^5$ V. (a) Compute $\lambda$ using the non-relativistic formula. (b) The relativistic momentum is $p = \sqrt{(K/c)^2 + 2m_eK}$ where $c = 3.0 \times 10^8$ m/s. Compute the relativistic $\lambda$. (c) By what percentage does the relativistic correction change $\lambda$? (d) In a TEM, the electron wavelength determines the minimum resolvable feature size (Rayleigh criterion). If the non-relativistic wavelength were used to set the microscope's resolution specification, how would the specification be in error?
   *Tests: ability to apply the relativistic formula, quantify its importance, and connect wavelength to instrument resolution.*

---

## LLM Exercises

The following exercises are designed to be worked with a large language model as a thinking partner — not to get the answer, but to check reasoning, generate counterexamples, and push on the boundaries of your understanding.

1. Ask an LLM to explain the Davisson–Germer experiment as if to someone who has never heard of wave-particle duality. Then ask it to identify the single most important conceptual step in the explanation. Do you agree with its choice?

2. The de Broglie relation $\lambda = h/p$ was proposed by analogy with photons. Ask an LLM: what would it mean for the analogy to *fail*? What experimental result would have shown that $\lambda = h/p$ does not apply to electrons? Use this to think about what the Davisson–Germer experiment actually proved.

3. Tonomura's experiment is often described as showing that a single electron "goes through both slits at once." Ask an LLM whether this phrase is accurate, misleading, or somewhere in between — and why. Compare its answer to what the Born rule actually says about the wave function before and after measurement.

4. Ask an LLM to work through the de Broglie wavelength calculation for a thermal neutron at room temperature ($k_BT$ at $T = 293$ K, neutron mass $1.675 \times 10^{-27}$ kg). Then ask it: why is neutron diffraction used to locate hydrogen atoms in protein crystals when X-ray diffraction struggles with this task? Evaluate whether its reasoning is physically correct.

5. The 2019 Fein et al. experiment showed diffraction for molecules of approximately 2,000 atoms. Ask an LLM: what physical mechanism limits how large an object can show quantum interference? What is "decoherence," and why does it become more severe for larger, warmer objects? Ask it to give a concrete numerical estimate for when decoherence becomes important.

---

## References

de Broglie, L. (1924). *Recherches sur la théorie des quanta*. Doctoral thesis, Université de Paris. Published as *Annales de Physique*, 3 (1925), 22–128.

Davisson, C., & Germer, L. H. (1927). Diffraction of electrons by a crystal of nickel. *Physical Review*, 30(6), 705–741. doi:10.1103/PhysRev.30.705

Tonomura, A., Endo, J., Matsuda, T., Kawasaki, T., & Ezawa, H. (1989). Demonstration of single-electron buildup of an interference pattern. *American Journal of Physics*, 57(2), 117–120. doi:10.1119/1.16104

Merli, P. G., Missiroli, G. F., & Pozzi, G. (1976). On the statistical aspect of electron interference phenomena. *American Journal of Physics*, 44(3), 306–307.

Bach, R., Pope, D., Liou, S.-H., & Batelaan, H. (2013). Controlled double-slit electron diffraction. *New Journal of Physics*, 15, 033018. doi:10.1088/1367-2630/15/3/033018

Arndt, M., Nairz, O., Vos-Andreae, J., Keller, C., van der Zouw, G., & Zeilinger, A. (1999). Wave–particle duality of C₆₀ molecules. *Nature*, 401, 680–682. doi:10.1038/44348

Fein, Y. Y., Geyer, P., Zwick, P., Kiałka, F., Pedalino, S., Mayor, M., Gerlich, S., & Arndt, M. (2019). Quantum superposition of molecules beyond 25 kDa. *Nature Physics*, 15, 1242–1245. doi:10.1038/s41567-019-0663-9

Townsend, J. S. (2012). *A Modern Approach to Quantum Mechanics* (2nd ed.). University Science Books.

Griffiths, D. J., & Schroeter, D. F. (2018). *Introduction to Quantum Mechanics* (3rd ed.). Cambridge University Press.

---

## Running Project — Build the 1D Quantum Sandbox

**This chapter adds:** the spatial grid the entire solver runs on — $N$ uniformly spaced points $x_j = x_\text{min} + j\,h$ with spacing $h = (x_\text{max} - x_\text{min})/(N-1)$ — sized so that the de Broglie wavelength $\lambda = h_\text{Planck}/p$ of the states you care about is resolved by enough grid points to avoid aliasing.

### Exercise R1 — When to Use AI
**The judgment:** In this chapter's project work, AI assistance is appropriate for:
- Writing a `makeGrid(xMin, xMax, N)` helper that returns the array $x_j$ and the spacing $h$ — *Why AI works here:* this is a one-line utility, and you can check it against $h = (x_\text{max}-x_\text{min})/(N-1)$ by hand.
- Drafting a "points per wavelength" diagnostic that reports $\lambda/h$ for a chosen $k$ — *Why AI works here:* it is arithmetic on the de Broglie relation you already command, easy to verify.
**The tell:** You are using AI well when you have an independent way to check the output — here, the resolution rule $\lambda = 2\pi/k$ and the requirement of roughly $\geq 8$–10 grid points per wavelength.

### Exercise R2 — When NOT to Use AI
**The judgment:** These tasks require your judgment; AI output here can't be trusted without redoing the work:
- Choosing $N$ and the grid bounds for a given physical problem — *Why AI fails here:* this is a physical-resolution call. The AI will pick round numbers, but whether $N$ resolves the shortest wavelength present ($\lambda_\text{min} = h_\text{Planck}/p_\text{max}$) is a judgment the AI has no way to verify, and an under-resolved grid produces a smooth, plausible, wrong spectrum.
- Deciding whether the grid is wide enough to contain the states without truncation — *Why AI fails here:* too narrow a box clips the wave function at the boundary and shifts the energies; the output looks fine until you compare against an analytic value.
**The tell:** If you could not explain the result without the AI — if the AI is your *reason* rather than your *tool* — it did work that should have been yours.
**Physics-judgment connection:** This trains checking a numerical grid against the de Broglie wavelength of the physics it must represent — a resolution check that prevents aliasing and boundary truncation before any energy is computed.

### Exercise R3 — LLM Exercise
**What you're building this chapter:** the grid-construction module plus a de Broglie resolution diagnostic that tells you whether a chosen $N$ resolves the states.
**Tool:** Claude chat — a small self-contained utility against the existing governing files; no persistent state beyond `constants.js`.
**The Prompt:**
```
Using the Chapter 0 CLAUDE.md and the Chapter 1 constants.js as binding
context, build grid.js and a small demo page 02-grid-resolution.html.

grid.js exports makeGrid(xMin, xMax, N) returning { x: Float64Array, h: number }
with x_j = xMin + j*h and h = (xMax − xMin)/(N − 1), plus a helper
pointsPerWavelength(k, h) = (2π/k)/h that reports how many grid points cover
one de Broglie wavelength λ = 2π/k (with p = ℏk).

02-grid-resolution.html: sliders for N (50–2000), x-range (±5 to ±50 nm), and
electron kinetic energy E (0.1–500 eV). From E compute p = √(2 m_e E),
k = p/ℏ, λ = h_Planck/p, and display λ in nm and pointsPerWavelength. Color
the readout green if ≥ 10 points/λ, yellow if 5–10, red if < 5. Plot a single
sample plane wave Re(e^{ikx}) on the grid so under-resolution is visible as a
jagged, aliased curve.

Do NOT solve any Schrödinger equation here — this page only sizes the grid.
After writing, list three checks I can run, including the 150 V electron case
where λ ≈ 0.1 nm.
```
**What this produces:** `grid.js` (used by every solver mode from Chapter 3 on) and a page that shows, visually, when a grid is too coarse for the physics.
**How to adapt:** *Your system:* if you work in atomic units elsewhere, keep `grid.js` in SI and convert at the display layer only. *ChatGPT/Gemini:* paste `constants.js` alongside the prompt. *Claude Project:* add `grid.js` to Project knowledge so Chapter 3's ψ array imports the same grid.
**Builds on:** the constants and units harness from Chapter 1.  **Next:** Chapter 3 puts a complex ψ array on this grid and applies the Born rule.

### Exercise R4 — CLI Exercise
**What you're building this chapter:** a grid module with an automated resolution assertion you can run before any later eigensolver trusts the grid.
**Tool:** Claude Code — it can add the module, run a resolution check across parameter values, and record the safe ranges in `PROJECT.md`.
**Skill level:** Beginner
**Setup — confirm:**
- [ ] `constants.js` from Chapter 1
- [ ] Node.js available
- [ ] The CLAUDE.md self-check rule from Chapter 1
**The Task:**
```
Read constants.js. Create grid.js with makeGrid(xMin, xMax, N) and
pointsPerWavelength(k, h) as specified. Write a Node script check-grid.js that,
for an electron at E = 150 eV (λ ≈ 0.1 nm) on x ∈ [−20 nm, +20 nm], finds the
smallest N (multiple of 100) giving ≥ 10 points per de Broglie wavelength, and
prints both N and the resulting points-per-λ. Do NOT change makeGrid's
spacing formula. Append to PROJECT.md under "Verified":
"Ch2 grid: 150 eV electron needs N ≥ <value> for 10 pts/λ on ±20 nm".
```
**Expected output:** `grid.js`, `check-grid.js`, a printed minimum $N$, and a `PROJECT.md` line.
**What to inspect:** that doubling $N$ roughly doubles points-per-$\lambda$ (linear in $N$), confirming the spacing formula is right; and that the reported $\lambda$ matches the hand value $h_\text{Planck}/\sqrt{2m_eE} \approx 0.1$ nm at 150 eV.
**If it goes wrong:** if points-per-$\lambda$ does not scale with $N$, the spacing used $(x_\text{max}-x_\text{min})/N$ instead of $/(N-1)$ — an off-by-one that silently mis-sizes the grid; fix the formula, not $N$.
**CLAUDE.md / AGENTS.md note:** add: "Before any eigensolve, assert the grid resolves the shortest expected wavelength to ≥ 8 points; otherwise widen N or narrow the energy range."

### Exercise R5 — AI Validation Exercise
**What you're validating:** the grid module and resolution diagnostic from R3/R4.
**Validation type:** Code + Numerical result
**Risk level:** Low — the de Broglie relation gives an exact target $\lambda$ to check against.
**Setup:** use your own R3/R4 artifacts.
**The Validation Task:** Evaluate against this checklist; mark Pass / Fail / Cannot determine with reasoning.
```
Validation Checklist — Spatial grid and de Broglie resolution
□ Correctness: is h = (xMax − xMin)/(N − 1), and x_0 = xMin, x_{N−1} = xMax?
□ Completeness: does the page report λ, points-per-λ, AND flag under-resolution?
□ Scope: did it sneak in a Schrödinger solve it was told to leave out?
□ Physics criterion 1: at 150 V (E = 150 eV → 150 eV here is non-rel.), λ ≈ 0.1 nm?
□ Physics criterion 2: does the aliased plane wave look jagged when pts/λ < 5?
□ Failure-mode check: any of —
  - fluent but wrong (off-by-one in h via /N instead of /(N−1))
  - λ computed from kinetic energy with a missing factor of 2 (p = √(2mE))
  - grid too narrow to contain the intended states (boundary truncation later)
  - silent unit slip (k in nm⁻¹ vs m⁻¹ mismatched against ℏ in SI)
```
**What to do with findings:** pass → use it; one fail → fix the spacing or the $p = \sqrt{2mE}$ factor and re-run; multiple fails / cannot-determine → recompute $\lambda$ and the needed $N$ by hand, since the grid sizes everything downstream.
**AI Use Disclosure (mandatory, two sentences):**
> *1:* The AI wrote the grid-construction module and the de Broglie resolution diagnostic page.
> *2:* The AI could not decide whether a given $N$ actually resolves the physics of interest — I made the resolution call against $\lambda = h/p$ myself, because an under-resolved grid yields a plausible but wrong spectrum.
**Physics-judgment connection:** trains the habit of sizing a numerical grid against the de Broglie wavelength it must represent, catching aliasing and truncation before they corrupt a spectrum.
