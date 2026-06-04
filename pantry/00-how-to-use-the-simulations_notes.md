# Research Notes: Chapter 00 — How to Use the Simulations

**Corresponding chapter:** chapters/00-how-to-use-the-simulations.md (not yet written)
**Generated:** 2026-06-03

---

## Chapter summary (capability built)

By the end of this chapter the student has a working browser simulation (`00-wave-packet.html`) — a free-particle Gaussian wave packet spreading and translating in real time under D3 v7. More importantly, they have three governing Markdown files (`CLAUDE.md`, `DESIGN.md`, `PROJECT.md`) and know the four-move prompt structure (Show / Say / Constrain / Verify) that will reproduce a working simulation on the first or second try throughout the rest of the book. No new physics is taught; the physics (dispersion, group vs. phase velocity) appears in Ch 1–2 proper. This chapter is pure apparatus installation.

---

## A. Conceptual foundations

### 1. The Brutalist three-file system

**Explanation.** Three Markdown files govern every simulation in the course:
- `CLAUDE.md` — coding constitution: runtime (browser, no build), library (D3 v7), drawing surface (SVG only), animation loop (`requestAnimationFrame`), normalization indicator, units conventions, what NOT to do (no Canvas, no WebGL, no explicit Euler, no silent unit swap).
- `DESIGN.md` — visual constitution: color tokens per curve type (|ψ|² in `#1f77b4`, Re ψ in `#ff7f0e`, Im ψ in `#888888`, V(x) in `#d62728`, energy levels in `#2ca02c`, classical turning points in `#9467bd`), colormap rules (Viridis for unsigned, RdBu for signed, never rainbow/jet), font, axis label conventions.
- `PROJECT.md` — project memory: chapter being worked, simulations built, parameter ranges used, verified items, open issues.

**Why three files, not one.** Token economy: in Chapter 7 a hydrogen-atom prompt should not re-read slider-styling rules. Debugging clarity: a wrong color is a `DESIGN.md` problem; a wrong dispersion relation is a `CLAUDE.md` problem. Accessibility/behavioral crossover is a known fuzzy boundary (see Section G).

**Common misconception.** "The files are bureaucracy." They are the reason simulations are consistent across 12 chapters and debuggable by anyone. Without them students re-discover the same conventions each week and produce 12 visually incompatible simulations.

**Worked example.** A student wants to add a momentum-space panel to the wave-packet simulation three weeks after the original prompt. Without `PROJECT.md` Claude has no memory of the grid parameters, the unit conventions, or the SVG layout already in use. With `PROJECT.md` the extension prompt is five lines; without it, a student spends 30 minutes re-specifying context.

**Sources.** `_lib_qmsri-00-how-to-use-the-simulations.md` §4 (the Brutalist system); colormap research: Kovesi 2015, [arXiv:1509.03700](https://arxiv.org/abs/1509.03700); Borland & Taylor 2007, *IEEE CG&A* 27, 14–17.

---

### 2. The four-move prompt: Show / Say / Constrain / Verify

**Explanation.**
- **Show:** paste the artifact — the exact equation (LaTeX if needed), not a description of it. Vague descriptions are the top cause of bad LLM-generated code.
- **Say:** one imperative sentence with audience and deliverable format ("a single HTML file I can open in Chrome with a slider for σ").
- **Constrain:** D3 v7 from CDN, SVG only, no build step, normalization indicator visible. Constraints shrink the model's search space and reduce hallucination.
- **Verify:** ask Claude what to check. This converts the model from oracle to collaborator. For the wave packet: (a) centroid at x = 0, t = 0; (b) centroid moves at v_g; (c) σ(t) grows per formula; (d) normalization stays at 1.000 ± 0.01.

**Common misconception.** "A good description is enough." No — showing the closed-form equation (e.g., the full complex Gaussian at time t including the γ(t) = a(1 + iℏt/(ma²))^{1/2} factor) is what distinguishes a first-try success from a seventh-try failure. LLMs hallucinate phase factors when not given the analytic expression.

**Worked example.** The Chapter 0 Part D simulation prompt (in the _lib_ file) is the canonical example: it pastes the closed-form |ψ(x,t)|² formula with σ(t) and v_g, states the deliverable in one sentence, names five constraints, and asks for four verification checks. This is the template for every LLM Exercise in the book.

**Sources.** `_lib_qmsri-00-how-to-use-the-simulations.md` §5.

---

### 3. The free-particle Gaussian and its two velocities

**Explanation.** The initial wave packet is:
$$\psi(x,0) = \left(\frac{1}{\pi a^2}\right)^{1/4} e^{-x^2/(2a^2)} e^{ik_0 x}$$
Time evolution under H = p²/2m gives the dispersion relation ω(k) = ℏk²/(2m). The packet remains Gaussian with a growing width σ(t) and a translating centroid:
$$|\psi(x,t)|^2 = \frac{1}{\sqrt{2\pi}\,\sigma(t)} \exp\!\left(-\frac{(x - v_g t)^2}{2\sigma(t)^2}\right), \quad \sigma(t)^2 = \frac{a^2}{2} + \frac{\hbar^2 t^2}{2m^2 a^2}$$
Two velocities:
- Group velocity: $v_g = \hbar k_0 / m = p_0/m$ — the speed of the envelope and centroid of |ψ|².
- Phase velocity: $v_p = \hbar k_0 / (2m) = v_g/2$ — the speed of individual wave crests (Re ψ ripples).

In the simulation: the blue |ψ|² blob moves at v_g; the orange Re ψ ripples inside it move at v_p = v_g/2, so in the rest frame of the blob the crests appear to travel backward.

**Common misconception.** "Phase velocity is the speed of the particle." Phase velocity belongs to individual un-normalizable plane-wave components; the particle (to whatever extent it has a speed) moves at v_g = p/m.

**Worked example (electron, a = 1 nm, k₀ = 10 nm⁻¹).**
- v_g = (1.055 × 10⁻³⁴)(10¹⁰)/(9.109 × 10⁻³¹) ≈ 1.16 × 10⁶ m/s (~0.4% c — non-relativistic).
- Doubling time (σ → 2σ): t ≈ √3 · ma²/ℏ ≈ 1.5 × 10⁻¹⁴ s = 15 fs.
- Position after 15 fs: ≈ 17 nm.
- Same calculation for a proton: doubling time ~27 ps (m_p/m_e ≈ 1836× longer).
- For a marble: doubling time >> age of universe. Quantum spreading is only observable for light/small objects.

**Sources.** `_lib_qmsri-00-how-to-use-the-simulations.md` §6–7; Griffiths *Introduction to Quantum Mechanics* §2.4, Problem 2.21.

---

### 4. The verification stack and its limits

**Explanation.** Every simulation ships with three checks:
1. **Format check:** single HTML file opens in browser without a console error, sliders respond, pause/play works.
2. **Physics check:** centroid position matches v_g × t to < 1%; σ(t) matches the analytic formula; normalization indicator reads 1.000 ± 0.01.
3. **Behavior check:** visual sanity — blue blob moves right while orange ripples slip backward through it, narrower packets spread faster.

The verification stack is the immune response against LLM hallucination. Known failure modes the prompt must actively guard against: wrong dispersion relation (ω = k² vs. ω = ℏk²/2m), static plot (animation loop not wired to physics update), normalization drift (numerical integration error), v_p/v_g swap in UI labels, Re/Im phase confusion (γ(t) factor dropped or handled incorrectly), silent unit swap (ℏ set to 1 without notice), SVG-per-point performance collapse (one path element per data point rather than one per curve), missing units on axes.

**Common misconception.** "The verification stack catches all bugs." It catches quantitative bugs. It does not catch label swaps (Re ψ and Im ψ mislabeled) or conceptual bugs that produce plausible-looking numerics. Visual inspection is the only defense, which requires the student to already know what the right picture should look like.

**Sources.** `_lib_qmsri-00-how-to-use-the-simulations.md` §5 (Verify move), §8 (open issues).

---

### 5. D3 v7 as the simulation library

**Explanation.** D3 v7 is loaded from CDN (`https://d3js.org/d3.v7.min.js`). The choice of SVG over Canvas or WebGL is deliberate: 1D wave functions are curves, SVG draws curves natively with `<path>` elements and D3's line generators, scaling is clean, and the resulting code is readable. One `<path>` per curve, not one element per data point. Axes use `d3.axisBottom` / `d3.axisLeft`. Animation uses `requestAnimationFrame`; D3's built-in transition system is not used for physics time evolution (it is too coarse — physics needs per-frame computation, not pre-specified tweens).

**Common misconception.** "D3 transitions handle animation." D3 transitions are for UI animations (bar growing, circle moving) not for real-time physics loops. For the wave packet, every frame re-computes the full analytic solution at the new t and re-binds the path data.

**Sources.** D3 v7 official docs: [d3js.org](https://d3js.org); DevDocs D3.js 7: [devdocs.io/d3~7/](https://devdocs.io/d3~7/); Observable D3 animation tutorial: [observablehq.com/@d3/learn-d3-animation](https://observablehq.com/@d3/learn-d3-animation).

---

## B. Domain examples and cases

### Case 1 — The first artifact: `00-wave-packet.html`
Three stacked SVG panels (Re ψ orange, Im ψ gray dashed, |ψ|² blue filled), sharing an x-axis over x ∈ [−20 nm, +20 nm], N = 200 grid points. Sliders: σ (0.1–5 nm, default 1 nm), k₀ (−20 to +20 nm⁻¹, default 10 nm⁻¹), dt (logarithmic 10⁻¹⁸ to 10⁻¹² s, default 10⁻¹⁵ s), mass dropdown (electron/proton). Buttons: play/pause, reset. Normalization indicator top-right. Three predicted vs. live readouts: v_g, v_p, σ(t), live centroid.

### Case 2 — Extension: momentum-space panel
Part F of the LLM Exercise adds a fourth panel showing |φ(k,t)|² — the Fourier transform. For the free Gaussian this is **time-independent**: |φ(k)|² = (a²/π)^{1/2} exp(−a²(k−k₀)²). The panel teaches the punchline: position spreads because momentum has a distribution; momentum is conserved (σ_k constant in t) because [H, p] = 0 for V = 0.

### Case 3 — k₀ = 0 exploration
Setting k₀ = 0: the centroid does not move (v_g = 0) but σ(t) still grows. This cleanly separates "spreading" from "translation" — a key conceptual distinction for the uncertainty principle discussion in Ch 1.

### Failure case — Explicit Euler time evolution
If a student or LLM uses explicit Euler to integrate the TDSE instead of the analytic closed form (or Crank-Nicolson for later simulations), normalization will drift visibly within tens of frames. The normalization indicator catches this immediately. `CLAUDE.md` explicitly forbids explicit Euler.

---

## C. Connections and dependencies

**Prerequisites:** No QM physics required. Students need only: comfort opening a `.html` file in a browser, ability to copy-paste text, and access to Claude or a comparable LLM.

**Unlocks:**
- Every subsequent LLM Exercise in the book (Chapters 1–11) uses the same four-move structure and the same three governing files.
- Chapter 1 gives the physics of what the Ch 0 simulation shows (wave function interpretation, uncertainty principle, Born rule).
- Chapter 2 uses the same Gaussian wave packet as a limiting case when introducing the time-independent Schrödinger equation.

**Adjacent chapters:**
- Ch 0 is structurally unique — no physics deep-dive. Ch 1 restores the standard anatomy and immediately references the simulation built here.

---

## D. Current state of the field

**Settled.** D3 v7 is a mature, stable library; the SVG-for-physics-curves approach is well-established in interactive science education tools (PhET, Observable notebooks). The Brutalist Markdown convention is the book's own design choice, not a field standard, but the underlying principle (explicit rules in version-controlled plain text) is standard software engineering practice.

**Contested / open.** LLM-generated simulation code drifts in style between sessions even with `CLAUDE.md` in context — the book acknowledges this and treats re-running the same prompt as part of the workflow. This has not been systematically studied.

**Key references (verified).**
- Hake, R.R. (1998). "Interactive-engagement versus traditional methods: A six-thousand-student survey of mechanics test data for introductory physics courses." *Am. J. Phys.* 66(1), 64–74. [doi:10.1119/1.18809](https://pubs.aip.org/aapt/ajp/article/66/1/64/1055076/Interactive-engagement-versus-traditional-methods) — the foundational meta-analysis showing ~2× normalized gain for interactive engagement over lecture.
- Wieman, C.E., Adams, W.K., & Perkins, K.K. (2008). "PhET: Simulations that enhance learning." *Science* 322, 682–683.
- Kovesi, P. (2015). "Good colour maps: How to design them." [arXiv:1509.03700](https://arxiv.org/abs/1509.03700) — colormap justification for Viridis/RdBu.
- McKagan et al. (2010). *Phys. Rev. ST PER* 6, 020121 — QMCS (Quantum Mechanics Conceptual Survey) instrument.

**Recent developments.** LLM-assisted code generation for physics education is new (2023–2026). The book is among the first to use it systematically at the undergraduate level. No peer-reviewed comparison studies of LLM-generated vs. human-written simulation curricula exist yet (as of 2026-06).

---

## E. Teaching considerations

**Where students get stuck.**
1. File setup friction: students create `CLAUDE.md` but do not load it in the prompt, so Claude ignores it. Fix: the prompt must quote or reference the file by name.
2. LLM produces Python instead of HTML. Fix: "Say" move must specify "a single HTML file I can double-click in Chrome."
3. Simulation renders but is static (no animation). Root cause: `requestAnimationFrame` loop exists but is not called, or the physics update is outside the loop. The behavior check catches this immediately.
4. Phase velocity vs. group velocity confusion when watching the simulation. The orange ripples moving "backward" through the blue blob is counterintuitive; students often think the blob is moving backward.
5. `PROJECT.md` neglect — students stop updating it after Ch 1, causing context loss in later chapters.

**Analogies.**
- The three-file split is like a restaurant: `CLAUDE.md` is the kitchen rules (how to cook), `DESIGN.md` is the plating guide (how it looks), `PROJECT.md` is the order log (what has been made today).
- Group vs. phase velocity: a wave on water — the ripple pattern (phase) moves at a different speed than the energy in a wave group (group). Boats at sea can move at the group velocity while the waves roll under them.

**Exercises (with Bloom level).**
- **Remember/Understand:** State in one sentence each what the three files do. (Bloom: Remember)
- **Apply:** Use the four-move prompt to produce `00-wave-packet.html` and run the four verification checks. (Bloom: Apply/Create)
- **Analyze:** Set k₀ = 0; observe spreading without translation. Explain in two sentences what this tells you about "spreading" vs. "motion." (Bloom: Analyze)
- **Evaluate:** Open the generated file. Find the line implementing the dispersion relation, the SVG path for |ψ|², and the normalization computation. Write an annotated walkthrough. (Bloom: Evaluate)
- **Create:** Add a fourth panel showing |φ(k,t)|² using the Part F extension prompt. Verify σ_k is constant in t to within 1%. (Bloom: Create)

---

## F. Library files relevant to this chapter

- `/Users/bear/Documents/CoWork/bear-textbooks/books/quantum-mechanics-vol1/pantry/_lib_qmsri-00-how-to-use-the-simulations.md` — **primary source.** Contains the complete chapter text including: all three governing file contents (verbatim), the four-move prompt structure, all five LLM Exercise prompts (Parts A–F), the worked numerical example (electron 1 nm packet), the five exercises with Bloom levels, the "what would change my mind" section citing Hake 1998 and McKagan 2010, and the "still puzzling" section. This file is the chapter in draft form; notes are a synthesis of it.

---

## G. Gaps and flags

**FLAG — Accessibility boundary.** The chapter acknowledges but does not resolve which file owns keyboard-accessibility rules for sliders — behavior (`CLAUDE.md`) or appearance (`DESIGN.md`). The chapter author should pick a side and document it.

**FLAG — LLM session drift.** The book notes that `CLAUDE.md` does not fully stabilize code style across sessions. The notes chapter does not document a systematic recovery procedure. The chapter author should either (a) add a "reset" prompt to Part A of the LLM Exercise, or (b) add a note to `PROJECT.md` conventions section.

**GAP — JavaScript prerequisite.** The chapter explicitly states it does not teach JavaScript and relies on students reading/modifying what Claude produces. Whether this is sufficient for Chapters 7 (hydrogen atom) and 11 (perturbation theory) is unresolved. The chapter author may want to add a "minimum JS you need to read a D3 file" sidebar.

**GAP — Failure mode documentation.** The chapter lists eight known LLM failure modes for the wave-packet prompt but does not systematically tell students how to diagnose and fix each one. A troubleshooting table (symptom → likely cause → fix prompt) would be high-value.

**GAP — Web research on D3 v7.** D3 v7 SVG path animation with `requestAnimationFrame` is well-documented at [d3js.org](https://d3js.org) and [devdocs.io/d3~7/](https://devdocs.io/d3~7/). The chapter does not need external citation here — the `CLAUDE.md` prompt itself specifies the exact CDN URL. Chapter author: confirm the CDN URL `https://d3js.org/d3.v7.min.js` is still live at time of publication.
