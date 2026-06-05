# Chapter 6 — Finite Wells, Steps, and Barriers
*Why walls that end are more interesting than walls that don't.*

In 1928 Friedrich Hund, looking at a nitrogen molecule, ran into something the Schrödinger equation was about to make awkward. The two nitrogen atoms sit in a potential well roughly 9.8 eV deep. Thermal energy at room temperature is about 0.025 eV. Classically there is nothing to discuss: the activation energy beats thermal fluctuations by nearly a factor of four hundred, so the molecule is stable, end of story.

Hund noticed otherwise. The wave function does not stop at the edge of the classically allowed region. It decays into the forbidden zone and emerges on the far side with nonzero amplitude. The barrier is not a wall; it is a region of exponential suppression — and exponential suppression, savage as it is, is never quite zero. So the molecule could, in principle, come apart without ever paying the activation energy. Here the barrier happens to be deep enough and wide enough that the dissociation rate is negligible, and the molecule is safe. But the rules had changed, and that is the point.

Two years later George Gamow turned the same mathematics on a problem that had defeated nuclear physicists for a decade. A nucleus holds an alpha particle behind a Coulomb barrier some 30 MeV high. The escaping alpha carries only 4–8 MeV of kinetic energy. Classically it is trapped forever. Quantum-mechanically it leaks — and the leak rate depends so violently on barrier height and particle energy that a factor of two in energy buys twenty-four orders of magnitude in half-life. Uranium-238 and polonium-212 differ in decay rate by a factor of $10^{21}$, and the tunneling formula accounts for the whole spread.

All of this rests on one change of assumption, which is the subject of this chapter: what happens when the walls are finite.

---

## The Finite Square Well

Take the infinite square well from Chapter 5 and lower the walls. The potential is $V = -V_0$ for $|x| < L/2$ and $V = 0$ outside, with $V_0 > 0$. Bound states have $-V_0 < E < 0$: below the top of the well, above its floor.

Inside, the particle has kinetic energy $E + V_0 > 0$, so the solutions oscillate:

$$\psi_\text{in}(x) = A\cos(kx) + B\sin(kx), \qquad k = \frac{\sqrt{2m(E+V_0)}}{\hbar}.$$

Outside, the kinetic energy is $E < 0$, so the solutions are exponentials, and normalizability demands the decaying ones:

$$\psi_\text{out}(x) = Ce^{-\kappa|x|}, \qquad \kappa = \frac{\sqrt{2m|E|}}{\hbar}.$$

Notice that $\psi$ does not vanish at $x = \pm L/2$. In the infinite well, the walls forced it to zero there and handed us quantization for free. Here we have to demand continuity of $\psi$ and $\psi'$ at both walls, and that matching is what fixes the allowed energies.

The potential is symmetric, so the solutions sort themselves into even-parity states (cosine inside) and odd-parity states (sine inside). Matching the even states at $x = L/2$ gives

$$\kappa = k\tan\!\left(\frac{kL}{2}\right),$$

and the odd states give

$$\kappa = -k\cot\!\left(\frac{kL}{2}\right).$$

Neither can be solved for $E$ in closed form. But the graphical route is clean. Set $z = kL/2$ and $z_0 = (L/2\hbar)\sqrt{2mV_0}$, so that $\kappa L/2 = \sqrt{z_0^2 - z^2}$. The even condition becomes

$$\sqrt{z_0^2 - z^2} = z\tan z.$$

The left side is a quarter-circle of radius $z_0$; the right side is a forest of tangent branches. Every place the circle crosses a tangent branch is one even-parity bound state. The odd states come from crossings with $-z\cot z$.

<!-- → [FIGURE: graphical solution plot — quarter-circle of radius z₀ intersecting z·tan(z) branches (even states) and −z·cot(z) branches (odd states); label each crossing with E₁, E₂, etc.; show two cases: z₀ = 3π/4 (two bound states) and z₀ = 3π/2 (four bound states)] -->

![graphical solution plot — quarter-circle of radius z₀ intersecting z·tan(z) branches (even states) and −z·cot(z) branches (odd states)](../images/06-finite-wells-steps-and-barriers-fig-01.png)
*Figure 6.1 — graphical solution plot — quarter-circle of radius z₀ intersecting z·tan(z) branches (even states) and −z·cot(z) branches (odd states)*

Count the crossings and the finite well teaches you something the infinite well could not: it has a **finite** number of bound states. Roughly $z_0/(\pi/2)$, rounded up — in physical units $N \approx (L/\pi\hbar)\sqrt{2mV_0}$. Shrink the well, in depth or width, and levels fall out the top; enlarge it and new levels appear. But one level always survives: the finite square well, however shallow, always holds a ground state. The proof is in the picture — the quarter-circle crosses the first tangent branch at least once for any $z_0$, no matter how small.

Outside the well the wave function decays as $e^{-\kappa|x|}$, with characteristic length $1/\kappa = \hbar/\sqrt{2m|E|}$, the penetration depth. A tightly bound state (large $|E|$) has a short penetration depth and hugs the well. A loosely bound state near $E = 0$ has a long one and reaches far past the classical turning points, into territory where a classical particle simply could not be.

This is not the wave function misbehaving. It is the wave function doing precisely what the Schrödinger equation demands.

<!-- → [FIGURE: side-by-side wave functions for two bound states in a finite well — tightly bound ground state with short evanescent tails vs. weakly bound excited state with long evanescent tails; show classical turning points as dashed lines] -->

![side-by-side wave functions for two bound states in a finite well — tightly bound ground state with short evanescent tails vs. weakly bound…](../images/06-finite-wells-steps-and-barriers-fig-02.png)
*Figure 6.2 — side-by-side wave functions for two bound states in a finite well — tightly bound ground state with short evanescent tails vs. weakly bound…*

As $V_0 \to \infty$, the penetration depth shrinks to zero and the energies climb back to the infinite-well values $n^2\pi^2\hbar^2/(2mL^2)$. The infinite well is nothing but the finite well with the walls cranked up until nothing leaks.

---

## The Potential Step: Partial Reflection from Nothing

Now switch from bound states to scattering. The potential is a single step: $V = 0$ for $x < 0$, $V = V_0$ for $x > 0$. Send a particle in from the left and ask how much transmits and how much reflects.

Before writing down any wave functions, get the right bookkeeping. The **probability current** is

$$J(x,t) = \frac{\hbar}{m}\,\mathrm{Im}\!\left(\psi^*\frac{\partial\psi}{\partial x}\right).$$

For a rightward plane wave $Ae^{ikx}$ it gives $J = \hbar k|A|^2/m$ — probability flowing right at a rate of speed times density, which is exactly what it should be. Transmission $T$ is transmitted current over incident current; reflection $R$ is reflected over incident. Conservation of probability insists $R + T = 1$.

**When the particle has the energy to spare** ($E > V_0$): region I holds $\psi_I = Ae^{ik_0 x} + Be^{-ik_0 x}$ with $k_0 = \sqrt{2mE}/\hbar$, and region II holds only a rightward wave $\psi_{II} = Ce^{ik_1 x}$ with $k_1 = \sqrt{2m(E-V_0)}/\hbar$. Matching $\psi$ and $\psi'$ at $x = 0$:

$$A + B = C, \qquad k_0(A-B) = k_1 C.$$

Solving gives $B/A = (k_0 - k_1)/(k_0 + k_1)$ and $C/A = 2k_0/(k_0 + k_1)$. Now the currents — and here is where it is easy to go wrong. The transmitted current is $\hbar k_1|C|^2/m$, not $\hbar k_0|C|^2/m$, because the particle moves at a different speed beyond the step. Use the current throughout and you get

$$R = \left(\frac{k_0 - k_1}{k_0 + k_1}\right)^2, \qquad T = \frac{4k_0 k_1}{(k_0 + k_1)^2}.$$

Check: $(k_0 - k_1)^2 + 4k_0k_1 = (k_0 + k_1)^2$, so $R + T = 1$. $\checkmark$

Here is the quantum surprise: $R \neq 0$ even though the particle clears the step with energy to spare. Classically, $E > V_0$ means full transmission and nothing else. Quantum-mechanically, any abrupt change in $k$ throws back part of the wave, the same way an impedance mismatch reflects part of a signal on a transmission line. What matters is not whether the particle can surmount the step energetically, but how sharply $k$ changes at the boundary. The reflection vanishes only when $k_0 = k_1$, i.e. $V_0 = 0$. Even a step *down* ($V_0 < 0$) reflects.

<!-- → [CHART: R(E) and T(E) vs E/V₀ for the potential step, linear axes — show R=1 for E<V₀, smooth transition at E=V₀, both curves approaching limiting values as E→∞] -->

![R(E) and T(E) vs E/V₀ for the potential step, linear axes — show R=1 for E<V₀, smooth transition at E=V₀, both curves approaching limiting…](../images/06-finite-wells-steps-and-barriers-fig-03.png)
*Figure 6.3 — R(E) and T(E) vs E/V₀ for the potential step, linear axes — show R=1 for E<V₀, smooth transition at E=V₀, both curves approaching limiting…*

**When the particle does not have the energy** ($E < V_0$): now $k_1 = \sqrt{2m(E-V_0)}/\hbar$ is imaginary. Write $\kappa = \sqrt{2m(V_0-E)}/\hbar$ (real and positive), so the bounded solution in region II is the decaying exponential $\psi_{II} = Ce^{-\kappa x}$. Matching gives $|B/A|^2 = 1$, hence $R = 1$ and $T = 0$.

Total reflection — but the wave function in region II is not zero. An evanescent tail penetrates the forbidden region over a length $1/\kappa$. Probability density lives there, yet no net current flows: the probability sloshes in and back out of the step without transmitting. This is not tunneling. The barrier has infinite extent, so the evanescent tail never reaches a far edge from which it could launch a transmitted wave.

---

## The Rectangular Barrier: Tunneling

Give the barrier a finite width. $V = V_0$ for $0 < x < L$ and $V = 0$ elsewhere; a particle with $E < V_0$ comes in from the left. Classical verdict: total reflection. Quantum verdict: not even close.

Three regions:

- Region I ($x < 0$): $\psi_I = Ae^{ikx} + Be^{-ikx}$, $\hspace{2pt}$ $k = \sqrt{2mE}/\hbar$.
- Region II ($0 < x < L$): $\psi_{II} = Ce^{\kappa x} + De^{-\kappa x}$, $\hspace{2pt}$ $\kappa = \sqrt{2m(V_0-E)}/\hbar$.
- Region III ($x > L$): $\psi_{III} = Fe^{ikx}$ (no reflected wave; nothing to reflect from on the right).

Match $\psi$ and $\psi'$ at both interfaces — four continuity conditions, four unknowns, ordinary algebra — and the result is exact:

$$T_\text{exact} = \left[1 + \frac{V_0^2\sinh^2(\kappa L)}{4E(V_0 - E)}\right]^{-1}.$$

<!-- → [CHART: T(E) on log y-axis from 10⁻¹² to 1, showing T_exact (solid) and T_WKB (dashed) vs E/V₀ — both curves below barrier, resonance peaks above barrier, vertical line at E=V₀] -->

![T(E) on log y-axis from 10⁻¹² to 1, showing T_exact (solid) and T_WKB (dashed) vs E/V₀ — both curves below barrier, resonance peaks above…](../images/06-finite-wells-steps-and-barriers-fig-04.png)
*Figure 6.4 — T(E) on log y-axis from 10⁻¹² to 1, showing T_exact (solid) and T_WKB (dashed) vs E/V₀ — both curves below barrier, resonance peaks above…*

Everything is in this formula: the dependence on barrier height $V_0$, width $L$, and energy $E$, exact and unapproximated. Read it carefully.

For a thick barrier ($\kappa L \gg 1$), $\sinh(\kappa L) \approx e^{\kappa L}/2$ and the exponential swamps the denominator:

$$T_\text{exact} \approx \frac{16E(V_0 - E)}{V_0^2}\,e^{-2\kappa L}.$$

The WKB approximation (Chapter 11) gives $T_\text{WKB} = e^{-2\kappa L}$. The ratio is $16E(V_0-E)/V_0^2$ — a smooth prefactor of order unity when $E$ sits well below $V_0$. WKB nails the exponential and misses only the prefactor. For most purposes the exponential is the whole story.

And the exponential is ferocious. $T \propto e^{-2\kappa L}$, so doubling the barrier width *squares* $e^{-2\kappa L}$ and the transmission collapses. The scanning tunneling microscope lives off exactly this: one extra ångström of gap between tip and surface changes the tunneling current by a factor of $e^{2\kappa} \approx 7$ to $10$, depending on the material. That single decade of sensitivity per ångström is what makes atomic-resolution imaging work. The instrument is a tunneling-current meter, and the current is an exponential ruler.

<!-- → [FIGURE: schematic of STM geometry — tip hovering over surface, tunneling gap d, wave function decaying exponentially in the gap, with annotation showing one-ångström change → factor-of-7 current change] -->

![schematic of STM geometry — tip hovering over surface, tunneling gap d, wave function decaying exponentially in the gap, with annotation…](../images/06-finite-wells-steps-and-barriers-fig-05.png)
*Figure 6.5 — schematic of STM geometry — tip hovering over surface, tunneling gap d, wave function decaying exponentially in the gap, with annotation…*

**Above the barrier** ($E > V_0$): $\kappa$ goes imaginary. Set $k_2 = \sqrt{2m(E-V_0)}/\hbar$, so $\kappa = ik_2$ and $\sinh(i\theta) = i\sin\theta$, and the formula turns into

$$T_\text{exact} = \left[1 + \frac{V_0^2\sin^2(k_2 L)}{4E(E - V_0)}\right]^{-1}.$$

Now $T = 1$ whenever $\sin(k_2 L) = 0$, that is, $k_2 L = n\pi$. The barrier becomes perfectly transparent when its width is exactly an integer number of half-wavelengths at the energy inside it. The wave fits the barrier, constructive interference erases it, and the particle sails through as if it were not there. These are **resonances** — the quantum cousins of anti-reflection coatings in optics, or of a Fabry-Pérot cavity tuned to resonance. Off resonance, $T < 1$ even with $E > V_0$: the particle has energy to burn and still bounces back in part.

---

## A Worked Calculation

An electron ($m_e = 9.109 \times 10^{-31}$ kg) with kinetic energy $E = 1$ eV strikes a rectangular barrier of height $V_0 = 5$ eV and width $L = 5$ Å. Find $T$.

Start with $\kappa$:

$$\kappa = \frac{\sqrt{2m_e(V_0 - E)}}{\hbar} = \frac{\sqrt{2 \times 9.109\times10^{-31} \times 4 \times 1.602\times10^{-19}}}{1.055\times10^{-34}} \approx 1.025\times10^{10}\ \text{m}^{-1} = 1.025\ \text{Å}^{-1}.$$

Then $\kappa L = 1.025 \times 5 = 5.125$. Since $\kappa L \gg 1$, this is squarely the thick-barrier limit.

$\sinh(5.125) = (e^{5.125} - e^{-5.125})/2 \approx (168.2 - 0.006)/2 \approx 84.1.$

Into the exact formula:

$$T_\text{exact} = \left[1 + \frac{25 \times (84.1)^2}{4 \times 1 \times 4}\right]^{-1} = \left[1 + 11052\right]^{-1} \approx 9.1\times10^{-5}.$$

WKB gives $T_\text{WKB} = e^{-10.25} \approx 3.5\times10^{-5}$.

The ratio: $T_\text{exact}/T_\text{WKB} \approx 2.56$. The prefactor $16E(V_0-E)/V_0^2 = 16\times1\times4/25 = 2.56$. They agree exactly, as they must. $\checkmark$

Now the physics. The transmission is $\sim 10^{-4}$ — tiny, but not zero. Widen the barrier to 10 Å and $\kappa L$ doubles to 10.25, dropping $T_\text{WKB}$ to $e^{-20.5} \approx 1.25\times10^{-9}$ — four more orders of magnitude gone. The exponential is relentless, which is why barrier width dominates almost every tunneling estimate you will ever make.

---

## Why There Is No Energy Debt

The popular account of tunneling goes like this: "The particle borrows energy from the vacuum — the time-energy uncertainty principle allows it — sprints across the barrier before the loan is recalled, and repays it on the far side." This story is wrong, and it is worth being exact about how.

The uncertainty relation $\Delta E\,\Delta t \geq \hbar/2$ does not license borrowing energy for a time $\Delta t$. That is simply not what it says. Energy is conserved at every instant inside the barrier; the total energy is $E$ in region I, inside the barrier, and in region III alike. The barrier wave function $Ce^{\kappa x} + De^{-\kappa x}$ is a perfectly legitimate solution of the time-independent Schrödinger equation for a particle of energy $E$ where $V = V_0 > E$. It is real and decaying rather than oscillatory, but it is the right solution. No negative kinetic energy, no overdraft, no repayment schedule.

What actually happens is plainer and stranger than the loan: the wave equation requires nonzero amplitude in the classically forbidden region, and when the barrier is finite that amplitude reaches the far edge and launches a transmitted wave. The transmitted amplitude is small because the decaying exponential has eaten away across the width $L$. That is the entire mechanism. The particle borrows nothing. It gets through because the mathematics of partial differential equations has no concept of "classically forbidden."

<!-- → [FIGURE: energy diagram for rectangular barrier — flat total energy E as horizontal line, barrier region V₀ above E, wave function shown below: oscillatory in regions I and III, decaying in region II, with annotation "E is constant throughout; only the character of the solution changes"] -->

![energy diagram for rectangular barrier — flat total energy E as horizontal line, barrier region V₀ above E, wave function shown below:…](../images/06-finite-wells-steps-and-barriers-fig-06.png)
*Figure 6.6 — energy diagram for rectangular barrier — flat total energy E as horizontal line, barrier region V₀ above E, wave function shown below:…*

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

**How long does tunneling take?** The formula for $T$ gives the probability of crossing, not the time spent inside the barrier. The literature offers several definitions of "tunneling time" — dwell time, phase time, Büttiker-Landauer time, Larmor clock time — and they disagree with one another. Attosecond-streaking experiments (Eckle et al., 2008; Sainadh et al., 2019) have measured *something*, but what the measured number means theoretically is still being argued. This chapter hands you $T$. It does not hand you a tunneling time. The framework is genuinely incomplete here.

**Does tunneling allow faster-than-light signaling?** The claim keeps resurfacing in popular accounts: a tunneled pulse can show a group velocity above $c$, so information must travel faster than light. What actually occurs is pulse reshaping. The barrier preferentially transmits the leading edge of the incident pulse — an edge that was already present before the barrier. The front of the pulse never exceeds $c$; the barrier simply favors its early part. No information moves faster than $c$.

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

---

## Running Project — Build the 1D Quantum Sandbox

**This chapter adds:** arbitrary potentials — the sandbox stops being hardwired to $V = 0$ and accepts any $V(x)$ array (finite well, step, rectangular barrier) into the same tridiagonal Hamiltonian — plus the transmission coefficient $T(E)$ and the tunneling check against the exact $T_\text{exact} = [1 + V_0^2\sinh^2(\kappa L)/4E(V_0-E)]^{-1}$.

### Exercise R1 — When to Use AI
**The judgment:** In this chapter's project work, AI assistance is appropriate for:
- Writing potential-builder functions `finiteWell`, `step`, `rectBarrier` that return a $V_j$ array on the grid — *Why AI works here:* these are piecewise-constant array fills, and the bound-state count or $T(E)$ curve checks them.
- Drafting the $T(E)$ plot with both $T_\text{exact}$ and $T_\text{WKB} = e^{-2\kappa L}$ on a log y-axis — *Why AI works here:* standard plotting, and the worked example ($V_0=5,L=5,E=1 \Rightarrow T\approx 9\times10^{-5}$) gives an exact anchor.
**The tell:** You are using AI well when you have an independent way to check the output — here, $R + T = 1$ at every energy, and the exact/WKB ratio equaling the analytic prefactor $16E(V_0-E)/V_0^2$.

### Exercise R2 — When NOT to Use AI
**The judgment:** These tasks require your judgment; AI output here can't be trusted without redoing the work:
- The sinh→sin switch when $E$ crosses $V_0$ — *Why AI fails here:* applying the $E<V_0$ formula above the barrier (or vice versa) gives a smooth, wrong $T(E)$ that still looks like a transmission curve; only your knowledge of which regime you are in catches it.
- Using probability current (with the $k$ ratio) rather than bare amplitude ratios for the step — *Why AI fails here:* $T = |C/A|^2$ omits the $k_1/k_0$ speed factor and silently breaks $R + T = 1$; the AI will not notice because each piece looks reasonable.
**The tell:** If you could not explain the result without the AI — if the AI is your *reason* rather than your *tool* — it did work that should have been yours.
**Physics-judgment connection:** This trains checking a scattering result against a conservation law ($R + T = 1$ from probability current) and against an exact closed form ($T_\text{exact}$), the discipline that catches regime-switch and amplitude-vs-current errors.

### Exercise R3 — LLM Exercise
**What you're building this chapter:** the arbitrary-$V(x)$ interface plus the transmission and tunneling calculators.
**Tool:** Claude chat — built on `hamiltonian.js` from Chapter 5; self-contained per scenario.
**The Prompt:**
```
Using the Chapter 0 CLAUDE.md, constants.js, grid.js, observables.js, and the
hamiltonian.js from Chapter 5 as binding context, build 06-barrier-explorer.html
with three tabs.

(1) FINITE WELL: a potentials.js helper finiteWell(x, L, V0) returns V_j
    (−V0 inside |x|<L/2, 0 outside). Feed V into hamiltonian.js's
    buildTridiagonal, diagonalize, and count/plot the bound states (E < 0).
    Confirm the bound-state count matches the graphical condition
    N ≈ ceil(z_0/(π/2)), z_0 = (L/2ℏ)√(2mV_0).

(2) STEP: plot R(E) and T(E) for V = V0·θ(x). For E > V0,
    k_0 = √(2mE)/ℏ, k_1 = √(2m(E−V0))/ℏ,
    R = ((k_0−k_1)/(k_0+k_1))², T = 4k_0k_1/(k_0+k_1)².
    Use PROBABILITY CURRENT (the k ratio), not |amplitude|². Log "R+T" to the
    console at every E — it must equal 1.

(3) BARRIER: plot T_exact and T_WKB on a LOG y-axis vs E/V0.
    For E < V0: κ = √(2m(V0−E))/ℏ,
      T_exact = 1/(1 + V0² sinh²(κL)/(4E(V0−E))),  T_WKB = exp(−2κL).
    For E > V0: switch sinh(κL) → sin(k_2 L), κ → ik_2, k_2 = √(2m(E−V0))/ℏ.
    BOX the two regimes separately; never apply the E<V0 formula when E>V0.

VERIFY: V0=5 eV, L=5 Å, E=1 eV → T_exact ≈ 9×10⁻⁵, T_WKB ≈ 3.5×10⁻⁵,
ratio ≈ 2.56 = 16E(V0−E)/V0². Report it.
```
**What this produces:** `potentials.js` (well/step/barrier builders, reused later) and `06-barrier-explorer.html` with bound-state, step, and tunneling tabs.
**How to adapt:** *Your system:* any new $V(x)$ you write plugs into the same `buildTridiagonal`. *ChatGPT/Gemini:* paste `hamiltonian.js`. *Claude Project:* add `potentials.js` to Project knowledge.
**Builds on:** the tridiagonal Hamiltonian from Chapter 5.  **Next:** Chapter 7 feeds the same builder the quadratic oscillator potential and validates $E_n = (n+\tfrac12)\hbar\omega$.

### Exercise R4 — CLI Exercise
**What you're building this chapter:** the tunneling calculator with automated $R+T=1$ and exact-vs-WKB checks.
**Tool:** Claude Code — it can sweep energies, assert conservation, and record the worked-example values in `PROJECT.md`.
**Skill level:** Intermediate
**Setup — confirm:**
- [ ] `hamiltonian.js`, `potentials.js`, `constants.js`
- [ ] Node.js available
- [ ] The CLAUDE.md rule boxing the $E<V_0$ and $E>V_0$ formulas separately
**The Task:**
```
Read potentials.js. Write a Node script check-scattering.js that:
  (1) for the STEP at V0 = 2 eV, sweeps E from 2.1 to 20 eV and asserts
      R + T = 1 within 1e-9 at every E (probability-current form);
  (2) for the BARRIER V0 = 5 eV, L = 5 Å, E = 1 eV, asserts
      T_exact ≈ 9×10⁻⁵, T_WKB ≈ 3.5×10⁻⁵, and ratio ≈ 2.56 = 16E(V0−E)/V0²;
  (3) confirms the sinh→sin switch: at E = V0 exactly, T_exact → 1 (limit κ→0).
Do NOT loosen tolerances. Append to PROJECT.md under "Verified":
"Ch6 scattering: R+T=1 ✓, barrier T_exact/T_WKB ratio = <v>".
```
**Expected output:** `check-scattering.js`, printed confirmations of $R+T=1$ and the ratio, and a `PROJECT.md` line.
**What to inspect:** that $R+T=1$ holds to machine precision (a current-vs-amplitude error breaks it at the 1% level) and that the exact/WKB ratio equals the analytic prefactor 2.56 exactly.
**If it goes wrong:** if $R+T \neq 1$ for the step, $T$ used $|C/A|^2$ without the $k_1/k_0$ factor — restore the current form. If $T(E)$ is discontinuous at $E = V_0$, the sinh→sin switch is missing or mis-placed.
**CLAUDE.md / AGENTS.md note:** add: "Every scattering computation logs $R+T$; deviation from 1 by more than 1e-6 is a current-accounting bug, not numerics."

### Exercise R5 — AI Validation Exercise
**What you're validating:** the arbitrary-$V(x)$ scattering and tunneling code from R3/R4.
**Validation type:** Numerical result
**Risk level:** Medium — regime-switch errors are silent and the tunneling exponential makes magnitudes hard to eyeball.
**Setup:** use your own R3/R4 artifacts.
**The Validation Task:** Evaluate against this checklist; mark Pass / Fail / Cannot determine with reasoning.
```
Validation Checklist — Arbitrary V(x), transmission, and tunneling
□ Correctness: does V(x) feed unchanged into buildTridiagonal (same eigensolver)?
□ Completeness: are both T_exact and T_WKB shown, on a log y-axis?
□ Scope: did the step use probability current (k ratio), not bare |amplitude|²?
□ Physics criterion 1: R + T = 1 to < 1e-6 at every energy?
□ Physics criterion 2: barrier (V0=5,L=5Å,E=1) gives T_exact≈9e-5, ratio 2.56?
□ Failure-mode check: any of —
  - E<V0 formula applied when E>V0 (sinh→sin switch missing)
  - T = |F/A|² without the k ratio (R+T ≠ 1 for the step)
  - linear T(E) axis hiding the exponential suppression
  - finite well claiming infinitely many bound states (should be finite, ≈ z_0/(π/2))
```
**What to do with findings:** pass → use it; one fail → fix the regime switch or restore the current form and re-run the $R+T$ sweep; multiple fails / cannot-determine → recompute $T$ at one energy by hand from the matching conditions.
**AI Use Disclosure (mandatory, two sentences):**
> *1:* The AI wrote the potential builders and the step/barrier transmission and tunneling calculators.
> *2:* The AI could not determine whether the sinh→sin regime switch and the probability-current accounting were correct — I verified $R+T=1$ and the exact-vs-WKB ratio against the closed forms myself.
**Physics-judgment connection:** trains checking a scattering result against a conservation law and an exact analytic formula, catching regime-switch and current-accounting errors a plausible curve would hide.
