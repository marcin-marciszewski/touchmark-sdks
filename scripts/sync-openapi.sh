#!/usr/bin/env bash
# Download the public Touchmark API document into openapi/openapi.json.
# Usage: bash scripts/sync-openapi.sh [URL]
# Then run scripts/generate.sh and review the diff.
set -euo pipefail
cd "$(dirname "$0")/.."
url=${1:-https://api.touchmark.dev/v1/openapi.json}
tmp=$(mktemp)
curl -fsS "$url" -o "$tmp"
python3 - "$tmp" openapi/openapi.json <<'PY'
import json
import sys

with open(sys.argv[1]) as source:
    document = json.load(source)
with open(sys.argv[2], "w") as target:
    json.dump(document, target, indent=2, ensure_ascii=False)
    target.write("\n")
PY
rm -f "$tmp"
echo "openapi/openapi.json updated from $url"
