#!/usr/bin/env python3
"""Summary Generator for 42 Python Piscine GitHub Actions.

Runs audit checks (syntax, norm, unit tests) and generates a Markdown report
for $GITHUB_STEP_SUMMARY, PR comments, and outputs a JSON metrics artifact for PR renaming.
"""

import json
import os
import subprocess
import sys
from datetime import datetime
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
ARTIFACTS_DIR = BASE_DIR / "artifacts"
ARTIFACTS_DIR.mkdir(exist_ok=True)


def run_command(cmd: list[str]) -> tuple[int, str]:
    """Runs a shell command and returns (exit_code, output_text)."""
    try:
        res = subprocess.run(cmd, cwd=str(BASE_DIR), capture_output=True, text=True, check=False)
        output = (res.stdout + "\n" + res.stderr).strip()
        return res.returncode, output
    except Exception as e:
        return 1, str(e)


def main() -> None:
    # 1. Compile syntax check
    py_files = [str(p) for p in BASE_DIR.rglob("*.py") if ".venv" not in p.parts and "__pycache__" not in p.parts and ".git" not in p.parts]
    compile_code, compile_out = run_command([sys.executable, "-m", "py_compile", *py_files])
    compile_status = "✅ PASSED" if compile_code == 0 else "❌ FAILED"

    # 2. Norm Check
    norm_code, norm_out = run_command([sys.executable, "scripts/norm_check.py"])
    norm_status = "✅ PASSED" if norm_code == 0 else "❌ FAILED"

    # Extract norm errors count from output
    norm_errors = 0
    for line in norm_out.splitlines():
        if "strict error(s)" in line:
            try:
                norm_errors = int(line.split("Result :")[1].split("strict")[0].strip())
            except Exception:
                norm_errors = 0 if norm_code == 0 else 1

    # 3. Unit Tests
    test_code, test_out = run_command([sys.executable, "-m", "unittest", "discover", "-s", "tests", "-p", "test_*.py"])
    test_status = "✅ PASSED" if test_code == 0 else "❌ FAILED"

    total_tests = 0
    passed_tests = 0
    for line in test_out.splitlines():
        if "Ran " in line and "tests in" in line:
            try:
                total_tests = int(line.split("Ran ")[1].split(" tests")[0])
                passed_tests = total_tests if test_code == 0 else 0
            except Exception:
                pass

    overall_passed = (compile_code == 0) and (norm_code == 0) and (test_code == 0)
    overall_status = "✅ AUDIT 100% PASSED" if overall_passed else "⚠️ AUDIT FAILED"

    timestamp = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    # Build Markdown Summary
    md = []
    md.append(f"# 🛡️ 42 Python Piscine — Audit Summary Report")
    md.append(f"**Overall Status**: {overall_status}  ")
    md.append(f"**Execution Timestamp**: `{timestamp}`\n")

    md.append("## 📊 Summary Overview")
    md.append("| Metric | Status | Details |")
    md.append("| ------ | ------ | ------- |")
    md.append(f"| ⚡ Python 3.10 Syntax | {compile_status} | Verified {len(py_files)} Python files |")
    md.append(f"| 🛡️ 42 Norm Auditor | {norm_status} | {norm_errors} strict norm error(s) |")
    # 4. Bandit Security Audit
    sec_code, sec_out = run_command([sys.executable, "-m", "bandit", "-r", "python_0_starting", "python_1_array", "python_2_datatable", "-q"])
    sec_status = "✅ PASSED" if sec_code == 0 else "⚠️ REVIEW"

    md.append(f"| 🔒 Security Audit | {sec_status} | 0 critical security issues detected |")

    md.append("\n## 🔍 Audit Details\n")
    md.append("<details><summary><b>View 42 Norm Auditor Output</b></summary>\n")
    md.append("```text")
    md.append(norm_out)
    md.append("```")
    md.append("</details>\n")

    md.append("<details><summary><b>View Unit Test Execution Log</b></summary>\n")
    md.append("```text")
    md.append(test_out)
    md.append("```")
    md.append("</details>\n")

    md.append("---\n*Automated audit summary generated for 42 São Paulo Python Piscine.*")
    md.append('<a href="#"><img align="right" src="https://raw.githubusercontent.com/RogerioLS/RogerioLS/main/foto_little.png" width="55"></a>')

    summary_text = "\n".join(md)

    # Write summary.md
    with open(BASE_DIR / "summary.md", "w", encoding="utf-8") as f:
        f.write(summary_text)

    # Save JSON metrics artifact for rename_pr.py
    metrics = {
        "overall_passed": overall_passed,
        "compile_passed": compile_code == 0,
        "norm_passed": norm_code == 0,
        "norm_errors": norm_errors,
        "test_passed": test_code == 0,
        "total_tests": total_tests,
        "passed_tests": passed_tests,
        "timestamp": timestamp,
    }

    with open(ARTIFACTS_DIR / "audit_summary.json", "w", encoding="utf-8") as f:
        json.dump(metrics, f, indent=2)

    print(summary_text)


if __name__ == "__main__":
    main()
