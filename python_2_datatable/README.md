# Module 02 — DataTable (Pandas & Data Visualization)

Centralized reference guide and learning documentation for Module 02 of the 42 Python Piscine.

---

## Navigation & Defense Guides

- 📑 **[Interactive Defense Dashboard (HTML)](defesa/index.html)**
- 🖨️ **[Print-Friendly Portuguese Defense Cheat Sheet (HTML)](defesa/defesa_print.html)**

---

## Module Overview

| Exercise | Name | Function / Script | Description |
| -------- | ---- | ----------------- | ----------- |
| **ex00** | Load my DB | `load(path: str) -> Optional[pd.DataFrame]` | Loads a CSV file using Pandas, displays dimensions, handles errors gracefully. |
| **ex01** | Afficher Life Expectancy | `aff_life.py` | Plots life expectancy over time for campus country (Brazil). |
| **ex02** | Afficher Population | `aff_pop.py` | Plots population comparison between two countries over time. |
| **ex03** | Projection Life Expectancy | `projection_life.py` | Scatter plot of GDP per capita vs. Life Expectancy for the year 1900. |
| **ex04** | Data Visualizer | `load_csv.py` | Module-wide reusable data table helper. |

---

## Detailed Exercise Notes

### Exercise 00 — Load my DB (`ex00`)
- **Objective**: Implement `load(path: str)` using Pandas to load CSV datasets.
- **Key Concepts**:
  - `pd.read_csv(path)` reads comma-separated datasets into a 2D DataFrame.
  - `df.shape` returns a tuple `(rows, columns)` representing matrix dimensions.
  - Exception handling for `FileNotFoundError` and `EmptyDataError`.
