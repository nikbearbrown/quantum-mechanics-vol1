"""
Generate all 12 missing figures for QM Vol 1.
Run from the images/ directory:
    cd .../quantum-mechanics-vol1/images && python3 _generate_missing_figs.py
"""

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import matplotlib.patheffects as pe
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch
import warnings
warnings.filterwarnings('ignore')

FIGSIZE = (7, 3.6)
DPI = 200

def savefig(fig, name):
    fig.savefig(name, dpi=DPI, facecolor='white', bbox_inches='tight')
    plt.close(fig)
    print(f"  saved {name}")


# ─────────────────────────────────────────────────────────────
# Fig 02-02  Bragg diffraction geometry (Davisson-Germer)
# ─────────────────────────────────────────────────────────────
def make_02_matter_waves_fig_02():
    fig, axes = plt.subplots(1, 2, figsize=FIGSIZE)
    fig.patch.set_facecolor('white')
    fig.suptitle('Bragg Diffraction — Davisson–Germer Geometry', fontsize=11, fontweight='bold')

    # --- Left panel: single-crystal Bragg geometry ---
    ax = axes[0]
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.set_aspect('equal')
    ax.axis('off')
    ax.set_title('Single-crystal (Davisson–Germer)', fontsize=8.5)

    # Crystal planes — horizontal lines
    d_nm = 0.091   # nm, (111) Ni spacing
    n_planes = 5
    y_planes = [2.0 + i * 1.6 for i in range(n_planes)]
    for y in y_planes:
        ax.plot([1, 9], [y, y], color='tab:gray', lw=1.2, zorder=1)
        # atom dots
        for x in np.linspace(1.5, 8.5, 7):
            ax.plot(x, y, 'o', color='tab:gray', ms=4, zorder=2)

    # Label d
    ax.annotate('', xy=(0.5, y_planes[1]), xytext=(0.5, y_planes[0]),
                arrowprops=dict(arrowstyle='<->', color='black', lw=1))
    ax.text(0.0, (y_planes[0]+y_planes[1])/2, r'$d$', ha='right', va='center', fontsize=9)

    # Incident beam (angle θ from the surface plane → Bragg angle from normal)
    theta_bragg = np.radians(66.6)   # angle from plane (Bragg convention)
    # We draw the beam from upper-left hitting the top plane
    hit_x, hit_y = 5.0, y_planes[0]
    beam_len = 3.0
    # incident from upper-left
    dx_in = -np.cos(theta_bragg)
    dy_in = -np.sin(theta_bragg)
    start_x = hit_x - dx_in * beam_len
    start_y = hit_y - dy_in * beam_len
    ax.annotate('', xy=(hit_x, hit_y),
                xytext=(start_x, start_y),
                arrowprops=dict(arrowstyle='->', color='tab:blue', lw=1.8))
    ax.text(start_x - 0.3, start_y + 0.1, 'incident\nbeam', ha='right', va='bottom',
            fontsize=7.5, color='tab:blue')

    # Reflected beam
    ax.annotate('', xy=(hit_x + beam_len * np.cos(theta_bragg),
                        hit_y + beam_len * np.sin(theta_bragg)),
                xytext=(hit_x, hit_y),
                arrowprops=dict(arrowstyle='->', color='tab:orange', lw=1.8))
    ax.text(hit_x + beam_len * np.cos(theta_bragg) + 0.1,
            hit_y + beam_len * np.sin(theta_bragg),
            'reflected\nbeam', ha='left', va='bottom', fontsize=7.5, color='tab:orange')

    # path-length difference annotation
    ax.text(5.0, y_planes[0] - 1.0,
            r'$2d\sin\theta_B = \lambda$' '\n' r'$\theta_B \approx 66.6°$',
            ha='center', va='top', fontsize=8,
            bbox=dict(boxstyle='round,pad=0.3', fc='lightyellow', ec='gray', alpha=0.8))
    ax.text(5.0, 1.0,
            r'$d = 0.091\ \mathrm{nm}$  (Ni 111 planes)',
            ha='center', va='bottom', fontsize=7.5, style='italic')

    # --- Right panel: polycrystalline rings (G.P. Thomson geometry) ---
    ax2 = axes[1]
    ax2.set_xlim(-1, 1)
    ax2.set_ylim(-1, 1)
    ax2.set_aspect('equal')
    ax2.axis('off')
    ax2.set_title('Polycrystalline film (G. P. Thomson)', fontsize=8.5)

    # Detector screen: circle representing a ring pattern
    theta_arr = np.linspace(0, 2*np.pi, 300)
    for r, lw in [(0.30, 2.5), (0.52, 1.8), (0.70, 1.3), (0.85, 0.9)]:
        ax2.plot(r * np.cos(theta_arr), r * np.sin(theta_arr),
                 color='tab:blue', lw=lw, alpha=0.85)

    # Central beam spot
    ax2.plot(0, 0, 'o', color='white', ms=6, zorder=5,
             markeredgecolor='tab:blue', markeredgewidth=1.5)
    ax2.text(0, -0.98, 'Debye–Scherrer rings\n(all orientations present)',
             ha='center', va='bottom', fontsize=8)
    ax2.text(0.32, 0.02, r'$n\!=\!1$', fontsize=7, color='tab:blue', ha='left')
    ax2.text(0.54, 0.02, r'$n\!=\!2$', fontsize=7, color='tab:blue', ha='left')

    plt.tight_layout(rect=[0, 0, 1, 0.93])
    savefig(fig, '02-matter-waves-fig-02.png')


# ─────────────────────────────────────────────────────────────
# Fig 02-03  Single-electron buildup (Tonomura-style)
# ─────────────────────────────────────────────────────────────
def make_02_matter_waves_fig_03():
    rng = np.random.default_rng(42)

    # Two-slit interference intensity:  I(y) ∝ cos²(π·d·y/(λ·D)) · envelope
    def intensity(y, slit_sep=0.5, width=0.12, n_fringes=6):
        # single-slit envelope
        u = np.pi * width * y
        env = np.where(np.abs(u) < 1e-9, 1.0, (np.sin(u)/u)**2)
        # double-slit interference
        phase = np.pi * slit_sep * y
        return env * np.cos(phase)**2

    # Normalise intensity to use as a probability
    y_vals = np.linspace(-4, 4, 2000)
    I_vals = intensity(y_vals)
    I_vals /= I_vals.sum()

    counts = [10, 200, 6000, 70000]
    labels = ['10 electrons', '200 electrons', '6 000 electrons', '70 000 electrons']

    fig, axes = plt.subplots(1, 4, figsize=FIGSIZE, sharey=True)
    fig.patch.set_facecolor('white')
    fig.suptitle('Single-Electron Double-Slit Buildup (after Tonomura 1989)',
                 fontsize=10, fontweight='bold')

    for ax, N, label in zip(axes, counts, labels):
        # Sample electron positions from the interference distribution
        positions = rng.choice(y_vals, size=N, p=I_vals)
        ax.scatter(positions, rng.uniform(0, 1, N),
                   s=0.4 if N > 1000 else (1.5 if N > 100 else 4),
                   color='tab:blue', alpha=0.6, linewidths=0)
        ax.set_xlim(-3.8, 3.8)
        ax.set_ylim(0, 1)
        ax.set_title(label, fontsize=7.5)
        ax.set_xticks([])
        ax.set_yticks([])
        for sp in ['top', 'right', 'left', 'bottom']:
            ax.spines[sp].set_visible(False)
        ax.set_facecolor('black' if N >= 6000 else '#0d0d1a')

    # Add fringe labels on last panel
    axes[-1].text(0.5, -0.08, 'position →', transform=axes[-1].transAxes,
                  ha='center', fontsize=7.5, color='gray')
    axes[0].text(0.5, -0.08, 'position →', transform=axes[0].transAxes,
                 ha='center', fontsize=7.5, color='gray')

    plt.tight_layout(rect=[0, 0, 1, 0.91])
    savefig(fig, '02-matter-waves-fig-03.png')


# ─────────────────────────────────────────────────────────────
# Fig 03-01  Born's timeline: 1926 → footnote → Nobel 1954
# ─────────────────────────────────────────────────────────────
def make_03_wave_function_fig_01():
    fig, ax = plt.subplots(figsize=FIGSIZE)
    fig.patch.set_facecolor('white')
    ax.axis('off')
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 6)
    ax.set_title("Born's Rule — From Footnote to Nobel Prize", fontsize=11, fontweight='bold')

    # Timeline spine
    tl_y = 3.0
    ax.annotate('', xy=(9.5, tl_y), xytext=(0.5, tl_y),
                arrowprops=dict(arrowstyle='->', color='tab:gray', lw=2))

    events = [
        (1.5,  '1926',   'Born submits\nscattering paper\n(original draft:\n'
                         r'$P \propto \psi$)', 'tab:blue'),
        (4.2,  '1926\n(footnote)', 'Added in proof:\n'
                                   r'$P \propto |\psi|^2$', 'tab:orange'),
        (7.8,  '1954',   'Nobel Prize\nin Physics\n(28 yr later)', 'tab:green'),
    ]

    for x, yr, txt, col in events:
        ax.plot(x, tl_y, 'o', ms=12, color=col, zorder=5)
        ax.text(x, tl_y - 0.25, yr, ha='center', va='top', fontsize=8, color=col,
                fontweight='bold')
        ax.text(x, tl_y + 0.4, txt, ha='center', va='bottom', fontsize=8,
                bbox=dict(boxstyle='round,pad=0.4', fc='white', ec=col, lw=1.5))

    # Side-by-side expressions at the bottom
    box_kw = dict(boxstyle='round,pad=0.5', lw=1.5)
    ax.text(2.8, 1.2, r'Original draft:  $P \propto \psi$',
            ha='center', va='center', fontsize=10,
            bbox=dict(**box_kw, fc='#ffe0e0', ec='tab:red'))
    ax.text(7.2, 1.2, r'Corrected (footnote):  $P \propto |\psi|^2$',
            ha='center', va='center', fontsize=10,
            bbox=dict(**box_kw, fc='#d4edda', ec='tab:green'))

    ax.annotate('', xy=(5.6, 1.2), xytext=(4.0, 1.2),
                arrowprops=dict(arrowstyle='->', color='black', lw=1.5))
    ax.text(4.8, 1.5, 'corrected\nin proof', ha='center', va='bottom', fontsize=7.5,
            style='italic')

    for sp in ['top', 'right', 'left', 'bottom']:
        ax.spines[sp].set_visible(False)

    plt.tight_layout()
    savefig(fig, '03-the-wave-function-fig-01.png')


# ─────────────────────────────────────────────────────────────
# Fig 03-03  Continuity equation analogy
# ─────────────────────────────────────────────────────────────
def make_03_wave_function_fig_03():
    fig, axes = plt.subplots(1, 2, figsize=FIGSIZE)
    fig.patch.set_facecolor('white')
    fig.suptitle('Conservation Law: Fluid Continuity vs. Quantum Probability',
                 fontsize=10, fontweight='bold')

    titles = ['Fluid mechanics', 'Quantum mechanics']
    colors = ['tab:blue', 'tab:orange']

    for ax, title, col in zip(axes, titles, colors):
        ax.axis('off')
        ax.set_xlim(0, 10)
        ax.set_ylim(0, 10)
        ax.set_title(title, fontsize=10, color=col, fontweight='bold')

        # Box around the content
        rect = FancyBboxPatch((0.3, 0.5), 9.4, 9.0,
                              boxstyle='round,pad=0.2',
                              fc='white', ec=col, lw=1.5)
        ax.add_patch(rect)

    # ---- Fluid side ----
    ax_f = axes[0]
    ax_f.text(5, 8.5, r'$\dfrac{\partial \rho}{\partial t} + \nabla \cdot \mathbf{J}_\mathrm{mass} = 0$',
              ha='center', va='center', fontsize=11)
    ax_f.text(5, 6.8, r'$\rho$ = mass density', ha='center', va='center', fontsize=9)
    ax_f.text(5, 5.9, r'$\mathbf{J}_\mathrm{mass}$ = mass current', ha='center', va='center', fontsize=9)
    ax_f.text(5, 4.8,
              'If no sources/sinks:\ntotal mass is constant',
              ha='center', va='center', fontsize=9,
              bbox=dict(boxstyle='round', fc='#e8f4fd', ec='tab:blue', lw=1))
    # Arrow showing flux
    ax_f.annotate('', xy=(7, 3.2), xytext=(3, 3.2),
                  arrowprops=dict(arrowstyle='->', color='tab:blue', lw=2))
    ax_f.text(5, 2.6, r'$\mathbf{J}_\mathrm{mass}$ flows out', ha='center', va='center',
              fontsize=8.5, color='tab:blue')
    ax_f.text(1, 3.2, r'$\rho_1$', ha='center', va='center', fontsize=10)
    ax_f.text(8.5, 3.2, r'$\rho_2$', ha='center', va='center', fontsize=10)
    ax_f.text(5, 1.5,
              r'$\int \rho\, dV = \mathrm{const}$',
              ha='center', va='center', fontsize=9.5,
              bbox=dict(boxstyle='round', fc='lightyellow', ec='gray'))

    # ---- Quantum side ----
    ax_q = axes[1]
    ax_q.text(5, 8.5,
              r'$\dfrac{\partial |\psi|^2}{\partial t} + \dfrac{\partial J}{\partial x} = 0$',
              ha='center', va='center', fontsize=11)
    ax_q.text(5, 6.8, r'$|\psi|^2$ = probability density', ha='center', va='center', fontsize=9)
    ax_q.text(5, 5.9,
              r'$J = \dfrac{\hbar}{m}\,\mathrm{Im}\!\left(\psi^*\dfrac{\partial\psi}{\partial x}\right)$',
              ha='center', va='center', fontsize=9.5)
    ax_q.text(5, 4.3,
              'Normalization preserved:\ntotal probability = 1 always',
              ha='center', va='center', fontsize=9,
              bbox=dict(boxstyle='round', fc='#fff3e0', ec='tab:orange', lw=1))
    ax_q.annotate('', xy=(7, 3.2), xytext=(3, 3.2),
                  arrowprops=dict(arrowstyle='->', color='tab:orange', lw=2))
    ax_q.text(5, 2.6, r'$J$ flows out', ha='center', va='center',
              fontsize=8.5, color='tab:orange')
    ax_q.text(1, 3.2, r'$|\psi|^2_L$', ha='center', va='center', fontsize=9.5)
    ax_q.text(8.5, 3.2, r'$|\psi|^2_R$', ha='center', va='center', fontsize=9.5)
    ax_q.text(5, 1.5,
              r'$\int_{-\infty}^{\infty} |\psi|^2\, dx = 1$',
              ha='center', va='center', fontsize=9.5,
              bbox=dict(boxstyle='round', fc='lightyellow', ec='gray'))

    plt.tight_layout(rect=[0, 0, 1, 0.93])
    savefig(fig, '03-the-wave-function-fig-03.png')


# ─────────────────────────────────────────────────────────────
# Fig 05-01  Quantum corral schematic (STM standing-wave pattern)
# ─────────────────────────────────────────────────────────────
def make_05_infinite_square_well_fig_01():
    """
    The actual IBM STM image is copyrighted; we produce a faithful physics-correct
    schematic: 48 Fe atoms in a circle, interior electron density as 2D Bessel J0.
    """
    fig, ax = plt.subplots(figsize=FIGSIZE)
    fig.patch.set_facecolor('white')
    ax.set_aspect('equal')
    ax.set_title('Quantum Corral — Crommie, Lutz & Eigler, IBM (1993)\n'
                 '48 Fe atoms on Cu(111): standing-wave electron density inside',
                 fontsize=9.5, fontweight='bold')

    R_corral = 7.13   # Å (physical radius of 48-Fe corral on Cu(111))
    # Place 48 Fe atoms on a circle
    n_atoms = 48
    phi = np.linspace(0, 2*np.pi, n_atoms, endpoint=False)
    ax_atoms_x = R_corral * np.cos(phi)
    ax_atoms_y = R_corral * np.sin(phi)

    # Electron probability density inside circular hard-wall corral.
    # Use the Hankel asymptotic expansion for J0 (accurate for z > ~3)
    # and a simple series for z < 3 — no scipy needed.
    def j0_num(z):
        """Numerically stable J0: power series for small z, asymptotic for large."""
        z = np.asarray(z, dtype=float)
        result = np.empty_like(z)
        small = z < 8.0
        # Power series (converges well for |z| < 8)
        zs = z[small]
        w = (zs / 2.0) ** 2
        term = np.ones_like(zs)
        s = term.copy()
        for k in range(1, 25):
            term = -term * w / (k * k)
            s += term
        result[small] = s
        # Asymptotic form for z >= 8:  J0 ≈ sqrt(2/(πz)) * cos(z - π/4)
        zl = z[~small]
        result[~small] = np.sqrt(2.0 / (np.pi * zl)) * np.cos(zl - np.pi / 4.0)
        return result

    # First four zeros of J0: 2.4048, 5.5201, 8.6537, 11.7915
    chi_vals = [2.4048, 5.5201, 8.6537, 11.7915]

    grid_N = 400
    x_g = np.linspace(-R_corral * 1.05, R_corral * 1.05, grid_N)
    y_g = np.linspace(-R_corral * 1.05, R_corral * 1.05, grid_N)
    X, Y = np.meshgrid(x_g, y_g)
    r_grid = np.sqrt(X**2 + Y**2)

    # The STM images at the Fermi level — dominant contribution is the mode
    # whose energy is closest to E_F.  The corral radius sets k = chi_n1/R
    # where chi_n1 are zeros of J_m (not just J0). For simplicity, use the
    # actual standing-wave solution ψ(r) = J0(chi_03 * r/R) — third zero —
    # which has two interior nodes and therefore shows clear concentric rings.
    # Additionally add the first excited J0 mode to enrich the pattern.

    def j_n1_mode(chi, r):
        """J0(chi * r/R) eigenstates, zeroed outside corral."""
        amp = j0_num(chi * r / R_corral)
        amp[r >= R_corral] = 0.0
        return amp

    # Use modes n=2 and n=3 (chi_vals[1] and chi_vals[2]) for ring visibility
    # These have 1 and 2 interior nodes respectively
    psi2 = j_n1_mode(chi_vals[1], r_grid)   # chi_02 = 5.5201 — 1 interior ring
    psi3 = j_n1_mode(chi_vals[2], r_grid)   # chi_03 = 8.6537 — 2 interior rings

    # Equal mix → shows concentric bull's-eye pattern
    rho = psi2**2 + 0.7 * psi3**2
    rho[r_grid >= R_corral] = 0.0

    from matplotlib.colors import PowerNorm
    im = ax.imshow(rho, extent=[-R_corral*1.05, R_corral*1.05,
                                -R_corral*1.05, R_corral*1.05],
                   origin='lower', cmap='hot', interpolation='bilinear', zorder=1,
                   norm=PowerNorm(gamma=0.4, vmin=0, vmax=rho.max()))

    # Fe atoms
    ax.scatter(ax_atoms_x, ax_atoms_y, s=60, color='cyan',
               edgecolors='white', linewidths=0.5, zorder=5, label='Fe atom')

    ax.set_xlabel(r'$x$ (Å)', fontsize=9)
    ax.set_ylabel(r'$y$ (Å)', fontsize=9)
    ax.legend(fontsize=8, loc='upper right')
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    cbar = fig.colorbar(im, ax=ax, shrink=0.8, pad=0.02)
    cbar.set_label(r'$|\psi|^2$ (arb. units)', fontsize=8)
    cbar.ax.tick_params(labelsize=7)

    plt.tight_layout()
    savefig(fig, '05-the-infinite-square-well-fig-01.png')


# ─────────────────────────────────────────────────────────────
# Fig 06-05  STM geometry schematic
# ─────────────────────────────────────────────────────────────
def make_06_finite_wells_fig_05():
    fig, ax = plt.subplots(figsize=FIGSIZE)
    fig.patch.set_facecolor('white')
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 7)
    ax.axis('off')
    ax.set_title('Scanning Tunneling Microscope — Exponential Sensitivity',
                 fontsize=10, fontweight='bold')

    # Surface
    ax.fill_between([0, 10], [0, 0], [1.2, 1.2], color='tab:gray', alpha=0.4)
    ax.text(5, 0.6, 'Metal surface', ha='center', va='center', fontsize=9, color='gray')

    # STM tip
    tip_base_y = 5.0
    tip_apex_y = 2.8
    tip_x = 5.0
    gap = tip_apex_y - 1.2   # tunneling gap
    ax.fill([tip_x-1.2, tip_x+1.2, tip_x+0.1, tip_x-0.1],
            [tip_base_y, tip_base_y, tip_apex_y, tip_apex_y],
            color='tab:blue', alpha=0.7)
    ax.fill([tip_x-0.1, tip_x+0.1, tip_x, tip_x],
            [tip_apex_y, tip_apex_y, tip_apex_y - 0.4, tip_apex_y - 0.4],
            color='tab:blue', alpha=0.9)
    ax.text(tip_x + 1.5, tip_base_y, 'STM tip', ha='left', va='center',
            fontsize=9, color='tab:blue')

    # Gap annotation
    ax.annotate('', xy=(tip_x + 2.5, 1.2), xytext=(tip_x + 2.5, tip_apex_y),
                arrowprops=dict(arrowstyle='<->', color='black', lw=1.5))
    ax.text(tip_x + 2.7, (1.2 + tip_apex_y)/2, r'$d$', ha='left', va='center', fontsize=12)
    ax.text(tip_x + 3.5, (1.2 + tip_apex_y)/2,
            '(tunneling\ngap)',
            ha='left', va='center', fontsize=7.5)

    # Decaying wave function in the gap
    x_gap = np.linspace(1.2, tip_apex_y, 200)   # using y-axis for spatial decay
    kappa = 1.025   # Å^-1 → decay rate in the gap
    # Convert: x_gap runs from surface to tip_apex in plot y-units
    gap_len = tip_apex_y - 1.2
    y_decay = np.exp(-kappa * 10 * (x_gap - 1.2) / gap_len)  # normalised

    x_plot = tip_x - 1.5 + 1.2 * y_decay   # shift horizontally
    ax.plot(x_plot, x_gap, color='tab:orange', lw=2, label=r'$|\psi|$ in gap')
    ax.text(tip_x - 2.9, 2.0, r'$\psi \propto e^{-\kappa x}$', ha='left', va='center',
            fontsize=9, color='tab:orange')

    # Sensitivity annotation box
    ax.text(0.4, 4.0,
            'One extra Å of gap:\n'
            r'$I \propto e^{-2\kappa d}$' '\n'
            r'$\Rightarrow$ current drops by $\times 7$–$10$' '\n'
            '→ atomic-resolution imaging',
            ha='left', va='center', fontsize=8.5,
            bbox=dict(boxstyle='round,pad=0.5', fc='lightyellow', ec='goldenrod', lw=1.2))

    ax.legend(loc='upper right', fontsize=8.5)
    plt.tight_layout()
    savefig(fig, '06-finite-wells-steps-and-barriers-fig-05.png')


# ─────────────────────────────────────────────────────────────
# Fig 06-06  Rectangular barrier energy diagram + wave function
# ─────────────────────────────────────────────────────────────
def make_06_finite_wells_fig_06():
    fig, ax = plt.subplots(figsize=FIGSIZE)
    fig.patch.set_facecolor('white')
    ax.set_title(r'Rectangular Barrier: $E < V_0$ — Energy Is Constant Throughout',
                 fontsize=10, fontweight='bold')

    # Geometry
    L = 2.0   # barrier width (arbitrary units)
    x_left_end = -4.0
    x_right_start = L
    x_right_end = 6.0
    V0 = 2.0   # barrier height
    E = 0.8    # particle energy
    kappa = 1.2  # decay rate in barrier (arbitrary, representative)
    k1 = 2.0   # wave vector in regions I and III

    # Potential profile (top panel — drawn in the plot)
    # Region I: x < 0
    # Region II: 0 <= x <= L
    # Region III: x > L

    x_pot = [x_left_end, 0, 0, L, L, x_right_end]
    V_pot = [0, 0, V0, V0, 0, 0]
    ax.fill_between(x_pot, V_pot, alpha=0.18, color='tab:gray')
    ax.plot(x_pot, V_pot, color='tab:gray', lw=2, label=r'$V(x)$')

    # Energy level
    ax.axhline(E, color='tab:red', lw=1.8, ls='--', label=r'total energy $E$')
    ax.text(x_right_end - 0.1, E + 0.05, r'$E$', ha='right', va='bottom',
            fontsize=11, color='tab:red')

    # V0 label
    ax.text(L/2, V0 + 0.07, r'$V_0$', ha='center', va='bottom', fontsize=11,
            color='tab:gray')
    ax.axhline(V0, color='tab:gray', lw=0.7, ls=':')

    # Wave function
    amp_wave = 0.55   # drawing amplitude

    # Region I: oscillatory A exp(ik1 x) + B exp(-ik1 x)
    x1 = np.linspace(x_left_end, 0, 300)
    A_inc = 1.0
    B_ref = 0.4
    psi_I = A_inc * np.cos(k1*x1) + B_ref * np.sin(k1*(x1 + 0.5))
    ax.plot(x1, E + amp_wave * psi_I, color='tab:blue', lw=1.8)

    # Region II: decaying C exp(-κx) + D exp(+κx)
    x2 = np.linspace(0, L, 200)
    C = 1.0
    D = 0.08
    psi_II = C * np.exp(-kappa * x2) + D * np.exp(kappa * x2)
    psi_II = psi_II / psi_II[0]  # continuity at x=0
    ax.plot(x2, E + amp_wave * psi_II, color='tab:blue', lw=1.8)

    # Region III: small transmitted oscillatory wave
    x3 = np.linspace(L, x_right_end, 300)
    T_amp = 0.28
    psi_III = T_amp * np.cos(k1 * (x3 - L))
    ax.plot(x3, E + amp_wave * psi_III, color='tab:blue', lw=1.8, label=r'$\psi(x)$')

    # Annotations
    ax.text(-2.5, 0.15, 'Region I\noscillatory', ha='center', fontsize=8,
            color='tab:blue')
    ax.text(L/2, 0.15, 'Region II\nexponential\ndecay', ha='center', fontsize=8,
            color='tab:blue')
    ax.text(4.0, 0.15, 'Region III\noscillatory\n(small amplitude)', ha='center',
            fontsize=8, color='tab:blue')

    ax.text(0, -0.25, r'$x=0$', ha='center', fontsize=8, color='gray')
    ax.text(L, -0.25, r'$x=L$', ha='center', fontsize=8, color='gray')

    # Annotation box
    ax.text(x_left_end + 0.2, V0 * 0.88,
            'E is constant throughout;\nonly character of solution changes',
            ha='left', va='top', fontsize=8,
            bbox=dict(boxstyle='round,pad=0.3', fc='#fff9e6', ec='goldenrod', lw=1))

    ax.set_xlabel(r'$x$', fontsize=10)
    ax.set_ylabel('Energy', fontsize=10)
    ax.set_xlim(x_left_end, x_right_end)
    ax.set_ylim(-0.4, V0 * 1.35)
    ax.set_yticks([0, E, V0])
    ax.set_yticklabels(['0', r'$E$', r'$V_0$'], fontsize=9)
    ax.set_xticks([])
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.legend(fontsize=8.5, loc='upper right')

    plt.tight_layout()
    savefig(fig, '06-finite-wells-steps-and-barriers-fig-06.png')


# ─────────────────────────────────────────────────────────────
# Fig 09-01  Fourier duality diagram
# ─────────────────────────────────────────────────────────────
def make_09_operators_fig_01():
    fig, ax = plt.subplots(figsize=FIGSIZE)
    fig.patch.set_facecolor('white')
    ax.axis('off')
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 6)
    ax.set_title('Fourier Duality: Position Space ↔ Momentum Space', fontsize=11,
                 fontweight='bold')

    # Left box: position space
    left_box = FancyBboxPatch((0.4, 1.5), 3.8, 3.0,
                              boxstyle='round,pad=0.3',
                              fc='#ddeeff', ec='tab:blue', lw=2)
    ax.add_patch(left_box)
    ax.text(2.3, 4.1, 'Position space', ha='center', va='center',
            fontsize=10, fontweight='bold', color='tab:blue')
    ax.text(2.3, 3.3, r'state: $\psi(x)$', ha='center', va='center', fontsize=10)
    ax.text(2.3, 2.6, r'$\hat{x} = x\cdot$', ha='center', va='center', fontsize=10)
    ax.text(2.3, 1.9, r'$\hat{p} = -i\hbar\,\partial_x$', ha='center', va='center',
            fontsize=10.5)

    # Right box: momentum space
    right_box = FancyBboxPatch((5.8, 1.5), 3.8, 3.0,
                               boxstyle='round,pad=0.3',
                               fc='#ffeedd', ec='tab:orange', lw=2)
    ax.add_patch(right_box)
    ax.text(7.7, 4.1, 'Momentum space', ha='center', va='center',
            fontsize=10, fontweight='bold', color='tab:orange')
    ax.text(7.7, 3.3, r'state: $\phi(p)$', ha='center', va='center', fontsize=10)
    ax.text(7.7, 2.6, r'$\hat{x} = i\hbar\,\partial_p$', ha='center', va='center',
            fontsize=10)
    ax.text(7.7, 1.9, r'$\hat{p} = p\cdot$', ha='center', va='center', fontsize=10.5)

    # Arrows between the two spaces
    ax.annotate('', xy=(5.7, 3.4), xytext=(4.3, 3.4),
                arrowprops=dict(arrowstyle='->', color='tab:green', lw=2.5))
    ax.text(5.0, 3.7, 'Fourier\ntransform', ha='center', va='bottom', fontsize=8.5,
            color='tab:green')

    ax.annotate('', xy=(4.3, 2.6), xytext=(5.7, 2.6),
                arrowprops=dict(arrowstyle='->', color='tab:purple', lw=2.5))
    ax.text(5.0, 2.3, 'Inverse Fourier\ntransform', ha='center', va='top', fontsize=8.5,
            color='tab:purple')

    # Key identity at bottom
    ax.text(5.0, 0.9,
            r'Both representations of the SAME state — related by $\phi(p) = \mathcal{F}[\psi](p)$',
            ha='center', va='center', fontsize=8.5,
            bbox=dict(boxstyle='round,pad=0.3', fc='lightyellow', ec='gray'))

    plt.tight_layout()
    savefig(fig, '09-operators-and-uncertainty-fig-01.png')


# ─────────────────────────────────────────────────────────────
# Fig 09-02  Classical phase space vs. quantum Hilbert space
# ─────────────────────────────────────────────────────────────
def make_09_operators_fig_02():
    fig, axes = plt.subplots(1, 2, figsize=FIGSIZE)
    fig.patch.set_facecolor('white')
    fig.suptitle(r'Classical vs. Quantum: Simultaneous Definiteness of $x$ and $p$',
                 fontsize=10, fontweight='bold')

    # ---- Classical phase space ----
    ax = axes[0]
    ax.set_title('Classical mechanics', fontsize=10, color='tab:blue')
    ax.set_xlabel(r'position $x$', fontsize=9)
    ax.set_ylabel(r'momentum $p$', fontsize=9)
    ax.set_xlim(-3, 3)
    ax.set_ylim(-3, 3)
    ax.axhline(0, color='lightgray', lw=0.8)
    ax.axvline(0, color='lightgray', lw=0.8)
    # A state is a point
    ax.plot(1.2, 0.8, 'o', ms=14, color='tab:blue', zorder=5)
    ax.annotate(r'state = point $(x_0, p_0)$' '\n' r'$x$ and $p$ both definite',
                xy=(1.2, 0.8), xytext=(0.0, -1.8),
                fontsize=8.5,
                arrowprops=dict(arrowstyle='->', color='tab:blue'),
                bbox=dict(boxstyle='round', fc='#ddeeff', ec='tab:blue', lw=1))
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    # ---- Quantum Hilbert space ----
    ax2 = axes[1]
    ax2.set_title('Quantum mechanics', fontsize=10, color='tab:orange')
    ax2.set_xlim(-4, 4)
    ax2.set_ylim(-0.05, 1.05)
    ax2.set_xlabel(r'$x$', fontsize=9)

    x = np.linspace(-4, 4, 600)

    # Eigenstate of x̂: delta-like spike (narrow Gaussian)
    sigma_x_state = 0.15
    delta_like = np.exp(-x**2 / (2 * sigma_x_state**2))
    delta_like /= delta_like.max()
    ax2.fill_between(x, delta_like, alpha=0.3, color='tab:blue')
    ax2.plot(x, delta_like, color='tab:blue', lw=1.8,
             label=r'$\psi_x$: definite $x$, spread $p$')

    # Eigenstate of p̂: plane wave envelope (spread-out Gaussian)
    sigma_p_state = 1.8
    plane_env = np.exp(-x**2 / (2 * sigma_p_state**2))
    k0 = 3.0
    plane_real = plane_env * np.cos(k0 * x)
    ax2.fill_between(x, 0.5 * (plane_real + 1) * 0.55, 0,
                     alpha=0.2, color='tab:orange')
    ax2.plot(x, 0.5 * (plane_real + 1) * 0.55, color='tab:orange', lw=1.8,
             label=r'$\psi_p$: definite $p$, spread $x$')

    ax2.text(0, 0.98, r'No state has both $\hat{x}$ and $\hat{p}$ definite', ha='center',
             va='top', fontsize=8, style='italic', color='black')
    ax2.text(0, 0.88, r'$[\hat{x},\hat{p}] = i\hbar \neq 0$', ha='center',
             va='top', fontsize=9,
             bbox=dict(boxstyle='round,pad=0.3', fc='lightyellow', ec='gray'))
    ax2.legend(fontsize=7.5, loc='lower right')
    ax2.spines['top'].set_visible(False)
    ax2.spines['right'].set_visible(False)
    ax2.set_yticks([])

    plt.tight_layout(rect=[0, 0, 1, 0.93])
    savefig(fig, '09-operators-and-uncertainty-fig-02.png')


# ─────────────────────────────────────────────────────────────
# Fig 11-01  Quantum sandbox UI schematic
# ─────────────────────────────────────────────────────────────
def make_11_capstone_fig_01():
    fig, ax = plt.subplots(figsize=FIGSIZE)
    fig.patch.set_facecolor('white')
    ax.axis('off')
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 7.2)
    ax.set_title('1D Quantum Sandbox — UI Schematic', fontsize=11, fontweight='bold')

    # Outer window border
    outer = FancyBboxPatch((0.2, 0.2), 9.6, 6.7,
                           boxstyle='round,pad=0.15',
                           fc='#f8f8f8', ec='#555555', lw=1.8)
    ax.add_patch(outer)

    # Title bar
    ax.fill_between([0.2, 9.8], [6.5, 6.5], [6.9, 6.9], color='#4a4a8a', alpha=0.9)
    ax.text(5.0, 6.7, '1D Quantum Sandbox', ha='center', va='center',
            fontsize=10, color='white', fontweight='bold')

    # Mode selector buttons
    for i, (label, col) in enumerate([('Eigensolver', 'tab:blue'),
                                       ('Time Evolution', 'tab:orange')]):
        bx = 1.0 + i * 3.5
        btn = FancyBboxPatch((bx, 6.0), 2.8, 0.42,
                             boxstyle='round,pad=0.1',
                             fc=col, ec='white', lw=1, alpha=0.85)
        ax.add_patch(btn)
        ax.text(bx + 1.4, 6.21, label, ha='center', va='center',
                fontsize=8, color='white', fontweight='bold')

    # Normalization indicator
    norm_box = FancyBboxPatch((7.5, 6.0), 2.1, 0.42,
                              boxstyle='round,pad=0.1',
                              fc='#d4edda', ec='tab:green', lw=1.2)
    ax.add_patch(norm_box)
    ax.text(8.55, 6.21, r'$\int|\psi|^2 dx = 1.000$', ha='center', va='center',
            fontsize=7.5, color='tab:green', fontweight='bold')

    # Potential + energy levels panel
    panel = FancyBboxPatch((0.5, 0.5), 5.8, 5.3,
                           boxstyle='round,pad=0.1',
                           fc='white', ec='tab:gray', lw=1.2)
    ax.add_patch(panel)
    ax.text(3.4, 5.6, 'Potential & Energy Levels', ha='center', va='center',
            fontsize=8.5, color='tab:gray', style='italic')

    # Harmonic oscillator potential V(x) = x^2
    xp = np.linspace(-2.2, 2.2, 200)
    yp = 0.5 + 0.6 * xp**2
    xp_plot = 3.4 + 1.8 * xp / 2.2
    yp_plot = 0.8 + 3.5 * (yp - 0.5) / (0.5 + 0.6*2.2**2 - 0.5)
    ax.fill_between(xp_plot, yp_plot, 0.8, alpha=0.12, color='tab:gray')
    ax.plot(xp_plot, yp_plot, color='tab:gray', lw=1.8)
    ax.text(0.8, 0.72, r'$V(x)$', fontsize=9, color='tab:gray')

    # Energy levels as horizontal lines
    E_levels = [0.5, 1.5, 2.5, 3.5]
    colors_e = ['tab:blue', 'tab:orange', 'tab:green', 'tab:red']
    for n, (E_n, col) in enumerate(zip(E_levels, colors_e)):
        y_level = 0.8 + 3.5 * E_n / (0.5 + 0.6*2.2**2)
        x_left = 3.4 - 1.8 * np.sqrt(2*E_n) / 2.2
        x_right = 3.4 + 1.8 * np.sqrt(2*E_n) / 2.2
        ax.plot([max(x_left, 0.7), min(x_right, 6.1)], [y_level, y_level],
                color=col, lw=1.8, alpha=0.9)
        # Eigenfunction offset on energy level
        xw = np.linspace(max(x_left, 0.7), min(x_right, 6.1), 200)
        xi = (xw - 3.4) / 1.8 * 2.2
        # Hermite polynomials H_n(xi) via recurrence
        def hermite(n_val, x_arr):
            if n_val == 0:
                return np.ones_like(x_arr)
            elif n_val == 1:
                return 2 * x_arr
            H_prev2 = np.ones_like(x_arr)
            H_prev1 = 2 * x_arr
            for k in range(2, n_val + 1):
                H_curr = 2 * x_arr * H_prev1 - 2*(k-1)*H_prev2
                H_prev2, H_prev1 = H_prev1, H_curr
            return H_prev1
        psi_n = hermite(n, xi) * np.exp(-xi**2/2)
        if np.max(np.abs(psi_n)) > 0:
            psi_n /= np.max(np.abs(psi_n))
        ax.plot(xw, y_level + 0.35 * psi_n, color=col, lw=1.2, alpha=0.8)
        ax.text(0.65, y_level, fr'$n={n}$', ha='right', va='center', fontsize=7.5,
                color=col)

    # Right panel: Hamiltonian matrix preview
    rpanel = FancyBboxPatch((6.6, 0.5), 3.1, 5.3,
                            boxstyle='round,pad=0.1',
                            fc='white', ec='tab:gray', lw=1.2)
    ax.add_patch(rpanel)
    ax.text(8.15, 5.6, 'H matrix (tridiagonal)', ha='center', va='center',
            fontsize=8, color='tab:gray', style='italic')
    # Draw a small tridiagonal matrix schematic
    N_small = 5
    cell = 0.48
    x0_m, y0_m = 6.75, 2.8
    for i in range(N_small):
        for j in range(N_small):
            val = ''
            if i == j:
                color_cell = '#aaccff'
                val = r'$2t$'
            elif abs(i-j) == 1:
                color_cell = '#ffddaa'
                val = r'$-t$'
            else:
                color_cell = '#f0f0f0'
                val = ''
            rect = FancyBboxPatch((x0_m + j*cell, y0_m - i*cell), cell*0.93, cell*0.93,
                                  boxstyle='square,pad=0.02',
                                  fc=color_cell, ec='gray', lw=0.6)
            ax.add_patch(rect)
            if val:
                ax.text(x0_m + j*cell + cell*0.46, y0_m - i*cell + cell*0.46,
                        val, ha='center', va='center', fontsize=5.5)

    ax.text(8.15, 2.1, 'boundary rows greyed', ha='center', va='center',
            fontsize=7, color='gray', style='italic')
    # Grey out top-left and bottom-right corners
    for corner_i, corner_j in [(0,0), (N_small-1, N_small-1)]:
        rect2 = FancyBboxPatch((x0_m + corner_j*cell, y0_m - corner_i*cell),
                               cell*0.93, cell*0.93,
                               boxstyle='square,pad=0.02',
                               fc='#cccccc', ec='gray', lw=0.8, alpha=0.7)
        ax.add_patch(rect2)
        ax.text(x0_m + corner_j*cell + cell*0.46,
                y0_m - corner_i*cell + cell*0.46,
                '0', ha='center', va='center', fontsize=5.5, color='gray')

    ax.text(8.15, 1.4,
            'Diagonalize → $E_n$, $\psi_n$',
            ha='center', va='center', fontsize=8.5,
            bbox=dict(boxstyle='round', fc='lightyellow', ec='gray'))
    ax.text(8.15, 0.8,
            r'$N=500$ grid points',
            ha='center', va='center', fontsize=8)

    plt.tight_layout()
    savefig(fig, '11-capstone-a-1d-quantum-sandbox-fig-01.png')


# ─────────────────────────────────────────────────────────────
# Fig 11-02  Tridiagonal Hamiltonian matrix schematic
# ─────────────────────────────────────────────────────────────
def make_11_capstone_fig_02():
    fig, ax = plt.subplots(figsize=FIGSIZE)
    fig.patch.set_facecolor('white')
    ax.axis('off')
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 6.5)
    ax.set_title(r'Tridiagonal Hamiltonian Matrix $\mathbf{H}$ — Finite-Difference Discretisation',
                 fontsize=10, fontweight='bold')

    N = 8   # display size
    cell_w = 0.72
    cell_h = 0.55
    x0 = 0.8
    y0 = 5.6

    col_diag = '#aaccff'
    col_offdiag = '#ffddaa'
    col_boundary = '#dddddd'
    col_zero = 'white'

    for i in range(N):
        for j in range(N):
            is_boundary = (i == 0 or i == N-1 or j == 0 or j == N-1)
            if i == j:
                if is_boundary:
                    fc = col_boundary
                    label = '1'
                    fs = 7
                else:
                    fc = col_diag
                    label = r'$2t_k\!+\!V_j$'
                    fs = 6
            elif abs(i-j) == 1:
                if is_boundary:
                    fc = col_boundary
                    label = '0'
                    fs = 7
                else:
                    fc = col_offdiag
                    label = r'$-t_k$'
                    fs = 7
            else:
                fc = col_zero
                label = '0' if (i == 0 or i == N-1 or j == 0 or j == N-1) else ''
                fs = 7

            rect = FancyBboxPatch((x0 + j*cell_w, y0 - (i+1)*cell_h),
                                  cell_w*0.94, cell_h*0.92,
                                  boxstyle='square,pad=0.03',
                                  fc=fc, ec='#888888', lw=0.7, zorder=2)
            ax.add_patch(rect)
            if label:
                ax.text(x0 + j*cell_w + cell_w*0.47,
                        y0 - i*cell_h - cell_h*0.5,
                        label, ha='center', va='center', fontsize=fs, zorder=3)

    # Bracket annotations
    ax.text(x0 - 0.55, y0 - N*cell_h/2, r'$\mathbf{H}$', ha='center', va='center',
            fontsize=18, color='black')
    ax.text(x0 + N*cell_w + 0.2, y0 - N*cell_h/2,
            r'$\vec{\psi}$', ha='left', va='center', fontsize=14)
    ax.text(x0 + N*cell_w + 0.75, y0 - N*cell_h/2, '=', ha='center', va='center',
            fontsize=14)
    ax.text(x0 + N*cell_w + 1.1, y0 - N*cell_h/2,
            r'$E\,\vec{\psi}$', ha='left', va='center', fontsize=14)

    # Legend
    legend_x = 0.8
    legend_y = 0.55
    for fc, label in [(col_diag, r'diagonal: $2t_k + V_j$  where $t_k = \hbar^2/(2mh^2)$'),
                      (col_offdiag, r'off-diagonal: $-t_k$'),
                      (col_boundary, 'boundary rows/cols (Dirichlet: $\psi=0$)')]:
        patch = FancyBboxPatch((legend_x, legend_y), 0.45, 0.3,
                               boxstyle='square,pad=0.02',
                               fc=fc, ec='#888888', lw=0.7)
        ax.add_patch(patch)
        ax.text(legend_x + 0.6, legend_y + 0.15, label,
                ha='left', va='center', fontsize=8.5)
        legend_x += 0
        legend_y += 0.52

    # Key formula note
    ax.text(5.0, 0.2,
            r'Key: diagonal $= 2t_k$, not $t_k$. Off-diagonal $= -t_k$. '
            r'Confusing them gives $E_n$ wrong by factor 2.',
            ha='center', va='bottom', fontsize=8, style='italic',
            bbox=dict(boxstyle='round', fc='#fff3e0', ec='goldenrod', lw=1))

    plt.tight_layout()
    savefig(fig, '11-capstone-a-1d-quantum-sandbox-fig-02.png')


# ─────────────────────────────────────────────────────────────
# Fig 11-03  FFT index mapping to physical wave vectors
# ─────────────────────────────────────────────────────────────
def make_11_capstone_fig_03():
    fig, axes = plt.subplots(2, 1, figsize=FIGSIZE, height_ratios=[1, 1.4])
    fig.patch.set_facecolor('white')
    fig.suptitle('FFT Output Index Mapping to Physical Wave Vectors\n'
                 '(Split-Step Fourier — mandatory correction)',
                 fontsize=10, fontweight='bold')

    N = 16  # example grid size

    # ---- Top panel: raw FFT index ----
    ax_top = axes[0]
    ax_top.set_xlim(-0.5, N - 0.5)
    ax_top.set_ylim(0, 2.2)
    ax_top.axis('off')
    ax_top.set_title('Raw FFT output indices (0 … N−1)', fontsize=8.5, pad=2)

    for m in range(N):
        col = 'tab:blue' if m < N//2 else 'tab:orange'
        rect = FancyBboxPatch((m + 0.05, 0.5), 0.9, 0.9,
                              boxstyle='square,pad=0.02',
                              fc=col, ec='white', lw=0.8, alpha=0.8)
        ax_top.add_patch(rect)
        ax_top.text(m + 0.5, 0.95, str(m), ha='center', va='center',
                    fontsize=6.5, color='white', fontweight='bold')

    ax_top.text(N//4, 1.65, 'positive frequencies', ha='center', va='bottom',
                fontsize=7.5, color='tab:blue', fontweight='bold')
    ax_top.text(N * 3//4, 1.65, 'negative frequencies\n(wrapped!)', ha='center',
                va='bottom', fontsize=7.5, color='tab:orange', fontweight='bold')
    ax_top.axvline(N//2 - 0.5, color='black', lw=1.5, ls='--')
    ax_top.text(N//2 - 0.5, 2.1, 'N/2', ha='center', va='top', fontsize=7.5)

    # ---- Bottom panel: physical k_m ----
    ax_bot = axes[1]
    k_phys = np.array([m if m < N//2 else m - N for m in range(N)])
    k_phys = k_phys.astype(float)  # units: 2π/(Nh)

    colors_bot = ['tab:blue' if m < N//2 else 'tab:orange' for m in range(N)]
    ax_bot.bar(range(N), k_phys, color=colors_bot, alpha=0.8, edgecolor='white', lw=0.6)
    ax_bot.axhline(0, color='black', lw=0.8)
    ax_bot.set_xlim(-0.5, N - 0.5)
    ax_bot.set_xticks(range(N))
    ax_bot.set_xticklabels([str(m) for m in range(N)], fontsize=6.5)
    ax_bot.set_xlabel('FFT output index $m$', fontsize=9)
    ax_bot.set_ylabel(r'$k_m \cdot \frac{Nh}{2\pi}$', fontsize=9)
    ax_bot.set_title(r'Physical wave vector: $k_m = (2\pi/Nh)\times m$ for $m<N/2$; '
                     r'$(2\pi/Nh)\times(m-N)$ for $m\geq N/2$',
                     fontsize=8.5, pad=3)
    ax_bot.spines['top'].set_visible(False)
    ax_bot.spines['right'].set_visible(False)

    # Annotation: what goes wrong without correction
    ax_bot.text(N * 0.72, -5.5,
                'Without correction: wrong KE\nfor negative-k components → divergence',
                ha='center', va='top', fontsize=7.5, color='tab:red',
                bbox=dict(boxstyle='round,pad=0.3', fc='#ffe0e0', ec='tab:red', lw=1))

    # Legend patches
    from matplotlib.patches import Patch
    legend_elements = [Patch(facecolor='tab:blue', label='positive $k$'),
                       Patch(facecolor='tab:orange', label='negative $k$ (wrapped)')]
    ax_bot.legend(handles=legend_elements, fontsize=8, loc='upper left')

    plt.tight_layout(rect=[0, 0, 1, 0.93])
    savefig(fig, '11-capstone-a-1d-quantum-sandbox-fig-03.png')


# ─────────────────────────────────────────────────────────────
# Run all
# ─────────────────────────────────────────────────────────────
if __name__ == '__main__':
    print("Generating missing figures for QM Vol 1...")

    make_02_matter_waves_fig_02()
    make_02_matter_waves_fig_03()
    make_03_wave_function_fig_01()
    make_03_wave_function_fig_03()
    make_05_infinite_square_well_fig_01()
    make_06_finite_wells_fig_05()
    make_06_finite_wells_fig_06()
    make_09_operators_fig_01()
    make_09_operators_fig_02()
    make_11_capstone_fig_01()
    make_11_capstone_fig_02()
    make_11_capstone_fig_03()

    print("\nDone.")
