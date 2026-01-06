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

MIRCF/
│

├── README.md

│   

├─ Project overview

│   ├─ CI badge

│   ├─ Reproduction instructions

│   ├─ License summary (Non-Commercial)

│
├── LICENSE

│   └─ Creative Commons Attribution-NonCommercial 4.0 International
│
├── CITATION.cff

│   ├─ Author name

│   ├─ ORCID: 0009-0000-4065-3370

│   ├─ Affiliation: Rushford Business School, Switzerland

│   ├─ Paper citation metadata

│
├── AUTHOR_CONTRIBUTIONS.md
│   └─ Formal contribution statement (conceptualization, theory, experiments, writing)

│
├── REPRODUCIBILITY_CHECKLIST.md
│   └─ Reviewer-facing checklist (environment, execution, artifacts, validation)

│
├── Makefile
│   ├─ make reproduce        # full deterministic run

│   ├─ make checksums        # regenerate checksums.txt

│   ├─ make clean            # remove outputs/

│
├── requirements.txt
│   └─ numpy
│      pandas
│      scipy
│      matplotlib
│      nbformat
│      nbconvert
│
├── .python-version
│   └─ 3.12.12
│
├── .pre-commitC
├── .pre-commit-config.yaml
│   └─ notebook normalization
│   └─ nbQA linting
│   └─ dict-mutation guard

│
├── .gitignore
│   └─ outputs/
│   └─ __pycache__/
│   └─ .ipynb_checkpoints/

│
├── .github/
│   └── workflows/
│       ├── ci.yml
│       │   ├─ Python 3.12.12
│       │   ├─ pre-commit enforcement
│       │   ├─ notebook execution (nbconvert)
│       │   ├─ checksum verification
│       │   └─ artifact upload (figures + tables)

│
├── scripts/
│   ├── check_dict_override.py
│   │   └─ forbids dict(**cfg, key=...)
│   ├── generate_checksums.py
│   │   └─ produces checksums.txt
│   └── verify_checksums.py
│       └─ CI checksum comparison
│
├── notebooks/
│   └── MIRCF_Section6_Reproduction.ipynb
│       ├─ RQ1–RQ6 cells (deterministic)
│       ├─ Table generation cells
│       ├─ Quantum RQ5-B extension
│       └─ Paper-numbered outputs
│
├── outputs/                # NOT committed (CI artifact)
│   ├── Fig_6_1_RQ1_Stability.svg
│   ├── Fig_6_1_RQ1_Stability.jpg
│   ├── Fig_6_2_RQ2_EDB.svg
│   ├── Fig_6_3_RQ3_Resonance.svg
│   ├── Fig_6_4_RQ4_Ablation.svg
│   ├── Fig_6_5_RQ5_Scaling.svg
│   ├── Fig_6_6_RQ5_Quantum.svg
│   ├── Fig_6_7_RQ6_Failure.svg
│   ├── Fig_6_8_Table_RQ_Metrics.svg
│   ├── Fig_6_9_Table_DSR_Alignment.svg
│   └── checksums.txt
│
└── Zenodo/
    ├── RELEASE_CHECKLIST.md
    └── metadata.json



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
