#!/usr/bin/env bash
# One real call per SDK against the API, with a test key. Run by hand; CI never
# runs it. It costs 2 credits (one email validation per SDK).
#   read -rs TOUCHMARK_API_KEY && export TOUCHMARK_API_KEY
#   bash scripts/live-check.sh [base URL]
set -euo pipefail
cd "$(dirname "$0")/.."
: "${TOUCHMARK_API_KEY:?Set TOUCHMARK_API_KEY to a test key}"
base=${1:-https://api.touchmark.dev}

(cd typescript && npm run --silent build && BASE="$base" node --input-type=module -e '
import { Touchmark } from "./dist/index.js"
const tm = new Touchmark({ baseUrl: process.env.BASE })
const answer = await tm.email.validate({ email: "smoke-test@example.com" })
if (answer.result !== "invalid") throw new Error(`unexpected result ${answer.result}`)
console.log(`typescript: ${answer.result}, ${answer.credits_charged} credit`)
')

(cd python && BASE="$base" uv run --quiet python - <<'PY'
import os

from touchmark import Touchmark

with Touchmark(base_url=os.environ["BASE"]) as tm:
    answer = tm.email.validate(email="smoke-test@example.com")
assert answer.result == "invalid", answer.result
print(f"python: {answer.result}, {answer.credits_charged} credit")
PY
)
