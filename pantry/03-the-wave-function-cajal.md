# CAJAL Figure Report — Chapter 3 — The Wave Function and Born's Rule

Recommended: 4 figures, Foundational density.

---

## Figure 1 — |ψ|² as Probability Density: The Density vs. Probability Distinction

**Rank: Critical | Heuristic: VG** — The chapter's opening argument is that |ψ|² is a density (units: nm⁻¹), not a probability (dimensionless). The text states explicitly: "The density |ψ|² can exceed 1 — it is per unit length, not a dimensionless probability." This is described as "the single most common first mistake." A grounding figure that makes the density/probability distinction spatial and visual is the highest-leverage illustration in the chapter.

---

### BLOCK 1 — ILLUSTRAE PASTE BLOCK

Draw a two-panel figure. In the left panel, show a filled curve representing |ψ(x)|² for a normalized Gaussian wave packet plotted against a horizontal position axis; the peak of the filled curve should visually exceed the horizontal midpoint of the panel, emphasizing that the density value at a point can be greater than one (when the axis is in nanometers). Mark a shaded interval [a, b] beneath the curve as a filled region with a distinct color, indicating the area under the curve over that interval — this area is the probability of finding the particle in [a, b]. In the right panel, draw a simple bar chart with two bars: the left bar represents the shaded area from the left panel (the integrated probability, a number between 0 and 1); the right bar represents the peak value of |ψ|² at the center of the distribution (which may exceed 1). The left bar is shorter than or equal to 1 in height; the right bar may be taller than the left bar. The y-axis of the right panel originates at zero. Both panels share a common visual style. No baked text. No numerical values. No axis labels.

---

### BLOCK 2 — FULL SCOPE

- **[S]** Single-column 89 mm, 300 DPI, vector, white background.
- **[C]** Chapter content only. Left panel: |ψ(x)|² for a normalized double-exponential or Gaussian profile (the chapter's worked example is ψ = (1/√a)e^{-|x|/a}, giving |ψ|² = (1/a)e^{-2|x|/a}; for a = 0.5 nm the peak is 2 nm⁻¹ > 1). Shaded interval [−a, a] with area ≈ 0.865 (from chapter's worked calculation). Right panel: two bars — shaded area (~0.865, less than 1) and peak density (potentially > 1 for small a). Y-axis of right panel runs from zero upward; the two bars visually demonstrate that the density value can exceed 1 while the integrated area is bounded by 1.
- **[O]** Left panel: x-axis horizontal (position), y-axis vertical (density), filled area curve with shaded sub-interval. Right panel: two-bar vertical bar chart, y-axis from zero. Panels side by side with a thin dividing rule.
- **[P]** Flat vector. Okabe-Ito. |ψ|² filled curve: Blue #0072B2 at 40% opacity fill, Blue #0072B2 stroke 1 pt. Shaded integral interval: Bluish Green #009E73 filled at 70% opacity (active — this is the probability, the thing that equals 1). Peak density bar in right panel: Vermillion #D55E00 (signals the potential for misconception — density can exceed 1). Integrated area bar in right panel: Bluish Green #009E73. Axis rules: Black, 1 pt. Panel divider: light gray, 0.5 pt. NO baked text, NO 3D, NO red-green.
- **[E]** EXCLUSIONS: Re ψ and Im ψ curves (belong to Figure 2); normalization proof derivation steps; probability current J; momentum-space density |φ(p)|²; Kennard bound illustration; any comparison with classical probability distributions.

---

### BLOCK 3 — NEGATIVE PROMPT

Re ψ oscillation curve, Im ψ oscillation curve, momentum space axis, probability current arrows, normalization integral derivation steps, Gaussian vs. exponential comparison panels, classical probability distribution overlay, pie chart, 3D bar chart, histogram with many bins, axis number labels, unit annotations, legend text, text labels, words, gibberish letters, titles, captions, decorative borders, realistic textures, drop shadows, gradient backgrounds, photographic elements, dual-headed arrows, hand-drawn styles, human figures, visual clutter, watermarks, red-green color combinations, rainbow color scales, 3D perspective distortion

---

## Figure 2 — Re ψ, Im ψ, and |ψ|² Three-Panel Stack for a Gaussian Wave Packet

**Rank: Critical | Heuristic: VG + PQ** — The chapter states: "The orange curve was Re ψ. The gray dashed curve was Im ψ. Both were non-trivial; the imaginary part led the real part by a quarter cycle." It then proves algebraically that |ψ|² = A²e^{-x²/a²} — no oscillation — even though both Re ψ and Im ψ oscillate. This is a structural comparison claim: three curves on a shared x-axis, where one surprising result (the cancellation of oscillations in |ψ|²) is the argument. A three-panel comparison figure with a shared axis is the canonical figure type.

---

### BLOCK 1 — ILLUSTRAE PASTE BLOCK

Draw three panels stacked vertically, all sharing an identical horizontal position axis. In the top panel, plot a damped cosine curve representing Re ψ for a Gaussian wave packet with nonzero central momentum k₀: the curve oscillates under a Gaussian envelope, positive and negative, symmetric about zero. In the middle panel, plot a damped sine curve representing Im ψ for the same wave packet: it oscillates under the same Gaussian envelope but shifted by a quarter cycle relative to Re ψ, so that where Re ψ peaks, Im ψ crosses zero. In the bottom panel, plot |ψ|² as a smooth filled Gaussian curve, entirely non-negative, with no oscillation structure — the modulation visible in the top two panels is completely absent. All three panels share the same horizontal extent and same x-axis scale. The top and middle panels have a zero-crossing horizontal axis rule; the bottom panel has a zero baseline at the bottom. A thin vertical dashed reference line passes through all three panels at the same x-position to make the phase relationship visible.

---

### BLOCK 2 — FULL SCOPE

- **[S]** Single-column 89 mm, 300 DPI, vector, white background.
- **[C]** Chapter content only. Wave packet: ψ(x) = A e^{-x²/(2a²)} e^{ik₀x}. Re ψ = A e^{-x²/(2a²)} cos(k₀x). Im ψ = A e^{-x²/(2a²)} sin(k₀x). |ψ|² = A² e^{-x²/a²}. Quarter-cycle phase lead of Im ψ relative to Re ψ explicitly visible. |ψ|² must show no oscillation. Use k₀ such that approximately 4–6 oscillation cycles are visible under the Gaussian envelope. Vertical reference line at x = 0 or at a peak of Re ψ to show Im ψ = 0 there.
- **[O]** Three panels stacked vertically, shared x-axis at bottom of stack. Top panel: Re ψ, oscillating, zero-mean, Gaussian-enveloped. Middle panel: Im ψ, oscillating, zero-mean, same envelope, quarter-cycle shifted. Bottom panel: |ψ|², non-negative filled Gaussian. Shared vertical reference dashed line. Each panel enclosed by thin border. Equal panel heights.
- **[P]** Flat vector. Okabe-Ito. Re ψ curve: Orange #E69F00, 1.5 pt stroke. Im ψ curve: Reddish Purple #CC79A7 dashed, 1.5 pt stroke (the chapter calls it "gray dashed" but the CAJAL palette avoids pure gray for the active curve; Reddish Purple distinguishes it without using red-green). |ψ|² fill: Blue #0072B2 at 50% opacity fill, Blue #0072B2 stroke 1.5 pt. Zero-axis rules in top and middle panels: light gray, 0.5 pt. Vertical reference line: light gray, dashed, 0.5 pt. Panel borders: light gray, 0.5 pt. NO baked text, NO 3D, NO red-green.
- **[E]** EXCLUSIONS: time evolution (snapshot at t = 0 only); momentum-space representation φ(p); probability current J; Kennard bound illustration; energy spectrum; complex-plane Argand diagram; any curve beyond the three stated.

---

### BLOCK 3 — NEGATIVE PROMPT

Argand diagram, complex plane plot, momentum space panel, time-evolution animation frames, probability current arrow overlay, energy spectrum panel, multiple wave packets compared, node labels, oscillation frequency annotation, envelope Gaussian outline curve, text labels, words, gibberish letters, titles, captions, decorative borders, realistic textures, drop shadows, gradient backgrounds, photographic elements, dual-headed arrows, hand-drawn styles, human figures, visual clutter, watermarks, red-green color combinations, rainbow color scales, 3D perspective distortion

---

## Figure 3 — Normalization as Area: The Continuity Equation as Conservation Analogy

**Rank: Important | Heuristic: VG** — The chapter derives the continuity equation ∂_t|ψ|² = −∂_x J and states: "Probability flows like a fluid with current J." It then draws an analogy to mass and charge conservation. This structural identity between classical fluid continuity and quantum probability conservation is a hierarchy/comparison claim that benefits from a two-column schematic showing the two equations' structures side by side.

---

### BLOCK 1 — ILLUSTRAE PASTE BLOCK

Draw a two-column comparison panel. In the left column, show a schematic representing classical fluid flow continuity: a horizontal pipe cross-section with an arrow indicating fluid flowing right (density current J_fluid), with a shaded region of the pipe representing a control volume, and two arrows on either side of the control volume indicating flow in and flow out. Below the pipe, show a density curve (mass density ρ vs. position x) with an arrow indicating that ρ increases where net inflow exceeds outflow. In the right column, show the analogous quantum picture: a position axis with a |ψ|² filled curve and two arrows indicating probability current J flowing in from the left and out to the right of a marked interval. Below the |ψ|² curve, show a small arrow at the interval indicating whether |ψ|² at that interval grows (more current in than out) or decreases (more current out than in). The two columns are connected by a horizontal double-headed equivalence bracket in the center. All shapes are flat vector; no baked text.

---

### BLOCK 2 — FULL SCOPE

- **[S]** Single-column 89 mm, 300 DPI, vector, white background.
- **[C]** Chapter content only. Left column: classical fluid continuity ∂_t ρ + ∂_x J_fluid = 0. Pipe cross-section, control volume, in/out flow arrows, density curve. Right column: quantum probability continuity ∂_t|ψ|² + ∂_x J = 0. |ψ|² curve, interval, probability current arrows, local density change indicator. Central equivalence bracket. No numerical values. No equations baked in.
- **[O]** Two columns side by side. Each column: top schematic (pipe or wave function), bottom density curve with local change indicator. Central column: equivalence connector bracket. Flow arrows use → convention for current direction. ⊣ (blockage) convention not needed here — continuity is about flow balance, not obstruction.
- **[P]** Flat vector. Okabe-Ito. Fluid pipe and flow arrows: Sky Blue #56B4E9. Control volume shading: Sky Blue #56B4E9 at 30% opacity. Fluid density curve: Sky Blue #56B4E9 stroke 1 pt. Quantum |ψ|² curve: Blue #0072B2 at 50% opacity fill, Blue #0072B2 stroke 1 pt. Probability current arrows: Bluish Green #009E73 (active flow). Local increase indicator: Bluish Green #009E73. Local decrease indicator: Vermillion #D55E00. Equivalence bracket: Orange #E69F00, 1 pt. Axis rules: Black, 1 pt. NO baked text, NO 3D, NO red-green.
- **[E]** EXCLUSIONS: electromagnetic charge continuity (analogous but not in chapter); mass continuity in 3D (chapter works in 1D only); Noether's theorem derivation; proof that V terms cancel (algebraic step, not a figure); numerical simulation diagnostic context.

---

### BLOCK 3 — NEGATIVE PROMPT

electromagnetic field lines, 3D pipe rendering, vector field map, Noether theorem diagram, potential energy term illustration, charge density coloring, thermodynamic cycle diagram, text labels, words, gibberish letters, titles, captions, decorative borders, realistic textures, drop shadows, gradient backgrounds, photographic elements, dual-headed arrows, hand-drawn styles, human figures, visual clutter, watermarks, red-green color combinations, rainbow color scales, 3D perspective distortion

---

## Figure 4 — Kennard Inequality: σ_x vs. σ_p Hyperbola for the Gaussian Wave Packet

**Rank: Important | Heuristic: PQ** — The chapter states: "σ_x ∝ a; σ_p ∝ 1/a. Narrow the wave packet in space — smaller a — and the momentum spread widens proportionally. The product is locked." A parametric plot of σ_x vs. σ_p as a varies is an explicit PQ figure called out in the chapter text (the chapter description: "parametric plot of σ_x vs σ_p as a varies from 0.2 to 4 nm"). This hyperbola is the Kennard bound made visible; the Gaussian lies exactly on it.

---

### BLOCK 1 — ILLUSTRAE PASTE BLOCK

Draw a line chart with the horizontal axis representing σ_x (position standard deviation) running from 0 to a maximum, and the vertical axis representing σ_p (momentum standard deviation) running from 0 upward, both axes originating at zero. Plot a smooth hyperbolic curve representing σ_p = ℏ/(2 σ_x), the Kennard lower bound. On this curve, place a series of filled dot markers representing the Gaussian wave packet at several values of the width parameter a, confirming that the Gaussian sits exactly on the hyperbola. Shade the region above the hyperbola in a light fill to indicate the allowed region (states with σ_x σ_p ≥ ℏ/2). Leave the region below the hyperbola unfilled (forbidden region). Mark the boundary curve with a distinct line style. No other wave function states are shown. Both axes start at zero. No gridlines, no tick labels, no equation text, no annotations.

---

### BLOCK 2 — FULL SCOPE

- **[S]** Single-column 89 mm, 300 DPI, vector, white background.
- **[C]** Chapter content only. Kennard bound: σ_x σ_p = ℏ/2 (lower bound, equality for Gaussian). Range: a from 0.2 to 4 nm, giving σ_x = a/√2 from ~0.14 nm to ~2.83 nm and σ_p = ℏ/(√2 a) accordingly. Gaussian dots sit on the hyperbola. Shaded region above the curve is the allowed region. No other wave functions (infinite well states are discussed in exercises but not in chapter body as a figure candidate).
- **[O]** Single panel. Horizontal axis: σ_x, origin at zero, runs right. Vertical axis: σ_p, origin at zero, runs up. Hyperbolic boundary curve. Filled dot markers on curve (5–7 evenly spaced in a). Shaded allowed region above curve. Forbidden region below curve (white, no fill). No secondary axes.
- **[P]** Flat vector. Okabe-Ito. Hyperbolic boundary curve: Blue #0072B2, 1.5 pt stroke. Gaussian dot markers: Bluish Green #009E73 filled, 1 pt stroke (active — the Gaussian is the special state that saturates the bound). Allowed region fill: Sky Blue #56B4E9 at 20% opacity. Forbidden region: white (no fill). Axis rules: Black, 1 pt. NO baked text, NO 3D, NO red-green.
- **[E]** EXCLUSIONS: infinite-well state points (not in chapter body, only in exercises); Robertson generalization (cited but not the chapter's focus); measurement-disturbance relation (chapter explicitly distinguishes this from the Kennard inequality; mixing them in the same figure would recreate the "most persistent conceptual error" the chapter warns against); time-energy uncertainty relation; any comparison hyperbola for ℏ (as opposed to ℏ/2).

---

### BLOCK 3 — NEGATIVE PROMPT

infinite well state scatter points, measurement disturbance relation curve, second bounding hyperbola, time-energy axes, Robertson generalization annotation, error ellipse overlay, 3D surface plot, log-scale axes, axis tick number labels, equation text overlay, legend text box, hatching in allowed region, text labels, words, gibberish letters, titles, captions, decorative borders, realistic textures, drop shadows, gradient backgrounds, photographic elements, dual-headed arrows, hand-drawn styles, human figures, visual clutter, watermarks, red-green color combinations, rainbow color scales, 3D perspective distortion

---

## Video Candidate Pass

**Figure 1 — |ψ|² as Probability Density**
STATIC SUFFICIENT. The density-vs-probability distinction is a structural comparison between a value at a point and an area under a curve. This is a snapshot argument; no temporal process is involved.

**Figure 2 — Re ψ, Im ψ, and |ψ|² Three-Panel Stack**
VIDEO CANDIDATE. This is the chapter's recommended video figure. The chapter explicitly references an interactive simulation ("you dragged a slider and the blue shape spread") and notes that Re ψ and Im ψ oscillate while |ψ|² does not. Animating the wave packet as k₀ increases — watching Re ψ and Im ψ spin faster while |ψ|² remains a smooth Gaussian — demonstrates in real time that momentum is encoded in the phase relationship between the two components, not in the density. The phase relationship between Re ψ and Im ψ is dynamic content. Criterion: PQ + VG where the key claim is about a phase relationship that is more naturally shown as motion than as a frozen curve. One-line reason: the quarter-cycle lag between Re ψ and Im ψ is a time-like relationship — showing it as motion makes the independence of |ψ|² from k₀ viscerally surprising.

**Figure 3 — Normalization as Area / Continuity Equation Analogy**
STATIC SUFFICIENT. A structural analogy between two equations is a fixed two-column comparison. The parallel structure is grasped immediately from a still; no sequential process unfolds.

**Figure 4 — Kennard Inequality Hyperbola**
STATIC SUFFICIENT. A parametric hyperbolic curve is a fixed geometric object. The trade-off between σ_x and σ_p is fully communicated by the shape of the curve and the dot markers sitting on it; no temporal unfolding is needed.
