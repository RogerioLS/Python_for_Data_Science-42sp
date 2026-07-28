# Copilot Instructions — 42 Python Piscine for Data Science

This repository contains solutions, tests, automation scripts, and peer defense documentation for the **42 Python Piscine for Data Science** at École 42 São Paulo.

The active module scope includes:

- **Python 0 — Starting:** Fundamentals, data structures, strings, filters, tqdm generators, packaging.
- **Python 1 — Array:** 2D slicing, NumPy vectorization, image loading, zooming, manual transposition, color filters.
- **Python 2 — DataTable:** Pandas DataFrames, CSV parsing, data visualization, country population plots.
- **Python 3 — OOP:** Abstract classes, inheritance, diamond problem, vector calculations.
- **Python 4 — Data Oriented Design:** Statistics, closures, decorators, dataclasses.

---

## 42 Principles & Standards

Always favor:

- Minimal, clean, and correct implementations matching the subject PDF.
- Strict type checking (`type(x) not in (int, float)` to reject boolean subclasses).
- Explicit imports (e.g. `import numpy as np`, never `from module import *`).
- Function docstrings (`__doc__`) on every function, class, and method.
- Main entrypoint guards (`if __name__ == "__main__":`).
- Graceful exception handling (programs must not crash abruptly).
- Vectorized operations over manual `for` loops when using NumPy/Pandas.
- Automation via the central `Makefile` (`make audit`, `make norm`, `make test`).

Avoid:

- Global variables and global executable scope.
- Overengineering or introducing unrequested frameworks/abstractions.
- Swallowing errors silently with empty returns.
- Hardcoded local absolute paths.
- Changing expected console output wording.

---

## Exercise Directory Structure

Each exercise folder follows a clean 42 delivery layout:

```text
exNN/
├── main.py        # Exercise implementation or test runner
├── <turn-in>.py   # Required files specified by the subject
```

Centralized module documentation and defense guides are located at:

```text
python_X_module/
├── README.md              # Centralized module specs & learning notes
└── defesa/
    ├── index.html         # Interactive HTML defense guide
    └── defesa_print.html  # Print-friendly Portuguese defense cheat sheet
```

---

## Definition of Done

An exercise is complete only when:

1. Code passes syntax compilation (`make compile`).
2. Code passes 42 Norm & Clean Code Auditor (`make norm`).
3. Automated unit tests pass (`make test`).
4. Output text and shapes match the subject PDF expected output.
5. Peer defense notes are updated in `defesa/index.html` and `defesa_print.html`.
