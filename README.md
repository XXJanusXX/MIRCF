# MIRCF
MIRCF

Dashboard: complete features & quick instructions
1) High-level features (what the notebook gives you)

Interactive multi-agent MIRCF simulation (classical):

N agents evolving under the unified MIRCF update.

Several adjacency modes (ring, Erdős–Rényi, random regular, fully connected, ramanujan_bipartite).

Per-agent RSI (Reflexive Stability Index) and per-agent EDB (Entropy Drift Bound).

Enhanced visualization panels:

Agent state trajectories (select/highlight agents).

RSI heatmap (time × agent).

EDB (entropy) heatmap (time × agent).

Lyapunov candidate / stability diagnostic with spectral gap line.

Final value distributions (state and RSI).

Adjacency graph or matrix view (uses networkx if installed).

Quantum extension (agent-specific):

Map selected classical agent → 2×2 density matrix (Bloch vector).

Time evolution of quantum state via simple toy CPTP steps (rotation + depolarization + dephasing).

Plots: purity, von Neumann entropy, Bloch components, linked RSI vs quantum purity.

Saveable runtime state (the simulation stores LAST_SIM in notebook memory for follow-up analysis or scripting).

Lightweight and fast for typical sizes (N ≤ 200, T ≤ few hundred).

2) Controls / Widgets — what each does

Row 1

N — number of agents (default 24).

T — number of timesteps to simulate (default 300).

graph (dropdown) — adjacency mode:

ring — nearest-neighbour ring (low expansion).

erdos_renyi — random graph with parameter p.

random_regular — each node has degree d (attempts networkx then fallback).

fully_connected — dense coupling (complete graph).

ramanujan_bipartite — approximate Ramanujan-like bipartite expander generator.

degree d — used by random_regular and ramanujan_bipartite (how many neighbors).

p (ER) — edge probability used when erdos_renyi chosen.

Row 2

a — primary recursion coefficient (multiplies x_t).

b — secondary recursion coefficient (multiplies x_{t-1}).

eps — Abel / Ramanujan regularization strength (small positive smooths/diverges).

gamma — multi-agent coupling strength (how strongly agents pull toward neighbors).

Row 3

K_RSI — strength of RSI-based corrective term.

K_EDB — strength of EDB (entropy) corrective term.

Plot adjacency checkbox — toggle adjacency visualization.

Run simulation — run the classical multi-agent MIRCF simulation.

Row 4 (quantum & highlight)

Highlight agents — select multiple agents to overlay their time series on the state plot.

Quantum agent — pick a single agent to launch a toy quantum sim for after the classical run.

Run quantum sim for selected agent — run the quantum density simulation for the chosen agent.

3) Plots & what they mean (how to interpret)

Agent state trajectories (mean + highlighted agents)

Shows global mean and selected agent trajectories. Look for convergence, oscillation, or runaway divergence. Convergence → MIRCF stabilizing.

RSI heatmap (time × agent)

RSI ∈ [0,1] in the notebook: higher RSI indicates stronger reflexive coherence/stability for that agent at that time. Patches of low RSI show instability pockets.

EDB heatmap (time × agent)

Higher EDB means higher entropy / uncertainty for that agent. Watch EDB collapse as evidence of MIRCF reducing uncertainty.

Lyapunov candidate V(t)

Aggregate diagnostic combining variance and RSI penalties. A downward trend + low oscillation indicates improved stability. The spectral gap (RM) is overlaid as a red dashed line — larger gap typically means faster stabilization.

Final distributions (histograms)

Compare distribution of final states vs RSI. A tight, centered final state distribution indicates effective regularization.

Adjacency graph / matrix

Visual inspection of connectivity; helps relate graph structure to spectral gap and dynamics.

Quantum plots (per selected agent)

Purity increases as state becomes more pure (lower mixedness).

von Neumann entropy decreases when the quantum state becomes less uncertain.

Bloch components show how the qubit orbits on the Bloch sphere; compare with classical trajectory.

Linked RSI vs purity demonstrates the classical→quantum correspondence: higher RSI tends to correlate with higher purity in the toy model.

4) Step-by-step usage (quick start)

Open the notebook mircf_full_notebook.ipynb in Jupyter / JupyterLab.

Ensure dependencies installed (see section 6).

Run the single big cell (or split it if you prefer editing). The dashboard interface appears.

Choose adjacency mode and N and T. Default ramanujan_bipartite is a good place to start.

Set MIRCF coefficients a, b. Reasonable starting values: a ≈ 1.0–1.2, b ≈ 0.9–1.1.

Set regularization eps small (0.01–0.05). Set gamma (coupling) 0.0–0.3 initially.

Click Run simulation. Wait — the UI will render the plots (should be fast for default sizes).

Inspect RSI & EDB heatmaps and Lyapunov plot. Try adjusting sliders (a, b, eps, gamma) and rerun.

To test quantum mapping: pick a Quantum agent (e.g., 0), then click Run quantum sim for selected agent. The quantum plots appear (linked to the last classical run).

For reproducible experiments, record the slider values and seed (seed is set internally to 42 in the notebook). Use the same values to reproduce the figure later.

5) Recommended experiments for Paper 0 (figures / tables you can produce)

A. Scalar baseline (Figure 1): set N=1, run with/without eps. Plot raw vs regularized trajectory and RSI/EDB.

B. Spectral gap study (Figure 4): fix N (e.g., 100), compare ring, erdos_renyi, random_regular and ramanujan_bipartite at same average degree. Plot Lyapunov V(t) and record spectral gap Δ — produce a table: Δ vs stabilization time (time to V(t) < threshold).

C. Multi-agent heatmaps (Figures 5–7): N=50–200, show RSI & EDB heatmaps for two parameter regimes (weak coupling vs strong coupling). Highlight emergence of clusters.

D. Expander effect (Figure 8): Create side-by-side runs on ER vs Ramanujan-like expanders; plot final distribution histograms and RSI variances.

E. Quantum mapping (Figure 10): For a selected agent, show classical RSI vs quantum purity over time and compute correlation coefficient.

F. Parameter sweep: Grid sweep over (eps, gamma) or (a, b) and produce heatmaps of final RSI mean and final EDB mean.

G. Ablation: Disable RSI or disable EDB correction to show their contribution to stabilization.

6) Installation & environment (dependencies)

Preferred: create a clean environment (conda recommended but pip works):

Conda example:

conda create -n mircf python=3.10 numpy scipy matplotlib ipywidgets networkx notebook
conda activate mircf
jupyter lab


Pip example:

python -m venv mircfenv
source mircfenv/bin/activate
pip install --upgrade pip
pip install numpy scipy matplotlib ipywidgets networkx notebook
jupyter notebook


Optional (for nicer quantum tools): qutip (not required for the toy quantum in the notebook).
If using JupyterLab, enable ipywidgets extension if necessary:

jupyter nbextension enable --py widgetsnbextension


(Recent JupyterLab versions often work out of the box.)

Note about PyQt5: you do not need PyQt5 to run the notebook. PyQt5 is only required if you later want a standalone PyQt desktop dashboard. You previously saw a PyQt crash — if you build a desktop dashboard later I can include safe install and Mac M1 tips.

7) Saving results & reproducibility

The notebook stores the last simulation object in LAST_SIM. From another code cell you can save:

import numpy as np
np.savez("mircf_sim_N24_T300.npz", **LAST_SIM)


Save figures as publication-quality PNG/PDF:

fig.savefig("mircf_rsi_heatmap.png", dpi=300, bbox_inches='tight')


If you want to export a reproducible script, I can refactor the big cell into numbered cells or into a standalone .py that accepts CLI args and writes full experiment outputs.

8) Performance notes & limits

Typical runtime (default N=24, T=300) — < 1s on modern laptop.

Larger N and T increase cost: eigenvalue computations for spectral gap scale as O(N^3) if done naïvely. For N > 500, reduce T or compute approximate spectral gap (via sparse methods).

The notebook is intentionally single-process and CPU-based. If you want GPU acceleration for very large experiments we can refactor to use PyTorch for large vectorized runs.

9) Troubleshooting & tips

No interactive widgets appear: ensure ipywidgets installed and enabled. In notebooks run the widget cell then jupyter nbextension enable --py widgetsnbextension or use JupyterLab extension if needed.

Adjacency graph blank or slow: if N is large, networkx layout is slow. Disable adjacency plotting or set N smaller when you want network layout.

Quantum sim says no classical sim: run Run simulation first (LAST_SIM must exist).

Different random seeds: the notebook uses a fixed rng seed for reproducibility; change if you want different draws.

PyQt crash from earlier: ignore unless you plan to use PyQt dashboard (we can build a robust PyQt version that avoids common macOS pitfalls).

Matplotlib rendering in JupyterLab: if plots don’t appear, ensure %matplotlib inline or %matplotlib widget (widget backend needs ipympl). Default inline is used; interactive will redraw properly.
