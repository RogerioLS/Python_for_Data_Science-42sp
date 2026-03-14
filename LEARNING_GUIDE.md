# Learning Guide

A set of guidelines to get the most out of this repository and the 42 curriculum.

---

## How to Study

1. **Read the exercise README first.**  
   Understand the objective before writing any code.

2. **Attempt the exercise independently.**  
   Spend at least 20–30 minutes trying on your own before looking for hints.

3. **Write notes as you go.**  
   Record observations, errors, and discoveries in `notes.md` while the context is fresh.

4. **Review your solution.**  
   After completing an exercise, re-read your code as if you were someone else. Is it clear?

5. **Iterate.**  
   Can the solution be simplified? Is there a more Pythonic approach?

---

## How to Approach Exercises

- Break the problem into the smallest possible steps.
- Write a function for each step.
- Test each function with a simple example before combining them.
- Use `print()` liberally during development; remove or comment out debug prints before committing.

---

## How to Debug Problems

1. **Read the error message carefully.**  
   Python tracebacks tell you exactly where the error occurred. Start from the bottom.

2. **Reproduce the problem with a minimal example.**  
   Strip away everything unrelated to the bug.

3. **Add print statements or use `pdb`.**  
   ```python
   import pdb; pdb.set_trace()  # drops into interactive debugger
   ```

4. **Search the Python documentation.**  
   [`docs.python.org`](https://docs.python.org/3/) is the primary reference.

5. **Check the notes.**  
   You may have encountered this problem before — check `notes.md`.

---

## How to Review Code

Use these questions as a checklist after finishing an exercise:

- [ ] Does the code do what the README says it should?
- [ ] Are all functions documented with a short docstring?
- [ ] Are variable names descriptive?
- [ ] Is there any duplicated logic that could be extracted into a function?
- [ ] Are there any edge cases the code doesn't handle?
- [ ] Does the code follow PEP 8?
- [ ] Are there any unused imports or variables?

---

## Useful Resources

| Topic | Link |
|-------|------|
| Python Docs | https://docs.python.org/3/ |
| PEP 8 Style Guide | https://peps.python.org/pep-0008/ |
| Real Python Tutorials | https://realpython.com/ |
| Python Tutor (visualizer) | https://pythontutor.com/ |
| 42 Intra | https://intra.42.fr/ |
