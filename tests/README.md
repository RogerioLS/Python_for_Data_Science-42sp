# 🧪 42 Python Piscine - Test Suite & Automation

This directory contains standalone, automated unit test suites for all Python Piscine modules, designed to assist cadets during peer reviews and self-evaluation.

---

## 🚀 Running Tests via Makefile (Recommended)

From the root directory of the repository, execute:

```bash
# Run all unit tests for all completed modules (Module 00 & Module 01)
make test

# Run unit tests specifically for Module 00 (Starting)
make test-m00

# Run unit tests specifically for Module 01 (Array)
make test-m01

# Run the 42 Norm & Clean Code Auditor (checks docstrings, guards, etc.)
make norm

# Run full audit: syntax compilation + norm checks + unit tests
make audit
```

---

## 🐍 Running Tests directly via Python

If you prefer using Python's standard `unittest` runner directly:

```bash
# Run all tests in the tests/ directory
python3 -m unittest discover -s tests -p "test_*.py"

# Run a specific module test file
python3 -m unittest tests/test_module_00.py
python3 -m unittest tests/test_module_01.py
```

---

## 🛡️ Covered Test Scenarios

- **Type strictness**: Verifies that boolean inputs (e.g. `True`, `False`) do not bypass integer checks.
- **Edge cases**: Dimension mismatches, negative indices, non-positive values, file IO exceptions, missing files.
- **Norm compliance**: Verifies docstrings, `if __name__ == "__main__":` entrypoint guards, and zero global scope pollution.
