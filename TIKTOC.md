# TIKTOC.md — Quantum Mechanics Vol. 1: Foundations: The Quantum World

**Series:** Quantum Mechanics+1 — A Simulation-First Undergraduate Series (Vol 1 of 5)
**Author:** Nik Bear Brown · Humanitarians AI
**Status:** Seeded from the series TIKTOC; chapters are titled stubs.

---

## Concept
Volume 1 teaches the student to **set up and solve any one-dimensional quantum problem — analytically and by simulation — and explain what the wave function means**, with the +1 simulation layer carried from Volume 1. Course textbook; chapter = week; read in sequence.

**Target course:** Intro/Modern Physics → first undergraduate QM course (sophomore–junior). 15-week map — chapters across Weeks 1–11, with the remaining weeks for the capstone project, review, and exam.

## The +1 Simulation System
Each chapter ends with an LLM Exercise block: the `CLAUDE.md` coding constitution, a copy-paste four-move D3 simulation prompt for the chapter's core object, exploration tasks, and an extension prompt. The Brutalist governing files are generated in Volume 1, Chapter 0 and travel with the student.

## Three-Act Arc
- Act One (1–3): the experiments force quantum mechanics into existence; the wave function and Born's rule arrive.
- Act Two (4–8): the Schrödinger equation and the canonical 1D systems — well, barrier, oscillator, wave packet.
- Act Three (9–11): operators, uncertainty, the first qubit, and a synthesis sandbox.

## Chapter-by-Chapter

| # | Chapter | Capability built (DO) |
|---|---------|----------------------|
| 0 | How to Use the Simulations | Build the three governing files and run the first D3 wave packet |
| 1 | Why Classical Physics Failed: Blackbody, Photoelectric, and the Photon | Explain which experiment each classical model cannot fit, and why | 
| 2 | Matter Waves: de Broglie, Davisson–Germer, and the Double Slit | Compute a de Broglie wavelength and predict an interference pattern | 
| 3 | The Wave Function and Born's Rule | Normalize a state and compute a probability from |psi|^2 | 
| 4 | The Schrödinger Equation and Stationary States | Separate variables and identify a stationary state | 
| 5 | The Infinite Square Well | Solve the well and simulate its superpositions | 
| 6 | Finite Wells, Steps, and Barriers | Match boundary conditions; simulate transmission and the first tunneling | 
| 7 | The Quantum Harmonic Oscillator | Solve by ladder operators and simulate the spectrum | 
| 8 | The Free Particle and Wave Packets | Build a wave packet and watch group velocity and spreading | 
| 9 | Operators, Expectation Values, and Uncertainty | Compute expectation values and verify the uncertainty bound | 
| 10 | Measurement, Superposition, and the Qubit | Predict measurement statistics for a two-state system | 
| 11 | Capstone — A One-Dimensional Quantum Sandbox | Build a configurable 1D solver and defend its physics | 

## Prerequisites
Carried from Volume 0 (Volume 1: ODEs, complex numbers, intro mechanics/waves). Any math gap is covered just-in-time by **Vol. 5 — Math for Quantum Physics**, indexed to each chapter.

## Positioning (one line)
Wave-function-first like Griffiths, scoped to a single course, with a built simulation as the unit of intuition in every chapter.

---
*Full series map, cross-volume prerequisites, the Volume 5 mirror index, and the comparison to other QM textbooks live in `physics-quantum-mechanics-sri/TIKTOC-series.md`.*
