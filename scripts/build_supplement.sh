#!/usr/bin/env bash
# Render the editable supplement without executing any study code.
set -euo pipefail
repo_root="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$repo_root"
pandoc docs/SUPPLEMENTARY_MATERIAL.md \
  --from=markdown --pdf-engine=pdflatex \
  -V fontfamily=lmodern \
  -o Topological_Quantum_Transistor_SupplementaryMaterial.pdf
