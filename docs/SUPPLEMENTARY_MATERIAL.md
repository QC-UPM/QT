---
title: "Supplementary Material: Topological Quantum Transistor"
subtitle: "Repository configuration, matched experiments and reproducibility record"
author:
  - Javier Villalba-Díez
  - Joaquín Ordieres-Meré
date: "Repository documentation revision: 10 September 2026"
lang: en-GB
fontsize: 10pt
geometry: margin=22mm
colorlinks: true
toc: true
header-includes:
  - \renewcommand{\thetable}{S\arabic{table}}
---

# S1. Scope and relationship to the manuscript

This supplement accompanies *Topological Quantum Transistor: A Standardized, Braid-Compiled Primitive for Quantum Feature Learning*. It specifies how the repository's primary notebook, `ablation_TQC.ipynb`, implements the computational study. It complements the manuscript's mathematical description and interpretation with configuration values, experiment identifiers, parameter accounting, execution requirements and artifact provenance.

The primary study is a 12-arm ablation of feature learning on walking-versus-not-walking recordings. **TQT-NB** denotes the audited notebook matrix implementation. A separately repaired logical TQT/QT pair evaluates corrections without silently changing the historical matrix model. None of these simulations constitutes physical anyon preparation, braiding or measurement.

The earlier *Standardized Quantum Transistor Block Enables Differentiable Learning on Gait Dynamics* materials are preserved in `legacy/`. They implement a related but different differentiable QT pipeline. The main manuscript identifies that antecedent as Villalba-Díez and Ordieres-Meré, *Scientific Reports* 16, 9506 (2026), DOI `10.1038/s41598-026-40424-7`. Its historical performance values are not additional matched observations in the present study.

This document was prepared from the supplied manuscript, notebook source and retained notebook output. The recorded execution is identified by `run_0f4dee9df4ca`, with a launch log dated 7 September 2026. Documentation preparation did not repeat training. The original external run directory and input tensors are absent from this snapshot. A saved output is evidence of the supplied execution record, not independent verification of its input data or a replacement for its full prediction artifacts.

\clearpage

# S2. Data representation and validation units

The completed notebook output reports 680 Parquet tensors: 483 not-walking recordings (label 0) and 197 walking recordings (label 1). The loader reads numerical tensors directly, rather than the image previews used in the earlier QT experiments. It ignores hidden metadata and PGM previews. Labels are parsed from filename suffixes; supported legacy aliases do not redefine the completed study's negative class as standing.

Numeric tensor identities include shape and canonical values. The data audit retains every loaded record and its original label, including contradictory labels on identical tensors. In the recorded run, two exact-duplicate sets contain four records, with one mixed-label pair. Connected components join original filename groups, exact-tensor identities and common-prefix collision constraints. This reduces 680 original filename groups to 678 effective groups; the saved output reports no additional common-prefix sets for this run.

The common-prefix check restricts partition membership only. It does not fit a global feature transform. The same connected-component groups are kept disjoint across every outer and inner train/evaluation boundary and are used as bootstrap clusters. These identifiers have not been verified as subject identities; subject-disjoint or clinical generalization is not established.

Three outer folds have train/test sizes 455/225, 452/228 and 453/227. Each outer training partition has three inner folds. The split routine searches deterministic alternatives for feasibility rather than selecting by model performance. It can explicitly reduce requested folds, with a minimum of two outer and two inner folds, or return a diagnostic-only result if the grouped data cannot support the protocol. The supplied completed run retained the requested 3-by-3 design. Actual split decisions belong in the generated split audit and should be checked in any reproduction.

Within each applicable training partition, tensor width is selected, tensors are flattened, scalar normalization is fitted, and PLS or PCA is fitted to 16 output components. Evaluation tensors are transformed using those fitted choices. Inner validation data do not fit the contraction used for their own model selection. After selection, preprocessing is refitted on the outer training data only. A finite 16-column output with zero-variance columns is retained and logged rather than silently replaced with a lower-dimensional pipeline.

\clearpage

# S3. Configuration and feature construction

Table S1 records the default scientific configuration used for the main study. Runtime paths and environment management are documented separately in Section S8.

Table: **Main-study configuration.**

| Component | Setting |
| :--- | :--- |
| Outer/inner validation | 3 outer folds; 3 inner folds; grouped and stratified |
| Initial split seeds | Outer 42; inner 123 |
| Feasibility search | 32 attempts; explicit fold reduction allowed |
| Contraction | PLS or PCA; 16 output components |
| Feature projections | Fixed projection seed 23; widths 8, 6 and 4 |
| Input pooling | Hyperbolic tangent of each projected component vector |
| Codebook | 0.5, 1.0, 1.5, 2.0 |
| Feature scales | Three real scales; fixed starting point (0.8, 0.8, 0.8) |
| Bias target | Controlled RY with angle pi/3; branch-specific implementation |
| Run seeds | 54, 1054, 2054 |
| Scale optimization | Mirrored CEM; 20 epochs; 10 mirrored pairs per epoch |
| CEM spread | Initial sigma 0.3; multiplicative decay 0.97 |
| Scale-search classifier | Balanced logistic regression with C = 1 |
| Head selection grid | C = 0.01, 0.1, 1, 10, 100 |
| Selection metric | Accuracy on inner validation folds |
| Final decision threshold | Probability 0.5, fixed |
| Head standardization | Enabled; fitted on the corresponding training features |
| Head optimization | L-BFGS; 4,000 iterations, with one 5-fold iteration-limit retry on nonconvergence |
| Historical compiler index | Epsilon = 12, fixed |
| Compiler dictionary | Construction depth 8; stored word lengths 0 through 7 |
| Compiler search | 1,024 sampled candidate pairs; seed 20260907 |
| Angle bin spacing | pi/128 |
| Bootstrap | 2,000 paired group-cluster replicates; seed 7319 |
| Numerical runtime | One BLAS thread by default; headless figures; PNG resolution 300 dpi |

All three feature stages act **in parallel** on the same 16-dimensional contracted input. QR-derived fixed projections produce 8, 6 and 4 pooled signals, respectively. For each signal, the four codebook entries scale input-dependent rotation targets. Each motif applies RZ and then RX chronologically. A stage shares one learned scale across its blocks. The block prepares its gate line, applies the input motif on its channel, applies the branch-specific bias and returns three post-bias expectation features, ordered Z, X and Y. Eighteen blocks therefore give 54 classifier inputs.

The feature pipeline is not the older 4-to-3-to-2 cascade. There is no learned linear input projection in this TQT implementation; PLS is itself a supervised fitted front end and must be included in the interpretation of the full pipeline.

In random-frozen arms, one scale vector is drawn per prespecified seed as the fixed starting vector plus 0.3 times a three-dimensional standard normal vector. That draw is shared across folds and is not selected using test performance. CEM evaluates the starting point and 20 candidates per epoch from 10 mirrored pairs. Scale optimization uses a common head regularization C = 1; head regularization is selected afterward using the inner folds. All three stochastic seeds are retained.

\clearpage

# S4. Experiment inventory and parameter accounting

Table S2 uses the exact experiment identifiers exported by the notebook. Every non-majority arm has a balanced logistic-regression head. “Exact notebook motifs” means replacing single-qubit approximations while retaining the notebook's composition; it does not mean that the nominal controlled gate has been repaired.

Table: **Twelve matched arms.** Dimensions count classifier inputs.

| Identifier | Construction | Dim. | Purpose |
| :--- | :--- | ---: | :--- |
| `majority` | Training-majority prediction | 0 | Class-imbalance reference |
| `pls_lr` | PLS directly to logistic head | 16 | Supervised classical front-end baseline |
| `pca_lr` | PCA directly to logistic head | 16 | Unsupervised front-end baseline |
| `tanh_lr` | PLS, fixed projections and tanh | 18 | Classical pooled-feature control |
| `tqt_fixed` | PLS, TQT-NB with fixed scales | 54 | Untrained feature-map control |
| `tqt_random` | PLS, TQT-NB with random frozen scales | 54 | Random-feature control |
| `tqt_trained` | PLS, TQT-NB with CEM scales | 54 | Main learned notebook model |
| `qt_exact` | PLS, exact notebook motifs with CEM | 54 | Remove single-qubit approximation |
| `qt_exact_grid` | PLS, exact motifs with angle rounding and CEM | 54 | Separate angle binning from braid effects |
| `pca_tqt` | PCA, trained TQT-NB | 54 | Complete PLS/PCA by direct/TQT comparison |
| `logical_tqt` | PLS, repaired compiled rotations, exact logical bias, CEM | 54 | Repaired logical sensitivity analysis |
| `logical_qt` | PLS, exact rotations, exact logical bias, CEM | 54 | Matched counterpart to repaired TQT |

The count exported as `trainable_parameters_after_contraction` deliberately excludes the fitted contraction and standardization statistics. A binary logistic head on d features has d+1 coefficients including its intercept. This gives 17 for each direct PLS/PCA head, 19 for the tanh head, and 55 for fixed or random-frozen TQT features. Learned 54-feature arms add three scales, yielding 58. The majority rule is assigned zero. These are **post-contraction counts**, not total training degrees of freedom or physical quantum resources.

The deterministic arms are fitted once per outer fold. Their predictions are reused across seed-indexed summary entries so that contrasts align with the stochastic arms; this does not create independent repeated fits. The random and CEM arms use all three prespecified seeds.

The exact notebook control retains the audited bias composition. The grid-matched exact control additionally preserves canonical angle rounding. The logical pair instead shares an exact block-diagonal controlled-RY(pi/3) bias and differs in the single-qubit compiled versus exact operations. Neither exact control reproduces the older differentiable QT architecture.

\clearpage

# S5. Compiler audit and interpretation of logical operations

The implementation keeps three issues separate from predictive performance:

1. **Phase alignment.** The source selection score uses a non-conjugated phase and is not invariant to global phase. TQT-NB preserves that selection objective. The repaired branch corrects phase alignment; achieved phase-free residuals are measured separately from the historical objective.
2. **Word replay.** The source combines word strings in an order that can replay to a different matrix from the selected product. TQT-NB word strings are diagnostics rather than certified executable programs. The repaired branch corrects the word-order convention and checks replay against the returned matrix.
3. **Gate composition.** The source's nominal Hadamard and controlled-RY compositions do not implement those exact gates. The main notebook/exact-motif comparisons retain the source composition. The separately repaired logical pair uses the intended exact controlled-RY matrix.

The successful compiler branch uses a depth-8 dictionary construction and 1,024 sampled pairs. Dictionary words have at most seven generators, so candidate concatenations have at most fourteen before simplification. Epsilon = 12 is a fixed historical configuration label, not an achieved tolerance or a guarantee of word length. This ablation does not establish a monotonic accuracy-versus-braid-length law.

Canonical angle-bin targets and independent per-key random streams remove first-caller cache dependence. These choices are part of the supplied ablation, not new changes introduced for this repository documentation. The resulting experiment is not a bit-for-bit replay of the historical epsilon sweep. Since epsilon = 12 was historically identified using reported test results on the cohort, the ablation is conditional on that choice rather than an independent validation of its optimality.

The runner exports implementation audits and numerical self-tests before model evaluation. The saved console output reports a vectorized/source feature discrepancy of approximately 2e-15. The complete audit JSON is not included in this snapshot; no additional measured replay errors or achieved braid residual distributions are reconstructed here.

Single-qubit matrices use the logical Fibonacci representation. The evaluation does not propagate a physical leakage sector, synthesize a complete physical two-qubit braid program, simulate realistic device noise or finite-shot sampling, or execute topological hardware. A replay-correct logical word and an accurate matrix simulation do not by themselves establish physical portability or fault tolerance.

\clearpage

# S6. Recorded results and statistical aggregation

Table S3 is transcribed from the final printed summary in the supplied notebook, with proportions converted to percentages. Its underlying six-decimal printed values are extracted into `results/recorded_summary.csv`. The extraction does not retrain models, recover full-precision predictions, or calculate missing uncertainty estimates. Accuracy values agree with the companion manuscript after rounding. For exact notebook motifs, converting the printed balanced-accuracy mean 0.932150 gives 93.22% at two decimals, whereas the manuscript displays 93.21%. The available rounded summary does not resolve that last-decimal discrepancy; the table below follows the printed notebook value.

Table: **Recorded 12-arm summary.** Accuracy is outer-fold mean ± sample SD after averaging run metrics within each fold. Balanced accuracy is the printed fold mean only; its SD is not part of the printed summary extracted here.

| Identifier | Accuracy (%) | Balanced accuracy mean (%) |
| :--- | ---: | ---: |
| `majority` | 71.04 ± 2.01 | 50.00 |
| `pls_lr` | 96.32 ± 1.36 | 95.06 |
| `pca_lr` | 96.03 ± 0.03 | 95.16 |
| `tanh_lr` | 93.96 ± 2.46 | 93.70 |
| `tqt_fixed` | 92.78 ± 2.98 | 92.45 |
| `tqt_random` | 93.13 ± 1.62 | 92.73 |
| `tqt_trained` | 93.72 ± 1.16 | 92.70 |
| `qt_exact` | 93.81 ± 2.27 | 93.22 |
| `qt_exact_grid` | 94.31 ± 1.65 | 93.70 |
| `pca_tqt` | 90.88 ± 0.49 | 89.60 |
| `logical_tqt` | 94.70 ± 0.85 | 93.81 |
| `logical_qt` | 94.01 ± 2.26 | 93.25 |

For fold tables, each metric is averaged over run seeds within an outer fold; the three fold averages determine the displayed mean and sample SD. The folds, rather than nine fold-seed combinations, are the units for that SD. For pooled out-of-fold estimates, a metric is computed for each run's predictions across all held-out records and then averaged across runs. Probabilities are not averaged to create an ensemble. Unequal test-fold sizes mean pooled and unweighted fold estimates need not coincide exactly.

Paired uncertainty uses the same group-cluster resampling weights across arms, retains the run structure, and averages run-wise metrics. The 2,000-replicate percentile intervals are descriptive and conditional on fitted out-of-fold models. They do not refit the training pipeline, remove dependence from overlapping cross-validation training sets, or make seeds independent subjects.

The companion manuscript reports a pooled trained-TQT-NB-minus-direct-PLS difference of -2.60 percentage points, with descriptive 95% interval [-3.87, -1.37]. It reports +0.69 points for the repaired logical TQT minus logical QT, with interval [-0.24, +1.57]. These contrast values are attributed to the manuscript and are not recomputed from the printed summary: reconstructing their intervals requires the original paired prediction artifacts.

The retained results do not establish predictive superiority over direct PLS plus logistic regression. They also do not establish a benefit from scale learning or braid approximation. Intervals containing zero do not demonstrate equivalence. Claims about the older QT's training-curve “switching effect” are outside the questions tested by these 12 arms.

\clearpage

# S7. Historical materials and possible complementary experiments

The legacy quantum notebook uses PennyLane/PyTorch, a trainable linear input contraction from 480 image values to eight signals, and cascaded stages with four, three and two QT blocks. It uses scalar Z outputs, input-dependent Y/X/Z rotations, Adam optimization and HyperBand experiments. Historical classical sections include CNN, DANN, logistic regression and Tiny MLP models. These image-based experiments use random train/validation/test partitions rather than the present grouped nested design.

The legacy README's roughly 45–48 parameter claim does not match the displayed QT implementation. The input projection alone has 480 times 8 plus 8 = 3,848 trainable parameters. Nine blocks with three parameters each bring the total to 3,875. The final classical Tiny MLP section reports 3,857. This differs fundamentally from the main notebook's post-contraction counts and should not be used to imply equal total budgets between the two studies.

Historical scores are preserved as reported, without being reconciled into a new matched comparison. The final Tiny MLP section records accuracy 0.968, whereas the old README and PDF report 1.000 for a classical model. Different sections and outputs require explicit execution provenance before such values can be compared. A shared seed value also does not ensure identical test partitions when different splitting implementations are used.

A complementary experiment could retrain a classical MLP using the same input records, folds, training-only transformations and inner selection discipline as the main ablation. Another could compare the complete older QT architecture under the same evaluation units. These would answer additional questions about classifier capacity or architectural changes. They are proposed extensions, not completed experiments in this release. Isolating compilation itself is already addressed more directly by the main study's exact and repaired logical controls.

\clearpage

# S8. Repository execution, artifacts and citation

The repository root identifies the TQT study as primary. `legacy/` contains the original QT notebooks, original supplement, original requirements and original README, preserved without changing their contents. The main notebook's documentation and default input/output paths have been made repository-relative; its scientific implementation and saved outputs are retained. The historical absolute paths in saved output describe the original execution environment.

Use a dedicated Python environment and the root pinned `requirements.txt`. The notebook's managed recovery supports Python 3.10–3.13. A current environment may be reused if it passes the probe; actual versions are recorded by the runner. The pinned list specifies the recovery environment, not an independently recovered lockfile for the original historical run.

From the repository root, supply Parquet files in `data/outs/` or change `CONFIG['data_dir']`. The first code cell starts execution when run; configure it beforehand. Outputs default to `outputs/R1_M1_ablation/`. A real-data preflight can audit data, splits and contractions without fitting feature models. Synthetic smoke mode reduces budgets and is explicitly excluded from manuscript evidence. Consult `docs/REPRODUCIBILITY.md` for the complete workflow.

A completed run generates data and split manifests; duplicate and contraction diagnostics; configuration, provenance and environment records; numerical audits; a braid inventory; per-arm checkpoints; per-record out-of-fold predictions; fold/seed summaries; paired contrasts; training traces; figures; and a full results PDF. These files have distinct roles: aggregate scores cannot substitute for paired predictions, and a selected matrix cannot substitute for a verified executable word.

This repository snapshot includes the code, saved notebook output, extracted printed summary, extraction provenance and this static supplementary document. It does **not** bundle raw tensors, verified subject mappings, or the original external prediction/audit/checkpoint/report directory. The absence of these artifacts limits independent reproduction and checking of the recorded estimates. This static PDF is not the runner-generated `R1_M1_ablation_report.pdf`.

For an archival release, preserve the exact code version together with whatever original run artifacts are available and state data access separately. The future version-specific Zenodo DOI should identify the repository release, while the companion manuscript is cited for the scientific study. No repository DOI is assigned in this document. `docs/ARCHIVING_AND_CITATION.md` supplies manuscript wording and release notes without asserting that a deposit has already occurred.
