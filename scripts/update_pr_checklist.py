#!/usr/bin/env python3
"""Automatically Check Off PR Description Checklists Upon Successful 42 Audit.

Reads audit_summary.json and updates checkboxes `- [ ]` to `- [x]` in the PR body text.
"""

import json
import os
import urllib.request
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
METRICS_PATH = BASE_DIR / "artifacts" / "audit_summary.json"


def main() -> None:
    event_path = os.getenv("GITHUB_EVENT_PATH")
    token = os.getenv("GH_TOKEN") or os.getenv("GITHUB_TOKEN")
    repo = os.getenv("GITHUB_REPOSITORY")

    if not event_path or not token or not repo:
        print("ℹ️ Skipping PR checklist update: Not running inside PR workflow or missing tokens.")
        return

    if not os.path.exists(event_path):
        return

    with open(event_path, "r", encoding="utf-8") as f:
        event_data = json.load(f)

    if "pull_request" not in event_data:
        return

    pr_number = event_data["pull_request"]["number"]
    body = event_data["pull_request"]["body"] or ""

    if not METRICS_PATH.exists():
        return

    with open(METRICS_PATH, "r", encoding="utf-8") as f:
        metrics = json.load(f)

    if not metrics.get("overall_passed", False):
        print("ℹ️ Audit did not pass completely. Leaving manual checklist items unchecked.")
        return

    # Checklist items to auto-check
    checklist_mappings = [
        "- [ ] Nenhuma variável global declarada no código?",
        "- [ ] Todas as funções possuem docstring (`__doc__`)?",
        "- [ ] Execução protegida por `if __name__ == \"__main__\":`?",
        "- [ ] Exceções tratadas sem crash brusco?",
        "- [ ] Rodou `make compile` localmente com 0 erros de sintaxe?",
        "- [ ] Rodou `make norm` e zerou erros do auditor?",
        "- [ ] Rodou `make test` e validou a suite de testes?",
    ]

    new_body = body
    checked_count = 0
    for target in checklist_mappings:
        replacement = target.replace("- [ ]", "- [x]")
        if target in new_body:
            new_body = new_body.replace(target, replacement)
            checked_count += 1

    if new_body == body:
        print("ℹ️ PR checklist body is already up to date.")
        return

    url = f"https://api.github.com/repos/{repo}/pulls/{pr_number}"
    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github+json",
        "User-Agent": "42-Python-Piscine-Checklist-Updater",
    }
    data = json.dumps({"body": new_body}).encode("utf-8")

    req = urllib.request.Request(url, data=data, headers=headers, method="PATCH")
    try:
        with urllib.request.urlopen(req) as resp:
            if resp.status == 200:
                print(f"✅ PR #{pr_number} checklist updated successfully ({checked_count} items checked [x]).")
            else:
                print(f"⚠️ Failed to update PR checklist: HTTP {resp.status}")
    except Exception as e:
        print(f"⚠️ Error updating PR checklist via API: {e}")


if __name__ == "__main__":
    main()
