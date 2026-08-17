#!/usr/bin/env bash
set -euo pipefail

PORT="${1:-4173}"
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

cd "$ROOT"

fix_output_owner() {
  local uid gid
  uid="$(id -u)"
  gid="$(id -g)"

  docker compose -f docker-compose.yml run --rm --no-deps --entrypoint sh jekyll \
    -c "cd /srv/jekyll && chown -R ${uid}:${gid} _site .jekyll-cache 2>/dev/null || chown -R ${uid}:${gid} _site" >/dev/null
}

if [[ -d _site ]]; then
  echo "[preview] Normalizing _site ownership before cleanup/build..."
  fix_output_owner
fi

echo "[preview] Building _site with Jekyll..."
docker compose -f docker-compose.yml run --rm --no-deps jekyll bundle exec jekyll build
fix_output_owner

echo "[preview] Checking for old preview processes on port ${PORT}..."
for pid in $(pgrep -f "python3 -m http.server ${PORT}" || true); do
  cwd="$(readlink -f "/proc/${pid}/cwd" 2>/dev/null || true)"
  cmd="$(tr '\0' ' ' < "/proc/${pid}/cmdline" 2>/dev/null || true)"

  if [[ "$cwd" == "$ROOT" && "$cmd" == *"--directory _site"* ]]; then
    echo "[preview] Stopping old preview process ${pid}."
    kill "$pid" 2>/dev/null || true
  fi
done

sleep 0.3

if ss -ltn "( sport = :${PORT} )" | grep -q ":${PORT}"; then
  echo "[preview] Port ${PORT} is still occupied by another process." >&2
  echo "[preview] Run this to inspect it: ss -ltnp | grep ':${PORT}'" >&2
  exit 1
fi

echo "[preview] Serving http://127.0.0.1:${PORT}/ from _site"
python3 -m http.server "$PORT" --bind 0.0.0.0 --directory _site
