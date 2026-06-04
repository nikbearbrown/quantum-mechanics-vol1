# CAJAL Figure Report — Chapter 9 — Operators and Uncertainty

Recommended: 4 figures, High density.

Chapter 9 has four figure-worthy claims: the commutator-incompatibility contrast (VG — classical point in phase space versus quantum eigenfunctions), the Fourier-duality diagram linking position and momentum representations (VG — structural/spatial architecture), the expectation value as a weighted average over |ψ|² (PQ — probability density with centroid marker), and the Robertson boundary hyperbola with states plotted as points (PQ — the central quantitative result of the chapter). The embedded chapter comment for an operator table (classical versus quantum observable) is a typography/layout item, not a figure. The Fourier duality diagram is an embedded comment in the chapter text, explicitly flagged. The canonical commutator derivation is a calculation, not a structural visual; the MC heuristic fires at the level of compatible-versus-incompatible observables as a conceptual contrast, not as a process flow. Four figures are the right count. One figure (the Robertson hyperbola) is the chapter's quantitative centerpiece and would anchor the worked calculation visually; the others are structural/pedagogical supports.

---

## Figure 1 — Classical Phase Space vs. Quantum Hilbert Space: Compatible and Incompatible Observables

**Heuristic:** VG (structural spatial claim — a classical state occupies a point in phase space where x and p are simultaneously definite; quantum eigenstates of x and p are mutually incompatible)
**Rank:** Critical

### BLOCK 1 — ILLUSTRAE PASTE BLOCK

Draw two panels side by side. In the left panel, draw a two-dimensional coordinate plane with a horizontal axis and a vertical axis. Place a single filled dot at one interior position in this plane — this represents a classical state that simultaneously has definite position and definite momentum. In the right panel, draw two sub-panels stacked vertically within the same panel boundary. In the upper sub-panel, draw a tall narrow spike centered on the horizontal position axis, reaching sharply upward and falling immediately back to the baseline on both sides — this represents a position eigenstate, a Dirac delta concentrated at one point in position. In the lower sub-panel, draw a sinusoidal wave of uniform amplitude extending across the full width of the sub-panel without any decay — this represents a momentum eigenstate, a plane wave that fills all of space. Connect the two sub-panels with a horizontal double-headed divider showing they are alternatives, not simultaneous possibilities. The diagram must be blank and unannotated — no text labels baked in.

### BLOCK 2 — FULL SCOPE

**[S]** Single-column 89 mm, 300 DPI, vector, white background.

**[C]** Left panel (classical phase space): a two-dimensional plot with position on horizontal axis and momentum on vertical axis. A single dot at an interior location represents the classical state (x₀, p₀) — simultaneous definiteness is possible. The chapter states explicitly: "In classical mechanics, position and momentum Poisson-commute: {x,p} = 1, no incompatibility." The dot is the visual encoding of this statement. Right panel (quantum Hilbert space): two alternative quantum states shown as spatial wave functions in position representation. Upper right: position eigenstate — a Dirac delta spike at one location, representing zero uncertainty in position (δ(x − x₀)), corresponding to infinite momentum spread (not shown — the contrast with the plane wave below conveys this). Lower right: momentum eigenstate — plane wave e^(ik₀x), sinusoidal, uniform amplitude across all space, representing definite momentum and infinite position uncertainty. A horizontal divider with a blocking symbol between the two right sub-panels encodes "no state can be both." Chapter text: "Any state with definite position (a Dirac delta in x) is infinitely spread in momentum; any state with definite momentum (a plane wave) is infinitely spread in position. The incompatibility is algebraic, baked into the operators themselves."

**[O]** Two main panels side by side with a thin vertical separator. Left panel occupies roughly 40% of the total width; right panel occupies 60%, divided horizontally into two equal sub-panels. Left panel: standard x-p axes (orthogonal, equal length), a single filled dot at (x₀, p₀), axis arrows, tick marks. Right panel upper sub-panel: horizontal position axis, a single sharp spike (Dirac delta profile) centered at one position, height 3–4× the visible axis range, peak width approximately 1/20 of the panel width — this extreme aspect ratio encodes the "concentrated at one point" claim. Right panel lower sub-panel: horizontal position axis, sinusoidal wave of constant amplitude extending edge-to-edge, amplitude approximately 1/3 of sub-panel height. Horizontal divider between sub-panels: double horizontal line with a small blocking symbol (a bar or X) in the center, 1 pt. Outer panel separator: thin vertical rule, 0.5 pt.

**[P]** Flat vector, Okabe-Ito palette, 1 pt strokes, white background, no baked text. Left panel axes: light gray 0.5 pt. Classical state dot: Blue #0072B2 (dominant), filled, 5 pt diameter. Position eigenstate spike: Bluish Green #009E73 (active — the focused/definite state), 2 pt stroke, filled triangle or sharp Gaussian peak. Plane wave: Orange #E69F00 (secondary — the momentum eigenstate), 1.5 pt sinusoidal. Blocking symbol between right sub-panels: Vermillion #D55E00 (negative), 1.5 pt. Right panel sub-panel divider lines: neutral gray #CCCCCC, 0.5 pt.

**[E]** EXCLUSIONS: do not show the commutator algebra as a bracket symbol in the visual — this is a structural contrast figure, not a formula illustration; do not show three or more states in the right panel; do not show a wave packet in the right panel — it is reserved for Figure 3 (the Robertson boundary); do not show probability density |ψ|² as a separate curve alongside each eigenstate; do not show a Wigner function or phase-space quasi-probability distribution; do not add a third panel for the Gaussian (minimum-uncertainty) state — that belongs to Figure 4.

### BLOCK 3 — NEGATIVE PROMPT

Wigner quasi-probability distribution contours, Husimi Q function heatmap, 3D phase-space surface, rainbow probability colormap, Bloch sphere, path-integral diagram, uncertainty ellipse overlaid on phase space, text labels, words, gibberish letters, titles, captions, decorative borders, realistic textures, drop shadows, gradient backgrounds, photographic elements, dual-headed arrows, hand-drawn styles, human figures, visual clutter, watermarks, red-green color combinations, rainbow color scales, 3D perspective distortion

---

## Figure 2 — Fourier Duality: Position Space and Momentum Space Representations

**Heuristic:** VG (structural diagram — the bidirectional Fourier transform relationship between ψ(x) and φ(p), and the dual role of the operators)
**Rank:** Important

### BLOCK 1 — ILLUSTRAE PASTE BLOCK

Draw two rectangular boxes arranged side by side at the same horizontal level, with a gap between them. In the left box, draw a small bell-shaped curve sitting on a horizontal axis — this represents a wave function in position space. Below the curve, indicate two elements: a horizontal axis labeled with the position coordinate, and a small differential operator symbol suggesting a derivative acting on the function. In the right box, draw a similar bell-shaped curve on a horizontal axis — this represents the same wave function in momentum space. Below that curve, indicate a horizontal axis for the momentum coordinate and a small multiplicative symbol suggesting that the momentum operator is multiplication by the coordinate value. Between the two boxes, draw two horizontal arrows: one pointing from the left box to the right box, and one pointing from the right box to the left box. The two arrows are distinct — they run at slightly different heights or are colored differently — representing the forward Fourier transform and its inverse. The diagram must be blank and unannotated — no text labels baked in.

### BLOCK 2 — FULL SCOPE

**[S]** Single-column 89 mm, 300 DPI, vector, white background.

**[C]** Two representations: position space (ψ(x), operator −iℏ∂_x) and momentum space (φ(p), operator ×p). The chapter states: "In momentum space, p̂ is multiplication by p. In position space, it is differentiation. The Fourier transform connects the two representations." The forward transform takes ψ(x) → φ(p); the inverse takes φ(p) → ψ(x). Each box shows the wave function representation (a Gaussian bell curve is appropriate as a concrete, symmetric example — the Gaussian is both position-space and momentum-space Gaussian) and indicates the operator form in that space. The operator indication is purely visual: in the position-space box, a differential operator icon (a curved arrow suggesting derivative action); in the momentum-space box, a multiplication icon (a dot product symbol or small scale indicator). These operator icons are the structural claim: the same physical observable p̂ has two distinct mathematical forms depending on which space you work in. The connection is the pair of Fourier arrows.

**[O]** Two boxes of equal size, horizontally centered in the figure, separated by a gap of approximately 30% of the box width. Each box: outer rectangle with rounded corners, 1 pt stroke; internal bell-curve shape (Gaussian profile) occupying roughly 50% of the box height, sitting on a baseline; a small operator icon below the bell curve (derivative curl for position space, dot-multiplication for momentum space). Between the boxes: two arrows, one from left-box right edge to right-box left edge (forward transform), one from right-box left edge to left-box right edge (inverse transform). Arrows are offset vertically so they do not overlap — forward arrow slightly above center, inverse arrow slightly below center. Arrow style: 1.5 pt solid line with filled arrowhead. No axis lines visible outside the boxes — this is an architectural diagram, not a chart.

**[P]** Flat vector, Okabe-Ito palette, 1 pt strokes, white background, no baked text. Position-space box border: Blue #0072B2 (dominant), 1 pt. Position-space bell curve: Blue #0072B2 fill at 40% opacity, stroke 1.5 pt. Momentum-space box border: Bluish Green #009E73 (active), 1 pt. Momentum-space bell curve: Bluish Green #009E73 fill at 40% opacity, stroke 1.5 pt. Forward Fourier transform arrow (left to right): Orange #E69F00 (secondary), 1.5 pt, filled arrowhead pointing right. Inverse Fourier transform arrow (right to left): Sky Blue #56B4E9 (anchor), 1.5 pt, filled arrowhead pointing left. Operator icon in position box: Blue #0072B2, 1 pt. Operator icon in momentum box: Bluish Green #009E73, 1 pt.

**[E]** EXCLUSIONS: do not show the energy operator or Hamiltonian — this figure is exclusively about the x-p duality; do not show the derivation steps of the Fourier transform (no integral symbol, no intermediate steps); do not show the time-domain wave function or its evolution — time is not part of the Fourier-duality structure being illustrated; do not show a third box for energy space or angular momentum; do not show explicit numerical Fourier pairs (sinc vs. rectangle, etc.); do not show the de Broglie relation as a separate element.

### BLOCK 3 — NEGATIVE PROMPT

Frequency-domain bar chart of Fourier coefficients, spectrogram, time-frequency scalogram, 3D Fourier surface, color-coded frequency bins across the bell curve, rainbow colormap, text labels, words, gibberish letters, titles, captions, decorative borders, realistic textures, drop shadows, gradient backgrounds, photographic elements, dual-headed arrows, hand-drawn styles, human figures, visual clutter, watermarks, red-green color combinations, rainbow color scales, 3D perspective distortion

---

## Figure 3 — Expectation Value as Weighted Average over |ψ|²

**Heuristic:** PQ (distribution curve with centroid marker — the expectation value as the first moment of the probability density, y-axis from zero)
**Rank:** Important

### BLOCK 1 — ILLUSTRAE PASTE BLOCK

Draw a single panel with a horizontal position axis beginning at zero on the left and a vertical probability-density axis beginning at zero at the bottom. Plot one smooth bell-shaped curve representing the probability density |ψ(x)|² — the curve rises from near zero on the left, peaks at an interior point, and descends symmetrically back to near zero on the right. The curve does not touch the vertical axis on the left and does not touch the right edge of the panel. Draw a vertical dashed line from the horizontal axis up to the curve at the position of the curve's peak — this marks the expectation value ⟨x⟩. Fill the area under the curve with a solid flat color. Along the horizontal axis, draw a small number of thin vertical lines at different x-positions, each of varying height proportional to the probability density at that point — these represent weighted contributions. At the base of the dashed vertical line, place a small downward triangle marker on the horizontal axis to indicate the centroid position. The diagram must be blank and unannotated — no text labels baked in.

### BLOCK 2 — FULL SCOPE

**[S]** Single-column 89 mm, 300 DPI, vector, white background.

**[C]** The chapter defines ⟨x⟩ = ∫x|ψ|²dx as "the centroid of the probability density." The figure makes this definition geometric: ⟨x⟩ is the first moment — the balance point — of the distribution |ψ|². Use a Gaussian |ψ(x)|² = (1/(σ√(2π))) exp(−(x−x₀)²/(2σ²)) for a representative x₀ not at the axis center — shifting the mean away from the panel center reinforces that ⟨x⟩ is the distribution's property, not the panel's midpoint. Six thin vertical bars at equal horizontal spacing, each with height proportional to |ψ(x)|² at that x — these represent sample weights in the average ⟨x⟩ = ∑ x_i × P(x_i) and encode the "weighted average" interpretation stated in the chapter. The dashed vertical line at x₀ is the geometric centroid, marking ⟨x⟩. Y-axis from zero — mandatory for all PQ figures. This figure encodes the chapter's statement: "For position, ⟨Â⟩ = ∫x|ψ|²dx — the centroid of the probability density."

**[O]** Single panel. Y-axis from zero (probability density in nm⁻¹), x-axis from zero (position in nm). Gaussian bell curve: smooth, with filled area under curve. Six equally spaced thin vertical bars from x-axis to curve height (not colored differently from each other — they serve as a single visual unit indicating discretized weights). Vertical dashed centroid line at x = x₀ (the distribution mean), from x-axis to curve peak. Small filled downward triangle on x-axis at x₀, 3–4 pt, pointing down to x-axis — the centroid pointer. The mean is visibly off-center (shifted right of the panel's horizontal midpoint by approximately 1.5σ) so the centroid is clearly a property of the distribution, not the panel.

**[P]** Flat vector, Okabe-Ito palette, 1 pt strokes, white background, no baked text. Gaussian fill: Sky Blue #56B4E9 at 35% opacity. Gaussian stroke: Blue #0072B2 (dominant), 1.5 pt. Vertical weight bars: Blue #0072B2, 0.75 pt solid, no fill — thin and non-distracting. Centroid dashed line: Bluish Green #009E73 (active — the expectation value, the physically meaningful output), 1.5 pt dashed. Centroid triangle marker on x-axis: Bluish Green #009E73, filled, 4 pt. Y-axis from zero: light gray 0.5 pt. X-axis: light gray 0.5 pt. Light horizontal grid lines: light gray #EEEEEE, 0.25 pt.

**[E]** EXCLUSIONS: do not show ψ(x) (complex wave function) on this figure — only |ψ(x)|², the probability density; do not show the momentum-space distribution φ(p) on the same panel; do not show a second Gaussian for a different state; do not show ⟨x²⟩ or σ_x as a separate marker on this figure (the variance is reserved for Figure 4); do not use a histogram with discrete bins to approximate the Gaussian — use the smooth probability density curve; do not show the integrals themselves or any formula elements baked into the figure.

### BLOCK 3 — NEGATIVE PROMPT

complex wave function phase spiral, split real/imaginary panels, histogram bins instead of smooth curve, two probability densities on same panel, 3D probability surface plot, polar probability diagram, text labels, words, gibberish letters, titles, captions, decorative borders, realistic textures, drop shadows, gradient backgrounds, photographic elements, dual-headed arrows, hand-drawn styles, human figures, visual clutter, watermarks, red-green color combinations, rainbow color scales, 3D perspective distortion

---

## Figure 4 — The Robertson Boundary: σ_xσ_p ≥ ℏ/2 with Gaussian and Infinite-Well States

**Heuristic:** PQ (quantitative distribution — the uncertainty product as a function of σ_x, shown on log-log axes, with specific states as point markers)
**Rank:** Critical

### BLOCK 1 — ILLUSTRAE PASTE BLOCK

Draw a single panel with a horizontal axis for position uncertainty and a vertical axis for momentum uncertainty, both axes beginning at a small positive value and increasing to the right and upward respectively. Draw a smooth decreasing hyperbolic curve — starting high on the left, curving down to the right — that represents the boundary where position uncertainty times momentum uncertainty equals a fixed constant. The forbidden region below and to the left of the curve is shaded in a light color; the allowed region above and to the right is left unshaded or lightly tinted in a contrasting color. Place one filled circular marker directly on the boundary curve — this represents the Gaussian minimum-uncertainty state. Place a second filled circular marker above and to the right of the first, in the allowed region but not on the curve — this represents the infinite-square-well ground state, which satisfies the bound but does not saturate it. Draw a small upward arrow beside the second marker pointing away from the curve to indicate that higher excited states would move further from the boundary. The diagram must be blank and unannotated — no text labels baked in.

### BLOCK 2 — FULL SCOPE

**[S]** Single-column 89 mm, 300 DPI, vector, white background.

**[C]** The Robertson boundary hyperbola: σ_x × σ_p = ℏ/2. Axes: log-log scale, σ_x on horizontal axis (nm), σ_p on vertical axis (ℏ/nm) — log scale is appropriate because the hyperbola σ_p = ℏ/(2σ_x) is a straight line with slope −1 on log-log axes, making the boundary immediately readable. The chapter gives two specific states with exact ratios: Gaussian — σ_xσ_p/(ℏ/2) = 1.000, a point on the boundary curve; infinite-square-well ground state n=1 — σ_xσ_p/(ℏ/2) ≈ 1.136, a point above the boundary. The chapter also states: "As n increases in the well, the point moves further from the boundary." The upward arrow next to the well-state marker encodes this asymptotic behavior (the ratio grows toward π/√3 ≈ 1.814 as n→∞, from exercise 4). The forbidden region σ_xσ_p < ℏ/2 is below the boundary — shaded to signal "physically impossible." The exact numerical values (1.000 and 1.136) and the n→∞ arrow are all directly from chapter text and the worked calculation.

**[O]** Single log-log panel. X-axis: σ_x from ~0.1 nm to ~10 nm, labeled at decade intervals. Y-axis: σ_p from ~0.1 ℏ/nm to ~10 ℏ/nm, labeled at decade intervals. Both axes from their lower limit (no zero on log scale — this is the one PQ exception, since the physical domain for standard deviations is strictly positive). Boundary hyperbola: smooth curve from upper-left to lower-right, 1.5 pt. Forbidden region below/left of hyperbola: light fill. Gaussian marker: filled circle directly on curve at (σ_x₀, ℏ/(2σ_x₀)) for representative σ_x₀ = 1 nm → σ_p = 0.5 ℏ/nm. Infinite-well marker: filled circle at (1.81 nm × scaling, 0.314 ℏ/nm for L=10 nm) — positioned visibly above the boundary. Upward arrow of length ~20% of panel height beside the well marker, pointing away from curve, indicating the direction of increasing n. Both marker circles: 5 pt diameter.

**[P]** Flat vector, Okabe-Ito palette, 1 pt strokes, white background, no baked text. Boundary hyperbola: Blue #0072B2 (dominant), 1.5 pt solid. Forbidden region fill: Vermillion #D55E00 (negative — the excluded zone), at 15% opacity below the boundary curve. Gaussian marker: Bluish Green #009E73 (active — minimum uncertainty, the saturated bound), filled circle, 5 pt. Infinite-well marker: Orange #E69F00 (secondary — above the bound but allowed), filled circle, 5 pt. Upward arrow: Orange #E69F00, 1.5 pt, filled arrowhead. Allowed region above boundary: no fill or very light gray #F5F5F5 at 20% opacity, subtly indicating the valid zone. Axis strokes: light gray 0.5 pt. Log grid lines: light gray #EEEEEE, 0.25 pt.

**[E]** EXCLUSIONS: do not show more than two state markers — the Gaussian and the n=1 well state are the two cases from the worked calculation; do not show the Schrödinger (tighter) bound as a second hyperbola — the chapter mentions it but does not compute it, and adding a second curve risks confusion; do not show a third axis for the uncertainty product σ_xσ_p; do not show the entropic uncertainty bound; do not show individual measurement outcomes as scatter points; do not show the Robertson derivation steps (Cauchy-Schwarz) visually.

### BLOCK 3 — NEGATIVE PROMPT

Wigner function ellipses in phase space, 3D uncertainty surface, error bar overlays, scatter cloud of individual measurement outcomes, second hyperbola for Schrödinger bound (unless explicitly requested), rainbow gradient coloring of the allowed region, text labels, words, gibberish letters, titles, captions, decorative borders, realistic textures, drop shadows, gradient backgrounds, photographic elements, dual-headed arrows, hand-drawn styles, human figures, visual clutter, watermarks, red-green color combinations, rainbow color scales, 3D perspective distortion

---

## Video Candidate Pass

**Figure 1 — Classical Phase Space vs. Quantum Hilbert Space:** STATIC SUFFICIENT. Criterion: the learning target is a structural contrast between two representations — a dot versus two incompatible eigenfunctions. Both sides are static configurations. No temporal sequence, cycle, or causal mechanism is being illustrated. The side-by-side panel is optimal for this comparison.

**Figure 2 — Fourier Duality:** STATIC SUFFICIENT. Criterion: the duality is a bidirectional structural relationship between two representation spaces, not a temporal process. The two-box-with-arrows architecture conveys the relationship in a single static frame.

**Figure 3 — Expectation Value as Weighted Average:** STATIC SUFFICIENT. Criterion: the expectation value is a property of a static state, not a time-evolving quantity. The centroid of |ψ|² is a fixed geometric fact about the distribution. No temporal mechanism benefits from animation here.

**Figure 4 — Robertson Boundary with State Points:** VIDEO CANDIDATE. Criterion: the chapter's simulation task (Task 3 in Part B) explicitly asks students to "step n from 1 to 10 and record the ratio at each n" and watch the dot move on the Robertson plot. A 10–15 second animation showing n increasing from 1 to 10 (or to the classical limit), with the Orange dot on the Robertson log-log plot moving upward and to the right along a visible trajectory away from the boundary, would demonstrate the chapter's claim that "as n increases in the well, the point moves further from the boundary" as a causal dynamic rather than as a static claim. The asymptotic approach to π/√3 ≈ 1.814 could be indicated by a horizontal dashed line that the moving dot approaches but never reaches. RECOMMENDED VIDEO.
