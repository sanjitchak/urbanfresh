#!/bin/zsh
set -eu

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"

PYTHON_BIN="${PYTHON_BIN:-$(command -v python3)}"
"$PYTHON_BIN" scripts/seo_improver.py >> seo/scheduler.log 2>> seo/scheduler-error.log

EXPORT_ROOT="$(cd "$ROOT/.." && pwd)/urbanfresh-export"
if [[ -f "$EXPORT_ROOT/scripts/seo_improver.py" ]]; then
  (
    cd "$EXPORT_ROOT"
    "$PYTHON_BIN" scripts/seo_improver.py >> seo/scheduler.log 2>> seo/scheduler-error.log
  )
fi
