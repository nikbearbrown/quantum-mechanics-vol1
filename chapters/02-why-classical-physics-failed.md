# Chapter 1 — Why Classical Physics Failed: Blackbody, Photoelectric, and the Photon

## TL;DR

Classical physics predicts that a hot object radiates infinite energy at short wavelengths (the ultraviolet catastrophe), and that any sufficiently bright light beam — regardless of color — should eject electrons from metal. Both predictions are wrong. Planck (1900) fixed the first by quantizing oscillator energies in units of $h\nu$; Einstein (1905) fixed the second by proposing that light itself arrives as discrete packets — photons — each with energy $E = h\nu$. Together, these two moves introduce Planck's constant $h$ and establish the first irreducible break between classical and quantum physics.

---

## Learning Objectives

By the end of this chapter you will be able to:

1. **(Understand)** Explain, using the equipartition theorem, why the Rayleigh–Jeans law diverges at high frequencies, and what assumption causes the divergence.
2. **(Analyze)** Identify which experimental features of the photoelectric effect are inexplicable classically, and map each to the photon picture.
3. **(Apply)** Calculate the stopping potential for the photoelectric effect given a photon frequency and a metal's work function, and compute the ratio of Planck to Rayleigh–Jeans spectral energy density at a given temperature and frequency.
4. **(Evaluate)** Distinguish Planck's quantization (of oscillator energies) from Einstein's quantization (of the electromagnetic field itself), and explain why the distinction matters.
5. **(Create)** Build a D3 simulation that plots both spectral distributions against frequency with a temperature slider, and verify that the Planck curve peaks near Wien's law at each temperature.

---

## The Scene: An Iron Poker in a Dark Forge

A blacksmith's iron poker sits in a forge. As it heats, it first glows a dim red, then orange, then yellow-white. The color shifts with temperature. Not with the particular iron — any iron, any steel, any ceramic at the same temperature emits the same spectrum of light. The total power radiated grows steeply with $T$. By 1900, all of this was measured precisely by Lummer and Pringsheim at the Physikalisch-Technische Reichsanstalt in Berlin. Their spectral curves were smooth, hump-shaped, reproducible to within a percent, and utterly inexplicable.

Every physicist at the turn of the twentieth century knew how to count: there are $8\pi\nu^2/c^3$ electromagnetic modes per unit volume per unit frequency interval in an enclosure. Every physicist knew equipartition: each quadratic degree of freedom in thermal equilibrium carries average energy $\frac{1}{2}k_BT$. An electromagnetic mode has two quadratic terms (electric energy and magnetic energy), so it should carry $k_BT$. The spectral energy density should be

$$u(\nu, T) = \frac{8\pi\nu^2}{c^3}\,k_BT.$$

This is the Rayleigh–Jeans law. It agrees with the Lummer–Pringsheim data at long wavelengths (low $\nu$). At short wavelengths (high $\nu$), it does not merely disagree — it predicts that $\int_0^\infty u(\nu,T)\,d\nu = \infty$. A hot poker would radiate infinite energy. You would be incinerated by ambient UV from your kitchen walls.

This is, obviously, not happening. The error is not in the measurement. The error is in the theory. And it took Planck, in desperation, to find the smallest possible change that would fix it.

---

## The Ultraviolet Catastrophe and Planck's Cure

### Why Rayleigh–Jeans Diverges

The mode counting — $8\pi\nu^2/c^3$ modes per unit frequency per unit volume — is correct. The error is equipartition. Equipartition assumes every mode can hold any energy continuously, and at temperature $T$ the average is $k_BT$. As $\nu$ grows without bound, the number of modes grows as $\nu^2$, and each holds $k_BT$. The product $\nu^2 \cdot k_BT$ diverges.

Equipartition holds when thermal energy ($k_BT$) is large compared to any relevant energy scale in the problem. For a harmonic oscillator with natural frequency $\nu$, the relevant energy scale is — as Planck found — $h\nu$. When $k_BT \gg h\nu$ (low frequency or high temperature), equipartition is an excellent approximation. When $k_BT \ll h\nu$ (high frequency or low temperature), the oscillator cannot absorb even one quantum of energy from the thermal field, and it is effectively frozen at zero energy. Modes at high frequency are *starved* out by their own quantization.

### Planck's Derivation

Max Planck presented his formula to the German Physical Society on 14 December 1900 — a date sometimes called the birth of quantum mechanics. He arrived at it by working backward from the data: he guessed the entropy of a resonator that would give a formula matching experiment, then asked what kind of combinatorial counting would produce that entropy.

The result: assume a resonator at frequency $\nu$ can only hold energies $0, h\nu, 2h\nu, 3h\nu, \ldots$ — integer multiples of $h\nu$, where $h$ is a constant to be fitted to the data. Then the average energy per mode at temperature $T$ is not $k_BT$ but

$$\langle E \rangle = \frac{h\nu}{e^{h\nu/k_BT} - 1}.$$

This follows directly from the Boltzmann distribution applied to discrete rather than continuous energies. (Derive it yourself: $\langle E \rangle = \sum_{n=0}^\infty (nh\nu)\,e^{-nh\nu/k_BT} / \sum_{n=0}^\infty e^{-nh\nu/k_BT}$; the geometric series are elementary.) Multiplying by the mode density gives the **Planck distribution**:

$$u(\nu, T) = \frac{8\pi h\nu^3}{c^3} \cdot \frac{1}{e^{h\nu/k_BT} - 1}.$$

Two limits confirm it is the right formula.

**Low-$\nu$ limit (classical).** When $h\nu \ll k_BT$, the exponential expands as $e^{h\nu/k_BT} \approx 1 + h\nu/k_BT$, so $e^{h\nu/k_BT} - 1 \approx h\nu/k_BT$, and

$$u(\nu, T) \approx \frac{8\pi h\nu^3}{c^3} \cdot \frac{k_BT}{h\nu} = \frac{8\pi\nu^2}{c^3}\,k_BT.$$

Exactly the Rayleigh–Jeans law. Planck's formula recovers the classical result where classical physics was already right.

**High-$\nu$ limit (quantum).** When $h\nu \gg k_BT$, $e^{h\nu/k_BT} \gg 1$, so the $-1$ is negligible, and

$$u(\nu, T) \approx \frac{8\pi h\nu^3}{c^3}\,e^{-h\nu/k_BT}.$$

The exponential kills the polynomial growth. Total energy is finite. No catastrophe.

### Wien's Displacement Law from Planck

Setting $\partial u / \partial \nu = 0$ (maximum of the Planck distribution) yields Wien's displacement law: the frequency of peak emission is proportional to temperature,

$$\nu_{\max} = \alpha \frac{k_BT}{h},$$

where $\alpha \approx 2.821$ (the solution to $xe^x/(e^x-1) = 3$, $x = h\nu/k_BT$). In wavelength form, the more familiar expression is

$$\lambda_{\max} T = 2.898 \times 10^{-3}\ \text{m}\cdot\text{K}.$$

At $T = 5778$ K (the Sun's photosphere), $\lambda_{\max} \approx 501$ nm — peak in the green part of the visible spectrum. At $T = 3000$ K (a hot tungsten filament), $\lambda_{\max} \approx 966$ nm — peak in the near-infrared, which is why incandescent bulbs are inefficient: most of their output is invisible.

The constant Planck fitted to the Berlin data was $h = 6.55 \times 10^{-34}$ J·s. The current SI value (exact since the 2019 redefinition) is $h = 6.62607015 \times 10^{-34}$ J·s. His original fit was within 1%.

---

## Worked Example 1 — Planck vs. Rayleigh–Jeans at $T = 3000$ K, UV

**Situation.** At what factor does the Planck distribution differ from the Rayleigh–Jeans law at $T = 3000$ K and $\nu = 3 \times 10^{15}$ Hz (ultraviolet, $\lambda \approx 100$ nm)?

**Process.** Both formulas share the mode density $8\pi\nu^2/c^3$. The Rayleigh–Jeans average energy per mode is $k_BT$; Planck's is $h\nu / (e^{h\nu/k_BT} - 1)$. The ratio is:

$$\frac{u_\text{Planck}}{u_\text{RJ}} = \frac{h\nu/k_BT}{e^{h\nu/k_BT} - 1}.$$

Compute $h\nu$ and $k_BT$:
- $h\nu = (6.626 \times 10^{-34})(3 \times 10^{15}) = 1.988 \times 10^{-18}\ \text{J} = 12.4\ \text{eV}.$
- $k_BT = (1.381 \times 10^{-23})(3000) = 4.14 \times 10^{-20}\ \text{J} = 0.259\ \text{eV}.$
- $x = h\nu/k_BT = 12.4/0.259 \approx 47.9.$

So $e^x \approx e^{47.9} \approx 7 \times 10^{20}$, and the ratio is:

$$\frac{u_\text{Planck}}{u_\text{RJ}} = \frac{47.9}{7 \times 10^{20} - 1} \approx 6.8 \times 10^{-20}.$$

**Resolution.** At UV frequencies and $T = 3000$ K, Planck predicts roughly $10^{-20}$ times the energy density that Rayleigh–Jeans predicts. Classical physics is wrong by twenty orders of magnitude. This is not a small correction; it is a complete breakdown.

**The lesson.** The critical parameter is $x = h\nu / k_BT$. When $x \ll 1$, the quantum and classical formulae agree. When $x \gg 1$, they disagree catastrophically. The boundary $h\nu \sim k_BT$ is where quantization matters.

**The limit.** This calculation treats the surface as a perfect blackbody. Real surfaces emit less than a blackbody at the same temperature by a factor called emissivity (0 to 1). The ratio $u_\text{Planck}/u_\text{RJ}$ is unchanged — it is a ratio of the two theoretical predictions, not a measurement.

---

## The Photoelectric Effect — A Different Crisis

The blackbody problem was about emission: what spectrum does a hot object radiate? The photoelectric effect was about absorption: what happens when light hits a metal? Heinrich Hertz discovered in 1887 that ultraviolet light striking a metal surface caused it to emit sparks (electrons, as Lenard established by 1902). The data told a story classical wave theory could not tell.

The experimental facts, established by Lenard (1902) and confirmed by Millikan (1914–1916):

1. **The threshold.** Electrons are ejected only if the light frequency exceeds a threshold $\nu_0$ that depends on the metal. Below $\nu_0$, no electrons are emitted — ever — no matter how intense the illumination. A dim UV lamp ejects electrons from sodium immediately. A blazing arc lamp at red frequencies ejects none.

2. **The kinetic energy rule.** Above threshold, the *maximum kinetic energy* of ejected electrons depends on frequency but not on intensity. Doubling the brightness of the light doubles the number of electrons per second but leaves their maximum energy unchanged.

3. **The time delay.** At any intensity above threshold, emission begins within nanoseconds. Classical wave theory predicts a delay — at very low intensities, the wave should take seconds or longer to deliver enough energy to eject one electron.

Every one of these facts is inexplicable classically. Classical wave theory says energy is delivered continuously and uniformly across the surface; any frequency at sufficient intensity should eventually accumulate enough energy to eject electrons. The threshold frequency makes no sense in this picture.

### Einstein's Photon (1905)

Albert Einstein's 1905 paper — published in the same year as special relativity and Brownian motion, in what is rightly called his *annus mirabilis* — proposed a simple, radical idea: light energy is not continuously distributed. It comes in discrete packets (he called them *Lichtquanten*, light quanta; we now say **photons**), each with energy

$$E = h\nu.$$

A single photon, arriving at the surface, is absorbed by a single electron. If $h\nu$ is less than the binding energy of the electron to the metal — the **work function** $\Phi$ — the electron cannot escape, regardless of how many photons per second arrive (low $\nu$, high intensity). If $h\nu > \Phi$, the electron escapes with maximum kinetic energy

$$K_{\max} = h\nu - \Phi.$$

The stopping potential $V_\text{stop}$ is the reverse voltage required to bring the fastest electrons to rest:

$$eV_\text{stop} = K_{\max} = h\nu - \Phi.$$

This is Einstein's photoelectric equation. It predicts:
- A linear relationship between $V_\text{stop}$ and $\nu$, with slope $h/e$.
- A threshold at $\nu_0 = \Phi/h$, below which $V_\text{stop} = 0$ (no emission).
- No dependence of $K_{\max}$ on intensity.

All three predictions are correct. Einstein received the Nobel Prize in Physics for 1921 (awarded 1922) explicitly for this work — not for relativity.

### Millikan's Confirmation

Robert Millikan set out, around 1914, to disprove Einstein's equation. He considered the photon idea physically absurd. Over two years of painstaking experimentation with freshly scraped sodium, lithium, and potassium surfaces in vacuum, he measured $V_\text{stop}$ as a function of $\nu$ for multiple metals. Every metal gave the same slope: $h/e = 4.136 \times 10^{-15}$ V·s. The intercept gave $\Phi$ for each metal. Einstein's equation fit perfectly. Millikan published in 1916 (Phys. Rev. 7, 355) and won the Nobel Prize for 1923 (for the charge of the electron and, specifically, for this measurement of $h$).

The work functions of some common metals, in eV: cesium (2.1), sodium (2.3), aluminum (4.1), copper (4.7), gold (5.1), platinum (6.35).

---

## Worked Example 2 — Stopping Potential for UV on Sodium

**Situation.** Ultraviolet light with wavelength $\lambda = 300$ nm ($\nu = c/\lambda$) strikes a sodium surface. The work function of sodium is $\Phi = 2.28$ eV. What is the stopping potential? Does a green ($\lambda = 546$ nm) beam eject electrons?

**Process.**

Step 1: find the photon energy. Use $E = h\nu = hc/\lambda$. The shortcut $hc = 1240\ \text{eV}\cdot\text{nm}$ is exact enough for this problem:

$$E = \frac{1240\ \text{eV}\cdot\text{nm}}{300\ \text{nm}} = 4.13\ \text{eV}.$$

Step 2: apply Einstein's equation.

$$K_{\max} = E - \Phi = 4.13\ \text{eV} - 2.28\ \text{eV} = 1.85\ \text{eV}.$$

Step 3: the stopping potential equals $K_{\max}$ in electron-volts divided by the elementary charge (which cancels $e$):

$$V_\text{stop} = \frac{K_{\max}}{e} = 1.85\ \text{V}.$$

**The dead end.** A student might try: "doubling the intensity doubles the energy delivered, so $K_{\max}$ should double." This is wrong. Doubling intensity doubles the *number* of photons per second, not the energy of each photon. Each photon still has $E = h\nu$. The kinetic energy of each ejected electron is still $h\nu - \Phi$.

**Green light.** $E = 1240/546 \approx 2.27$ eV. This is less than $\Phi = 2.28$ eV. No electrons are ejected. Not one. Not even with a 10,000 W lamp.

**The lesson.** The threshold is frequency, not intensity. One photon of sufficient frequency ejects one electron; ten trillion photons of insufficient frequency eject none.

**The limit.** This is for the *maximum* kinetic energy — electrons from the surface layer. Electrons deeper in the metal lose additional energy through collisions before reaching the surface; the measured $K$ distribution is a spread below $K_{\max}$, not a sharp line. The stopping potential selects the maximum, which is what Einstein's equation predicts.

---

## The Photon and Wave–Particle Duality

By 1905, the wave theory of light was not merely a hypothesis — it was the consensus of half a century of experimental confirmation. Young's 1801 double-slit experiment, Maxwell's electromagnetic theory (1865), Hertz's direct demonstration of electromagnetic waves (1887, the same year he discovered the photoelectric effect) — all of this established that light is a wave. Interference and diffraction are not compatible with a purely corpuscular picture.

And yet, the photoelectric effect requires that light energy be delivered in discrete chunks. It is not an either/or. Light has both wave properties (it interferes; it diffracts; its energy density is described by Maxwell's equations) and particle properties (it is absorbed in discrete quanta; each photon deposits $h\nu$ into a single electron).

Arthur Holly Compton's 1923 experiment closed any remaining loophole. When X-rays (wavelength $\lambda \approx 0.071$ nm) scatter from graphite, the scattered X-rays have a longer wavelength than the incident X-rays. The shift is

$$\Delta\lambda = \frac{h}{m_e c}(1 - \cos\theta),$$

where $\theta$ is the scattering angle. The quantity $\lambda_C = h/(m_e c) = 2.426 \times 10^{-12}$ m is the **Compton wavelength** of the electron. This formula follows from treating the photon as a particle with momentum $p = h/\lambda = E/c$, undergoing elastic collision with an electron — classical wave theory (which predicts no wavelength shift) is unambiguous contradicted. Compton received the Nobel Prize in 1927.

The modern resolution is not that light "sometimes" behaves as a wave and "sometimes" as a particle — as if it switches between modes. The quantum mechanical description is that light is always described by a probability amplitude (a quantum field); the wave interference governs where photons are *likely to be detected*; detection events are discrete. Chapter 3 will develop this picture for massive particles.

---

## Planck's Constant — The Quantum of Action

Two constants characterize the new physics:

$$h = 6.62607015 \times 10^{-34}\ \text{J}\cdot\text{s} \quad (\text{exact since the 2019 SI redefinition})$$
$$\hbar = \frac{h}{2\pi} = 1.054571817 \times 10^{-34}\ \text{J}\cdot\text{s}.$$

In electron-volts: $h = 4.136 \times 10^{-15}\ \text{eV}\cdot\text{s}$, $\hbar = 6.582 \times 10^{-16}\ \text{eV}\cdot\text{s}$. The shortcut $hc = 1240\ \text{eV}\cdot\text{nm}$ is exact to four significant figures.

The units of $h$ are J·s — energy times time, or equivalently momentum times length. This is the unit of **action** (the same quantity that appears in Lagrangian mechanics' principle of least action). Planck's constant is not an energy; it is an action. The energy is $h\nu$ (action × frequency). The momentum is $h/\lambda = \hbar k$ (action / length). Confusing $h$ with an energy is the most common dimensional-analysis error in this chapter.

$h$ sets the scale at which quantum behavior matters. For any system, quantum effects become important when the relevant action — momentum × distance, or energy × time — is comparable to $h$. For an electron in a 1 nm potential well, the ground-state kinetic energy is of order $\hbar^2/(2m_e L^2) \approx 0.4$ eV — large enough to measure. For a 1 g marble in a 10 cm box, the corresponding energy is $\sim 10^{-65}$ J — utterly unobservable. Quantum mechanics is not wrong for macroscopic objects; it is just irrelevant.

---

## Common Misconceptions

**"Planck quantized the electromagnetic field itself."** No. Planck quantized the energies of the material oscillators in the cavity walls. He assumed the oscillators could only exchange energy with the field in multiples of $h\nu$. The electromagnetic field in his model was still classical. Einstein's 1905 step — that the *field itself* comes in discrete quanta — was a qualitatively different and far more radical claim. Planck resisted this interpretation for years.

**"Brighter light means more energetic electrons."** Intensity (power per area) controls the rate of photon arrivals — photons per second per area — not the energy of each photon. Each photon has energy $h\nu$, fixed by frequency alone. Doubling intensity doubles the number of electrons ejected per second, but leaves $K_{\max} = h\nu - \Phi$ unchanged. A very bright red beam and a very dim UV beam: only the dim UV beam ejects electrons (if $h\nu_\text{UV} > \Phi$), and each ejected electron carries the same kinetic energy regardless of the beam's intensity.

**"The threshold is a rough guideline — given enough time, sub-threshold light will eventually eject electrons."** This misconception confuses quantum photons with classical waves. Classically, energy accumulates; given long enough, any frequency would suffice. In the quantum picture, a single photon with $h\nu < \Phi$ simply cannot eject an electron — the energy packet is too small. You can wait for years; if every photon has $h\nu < \Phi$, the answer is zero electrons. The experimental evidence (Lenard 1902, Millikan 1914–16) is unambiguous. [verify: Lenard's 1902 results on threshold — the claim of "no electrons, ever" at sub-threshold intensity is the experimental finding; confirm citation.]

**"Wave-particle duality means light alternates between being a wave and a particle."** The photon is not a tiny ball that occasionally undergoes wave-like behavior. It is always a quantum object described by a probability amplitude. The amplitude (governed by Maxwell's equations) tells you where the photon is likely to be detected; the detection event itself is discrete and localized. The "wave" is the probability amplitude; the "particle" is the detection event. They are not two different modes of existence.

**"$h$ has units of energy."** Planck's constant has units of J·s (energy × time = action). Energy is $E = h\nu$. If you find yourself writing $E = h$ without a frequency, check your algebra.

---

## Exercises

**1.1 — (Remember/Understand).** State in your own words the two assumptions that lead to the Rayleigh–Jeans law: (a) the mode counting and (b) equipartition. Which assumption does Planck change? Which does Einstein change? (Hint: they are different changes.)

**1.2 — (Apply — calculation).** Light of wavelength 200 nm strikes a copper surface (work function $\Phi = 4.7$ eV). (a) Compute the photon energy using $E = hc/\lambda$ with $hc = 1240$ eV·nm. (b) Compute the maximum kinetic energy of ejected electrons. (c) Compute the stopping potential. (d) If the wavelength is doubled to 400 nm, what happens? Give a number if electrons are emitted; otherwise state clearly that no electrons are emitted.

**1.3 — (Apply — calculation).** At temperature $T = 6000$ K (approximate solar surface), compute the ratio $u_\text{Planck}/u_\text{RJ}$ at frequency $\nu = 3 \times 10^{15}$ Hz (UV). Express your answer as a power of 10. At what frequency (approximately) does the ratio first drop below $10^{-5}$ at this temperature?

**1.4 — (Analyze).** In Millikan's 1916 experiment, the slope of the $V_\text{stop}$ vs. $\nu$ graph is $h/e$, not $h$. (a) Why $h/e$ and not $h$? (b) Millikan measured the slope to be $4.124 \times 10^{-15}$ V·s. Using $e = 1.602 \times 10^{-19}$ C, compute $h$ from this measurement and compare it to the accepted value $6.626 \times 10^{-34}$ J·s. What is the percentage error? (c) The intercept of the $V_\text{stop}$ vs. $\nu$ line gives $-\Phi/e$. Millikan found the threshold frequency for sodium to be $\nu_0 = 5.52 \times 10^{14}$ Hz. Compute $\Phi$ in eV.

**1.5 — (Evaluate — synthesis).** A student argues: "Since Planck's formula works perfectly and classical physics fails, Planck must have had physical insight into why quantization is correct." Is this right? Write a short paragraph explaining what Planck actually understood (and did not understand) in 1900, and why the physical interpretation of quantization had to wait for Einstein (1905) and later Bohr, Heisenberg, and Schrödinger.

**1.6 — (Create — production exercise).** Complete the LLM Exercise (The +1) in the next section. Then: using the simulation, find the temperature at which the Planck peak frequency reaches the visible range (400–700 nm). Record the temperature and the peak wavelength. Compare to the known solar surface temperature and the color of the Sun as seen from space.

---

## Still Puzzling

- Planck arrived at his formula by a semi-combinatorial argument about discrete energy levels. He did not have a physical model for why oscillators should only exchange energy in multiples of $h\nu$. That explanation had to wait until 1925–1926 (quantum mechanics). This is a recurring pattern in the history of physics: the correct formula arrives before the correct mechanism.

- The "photon" is a stable concept in non-relativistic quantum mechanics (this book), but its full description requires quantum field theory (QFT). In QFT, photons are excitations of the quantized electromagnetic field; they have no well-defined position operator and cannot be described by a wave function $\psi(x,t)$ in the usual sense. This book uses the photon as a stepping stone to the Schrödinger-equation description of massive particles, which *does* have a position representation.

- The wave–particle duality of light remains philosophically contentious. The experimental facts (interference + discrete absorption) are not in dispute; what they mean about the nature of reality is. The Copenhagen interpretation, the many-worlds interpretation, pilot-wave theory, and QBism each give different answers. This book defers to Chapter 11 for a first look at interpretational issues; the present chapter presents the experimental situation only.

- Compton scattering is treated here as a supporting argument for the photon picture. It is not covered in full; a complete treatment requires relativistic kinematics ($E = \sqrt{p^2c^2 + m^2c^4}$). If you want to derive the Compton formula, the calculation is in any modern physics text (e.g., Krane §3.5) and makes a good exercise for a student who has seen special relativity.

---

## The +1 — Simulation Exercise: Planck vs. Rayleigh–Jeans

The deliverable: `01-blackbody.html`. A two-panel D3 plot showing $u(\nu, T)$ for both the Planck distribution and the Rayleigh–Jeans law on the same axes, with a temperature slider and a frequency cursor.

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

### Exploration Tasks

**Task 1 — The classical limit.** Set $T = 5778$ K. Drag the cursor to the far left, where $\nu \sim 10^{12}$ Hz (microwave). The ratio $u_\text{Planck}/u_\text{RJ}$ should read close to 1. Drag the cursor to the right (UV). Watch the ratio collapse. At what frequency does the ratio first drop below $10^{-3}$? Record the corresponding wavelength and compare it to the boundaries of the visible spectrum.

**Task 2 — The Sun.** At $T = 5778$ K, the Wien peak in frequency is near $3.4 \times 10^{14}$ Hz (near-IR). The Wien peak in wavelength ($\lambda_\text{max} = 2.898 \times 10^{-3}/T\ \text{m} \approx 501\ \text{nm}$) is in the green. These are not the same peak. Explain in two sentences why the frequency-domain peak and the wavelength-domain peak are different frequencies. (Hint: $d\nu \neq d\lambda$.)

**Task 3 — Wien's law in action.** Drag $T$ from 1000 K to 10,000 K. Watch the Wien peak move. Confirm that $\nu_\text{max}$ scales linearly with $T$ (doubling $T$ should double $\nu_\text{max}$). At what $T$ does the Wien peak first enter the visible range (approximately $4 \times 10^{14}$ Hz)?

**Task 4 — Catastrophe for real.** At $T = 1000$ K, $\nu = 10^{15}$ Hz (far UV): record the ratio $u_\text{Planck}/u_\text{RJ}$. Compute $h\nu/k_BT$ by hand. Verify it is consistent with the formula $u_\text{Planck}/u_\text{RJ} = (h\nu/k_BT)/(e^{h\nu/k_BT} - 1)$.

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

- Planck, M. (1901). "Ueber das Gesetz der Energieverteilung im Normalspectrum." *Annalen der Physik* 4, 553–563. — The original blackbody quantization paper. [verify: full journal citation; OCR from secondary sources.]
- Einstein, A. (1905). "Über einen die Erzeugung und Verwandlung des Lichtes betreffenden heuristischen Gesichtspunkt." *Annalen der Physik* 17, 132–148. — The photoelectric effect paper introducing photons.
- Millikan, R.A. (1916). "A direct photoelectric determination of Planck's h." *Physical Review* 7(3), 355–388. [doi:10.1103/PhysRev.7.355](https://doi.org/10.1103/PhysRev.7.355) — Millikan's confirmation of Einstein's equation.
- Compton, A.H. (1923). "A quantum theory of the scattering of X-rays by light elements." *Physical Review* 21(5), 483–502. [doi:10.1103/PhysRev.21.483](https://doi.org/10.1103/PhysRev.21.483) — Compton scattering and the photon momentum.
- NIST CODATA 2018 recommended values of fundamental physical constants. [physics.nist.gov/constants](https://physics.nist.gov/cgi-bin/cuu/Value?h) — source for $h$, $k_B$, $c$ used in this chapter.
- Griffiths, D.J. (2018). *Introduction to Quantum Mechanics* (3rd ed.). Cambridge University Press. §1.2 (blackbody radiation, brief) — for historical framing; Griffiths begins with the wave function, so Ch 1 here precedes his Chapter 1.
- Townsend, J.S. (2012). *A Modern Approach to Quantum Mechanics* (2nd ed.). University Science Books. §1.3 (photons, particle nature of light), §1.4 (probability and quantum nature) — confirms the three photoelectric experimental facts and the Einstein/Millikan sequence.
- Krane, K.S. (2019). *Modern Physics* (4th ed.). Wiley. Chapter 3 — more extended treatment of photoelectric effect and Compton scattering with relativistic kinematics.
- Nobel Prize facts: Einstein 1921 (awarded 1922) — [nobelprize.org/prizes/physics/1921/einstein/facts/](https://www.nobelprize.org/prizes/physics/1921/einstein/facts/); Millikan 1923 — [nobelprize.org/prizes/physics/1923/millikan/facts/](https://www.nobelprize.org/prizes/physics/1923/millikan/facts/); Compton 1927 — [nobelprize.org/prizes/physics/1927/compton/facts/](https://www.nobelprize.org/prizes/physics/1927/compton/facts/).
- Hake, R.R. (1998). "Interactive-engagement versus traditional methods." *Am. J. Phys.* 66(1), 64–74. [doi:10.1119/1.18809](https://pubs.aip.org/aapt/ajp/article/66/1/64/1055076/Interactive-engagement-versus-traditional-methods) — pedagogical basis for simulation-first approach.

---

*Chapter 2 follows: de Broglie turns the argument around and asks whether the particle-nature of light implies a wave-nature of matter. If photons have momentum $p = h/\lambda$, what is the wavelength of an electron?*
