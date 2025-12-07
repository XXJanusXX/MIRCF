📘 MIRCF Interactive Dashboard
Meta-Intentional Reflexive Cybernetic Framework — Classical, Multi-Agent & Quantum Simulation Environment

This repository contains an interactive Jupyter-based dashboard implementing the Meta-Intentional Reflexive Cybernetic Framework (MIRCF), including:

Classical recursive MIRCF dynamics

Multi-agent distributed MIRCF

Ramanujan-inspired regularization of divergent recursions

Reflexive Stability Index (RSI)

Entropy Drift Bound (EDB)

Resonance Metrics (spectral-gap / expander analysis)

Quantum density-matrix simulation mapped from selected classical agents

Full interactive visualization toolkit (heatmaps, trajectories, Lyapunov diagnostics, adjacency graphs)

This environment supports experiments used in Paper 0: “Meta-Intentional Reflexive Cybernetic Framework (MIRCF): A Mathematical Model for Sustainable and Self-Regulating Digital Intelligence.”

🚀 Features
✔ 1. Multi-Agent MIRCF Simulation

N agents evolving under the unified MIRCF equation:

recursive terms (a, b)

Abel–Ramanujan regularization (ε)

RSI corrective term (K_RSI)

EDB entropy corrective term (K_EDB)

coupling term γ with adjacency A

Multiple graph topologies:

Ring lattice

Erdős–Rényi random graph

Random regular graph

Fully connected network

Ramanujan-like bipartite expander (approximate)

✔ 2. Visualization Layer

Automatically generated after each simulation:

Agent state trajectories (with agent highlighting)

RSI heatmap (time × agent)

EDB entropy heatmap (time × agent)

Lyapunov-like stability curve + spectral-gap overlay

Final-state histograms

Graph adjacency visualization (matrix or networkx layout)

These plots map directly to figures in Paper 0.

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

✔ 4. Interactive Dashboard Controls

All parameters adjustable in real time:

N (agents), T (timesteps)

Graph topology settings (degree, ER-p)

MIRCF coefficients (a, b, ε, γ, K_RSI, K_EDB)

Agent highlight selector

Quantum agent selector

Toggle adjacency visualization

"Run simulation" → classical

"Run quantum sim" → quantum

✔ 5. Reproducible Experimental Environment

Fixed RNG seed

Internal LAST_SIM object stores the full simulation

Can be exported for publication or downstream analysis

📁 Files Included
File	Description
mircf_full_notebook.ipynb	Full dashboard notebook (classical + multi-agent + heatmaps + expander graphs + quantum)
README.md	Documentation (this file)
Additional notebooks (optional)	Scalar MIRCF demos, Ablation studies
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

📬 Support

If you want help with:

Creating a PyQt desktop version

Exporting publication-quality figure sets

Matplotlib rendering in JupyterLab: if plots don’t appear, ensure %matplotlib inline or %matplotlib widget (widget backend needs ipympl). Default inline is used; interactive will redraw properly.
