# Chapter 0 — How to Use the Simulations

## TL;DR

Before you read a single line of physics, ask yourself: could you build a quantum simulation right now, today, with the tools on your laptop? Most readers assume the answer is "not yet — I need the theory first." It is the other way around. In this chapter you write three governing Markdown files (`CLAUDE.md`, `DESIGN.md`, `PROJECT.md`), paste a four-move prompt (Show / Say / Constrain / Verify) into Claude, and watch a free-particle Gaussian wave packet animate in your browser before any new physics arrives. This is toolchain installation, not theory: every later LLM Exercise inherits these files. The physics the packet is doing — dispersion, group velocity, spreading — gets its proper treatment in Chapters 1 and 2. Here it is bait.

---

## Learning Objectives

By the end of this chapter you will be able to:

1. **(Understand)** State in one sentence each what `CLAUDE.md`, `DESIGN.md`, and `PROJECT.md` do, and explain why they are three files rather than one.
2. **(Apply)** Use the four-move prompt structure (Show / Say / Constrain / Verify) to produce a working D3 simulation from Claude on the first or second try.
3. **(Apply)** Read the generated HTML and locate the lines that implement the physics (dispersion relation, time evolution, normalization indicator).
4. **(Analyze)** Distinguish group velocity from phase velocity visually and numerically in the wave-packet animation.
5. **(Evaluate)** Apply the three-check verification stack (format, physics, behavior) to any LLM-generated simulation and name what each check catches.

---

## The Problem Before the Physics

Here is an image you will meet many times in this book: a blue filled curve drifting to the right while orange ripples slip backward through it, and a number in the corner reading `1.000`. Before you read on, sit with a question. You do not yet know what any of it means — so why would I show it to you *first*, before the physics that explains it?

The reflexive answer is that I should not. Theory before picture, definitions before demonstrations — that is how textbooks are built, and most readers expect it. That instinct is almost right, and here is where it breaks. Quantum mechanics is unusually hard to learn from words alone, because its objects have no classical analogue. There is no everyday thing you can point to and say "it's like that." The standard textbook hands you symbols and asks you to trust them; it gives you nothing to hold, turn, or poke with a slider. So what is the missing ingredient? A third object, alongside the text and the mathematics: a simulation you built yourself, governed by physics you can derive, that responds when you change parameters. You see it before you understand it for the same reason you'd hand a child an instrument before teaching music theory — the puzzlement is the point.

So what problem does this chapter actually solve? Predict before reading: is it a physics problem or something else? It is not physics at all. It is logistics. Before you can use simulations to *learn* physics, you need a stable, repeatable way to *produce* them. The tool is Claude (or any capable LLM). The method is the four-move prompt. The stability comes from three Markdown files you write once and carry through the whole book. That is the apparatus we install today — and noticing that the hard part here is reproducibility, not quantum theory, is itself the first lesson.

By the time you close this chapter, you will have a file called `00-wave-packet.html` on your machine. Open it. Press play. Watch the blue blob drift. Watch the orange ripples slip backward through it. Stay in the mild confusion of watching something you cannot yet name. Chapter 1 will name it.

---

## The Brutalist System — Three Files, One Apparatus

Where does the word *Brutalist* come from, and why borrow it for code? Guess before reading. In architecture it names a style that exposes its structural materials rather than hiding them behind decoration — a Brutalist building shows you the concrete, the steel, the pipes. Now carry the metaphor across: what would it mean to expose the structure of a simulation rather than hide it? It means the rules governing the simulations live in plain Markdown files you can read, edit, and version-control. Nothing is buried in a tool you do not own. That is the whole commitment.

Three files do all the work.

### `CLAUDE.md` — The Coding Constitution

This is the file Claude reads before every coding prompt. It specifies: the runtime (a modern browser, no build step), the library (D3 v7 loaded from CDN), the drawing surface (SVG only — not Canvas, not WebGL), the parameter exposure convention (HTML `<input type="range">` sliders firing on `input`), the animation loop (`requestAnimationFrame`), the storage convention for complex wave functions (`{re, im}` objects or two parallel `Float64Array`s), the units convention (SI internally, physical units displayed), and the normalization indicator (every simulation prints $\int |\psi|^2\,dx$ and warns if it strays from 1 by more than 1%).

Three of these rules deserve scrutiny — and each is worth predicting before you read the answer.

**SVG, not Canvas.** Why would a physics book legislate the drawing technology? Ask yourself first: what is a one-dimensional wave function, geometrically? It is a curve. So is a probability density. So is a potential. SVG draws curves natively — one `<path>` element per curve, a vector representation that scales cleanly. Canvas, by contrast, forces you to manage a pixel buffer and reimplement axes from scratch. D3 v7 is built around SVG. So the choice is not aesthetic; it follows from what the objects *are*. The match is natural and the resulting code is readable.

**Functions, not classes.** Here is a tempting move: wrap the physics in a class, the way "good software engineering" seems to demand. Before you accept that, ask what the simulation core actually *is*. It is mostly a pure function from parameters to an array of values: `computeWavefunction(x, t, params)` returns a typed array. What does wrapping that in a class buy you? It hides the structure and creates lifecycle questions — when do you instantiate, when do you destroy? Plain functions sidestep all of it, and they are easier to read, modify, and debug.

**The normalization indicator.** Every simulation displays $\int |\psi|^2\,dx$ in a corner of the screen. What number should it read? It should read `1.000`. Now the real question: what does it mean if it drifts? Something is wrong — the LLM introduced a numerical error, or you pushed a parameter outside the physical range, or there is a bug. The indicator is the simulation's lie detector. Do not ship any simulation without it.

### `DESIGN.md` — The Visual Constitution

`DESIGN.md` governs what the simulation *looks like*: colors, fonts, axis labels, slider styling, colormap choices. Why split it off from `CLAUDE.md` at all — isn't it all just "the rules"? Consider how the two kinds of rule break. Visual decisions and behavioral decisions fail differently and independently. If you want to change the color palette, you edit `DESIGN.md` alone; the physics is untouched. The separation pays for itself the first time you change a color without fear of breaking the dynamics.

The color commitments this book makes, and why:

- $|\psi|^2$ in blue (filled): it is the panel you look at most. Blue reads well against both light and dark backgrounds.
- $\mathrm{Re}\,\psi$ in orange (solid line): it oscillates and goes negative; orange on a neutral background stays readable.
- $\mathrm{Im}\,\psi$ in gray dashed: same envelope, quarter-cycle phase shift; the dashed style encodes "secondary information."
- Potential $V(x)$ in red.
- Energy levels in green, horizontal.
- Classical turning points in purple, dashed vertical.

For two-dimensional density maps: **Viridis** for unsigned quantities (it is monotonic in luminance — readable in grayscale, readable for color-blind readers). **RdBu** for signed amplitudes (red positive, blue negative, centered on zero). Never rainbow/jet: those palettes lie about the data by creating perceptual jumps at arbitrary values. The research on this is unambiguous (Kovesi 2015; Borland & Taylor 2007).

### `PROJECT.md` — The Project State

`PROJECT.md` is the file Claude reads to remember the project. It is short — a few hundred words — and lists: which chapter you are working on, which simulations exist and have been verified, which parameter ranges were used, what is broken. Every time you finish a simulation, you add a line. Every time you fix a bug, you note it.

Students forget this file exists. Before I tell you why that matters, predict the failure: what goes wrong when you return to a Claude session three weeks later? Most people assume the model "remembers" the project. It does not. Claude has no persistent memory between sessions. When you come back to extend the Chapter 3 simulation, the model has forgotten every parameter, every convention, every verified fact. `PROJECT.md` *is* the memory. Without it, every extension prompt starts from scratch. With it, the extension prompt is five lines.

### Why Three Files, Not One

The natural objection: why not put everything in one `CLAUDE.md`? Write down your reason before reading mine.

The first answer is token economy. Picture Chapter 7: you ask for a simulation. Should that request force the model to re-read every slider-styling rule? It should not. The chapter-7 prompt loads `CLAUDE.md` (behavior) and `PROJECT.md` (state), and references `DESIGN.md` by name without quoting it. The visual rules are still in force; they are simply not burning context.

The second answer is debugging — and here is a question to test the split. When a simulation looks wrong, what is the first thing you should ask? Behavioral problem (wrong physics, wrong animation) or visual problem (wrong color, wrong layout)? The moment you can answer that, you know which file to open. The three-file split is for debugging as much as for token economy.

**The "bureaucracy" misconception.** You might suspect all this file-keeping is overhead — bureaucracy dressed up as discipline. Test the suspicion against the alternative: what happens *without* the files? You rediscover the same conventions every week and produce twelve visually incompatible simulations. The files make the rules explicit so you stop relitigating them. They are the opposite of bureaucracy; they are what lets you stop thinking about settled questions.

---

## The Four-Move Prompt — Show, Say, Constrain, Verify

What is a prompt to Claude, really — a wish, or a specification? Treat it as a wish and you will get wish-quality results. The four-move structure below is the one this book uses for every LLM Exercise. It is short, it is testable, and it is the reason most chapter simulations work on the first or second try.

**Show.** Paste the artifact. The equation — in LaTeX if needed, not a description of it. If you want the wave function $\psi(x, 0) = (1/(\pi a^2))^{1/4}\,e^{-x^2/(2a^2)}\,e^{ik_0 x}$, put that formula in the prompt. What happens if instead you write "a Gaussian wave packet" and hope? The model must guess what you meant, and the guess is often wrong. Vague descriptions are the number-one cause of bad LLM-generated code: LLMs hallucinate phase factors when not given the analytic expression. Show the artifact, not a gesture toward it.

**Say.** State the deliverable in one sentence with the audience and format: *"Produce a single HTML file I can open in Chrome with sliders for $\sigma$ and $k_0$ that animates $|\psi|^2$ in real time."* Why does naming the use case ("open in Chrome," "single file") matter so much? Because it fixes the shape of the output. Leave it out, and you may get a Python notebook — technically a wave packet, useless to you.

**Constrain.** Name the constraints. D3 v7 from CDN. Single file. No build step. SVG only. Normalization indicator visible. What do constraints do for the model? They shrink its search space and reduce hallucination. The `CLAUDE.md` constraints are already in force; the Constrain move names only the additional constraints specific to this simulation.

**Verify.** Here is the move most people skip — and the most important. Instead of asking Claude for the answer and trusting it, ask Claude what *you* should check: *"Tell me four things I should verify in the browser to confirm the physics is correct."* What does that one question change? It converts Claude from oracle to collaborator. You get back a rubric: *(a) centroid at $x=0$ at $t=0$; (b) centroid moves at $v_g$; (c) $\sigma(t)$ grows as predicted; (d) normalization stays at 1.000.* You apply it to the rendered output. If a check fails, you know what to fix. The Verify move is the chapter-zero habit. The verification stack is the immune response against LLM hallucination.

---

## The Physics You Need for the Simulation (Given Without Proof)

You will see this material derived in Chapters 1 and 2. Here we state the results and use them to build the simulation.

### The Gaussian Wave Packet at $t = 0$

$$\psi(x, 0) = \left(\frac{1}{\pi a^2}\right)^{1/4} \exp\!\left(-\frac{x^2}{2a^2}\right) \exp(i k_0 x).$$

Two ingredients. The Gaussian envelope $\exp(-x^2/(2a^2))$ localizes the particle around $x = 0$ with width parameter $a$. The plane-wave carrier $\exp(i k_0 x)$ gives the packet a central wavenumber $k_0$, corresponding to central momentum $p_0 = \hbar k_0$. The prefactor normalizes the wave function: $\int |\psi(x,0)|^2\,dx = 1$.

### Time Evolution — The Dispersion Relation

For a free particle ($V = 0$), each plane-wave component $e^{ikx}$ evolves with phase $e^{-i\omega(k)t}$, where the **dispersion relation** is

$$\omega(k) = \frac{\hbar k^2}{2m}.$$

This is quadratic in $k$. Because different wavenumbers evolve at different rates, the packet spreads. The closed-form result (Griffiths §2.4, Problem 2.21) is:

$$|\psi(x, t)|^2 = \frac{1}{\sqrt{2\pi}\,\sigma(t)} \exp\!\left(-\frac{(x - v_g t)^2}{2\sigma(t)^2}\right),$$

with

$$\sigma(t)^2 = \frac{a^2}{2} + \frac{\hbar^2 t^2}{2 m^2 a^2}.$$

The width $\sigma(t)$ grows monotonically. The centroid translates at the **group velocity**:

$$v_g = \left.\frac{d\omega}{dk}\right|_{k_0} = \frac{\hbar k_0}{m} = \frac{p_0}{m}.$$

This is the classical velocity $p/m$. Good — the quantum centroid follows Newton.

### Phase Velocity — Not the Same Thing

The **phase velocity** is the speed of an individual wave crest:

$$v_p = \frac{\omega(k_0)}{k_0} = \frac{\hbar k_0}{2m} = \frac{v_g}{2}.$$

The envelope moves at $v_g$. The crests inside the envelope move at $v_p = v_g/2$. In the rest frame of the blob, the crests appear to move *backward* — born at the front, sliding through, dying at the back. They are phase, not matter. The blob carries the momentum; the crests are bookkeeping.

The full complex wave function at time $t$ (needed for $\mathrm{Re}\,\psi$ and $\mathrm{Im}\,\psi$) is:

$$\psi(x, t) = \left(\frac{1}{\pi a^2}\right)^{1/4} \left(\frac{a}{\gamma(t)}\right)^{1/2} \exp\!\left(ik_0 x - i\omega_0 t\right) \exp\!\left(-\frac{(x - v_g t)^2}{2\gamma(t)^2}\right),$$

where $\gamma(t) = a\left(1 + i\hbar t/(ma^2)\right)^{1/2}$ is complex, and $\omega_0 = \hbar k_0^2 / (2m)$. The simulation must use this complex form to draw $\mathrm{Re}\,\psi$ and $\mathrm{Im}\,\psi$; dropping $\gamma(t)$ and using a real Gaussian is a common LLM failure mode.

---

## Worked Example — An Electron in a 1 nm Wave Packet

Let us put numbers on it. An electron ($m = 9.109 \times 10^{-31}$ kg), $a = 1$ nm, $k_0 = 10$ nm$^{-1}$, $\hbar = 1.055 \times 10^{-34}$ J·s.

**Group velocity.**
$$v_g = \frac{\hbar k_0}{m} = \frac{(1.055 \times 10^{-34})(10^{10})}{9.109 \times 10^{-31}} \approx 1.16 \times 10^6 \text{ m/s}.$$
About 0.4% of the speed of light. The non-relativistic assumption holds.

**Phase velocity.**
$$v_p = v_g/2 \approx 5.8 \times 10^5 \text{ m/s}.$$
Half the group velocity. Watch the simulation: the orange ripples inside the blue blob move at this speed, not $v_g$.

**Doubling time.** The width has doubled when $\sigma(t) = \sqrt{2}\,a$, which requires $\sigma(t)^2 = 2a^2 = a^2/2 + \hbar^2 t^2 / (2m^2 a^2)$, giving $t = \sqrt{3}\,ma^2/\hbar$. Numerically:
$$t \approx 1.73 \cdot \frac{(9.109 \times 10^{-31})(10^{-9})^2}{1.055 \times 10^{-34}} \approx 1.5 \times 10^{-14}\ \text{s} = 15\ \text{fs}.$$
In 15 femtoseconds the packet doubles in width.

**Position at $t = 15$ fs.** $v_g \cdot t \approx (1.16 \times 10^6)(1.5 \times 10^{-14}) \approx 17$ nm. Fifteen femtoseconds later, 17 nm to the right, twice as wide.

**The lesson.** Quantum particles on these scales spread fast. A proton of the same width spreads $m_p/m_e \approx 1836$ times more slowly — spreading time $\sim 27$ ps. A marble: longer than the age of the universe. Quantum spreading is only observable for light, small objects where action ($mv \cdot \Delta x$) is comparable to $\hbar$.

**The dead end.** You might try to use explicit Euler to evolve the wave function numerically instead of the analytic closed form. Don't. Explicit Euler is not a unitary integrator; normalization drifts visibly within tens of frames. The normalization indicator catches this immediately, which is why `CLAUDE.md` forbids explicit Euler. The analytic form is exact and computationally cheap.

**The limit.** This calculation assumes a free particle. In a potential, the packet does something else entirely — that is Chapter 5 onward.

---

## Common Misconceptions

**"Phase velocity is the speed of the particle."** Stop and predict: if you watch a wave packet, which speed is the particle's — the speed of the envelope, or the speed of the crests inside it? The crests are tempting, because they are what your eye tracks. But phase velocity belongs to a single, non-normalizable plane-wave component, while a physical (localizable) particle moves at the group velocity $v_g = p/m$. The simulation settles it visually: the orange ripples slip *backward* through the blob even as the blob drifts forward. If phase velocity were "the speed," the particle would appear to move backward while its probability blob moved forward — which is nonsense. Phase velocity is bookkeeping about the oscillation pattern; it carries no momentum.

**"The Brutalist files are bureaucracy."** This one feels true until you run the experiment of doing without them. What does every prompt re-discover when there is no `CLAUDE.md`? The same failure modes: wrong dispersion relation, Canvas instead of SVG, explicit Euler, dropped imaginary part. The file is a memory of failures. And without `PROJECT.md` you lose the parameter conventions mid-semester and spend 30 minutes reconstructing context. The files are the opposite of bureaucracy: they are the reason one prompt works instead of seven.

**"A description is as good as the equation."** Would you accept "a Gaussian wave packet evolving in time" as a spec? Trace what it leaves free: the LLM can use the wrong dispersion relation, drop the $\gamma(t)$ factor, set $\mathrm{Im}\,\psi = 0$, or compute $|\psi|^2$ from a real function. Pasting the closed-form complex equation reduces seven-try problems to one-try problems. Show the artifact.

**"The verification step is optional once you trust Claude."** Ask yourself: what does plausible-looking code hide? LLMs produce output that can be quantitatively wrong in subtle ways — the dispersion relation off by a factor of 2, the normalization integral using the trapezoidal rule on a grid that is too coarse. The verification rubric catches exactly these. Trust but verify — especially the physics.

---

## Exercises

**0.1 — (Understand).** State in one sentence each what `CLAUDE.md`, `DESIGN.md`, and `PROJECT.md` do. Now state what each file is *not* for. (Hint: keyboard-accessibility rules for sliders — behavior or appearance? Pick a side and defend it.)

**0.2 — (Apply).** The dispersion relation for a non-relativistic massive particle is $\omega(k) = \hbar k^2 / (2m)$. Compute the group velocity $v_g = d\omega/dk$ and the phase velocity $v_p = \omega/k$ at a general $k$. Verify $v_g = 2v_p$. Now do the same for a photon ($\omega = ck$): show $v_g = v_p = c$. What does the agreement of group and phase velocity tell you about whether a photon "spreads"?

**0.3 — (Analyze).** A proton wave packet ($m_p = 1.673 \times 10^{-27}$ kg) is prepared with $a = 1$ nm and $k_0 = 10$ nm$^{-1}$. Compute its group velocity, its doubling time, and its position after 15 fs. Compare to the electron values in the Worked Example. Why is the proton "more classical" on these scales?

**0.4 — (Create — production exercise).** Complete the LLM Exercise in the next section. Save the resulting `00-wave-packet.html`. Then modify it: set $k_0 = 0$ and run the animation. The packet does not translate — it only spreads. Explain in two sentences what this tells you about the distinction between "motion" and "uncertainty growth."

**0.5 — (Evaluate).** Open the file Claude produced in Exercise 0.4. Find the line of code that implements the dispersion relation $\omega = \hbar k^2 / (2m)$. Find the line that draws the SVG path for $|\psi|^2$. Find the line that updates the normalization indicator. Write a one-paragraph annotated walkthrough of these three lines. If you cannot find any of the three: that is a bug. The verification stack should have caught it. Re-run the prompt.

---

## Still Puzzling

- **The Brutalist file split is principled, but the boundaries are not always obvious.** When does a slider's keyboard-accessibility rule belong in `CLAUDE.md` (behavior) versus `DESIGN.md` (appearance)? The answer is: behavior. Accessibility rules govern how the component responds, not how it looks. But the book acknowledges this is a fuzzy boundary and asks you to document your choice in `CLAUDE.md`.

- **The verification stack catches arithmetic errors. It does not catch *conceptual* errors that produce numerically plausible output.** A simulation that swaps the labels "Re $\psi$" and "Im $\psi$" will pass every quantitative check. The visual check is the only defense, and it requires you to already know what the correct picture looks like — which is why Chapter 1 begins by pointing directly at what you built here.

- **LLM-generated simulation code drifts in style between sessions even with `CLAUDE.md` in the prompt.** The book treats re-running the same prompt as part of the workflow. This has not been systematically studied in the quantum mechanics curriculum setting; the claim that LLM-assisted interactive learning improves conceptual gains over static text awaits a careful replication study at the upper-division level.

- **This chapter does not teach JavaScript.** It teaches you to read and modify what Claude produces. Whether that is sufficient for Chapters 8 (harmonic oscillator) and 12 (capstone sandbox) remains an open empirical question that the first run of this course will answer.

---

## The +1 — Simulation Exercise: Your First Wave Packet

This is the chapter's deliverable. You will produce three Markdown files and one HTML file. Open Claude and paste the four prompts below in order. The prompts are written to be paste-ready; do not edit them on the first run.

### Part A — The `CLAUDE.md` Prompt (the Coding Constitution)

````markdown
You are helping me build a series of interactive quantum mechanics simulations
in D3.js v7. I am going to give you a coding constitution that you will follow
on every simulation request in this project. Save the following as CLAUDE.md
in the project root, verbatim:

---
# CLAUDE.md — Coding Constitution for QM+1 Simulations

## Runtime and stack
- Single HTML file the user can double-click. No build step. No npm. No server.
- D3.js v7 loaded from https://d3js.org/d3.v7.min.js via a <script> tag.
- Vanilla JavaScript only. No React, no Vue, no jQuery.
- ES2020+ syntax (arrow functions, const/let, template literals, optional chaining).

## Drawing surface
- SVG only. No HTML canvas. No WebGL.
- One <path> element per curve. Never one element per data point.
- Axes drawn with d3.axisBottom / d3.axisLeft.
- Layout: explicit margin object {top, right, bottom, left}.

## Simulation core
- Functions, not classes, for the physics. computeWavefunction(x, t, params)
  returns a typed array.
- SI units internally. Display in physical units (nm, fs, eV) with labels.
- Complex storage as {re, im} objects OR two parallel Float64Arrays.
- Use analytic time evolution where a closed form exists. Numerical PDE
  integration only with a unitary scheme (Crank-Nicolson), never explicit Euler.

## Parameter exposure
- HTML <input type="range"> sliders. Event: "input", not "change".
- Every parameter has a visible numeric readout that updates live.
- Sliders labeled with their physical units.

## Animation
- Single requestAnimationFrame loop. State: {t, dt, paused}.
- Pause/play button. Reset button (returns to t = 0).
- Target 60 fps. If per-frame work exceeds 16 ms, reduce grid resolution
  and warn in the console.

## Verification (required for every simulation)
- A normalization indicator at the top of the page: "∫|ψ|² dx = 1.000".
  If the integral strays from 1 by more than 0.01, color the readout red.
- Print at least three predicted physical values in the UI ("v_g = ...",
  "σ(t) = ...", etc.) so the user can compare against the live simulation.

## Accessibility and dark mode
- Respect @media (prefers-color-scheme: dark).
- Color choices conform to DESIGN.md (separate file).
- Sliders keyboard-navigable. ARIA labels on all interactive elements.

## What NOT to do
- Do not use canvas, WebGL, or any image-based rendering.
- Do not use any library other than D3 v7. (Math.js and fft-js may be added
  later with explicit prompt approval.)
- Do not silently switch to natural units (ℏ = 1, m = 1). If natural units
  help, say so in a comment AND display a unit-conversion note in the UI.
- Do not use explicit Euler for time evolution of the Schrödinger equation.
---

When I ask for a simulation in subsequent prompts, you will read this file
as the binding constitution. If a chapter prompt conflicts with this file,
the chapter prompt wins for that simulation only; flag the conflict in
your response.

Output: confirm you have saved CLAUDE.md, and echo the first 10 lines back
to me so I can verify the save was clean.
````

### Part B — The `DESIGN.md` Prompt (the Visual Constitution)

````markdown
Now save the following as DESIGN.md in the same project root, verbatim:

---
# DESIGN.md — Visual Constitution for QM+1 Simulations

## Color tokens (CSS variables)
- --color-psi-sq:    #1f77b4   (probability density, filled)
- --color-re-psi:    #ff7f0e   (real part of ψ, solid line)
- --color-im-psi:    #888888   (imaginary part of ψ, dashed line)
- --color-potential: #d62728   (V(x), solid)
- --color-energy:    #2ca02c   (energy levels, horizontal solid)
- --color-turning:   #9467bd   (classical turning points, dashed vertical)
- --color-axis:      CanvasText (follows prefers-color-scheme)
- --color-bg:        Canvas     (follows prefers-color-scheme)

## Colormaps for 2D plots
- Unsigned densities (|ψ|², probability surfaces): Viridis.
- Signed amplitudes (Re ψ, perturbation matrices): RdBu centered on 0.
- Never rainbow / jet. Never HSV-cycling palettes.

## Typography
- Numeric readouts in a monospace font (system-ui-monospace).
- Labels and prose in the platform's default sans-serif.
- Math labels use Unicode (ψ, ℏ, σ, π) directly. No MathJax in axis labels.

## Layout
- Stack panels vertically when comparing curves (Re ψ on top of Im ψ on top
  of |ψ|², sharing x-axis).
- Sliders in a fixed panel below or beside the plots.
- Normalization indicator pinned top-right.

## Slider styling
- Range slider with visible thumb and a numeric input next to it for precise
  values. Both update each other.
- Show min, current, max as small text under the slider.

## Legend and units
- Every axis labeled with its physical units in parentheses, e.g. "x (nm)".
- Curves labeled in a small legend in the upper-left of each panel.
- The y-axis of |ψ|² is labeled "|ψ|² (1/nm)" — densities have units.

## Dark / light mode
- All colors above must be readable on both light (#fff) and dark (#111)
  backgrounds. Adjust opacity, not hue, when switching.
---

Confirm save and echo the first 10 lines.
````

### Part C — The `PROJECT.md` Prompt (Project State)

````markdown
Now save the following as PROJECT.md in the same project root:

---
# PROJECT.md — Quantum Mechanics +1 Simulations

**Owner:** [your name]
**Course:** QM Vol. 1, [semester/year]
**Status:** Chapter 0 in progress.

## Built so far
- (none yet)

## Verified
- (none yet)

## Open issues
- (none yet)

## Conventions in use
- Units: SI internally, displayed in nm, fs, eV.
- Default mass: electron, m = 9.109 × 10⁻³¹ kg.
- Default grid: N = 200 points on x ∈ [−20 nm, +20 nm] for free-particle work.
---

Confirm save.
````

### Part D — The Simulation Prompt (Four Moves: Show / Say / Constrain / Verify)

````markdown
SHOW.
The free-particle Gaussian wave packet has the closed-form solution

  ψ(x, 0) = (1/(πa²))^(1/4) · exp(−x²/(2a²)) · exp(i k₀ x)

evolving under Ĥ = p̂²/(2m) to

  |ψ(x, t)|² = (1/(√(2π) σ(t))) · exp(−(x − v_g t)²/(2 σ(t)²))

with σ(t)² = a²/2 + ℏ²t²/(2 m² a²), v_g = ℏk₀/m, v_p = ℏk₀/(2m).

The full complex wave function at time t (analytic, Griffiths §2.4
Problem 2.21) is

  ψ(x, t) = (1/(πa²))^(1/4) · (a / γ(t))^(1/2) ·
             exp(i k₀ x − i ω₀ t) ·
             exp( −(x − v_g t)² / (2 γ(t)²) )

where γ(t) = a · (1 + i ℏ t / (m a²))^(1/2) is complex. Compute
Re ψ and Im ψ from this complex form. ω₀ = ℏ k₀² / (2m).

Use the CLAUDE.md and DESIGN.md saved earlier as binding context.

SAY.
Produce a single file named `00-wave-packet.html`. It opens in a browser and
shows three stacked SVG panels sharing an x-axis:
  - Top:    Re ψ(x, t)   (orange solid line)
  - Middle: Im ψ(x, t)   (gray dashed line)
  - Bottom: |ψ(x, t)|²   (blue filled curve)
Sliders below the plots:
  - a (initial Gaussian width): 0.1 nm to 5 nm, default 1 nm
  - k₀ (central wavenumber): −20 nm⁻¹ to +20 nm⁻¹, default 10 nm⁻¹
  - dt (time step per frame): 10⁻¹⁸ s to 10⁻¹² s, logarithmic, default 10⁻¹⁵ s
  - Mass: dropdown {electron, proton}, default electron.
Buttons: play/pause and reset (returns to t = 0).

CONSTRAIN.
- D3 v7 from CDN. SVG only. Vanilla JS.
- N = 200 grid points on x ∈ [−20 nm, +20 nm].
- Use the analytic complex γ(t) form above. Do NOT integrate the TDSE
  numerically. The closed form is exact.
- Normalization indicator pinned top-right: "∫|ψ|² dx = 1.000".
  Recompute every frame with the trapezoidal rule; red if |I − 1| > 0.01.
- Print three predicted values in the UI:
    v_g = ℏ k₀ / m  (in m/s)
    v_p = ℏ k₀ / (2m)  (in m/s)
    σ(t) = √(a²/2 + ℏ²t²/(2m²a²))  (live, in nm)
  alongside a live readout of the centroid (∫ x |ψ|² dx). The predicted
  and live centroid values should agree to < 1%.

VERIFY.
After writing the file, tell me four things to check in the browser:
(a) at t = 0, the centroid is at x = 0 and σ(0) = a/√2.
(b) the centroid moves at v_g; check by reading the live centroid readout
    at t = 10 fs against the predicted value v_g × t.
(c) σ(t) grows as √(a²/2 + ℏ²t²/(2m²a²)) — check the live readout at
    t = 10 fs against the predicted value.
(d) the normalization indicator stays at 1.000 ± 0.01 throughout.

Then list the known LLM failure modes for this code (wrong dispersion
relation, static plot, normalization drift, v_p/v_g swap in UI labels,
Re/Im phase confusion with γ(t) dropped, silent unit swap, SVG-per-point
performance collapse, missing units on axes) and confirm which you have
actively guarded against.
````

### Part E — Exploration Tasks

After the simulation renders and passes all four verification checks:

1. **Spreading without translation.** Set $k_0 = 0$. The centroid does not move ($v_g = 0$), but the packet still spreads. Write down in two sentences what this distinguishes: spreading is about the *distribution* of position measurements growing wider; it has nothing to do with any notion of the particle "moving."

2. **Narrow spreads faster.** Set $a = 0.2$ nm, $k_0 = 10$ nm$^{-1}$. Run for 5 fs. Then set $a = 2$ nm, same $k_0$. Run for 5 fs. The narrow packet spreads visibly faster. Use $\sigma(t)^2 = a^2/2 + \hbar^2 t^2 / (2m^2 a^2)$ to explain why: the spreading rate $d\sigma/dt$ at small $t$ scales as $\hbar / (ma)$, inversely proportional to $a$.

3. **Watch the inside of the packet.** Set $k_0 = 5$ nm$^{-1}$, $a = 2$ nm, $dt = 10^{-16}$ s. The blue blob moves right at $v_g$. The orange Re $\psi$ ripples move right at $v_p = v_g/2$. In the rest frame of the blob, the ripples slip backward. State clearly: this is not physical motion of any material. It is a phase effect.

4. **Compare to classical.** A classical electron at $x = 0$ with momentum $\hbar k_0$ moves at $v_g$ and stays a point. Run the simulation. At $t = 0$ and $t = 30$ fs, note where the centroid is. It agrees with the classical prediction. But the quantum width has grown; the classical point has not. The centroid obeys Newton. The width does not.

### Part F — Extension Prompt (Momentum-Space Panel)

````markdown
Modify 00-wave-packet.html to add a fourth SVG panel below the existing
three: the momentum-space probability density |φ(k, t)|², where φ(k) is
the spatial Fourier transform of ψ(x).

For the free Gaussian, the analytic result is

  |φ(k, t)|² = (a²/π)^(1/2) · exp(−a² (k − k₀)²)

which is INDEPENDENT OF t. The momentum-space distribution does not spread,
because [Ĥ, p̂] = 0 when V = 0 — momentum is conserved.

Add a line of text under this panel: "Notice: σ_k is constant in t.
This is momentum conservation, made visible."

Verify: σ_k from the simulation should match 1/(a√2) to within 1%.

Keep all existing features as-is. Do not regress any of the three panels.
````

When this extension renders correctly, you have seen the central fact this chapter was building toward: position spreads because momentum has a distribution; momentum does not spread because the free-particle Hamiltonian commutes with the momentum operator. The width of $|\phi(k)|^2$ is fixed. The width of $|\psi(x,t)|^2$ is not. Chapter 1 will name this relationship precisely.

---

## References

- Griffiths, D.J. (2018). *Introduction to Quantum Mechanics* (3rd ed.). Cambridge University Press. §2.4, Problem 2.21 — free-particle Gaussian wave packet analytic solution.
- Hake, R.R. (1998). "Interactive-engagement versus traditional methods: A six-thousand-student survey of mechanics test data for introductory physics courses." *Am. J. Phys.* 66(1), 64–74. [doi:10.1119/1.18809](https://pubs.aip.org/aapt/ajp/article/66/1/64/1055076/Interactive-engagement-versus-traditional-methods) — the foundational meta-analysis on interactive engagement; the ~2× normalized gain is the pedagogical basis for the simulation-first approach.
- Wieman, C.E., Adams, W.K., & Perkins, K.K. (2008). "PhET: Simulations that enhance learning." *Science* 322, 682–683. [doi:10.1126/science.1161948](https://www.science.org/doi/10.1126/science.1161948) — evidence for interactive simulation in physics education.
- McKagan, S.B., Perkins, K.K., & Wieman, C.E. (2010). "Design and validation of the Quantum Mechanics Conceptual Survey." *Phys. Rev. ST PER* 6, 020121. [doi:10.1103/PhysRevSTPER.6.020121](https://journals.aps.org/prper/abstract/10.1103/PhysRevSTPER.6.020121) — the QMCS instrument for assessing conceptual understanding.
- Kovesi, P. (2015). "Good colour maps: How to design them." [arXiv:1509.03700](https://arxiv.org/abs/1509.03700) — the perceptual-uniformity argument for Viridis and RdBu over rainbow/jet palettes.
- Borland, D. & Taylor, R.M. (2007). "Rainbow color map (still) considered harmful." *IEEE CG&A* 27(2), 14–17. [doi:10.1109/MCG.2007.323435](https://doi.org/10.1109/MCG.2007.323435) — companion evidence on colormap perceptual distortion.
- D3.js v7 documentation. [d3js.org](https://d3js.org) — CDN URL confirmed live: `https://d3js.org/d3.v7.min.js`.

---

*The next chapter tells you what the wave packet you just built is actually saying. You watched a blue curve drift and spread. Now we figure out what it means.*

---

## Running Project — Build the 1D Quantum Sandbox

**This chapter adds:** the project skeleton — the three Brutalist governing files (`CLAUDE.md`, `DESIGN.md`, `PROJECT.md`), the SI-units convention, the `{re, im}` complex-array storage rule, and the normalization indicator that every later piece of the sandbox will be judged against.

### Exercise R1 — When to Use AI
**The judgment:** In this chapter's project work, AI assistance is appropriate for:
- Drafting the `CLAUDE.md` / `DESIGN.md` / `PROJECT.md` files from your dictated rules — *Why AI works here:* reformatting your stated conventions into clean Markdown is boilerplate; you can read every line back and confirm it says what you meant.
- Scaffolding the SVG plotting and slider wiring for the first wave-packet page — *Why AI works here:* this is generating standard D3 boilerplate against a fixed spec, and the analytic Gaussian gives you an independent check on the output.
**The tell:** You are using AI well when you have an independent way to check the output — here, the analytic closed form $\sigma(t) = \sqrt{a^2/2 + \hbar^2 t^2/(2m^2a^2)}$ and the normalization integral that must read 1.000.

### Exercise R2 — When NOT to Use AI
**The judgment:** These tasks require your judgment; AI output here can't be trusted without redoing the work:
- Deciding which rules belong in `CLAUDE.md` (behavior) versus `DESIGN.md` (appearance) — *Why AI fails here:* this is a design-architecture call about your own debugging workflow; the AI will produce a plausible split that may scatter behavioral rules into the visual file, and nothing in the output flags the mistake.
- Choosing the units convention and the meaning of the normalization indicator — *Why AI fails here:* a physical-validity call. The AI can write `∫|ψ|²dx` in a corner, but whether it reads 1.000 because the physics is right or because of a compensating bug is a judgment only you can make.
**The tell:** If you could not explain the result without the AI — if the AI is your *reason* rather than your *tool* — it did work that should have been yours.
**Physics-judgment connection:** This trains the habit of checking a numerical result against normalization (∑|ψ|²·h = 1) and against an analytic closed form before believing the picture on screen.

### Exercise R3 — LLM Exercise
**What you're building this chapter:** the three governing Markdown files plus the analytic free-particle wave-packet page, which together fix every convention the sandbox inherits.
**Tool:** Claude Project — the three governing files are persistent context that every subsequent chapter's prompt loads, which is exactly what a Project's knowledge files are for.
**The Prompt:**
```
You are setting up a single-page JavaScript/D3 quantum-mechanics simulation
project that will grow, one chapter at a time, into a configurable 1D
Schrödinger solver. Produce three Markdown governing files and one HTML file.

CLAUDE.md (coding constitution): single self-contained HTML file, no build
step; D3 v7 from CDN; SVG only (one <path> per curve); physics as pure
functions, not classes; SI units internally, displayed in nm/fs/eV; complex
wave functions stored as two parallel Float64Arrays (re, im) — never collapsed
to a real array; analytic time evolution where a closed form exists, and if a
numerical Schrödinger stepper is ever needed it must be unitary (Crank-Nicolson
or split-step), never explicit Euler; every page shows a normalization
indicator ∫|ψ|²dx that reads 1.000 and turns red if it strays by >1%.

DESIGN.md (visual constitution): |ψ|² blue filled; Re ψ orange solid; Im ψ
gray dashed; V(x) red; energy levels green horizontal; turning points purple
dashed. Viridis for unsigned 2D maps, RdBu for signed; never rainbow/jet.
Monospace for numeric readouts. Every axis labeled with physical units.

PROJECT.md (project state): owner, course, status "Chapter 0 — sandbox
skeleton", a "Built so far" list (empty), a "Verified" list (empty), and the
default conventions (electron mass m_e = 9.109e-31 kg; default grid N points
on a stated x-range).

Then build 00-wave-packet.html: a free-particle Gaussian wave packet using the
ANALYTIC complex solution
  ψ(x,t) = (1/(πa²))^(1/4) (a/γ(t))^(1/2) exp(i k₀ x − i ω₀ t)
           exp(−(x − v_g t)²/(2 γ(t)²)),
  γ(t) = a (1 + iℏt/(ma²))^(1/2),  ω₀ = ℏk₀²/(2m),  v_g = ℏk₀/m.
Three stacked SVG panels (Re ψ, Im ψ, |ψ|²) sharing an x-axis, sliders for a
and k₀, a pinned normalization indicator, and live readouts of v_g and σ(t).
Do NOT integrate the time-dependent Schrödinger equation numerically — the
closed form is exact. After writing, list four browser checks I can run.
```
**What this produces:** `CLAUDE.md`, `DESIGN.md`, `PROJECT.md`, and `00-wave-packet.html` — the skeleton every later sandbox piece bolts onto.
**How to adapt:** *Your system:* if you prefer dark mode, set the palette in `DESIGN.md` only and re-run. *ChatGPT/Gemini:* paste the three files as a preamble in every session since they lack a persistent Project store. *Claude Project:* put the three files in the Project's knowledge, not in the message, so they bind every chapter without re-pasting.
**Builds on:** nothing — this is the foundation.  **Next:** Chapter 2 turns de Broglie's $\lambda = h/p$ into the spatial grid the solver runs on.

### Exercise R4 — CLI Exercise
**What you're building this chapter:** a verified project directory with the three governing files and the wave-packet page, committed so later chapters extend a known-good base.
**Tool:** Claude Code — it can create the files on disk, run a normalization check, and leave the directory in a state you can diff and version-control.
**Skill level:** Beginner
**Setup — confirm:**
- [ ] `00-wave-packet.html` from the R3 prompt (or let Claude Code generate it)
- [ ] Node.js or a browser available to open the HTML
- [ ] A `CLAUDE.md` in the project root with the coding-constitution rules above
**The Task:**
```
In the project directory, confirm CLAUDE.md, DESIGN.md, and PROJECT.md exist
and match the conventions stated in CLAUDE.md (SI units, {re, im} storage,
normalization indicator, no explicit Euler). Do NOT edit the physics in
00-wave-packet.html. Add a tiny standalone Node script check-norm.js that
reproduces the analytic |ψ(x,0)|² on a grid of N = 500 points over
x ∈ [−20 nm, +20 nm] and prints the trapezoidal integral ∫|ψ|²dx. Run it and
report the number; it must read 1.000 ± 0.001. Append one line to PROJECT.md
under "Verified": "Ch0 wave packet: ∫|ψ|²dx = <value>". Leave all .html
physics untouched.
```
**Expected output:** a `check-norm.js` script, a printed normalization value near 1.000, and one new line in `PROJECT.md`.
**What to inspect:** that the integral uses the $h$-weighted trapezoidal rule (spacing $h = 40\,\text{nm}/(N-1)$), and that the printed value is 1.000, not 250 or 0.004 (those would signal a missing or doubled $h$ factor).
**If it goes wrong:** if the integral reads ~250, the script summed $|\psi|^2$ without multiplying by the grid spacing $h$ — the single most common normalization bug, and the one that will haunt the eigensolver in Chapter 5. Fix the weighting, don't rescale ψ.
**CLAUDE.md / AGENTS.md note:** add a standing rule: "Every normalization integral is ∑ⱼ|ψⱼ|²·h, not ∑ⱼ|ψⱼ|². State h explicitly in the code."

### Exercise R5 — AI Validation Exercise
**What you're validating:** the `00-wave-packet.html` page and the three governing files the AI produced in R3.
**Validation type:** Code + Numerical result
**Risk level:** Low — there is an exact analytic answer to check against, so failures are catchable.
**Setup:** use your own R3/R4 artifacts.
**The Validation Task:** Evaluate against this checklist; mark Pass / Fail / Cannot determine with reasoning.
```
Validation Checklist — How to Use the Simulations (sandbox skeleton)
□ Correctness: does ψ use the complex γ(t) form, so Im ψ is non-zero for k₀ ≠ 0?
□ Completeness: are all three governing files present, and does CLAUDE.md
  forbid explicit Euler and mandate {re, im} storage?
□ Scope: did it add a build step, npm, or a non-D3 library it was told not to?
□ Normalization: does ∫|ψ|²dx read 1.000 ± 0.001 at t = 0 and stay there as t runs?
□ Group velocity: does the live centroid move at v_g = ℏk₀/m (check at t = 10 fs)?
□ Failure-mode check: any of —
  - fluent but wrong (static plot that looks animated, or |ψ|² that ignores spreading)
  - dropped imaginary part (Im ψ ≡ 0 for k₀ ≠ 0)
  - normalization read without the h weighting (indicator reads ~250 or ~0.004)
  - silent unit swap (natural units ℏ = m = 1 with no UI note)
```
**What to do with findings:** pass → use it, note that the analytic form made it trustworthy; one fail → revise the prompt to re-state the γ(t) form explicitly, re-run, document the change; multiple fails / cannot-determine → do the wave-packet math yourself and have the AI only wire the plot.
**AI Use Disclosure (mandatory, two sentences):**
> *1:* The AI drafted the three governing Markdown files and the D3 wave-packet page from my dictated conventions and the analytic ψ(x,t) formula.
> *2:* The AI could not determine whether the normalization indicator read 1.000 because the physics was correct or because of a compensating h-weighting error — I verified that independently against the trapezoidal integral.
**Physics-judgment connection:** establishes the discipline that anchors the whole project — never trust a simulation's picture until its normalization integral and its analytic limit both check out.
