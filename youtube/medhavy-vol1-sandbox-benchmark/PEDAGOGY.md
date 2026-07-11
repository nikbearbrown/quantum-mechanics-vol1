# PEDAGOGY — medhavy-vol1-sandbox-benchmark

## What the learner already knows
Infinite square well analytic spectrum, matrix diagonalization, the tridiagonal
central-difference Hamiltonian structure.

## What this reel teaches
The workflow: how to prompt Claude Code to build a 1D quantum eigensolver,
read the generated code and verify the tridiagonal H structure (diagonal=2t_k,
off-diagonal=-t_k, t_k=ℏ²/2mh²), run the benchmark against the infinite square
well and check two predictions (E₂/E₁=4.000 exactly, fractional error <10⁻⁵
for N=500), then iterate to add a ratio column to the output table.

## Loop structure
PROMPT → SCRIPT → RUN → CHANGE

## Physics gate numbers
- t_k = ℏ²/(2mh²); diagonal = 2t_k + V_j; off-diagonal = -t_k ✓ FACTCHECK
- E₁ ≈ 0.094 eV (L=2 nm, m=m_e) ✓
- E₂/E₁ = 4.000 exactly ✓
- Fractional error in E₁ < 10⁻⁵ for N=500 ✓
- P1: E₂/E₁ = 4.000 ± 0.001
- P2: fractional error in E₁ < 10⁻⁵

## Medhavy register compliance
- FIRST beat: MedhavyOpen ✓
- LAST beat: MedhavyOutro ✓
- tts: "med dahvy" in narration, "Medhavy" on screen ✓
- No "important to understand" framing ✓
- All Text() in INK ✓

VERDICT: PASS
