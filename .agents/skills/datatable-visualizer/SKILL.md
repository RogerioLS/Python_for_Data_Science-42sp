---
name: datatable-visualizer
description: use for python 2 datatable exercises: csv loading, pandas manipulation, gapminder life expectancy/population plots, labels, titles, and data cleaning.
---

# DataTable Visualizer

## Mission

Implement Python 2 DataTable exercises with correct loading, plotting, and error behavior.

## Checklist

- `load(path)` prints dataset dimensions and returns the dataset.
- Bad path or bad format returns `None` when required.
- Charts include title and axis labels.
- Country selection follows campus/user context unless subject says otherwise.
- Convert population suffixes explicitly before numeric comparison.
- Do not hardcode local absolute paths.

## Review traps

- Extra print noise.
- Missing plot labels.
- Assuming CSV columns without checking.
- Using data from the wrong country because France was in the example.

