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

## Commit emoji hook (per-repository)

This repository includes a small Git hook that prepends an emoji to commit messages
based on the Conventional Commit `type:` prefix (for example `feat:`, `fix:`), or
falls back to the branch name when no prefix is present. The hook lives in
`.git/hooks/prepare-commit-msg` and runs automatically when creating commits.

How it works:
- If your commit message starts with a Conventional Commit type (e.g. `feat:`),
    an emoji is prepended (e.g. `✨ feat: ...`).
- If there is no prefix, the hook looks at the current branch name and selects
    an emoji by the branch prefix (e.g. `fix/*` → 🐛).
- If the message already starts with a recognized emoji, the hook does nothing.

Examples:

```
feat: add progress bar
# becomes
✨ feat: add progress bar

fix(parser): handle edge case
# becomes
🐛 fix(parser): handle edge case
```

If you prefer a different emoji mapping, edit `.git/hooks/prepare-commit-msg`.
If you want this behaviour globally for your account, use a global hooks folder
and set `git config --global core.hooksPath /path/to/hooks` (not required here).

### Installing the hooks from the repository

If you want to enable the emoji hook for this repository, run the helper script from
the project root:

```bash
./scripts/install-hooks.sh
```

This sets the repo's `core.hooksPath` to `.githooks` and ensures the hook is
executable. Alternatively, to enable manually:

```bash
chmod +x .githooks/*
git config core.hooksPath .githooks
```

To undo the repo-level setting:

```bash
git config --unset core.hooksPath
```

Notes:
- The repository includes `.githooks/prepare-commit-msg` so contributors can
    enable hooks without needing global configuration.
- The project also contains a global example in your home folder (optional);
    keep only one active hooks path to avoid confusion.


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
