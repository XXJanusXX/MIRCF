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

License

MIT License. See LICENSE.
