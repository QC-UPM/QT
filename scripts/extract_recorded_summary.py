#!/usr/bin/env python3
"""Extract the printed 12-arm summary; never execute notebook code or infer scores."""
from pathlib import Path
import csv
import hashlib
import io
import json
import re

ROOT = Path(__file__).resolve().parents[1]
NOTEBOOK = ROOT / "ablation_TQC.ipynb"
COLUMNS = ("model", "accuracy_fold_mean", "accuracy_fold_sd", "balanced_accuracy_fold_mean")
MODELS = (
    "majority", "pls_lr", "pca_lr", "tanh_lr", "tqt_fixed", "tqt_random",
    "tqt_trained", "qt_exact", "qt_exact_grid", "pca_tqt", "logical_tqt", "logical_qt",
)


def main():
    notebook_bytes = NOTEBOOK.read_bytes()
    notebook = json.loads(notebook_bytes)
    streams = []
    for cell in notebook["cells"]:
        for output in cell.get("outputs", []):
            if output.get("output_type") == "stream":
                value = output.get("text", "")
                streams.append(value if isinstance(value, str) else "".join(value))
    text = "".join(streams)
    if "SYNTHETIC SMOKE TEST" in text:
        raise ValueError("Refusing to export smoke output as the recorded study summary.")
    header = re.compile(r"^\s*" + r"\s+".join(COLUMNS) + r"\s*$", re.MULTILINE)
    matches = list(header.finditer(text))
    if len(matches) != 1:
        raise ValueError(f"Expected one printed summary, found {len(matches)}.")
    rows = []
    for line in text[matches[0].end():].splitlines():
        if not line.strip() and not rows:
            continue
        fields = line.split()
        if len(fields) != 4 or fields[0] not in MODELS:
            break
        for value in fields[1:]:
            if not re.fullmatch(r"\d+\.\d{6}", value) or not 0 <= float(value) <= 1:
                raise ValueError(f"Unexpected printed metric: {value}")
        rows.append(dict(zip(COLUMNS, fields)))
    if tuple(row["model"] for row in rows) != MODELS:
        raise ValueError("Missing, duplicate or reordered study arms in recorded summary.")
    run_ids = sorted(set(re.findall(r"\brun_[0-9a-f]{12}\b", text)))
    if len(run_ids) != 1 or "Completed. No historical accuracies were substituted." not in text:
        raise ValueError("Expected a single completed recorded run.")
    target = ROOT / "results"
    target.mkdir(exist_ok=True)
    buffer = io.StringIO(newline="")
    writer = csv.DictWriter(buffer, fieldnames=COLUMNS, lineterminator="\n")
    writer.writeheader()
    writer.writerows(rows)
    csv_bytes = buffer.getvalue().encode()
    (target / "recorded_summary.csv").write_bytes(csv_bytes)
    provenance = {
        "source": "ablation_TQC.ipynb",
        "source_notebook_sha256": hashlib.sha256(notebook_bytes).hexdigest(),
        "source_stream_output_sha256": hashlib.sha256(text.encode()).hexdigest(),
        "summary_csv_sha256": hashlib.sha256(csv_bytes).hexdigest(),
        "recorded_run_id": run_ids[0],
        "method": "Parse final printed summary from retained stream outputs; no code execution or model refitting.",
        "units": "proportions, as printed to six decimal places",
        "aggregation": "Run metrics averaged within each outer fold; mean and sample SD across three outer folds.",
        "limits": "No per-record predictions, bootstrap intervals, or unprinted precision reconstructed.",
    }
    (target / "recorded_summary_provenance.json").write_text(
        json.dumps(provenance, indent=2) + "\n", encoding="utf-8"
    )
    print(f"Extracted {len(rows)} arms from {run_ids[0]}; no models executed.")


if __name__ == "__main__":
    main()
