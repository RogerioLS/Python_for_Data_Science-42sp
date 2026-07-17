# 02 — Python Norm

## Required style

- Python 3.10.
- Explicit imports only.
- No globals.
- No executable global scope except definitions and constants only when unavoidable.
- Prefer short functions.
- Public function signatures must match the subject.
- Required functions/classes/methods must have docstrings.
- Use clear names.
- Avoid magic constants unless the subject implies them.

## Main pattern

```python
def main() -> None:
    """Run local checks for the exercise."""


if __name__ == "__main__":
    main()
```

## Error handling

Catch expected errors near the boundary. Do not hide logic bugs with a black-hole `except`.
