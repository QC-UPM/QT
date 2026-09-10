# Archiving and citation

## Scientific scope of this release

The primary artifact is the 12-arm TQT ablation implementation and its retained execution output. The technical supplement documents how repository settings implement the manuscript protocol. `legacy/` preserves the earlier differentiable QT study as an antecedent. Historical scores are not additional matched TQT experiments.

No Zenodo deposit, release tag or repository DOI has been created by this documentation update. `CITATION.cff` contains the authors and repository title without an invented DOI or release version.

## Suggested manuscript wording

Use the following wording when citing a deposited release; attach the actual repository reference in the manuscript's citation system:

> The accompanying repository provides the 12-arm TQT ablation implementation, retained execution output and technical supplementary material specifying preprocessing, grouped nested evaluation, compiler controls and model comparisons. Materials from the earlier differentiable QT study are archived separately as historical antecedents and are not used as matched controls in the present ablation.

For the current snapshot, the availability statement should also say:

> The repository includes the saved notebook summary but does not include the input tensors or the original external per-record prediction and audit files. The retained results were not independently recomputed during preparation of the repository documentation.

Revise that second statement only if the deposited contents actually change. Cite `Topological_Quantum_Transistor_SupplementaryMaterial.pdf`, especially Tables S1–S3 and Sections S5–S8, for implementation and provenance details. Cite the companion TQT manuscript for scientific conclusions. The older QT article remains a separate antecedent reference, as identified in the manuscript: Villalba-Díez and Ordieres-Meré, *Scientific Reports* 16, 9506 (2026), DOI `10.1038/s41598-026-40424-7`.

## Preparing the Zenodo snapshot

- Include the main notebook, current READMEs, editable and rendered supplement, recorded-summary CSV/provenance, scripts, requirements, citation metadata, license and `legacy/` materials.
- Rebuild the recorded summary and supplementary PDF using the commands in the root README. Confirm the saved notebook outputs remain associated with the documented historical run.
- Decide whether to add the original run-generated prediction/audit files and data access information. They are absent from this snapshot; do not describe them as deposited unless they are included. In particular, retain the data and split manifests, complete configuration/environment, per-record OOF predictions and paired contrasts if available.
- Assign a release version and record the corresponding Git commit. Use the version-specific Zenodo DOI for an exact reproducible citation. Add the real DOI, version and release date to `CITATION.cff` and the README when available.
- Describe raw-data availability separately from code availability. Do not infer a data license from the repository's software license.

The preserved historical notebooks are executable source files, but their external datasets and complete original environments are not bundled. The root dependencies are for the TQT analysis, not a universal environment for every legacy experiment.
