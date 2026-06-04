# Chapter 6 — Finite Wells, Steps, and Barriers
*Why walls that end are more interesting than walls that don't.*

In 1928, Friedrich Hund was staring at a nitrogen molecule and noticing that the Schrödinger equation was about to tell him something uncomfortable. The two nitrogen atoms sit in a potential well roughly 9.8 eV deep. Thermal energy at room temperature is about 0.025 eV. Classical mechanics says: the molecule is stable, obviously. The activation energy dwarfs thermal fluctuations by a factor of nearly four hundred.

But Hund noticed that the wave function does not vanish at the edge of the classically allowed region. It decays into the forbidden zone and arrives at the other side with non-zero amplitude. The barrier is not a wall. It is a region of exponential suppression — and exponential suppression, however ferocious, is not zero. The molecule could, in principle, fall apart without ever acquiring the activation energy. In this case the barrier is wide enough and deep enough that the dissociation rate is negligibly small — but the point stands: the rules had changed.

Two years later, George Gamow used the same mathematics to solve a puzzle that had stumped nuclear physicists for a decade. A nucleus traps an alpha particle behind a Coulomb barrier roughly 30 MeV high. The alpha particle that escapes has only 4–8 MeV of kinetic energy. Classically, it is stuck permanently. Quantum-mechanically, it leaks out — and the leaking rate depends so sensitively on barrier height and particle energy that a factor of two in energy produces twenty-four orders of magnitude of difference in half-life. The decay rate of uranium-238 differs from that of polonium-212 by a factor of $10^{21}$, and the tunneling formula accounts for it.

What makes all of this possible is the subject of this chapter: what happens when the walls are finite.

---

## The Finite Square Well

Start by taking the infinite square well from Chapter 5 and lowering the walls. The potential is $V = -V_0$ for $|x| < L/2$ and $V = 0$ outside, with $V_0 > 0$. Bound states have $-V_0 < E < 0$ — they sit below the top of the well but above its floor.

Inside the well, the Schrödinger equation describes a particle with kinetic energy $E + V_0 > 0$, so the solutions are oscillatory:

$$\psi_\text{in}(x) = A\cos(kx) + B\sin(kx), \qquad k = \frac{\sqrt{2m(E+V_0)}}{\hbar}.$$

Outside, the kinetic energy is $E < 0$, so the solutions are exponentials. Normalizable solutions must decay away from the well:

$$\psi_\text{out}(x) = Ce^{-\kappa|x|}, \qquad \kappa = \frac{\sqrt{2m|E|}}{\hbar}.$$

The first thing to notice is that $\psi$ does not vanish at $x = \pm L/2$. In the infinite well, the infinite walls forced it to zero there, which gave us quantization directly. Here, we have to impose continuity of $\psi$ and $\psi'$ at both walls, and that matching gives the condition on allowed energies.

The potential is symmetric, so solutions split cleanly into even-parity states (cosine inside) and odd-parity states (sine inside). For even-parity states, matching at $x = L/2$ yields:

$$\kappa = k\tan\!\left(\frac{kL}{2}\right).$$

For odd-parity states:

$$\kappa = -k\cot\!\left(\frac{kL}{2}\right).$$

Neither equation can be solved analytically for $E$. But there is a clean graphical approach. Define $z = kL/2$ and $z_0 = (L/2\hbar)\sqrt{2mV_0}$, so that $\kappa L/2 = \sqrt{z_0^2 - z^2}$. The even condition becomes:

$$\sqrt{z_0^2 - z^2} = z\tan z.$$

The left side is a quarter-circle of radius $z_0$. The right side is a series of tangent branches. Each intersection of the circle with a tangent branch is one even-parity bound state. The odd states come from intersections with $-z\cot z$.

<!-- → [FIGURE: graphical solution plot — quarter-circle of radius z₀ intersecting z·tan(z) branches (even states) and −z·cot(z) branches (odd states); label each crossing with E₁, E₂, etc.; show two cases: z₀ = 3π/4 (two bound states) and z₀ = 3π/2 (four bound states)] -->

Count the crossings and you learn something the infinite well never taught: the finite well has a **finite** number of bound states. The number is roughly $z_0/(\pi/2)$ rounded up — which means $N \approx (L/\pi\hbar)\sqrt{2mV_0}$ in physical units. Make the well shallower or narrower and levels disappear from the top. Make it deeper or wider and new levels appear. But there is always at least one — the finite square well always has a ground state, no matter how shallow. You can prove this graphically: the quarter-circle always intersects the first tangent branch at least once, no matter how small $z_0$.

What does the wave function look like outside the well? It decays as $e^{-\kappa|x|}$. The characteristic length $1/\kappa = \hbar/\sqrt{2m|E|}$ is the penetration depth. A tightly-bound ground state with large $|E|$ has a small penetration depth — the wave function hugs the well. A loosely-bound state near $E = 0$ has a large penetration depth — the wave function leaks far beyond the classical turning points, extending into space where the particle classically has no business being.

This is not the wave function misbehaving. It is the wave function doing exactly what the Schrödinger equation requires.

<!-- → [FIGURE: side-by-side wave functions for two bound states in a finite well — tightly bound ground state with short evanescent tails vs. weakly bound excited state with long evanescent tails; show classical turning points as dashed lines] -->

As $V_0 \to \infty$, the penetration depth goes to zero and the energy levels recover the infinite-well values $n^2\pi^2\hbar^2/(2mL^2)$. The infinite well is just the limit of the finite well with infinitely impenetrable walls.

---

## The Potential Step: Partial Reflection from Nothing

Now study scattering. The potential is a step: $V = 0$ for $x < 0$, $V = V_0$ for $x > 0$. A particle comes in from the left. The question is how much transmits and how much reflects.

Before writing any wave functions, set up the right accounting tool. The **probability current** is:

$$J(x,t) = \frac{\hbar}{m}\,\mathrm{Im}\!\left(\psi^*\frac{\partial\psi}{\partial x}\right).$$

For a rightward plane wave $Ae^{ikx}$, this gives $J = \hbar k|A|^2/m$ — probability flowing rightward at rate proportional to speed times density, exactly as you'd expect. The transmission coefficient $T$ is the ratio of transmitted current to incident current; the reflection coefficient $R$ is reflected current over incident current. Conservation of probability demands $R + T = 1$.

**When the particle has enough energy** ($E > V_0$): in region I, $\psi_I = Ae^{ik_0 x} + Be^{-ik_0 x}$ with $k_0 = \sqrt{2mE}/\hbar$; in region II, only a rightward wave $\psi_{II} = Ce^{ik_1 x}$ with $k_1 = \sqrt{2m(E-V_0)}/\hbar$. Matching $\psi$ and $\psi'$ at $x = 0$:

$$A + B = C, \qquad k_0(A-B) = k_1 C.$$

Solving: $B/A = (k_0 - k_1)/(k_0 + k_1)$ and $C/A = 2k_0/(k_0 + k_1)$. Now compute currents — and here is where the subtlety appears. The transmitted current is $\hbar k_1|C|^2/m$, not $\hbar k_0|C|^2/m$, because the particle moves at a different speed on the far side. Using probability current throughout:

$$R = \left(\frac{k_0 - k_1}{k_0 + k_1}\right)^2, \qquad T = \frac{4k_0 k_1}{(k_0 + k_1)^2}.$$

Check: $(k_0 - k_1)^2 + 4k_0k_1 = (k_0 + k_1)^2$. $R + T = 1$. $\checkmark$

Here is the quantum surprise: $R \neq 0$ even though the particle has enough energy to clear the step. Classically, a particle with $E > V_0$ transmits — full stop. Quantum-mechanically, any abrupt change in $k$ produces partial reflection, the same way an impedance mismatch in a transmission line reflects part of a signal. What matters is not whether the particle can clear the barrier energetically, but how sharply $k$ changes at the boundary. Reflection vanishes only when $k_0 = k_1$, which requires $V_0 = 0$. Even a step downward ($V_0 < 0$) partially reflects.

<!-- → [CHART: R(E) and T(E) vs E/V₀ for the potential step, linear axes — show R=1 for E<V₀, smooth transition at E=V₀, both curves approaching limiting values as E→∞] -->

**When the particle does not have enough energy** ($E < V_0$): now $k_1 = \sqrt{2m(E-V_0)}/\hbar$ is imaginary. Write $\kappa = \sqrt{2m(V_0-E)}/\hbar$ (real, positive), and the bounded solution in region II is $\psi_{II} = Ce^{-\kappa x}$ — a decaying exponential. Matching gives $|B/A|^2 = 1$, so $R = 1$ and $T = 0$.

Total reflection. But the wave function in region II is not zero. There is an evanescent tail penetrating the forbidden region with characteristic length $1/\kappa$. Probability density is present there — but no net current flows. The probability sloshes in and out of the step without transmitting. This is not tunneling — the barrier has infinite extent, so the evanescent tail never reaches a far edge where it can launch a transmitted wave.

---

## The Rectangular Barrier: Tunneling

Now give the barrier a finite width. $V = V_0$ for $0 < x < L$ and $V = 0$ elsewhere. A particle with $E < V_0$ comes in from the left. Classical prediction: total reflection. Quantum prediction: something else entirely.

Three regions:

- Region I ($x < 0$): $\psi_I = Ae^{ikx} + Be^{-ikx}$, $\hspace{2pt}$ $k = \sqrt{2mE}/\hbar$.
- Region II ($0 < x < L$): $\psi_{II} = Ce^{\kappa x} + De^{-\kappa x}$, $\hspace{2pt}$ $\kappa = \sqrt{2m(V_0-E)}/\hbar$.
- Region III ($x > L$): $\psi_{III} = Fe^{ikx}$ (no reflected wave; nothing to reflect from on the right).

Match $\psi$ and $\psi'$ at both interfaces. The algebra is straightforward — four continuity conditions, four unknowns — and the result is exact:

$$T_\text{exact} = \left[1 + \frac{V_0^2\sinh^2(\kappa L)}{4E(V_0 - E)}\right]^{-1}.$$

<!-- → [CHART: T(E) on log y-axis from 10⁻¹² to 1, showing T_exact (solid) and T_WKB (dashed) vs E/V₀ — both curves below barrier, resonance peaks above barrier, vertical line at E=V₀] -->

This formula contains everything. The dependence on barrier height $V_0$, barrier width $L$, and particle energy $E$ is all there, exact, no approximations. Let me unpack what it says.

For a thick barrier ($\kappa L \gg 1$), $\sinh(\kappa L) \approx e^{\kappa L}/2$, and the denominator is dominated by the exponential:

$$T_\text{exact} \approx \frac{16E(V_0 - E)}{V_0^2}\,e^{-2\kappa L}.$$

The WKB approximation (which I'll develop in Chapter 11) gives $T_\text{WKB} = e^{-2\kappa L}$. The ratio is $16E(V_0-E)/V_0^2$ — a smooth prefactor of order unity when $E$ is well below $V_0$. WKB captures the exponential suppression exactly; it misses only the prefactor. For most purposes, the exponential is all that matters.

And the exponential is extraordinary. $T \propto e^{-2\kappa L}$. Double the barrier width and you square $e^{-2\kappa L}$ — the transmission plummets. A scanning tunneling microscope exploits this directly: one extra ångström of gap between tip and surface changes the tunneling current by a factor of $e^{2\kappa} \approx 7$ to $10$ depending on the material. That single decade of sensitivity per ångström is what makes atomic-resolution imaging possible — the instrument is a tunneling current meter, and the current is an exponential ruler.

<!-- → [FIGURE: schematic of STM geometry — tip hovering over surface, tunneling gap d, wave function decaying exponentially in the gap, with annotation showing one-ångström change → factor-of-7 current change] -->

**Above the barrier** ($E > V_0$): $\kappa$ becomes imaginary. Let $k_2 = \sqrt{2m(E-V_0)}/\hbar$, so $\kappa = ik_2$ and $\sinh(i\theta) = i\sin\theta$. The formula becomes:

$$T_\text{exact} = \left[1 + \frac{V_0^2\sin^2(k_2 L)}{4E(E - V_0)}\right]^{-1}.$$

Now $T = 1$ whenever $\sin(k_2 L) = 0$, i.e., when $k_2 L = n\pi$. The barrier is perfectly transparent when its width is exactly an integer number of half-wavelengths at the energy inside the barrier. The wave fits the barrier; constructive interference makes it as though the barrier is not there. These are **resonances** — and they are the quantum analogue of anti-reflection coatings in optics, or of a Fabry-Pérot cavity at resonance. Between resonances, $T < 1$ even with $E > V_0$. The particle has plenty of energy and still partially reflects.

---

## A Worked Calculation

An electron ($m_e = 9.109 \times 10^{-31}$ kg) with kinetic energy $E = 1$ eV hits a rectangular barrier of height $V_0 = 5$ eV and width $L = 5$ Å. What is $T$?

First, $\kappa$:

$$\kappa = \frac{\sqrt{2m_e(V_0 - E)}}{\hbar} = \frac{\sqrt{2 \times 9.109\times10^{-31} \times 4 \times 1.602\times10^{-19}}}{1.055\times10^{-34}} \approx 1.025\times10^{10}\ \text{m}^{-1} = 1.025\ \text{Å}^{-1}.$$

Then $\kappa L = 1.025 \times 5 = 5.125$. Since $\kappa L \gg 1$, the thick-barrier limit applies.

$\sinh(5.125) = (e^{5.125} - e^{-5.125})/2 \approx (168.2 - 0.006)/2 \approx 84.1.$

Plugging into the exact formula:

$$T_\text{exact} = \left[1 + \frac{25 \times (84.1)^2}{4 \times 1 \times 4}\right]^{-1} = \left[1 + 11052\right]^{-1} \approx 9.1\times10^{-5}.$$

WKB gives $T_\text{WKB} = e^{-10.25} \approx 3.5\times10^{-5}$.

The ratio: $T_\text{exact}/T_\text{WKB} \approx 2.56$. The prefactor $16E(V_0-E)/V_0^2 = 16\times1\times4/25 = 2.56$. Agreement exact, as it must be. $\checkmark$

Now the physical punchline. The transmission is $\sim 10^{-4}$ — small, but non-zero. If the barrier were 10 Å wide instead of 5, $\kappa L$ doubles to 10.25, and $T_\text{WKB}$ drops to $e^{-20.5} \approx 1.25\times10^{-9}$ — four additional orders of magnitude. The exponential is relentless. This is why barrier width matters so much more than almost anything else in tunneling calculations.

---

## Why There Is No Energy Debt

The pop-science version of tunneling says: "The particle borrows energy from the vacuum — permitted by the time-energy uncertainty principle — crosses the barrier before the debt is called in, and pays it back on the other side." This story is wrong, and it is worth being precise about why.

The uncertainty relation $\Delta E\,\Delta t \geq \hbar/2$ does not license energy borrowing for a time $\Delta t$. That is not what the relation means. Energy is conserved at every moment inside the barrier; the total energy of the particle is $E$ throughout — in region I, inside the barrier, and in region III. The wave function inside the barrier, $Ce^{\kappa x} + De^{-\kappa x}$, is a perfectly valid solution to the time-independent Schrödinger equation for a particle of energy $E$ in a region where $V = V_0 > E$. The function is real and decaying — not oscillatory — but it is the correct solution. There is no negative kinetic energy; there is no energy overdraft; there is no payment schedule.

What happens is simpler and stranger than the pop-science story: the wave equation requires non-zero amplitude in the classically forbidden region, and when the barrier is finite, that amplitude reaches the far side and launches a transmitted wave. The transmitted amplitude is small because the decaying exponential has attenuated across the width $L$. That is all. The particle does not borrow anything. It passes through because the mathematics of partial differential equations does not know what "classically forbidden" means.

<!-- → [FIGURE: energy diagram for rectangular barrier — flat total energy E as horizontal line, barrier region V₀ above E, wave function shown below: oscillatory in regions I and III, decaying in region II, with annotation "E is constant throughout; only the character of the solution changes"] -->

---

## LLM Exercises

### The deliverable

`06-barrier-explorer.html` — a single self-contained HTML file with three tabs: **Bound States** (graphical solution for the finite well), **Step** ($R$ and $T$ vs. $E$ for a potential step), and **Barrier** ($T_\text{exact}$ and $T_\text{WKB}$ vs. $E$, plus an animated wave packet on a rectangular barrier).

### CLAUDE.md amendment for this chapter

````markdown
## Chapter 6 — Finite Wells, Steps, and Barriers

BARRIER AND STEP PHYSICS RULES

1. EXACT RECTANGULAR BARRIER (E < V₀):
     T_exact = 1 / (1 + (V₀² sinh²(κL)) / (4E(V₀ − E)))
     κ = sqrt(2m(V₀ − E)) / ℏ
   For E > V₀, replace sinh(κL) → i sin(k₂L), κ → ik₂,
   k₂ = sqrt(2m(E − V₀)) / ℏ:
     T_exact = 1 / (1 + (V₀² sin²(k₂L)) / (4E(E − V₀)))
   Box these two cases separately in comments; never apply the
   E < V₀ formula when E > V₀.

2. TRANSMISSION FOR A STEP:
     R = ((k₀ − k₁) / (k₀ + k₁))²
     T = 4k₀k₁ / (k₀ + k₁)²
   VERIFY R + T = 1 at every parameter setting as a runtime check.
   T ≠ |amplitude ratio|² unless k₀ = k₁. Use probability current.

3. WKB FOR RECTANGULAR BARRIER:
     T_WKB = exp(−2κL)   for E < V₀
   On the T(E) plot, show both curves on a LOG y-axis. The two
   curves run parallel below the barrier; label the offset
   "WKB misses prefactor 16E(V₀−E)/V₀²."

4. FINITE WELL GRAPHICAL SOLUTION:
   Plot f_even(z) = z·tan(z) and f_odd(z) = −z·cot(z) vs.
   the circle sqrt(z₀² − z²). Crossings are bound states.
   z₀ = (L / 2ℏ) sqrt(2mV₀). z ∈ (0, z₀).
   Accurately handle the asymptotes of tan(z) at z = π/2, 3π/2 …

5. CRANK-NICOLSON WAVE PACKET (same architecture as Ch 11):
   Natural units ℏ = m = 1. 500 spatial points. Absorbing
   boundaries at 80% of box edges. Thomas tridiagonal solve.
   Pre-compute all frames on Play; cache; animate at 60 fps.
   Initial state: Gaussian centered left of barrier.

KNOWN FAILURE MODES:
(a) Applying E<V₀ formula when E>V₀ (sinh→sin switch missing).
(b) T = |F/A|² without the k ratio (wrong for a step).
(c) Linear y-axis on T(E) — always log.
(d) tan(z) asymptotes causing NaN in graphical solution.
(e) Missing absorbing boundaries → wave packet reflects off walls.
````

### The simulation prompt

````markdown
SHOW.
Three physical scenarios for a particle hitting a potential barrier or well:

1. FINITE SQUARE WELL BOUND STATES
Graphical solution: plot two curves vs z on [0, z₀]:
  Left side of matching condition: g(z) = sqrt(z₀² − z²)   (quarter-circle)
  Even states: f_e(z) = z tan(z)
  Odd states:  f_o(z) = −z cot(z)
Intersections of g with f_e or f_o are bound states.
z₀ = (L/2ℏ)·sqrt(2mV₀). Use natural units ℏ = 2m = 1 so z₀ = L·sqrt(V₀)/2.
Controls: V₀ slider (1–20), L slider (1–10). Label each intersection with
its parity (E or O) and energy level number.

2. POTENTIAL STEP: R AND T vs E
Plot R(E) (red) and T(E) (blue) on linear y-axis [0,1] vs E/V₀ on [0,3].
For E < V₀: R = 1, T = 0.
For E > V₀: R = ((k₀−k₁)/(k₀+k₁))², T = 4k₀k₁/(k₀+k₁)².
k₀ = sqrt(E), k₁ = sqrt(E−V₀) in natural units.
Verify R + T = 1 (log to console at every E). Mark V₀ with a vertical line.
Note the approach to R→0 only as E→∞.
Controls: V₀ slider (1–10).

3. RECTANGULAR BARRIER: T(E) AND ANIMATED WAVE PACKET
Panel A (left, 600px wide, log y-axis): T vs E/V₀ from 10⁻¹² to 1.
Two curves: T_exact (solid) and T_WKB (dashed).
For E < V₀: T_exact from sinh formula; T_WKB = exp(−2κL).
For E > V₀: T_exact from sin formula; T_WKB not shown (classical).
Show resonance peaks above the barrier.

Panel B (right, 400px wide): animated Gaussian wave packet hitting barrier.
Crank-Nicolson, 500 points, x ∈ [−50, 50], ℏ = m = 1.
Initial packet: center x₀ = −20, width σ = 3, momentum p₀ = sqrt(2E).
Barrier as translucent gray fill. Energy E as horizontal dashed line.
Play/Pause/Reset. Time counter.

Controls: V₀ (1–10), L (1–10), E (0.1·V₀ to 2·V₀).

SAY.
Produce a single file `06-barrier-explorer.html`.
Three tabs at the top: "Finite Well", "Step", "Barrier".
Each tab contains its own SVG and controls.
D3 v7 from CDN. Vanilla JS. No math.js or numeric.js.
Thomas algorithm for Crank-Nicolson solve (pure JS, ~25 lines).
Complex arithmetic as {re, im} objects throughout.

CONSTRAIN.
- Natural units ℏ = m = 1 throughout.
- The T vs E/V₀ plot MUST use a LOG y-axis (10⁻¹² to 1).
- R + T = 1 check logged to console every time parameters change.
- The barrier tab must show both T_exact and T_WKB on the same plot.
- The wave packet must use absorbing boundaries (imaginary potential at edges).
- All physics steps commented in code.

VERIFY.
After writing the file, check:
(a) V₀=5, L=5, E=1: T_exact ≈ 9×10⁻⁵, T_WKB ≈ 3.5×10⁻⁵, ratio ≈ 2.56.
(b) V₀=5, L=5, E=5 (at barrier top): T_exact = [1 + 0]⁻¹ = 1? No — at E=V₀,
    κ→0 and sinh(κL)→κL→0, so T_exact→1. Verify this limit.
(c) Step, V₀=2, E=8: k₀=sqrt(8), k₁=sqrt(6); R=((√8−√6)/(√8+√6))²≈0.0102.
(d) Resonance: V₀=2, L=π/sqrt(2E−V₀) for E=4; T_exact=1. Verify resonance peak.
````

### Exploration tasks

**Task 1 — Counting bound states.** In the Finite Well tab, set $V_0 = 4$ and $L = 5$. Count the intersections. Now reduce $V_0$ until one level disappears. At what $V_0$ does the second bound state vanish? Record the value of $z_0$ at that point. Compare to the threshold condition $z_0 = \pi/2$ (first odd-parity state just appears when $z_0 = \pi/2$).

**Task 2 — Reflection at the step.** In the Step tab, observe that $R \to 1$ as $E \to V_0$ from above. At $E = 2V_0$, read off $R$. At $E = 10V_0$, read off $R$. Does $R$ approach zero? Explain physically why a very high-energy particle still reflects slightly.

**Task 3 — Exponential sensitivity.** In the Barrier tab, set $V_0 = 5, E = 1$. Read off $T_\text{exact}$. Now double $L$. By what factor does $T$ change? Double $L$ again. Now vary $V_0$ at fixed $L$ and $E$. Which parameter — height or width — gives more control over $T$?

**Task 4 — The resonance peaks.** Set $E > V_0$ in the Barrier tab. Find the first resonance (first energy above $V_0$ where $T = 1$). Verify that the barrier width is exactly half a de Broglie wavelength: $L = \pi/k_2$ in natural units.

**Task 5 — The wave packet.** Play the animation with $V_0 = 5, L = 3, E = 1$. Pause as the wave packet reaches the barrier. Describe what is happening in the barrier region. After the packet fully passes, compare the relative sizes of the transmitted and reflected pulses. Use the $T$ value from Panel A to predict $|\psi_\text{trans}|^2_\text{max}/|\psi_\text{inc}|^2_\text{max}$ and check it against the simulation.

---

## Still Puzzling

**How long does tunneling take?** The formula for $T$ gives the probability of crossing, not the time spent inside the barrier. Several definitions of "tunneling time" appear in the literature — the dwell time, the phase time, the Büttiker-Landauer time, the Larmor clock time — and they give different answers. Attosecond-streaking experiments (Eckle et al., 2008; Sainadh et al., 2019) have measured something, but the theoretical interpretation is still contested. This chapter gives you $T$. It does not give you a tunneling time. The framework is incomplete here.

**Does tunneling allow faster-than-light signaling?** The claim recurs in popular science: a tunneled pulse can have a group velocity exceeding $c$, therefore information travels faster than light. What actually happens is pulse reshaping. The barrier selects and amplifies the leading edge of the incident pulse, which was already there before the barrier. The front of the pulse does not move faster than $c$; the barrier preferentially transmits its early part. No information travels faster than $c$.

---

## Exercises

**Warm-up**

1. *[Transcendental matching, graphical counting]* A particle of mass $m$ is in a finite square well of width $L$ and depth $V_0$. (a) Show that the even-parity matching condition can be written $\sqrt{z_0^2 - z^2} = z\tan z$. (b) Sketch both sides for $z_0 = 3\pi/2$ and count the even-parity bound states. (c) How many total bound states (even + odd) exist for this $z_0$?
*What this tests: reading bound-state count from the graphical solution without solving transcendental equations numerically.*

2. *[$R + T = 1$ from probability current]* For the potential step at $E > V_0$: (a) verify $R + T = 1$ algebraically; (b) explain in one sentence why $T \neq |C/A|^2$; (c) compute $R$ when $E = 2V_0$.
*What this tests: keeping probability current accounting straight, and recognizing that amplitude ratios are not transmission coefficients.*

3. *[Evanescent penetration depth]* A particle with $E = 2$ eV hits a step with $V_0 = 5$ eV, $m = m_e$. (a) Compute $1/\kappa$ in nm. (b) By what factor does $|\psi|^2$ drop at $x = 1/\kappa$? At $x = 2/\kappa$?
*What this tests: quantifying how rapidly the evanescent tail decays and building intuition for penetration depth as a physical length.*

**Application**

4. *[Exact barrier transmission, numerical]* An electron with $E = 3$ eV hits a barrier with $V_0 = 6$ eV and $L = 3$ Å. (a) Compute $\kappa$ in Å$^{-1}$. (b) Compute $T_\text{exact}$ from equation (6.1). (c) Compute $T_\text{WKB}$. (d) Find the ratio and compare to $16E(V_0-E)/V_0^2$.
*What this tests: numerical fluency with the exact tunneling formula and verifying where WKB is accurate.*

5. *[Resonance condition above the barrier]* For $V_0 = 2$ eV, $L = 1$ nm, find the two lowest energies above $V_0$ at which $T = 1$. Then find the minimum value of $T$ between the first and second resonances.
*What this tests: applying the above-barrier formula and locating resonances as a condition on $k_2 L$.*

6. *[STM physics, exponential sensitivity]* An STM tip is held 4 Å above platinum ($\phi \approx 5.7$ eV). (a) Compute $\kappa$ in Å$^{-1}$. (b) Find the ratio of tunneling current at 4 Å vs. 5 Å. (c) By what factor does current change over a 2 Å surface step? (d) Explain in one sentence why this sensitivity enables atomic-resolution imaging.
*What this tests: connecting the tunneling formula to a real instrument and appreciating what exponential transduction means in practice.*

**Synthesis**

7. *[Finite well applied to nuclear physics]* The deuteron can be modeled as a finite square well with $V_0 \approx 35$ MeV, $L \approx 2.1$ fm, reduced mass $\mu \approx m_p/2$. (a) Compute $z_0$ using $\hbar c \approx 197$ MeV·fm. (b) How many even-parity bound states does this well support? (c) The deuteron has only one bound state. Is this consistent? What does it say about deuteron excited states?
*What this tests: applying the graphical bound-state formalism to a real physical system and cross-checking against experimental fact.*

8. *[Probability current as physical constraint]* Suppose someone proposes $\psi_{II} = Ce^{\kappa x}$ only (growing exponential) in the barrier region of the step. (a) Compute $J_{II}$. (b) Is $R + T = 1$ satisfied? (c) Why is this solution inadmissible?
*What this tests: using boundary conditions and current conservation to reject unphysical solutions rather than accepting any function that solves the TISE locally.*

**Challenge**

9. *[Resonances as anti-reflection coatings]* The above-barrier resonance condition $k_2 L = n\pi$ is structurally identical to the condition for a thin-film anti-reflection coating in optics ($n_\text{film} t = \lambda/4$ per layer). (a) Identify the optical analogue of each quantum quantity ($k_2$, $L$, $V_0$, $E$). (b) In a Fabry-Pérot cavity, resonances occur when the round-trip phase is $2\pi n$. Show that the quantum resonance condition has the same origin. (c) Suppose a "double barrier" potential has two rectangular barriers separated by a well. Predict qualitatively where resonances occur and explain the concept of a resonant tunneling diode.
*What this tests: transferring the resonance concept across physical contexts and beginning to think about devices built on controlled tunneling.*

---

## References

Griffiths, D. J., & Schroeter, D. F. (2018). *Introduction to Quantum Mechanics* (3rd ed.). Cambridge University Press. §2.5–2.6 (finite well), §2.7 (scattering, step, barrier).

Gamow, G. (1928). Zur Quantentheorie des Atomkernes. *Zeitschrift für Physik*, 51, 204.

Gurney, R. W., & Condon, E. U. (1928). Wave mechanics and radioactive disintegration. *Nature*, 122, 439; and *Physical Review*, 33, 127 (1929).

Binnig, G., & Rohrer, H. (1982). Scanning tunneling microscopy. *Physical Review Letters*, 49, 57.

Eckle, P. et al. (2008). Attosecond ionization and tunneling delay time measurements in helium. *Science*, 322, 1525.

Sainadh, U. S. et al. (2019). Attosecond angular streaking and tunnelling time in atomic hydrogen. *Nature*, 568, 75.

PhysicsLibreTexts: "3.4 — Finite Square Well," UCD Physics 9HE. https://phys.libretexts.org/Courses/University_of_California_Davis/UCD:_Physics_9HE_-_Modern_Physics/03:_One-Dimensional_Potentials/3.4:_Finite_Square_Well
