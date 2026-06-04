# Chapter 6 — Finite Wells, Steps, and Barriers

## TL;DR

- Removing the infinite walls lets the wave function leak out — and creates a finite, countable set of bound states.
- A particle with *more* than enough energy to clear a step is still partially reflected; the wave cannot not interfere with itself.
- A particle with *less* than enough energy to cross a barrier crosses anyway, with probability $T = [1 + V_0^2\sinh^2(\kappa L)/(4E(V_0-E))]^{-1}$. This is tunneling.
- The +1 simulation shows all three phenomena live: drag a slider and watch transmission switch from "essentially zero" to "essentially one" as you cross the barrier top.

---

## Learning Objectives

By the end of this chapter you will be able to:

1. **Apply** the transcendental matching conditions for the finite square well to find bound-state energies graphically and numerically. *(Apply — Bloom level 3)*
2. **Derive** the reflection and transmission coefficients $R$ and $T$ for a potential step at both $E < V_0$ and $E > V_0$, and verify $R + T = 1$ from probability current conservation. *(Analyze — Bloom level 4)*
3. **Compute** the exact transmission coefficient $T_\text{exact}$ for a rectangular barrier, evaluate it numerically for given parameters, and compare it to the WKB approximation. *(Apply — Bloom level 3)*
4. **Explain** why tunneling does not violate energy conservation, and why classically forbidden does not mean quantum-mechanically forbidden. *(Understand — Bloom level 2)*
5. **Construct** an interactive simulation that plots $T(E)$ and the wave function profile in real time, varying barrier height and width. *(Create — Bloom level 6)*

---

## Scene

It is 1926 and Friedrich Hund is working on diatomic molecules. He has just been handed the Schrödinger equation, and he notices something uncomfortable. A nitrogen molecule, $\mathrm{N_2}$, consists of two nitrogen atoms held together by a covalent bond. Classically, for the molecule to come apart you would need to supply enough energy to get over the binding-energy barrier — roughly 9.8 eV. Room-temperature molecules have roughly 0.025 eV of thermal kinetic energy. The classical prediction is that $\mathrm{N_2}$ is stable at room temperature, which is correct.

But Hund notices that the wave function does not vanish at the edge of the classically allowed region. It decays into the forbidden zone and reaches the other side with non-zero amplitude. The molecule could, in principle, dissociate without ever acquiring the activation energy. The barrier is not a wall. It is a region of exponential suppression — wide enough in this case to make the dissociation rate negligibly small, but not zero.

Hund's observation in 1927 was the first explicit recognition that quantum tunneling changes the rules. Two years later, George Gamow used the same mathematics to explain alpha decay — a puzzle that had stumped nuclear physicists for a decade. A nucleus sits inside a Coulomb barrier roughly 30 MeV high; the emitted alpha particle has only 4–8 MeV. Classically, it is stuck. Quantum-mechanically, it leaks out, and the leaking rate depends so sensitively on barrier height and particle energy that a factor of two in energy produces 24 orders of magnitude in halflife.

The chapter that sets all of this up is this one.

---

## Core Development

### The Finite Square Well

Recall the infinite square well from Chapter 5: $V = 0$ for $|x| < L/2$ and $V = \infty$ outside. The infinite walls force $\psi$ to vanish at $\pm L/2$, producing an infinite tower of bound states with energies $E_n = n^2\pi^2\hbar^2/(2mL^2)$.

Now lower those walls to a finite height. Set $V = -V_0$ for $|x| < L/2$ and $V = 0$ outside, with $V_0 > 0$. (The sign convention: we choose the zero of energy at the top of the well so that bound states have negative energy $E < 0$.) Equivalently, you may think of $V = 0$ inside and $V = +V_0$ outside — the physics is the same, only the energy reference shifts; what matters is the depth $V_0$.

**Inside the well** ($|x| < L/2$): the Schrödinger equation reads $-(\hbar^2/2m)\psi'' = (E + V_0)\psi$, which for a bound state with $-V_0 < E < 0$ gives oscillatory solutions:

$$\psi_\text{in}(x) = A\cos(kx) + B\sin(kx), \quad k = \frac{\sqrt{2m(E+V_0)}}{\hbar}.$$

**Outside the well** ($|x| > L/2$): the Schrödinger equation gives $-(\hbar^2/2m)\psi'' = E\psi$. With $E < 0$, this is $\psi'' = \kappa^2\psi$ where

$$\kappa = \frac{\sqrt{-2mE}}{\hbar} = \frac{\sqrt{2m|E|}}{\hbar},$$

and the normalizable solutions are decaying exponentials: $\psi_\text{out} = Ce^{-\kappa|x|}$ on the left, and on the right.

Here is the first important difference from the infinite well: the wave function does not vanish at $x = \pm L/2$. It transitions smoothly from oscillatory to exponentially decaying. Continuity of $\psi$ and $\psi'$ at both walls yields the **transcendental matching conditions**.

By the symmetry of the potential, solutions split into **even-parity** (cosine inside) and **odd-parity** (sine inside) states.

For even-parity states, matching $\psi$ and $\psi'$ at $x = L/2$ gives:

$$\kappa = k\tan\!\left(\frac{kL}{2}\right). \tag{even}$$

For odd-parity states:

$$\kappa = -k\cot\!\left(\frac{kL}{2}\right). \tag{odd}$$

These cannot be solved analytically. But you can solve them graphically: plot $\kappa$ as a function of the energy $E$ (remembering that both $k$ and $\kappa$ are functions of $E$) and find the intersections. Each intersection is one bound state.

A useful dimensionless rewriting: let $z = kL/2$ and $z_0 = (L/2\hbar)\sqrt{2mV_0}$. Then $\kappa L/2 = \sqrt{z_0^2 - z^2}$, and the even condition becomes:

$$\sqrt{z_0^2 - z^2} = z\tan z.$$

The left side is a quarter-circle of radius $z_0$; the right side is a sequence of tangent curves. Each crossing of the quarter-circle with a tangent branch is one bound state. The number of even-parity crossings is $\lceil z_0/\pi \rceil$ — and similarly for odd. The total number of bound states is finite.

**Key result**: the finite square well always has **at least one bound state**, but it has **at most** $N$ bound states where $N \approx (L/\pi\hbar)\sqrt{2mV_0}$, rounded up. As $V_0 \to \infty$, the energy levels recover the infinite-well values. As $V_0 \to 0$, all levels but the ground state disappear.

**The penetration depth**: just outside the well, $\psi \propto e^{-\kappa|x|}$. The characteristic length $1/\kappa = \hbar/\sqrt{2m|E|}$ is called the penetration depth. A loosely-bound state ($|E|$ small) has a large penetration depth — the wave function leaks far beyond the classical turning points. This is not a wave function misbehaving. It is a wave function doing exactly what the Schrödinger equation requires.

---

### The Potential Step

Now study scattering rather than bound states. Let the potential be a step: $V = 0$ for $x < 0$ and $V = V_0$ for $x > 0$. A particle is incident from the left.

**Probability current** enters here as the right tool. From Chapter 1, recall:

$$J(x,t) = \frac{\hbar}{m}\,\mathrm{Im}\!\left(\psi^*\frac{\partial\psi}{\partial x}\right).$$

For a plane wave $\psi = Ae^{ikx}$, the current is $J = \hbar k|A|^2/m$. This is the rate at which probability flows past a point. The **transmission coefficient** $T$ is the ratio of transmitted current to incident current, and the **reflection coefficient** $R = |J_\text{reflected}|/J_\text{incident}$. Conservation of probability requires $R + T = 1$.

**Case 1: $E > V_0$** (particle has enough energy to clear the step classically).

In region I ($x < 0$): $\psi_I = Ae^{ik_0 x} + Be^{-ik_0 x}$, where the first term is the incident wave and the second is the reflected wave. The wave number is $k_0 = \sqrt{2mE}/\hbar$.

In region II ($x > 0$): only a rightward-moving wave, $\psi_{II} = Ce^{ik_1 x}$, with $k_1 = \sqrt{2m(E-V_0)}/\hbar$.

Continuity of $\psi$ and $\psi'$ at $x = 0$:

$$A + B = C, \quad k_0(A - B) = k_1 C.$$

Solve: $B/A = (k_0 - k_1)/(k_0 + k_1)$ and $C/A = 2k_0/(k_0 + k_1)$.

Now compute $R$ and $T$ using probability currents. The incident current is $J_\text{inc} = \hbar k_0|A|^2/m$; the reflected current is $\hbar k_0|B|^2/m$; the transmitted current is $\hbar k_1|C|^2/m$. (Notice the $k_1$ in the transmitted current — this matters because the particle moves at a different speed on the far side.)

$$\boxed{R = \left(\frac{k_0 - k_1}{k_0 + k_1}\right)^2, \qquad T = \frac{4k_0 k_1}{(k_0 + k_1)^2}.}$$

Verify $R + T = 1$: $(k_0 - k_1)^2 + 4k_0 k_1 = (k_0 + k_1)^2$. Check. $\checkmark$

The quantum surprise is this: $R \neq 0$ even when $E > V_0$. Classically, a particle with enough energy always transmits. Quantum-mechanically, the abrupt change in $k$ at $x = 0$ acts like an impedance mismatch in a transmission line — any discontinuity in the medium reflects some of the wave. The reflection vanishes only if $k_0 = k_1$, i.e., $V_0 = 0$. Even a downward step ($V_0 < 0$) produces partial reflection, because what matters is not the sign of $V_0$ but the size of $|k_0 - k_1|/(k_0 + k_1)$.

**Case 2: $E < V_0$** (particle does not have enough energy classically).

In region II, $k_1 = \sqrt{2m(E - V_0)}/\hbar$ is imaginary. Define $\kappa = \sqrt{2m(V_0 - E)}/\hbar$ (real and positive). The solution in region II must remain bounded as $x \to \infty$, so $\psi_{II} = Ce^{-\kappa x}$ — a decaying exponential. Matching gives $B/A = (k_0 - i\kappa)/(k_0 + i\kappa)$, and $|B/A|^2 = 1$. So $R = 1$ and $T = 0$.

The particle is totally reflected. But the wave function in region II is not zero. There is an **evanescent tail** penetrating into the classically forbidden region with characteristic length $1/\kappa$. Probability density is present there — but no net probability current flows (the current in the decaying exponential is zero). The probability sloshes in and out of the barrier without any net transmission.

---

### The Rectangular Barrier and Tunneling

Now make the step finite in width. Let $V = V_0 > 0$ for $0 < x < L$ and $V = 0$ elsewhere. A particle is incident from the left with energy $E < V_0$. Classically: reflection is total, no transmission. Quantum-mechanically: transmission is not zero.

Divide space into three regions:

- Region I ($x < 0$): $\psi_I = Ae^{ikx} + Be^{-ikx}$, $k = \sqrt{2mE}/\hbar$.
- Region II ($0 < x < L$): $\psi_{II} = Ce^{\kappa x} + De^{-\kappa x}$, $\kappa = \sqrt{2m(V_0 - E)}/\hbar$.
- Region III ($x > L$): $\psi_{III} = Fe^{ikx}$ (no reflected wave in III).

Apply continuity of $\psi$ and $\psi'$ at $x = 0$ and $x = L$. Four equations, four unknowns ($B, C, D, F$ in terms of $A$). The algebra is straightforward but tedious; the result is:

$$\boxed{T_\text{exact} = \left[1 + \frac{V_0^2\sinh^2(\kappa L)}{4E(V_0 - E)}\right]^{-1}} \tag{6.1}$$

where $\sinh(\kappa L) = (e^{\kappa L} - e^{-\kappa L})/2$ is the hyperbolic sine.

This is the **exact** transmission coefficient for the rectangular barrier at $E < V_0$. Nothing is approximate. The formula encodes everything: the dependence on barrier height $V_0$, barrier width $L$, and particle energy $E$.

**The thick-barrier limit** ($\kappa L \gg 1$): $\sinh(\kappa L) \approx e^{\kappa L}/2$, so $\sinh^2(\kappa L) \approx e^{2\kappa L}/4$. The denominator is dominated by the exponential term:

$$T_\text{exact} \approx \frac{16E(V_0 - E)}{V_0^2}\,e^{-2\kappa L}.$$

The WKB approximation (Chapter 11) gives $T_\text{WKB} = e^{-2\kappa L}$. The ratio $T_\text{exact}/T_\text{WKB} = 16E(V_0 - E)/V_0^2$ is a smooth prefactor of order unity for $E$ well below $V_0$. WKB nails the exponential suppression; it misses only the prefactor.

**For $E > V_0$** (above-barrier scattering), $\kappa$ becomes imaginary. Let $k_2 = \sqrt{2m(E - V_0)}/\hbar$; then $\kappa = ik_2$ and $\sinh(i\theta) = i\sin\theta$. The formula becomes:

$$T_\text{exact} = \left[1 + \frac{V_0^2\sin^2(k_2 L)}{4E(E - V_0)}\right]^{-1}. \tag{6.2}$$

Notice: $T = 1$ when $\sin(k_2 L) = 0$, i.e., when $k_2 L = n\pi$ for integer $n$. These are **resonances** — the barrier is transparent when its width equals an integer number of half-wavelengths inside the barrier. The wave function inside the barrier constructively "fits" the barrier exactly. This is the quantum analogue of an anti-reflection coating in optics.

---

### Why Tunneling Does Not Violate Energy Conservation

This deserves a careful paragraph, because the pop-science version of tunneling is wrong.

The pop-science version says: "The particle borrows energy from the vacuum, allowed by the time-energy uncertainty principle, and pays it back before anyone notices." This is not what happens. The uncertainty relation $\Delta E\,\Delta t \geq \hbar/2$ does not mean energy can be borrowed for a time $\Delta t$. Energy is not borrowed. Energy is conserved at every step.

What actually happens: inside the barrier, $\psi_{II} = Ce^{\kappa x} + De^{-\kappa x}$ is a perfectly valid solution to the Schrödinger equation for a particle with total energy $E$ in a region where the potential is $V_0$. The wave function is real and decaying — not oscillatory, but real. The particle does not have negative kinetic energy inside the barrier (that phrase is not meaningful); rather, the Schrödinger equation simply has a different character in this region. The total energy of the particle is $E$ everywhere. The wave function decays because that is what solutions to $\psi'' = \kappa^2\psi$ do, and that equation comes directly from the TISE with $E < V_0$.

The transmitted amplitude is small because the decaying exponential has attenuated from one side of the barrier to the other. The particle "passes through the barrier" in the same sense that an evanescent electromagnetic wave in total internal reflection leaks into the lower-index medium: not by borrowing energy, but by the wave equation requiring non-zero amplitude there.

---

## Worked Example: Transmission Through a Barrier

**The lesson.** An electron ($m_e = 9.109 \times 10^{-31}$ kg) with kinetic energy $E = 1$ eV encounters a rectangular barrier of height $V_0 = 5$ eV and width $L = 5$ Å $= 5 \times 10^{-10}$ m. Compute $T_\text{exact}$ and $T_\text{WKB}$ and compare.

**Step 1: Compute $\kappa$.**

$$\kappa = \frac{\sqrt{2m_e(V_0 - E)}}{\hbar} = \frac{\sqrt{2 \times 9.109 \times 10^{-31} \times 4 \times 1.602 \times 10^{-19}}}{1.055 \times 10^{-34}} \approx 1.025 \times 10^{10}\ \text{m}^{-1}.$$

In convenient units: $\kappa \approx 1.025\ \text{Å}^{-1}$.

**Step 2: Compute $\kappa L$.**

$$\kappa L = 1.025\ \text{Å}^{-1} \times 5\ \text{Å} = 5.125.$$

Since $\kappa L \gg 1$, the thick-barrier approximation is reasonable.

**Step 3: Compute $\sinh(\kappa L)$.**

$$\sinh(5.125) = \frac{e^{5.125} - e^{-5.125}}{2} \approx \frac{168.2 - 0.00595}{2} \approx 84.1.$$

**Step 4: Compute $T_\text{exact}$.**

$$T_\text{exact} = \left[1 + \frac{(5)^2 \times (84.1)^2}{4 \times 1 \times (5-1)}\right]^{-1} = \left[1 + \frac{25 \times 7073}{16}\right]^{-1} = \left[1 + 11052\right]^{-1} \approx 9.05 \times 10^{-5}.$$

**Step 5: Compute $T_\text{WKB}$.**

$$T_\text{WKB} = e^{-2\kappa L} = e^{-10.25} \approx 3.54 \times 10^{-5}.$$

**Step 6: Compare.**

$$\frac{T_\text{exact}}{T_\text{WKB}} \approx \frac{9.05 \times 10^{-5}}{3.54 \times 10^{-5}} \approx 2.56.$$

The analytical prefactor: $16E(V_0 - E)/V_0^2 = 16 \times 1 \times 4/25 = 2.56$. The WKB prediction of the ratio is exact here. $\checkmark$

**The limit.** This calculation has a physical punchline. The transmission is roughly $10^{-4}$ — tiny, but not zero. If this were a 10 Å barrier instead of 5 Å, $\kappa L$ would double to 10.25, and $T_\text{WKB}$ would drop to $e^{-20.5} \approx 1.25 \times 10^{-9}$ — four orders of magnitude smaller. Exponential suppression means that barrier width controls $T$ more powerfully than almost anything else. An STM exploits exactly this: one extra ångström of gap changes the tunneling current by a factor of $e^2 \approx 7$. That exponential transduction makes sub-ångström topographic imaging possible.

---

## Common Misconceptions

**"The finite well has infinitely many bound states, like the infinite well."** No. The number is finite: $N \approx (L/\pi\hbar)\sqrt{2mV_0}$, rounded up. The difference is that in the infinite well, arbitrarily high energy levels fit because the walls are impenetrable. In the finite well, a level too close to the top of the well has a wave function that barely decays outside — it requires effectively infinite spatial extent to be normalized, which is only possible below the potential energy of the continuum. Above $V = 0$, the states are scattering states, not bound states. A well that is too shallow or narrow for a second level will have exactly one bound state and no others.

**"A particle with $E > V_0$ always transmits perfectly at a step."** No. $R = (k_0 - k_1)^2/(k_0 + k_1)^2 \neq 0$ whenever $k_0 \neq k_1$, which requires $V_0 \neq 0$. Partial reflection is a wave phenomenon arising from impedance mismatch, not an energy phenomenon. Even a step downward (attractive step) partially reflects. This surprises students because the word "barrier" suggests energy. But it is about wave mechanics, not energy.

**"Tunneling means the particle has negative kinetic energy inside the barrier."** Kinetic energy is not a well-defined observable in the sense of "a value the particle has." Inside the barrier, $\psi$ is real and decaying; the total energy is $E$; the potential energy is $V_0 > E$. If you insisted on defining kinetic energy as $E - V_0$, you would get a negative number — but this is not physically meaningful because you cannot measure the kinetic energy of a particle inside the barrier without perturbing it enough to collapse the wave function. The correct statement is: the wave function in the classically forbidden region is an exponentially decaying solution to the TISE for a particle of energy $E$. Nothing more.

**"$T = |F/A|^2$ for the barrier."** Wrong by a factor of $k_0/k_0 = 1$ here (since the wave number is the same on both sides of the barrier), but the mistake propagates dangerously in the step problem, where $T \neq |C/A|^2$. The correct formula uses probability current: $T = J_\text{trans}/J_\text{inc} = (k_\text{trans}/k_\text{inc})|C/A|^2$ for a step, or $(k_\text{III}/k_\text{I})|F/A|^2$ for a barrier where the wave numbers on both sides differ. For the rectangular barrier with equal free-space wave numbers on both sides, $T = |F/A|^2$ is accidentally correct — but the justification must go through probability current, not amplitude alone.

---

## Exercises

**Warm-up**

1. *[Tests: transcendental matching, graphical solution]* A particle of mass $m$ is in a finite square well of width $L$ and depth $V_0$. Define $z = kL/2$ and $z_0 = (L/2\hbar)\sqrt{2mV_0}$. (a) Show that the even-parity matching condition can be written $\sqrt{z_0^2 - z^2} = z\tan z$. (b) Sketch both sides as functions of $z$ for $z_0 = 3\pi/2$. How many even-parity bound states exist? (c) How many total bound states (even + odd) are there for this $z_0$? *Difficulty: warm-up.*

2. *[Tests: R + T = 1 from probability current]* For the potential step at $E > V_0$, the transmission coefficient is $T = 4k_0 k_1/(k_0 + k_1)^2$. (a) Compute $R + T$ algebraically and verify it equals 1. (b) Why is $T \neq |C/A|^2$ for the step? Write one sentence connecting the answer to probability current. (c) Compute $R$ when $E = 2V_0$. Is it closer to 0 or 1? *Difficulty: warm-up.*

3. *[Tests: evanescent decay, penetration depth]* A particle with $E = 2$ eV hits a step with $V_0 = 5$ eV. (a) Compute the penetration depth $1/\kappa$ in nm, taking $m = m_e$. (b) By what factor does the probability density at $x = 1/\kappa$ differ from its value at the step ($x = 0$)? (c) By what factor does the probability density differ at $x = 2/\kappa$? What does this tell you about how rapidly the evanescent tail decays? *Difficulty: warm-up.*

**Application**

4. *[Tests: exact barrier transmission formula, numerical evaluation]* An electron ($m_e = 9.109 \times 10^{-31}$ kg) with $E = 3$ eV encounters a rectangular barrier with $V_0 = 6$ eV and $L = 3$ Å. (a) Compute $\kappa$ in Å$^{-1}$. (b) Compute $T_\text{exact}$ using equation (6.1). (c) Compute $T_\text{WKB} = e^{-2\kappa L}$. (d) Find the ratio $T_\text{exact}/T_\text{WKB}$ and compare to $16E(V_0 - E)/V_0^2$. *Difficulty: application.*

5. *[Tests: resonance condition, above-barrier transmission]* For the rectangular barrier at $E > V_0$, resonances (perfect transmission, $T = 1$) occur when $k_2 L = n\pi$ where $k_2 = \sqrt{2m(E - V_0)}/\hbar$. (a) For an electron, $V_0 = 2$ eV, $L = 1$ nm, find the two lowest energies above $V_0$ at which $T = 1$. (b) Between resonances, $T < 1$. What is the minimum value of $T$ for $E$ between the first and second resonances? (Hint: the minimum occurs when $\sin^2(k_2 L) = 1$.) *Difficulty: application.*

6. *[Tests: STM physics, exponential sensitivity]* A scanning tunneling microscope tip is held $d = 4$ Å above a platinum surface. The effective barrier height (work function of Pt) is $\phi \approx 5.7$ eV. (a) Compute $\kappa = \sqrt{2m_e\phi}/\hbar$ in Å$^{-1}$. (b) Compute the ratio of tunneling currents when the tip moves from $d = 4$ Å to $d = 5$ Å. (c) A surface step is 2 Å high. By what factor does the current change when the tip passes over it? (d) Explain in one sentence why this exponential sensitivity enables atomic-resolution imaging. *Difficulty: application.*

**Synthesis**

7. *[Tests: connecting finite well to nuclear physics]* The deuteron — a proton and neutron bound by the nuclear force — can be modeled as a finite square well of depth $V_0 \approx 35$ MeV and width $L \approx 2.1$ fm ($1\ \text{fm} = 10^{-15}$ m), with reduced mass $\mu \approx m_p/2 \approx 938/2$ MeV/$c^2$. (a) Compute $z_0 = (L/2\hbar c)\sqrt{2\mu c^2 V_0}$ (using $\hbar c \approx 197$ MeV·fm). (b) How many even-parity bound states does this well support? (c) The deuteron has only one bound state (the ground state). Is this consistent with your calculation? What does this say about deuteron excited states? *Difficulty: synthesis.*

8. *[Tests: probability current conservation as a physical constraint]* Suppose someone proposes a wave function in region II of the step (with $E < V_0$) of the form $\psi_{II} = Ce^{\kappa x}$ only (growing exponential, no decaying piece). (a) Compute the probability current $J_{II}$ for this wave function. (b) Is $R + T = 1$ satisfied? (c) Why is this solution physically inadmissible, and how does the boundary condition at $x \to \infty$ rule it out? *Difficulty: synthesis.*

---

## Still Puzzling

How long does tunneling take? The transmission coefficient $T$ gives the probability of crossing, but not the time spent inside the barrier. Several definitions of "tunneling time" appear in the literature — the dwell time, the phase time, the Büttiker-Landauer time, the Larmor clock time — and they give different answers. Recent attosecond-streaking experiments (Eckle et al., *Science* 2008; Satya Sainadh et al., *Nature* 2019) measure something, but the theoretical interpretation remains contested. This chapter gives you $T$ but not a tunneling time. The framework is incomplete here.

The pop-science claim that tunneling allows faster-than-light signaling (because the group velocity of a tunneled pulse can apparently exceed $c$) is not correct. What happens is pulse reshaping: the barrier selects and amplifies the leading edge of the incident pulse, which was already there before the barrier. No information travels faster than $c$. But the claim recurs in the popular press with enough regularity that knowing the refutation matters.

---

## The +1 — Simulation Exercise

### The deliverable

`06-barrier-explorer.html` — a single self-contained HTML file with three tabs: **Bound States** (graphical solution for the finite well), **Step** (R and T vs. E for a potential step), and **Barrier** ($T_\text{exact}$ and $T_\text{WKB}$ vs. E, plus an animated wave packet on a rectangular barrier).

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

**Task 1 — Counting bound states.** In the Finite Well tab, set $V_0 = 4$ and $L = 5$. Count the intersections on the graphical solution. Now reduce $V_0$ until one level disappears. At what $V_0$ does the second bound state vanish? Record the value of $z_0$ at that point. Compare to the threshold condition $z_0 = \pi/2$ (first odd-parity state just appears when $z_0 = \pi/2$).

**Task 2 — Reflection at the step.** In the Step tab, observe that $R \to 1$ as $E \to V_0$ from above. At $E = 2V_0$, read off $R$. At $E = 10V_0$, read off $R$. Does $R$ approach zero? Explain physically why a very-high-energy particle still reflects slightly.

**Task 3 — Exponential sensitivity.** In the Barrier tab, set $V_0 = 5, E = 1$ (so $E/V_0 = 0.2$). Read off $T_\text{exact}$. Now double $L$. By what factor does $T$ change? Double $L$ again. Now vary $V_0$ at fixed $L$ and $E$. Which parameter (height or width) gives you more control over $T$?

**Task 4 — The resonance peaks.** Set $E > V_0$ in the Barrier tab. Find the first resonance (first energy above $V_0$ where $T = 1$). Verify that the barrier width is exactly half a de Broglie wavelength: $L = \pi/k_2 = \pi\hbar/\sqrt{2m(E - V_0)}$ (in natural units, $L = \pi/k_2$).

**Task 5 — The wave packet.** Play the Crank-Nicolson animation with $V_0 = 5, L = 3, E = 1$. Pause just as the wave packet reaches the barrier. Describe what you see in the barrier region. After the packet has fully passed, observe the relative size of the transmitted and reflected pulses. Use the T value from Panel A to predict the ratio $|\psi_\text{trans}|^2_\text{max}/|\psi_\text{inc}|^2_\text{max}$ and check it against the simulation.

---

## References

- Griffiths, D. J., *Introduction to Quantum Mechanics*, 3rd ed., §2.5–2.6 (finite well), §2.7 (scattering, step, barrier). Canonical undergraduate source; formulae in this chapter verified against this text. `[verify]`
- Walet, N., *Quantum Mechanics* (University of Manchester lecture notes), §6.2–6.3. Open-access source for the step and barrier, with probability-current derivations explicit. https://phys.libretexts.org/Bookshelves/Quantum_Mechanics/Quantum_Mechanics_(Walet)/06:_Scattering_from_Potential_Steps_and_Square_Barriers/6.02:_Potential_step
- Wikipedia, "Rectangular potential barrier." Derivation section matches the result in this chapter; verified against _lib_qmsri-11. https://en.wikipedia.org/wiki/Rectangular_potential_barrier
- Gamow, G., "Zur Quantentheorie des Atomkernes," *Zeitschrift für Physik* **51**, 204 (1928). Original alpha-decay tunneling paper. `[verify — primary source; confirm journal volume/page]`
- Gurney, R. W. and Condon, E. U., "Wave Mechanics and Radioactive Disintegration," *Nature* **122**, 439 (1928); and *Physical Review* **33**, 127 (1929). Simultaneous independent derivation of tunneling-based alpha decay.
- Binnig, G. and Rohrer, H., "Scanning Tunneling Microscopy," *Physical Review Letters* **49**, 57 (1982). Nobel Prize 1986; foundational STM paper demonstrating the tunneling current formula in practice.
- Eckle, P. et al., "Attosecond Ionization and Tunneling Delay Time Measurements in Helium," *Science* **322**, 1525 (2008). Key experimental paper on tunneling time; cited in the "Still puzzling" section. `[verify]`
- Herman, R. L., "PHY 444 — Finite Square Well," UNCW lecture notes (Fall 2021). https://people.uncw.edu/hermanr/qm/Finite_Square_Well.pdf `[verify — confirm URL still active]`
- PhysicsLibreTexts, "3.4: Finite Square Well," UCD Physics 9HE. https://phys.libretexts.org/Courses/University_of_California_Davis/UCD:_Physics_9HE_-_Modern_Physics/03:_One-Dimensional_Potentials/3.4:_Finite_Square_Well
