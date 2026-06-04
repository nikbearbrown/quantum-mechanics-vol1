# CAJAL Figure Report — Chapter 4 — The Schrödinger Equation and Stationary States

Recommended: 3 figures, moderate density.

---

## Figure 4-1 — Separation of Variables: TDSE → TISE (Critical)

**Rank:** Critical
**Type:** Flowchart (numbered panels)
**Heuristic:** MC — the separation of variables is a four-stage process (write PDE → apply product ansatz → divide to isolate sides → invoke separation constant) with logical dependencies at each step; each stage alters the mathematical object being handled, making spatial representation essential for tracking what changes and when.

---

### BLOCK 1 — ILLUSTRAE PASTE BLOCK

Draw a vertical flowchart with five distinct rectangular process nodes connected by downward arrows. The first node represents the full time-dependent Schrödinger equation as a partial differential equation with both spatial and temporal derivatives coupled together. The second node shows the product ansatz substitution, indicating the wave function is assumed to be a product of a spatial function and a time function. The third node shows the result after substitution and division, with the left side depending only on time and the right side depending only on space; mark the left side and right side with distinct fills. The fourth node introduces the separation constant E, splitting the equation into two branches via a fork symbol, one branch going to an ordinary differential equation in time only and the other to an ordinary differential equation in space only. The fifth node on the time branch shows the analytic solution, a complex exponential phase rotating at angular frequency proportional to E. The fifth node on the spatial branch labels the result as the time-independent Schrödinger equation, an eigenvalue problem. Connect each node with a single-headed downward arrow. Mark the fork node with a distinctive fill to signal the logical branch. Do not include any text, labels, symbols, or mathematical notation baked into the image; all annotations will be overlaid separately.

---

### BLOCK 2 — FULL SCOPE

**[S]** Single-column, 89 mm wide, 300 DPI, vector, white background.

**[C]** Chapter 4 content only. Concepts: TDSE (PDE, coupled spatial and temporal derivatives); product ansatz Ψ(x,t) = ψ(x)φ(t); division to isolate time-only left side from space-only right side; separation constant E; time ODE yielding φ(t) = e^{−iEt/ℏ}; spatial ODE yielding the TISE Ĥψ = Eψ. Inferred relation: the separation constant E is simultaneously the quantity that labels the time phase and the eigenvalue of the Hamiltonian — this dual identity is the key insight the layout should make visually apparent by placing the E-fork node at center stage.

**[O]** Strictly vertical layout, top to bottom. Five nodes total: node 1 (TDSE rectangle, full-width, top), node 2 (ansatz rectangle, full-width), node 3 (separated-sides rectangle, full-width, with left half and right half shaded differently to distinguish time-side from space-side), node 4 (fork diamond or wide rectangle with two outgoing arrows diverging left-right, representing the two ODEs), node 5-left (time ODE / analytic solution, half-width), node 5-right (TISE eigenvalue problem, half-width). Arrows: single-headed, 1 pt, downward except at fork where they diverge. No dual-headed arrows anywhere. Fork node fill: dominant blue (#0072B2). Time-branch node fill: secondary gold (#E69F00). Space-branch node fill: active green (#009E73). Separation-sides node: left half transitional (#CC79A7), right half anchor (#56B4E9) to visually encode that these two sides are different in character.

**[P]** Flat vector. Okabe-Ito palette as specified. 1 pt strokes throughout. No baked text. No red-green combinations. No gradient or texture fills. No 3D. White background.

**[E]** Do not include: any text, mathematical symbols, variable names, equation content, or annotations of any kind baked into the vector. Do not include decorative icons or physical diagrams of waves. Do not include a timeline axis. Do not show numerical values.

---

### BLOCK 3 — NEGATIVE PROMPT

No ansatz label, no equation text, no E symbol, no arrow labels, no step numbers, no branch labels, no node captions, no variable names; text labels, words, gibberish letters, titles, captions, decorative borders, realistic textures, drop shadows, gradient backgrounds, photographic elements, dual-headed arrows, hand-drawn styles, human figures, visual clutter, watermarks, red-green color combinations, rainbow color scales, 3D perspective distortion.

---

## Figure 4-2 — The Stationary State: A Complex Clock (Important)

**Rank:** Important
**Type:** Structural schematic / conceptual diagram (three-panel)
**Heuristic:** VG — the chapter makes a structural claim that is hard to verify from text alone: Ψ_n rotates as a complex vector at constant angular velocity while |Ψ_n|² stays frozen. The "clock" metaphor requires a spatial comparison showing Re Ψ, Im Ψ, and |Ψ|² simultaneously at two or three time snapshots. Without a figure, students conflate the rotating wave function with a non-stationary probability density.

---

### BLOCK 1 — ILLUSTRAE PASTE BLOCK

Draw three horizontally stacked panels that share the same horizontal position axis running left to right, representing the interior of a one-dimensional well. In the top panel, show a smooth sinusoidal curve at three superimposed time snapshots, each snapshot shifted in vertical amplitude but identical in spatial envelope shape; the three curves should be the same spatial function scaled and reflected, representing the real part of a stationary state as it oscillates between positive peak, zero, and negative peak, rotating like a clock hand. In the middle panel, show the corresponding imaginary part at the same three time snapshots, phase-shifted ninety degrees relative to the top panel: when the top panel curve is at maximum, the middle panel curve is near zero; when the top panel curve is near zero, the middle panel curve is at maximum. Use a different color for the middle panel curves. In the bottom panel, draw a single filled curve — the probability density — that is identical at all three time snapshots, conveying that it does not move. Indicate the identity of the three time snapshots with matched small circular markers or tick marks on a notional phase axis beside the figure, without using text labels. Do not bake any text into the image.

---

### BLOCK 2 — FULL SCOPE

**[S]** Single-column, 89 mm wide, 300 DPI, vector, white background.

**[C]** Chapter 4 content only. Concepts: stationary state Ψ_n(x,t) = ψ_n(x)e^{−iEt/ℏ}; real part Re Ψ_n = ψ_n(x)cos(E_n t/ℏ); imaginary part Im Ψ_n = −ψ_n(x)sin(E_n t/ℏ); probability density |Ψ_n|² = |ψ_n(x)|² independent of time; the 90-degree phase offset between Re and Im components. Inferred relation: the Re and Im components together constitute a rotating two-component vector whose squared modulus is constant — this is the clock metaphor the chapter articulates explicitly.

**[O]** Three vertically stacked horizontal panels, each identical in width and x-axis scale, representing position 0 to L. Top panel: Re Ψ — three superimposed curves at t = 0, t = T/4, t = T/2 in dominant blue (#0072B2), varying in signed amplitude, all with the same spatial envelope. Middle panel: Im Ψ — three superimposed curves at the same three times in secondary gold (#E69F00), ninety degrees out of phase from top panel. Bottom panel: |Ψ|² — single filled region in anchor blue (#56B4E9); the same curve drawn three times coincides exactly, visually encoded by making it a solid filled area rather than three offset lines. Phase indicators: three small filled circles of matching colors on a small vertical phase-clock icon at right margin (no text). Panel dividers: thin neutral gray lines. Axes: thin 1 pt lines, no tick labels or numbers.

**[P]** Flat vector. Okabe-Ito HEX as above. 1 pt strokes. No baked text. No 3D. White background.

**[E]** Do not include: time labels, t = 0 annotations, axis tick values, panel title text, equation overlays, the word "frozen," clock icons with hands, or any typographic content baked into the image. Do not include arrows showing direction of rotation.

---

### BLOCK 3 — NEGATIVE PROMPT

No time labels, no panel titles, no axis numbers, no equation overlays, no clock hands, no rotation arrows, no legend text; text labels, words, gibberish letters, titles, captions, decorative borders, realistic textures, drop shadows, gradient backgrounds, photographic elements, dual-headed arrows, hand-drawn styles, human figures, visual clutter, watermarks, red-green color combinations, rainbow color scales, 3D perspective distortion.

---

## Figure 4-3 — Single Eigenstate vs. Two-State Superposition: What "Stationary" Means (Important)

**Rank:** Important
**Type:** Comparison panels (shared axis)
**Heuristic:** VG + MC — the chapter's central claim is that a single eigenstate is stationary while a superposition of two eigenstates is not. This requires a direct side-by-side structural comparison at two time snapshots, showing probability density frozen on the left and sloshing on the right. The cross-term oscillation is a structural claim (the interference term beats at ω₁₂) that becomes invisible without a spatial comparison.

---

### BLOCK 1 — ILLUSTRAE PASTE BLOCK

Draw a two-column comparison figure. The left column shows a single eigenstate scenario: two panels vertically stacked, each depicting the probability density over position from zero to L. Both panels in the left column are identical — the same bell-shaped half-sinusoid squared — indicating that the probability density does not change between the first time snapshot and the second. The right column shows a two-state superposition scenario: two panels vertically stacked with the same horizontal scale. The top-right panel shows a probability density peaked toward the left half of the well, representing the state at an early time when constructive interference concentrates weight near the left wall. The bottom-right panel shows the same probability density peaked toward the right half of the well at a later time, after half a beat period has elapsed. Draw horizontal position axes at the bottom of each pair of panels. The two columns share a common time-axis indicator at the far left using two horizontal bands labeled only by position, not text. Use contrasting fills for the two columns to make the frozen versus sloshing distinction immediate. Include no baked text.

---

### BLOCK 2 — FULL SCOPE

**[S]** Single-column, 89 mm wide, 300 DPI, vector, white background.

**[C]** Chapter 4 content only. Concepts: single eigenstate |ψ₁(x)|² = (2/L)sin²(πx/L), time-independent; superposition |Ψ(x,t)|² = ½[ψ₁² + ψ₂² + 2ψ₁ψ₂cos(ω₁₂t)] oscillating at beat frequency ω₁₂ = (E₂ − E₁)/ℏ; the cross-term as the source of time dependence; the initial state being left-heavy (peak near x = L/4) because ψ₁ + ψ₂ has constructive interference in the left half; the half-period state being right-heavy. Inferred relation: the presence or absence of the interference cross-term is the binary distinction between stationary and non-stationary behavior.

**[O]** Two columns, two rows. Column 1 (stationary): fill color neutral light gray for both panels, identical density shapes — smooth half-sinusoid bell, symmetric about L/2. Column 2 (superposition): top panel fill active green (#009E73) with peak shifted left of center; bottom panel fill anchor blue (#56B4E9) with peak shifted right of center, mirror of top panel. Shared horizontal position axis at bottom of each column, identical scale 0 to L. Row separator: thin 1 pt neutral gray horizontal line. Column separator: thin 1 pt neutral gray vertical line. Time rows: indicate two time snapshots using small circular markers on a vertical strip at far left — same size, no labels. No arrows inside the panels. Panel proportions: square or slightly landscape. 1 pt strokes throughout.

**[P]** Flat vector. Okabe-Ito HEX as above. No baked text. No 3D. White background.

**[E]** Do not include: column header text, time labels, t = 0 annotations, ψ₁ or ψ₂ labels, "stationary" or "sloshing" text, axis tick numbers, or any typographic content. Do not show the individual eigenstates ψ₁ and ψ₂ separately — only the probability densities |Ψ|².

---

### BLOCK 3 — NEGATIVE PROMPT

No column headers, no time labels, no eigenstate labels, no axis numbers, no equation overlays, no legend text, no "frozen" or "sloshing" annotations; text labels, words, gibberish letters, titles, captions, decorative borders, realistic textures, drop shadows, gradient backgrounds, photographic elements, dual-headed arrows, hand-drawn styles, human figures, visual clutter, watermarks, red-green color combinations, rainbow color scales, 3D perspective distortion.

---

## Video Candidate Pass

**Status:** One video candidate identified.
**Figure:** Figure 4-3 analog — the two-state superposition sloshing over a full beat period.
**Criterion:** The beat-frequency oscillation of |Ψ(x,t)|² in the superposition state is a continuous temporal process where the key insight — probability sloshes while energy does not — requires seeing the motion unfold, not just two snapshots.
**Reason:** Two static comparison panels (Figure 4-3) show the qualitative distinction, but the quantitative periodicity (the cosine modulation at ω₁₂, the exact swing from 0.32L to 0.68L and back) is a dynamic claim that a short looping animation demonstrates in a way static panels cannot. The simulation prompt in the chapter's +1 section already specifies exactly this animation. A 10–15 second loop at ×5 speed showing |Ψ(x,t)|² alongside ⟨x⟩(t) as a live trace below it — with ⟨H⟩ shown as a flat horizontal line — would make the chapter's central contrast (sloshing position, constant energy) immediately visceral.
**Not selected as video alone because:** time and complexity are not sufficient reasons; the reason here is that the continuous periodicity of the beat frequency cannot be inferred from two snapshots without the student already understanding the cosine modulation — a full-period loop closes that gap.
