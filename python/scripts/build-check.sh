#!/usr/bin/env bash
# Build the wheel, install it in a clean environment, and check that it imports.
set -euo pipefail
cd "$(dirname "$0")/.."
rm -rf dist
uv build --quiet
work=$(mktemp -d)
trap 'rm -rf "$work"' EXIT
uv venv --quiet --python 3.11 "$work/venv"
VIRTUAL_ENV="$work/venv" uv pip install --quiet dist/touchmark-*.whl
"$work/venv/bin/python" - <<'PY'
from touchmark import AsyncTouchmark, Touchmark, TouchmarkError, models

client = Touchmark("vld_live_check")
assert callable(client.email.validate) and issubclass(TouchmarkError, Exception)
assert models.ValidateResponse is not None and AsyncTouchmark is not None
print("wheel import ok")
PY
