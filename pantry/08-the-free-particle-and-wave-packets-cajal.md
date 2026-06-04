# CAJAL Figure Report — Chapter 8 — The Free Particle and Wave Packets

Recommended: 4 figures, High density.

Chapter 8 is unusually rich in PQ and VG material. Three spatial/structural claims require figures: the plane-wave-versus-packet contrast (VG, two-state visual comparison), the Fourier superposition that builds a packet (MC, constructive-interference process), the group-velocity-versus-phase-velocity kinematics (VG + MC, two simultaneous motions in a time sequence), and the dispersion-spreading formula as a quantitative curve family (PQ). A fifth embedded placeholder — the doubling-time table — is not a figure; it is a data table best rendered as typography with light gridding, not a chart, and is excluded. Four figures are the right count: the pair-contrast opener, the Fourier superposition mechanism, the phase-versus-group-velocity schematic, and the spreading-versus-time chart. No figure is needed for the classical-limit section (the twenty-orders-of-magnitude range is already conveyed by the doubling-time table in prose); that material earns a figure only if the table is reformatted as a dot-chart in Chapter 11 synthesis work.

---

## Figure 1 — Plane Wave vs. Wave Packet: Delocalized Eigenstate and Normalizable Physical State

**Heuristic:** VG (structural spatial claim — constant probability density extending to infinity versus localized normalizable envelope)
**Rank:** Critical

### BLOCK 1 — ILLUSTRAE PASTE BLOCK

Draw two side-by-side panels sharing a horizontal position axis and a vertical probability-density axis that begins at zero. In the left panel, draw a flat horizontal line at a constant nonzero height extending across the full width of the panel from the left edge to the right edge, indicating constant probability density. Beneath this flat line, draw a sinusoidal oscillation of smaller amplitude representing the real part of the wave function, with uniform amplitude and period across the entire axis width. In the right panel, draw a bell-shaped envelope centered in the panel, rising from near zero at the edges, peaking at the center, and descending symmetrically back to near zero — this is the localized probability density. Inside the envelope, draw visible sinusoidal oscillations of the real part of the wave function, with amplitude modulated by the envelope so that oscillations are largest at the center and taper to zero at the edges. The oscillations inside the envelope must be visibly denser (shorter wavelength) than the envelope width — approximately five to eight oscillation cycles visible within the half-maximum width. Both panels use the same axis scales. The diagram must be blank and unannotated — no text labels baked in.

### BLOCK 2 — FULL SCOPE

**[S]** Single-column 89 mm, 300 DPI, vector, white background.

**[C]** Left panel: plane wave |Ψ_k|² = |A|² — constant probability density, the non-normalizable eigenstate with definite momentum. Re(Ψ_k) plotted as sinusoidal oscillation of uniform amplitude beneath the flat density line. Right panel: Gaussian wave packet — |Ψ(x,0)|² as a bell-shaped Gaussian envelope peaked at center. Re(Ψ) plotted as a sinusoid modulated by the Gaussian envelope, showing approximately 6 full oscillation cycles within the main lobe. Both panels derived directly from chapter text: the chapter names these the "delocalized eigenstate" and "normalizable physical state" as the conceptual hinge of the chapter. The carrier oscillations in the right panel must have a shorter spatial period than the envelope width (carrier wavenumber k₀ substantially larger than packet width Δk) — this is the physical regime described in the text. Y-axis from zero. Left panel x-axis: position, spanning approximately ±4 packet widths equivalent to show the "extending everywhere" contrast. Right panel x-axis: same span.

**[O]** Two side-by-side panels, equal width, separated by a thin neutral gray divider. Shared x-axis (position) at bottom of each panel; shared y-axis scale (probability density) marked at left of left panel only. Left panel: flat probability density line (upper trace) at constant height, sinusoidal Re(Ψ) trace (lower trace) of uniform amplitude, separated vertically so both are readable. Right panel: filled Gaussian area under |Ψ|² curve (filled to x-axis), sinusoidal Re(Ψ) trace oscillating within envelope, amplitude tapering to zero at edges. Both panel x-axes extend to panel edges showing the contrast between infinite extent and localization. No panel borders beyond the shared divider. Y-axes from zero.

**[P]** Flat vector, Okabe-Ito palette, 1 pt strokes, white background, no baked text. Left panel probability density: Blue #0072B2 flat line, 1.5 pt. Left panel Re(Ψ) oscillation: Sky Blue #56B4E9, 1 pt. Left panel background: very light gray (#F0F0F0) fill to signal "delocalized." Right panel |Ψ|² Gaussian fill: Sky Blue #56B4E9 at 30% opacity. Right panel |Ψ|² envelope stroke: Blue #0072B2, 1.5 pt. Right panel Re(Ψ) carrier: Bluish Green #009E73 (active — this is the physical state), 1 pt, oscillating within envelope. Panel divider: neutral light gray, 0.5 pt. Y-axis and x-axis strokes: light gray 0.5 pt.

**[E]** EXCLUSIONS: do not show ψ(x) and |ψ(x)|² on the same panel as two labelled curves — only one trace for Re(Ψ) and one for |Ψ|² per panel; do not show the momentum-space representation φ(k) in this figure (that belongs to Figure 2); do not show Im(Ψ); do not show Ψ at a later time; do not show a phase portrait; do not add axis break markers on the left panel to indicate infinite extent — the line simply runs to the panel edges; do not show three or more panels.

### BLOCK 3 — NEGATIVE PROMPT

3D waveform visualization, perspective projection of wave plane, complex plane spiral, Argand diagram, colored interference fringes, rainbow spectral gradient, multiple overlapping plane waves, annotation callout boxes, time-evolution arrow, text labels, words, gibberish letters, titles, captions, decorative borders, realistic textures, drop shadows, gradient backgrounds, photographic elements, dual-headed arrows, hand-drawn styles, human figures, visual clutter, watermarks, red-green color combinations, rainbow color scales, 3D perspective distortion

---

## Figure 2 — Fourier Superposition: Building a Wave Packet from Plane Waves

**Heuristic:** MC (process with three interdependent steps: individual plane waves with spread momenta → superposition → interference that localizes the packet)
**Rank:** Critical

### BLOCK 1 — ILLUSTRAE PASTE BLOCK

Draw a vertical sequence of four horizontal panels sharing a common position axis. In the top three panels, draw individual sinusoidal plane waves of slightly different spatial frequencies — each panel shows one plane wave, with oscillation frequency increasing from first to third panel. All three waves have uniform amplitude and extend across the full panel width. Below all three, place a horizontal arrow or connector pointing downward to the fourth and final panel. In the fourth panel, draw the result of superposing the three plane waves: a wave packet with a prominent central oscillating lobe and smaller side lobes or a smooth envelope decay on both sides, showing that the waves add constructively at the center and cancel away from it. The oscillation inside the lobe is visible. The diagram must be blank and unannotated — no text labels baked in.

### BLOCK 2 — FULL SCOPE

**[S]** Single-column 89 mm, 300 DPI, vector, white background.

**[C]** Three component plane waves (top three panels): the chapter states the superposition is over all k, but three representative waves near k₀ with slightly different k values are sufficient to demonstrate the principle. The waves must have visibly distinct spatial frequencies: k₁ < k₀ < k₂, with the middle wave (k₀) having the intermediate wavelength. All three waves extend across the full panel width, representing their infinite spatial extent. Bottom panel: the resulting wave packet Re(Ψ(x,0)) — a sinusoidal oscillation modulated by an envelope that is large at center and decays toward zero at the edges. The chapter describes this as destructive interference canceling everything except near the packet center. The constructive/destructive interference pattern is the process being illustrated. The superposition panel must clearly show a localized structure absent from any individual component — this is the mechanism claim of the chapter.

**[O]** Four horizontal panels stacked vertically, equal height, with a downward-pointing process arrow between the third and fourth panels indicating summation. Each of the top three panels shows a single sinusoidal wave at constant amplitude spanning the full panel width. Panels are separated by thin horizontal rules. The fourth panel shows the superposition result: an oscillating waveform with a visible envelope peak at center and decay on both sides. A bracket or curved arc spanning all three top panels and pointing to the fourth would reinforce the "sum of all three" relationship. All four panels share the same x-axis (position) and same y-axis scale. Y-axis from zero is not applicable here (wave functions are signed quantities) — the y-axis spans negative to positive symmetrically; however, the envelope of the bottom panel's positive peaks should form a shape consistent with Gaussian or sinc profile, which is asymmetric about zero, and this profile is the figure's visual payload.

**[P]** Flat vector, Okabe-Ito palette, 1 pt strokes, white background, no baked text. Component wave k₁ (lowest frequency): Sky Blue #56B4E9, 1 pt. Component wave k₀ (middle frequency): Blue #0072B2 (dominant, the central momentum), 1.5 pt. Component wave k₂ (highest frequency): Reddish Purple #CC79A7 (transitional), 1 pt. Process arrow between row 3 and row 4: Orange #E69F00 (secondary, process indicator), 1.5 pt downward arrow. Superposition result panel: Bluish Green #009E73 (active — this is the constructed packet), 1.5 pt for the waveform. Envelope outline atop the result: dashed Blue #0072B2, 0.75 pt, tracing the amplitude peaks. Panel separator rules: neutral light gray, 0.25 pt.

**[E]** EXCLUSIONS: do not show more than three component waves — the mechanism is clear with three; do not show φ(k) the momentum-space amplitude on a separate panel in this figure (save for a standalone chart if needed); do not show the time-evolved packet; do not show a Fourier transform graph in frequency space; do not show complex exponentials — only the real parts of the component waves; do not use an irregular or asymmetric set of component frequencies that would obscure the symmetry of the packet construction; do not show more than four panels total.

### BLOCK 3 — NEGATIVE PROMPT

Fourier frequency spectrum bar chart shown alongside the spatial panels, complex plane diagram, 3D waterfall plot of frequency versus position, animated frame sequence still, color gradient along wave crests, text labels, words, gibberish letters, titles, captions, decorative borders, realistic textures, drop shadows, gradient backgrounds, photographic elements, dual-headed arrows, hand-drawn styles, human figures, visual clutter, watermarks, red-green color combinations, rainbow color scales, 3D perspective distortion

---

## Figure 3 — Phase Velocity vs. Group Velocity: Envelope and Carrier in a Moving Packet

**Heuristic:** VG (structural spatial claim about two simultaneous velocities of a single moving object) + MC (sequence of positions at three time instants)
**Rank:** Critical

### BLOCK 1 — ILLUSTRAE PASTE BLOCK

Draw three horizontal panels stacked vertically, each showing a snapshot of the same wave packet at a successive time. Each panel shows a bell-shaped probability-density envelope that translates to the right across the panels, with its center at a different position in each panel — leftmost in the top panel, middle in the second, rightmost in the third. Inside each envelope, draw the sinusoidal carrier wave oscillations whose crests advance to the right at a slower speed than the envelope center — such that at each successive time, the carrier crests inside the envelope have moved by a smaller distance than the envelope center has moved. To show this explicitly, mark one labeled crest position with a vertical reference line in the top panel, and show in each subsequent panel that the crest reference line has moved by a smaller horizontal distance than the envelope peak reference line. Use two distinct vertical dashed marker lines — one tracking the envelope peak position and one tracking the carrier crest position — that are at the same position in the top panel but progressively separate across the three panels. The diagram must be blank and unannotated — no text labels baked in.

### BLOCK 2 — FULL SCOPE

**[S]** Single-column 89 mm, 300 DPI, vector, white background.

**[C]** Three time snapshots: t = 0, t = T, t = 2T for some representative T. The chapter states explicitly: v_g = ℏk₀/m (classical velocity), v_ph = ℏk₀/(2m) = v_g/2. The carrier crests advance at half the envelope speed. In each panel, the spatial period of the carrier oscillations inside the envelope is the same across all three panels (the wave vector k₀ is constant — only the spatial phase advances). The envelope shape is unchanged at each snapshot (spreading is not the focus here; use t values small enough that spreading is negligible, or explicitly draw a constant-width envelope to isolate the velocity comparison). The key geometric fact: over the three panels, the envelope center moves a distance d_g = v_g × 2T while the carrier crest moves d_ph = v_ph × 2T = d_g/2. This factor-of-two ratio is stated precisely in the chapter and is the single most important quantitative fact in this figure. Two vertical dashed reference lines: one anchored to the envelope peak (advancing at v_g), one anchored to a specific carrier crest (advancing at v_ph = v_g/2).

**[O]** Three horizontally wide panels stacked vertically with thin separator rules. In each panel: filled Gaussian envelope (|Ψ|²) centered at its panel-specific position, with the sinusoidal carrier wave (Re(Ψ)) drawn inside and modulated by the envelope. Two dashed vertical reference lines span all three panels, running continuously from top to bottom of the figure: the envelope-peak tracker (left-to-right displacement = v_g × 2T) and the carrier-crest tracker (left-to-right displacement = v_ph × 2T = half the envelope tracker displacement). By the third panel, the two reference lines must be visibly separated. Each panel has the same x-axis (position) span. The reference lines run through all three panels — their continuous downward extent shows motion over time without requiring a time axis.

**[P]** Flat vector, Okabe-Ito palette, 1 pt strokes, white background, no baked text. Envelope fill: Sky Blue #56B4E9 at 30% opacity in all three panels. Envelope stroke: Blue #0072B2 (dominant), 1.5 pt. Carrier oscillation (Re(Ψ)): Bluish Green #009E73 (active), 1 pt, sinusoidal. Envelope-peak reference line: Orange #E69F00 (secondary — tracks the group velocity, the physically meaningful one), 1 pt dashed, spanning all three panels. Carrier-crest reference line: Reddish Purple #CC79A7 (transitional — tracks phase velocity, the one that means less), 1 pt dashed, spanning all three panels. Panel separator rules: neutral light gray #CCCCCC, 0.25 pt.

**[E]** EXCLUSIONS: do not show packet spreading — hold the envelope width constant across the three panels to isolate the velocity comparison; do not show the momentum-space distribution; do not show a separate v_g vs. v_ph comparison arrow outside the three-panel layout; do not show four or more time snapshots — three is sufficient and the figure risks width-to-height problems beyond three; do not show individual plane-wave components alongside the composite packet; do not show any propagation in two spatial dimensions.

### BLOCK 3 — NEGATIVE PROMPT

Dispersion relation ω(k) plot shown in a panel alongside the packet, 2D spatial propagation image, colormap of phase, rainbow phase gradient, interference fringe image, 3D wave surface, animated-frame layout with arrows connecting panels rather than continuous reference lines, text labels, words, gibberish letters, titles, captions, decorative borders, realistic textures, drop shadows, gradient backgrounds, photographic elements, dual-headed arrows, hand-drawn styles, human figures, visual clutter, watermarks, red-green color combinations, rainbow color scales, 3D perspective distortion

---

## Figure 4 — Gaussian Packet Spreading: σ_x(t) vs. t for Three Initial Widths

**Heuristic:** PQ (quantitative distribution curves — σ_x as a function of t — with y-axis from zero, comparing three initial conditions)
**Rank:** Important

### BLOCK 1 — ILLUSTRAE PASTE BLOCK

Draw a single-panel line chart with a horizontal time axis beginning at zero and a vertical position-spread axis beginning at zero. Plot three curves, each starting at a different nonzero value on the vertical axis at time zero and each rising monotonically from left to right. The curve starting at the highest initial value rises the most slowly and remains the highest throughout. The curve starting at the smallest initial value rises steeply and overtakes the others at sufficiently long times. All three curves are concave-up, indicating accelerating growth rate. The three curves cross — the initially narrowest packet, which starts lowest on the vertical axis, eventually exceeds the others because its doubling time is shortest. Mark the initial values where the three curves begin at t = 0 on the vertical axis. Draw a horizontal reference line at double the initial value of the narrowest packet to indicate its doubling time, and a corresponding vertical reference line at the time where that curve intersects the doubled-width level. The diagram must be blank and unannotated — no text labels baked in.

### BLOCK 2 — FULL SCOPE

**[S]** Single-column 89 mm, 300 DPI, vector, white background.

**[C]** The chapter's spreading formula σ(t) = σ₀√(1 + (ℏt/2mσ₀²)²) with three initial widths from the chapter comment: σ₀ = 0.5 nm, σ₀ = 1 nm, σ₀ = 2 nm, for electron mass m = m_e = 9.109×10⁻³¹ kg. Time axis in femtoseconds, spanning 0 to approximately 400 fs (the chapter's worked example gives t_{2x} ≈ 69 fs for σ₀ = 2 nm; 17 fs for σ₀ = 1 nm; ~4 fs for σ₀ = 0.5 nm — all three doubling events visible within 400 fs). Vertical axis from zero in nm, spanning 0 to approximately 8 nm to show all three curves including the widened σ₀ = 2 nm packet. The chapter explicitly states t_{2x} ∝ σ₀²: the figure must make this scaling visible through the visual separation of the three curves' doubling times. The formula is directly from chapter text; all three representative widths are explicitly named in the chapter's embedded figure comment. Reference lines at the σ₀ = 0.5 nm doubling event (most dramatic visually).

**[O]** Single panel. Three curves labeled only by their initial height on the y-axis (no text — color only). Y-axis from zero in nm. X-axis from zero in fs. Horizontal reference line at y = 2 × σ₀(smallest) = 1.0 nm (double the 0.5 nm starting width), 0.5 pt dashed. Vertical reference line dropping from the intersection of the σ₀ = 0.5 nm curve with the 1.0 nm reference line to the x-axis, 0.5 pt dashed — this visually reads off t_{2x} ≈ 4 fs. Tick marks on both axes at round numbers. Three initial-value tick marks on y-axis at 0.5, 1, and 2 nm. All three curves start at their respective initial values; initial value points are marked with small filled circles. Light horizontal grid lines at round nm values, 0.25 pt.

**[P]** Flat vector, Okabe-Ito palette, 1 pt strokes, white background, no baked text. σ₀ = 0.5 nm curve: Vermillion #D55E00 (negative — tightest confinement, fastest spreading), 1.5 pt solid. σ₀ = 1 nm curve: Orange #E69F00 (secondary — intermediate), 1.5 pt solid. σ₀ = 2 nm curve: Blue #0072B2 (dominant — widest initial, slowest spreading), 1.5 pt solid. Initial-value filled circles: same color as their respective curves, 3 pt diameter. Horizontal reference dashed line at y = 1.0 nm: Vermillion #D55E00, 0.5 pt dashed. Vertical reference line at t_{2x}: Vermillion #D55E00, 0.5 pt dashed. Grid lines: light gray #EEEEEE, 0.25 pt. Axis strokes: light gray 0.5 pt.

**[E]** EXCLUSIONS: do not show a fourth curve for the grain of sand or marble — the classical-limit comparison belongs to the doubling-time table in the prose, not to this figure; do not show σ_p(t) on the same axes (it is constant and is the subject of a different point in the chapter); do not show a separate panel for momentum space; do not use a log scale on either axis — the chapter text presents the σ₀² scaling in linear terms and the figure should confirm this at the same scale; do not show more than three σ₀ values; do not show the complex-width derivation or the chirp variable on this chart.

### BLOCK 3 — NEGATIVE PROMPT

log-log axes that obscure the σ₀² quadratic scaling, σ_p(t) overlaid as a flat dashed line, momentum-space inset panel, separate panel showing the dispersion relation, text labels, words, gibberish letters, titles, captions, decorative borders, realistic textures, drop shadows, gradient backgrounds, photographic elements, dual-headed arrows, hand-drawn styles, human figures, visual clutter, watermarks, red-green color combinations, rainbow color scales, 3D perspective distortion

---

## Video Candidate Pass

**Figure 1 — Plane Wave vs. Wave Packet:** STATIC SUFFICIENT. Criterion: the contrast is a fixed structural comparison between two spatial profiles. Both panels are viewed simultaneously. No temporal sequence is the learning target; the chapter's conceptual claim is about the difference in spatial structure, not about how that structure evolves. A static side-by-side is optimal.

**Figure 2 — Fourier Superposition:** VIDEO CANDIDATE. Criterion: the learning target is a constructive-interference process — individual plane waves arriving, superposing, and building up localized structure. A 10–15 second animation that starts with a single plane wave and adds components one by one (increasing the number of superposed k-values from 1 to ~20), showing the gradual emergence of a localized packet from the growing constructive-destructive pattern, would demonstrate that localization is the result of superposition accumulation rather than a property of any single wave. This is an MC figure (≥3 interdependent steps) with a clear causal sequence that benefits from temporal display. RECOMMENDED VIDEO.

**Figure 3 — Phase vs. Group Velocity:** STATIC SUFFICIENT. Criterion: the three-snapshot layout with continuous vertical reference lines conveys the two-speed motion without animation. However, the chapter itself notes "you can watch this happen" — the time-sequence schematic captures the structure, but the dynamic version is handled by the simulation referenced in the chapter (not a CAJAL-scope deliverable).

**Figure 4 — Gaussian Spreading:** STATIC SUFFICIENT. Criterion: σ(t) vs. t is a set of monotone increasing curves. The qualitative and quantitative message (faster spreading for smaller σ₀, σ₀² scaling of doubling time) is fully readable from the static chart. No hidden temporal mechanism requires animation.
