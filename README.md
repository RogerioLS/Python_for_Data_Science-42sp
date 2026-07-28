<div align = center>

# :snake: Python for Data Science | 42 SP

[![Full Piscine Audit](https://github.com/RogerioLS/Python_for_Data_Science-42sp/actions/workflows/audit.yml/badge.svg)](https://github.com/RogerioLS/Python_for_Data_Science-42sp/actions/workflows/audit.yml)
[![Run All Unit Tests](https://github.com/RogerioLS/Python_for_Data_Science-42sp/actions/workflows/test.yml/badge.svg)](https://github.com/RogerioLS/Python_for_Data_Science-42sp/actions/workflows/test.yml)
[![42 Norm Auditor](https://github.com/RogerioLS/Python_for_Data_Science-42sp/actions/workflows/norm.yml/badge.svg)](https://github.com/RogerioLS/Python_for_Data_Science-42sp/actions/workflows/norm.yml)
[![Test Module 00](https://github.com/RogerioLS/Python_for_Data_Science-42sp/actions/workflows/test-m00.yml/badge.svg)](https://github.com/RogerioLS/Python_for_Data_Science-42sp/actions/workflows/test-m00.yml)
[![Test Module 01](https://github.com/RogerioLS/Python_for_Data_Science-42sp/actions/workflows/test-m01.yml/badge.svg)](https://github.com/RogerioLS/Python_for_Data_Science-42sp/actions/workflows/test-m01.yml)
[![Syntax Compilation Check](https://github.com/RogerioLS/Python_for_Data_Science-42sp/actions/workflows/compile.yml/badge.svg)](https://github.com/RogerioLS/Python_for_Data_Science-42sp/actions/workflows/compile.yml)
![Static Badge](https://custom-icon-badges.demolab.com/badge/PYTHON--PISCINE--42-blue?logo=repo)
![42 São Paulo](https://custom-icon-badges.demolab.com/badge/42-SP-1E2952)
![License](https://custom-icon-badges.demolab.com/github/license/RogerioLS/Python_for_Data_Science-42sp?logo=law&color=dark-green)
![Code size in bytes](https://custom-icon-badges.demolab.com/github/languages/code-size/RogerioLS/Python_for_Data_Science-42sp?logo=file-code&color=dark-green)
![Top language](https://custom-icon-badges.demolab.com/github/languages/top/RogerioLS/Python_for_Data_Science-42sp?color=dark-green)
![Last commit](https://custom-icon-badges.demolab.com/github/last-commit/RogerioLS/Python_for_Data_Science-42sp?logo=history&color=dark-green)
![Repo size](https://custom-icon-badges.demolab.com/github/repo-size/RogerioLS/Python_for_Data_Science-42sp?logo=database)
![Languages](https://custom-icon-badges.demolab.com/github/languages/count/RogerioLS/Python_for_Data_Science-42sp?logo=command-palette&color=red)
</div>

A personal learning repository for the Python for Data Science piscine from École 42 São Paulo.

---

## What Is the Piscine?

The Python for Data Science piscine is an intensive learning program at École 42 that covers Python programming fundamentals and data science concepts through a series of hands-on modules and exercises.

---

## Repository Structure

The repository is organized by module, following the official piscine structure:

```
python_0_starting/      — Python basics and getting started (ex00–ex09)
python_1_array/         — Arrays and NumPy fundamentals (ex00–ex05)
python_2_datatable/     — DataFrames and data manipulation (ex00–ex04)
python_3_oop/           — Object-oriented programming (ex00–ex04)
python_4_dod/           — Data-oriented design (ex00–ex02)
tests/                  — Automated unittest suites for peer evaluation
scripts/                — 42 Norm & Clean Code Auditor scripts
defesa/                 — Interactive & printable peer defense guides
```

---

## How Exercises Are Organized

Each module contains numbered exercise folders and module-level documentation:

| File / Folder | Purpose |
|--------------|---------|
| `main.py` | Exercise implementation or test runner file |
| `python_X_module/README.md` | Centralized module documentation, specifications, and learning notes |
| `python_X_module/defesa/` | Interactive HTML dashboard & printable Portuguese peer defense guide |
| `tests/` | Automated unit test suite run via `make test` or `unittest` |

---

## How to Run Python Scripts & Automation

```bash
# Clone the repository
git clone https://github.com/RogerioLS/Python_for_Data_Science-42sp.git
cd Python_for_Data_Science-42sp

# (Optional) Create and activate a virtual environment
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt  # Or install numpy pillow matplotlib

# Execute an exercise directly
python python_1_array/ex00/main.py

# Run the 42 Command Center via Makefile
make help       # Display interactive menu
make audit      # Run full audit (compile + norm check + unit tests)
make test       # Run unit test suites
make norm       # Run 42 Norm & Clean Code Auditor
```

---

## Modules Overview

| Module | Topic | Exercises | Status |
|--------|-------|-----------|--------|
| [Python 0 — Starting](python_0_starting/) | Python basics | ex00–ex09 | :white_check_mark: Completed |
| [Python 1 — Array](python_1_array/) | Arrays and NumPy | ex00–ex05 | :white_check_mark: Completed |
| Python 2 — DataTable | DataFrames & Plots | ex00–ex04 | :hourglass: Next |
| Python 3 — OOP | Object-Oriented Programming | ex00–ex04 | :hourglass: Upcoming |
| Python 4 — DoD | Data-Oriented Design | ex00–ex02 | :hourglass: Upcoming |

---

## References & Resources

- [42 São Paulo](https://www.42sp.org.br/)
- [Python 3.10 Documentation](https://docs.python.org/3.10/)
- [NumPy Documentation](https://numpy.org/doc/)
