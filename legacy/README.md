# Historical Quantum Transistor study

This directory preserves the earlier repository materials for **“Standardized Quantum Transistor Block Enables Differentiable Learning on Gait Dynamics”**, by Javier Villalba-Díez and Joaquín Ordieres-Meré. The companion TQT manuscript identifies this article as *Scientific Reports* **16**, 9506 (2026), DOI `10.1038/s41598-026-40424-7`.

These files are retained as antecedents, not as matched TQT ablation results. Their original bytes have been preserved when moved from the repository root.

| File | Historical role |
| :--- | :--- |
| `quantum_transistor_ablation_Q.ipynb` | PennyLane/PyTorch QT implementation; cascaded 4 → 3 → 2 blocks, scalar Z readout, Adam and HyperBand experiments |
| `quantum_transistor_ablation_Classic.ipynb` | Several classical experiments, including CNN, DANN, logistic and Tiny MLP sections |
| `Standardized_Quantum_Transistor_Block_SupplementaryMaterial.pdf` | Original QT supplement; superseded as the repository's primary supplement by the root TQT PDF |
| `README.original.md` | Original repository description, preserved for provenance |
| `requirements.txt` | Original dependency list, preserved for provenance rather than endorsed as a complete environment |

## Relationship to the main study

The historical pipeline consumes image files in `processed_images/clase_0` and `processed_images/clase_1`. The new main study consumes Parquet tensors, fits PLS/PCA within training partitions, creates parallel triplet features and uses a balanced logistic head. The historical random train/validation/test splits do not reproduce the main study's grouped nested folds. Image filenames have not been mapped to the new tensor manifest in this repository.

The main study's `qt_exact` and `logical_qt` controls retain its own pooling, readout and evaluation protocol. Neither is a rerun of the cascaded QT in this directory.

## Known documentation discrepancies

The original README's estimate of roughly 45–48 parameters is inconsistent with the displayed QT code. `Linear(480, 8)` contains 3,848 trainable parameters; the nine blocks add 27 when three parameters per block are used, giving 3,875 in total. The final Tiny MLP section reports 3,857 parameters. The original supplementary description also should not be treated as a precise inventory of every classical architecture in the notebook.

Historical scores vary between experiments and documentation. For example, the final Tiny MLP section records test accuracy 0.968 and F1 0.9683, whereas the historical README/supplement reports 1.000. The files do not provide a unified provenance mapping that resolves these figures into one matched comparison. Retaining them does not endorse their use in the TQT results table.

The original “switching effect” narrative is a historical interpretation of training curves. Those curves alone do not establish a uniquely quantum causal mechanism, and the new TQT ablation does not test that claim.

## Reuse

Run these notebooks in a separate environment and inspect their paths and imports first. The archived requirements omit dependencies used by some cells, including `torchvision`, `Pillow`, `ray`, `ptflops` and `opencv-python`. No complete historical environment lock or input image dataset is included. Moving the notebooks does not relocate their external datasets; relative data paths resolve against the kernel working directory.

To reuse a baseline as a new TQT experiment, evaluate it on the same recordings and outer/inner partitions, keep preprocessing and selection within training data, document its feature and parameter budget, and export paired out-of-fold predictions. Report such a run as a new experiment rather than reusing the historical score.
