# Topological Quantum Transistor: matched feature-learning ablation

This repository accompanies **“Topological Quantum Transistor: A Standardized, Braid-Compiled Primitive for Quantum Feature Learning”**, by Javier Villalba-Díez and Joaquín Ordieres-Meré. Its main study is the 12-arm computational ablation in [`ablation_TQC.ipynb`](ablation_TQC.ipynb).

The study compares classical feature pipelines, fixed and learned notebook-based TQT features, exact-rotation controls, and a separately repaired logical TQT/QT pair. **TQT-NB** denotes the audited notebook matrix implementation. It must be distinguished from the intended logical template and the repaired implementation.

The earlier **“Standardized Quantum Transistor Block Enables Differentiable Learning on Gait Dynamics”** project is retained in [`legacy/`](legacy/README.md) as the architectural antecedent. Its cascaded differentiable QT and image-based benchmarks use a different pipeline and evaluation protocol; their historical scores are not matched controls for the present ablation.

## Main finding and evidence status

The supplied notebook contains a completed run on 680 sensor recordings, with three outer folds, three inner folds and three prespecified stochastic run seeds. Filename and duplicate constraints produce 678 effective groups; subject identities are unverified.

| Model | Accuracy, outer-fold mean ± SD (%) |
| :--- | ---: |
| PLS(16) + balanced logistic regression | 96.32 ± 1.36 |
| PLS + fixed TQT-NB + logistic regression | 92.78 ± 2.98 |
| PLS + random-frozen TQT-NB + logistic regression | 93.13 ± 1.62 |
| PLS + trained TQT-NB + logistic regression | 93.72 ± 1.16 |
| PLS + exact notebook motifs + logistic regression | 93.81 ± 2.27 |
| PLS + repaired logical TQT + logistic regression | 94.70 ± 0.85 |
| PLS + logical-CRY QT + logistic regression | 94.01 ± 2.26 |

Run-specific metrics are averaged within each outer fold before computing the mean and sample standard deviation across folds. These are **recorded results**, not a new execution. The full 12-arm summary and its extraction provenance are in [`results/`](results/README.md).

The feature layer does not outperform direct PLS classification in this experiment. The study evaluates simulated matrices and logical operations; it does not demonstrate physical anyon execution, fault tolerance, hardware portability, or verified subject-disjoint generalization.

## Repository contents

| Path | Purpose |
| :--- | :--- |
| [`ablation_TQC.ipynb`](ablation_TQC.ipynb) | Main implementation, numerical audits, nested evaluation, and retained execution output |
| [`docs/SUPPLEMENTARY_MATERIAL.md`](docs/SUPPLEMENTARY_MATERIAL.md) | Editable technical supplement: configuration, 12 arms, parameter accounting, audits and provenance |
| [`Topological_Quantum_Transistor_SupplementaryMaterial.pdf`](Topological_Quantum_Transistor_SupplementaryMaterial.pdf) | Rendered supplement for citation alongside the manuscript |
| [`docs/REPRODUCIBILITY.md`](docs/REPRODUCIBILITY.md) | Data contract, execution instructions, outputs and reproducibility limits |
| [`results/`](results/README.md) | Summary extracted from saved notebook output; not a substitute for per-record predictions |
| [`legacy/`](legacy/README.md) | Unmodified historical QT notebooks, PDF supplement, original README and requirements |
| [`requirements.txt`](requirements.txt) | Pinned TQT analysis stack matching the notebook's managed-recovery requirements |
| [`docs/ARCHIVING_AND_CITATION.md`](docs/ARCHIVING_AND_CITATION.md) | Citation wording and release guidance for the planned Zenodo deposit |

The companion manuscript itself, raw Parquet data, verified subject/session mapping, and original external run artifacts are not included in this repository snapshot.

## Run the main study

Use Python 3.10–3.13 in a dedicated environment; Python 3.12 is a suitable starting point for the notebook's pinned recovery stack.

```bash
python3.12 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python -m pip install jupyterlab
python -m jupyterlab ablation_TQC.ipynb
```

Start Jupyter in the repository root. Place the original tensors in `data/outs/`, or edit `CONFIG['data_dir']` in the first code cell **before executing it**. Outputs default to `outputs/R1_M1_ablation/`. Set `preflight_only=True` for a real-data audit without feature-model fitting; reset it to `False` for the full study.

The notebook runs the analysis in a child process. In automatic runtime mode it can create a dedicated cached environment if its dependency probe fails. `RUNTIME['allow_install']=False` disables managed installation. Synthetic `mode='smoke'` is available for software checks only and uses reduced budgets; its output is not manuscript evidence.

Read the [reproduction guide](docs/REPRODUCIBILITY.md) before running. A fresh full study cannot be reproduced from the code and saved summary alone because the input data are absent.

## Rebuild documentation and extract the recorded summary

```bash
python scripts/extract_recorded_summary.py
bash scripts/build_supplement.sh
```

Summary extraction uses only the Python standard library and never trains a model. PDF generation requires Pandoc and a LaTeX installation with `pdflatex`, Latin Modern and the packages used by Pandoc's default LaTeX template. It does not require the study data.

## Citation and license

Cite the TQT manuscript for the scientific study and the eventual **version-specific Zenodo DOI** for this repository release. No repository DOI has been assigned here. See [`CITATION.cff`](CITATION.cff) and the [citation notes](docs/ARCHIVING_AND_CITATION.md); the older QT article is cited separately as an antecedent.

The existing GNU Affero General Public License, version 3, is retained in [`LICENSE`](LICENSE). This repository does not establish redistribution terms for input data that are not included.
