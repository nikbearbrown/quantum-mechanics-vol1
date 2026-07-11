# PEDAGOGY — medhavy-vol1-packet-spread

## What the learner already knows
Fourier superposition, free-particle Schrödinger equation, Gaussian integrals, uncertainty principle basics.

## What this reel teaches
The workflow: how to prompt Claude Code to simulate a Gaussian wave packet
spreading over time, read the generated code and verify the σ(t) formula
and doubling-time formula τ=2mσ₀²/ℏ, run the simulation and check two
predictions (centroid moves at classical group velocity, width reaches √2·σ₀
at t=τ), then iterate to annotate the doubling point.

## Loop structure
PROMPT → SCRIPT → RUN → CHANGE

## Physics gate numbers
- σ(t) = σ₀√(1+(ℏt/2mσ₀²)²) ✓ FACTCHECK
- τ = 2mσ₀²/ℏ ≈ 17.3 fs for σ₀=1 nm, m=m_e ✓
- σ(τ) = √2·σ₀ exactly ✓
- v_g = ℏk₀/m (classical velocity) ✓
- P1: centroid moves at v_g
- P2: width reaches √2·σ₀ at t=τ

## Medhavy register compliance
- FIRST beat: MedhavyOpen ✓
- LAST beat: MedhavyOutro ✓
- tts: "med dahvy" in narration, "Medhavy" on screen ✓
- No "important to understand" framing ✓
- All Text() in INK ✓

VERDICT: PASS
