# Piscine Python for Data Science – Module 00 (Starting)

## Overview

This repository contains the solutions for **Module 00 – Starting** from the **42 Piscine Python for Data Science** training.

The goal of this module is to introduce the fundamental concepts of the Python programming language and basic software engineering practices used throughout the program.

The exercises progressively cover:

- Python data structures
- Functions and typing
- CLI argument handling
- String analysis
- Functional programming concepts
- Generators
- Dictionary usage
- Python package creation

All exercises are implemented using **Python 3.10**, following the constraints and coding standards defined by the subject.

---

# Project Structure

```
.
├── ex00/
│   └── Hello.py
├── ex01/
│   └── format_ft_time.py
├── ex02/
│   └── find_ft_type.py
├── ex03/
│   └── NULL_not_found.py
├── ex04/
│   └── whatis.py
├── ex05/
│   └── building.py
├── ex06/
│   ├── ft_filter.py
│   └── filterstring.py
├── ex07/
│   └── sos.py
├── ex08/
│   └── Loading.py
├── ex09/
│   ├── ft_package/
│   ├── README.md
│   ├── LICENSE
│   └── pyproject.toml
└── README.md
```

---

# General Rules

The following rules apply to all exercises:

- Python **3.10** must be used.
- **No global variables** are allowed.
- Imports must be **explicit**.

Example:

```python
import numpy as np
```

Forbidden:

```python
from numpy import *
```

- Programs must **not crash** (no uncaught exceptions).
- Code must follow **flake8** standards.

Install flake8:

```bash
pip install flake8
```

Run lint check:

```bash
flake8 .
```

---

# Execution

Each exercise can be executed directly using Python.

Example:

```bash
python ex04/whatis.py 14
```

Example output:

```
I'm Even.
```

---

# Exercises

## ex00 – First Python Script

Manipulation of Python data structures:

- list
- tuple
- set
- dictionary

Goal: modify values in each structure to produce specific outputs.

<details>

<summary><b>📘 Exercise 00 – Learning Notes</b></summary>

## Exercise 00 – Key Concepts Learned

This exercise focuses on understanding how different Python data structures behave when modifying their contents. The goal is not only to change values, but to understand **mutability, indexing, and internal structure behavior**.

### 1. Lists

Lists are **mutable and ordered** collections.

Internally, a list behaves like a **dynamic array of references to objects**. Each position in the list stores a reference to an object rather than the object itself.

Example:

```python
ft_list = ["Hello", "tata!"]
```

Because lists are mutable, elements can be modified directly using their index:

```python
ft_list[1] = "World!"
```

This operation replaces the reference stored at index `1` with a new object.

Key properties:

- ordered
- mutable
- indexed access
- dynamic size

---

### 2. Tuples

Tuples are **ordered but immutable** collections.

Once created, their elements **cannot be modified, added, or removed**. This immutability allows tuples to be **hashable**, which means they can be used as dictionary keys or stored in sets.

Example:

```python
ft_tuple = ("Hello", "toto!")
```

Since tuples cannot be modified directly, changing a value requires creating a **new tuple**:

```python
ft_tuple = ("Hello", "Brazil!")
```

Key properties:

- ordered
- immutable
- hashable (if elements are hashable)

---

### 3. Sets

Sets are **unordered collections of unique elements**.

Internally, they are implemented using a **hash table**, meaning elements are stored based on their hash values rather than their insertion order.

Example:

```python
ft_set = {"Hello", "tutu!"}
```

Because sets are unordered, they **do not support indexing**.

Elements are modified using value-based operations:

```python
ft_set.remove("tutu!")
ft_set.add("Sao Paulo!")
```

Due to the hash-based implementation, the printed order of elements may change between executions.

Key properties:

- unordered
- mutable
- unique elements
- no indexing

---

### 4. Dictionaries

Dictionaries are **key–value mappings**, also implemented using a **hash table**.

Each key is hashed to locate the corresponding value efficiently.

Example:

```python
ft_dict = {"Hello": "titi!"}
```

To update a value, we reference the key directly:

```python
ft_dict["Hello"] = "42SaoPaulo!"
```

Since Python 3.7, dictionaries **preserve insertion order**, although lookup is still performed using hashing.

Key properties:

- key–value structure
- mutable
- fast lookups via hashing
- insertion order preserved (Python ≥ 3.7)

---

### Summary

| Structure | Ordered | Mutable | Indexed | Based on Hash |
|-----------|--------|--------|--------|---------------|
| List      | Yes    | Yes    | Yes    | No |
| Tuple     | Yes    | No     | Yes    | No |
| Set       | No     | Yes    | No     | Yes |
| Dict      | Yes*   | Yes    | No     | Yes |

\* Dictionaries preserve insertion order starting from Python 3.7.

This exercise demonstrates how each data structure requires **different modification strategies**, reinforcing the importance of understanding mutability and internal data structure behavior in Python.

</details>

---

## ex01 – First Use of Package

Use Python libraries (`time`, `datetime`) to format and display:

- seconds since the Unix epoch
- formatted date output

<details>
<summary><b>📘 Exercise 01 – Learning Notes</b></summary>

## Exercise 01 – Key Concepts Learned

This exercise introduces how Python interacts with system time and how numeric and date values can be formatted for human-readable output.

The goal is not only to obtain the current timestamp, but also to understand **Unix time, numeric formatting, scientific notation, and date formatting in Python**.

---

### 1. Unix Timestamp

Python can retrieve the current time as a **Unix timestamp**, which represents the number of seconds that have elapsed since:

```
January 1, 1970 (00:00:00 UTC)
```

This reference point is known as the **Unix Epoch**.

Example in Python:

```python
import time

timestamp = time.time()
```

This returns a floating-point number such as:

```
1713648000.1234
```

The decimal part represents **fractions of a second**.

---

### 2. Numeric Formatting

Python allows numbers to be formatted using **format specifiers** inside f-strings.

Example:

```python
f"{timestamp:,.4f}"
```

Explanation of the format:

| Specifier | Meaning |
|----------|--------|
| `,` | Adds thousands separators |
| `.4f` | Keeps 4 decimal places |
| `f` | Fixed-point notation |

Example output:

```
1,713,648,000.1234
```

This improves readability for large numbers.

---

### 3. Scientific Notation

Scientific notation expresses large numbers in the form:

```
a × 10ⁿ
```

Python formats numbers this way using the `e` format specifier.

Example:

```python
f"{timestamp:.2e}"
```

Explanation:

| Specifier | Meaning |
|----------|--------|
| `.2` | Two digits after the decimal |
| `e` | Scientific notation |

Example output:

```
1.71e+09
```

This format is widely used in **scientific computing and data science**.

---

### 4. Date Formatting with `strftime`

Python's `time` module can convert timestamps into human-readable date formats.

Example:

```python
time.strftime("%b %d %Y", time.localtime())
```

Format codes used:

| Code | Meaning | Example |
|-----|--------|--------|
| `%b` | Month abbreviation | Oct |
| `%d` | Day of month | 21 |
| `%Y` | Full year | 2022 |

Example result:

```
Oct 21 2022
```

---

### Summary

| Concept | Purpose |
|-------|--------|
| `time.time()` | Retrieve Unix timestamp |
| Numeric formatting (`:,.4f`) | Improve readability of large numbers |
| Scientific notation (`:.2e`) | Represent large numbers compactly |
| `strftime()` | Format dates for human-readable output |

This exercise demonstrates how Python can **retrieve system time and present it in different numeric and textual formats**, which is a common requirement in logging systems, data processing, and scientific applications.

</details>

---

## ex02 – First Function

Implement a function that:

- detects object types
- prints the type
- returns the integer `42`.

---

## ex03 – NULL Not Found

Create a function that detects different **null-like values** in Python:

- `None`
- `NaN`
- `0`
- `""`
- `False`

The function must return:

```
0 → success
1 → error
```

---

## ex04 – Even or Odd

Create a CLI program that:

- accepts a number as argument
- determines if it is **Even or Odd**

Errors must be handled using `AssertionError`.

---

## ex05 – Text Analyzer

Standalone program that analyzes a string and counts:

- uppercase letters
- lowercase letters
- punctuation
- spaces
- digits

---

## ex06 – Custom Filter

Reimplement Python's built-in `filter()` function.

Constraints:

- `filter()` cannot be used
- must use **list comprehension**

A program is also created to filter words by length.

---

## ex07 – Morse Code Encoder

Create a program that:

- converts alphanumeric text into **Morse code**
- uses a **dictionary mapping**

Rules:

- characters separated by spaces
- word spaces represented by `/`

---

## ex08 – Progress Bar (tqdm clone)

Implement a custom progress bar similar to **tqdm** using:

- `yield`
- iteration tracking
- terminal width handling (`os.get_terminal_size`)

---

## ex09 – Python Package Creation

Create and distribute a simple Python package:

```
ft_package
```

The package must be installable using:

```bash
pip install ./dist/ft_package-0.0.1.tar.gz
```

Example usage:

```python
from ft_package import count_in_list

print(count_in_list(["toto", "tata", "toto"], "toto"))
```

Expected output:

```
2
```

---

# Learning Objectives

This module focuses on developing the following skills:

- Python syntax fundamentals
- data structure manipulation
- functional programming
- CLI programs
- error handling
- generators
- Python packaging

---

# Author

Student at **42 School – Piscine Python for Data Science**