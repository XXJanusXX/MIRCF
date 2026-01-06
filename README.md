# MIRCF — Meta-Intentional Reflexive Cybernetic Framework

This repository is the official open research artifact accompanying the MIRCF study.
It provides a fully reproducible implementation of the experimental results
reported in Section 6 (RQ1–RQ6).

The artifact follows Design Science Research (DSR) best practices and includes
continuous integration to validate reproducibility.

---

## Contents

- Reproducible Jupyter notebook for RQ1–RQ6
- Programmatic generation of all figures and tables (SVG + JPG)
- Quantum-inspired extension (RQ5)
- Counterfactual safety analysis (RQ6)
- Continuous Integration (CI) for notebook execution

---

## Repository Structure

notebooks/ # Reproducible experiments (canonical artifact)
src/ # Optional modular implementation
paper/ # Paper-facing prose, captions, tables
outputs/ # Generated figures/tables (not committed)
reproducibility/ # Reproduction and environment manifests
.github/ # CI workflow


---

## Quick Start

```
pip install -r requirements.txt

Open and run:

notebooks/MIRCF_Section6_Reproduction.ipynb

All figures and tables will be regenerated in the outputs/ directory.

Reproducibility Guarantee

Deterministic seeds used throughout

No external data dependencies

All figures and tables generated programmatically

Notebook execution validated on every commit via GitHub Actions

Author Contribution Statement

Siddarth L. conceived and designed the Meta-Intentional Reflexive Cybernetic Framework (MIRCF). The author developed the theoretical framework, formulated the research questions, and defined the intrinsic stability, reflexive coherence, entropy regulation, resonance, scalability, and safety metrics used in the study.

The author implemented the complete computational models, simulation environment, and quantum-inspired extension, and conducted all experiments reported in the manuscript. All empirical analyses, ablation studies, scalability evaluations, counterfactual safety tests, and figure and table generation were performed by the author.

The author wrote the manuscript, including the conceptual framework, methodology, results, discussion, and conclusions, and prepared all figures, tables, and supplementary materials. The author also designed, implemented, and validated the full reproducibility artifact, including the deterministic Jupyter notebook, continuous integration workflow, and open research metadata.

The author approved the final version of the manuscript and is solely responsible for the integrity, accuracy, and reproducibility of the work.


License

MIT License. See LICENSE.
