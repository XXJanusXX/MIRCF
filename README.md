📘 MIRCF Interactive Dashboard — README.md
Meta-Intentional Reflexive Cybernetic Framework (MIRCF)
Multi-Agent Simulator + Ramanujan Expanders + Quantum Density Evolution

This repository contains an interactive Jupyter Notebook implementing the full MIRCF dashboard, including:

1.Multi-agent MIRCF recursion

2.Abel/Ramanujan regularization

3.Reflexive Stability Index (RSI)

4.Entropy Drift Bound (EDB)

5.Ramanujan-like bipartite expander graphs

6.Per-agent entropy + RSI heatmaps

7.Agent highlighting & comparisons

8.Spectral gap diagnostics (Resonance Metrics)

9.Quantum density-matrix simulation linked to classical agent states

This dashboard serves as an experimental cockpit for Paper 0 and subsequent MIRCF publications.

🔧 1. Features Overview

✅ Classical MIRCF Layer

Multi-agent MIRCF recursive update

Regularization via Abel/Ramanujan smoothing

Per-agent RSI and EDB computation

Adjustable:

recursion parameters a, b

regularization eps

coupling gamma

entropy & stability strengths K_RSI, K_EDB

✅ Network / Graph Layer

Selectable graph models:

ring

erdos_renyi

random_regular

fully_connected

ramanujan_bipartite (approximate Ramanujan expander generator)

Visual adjacency matrix and optional graph drawing

Automatic spectral-gap calculation (Resonance Metric RM)

✅ Visualization Layer

Agent trajectory plot (with highlight)

RSI heatmap (time × agent)

EDB entropy heatmap (time × agent)

Lyapunov-like stability monitor + spectral gap overlay

Final distribution histograms

Adjacency visualization (matrix or full graph if networkx installed)

✅ Quantum MIRCF Layer

Choose any agent to map into a quantum state

Construct a 2×2 density matrix from the agent’s classical state

CPTP evolution influenced by classical MIRCF values

Plots:

quantum purity

von Neumann entropy

Bloch-vector components

RSI ↔ purity mapping (classical ↔ quantum correspondence)


🖥 2. Controls & Widgets

Simulation Controls

| Control          | Description                                 |
| ---------------- | ------------------------------------------- |
| `N`              | Number of agents                            |
| `T`              | Number of timesteps                         |
| `graph`          | Adjacency generator mode                    |
| `degree d`       | Graph degree (used in regular + expander)   |
| `p (ER)`         | Edge probability (Erdős–Rényi)              |
| `a`, `b`         | Recursion coefficients                      |
| `eps`            | Abel/Ramanujan regularization strength      |
| `gamma`          | Inter-agent coupling strength               |
| `K_RSI`, `K_EDB` | Strength of stability & entropy corrections |
| `Plot adjacency` | Toggle between adjacency matrix/graph       |
| `Run simulation` | Execute classical MIRCF                     |

Quantum Controls

| Control            | Description                             |
| ------------------ | --------------------------------------- |
| `Highlight agents` | Plot chosen agents over the global mean |
| `Quantum agent`    | Select agent to quantize                |
| `Run quantum sim`  | Executes density evolution              |



✔ 3. Quantum MIRCF Simulation


For any selected classical agent:

Classical agent state mapped to a qubit density matrix

Time evolution under a MIRCF-inspired CPTP channel:

unitary rotation

depolarization

dephasing

entropic corrections

Quantum visualizations include:

purity trajectory

von Neumann entropy trajectory

Bloch vector components

RSI ↔ purity linkage plot

This demonstrates MIRCF’s quantum generalization.


📊 4. Interpretation of Outputs


State Trajectories

Shows stabilization, oscillation, divergence, or clustering.

RSI Heatmap

High RSI → high reflexive coherence.
Low RSI → instability or unresolved recursion.

EDB Heatmap

Measures uncertainty / entropy drift across agents.

Lyapunov Diagnostic

Downward trend indicates stability gain.
Overlaid spectral gap shows RM → stability correlation.

Final State Distributions

Assess convergence and regularization quality.

Quantum Outputs

Purity ↑ → agent internally stabilizing

Entropy ↓ → uncertainty reduction

Bloch vector → trajectory on quantum sphere

RSI vs Purity → classical→quantum reflexive link


✔ 5. Reproducible Experimental Environment


Fixed RNG seed

Internal LAST_SIM object stores the full simulation

Can be exported for publication or downstream analysis


🔧 Installation

Recommended: conda environment

conda create -n mircf python=3.10
conda activate mircf
conda install numpy scipy matplotlib networkx ipywidgets notebook


Enable widgets if needed:

jupyter nbextension enable --py widgetsnbextension


Run the dashboard:

jupyter notebook


Then open mircf_full_notebook.ipynb.

Optional: Quantum enhancement (not required for default)

Install QuTiP (if available in your environment):

pip install qutip


The notebook gracefully falls back to numpy-only quantum simulation.

🧭 Usage Instructions

1. Launch the notebook

Open:
mircf_full_notebook.ipynb

Run the main cell — the dashboard UI will appear.

2. Configure the classical simulation

Select:

Agent count N

Timesteps T

Graph topology (ring, erdos_renyi, random_regular, ramanujan_bipartite, etc.)

Recursion coefficients (a, b)

Regularization ε

Coupling γ

Correction parameters (K_RSI, K_EDB)

When ready → click Run simulation.

3. Inspect the plots

You will see:

Mean trajectory + highlighted agents

RSI & entropy heatmaps

Lyapunov diagnostic with graph spectral gap

Final state distribution

Optional adjacency graph

These directly correspond to MIRCF stability metrics.

4. Run the quantum extension

Choose a Quantum agent → click Run quantum sim.

You will see:

Purity over time

Von Neumann entropy

Bloch vector components

Correlation between RSI and purity

5. Export results

Inside a code cell:

import numpy as np
np.savez("mircf_sim_export.npz", **LAST_SIM)


Save any figure:

fig.savefig("rsi_heatmap.png", dpi=300)

🔬 Recommended Experiments (for Paper 0)

Use this dashboard to generate:

1. Scalar MIRCF baseline

Internal reflexive stabilization without coupling.

2. Spectral gap vs stability

Show that Ramanujan-like expanders outperform ER/ring networks.

3. RSI & EDB temporal landscapes

Produce heatmaps to demonstrate reflective coherence formation.

4. Quantum–classical linkage

Plot RSI vs quantum purity.

5. Ablation experiments

Disable RSI or EDB to show their necessity.

6. Parameter sweeps

Generate 2D heatmaps of stabilization success across parameters.

🧩 Architecture Overview
MIRCF Core (recursion + regularization)
│
├── Multi-Agent Layer (N agents, adjacency A)
│   ├─ RSI
│   ├─ EDB
│   ├─ RM (spectral gap)
│   └─ Coupling dynamics
│
├── Visualization Layer
│   ├─ Heatmaps
│   ├─ Trajectories
│   ├─ Lyapunov diagnostics
│   └─ Graph visualization
│
└── Quantum Layer (optional)
    ├─ density matrix ρ_t
    ├─ purity & entropy
    └─ Bloch dynamics

🛠 Troubleshooting
Widgets not appearing?

Run:

pip install ipywidgets
jupyter nbextension enable --py widgetsnbextension

Adjacency graph crashes for large N

Disable "Plot adjacency" or reduce N.

Quantum sim not running

You must run Run simulation first.

Performance slow?

Lower timesteps T or agent count N.
Spectral gap computation is O(N³); consider disabling it for N > 300.

📄 Citation (for academic usage)


If you use this dashboard in research, cite:

Siddarth L., 2025.
Meta-Intentional Reflexive Cybernetic Framework (MIRCF):
A Mathematical Model for Sustainable and Self-Regulating Digital Intelligence.
Working Paper / Preprint.

🤝 Contributing

Pull requests welcome!

Enhancements especially desired:

GPU/parallel batching of MIRCF runs

Efficient spectral-gap approximation

More accurate Ramanujan expander generator

Higher-dimensional quantum MIRCF (qutrits or multi-qubit systems)

Matplotlib rendering in JupyterLab: if plots don’t appear, ensure %matplotlib inline or %matplotlib widget (widget backend needs ipympl). Default inline is used; interactive will redraw properly.
