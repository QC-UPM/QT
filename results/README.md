# Recorded results and provenance

`recorded_summary.csv` is extracted from the final printed table in the saved stream output of `ablation_TQC.ipynb`. It contains all 12 arms and exactly the displayed columns: accuracy fold mean, accuracy fold SD and balanced-accuracy fold mean. Values are proportions at the printed six-decimal precision.

`recorded_summary_provenance.json` identifies the notebook, saved run identifier, extraction method and SHA-256 hashes of the notebook, concatenated stream outputs and CSV. The notebook hash describes the documented repository copy; the stream hash identifies its retained output. No timestamp or identifier for a newly trained model is created.

To regenerate these files from the current notebook, run from the repository root:

```bash
python scripts/extract_recorded_summary.py
```

The script reads JSON and printed text only. It refuses synthetic smoke output, an incomplete arm table or ambiguous recorded runs. If the notebook is rerun, re-extraction refers to that new saved output; update the README and supplement accordingly rather than assuming they still describe the historical study.

The source run is `run_0f4dee9df4ca`, logged on 2026-09-07. This repository update did not repeat that run. The original per-record OOF predictions, full-precision metrics, paired-bootstrap contrasts, data/split manifests, compiler inventory, checkpoints and generated reports are **not included** here. The printed summary cannot reconstruct them. Contrast intervals mentioned in the supplement are attributed to the supplied manuscript, not derived from this CSV.

The repository's static supplementary PDF documents the experiment; it is distinct from the full PDF report emitted by the study runner. See `../docs/REPRODUCIBILITY.md` for expected generated artifacts and `../docs/ARCHIVING_AND_CITATION.md` for preparing the Zenodo release.
