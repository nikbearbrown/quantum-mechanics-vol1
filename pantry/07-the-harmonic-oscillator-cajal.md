# CAJAL Figure Report — Chapter 7 — The Quantum Harmonic Oscillator

Recommended: 4 figures, High density.

Chapter 7 fires all three CAJAL heuristics. PQ fires twice at Critical: the evenly spaced energy spectrum E_n = (n+½)ℏω shown as horizontal levels on a parabolic potential is the chapter's central quantitative result — spacing, zero-point offset, and the parabola shape are all precisely asserted; the Hermite-Gauss eigenfunctions for n=0 through n=3 or n=4 plotted as a stacked comparison panel make the node count rule (n nodes), the growing spread with n, and the evanescent tails visible as a family. MC fires once at Important: the ladder-operator action — a† raises, a lowers, both by exactly ℏω, terminated at the bottom by a₋|0⟩=0 — is a cyclical process with ≥3 interdependent steps (define ground state, apply a†, verify new eigenvalue, apply a₋ to the previous output, verify descent, arrive at floor). VG fires once at Supplementary: the coherent state phase-space orbit (⟨x⟩(t) vs. ⟨p⟩(t) tracing a circle) is a spatial/structural claim. The chapter's own comment marker at line 205 identifies a data table (harmonic oscillator parameters for HCl, N₂, CO, H₂) — this is a clean PQ candidate as a dot-plot rather than a figure, but it ranks Supplementary because the prose makes the comparison without requiring a chart. Four figures are recommended; the diatomic table is treated as a Supplementary figure with low marginal value and not elevated to Critical.

---

## Figure 1 — Equally Spaced Energy Spectrum on the Parabolic Potential

**Heuristic:** PQ (energy levels E_n = (n+½)ℏω as horizontal lines on a parabola; zero-point energy ℏω/2 above classical minimum; uniform spacing ℏω)
**Rank:** Critical

### BLOCK 1 — ILLUSTRAE PASTE BLOCK

Draw a single-panel diagram with a horizontal position axis and a vertical energy axis starting at zero. Draw a smooth upward-opening parabola centered on the position axis — this represents the harmonic potential V(x) = ½mω²x². Inside the parabola, draw six equally spaced horizontal line segments, each extending only as wide as the parabola is at that energy level — these are the energy levels n=0 through n=5. The lowest line segment sits at a small but visible distance above the bottom of the parabola — this is the zero-point energy, not zero. The gap between each consecutive pair of line segments is equal and uniform. Mark the vertical gap between any two adjacent levels with a small bidirectional bracket on the right side of the parabola. Mark the gap between the parabola minimum and the n=0 level with a separate small bracket on the right side below the first level. The line segments do not extend beyond the parabola walls. The diagram must be blank and unannotated — no text labels baked in.

### BLOCK 2 — FULL SCOPE

**[S]** Single-column 89 mm, 300 DPI, vector, white background.

**[C]** Six energy levels: n=0 (E₀=ℏω/2), n=1 (E₁=3ℏω/2), n=2 (E₂=5ℏω/2), n=3 (E₃=7ℏω/2), n=4 (E₄=9ℏω/2), n=5 (E₅=11ℏω/2). Uniform spacing: ΔE = ℏω between every consecutive pair — the central quantitative claim of the chapter. Zero-point energy: E₀ = ℏω/2 above the parabola minimum (V=0 at x=0) — chapter states this explicitly: "Not zero — ℏω/2." Energy axis starts at V=0 (parabola minimum), runs up to just above E₅. Each level line segment: horizontal extent from x=−√(2E_n/(mω²)) to x=+√(2E_n/(mω²)) — the classical turning points at that energy. The parabola V(x) = ½mω²x² plotted continuously behind the levels. Two bracket markers: one for ΔE=ℏω (between any adjacent pair, e.g., n=1 to n=2), one for E₀=ℏω/2 (between parabola floor and n=0). These two brackets encode the entire spectrum formula.

**[O]** Single panel. Parabola: continuous smooth curve, centered. Six horizontal energy level lines, stacked with equal vertical spacing. Classical turning-point extent of each level line: levels get progressively wider upward (parabola is wider at higher energies). ΔE bracket: placed on the right margin between n=1 and n=2 lines, with a vertical extent bracket symbol. E₀ bracket: placed on the right margin between the parabola floor and n=0 line. Energy axis: vertical, from 0 at bottom, running to just above E₅. Position axis: horizontal, symmetric about 0. No secondary axes.

**[P]** Flat vector, Okabe-Ito palette, 1 pt strokes, white background, no baked text. Parabola: neutral gray #AAAAAA, 1 pt solid. Energy level lines n=0 to n=5: Blue #0072B2 (dominant), 1.5 pt solid — all levels same color to emphasize uniformity of spacing. Zero-point energy bracket (E₀): Bluish Green #009E73 (active — the key non-classical result), 1 pt with end-caps. Level-spacing bracket (ΔE): Orange #E69F00 (secondary — the uniform spacing), 1 pt with end-caps. Classical turning-point markers (optional small tick at each end of each level line): light gray #CCCCCC, 0.5 pt. Energy axis stroke: light gray #AAAAAA, 0.5 pt. Parabola fill: very light gray at 10% opacity inside parabola interior.

**[E]** EXCLUSIONS: do not show wave functions on this energy-level diagram — that is Figure 2; do not show the classical turning points as separate vertical dashed lines crossing multiple levels; do not show a second potential (e.g., the infinite square well) for comparison; do not show the coherent state or superposition on this diagram; do not show the zero-point energy comparison to liquid helium or Casimir effect as a separate panel; do not label n values numerically (labels added in production); do not show more than six levels.

### BLOCK 3 — NEGATIVE PROMPT

3D surface rendering of the parabola, rainbow energy-level color gradient, non-uniform level spacing, level lines extending beyond the parabola walls, text labels, words, gibberish letters, titles, captions, decorative borders, realistic textures, drop shadows, gradient backgrounds, photographic elements, dual-headed arrows, hand-drawn styles, human figures, visual clutter, watermarks, red-green color combinations, rainbow color scales, 3D perspective distortion

---

## Figure 2 — Hermite-Gauss Eigenfunctions as Stacked Comparison Panels

**Heuristic:** PQ (four eigenfunctions ψ₀ through ψ₃ as stacked overlapping comparison panels sharing a common x-axis; node count n, growing spread √(2n+1), evanescent tails beyond classical turning points visible)
**Rank:** Critical

### BLOCK 1 — ILLUSTRAE PASTE BLOCK

Draw four sub-panels arranged vertically and sharing a common horizontal position axis. In each sub-panel, draw a single smooth wave function curve. The bottom sub-panel shows a smooth Gaussian bell curve with no crossings of the baseline — zero nodes. The second sub-panel shows a curve that crosses the baseline exactly once, with two lobes of opposite sign. The third sub-panel shows a curve with two nodes — three lobes. The fourth sub-panel shows a curve with three nodes — four lobes. In each sub-panel, draw two short vertical tick marks symmetrically placed on the baseline to indicate the classical turning points for that level — the horizontal distance between the turning points increases from the bottom sub-panel to the top sub-panel. The wave function curves in each sub-panel visibly extend slightly beyond the turning-point tick marks before decaying toward zero, showing the evanescent tails. The four sub-panels share the same horizontal axis extent and the same vertical zero line. The diagram must be blank and unannotated — no text labels baked in.

### BLOCK 2 — FULL SCOPE

**[S]** Single-column 89 mm, 300 DPI, vector, white background.

**[C]** Four eigenfunctions: ψ₀ (Gaussian, no nodes), ψ₁ (one node, antisymmetric), ψ₂ (two nodes, symmetric), ψ₃ (three nodes, antisymmetric). Plotted in position space x as ψ_n(x), not |ψ_n|². Using dimensionless variable ξ = √(mω/ℏ) x: ψ₀ ∝ exp(−ξ²/2); ψ₁ ∝ 2ξ exp(−ξ²/2); ψ₂ ∝ (4ξ²−2) exp(−ξ²/2); ψ₃ ∝ (8ξ³−12ξ) exp(−ξ²/2). Classical turning points for level n: ξ = ±√(2n+1) — these widen with n and are visible as the brackets grow from ψ₀ to ψ₃. Chapter states: "ψ_n has exactly n nodes" and "roughly 16% of the ground-state probability density lies outside the classical turning points." The evanescent extension beyond the turning-point ticks in each panel must be visible — the curve should not truncate at the tick marks. All four panels share the same ξ-axis range (approximately −4 to +4 in units of √(ℏ/mω)).

**[O]** Four sub-panels stacked vertically, equal height, shared horizontal axis range [−4, +4] in dimensionless ξ units. Each sub-panel has its own horizontal zero line (ψ = 0 reference). Wave function curve: signed (not absolute value), so odd-parity states (ψ₁, ψ₃) show antisymmetric curves crossing zero. Classical turning-point ticks: short vertical marks at ±√(2n+1) on the zero line of each sub-panel; these marks widen from bottom to top sub-panel. Sub-panels are stacked with minimal gap; the shared horizontal axis is visible only at the bottom of the lowest sub-panel. Vertical extent of each sub-panel: sufficient to show the maximum amplitude without clipping. Each sub-panel has the same height; amplitude is rescaled within each panel to fill the sub-panel height (normalized independently per panel, which is acceptable because the chapter shows ψ, not |ψ|² normalized to the same absolute scale).

**[P]** Flat vector, Okabe-Ito palette, 1 pt strokes, white background, no baked text. ψ₀ curve: Bluish Green #009E73 (active — the special ground state, minimum uncertainty), 1.5 pt solid. ψ₁ curve: Blue #0072B2 (dominant), 1.5 pt solid. ψ₂ curve: Sky Blue #56B4E9 (anchor), 1.5 pt solid. ψ₃ curve: Orange #E69F00 (secondary), 1.5 pt solid. Horizontal zero lines: light gray #CCCCCC, 0.5 pt. Classical turning-point ticks: Vermillion #D55E00 (blocking — classical forbidden boundary), 1 pt vertical stroke on each zero line. Sub-panel separator lines: light gray #EEEEEE, 0.25 pt. Evanescent tail region (beyond turning-point ticks): no separate color change — the wave function curve continues in the same color to show the smooth mathematical continuation.

**[E]** EXCLUSIONS: do not show |ψ_n|² (probability density) — wave functions ψ_n only (signed); do not show all six levels from Figure 1 — only n=0, 1, 2, 3; do not show the parabolic potential as a background in these panels — that is Figure 1's job; do not show n=4 or n=5; do not show coherent state or superposition wave functions; do not normalize all four curves to the same vertical scale — each sub-panel fills its own height for readability; do not show separate labeled markers for lobes.

### BLOCK 3 — NEGATIVE PROMPT

probability density |ψ|² (absolute value squared), 3D surface rendering of Hermite polynomials, color-coded probability heatmap, single merged panel showing all four curves superimposed, text labels, words, gibberish letters, titles, captions, decorative borders, realistic textures, drop shadows, gradient backgrounds, photographic elements, dual-headed arrows, hand-drawn styles, human figures, visual clutter, watermarks, red-green color combinations, rainbow color scales, 3D perspective distortion

---

## Figure 3 — Ladder Operator Action: a† Raises, a₋ Lowers

**Heuristic:** MC (process with ≥3 interdependent steps: ground state defined by a₋|0⟩=0; applying a† steps up by ℏω; applying a₋ steps down by ℏω; floor terminates descent)
**Rank:** Important

### BLOCK 1 — ILLUSTRAE PASTE BLOCK

Draw a vertical arrangement of five horizontal bars at equally spaced heights, representing energy levels n=0 through n=4. From the leftmost level line at each height, draw an upward curved arrow reaching the level one step above — these arrows represent the raising operator. From the rightmost level line at each height (except the bottom), draw a downward curved arrow reaching the level one step below — these arrows represent the lowering operator. At the bottom level, draw a short stubbed downward arrow terminating with a small blocking cross or circle symbol, indicating that the lowering operator kills the ground state and does not produce a level below it. The upward arrows and downward arrows should arc on opposite sides of the level lines to keep the diagram from crossing. All steps are equal in height. The diagram must be blank and unannotated — no text labels baked in.

### BLOCK 2 — FULL SCOPE

**[S]** Single-column 89 mm, 300 DPI, vector, white background.

**[C]** Five levels: n=0, 1, 2, 3, 4 at equally spaced heights. Raising arrows (a†): one curved upward arrow per rung connecting level n to level n+1, for n=0,1,2,3 — four raising arrows total. Lowering arrows (a₋): one curved downward arrow per rung connecting level n to level n−1, for n=1,2,3,4 — four lowering arrows total. The floor termination: at n=0, the lowering arrow is drawn as a stub pointing downward with a terminating symbol (small filled circle or square block), representing a₋|0⟩=0. Chapter states: "the lowering operator kills the ground state" and "there exists a ground state |0⟩ that the lowering operator kills." The equal vertical spacing between all levels is the visual claim of uniform ℏω gap. The blocking symbol at n=0 is the visual assertion of the floor. Raising and lowering arrows arc on opposite sides (raising arrows arc left, lowering arrows arc right) to avoid occlusion. Prefactors √(n+1) and √n on the arrows are structural claims that can be indicated by arrow line weight graduated from thin (n=0→1) to thick (n=3→4) — thicker arrows indicate larger prefactor.

**[O]** Single panel. Five horizontal level bars, stacked vertically with equal spacing (approximately 20% of panel height each). Raising arrows: curved arcs on left side, one per step, arrowhead pointing upward. Lowering arrows: curved arcs on right side, one per step, arrowhead pointing downward. Floor termination stub at n=0: downward short arrow ending in a blocking symbol. Level bars: horizontal lines of fixed width, centered. No secondary axes. Overall layout: tall narrow format with levels stacked from n=0 at bottom to n=4 at top.

**[P]** Flat vector, Okabe-Ito palette, 1 pt strokes, white background, no baked text. Level bars n=0 to n=4: Blue #0072B2 (dominant), 1.5 pt solid — all same color. Raising arrows (a†): Bluish Green #009E73 (active — creation, positive action), 1 pt solid arcs, arrowheads at terminal end; line weight graduated: 1 pt at n=0→1, 1.5 pt at n=1→2, 2 pt at n=2→3, 2 pt at n=3→4. Lowering arrows (a₋): Vermillion #D55E00 (blocking — the destructive/lowering direction), 1 pt solid arcs, arrowheads at terminal end; line weight graduated similarly. Floor termination stub and blocking symbol at n=0: Vermillion #D55E00, with a filled square blocking cap. Arrow line weight graduation encodes the √(n) and √(n+1) scaling.

**[E]** EXCLUSIONS: do not show the energy axis as a vertical number line — the equal level spacing is structural, not quantitative in this diagram; do not show wave functions at each level (that is Figure 2); do not show the commutator [a₋, a†]=1 as a separate annotation; do not show the raising arrows on the right side and lowering arrows on the left — they must arc on opposite sides to avoid crossing; do not show the coherent state as a superposition spread over multiple levels; do not show more than five levels; do not show a₊² or a₋² (two-step jumps).

### BLOCK 3 — NEGATIVE PROMPT

crossing arrows forming an X pattern, circular level diagram (ring topology), arrows with gradient color fill, text labels, words, gibberish letters, titles, captions, decorative borders, realistic textures, drop shadows, gradient backgrounds, photographic elements, dual-headed arrows, hand-drawn styles, human figures, visual clutter, watermarks, red-green color combinations, rainbow color scales, 3D perspective distortion

---

## Figure 4 — Diatomic Molecule Vibrational Parameters (Dot-Plot)

**Heuristic:** PQ (four molecules, three quantitative parameters each — ℏω in eV, λ in μm, T_classical onset; bar or dot chart)
**Rank:** Supplementary

### BLOCK 1 — ILLUSTRAE PASTE BLOCK

Draw a horizontal dot-plot with a vertical axis listing four diatomic molecules and a horizontal axis showing energy level spacing ℏω in electron volts, starting at zero and running to approximately 0.6 eV. For each molecule, place a filled circle at its level spacing value. Draw a vertical dashed reference line at the room-temperature thermal energy kT ≈ 0.025 eV. All four molecular dots lie to the right of this reference line. Place a second horizontal dot-plot panel directly below the first, sharing the same vertical molecule axis but with a horizontal axis showing wavelength in micrometers from zero to approximately 9 μm. The four dots in the lower panel show the infrared absorption wavelength for each molecule. The two panels share vertical alignment so horizontal comparison between energy and wavelength is possible. The diagram must be blank and unannotated — no text labels baked in.

### BLOCK 2 — FULL SCOPE

**[S]** Single-column 89 mm, 300 DPI, vector, white background.

**[C]** Four molecules from the chapter comment table at line 205: HCl (ℏω ≈ 0.37 eV, λ ≈ 3.4 μm), N₂ (ℏω ≈ 0.29 eV, λ ≈ 4.3 μm), CO (ℏω ≈ 0.27 eV, λ ≈ 4.6 μm), H₂ (ℏω ≈ 0.54 eV, λ ≈ 2.3 μm). Room-temperature thermal energy: kT ≈ 0.025 eV (referenced in chapter: "Since kT ≪ ℏω, essentially all HCl molecules are in the vibrational ground state at room temperature"). The reference line at kT = 0.025 eV separates classical vs. quantum vibrational behavior — all four molecules fall in the quantum regime (ℏω ≫ kT). Upper panel: ℏω axis from 0 to 0.6 eV. Lower panel: λ axis from 0 to 9 μm. Molecules listed on shared y-axis in order of decreasing ℏω: H₂, HCl, N₂, CO. Relationship between panels: ℏω = hc/λ — the inverse proportionality is readable from the two-panel layout (H₂ has largest ℏω and smallest λ; CO has smallest ℏω and largest λ).

**[O]** Two panels stacked vertically, each a horizontal dot-plot. Shared vertical y-axis lists four molecules. Upper panel: ℏω axis from 0 to 0.6 eV, reference dashed line at kT=0.025 eV. Lower panel: λ axis from 0 to 9 μm, no reference line needed. Dots: 4 pt filled circles, one per molecule per panel. Horizontal guide lines (one per molecule row): light gray, 0.25 pt. Both panels share the same vertical alignment (molecules at same y-positions in both panels). Axes both start at zero.

**[P]** Flat vector, Okabe-Ito palette, 1 pt strokes, white background, no baked text. H₂ dots (both panels): Bluish Green #009E73 (active — highest frequency, most quantum), filled circles. HCl dots: Blue #0072B2 (dominant), filled circles. N₂ dots: Sky Blue #56B4E9 (anchor), filled circles. CO dots: Orange #E69F00 (secondary), filled circles. Same color per molecule in both panels — enabling cross-panel identification by color. kT reference line: Vermillion #D55E00 (blocking — the classical boundary), 1 pt dashed. Guide lines: light gray #DDDDDD, 0.25 pt. Axis strokes: light gray, 0.5 pt.

**[E]** EXCLUSIONS: do not show reduced mass μ on either axis — ℏω and λ only; do not show multiple temperature reference lines; do not show a third panel for angular frequency ω in rad/s — eV and μm only (SI units are in the chapter text, the figure needs physics-accessible units); do not show error bars; do not show anharmonic correction terms; do not show ω slider behavior from the simulation.

### BLOCK 3 — NEGATIVE PROMPT

bar chart with vertical bars, 3D bar chart, pie segment for each molecule, scatter plot with non-zero baseline, molecular structure diagrams, text labels, words, gibberish letters, titles, captions, decorative borders, realistic textures, drop shadows, gradient backgrounds, photographic elements, dual-headed arrows, hand-drawn styles, human figures, visual clutter, watermarks, red-green color combinations, rainbow color scales, 3D perspective distortion

---

## Video Candidate Pass

**Figure 1 — Equally Spaced Energy Spectrum on the Parabolic Potential:** STATIC SUFFICIENT. Criterion: the six levels and their spacings are a fixed structure, not a temporal sequence. The zero-point offset and uniform ℏω gap are readable statically from the two bracket markers.

**Figure 2 — Hermite-Gauss Eigenfunctions:** VIDEO CANDIDATE — NOT RECOMMENDED. The natural video would step n from 0 to 5, adding one node and widening the classical turning points with each step. This is pedagogically compelling, but the four-panel stacked figure accomplishes the comparison simultaneously — the student can see all four at once and count nodes across panels without temporal sequencing. The simulation deliverable (07-harmonic-oscillator.html eigenstate mode) does this interactively. Static figure recommended.

**Figure 3 — Ladder Operator Action:** VIDEO CANDIDATE — RECOMMENDED. The learning target is a sequential process: a† acting on |n⟩ produces |n+1⟩ (show the level lighting up one step above); a₋ acting on |n⟩ produces |n−1⟩ (show the level lighting up one step below); a₋ acting on |0⟩ produces nothing — show the blocking symbol activate. A 10–12 second loop in three stages — raise, lower, floor termination — demonstrates the causal chain in the order the chapter presents it. The floor termination is the key pedagogical moment: the animation shows a₋ reaching for a level below n=0 and finding none, which is more vivid than a static blocking symbol. No other figure in this chapter has a sequential causal mechanism that animation exposes better than the static form. RECOMMENDED VIDEO.

**Figure 4 — Diatomic Molecule Vibrational Parameters:** STATIC SUFFICIENT. Criterion: a dot-plot of measured constants is a lookup and comparison task with no temporal sequence.
