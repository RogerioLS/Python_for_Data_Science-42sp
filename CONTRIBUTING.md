# Contributing Guide

This document describes the conventions used in this learning repository.

## Coding Standards

- Follow [PEP 8](https://peps.python.org/pep-0008/) for all Python code.
- Keep functions small and focused — one function, one responsibility.
- Prefer clarity over cleverness.
- Add a short docstring to every function explaining what it does.
- Avoid external dependencies unless they are part of the exercise requirements.

## Commit Message Style

Use the following format:

```
<type>(<scope>): <short description>
```

**Types:**

| Type | When to use |
|------|-------------|
| `feat` | Adding new code or a new exercise |
| `fix` | Correcting a bug or mistake |
| `docs` | Documentation-only changes |
| `refactor` | Restructuring code without changing behavior |
| `test` | Adding or updating test scripts |
| `chore` | Maintenance tasks (renaming files, updating .gitignore, etc.) |

**Examples:**

```
feat(ex03): implement bubble sort exercise
docs(notes): add notes on list comprehensions
fix(ex01): correct off-by-one error in loop
```

## Exercise Structure

Every exercise folder must contain:

```
exNN/
├── main.py      # Implementation
├── README.md    # Exercise description and objectives
└── notes.md     # Personal observations and key learnings
```

### main.py conventions

- Start with a module-level docstring describing the exercise.
- Keep the `main()` function as an entry point.
- Guard execution with `if __name__ == "__main__":`.

```python
"""Exercise NN — Short Title.

Brief description of what this exercise covers.
"""


def main() -> None:
    """Entry point for exercise NN."""
    pass


if __name__ == "__main__":
    main()
```

### README.md conventions

Each exercise README should briefly cover:

1. **Objective** — what you are practicing
2. **Instructions** — what to implement
3. **Example** — sample input/output if applicable

### notes.md conventions

Use this file freely to record:

- What was difficult or surprising
- Key concepts discovered during the exercise
- Ideas for improvement or follow-up exploration
