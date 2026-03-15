#!/usr/bin/env bash
set -euo pipefail
# Installs repository hooks by setting local git config to use .githooks

REPO_ROOT=$(git rev-parse --show-toplevel 2>/dev/null || pwd)
HOOKS_DIR="$REPO_ROOT/.githooks"

if [[ ! -d "$HOOKS_DIR" ]]; then
  echo "Creating $HOOKS_DIR"
  mkdir -p "$HOOKS_DIR"
fi

# Ensure the hook file is present and executable
if [[ -f "$REPO_ROOT/.githooks/prepare-commit-msg" ]]; then
  chmod +x "$REPO_ROOT/.githooks/prepare-commit-msg"
else
  echo "No prepare-commit-msg found in $REPO_ROOT/.githooks"
  exit 1
fi

# Set repository-level hooks path
git config core.hooksPath .githooks

echo "Installed hooks to .githooks and set 'core.hooksPath' for this repository."
echo "To undo: git config --unset core.hooksPath"
