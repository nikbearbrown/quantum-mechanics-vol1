# CAJAL Figure Report — Chapter 1 — Why Classical Physics Failed: Blackbody, Photoelectric, and the Photon

Recommended: 4 figures, Mixed density.

Chapter 1 is dense with PQ material: the blackbody spectral curves (Planck vs. Rayleigh–Jeans), the quantitative collapse of the classical prediction (twenty orders of magnitude at UV frequencies), the photoelectric stopping-voltage vs. frequency linear relationship across multiple metals, and the work-function threshold structure. Three PQ heuristics and one MC heuristic fire. One chapter-embedded table (work functions) also warrants a quantitative figure — the author has embedded it as a comment placeholder, confirming intent. No figure is needed for the Compton scattering section: the scattering geometry and wavelength-shift formula are the standard textbook schematic, and the chapter does not claim any structural relationship that cannot be followed from the equation and prose; that figure belongs to a future chapter on photon momentum if one exists.

---

## Figure 1 — Planck vs. Rayleigh–Jeans Spectral Distribution

**Heuristic:** PQ (quantitative spectral curves with Wien peak and catastrophe regime)
**Rank:** Critical

### BLOCK 1 — ILLUSTRAE PASTE BLOCK

Draw a single-panel line chart with a horizontal frequency axis running from low to high frequency and a vertical spectral energy density axis starting at zero. Plot two curves sharing the same axes: one hump-shaped curve that rises from near zero at low frequency, peaks at an intermediate frequency, and falls back toward zero at high frequency — this is the Planck distribution. The second curve rises from near zero at low frequency, passes through the peak region in agreement with the first curve, continues rising steeply at high frequencies and is clipped at a fixed multiple of the Planck peak with a terminating marker — this is the Rayleigh–Jeans law that diverges. Mark the peak of the Planck curve with a vertical dashed line. In the low-frequency region where the two curves overlap, indicate the agreement zone with a horizontal bracket or shaded band. In the high-frequency region above the clip, indicate the divergence regime. The diagram must be blank and unannotated — no text labels baked in.

### BLOCK 2 — FULL SCOPE

**[S]** Single-column 89 mm, 300 DPI, vector, white background.

**[C]** Two curves only — Planck distribution (hump-shaped, finite peak, falls exponentially at high frequency) and Rayleigh–Jeans law (quadratic rise, clipped, diverges). Agreement zone at low frequency: explicitly stated in chapter ("agrees with measurement at long wavelengths"). Wien peak: vertical dashed line at peak of Planck curve. Divergence regime: region above the clip marker. The chapter states the ratio Planck/RJ at UV is ~7×10⁻²⁰ — this asymptotic separation is the visual drama of the figure and must be represented by the clip with a visible gap between where RJ was clipped and where the Planck curve lies at that same frequency. Y-axis from zero — no exceptions. X-axis: frequency, monotonically increasing left to right (log-spaced axis matches simulation spec in chapter, but for the static figure a linear-in-frequency axis showing [0, ~10¹⁵ Hz] is sufficient to show both the agreement region and the catastrophe). Do not fabricate a specific numerical temperature — draw at a representative T that shows both curves clearly.

**[O]** Single panel. Planck curve: filled area under curve. Rayleigh–Jeans: solid line, clipped at 3× Planck maximum with a vertical terminating stroke and upward arrow stub indicating "continues to infinity." Agreement bracket: horizontal double-headed bracket below both curves in the low-frequency overlap region, 1 pt gray. Wien peak dashed line: vertical dashed from x-axis to Planck curve peak. Y-axis from zero. Both curves share the same x-axis and y-axis.

**[P]** Flat vector, Okabe-Ito palette, 1 pt strokes, white background, no baked text. Planck curve fill: Sky Blue #56B4E9 at 40% opacity, stroke Blue #0072B2, 1 pt. Rayleigh–Jeans line: Vermillion #D55E00 (blocking/negative — the catastrophic prediction), 1 pt solid, terminated with upward arrow stub. Wien peak dashed line: Bluish Green #009E73 (active/positive — the correct prediction), 1 pt dashed. Agreement zone bracket: light gray, 0.5 pt. Divergence regime: very light Vermillion tint background above clip level, no fill below clip.

**[E]** EXCLUSIONS: do not show a temperature slider or multiple temperature curves on the same panel — one representative temperature only; do not show the ratio u_Planck/u_RJ as a separate curve or annotation number — the visual separation conveys this; do not show Compton or photoelectric data; do not show the mode density factor separately; do not include a legend box with text.

### BLOCK 3 — NEGATIVE PROMPT

3D surface plot, rainbow spectral color gradient applied to curves, multiple overlapping temperature curves, inset data table, annotation callout boxes with numbers, text labels, words, gibberish letters, titles, captions, decorative borders, realistic textures, drop shadows, gradient backgrounds, photographic elements, dual-headed arrows, hand-drawn styles, human figures, visual clutter, watermarks, red-green color combinations, rainbow color scales, 3D perspective distortion

---

## Figure 2 — Photoelectric Stopping Potential vs. Frequency

**Heuristic:** PQ (linear quantitative relationship across multiple metals, threshold structure)
**Rank:** Critical

### BLOCK 1 — ILLUSTRAE PASTE BLOCK

Draw a single-panel scatter-line chart with a horizontal frequency axis and a vertical stopping-potential axis. Plot three parallel line segments with identical slope, each starting at a different threshold frequency on the x-axis where the line crosses zero stopping potential, and each rising linearly to the right of its threshold. Below each threshold frequency, draw a flat horizontal segment at zero (no emission). Mark the three threshold frequencies with vertical tick marks on the x-axis. Mark the shared slope visually with a right-triangle rise-over-run indicator on one of the lines. The vertical axis must start at zero or slightly below zero to show the threshold clearly. The diagram must be blank and unannotated — no text labels baked in.

### BLOCK 2 — FULL SCOPE

**[S]** Single-column 89 mm, 300 DPI, vector, white background.

**[C]** Three metals from chapter text: Na (threshold ~5.51×10¹⁴ Hz, Φ = 2.28 eV), Al (threshold ~9.92×10¹⁴ Hz, Φ = 4.1 eV), Cu (threshold ~1.14×10¹⁵ Hz, Φ = 4.7 eV). Each metal: one line segment rising from its threshold frequency with slope h/e = 4.136×10⁻¹⁵ V·s (all three slopes identical — this is the central quantitative claim of the chapter). Pre-threshold flat segment at V = 0 for each metal. The shared slope is a structural/quantitative claim explicitly stated in the chapter (Millikan measured h/e = 4.136×10⁻¹⁵ V·s for all metals). Rise-over-run triangle on the Na line to indicate slope. Y-axis from zero (or slightly below to accommodate threshold marker at y=0). X-axis frequency range: [3×10¹⁴, 3×10¹⁵] Hz as specified in the chapter's simulation section.

**[O]** Single panel. Three line segments, left-to-right ordered by threshold frequency (Na leftmost, Al middle, Cu rightmost). Pre-threshold segments: dashed or lighter weight indicating "zero, not just low." Post-threshold segments: solid, labeled implicitly by color. Rise-over-run triangle: small gray right triangle attached to the Na line between two representative points. Threshold tick marks: short vertical lines on the x-axis at each threshold. Y-axis: stopping potential V, starts at 0, runs to ~5 V. All three lines share common x-axis and y-axis.

**[P]** Flat vector, Okabe-Ito palette, 1 pt strokes, white background, no baked text. Na line (lowest threshold): Bluish Green #009E73 (primary anchor, earliest/most accessible threshold). Al line: Sky Blue #56B4E9. Cu line: Reddish Purple #CC79A7. Pre-threshold flat segments: light gray, 0.5 pt dashed. Rise-over-run triangle: Orange #E69F00 outline, 0.5 pt, no fill. Threshold tick marks: neutral light gray, 0.5 pt vertical stroke on x-axis. Axis strokes: neutral gray, 0.5 pt.

**[E]** EXCLUSIONS: do not show intensity on any axis — the chapter is explicit that intensity does not affect stopping potential; do not show the photon energy E=hν as a separate curve; do not show a wave vs. particle comparison panel; do not show the work function as a separate annotation rectangle; do not show more than three metals on this panel; do not include error bars (Millikan's data is presented as definitive, not probabilistic, in this chapter).

### BLOCK 3 — NEGATIVE PROMPT

wave amplitude oscillation curves, intensity vs. stopping potential axes, bar chart form, pie segments, scatter dots without connecting lines, text labels, words, gibberish letters, titles, captions, decorative borders, realistic textures, drop shadows, gradient backgrounds, photographic elements, dual-headed arrows, hand-drawn styles, human figures, visual clutter, watermarks, red-green color combinations, rainbow color scales, 3D perspective distortion

---

## Figure 3 — The x = hν/k_BT Regime Map

**Heuristic:** PQ (the chapter's central quantitative discriminant — when does quantum mechanics matter?)
**Rank:** Important

### BLOCK 1 — ILLUSTRAE PASTE BLOCK

Draw a single horizontal axis representing the dimensionless ratio x = hν/k_BT, running from 0 on the left to a value of approximately 10 on the right. At x = 1, place a vertical dividing line. To the left of x = 1, shade a band indicating the classical agreement regime — where the Planck formula reduces to the Rayleigh–Jeans law. To the right of x = 1, shade a band in a contrasting color indicating the quantum regime — where the exponential suppression dominates and classical physics fails. Below the axis, mark three representative points: one at x ≈ 0.1 with a small circle (deep infrared at room temperature — classical regime), one at x ≈ 1 with a diamond marker at the boundary, and one at x ≈ 48 with a triangle marker (UV at 3000 K — the twenty-orders-of-magnitude failure case from the worked example). Above the boundary line at x = 1, draw a small bracket indicating the transition width. The diagram must be blank and unannotated — no text labels baked in.

### BLOCK 2 — FULL SCOPE

**[S]** Single-column 89 mm, 300 DPI, vector, white background.

**[C]** The chapter defines x = hν/k_BT as the controlling parameter explicitly: "when x ≪ 1, the two theories agree; when x ≫ 1, they disagree by factors that grow like e^x." Three regimes from chapter text: classical (x ≪ 1, Rayleigh–Jeans valid), boundary (x ~ 1, quantization begins to matter), quantum (x ≫ 1, exponential suppression, classical catastrophically wrong). Three representative points from chapter: x ≈ 0.1 (infrared, classical), x ≈ 1 (boundary), x ≈ 47.9 (UV at 3000 K, the worked example). The x-axis is intentionally truncated on the right — the x=48 point should be shown by a break marker on the axis rather than stretching the axis to 48 (which would compress all the interesting structure). All relationships are directly from chapter text — no inferences.

**[O]** Horizontal axis, left to right from x=0 to x≈10 with an axis break and compressed representation of x=48. Classical band: left of x=1, shaded. Quantum band: right of x=1, shaded. Vertical dividing line at x=1, 1 pt solid. Three point markers below axis at their x-values: open circle (x≈0.1), diamond (x=1), triangle with an axis-break representation near x=48. Transition bracket above x=1 line. No secondary axes.

**[P]** Flat vector, Okabe-Ito palette, 1 pt strokes, white background, no baked text. Classical band: Orange #E69F00 at 20% opacity (secondary, "the old picture"). Quantum band: Blue #0072B2 at 20% opacity (dominant, "the correct regime"). Dividing line at x=1: Bluish Green #009E73 (active/positive — the boundary that matters), 1 pt solid. x≈0.1 circle marker: Orange #E69F00, filled. x=1 diamond marker: Bluish Green #009E73, filled. x≈48 triangle marker: Sky Blue #56B4E9 (this is the quantum extreme). Axis stroke: light gray 0.5 pt. Axis break marker: diagonal double-slash, neutral gray.

**[E]** EXCLUSIONS: do not show the Planck formula or Rayleigh–Jeans formula as separate curves on this diagram — this is a regime-map only; do not show temperature on a separate axis; do not show specific materials or metal work functions; do not show a two-dimensional heatmap of x as a function of both ν and T — one-dimensional regime axis only; do not show the Compton wavelength or photoelectric threshold on this axis.

### BLOCK 3 — NEGATIVE PROMPT

2D heatmap of x(ν, T), rainbow colorscale for regime bands, pie chart partition, 3D surface, multiple overlapping curves, text labels, words, gibberish letters, titles, captions, decorative borders, realistic textures, drop shadows, gradient backgrounds, photographic elements, dual-headed arrows, hand-drawn styles, human figures, visual clutter, watermarks, red-green color combinations, rainbow color scales, 3D perspective distortion

---

## Figure 4 — Work Functions of Common Metals (Quantitative Comparison)

**Heuristic:** PQ (the embedded table in chapter text — 11 metals, work functions spanning 2.1–6.35 eV)
**Rank:** Supplementary

### BLOCK 1 — ILLUSTRAE PASTE BLOCK

Draw a horizontal dot-plot (also called a Cleveland dot chart) with a vertical axis listing eleven metals and a horizontal axis showing work function in electron volts, starting at zero and running to approximately 7 eV. For each metal, place a filled circle at its work function value. Draw a vertical dashed reference line at the photon energy corresponding to the UV example (approximately 4.1 eV) to indicate where one specific example photon frequency would place the threshold. Group the metals implicitly by whether their work function falls below or above this reference line by coloring the dots differently on each side. Arrange the metals vertically in ascending order of work function. The diagram must be blank and unannotated — no text labels baked in.

### BLOCK 2 — FULL SCOPE

**[S]** Single-column 89 mm, 300 DPI, vector, white background.

**[C]** Eleven metals and their work functions exactly as listed in chapter comment: Cs 2.1 eV, Na 2.28 eV, K 2.3 eV, Mg 3.7 eV, Al 4.1 eV, Ag 4.3 eV, Fe 4.5 eV, Cu 4.7 eV, Ni 5.0 eV, Au 5.1 eV, Pt 6.35 eV. Reference line at 4.13 eV (photon energy used in the sodium worked example: hc/300 nm = 4.13 eV — explicitly calculated in chapter). Metals below reference: would emit at the example UV frequency. Metals above reference: would not emit. Y-axis: metals listed vertically in ascending work-function order. X-axis: work function in eV, from 0. All values are exactly from chapter text — no inferences.

**[O]** Horizontal dot-plot. Vertical y-axis lists metals (text labels will be added in production — CAJAL delivers blank vector; illustrator adds labels). Horizontal x-axis from 0 to 7 eV. One filled dot per metal at its work function value. Horizontal grid lines: light gray, 0.25 pt, one per metal row. Reference vertical dashed line at ~4.13 eV. Dots: 4 pt filled circles. No connecting lines between dots. X-axis from zero.

**[P]** Flat vector, Okabe-Ito palette, 1 pt strokes, white background, no baked text. Dots for metals with Φ < 4.13 eV (Cs, Na, K, Mg): Bluish Green #009E73 (active/positive — these metals emit at the example frequency). Dots for metals with Φ ≥ 4.13 eV (Al, Ag, Fe, Cu, Ni, Au, Pt): Blue #0072B2 (dominant — do not emit). Al dot sits at boundary — use Orange #E69F00 (secondary, boundary). Reference dashed line: Vermillion #D55E00 (blocking/negative — the threshold barrier), 1 pt dashed. Grid lines: light gray #DDDDDD, 0.25 pt. X-axis stroke: light gray, 0.5 pt.

**[E]** EXCLUSIONS: do not show threshold frequencies on this chart — work functions in eV only, as stated in the chapter's embedded table; do not show electron emission probability curves; do not show the stopping potential on this chart — that is Figure 2; do not show atomic number or period/group structure; do not show error bars or uncertainty ranges; do not sort by any property other than work function value.

### BLOCK 3 — NEGATIVE PROMPT

bar chart with vertical bars, 3D bar chart, pie chart, grouped bar clusters, element periodic table layout, scatter plot with non-zero y-axis baseline, text labels, words, gibberish letters, titles, captions, decorative borders, realistic textures, drop shadows, gradient backgrounds, photographic elements, dual-headed arrows, hand-drawn styles, human figures, visual clutter, watermarks, red-green color combinations, rainbow color scales, 3D perspective distortion

---

## Video Candidate Pass

**Figure 1 — Planck vs. Rayleigh–Jeans Spectral Distribution:** VIDEO CANDIDATE. Criterion: the learning target is a transition mechanism — as temperature T increases, the Planck peak shifts right (Wien's law) while the RJ law scales everywhere, and the catastrophic divergence of RJ relative to Planck becomes visible at higher frequencies. A 15-second animation showing T sweeping from 1000 K to 10000 K with both curves updating in real time would demonstrate Wien's displacement and the UV catastrophe as a dynamic process rather than a snapshot. RECOMMENDED VIDEO.

**Figure 2 — Photoelectric Stopping Potential vs. Frequency:** STATIC SUFFICIENT. Criterion: the relationship is a static linear family — three parallel lines with different x-intercepts. There is no temporal sequence or cyclical transformation to animate. The shared slope is immediately readable from a static comparison.

**Figure 3 — The x = hν/k_BT Regime Map:** STATIC SUFFICIENT. Criterion: a regime-boundary diagram is a fixed classification, not a sequential causal process. No transition mechanism is the learning target.

**Figure 4 — Work Functions of Common Metals:** STATIC SUFFICIENT. Criterion: a sorted dot-plot of measured values with a reference line is a lookup and comparison task, not a process. No causal stages or transformations.
