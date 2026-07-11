# PEDAGOGY — medhavy-vol1-harmonic-ladder

## What the learner already knows
Energy eigenvalues, operators, the infinite square well result.

## What this reel teaches
The workflow: how to prompt Claude Code to generate a harmonic oscillator
ladder scene, how to read the generated file and verify the n+½ formula
and ℏω spacing, how to run the sim and check two boundary predictions
(uniform spacing, non-zero ground state), how to iterate with a change
command.

## Loop structure
PROMPT → SCRIPT → RUN → CHANGE

## Physics gate numbers
- ℏω ≈ 0.066 eV (ω=10¹⁴ rad/s) ✓ FACTCHECK
- E_0 = ℏω/2 ≈ 0.033 eV > 0 ✓
- E_1 − E_0 = ℏω uniform ✓
- P1: spacing is uniform (test: E_1−E_0 = E_2−E_1 = 0.066 eV)
- P2: E_0 = 0.033 eV > 0 (not zero)

## Medhavy register compliance
- FIRST beat: MedhavyOpen ✓
- LAST beat: MedhavyOutro ✓
- tts: "med dahvy" in narration, "Medhavy" on screen ✓
- No "important to understand" framing ✓
- All Text() in INK ✓

VERDICT: PASS
