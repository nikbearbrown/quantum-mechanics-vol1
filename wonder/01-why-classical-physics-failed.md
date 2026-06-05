# Chapter 1 — Why Classical Physics Failed: Blackbody, Photoelectric, and the Photon

Picture a poker shoved into a blacksmith's forge. As the iron heats it glows — first a dull red, then orange, then a yellow-white. The color climbs. And here is the curious part: it is not *this* particular poker that climbs through those colors. Any iron does it. So does any ceramic, any lump of anything, as long as it sits at the same temperature. Same temperature, same color, same spectrum. By 1900 Lummer and Pringsheim had pinned those spectral curves down with beautiful precision — smooth humps, reproducible to a fraction of a percent. And every physicist in Europe knew exactly what the best theory of the day predicted for those curves, and knew, just as exactly, how spectacularly it failed.

The prediction was infinite energy. Not "a great deal." Infinite. Take that seriously for a second: a warm poker, left sitting in a room, should fry you with ultraviolet pouring off the walls. It obviously doesn't. You can stand next to a fire and keep your skin. That gap — between what the theory insisted on and what plainly happens — was, to put it gently, a problem worth losing sleep over.

---

## How You Get Infinite Energy from Perfectly Good Physics

Let me walk you into the trap, because each step is clean and reasonable, and that is exactly what makes the ending so alarming. Inside a cavity at temperature $T$, the electromagnetic field can wiggle at any frequency it likes. Count up how many ways it can wiggle — how many standing-wave modes fit in the box — and you find there are

$$\frac{8\pi\nu^2}{c^3}$$

modes per unit volume per unit frequency interval. Nobody argues with this part. It is pure geometry, a fact about how standing waves pack into a box, and it is right.

Now you have to put energy into each mode. The classical rule for that is equipartition: every degree of freedom in thermal equilibrium at temperature $T$ carries, on average, $\frac{1}{2}k_BT$. An electromagnetic mode has two ways to store energy — in the electric field and in the magnetic field — so it carries $k_BT$. Multiply the energy per mode by the count of modes:

$$u(\nu, T) = \frac{8\pi\nu^2}{c^3}\,k_BT.$$

This is the Rayleigh–Jeans law, and at long wavelengths it is lovely — it matches the measurements. But now follow it the wrong way, toward short wavelengths. The mode count climbs as $\nu^2$, and each mode is handed the same flat $k_BT$ no matter how high its frequency. The product runs away. Integrate over all frequencies and you get infinity. They called it the ultraviolet catastrophe, which, as disaster names go, is more honest than most.

So where is the lie? It is not in the mode counting — that was solid. And equipartition is not wrong in general; it works gorgeously for ideal gases (set the low-temperature heat-capacity puzzles aside for now). The poison is buried in one quiet assumption: that energy can be ladled into a mode *continuously*, with no smallest spoonful. Any mode, however fast it oscillates, can hold any amount from zero on up, and on average it holds $k_BT$. That assumption — no smallest chunk — is what kills you.

---

## Planck's Desperate Remedy

Max Planck was not hunting for quantum mechanics. He had no idea it was there to be found. He was trying to fit a curve. He had Lummer and Pringsheim's data on his desk and he wanted a formula that would lie down on top of it. So he worked backward from the measurements — a perfectly respectable thing to do, if you are honest that that is what you are doing — and he found that the only way to make the total energy come out finite was to twist the entropy of a resonator in one very particular way.

What the twist amounted to was this. Suppose the oscillators in the cavity walls cannot hold just any energy at all. Suppose they are allowed only the values $0, h\nu, 2h\nu, 3h\nu, \ldots$ — whole-number multiples of a basic unit $h\nu$, with $h$ a brand-new constant. Then you no longer integrate over a smooth continuum (which would have handed you the flat $k_BT$). Instead you sum a discrete geometric series, and out comes:

$$\langle E \rangle = \frac{h\nu}{e^{h\nu/k_BT} - 1}.$$

This is the Planck average energy per mode. Multiply by the mode density and you have the **Planck distribution**:

$$u(\nu, T) = \frac{8\pi h\nu^3}{c^3} \cdot \frac{1}{e^{h\nu/k_BT} - 1}.$$

Now do the two checks that any new formula has to survive. Go to low frequencies, where $h\nu \ll k_BT$. Expand the exponential: $e^{h\nu/k_BT} \approx 1 + h\nu/k_BT$, the denominator collapses to $h\nu/k_BT$, and the whole expression melts back into $k_BT$. So Planck's formula agrees with classical physics in exactly the region where classical physics was already correct — which is the mark of a good theory, not a lucky one. Now go the other way, to high frequencies, $h\nu \gg k_BT$. The exponential becomes gigantic, the $-1$ is a rounding error, and $u$ dies off like $e^{-h\nu/k_BT}$. The exponential strangles the polynomial. No catastrophe.

The constant $h$ that Planck fitted to the Berlin data came out to $6.55 \times 10^{-34}$ J·s. Today's accepted value is $6.626 \times 10^{-34}$ J·s — his very first fit landed within one percent.

But here is the thing I most want you to hold onto, because the textbooks blur it. Planck quantized the *oscillators in the walls*, not the electromagnetic field itself. In his picture the field was still perfectly classical. The wall oscillators could only swap energy with the field in lumps of $h\nu$ — but between swaps the field did whatever Maxwell's equations told it to. And Planck *hated* this. He spent years trying to weasel out of the discrete energies, to rederive his own formula without them. He never managed it, because it cannot be done. But the genuinely radical step — saying that *the field itself* comes in lumps, that light is made of particles — that step was not his to take. He would not go there.

---

## What the Spectral Peak Tells You

From the Planck distribution you can derive Wien's displacement law by finding where $\partial u/\partial\nu = 0$. The algebra is not hard — you get a transcendental equation whose solution is $x = h\nu/k_BT \approx 2.821$, so

$$\nu_\text{max} = 2.821\,\frac{k_BT}{h}.$$

So the peak frequency rides directly on temperature. Double the temperature and you double the peak frequency, halving the peak wavelength. Run the numbers: at $T = 5778$ K — the surface of the Sun — the peak wavelength comes out near 501 nm, which is green. At $T = 3000$ K, a tungsten filament, the peak is around 966 nm, deep in the infrared. Which is to say most of what an incandescent bulb radiates is light you cannot see at all. That is why we gave up on them.

One subtlety is worth pausing over, because it trips people up. The peak *in frequency* and the peak *in wavelength* are not the same place. Take $\nu_\text{max}$, convert it to a wavelength by $\lambda = c/\nu$, and you will *not* land on the $\lambda_\text{max}$ that Wien's law gives in wavelength form. That is not a contradiction — it is the honest consequence of $d\nu$ and $d\lambda$ not being proportional to each other. The spectral density per unit frequency and the spectral density per unit wavelength are genuinely different functions. Both are legitimate. They just describe the same spectrum in two different coordinate systems.

---

## Worked Example — Twenty Orders of Magnitude

At $T = 3000$ K and $\nu = 3 \times 10^{15}$ Hz (ultraviolet), how wrong is Rayleigh–Jeans?

Both formulas share the mode density $8\pi\nu^2/c^3$. The ratio of Planck to Rayleigh–Jeans is just the ratio of the average energies per mode:

$$\frac{u_\text{Planck}}{u_\text{RJ}} = \frac{h\nu/k_BT}{e^{h\nu/k_BT} - 1}.$$

Compute $h\nu = (6.626\times10^{-34})(3\times10^{15}) = 1.988\times10^{-18}$ J $= 12.4$ eV. And $k_BT = (1.381\times10^{-23})(3000) = 4.14\times10^{-20}$ J $= 0.259$ eV. So $x = h\nu/k_BT \approx 47.9$.

Then $e^{47.9} \approx 7\times10^{20}$, and

$$\frac{u_\text{Planck}}{u_\text{RJ}} \approx \frac{47.9}{7\times10^{20}} \approx 7\times10^{-20}.$$

Twenty orders of magnitude. Sit with that number for a moment. At ultraviolet frequencies and ordinary-ish temperatures, classical physics is not a little off, not "approximately wrong" — it overshoots reality by a factor of a hundred billion billion. The dial that controls everything is $x = h\nu/k_BT$. When $x \ll 1$ the two theories shake hands. When $x \gg 1$ they fly apart by factors that grow like $e^x$. And the crossover, $h\nu \sim k_BT$, is precisely the line where quantization stops being a footnote and starts running the show.

---

## A Completely Different Crisis

While Planck was fitting curves in Berlin, an entirely separate puzzle was simmering, and it had nothing to do with hot pokers. Back in 1887 — the very year he proved electromagnetic waves were real and vindicated Maxwell — Heinrich Hertz had noticed something odd on the side: ultraviolet light striking a metal made it spit sparks. Philipp Lenard pinned down by 1902 that the sparks were electrons. By 1914 Robert Millikan had measured everything about the effect there was to measure. And the data said three things, each one of them flatly impossible to square with the wave picture of light:

**First**, there is a threshold frequency. Below some $\nu_0$ that depends on the metal, no electrons come off — none, ever, at any brightness you care to throw at it. Blast sodium with a dazzling red arc lamp and you liberate nothing. Touch it with a feeble ultraviolet lamp and electrons fly off immediately. Brightness is beside the point; frequency is everything.

**Second**, the maximum kinetic energy of the ejected electrons depends on frequency but not on intensity. Double the brightness of the light, and you get twice as many electrons per second, but each electron has the same energy as before.

**Third**, emission begins with no measurable time delay — within nanoseconds, at any intensity above the threshold.

Every one of these is a slap in the face to the wave picture. In a wave, energy washes over the surface continuously and evenly. So there should be no threshold — give it long enough, and any frequency at sufficient brightness ought to pool up the energy needed to kick an electron loose. The time delay should *grow* as you dim the light. And the kinetic energy should track how hard the wave shoves, which means intensity, not frequency. The wave theory gets every single detail backward.

---

## Einstein's Light Quanta

Then, in 1905, Einstein said something genuinely reckless. Not merely that oscillators trade energy in lumps — Planck had already said that, grudgingly. Einstein went further: light energy is *not spread out continuously at all*. It travels in discrete packets, and each packet carries energy

$$E = h\nu.$$

He called them *Lichtquanten* — light quanta. We call them photons.

Here is the picture, and it explains everything in one stroke. A single photon hits the metal and is swallowed whole by a single electron. If $h\nu$ falls short of the energy needed to rip that electron free of the metal — the **work function** $\Phi$ — the electron stays put, and it does not matter how many photons per second you rain down. None of them helps; each acts alone. But if $h\nu > \Phi$, the electron escapes, and whatever energy is left over becomes its kinetic energy:

$$K_\text{max} = h\nu - \Phi.$$

This is Einstein's photoelectric equation. The **stopping potential** $V_\text{stop}$ — the reverse voltage needed to halt the fastest electrons — satisfies

$$eV_\text{stop} = K_\text{max} = h\nu - \Phi.$$

Now watch every mystery dissolve. There is a threshold because a photon with $h\nu < \Phi$ simply cannot do the job — not "almost, if only the next one chipped in," but genuinely, permanently cannot, because each photon acts alone. The kinetic energy tracks frequency because it tracks the photon energy $h\nu$, which frequency alone decides. Intensity? That only sets how many photons arrive each second, nothing more. And the missing time delay is the most natural thing in the world: one photon, one electron, done.

The lovely twist is that Millikan set out around 1914 to *demolish* this idea. He thought the photon was nonsense. So he spent two years doing exquisitely careful work — freshly scraped metal surfaces, hard vacuum — measuring $V_\text{stop}$ against $\nu$ for sodium, lithium, and potassium. And every metal handed him the same slope: $h/e = 4.136\times10^{-15}$ V·s. Einstein's equation fit perfectly, dead on. Millikan published the confirmation in 1916, noting drily that the result came "in spite of my personal conviction," and collected the Nobel Prize in 1923 specifically for this measurement of $h$. Einstein won his in 1921 specifically for the photoelectric effect — not, as people assume, for relativity.

---

## Worked Example — Stopping Potential for UV on Sodium

Ultraviolet light with wavelength $\lambda = 300$ nm strikes sodium. The work function of sodium is $\Phi = 2.28$ eV. What is the stopping potential?

The shortcut $hc = 1240$ eV·nm makes this fast:

$$E = \frac{1240\ \text{eV}\cdot\text{nm}}{300\ \text{nm}} = 4.13\ \text{eV}.$$

Then $K_\text{max} = 4.13 - 2.28 = 1.85$ eV, and

$$V_\text{stop} = 1.85\ \text{V}.$$

Now try green light at $\lambda = 546$ nm. Then $E = 1240/546 \approx 2.27$ eV — a hair *below* the work function $\Phi = 2.28$ eV. So: no electrons. Not one. Not with a 10,000-watt lamp blazing away. The photon energy sits under the threshold, and no pile of sub-threshold photons ever adds up to one that clears it. Brightness cannot buy you what frequency refuses to provide.

---

## Wave and Particle — Not an Either/Or

Now we have a genuine collision, and you should feel the weight of it. By 1905 the wave nature of light was not a hunch — it was a fortress. Young's double-slit experiment in 1801, Maxwell's electromagnetic theory in 1865, Hertz's radio waves in 1887: half a century of airtight evidence said light is a wave. Interference, diffraction, polarization — none of it is possible with bullets. And yet here is Einstein, with equally airtight evidence, saying light comes in particles. How can both be right?

The resolution is *not* that light "sometimes" acts as a wave and "sometimes" as a particle, flipping between two costumes depending on which experiment you run. That story makes it sound as though light has a split personality, switching moods, and that is simply not what happens. The quantum description is one thing, not two: light is always described by a probability amplitude — a wave. That wave tells you where detection events are likely. The detection events themselves, when they happen, are discrete and localized. The wave is real. The particle is real. They were never two separate things you had to choose between.

Arthur Compton slammed the last door shut in 1923. Fire X-rays at graphite, and the scattered X-rays come back with a *longer* wavelength than they went in with. The shift is

$$\Delta\lambda = \frac{h}{m_e c}(1 - \cos\theta),$$

where $\theta$ is the scattering angle and $h/(m_e c) = 2.426\times10^{-12}$ m is the Compton wavelength of the electron. You get this formula by treating the photon as a particle carrying momentum $p = h/\lambda = E/c$ and working out an elastic collision with an electron using relativistic kinematics — billiard balls, basically. Classical wave theory predicts no wavelength shift whatsoever — none. The experiment is brutally unambiguous, and the particle picture wins this round. Compton took the Nobel Prize in 1927.

---

## The Constant That Tells You When Quantum Mechanics Matters

Two numbers stake out the quantum scale:

$$h = 6.62607015\times10^{-34}\ \text{J}\cdot\text{s}, \qquad \hbar = \frac{h}{2\pi} = 1.054571817\times10^{-34}\ \text{J}\cdot\text{s}.$$

Look at the units: J·s — energy times time, or equally momentum times length. That combination is called **action**, the same quantity that runs through Lagrangian mechanics. So Planck's constant is *not* an energy, and it is worth being stubborn about this. The energy is $h\nu$. The momentum is $h/\lambda$. Planck's constant is the thing you multiply a frequency by, or divide a wavelength into, to get out an energy or a momentum.

Here is the rule of thumb that falls out, and it is the most useful sentence in the chapter. For any system, quantum mechanics starts to matter when the relevant action — momentum times distance, or energy times time — is in the same league as $h$. Take an electron in a 1-nanometer potential well: its ground-state kinetic energy is roughly $\hbar^2/(2m_e L^2) \approx 0.4$ eV. Measurable. Important. Now take a 1-gram marble in a 10-centimeter box: the matching energy is something like $10^{-65}$ J. And here is the part people get wrong — quantum mechanics is *not false* for the marble. It is exactly true for the marble. It is just that when the mass and the size are this large, the quantum energy scales shrink to something so unimaginably tiny that classical mechanics becomes indistinguishable from the real, exact answer. Classical physics is not a different theory. It is quantum mechanics with the quantum part too small to see.

---

## What Planck Did Not Know

It is worth being clear about what actually happened in 1900, because the history gets garbled in the retelling. Planck did not discover quantum mechanics. He found a formula that matched a curve, and then he found a derivation for that formula that demanded discrete energy levels in the oscillators. And he was explicit — in the original paper and for years after — that he *hoped* the discrete energies were a mathematical trick, an artifact of how he had done the counting, something that would eventually be derived from ordinary classical physics without nature actually being lumpy. He was wrong about that. But he did not know he was wrong, and he resisted Einstein's photon for years.

Einstein's 1905 move was a different animal altogether. Planck had quantized the material oscillators sitting at the wall of the cavity. Einstein quantized the electromagnetic field itself — and that is a vastly bolder claim. It is not "matter trades energy with the field in chunks." It is "the field energy is intrinsically lumpy, full stop, regardless of whatever matter it happens to be touching." Planck would not sign that statement. Einstein did. And Planck's discomfort with his own creation is a useful reminder for the whole rest of this book: finding the right formula and understanding what it means are two completely different achievements, and they can arrive a quarter century apart.

Which is roughly the gap. The real understanding of *why* oscillators have discrete energy levels had to wait for quantum mechanics proper — 1925 and 1926, Heisenberg and Schrödinger. In 1900 Planck had the formula in his hand. The machinery behind it took another twenty-five years to build.

<!-- → [TABLE: Work functions of common metals in eV — Cs 2.1, Na 2.28, K 2.3, Mg 3.7, Al 4.1, Ag 4.3, Fe 4.5, Cu 4.7, Ni 5.0, Au 5.1, Pt 6.35] -->

---

## The +1 — Simulation Exercise: Planck vs. Rayleigh–Jeans

The deliverable: `01-blackbody.html`. A D3 plot showing $u(\nu, T)$ for both the Planck distribution and the Rayleigh–Jeans law on the same axes, with a temperature slider and a frequency cursor.

### Updated `CLAUDE.md` Stanza for This Chapter

Add this stanza to your existing `CLAUDE.md`:

````markdown
## Chapter 1 — Blackbody and Planck vs. Rayleigh–Jeans

- Physics constants (SI, exact where applicable):
    h  = 6.62607015e-34  J·s
    kB = 1.380649e-23    J/K
    c  = 2.99792458e8    m/s
- Frequency grid: ν ∈ [1e12, 1e16] Hz, N = 500 log-spaced points.
  (Linear spacing compresses the interesting region; log-spacing is required.)
- Plot spectral energy density u(ν, T) in J·s·m⁻³ (SI) on a linear y-axis.
  The axis rescales automatically with the slider so both curves are visible.
- The Rayleigh–Jeans curve must be drawn only up to the value where it
  exceeds 3× the Planck maximum — clip or gray it out above that point with
  a label "Rayleigh–Jeans diverges here."
- Wien frequency marker: a vertical dashed line at ν_max = 2.821 kB T / h,
  labeled "Wien peak."
- hν/kT cursor: a vertical draggable line showing the value of hν/kT at
  that frequency, so the student can see when x = hν/kT crosses 1.
````

### The Simulation Prompt

````markdown
SHOW.
The Planck spectral energy density (energy per unit volume per unit frequency):

  u_Planck(ν, T) = (8π h ν³ / c³) · 1 / (exp(hν / kB T) − 1)

The Rayleigh–Jeans law (classical limit):

  u_RJ(ν, T) = (8π ν² / c³) · kB T

Wien's displacement law (peak frequency):

  ν_max = 2.821 · kB T / h

Physical constants (use exactly):
  h  = 6.62607015 × 10⁻³⁴ J·s
  kB = 1.380649 × 10⁻²³ J/K
  c  = 2.99792458 × 10⁸ m/s

Use the CLAUDE.md and DESIGN.md saved earlier as binding context.

SAY.
Produce a single file named `01-blackbody.html`. It opens in a browser and
shows:
  Top panel (600 px wide, 300 px tall):
    - Planck curve u_Planck(ν, T) in blue (filled area under curve)
    - Rayleigh–Jeans curve u_RJ(ν, T) in red (line, clipped at 3× Planck max,
      with a label "diverges →" beyond the clip)
    - A green dashed vertical line at ν_max (Wien peak), labeled
    - x-axis: frequency ν in units of 10¹³ Hz, range [0.1, 10] × 10¹⁴ Hz
    - y-axis: u(ν, T) in J·s·m⁻³, auto-rescaling with T
    - A text overlay showing the ratio u_Planck / u_RJ at the cursor frequency
  Bottom controls:
    - Temperature slider: T ∈ [1000, 10000] K, default 5778 K
    - Draggable frequency cursor (vertical line) showing current ν, hν/kT
  Normalization check (displayed top-right):
    ∫u_Planck dν from 10¹² to 10¹⁶ Hz (numerical) vs.
    Stefan–Boltzmann result σT⁴ × (4/c) (where σ = 5.670 × 10⁻⁸ W·m⁻²·K⁻⁴).
    Label: "Numerical / exact = X.XXX" (must be > 0.99 for the default grid).

CONSTRAIN.
- D3 v7 from CDN. SVG only. Vanilla JS.
- N = 500 log-spaced frequency points on [10¹², 10¹⁶] Hz. (Log-spacing is
  mandatory: linear spacing undersamples the peak region.)
- Planck curve computed via u_P = 8π*h*ν³/c³ / (Math.exp(h*ν/(kB*T)) - 1).
  Guard against overflow: if h*ν/(kB*T) > 700, return 0.
- Rayleigh–Jeans computed via u_RJ = 8π*ν²*kB*T/c³. Clip the SVG path at
  y = 3 × max(u_Planck) and draw a red arrow labeled "diverges →".
- Wien peak line: ν_max = 2.821 * kB * T / h, recomputed on every slider move.
- The hν/kT cursor shows the numerical value of x = hν/kT at the current
  cursor position, and colors the background pale yellow when x < 1 (classical
  regime) and pale blue when x > 1 (quantum regime).

VERIFY.
After writing the file, give me these checks:
(a) At T = 5778 K, ν_max should appear near 3.4 × 10¹⁴ Hz (λ ≈ 880 nm —
    actually peak in near-IR when expressed in ν; Wien in wavelength gives
    ~500 nm but ν-peak and λ-peak differ because dν ≠ dλ). The simulation
    should label both.
(b) At T = 5778 K, the ratio u_Planck / u_RJ at the cursor placed at
    ν = 3 × 10¹⁵ Hz should be approximately 10⁻²⁰.
(c) At T = 1000 K, ν_max shifts to lower frequency. Verify that the Planck
    peak moves left when T decreases.
(d) The numerical integral ∫u_Planck dν over [10¹², 10¹⁶] Hz should match
    σT⁴ × (4/c) to within 1% for T = 5778 K. (The integral misses power
    outside the grid; warn if the captured fraction drops below 99%.)

Then list the known LLM failure modes for this code:
  - Using linear instead of log-spaced ν grid (undersamples the peak)
  - Integer overflow in Math.exp(h*ν/(kB*T)) at large ν/T ratio
  - Wrong normalization claim (∫u dν ≠ σT⁴ × 4/c — off by factors of π or c)
  - Rayleigh–Jeans not clipped (Planck curve invisible at any T because RJ
    dominates the scale)
  - ν_max line not updating with slider
  - Missing units on axes
Confirm which you have guarded against.
````

### Extension Prompt — Photoelectric Stopping Potential Plotter

````markdown
Add a second tab to 01-blackbody.html: "Photoelectric Effect."

In this tab, show:
  - An x-axis: frequency ν ∈ [3 × 10¹⁴, 3 × 10¹⁵] Hz.
  - A y-axis: stopping potential V_stop (in volts), range [−1, 5] V.
  - For three metals simultaneously (Na: Φ = 2.28 eV, Al: Φ = 4.1 eV,
    Cu: Φ = 4.7 eV), plot V_stop(ν) = (hν − Φ) / e for ν above threshold,
    and V_stop = 0 for ν below threshold.
  - The slope of all three lines is h/e = 4.136 × 10⁻¹⁵ V·s. Verify by
    displaying the fitted slope from the Na line.
  - A draggable cursor showing ν, E_photon = hν (in eV), and V_stop for
    each metal.
  - A dropdown to add additional metals from a table:
    [Cs: 2.1, Na: 2.28, K: 2.3, Mg: 3.7, Al: 4.1, Ag: 4.3,
     Fe: 4.5, Cu: 4.7, Ni: 5.0, Au: 5.1, Pt: 6.35] (all in eV).

Use the same CLAUDE.md and DESIGN.md. Do not regress the blackbody tab.

Verify: slope of any V_stop vs. ν line must equal h/e = 4.136 × 10⁻¹⁵ V·s
to within 0.1%.
````

---

## References

- Planck, M. (1901). "Ueber das Gesetz der Energieverteilung im Normalspectrum." *Annalen der Physik* 4, 553–563. — The original blackbody quantization paper.
- Einstein, A. (1905). "Über einen die Erzeugung und Verwandlung des Lichtes betreffenden heuristischen Gesichtspunkt." *Annalen der Physik* 17, 132–148. — The photoelectric effect paper introducing photons.
- Millikan, R.A. (1916). "A direct photoelectric determination of Planck's h." *Physical Review* 7(3), 355–388. [doi:10.1103/PhysRev.7.355](https://doi.org/10.1103/PhysRev.7.355)
- Compton, A.H. (1923). "A quantum theory of the scattering of X-rays by light elements." *Physical Review* 21(5), 483–502. [doi:10.1103/PhysRev.21.483](https://doi.org/10.1103/PhysRev.21.483)
- NIST CODATA 2018 recommended values of fundamental physical constants. [physics.nist.gov/constants](https://physics.nist.gov/cgi-bin/cuu/Value?h)
- Griffiths, D.J. (2018). *Introduction to Quantum Mechanics* (3rd ed.). Cambridge University Press. §1.2.
- Townsend, J.S. (2012). *A Modern Approach to Quantum Mechanics* (2nd ed.). University Science Books. §1.3–1.4.
- Krane, K.S. (2019). *Modern Physics* (4th ed.). Wiley. Chapter 3.
- Nobel Prize facts: Einstein 1921 — [nobelprize.org/prizes/physics/1921/einstein/facts/](https://www.nobelprize.org/prizes/physics/1921/einstein/facts/); Millikan 1923 — [nobelprize.org/prizes/physics/1923/millikan/facts/](https://www.nobelprize.org/prizes/physics/1923/millikan/facts/); Compton 1927 — [nobelprize.org/prizes/physics/1927/compton/facts/](https://www.nobelprize.org/prizes/physics/1927/compton/facts/).
- Hake, R.R. (1998). "Interactive-engagement versus traditional methods." *Am. J. Phys.* 66(1), 64–74. [doi:10.1119/1.18809](https://pubs.aip.org/aapt/ajp/article/66/1/64/1055076/Interactive-engagement-versus-traditional-methods)

---

*Chapter 2 follows: de Broglie turns the argument around and asks whether the particle-nature of light implies a wave-nature of matter. If photons have momentum $p = h/\lambda$, what is the wavelength of an electron?*

---

## Running Project — Build the 1D Quantum Sandbox

**This chapter adds:** the physical-constants and units harness — the exact values of $h$, $\hbar$, $k_B$, $c$, $m_e$, and the eV/J/nm conversions — plus the discipline of self-checking a numerical integral against a known closed-form result (Stefan–Boltzmann), the prototype for every validation the sandbox will run.

### Exercise R1 — When to Use AI
**The judgment:** In this chapter's project work, AI assistance is appropriate for:
- Generating a constants module with $h$, $\hbar$, $k_B$, $c$, $m_e$ and the eV↔J, nm↔m conversions — *Why AI works here:* transcribing CODATA values into a code block is reformatting, and each value is checkable against a reference in one line.
- Scaffolding the Planck-vs-Rayleigh–Jeans plot with a log-spaced frequency grid — *Why AI works here:* this is standard D3 plotting boilerplate, and the Stefan–Boltzmann integral gives an independent numeric check.
**The tell:** You are using AI well when you have an independent way to check the output — here, $\int u_\text{Planck}\,d\nu = (4/c)\sigma T^4$ with no fitting parameters.

### Exercise R2 — When NOT to Use AI
**The judgment:** These tasks require your judgment; AI output here can't be trusted without redoing the work:
- Choosing the log-spaced frequency grid and the overflow guard on $e^{h\nu/k_BT}$ — *Why AI fails here:* a linear grid undersamples the peak and a missing guard returns `NaN` at large $\nu/T$; the curve still *looks* plausible, so the failure is silent until you check the integral.
- Confirming the constants are right to the last digit — *Why AI fails here:* a transposed digit in $\hbar$ or a wrong eV/J factor is a hallucinated-constant error the AI will state with full confidence, and it propagates into every energy the sandbox ever reports.
**The tell:** If you could not explain the result without the AI — if the AI is your *reason* rather than your *tool* — it did work that should have been yours.
**Physics-judgment connection:** This trains checking a numerical integral against a known analytic value (Stefan–Boltzmann) and checking every physical constant against a cited reference before trusting downstream numbers.

### Exercise R3 — LLM Exercise
**What you're building this chapter:** a shared constants/units module and a blackbody page whose numerical integral self-validates against $\sigma T^4$.
**Tool:** Claude chat — this is a self-contained artifact built against a fixed spec; no persistent project state is needed beyond the governing files already in place.
**The Prompt:**
```
Using the CLAUDE.md and DESIGN.md governing files from Chapter 0 as binding
context, do two things.

(1) Create a constants module constants.js exporting exact SI values:
    h = 6.62607015e-34 J·s, hbar = 1.054571817e-34 J·s,
    kB = 1.380649e-23 J/K, c = 2.99792458e8 m/s,
    m_e = 9.1093837015e-31 kg, eV = 1.602176634e-19 J,
    plus helpers J_to_eV, eV_to_J, nm_to_m, m_to_nm. Comment the source (CODATA).

(2) Build 01-blackbody.html plotting, on the same axes, the Planck law
    u_Planck(ν,T) = (8π h ν³ / c³) / (exp(hν/kBT) − 1)
    and Rayleigh–Jeans u_RJ(ν,T) = (8π ν² / c³) kB T,
    with a temperature slider (1000–10000 K). Use a LOG-spaced ν grid of
    N = 500 points on [1e12, 1e16] Hz. Guard the exponential: if hν/kBT > 700,
    return 0. Clip the Rayleigh–Jeans curve at 3× the Planck maximum.
    Add a Wien-peak marker at ν_max = 2.821 kB T / h.

SELF-CHECK (this is the point): numerically integrate u_Planck over the grid
and display "numerical / (4σT⁴/c)" using σ = 5.670374e-8 W·m⁻²·K⁻⁴. It must
read > 0.99 at T = 5778 K. If it does not, tell me whether the error is the
grid (too narrow / linear) or a wrong constant — do not silently rescale.
```
**What this produces:** `constants.js` (reused by every later sandbox page) and `01-blackbody.html` with a live integral-vs-analytic ratio readout.
**How to adapt:** *Your system:* if you display energies in eV elsewhere, route every conversion through `constants.js` so there is one source of truth. *ChatGPT/Gemini:* re-paste the constants block each session. *Claude Project:* add `constants.js` to the Project knowledge so later chapters import rather than re-declare it.
**Builds on:** the governing files and units convention from Chapter 0.  **Next:** Chapter 2 uses these constants to turn $\lambda = h/p$ into the solver's spatial grid.

### Exercise R4 — CLI Exercise
**What you're building this chapter:** a tested constants module and a blackbody self-check you can run from the command line.
**Tool:** Claude Code — it can run the Stefan–Boltzmann integral as a script and report the ratio, then record it in `PROJECT.md`.
**Skill level:** Beginner
**Setup — confirm:**
- [ ] `constants.js` from the R3 prompt
- [ ] Node.js available to run a check script
- [ ] The Chapter 0 rule in `CLAUDE.md` that all conversions route through one module
**The Task:**
```
Read constants.js. Write a standalone Node script check-stefan.js that
integrates u_Planck(ν, 5778 K) over a log-spaced grid of N = 2000 points on
[1e11, 1e17] Hz (trapezoidal in log space), then prints the ratio
  numerical_integral / (4 σ T⁴ / c)
using σ = 5.670374e-8. It must print a value between 0.99 and 1.01. Do NOT
edit constants.js values. If the ratio is low, widen the grid rather than
changing any constant, and say so. Append to PROJECT.md under "Verified":
"Ch1 blackbody: ∫u dν / (4σT⁴/c) = <ratio>".
```
**Expected output:** `check-stefan.js`, a printed ratio in [0.99, 1.01], and one new `PROJECT.md` line.
**What to inspect:** that the ratio is close to 1 *because the grid captures the spectrum*, not because a constant was nudged; widening the grid should push the ratio toward 1 from below (the integral misses tail power on a narrow grid).
**If it goes wrong:** a ratio far from 1 with a wide grid means a wrong constant or a missing $\nu^3$/$\nu^2$ factor — check the constants against CODATA before touching the grid. A ratio that *won't* climb toward 1 as you widen the grid points at the integrand, not the bounds.
**CLAUDE.md / AGENTS.md note:** add: "Any new spectral or eigenvalue quantity must ship with one self-check against a known analytic value (here: Stefan–Boltzmann)."

### Exercise R5 — AI Validation Exercise
**What you're validating:** the constants module and the blackbody self-check from R3/R4.
**Validation type:** Code + Numerical result
**Risk level:** Medium — a wrong constant is silent and contaminates every later energy, so the cost of a missed error is high even though the check itself is simple.
**Setup:** use your own R3/R4 artifacts.
**The Validation Task:** Evaluate against this checklist; mark Pass / Fail / Cannot determine with reasoning.
```
Validation Checklist — Constants and the Stefan–Boltzmann self-check
□ Correctness: are h, ħ, kB, c, m_e, and the eV factor correct to all stated digits?
□ Completeness: does the page show the integral-vs-(4σT⁴/c) ratio, not just the curves?
□ Scope: did it hardcode constants inside the HTML instead of importing constants.js?
□ Physics criterion 1: ratio ∫u dν / (4σT⁴/c) reads 0.99–1.01 at T = 5778 K?
□ Physics criterion 2: ν_max tracks 2.821 kB T / h and shifts left as T drops?
□ Failure-mode check: any of —
  - fluent but wrong (Rayleigh–Jeans drawn but Planck invisible due to no clip)
  - hallucinated constant (a transposed digit in ħ or a wrong eV/J factor)
  - NaN from un-guarded exp(hν/kBT) at high ν, plotted as a gap
  - linear ν grid that undersamples the peak and biases the integral low
```
**What to do with findings:** pass → use it; one fail → fix the single constant or the grid and re-run the self-check; multiple fails / cannot-determine → re-enter the constants by hand from CODATA, since this module is load-bearing for the entire sandbox.
**AI Use Disclosure (mandatory, two sentences):**
> *1:* The AI produced the constants module and the blackbody page, including the numerical integral compared to the Stefan–Boltzmann law.
> *2:* The AI could not certify that each physical constant matched CODATA to the last digit — I verified the constants against the reference myself, because a silent digit error would corrupt every later energy.
**Physics-judgment connection:** trains the two habits the whole sandbox rests on — checking constants against a cited value, and checking a numerical integral against a known analytic result.
