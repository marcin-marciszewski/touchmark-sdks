#!/usr/bin/env bash
# Regenerate the clients' types and models from openapi/openapi.json.
# Usage: bash scripts/generate.sh [typescript|python]   (default: both)
set -euo pipefail
cd "$(dirname "$0")/.."
what=${1:-all}
case $what in
  all | typescript | python) ;;
  *) echo "Usage: bash scripts/generate.sh [typescript|python]" >&2; exit 2 ;;
esac
if [ "$what" != python ]; then
  (cd typescript && npm run generate)
fi
if [ "$what" != typescript ]; then
  (
    cd python
    # The generator warns about the application/problem+json error answers; it
    # skips only their request code, which is removed below anyway.
    log=$(mktemp)
    uvx --quiet openapi-python-client@0.29.1 generate --path ../openapi/openapi.json \
      --meta none --output-path touchmark/_gen --config openapi-python-client.yaml \
      --overwrite >"$log" 2>&1 || { cat "$log"; rm -f "$log"; exit 1; }
    rm -f "$log"
    rm -rf touchmark/_gen/api touchmark/_gen/client.py touchmark/_gen/errors.py
    printf '"""Models generated from the Touchmark API document; do not edit."""\n' \
      > touchmark/_gen/__init__.py
  )
fi
