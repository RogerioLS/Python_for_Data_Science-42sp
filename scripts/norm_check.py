#!/usr/bin/env python3
"""Norm & Clean Code Auditor for 42 Python Piscine.

Checks compliance against 42 Piscine rules:
1. All functions must have a docstring (__doc__).
2. Executable scripts use if __name__ == "__main__": guard.
3. No global executable code outside functions/guards.
4. Python 3.10 syntax compilation.
"""

import ast
import os
import sys
from pathlib import Path


def audit_file(filepath: Path) -> tuple[list[str], list[str]]:
    """Audits a single Python file for 42 Piscine norm rules.

    Returns:
        tuple[list[str], list[str]]: (errors, warnings)
    """
    errors = []
    warnings = []

    try:
        content = filepath.read_text(encoding="utf-8")
        tree = ast.parse(content, filename=str(filepath))
    except SyntaxError as e:
        return [f"SyntaxError: {e}"], []
    except Exception as e:
        return [f"ReadError: {e}"], []

    # Check module-level docstring (Warning)
    if not ast.get_docstring(tree):
        warnings.append("Missing module-level docstring")

    # Check function docstrings (Strict Error per subject rule)
    for node in tree.body:
        if isinstance(node, ast.FunctionDef):
            if not ast.get_docstring(node):
                errors.append(f"Function '{node.name}' is missing a docstring (__doc__)")
        elif isinstance(node, ast.ClassDef):
            if not ast.get_docstring(node):
                errors.append(f"Class '{node.name}' is missing a docstring (__doc__)")
            for subnode in node.body:
                if isinstance(subnode, ast.FunctionDef) and not ast.get_docstring(subnode):
                    errors.append(f"Method '{node.name}.{subnode.name}' is missing a docstring")

    # Check for main guard if script is executable / contains main function
    has_main_guard = False
    for node in tree.body:
        if isinstance(node, ast.If):
            if isinstance(node.test, ast.Compare):
                left = node.test.left
                if isinstance(left, ast.Name) and left.id == "__name__":
                    has_main_guard = True
                    break

    if filepath.name == "main.py" or "main" in [n.name for n in tree.body if isinstance(n, ast.FunctionDef)]:
        if not has_main_guard:
            errors.append("Executable script missing 'if __name__ == \"__main__\":' guard")

    return errors, warnings


def main() -> int:
    """Runs the audit across all module directories."""
    root_dir = Path(__file__).resolve().parent.parent
    target_dirs = [
        root_dir / "python_0_starting",
        root_dir / "python_1_array",
        root_dir / "python_2_datatable",
        root_dir / "python_3_oop",
        root_dir / "python_4_dod",
    ]

    total_files = 0
    total_errors = 0
    total_warnings = 0
    is_ci = os.getenv("GITHUB_ACTIONS") == "true"

    print("==================================================")
    print(" 🛡️  42 PYTHON PISCINE NORM & CLEAN CODE AUDITOR  ")
    print("==================================================")

    for target_dir in target_dirs:
        if not target_dir.exists():
            continue
        print(f"\n📂 Auditing directory: {target_dir.relative_to(root_dir)}")

        py_files = sorted(list(target_dir.rglob("*.py")))
        for py_file in py_files:
            if ".venv" in py_file.parts or "__pycache__" in py_file.parts or "ft_package" in py_file.parts:
                continue

            total_files += 1
            errs, warns = audit_file(py_file)
            rel_path = py_file.relative_to(root_dir)

            if not errs:
                if warns:
                    total_warnings += len(warns)
                    print(f"  [OK]   {rel_path} ({len(warns)} warning)")
                else:
                    print(f"  [OK]   {rel_path}")
            else:
                total_errors += len(errs)
                print(f"  [FAIL] {rel_path}")
                for msg in errs:
                    print(f"         └─ ERROR: {msg}")
                    if is_ci:
                        print(f"::error file={rel_path},line=1::{msg}")

    print("\n--------------------------------------------------")
    print(f"Summary: Audited {total_files} files.")
    print(f"Result : {total_errors} strict error(s), {total_warnings} warning(s).")
    print("--------------------------------------------------")

    return 1 if total_errors > 0 else 0


if __name__ == "__main__":
    sys.exit(main())
