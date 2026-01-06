## Repository Structure

```text
MIRCF/
├── README.md
├── LICENSE
├── CITATION.cff
├── AUTHOR_CONTRIBUTIONS.md
├── REPRODUCIBILITY_CHECKLIST.md
├── Makefile
├── requirements.txt
├── .python-version
├── .pre-commit-config.yaml
├── .gitignore
│
├── .github/
│   └── workflows/
│       └── ci.yml
│
├── scripts/
│   ├── check_dict_override.py
│   ├── generate_checksums.py
│   └── verify_checksums.py
│
├── notebooks/
│   └── MIRCF_Section6_Reproduction.ipynb
│
├── outputs/                  # generated (NOT committed)
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
```
# Meta-Intentional Reflexive Cybernetic Framework (MIRCF)

[![CI](https://github.com/XXJanusXX/MIRCF/actions/workflows/ci.yml/badge.svg)](https://github.com/XXJanusXX/MIRCF/actions)

This repository provides the **official, reproducible research artifact** for the paper:

**Meta-Intentional Reflexive Cybernetic Framework (MIRCF)**

The artifact reproduces all empirical results reported in **Section 6** of the paper, including:
- Figures 6.1–6.9
- All ablation and counterfactual experiments
- Classical and quantum-inspired extensions
- Programmatic table figures
- Deterministic checksums for verification

The repository is designed to meet **journal, reviewer, and archival (Zenodo) standards**.

---

## License

This project is released under the  
**Creative Commons Attribution–NonCommercial 4.0 International (CC BY-NC 4.0)** license.

- ✅ Academic and research use permitted  
- ❌ Commercial use prohibited  

See `LICENSE` for full terms.

---

## Citation

If you use this work, please cite it using the provided `CITATION.cff`.

**Author:** Siddarth Laxminarayanan  
**ORCID:** 0009-0000-4065-3370  
**Affiliation:** Research Scholar, Rushford Business School, Switzerland

---

## Quick Start (Reproducibility)

### Requirements
- Python **3.12.12**
- Linux / macOS / Windows
- No GPU required

### Setup
```bash
git clone https://github.com/XXJanusXX/MIRCF.git
cd MIRCF
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
