# CAJAL Figure Report — Chapter 5 — The Infinite Square Well

Recommended: 4 figures, moderate-high density.

---

## Figure 5-1 — The Infinite Square Well Potential and First Three Eigenstates (Critical)

**Rank:** Critical
**Type:** Structural schematic with energy-level diagram overlay
**Heuristic:** VG — the chapter's core spatial claim is that each eigenstate ψ_n is a half-integer multiple of a sine wave fitting exactly between the walls, offset vertically to the energy level E_n ∝ n². The n² spacing must be visible by eye. Without a grounding figure showing both the potential geometry and the eigenstates offset to their energy levels, students have no spatial reference for every subsequent calculation.

---

### BLOCK 1 — ILLUSTRAE PASTE BLOCK

Draw a vertical axis representing energy and a horizontal axis representing position from zero to L. On the position axis, draw two tall vertical bars at x = 0 and x = L representing the infinite potential walls; use hatching or a thick fill to indicate they extend upward without bound. Between the walls, draw three horizontal energy levels at heights proportional to 1, 4, and 9 in arbitrary units, spaced to make the n-squared scaling visually apparent — the gap between levels 2 and 3 must be clearly larger than the gap between levels 1 and 2, and the gap between levels 1 and 2 must be clearly larger than E₁ itself. On top of each horizontal energy level, draw the corresponding normalized eigenstate as a sine curve whose baseline is the energy level itself and whose amplitude is scaled to fit neatly: the first eigenstate is one half-period of a positive sine, the second eigenstate shows one full period of a sine with one interior zero crossing at x = L/2, and the third eigenstate shows one and a half periods of a sine with two interior zero crossings. Draw a ground-state zero-point indicator showing that the lowest energy level sits above zero — do not place any level at the zero of the energy axis. Use distinct colors for the three eigenstates. Include no baked text, labels, numbers, or annotations.

---

### BLOCK 2 — FULL SCOPE

**[S]** Single-column, 89 mm wide, 300 DPI, vector, white background.

**[C]** Chapter 5 content only. Concepts: infinite potential walls at x = 0 and x = L; zero potential inside; quantized energy levels E_n = n²π²ℏ²/(2mL²) with n = 1, 2, 3; n² spacing (1:4:9) must be visible by eye in the vertical placement of the three levels; normalized eigenstates ψ_n(x) = √(2/L)sin(nπx/L) drawn as sine curves offset to their energy level baselines; node count (0, 1, 2 interior nodes for n = 1, 2, 3); zero-point energy E₁ > 0. Inferred relation: the visual gap between consecutive levels grows with n, encoding the accelerating n² spacing — this should be unambiguous from the figure geometry alone.

**[O]** Vertical energy axis at left, position axis at bottom running 0 to L. Walls: two filled vertical rectangles with dense hatching (45-degree lines, neutral gray #CCCCCC) at x = 0 and x = L, extending to top of figure. Energy levels: three thin horizontal lines at y proportional to 1, 4, 9. Spacing: level 1 at roughly 11% of figure height from bottom, level 2 at roughly 44%, level 3 at roughly 100% (or scale to fit). Eigenstates: ψ₁ curve in active green (#009E73), ψ₂ in dominant blue (#0072B2), ψ₃ in secondary gold (#E69F00); each drawn as a smooth sine wave with baseline anchored to its energy level; amplitude ≈ 0.5 × (E_n − E_{n−1}) spacing for visual clarity. Zero-point indicator: a small filled circle on the energy axis at E₁ height, in anchor blue (#56B4E9). Bottom zero line: thin neutral gray, V = 0 inside, no label. 1 pt strokes. No baked text.

**[P]** Flat vector. Okabe-Ito HEX. 1 pt strokes. No baked text. No 3D. White background.

**[E]** Do not include: energy labels, n = 1/2/3 annotations, E_n formulae, axis tick numbers, well-width label L, any text on the potential walls. Do not include probability density curves in this figure — only eigenstates. Do not show the potential itself as a continuous U-shape; use only the two wall bars.

---

### BLOCK 3 — NEGATIVE PROMPT

No energy labels, no quantum-number labels, no axis numbers, no formula overlays, no wall labels, no n indicators; text labels, words, gibberish letters, titles, captions, decorative borders, realistic textures, drop shadows, gradient backgrounds, photographic elements, dual-headed arrows, hand-drawn styles, human figures, visual clutter, watermarks, red-green color combinations, rainbow color scales, 3D perspective distortion.

---

## Figure 5-2 — Eigenstates and Probability Densities: Node Structure (Important)

**Rank:** Important
**Type:** Comparison panels (shared axis)
**Heuristic:** VG — the chapter makes two related spatial claims: ψ_n has exactly n − 1 interior nodes, and |ψ_n|² has n probability peaks. These are distinct structural features. Showing ψ₁, ψ₂, |ψ₁|², |ψ₂|² in a 2×2 panel layout with a shared horizontal axis makes the node-to-peak correspondence and the zero-point energy argument (ψ₁ has no nodes, cannot be the zero-energy flat state) immediately verifiable by inspection.

---

### BLOCK 1 — ILLUSTRAE PASTE BLOCK

Draw a two-by-two grid of panels sharing a common horizontal position axis from zero to L. The top-left panel shows ψ₁, a single smooth half-period sine arch, positive throughout the interior, going to zero at both walls; it has no interior zero crossings. The top-right panel shows ψ₂, a full-period sine that crosses zero once at x = L/2, with one positive arch on the left and one negative arch on the right. The bottom-left panel shows |ψ₁|², a single smooth hill centered at x = L/2, with the axis starting at zero. The bottom-right panel shows |ψ₂|², two separate hills of equal height at x = L/4 and x = 3L/4, separated by a zero at x = L/2, with the axis starting at zero. In each panel, draw small filled circular markers at the interior zero crossings of the eigenstate or probability density to make nodes visually explicit. Use distinct contrasting fills for the ψ panels versus the |ψ|² panels. All vertical axes start at zero; do not clip the negative lobe of ψ₂. Include no baked text.

---

### BLOCK 2 — FULL SCOPE

**[S]** Single-column, 89 mm wide, 300 DPI, vector, white background.

**[C]** Chapter 5 content only. Concepts: ψ₁(x) = √(2/L)sin(πx/L) — no interior nodes; ψ₂(x) = √(2/L)sin(2πx/L) — one interior node at L/2; |ψ₁|² = (2/L)sin²(πx/L) — one peak; |ψ₂|² = (2/L)sin²(2πx/L) — two peaks; zero-point energy: ψ₁ is the lowest non-trivial mode because it has the minimum spatial frequency consistent with vanishing at both walls; the negative lobe of ψ₂ is physically real and must be shown. Inferred relation: the node count of ψ_n and the peak count of |ψ_n|² differ by one in a consistent pattern — the figure should make this countable.

**[O]** 2×2 grid. Top row: wave function panels (ψ₁ left, ψ₂ right). Bottom row: probability density panels (|ψ₁|² left, |ψ₂|² right). Shared horizontal position axis at bottom of each column, 0 to L, no tick labels. Vertical axes: ψ panels include zero-crossing line at midheight (thin neutral gray, 1 pt dashed); |ψ|² panels have baseline at zero, filled area in light tint. Colors: ψ₁ and |ψ₁|² in active green (#009E73) with corresponding tint fill (#009E73 at 20% opacity); ψ₂ and |ψ₂|² in dominant blue (#0072B2) with tint fill. Node markers: small filled circles, neutral gray (#888888), 3 pt diameter, placed at interior zero crossings of eigenstates. Probability density peaks: no markers needed — shape is self-evident. Panel borders: thin 1 pt neutral gray. No baked text.

**[P]** Flat vector. Okabe-Ito HEX. 1 pt strokes. No baked text. No 3D. White background.

**[E]** Do not include: node-count labels, ψ₁/ψ₂ text annotations, axis tick values, panel headers, |ψ|² formula overlays, or any typographic content. Do not show the potential walls in this figure — focus is on wave function structure only. Do not show eigenstates n = 3 or higher.

---

### BLOCK 3 — NEGATIVE PROMPT

No node-count text, no ψ labels, no panel headers, no axis numbers, no formula text; text labels, words, gibberish letters, titles, captions, decorative borders, realistic textures, drop shadows, gradient backgrounds, photographic elements, dual-headed arrows, hand-drawn styles, human figures, visual clutter, watermarks, red-green color combinations, rainbow color scales, 3D perspective distortion.

---

## Figure 5-3 — Energy Spectrum: n² Spacing as a Bar/Dot Diagram (Critical)

**Rank:** Critical
**Type:** Statistical / energy-level diagram (dot plot or bar chart)
**Heuristic:** PQ — the quantitative claim that E_n ∝ n² (spacing grows as 2n − 1 between successive levels) is a distributional statement about a discrete spectrum. A horizontal bar or dot-on-axis representation with vertical axis starting at zero and levels placed at proportional heights makes the n² acceleration unambiguous and countable. This is a precision quantitative figure; the visual encoding must preserve the proportional gaps.

---

### BLOCK 1 — ILLUSTRAE PASTE BLOCK

Draw a vertical energy axis beginning at zero and a set of five horizontal tick marks or short horizontal line segments placed at heights proportional to 1, 4, 9, 16, and 25 in arbitrary scaled units representing the first five energy levels E₁ through E₅. The vertical spacing between consecutive levels must be proportional to the odd integers 3, 5, 7, 9 — that is, each successive gap is noticeably larger than the one below it. Draw a small filled circle on the vertical axis at each energy level position. Draw a thin vertical line connecting zero to E₁ and additional thin vertical segments between consecutive levels; shade alternate inter-level gaps with light fill to make the growing interval widths visually salient. Do not place any energy level at the zero baseline. Draw the axis starting at zero with a clear gap between the axis origin and the first level E₁. Include no baked text, tick labels, or numbers in the image itself.

---

### BLOCK 2 — FULL SCOPE

**[S]** Single-column, 89 mm wide, 300 DPI, vector, white background.

**[C]** Chapter 5 content only. Concepts: E_n = n²π²ℏ²/(2mL²) for n = 1, 2, 3, 4, 5; the ratios E₁:E₂:E₃:E₄:E₅ = 1:4:9:16:25; the gaps ΔE_n = E_{n+1} − E_n = (2n+1)E₁ grow linearly; the ground state E₁ > 0 (zero-point energy). Inferred relation: the visual acceleration of inter-level spacing encodes the n² law — the figure must make it clear that the levels are not evenly spaced and that each additional level is further from the one below.

**[O]** Single vertical axis, energy, baseline at zero. Five horizontal tick marks or short line segments (3–5 mm wide, 1 pt, dominant blue #0072B2) at positions proportional to 1, 4, 9, 16, 25 on the axis. Filled circles: 4 pt diameter, dominant blue, one per level. Vertical connecting segments between levels: 1 pt neutral gray dashed lines. Alternate inter-level bands (E₁–E₂, E₃–E₄): light gray fill (#F0F0F0) to make growing widths visually countable. Zero-point indicator: small filled circle in anchor blue (#56B4E9) at E₁ height, distinct from the other level markers. Gap width between E₁ and zero: clearly non-zero, about the same as the E₁ baseline position. Overall axis height: sized so that the E₅ level fits within the figure with a small margin. No horizontal position axis needed — this is a one-dimensional diagram. 1 pt strokes.

**[P]** Flat vector. Okabe-Ito HEX. 1 pt strokes. No baked text. No 3D. White background.

**[E]** Do not include: n = 1–5 labels, energy value labels, eV units, axis tick numbers, spacing annotations, "n² scaling" text, or any typographic content. Do not draw the well geometry. Do not include eigenstates in this figure — energy values only.

---

### BLOCK 3 — NEGATIVE PROMPT

No level labels, no n indicators, no energy-unit text, no axis numbers, no "n² scaling" annotation; text labels, words, gibberish letters, titles, captions, decorative borders, realistic textures, drop shadows, gradient backgrounds, photographic elements, dual-headed arrows, hand-drawn styles, human figures, visual clutter, watermarks, red-green color combinations, rainbow color scales, 3D perspective distortion.

---

## Figure 5-4 — Two-State Superposition Sloshing: Probability Density at Four Time Snapshots (Critical)

**Rank:** Critical
**Type:** Comparison panels (shared axis), four-panel temporal sequence
**Heuristic:** MC + VG — the sloshing probability density is the chapter's primary dynamic claim. Four time snapshots at t = 0, T/4, T/2, 3T/4 show the cosine-modulated interference term in all four phases of its oscillation. The critical content constraint is: at t = 0 the distribution is left-heavy with ⟨x⟩(0) ≈ 0.320L (the chapter explicitly corrects the sign: ψ₁ + ψ₂ has constructive interference in the left half, so the peak is near x = L/4). At t = T/2 the distribution is right-heavy and ⟨x⟩ ≈ 0.680L. At t = T/4 and 3T/4 the distribution is symmetric, peaked at both sides equally.

---

### BLOCK 1 — ILLUSTRAE PASTE BLOCK

Draw four horizontally aligned panels sharing the same horizontal position axis from zero to L and the same vertical probability-density axis starting at zero. Each panel shows the probability density |Ψ(x,t)|² for the equal-weight superposition of the first two eigenstates at one of four sequential time snapshots. In the first panel, the probability density is distinctly left-heavy: a single tall peak located at roughly one-quarter of the way across the well, with lower amplitude in the right half. In the second panel, the distribution is approximately symmetric but with two mild humps flanking the center, representing the midpoint when the interference term has passed through zero. In the third panel, the distribution is right-heavy: the tall peak is now located at roughly three-quarters of the way across the well, the mirror image of panel one. In the fourth panel, the distribution returns to approximately symmetric with two mild humps, the mirror of panel two. Draw a small filled downward-pointing triangle or a thin vertical tick mark below each panel's horizontal axis at the position of the mean ⟨x⟩ for that snapshot, indicating leftward displacement in panel one, center in panels two and four, and rightward displacement in panel three. All four panels must share identical y-axis scaling. Include no baked text or labels.

---

### BLOCK 2 — FULL SCOPE

**[S]** Single-column, 89 mm wide, 300 DPI, vector, white background.

**[C]** Chapter 5 content only. Concepts: equal-weight superposition Ψ = (1/√2)(ψ₁e^{−iE₁t/ℏ} + ψ₂e^{−iE₂t/ℏ}); probability density |Ψ|² = ½[ψ₁² + ψ₂² + 2ψ₁ψ₂cos(ω₁₂t)] where ω₁₂ = (E₂ − E₁)/ℏ = 3E₁/ℏ; ⟨x⟩(t) = L/2 − (16L/9π²)cos(ω₁₂t); ⟨x⟩(0) ≈ 0.320L (left-heavy, peak near x = L/4); ⟨x⟩(T/2) ≈ 0.680L (right-heavy, peak near x = 3L/4); ⟨x⟩(T/4) = ⟨x⟩(3T/4) = L/2 (symmetric, interference term zero). At t = 0 the initial state is left-heavy because ψ₁(x) + ψ₂(x) = √(2/L)[sin(πx/L) + sin(2πx/L)] has constructive interference in the left half — this is the chapter's explicitly stated and corrected result. The initial ⟨x⟩ is at rest (cosine at its turning point) and first moves rightward.

**[O]** Four panels side by side, each 20–22 mm wide (fitting 89 mm total with 1 mm gutters). Shared horizontal axis: position 0 to L, no tick labels. Shared vertical axis: probability density, baseline at zero, same scale in all four panels, no tick labels. Fills: smooth filled curve, active green (#009E73) in panels 1 and 3 (where asymmetry is maximum), anchor blue (#56B4E9) in panels 2 and 4 (symmetric midpoints) — this color alternation reinforces the temporal phase relationship. ⟨x⟩ indicator: small filled downward triangle (3 pt, secondary gold #E69F00) placed below the x-axis at the computed mean position for each panel: ≈0.32L in panel 1, ≈0.5L in panels 2 and 4, ≈0.68L in panel 3. Panel borders: thin 1 pt neutral gray vertical lines. Bottom shared axis: 1 pt black. All panels equal width.

**[P]** Flat vector. Okabe-Ito HEX. 1 pt strokes. No baked text. No 3D. White background.

**[E]** Do not include: time labels (t = 0, T/4, etc.), ⟨x⟩ numerical values, axis tick numbers, panel number labels, formula overlays, or any typographic content. Do not show the individual eigenstates ψ₁ and ψ₂ separately. Do not show ⟨H⟩ in this figure — energy constancy is addressed separately. Do not use symmetric bell shapes in panels 1 and 3 — the asymmetry must be pronounced and unmistakably left-heavy in panel 1.

---

### BLOCK 3 — NEGATIVE PROMPT

No time labels, no panel numbers, no ⟨x⟩ numerical annotations, no formula text, no axis numbers, no legend text; text labels, words, gibberish letters, titles, captions, decorative borders, realistic textures, drop shadows, gradient backgrounds, photographic elements, dual-headed arrows, hand-drawn styles, human figures, visual clutter, watermarks, red-green color combinations, rainbow color scales, 3D perspective distortion.

---

## Video Candidate Pass

**Status:** One video candidate identified — strong recommendation.
**Figure:** Figure 5-4 extension — the full-period cosine oscillation of |Ψ(x,t)|² alongside ⟨x⟩(t) as a live trace and ⟨H⟩(t) as a flat line.
**Criterion:** The sloshing probability density is a continuous periodic process whose key pedagogical content — position oscillates, energy does not — requires seeing the motion in real time, not four frozen snapshots.
**Reason:** Four static panels (Figure 5-4) establish the phase structure of the sloshing, but they cannot show the smooth, sinusoidal character of the oscillation, the fact that ⟨x⟩ starts at rest and accelerates rightward (the cosine turning-point behavior at t = 0), or the contrast between a continuously moving probability distribution and a perfectly flat energy line. A 10–15 second loop — showing |Ψ(x,t)|² as a filled animated curve, ⟨x⟩(t) as a dot tracing a cosine below it, and ⟨H⟩(t) as a horizontal flat line in a separate strip — would make the chapter's central dynamical claim viscerally clear in a way no combination of static panels can replicate. The chapter's +1 simulation prompt already specifies exactly this content. This is the single highest-value video candidate in the chapter.
**Not a video because of time/complexity alone:** the pedagogical gap — the contrast between oscillating position expectation and constant energy, including the turning-point start condition — is genuinely inaccessible to static panels without prior understanding of cosine functions and their derivatives. The video closes a specific, identifiable gap.
