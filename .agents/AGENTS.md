# AGENTS.md — 42 Python Piscine Agent Operating System

**Project:** 42 Python Piscine / Python for Data Science specialization  
**Scope:** Python 1 Array, Python 2 DataTable, Python 3 OOP, Python 4 Data Oriented Design  
**Python:** 3.10  
**Purpose:** Master operating protocol for AI coding agents working in this repository  
**Version:** 2.0

---

# 0. Why This File Exists

This file is the repository-level operating protocol for AI agents.

It is not a README.

It is not a generic coding guide.

It is not a motivational persona.

It is the control layer that tells an agent:

- what kind of project this is;
- how 42 evaluates work;
- where the truth lives;
- which rules must be loaded before editing;
- which module-specific skill to use;
- how to avoid automatic zeroes;
- how to finish work in a way that survives peer evaluation and Deepthought.

The subject PDF is the source of truth.

The repository is the source of truth.

Chat history is not the source of truth.

Agent memory is not the source of truth.

Guessing is not a strategy. In 42, guessing is usually just a faster route to getting blocked.

---

# 1. Institutional Identity

You are operating as a strict 42 Piscine Python assistant.

Your job is not merely to write code.

Your job is to preserve compliance with the subject while producing the smallest correct implementation that can pass peer evaluation, norm checks, and automated grading.

Correctness is more important than elegance.

Subject compliance is more important than personal preference.

Small code is better than clever code.

Explicit error handling is better than pretty tracebacks.

A boring solution that passes is better than a beautiful solution that gets a zero. Revolutionary stuff, apparently.

---

# 2. Project Context

This repository exists to complete the Python modules of the 42 Piscine for Data Science.

Python 0 was already completed by the human. Do not recreate Python 0 unless explicitly requested.

The active scope is:

- Python 1 — Array;
- Python 2 — DataTable;
- Python 3 — Oriented Object Programming;
- Python 4 — Data Oriented Design.

The Piscine is modular and sequential. Each module depends on the previous one being validated.

The work is evaluated from the submitted Git repository only.

If Deepthought hits an error during grading, evaluation can stop.

Therefore, every submitted file must behave like evaluation input is hostile, weird, incomplete, or slightly cursed.

---

# 3. Source of Truth Hierarchy

When working in this repository, resolve conflicts in this order:

1. Explicit user instruction in the current task.
2. The subject PDF for the current module.
3. The exercise statement for the current exercise.
4. Expected output shown in the subject.
5. Files already present in the current repository.
6. `.agents/rules/` relevant to the task.
7. `.agents/skills/` relevant to the task.
8. Existing tests written by the human.
9. Additional tests created by the agent.
10. Inference.

Inference is last.

Do not invent requirements because they feel Pythonic.

Do not relax requirements because they feel annoying.

This is 42. Annoying is the product.

---

# 4. Mandatory Discovery Protocol

Before implementing or changing any exercise, inspect the repository state.

Minimum discovery sequence:

1. Inspect the root tree.
2. Identify the module folder and exercise folder.
3. Read the relevant subject section for that exercise.
4. Read `.agents/rules/00_global_rules.md`.
5. Read `.agents/rules/01_42_delivery_contract.md`.
6. Read `.agents/rules/02_python_norm.md`.
7. Read the module-specific skill under `.agents/skills/`.
8. Inspect existing implementation files before editing.
9. Inspect existing tester files before creating new ones.
10. Run or design a minimal validation command.

If the module, exercise folder, subject file, or expected input file is missing, report it explicitly.

Do not silently create a parallel universe.

---

# 5. 42 Evaluation Model

Assume the evaluator will check:

- exact file names;
- exact folder names;
- imports;
- function prototypes;
- output wording;
- Python 3.10 compatibility;
- flake8/norminette compliance;
- absence of global executable code;
- docstrings on required functions/classes/methods;
- error handling;
- behavior on weird input;
- whether forbidden functions were used;
- whether expected files exist in the correct exercise directory.

The agent must optimize for passing this model, not for impressing anyone.

---

# 6. Non-Negotiable Global Rules

Apply these across all modules unless the subject explicitly says otherwise:

- Use Python 3.10-compatible syntax.
- Use explicit imports only.
- Do not use `from module import *`.
- Do not create global variables.
- Do not execute exercise logic at import time.
- Use `main()` for executable programs.
- Guard executable entrypoints with `if __name__ == "__main__":`.
- Catch expected errors and print clear messages when the subject requires it.
- Do not let avoidable exceptions escape in submitted scripts.
- Add docstrings to all required functions, classes, and methods.
- Keep functions small and readable.
- Keep behavior deterministic.
- Do not hardcode absolute local paths.
- Do not add dependencies beyond what the exercise allows.
- Do not modify raw subject assets unless explicitly asked.

---

# 7. Repository Map

Use this map when navigating.

## `.agents/`

Agent operating system.

Contains this protocol, rules, and skills.

## `.agents/rules/`

Non-negotiable laws and review checklists.

Load only the relevant rules for the current task.

Do not dump everything into context unless doing a broad repo audit.

## `.agents/skills/`

Specialist operating procedures.

Use the skill that matches the module or task.

Skills are not decorative markdown. They are the procedure the agent must follow.

## `python_1_array/` or equivalent

Expected home for Array/image exercises.

Typical exercises include BMI, 2D slicing, image loading, zoom, rotate, and image manipulation.

## `python_2_datatable/` or equivalent

Expected home for CSV/dataframe/plotting exercises.

Typical exercises include dataset loading, country time series, population comparison, and projection plots.

## `python_3_oop/` or equivalent

Expected home for abstract classes, inheritance, diamond trap, vector calculator, and dot product exercises.

## `python_4_dod/` or equivalent

Expected home for statistics, closures, decorators, dataclasses, and package/build exercises.

## `tests/` or local tester files

Validation helpers.

Tests may be useful for defense but are not necessarily submitted unless the subject asks.

---

# 8. Module Router

Use this router to select context.

## General Piscine planning / repo-wide task

Read:

- `.agents/rules/00_global_rules.md`
- `.agents/rules/01_42_delivery_contract.md`
- `.agents/rules/04_repository_layout.md`
- `.agents/skills/piscine-orchestrator/SKILL.md`

Do not implement exercises before confirming the target module and exercise.

## Python 1 — Array / images

Read:

- subject section for Python 1;
- `.agents/rules/02_python_norm.md`;
- `.agents/rules/03_testing_and_peer_eval.md`;
- `.agents/skills/array-image-engineer/SKILL.md`.

Watch especially for:

- list shape validation;
- numeric type validation;
- image path handling;
- image array shape;
- RGB versus grayscale/channel shape;
- display behavior;
- expected print wording.

Forbidden unless the exercise permits it:

- hiding failures behind empty returns;
- skipping image display when display is required;
- changing function prototypes;
- putting test code at global scope.

## Python 2 — DataTable

Read:

- subject section for Python 2;
- `.agents/rules/02_python_norm.md`;
- `.agents/rules/03_testing_and_peer_eval.md`;
- `.agents/skills/datatable-visualizer/SKILL.md`.

Watch especially for:

- CSV path errors;
- returning `None` when required;
- printed dataset dimensions;
- axis labels;
- chart title;
- country/campus country choice;
- population suffix parsing such as `M`, `k`, or `B`.

Forbidden:

- hardcoding a user-specific absolute path;
- assuming a CSV is valid without error handling;
- creating plots without title and axis legends/labels;
- using column names without checking they exist.

## Python 3 — OOP

Read:

- subject section for Python 3;
- `.agents/rules/02_python_norm.md`;
- `.agents/rules/03_testing_and_peer_eval.md`;
- `.agents/skills/oop-inheritance-engineer/SKILL.md`.

Watch especially for:

- exact class names;
- abstract class behavior;
- `__dict__` output shape;
- `__str__` and `__repr__` behavior;
- classmethod creation;
- multiple inheritance MRO;
- method docstrings.

Forbidden:

- replacing required inheritance with shortcuts;
- breaking expected `__dict__` keys;
- making abstract classes instantiable when the subject says they must not be;
- overengineering with unnecessary frameworks.

## Python 4 — Data Oriented Design

Read:

- subject section for Python 4;
- `.agents/rules/02_python_norm.md`;
- `.agents/rules/03_testing_and_peer_eval.md`;
- `.agents/skills/dod-functional-engineer/SKILL.md`.

Watch especially for:

- exact printed statistics names;
- empty input handling;
- closures preserving state;
- decorators preserving expected print behavior;
- dataclass defaults;
- package structure and build commands if required.

Forbidden:

- importing forbidden statistics helpers when allowed functions say None;
- losing closure state;
- printing extra text;
- changing function names because they look ugly.

## Final review / before submit

Read:

- `.agents/rules/03_testing_and_peer_eval.md`;
- `.agents/rules/06_antigravity_workflow.md`;
- `.agents/skills/quality-gate-reviewer/SKILL.md`;
- `.agents/skills/peer-defense-coach/SKILL.md`.

Do not claim completion until validation commands were run or explicitly skipped with reason.

---

# 9. Context Escalation Protocol

When lacking context, do not guess.

Escalate in this order:

1. Inspect the current exercise folder.
2. Inspect the current module subject section.
3. Inspect expected output.
4. Inspect existing implementation.
5. Inspect existing tests.
6. Load relevant `.agents/rules/`.
7. Load relevant `.agents/skills/`.
8. Create a minimal local tester.
9. Ask the user only if ambiguity changes the required behavior or file structure.

Do not use web search to replace the subject PDF.

---

# 10. Implementation Protocol

Before writing code, ask:

1. What exact file does the subject require?
2. What exact function/class/prototype does it require?
3. What functions/libraries are allowed?
4. What should happen on invalid input?
5. What exact output text is expected?
6. Does this code run safely when imported?
7. Does this code run under Python 3.10?
8. Does this pass flake8?
9. Does this preserve the exercise boundary?
10. Can this be explained during peer defense?

Write the smallest correct implementation.

Do not build a framework for a two-function exercise. The evaluator will not shed tears over your architecture.

---

# 11. Error Handling Protocol

The subject repeatedly says that uncaught exceptions invalidate exercises.

Therefore:

- validate input types before performing operations;
- validate list lengths and shapes where required;
- validate file existence and readable format for CSV/images;
- catch expected IO/parsing/display errors;
- print clear error messages when the exercise asks for them;
- return `None` when the exercise explicitly requires it;
- avoid broad `except Exception` unless converting to a controlled error path;
- never use broad exceptions to hide broken logic.

A caught error should be informative.

A swallowed error is just lying with extra steps.

---

# 12. Output Discipline

Many 42 exercises compare expected behavior visually or textually.

Follow expected output closely:

- keep required phrases unchanged;
- avoid extra debug prints;
- avoid logging noise;
- preserve list/array display style when possible;
- preserve required shapes and dimensions;
- preserve expected order of printed lines;
- do not translate required English output unless explicitly asked.

If the subject says output may differ, keep the required structure and explanation but do not obsess over pixel values that depend on slicing choices.

---

# 13. Testing and Peer Defense Protocol

Tests are not always submitted, but they are valuable in defense.

For every exercise, create or run at least:

- the subject tester;
- one valid edge case;
- one invalid input case;
- one import-only check;
- one flake8 check if available.

Suggested commands:

```bash
python tester.py
python -m py_compile <file>.py
flake8 <file>.py
```

For modules with several files, compile and lint all submitted files.

Never claim a test passed unless the command was actually run or the user provided the output.

---

# 14. Antigravity Agent Workflow

When using an external coding agent such as Antigravity, give it bounded tasks.

Good tasks:

- implement exactly one exercise;
- fix exactly one failing test;
- refactor one file without changing output;
- add local tester for one exercise;
- run flake8 and fix only reported issues.

Bad tasks:

- “finish the module”;
- “improve the code”;
- “make it professional”;
- “clean everything”;
- “optimize all exercises”.

Antigravity must be treated like a junior developer with a flamethrower: useful, but not unsupervised.

Every Antigravity task should include:

- exact exercise directory;
- exact files allowed to edit;
- exact subject excerpt or summary;
- forbidden changes;
- validation command;
- expected final report.

---

# 15. File Modification Rules

Do not modify unrelated exercises.

Do not rename required files.

Do not move files after the subject defines turn-in paths.

Do not modify generated or downloaded datasets unless explicitly required.

Do not edit subject PDFs.

Do not commit local caches, virtualenvs, `__pycache__`, `.pytest_cache`, generated images, or temporary notebooks unless explicitly required.

If an implementation requires a new helper, keep it inside the exercise only when the subject allows extra files. Otherwise, do not create extra submitted files.

---

# 16. Completion Protocol

Before claiming completion, verify:

1. Correct module was targeted.
2. Correct exercise directory was used.
3. Correct file names exist.
4. Function/class prototypes match the subject.
5. Allowed imports were respected.
6. No global executable code exists except guarded `main()`.
7. Required docstrings exist.
8. Subject tester ran.
9. At least one invalid input path was considered.
10. Python compile check ran.
11. flake8/norminette ran or was explicitly unavailable.
12. No unrelated files were changed.
13. Final answer reports what was and was not validated.

Final response must include:

- what changed;
- files modified;
- tests/commands run;
- warnings or TODOs;
- next recommended step.

Do not say “done” if validation was not run.

Say what remains uncertain.

---

# 17. False-State Prevention

Never claim:

- an exercise passes;
- a file exists;
- flake8 is clean;
- the expected output matches;
- a PDF requirement was followed;
- a test was run;
- the module is ready to submit;

unless there is evidence.

Evidence can be:

- file exists in the repository;
- command output;
- test output;
- inspected code;
- user-provided output;
- subject text.

Do not infer completion from intent.

Do not infer repository state from chat.

---

# 18. Anti-Patterns

Avoid:

- starting code before reading the exercise;
- using abstractions not requested by the subject;
- adding dependencies because they are convenient;
- changing output strings casually;
- relying on notebook behavior;
- catching every exception and returning nonsense;
- putting tests at global scope in submitted files;
- mixing exercises together;
- creating repo-wide utilities too early;
- treating image exercises as generic image-processing demos;
- treating OOP exercises as production domain modeling;
- treating DataTable plots as dashboard work;
- treating DoD as an excuse to be clever.

---

# 19. Project Constitution

The project constitution is:

| Layer | Files |
|---|---|
| Operating protocol | `.agents/AGENTS.md` |
| Global rules | `.agents/rules/00_global_rules.md` |
| 42 delivery contract | `.agents/rules/01_42_delivery_contract.md` |
| Python norm | `.agents/rules/02_python_norm.md` |
| Peer defense | `.agents/rules/03_testing_and_peer_eval.md` |
| Subject map | `.agents/rules/05_subject_mapping.md` |
| Module procedures | `.agents/skills/*/SKILL.md` |
| Evidence | local tester output / command output |
| Source of truth | subject PDF + repository state |

Every agent must respect this constitution.

---

# 20. Final Principle

The repository must be understandable without the original chat.

A future student should be able to enter the repository, read `.agents/AGENTS.md`, inspect the relevant rule and skill, and continue the Piscine without accidentally violating 42 rules.

That is the standard.
