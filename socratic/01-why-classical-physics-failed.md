# Chapter 1 — Why Classical Physics Failed: Blackbody, Photoelectric, and the Photon

Picture a poker in a blacksmith's forge. As the iron heats, it glows red, then orange, then yellow-white. Before you read on, ask: does the color depend on *which* iron? Most people assume the metal's identity matters — that copper would glow differently from steel. It does not. Any iron, any ceramic, any object at the same temperature glows the same color and emits the same spectrum. By 1900, Lummer and Pringsheim had measured those spectral curves with extraordinary precision: smooth, hump-shaped, reproducible to within a percent. So here is the puzzle for the physicists of Europe — they knew exactly what the theory predicted, and exactly how badly the prediction failed.

How badly? Make a guess before reading. "Off by a lot" is the natural answer. It is far worse than that. The prediction was *infinite* energy. A hot poker, left alone in a room, should incinerate you with UV radiation pouring off the walls. The fact that this manifestly does not happen was, to put it mildly, a problem.

---

## How You Get Infinite Energy from Perfectly Good Physics

Where does an infinity come from in a theory that works everywhere else? Let us build the argument and watch for the step that breaks. Inside a cavity at temperature $T$, the electromagnetic field can vibrate at any frequency. Count the modes: there are

$$\frac{8\pi\nu^2}{c^3}$$

modes per unit volume per unit frequency interval. Is this the suspect step? It is not — this counting is correct, a geometric fact about standing waves in a box, and nobody disputes it.

Now assign energy to each mode. Here the classical answer is equipartition: any degree of freedom in thermal equilibrium at temperature $T$ carries average energy $\frac{1}{2}k_BT$. An electromagnetic mode has two quadratic terms — electric field energy and magnetic field energy — so it carries $k_BT$. Multiply by the mode count:

$$u(\nu, T) = \frac{8\pi\nu^2}{c^3}\,k_BT.$$

This is the Rayleigh–Jeans law. Now look at what it does. At long wavelengths it agrees with measurement. But at short wavelengths the mode count grows as $\nu^2$ while each mode still carries a fixed $k_BT$ — so the product grows without bound. Integrate over all frequencies and you get infinity. This was called the ultraviolet catastrophe, which is a better name than most disasters get.

So which step is guilty? The mode counting is not wrong. Equipartition is not wrong in general — it works beautifully for ideal gases (heat capacities at low temperature aside). The trouble is hidden in an assumption equipartition smuggles in: that energy can be distributed *continuously* among modes. There is no smallest chunk. Any mode, however high its frequency, can hold any energy from zero to infinity, and on average it holds $k_BT$. That continuity assumption is what kills you. Hold onto it — it is the thing about to be denied.

---

## Planck's Desperate Remedy

What was Max Planck actually trying to do in 1900? You might assume he set out to discover quantum mechanics. He did not — he was trying to fit a curve. He had the experimental data from Lummer and Pringsheim, and he wanted a formula that would match it. Working backward from the data — a perfectly respectable thing to do if you are honest about what you are doing — he found that the only way to get a finite total energy was to change the entropy of a resonator in a very specific way.

What change? Suppose the oscillators in the cavity walls cannot hold arbitrary energies. Suppose instead they are restricted to values $0, h\nu, 2h\nu, 3h\nu, \ldots$ — discrete multiples of some basic unit $h\nu$, where $h$ is a new constant. Then instead of integrating over a continuous distribution (which gives $k_BT$), you sum a discrete geometric series:

$$\langle E \rangle = \frac{h\nu}{e^{h\nu/k_BT} - 1}.$$

This is the Planck average energy per mode. Multiply by the mode density and you have the **Planck distribution**:

$$u(\nu, T) = \frac{8\pi h\nu^3}{c^3} \cdot \frac{1}{e^{h\nu/k_BT} - 1}.$$

Before trusting any new formula, where should you test it? At the two ends — where you already know the answer. At low frequencies, $h\nu \ll k_BT$, expand the exponential: $e^{h\nu/k_BT} \approx 1 + h\nu/k_BT$, so the denominator becomes $h\nu/k_BT$, and the whole expression reduces to $k_BT$. You recover exactly the Rayleigh–Jeans law — Planck's formula agrees with classical physics precisely where classical physics was already right. At high frequencies, $h\nu \gg k_BT$, the exponential is enormous, the $-1$ is negligible, and $u$ falls off like $e^{-h\nu/k_BT}$. The exponential kills the polynomial. No catastrophe. The formula passes both tests.

The constant $h$ that Planck fitted to the Berlin data was $6.55 \times 10^{-34}$ J·s. The current accepted value is $6.626 \times 10^{-34}$ J·s — his first fit was within one percent.

Now here is the question that separates getting the right formula from understanding it: *what*, exactly, did Planck quantize? The tempting answer is "light." But that is not his step. Planck quantized the *oscillators in the walls*, not the electromagnetic field itself. In his picture the field was still classical. The oscillators could only exchange energy with the field in chunks of $h\nu$, but between those exchanges the field did whatever Maxwell's equations said. Planck found this uncomfortable. He spent years trying to derive his formula without the discrete energies, and never succeeded — because you cannot. The radical step, saying that *the field itself* comes in discrete packets, that light is made of particles, was not his to take.

---

## What the Spectral Peak Tells You

Look again at the hump-shaped curve. Where is the peak, and what controls it? From the Planck distribution you can find out by locating where $\partial u/\partial\nu = 0$. The algebra is not hard — you get a transcendental equation whose solution is $x = h\nu/k_BT \approx 2.821$, so

$$\nu_\text{max} = 2.821\,\frac{k_BT}{h}.$$

Read what this says before moving on: the peak frequency is proportional to temperature. Double the temperature, double the peak frequency, halve the peak wavelength. At $T = 5778$ K (the Sun's photosphere), the peak wavelength is about 501 nm — green. At $T = 3000$ K (a tungsten filament), the peak is near 966 nm — infrared. So most of the light from an incandescent bulb is invisible, which is why we stopped making them.

Here is a trap worth predicting your way into. If you know $\nu_\text{max}$, can you just convert to a wavelength via $\lambda = c/\nu$ and call it $\lambda_\text{max}$? It seems like it must work. It does not — the peak *in frequency* and the peak *in wavelength* are not at the same place. This is not a contradiction; it is a consequence of the fact that $d\nu$ and $d\lambda$ are not proportional. The spectral density per unit frequency and the spectral density per unit wavelength are different functions. Both are legitimate; they simply describe the spectrum in different coordinates.

---

## Worked Example — Twenty Orders of Magnitude

Before computing, predict: at ultraviolet frequencies and a few thousand kelvin, how wrong is Rayleigh–Jeans? Factor of ten? Factor of a thousand? Write down a number, then watch it shatter.

At $T = 3000$ K and $\nu = 3 \times 10^{15}$ Hz (ultraviolet), how wrong is Rayleigh–Jeans?

Both formulas share the mode density $8\pi\nu^2/c^3$. The ratio of Planck to Rayleigh–Jeans is just the ratio of the average energies per mode:

$$\frac{u_\text{Planck}}{u_\text{RJ}} = \frac{h\nu/k_BT}{e^{h\nu/k_BT} - 1}.$$

Compute $h\nu = (6.626\times10^{-34})(3\times10^{15}) = 1.988\times10^{-18}$ J $= 12.4$ eV. And $k_BT = (1.381\times10^{-23})(3000) = 4.14\times10^{-20}$ J $= 0.259$ eV. So $x = h\nu/k_BT \approx 47.9$.

Then $e^{47.9} \approx 7\times10^{20}$, and

$$\frac{u_\text{Planck}}{u_\text{RJ}} \approx \frac{47.9}{7\times10^{20}} \approx 7\times10^{-20}.$$

Twenty orders of magnitude. At UV frequencies and room-ish temperatures, classical physics is not approximately wrong — it is catastrophically, completely wrong. And notice the single parameter that controls it all: $x = h\nu/k_BT$. When $x \ll 1$, the two theories agree. When $x \gg 1$, they disagree by factors growing like $e^x$. The boundary $h\nu \sim k_BT$ marks where quantization starts to matter.

---

## A Completely Different Crisis

Now leave the forge and go to a different laboratory, a different decade, a different phenomenon — and ask whether it could possibly be connected. While Planck was fitting curves in Berlin, Heinrich Hertz had noticed something odd. In 1887 — the same year he demonstrated electromagnetic waves, confirming Maxwell — he found that ultraviolet light striking a metal surface caused it to emit sparks. Philipp Lenard established by 1902 that the sparks were electrons. By 1914, Robert Millikan had measured everything there was to measure. The data said three things, and before reading each, try to predict what a wave theory of light would say should happen:

**First**, there is a threshold frequency. Below a certain $\nu_0$ that depends on the metal, no electrons are emitted — ever, at any intensity. A blinding arc lamp at red frequencies liberates nothing from sodium. A dim UV lamp liberates electrons immediately. Intensity is irrelevant; frequency is everything. (Did you predict a threshold? Wave theory does not — turn the lamp up bright enough and energy should accumulate.)

**Second**, the maximum kinetic energy of the ejected electrons depends on frequency but not on intensity. Double the brightness, and you get twice as many electrons per second, but each electron carries the same energy as before.

**Third**, emission begins with no measurable time delay — within nanoseconds, at any intensity above threshold.

Now resolve the tension. Every one of these facts is inexplicable classically. In the wave picture, energy is delivered continuously and uniformly across the surface. There should be no threshold — given enough time, any frequency at sufficient intensity should accumulate the energy to free an electron. The time delay should grow as intensity drops. The kinetic energy should depend on how hard the wave pushes, which means intensity. Classical physics gets every single detail of this experiment wrong.

---

## Einstein's Light Quanta

So what would it take to explain all three facts at once? In 1905, Einstein proposed something more radical than Planck had dared. Not merely that oscillators exchange energy in discrete units — Planck had done that. Einstein proposed that light energy is *not continuously distributed at all*. It arrives in discrete packets, each with energy

$$E = h\nu.$$

He called them *Lichtquanten* — light quanta. We call them photons.

Now follow the consequence through. A single photon, arriving at a metal surface, is absorbed by a single electron. What happens if $h\nu$ is less than the energy needed to pull the electron free of the metal — the **work function** $\Phi$? The electron cannot escape, no matter how many photons per second you throw at the surface. And if $h\nu > \Phi$? The electron escapes, and the excess becomes kinetic energy:

$$K_\text{max} = h\nu - \Phi.$$

This is Einstein's photoelectric equation. The **stopping potential** $V_\text{stop}$ — the reverse voltage needed to halt the fastest electrons — satisfies

$$eV_\text{stop} = K_\text{max} = h\nu - \Phi.$$

Check the three facts against this one equation. The threshold appears because a photon with $h\nu < \Phi$ simply cannot do the job — not "doesn't quite have enough until the next one helps," but genuinely cannot, ever, because each photon acts alone. The kinetic energy tracks frequency because it tracks the photon energy $h\nu$, fixed by frequency alone. Intensity controls only how many photons arrive per second. And the absence of time delay is automatic: one photon, one electron, immediate. Three impossibilities dissolve into one picture.

Did everyone believe it? Millikan did not. He set out around 1914 to *disprove* the photon idea, which he thought absurd. He spent two years making extraordinarily careful measurements with freshly scraped metal surfaces in vacuum, measuring $V_\text{stop}$ as a function of $\nu$ for sodium, lithium, and potassium. Every metal gave the same slope: $h/e = 4.136\times10^{-15}$ V·s. Einstein's equation fit perfectly. Millikan published his confirmation in 1916, noted that the result was "obtained in spite of my personal conviction," and won the Nobel Prize in 1923 specifically for this measurement of $h$. Einstein won the Nobel Prize in 1921 specifically for the photoelectric effect — not for special relativity.

---

## Worked Example — Stopping Potential for UV on Sodium

Ultraviolet light with wavelength $\lambda = 300$ nm strikes sodium. The work function of sodium is $\Phi = 2.28$ eV. What is the stopping potential?

The shortcut $hc = 1240$ eV·nm makes this fast:

$$E = \frac{1240\ \text{eV}\cdot\text{nm}}{300\ \text{nm}} = 4.13\ \text{eV}.$$

Then $K_\text{max} = 4.13 - 2.28 = 1.85$ eV, and

$$V_\text{stop} = 1.85\ \text{V}.$$

Now a question to test whether you have absorbed the threshold idea: what happens with bright green light at $\lambda = 546$ nm? Then $E = 1240/546 \approx 2.27$ eV, which is *slightly less* than $\Phi = 2.28$ eV. The verdict: no electrons. Not one. Not with a 10,000-watt lamp. The photon energy is below the threshold, and no number of sub-threshold photons adds up to one that works.

---

## Wave and Particle — Not an Either/Or

Now we have a contradiction staring at us. By 1905, the wave nature of light was not a hypothesis. Young's 1801 double-slit experiment, Maxwell's 1865 electromagnetic theory, Hertz's 1887 demonstration of radio waves — half a century of evidence said light is a wave. Interference, diffraction, polarization: impossible with bullets. And here is Einstein saying light comes in particles. So which is it?

The instinct is to answer "both, depending on the experiment" — light *sometimes* behaves as a wave and *sometimes* as a particle, switching modes. Sit with that phrasing and notice what it implies: two personalities that light alternates between. That is not what is happening, and the phrasing will mislead you. The quantum mechanical description is that light is *always* described by a probability amplitude — a wave. The amplitude tells you where detection events are likely; the detection events themselves are discrete and localized. The wave is real. The particle is real. They are not two separate things switching on and off.

Was there a remaining loophole? Arthur Compton's 1923 experiment closed it. When X-rays scatter from graphite, the scattered X-rays have a *longer* wavelength than the incident ones. The wavelength shift is

$$\Delta\lambda = \frac{h}{m_e c}(1 - \cos\theta),$$

where $\theta$ is the scattering angle and $h/(m_e c) = 2.426\times10^{-12}$ m is the Compton wavelength of the electron. This formula follows from treating the photon as a particle with momentum $p = h/\lambda = E/c$ and computing the elastic collision with an electron using relativistic kinematics. And what does classical wave theory predict for the shift? No shift at all — none. The experiment is unambiguous. Compton won the Nobel Prize in 1927.

---

## The Constant That Tells You When Quantum Mechanics Matters

Two numbers define the quantum scale:

$$h = 6.62607015\times10^{-34}\ \text{J}\cdot\text{s}, \qquad \hbar = \frac{h}{2\pi} = 1.054571817\times10^{-34}\ \text{J}\cdot\text{s}.$$

Look at the unit before reading on: J·s. What kind of quantity is that? It is energy times time, or equivalently momentum times length — the unit of **action**, the same quantity that appears in Lagrangian mechanics. So Planck's constant is *not* an energy, despite how often it gets used to compute one. The energy is $h\nu$. The momentum is $h/\lambda$. Planck's constant is what you multiply frequency by, or divide wavelength by, to get an energy or a momentum.

This gives you a portable rule of thumb. When does quantum mechanics become important for a system? When the relevant action — momentum times distance, energy times time — is comparable to $h$. Test it on two cases. For an electron in a 1-nanometer potential well, the ground-state kinetic energy is of order $\hbar^2/(2m_e L^2) \approx 0.4$ eV. Measurable. Important. For a 1-gram marble in a 10-centimeter box, the corresponding energy is roughly $10^{-65}$ J. Now resist the obvious conclusion: it is *not* that quantum mechanics is "wrong" for macroscopic objects. It is exact for them. It is just that for large mass and large dimensions, the quantum energy scales are so inconceivably small that classical mechanics is indistinguishable from the correct theory.

---

## What Planck Did Not Know

The history gets garbled in the retelling, so it is worth being precise about what happened in 1900. Did Planck discover quantum mechanics? The popular story says yes. The truth is narrower. He found a formula that matched a curve, and a derivation for that formula that required discrete energy levels in the oscillators. He was explicit, in his original paper and for years afterward, that he *hoped* the discrete energies were a mathematical trick — an artifact of his combinatorial counting — that could eventually be derived from classical physics without requiring discreteness in nature. He was wrong, but he did not know he was wrong. He resisted the photon idea for years after Einstein proposed it.

What made Einstein's 1905 step different in kind? Trace the contrast. Planck quantized the material oscillators at the boundary of the cavity. Einstein quantized the electromagnetic field itself. That is a far more radical claim: not that matter exchanges energy with the field in chunks, but that the field energy is intrinsically discrete regardless of the matter it interacts with. Planck would not say this. Einstein would. And Planck's discomfort with his own discovery is a useful reminder that finding the right formula and understanding what it means are two very different achievements.

When did the *mechanism* — why oscillators have discrete energy levels at all — finally arrive? Not until quantum mechanics proper: 1925 and 1926, Heisenberg and Schrödinger. In 1900, Planck had the formula. The understanding behind it would take another quarter century.

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
