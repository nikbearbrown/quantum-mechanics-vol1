# CAJAL Figure Report — Chapter 11 — Capstone: A 1D Quantum Sandbox

Recommended: 4 figures, Mixed density.

Chapter 11 is a methods-and-validation chapter. Its visual demands are architectural and comparative rather than quantitative-curve-heavy. Four heuristics fire distinctly. The 1D solver architecture is a VG/MC heuristic: two operational modes (eigensolver and time-evolution) sharing an infrastructure of arrays, grids, and boundary conditions — a systems diagram with data-flow structure. The numerical method choice (Numerov vs. matrix diagonalization vs. split-step Fourier) is a comparison-panels heuristic with a shared criterion axis (accuracy, cost, suitability by use case): three methods, five criteria, and two explicit chapter verdicts (Numerov first; matrix for full spectrum; split-step for free-space/periodic). The validation loop against the infinite-square-well analytic spectrum is a PQ heuristic: six plotted numerical points against an analytic n² curve — quantitative agreement made visual. The build-and-defend workflow is an MC heuristic: a five-stage sequential process (construct H → diagonalize → normalize → validate → display) whose stages are causally ordered and must not be reordered. A fifth candidate — the FFT k-grid wrapping diagram embedded as a comment placeholder in the chapter source — is confirmed by the chapter's own comment tag (`<!-- → [FIGURE: diagram of the FFT output index mapping...] -->`) and fires as a VG heuristic; it is included as Figure 5. The scaling-ladder infographic embedded as a comment placeholder at the chapter's end is an annotated hierarchy (VG), but its content (2D quantum dots, hydrogen atom, helium, DFT) lies outside this volume's scope — it is marked Supplementary and described but not ranked Critical or Important.

---

## Figure 1 — 1D Solver Architecture: Two Modes on Shared Infrastructure

**Heuristic:** VG + MC (structural data-flow with two operational branches sharing a common grid infrastructure)
**Rank:** Critical

### BLOCK 1 — ILLUSTRAE PASTE BLOCK

Draw a systems diagram in a top-down or left-to-right layout with three zones. The top zone contains the shared infrastructure: a grid-points block connected by arrows to a wave-function array block and a potential array block. The middle zone splits into two parallel branches. The left branch represents the eigensolver mode: a block for constructing the tridiagonal Hamiltonian matrix, connected downward to a block for diagonalization (calling eigs), connected downward to a normalization block, connected downward to an output block showing energy levels as horizontal lines. The right branch represents the time-evolution mode: a block for choosing a time stepper, connected downward to a single-step propagation block, connected downward by a looping arrow back to itself (indicating iteration), with an output block showing probability density frames. A horizontal dashed line separates the shared infrastructure zone from the two branch zones. All blocks are rectangles. Arrows connecting the infrastructure blocks to both branches are solid and fork from a single node. The diagram must be blank and unannotated — no text labels baked in.

### BLOCK 2 — FULL SCOPE

**[S]** Single-column 89 mm, 300 DPI, vector, white background.

**[C]** All elements from chapter text. Shared infrastructure (chapter: "Both modes run on the same infrastructure"): N uniformly spaced grid points xⱼ; complex-valued array of length N for ψ; real-valued array of length N for V(x). Eigensolver branch (chapter section "The Eigensolver: TISE as a Matrix Problem"): construct tridiagonal H (diagonal 2tₖ + Vⱼ, off-diagonal −tₖ); diagonalize (math.eigs or Numerov shoot); normalize (divide by √h); output energy levels and eigenfunctions. Time-evolution branch (chapter sections "Crank-Nicolson" and "Split-Step Fourier"): choose stepper (CN or split-step); propagate ψ one step; loop; output |Ψ(t)|² animation. The fork from shared infrastructure to both branches is the chapter's central organizational claim. The loop arrow on the time-evolution propagation block represents the animation loop. No numerical values embedded.

**[O]** Three-zone vertical layout. Top zone (shared infrastructure): three blocks in a horizontal row — grid block, ψ-array block, V-array block — connected by horizontal arrows, all feeding downward into a fork node. Fork node: single circle from which two arrows diverge left-downward (eigensolver) and right-downward (time evolution). Left branch: four stacked blocks (construct H → diagonalize → normalize → output). Right branch: three stacked blocks (choose stepper → propagate one step → output), with a backward-looping arrow from the propagation block back to itself. Output blocks for both branches: slightly wider than the method blocks, lighter fill. Horizontal dashed separator line between top zone and branch zones. All arrows single-headed, 1 pt.

**[P]** Flat vector, Okabe-Ito palette, 1 pt strokes, white background, no baked text. Shared infrastructure blocks: Blue #0072B2 fill at 15% opacity, Blue #0072B2 stroke (dominant — the foundation). Fork node: Blue #0072B2 filled circle. Eigensolver branch blocks: Bluish Green #009E73 fill at 15% opacity, Bluish Green #009E73 stroke (active — the primary mode for this capstone). Time-evolution branch blocks: Orange #E69F00 fill at 15% opacity, Orange #E69F00 stroke (secondary — the second mode). Loop-back arrow on time-evolution: Orange #E69F00, 0.75 pt, dashed arc. Output blocks (both branches): Sky Blue #56B4E9 fill at 15% opacity, Sky Blue #56B4E9 stroke (anchor — the displayed result). Horizontal dashed separator: neutral gray #AAAAAA, 0.5 pt. Connecting arrows: neutral gray #666666, 1 pt, single-headed.

**[E]** EXCLUSIONS: do not show the Thomas algorithm or QR algorithm as sub-blocks — the chapter treats math.eigs as a single call; do not show 2D or periodic extensions of the solver — this chapter is 1D only; do not show the simulation UI layout (that is the deliverable, not the architecture diagram); do not show boundary condition enforcement as a separate block — it is part of H construction; do not show the validation benchmark as part of this diagram — that is Figure 3.

### BLOCK 3 — NEGATIVE PROMPT

UML class diagram notation, database entity-relationship format, UI wireframe mockup of the HTML interface, 3D pipeline diagram, circular flowchart, swim-lane format with labeled actor rows, text labels, words, gibberish letters, titles, captions, decorative borders, realistic textures, drop shadows, gradient backgrounds, photographic elements, dual-headed arrows, hand-drawn styles, human figures, visual clutter, watermarks, red-green color combinations, rainbow color scales, 3D perspective distortion

---

## Figure 2 — Numerical Method Comparison: Numerov vs. Matrix Diagonalization vs. Split-Step

**Heuristic:** PQ + VG (three methods on five shared criteria — comparison panels with shared axis)
**Rank:** Important

### BLOCK 1 — ILLUSTRAE PASTE BLOCK

Draw a matrix-style grid of filled cells arranged as three columns and five rows. The three columns correspond to three numerical methods. The five rows correspond to five evaluation criteria. Each cell contains a shaded fill whose intensity encodes a qualitative rating — dark fill for favorable, light fill for unfavorable, medium fill for intermediate. The cell for each method-criterion combination is a filled rectangle. A vertical colored stripe at the top of each column encodes the method identity by color, with no text. A horizontal stripe on the left of each row encodes the criterion identity by position but not text. The overall shape is a compact rectangular grid with visible cell borders. A small checkmark glyph (a simple tick symbol, not text) appears inside cells designated as the chapter's recommended method for a given use case. The diagram must be blank and unannotated — no text labels baked in.

### BLOCK 2 — FULL SCOPE

**[S]** Single-column 89 mm, 300 DPI, vector, white background.

**[C]** Three methods from chapter text: Numerov shooting (column 1), matrix diagonalization via math.eigs (column 2), split-step Fourier (column 3). Five criteria from chapter text: (1) accuracy per grid point — Numerov O(h⁶) favorable, matrix O(h²) moderate, split-step spectral in space favorable; (2) finds all eigenvalues at once — Numerov unfavorable (one at a time), matrix favorable (all at once), split-step N/A (time-evolution, not eigensolver); (3) requires linear algebra library — Numerov favorable (arithmetic only), matrix unfavorable (requires math.eigs), split-step requires FFT (moderate); (4) suitable for hard-wall boundary conditions — Numerov favorable (natural shooting), matrix favorable (Dirichlet direct), split-step unfavorable (designed for periodic/free-space); (5) suitable for free-space/large periodic domain — Numerov moderate, matrix moderate, split-step favorable. The chapter's two explicit recommendations: "For this capstone, start with Numerov" and "For twenty or more states, load the library" — these are the checkmark cells: Numerov recommended for criterion 1 and 4 (accuracy and hard-wall); matrix recommended for criterion 2 (all eigenvalues at once); split-step recommended for criterion 5 (free-space). All ratings derived directly from chapter text.

**[O]** Five-row by three-column grid. Cell size: approximately 14 mm wide × 7 mm tall. Column header stripe: 3 mm tall colored bar above the three columns. Row label zone: 3 mm wide neutral-gray stripe at left of grid (text labels added by illustrator in production). Cell fill: three levels — favorable (60% opacity of method's column color), moderate (30% opacity), unfavorable (light gray #DDDDDD). Checkmark glyph: simple tick inside recommended cells, 1 pt stroke, same color as column header. Grid cell borders: 0.5 pt neutral gray. Outer border of full grid: 1 pt neutral gray.

**[P]** Flat vector, Okabe-Ito palette, 1 pt strokes, white background, no baked text. Column 1 (Numerov): Bluish Green #009E73 header stripe; favorable cells: #009E73 at 60% opacity; moderate: 30%; unfavorable: gray. Column 2 (matrix diagonalization): Blue #0072B2 header stripe; favorable cells: #0072B2 at 60% opacity; moderate: 30%; unfavorable: gray. Column 3 (split-step Fourier): Orange #E69F00 header stripe; favorable cells: #E69F00 at 60% opacity; moderate: 30%; unfavorable: gray. Checkmark glyphs: same color as column header, 1 pt stroke. Row stripe at left: neutral gray #BBBBBB, no color encoding — position only. Grid borders: #AAAAAA, 0.5 pt interior; 1 pt outer.

**[E]** EXCLUSIONS: do not show quantitative error formulas inside cells — the cell fill encodes qualitative rating only; do not show the Crank-Nicolson method as a fourth column — the chapter subordinates it to split-step in the method comparison and treats it as an implementation of the time-evolution stepper rather than a competing eigensolver; do not show a bar chart with quantitative accuracy numbers — the chapter gives the error formula in prose and exercise 9, but the method comparison in the main text is qualitative; do not show a decision tree or flowchart for method selection — that is Figure 4; do not show more than three methods and five criteria.

### BLOCK 3 — NEGATIVE PROMPT

radar/spider chart for method comparison, bar chart with quantitative accuracy values, decision flowchart format, Venn diagram, table with typography-only cells (no fill encoding), heat map with rainbow colorscale, text labels, words, gibberish letters, titles, captions, decorative borders, realistic textures, drop shadows, gradient backgrounds, photographic elements, dual-headed arrows, hand-drawn styles, human figures, visual clutter, watermarks, red-green color combinations, rainbow color scales, 3D perspective distortion

---

## Figure 3 — Validation Loop: Numerical Eigenvalues vs. Analytic n² Spectrum

**Heuristic:** PQ (quantitative agreement between discrete numerical points and analytic n² curve, y-axis from zero)
**Rank:** Critical

### BLOCK 1 — ILLUSTRAE PASTE BLOCK

Draw a single-panel line-and-scatter chart. The horizontal axis represents the mode number n, running from 1 to at least 5. The vertical axis represents the ratio of each eigenvalue to the ground-state eigenvalue, starting at zero. Draw a smooth parabolic reference curve rising from the value 1 at n = 1 through 4 at n = 2, 9 at n = 3, 16 at n = 4, and 25 at n = 5 — this is the analytic n² law. On the same axes, plot five discrete filled circles, one at each integer n from 1 to 5, placed at the y-value corresponding to the numerically computed ratio. The circles should fall visually on or extremely close to the parabolic curve. Below the horizontal axis, a small inset zone shows five short vertical tick marks at n = 1 through 5 with no labels. Above the parabola at n = 5, draw a small bracket indicating the gap between the parabola and a hypothetical second curve at a higher level (representing where the numerical points would land if the method had a large systematic error) — this bracket is empty and indicates the validation target zone. The diagram must be blank and unannotated — no text labels baked in.

### BLOCK 2 — FULL SCOPE

**[S]** Single-column 89 mm, 300 DPI, vector, white background.

**[C]** All values from chapter text. Analytic curve: Eₙ/E₁ = n², a parabola passing through (1,1), (2,4), (3,9), (4,16), (5,25). Numerical points: five filled circles at (n, Eₙ_numerical/E₁_numerical) for n = 1 through 5, with N = 500, L = 2 nm, m = mₑ — the chapter specifies these as the validation parameters. The chapter states: "The error should be below 10⁻⁵ for n = 1 and below 1% for n = 10 with N = 500." At this accuracy the numerical circles are visually indistinguishable from the parabola at the printed scale — they should be plotted exactly on the parabola in the figure, as the validation goal is agreement. A secondary element: the chapter's ratio test is that E₂/E₁ = 4.000, E₃/E₁ = 9.000 — these are dimensionless checks. Y-axis: ratio Eₙ/E₁ from 0 to 26. X-axis: n from 0 to 6 (with values plotted at n = 1 through 5). Y-axis starts at zero — no exceptions. The parabola is smooth (continuous curve), not a connect-the-dots line.

**[O]** Single panel. Smooth parabolic reference curve from (0,0) through (5,25): 1.5 pt solid line. Five discrete filled circle markers at n = 1, 2, 3, 4, 5 on or very near the parabola: 5 pt diameter, filled. Horizontal grid lines at y = 0, 4, 9, 16, 25 (the exact analytic values): light gray, 0.25 pt dashed. Vertical grid lines at n = 1, 2, 3, 4, 5: light gray, 0.25 pt dashed. Y-axis tick marks at 0, 4, 9, 16, 25. X-axis tick marks at n = 1 through 5. Validation bracket at n = 5: small vertical bracket from y = 25 to y = 25.5 indicating the 1% error window — bracket width 2 pt, ends capped. Y-axis from zero.

**[P]** Flat vector, Okabe-Ito palette, 1 pt strokes, white background, no baked text. Analytic parabola: Blue #0072B2, 1.5 pt solid (dominant — the exact known result). Numerical marker circles: Bluish Green #009E73 filled circles, 5 pt (active — the numerical computation agrees with analytic). Grid lines: neutral gray #DDDDDD, 0.25 pt dashed. Axis lines: neutral gray #888888, 0.5 pt. Tick marks: neutral gray, 0.5 pt. Validation bracket at n = 5: Orange #E69F00, 1 pt (secondary — the tolerance window). Horizontal reference lines at exact squares: neutral gray #CCCCCC, 0.25 pt dotted.

**[E]** EXCLUSIONS: do not plot fractional error as a second panel or second y-axis — the chapter presents the ratio test and the absolute comparison separately; do not show all N − 2 eigenvalues — five modes only, as the chapter specifies; do not show the Numerov accuracy curve as a separate series — this figure is about the validation result, not method comparison (that is Figure 2); do not show experimental data points alongside numerical points — this is a computation vs. analytic benchmark, not an experiment; do not use a log-log scale — the n² scaling is clear on a linear-linear plot for n = 1 through 5.

### BLOCK 3 — NEGATIVE PROMPT

log-log scale axes, multiple method series on the same panel, fractional-error bar chart inset, experimental data markers, connect-the-dots jagged line instead of smooth parabola, zero-suppressed y-axis, scatter points without reference curve, text labels, words, gibberish letters, titles, captions, decorative borders, realistic textures, drop shadows, gradient backgrounds, photographic elements, dual-headed arrows, hand-drawn styles, human figures, visual clutter, watermarks, red-green color combinations, rainbow color scales, 3D perspective distortion

---

## Figure 4 — FFT k-Grid: Output Index to Physical Wave Vector Mapping

**Heuristic:** VG (structural spatial claim — the wrapping of FFT indices N/2 through N−1 to negative wave vectors)
**Rank:** Important

### BLOCK 1 — ILLUSTRAE PASTE BLOCK

Draw a horizontal number line representing FFT output indices running from 0 on the left to N−1 on the right, with a visible midpoint at N/2. Above this number line, draw a second horizontal axis representing physical wave vectors, running from a large negative value on the left through zero in the center to a large positive value on the right. Connect each index position to its corresponding physical wave vector with a curved arc or a vertical line segment that bends: index 0 maps to k = 0 (vertical, straight); indices 1 through N/2−1 map to progressively larger positive k values (arcs curving upward to the right half of the wave vector axis); index N/2 maps to the most negative k value on the left end of the wave vector axis (a long arc that crosses the center); indices N/2+1 through N−1 map to negative k values progressively approaching zero (arcs curving upward to the left half of the wave vector axis). Use color to distinguish the positive-k mapping region (indices 0 through N/2−1) from the negative-k mapping region (indices N/2 through N−1). Mark the midpoint at N/2 with a vertical dashed dividing line on the index axis. The diagram must be blank and unannotated — no text labels baked in.

### BLOCK 2 — FULL SCOPE

**[S]** Single-column 89 mm, 300 DPI, vector, white background.

**[C]** The chapter's exact formula: kₘ = (2π/Nh) × m for m < N/2; kₘ = (2π/Nh) × (m − N) for m ≥ N/2. For concreteness, draw for N = 8 (the exercise uses N = 8 explicitly): indices 0, 1, 2, 3 map to k = 0, +Δk, +2Δk, +3Δk (positive k, leftward indices); indices 4, 5, 6, 7 map to k = −4Δk, −3Δk, −2Δk, −Δk (negative k, rightward indices). The visual claim: the second half of the FFT output (indices 4–7 for N = 8) wraps to negative wave vectors, and using the raw index m as if it were k gives the wrong (positive) k for every negative-momentum component. The chapter states: "the second half of the FFT output corresponds to negative wave vectors" and the fix is the five-line sign-flip formula. The mapping must make this wrap-around geometrically obvious. The chapter uses N = 8 in Exercise 5 — draw for N = 8 specifically.

**[O]** Two horizontal axes, stacked vertically with a gap of 15 mm between them. Bottom axis: FFT output index axis, 0 through 7 (for N = 8), left to right, evenly spaced. Vertical dashed dividing line at index m = 4 (the N/2 boundary). Top axis: physical wave vector axis, −4Δk through +3Δk, with zero at center, positive right, negative left. Mapping connectors: curved arcs from each index tick mark on the bottom axis to the corresponding k-value tick mark on the top axis. Each arc starts at the index position and ends at the k-axis position. Arcs for indices 0–3 curve upward and land on the positive-k right half of the top axis. Arcs for indices 4–7 curve upward and land on the negative-k left half of the top axis — these arcs cross the center line of the top axis, making the wrap-around visible. No crossing arcs for the positive-k group; crossing is only in the negative-k group. Both axes the same length. Tick marks at each integer position on both axes.

**[P]** Flat vector, Okabe-Ito palette, 1 pt strokes, white background, no baked text. Bottom index axis: neutral gray #888888, 1 pt. Top k-vector axis: neutral gray #888888, 1 pt. Positive-k mapping connectors (indices 0–3 → right half of k-axis): Bluish Green #009E73, 1 pt solid arcs (active — these map correctly under the raw-index formula). Negative-k mapping connectors (indices 4–7 → left half of k-axis): Vermillion #D55E00, 1 pt solid arcs (negative/blocking — these are the wrap-around indices that require the sign-flip correction). Vertical dashed dividing line at N/2 = 4: Orange #E69F00, 1 pt dashed (secondary — the boundary between the two regimes). Zero-crossing mark on k-axis: Blue #0072B2, 1 pt vertical tick (dominant — the k = 0 reference). Tick marks: matching color of their axis, 0.5 pt.

**[E]** EXCLUSIONS: do not show a specific numerical example with labeled kₘ values in eV/nm or Hz — the diagram is structural (the mapping pattern), not a lookup table; do not show the kinetic phase e^(−iℏk²Δt/2m) as an expression inside the diagram; do not extend to N = 500 (the production grid size) — N = 8 makes the pattern readable; do not show the FFT algorithm butterfly diagram; do not show time-domain and frequency-domain as separate vertical columns — this is specifically the index-to-k mapping, not a general FFT concept diagram; do not show the wrong mapping (using raw index m as k) as a second overlaid arc set — the Vermillion arcs crossing to the negative-k side already encode the wrap-around that must be corrected.

### BLOCK 3 — NEGATIVE PROMPT

FFT butterfly algorithm diagram, DFT complex plane Argand diagram, spectrogram time-frequency plot, raw-index-as-k overlaid comparison arcs, N=500 grid with illegible fine structure, kinetic phase formula as graphical overlay, text labels, words, gibberish letters, titles, captions, decorative borders, realistic textures, drop shadows, gradient backgrounds, photographic elements, dual-headed arrows, hand-drawn styles, human figures, visual clutter, watermarks, red-green color combinations, rainbow color scales, 3D perspective distortion

---

## Video Candidate Pass

**Figure 1 — 1D Solver Architecture:** STATIC SUFFICIENT. Criterion: the systems diagram is a reference architecture — the two branches and shared infrastructure are a structural fact the student reads once and returns to. There is no temporal sequence to animate; the eigensolver and time-evolution branches are parallel alternatives, not sequential stages. The diagram is a navigation aid, not a process demonstration.

**Figure 2 — Method Comparison Grid:** STATIC SUFFICIENT. Criterion: a criterion-by-method comparison matrix is a reference table. The student uses it to look up which method to choose for a given need. No transformation unfolds; the comparison is static. Animation would add nothing to the comparative-lookup function.

**Figure 3 — Validation Spectrum:** STATIC SUFFICIENT. Criterion: five discrete points against an analytic curve is a result-comparison figure, not a process. The student reads it once to confirm the solver is correct. The chapter's own simulation exercise provides the dynamic version (the student runs the solver and produces the table themselves). The figure is the reference for what correct output looks like.

**Figure 4 — FFT k-Grid Mapping:** VIDEO CANDIDATE. Criterion: the wrap-around of FFT indices to negative wave vectors is a transformation that is extremely common to get wrong and difficult to understand from a static diagram alone. A 10-second animation that highlights indices 0 through N/2−1 one by one (each arc lighting up green as it maps to its correct positive-k position), then pauses at the N/2 boundary, then shows indices N/2 through N−1 one by one (each arc lighting up vermillion as it maps to its negative-k position, crossing the zero line to the left half) would make the wrap-around kinematically vivid. The chapter devotes a full paragraph to this "mandatory detail" and calls it "the single most common implementation error." RECOMMENDED VIDEO.
