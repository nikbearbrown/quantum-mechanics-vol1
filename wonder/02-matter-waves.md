# Chapter 2 — Matter Waves: de Broglie, Davisson–Germer, and the Double Slit
*The accident that proved every moving thing is also a wave.*

It is 1926, and Lester Germer is staring at a problem he does not yet realize is a discovery. For months he and Clinton Davisson had been firing electrons at a nickel surface and noting where they bounced. The results were aggressively boring: a smooth, shapeless blob of electrons spraying off in every direction, exactly what you would get from throwing marbles at a rough wall. Then a flask of liquid air burst near the rig. The vacuum tube cracked. Air rushed in, oxidized the nickel, and ruined weeks of careful work. To salvage the target they baked it — heated it slowly until the oxide cooked off. And when they switched the experiment back on, the boring blob had vanished. In its place stood sharp peaks at particular angles.

What had they done? Without meaning to, they had cooked the polycrystalline nickel into a single crystal. A single crystal has neat, regular atomic planes — the very planes that William Lawrence Bragg had shown would diffract X-rays. The electrons, it turned out, were behaving precisely the way X-rays do when they scatter off a crystal lattice. Not because anyone planned it. Because the physics had no choice.

And the strange thing is, two years earlier a graduate student in Paris had seen it coming. Louis-Victor de Broglie had argued — in a thesis his committee very nearly threw out — that if light waves can act like particles, which is what Einstein's 1905 photoelectric work had shown, then surely particles of matter ought to act like waves. The symmetry is almost too clean to resist. Einstein had shown that electromagnetic waves carry momentum $p = h/\lambda$. De Broglie simply read the equation right-to-left: a particle carrying momentum $p$ should have a wavelength

$$\lambda = \frac{h}{p}.$$

The committee, unsure what to make of it, asked Einstein. Einstein called the idea brilliant, and the thesis passed. De Broglie won the Nobel Prize in 1929 — to this day the only one ever given for a doctoral thesis. Seen in that light, the Davisson–Germer accident was simply the confirmation arriving on schedule. But the confirmation dragged a much harder question in behind it, one the tidy formula does not touch: what, exactly, is doing the waving?

<!-- → [IMAGE: photograph or schematic of the Davisson–Germer apparatus — showing the electron gun, rotatable detector, and nickel crystal target; caption should note the accidental annealing that converted the sample to a single crystal] -->

![photograph or schematic of the Davisson–Germer apparatus — showing the electron gun, rotatable detector, and nickel crystal target](../images/02-matter-waves-fig-01.png)
*Figure 2.1 — photograph or schematic of the Davisson–Germer apparatus — showing the electron gun, rotatable detector, and nickel crystal target*

---

## The Formula and What It Means

Let me start with what de Broglie actually wrote down, and then chase what it forces. For a non-relativistic particle with kinetic energy $K$ and mass $m$, momentum and energy are tied together by $K = p^2/2m$, so $p = \sqrt{2mK}$. Slide that in:

$$\lambda = \frac{h}{\sqrt{2mK}}.$$

For a charged particle of charge $e$ accelerated from rest through a potential difference $V$, the kinetic energy is $K = eV$, giving

$$\lambda = \frac{h}{\sqrt{2meV}}.$$

For electrons specifically — and you will be reaching for this constantly — the numbers collapse into a handy shortcut:

$$\lambda_{\text{electron}} \approx \frac{1.226\text{ nm}}{\sqrt{V\text{ (in volts)}}}.$$

Put in 150 volts and out comes $\lambda \approx 0.1$ nm. A tenth of a nanometer. One ångström. Now, that number is not a coincidence dropped from the sky — it is, near enough, the spacing between atoms in a solid. And there is the whole secret to why diffraction works: a wave only diffracts off a grating when its wavelength is about the size of the grating's spacing. X-rays can do it because their wavelengths sit in the ångström range. De Broglie's formula is telling you that an electron pushed through a few hundred volts lands in that exact same range. *That* is why Davisson and Germer saw anything at all, and why Bragg's law — invented entirely for X-rays — worked on electrons without changing a single symbol.

Now let me head off a wrong picture before it takes root, because almost everyone forms it. The wavelength is *not* the physical size of the electron. The classical electron radius is around $2.8 \times 10^{-15}$ m — eight orders of magnitude smaller than the 0.167 nm de Broglie wavelength of a 54 eV electron. So the wavelength is not how big the electron is; it is a property of the electron's *state of motion*. This matters enormously the first time you meet the idea, because the tempting cartoon — a tiny ball with little ripples decorating it — is just wrong. The wave and the particle are not two parts you can pry apart. The wave *is* the thing, in the precise sense that the wave is the only object that evolves smoothly and predictably between observations.

<!-- → [TABLE: de Broglie wavelengths for several particles — columns: particle, mass, speed or energy, λ; rows: electron at 54 eV (the Davisson–Germer case), proton at same kinetic energy, C₆₀ buckyball at 900 K, 70 kg person walking at 1 m/s; the last row makes the classical limit visceral] -->

De Broglie's idea was not pulled out of thin air, and the logic underneath it is worth tracing. Einstein's special relativity had required energy and momentum to travel together as a four-vector. De Broglie noticed that frequency and wave vector — the spatial frequency $1/\lambda$ — also pack together as a four-vector. For a photon, the single relation $E = h\nu$ links those two four-vectors through one constant, $h$. De Broglie's leap was to assert that the *same* constant links them for any particle, photon or not. So this was a symmetry argument, not a fit to data. The data showed up afterward to confirm what the symmetry had already insisted on.

---

## The Davisson–Germer Experiment

Rebuild the 1927 result from scratch and you will see exactly why it convinced everyone.

Davisson and Germer measured a sharp diffraction peak at 50° for electrons accelerated through 54 V. What wavelength does de Broglie assign a 54 eV electron?

$$p = \sqrt{2 \times (9.109 \times 10^{-31}) \times (54 \times 1.602 \times 10^{-19})} = 3.970 \times 10^{-24}\text{ kg m s}^{-1}$$

$$\lambda = \frac{6.626 \times 10^{-34}}{3.970 \times 10^{-24}} \approx 0.167\text{ nm.}$$

The relevant crystal planes in nickel are the (111) planes of the face-centered cubic lattice, with spacing $d = 0.091$ nm. Bragg's law for first-order diffraction:

$$2d\sin\theta_{\text{Bragg}} = \lambda \implies \sin\theta_{\text{Bragg}} = \frac{0.167}{2 \times 0.091} = 0.918 \implies \theta_{\text{Bragg}} \approx 66.6°.$$

The scattering angle measured from the forward beam in the Davisson–Germer geometry converts to roughly 47° — close to the observed 50°, but not exact. And the small leftover gap is not a crack in de Broglie's idea. It comes from a real physical effect: an electron entering a metal crystal feels an attractive inner potential that nudges it faster and shortens its wavelength once inside. Correct for that inner potential and the prediction snaps into exact agreement.

This is the anatomy of a real quantitative triumph, and it is worth naming the parts. A parameter-free prediction, assembled from quantities ($h$, $m_e$, $d$) measured in completely unrelated experiments, is checked against an angle that came out of yet another experiment — one that was not even designed to test the prediction. The match is not "roughly." It is exact, once you account for all the physics.

Davisson and Germer themselves did not fully grasp what they had until Davisson sailed to Europe and talked it over with Max Born, James Franck, and others who had been chewing on de Broglie's and Schrödinger's new wave mechanics. Meanwhile, George Paget Thomson was running a parallel experiment in Aberdeen — firing electrons through thin metal films and getting rings, the Debye–Scherrer pattern you see in polycrystalline X-ray diffraction. Thomson and Davisson split the 1937 Nobel Prize. (Davisson–Germer, *Physical Review* **30**, 705–740 (1927). doi:10.1103/PhysRev.30.705)

<!-- → [FIGURE: diagram of Bragg diffraction geometry applied to the Davisson–Germer case — showing incident and reflected electron beams, crystal planes separated by d = 0.091 nm, path-length difference of 2d sin θ, and the condition for constructive interference; contrast with a polycrystalline diffraction ring geometry for Thomson's version] -->

![diagram of Bragg diffraction geometry applied to the Davisson–Germer case — showing incident and reflected electron beams, crystal planes…](../images/02-matter-waves-fig-02.png)
*Figure 2.2 — diagram of Bragg diffraction geometry applied to the Davisson–Germer case — showing incident and reflected electron beams, crystal planes…*

There is a fine point of logic here that I do not want to let slide by. The Davisson–Germer experiment does *not* prove that electrons "are" waves in any classical sense — it does not prove they are extended oscillations rippling through a medium, the way sound ripples through air. What it proves is narrower and stranger: electrons produce interference and diffraction that can only be *calculated* using wave mechanics. The distinction is not pedantry. The very same electron that builds up a diffraction peak shows up at the detector as a single localized event — one click, one dot, in one place.

---

## Single Electrons, One at a Time

The hardest version of the experiment — and for exactly that reason the most illuminating — is the one Akira Tonomura and colleagues at Hitachi pulled off in 1989. They built a double-slit setup with an electron biprism: a fine wire held at positive voltage that splits an electron beam into two coherent paths, which is physically the same thing as two slits. Then they turned the beam down so far that, at any given instant, there was less than one electron inside the whole apparatus. Each electron struck a position-sensitive detector and was recorded as a single localized dot.

Now watch the pattern assemble, because this is the part that should make the hair stand up:

At ten electrons, you have ten random-looking dots. No order, no hint of anything. At two hundred, there is a faint suggestion of clustering, nothing you would bet on. At six thousand, stripes start to surface out of the noise. At seventy thousand, there is no arguing with it: a crisp interference pattern, bright and dark fringes marching across the detector — the exact pattern you predict by treating each electron as a wave passing through both paths at once.

And here is what makes it impossible to wave away. The electrons did not interfere with *each other* — there was never more than one in the apparatus. Each one arrived as a particle, a single point, and dropped one dot onto the pattern. Yet the accumulated distribution of those lonely dots has the mathematical fingerprint of wave interference. The conclusion is forced, not optional: each individual electron's wave function passed through *both* arms of the apparatus and interfered with itself. The dot is where the wave function collapsed when the measurement happened. The pattern is the piled-up probability, and that probability was set by a wave that explored the entire geometry on every single pass.

Tonomura's 1989 paper is the most famous demonstration of its kind, but it was not the first. The first single-electron buildup was shown by Pier Giorgio Merli, Giulio Missiroli, and Gianfranco Pozzi in Bologna in 1974 (published 1976 in *American Journal of Physics*). Their experiment was voted one of the most beautiful in all of physics in a 2002 *Physics World* poll. And the first experiment to use physically nano-fabricated real double slits — actual gaps cut in a membrane, not a biprism — was Bach et al. in 2013. (Tonomura et al., *Am. J. Phys.* **57**, 117–120 (1989). doi:10.1119/1.16104; Bach et al., *New J. Phys.* **15**, 033018 (2013). doi:10.1088/1367-2630/15/3/033018)

<!-- → [CHART: sequence of detector images from the single-electron buildup — showing the pattern at approximately 10, 200, 6,000, and 70,000 electrons; this is the most important visual in the chapter and must show both the particle nature (individual dots) and wave nature (emerging fringes)] -->

![sequence of detector images from the single-electron buildup — showing the pattern at approximately 10, 200, 6,000, and 70,000 electrons](../images/02-matter-waves-fig-03.png)
*Figure 2.3 — sequence of detector images from the single-electron buildup — showing the pattern at approximately 10, 200, 6,000, and 70,000 electrons*

Now, what does this experiment *rule out*? This is the part students most need to hear slowly. It rules out any model in which the electron rides a definite path through one slit or the other. Because if electrons had definite trajectories, then dribbling them through one at a time would change nothing — you would simply get two bright stripes behind the two slits, with darkness between. You do not get that. You get fringes that reach well into the geometric shadow where no straight-line trajectory could deposit anything. The pattern depends on the separation of *both* slits, even though each electron is only ever caught in one spot.

There is a clever escape people reach for: maybe the electron really does go through one slit, but somehow the act of not being detected at the other slit nudges the outcome. It is a tempting move, and it is dead on arrival. You can widen the slits as much as you like and make the detector as gentle as you like, and the interference survives — as long as you do not acquire information about which slit the electron used. What kills the interference is not a physical jostle. It is information. Knowledge of the path, not disturbance of the electron, is what erases the fringes.

---

## Why Human-Scale Objects Don't Diffract

The de Broglie relation is not picky. It applies to everything — not just electrons, not just "quantum particles." Anything with momentum carries a wavelength. The only question that ever matters is whether that wavelength is big enough to do anything you could notice.

Take a proton accelerated through the same 54 V. It has 1836 times the electron's mass, so at the same kinetic energy its momentum is $\sqrt{1836}$ times larger, and its wavelength is $\sqrt{1836} \approx 43$ times *smaller* — about 4 pm. That is still in the range where crystal diffraction is doable, which is why neutron and proton diffraction are genuine tools in materials science, not curiosities.

Push further. A $\text{C}_{60}$ buckyball — sixty carbon atoms, mass around 720 atomic mass units — was diffracted off a grating with 50 nm slits by Anton Zeilinger's group in Vienna in 1999. At the oven temperature of 900 K, the de Broglie wavelength works out to roughly 2.5 pm — *smaller than the molecule itself.* And yet the fringes appeared. The 2019 experiments by Fein and colleagues pushed this all the way to molecules of about 2,000 atoms. (Arndt et al., *Nature* **401**, 680–682 (1999). doi:10.1038/44348; Fein et al., *Nat. Phys.* **15**, 1242–1245 (2019). doi:10.1038/s41567-019-0663-9)

Now compute the wavelength of a 70 kg person walking at 1 m/s:

$$\lambda = \frac{6.626 \times 10^{-34}}{70 \times 1} \approx 10^{-35}\text{ m.}$$

That is something like twenty orders of magnitude smaller than a proton. No slit, no crystal lattice, no instrument that could ever be built, could resolve a wavelength that small. So here is the honest statement of the classical limit, and it is more interesting than "quantum mechanics turns off." Quantum interference is not *absent* for big objects — it is present, and utterly invisible. Quantum mechanics does not break down at human scales. It simply becomes indistinguishable from classical mechanics, because the wavelengths shrink past any aperture nature or engineering could supply to reveal the fringes.

This is Bohr's correspondence principle made concrete and quantitative: quantum mechanics contains classical mechanics as the limiting case where the system's action is enormous compared to $\hbar$. The de Broglie wavelength turns that limit from a slogan into a calculation. You do not need a philosophy seminar to see where the quantum world fades into the classical one. You just compute $h/p$ and read off the answer.

<!-- → [INFOGRAPHIC: scale comparison — showing λ for electron at 54 eV (0.167 nm), thermal neutron (~1 Å), C₆₀ at 900 K (~2.5 pm), and 70 kg person walking (10⁻³⁵ m), placed on a logarithmic scale alongside reference lengths: proton radius, hydrogen atom, visible light wavelength, human hair; the goal is to make viscerally clear why quantum wavelengths are measurable for small particles and invisible for large ones] -->

---

## What the Wave Function Is Not Yet

De Broglie told you there is a wave. He did not tell you what it is a wave *of*. That is the harder question, and the answer arrived — provisionally, and amid real controversy — from Max Born in 1926, the same year Davisson's tube cracked. Born proposed that the wave function $\psi(x,t)$ is not a physical wave rippling through space, like water or sound. Instead, its squared modulus $|\psi(x,t)|^2$ is a probability density: the probability of finding the particle at position $x$ at time $t$, *if you go and look*.

And you cannot derive this from the de Broglie relation. It is a separate postulate, bolted on — and it is the one that makes quantum mechanics genuinely strange rather than merely unfamiliar. The wave function is a wave of probability amplitude: complex-valued, not directly observable, and yet entirely real in the only sense that matters, because it predicts observable interference.

Tonomura's experiment is Born's rule made visible. The interference pattern that piles up dot by dot is exactly the pattern $|\psi|^2$ predicts. The dots themselves are random — you cannot say where the next electron will land, ever. But their distribution, after enough of them, converges onto $|\psi|^2$ computed from the wave equation. And the randomness, as far as anyone has ever been able to determine, is not ignorance of some hidden machinery underneath. It is irreducible. There is no smaller story.

The bridge between the de Broglie wavelength and the wave function $\psi$ is not loose analogy — it is exact. A state of definite momentum $p$ is a plane wave $\psi(x) \propto e^{ipx/\hbar}$, a function that oscillates with spatial period $\lambda = h/p = 2\pi\hbar/p$. That is de Broglie's wavelength, popping right back out as the spatial period of the quantum state. Chapter 3 takes up what the wave function means precisely, how it is normalized, and why $|\psi|^2$ gives probabilities. Chapter 4 gives the equation that governs how $\psi$ evolves.

Let me leave you with one puzzle to carry forward into those chapters, because it is the seed of everything. A state of definite momentum has a perfectly definite wavelength — but the plane wave $e^{ipx/\hbar}$ stretches across *all* space. It is nowhere in particular; it has no localization at all. So if you want a particle that actually sits somewhere — confined to a finite region — you cannot use one pure momentum. You have to pile up plane waves of many different momenta. Superpose a spread of momenta $\Delta p$ and you build a packet localized to a width $\Delta x \sim h/\Delta p$. Notice: this is not a theorem of quantum mechanics. It is a theorem of Fourier analysis, old and unavoidable. And in the next chapter, dressed in physical clothing, it becomes the Heisenberg uncertainty principle.

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
